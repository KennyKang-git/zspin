**ZS-A23**

**Dimension-Weighted Mediator Semigroups and Observer-Algebra Weights in a Finite-Register de Sitter Model**

*An exact three-sector Markov–operator correspondence: a Mediator-Graph algebra-generation theorem, a dimension-weighted mediator semigroup unifying the trace weights, the inter-sector rates and the relaxation spectrum, a modular detailed-balance theorem, and the late-time vacuum-scale reduction in Z-Spin Cosmology*

**Author:** Kenny Kang

**Affiliation:** Z-Spin Cosmology Collaboration

**Theme / Code:** Astrophysics — **ZS-A23 v3.3**

**Date:** March 2026

**Repository:** github.com/KennyKang-git/zspin

**Verification: 26/26 internal consistency checks PASS | Zero Free Parameters.** Built on exact symbolic computation: the Mediator-Graph algebra generation to M₁₁; the dimension-weighted semigroup (stationary (3,2,6)/11, the general characteristic polynomial λ(λ+bκ²)(λ+Dκ²), the spectrum {0, −2A/Q, −A}, both rates as matrix elements); the sector-covariant uniqueness lemma (commutant 1-dimensional); the exact H-theorem; modular detailed balance ln(qᵢⱼ/qⱼᵢ) \= −Δ**K**; the observer size-bias ω \= sizebias(π); and the relaxation-ratio and reverse-rate predictions. The audit is attached (zs\_a23\_v3\_3\_audit.py); the cosmological identifications (offset, embedding, period-2) remain theorem-level arguments, and the NOTE says so. Independent rerun recommended.

Sole geometric inputs: **A** \= 35/437, **Q** \= 11, (Z, X, Y) \= (2, 3, 6), **LOCKED**, with **κ² \= A/Q \= 35/4807** (PROVEN, ZS-A19). Units: reduced Planck mass M̄\_P² \= (8πG)⁻¹. H̄₀/M̄\_P ≈ 6.0×10⁻⁶¹ is a disclosed external normalisation, not derived.

**This is v3.3, the final patched version (twentieth named version).** It applies the five external-review patches to v3.2: (1) Main Theorem 2 is split into a **mathematical** semigroup theorem (PROVEN under edge-isotropy) and a **Z-Spin realization** (DERIVED-CONDITIONAL on the sector-isotropic mediation principle); (2) a **sector-covariant uniqueness lemma** (Schur) shows the dimension-weighted generator is the unique sector-covariant edge-isotropic generator; (3) the rate **units** are fixed by a reference scale Γ₀ (the values 2A/Q, 6A/Q are Γ₀-normalized dimensionless rates); (4) the **H-theorem** is given an exact one-line proof (the Monte-Carlo is demoted to a regression test); (5) the embedding **domain** is corrected to the face algebra A\_face \= ℂ¹²¹. Zero free parameters; (**A**, **Q**, dim Z) \= (35/437, 11, 2\) LOCKED.

**§0. Abstract**

ZS-A23 establishes an exact correspondence between the Z-mediated finite-register operator algebra and a reversible three-sector Markov semigroup, and applies it to reduce ZS-A22's late-time vacuum-scale debts.

**Main Theorem 1 (Mediator-Graph Algebra Generation, PROVEN).** M₃ ⊕ M₂ ⊕ M₆ with nonzero X–Z and Z–Y intertwiners (no X–Y) generates M₁₁(ℂ); unique trace (3, 2, 6)/11.

**Main Theorem 2 (Dimension-Weighted Mediator Semigroup).** **(2a, PROVEN)** Under edge-isotropic microtransition amplitudes, the generator qᵢ→ⱼ \= Γ₀κ²dⱼ on the path X–Z–Y has stationary π \= (3,2,6)/11, characteristic polynomial λ(λ+bκ²)(λ+Dκ²) (general in (a,b,c)), spectrum {0, −2A/Q, −A} \= the ZS-Q7 cubic, and matrix elements 2A/Q, 6A/Q \= the ZS-M43 rates; a GKLS construction gives it with no energy-ladder assumption, and a uniqueness lemma fixes it as the unique sector-covariant edge-isotropic generator. **(2b, DERIVED-CONDITIONAL)** Its Z-Spin realization is conditional on the sector-isotropic mediation principle.

**Main Theorem 3 (Modular Detailed Balance & Observer Size-Bias, PROVEN).** ln(qᵢ→ⱼ/qⱼ→ᵢ) \= −Δ**K**ᵢ→ⱼ; ω \= sizebias(π), hᵢ \= 11dᵢ/49. Corollary: D(r‖π) Lyapunov (exact proof); γ\_fast/γ\_slow \= Q/2 \= 11/2; reverse rates 3A/Q, 2A/Q.

**Main Theorem 4 (Modular-Centralizer Observer Theorem, PROVEN).** ω\_reg's modular centralizer is exactly N \= M₃ ⊕ M₂ ⊕ M₆, σ\_t^ω(Cᵢⱼ) \= (dᵢ/dⱼ)^{it}Cᵢⱼ, e⁻ᶜ \= 121/49, index \= 3 (tight).

**Main Theorem 5 (boundary non-predictivity, PROVEN-with-hypotheses).** One free vacuum-proportional counterterm makes the Brown–York coefficient scheme-dependent.

**The cosmological reductions.** Offset \= A\_dS/4G (CLPW matching), residual \= B3; b-energy DERIVED-CONDITIONAL (carrier \= face algebra, combinatorial-holography prediction); embedding Φ\_face OPEN (needs ZS-F2); period-2 OPEN, sharpened by the two-edge-mediation route. **Net.** The trace weights, the inter-sector rates, the relaxation spectrum, and the modular differences are unified in one dimension-weighted generator, with new exact predictions; the cosmological-constant problem is localized to the embedding, the B3 scale, and the absolute O(1) factor. Zero free parameters; (**A**, **Q**, dim Z) \= (35/437, 11, 2\) LOCKED.

**Epistemic Status Legend**

Table 1\. Epistemic status legend.

| STATUS | DEFINITION |
| ----- | ----- |
| PROVEN | Mathematical theorem; standard mathematics alone, machine-verifiable. |
| PROVEN-with-hypotheses | Theorem under explicitly stated physical hypotheses (named in situ). |
| IMPORTED-PROVEN | Result proved externally, used without re-proof; full citation given. |
| DERIVED | Z-Spin action plus standard physics; zero free parameters. |
| DERIVED-dynamical | DERIVED from an explicit open-system / dynamical mechanism (leading order). |
| DERIVED-CONDITIONAL | DERIVED conditional on listed hypotheses not themselves closed. |
| PREDICTION | A falsifiable consequence stated as such. |
| HYPOTHESIS-strong / weak | Motivated conjecture; documented closure route / failing chain. |
| OBSERVATION / CONSISTENCY | A numerical agreement reported as such, not a derivation. |
| NON-CLAIM | Explicit declaration of what is NOT asserted. |
| OPEN | Recognized gap; an executable closure route is named where one exists. |
| CLOSED-NEGATIVE | A registered gate / sub-route resolved in the negative (a theorem). |
| WITHDRAWN | A prior-version claim retracted as unsupported, with reason. |
| LOCKED | Core constant fixed upstream; immutable downstream. |

**§1. Introduction**

The ZS-A23 program reduces ZS-A22's P0 (action-level positive vacuum source) and B3 (absolute IR scale) debts at their true level. Through nineteen versions it accumulated a set of operator-algebra and dynamical results that were, until now, separate: the sector trace weights (3, 2, 6)/11 (A23.5a), the inter-sector relaxation rates 2**A**/**Q**, 6**A**/**Q** (ZS-M43), the ZS-Q7 relaxation cubic, the modular difference −ln 2 (ZS-F19), and the observer weight (9, 4, 36)/49 (A23.MC).

**v3.2 unified all of these; v3.3 seals the result for external review.** The organizing insight — that every allowed microstate transition carries the same Z-Spin mediation strength κ² \= **A**/**Q**, so the coarse-grained sector rate is qᵢ→ⱼ \= Γ₀κ²dⱼ (one quantum of mediation per available final microstate) — fixes a single dimension-weighted mediator generator whose stationary distribution is the trace weights, whose spectrum is the ZS-Q7 cubic, whose matrix elements are the ZS-M43 rates, whose log-ratios are the ZS-F19 modular differences, and whose operator-space size-bias is the A23.MC weight. The energy-ladder reading of v3.0/v3.1 is removed by a GKLS construction; a uniqueness lemma fixes the generator; and the result is exact and general (the characteristic polynomial factors as λ(λ+bκ²)(λ+Dκ²) for arbitrary sector dimensions), so it is structural, not a numerical coincidence — yielding new exact predictions (the relaxation ratio Q/2, the reverse rates).

§§3–6 give the five main theorems; §7 upgrades the A23.8 retraction to the dimension-weighted-Laplacian theorem and gives a quantum-simulator protocol; §8 carries the cosmological reductions; §§9–12 the cross-version audit, ledger, conclusion, and residuals; Appendices A (Mediator-Graph proof), B (the generator's exact spectrum). The posture is the corpus's honest conditional reduction.

**§2. Locked Inputs and Conventions**

(**A**, **Q**, (Z,X,Y)) \= (35/437, 11, (2,3,6)) **LOCKED**. **κ² \= A/Q \= 35/4807**, 1/κ² \= **Q**/**A** \= 4807/35 (PROVEN, ZS-A19). Units: reduced Planck mass M̄\_P² \= (8πG)⁻¹; H̄₀/M̄\_P \= 5.9×10⁻⁶¹ (NON-CLAIM, \= B3). Dynamical algebra A\_phys \= M₁₁(ℂ) (Hilbert dim 11, operator dim 121); observer algebra N \= M₃ ⊕ M₂ ⊕ M₆ (operator dim 49). **121 \= dim M₁₁ is an operator count; rank P ≤ 11 in M₁₁.** Sector dimensions (d\_X, d\_Z, d\_Y) \= (a, b, c) \= (3, 2, 6), D \= a \+ b \+ c \= **Q** \= 11\. Mediator-Graph \= path X–Z–Y (A23.7); L\_XY ≡ 0\. Mediation strength **κ²** is the single dynamical coupling.

**Rate units (patch).** κ² \= **A**/**Q** is dimensionless. Rates are stated in the **dimensionless-time convention** τ \= Γ₀t, in which qᵢ→ⱼ(τ) \= κ²dⱼ; the physical rate is qᵢ→ⱼ(t) \= Γ₀κ²dⱼ, with Γ₀ the (single) microscopic attempt scale. The values **2A/Q** and **6A/Q** are accordingly Γ₀-normalized dimensionless rates, not dimensionful frequencies.

**§3. Main Theorem 1 — Mediator-Graph Algebra Generation**

**Theorem A23.5a / A23.7 (PROVEN — Appendix A).** Blocks M\_{dᵢ}(ℂ) plus one nonzero intertwiner per edge generate, within each connected component α, the full M\_{Dα}(ℂ) (Dα \= Σ\_{i∈α} dᵢ); the generated algebra is ⊕\_α M\_{Dα}(ℂ), irreducible (= M\_D) iff connected, with dim(commutant) \= \#components. **Z-Spin is the path X–Z–Y → M₁₁(ℂ)**, unique trace τ(P\_X, P\_Z, P\_Y) \= (3, 2, 6)/11. Verified by the matrix-unit argument, a multiplicity-2 control, and a span closure to 121 (= dim M₁₁; the Hilbert dimension is 11).  The path is connected and ordered — the connectivity gives the algebra (this theorem), the ordering gives the semigroup (§4).

**§4. Main Theorem 2 — The Dimension-Weighted Mediator Semigroup**

**The principle.** Every allowed microstate transition between adjacent sectors carries the same Z-Spin mediation strength κ² \= **A**/**Q**. A microstate in sector i can transition to any of the dⱼ microstates of an adjacent sector j, so the coarse-grained sector-population rate is qᵢ→ⱼ \= Γ₀κ²dⱼ (one mediation quantum per available final microstate), with no X–Y transition (L\_XY ≡ 0). On the path X–Z–Y this fixes the generator **Q** (rows \= rate i→j; Γ₀ \= 1 in dimensionless time):

**Q** \= κ² · \[ \[−d\_Z, d\_Z, 0\], \[d\_X, −(d\_X+d\_Y), d\_Y\], \[0, d\_Z, −d\_Z\] \] \= κ² · \[ \[−2, 2, 0\], \[3, −9, 6\], \[0, 2, −2\] \].

**§4.1  A23.14a — Mathematical Semigroup Theorem \[PROVEN\]**

**Theorem A23.14a (PROVEN).** For the path X–Z–Y with edge-isotropic rates qᵢ→ⱼ \= Γ₀κ²dⱼ and sector dimensions (a, b, c):

**(i) Stationary distribution.** π**Q** \= 0 has the unique solution **πᵢ \= dᵢ/D \= (3, 2, 6)/11** — the A23.5a trace weights, now the dynamical stationary distribution.

**(ii) Exact spectrum (general).** The characteristic polynomial factors, for arbitrary (a, b, c), as

**det(λI − Q) \= λ(λ \+ bκ²)(λ \+ Dκ²),**

so the eigenvalues are {0, −bκ², −Dκ²}. With b \= d\_Z \= 2, D \= **Q** \= 11, κ² \= **A**/**Q**: bκ² \= 2**A**/**Q** and Dκ² \= **Q**·(**A**/**Q**) \= **A**, giving **{0, −2A/Q, −A}** — exactly the ZS-Q7 cubic λ(λ \+ 2A/Q)(λ \+ A) \= 0 (verified by exact symbolic computation, both for (3, 2, 6\) and for symbolic (a, b, c)).

**(iii) Both corpus rates as matrix elements.** q\_{X→Z} \= d\_Zκ² \= **2A/Q** and q\_{Z→Y} \= d\_Yκ² \= **6A/Q** — the two ZS-M43 rates are entries of the generator, not separate inputs.  These are mathematical identities, given the generator; the Monte-Carlo H-theorem of v3.2 is replaced by the exact proof of §5.

**The GKLS construction (no energy ladder).** Define, for each allowed edge i\~j and microstates α \= 1…dᵢ, β \= 1…dⱼ, the jump operator **L\_{jβ←iα} \= √(Γ₀κ²) |j,β⟩⟨i,α|** (and L\_{Y←X} \= 0). The GKLS generator, summed over sector populations, gives dpᵢ/dt \= Σ\_{j\~i} Γ₀κ²(dᵢ pⱼ − dⱼ pᵢ), i.e. exactly qᵢ→ⱼ \= Γ₀κ²dⱼ — with no energy ladder, no equal-spacing assumption, and no bath spectral density; L\_XY \= 0 reflects the absent X–Y intertwiner directly.

**§4.2  A23.14c — Sector-Covariant Uniqueness Lemma \[PROVEN\]**

**Lemma A23.14c (PROVEN).** Among GKLS generators that are (i) covariant under U(d\_X)×U(d\_Z)×U(d\_Y), (ii) free of any direct X–Y channel, (iii) edge-isotropic (one common mediation scale), and (iv) primitive and trace-preserving, the dimension-weighted generator is unique. **Proof.** The jump operators on an edge (i, j) live in Hom(H\_j, H\_i), on which U(d\_i)×U(d\_j) acts as the irreducible external tensor product fund ⊠ antifund; its commutant is one-dimensional (verified: the group generates the full matrix algebra M\_{d\_i d\_j}, so the commutant has dimension 1 for both the X–Z and Z–Y edges). By Schur's lemma the (covariant, positive) Kossakowski block is a scalar, so the jump amplitudes are uniform on each edge; edge isotropy sets the common scale to Γ₀κ², giving qᵢ→ⱼ \= Γ₀κ²dⱼ.  This seals the “arbitrary generator” objection: under sector covariance and edge isotropy the generator is forced.

**§4.3  A23.14b — Z-Spin Realization \[DERIVED-CONDITIONAL\]**

**A23.14b (DERIVED-CONDITIONAL).** The identification of this generator as the physical Z-Spin sector dynamics is conditional on the **sector-isotropic mediation principle**: that every allowed microtransition carries the common amplitude √(Γ₀κ²). The GKLS construction (A23.14a) proves this generator is realizable, and the uniqueness lemma (A23.14c) proves it is the only sector-covariant edge-isotropic option; what is not proved here is that the Z-Spin master action selects sector covariance and edge isotropy at the microscopic level. **\[A23.14a (the mathematics) and A23.14c (uniqueness under symmetry) are PROVEN; A23.14b (the physical Z-Spin realization) is DERIVED-CONDITIONAL on the sector-isotropic mediation principle. The inter-sector rates, stationary trace weights, and full spectrum follow from the single coupling κ² \= A/Q with no energy-ladder hypothesis; the general (a,b,c) factorization shows the slow mode \= d\_Z·κ² and fast mode \= Q·κ² are structural, not numerological.\]**

**§5. Main Theorem 3 — Modular Detailed Balance and Observer Size-Bias**

**Theorem A23.15 (PROVEN).** The dimension-weighted generator of §4 is reversible, and:

**(i) Detailed balance.** πᵢ qᵢ→ⱼ \= (dᵢ/D)κ²dⱼ \= κ²dᵢdⱼ/D, symmetric in i, j; hence **πᵢ qᵢ→ⱼ \= πⱼ qⱼ→ᵢ**.

**(ii) Modular detailed balance.** With the modular Hamiltonian **K**ᵢ \= −ln πᵢ,

**qᵢ→ⱼ / qⱼ→ᵢ \= dⱼ/dᵢ \= πⱼ/πᵢ \= e^{−(Kⱼ − Kᵢ)},   i.e.   ln(qᵢ→ⱼ/qⱼ→ᵢ) \= −ΔKᵢ→ⱼ.**

This single identity links A23.5a's trace weights, A23.MC's modular differences, ZS-F19's −ln 2 (q\_{Z→Y}/q\_{Y→Z} \= d\_Y/d\_Z \= 3 ⇒ Δ**K**\_{Z→Y} \= −ln 3; q\_{X→Z}/q\_{Z→X} \= 2/3), ZS-M43's rates, and ZS-Q7's arrow-of-time relaxation into one modular-thermodynamic relation.

**(iii) Observer size-bias.** The observer weight is the size-bias of the stationary distribution: **ωᵢ \= dᵢ πᵢ / Σⱼ dⱼ πⱼ \= dᵢ²/Σⱼ dⱼ² \= (9, 4, 36)/49**, with Radon–Nikodym density **hᵢ \= ωᵢ/πᵢ \= D dᵢ/Σⱼ dⱼ² \= 11 dᵢ/49** — exactly the A23.MC density. State sampling gives π ∝ dᵢ; operator sampling gives ω ∝ dᵢ². The two weightings are one Z-mediated equilibrium sampled in state space and in operator space. 

**Corollary A23.15.1 (exact H-theorem, PROVEN).** With detailed balance, write x \= rᵢ qᵢ→ⱼ, y \= rⱼ qⱼ→ᵢ. Then

d/dt D(r‖π) \= −½ Σ\_{i,j} (rᵢ qᵢ→ⱼ − rⱼ qⱼ→ᵢ) · ln\[(rᵢ qᵢ→ⱼ)/(rⱼ qⱼ→ᵢ)\] \= −½ Σ (x − y) ln(x/y) ≤ 0,

since (x − y) ln(x/y) ≥ 0 for all x, y \> 0\. Hence **D(r‖π) is a Lyapunov function** (verified symbolically; the Monte-Carlo over random distributions is retained only as a regression test). The nonzero relaxation rates are γ\_slow \= 2**A**/**Q** and γ\_fast \= **A**, giving the new exact prediction **γ\_fast/γ\_slow \= A/(2A/Q) \= Q/2 \= 11/2**, with timescales τ\_slow \= **Q**/(2**A**), τ\_fast \= 1/**A**. 

**The new predictions (PREDICTION).** Beyond reproducing γ\_xz \= 2**A**/**Q** and γ\_zy \= 6**A**/**Q**, the generator fixes the reverse rates γ\_zx \= d\_Xκ² \= **3A/Q** and γ\_yz \= d\_Zκ² \= **2A/Q**, so the four edge-direction rates are **γ\_xz : γ\_zx : γ\_zy : γ\_yz \= 2 : 3 : 6 : 2**, with detailed-balance ratios 2/3 and 3\. These two reverse rates and the ratio **Q**/2 are new, falsifiable consequences not present in the prior corpus. **\[PREDICTION.\]**

**§6. Main Theorem 4 — The Modular-Centralizer Observer Theorem**

**Theorem A23.MC (PROVEN).** ω\_reg(Pᵢ) \= dᵢ²/49 \= (9, 4, 36)/49 (= the §5(iii) size-bias), density h \= ⊕ᵢ (11 dᵢ/49) I\_{dᵢ}; since the dᵢ are distinct, **(i)** the modular centralizer M^{σ^ω} \= commutant(h) \= **N**; **(ii)** σ\_t^ω(Cᵢⱼ) \= (dᵢ/dⱼ)^{it}Cᵢⱼ; **(iii)** e⁻ᶜ \= 121/49 \= dim M₁₁/dim N, Δ**K**\_{X→Y} \= −ln 2\.  Pinching index \= **3** (tight), distinct from 121/49. Where §5 derives ω dynamically (the size-bias of the semigroup stationary state), A23.MC derives it modular-theoretically (the intrinsic centralizer of the regular state) — the same (9, 4, 36)/49 from two routes. A23.5b is a DERIVED observer-algebra realization, conditional only on the entropy offset (now \= A\_dS/4G, §8).

**§7. The Dimension-Weighted Laplacian (Upgrading A23.8) and a Quantum-Simulator Protocol**

**The A23.8 upgrade (CLOSED-NEGATIVE → general theorem).** A23 once claimed the ordinary unweighted graph Fiedler eigenvalue equalled 2**A**/**Q**, then retracted it (the ordinary path-Laplacian Fiedler value is 1, not 2**A**/**Q**). v3.3 explains why: the ordinary graph Laplacian is the wrong generator. The correct object is the dimension-weighted mediator Laplacian qᵢⱼ \= κ²aᵢⱼdⱼ, reversible w.r.t. πᵢ \= dᵢ/D; its symmetrization S \= Π^{1/2}**Q**Π^{−1/2} has off-diagonal entries Sᵢⱼ \= κ²aᵢⱼ√(dᵢdⱼ), and its spectral gap is 2**A**/**Q** — not the ordinary Fiedler value. **\[The retraction is upgraded to a theorem: the relaxation gap is the dimension-weighted Laplacian gap (incorporating the multiplicities dᵢ), explaining the failure of the ordinary unweighted graph gap. PROVEN.\]**

**A quantum-simulator protocol (TESTABLE).** The architecture H \= ℂ³ ⊕ ℂ² ⊕ ℂ⁶ (a 3-level X register, a 2-channel Z mediator, a 6-channel Y reservoir) realizes the generator directly: prepare population in X, activate only the X–Z and Z–Y jump channels with equal microtransition amplitudes, measure p\_X(t), p\_Z(t), p\_Y(t), fit the two decay exponents, and check the equilibrium ratio. Predictions: p(∞) \= (3, 2, 6)/11, λ\_slow \= −2**A**/**Q**, λ\_fast \= −**A**, λ\_fast/λ\_slow \= **Q**/2 \= 11/2; observer tomography checks the size-biased ω \= (9, 4, 36)/49. **\[TESTABLE — the core A23 dynamics is verifiable on a small open-system simulator without awaiting the absolute cosmological scale.\]**

**§8. The Cosmological Reductions**

**(offset) — DERIVED-CONDITIONAL.** The CLPW reference matching fixes the crossed-product entropy offset: at the maximum-entropy (tracial) state the Type-II entropy is zero, so the offset equals the de Sitter horizon entropy, **S₀ \= A\_dS/4G \= 8π²M̄\_P²/H²** (Gibbons–Hawking) — not free. A23.5b's residual reduces to the corpus-wide **B3 absolute scale** H/M̄\_P.

**(b-energy) — DERIVED-CONDITIONAL.** Since rank P ≤ 11 in M₁₁, the face counts (6, 32, 83\) need a separate 121-carrier \= the **face algebra A\_face \= ℂ¹²¹** (the abelian algebra of functions on the 121 faces; structurally distinct from L²(M₁₁)). Within-component slot-universality is DERIVED (polytope face-transitivity), and the cross-component one-quantum-per-face is **combinatorial (not metric) holography** — a PREDICTION, since the faces have unequal areas (cube 1.33 vs dodecahedron 0.88). A BV–BFV/TQFT state-sum route (ZS-F0's cobordism functor) could promote it: Pachner-move invariance with one representation label per face forces equal face weights, so topological state-sum invariance ⇒ equal face weight.

**(embedding) — OPEN.** The trace-preserving \*-homomorphism **Φ\_face : A\_face → M\_dS** — with domain the face algebra A\_face \= ℂ¹²¹ (not a Hilbert space) — selecting the rank-(6, 32, 83\) face-indicator projectors needs the ZS-F2 §11.4 construction; the matter/empty-cell picture (38 filled \+ 83 empty cells of the Q² \= 121 register, Ω\_cdm \= 32 \= dodecahedron \+ icosahedron faces) is a coherent interpretation, not a derivation. **The deepest remaining cosmological gap.**

**(period-2) — OPEN, sharpened.** The absolute O(1) factor |Δ**W**| \= 2: beyond the complex-bion (S\_bion \= 2S\_I), RG (b₀ \= 1/2), and SU(2)/ℤ₂ routes (all needing the master action), v3.2 adds a Markov large-deviation route built on the §4 generator: the X→Y rare-event path must traverse two edges (the graph distance d(X, Y) \= 2 on the PROVEN path X–Z–Y), so the minimal large-deviation action decomposes S\_{X→Y} \= S\_{X→Z} \+ S\_{Z→Y}; if each elementary seam crossing has action 1/κ², then S\_{X→Y} \= 2/κ². **The factor 2 is the mandatory two-edge mediation (a structural graph distance), not a spinor number** — reducing period-2 to the per-edge action normalization. **\[OPEN; the double-well control ΔW \= 4/3 confirms the value is non-generic.\]**

**§9. Main Theorem 5 — Finite-Boundary Non-Predictivity**

**Theorem A23.10 (PROVEN-with-hypotheses).** If the admissible finite covariant counterterm class contains one free vacuum-proportional term α₀∫√h and no independent normalization fixes α₀ (with boundary diffeomorphism invariance and a finite boundary), then T\_ij^vac ↦ T\_ij^vac \+ (α₀/2)√h h\_ij.  GHY-counterterm-alone route **CLOSED-NEGATIVE**; the Wald first-law fixes α₀ (pure-dS → Ω\_Λ \= 1). This Brown–York no-go is logically independent of the §4–§6 dynamics; it resolves gate G14c and may be spun off.

**§10. Cross-Version Consistency Audit**

Table 2\. Cross-version dependency audit.

| Upstream result | Status | v3.3's effect | Safe? |
| ----- | ----- | ----- | ----- |
| ZS-A19 κ² \= A/Q \= 35/4807 | PROVEN | §4: the single generator coupling; unchanged | ✓ |
| A23.5a weights (3,2,6)/11 | PROVEN | §4: now also the dynamical stationary distribution | ✓ |
| ZS-M43 rates 2A/Q, 6A/Q | PROVEN | §4: now matrix elements; reverse rates 3A/Q, 2A/Q predicted | ✓ |
| ZS-Q7 cubic λ(λ+2A/Q)(λ+A) | PROVEN | §4: now the generator's characteristic polynomial | ✓ |
| ZS-F19 ΔK\_{X→Y} \= −ln 2 | DERIVED | §5: from modular detailed balance ln(qᵢⱼ/qⱼᵢ) \= −ΔK | ✓ |
| A23.MC ω \= (9,4,36)/49 | PROVEN | §5(iii): the size-bias of π; §6: the centralizer — two routes | ✓ |
| A23.8 (graph gap) | WITHDRAWN | §7: upgraded to the dimension-weighted Laplacian theorem | ✓ |
| ZS-F2 §11.4 Ω\_Λ \= 83/121 | DERIVED | §8: combinatorial-holography prediction; embedding OPEN | ✓ |
| CLPW max-entropy \= unit 1 | IMPORTED-PROVEN | §8: offset \= A\_dS/4G | ✓ |

**Result.** No version conflict; v3.3 unifies five previously separate PROVEN/DERIVED results into one generator, seals the realization with a uniqueness lemma, and upgrades the A23.8 retraction, without disturbing anything upstream. **\[DERIVED.\]**

**§11. Consolidated Gate Ledger**

Table 3\. Consolidated gate ledger (v3.3).

| Gate | Calculation | Status (v3.3) |
| ----- | ----- | ----- |
| G-algebra (MT1) | M₃⊕M₂⊕M₆ \+ C \= M₁₁; weights (3,2,6)/11. | PROVEN (A23.5a / A23.7). |
| G-semigroup (MT2) | dimension-weighted generator. | A23.14a PROVEN; A23.14c uniqueness PROVEN; A23.14b realization DERIVED-CONDITIONAL. |
| G-modular (MT3) | detailed balance & size-bias. | PROVEN (A23.15): exact H-theorem; Q/2; reverse rates. |
| G-centralizer (MT4) | observer \= modular centralizer. | PROVEN (A23.MC); index 3\. |
| G12a-phys (A23.5b) | de Sitter observer realization. | DERIVED-CONDITIONAL — offset \= A\_dS/4G (§8); residual \= B3. |
| G12b-exponent | 1/κ² \= Q/A. | PROVEN. |
| G12b-O(1) | S\_inst \= 2/κ² \= |ΔW| \= 2\. | OPEN; two-edge-mediation makes ‘2’ structural (§8); per-edge action pending. |
| G14c (MT5) | boundary reproduces Ω\_Λ? | CLOSED-NEGATIVE (GHY-alone); Wald fixes coeff. |
| G14-energy (b-energy) | Ωᵢ \= rank Pᵢ/121. | DERIVED-CONDITIONAL — combinatorial-holography PREDICTION (§8); embedding OPEN. |
| G-laplacian (A23.8) | spectral gap. | PROVEN — dimension-weighted Laplacian gap \= 2A/Q (§7). |

**§12. Conclusion**

Across twenty versions the ZS-A23 program has matured from a defensive record of “how far the vacuum-scale debt was reduced” into an exact correspondence between a finite-register operator algebra and a reversible three-sector Markov semigroup.

**The unification (the centerpiece).** One dimension-weighted generator — built from the single coupling κ² \= **A**/**Q** by the rule qᵢ→ⱼ \= Γ₀κ²dⱼ — has the trace weights (3, 2, 6)/11 as its stationary distribution (A23.5a), the cubic λ(λ \+ 2A/Q)(λ \+ A) as its characteristic polynomial (ZS-Q7), the rates 2**A**/**Q**, 6**A**/**Q** as its matrix elements (ZS-M43), the modular difference −ln 2 from its log-ratios (ZS-F19), and the observer weight (9, 4, 36)/49 as its operator-space size-bias (A23.MC). The general (a, b, c) factorization λ(λ \+ bκ²)(λ \+ Dκ²) shows the slow mode is set by d\_Z and the fast mode by **Q** — structural, not numerological — a GKLS construction removes the energy-ladder assumption, and a Schur uniqueness lemma fixes the generator. New exact predictions follow: the relaxation ratio **Q**/2 \= 11/2 and the reverse rates (the four edge rates 2 : 3 : 6 : 2). The A23.8 retraction is upgraded to the dimension-weighted-Laplacian theorem.

**The cosmological reductions.** The entropy offset is the de Sitter entropy A\_dS/4G (residual \= the universal B3 scale); b-energy is DERIVED-CONDITIONAL with the dark-sector budget identified as a combinatorial-holography prediction (with a BV–BFV closure route); the embedding functor Φ\_face : A\_face → M\_dS (needing ZS-F2) and the absolute O(1) factor remain OPEN, the latter sharpened so its factor 2 is the mandatory two-edge mediation.

**Net.** The dynamical heart of A23 — trace weights, inter-sector rates, relaxation spectrum, modular differences, observer weight — is now a single dimension-weighted mediator principle with new predictions and an experimental protocol; the cosmological-constant problem is localized to the embedding, the B3 scale, and the absolute O(1) factor. The corpus standard — honest conditional reduction, anti-numerology enforced (the general (a, b, c) factorization, the double-well control), every over-claim retracted — is maintained. Zero free parameters; (**A**, **Q**, dim Z) \= (35/437, 11, 2\) LOCKED.

**§13. Remaining Programs and Spin-Off Potential**

**Remaining.** (embedding) Φ\_face : A\_face → M\_dS from ZS-F2 (§8). (combinatorial holography) the BV–BFV state-sum giving equal face weights (§8). (B3) the absolute IR scale H/M̄\_P (the corpus-wide debt). (period-2) the per-edge large-deviation action normalizing each seam crossing to 1/κ² (§8). **Spin-off potential:** (1) the dimension-weighted mediator semigroup (§§4–7) — algebra generation, the exact Markov–operator correspondence, the uniqueness lemma, modular detailed balance, the exact H-theorem, the dimension-weighted Laplacian, and the simulator protocol — is a self-contained operator-algebra / open-quantum-systems paper, the strongest spin-off; (2) the de Sitter observer algebra with the CLPW offset \= A\_dS/4G; (3) the Boundary Non-Predictivity Theorem (§9); (4) the unified spin-graded continuous-clock program (ZS-A24).

**Appendix A — General Proof of the Mediator-Graph Theorem**

Let A be generated by ⊕ᵢ M\_{dᵢ}(ℂ) (matrix units e^{(i)}\_{ab}) and, per edge (i, j), one nonzero Cᵢⱼ with a nonzero entry at (a₀, b₀). Then e^{(i)}\_{a a₀}·Cᵢⱼ·e^{(j)}\_{b₀ b} is a nonzero multiple of e\_{ab}, so A ⊇ Hom(H\_j, H\_i) (and adjoints). Iterating along a connected path generates every e\_{ab} within a component, so A \= ⊕\_α M\_{Dα}(ℂ), \= M\_D iff connected, dim(commutant) \= \#components.  The path X–Z–Y is connected → M₁₁, and ordered → the §4 semigroup. The 121 is the operator dimension; the Hilbert dimension is 11, rank P ≤ 11\.

**Appendix B — The Generator's Exact Spectrum**

For the path X–Z–Y with qᵢ→ⱼ \= κ²dⱼ, **Q** \= κ²\[\[−b, b, 0\], \[a, −(a+c), c\], \[0, b, −b\]\] (rows \= rate i→j). Direct expansion:

det(λI − **Q**) \= (λ \+ bκ²)·{(λ \+ (a+c)κ²)(λ \+ bκ²) − b(a+c)κ⁴} \= (λ \+ bκ²)·λ·(λ \+ (a+b+c)κ²) \= **λ(λ \+ bκ²)(λ \+ Dκ²)**.

Eigenvalues {0, −bκ², −Dκ²}; with (a, b, c) \= (3, 2, 6), κ² \= **A**/**Q**: {0, −2**A**/**Q**, −**A**}. The slow gap is set by the mediator dimension b \= d\_Z; the fast rate by the total D \= **Q**. The five invariants of N ⊂ M₁₁ (dim H \= 11, dim N \= 49, dim M₁₁ \= 121, ratio 121/49, index 3\) are unchanged; 121 is the operator dimension, structurally distinct from the face-count total 6 \+ 32 \+ 83\.

**Acknowledgements and Code Availability**

This v3.3 applies five external-review patches to v3.2: the split of Main Theorem 2 into a mathematical semigroup theorem (A23.14a, PROVEN) and a Z-Spin realization (A23.14b, DERIVED-CONDITIONAL); the sector-covariant uniqueness lemma (A23.14c, PROVEN via Schur); the rate-unit convention (Γ₀); the exact one-line H-theorem proof (the Monte-Carlo demoted to a regression test); and the correction of the embedding domain to the face algebra A\_face. The Dimension-Weighted Mediator Semigroup Theorem unifies the sector trace weights, the inter-sector rates, the relaxation cubic, the modular difference, and the observer weight as exact consequences of one generator built from the single coupling κ² \= **A**/**Q**.

**zs\_a23\_v3\_3\_audit.py** (exact symbolic): algebra generation; the dimension-weighted generator (stationary, the general (a,b,c) factorization, the spectrum, the rates); the **sector-covariant uniqueness lemma** (commutant 1-dimensional); detailed and modular detailed balance; the observer size-bias and RN density; the **exact H-theorem** (with the Monte-Carlo retained as a regression test); the new predictions (Q/2, reverse rates 2:3:6:2); the ordinary-vs-dimension-weighted Laplacian comparison; and the cosmological identifications. The NOTE states: “26/26 internal consistency checks PASS; the cosmological identifications (offset, embedding, combinatorial holography, period-2) remain theorem-level arguments, not code-verified results.” Independent rerun recommended.

**References**

\[W89\] S. Weinberg, The Cosmological Constant Problem, Rev. Mod. Phys. 61, 1 (1989).

\[GH77\] G. W. Gibbons and S. W. Hawking, Cosmological Event Horizons, Phys. Rev. D 15, 2738 (1977).

\[Bog76\] E. B. Bogomolny, Stability of Classical Solutions, Sov. J. Nucl. Phys. 24, 449 (1976).

\[Wed08\] J. H. M. Wedderburn, On hypercomplex numbers, Proc. London Math. Soc. 6, 77 (1908).

\[Schur05\] I. Schur, Neue Begründung der Theorie der Gruppencharaktere, Sitzungsber. Preuss. Akad. (1905).

\[Nor97\] J. R. Norris, Markov Chains, Cambridge University Press (1997).

\[GKS76\] V. Gorini, A. Kossakowski and E. C. G. Sudarshan, J. Math. Phys. 17, 821 (1976).

\[Lin76\] G. Lindblad, On the generators of quantum dynamical semigroups, Commun. Math. Phys. 48, 119 (1976).

\[Dav74\] E. B. Davies, Markovian master equations, Commun. Math. Phys. 39, 91 (1974).

\[Con73\] A. Connes, Une classification des facteurs de type III, Ann. Sci. ÉNS 6, 133 (1973).

\[TT70\] M. Takesaki, Tomita's Theory of Modular Hilbert Algebras and its Applications, LNM 128, Springer (1970).

\[PP86\] M. Pimsner and S. Popa, Entropy and index for subfactors, Ann. Sci. ÉNS 19, 57 (1986).

\[FW98\] M. I. Freidlin and A. D. Wentzell, Random Perturbations of Dynamical Systems, Springer (1998).

\[Doi76\] M. Doi, J. Phys. A 9, 1465 (1976); L. Peliti, J. Physique 46, 1469 (1985).

\[DU14\] G. V. Dunne and M. Ünsal, Phys. Rev. D 89, 041701 (2014).

\[CLPW22\] V. Chandrasekaran, R. Longo, G. Penington and E. Witten, JHEP 02 (2023) 082, arXiv:2206.10780.

\[DEHK25a\] K. De Vuyst, S. Eccles, P. A. Höhn and J. Kirklin, JHEP 07 (2025) 146, arXiv:2405.00114.

\[DEHK25b\] K. De Vuyst, S. Eccles, P. A. Höhn and J. Kirklin, JHEP 07 (2025) 063, arXiv:2412.15502.

\[Wald93\] R. M. Wald, Black hole entropy is the Noether charge, Phys. Rev. D 48, R3427 (1993).

\[BK99\] V. Balasubramanian and P. Kraus, Commun. Math. Phys. 208, 413 (1999), arXiv:hep-th/9902121.

\[tH93\] G. 't Hooft, arXiv:gr-qc/9310026; L. Susskind, J. Math. Phys. 36, 6377 (1995).

\[ZS-Q7\] K. Kang, ZS-Q7: Y-Sector Gravitational Entropy Dominance, Z-Spin Cosmology (2026).

\[ZS-QH\] K. Kang, ZS-QH: A 3-2-6 Open-System Hardware Architecture, Z-Spin Cosmology (2026).

\[ZS-F0\] K. Kang, ZS-F0: BV–BFV Cobordism and Wilson Loops, Z-Spin Cosmology (2026).

\[ZS-F2\] K. Kang, ZS-F2: Geometric Impedance A \= 35/437 (§11.4 face-counting), Z-Spin Cosmology (2026).

\[ZS-F19\] K. Kang, ZS-F19: Frame-Invariant Tilt Theorem, Z-Spin Cosmology (2026).

\[ZS-M3\] K. Kang, ZS-M3: Regge-Holonomy, Immirzi & Z-Telomere, Z-Spin Cosmology (2026).

\[ZS-A19\] K. Kang, ZS-A19: Z-Spin Boundary Tension as Geometric Dust, Z-Spin Cosmology (2026).

\[ZS-M43\] K. Kang, ZS-M43: The Z-Goldstone Is a Coherent Superfluid, Z-Spin Cosmology (2026).

\[ZS-A22\] K. Kang, ZS-A22 v2.2: The Phantom-Divide Gate, Z-Spin Cosmology (2026).

\[Book\] K. Kang, The Book of Z-Spin Cosmology v9.0 (Light OS for AI), Z-Spin Cosmology (2026).

**Version History**

Table 4\. Version history.

| Version | Date | Change |
| ----- | ----- | ----- |
| v1.0–v2.9 | 2026 | v1.0 over-claimed → algebraic weights, Mediator-Graph, observer theorem, Modular-Centralizer unification, programs executed, corrections. Superseded. |
| v3.0 | 2026 | Four priority programs: the Davies rate γᵢ→ⱼ \= dⱼ·(A/Q); carrier ≠ L²(M₁₁); within-component slot-universality; the ℤ\_N entropy divergence. Superseded. |
| v3.1 | 2026 | Five residual programs: offset \= A\_dS/4G; equal spacing from the path; combinatorial-holography prediction; embedding/period-2 OPEN. Superseded. |
| v3.2 | 2026 | Restructured around the Dimension-Weighted Mediator Semigroup Theorem; A23.8 upgraded; new predictions Q/2, reverse rates 2:3:6:2; quantum-simulator protocol. Superseded. |
| v3.3 | March 2026 | Final patched version (twentieth). (1) MT2 split into A23.14a (PROVEN math) \+ A23.14b (DERIVED-CONDITIONAL realization); (2) A23.14c sector-covariant uniqueness lemma (Schur, PROVEN); (3) rate units fixed by Γ₀; (4) exact one-line H-theorem (MC demoted to regression test); (5) embedding domain corrected to A\_face \= ℂ¹²¹. 26/26 checks PASS. Zero free parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED. (Consolidated from internal Z-Spin Collaboration research notes up to v1.6.0.) |

— End of ZS-A23 v3.3 —