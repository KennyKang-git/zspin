# **ZS-F39**

# **The Seam Uniformization Theorem: The Modular Length Functor, the Physical Clock-Gate Execution, and the One-Isomorphism Reduction of the Register-Clock Registry**

*Consolidation of the (H-CLK), (H-Σ2), and (H-eval-N/F) Gates into a Single Seam Chart Φ\_seam; the Modular Length Functor E\_len; the EHK Channel-Level Register Measure; Model-Tier Execution and the Physical Clock-Gate Discharge Protocol*

**Author:** Kenny Kang (Z-Spin Collaboration) **Date:** July 2026 **Theme / Code:** Foundations / ZS-F39 · Integrates the pre-scoped ZS-M48 deliverables (collaboration decision of record) · Consumes ZS-F38 v1.1 Appendix D target, ZS-A32 v1.0 discharge criterion · Upstream of ZS-F39.1 (ε\_phys execution) and ZS-F40 (C\_UV proof-carrying global-minimum gate, pre-registered outlook)

---

**Verification: 54/54 exact/numerical checks PASS \+ 8/8 guards | Zero Free Parameters** (zs\_f39\_verify\_v1\_1.py; SymPy exact rational linear algebra \+ mpmath 50-digit locked dynamics \+ NumPy superoperator spectra and the frozen seed-11 null. v1.0 baseline 49/49 \+ 7/7 reproduced unchanged; v1.1 adds T1D1–T1D3 and N1d–N1e plus guard N1-G2. All v1.0 frozen registrations — seed 11, null thresholds, the Appendix C decision rule — are byte-identical.)

Sole geometric inputs: **A** \= 35/437, **Q** \= 11, (Z, X, Y) \= (2, 3, 6), dim **Z** \= 2\. LOCKED.

---

## §0. Abstract

ZS-F38 and ZS-A32 left the ZS-A22 barrier B3 as a two-gate debt {(H-CLK) discharge, C\_UV full 1PI}, with the modular length functor E\_len named as a proof target (ZS-F38 Appendix D, NC-F38.7) and the physical ε\_C\_int computation named as the discharge criterion (ZS-A32 §5). This paper performs the pre-scoped ZS-M48/ZS-F39 consolidation. **First (uniformization),** we define the seam chart **Φ\_seam** and prove **Theorem F39.T1**: the four previously separate gates — (H-CLK) register-clock identity, (H-Σ2) seam-gauge holonomy equality on Σ₂, (H-eval-N/F) normalization and functoriality, and the ZS-M47 §12.3 operator rows inherited through ZS-A32 — are projections of a single uniformization datum, unique up to cocycle conjugacy and a central phase. v1.1 adds the explicit three-level commutative diagram (germ / standard-pair / algebra; Appendix A, Lemma F39.L2) requested in external review, exhibiting how Koenigs scalar uniqueness, Stone–von Neumann uniqueness, and the HSMI/standard-pair normal form land in the same equivalence class. **Second (length),** we deliver the ZS-F38 Appendix D target: **Lemma F39.L1 / Theorem F39.T2** construct the modular length functor E\_len on Z-Spin seam standard pairs via Connes spectral distance on the compact dual, with scaling covariance E\_len(Δ^(−it) U(1) Δ^(it)) \= e^(2πt) ℓ̄\_P verified exactly; delivery discharges **(H-eval-N) ∧ (H-eval-F) at the mathematical tier**, shortening the ZS-F38.T3 registry to {(H-CLK), (H-cycle), KH1–KH4}. **Third (measure),** **Theorems F39.T3/T4** lift the register measure ρ\_Q \= I\_Q/**Q** from classical ergodicity (ZS-F38.T1′) to the quantum channel level: the A24-refining equivariant slot lift is a unital irreducible GKLS generator whose *unique* stationary state is I\_Q/**Q** (Evans–Høegh-Krohn / quantum Perron–Frobenius), while the multiplicity-weighted lift is a non-unital generator whose stationary sector law is the *distinct* transport weight (9, 4, 36)/49 \= (d\_X², d\_Z², d\_Y²)/49 (ZS-F37 two-leg ω); a selection lemma shows only the equivariant lift coarse-grains to the ZS-A24 sector generator. This structurally separates state density from transport weight (guard DS2 / NC-F38.2 preserved). **Fourth (discharge),** the ε\_C\_int computation is stratified into two tiers: the **model tier is executed** — ε\_C\_int^(model) \= 0 exactly on the F38.T2 Hardy chain (branch-free Abel unit step to \< 10⁻²⁰ at twelve Koenigs orbit points) — and the **physical tier is protocolized, not executed**: the frozen decision rule (Appendix C: ε\_phys \< 10⁻¹⁰ ∧ P\_null ≤ 5% on the ZS-F31 GKLS / ZS-A24 core data) is pre-registered together with an executed 2000-draw seed-11 Haar null (min ε \= 1.0975, p5 \= 1.1585). v1.1 adds **Lemma F39.N1.L**: the ε \= 0 locus is a nonempty *proper* real-algebraic subvariety of the unital pair-Kraus space, hence of Haar measure zero — an analytic exclusion that the finite sample alone could not supply; the sample null estimates only the finite-threshold false-positive rate, and the frozen rule is unchanged. **Honest terminus:** B3 is **not closed**. If the physical ε\_C\_int discharge succeeds, (H-CLK)/(H-Σ2) close and the remaining debt is exactly one number — the C\_UV full 1PI factor (ZS-F36 programme (i), untouched here; target ≈ 1.244 within the a-priori band \[1/4, 4\]). Appendix D pre-registers the ZS-F40 proof-carrying global-minimum gate for that computation (lexicographic constraints; certification by interval arithmetic / SDP hierarchy / branch-and-bound; AI proposes candidates, certificates close), as OUTLOOK / NON-CLAIM. Verification: 54/54 PASS \+ 8/8 guards; zero fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED.

---

## Epistemic Status Legend

| Tag | Meaning |
| ----- | ----- |
| **PROVEN** | Established by exact mathematics within the stated finite model, machine-verified. |
| **IMPORTED-PROVEN** | External theorem of the mathematical literature, consumed with citation (Koenigs; Stone–von Neumann; Borchers–Wiesbrock; Evans–Høegh-Krohn; Connes; measure-zero of proper algebraic subvarieties). |
| **DERIVED** | Follows from PROVEN/IMPORTED-PROVEN inputs and locked corpus constants with no new assumption. |
| **DERIVED-CONDITIONAL** | Derived modulo explicitly named, falsifiable conditions ((H-CLK), (H-cycle), KH1–KH4). |
| **HYPOTHESIS-strong / \-weak** | Registered hypothesis with executed / pending anti-numerology protocol. |
| **OPEN-PROTOCOLIZED** | Not executed; a frozen, pre-registered finite decision procedure exists (this paper's physical ε\_C\_int tier). |
| **OPEN** | Neither executed nor yet reduced to a frozen finite procedure (C\_UV full 1PI). |
| **OBSERVATION** | Consumed empirical package, firewalled (single ΛCDM package, §9 block CR only). |
| **NON-CLAIM** | Explicit disclaimer of scope. |

---

## §1. Introduction: the seam debt ledger after ZS-F38 / ZS-A32

ZS-F36 v2.1 terminated the charge-unit line at ρ\_Λ,Z \= (1260/4807) C\_UV M\_K⁴ with three open programmes; ZS-F38 compressed them into the Register Clock Identity (H-CLK) — "the register's tick is the seam's unit modular time" — plus the structural condition (H-cycle), the evaluation condition (H-eval), and one computation (C\_UV). ZS-A32 executed the pre-registered anti-numerology Monte Carlo (p\_single \= 0.50%), executed the *model-level* C\_int at ε\_C\_int \= 0 exactly on the F38.T2 Hardy chain, and fixed the discharge criterion for this paper: compute ε\_C\_int^(phys) on the actual ZS-F31 GKLS / ZS-A24 seam-channel core data.

At the close of ZS-A32, the ledger read:

| Item | Status entering F39 |
| ----- | ----- |
| (H-CLK) register-clock identity | OPEN (condition reuse; F37 C.5 ∧ CRT-4a) |
| (H-Σ2) seam-gauge holonomy gate on Σ₂ | OPEN (bundled inside (H-CLK)(a)) |
| (H-eval-N) normalization, (H-eval-F) functoriality | OPEN; E\_len named as target (F38 App. D, NC-F38.7) |
| ZS-M47 §12.3 operator rows | INHERITED-OPEN → ZS-M48/ZS-F39 (A32 registration) |
| ρ\_Q \= I\_Q/Q | DERIVED-CONDITIONAL on (H-CLK) ∧ (H-mix), classical tier (F38.T1′) |
| ε\_C\_int | model tier PROVEN (= 0); physical tier OPEN behind (H-CLK)/(H-Σ2) |
| C\_UV full 1PI | OPEN (F36 programme (i); inferred ≈ 1.24, A32 band) |
| **B3** | **two-gate debt {(H-CLK) discharge, C\_UV 1PI}; statistical leg closed (p \= 0.50%)** |

This paper's thesis is that the first four rows are not four problems. They are four projections of one uniformization problem: does there exist a single seam chart carrying the ZS-F31 GKLS register clock onto the ZS-M46 seam modular clock, compatibly with the Σ₂ holonomy gauge and the length normalization? We name that chart **Φ\_seam**, prove its uniqueness class (§4), deliver the length functor it must intertwine (§5), lift the register measure it must average (§6), stratify its verification into an executed model tier and a protocolized physical tier (§7–§8), and state honestly what remains (§10).

**What v1.1 changes relative to v1.0 (external review of record, integrated in full).** (i) The subtitle phrase "Physical Clock-Gate Execution" is replaced by "Model-Tier Execution and the Physical Clock-Gate Discharge Protocol": the model tier is executed, the physical tier is OPEN-PROTOCOLIZED, and the title now says exactly that. (ii) The N1 null is epistemically split: the executed 2000-draw sample estimates the finite-threshold false-positive rate, while the new **Lemma F39.N1.L** supplies the analytic (measure-zero) exclusion that a sample cannot; the sentence requested in review is adopted verbatim in §8.3. (iii) **Theorem F39.T1** gains the explicit commutative diagram (Appendix A, Lemma F39.L2) showing how Koenigs scalar uniqueness, Stone–von Neumann uniqueness, HSMI/standard-pair normal form, cocycle conjugacy, and the central phase fall into one equivalence class — with three new machine checks (T1D1–T1D3). (iv) The B3-closure attempt is *not* absorbed into this paper: Appendix D pre-registers it as ZS-F40 (proof-carrying global-minimum gate), per the review's separation recommendation. No frozen registration of v1.0 is altered.

---

## §2. Locked inputs

All theorem-side constants are fixed here, above the single firewalled observation block (§9), reproducing the ZS-F36/A31/A32 declared-before-loaded discipline.

- **A** \= 35/437 (geometric impedance, ZS-F2, LOCKED); **Q** \= 11; (Z, X, Y) \= (2, 3, 6); dim **Z** \= 2; Σd² \= 4 \+ 9 \+ 36 \= 49\.  
- Slot-normalized register-trace coupling κ² \= **A**/**Q** \= 35/4807 (ZS-M44/F38.T1′); vacuum combination 1260/4807 \= 36 **A**/**Q** exact (ZS-F36).  
- Locked seam dynamics: the i-tetration germ f(z) \= e^(iπz/2), fixed point z\* \= 0.4382829367 \+ 0.3605924719 i, multiplier λ\* \= (iπ/2) z\*, μ \= −ln|λ\*| \= 0.1148346250, θ \= arg λ\* \= 2.2592495540 (ZS-M1, 10 locked digits re-verified at 50-digit precision; checks K5–K7).  
- Branch-free Abel unit step: u(f z) − u(z) \= 1 along the Koenigs coordinate at twelve independently computed orbit points, deviation \< 10⁻²⁰ (check K8; re-verifies ZS-M46 GEO2-class data).

Checks K1–K8 PASS. Zero fitted parameters.

---

## §3. The seam chart Φ\_seam: definition and gate consolidation

**Definition F39.D1 (Seam chart).** A *seam chart* is a triple Φ\_seam \= (Φ\_clk, Φ\_hol, Φ\_len) consisting of:

(a) **Φ\_clk** — a CPTP-covariant identification of the ZS-F31 GKLS register clock (one slot advance per unit register time) with the modular flow σ\_t^M of the ZS-M46 seam inclusion at equal speed (a central cocycle cannot rescale a flow; ZS-F38 App. B.3);

(b) **Φ\_hol** — the ZS-F37 Appendix C.5 seam-gauge equality Hol\_{A\_Z}(γ) \= g⁻¹ Hol\_{A\_K}(γ) g on Σ₂, i.e. the (H-Σ2) gate;

(c) **Φ\_len** — the evaluation of the unit seam step in Planck length via the modular length functor E\_len of §5, i.e. the (H-eval-N/F) content.

**Proposition F39.P1 (Gate consolidation) \[DERIVED\].** The existence of Φ\_seam is *equivalent* to the conjunction (H-CLK) ∧ (H-Σ2) ∧ (H-eval-N) ∧ (H-eval-F), and it subsumes the ZS-M47 §12.3 operator rows registered INHERITED-OPEN by ZS-A32: each row is the statement that one component of Φ\_seam acts as the identity on the corresponding operator datum. No new condition is introduced; Φ\_seam is *condition reuse* in the exact sense of ZS-F38 Definition F38.D1 — a bundling that adds no registry entry. Its content in one sentence: **one chart carries the register's tick, the seam's gauge, and the Planck ruler simultaneously.**

The consolidation is the paper's first contribution: what entered as four scattered OPENs leaves as one object whose existence is a single physical question (§7–§8) and whose *uniqueness*, given existence, is a theorem (§4).

---

## §4. Theorem F39.T1 — Seam Uniformization

**Theorem F39.T1 (Seam Uniformization) \[mathematics IMPORTED-PROVEN \+ PROVEN in the finite instance; as a statement about the physical seam, DERIVED-CONDITIONAL on KH1–KH4\].** *Let (M, U, Ω) be a Z-Spin seam standard pair satisfying KH1–KH4, equipped with the locked germ dynamics of §2. If a seam chart Φ\_seam exists, it is unique up to (i) a Connes cocycle conjugacy of the modular flow and (ii) a central phase; equivalently, the space of seam charts is either empty or a single torsor under Z(M)\_unitary × Cocycle(σ^M).*

**Proof architecture (three levels; full diagram in Appendix A).**

1. **Germ level (Koenigs).** The linearizing coordinate κ of f at z\* with multiplier λ\* (0 \< |λ\*| ≠ 1\) is unique up to a nonzero scalar; the multiplier — hence the modular speed μ and phase θ — is a conjugacy invariant \[Koenigs 1884; IMPORTED-PROVEN\]. Machine witnesses: K8 (additive Abel form), **T1D1** (multiplicative form, κ(f z) \= λ\* κ(z) to \< 10⁻²⁰ at six orbit points, NEW v1.1).  
     
2. **Operator level (Weyl / standard pair).** The pair (translation unitaries U(a), modular unitaries Δ^(it)) satisfying the Borchers commutation Δ^(∓it) U(a) Δ^(±it) \= U(e^(±2πt) a) is an irreducible Weyl-type pair for the ax+b relations; by Stone–von Neumann-type uniqueness for the standard pair \[Wiesbrock; Longo; IMPORTED-PROVEN\], any two realizations are unitarily equivalent, with the intertwiner unique up to a central phase.  
     
3. **Algebra level (HSMI normal form).** The half-sided modular inclusion N ⊂ M with Ω cyclic-separating is, under KH1–KH4, in the Borchers–Wiesbrock normal form; two charts implementing the same inclusion differ by a Connes cocycle of σ^M \[IMPORTED-PROVEN\].

Composing: any two seam charts agree at germ level up to scalar, at operator level up to central phase, and at algebra level up to cocycle conjugacy; the scalar is absorbed into the central phase (**T1D2**: κ → cκ, |c| \= 1, leaves λ\* exactly invariant; **T1D3**: |cλ\*| \= |λ\*| exact — NEW v1.1), yielding the stated torsor. 

**What T1 does and does not say.** T1 is a *uniqueness* theorem, not an existence theorem. Existence of Φ\_seam is exactly the physical content of (H-CLK)/(H-Σ2) and is addressed only by the discharge computation of §7–§8. Guard G1 registers this. **\[NON-CLAIM NC-F39.1\]**

---

## §5. Lemma F39.L1 / Theorem F39.T2 — the modular length functor E\_len

ZS-F38 Appendix D stated the target: a functor E\_len : StandardPair\_Z-Spin → ℝ₊ with **(N)** E\_len(U(a)) \= a·ℓ̄\_P for a ≥ 0 and **(F)** E\_len(Δ^(−it) U(1) Δ^(it)) \= e^(2πt) ℓ̄\_P. This section delivers the mathematical construction along the route F38 itself named: the ZS-M47 NDC3 modular-Dirac spectral geometry, with the length element as the inverse Dirac scale and Connes distance on the compact dual.

**Lemma F39.L1 (Scaling covariance of spectral distance) \[PROVEN\].** *For a spectral triple (A, H, D) with Connes distance d\_D(p, q) \= sup{|f(p) − f(q)| : ‖\[D, f\]‖ ≤ 1}, the modular dilation D ↦ e^(−2πt) D on the stage-oriented branch scales the distance as d(e^(−2πt) D) \= e^(+2πt) d(D), exactly.* Machine witnesses: EL1 (exact at t \= 0, 0.1, 0.3, 1.0); EL2 (the two-point triple reproduces d \= 1/m by direct sup over commutator-bounded functions); EL3 (the S³ compact-dual Dirac spectrum ±(n \+ 3/2) with multiplicity (n+1)(n+2) obeys Weyl-3 counting N(λ)/((2/3)λ³) → 1, echoing ZS-M47 (IV)).

**Theorem F39.T2 (E\_len delivery) \[DERIVED; as applied to the physical seam, DERIVED-CONDITIONAL on KH1–KH4\].** *Define E\_len on objects by the Connes distance of the NDC3 modular-Dirac triple attached to the seam standard pair, normalized by (N). Then (F) holds by Lemma F39.L1, E\_len is functorial under cocycle-covariant isomorphisms (the distance is a sup over a conjugation-invariant ball), and delivery discharges (H-eval-N) ∧ (H-eval-F) at the mathematical tier. Consequently the ZS-F38.T3 registry shortens from {(H-CLK), (H-cycle), KH1–KH4, (H-eval-N/F/B)} to {(H-CLK), (H-cycle), KH1–KH4}, with (H-eval-B) reduced to the orientation bookkeeping fixed in ZS-F38 §6.*

**Boundary of the claim.** T2 discharges the *evaluation* gates as mathematics: modular dilation ↦ physical length scaling is now a theorem about the functor, not a physical assumption. What it does not do is assert that the physical seam realizes the NDC3 triple — that is, once more, existence of Φ\_seam. **\[NON-CLAIM NC-F39.2\]**

---

## §6. Theorems F39.T3 / T4 — the register measure at channel level, and the selection lemma

ZS-F38.T1′ derived ρ\_Q \= I\_Q/**Q** by *classical* Perron–Frobenius ergodicity conditional on (H-CLK) ∧ (H-mix). External review of F38 flagged the residual risk of conflating the state density I\_Q/**Q** with the Plancherel transport weight ω \= (d\_Z², d\_X², d\_Y²)/49 (guard DS2, NC-F38.2). This section removes the risk structurally by lifting both objects to the quantum channel level and proving they arise from *different lifts*.

**Theorem F39.T3 (Equivariant lift → democracy) \[PROVEN in the finite instance; physical instance DERIVED-CONDITIONAL on (H-CLK)\].** *Let the slot graph on the **Q** \= 11 register carry the sector-adjacency X–Z–Y (L\_XY ≡ 0), and let the equivariant (A24-refining) lift place jump operators √κ² |b⟩⟨a| on each adjacent ordered slot pair. Then the classical generator is doubly stochastic (unital) and irreducible with unique stationary law I\_Q/**Q** (EQ1–EQ3, exact rationals), and the quantum GKLS lift is a unital irreducible superoperator with one-dimensional kernel whose unique stationary state is I\_Q/**Q** — by the Evans–Høegh-Krohn quantum Perron–Frobenius theorem for irreducible unital semigroups (EQ4–EQ5; spectral gap \> 0, EQ6). The sector marginal of I\_Q/**Q** is exactly (3, 2, 6)/11, the ZS-A24 stationary law (EQ3).*

**Theorem F39.T4 (Multiplicity lift → transport weight; the second branch) \[PROVEN in the finite instance\].** *The multiplicity-weighted lift, with rates κ² d\_(target slot), is non-unital (ML1: a column sum ≠ 0, exact witness), irreducible (ML2), with stationary slot weights d\_slot/49 (ML3) and sector law (9, 4, 36)/49 \= (d\_X², d\_Z², d\_Y²)/49 — exactly the ZS-F37 two-leg transport weight ω, distinct from (3, 2, 6)/11 (ML4–ML5).*

**Lemma F39.SEL (Selection) \[PROVEN\].** *Only the equivariant lift coarse-grains to the ZS-A24 sector generator: its X→Z coarse rate is κ² d\_Z (SEL2, matching A24 exactly), whereas the multiplicity lift coarse-grains to κ² d\_Z² ≠ κ² d\_Z (SEL1). Hence the corpus's sector mediator selects the equivariant lift, whose stationary state is the democratic I\_Q/**Q**; the transport weight ω lives on the other branch and is never a state density.*

The DS2 separation is thereby upgraded from a guard to a theorem-level dichotomy: two lifts, two invariant objects, one selection criterion. Guard G3 retains the NC-F38.2 wording — T4 relates the *origins* of the two objects, not the objects.

Sector-level cross-checks: the ZS-A24 mediator on the path X–Z–Y with rates κ² d\_j has exact spectrum {0, −2**A**/**Q**, −**A**} and stationary (3, 2, 6)/11 (S1–S3); character bookkeeping χ₂χ₃ \= χ₄ \+ χ₂ symbolically (CH1), ρ\_b \= ½ ln(9/7) (CH2), with the F37 convention value Δχ(ρ\_b) consumed as reported (guard CH-G).

---

## §7. ε\_C\_int, tier I: the model execution (of record)

The ZS-A32 model-level result is reproduced within this suite as part of the locked baseline: on the F38.T2 Hardy chain the register shift and the seam modular step are the same map — z·(z^k) \= z^(k+1) exactly for all k ≤ **Q** (CI1), and the branch-free Abel increment equals 1 at twelve Koenigs orbit points to \< 10⁻²⁰ (CI2, K8). Hence

**ε\_C\_int^(model) \= 0, identically \[PROVEN (model)\].**

Not small — zero, because in the canonical model the clock identity holds by construction. The conjugate seam carries equal modular speed, |conj λ\*| \= |λ\*| exactly (CJ1–CJ2, the (H-2D) speed half), and the tensor Borchers triple keeps the joint spectrum in the closed forward cone at the model bookkeeping level (TB1).

**What the model tier does:** it sharpens the physical target. Any future physical computation returning ε\_C\_int ≠ 0 falsifies the clock identity itself, not a calibration (A32 §5 wording, inherited).

---

## §8. ε\_C\_int, tier II: the physical discharge protocol (OPEN-PROTOCOLIZED)

### 8.1 The frozen decision rule (Appendix C, unchanged from v1.0)

Compute ε\_C\_int^(phys) — the normalized deviation ‖Φ\_clk(P\_K) − P\_A‖/‖P\_A‖ between the seam-transported register one-tick map and the ZS-A24/F31 GKLS core generator's canonical clock — on the actual ZS-F31 GKLS / ZS-A24 seam-channel core data. **Discharge criterion:** ε\_phys \< 10⁻¹⁰ **and** P\_null ≤ 5% under the frozen null of §8.2. If met, (H-CLK) ∧ (H-Σ2) are discharged and Φ\_seam exists (T1 then makes it unique up to the stated torsor). If not met, the F38 mechanism leg fails while the A32 statistical leg survives independently — the two-leg architecture already prices both outcomes.

### 8.2 The executed frozen null (seed 11\)

Pre-registered and executed: 2000 unital pair-Kraus channels Φ(ρ) \= ½(V₁ρV₁† \+ V₂ρV₂†) with V₁, V₂ Haar-random (seed 11), scored by ε \= ‖Φ(C) − C‖/‖C‖ against the canonical **Q** \= 11 clock unitary C. Result of record: **min ε \= 1.0975, p5 \= 1.1585, median \= 1.2223** (N1b–N1c). The target is attainable: the clock-conjugation channel gives ε \= 0 exactly (N1a).

### 8.3 Lemma F39.N1.L — the analytic exclusion (NEW, v1.1)

External review (of record): *"ε \= 0 is unreachable by chance"* is not made rigorous by sampling alone; the sample-null statement and the measure-zero analytic statement must be separated. We adopt the review sentence verbatim and then close the analytic half:

Exact ε \= 0 belongs to the clock-implementing subvariety of the unital pair-Kraus space; the 2000-draw Haar null estimates the finite-threshold false-positive rate but does not by itself prove an analytic exclusion.

**Lemma F39.N1.L (Measure-zero exclusion) \[DERIVED from IMPORTED-PROVEN\].** *Let 𝒫 be the compact real-algebraic manifold of unital pair-Kraus channels on ℂ^Q (parameters (V₁, V₂) ∈ U(Q) × U(Q)), and let Z\_clk \= {Φ ∈ 𝒫 : Φ(C) \= C} be the clock-implementing locus. Then Z\_clk is a real-algebraic subvariety (the defining equations Φ(C) − C \= 0 are polynomial in the real and imaginary parts of the Kraus entries), it is nonempty (the clock-conjugation channel V₁ \= V₂ \= C lies in it; witness N1d, ε \= 0 to machine exactness), and it is proper (an explicit deterministic unital channel — V₁ \= I, V₂ \= diag((−1)^k) — has ε \= 0.9535 \> 0; witness N1e). A nonempty proper real-algebraic subvariety of a connected real-algebraic manifold has Haar (Lebesgue-class) measure zero \[standard real-algebraic geometry: proper Zariski-closed sets are null; e.g. Federer §3.4 / stratification\]. Hence the Haar probability of drawing ε \= 0 exactly is zero.* 

**Epistemic separation (guard N1-G2, NEW).** The lemma is the analytic exclusion; the executed sample is the *finite-threshold* calibration (how often a random channel lands within any given ε-band). The two are different statements with different uses, and — critically — the frozen Appendix C decision rule is **unchanged** by the lemma: pre-registration integrity is preserved.

### 8.4 Status

**ε\_C\_int^(phys): OPEN-PROTOCOLIZED.** This paper protocolizes the discharge; it does not execute it. Execution on the ZS-F31/ZS-A24 data is scoped to **ZS-F39.1** (guard N1-G). The v1.0 subtitle wording that could be read as claiming execution is retired in v1.1 (§1).

---

## §9. Corner consistency (firewalled; one ΛCDM package consumed)

Declared-before-loaded: every theorem-side constant of this paper appears above this section; the single observation package (Planck-2018-class M̄\_P, ρ\_Λ^(1/4), H₀, t\_U, M\_eff) loads only in block CR (guard CR-G0; A31/A32 firewall inherited). Consistency class results (A32 Table 2 class, reproduced): corner (W) deviation 0.078% against 2π**Q**; (V) 0.067% against 8π**Q**; (L) 0.327% and (T) 0.291% against 4π**Q**; vacuum factor ½(1260/4807)θ² \= 0.668952; the corner-(W) inference C\_UV ≈ 1.242, inside the a-priori band \[1/4, 4\] and within 2% of the A32 cross-corner value 1.244 (CR-W/V/L/T, CR5). These are **consistency reproductions, not new evidence**; the statistical adjudication of record remains ZS-A32's executed p\_single \= 0.50%. **\[OBSERVATION, firewalled\]**

Cross-version echoes: 4**QA** \= 1540/437 exact (XV1); e^(−2π**Q**) \= 9.632×10⁻³¹ (XV2); the A24 dimensionless rates {2**A**/**Q**, 6**A**/**Q**} appear verbatim in L\_sec (XV3); the F37 ω reordering identity (XV4).

---

## §10. What F39 closes, and what it does not: the B3 ledger

| Gate | Before F39 | After F39 v1.1 |
| ----- | ----- | ----- |
| (H-CLK) ∧ (H-Σ2) | two separate OPEN gates | one object (Φ\_seam existence); uniqueness class PROVEN/IMPORTED-PROVEN (T1); discharge reduced to one finite computation, OPEN-PROTOCOLIZED (§8) |
| (H-eval-N) ∧ (H-eval-F) | OPEN; E\_len a named target | discharged at the mathematical tier (L1/T2); F38.T3 registry shortens to {(H-CLK), (H-cycle), KH1–KH4} |
| ZS-M47 §12.3 operator rows | INHERITED-OPEN | absorbed into Φ\_seam (P1); no separate registry entries remain |
| ρ\_Q \= I\_Q/**Q** | classical ergodicity tier | quantum channel tier (EHK), with the ω-dichotomy now a theorem (T3/T4/SEL) |
| ε\_C\_int | model \= 0 (A32); physical OPEN | model \= 0 reproduced; physical OPEN-PROTOCOLIZED with frozen rule \+ executed null \+ analytic exclusion (N1.L) |
| C\_UV full 1PI | OPEN | **OPEN — untouched** (guard G4; no Q-absorption, A31 rule) |
| **B3** | two-gate debt | **NOT CLOSED.** Compressed: if ZS-F39.1's ε\_phys discharge succeeds, the entire remaining debt is the single number C\_UV (full 1PI, target ≈ 1.244) |

**Positioning (of record).** This paper is not a B3-closure paper. It is the paper that makes B3 closable in exactly two named finite steps: **ZS-F39.1** (execute ε\_C\_int^(phys) under the frozen rule) and **ZS-F40** (compute C\_UV with a proof-carrying certificate; Appendix D). The corpus pattern holds: internal iteration converges to honesty, and the honest statement here is a *uniformization plus a protocol*, not a closure.

---

## Falsification Gates

**F-F39.1 (physical clock gate).** If ZS-F39.1 returns ε\_C\_int^(phys) ≥ 10⁻¹⁰ or P\_null \> 5% under the frozen Appendix C rule, (H-CLK)/(H-Σ2) fail; T1 becomes a uniqueness theorem about an empty set for the physical seam; F38.T1′(iii)/T3 revert to their prior statuses. The A32 statistical leg survives independently. *(Immediate, finite.)*

**F-F39.2 (functor collapse).** If the NDC3 modular-Dirac triple of the physical seam violates scaling covariance (Lemma L1 premise) — e.g. a nonlinear dilation law is measured on the compact dual spectrum — T2's physical application fails and (H-eval-N/F) reopen. *(Theory/simulation.)*

**F-F39.3 (measure dichotomy).** If any corpus computation is found in which the transport weight ω \= (9,4,36)/49 functions as a state density, or I\_Q/**Q** as a transport weight, Lemma SEL's selection collapses and the DS2 separation fails. *(Registry-level, immediate.)*

**F-F39.4 (uniqueness breach).** Exhibition of two seam charts inequivalent under Z(M) × Cocycle(σ^M) on a KH1–KH4 pair falsifies T1 (and with it the Borchers–Wiesbrock import chain as applied here). *(Mathematical collapse — immediate rejection.)*

**F-F39.5 (C\_UV band, inherited).** If the ZS-F40 certified computation returns C\_UV outside \[1/4, 4\], the B3 C\_UV route fails (F-F38.3 wording inherited); the statistical leg survives.

---

## Non-Claims

**NC-F39.1.** T1 proves uniqueness, not existence, of Φ\_seam; existence is the physical (H-CLK)/(H-Σ2) content, OPEN-PROTOCOLIZED. **NC-F39.2.** T2 does not assert the physical seam realizes the NDC3 triple. **NC-F39.3.** B3 is not closed; C\_UV full 1PI is untouched here (guard G4). **NC-F39.4.** Lemma N1.L does not alter the frozen decision rule or thresholds; pre-registration is preserved byte-identically. **NC-F39.5.** Appendix D (ZS-F40 gate) is OUTLOOK / pre-registration only; no candidate value of C\_UV is claimed, and "AI finds a minimum" is explicitly *not* a closure criterion — only a certificate is. **NC-F39.6.** NC-F38.2 (ω vs I\_Q/**Q** distinctness), NC-F38.3 (no dimensional scale from (**A**, **Q**) alone; A17/A27/A28 no-gos), and NC-F38.6 (no Millennium-problem claim) are inherited unchanged. **NC-F39.7.** The corner block (§9) is consistency reproduction, not new statistical evidence.

---

## Verification Summary

zs\_f39\_verify\_v1\_1.py — FAIL-CLOSED; SymPy exact rationals for every exact claim; mpmath 50-digit for locked dynamics; NumPy for superoperator spectra and the frozen null.

| Block | Checks | Content |
| ----- | ----- | ----- |
| K | K1–K8 | locked inputs; z\*, μ, θ to 10 digits; branch-free Abel unit step \< 10⁻²⁰ |
| S | S1–S3 | A24 mediator spectrum {0, −2A/Q, −A}, stationary (3,2,6)/11, irreducible — exact |
| EQ | EQ1–EQ6 | equivariant lift: unital, unique kernel, stationary I\_Q/Q (EHK), gap \> 0 |
| ML/SEL | ML1–ML5, SEL1–SEL2 | multiplicity lift: non-unital witness, d\_slot/49, sector (9,4,36)/49; selection dichotomy — exact |
| EL | EL1–EL3 | E\_len scaling covariance exact; Connes two-point sup; S³ Weyl-3 echo |
| CH | CH1–CH2 (+CH-G) | χ₂χ₃ \= χ₄ \+ χ₂ symbolic; ρ\_b \= ½ ln(9/7) |
| CI | CI1–CI2 | ε\_C\_int^(model) \= 0: Hardy shift exact; Abel unit step |
| CJ | CJ1–CJ2 | conjugate seam equal modular speed, exact |
| **T1D** | **T1D1–T1D3 (NEW v1.1)** | Koenigs square commutes (multiplicative, \< 10⁻²⁰); central-phase invariance of λ\*; quotient bookkeeping — exact |
| TB | TB1 | tensor Borchers joint-cone model bookkeeping |
| N1 | N1a–N1c, **N1d–N1e (NEW)** (+N1-G, **N1-G2 NEW**) | frozen null executed (min 1.0975, p5 1.1585); N1.L witnesses: locus nonempty and proper |
| CR | CR-W/V/L/T, CR5 (+CR-G0) | firewalled corner consistency; C\_UV(W) \= 1.242 in band |
| XV | XV1–XV4 | cross-version echoes |
| G | G1–G4 | scope guards (certify nothing) |

**Total: 54/54 PASS \+ 8/8 guards.** v1.0 baseline (49/49 \+ 7/7) reproduced unchanged inside this suite.

---

## Acknowledgements & Code Availability

Verification suite zs\_f39\_verify\_v1\_1.py accompanies this paper; all checks are re-runnable with no fitted input. External review of v1.0 (of record) is integrated in full; the review's separation recommendation (B3 closure → ZS-F40) is followed.

---

## Appendix A. The T1 uniqueness diagram (Lemma F39.L2, NEW v1.1)

**Lemma F39.L2 (Commutation of the three-level uniqueness data).** The following diagram commutes, and every vertical arrow is unique up to the group written beside it:

germ level          (ℂ, f)  ──κ──▶  (ℂ, w ↦ λ\*w)            \[Koenigs; unique up to ℂ\*-scalar\]

                       │                    │

   Abel/exp        u \= log\_λ\*κ         dilation by |λ\*|

                       ▼                    ▼

operator level   (U(a), Δ^(it))  ──W──▶  ax+b Weyl pair       \[Stone–von Neumann-type;

                       │                    │                   unique up to central phase U(1)\]

   GNS/standard        │                    │

                       ▼                    ▼

algebra level     N ⊂ M, Ω   ──Φ\_seam──▶  BW normal form      \[Borchers–Wiesbrock HSMI;

                                                                unique up to Cocycle(σ^M)\]

**Square (i)** (germ → operator): the Koenigs coordinate's multiplicative covariance κ∘f \= λ\*·κ (T1D1) exponentiates the Abel step (K8) to the Borchers commutation at unit t. **Square (ii)** (operator → algebra): the standard-pair GNS construction sends the Weyl pair to the HSMI, and the central phase of the intertwiner descends to the inner part of a modular cocycle. **Square (iii)** (equivalence classes): the ℂ\*-scalar of level 1 restricted to |c| \= 1 is exactly the central phase of level 2 (T1D2 — the multiplier, hence (μ, θ), is invariant), and the modulus part is absorbed by the normalization (N) of E\_len (§5); the residual freedom at level 3 is the Connes cocycle (T1D3 bookkeeping). Chasing the diagram: two seam charts differ by (central phase, cocycle), which is Theorem T1's torsor. 

The three imported uniqueness theorems are consumed with their standard hypotheses only; no Z-Spin-specific strengthening is assumed. **\[IMPORTED-PROVEN composition; machine witnesses T1D1–T1D3, K8, CJ1–CJ2\]**

## Appendix B. E\_len construction details

Objects: seam standard pairs (M, U, Ω) under KH1–KH4 with the NDC3 modular-Dirac triple (A, H, D) of ZS-M47 on the compact dual. E\_len(U(a)) := a·ℓ̄\_P (normalization (N)); on modular translates, E\_len(Δ^(−it) U(1) Δ^(it)) := d\_{e^(−2πt)D}-evaluation of the unit step \= e^(2πt) ℓ̄\_P by Lemma L1. Functoriality: for a cocycle-covariant isomorphism α, ‖\[αDα⁻¹, αfα⁻¹\]‖ \= ‖\[D, f\]‖, so the sup defining d is invariant; hence E\_len∘α \= E\_len. Machine anchors: EL1 (four dilation values, exact), EL2 (two-point sup within 2×10⁻²), EL3 (S³ Weyl-3 counting ratio 0.9926 at λ \= 100.5, echoing ZS-M47 (IV)).

## Appendix C. The frozen physical-discharge decision rule (byte-identical to v1.0)

**Input data:** the ZS-F31 GKLS register generator and the ZS-A24 seam-channel core (both corpus-locked; no free parameter). **Statistic:** ε\_C\_int^(phys) \= ‖Φ\_clk(P\_K) − P\_A‖\_F / ‖P\_A‖\_F. **Null:** the seed-11, 2000-draw unital pair-Kraus Haar ensemble of §8.2 (executed; min 1.0975, p5 1.1585, median 1.2223). **Rule:** discharge (H-CLK) ∧ (H-Σ2) iff ε\_phys \< 10⁻¹⁰ **and** P\_null(ε ≤ ε\_phys) ≤ 5%. **Scope:** execution belongs to ZS-F39.1; this paper registers and freezes only. Lemma F39.N1.L (v1.1) supplements the null's interpretation and changes nothing in this rule.

## Appendix D. ZS-F40 pre-registration: the proof-carrying global-minimum gate for C\_UV (OUTLOOK / NON-CLAIM)

Following the review of record, the B3-closure computation is *separated* from this paper and pre-registered as **ZS-F40 — The Proof-Carrying Global-Minimum Gate for the Z-Spin C\_UV 1PI Factor**, with the following frozen architecture:

**(F40.1) Admissible parent-space compactification.** Fix the admissible space 𝒜 of parent 1PI data by the proven/locked constraints only (KH1–KH4 admissibility, unital irreducibility, holonomy equivalence, ε\_C\_int \= 0), *as constraints — not as weighted penalties*: a lexicographic constraint structure, because tunable penalty weights λ would reintroduce numerology (review §4, adopted).

**(F40.2) Certified ε\_C\_int discharge.** Execute Appendix C on the ZS-F31/ZS-A24 data with an interval-arithmetic certificate on the norm evaluation.

**(F40.3) 1PI determinant formula.** C\_UV \= exp(−Γ^ren\_1PI), or an explicit zeta-regularized determinant ratio, stated at action level before any evaluation.

**(F40.4) Global-minimum certificate.** Minimize J(Θ) \= |log C\_UV^1PI(Θ) − log 1.244|² over Θ ∈ 𝒜. Closure requires a *certificate*, one of: (a) interval-arithmetic lower bounds on every parameter cell; (b) a Lasserre/SDP-hierarchy global lower bound matching the candidate upper bound; (c) KKT \+ Hessian positivity \+ certified exclusion of all other branches; (d) zeta-determinant / heat-kernel tail bounds sealing the 1PI error; with Galerkin truncation error bounds if truncated. **AI search proposes candidates; only the certificate closes.** Falsification: a certified C\_UV outside the A32 band ≈ 1.244 (a-priori \[1/4, 4\]) fails the C\_UV route of B3 while leaving the A32 statistical leg intact.

Nothing in this appendix is claimed; it is a frozen protocol so that ZS-F40 can execute without post-hoc freedom — the same discipline that F38 Appendix C established for A32.

---

## References

\[1\] Z-Spin Collaboration (K. Kang), *ZS-F38: The Register Clock Identity*, v1.1 (2026). \[2\] Z-Spin Collaboration, *ZS-A32: Friedmann-Forced Squares of the Register-Clock Depth*, v1.0 (2026). \[3\] Z-Spin Collaboration, *ZS-F36* v2.1; *ZS-F37* v1.3; *ZS-M46*; *ZS-M47*; *ZS-M44*; *ZS-A24*; *ZS-F31*; *ZS-A31* v1.5 (2025–2026). \[4\] G. Koenigs, "Recherches sur les intégrales de certaines équations fonctionnelles," Ann. Sci. Éc. Norm. Supér. **1**, 3–41 (1884). \[5\] M. H. Stone, Proc. Natl. Acad. Sci. USA **16**, 172 (1930); J. von Neumann, Math. Ann. **104**, 570 (1931). \[6\] H.-J. Borchers, "The CPT-theorem in two-dimensional theories of local observables," Commun. Math. Phys. **143**, 315 (1992). \[7\] H.-W. Wiesbrock, "Half-sided modular inclusions of von Neumann algebras," Commun. Math. Phys. **157**, 83 (1993). \[8\] D. E. Evans and R. Høegh-Krohn, "Spectral properties of positive maps on C\*-algebras," J. London Math. Soc. **17**, 345 (1978). \[9\] A. Connes, *Noncommutative Geometry* (Academic Press, 1994), Ch. VI (spectral distance). \[10\] H. Federer, *Geometric Measure Theory* (Springer, 1969), §3.4 (null sets of proper algebraic varieties). \[11\] V. F. R. Jones and R. Longo (HSMI tunnel structure), as consumed in ZS-M47; J. Koot, relative-position criterion (2025), as consumed in ZS-F38.T2. \[12\] J. B. Lasserre, "Global optimization with polynomials and the problem of moments," SIAM J. Optim. **11**, 796 (2001) \[Appendix D certificate class\]. \[13\] Planck Collaboration, Astron. Astrophys. **641**, A6 (2020) \[single firewalled package, §9\].

---

## Version History

**v1.0 (July 2026):** Initial public release. Seam chart Φ\_seam defined; Theorem F39.T1 (uniqueness up to cocycle conjugacy × central phase); Lemma F39.L1 / Theorem F39.T2 (E\_len delivery; (H-eval-N/F) mathematical-tier discharge; F38.T3 registry shortened); Theorems F39.T3/T4 \+ Lemma SEL (EHK channel-level register measure; ω-dichotomy); model-tier ε\_C\_int \= 0 reproduced; physical-tier frozen decision rule \+ executed seed-11 null; firewalled corner consistency. Verification 49/49 PASS \+ 7/7 guards (zs\_f39\_verify\_v1\_0.py). Zero fitted parameters. (Consolidated from internal Z-Spin Collaboration research notes following ZS-F38 v1.1 and ZS-A32 v1.0; integrates the pre-scoped ZS-M48 deliverables per the collaboration decision of record.)

**v1.1 (July 2026):** Review-integration revision; no frozen registration altered. (1) Subtitle corrected from "Physical Clock-Gate Execution" to "Model-Tier Execution and the Physical Clock-Gate Discharge Protocol"; the physical tier is tagged OPEN-PROTOCOLIZED throughout. (2) §8.3 adds the review sentence verbatim and Lemma F39.N1.L (measure-zero analytic exclusion of exact ε \= 0; witnesses N1d–N1e; guard N1-G2), separating the sample-null and analytic statements. (3) Appendix A adds the T1 three-level commutative diagram (Lemma F39.L2) with machine witnesses T1D1–T1D3. (4) Appendix D pre-registers ZS-F40 (proof-carrying global-minimum C\_UV gate; lexicographic constraints; certificate-only closure) as OUTLOOK/NON-CLAIM, per the review's separation recommendation; ZS-F39.1 (ε\_phys execution) scoped. Verification 54/54 PASS \+ 8/8 guards (zs\_f39\_verify\_v1\_1.py). Zero fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED.  
