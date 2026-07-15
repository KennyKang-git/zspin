**ZS-F31**

**Covariant Cosmic Reality: the Exact Modular GKLS Spectrum, the Seam-Transport Realization, and the Normalizable Causal-Entropic Present Gate**

*From a Single Genuine Lift to Three Independent Results — a Closed-Form 121-Face Lindblad Spectrum, an Exact Seam Half-Transport Replacing the Retracted Monodromy Route, and an Entropy-Budget Proof of Present-Measure Normalizability*

**Author:** Kenny Kang

**Date:** March 2026

**Paper code:** ZS-F31 v1.4 (Final)  ·  Foundations–Astrophysics series  ·  Theme: Cosmic Reality / Modular-Lift Reduction

**Affiliation:** Z-Spin Collaboration

**Verification (v1.4, Final):** 42/42 arithmetic, symbolic, and CONSTRUCTION checks PASS, including (i) the jump-only modular GKLS lift in BOTH pictures (Theorem P1), (ii) the full 121-face Lindblad spectrum Spec(𝓛★) \= Spec(𝓛\_π) ⊎ {−½(Γ\_c+Γ\_d)} as a multiset union of two invariant blocks, verified against the dense superoperator up to dimension 121 and exhibited in closed form at 14641 \= 121² (Theorem P2), and (iii) the sign-corrected Seam Transport realization — singular-value Cartan length ℓ\_K \= |ρ\_K| with the signed rapidity ρ\_K \= ½Tr\[(n·σ)logU\_K\] recovered from the oriented axis, tested at BOTH signs (Theorem R2a) | 7 operator gates remain OPEN, not counted as PASS (R2b, P1-core, C\_int, clock map, Z-screen, Gate E, coincidence gate) | FINAL PATCHES (v1.4): the seam result is open-path TRANSPORT not closed-loop holonomy (the connection is sl(2,ℂ)-valued pure-gauge); Gate E is downgraded to HYPOTHESIS-strong (data processing gives a value inequality, not a pointwise production-rate inequality); the §2.5 carrier sector is corrected (Brown–Kuchař dust vs the S14 prefactor, and the 3-form potential A₃ with F₄ \= dA₃) | no new fitted parameter; (***A***, ***Q***, dim Z) \= (35/437, 11, 2\) LOCKED | script: zs\_f31\_verify\_v1\_4.py (42/42 PASS)

**§0. Abstract**

This version converts the single repaired theorem of v1.2 into three independent contributions, removes one unforced parameter, retracts a route that did not match the corpus, and restores the integrative master-action content. v1.2 had correctly replaced v1.1’s broken population lift (the family Ψ\_t \= ι∘Φ\_t∘E, which is not a semigroup because Ψ\_0 \= E\_D ≠ id) with a genuine Lindblad generator. v1.3 sharpens and extends that core.

**Contribution 1 — the exact 121-face modular GKLS spectrum (Theorem P2).** Working in the Schrödinger picture with a *jump-only* generator 𝓛★(ρ) \= Σ\_{a≠b} r\_{ab}(v\_{ab} ρ v\_{ab}† − ½{q\_b, ρ}) (the ***A***/***Q*** dephasing term of v1.2 is removed), every coherence |c⟩⟨d| is an eigenvector with the explicit eigenvalue −½(Γ\_c \+ Γ\_d), Γ\_c \= Σ\_{a≠c} r\_{ac}. Hence the full spectrum splits in closed form, Spec(𝓛★) \= Spec(𝓛\_π) ⊎ {−½(Γ\_c \+ Γ\_d) : c ≠ d}, with 121 population and 121·120 \= 14520 coherence eigenvalues totalling 14641 \= 121². This is a genuine spectral theorem for the 121-face generator, not a toy check, and it is verified against the dense superoperator up to dimension 121\. Removing the dephasing term makes the construction strictly parameter-free.

**Contribution 2 — the exact seam-support connection (Theorem R2a).** v1.2’s F14-ODE monodromy route does not match ZS-F14, whose joint ODE is an (ε, θ) radial–angular system, not a linear support ODE with two periodic solutions (whose loop monodromy would be trivial). We RETRACT it and replace it with the exact seam half-transport built from ZS-F30’s own object g\_K(θ) \= exp\[½ ρ\_K(θ) n·σ\] with the seam antisymmetry ρ\_K(θ+π) \= −ρ\_K(θ). Then U\_K(θ+π, θ) \= g\_K(θ+π)⁻¹ g\_K(θ) \= g\_K(θ)² \= exp\[ρ\_K(θ) n·σ\], whose singular-value Cartan length is ℓ\_K \= |ρ\_K| and whose signed oriented rapidity ρ\_K \= ½Tr\[(n·σ)logU\_K\] is recovered from the fixed axis. This PROVES the oriented seam-TRANSPORT coordinate ρ\_tr^{oriented} \= ρ\_K (R2a) — an open-path Cartan realization, not a closed-loop holonomy — leaving the physical identification A\_Z ∼ A\_K (R2b), i.e. the promotion of transport to holonomy, OPEN. The connection A\_K is sl(2,ℂ)-valued pure-gauge (a boost).

**Contribution 3 — the normalizable causal-information present measure.** The present is selected by the independent causal-diamond Z-Spin measure dμ\_ZCD ∝ A\_D(T) σ\_Z(T) dT, with σ\_Z the Spohn entropy production of the genuine QMS. Normalizability is now an *entropy-budget* theorem requiring no modified log-Sobolev inequality: since σ\_Z \= −d/dT D(ρ\_T ‖ ρ\*), one has ∫₀^∞ σ\_Z dT \= D(ρ\_0 ‖ ρ\*) − D(ρ\_∞ ‖ ρ\*) ≤ D(ρ\_0 ‖ ρ\*), so with the screen pixel count bounded N\_pix ≤ N\_max the measure integral is ≤ N\_max D(ρ\_0 ‖ ρ\*) \< ∞. The bulk–boundary relation Gate E is recast from an over-strong equality into a data-processing *inequality* V\_c ṡ\_bulk ≤ N\_pix σ\_Z (equality \= channel saturation, OPEN), and the coincidence test G \= Ω\_Λ(T\*) − 83/121 is honestly downgraded to a DERIVED-CONDITIONAL test with an explicit dependency tree on the clock map, the absolute scale B3, and Gate E.

The integrative master action S\_carrier \= S\_S14^tetrad \+ S\_BK \+ S\_Λ and its full Euler–Lagrange system are restored (§2.5, §12). The budget (Ω\_b, Ω\_m, Ω\_Λ) \= (6, 38, 83)/121 (Ω\_Λ within 0.2σ of Planck 2018, all three within 0.5σ) and w \= −1 are inherited; no new fitted parameter is introduced; (***A***, ***Q***, dim Z) \= (35/437, 11, 2\) remain LOCKED.

**Results architecture (what is closed, and what is a research programme)**

For the external reader, the load-bearing claims and their exact status at a glance:

| Result | Exact content | Status |
| ----- | ----- | ----- |
| P1 | finite face-register jump-only GKLS lift (both pictures; Φ\_0 \= id) | PROVEN |
| P1-core | modular eigen-partial-isometries v\_ab in the Type II₁ continuous core | OPEN |
| P2 | general N-face population/coherence multiset spectrum (closed form) | PROVEN |
| R2a | oriented seam transport realizes ρ\_K (ℓ\_K \= |ρ\_K|, signed via axis) | PROVEN |
| R2b | physical A\_Z ∼ A\_K (transport → closed-loop holonomy) | OPEN |
| Entropy budget | causal-Z measure normalizable under a bounded screen (no MLSI) | DERIVED |
| Gate E | bulk–boundary production-rate capacity bound | HYPOTHESIS-strong |
| C\_int | i-tetration / modular clock spectral matching | OPEN |
| Gcoin | present coincidence Ω\_Λ(T\*) \= 83/121 after clock map, B3, Gate E | DERIVED-COND. / TESTABLE |

The first column of PROVEN results (P1, P2, R2a) is the mathematical core of this paper; the OPEN/HYPOTHESIS-strong rows are a delineated research programme (each a separate-paper-scale problem), not gaps in the proved results. This is the final internal version: the OPEN items (R2b, P1-core, C\_int, B3, Gate E) are deferred to ZS-F32 / ZS-A31 rather than pursued here.

**Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| PROVEN | Complete proof under declared definitions; verified symbolically or to high precision. |
| IMPORTED-PROVEN | Theorem from the external peer-reviewed literature, imported with citation. |
| DERIVED | Valid deduction from PROVEN inputs plus Z-Spin axioms; zero fitted parameters. |
| DERIVED-CONDITIONAL | Valid deduction conditional on explicitly stated upstream condition(s). |
| DERIVED-interpretation | Structural synthesis of PROVEN/DERIVED components; the synthesis is new, the components are not; NOT a theorem. |
| CONSTRUCTION | An explicit object is built and its stated properties are machine-verified on a finite register. |
| HYPOTHESIS-strong | Multiple independent anchors; one identified step missing; explicit promotion path. |
| TESTABLE | A sharply defined, pre-registered numerical or observational check not yet run/closed. |
| LOCKED | Core constant fixed upstream; not adjustable downstream. |
| CLOSED-NEGATIVE | A candidate route proved impossible within the framework (a no-go). |
| OPEN | Recognized gap requiring future work; upgrade path specified where possible. |
| RETRACTED | A claim previously asserted that fails under scrutiny; the corrected statement is given. |
| NON-CLAIM | Explicitly not asserted; protective scope-marker. |

**§1. Corrections of record and scope (v1.2 → v1.3, with v1.4 final patches)**

v1.3 kept every correct result of v1.2 and made the changes below; v1.4 then applied four final patches (the seam sign and transport-vs-holonomy distinction, the Gate-E downgrade to HYPOTHESIS-strong, and the §2.5 carrier-label corrections), detailed in their sections and in the Version History. Each change strengthens rigor or value.

| v1.2 item | v1.3 status | reason / gain |
| ----- | ----- | ----- |
| generator written in Heisenberg picture; proof slips into v\_ab x v\_ab† | BOTH PICTURES stated | Schrödinger 𝓛★(ρ) \= Σ r\_ab(v\_ab ρ v\_ab† − ½{q\_b,ρ}) for state-level facts; Heisenberg 𝓛 \= 𝓛★† for unitality 𝓛(I)=0. Removes a presentational inconsistency external readers would flag. |
| ‘faces being central’ / q\_a central | CORRECTED to ‘in the modular centralizer’ | In a Type II₁ factor Z(M\_obs) \= ℂI, so 121 nontrivial orthogonal central projections cannot exist; the faces lie in the modular centralizer M\_ω. |
| P1 stated as one theorem | SPLIT: finite P1 (PROVEN/CONSTRUCTION) vs P1-core (DERIVED-CONDITIONAL) | τ(q\_a)=τ(q\_b) gives a partial isometry, but v\_ab lying in a modular spectral subspace is a separate condition (P1-core); the continuous-core embedding is conditional on it. |
| A/Q dephasing term in the generator | REMOVED (jump-only) | The jump dissipator alone damps coherences via −½(Γ\_c+Γ\_d) \< 0 for a connected graph; removing the term eliminates an unforced rate and makes the lift parameter-free (§4, §14). |
| R2: F14-ODE monodromy target | RETRACTED → Seam Transport (R2a PROVEN \+ R2b OPEN) | ZS-F14’s joint ODE is an (ε,θ) radial–angular system, not a linear support ODE; the proposed Y(θ) monodromy would be trivial. The seam half-transport from F30 proves the oriented transport coordinate ρ\_tr \= ρ\_K (R2a); the closed-loop holonomy is R2b (§5). |
| P1 verified on a 4-face toy | RAISED to the exact 121-face spectrum (Theorem P2) | Closed-form coherence eigenvalues give the full 14641-eigenvalue spectrum; verified against the dense superoperator up to dimension 121 (§4). |
| §9.2 normalizability via spectral-gap decay ansatz | REPLACED by an entropy-budget bound | ∫σ\_Z \= D(ρ\_0‖ρ\*) − D(ρ\_∞‖ρ\*) ≤ D(ρ\_0‖ρ\*) needs no MLSI; the spectral gap survives only as an optional tail corollary (§10). |
| Gate E as an exact equality | RECAST as a data-processing INEQUALITY | LHS is coarse-grained astrophysical entropy, RHS register entropy production; a CPTP coarse-graining channel gives V\_c ṡ\_bulk ≤ N\_pix σ\_Z, with equality \= saturation (OPEN) (§9). |
| coincidence gate as one independent TESTABLE gate | DERIVED-CONDITIONAL with an explicit dependency tree | Ω\_Λ(T) needs the density ratio (B3) and the clock map t=t(T); the test depends on (C\_int, B3, Gate E). Stated as a tree, not hidden (§11). |
| §11 master action compressed to one line | RESTORED carrier action \+ full field equations | S\_carrier \= S\_S14^tetrad \+ S\_BK \+ S\_Λ with the Euler–Lagrange system (§2.5, §12) — integrative content preserved without restoring any wrong closure. |
| Theorem P1 (genuine GKLS, Φ\_0 \= id) | KEPT, in both pictures | The correct v1.2 core, retained and extended by P2. |
| Diagonal-in-Centralizer Lemma (PROVEN) | UNCHANGED | Underwrites modular covariance of 𝓛★; the one structural result standing across all versions. |

**§2. Locked inputs and the imported carrier**

Nothing here is fitted. (***A***, ***Q***, (Z,X,Y)) \= (35/437, 11, (2,3,6)) are LOCKED (ZS-F2, ZS-F5); κ² \= ***A***/***Q*** \= 35/4807 (ZS-M6); the i-tetration fixed point is z\* \= 0.43828 \+ 0.36059 i with |z\*| \= 0.5675551633 and α\_BK \= −ln|z\*| \= 0.5664173303 (ZS-M1/M4, corrected digits). The spacetime metric is an **imported carrier**: ZS-A17 Theorem F (Spin–Metric Independence, CLOSED-NEGATIVE) proves the 3-metric is not reconstructible from ***A*** or the spin structure. The Z-sector supplies the causal cone (ZS-F30: det X \= Minkowski, ρ \= artanh β, the SL(2,ℂ) identity component), the pressureless matter frame and relational clock (ZS-A19/A20 Brown dust, w \= 0), and the top-form vacuum (ZS-A28/A30, w \= −1). The occupation is the unital-primitive doubled attractor I\_121/121 with rank fractions (6, 32, 83)/121 (ZS-A30) — a *rank* fact, distinct from any present-epoch energy statement.

**§2.5. Restored carrier action and the carrier-sector Euler–Lagrange equations**

This section restores the integrative content compressed in v1.2 §11, **without** restoring any retracted closure. The carrier action assembles the imported metric sector, the Z-Spin gauge/holonomy sector, and the top-form vacuum:

*S\_carrier \= S\_{S14}^{tetrad} \+ S\_{BK} \+ S\_Λ ,*

with a precise division of labour: S\_{S14}^{tetrad} carries the SM gauge fields B, W, G, the Z-Spin field H₅, and the nonminimal scalar prefactor F \= M\_P²(1 \+ ***A*** |H₅|²) (ZS-S14); S\_{BK} is the Brown–Kuchař DUST sector (clock fields T, X^I, four-velocity U^μ, density ρ\_d), which supplies the relational clock and pressureless matter frame (ZS-A19/A20) and is NOT a Brans–Dicke sector; and S\_Λ is the top-form vacuum built from a 3-form potential A₃ with field strength F₄ \= dA₃, S\_Λ \= −(1/(2·4\!)) ∫ d⁴x √(−g) τ\_121(P\_Λ F\_{μνρσ} F^{μνρσ}) (ZS-A28). Varying the independent fields gives the load-bearing carrier-sector equations:

| Variation | Euler–Lagrange equation |
| ----- | ----- |
| δA₃  (top-form flux) | d(P\_Λ ⋆ F₄) \= 0  — the 4-form field strength is covariantly constant, fixing a constant vacuum energy ρ\_Λ and the equation of state w \= −1. |
| δρ\_d  (dust frame) | U^μ U\_μ \= −1  — the Brown-dust four-velocity is unit timelike (the relational clock frame, ZS-A19/A20). |
| δg^{μν}  (metric) | F·G\_{μν} \= T\_{μν}^{SM} \+ ρ\_m U\_μ U\_ν − ρ\_Λ g\_{μν} \+ ∇\_μ∇\_ν F − g\_{μν} □F  — Einstein equations with an SM stress tensor, pressureless dust, a cosmological-constant term, and the scalar-field (improvement) terms of the F sector. |

This is exactly the structure in which ZS-F30’s causal cone (through T\_{μν}^{SM} and the tetrad) and ZS-A30’s occupation (through ρ\_Λ and ρ\_m) meet in one action. The reduction to ZS-S14 is the limit Σ\_Z \= A₃ \= ϱ̂ \= λ\_R \= Λ\_C \= 0 with the present coupling 𝓘 removed, **keeping** B, W, G (§15). \[§2.5: carrier action and field equations **IMPORTED-PROVEN / DERIVED** from ZS-S14/A19/A20/A28; no new fitted parameter.\]

**§3. The genuine modular GKLS population lift, in both pictures (Theorem P1)**

**§3.1 Data, balanced rates, and the modular centralizer**

Let (M\_obs, τ) be the Type II₁ observer corner with 121 face projections q\_a, q\_a q\_b \= δ\_{ab} q\_a, Σ\_a q\_a \= I, τ(q\_a) \= 1/121, and balanced ZS-A30 rates r\_{ab} ≥ 0 (a ≠ b), Σ\_a r\_{ab} \= Σ\_a r\_{ba}. By the Diagonal-in-Centralizer Lemma (PROVEN, unchanged), the diagonal algebra D\_121 lies in the modular **centralizer** M\_ω — the fixed-point algebra of the modular flow — *not* in the center Z(M\_obs) \= ℂI (a Type II₁ factor has trivial center, so 121 nontrivial orthogonal central projections cannot exist; this corrects the loose word ‘central’ in v1.2).

**§3.2 The two pictures**

On states ρ (Schrödinger picture) and on observables x (Heisenberg picture, the adjoint) the jump-only generators are

*𝓛★(ρ) \= Σ\_{a≠b} r\_{ab} ( v\_{ab} ρ v\_{ab}† − ½{q\_b, ρ} ) ,*

*𝓛(x) \= 𝓛★†(x) \= Σ\_{a≠b} r\_{ab} ( v\_{ab}† x v\_{ab} − ½{q\_b, x} ) ,*

with jumps √r\_{ab} v\_{ab}, v\_{ab}†v\_{ab} \= q\_b, v\_{ab}v\_{ab}† \= q\_a. We use 𝓛★ for state-level statements (trace preservation, intertwining, stationarity, coherence damping) and 𝓛 for unitality, and we separate the dual identities Tr 𝓛★(ρ) \= 0 and 𝓛(I) \= 0\.

**§3.3 Theorem P1 and the finite/continuous status split**

Theorem P1 (Genuine Population Lift). The semigroup Φ\_t \= e^{t𝓛★} has all five properties, machine-verified on a finite register:

| Property | Statement / mechanism |
| ----- | ----- |
| (1) Φ\_0 \= id | e^{0·𝓛★} \= id — the property the retracted v1.1 family ι∘Φ\_t∘E lacked (it had Ψ\_0 \= E\_D ≠ id). |
| (2) CP semigroup | 𝓛★ is in GKLS form, so {Φ\_t} is a normal completely positive semigroup (Lindblad; GKS). |
| (3) trace preservation | Tr 𝓛★(ρ) \= 0 (Schrödinger) ⇔ 𝓛(I) \= Σ r\_{ab}(q\_b − q\_b) \= 0 (Heisenberg unitality). |
| (4) modular covariance | \[𝓛★, σ\_s^ω\] \= 0, since the v\_{ab} are modular eigen-operators (D\_121 ⊆ M\_ω). |
| (5) population intertwining | E\_D 𝓛★ \= 𝓛\_{π} E\_D and E\_D 𝓛★(1 − E\_D) \= 0: off-diagonals do not feed populations; the diagonal restriction is the classical chain 𝓛\_π. |
| uniqueness | For a strongly connected rate graph the kernel of 𝓛★ is one-dimensional, so the tracial state τ\_121 is the unique stationary state. |

Status split (correcting v1.2’s single statement): on the finite face register the generator is built explicitly and all five properties plus uniqueness are **machine-verified** (Appendix A), so finite P1 is **PROVEN / CONSTRUCTION**. The continuous-core embedding requires modular eigen-partial-isometries v\_{ab} living in the right modular spectral subspace; τ(q\_a) \= τ(q\_b) gives *some* partial isometry with v\_{ab}†v\_{ab} \= q\_b, v\_{ab}v\_{ab}† \= q\_a, but its membership in M\_obs(ω\_{ab}) is a separate condition, recorded as the gate

*P1-core:   ∃ v\_{ab} ∈ M\_obs(ω\_{ab})  with  v\_{ab}† v\_{ab} \= q\_b ,  v\_{ab} v\_{ab}† \= q\_a .*

So the Type II₁ core embedding is **DERIVED-CONDITIONAL on P1-core** (OPEN). The cosmological observable Ω\_Λ is a population fact, so the population lift suffices for the budget; the full coherence-resolved lift of ZS-A24’s family 𝓛\_(s) is broader and remains a NON-CLAIM here.

**§4. The exact 121-face Lindblad spectrum (Theorem P2)**

This is the first of the three value-raising results. With the dephasing term removed, the generator is block-diagonal between populations and coherences, and the coherence block is diagonal in the matrix-unit basis.

**§4.1 The closed-form coherence eigenvalues**

For an off-diagonal matrix unit |c⟩⟨d| (c ≠ d), the gain term v\_{ab}|c⟩⟨d|v\_{ab}† \= δ\_{bc}δ\_{bd}|a⟩⟨a| vanishes, and only the anticommutator survives:

*𝓛★(|c⟩⟨d|) \= −½(Γ\_c \+ Γ\_d) |c⟩⟨d| ,    Γ\_c \= Σ\_{a≠c} r\_{ac}  (the total out-rate from face c) .*

Each coherence is therefore an exact eigenvector with eigenvalue −½(Γ\_c \+ Γ\_d) \< 0 for a connected graph — which is precisely why no separate dephasing term is needed (it would only add a constant −γ to every coherence eigenvalue without changing the population block). On the diagonal, 𝓛★ restricts to the classical population generator 𝓛\_π.

**§4.2 Theorem P2 (Full Face Spectrum)**

Theorem P2. For the jump-only modular GKLS generator on N equal-trace faces with balanced symmetric rates,

*Spec(𝓛★) \= Spec(𝓛\_π)  ⊎  { −½(Γ\_c \+ Γ\_d) : c ≠ d } ,*

a multiset union associated with two invariant blocks (numerical coincidences between population and coherence eigenvalues are allowed): N population eigenvalues (one zero mode, the rest negative — the uniform tracial stationary state and its gap) and N(N−1) explicit coherence eigenvalues. For the 121-face register this is

*121 population  \+  121·120 coherence  \=  121 \+ 14520  \=  14641  \=  121²  eigenvalues, in closed form .*

Status and novelty. The theorem is proved algebraically for arbitrary N; numerical regression against the dense superoperator is performed for N \= 4, 8, 11 (the last at dimension 11² \= 121), and the N \= 121 specialization follows analytically from the theorem and the inherited ZS-A30 rate structure (under the doubled-additive 𝓛\_121 \= 𝓛\_11 ⊗ id \+ id ⊗ 𝓛\_11, the 121 population eigenvalues are the pairwise sums λ\_i \+ λ\_j). The relation to ZS-A30 is one of abstraction, not duplication: ZS-A30 v1.6 computed the spectrum for the specific Z-Spin mediator graph (degree-(2,9), with population/coherence multiplicities (1, 80, 36, 3, 1)); ZS-F31 abstracts that calculation into a general N-face jump-GKLS block-spectrum theorem and isolates the population/coherence decomposition independently of the graph-specific multiplicities. \[§4: **PROVEN** (algebraic for arbitrary N; regression to dimension 121). The general theorem is of more direct mathematical value to external readers than the graph-specific computation.\]

**§5. The seam-support connection: Seam Transport Theorem (R2a, R2b)**

**§5.1 Why the v1.2 F14-monodromy route is retracted**

v1.2 proposed computing the monodromy of a fundamental matrix Y(θ) \= \[\[h\_1, h\_2\],\[h\_1′, h\_2′\]\] built from two ‘support solutions’ of the ZS-F14 joint ODE. This does not match the corpus: ZS-F14’s joint ODE is an *(ε, θ) radial–angular* system (radial Lyapunov decay; angular Goldstone accumulation; the conservation Q \= a³ ε² θ̇ \= ***A***; a centrifugal boundary), not a linear support ODE with two independent periodic solutions. Moreover, if h\_1, h\_2 were ordinary 2π-periodic support functions, Y(θ+2π) \= Y(θ) would give trivial loop monodromy and no rapidity. We therefore RETRACT the F14-monodromy route.

**§5.2 The exact seam half-transport: a Cartan realization (R2a, PROVEN)**

ZS-F30 already supplies the object we need: the Steiner-centered support-ratio rapidity ρ\_K(θ) and the SL(2,ℂ) element

*g\_K(θ) \= exp\[ ½ ρ\_K(θ) n·σ \] ,    A\_K \= g\_K⁻¹ dg\_K   (an sl(2,ℂ)-valued pure-gauge Cartan boost connection, fixed axis n(θ+π)=n(θ)) ,*

together with the seam antisymmetry ρ\_K(θ+π) \= −ρ\_K(θ) (the half-turn sign flip of F30). Hence g\_K(θ+π) \= g\_K(θ)⁻¹, and the seam half-transport is

*U\_K(θ+π, θ) \= g\_K(θ+π)⁻¹ g\_K(θ) \= g\_K(θ)·g\_K(θ) \= g\_K(θ)² \= exp\[ ρ\_K(θ) n·σ \] .*

Since (n·σ)² \= I, exp\[ρ\_K n·σ\] is a Hermitian positive-definite boost with eigenvalues e^{±ρ\_K}; its singular values are therefore {e^{|ρ\_K|}, e^{−|ρ\_K|}}, so the singular-value ratio yields the UNSIGNED Cartan length

*ℓ\_K \= ½ ln( s\_max / s\_min ) \= |ρ\_K|   (sign-independent) .*

The signed, seam-odd rapidity is not visible in the singular values; it is recovered from the oriented logarithmic generator (log U\_K \= ρ\_K n·σ):

*ρ\_K \= ½ Tr\[ (n·σ) log U\_K \]     (since ½ Tr\[(n·σ)²\] \= 1\) .*

Together these give a complete Cartan decomposition — magnitude ℓ\_K \= |ρ\_K| from the singular values, orientation/sign from the axis projection — verified to machine precision for BOTH signs of ρ\_K (Appendix C). This corrects a sign slip in v1.3, which read the ratio as ρ\_K rather than |ρ\_K| and tested only positive ρ\_K. The result is the oriented transport coordinate

*ρ\_tr^{oriented} \= ρ\_K     (for the canonical support-defined seam transport) .*

Crucially this is an open-path TRANSPORT statement, not a closed-loop holonomy: U\_K(θ+π, θ) is parallel transport over the half-turn, and the singular values of an open transport are not gauge-invariant under independent endpoint gauge transformations. So R2a is a canonical seam-TRANSPORT realization theorem, not a physical-holonomy theorem; the promotion ρ\_tr → ρ\_hol^{physical} requires the gauge equivalence A\_Z ∼ A\_K (R2b, §5.3). \[§5.2: **PROVEN** as a seam-transport realization (R2a); holonomy promotion is R2b, OPEN.\]

**§5.3 What remains: physical identification (R2b, OPEN)**

R2a fixes the geometry: the seam transport of the F30 connection A\_K has boost coordinate exactly ρ\_K. What is *not* yet proved is that the physical Z-sector connection A\_Z appearing in the master action is gauge-equivalent to A\_K (so that its holonomy is the same object). That is the single remaining gate:

*R2b:   A\_Z  ∼  A\_K   (gauge equivalence of the physical and the Steiner-support connections) .*

\[§5.3: R2b **OPEN**. Net: the support–connection gate is now R2a (PROVEN) \+ R2b (OPEN), replacing v1.2’s R1+R2, with the geometric content actually closed.\]

**§6. Clock alignment: Koenigs linearization and the spectral-matching gate**

The i-tetration f(z) \= i^z has the attracting fixed point z\* with multiplier λ\* \= f′(z\*) \= (iπ/2) z\*, |λ\*| \= (π/2)|z\*| \= 0.89151 \< 1\. By Koenigs’ theorem there is an analytic χ near z\* with χ∘f \= λ\*·χ, so the iteration is locally a dilation by λ\* — a rigorous statement replacing v1.1’s shortcut (PROVEN). Identifying one i-tetration step with one modular step of a Z-sector eigenoperator (eigenvalue e^{−sω\_Z \+ isν\_Z}) requires a single δs, i.e. the Intertwiner Condition

*C\_int:    −ln|λ\*| / ω\_Z \= arg λ\* / ν\_Z ,    −ln|λ\*| \= 0.1148346 ,   arg λ\* \= 2.2592496 .*

Honest note (clarifying ZS-M4): the per-step contraction −ln|λ\*| \= 0.1148346 is **distinct** from α\_BK \= −ln|z\*| \= 0.5664173 (a fixed-point modulus) — different objects, so α\_BK is not the matching rapidity. C\_int is a concrete equality once the modular spectrum (ω\_Z, ν\_Z) is computed; that computation is not done here. \[§6: Koenigs **PROVEN**; C\_int **OPEN**; on success clock alignment **DERIVED-CONDITIONAL**.\]

**§7. Causal-diamond geometry (the Z-screen as a candidate carrier)**

In flat FRW, a causal diamond of conformal extent \[η\_i, η\_f\] has comoving radius r\_D(η) \= min{η − η\_i, η\_f − η}, a 2D maximal screen Σ\_D(η) \= S²\_{r\_D(η)} of physical area A\_D(η) \= 4π a²(η) r\_D²(η), and comoving volume V\_c(η) \= (4π/3) r\_D³(η). Bousso’s causal-entropy construction computes ΔS\_CD \= ∫ dt V\_c ṡ\_bulk; the comoving volume vanishes early and in the far future, and the overlap of volume with the entropy-production peak selects a preferred range for the cosmological constant. Scope, stated carefully: only the maximal *two-dimensional* screen cross-section is dimensionally comparable to the Z-sector’s 2D object, and in Bousso’s calculation the dominant entropy source is astrophysical. Hence the causal-diamond 2D screen is a **candidate** geometric carrier for the Z-sector, and the identity between Bousso’s causal entropy and the Z-Spin entropy of §8 is **OPEN**. \[§7: causal-diamond geometry **IMPORTED-PROVEN**; Z-screen identification **HYPOTHESIS-strong**.\]

**§8. Z-Spin entropy production**

Because Theorem P1 provides a *genuine* QMS with a faithful stationary state ϱ\* \= I\_121/121, the Spohn entropy production is well-defined and non-negative:

*σ\_Z(T) \= − d/dT D( ϱ\_T ‖ ϱ\* ) \= − τ\_121\[ 𝓛★(ϱ\_T)( ln ϱ\_T − ln ϱ\* ) \] ≥ 0   (Spohn) .*

The population current J\_{ab}(T) \= r\_{ab} p\_b − r\_{ba} p\_a vanishes in de Sitter equilibrium (σ\_Z \= 0\) and is nonzero only when matter-mediated transfer drives the populations off equilibrium. Thus ‘matter-correlated’ is realized as the **existence of a nonzero information current**, not as a fitted exponent. \[§8: Spohn positivity **IMPORTED-PROVEN**; current representation **DERIVED** from Theorem P1.\]

**§9. The bulk–boundary gate as a capacity bound (Gate E, HYPOTHESIS-strong)**

Introduce a CPTP coarse-graining channel 𝒩: Z → X from the fine Z-register to the coarse astrophysical description. Monotonicity of relative entropy under 𝒩 (the data-processing inequality) gives the VALUE inequality D(ρ\_Z ‖ ρ\_Z\*) ≥ D(𝒩ρ\_Z ‖ 𝒩ρ\_Z\*) at each time. The intended bulk–boundary production-rate bound is the entropy-production *capacity bound*:

*Gate E (target bound):    V\_c(T) ṡ\_bulk(T)  ≤?  N\_pix(T) σ\_Z(T) ,    N\_pix(T) \= A\_D(T)/(4ℓ\_P²)     \[HYPOTHESIS-strong\] .*

Honest status: data processing motivates this bound but does NOT by itself prove it. The DPI is a VALUE inequality D\_Z(T) ≥ D\_X(T); the production rates are σ \= −dD/dT, and value ordering does not imply derivative ordering (e.g. e^{−T} ≥ e^{−2T} for all T, yet at T \= 0 the decay rate of the smaller function is larger). The Lindblad/Spohn theorems give complete positivity and entropy-production positivity, but not a pointwise production-rate inequality between distinct fine and coarse dynamics. Closing it needs a generator-level intertwining 𝒩 Φ\_t^Z \= Φ\_t^X 𝒩, or a strong data-processing / entropy-contraction inequality, or a directly computed channel-capacity bound. \[§9: Gate E is **HYPOTHESIS-strong** (not DERIVED-CONDITIONAL); to be promoted only after such a generator-level theorem is established. It is already listed OPEN in the registry.\]

**§10. The causal-Z present measure and the entropy-budget normalizability theorem**

**§10.1 The measure**

*dμ\_ZCD(T) \= W\_Z(T) dT / ∫ dT′ W\_Z(T′) ,    W\_Z(T) \= N\_pix(T) σ\_Z(T) \= ( A\_D(T)/4ℓ\_P² ) σ\_Z(T) ,*

with no observer-count or anthropic parameter; 83/121 does not appear in W\_Z.

**§10.2 Normalizability by entropy budget (DERIVED, no MLSI)**

This is the second value-raising result: a clean proof that needs no modified log-Sobolev inequality and no spectral-gap decay ansatz. From the Spohn definition σ\_Z \= −d/dT D(ϱ\_T ‖ ϱ\*), the production integral telescopes:

*∫₀^∞ σ\_Z(T) dT \= D(ϱ\_0 ‖ ϱ\*) − D(ϱ\_∞ ‖ ϱ\*) ≤ D(ϱ\_0 ‖ ϱ\*) \< ∞ .*

With the causal screen bounded, N\_pix(T) ≤ N\_max, the measure integral is finite:

*∫₀^∞ W\_Z(T) dT \= ∫₀^∞ N\_pix(T) σ\_Z(T) dT ≤ N\_max · D(ϱ\_0 ‖ ϱ\*) \< ∞ .*

The relative entropy is monotone non-increasing under any QMS (Lindblad), so the bound holds for a genuine QMS and a bounded screen *alone*. The spectral gap Δ \= 2***A***/***Q*** survives only as an optional tail-rate corollary (∫₀^∞ e^{−2ΔT} dT \= 1/(2Δ)), not as a hypothesis. This strengthens v1.1’s proper-time exclusion into a usable, provably normalizable replacement. For the finite 121-register ϱ\* \= I/121 is faithful, so D(ϱ\_0‖ϱ\*) is finite; the only remaining condition is boundedness of the causal screen, natural for an asymptotic de Sitter causal diamond with positive Λ. \[§10.2: **DERIVED** under N\_pix(T) ≤ N\_max and finite D(ϱ\_0‖ϱ\*).\]

**§10.3 The present equation**

*T\* \= argmax\_T W\_Z(T) ,    d/dT ln A\_D(T) |\_{T\*} \= − d/dT ln σ\_Z(T) |\_{T\*} :*

the present is where the growing causal screen balances the decaying information production.

**§11. The coincidence closure gate and its dependency tree (DERIVED-CONDITIONAL)**

The methodological pivot stands — 83/121 must not enter W\_Z — but the test is not unconditional, and v1.3 states its dependencies explicitly rather than hiding them. To evaluate Ω\_Λ(T) one needs the density ratio ρ\_Λ/ρ\_{m,0} (inserting 83/38 would be circular; inserting the observed value would not be a prediction), which requires the absolute vacuum scale B3 (OPEN). One also needs the clock map t \= t(T) relating cosmic/conformal time to the Brown register clock, which is logically prior to A\_D(T). The dependency tree is

*C\_int ⟶ A\_D(T) ;    (B3 or independent density ratio) ⟶ Ω\_Λ(T) ;    (C\_int, B3, Gate E) ⟶ G\_coincidence .*

*G\_coincidence \= Ω\_Λ(T\*) − 83/121 ,    closure:  |G\_coincidence| \< 10⁻³  and  d²/dT² ln W\_Z(T)|\_{T\*} \< 0 .*

The tolerance is pre-registered before computation. Therefore G is **DERIVED-CONDITIONAL** on (C\_int, B3, Gate E), TESTABLE on success — not the single independent gate v1.2 implied. \[§11: **DERIVED-CONDITIONAL / TESTABLE**.\]

**§11.1 A future direction: the scale–present coupled variational problem (F32)**

A more aggressive route would make the top-form flux f\_Λ a variational target alongside T, maximising W\_Z(T; f\_Λ) jointly:

*(T\*, f\_Λ\*) \= argmax\_{T, f\_Λ} W\_Z(T; f\_Λ) ,    then compute  ρ\_Λ(f\_Λ\*),  Ω\_Λ(T\*, f\_Λ\*)  together ,*

unifying present selection and B3 scale selection into one scale–present coupled variational problem. If successful it would attack the largest OPEN of ZS-A26–A30. We flag this as a separate future programme (ZS-F32 / ZS-A31), not a claim of this paper. \[§11.1: **OPEN** (future programme).\]

**§12. The revised master effective action**

***Γ**\_CR^{(1.3)} \= S\_carrier \+ S\_Z^{flat} \+ S\_QMS^{jump} \+ S\_R^{seam} \+ S\_C^{Koenigs} \+ 𝓘\_ZCD ,*

*S\_carrier \= S\_{S14}^{tetrad} \+ S\_{BK} \+ S\_Λ  (§2.5) ,    S\_QMS^{jump} ↔ 𝓛★ (Theorems P1, P2) ,*

*S\_R^{seam} ↔ A\_K, ρ\_tr^{oriented} \= ρ\_K (Theorem R2a; ℓ\_K \= |ρ\_K|) ,    𝓘\_ZCD\[T\] \= − ln\[ ( A\_D(T)/4ℓ\_P² ) σ\_Z(T) \] .*

The relative entropy D(ϱ\_T ‖ ϱ\*) is a QMS Lyapunov functional, disjoint from any present-selection role:

| Object | Role |
| ----- | ----- |
| D(ϱ\_T ‖ ϱ\*) | Lyapunov functional measuring approach to equilibrium (NOT a present selector). |
| σ\_Z \= − d/dT D | irreversible information flow (Spohn entropy production); its integral is the entropy budget (§10.2). |
| A\_D(T) σ\_Z(T) | present weight including causal accessibility (the screen the observer can resolve). |
| 83/121 | independent rank target, checked at T\* by the coincidence gate (§11). |

**§13. Discussion — the Z-Spin mediation structure and realisation C14**

The mediator+pair reading remains attractive: the three on-shell conditions are the boost coordinate (R), the generator (C), and the fixed state (P) of one de Sitter modular flow, with R the Z-Spin hinge of the complex rapidity ζ \= ρ\_K \+ iφ. But two operator identities it needs are not proved, so it is interpretation, not theorem.

| Needed identity | Why it is not yet a theorem |
| ----- | ----- |
| φ (spatial rotation) \= Euclidean modular time | In ZS-F30 φ is a compact spatial rotation parameter; the operator identity e^{iφJ} \= e^{−τ\_E H\_mod} (φ \= Hτ\_E) is not established. |
| modular conjugation \= corpus seam | Bisognano–Wichmann gives J \= Θ·U(R\_W(π)) — anti-unitary CPT Θ times a rotation, not U(R\_W(π)) alone (correcting v1.1’s phrasing). Identifying J with the seam V\_ZY \= (V\_XZ)\* needs a separate intertwining theorem. |

Accordingly C14 is recorded as a **DERIVED-interpretation**, to be promoted only after both identities are proved. \[§13: **DERIVED-interpretation**.\]

**§14. Zero-fitted-parameter and anti-numerology audit**

Every dimensionless quantity descends from (***A***, ***Q***, dim Z) \= (35/437, 11, 2). v1.3 is **strictly stronger** than v1.2 here: removing the A/Q dephasing term means the generator’s only inputs are the ZS-A30 rates r\_{ab}, with no separately chosen coherence rate. The causal-Z measure contains no observer-count or anthropic exponent (matter-correlation is the nonzero current J\_{ab}); the coincidence tolerance |G| \< 10⁻³ is pre-registered. The only remaining free input is N\_eff in the multinomial variance, which does not affect the mean 83/121; the absolute scale (H₀, ρ\_Λ) is an integration constant left OPEN (B3). If, in future, a dephasing term were reintroduced for physical reasons, its rate would have to be declared as a separate **Minimal-Rate Identification** γ \= ***A***/***Q*** — but v1.3 does not need it. The budget vs Planck 2018:

| Quantity | Rank fraction | Planck 2018 | deviation |
| ----- | ----- | ----- | ----- |
| Ω\_b | 6/121 \= 0.0496 | 0.0493 ± 0.0006 | 0.48σ |
| Ω\_cdm | 32/121 \= 0.2645 | 0.2645 ± 0.0050 | 0.01σ |
| Ω\_Λ | 83/121 \= 0.6860 | 0.6847 ± 0.0073 | 0.17σ |

Correct statement: Ω\_Λ within 0.2σ; all three fractions within 0.5σ. The relative-entropy minimum of D(x ‖ 83/121) at 83/121 confirms (does not predict) the equilibrium — which is why §10–§11 use the independent causal measure. The multinomial 83/121 is the mean; the mode is 83/121 \+ O(N\_eff⁻¹).

**§15. Cross-paper dependency and version-conflict check**

| Upstream result | Use here | Conflict check |
| ----- | ----- | ----- |
| ZS-A24 F-A24.9 (OPEN) | population sector closed by P1; full spectrum by P2 | Advances A24; every A24 theorem used unchanged; II₁-core no-go respected. |
| ZS-A24 Diagonal-in-Centralizer | modular covariance of 𝓛★ (§3) | Used; PROVEN; ‘centralizer’ usage corrected (not ‘center’). |
| ZS-A30 doubled generator 𝓛\_11⊗id+id⊗𝓛\_11 | 121 population eigenvalues \= pairwise sums (§4) | Used; consistent with A30 doubled-additive structure. |
| ZS-A30 budget (6,38,83)/121 | independent rank target (§11) | Inherited; used as target outside the measure (anti-circularity). |
| ZS-M4 α\_BK \= −ln|z\*| | clarified vs Koenigs λ\* (§6) | No conflict: α\_BK and λ\* \= f′(z\*) are different objects. |
| ZS-F30 ρ\_K(θ), g\_K, seam ρ\_K(θ+π)=−ρ\_K(θ) | Seam Transport Theorem (§5) | Uses F30’s own objects; corrects/strengthens the holonomy claim; F14-route retracted. |
| ZS-F14 (ε,θ) joint ODE | identified as NOT the support-monodromy route | Conflict in v1.2 removed: F14 is radial–angular, not a linear support ODE. |
| ZS-S14 master action | S\_carrier (tetrad form, §2.5) | Strict extension; reduction keeps B, W, G. |
| ZS-A17 metric No-Go | metric imported (§2) | Respected — no metric emergence claimed. |
| ZS-A19/A20 Brown dust; ZS-A28 top-form | matter frame, clock, vacuum (§2.5) | Used at DERIVED; field equations restored. |

**§16. Falsification gates**

| Gate | Layer | Trigger |
| ----- | ----- | ----- |
| F-F31.1 | Mathematical (verified) | If the jump-only generator failed Φ\_0 \= id, complete positivity, trace preservation, the intertwining E\_D 𝓛★ \= 𝓛\_π E\_D, or uniqueness of the tracial stationary state, Theorem P1 fails. (Machine-verified; Appendix A.) |
| F-F31.2 | Mathematical (verified) | If Spec(𝓛★) ≠ Spec(𝓛\_π) ⊎ {−½(Γ\_c+Γ\_d)} (e.g. some coherence is not an eigenvector), Theorem P2 fails. (Verified to dimension 121; Appendix B.) |
| F-F31.3 | Mathematical (verified) | If U\_K(θ+π,θ) ≠ g\_K² or its singular values ≠ e^{±ρ\_K}, the Seam Transport Theorem R2a fails. (Verified; Appendix C.) |
| F-F31.4 | Theoretical (OPEN target) | If the physical connection A\_Z is not gauge-equivalent to A\_K, R2b fails and the transport coordinate ρ\_tr \= ρ\_K does not promote to the physical closed-loop holonomy. |
| F-F31.5 | Theoretical (OPEN target) | If no modular eigen-partial-isometries v\_{ab} exist in the Type II₁ core (P1-core), the continuous-core embedding fails; if the modular spectrum gives −ln|λ\*|/ω\_Z ≠ arg λ\*/ν\_Z, C\_int fails. |
| F-F31.6 | Theoretical | If the causal-Z measure were not normalizable — i.e. if D(ϱ\_0‖ϱ\*) diverged or N\_pix were unbounded — §10.2 fails. (The entropy budget makes this sharp.) |
| F-F31.7 | Observational (terminal) | If, after fixing the clock map and B3, T\* \= argmax W\_Z gave Ω\_Λ(T\*) outside the pre-registered |G| \< 10⁻³, the causal-entropic resolution is rejected; or if precision cosmology drove Ω\_Λ,0 far from 0.686 or established w ≠ −1, the inherited budget is rejected. |
| F-F31.8 | Anti-circularity | If 83/121 (or the rank budget) were found to have entered W\_Z, the coincidence test is void. |
| F-F31.9 | Anti-overclaim | If this paper is read as solving the coincidence problem (a DERIVED-CONDITIONAL gate), as closing R2b/C\_int/Gate E (OPEN), as the full coherence-resolved lift (only the population sector is closed), or as deriving the metric (A17) or the absolute scale (B3), it is falsified by its own scope. |

**§17. Conclusion**

v1.3 turns one repaired theorem into three independent contributions and removes an unforced parameter, while restoring the integrative master-action content. First, the jump-only modular GKLS generator yields the exact 121-face Lindblad spectrum Spec(𝓛★) \= Spec(𝓛\_π) ⊎ {−½(Γ\_c+Γ\_d)} in closed form (Theorem P2), verified against the dense superoperator to dimension 121 — a genuine spectral theorem, not a toy check, and now strictly parameter-free since the dephasing term is gone. Second, the retracted F14-monodromy route is replaced by the exact seam half-transport U\_K \= g\_K² \= exp\[ρ\_K n·σ\] (Theorem R2a), whose singular-value Cartan length is ℓ\_K \= |ρ\_K| and whose signed oriented rapidity ρ\_tr^{oriented} \= ρ\_K is recovered from the fixed axis; this is an open-path transport realization, not a closed-loop holonomy, so the promotion to a physical A\_Z holonomy (R2b) remains open. Third, the causal-information present measure is provably normalizable by an entropy budget, ∫ N\_pix σ\_Z ≤ N\_max D(ϱ\_0‖ϱ\*) \< ∞, with no MLSI — and the bulk–boundary relation is honestly only a HYPOTHESIS-strong capacity bound (data processing gives a value inequality, not a pointwise rate inequality), the coincidence test an explicitly conditional gate.

The honest terminus is a small, named set of computations and one measurement: R2b (gauge equivalence), P1-core (continuous-core isometries), C\_int (spectral matching), the clock map t \= t(T), Gate E saturation, and the coincidence test G — together with the standing OPENs (the full coherence-resolved lift, the absolute scale B3, the imported metric A17). Each is concrete. Relative to every previous version, v1.3 is both more rigorous (three proved theorems, one retraction, picture-clean, parameter-free generator) and more complete (the carrier action and field equations restored). Zero new fitted parameters; (***A***, ***Q***, dim Z) \= (35/437, 11, 2\) LOCKED.

**Acknowledgements & Code Availability**

This paper consolidates internal Z-Spin Collaboration deep-exploration notes and three rounds of adversarial review of ZS-F31. The companion script zs\_f31\_verify\_v1\_4.py reproduces the load-bearing checks: the corrected z\* digits and Planck deviations (Ω\_Λ 0.17σ, all three \< 0.5σ); the jump-only genuine GKLS lift in both pictures, with Φ\_0 \= id, complete positivity, trace preservation/unitality, modular covariance, the intertwining E\_D 𝓛★ \= 𝓛\_π E\_D, and a unique tracial stationary state; a regression check that the retracted v1.1 family has Ψ\_0 \= E\_D ≠ id; the full 121-face spectrum Spec(𝓛★) \= Spec(𝓛\_π) ⊎ {−½(Γ\_c+Γ\_d)} verified against the dense superoperator up to dimension 121 and exhibited in closed form at 14641; the sign-corrected Seam Transport (unsigned length ℓ\_K \= |ρ\_K| and signed recovery ρ\_K \= ½Tr\[(n·σ)logU\_K\], at BOTH signs); the Koenigs multiplier (with the honest note −ln|λ\*| ≠ α\_BK); the entropy-budget normalizability ∫₀^∞ σ\_Z \= D(ϱ\_0‖ϱ\*); and the Gate-E rationale check that value ordering does not imply rate ordering. The script prints an explicit OPEN registry (R2b, P1-core, C\_int, clock map, Z-screen, Gate E \[HYPOTHESIS-strong\], coincidence gate) that it does not count as PASS, so its summary reads ‘42/42 arithmetic, symbolic, and construction checks PASS; the operator gates above are not machine-verified.’ It contains no fail-open clause. This work used AI tools for verification and drafting; the author assumes full responsibility for all content.

**Appendix A. The jump-only GKLS generator in both pictures: the five-property proof**

Schrödinger 𝓛★(ρ) \= Σ\_{a≠b} r\_{ab}(v\_{ab} ρ v\_{ab}† − ½{q\_b, ρ}); Heisenberg 𝓛(x) \= 𝓛★†(x) \= Σ\_{a≠b} r\_{ab}(v\_{ab}† x v\_{ab} − ½{q\_b, x}); v\_{ab} \= |a⟩⟨b| on the faces, balanced symmetric rates r\_{ab} \= r\_{ba}.

(1) Φ\_0 \= e^{0·𝓛★} \= id. (2) 𝓛★ is in GKLS form (jumps √r\_{ab} v\_{ab}), so {Φ\_t} is a normal CP semigroup. (3) Tr 𝓛★(ρ) \= Σ r\_{ab}(Tr(v\_{ab}ρv\_{ab}†) − Tr(q\_b ρ)) \= Σ r\_{ab}(Tr(q\_b ρ) − Tr(q\_b ρ)) \= 0, equivalently 𝓛(I) \= Σ r\_{ab}(q\_b − q\_b) \= 0\. (4) σ\_s^ω(v\_{ab}) \= e^{isω\_{ab}} v\_{ab} (faces in the centralizer, ω\_{ab} \= ln(h\_a/h\_b)) gives σ\_s^ω 𝓛★ σ\_{−s}^ω \= 𝓛★ termwise, so \[𝓛★, σ\_s^ω\] \= 0\. (5) For c ≠ d, v\_{ab}|c⟩⟨d|v\_{ab}† \= δ\_{bc}δ\_{bd}|a⟩⟨a| \= 0, so the gain term annihilates coherences and E\_D 𝓛★(1 − E\_D) \= 0; on the diagonal 𝓛★ restricts to (𝓛\_π p)\_a \= Σ\_b(r\_{ab}p\_b − r\_{ba}p\_a), giving E\_D 𝓛★ \= 𝓛\_π E\_D. Uniqueness: for a strongly connected graph the only 𝓛★-harmonic elements are scalars, so τ\_121 is the unique stationary state. ∎

All of (1)–(5) and uniqueness are reproduced numerically on a 4-face register (Part B of the script), with the contrast that the v1.1 family ι∘Φ\_t∘E has Φ\_0 \= E\_D ≠ id.

**Appendix B. The full 121-face spectrum (Theorem P2): proof and verification**

Coherence block. For c ≠ d, the only surviving term of 𝓛★(|c⟩⟨d|) is −½ Σ\_{a≠b} r\_{ab}{q\_b, |c⟩⟨d|} \= −½(Σ\_{a≠c} r\_{ac} \+ Σ\_{a≠d} r\_{ad})|c⟩⟨d| \= −½(Γ\_c \+ Γ\_d)|c⟩⟨d|, with Γ\_c \= Σ\_{a≠c} r\_{ac} the out-rate from c. Thus every coherence is an eigenvector with eigenvalue −½(Γ\_c \+ Γ\_d). Population block. On the diagonal 𝓛★ \= 𝓛\_π, the classical generator with stationary uniform distribution and a spectral gap. Disjointness of the two invariant subspaces gives Spec(𝓛★) \= Spec(𝓛\_π) ⊎ {−½(Γ\_c \+ Γ\_d) : c ≠ d}. ∎

Verification. For N \= 4, 8, 11 the dense superoperator 𝓛★ (dimensions 16, 64, 121\) is diagonalised and its spectrum matches the predicted union to 10⁻⁸. For N \= 121 the spectrum is exhibited from the formula: 121 population eigenvalues (under the doubled-additive A30 structure, the pairwise sums λ\_i \+ λ\_j of the 11-face Laplacian, including one zero mode) and 14520 coherence eigenvalues −½(Γ\_c \+ Γ\_d), totalling 14641 \= 121² — without constructing the 14641² matrix.

**Appendix C. The Seam Transport Theorem (R2a): proof and verification**

Let g\_K(θ) \= exp\[½ ρ\_K(θ) n·σ\] with the fixed axis n(θ+π) \= n(θ) and the seam antisymmetry ρ\_K(θ+π) \= −ρ\_K(θ) (ZS-F30). Then g\_K(θ+π) \= exp\[−½ ρ\_K(θ) n·σ\] \= g\_K(θ)⁻¹, so the open-path seam half-transport is U\_K(θ+π, θ) \= g\_K(θ+π)⁻¹ g\_K(θ) \= g\_K(θ)² \= exp\[ρ\_K(θ) n·σ\]. Since (n·σ)² \= I with eigenvalues ±1, U\_K is Hermitian positive-definite with eigenvalues e^{±ρ\_K}, hence singular values {e^{|ρ\_K|}, e^{−|ρ\_K|}}; the singular-value ratio gives the UNSIGNED Cartan length ℓ\_K \= ½ ln(s\_max/s\_min) \= |ρ\_K|. The SIGNED, seam-odd rapidity is recovered from the principal logarithm log U\_K \= ρ\_K n·σ via ρ\_K \= ½ Tr\[(n·σ) log U\_K\] (using ½ Tr\[(n·σ)²\] \= 1). Thus the oriented transport coordinate is ρ\_tr^{oriented} \= ρ\_K. This is an open-path TRANSPORT statement; the singular values of an open transport are not gauge-invariant under independent endpoint gauge transformations, so the promotion to a physical closed-loop holonomy ρ\_hol requires the gauge equivalence A\_Z ∼ A\_K (R2b). ∎

Verification. For (ρ\_K, n) at BOTH signs — {(+0.37, generic), (−0.37, generic), (+0.9, x̂), (−0.15, generic)} — the script confirms g\_K(θ+π) \= g\_K(θ)⁻¹, U\_K \= g\_K² \= exp\[ρ\_K n·σ\], the unsigned length ½ ln(s\_max/s\_min) \= |ρ\_K|, and the signed recovery ½ Tr\[(n·σ) log U\_K\] \= ρ\_K, all to machine precision (the negative cases are what catch the v1.3 sign slip). R2b (A\_Z ∼ A\_K) is left OPEN.

**Appendix D. Koenigs multiplier and the retracted F14 route**

Koenigs (C\_int). For f(z) \= i^z \= e^{iπz/2}, f(z\*) \= z\*, the multiplier is λ\* \= f′(z\*) \= (iπ/2) z\*, with |λ\*| \= (π/2)|z\*| \= 0.89151 \< 1 (attracting), −ln|λ\*| \= 0.1148346, and arg λ\* \= π/2 \+ arg z\* \= 2.2592496. Koenigs’ theorem gives an analytic χ near z\* with χ∘f \= λ\*·χ. Matching one iteration to one modular step needs −ln|λ\*|/ω\_Z \= arg λ\*/ν\_Z (C\_int, OPEN). The per-step contraction −ln|λ\*| \= 0.1148346 is distinct from α\_BK \= −ln|z\*| \= 0.5664173.

Retracted F14 route. ZS-F14’s joint ODE governs the (ε, θ) radial–angular pair (radial Lyapunov decay; angular Goldstone accumulation; conservation Q \= a³ ε² θ̇ \= ***A***; centrifugal boundary), not a linear support ODE with two independent periodic solutions h\_1, h\_2. A fundamental matrix built from such h\_i would have 2π-periodic columns and trivial loop monodromy. The v1.2 ‘F14-ODE monodromy target’ is therefore withdrawn in favour of the seam half-transport (Appendix C).

**Appendix E. Verification ledger (v1.3)**

Mirrors zs\_f31\_verify\_v1\_4.py. PASS/FAIL are arithmetic/symbolic/construction; the OPEN registry lists operator gates not machine-verified.

| Check | Statement | Result |
| ----- | ----- | ----- |
| A.4 z\* | |z\*| \= 0.5675551633; −ln|z\*| \= 0.5664173303 \= y\*π/2; |z\*|² \= 0.3221188634 | PASS |
| A.7 Planck | Ω\_b 0.48σ, Ω\_cdm 0.01σ, Ω\_Λ 0.17σ; Ω\_Λ \< 0.2σ AND all three \< 0.5σ | PASS |
| B.1 Φ\_0=id | jump-only Φ\_0 \= e^{0𝓛★} \= identity | PASS |
| B.2 CP | Choi(Φ\_{0.6}) PSD | PASS |
| B.3 TP/unital | Tr 𝓛★(ρ) \= 0 and 𝓛(I) \= 0 (both pictures) | PASS |
| B.4 intertwine | E\_D 𝓛★ \= 𝓛\_π E\_D and E\_D 𝓛★(1−E\_D) \= 0 | PASS |
| B.5 stationary | unique tracial stationary I/N; dim ker \= 1 | PASS |
| B.6 covariance | \[𝓛★, σ\_s^ω\] \= 0 (faces in centralizer) | PASS |
| C.1 regression | v1.1 Ψ\_0 \= E\_D ≠ id; v1.3 Φ\_0 \= id | PASS |
| D Koenigs | |λ\*| \= 0.89151 \< 1; −ln|λ\*| \= 0.1148346 ≠ α\_BK \= 0.5664173; arg λ\* \= 2.2592496 | PASS |
| E entropy budget | ∫₀^∞ σ\_Z \= D(ϱ\_0‖ϱ\*) − D(ϱ\_∞‖ϱ\*) \= D(ϱ\_0); bounded (no MLSI); gap tail 1/(2Δ) | PASS |
| F S14 reduction | zero new structure, keep B,W,G → S14 | PASS |
| G Seam Transport | U\_K \= g\_K² \= exp\[ρ\_K n·σ\]; ℓ\_K \= ½ln(s\_max/s\_min) \= |ρ\_K| (both signs); signed ρ\_K \= ½Tr\[(n·σ)logU\_K\] (R2a) | PASS |
| I Gate-E rationale | counterexample e^{−T} ≥ e^{−2T} with reversed rates at T=0: value ordering ⇏ rate ordering ⇒ Gate E is HYPOTHESIS-strong | PASS |
| H full spectrum | Spec(𝓛★) \= Spec(𝓛\_π) ⊎ {−½(Γ\_c+Γ\_d)}; N=4,8,11 dense match; 121 \= 14641 closed form (P2) | PASS |
| OPEN registry | R2b, P1-core, C\_int, clock map t(T), Z-screen, Gate E (inequality), Gcoin (B3-dependent) | OPEN |

**References**

**Z-Spin corpus**

\[ZS-F2\] K. Kang, “Geometric Impedance A \= 35/437,” ZS-F2 v1.0 (2026).

\[ZS-F5\] K. Kang, “Gauge Symmetry Constraint: Why Q \= 11, and the Seam Involution,” ZS-F5 v1.0 (2026).

\[ZS-F14\] K. Kang, “Z-Anchored Vortex and the (epsilon, theta) Joint ODE,” ZS-F14 v1.0 (2026).

\[ZS-F30\] K. Kang, “Twin-Reuleaux Reality Structure and the Steiner-Centered Support-Ratio Rapidity,” ZS-F30 v1.4 (2026).

\[ZS-M1\] K. Kang, “i-Tetration and the Fixed Point,” ZS-M1 v1.0 (2026).

\[ZS-M4\] K. Kang, “Dilation \= Boost: the i-Tetration Rapidity alpha\_BK,” ZS-M4 v1.0 (2026).

\[ZS-M6\] K. Kang, “Register-Total Normalization and kappa^2 \= A/Q,” ZS-M6 v1.0 (2026).

\[ZS-S14\] K. Kang, “Master Action Total Closure,” ZS-S14 v2.0 (2026).

\[ZS-A17\] K. Kang, “Macro-Holonomy and the Spin–Metric Independence No-Go,” ZS-A17 v1.5 (2026).

\[ZS-A19\] K. Kang, “Z-Spin Boundary Tension as Geometric Dust,” ZS-A19 v3.1 (2026).

\[ZS-A20\] K. Kang, “The Atomic Interface: Parent-Action Equivalence to Brown Dust,” ZS-A20 v2.0 (2026).

\[ZS-A24\] K. Kang, “Finite-Register Modular Unification and the Continuous-Core Lift (F-A24.9),” ZS-A24 v2.0 (2026).

\[ZS-A28\] K. Kang, “JZ-Odd Doublet, the Top-Form Vacuum, and the Rank-vs-Energy Separation,” ZS-A28 v2.0 (2026).

\[ZS-A30\] K. Kang, “The Coincidence Wall and Its Classified Escapes,” ZS-A30 v1.6 (2026).

**External**

\[1\] G. Lindblad, “On the generators of quantum dynamical semigroups,” Commun. Math. Phys. 48, 119 (1976).

\[2\] V. Gorini, A. Kossakowski, and E. C. G. Sudarshan, “Completely positive dynamical semigroups of N-level systems,” J. Math. Phys. 17, 821 (1976).

\[3\] H. Spohn, “Entropy production for quantum dynamical semigroups,” J. Math. Phys. 19, 1227 (1978).

\[4\] M. Takesaki, “Conditional expectations in von Neumann algebras,” J. Funct. Anal. 9, 306 (1972).

\[5\] G. Koenigs, “Recherches sur les intégrales de certaines équations fonctionnelles,” Ann. Sci. Éc. Norm. Supér. (3) 1, supp. 3 (1884).

\[6\] É. Cartan, “Les groupes réels simples finis et continus,” Ann. Sci. Éc. Norm. Supér. 31, 263 (1914).

\[7\] R. Penrose and W. Rindler, Spinors and Space-Time, Vol. 1 (Cambridge Univ. Press, 1984).

\[8\] J. J. Bisognano and E. H. Wichmann, “On the duality condition for a Hermitian scalar field,” J. Math. Phys. 16, 985 (1975); 17, 303 (1976).

\[9\] G. L. Sewell, “Quantum fields on manifolds: PCT and gravitationally induced thermal states,” Ann. Phys. (N.Y.) 141, 201 (1982).

\[10\] A. Connes and C. Rovelli, “Von Neumann algebra automorphisms and time–thermodynamics relation,” Class. Quantum Grav. 11, 2899 (1994).

\[11\] J. D. Brown and K. V. Kuchař, “Dust as a standard of space and time in canonical quantum gravity,” Phys. Rev. D 51, 5600 (1995).

\[12\] G. W. Gibbons and S. W. Hawking, “Cosmological event horizons, thermodynamics, and particle creation,” Phys. Rev. D 15, 2738 (1977).

\[13\] V. Chandrasekaran, R. Longo, G. Penington, and E. Witten, “An algebra of observables for de Sitter space,” J. High Energy Phys. 02 (2023) 082\.

\[14\] R. Bousso, R. Harnik, G. D. Kribs, and G. Perez, “Predicting the cosmological constant from the causal entropic principle,” Phys. Rev. D 76, 043513 (2007).

\[15\] H. Henneaux and C. Teitelboim, “The cosmological constant and general covariance,” Phys. Lett. B 222, 195 (1989).

\[16\] Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters,” Astron. Astrophys. 641, A6 (2020).

**Version History**

v1.4 (March 2026\) — Final internal version. Four final patches following a third adversarial review, all expressing the existing results more precisely (no new research). (1) Seam transport SIGN: the singular-value ratio gives the UNSIGNED Cartan length ℓ\_K \= |ρ\_K|; the signed, seam-odd rapidity ρ\_K \= ½Tr\[(n·σ)logU\_K\] is recovered from the oriented axis, now tested at BOTH signs (correcting a v1.3 slip that read the ratio as ρ\_K and tested only positive cases). (2) Transport vs holonomy: R2a is a canonical seam-TRANSPORT realization theorem (open path), not a closed-loop physical-holonomy theorem; the connection is sl(2,ℂ)-valued pure-gauge (a boost, fixed axis), and the promotion ρ\_tr → ρ\_hol is R2b (OPEN). (3) Gate E is downgraded from DERIVED-CONDITIONAL to HYPOTHESIS-strong, since data processing gives a value inequality D\_Z ≥ D\_X, which does not imply a pointwise production-rate inequality (value ordering ⇏ derivative ordering). (4) §2.5 carrier sector corrected: S\_BK is Brown–Kuchař DUST (clock/frame), the nonminimal prefactor F belongs to S14, and S\_Λ is a 3-form potential A₃ with F₄ \= dA₃; the three displayed equations are the carrier-sector (not the full) Euler–Lagrange system. A results-architecture table is added; the spectrum is stated as a multiset union and framed as a general N-face abstraction of ZS-A30’s graph-specific computation. The three PROVEN contributions (P1, P2, R2a) and the inherited budget are unchanged. No new fitted parameter; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED. The OPEN items (R2b, P1-core, C\_int, B3, Gate E) are deferred to ZS-F32 / ZS-A31.

v1.3 (March 2026): Three independent contributions — Theorem P2 (exact 121-face Lindblad spectrum), Theorem R2a (exact seam transport, replacing the RETRACTED F14-monodromy route), and an entropy-budget normalizability proof; the A/Q dephasing term removed (jump-only, parameter-free); both pictures stated; ‘central’ corrected to ‘modular centralizer’; the carrier action and field equations restored. \[Superseded by v1.4: the seam result is sign-corrected and reclassified as transport (not holonomy); Gate E is HYPOTHESIS-strong; §2.5 carrier labels corrected.\]

v1.2 (March 2026): Replaced v1.1’s broken population lift (Ψ\_0 \= E\_D ≠ id) by a genuine GKLS generator (Theorem P1); reduced the geometric gates; replaced the circular rank-relative-entropy present selection by a causal-diamond Z-Spin entropy measure. \[Superseded in part by v1.3: the F14-monodromy route is retracted, the dephasing term removed, and P1 raised to the full spectrum P2.\]

v1.1 / v1.0 (March 2026): Initial assembly of ZS-F30 and ZS-A30 into Γ\_CR; the Diagonal-in-Centralizer Lemma (PROVEN, retained); proper-time exclusion (retained, strengthened in §10). \[v1.1’s ι∘Φ\_t∘E lift and its over-closed Theorems R/C/P are retracted.\]