**ZS-S20**  
**The Cellular Reduction of the Z-Spin Master Action:**  
**Projection, Legendre Closure, the Non-Abelian Gauss Law,**  
**and the Non-Identifiability of the Truncated-Icosahedron Hodge Measure**

Author: Kenny Kang · Z-Spin Cosmology Collaboration  
Date: July 2026  
Theme / Paper Code: Standard Model — ZS-S20   |   Version: v2.2  
Locked constants: A \= 35/437, Q \= 11, dim Z \= 2, z\*, λ₁ — never re-fit.  
Supersedes: ZS-S20 v1.0 and v1.1 (internal). Executes gates F-S19.6a, F-S20.8 and the identifiability question of the ZS-S19/S20 line.  
Headline: TWO LAYERS, KEPT APART. LAYER 1 — the arithmetic uniqueness theorem: within the positive DIAGONAL I\_h-invariant family on K\_TI, (H-ALG) ∧ (H-TR) have the unique solution ρ \= σ \= r \= 1\. PROVEN analytically over all positive reals. LAYER 2 — the physical selection ZS-S14 ⇒ (H-ALG) ∧ (H-TR): NOT PROVEN. Both hypotheses are HYPOTHESIS-strong postulates. The Yang–Mills bridge is therefore DERIVED-CONDITIONAL, not closed. The dimensionless λ₁ closes conditionally; Λ\_QCD \= 264.1 MeV does not, since F-S19.3 remains open.

# **Verification Summary**

**Verification: 212 PASS  |  0 FAIL  |  22 active OPEN (printed, not counted)  |  Zero Free Parameters**  
**Check composition: 183 EXECUTABLE \+ 27 DECLARATIVE \+ 2 PROXY. No executable check is a literal True. Part 28 independently re-derives the v1.5 claims; Part 33 independently cross-checks the v2.1–v2.2 arithmetic uniqueness theorem.** Version 1.0 reported a flat “83/83”; version 1.1 reported 101 executable but two of those, T14 and T92, still carried a literal True. Both are now real computations — T14 verifies the Kirchhoff identity det′(Δ₀) \= V·τ numerically, T92 is the boolean conjunction of T88–T91 — and no executable check anywhere in the suite is a literal True. The anti-regression block is now a real static analysis: the suite parses its own source with the Python ast module, restricted to the production slice, and asserts that forbidden numeric literals occur in no expression.  
Companion code: zs\_s20\_verify\_v2\_2.py. Environment: Python 3.12.3+, numpy 2.4+, mpmath 1.3.0, sympy 1.14.0, scipy 1.17.1; deterministic seed 20260319\. Results block delimited by BEGIN\_ZS\_S20\_RESULTS / END\_ZS\_S20\_RESULTS; SHA256 of the file is emitted by the file itself.  
Pre-registered outcome realised: the numerical branch A\_weights only, under (R) ∧ (H-UA) ∧ (H-UA\*) ∧ (H-SYM). No ledger number moves. **The Yang–Mills physics bridge is NOT closed:** the action-to-Hodge selection step remains OPEN, and gate F-S20.8 — the pre-registered attempt to derive the selection from a single Hermitian operator in ZS-S14 — was executed in this version and **FIRED**. Four candidate selection principles are refuted here with explicit counterexamples: regulator locality (L), the arithmetic-versus-harmonic form of Poincaré-duality invariance, the incidence-intertwiner route, and the claim that (H-UA) ∧ (H-UA\*) alone forces uniformity.

# **§0. Abstract**

ZS-S20 reduces the ZS-S14 SU(3) Yang–Mills master action onto the truncated-icosahedron cell complex K\_TI and asks what fixes the Hodge measure (M₁, M₂) that the reduction requires. Successive versions have returned the same answer with progressively sharper reasons: nothing in ZS-S14 fixes it.  
The negative results are the substance. Hermiticity selects nothing, because the adjoint is defined by M (Theorem S20.O, firing gate F-S20.8). Every positive-definite matrix is already a Gram matrix, so the metric is free data (Theorem S20.N-a). Reading M from the transfer free-energy Hessian returns the M that was put in, exactly and for every positive M (Theorem S20.T1). Register democracy fails because a stationary density is not a kinetic rate; integrality fails for want of an SU(3) charge-lattice bridge; and ρ \= 1 is not symmetry-protected, since the orbit-contrast operator is itself I\_h-invariant. One mechanism runs through all of them: a fixed-point condition built solely from the action admits the action as a solution, and constrains M only if over-determined.  
Closure therefore needs a non-quadratic or coarse-graining step. The compact-group heat-kernel semigroup is verified rather than cited — to 4.3 × 10⁻¹⁴ for U(1) and 2.8 × 10⁻¹⁷ for the non-abelian SU(2) — which makes the face parameter exactly additive under subdivision and the inverse-area law β(A) \= 1/(cA) non-perturbative. That does not fix ρ; it replaces the weight question by an area-measure question.  
Version 2.1 imposes two conditions and keeps their consequences separate from their justification. (H-ALG), integral counting-spectrum degeneracy: the characteristic polynomial of N \= B₂M₁⁻¹B₂ᵀM₂ splits over ℤ into linear factors of multiplicity 1, 4 and 5, a quadratic of multiplicity 5 and a quartic of multiplicity 3\. The multiplicity-5 linear level is not produced by a five-dimensional irreducible representation — it is an accidental collision of a four-dimensional block with a singlet, which is what makes the condition informative. (H-TR), an incidence sum rule: Tr Δ₂ \= 2E \= 180\. Neither has {M uniform} as its solution set.  
Writing X \= ρ, Y \= 1/σ and keeping r explicit, three linear eigenvalues r(3Y+3), r(3Y+5) and rY(5X+3) exist for every positive (X, Y, r), with multiplicities 4, 4 and 1\. A multiplicity-5 linear level can only be 4 \+ 1, giving exactly two branches, ρ/σ \= 1 and ρ/σ \= 3/5. The sum rule fixes r \= 3/(XY \+ Y \+ 1). On the first branch the quintuplet is 9 − 3/(Y+2) ∈ (7.5, 9), whose only integer is 8, forcing ρ \= σ \= r \= 1; on the second the remaining quadruplet is 9 \+ 3/(5Y+8) ∈ (9, 9.375), which contains no integer. Hence, within the positive diagonal I\_h-invariant three-ratio family, M₁ \= M₂ \= m·I uniquely, and λ₁ \= 1.2428416164 at multiplicity three. This is proven over all positive reals; version 2.0 claimed it from a 729-point rational grid and that claim is withdrawn.  
The status is stated in two layers. The arithmetic uniqueness theorem is PROVEN. The physical selection ZS-S14 ⟹ (H-ALG) ∧ (H-TR) is NOT proven: both are HYPOTHESIS-strong postulates, and (H-TR) may be no more than the convention a\_TI \= 1, since r \= 1/a². The Yang–Mills bridge is therefore DERIVED-CONDITIONAL, not closed. The dimensionless λ₁ closes conditionally; Λ\_QCD \= 264.1 MeV does not, gate F-S19.3 being untouched. The theorem is also restricted to the diagonal family: non-diagonal I\_h-equivariant mass matrices and the Whitney/FEEC branch remain open under F-S20.5.  
A by-product stands independently of all of this. The characteristic polynomial of B₂B₂ᵀ factors over ℤ as λ(λ−6)⁴(λ−8)⁵(λ²−10λ+22)⁵(λ⁴−22λ³+166λ²−480λ+380)³, the quartic is irreducible over ℚ, and both ledger eigenvalues are its roots. λ₁ and λ\_h are algebraic integers of degree four with an exact minimal polynomial, where the corpus previously carried ten-digit decimals. That the four roots sum to 22 is Vieta; that 22 \= 2Q reflects the register structure is an observation awaiting a connecting theorem, and version 2.0 overstated it.  
One route was executed and closed negative: restoring the ℓ \= 3 and ℓ \= 4 continuum degeneracies, which I\_h does not protect, splits by 21.3 % and 11.5 % at the counting star with mutually inconsistent minima. Ten rounds of adversarial review produced ten retractions, each recorded with the statement that killed it; six shared one shape, a proxy reported as the target, and the companion carries a PROXY check kind and a basis-label guard in response.

# **§1. Introduction, Honest Assessment, and the Pre-Registration**

## **§1.1 What ZS-S19 left**

The guiding aim of the S-line is unchanged:  
S14 action → measurement instrument → L\_Z transfer operator → gauge observable → data  
ZS-S19 did three things and no more. It proved one candidate route impossible with an interval certificate (Theorem S19.6: Q(t) \> 1 for every t \> 0, min P \= 65.7130202935 \> 0 at u₊ \= 2.2047424786). It removed every false closure of the metric question, including three of its own. And it isolated the real gate. The auditability and falsifiability of the bridge improved a great deal; the positive derivation did not advance at all.  
The sharpest debt ZS-S19 created was against ZS-S14 itself. The master action contains −¼Gᵃ\_μν Gᵃ^μν inside ∫d⁴x √(−g), but it defines neither the projection A\_i^a(x,t) ↦ {q\_e^a(t)} nor the prescription that turns ∫d³x into a sum over cells. Every statement in ZS-S17 through ZS-S19 beginning "the TI reduction of ZS-S14…" presupposes both. **This paper says so first, and then supplies them.**

## **§1.2 The pre-registration, written before any computation**

Stated here, before any result of this paper:  
**PRE-REGISTERED. We compute the I\_h-invariant cellular reduction of the ZS-S14 SU(3) sector and its Legendre transform. The output is the pair (M₁, M₂) and the constraint algebra G\_v. Four outcomes are possible and all four are recorded in advance.**  
Table 1.1. The four pre-registered outcomes of gate F-S19.6.

| OUTCOME | CONTENT | CONSEQUENCE |
| ----- | ----- | ----- |
| A (weights \+ epistemic) | M₁ \= M₂ \= I up to one overall scale. | (R\_C) promoted from HYPOTHESIS-strong to an action-derived prescription; ρ \= (1,1) and λ₁ \= 1.2428416164 become DERIVED; F-S18.16 and F-S19.6 both CLOSE. |
| B | M₁, M₂ diagonal but non-uniform, β₅/β₆ ≠ 1\. | λ₁, λ\_h, Ω₀, c₁, G\_exch and Λ\_QCD must be RECOMPUTED. ZS-S7 revised, not retracted. |
| C | M₁ or M₂ non-diagonal (Whitney / Galerkin). | The entire diagonal-star analysis of ZS-S19 §§3–4 is inapplicable; Δ₂ \= M₂^{1/2}B₂M₁^{−1}B₂ᵀM₂^{1/2}. |
| D | The reduction is inconsistent with (H-UA). | Universal anchoring cannot be adopted as a physical axiom; only the λ₁-channel identity survives; F-S18.16 returns to fully OPEN. |

No outcome is preferred. Outcome A is the only one that leaves the present ledger intact, which is precisely why it must not be assumed. The counting star is the thing being tested; §9 records that no code path in the companion assigns unit weights before the conclusion is reached.

## **§1.3 Zero free parameters and the anti-numerology audit**

ZS-S20 introduces no number of its own. The truncated icosahedron is not a fitted object: it is the ZS-F5 register, **Q** \= 11 \= 3 \+ 6 \+ 2, realised as the Y-sector polyhedral pair mediated by the truncated icosahedron, and the geometric impedance **A** \= δ\_X δ\_Y \= 35/437 is a counting invariant of the same structure. Every quantity in this paper is either (i) a combinatorial invariant of K\_TI, (ii) a locked constant imported without refitting, or (iii) an exact algebraic identity. No fudge factor, no tuned variable, no external constant is introduced. In particular the closure conclusion M₁ \= M₂ \= m·I is scale-free: the value of m never enters, because ZS-S19 Corollary S19.2a shows Δ₂ is exactly invariant under M → sM (verified at s \= 7.3).

# **§2. Step 0 — R\_TI, and the Admission that ZS-S14 Does Not Define It**

## **§2.1 What the master action contains**

ZS-S14 Definition 3.1 gives the SU(3) sector as the continuum term −¼Gᵃ\_μν Gᵃ^μν with the unified covariant derivative on H₅. It contains no cell complex, no lattice spacing, and no measure. This is stated, not inferred: the words "truncated icosahedron" do not appear in the master action.

## **§2.2 The projection, written explicitly**

We define the truncation:  
A\_i^a(x,t) \= Σ\_{e=1}^{90} q\_e^a(t) ω\_e(x) \+ A\_⊥^a(x,t),   with A\_⊥ → 0\.  
The choice of {ω\_e} **is** the choice of route, so we state it here in §2 rather than discover it in §7. We take {ω\_e} to be an abstract one-cochain basis of K\_TI, and the setting to be internal-mode gauge quantum mechanics on ℝ\_t × K\_TI — not a lattice embedded in physical three-space. The justification is ZS-F5's dim(**Z**) \= 2: the Z-sector stage is two-dimensional, so K\_TI is the whole spatial complex, and time is the only additional direction. This is the most consistent reading of the corpus, and it is what makes ZS-S7's regulator axiom (R) — that the truncated icosahedron **is** the ultraviolet regulator, not a discretisation of an ambient metric — coherent rather than merely stipulated.

## **§2.3 Route W is not disfavoured; under (R) it is undefined**

The Whitney / Galerkin route defines the inner product by ⟨W\_σ, W\_σ′⟩ \= ∫ W\_σ ∧ ⋆W\_σ′. The symbol ⋆ there is the continuum Hodge star of an ambient Riemannian metric. Under (R) no such metric exists. The Whitney inner product is therefore not merely disfavoured on this complex; it is ill-posed. \[DERIVED-CONDITIONAL on (R)\]  
Consequence: NC-S19.16, which recorded that Theorem S19.6 does not exclude Outcome C, is resolved by naming (R). Outcome C is excluded by the regulator axiom, not by the Regge geometry. We flag the dependency explicitly rather than bundling it into a general claim.

# **§3. Steps 1–3 — Holonomies, A₀, and the Most General I\_h-Invariant Lagrangian**

Link and face holonomies (Step 1):  
U\_e(t) \= P exp(i g ∫\_e A) ∈ SU(3),   U\_e \= exp(i g q\_e^a T^a),   U\_f \= Π\_e U\_e^{(B₂)\_{fe}},  
with the gauge action U\_e ↦ h\_{s(e)} U\_e h\_{t(e)}^{−1}, h\_v ∈ SU(3). We keep A₀ (Step 2\) and do not gauge it away before the Legendre transform; dropping it here loses the Gauss law and is the single most likely way to get a wrong answer:  
D\_t U\_e \= U̇\_e \+ i A\_{0,s(e)} U\_e − i U\_e A\_{0,t(e)},   Ω\_e \= −(i/g) U\_e† D\_t U\_e \= Ω\_e^a T^a.  
The most general I\_h-invariant local Lagrangian (Step 3\) is written before any diagonality is assumed:  
L\_TI \= (1/2g²) Ωᵀ M₁ Ω − (2/g²) Σ\_f β\_f \[N − Re Tr U\_f\],  
M₁ ∈ ℝ^{90×90},   M₂ \= diag(β\_f) ∈ ℝ^{32×32}   — diagonality is NOT assumed.  
We state the parameter count **before** any scan, as ZS-S19 §3.4 requires. If M₁ and M₂ turn out diagonal, I\_h invariance leaves two values each — m₅₆, m₆₆ and β₅, β₆ — because I\_h has exactly two orbits on edges (60 and 30\) and two on faces (12 and 20). After the overall scale that is three independent ratios, not two and not one. All four orbit counts and the group order |I\_h| \= 120 are verified in the companion (checks T15–T18), together with the equivariance residual \[P\_F, |B₂|\] \= 0 over all 120 elements (T19).

# **§4. Steps 5–6 — Lemma S20.T and the Legendre Transform**

## **§4.1 The kinetic term from a time-like plaquette, not from the Haar measure**

ZS-S19 v1.2 withdrew a derivation that had obtained M₁ ∝ I from Haar democracy. The withdrawal was correct: Haar fixes the integration measure, not the kinetic coefficients, and I\_h permits κ₅₆ ≠ κ₆₆. The repair is to take the electric coefficients from an action. Discretise time on K\_TI × ℤ\_t and, for each spatial link, form  
P\_{e0}(n) \= U\_{0,s(e)}(n) U\_e(n+1) U\_{0,t(e)}(n)^{−1} U\_e(n)^{−1},  
S\_Δt \= Σ\_n \[ (2/g²Δt) Σ\_e c\_e (N − Re Tr P\_{e0}) \+ (2Δt/g²) Σ\_f β\_f (N − Re Tr U\_f) \].  
Since N − Re Tr U \= ¼ g² q^a q^a \+ O(q⁴) for SU(3) with Tr(T^aT^b) \= ½δ^{ab} (verified to 10⁻¹² in check T35, with the normalisation itself checked in T35a), one has N − Re Tr P\_{e0} \= (g²Δt²/4) Ω\_e^aΩ\_e^a \+ O(Δt³) and the Δt → 0 limit gives L\_E \= ½ Σ\_e c\_e Ω\_e² directly. The electric coefficients now come from an action, the Gauss law is automatic, c\_e and β\_f are comparable within one discrete action, and transfer-matrix positivity becomes checkable.

## **§4.2 Lemma S20.T (Temporal-Plaquette Reduction)**

**Lemma S20.T.** On K\_TI × ℤ\_t with a product regulator measure μ\_K \= μ\_TI ⊗ μ\_t, the weight of the time-like two-cell e × I is w(e × I) \= μ₁(e)·Δt, and hence (M₁)\_e \= μ₁(e): the electric coefficient is the one-cell measure of the spatial complex. It carries no ambient metric and is not derived from any measure on the group. \[DERIVED\]  
**This is a reduction, not a selection, and we insist on the distinction.** It converts the question "which metric?" into the strictly narrower question "which one-cell measure?" — precisely the object that ZS-M44, ZS-F38 and ZS-F39 have been contesting elsewhere in the corpus. It does not by itself determine μ₁. Any claim that it does is refuted in §6.

## **§4.3 Step 6 — the Legendre transform, both forms printed**

ZS-S19 v1.2 carried an error for two versions because it named a Hamiltonian coefficient without performing the Legendre inverse. Both forms are therefore printed here side by side and labelled:  
Π\_e^a \= ∂L/∂Ω\_e^a \= (1/g²)(M₁)\_{ee′} Ω\_{e′}^a  
H\_E \= (g²/2) Πᵀ M₁^{−1} Π    ⟹    κ\_e \= (M₁^{−1})\_e  
H\_B \= (2/g²) Σ\_f β\_f \[N − Re Tr U\_f\]  
Table 4.1. The two forms of star compatibility. They are different functions and must never be interchanged.

| VARIABLES | RELATION | MEAN |
| ----- | ----- | ----- |
| Lagrangian (M₁, M₂) | (M₁)\_e \= ½(β\_{f₁} \+ β\_{f₂}) | arithmetic mean of the face weights |
| Hamiltonian (κ, b \= 1/β) | κ\_e \= (M₁^{−1})\_e \= 2/(β\_{f₁} \+ β\_{f₂}) | harmonic mean of the inverse face weights |

After quantisation Π\_e^a is the left/right-invariant vector field, that is the electric generator E\_e^a. Check AR2 of the companion asserts that no code path uses the arithmetic form as the Hamiltonian relation.

# **§5. Step 7 — The Non-Abelian Gauss Law and the 59 \+ 31 Census**

Varying A₀ gives, with ρ\_v \= 0 for pure glue,  
G\_v^a \= Σ\_{e: s(e)=v} E\_e^a − Σ\_{e: t(e)=v} (Ad\_{U\_e^{−1}} E\_e)^a \= 0\.  
Sixty vertex constraints minus one global mode give 59 independent gauge directions. ZS-S19 proved this census is metric-free — it is the rank of B₁ᵀ and of B₂ᵀ — so it must come out at 59 \+ 31 in every outcome, and it is the first regression test on any new incidence matrices. The companion verifies rank B₁ᵀ \= 59, rank B₂ᵀ \= 31, 59 \+ 31 \= 90 (checks T10–T12), and B₂B₁ᵀ \= 0 to better than 10⁻¹² (T07), on a complex rebuilt from Cartesian coordinates rather than imported.  
The structural point for what follows: **the Gauss law is a statement about B₁ alone.** The electric register is the edge set as seen by the vertex incidence, not as seen by the face incidence. §10 shows this distinction is exactly what separates the uniform answer from the degree-biased one.

# **§6. Adversarial Review — Two Candidate Axioms Refuted Before Use**

ZS-S19 issued four self-retractions across five review cycles, every one caught by review rather than by the author, and three of the six were inflicted by the repair rather than by the original error. We assume the same of ZS-S20 and therefore submit the two candidate axioms of the exploration phase to adversarial review here, in §6, before any theorem of this paper is allowed to depend on them. Both fail. Both are retracted.

## **§6.1 Candidate axiom (L), regulator locality — RETRACTED**

The candidate stated that the regulator weight of a cell depends only on the isomorphism class of that cell. On K\_TI × ℤ\_t every time-like two-cell is a square while spatial two-cells are pentagons and hexagons, so (L) would give c\_e uniform at once.  
**Counter (L-A), the stabiliser objection.** I\_h has two orbits on edges with stabiliser orders |I\_h|/60 \= 2 and |I\_h|/30 \= 4 (check T37). An orbit-indexed measure is perfectly I\_h-invariant and non-uniform. Symmetry alone therefore cannot select, and (L) is an assumption strictly beyond symmetry. This counter weakens (L) but is not fatal to it.  
**Counter (L-B), the anisotropy objection — FATAL.** On a hypercubic lattice the temporal and spatial plaquettes are both squares, yet they carry different couplings β\_τ ≠ β\_s; the Hamiltonian limit requires precisely that anisotropy. The combinatorial cell type therefore does not fix the weight, in the one setting where the answer is known independently. (L) is false as stated.  
**Verdict.** (L) is RETRACTED as a selection principle. What survives the counter is exactly Lemma S20.T: the product structure of K\_TI × ℤ\_t identifies the temporal weight with the spatial one-cell measure μ₁, which is a reduction and not a determination. Check AR8 asserts that no code path uses (L) as a selection.

## **§6.2 Candidate axiom (H-PD) in its arithmetic-versus-harmonic-mean form — RETRACTED**

The candidate observed that star compatibility reads as an arithmetic mean in Lagrangian variables and as a harmonic mean in Hamiltonian variables (Table 4.1), and proposed to demand that the two forms coincide. By the equality condition of the arithmetic–harmonic mean inequality this forces β\_{f₁} \= β\_{f₂} on every edge and hence, the face-adjacency graph being connected, β constant.  
**Counter (PD-A).** The Legendre transform is not supposed to preserve coefficients. For a free particle L \= ½mv² and H \= p²/2m, and nobody demands m \= 1/m. A blanket "form invariance under Legendre" is simply false.  
**Counter (PD-B) — FATAL.** The proposal misidentifies the dual incidence. In two dimensions the Hodge star maps a face to a dual vertex, an edge to a dual edge, and a vertex to a dual face. Hence the dual edge ⋆e is bounded by the two dual faces ⋆v₁ and ⋆v₂, where v₁, v₂ are the **endpoints** of e — not by ⋆f₁ and ⋆f₂. The dual compatibility relation therefore involves the zero-cell weights, not the two-cell weights, and the arithmetic-versus-harmonic identification never arises.  
**Verdict.** The arithmetic-versus-harmonic form of (H-PD) is RETRACTED. Check AR9 asserts that no code path produces it. But counter (PD-B) is constructive: implemented correctly it yields Theorem S20.D of §7, which is both stronger and cleaner than the retracted version, and which uses no inequality at all. We record that the theorem the paper actually rests on was obtained by taking the refutation seriously, not by patching the original claim forward.

# **§7. Theorem S20.D — Dual Compatibility Plus Weight Equivariance Forces M₁ Uniform**

## **§7.1 The axiom, stated as a formula and never paraphrased**

ZS-S19 registered universal harmonic anchoring on the primal complex:  
(H-UA)   ⟨h, Θ(a\_α, a\_β)⟩ \= δ\_{αβ}(λ − 2)/λ  in EVERY eigen-channel of Δ₂,  
which by Theorem S19.2′ is equivalent, given two independent channels, to pointwise star compatibility (M₁)\_e \= ½(β\_{f₁} \+ β\_{f₂}). ZS-S20 adds:  
(H-UA\*)   The same demand holds on the dual complex ⋆K\_TI.  
**(H-UA\*) is a HYPOTHESIS-strong structural axiom and is registered as gate F-S20.2. It is not a theorem of ZS-S14 and this paper does not claim it is.** Its content is a symmetry statement, not a value assignment: it says that the criterion by which weights are judged to come from one geometry cannot depend on whether the complex is labelled primal or dual. It is strictly weaker than (R\_C), which assigns the value 1 to every cell.  
A third condition was used silently in version 1.0 and is now stated and counted:  
(H-SYM)   M is invariant under the automorphism group I\_h of K\_TI.  
**(H-SYM) is load-bearing, not cosmetic.** §15 exhibits an explicit positive non-uniform solution of (H-UA) ∧ (H-UA\*) on K\_TI. Version 1.0 obtained α\_v \= α from vertex-transitivity of the **complex**; that step in fact requires invariance of the **weights**, which is (H-SYM). The correction does not change any conclusion, but it changes the axiom count from two conditions to four.

## **§7.1a Proposition S20.P — (H-UA) and (H-UA\*) are one functional applied to two complexes**

The referee asks whether (H-UA) and (H-UA\*) are two restrictions of a single operator identity or two independent assumptions. The answer is the first, and it can be made precise. Define the block Hodge star as the degree-reversing diagonal map  
⋆ \= (⋆₀, ⋆₁, ⋆₂),   ⋆\_k : C^k(K) → C^{2−k}(⋆K),   ⋆\_0 \= M₀, ⋆\_1 \= M₁, ⋆\_2 \= M₂,  
with the standard discrete-exterior-calculus convention that the weight of a dual cell is the reciprocal of the weight of its primal partner, w\_{⋆K}(⋆σ) \= 1/w\_K(σ) \[20, 21, 44\]. The codifferential is then the single operator identity  
δ \= ⋆⁻¹ d\_{⋆K} ⋆,  
whose two degree components are exactly δ₁ \= M₀⁻¹B₁M₁ on C¹ → C⁰ and δ₂ \= M₁⁻¹B₂ᵀM₂ on C² → C¹. Now let Φ be the single anchoring functional  
Φ :  “the weight of a 1-cell is the arithmetic mean of the weights of the two 2-cells it bounds.”  
**Proposition S20.P.** Φ applied to K is (H-UA): m\_e \= ½(β\_{f₁} \+ β\_{f₂}). Φ applied to ⋆K is (H-UA\*): 1/m\_e \= ½(1/α\_{v₁} \+ 1/α\_{v₂}), the reciprocals arising from the dual-weight convention rather than from any added assumption. Hence (H-UA) and (H-UA\*) are one functional evaluated on two complexes. \[PROVEN\]  
**The honest qualification.** Sameness of **form** is not logical dependence. Φ(K) and Φ(⋆K) are two conditions and are counted as two throughout this paper. What Proposition S20.P buys is that the pair is not ad hoc: it is a single demand, made twice, of a structure that Poincaré duality says should not privilege the primal labelling. Version 1.0’s phrase “one axiom applied twice” is accurate as a description of the form and inaccurate as a count; both readings are now stated explicitly.

## **§7.2 The dual complex of K\_TI**

⋆K\_TI has 32 vertices (one per face), 90 edges (one per edge), and 60 faces (one per vertex); each dual face has the degree of its primal vertex, namely 3, so every dual face is a triangle and ⋆K\_TI is the pentakis dodecahedron. χ(⋆K) \= 32 − 90 \+ 60 \= 2\. Checks T40–T42.

## **§7.3 Statement and proof**

**Theorem S20.D (Dual Compatibility with Weight Equivariance).** Let K be a closed two-complex whose vertex set is a single orbit under Aut(K), let the weight assignment M be Aut(K)-invariant — hypothesis (H-SYM) — and assume star compatibility on ⋆K. Then the primal one-cell weights are uniform: m\_e \= α for all e, where α is the common zero-cell weight. The equivariance hypothesis is not decorative: §15 exhibits an explicit positive non-uniform solution when it is dropped.  
**Proof.** Star compatibility on ⋆K relates the weight of a dual edge to the weights of the two dual faces bounding it. The dual edge ⋆e is bounded by ⋆v₁ and ⋆v₂ with v₁, v₂ the endpoints of e. In the dual variables the one-cell weight is (M₁^⋆)\_{⋆e} \= 1/m\_e and the two-cell weight is β^⋆\_{⋆v} \= 1/α\_v, so compatibility reads  
1/m\_e \= ½ ( 1/α\_{v₁} \+ 1/α\_{v₂} ).  
If Aut(K) acts transitively on vertices AND the weights are Aut(K)-invariant, then α\_v \= α for all v, whence 1/m\_e \= 1/α for every e, that is m\_e \= α. \[PROVEN\]  
**Application to K\_TI.** The truncated icosahedron is vertex-transitive under I\_h: the companion constructs all 120 orthogonal maps preserving the vertex set and finds a single vertex orbit of size 60 (checks T15, T16). Substituting the uniform α gives a spread of exactly 0.0 in 1/m\_e (check T43), and the 90 × 60 dual-incidence system has full rank 60 (check T44), so the conclusion is not an artefact of an under-determined system. Hence  
**M₁ \= m · I₉₀.**  
\[DERIVED-CONDITIONAL on (H-UA\*)\]  
Two remarks against interest. First, vertex-transitivity is doing real work: on a complex with two vertex orbits the theorem gives nothing. Second, the theorem determines M₁ only up to the scale α, which is exactly the freedom ZS-S19 Corollary S19.2a removes.

# **§8. Theorem S20.U — Uniform M₁ Forces M₂ Uniform**

**Theorem S20.U (Uniformity Transfer).** Let K be a closed two-complex whose face-adjacency graph G\_F is connected and non-bipartite. Assume star compatibility on K and that M₁ is uniform, (M₁)\_e \= m for all e. Then M₂ is uniform and M₂ \= M₁ \= m·I.  
**Proof.** Compatibility with uniform M₁ gives β\_{f₁} \+ β\_{f₂} \= 2m on every edge. Set δ\_f := β\_f − m. Then δ\_{f₁} \= −δ\_{f₂} whenever f₁ and f₂ share an edge, so δ is an alternating labelling on G\_F. Traversing an odd cycle returns δ \= −δ, hence δ ≡ 0 on that cycle; connectedness propagates δ ≡ 0 to all of G\_F. Therefore β\_f \= m for every face, and by compatibility (M₁)\_e \= ½(m \+ m) \= m. \[PROVEN\]  
**Why non-bipartiteness is essential.** On a bipartite G\_F the alternating labelling δ\_f \= ±t survives for any t, and a one-parameter family of non-uniform M₂ would remain. The theorem is therefore not a formality; it is a property of the truncated icosahedron.  
On K\_TI the companion verifies: G\_F connected (32/32, check T46); non-bipartite, with the explicit 3-cycle hexagon–pentagon–hexagon (check T47) — two hexagons adjacent to a common pentagon are themselves adjacent, since a pentagon of the truncated icosahedron is surrounded entirely by hexagons and consecutive ones share an edge; the 90 × 32 incidence system has rank 32 and alternating nullity exactly zero (check T48); and the forced solution is β ≡ 1 with min \= max to twelve decimals and residual below 10⁻¹⁰ (checks T49, T50).

# **§9. Corollary S20.A — Numerical Branch A\_weights, and What May Be Said About (R\_C)**

Combining §7 and §8 in the I\_h-invariant diagonal parametrisation is a single line. Primal compatibility gives m₅₆ \= ½(β₅ \+ β₆) and m₆₆ \= β₆, because every (6,6)-edge bounds two hexagons and every (5,6)-edge bounds one pentagon and one hexagon and there are no (5,5)-edges (check T09). Theorem S20.D gives m₅₆ \= m₆₆ \= α. Hence ½(β₅ \+ β₆) \= β₆, so β₅ \= β₆ \= α.  
**Corollary S20.A (Counting-Star Selection).** Under (R), (H-UA), (H-UA\*) and (H-SYM), the cellular reduction of the ZS-S14 SU(3) sector on ℝ\_t × K\_TI yields M₁ \= M₂ \= α·I. The overall scale α is removed exactly by ZS-S19 Corollary S19.2a, so  
**Δ₂ \= B₂B₂ᵀ,    λ₁ \= 1.2428416164 (threefold),    Ω₀ \= √λ₁ \= 1.1148280659.**  
\[DERIVED-CONDITIONAL on (R) ∧ (H-UA) ∧ (H-UA\*) ∧ (H-SYM)\]  
**What Corollary S20.A does and does not establish.** It reproduces, conditionally, the **spectral consequence** previously obtained from (R\_C). It does **not** derive the literal cellular counting trace. By Theorem S20.E no reduction in logical strength is obtained on K\_TI; only the formulation has changed. What is realised is therefore the **numerical branch A\_weights**, not the epistemic Outcome A of Table 1.1, whose second clause — that (R\_C) be promoted to an action-derived prescription — is refuted by Theorem S20.N of §17. Gates F-S18.16a and F-S19.6a CLOSE; F-S18.16b and F-S19.6b remain OPEN-TERMINAL. No number in the ledger moves; check AR9 asserts λ₁ is unchanged to ten digits.

# **§10. Independent Corroboration and the Exclusion of ρ\_F \= 5/6**

## **§10.1 Which registers on K\_TI are uniform?**

Corollary S20.A rests on (H-UA\*). It is worth asking whether an entirely independent line of the corpus points the same way. ZS-F38 Theorem T1′ proves that an irreducible doubly stochastic transition on a finite register has the uniform measure as its unique stationary state, by Perron–Frobenius and Birkhoff–von Neumann; ZS-F39 Lemma SEL proves that the equivariant lift is the state density while the size-biased transport weight is never a state density. Transplanting T1′ from the Q-slot register to the edge register of K\_TI gives a sharp dichotomy.  
Table 10.1. Stationary measures of the natural registers on K\_TI. B₁-generated registers on the edge set are uniform; B₂-generated registers are degree-biased.

| REGISTER | GENERATED BY | DEGREES | STATIONARY |
| ----- | ----- | ----- | ----- |
| edge–edge, sharing a vertex (line graph) | B₁ | {4} — 4-regular | uniform |
| vertex–edge incidence walk | B₁ | edges have 2 endpoints | uniform on E |
| edge–edge, sharing a face | B₂ | {9, 10} | ratio 9/10 |
| face–face adjacency (dual walk) | B₂ | {5, 6} | ratio 5/6 |

The line graph of a 3-regular graph is 2(3 − 1\) \= 4-regular; the walk is therefore doubly stochastic and, being irreducible (rank(I − P) \= 89), has the uniform measure as its unique stationary state, confirmed by P⁴⁰⁰⁰ agreeing with J/90 to better than 10⁻¹² (checks T55–T58). \[IMPORTED-PROVEN mathematics; DERIVED-CONDITIONAL as a physical statement\]  
The Gauss law G\_v^a is a statement about B₁ and about nothing else (§5). The electric register is therefore B₁-generated, and every B₁-generated register on the edge set of K\_TI is uniform. This is an **independent corroboration** of Theorem S20.D and not a second proof of it; it is tagged as such and no ledger value depends on it.

## **§10.2 The degree-biased candidate is CLOSED-NEGATIVE**

The competing reading is the size-biased one, natural in the ZS-F37 line: weigh a face by its degree. On K\_TI this gives exactly ρ\_F \= β₅/β₆ \= 5/6, the dual walk's stationary ratio (check T62), and it is one of the five sensitivities ZS-S19 pre-registered. Under primal compatibility it forces m₅₆/m₆₆ \= 11/12 ≠ 1 (check T63), contradicting Theorem S20.D. It is therefore **CLOSED-NEGATIVE** under (H-UA\*).  
Had it held, λ₁ \= 1.2155777721, a shift of −2.1937 %, and Λ\_QCD \= 270.0 MeV. We report the number that would have followed rather than only the exclusion. We also record, and decline to use, the fact that 11/12 contains the register integer 11; reading significance into it would be exactly the numerology this corpus exists to avoid.  
ZS-F39 Lemma SEL is the reason the two readings need not be in conflict at the level of the corpus: the size-biased weight is a transport weight and the object M₁ is a state density. NC-S20.4 below records that ZS-S20 does not overturn ZS-F37.

# **§11. Step 8 — The Regression Gate, and the Acceptance Tests**

Expanding U\_e \= exp(i g q\_e) gives U\_f \= exp\[i g (B₂q)\_f \+ O(g²)\] and  
H^{(2)} \= (g²/2) Eᵀ M₁^{−1} E \+ ½ qᵀ B₂ᵀ M₂ B₂ q,    q̈ \+ M₁^{−1} B₂ᵀ M₂ B₂ q \= 0\.  
The reduction is acceptable only if it returns the generalised eigenproblem M₁^{−1}B₂ᵀM₂B₂ a \= λa. The companion checks this in two independent ways: it builds genuine SU(3) link variables at g \= 10⁻⁵, forms the face holonomies by ordered products with the orientations read from B₂, extracts Y\_f \= −i log(U\_f)/g and finds max|Y\_f − (B₂q)\_f| \= 1.3 × 10⁻⁴, of order g as required (check T35b); and it confirms that the 31 non-zero eigenvalues of M₁^{−1}B₂ᵀM₂B₂ on the 90-dimensional edge space coincide with the 31 non-zero eigenvalues of Δ₂ on the 32-dimensional face space (check T35c). The gate PASSES, so the projection R\_TI of §2 is acceptable and Steps 1–7 need not be redone.  
Table 11.1. Acceptance tests of ZS-S19 §4.3. All are reproduced from a complex rebuilt from Cartesian coordinates.

| TEST | TARGET | OBTAINED | CHECK |
| ----- | ----- | ----- | ----- |
| gauge census | rank B₁ᵀ \= 59, rank B₂ᵀ \= 31 | 59, 31 | T10–T12 |
| eigenproblem form | M₁^{−1}B₂ᵀM₂B₂ a \= λa | recovered | T35b, T35c |
| I\_h equivariance | \[P\_F, B₂\] residual 0 over 120 elements | \< 10⁻¹² | T19 |
| Route C spectrum | λ₁ \= 1.2428416164, threefold | exact | T20, T21 |
| second T₁ copy | λ\_h \= 7.5210904061 | exact | T22 |
| full L₂ spectrum | 9 levels, multiplicities summing to 32 | exact | T23–T25 |
| Ω₀ | 1.1148280659 | exact | T26 |
| scale gauge | Δ₂ invariant under M → sM | exact at s \= 7.3 | T27 |
| S19 counterexample | W₅₆ \= \+0.323137, W₆₆ \= −2 | exact | T28, T29 |
| full-DEC gap at a\_TI \= 1 | 0.3600376672 (−71.031 %) | exact | T32 |
| a\_TI reproducing the lock | 0.5382277383 | exact | T33 |
| FP zeroth order | det′Δ₀ \= 60 × 375291866372898816000 | exact integer | T13, T14 |
| star compatibility | (M₁)\_e \= ½(β\_{f₁} \+ β\_{f₂}) | satisfied at Outcome A | T49–T53 |

The Kirchhoff identity is the fastest way to detect a silent sign error in a rebuilt B₁ or B₂, and it is exact: the 59 × 59 reduced Laplacian determinant is the integer 375291866372898816000 at 60-digit precision.

# **§12. Anti-Numerology — A Pre-Registered Test That Came Back Negative**

Pre-registered before execution: under the null hypothesis that ρ \= β₅/β₆ is drawn log-uniformly on \[1/4, 4\], compute the probability that |λ₁(ρ)/λ₁(1) − 1| falls inside the corpus band 89/3600 \= 2.4722 %. Decision rule fixed in advance: if that probability exceeds 5 %, the band is not a discriminator and no support may be claimed from the fact that Outcome A leaves the ledger intact.  
**Result: p \= 33.82 % at N \= 200 000, seed 20260319; the in-band interval is ρ ∈ \[0.8190, 2.0849\]. The test fails.** We therefore state plainly that ledger survival is **not** evidence for Outcome A, and no argument anywhere in this paper appeals to it. Checks T68 and T69 record the execution and the verdict.  
The claim itself, however, is not of the kind anti-numerology tests. Theorem S20.D reduces to the observation that a constant plus a constant divided by two is that constant; Theorem S20.U reduces to the observation that an alternating labelling vanishes on an odd cycle. Both are algebraic identities with zero tunable content, and the selected value ρ \= 1 is the unique root of (ρ \+ 1)/2 \= 1 (check T51), a measure-zero point. Anti-numerology does not apply to an identity. Both statements are reported; neither is used to prop up the other.  
For calibration: over the same window the unrestricted three-ratio family spans λ₁ by a factor of 94.5, star compatibility alone reduces the span to a factor of 1.69, and Corollary S20.A reduces it to a point.

# **§13. Erratum, Status Delta, Falsification Gates, and Non-Claims**

## **§13.1 Erratum against ZS-S19 §1.1**

ZS-S19 §1.1 lists the truncated-icosahedron face areas at unit edge as A₅ \= 1.7204774006, A₆ \= 2.5980762114 and A₆/A₅ \= 1.5100871129. The first two are correct. The ratio is not: exactly,  
A₆/A₅ \= 6√(15 − 6√5)/5 \= 1.5100902868,  
which differs from the tabulated value in the sixth decimal. The error does not propagate — the circumcentric route is CLOSED-NEGATIVE and the full-DEC gap 0.3600376672 is reproduced here from the exact areas — but the ZS-S19 table should be corrected. Checks T30, T31, T34 and AR7.

## **§13.2 Status delta**

Table 13.1. What ZS-S20 changes in each upstream paper.

| PAPER | CHANGE | NEW STATUS |
| ----- | ----- | ----- |
| ZS-S7 | λ₁ \= 1.2428416164 and Λ\_QCD \= 264.1 MeV keep their values. Their status changes: no longer DERIVED-CONDITIONAL on (R\_C), now DERIVED-CONDITIONAL on (R) ∧ (H-UA) ∧ (H-UA\*) ∧ (H-SYM). §1's regulator axiom (R) should be promoted from a remark to a stated axiom, as it is load-bearing for the exclusion of Route W. §2.2's face-representation claim remains formally uncorrected in ZS-S7 itself. | Revised, not retracted. |
| ZS-S14 | The projection R\_TI and the cellular integration prescription are supplied by ZS-S20 §2 and §4 and should be back-referenced. ZS-S14 itself is unchanged; the debt recorded in ZS-S19 §3.2 is discharged by an external supply, not by a correction to ZS-S14. | Debt discharged. |
| ZS-S17 | All O(g²) results stand at the same values and remain DERIVED-PERT-COND. λ\_h \= 7.5210904061 reconfirmed independently. | Unchanged. |
| ZS-S18 | The gate is SPLIT. F-S18.16a (reduction to a finite metric family) CLOSES; F-S18.16b (selection of ρ from the ZS-S14 inner product) is OPEN-TERMINAL by Theorem S20.N. The census 90 \= 59 \+ 31 is reconfirmed as metric-free and survives, as ZS-S18 predicted, in every outcome. c₁, G\_exch and the Sym² block structure are unaffected. | F-S18.16a CLOSED; F-S18.16b OPEN-TERMINAL. |
| ZS-S19 | The gate is SPLIT. F-S19.6a (explicit projection, plaquette reduction, Legendre transform, Gauss law) CLOSES; F-S19.6b (action-level determination of M₁, M₂) does NOT close and is OPEN-TERMINAL relative to ZS-S14 alone. Theorem S19.7 is superseded as a derivation but not as a statement: its conclusion is now Corollary S20.A, conditionally. Theorem S19.6 keeps its full force. NC-S19.15 is resolved. NC-S19.16 is resolved by naming (R). The A₆/A₅ erratum of §13.1 applies to §1.1. | F-S19.6a CLOSED; F-S19.6b OPEN-TERMINAL. |

## **§13.3 Falsification gates**

Table 13.2. Falsification registry. Multi-layer: mathematical collapse, simulation/consistency collapse, and observational collapse.

| GATE | CONDITION THAT FIRES IT | LAYER / STATUS |
| ----- | ----- | ----- |
| F-S20.2 (restated in v1.1) | The discrete codifferential is shown not to be the transpose of the differential on K\_TI — equivalently (H-IR) fails, equivalently (H-UA) ∧ (H-UA\*) ∧ (H-SYM) is shown incompatible with the ZS-S14 reduction. By Theorem S20.E all four hypothesis sets fall together, Corollary S20.A fails, and the paper reverts to Outcome D. | Mathematical / theoretical collapse — immediate rejection. OPEN. This is the corpus's single remaining structural failure point on the Yang–Mills bridge. |
| F-S20.4 | A closed two-complex is exhibited that is vertex-transitive, has a non-bipartite face-adjacency graph, satisfies star compatibility on both K and ⋆K, and admits a non-uniform diagonal metric. Theorem S20.D or S20.U would then contain an error. | Mathematical collapse — immediate rejection. OPEN. |
| F-S20.5 | An independent cellular reduction of ZS-S14 on ℝ\_t × K\_TI returns a non-diagonal M₁ or M₂ without violating (R). Outcome C would then be live and ZS-S19 §§3–4 and this paper's §§7–9 would require rewriting in full matrix form. | Simulation / consistency collapse — revision required. OPEN. |
| F-S20.6 | The B₁-generated edge register is shown not to be the electric register — for instance if the constraint algebra of §5 is shown to require a face-indexed measure. The §10 corroboration would fail, though Corollary S20.A would survive on (H-UA\*) alone. | Consistency collapse — corroboration only. OPEN. |
| F-S20.7 | A lattice or continuum determination of Λ\_QCD in the quenched theory, matched to the ZS-S22 scheme, falls outside \[261.6, 275.3\] MeV by more than the quoted uncertainty at the fixed a\_TI of ZS-S22. | Observational collapse — external data. OPEN, deferred to ZS-S22. |
| F-S20.8 | The reduction generates a weighted adjoint δ \= M⁻¹d^T M, so that self-adjointness holds automatically for every M and imposes no condition. Pre-registered by the referee before execution. | Mathematical / theoretical. EXECUTED IN v1.1 — FIRES (Thm S20.O). Intertwiner route CLOSED-NEGATIVE. |
| F-S20.9a / F-S20.9b | overall normalisation Z\_E \= Z\_B / orbit contrast Δβ\_R \= 0 | SPLIT in v1.2. 9a does not determine ρ; 9b is the live gate. Both OPEN, deferred to ZS-S21. |
| F-S20.10 | A full Whitney/FEEC mass matrix on K\_TI, computed under an adopted ambient metric, fails to preserve the T₁ representation content or the exactness of the gauge zero modes, or fails to converge under refinement. | Simulation / consistency. OPEN, criteria restated in §16.3. |
| F-S19.6 | Discretising the ZS-S14 canonical action on the TI and Legendre-transforming yields β₅ ≠ β₆. | EXECUTED. Does not fire. CLOSED. |
| F-S18.16a / F-S18.16b | reduction to a finite metric family / selection of ρ from the ZS-S14 inner product | a: EXECUTED, CLOSED.  b: OPEN-TERMINAL (Thm S20.N-a, S20.T1). |

## **§13.4 Non-claims**

NC-S20.1 (corrected in v1.1). ZS-S20 does NOT derive (H-UA), (H-UA\*), (H-SYM) or (H-IR) from ZS-S14. All are added structural axioms. The paper claims NO reduction in postulate count relative to ZS-S19: Theorem S20.E shows that on K\_TI every hypothesis set considered here is equivalent to the spectral content of (R\_C). What is claimed is a change of form, from an integration prescription to a symmetry-level compatibility condition, and the removal of the primal/dual asymmetry. Version 1.0's claim of one fewer postulate is withdrawn (§17).  
NC-S20.8 (new in v1.1). ZS-S20 does NOT close the Yang–Mills bridge. The action-to-Hodge selection step is OPEN. Theorem S20.O proves that Hermiticity of the reduced operator is not a selection principle, and gate F-S20.8 fired.  
NC-S20.9 (new in v1.1). ZS-S20 does NOT claim that Theorem S20.R derives M \= m·I from physics. It derives it from the commutant condition, which is itself an axiom of the same logical strength as the counting star.  
NC-S20.10 (new in v1.1). ZS-S20 does NOT claim that a non-diagonal mass matrix would refute the corpus. It would refute the diagonal counting model. §16.3 restates the success criteria for that eventuality in advance.  
NC-S20.2. ZS-S20 does NOT run the Lanczos, does NOT compute the non-perturbative spectrum, and does NOT fix a\_TI or match schemes. Those are ZS-S21 and ZS-S22.  
NC-S20.3. ZS-S20 does NOT establish perturbative control at λ\_t ≈ 5.54. Every O(g²) statement in ZS-S17 through ZS-S20 remains DERIVED-PERT-COND.  
NC-S20.4. ZS-S20 does NOT overturn ZS-F37's size-biased two-leg law. It excludes the degree-biased weight for M₂ specifically, on the ground that M₂ is fixed by compatibility with a state density; ZS-F39 Lemma SEL already separates the two objects.  
NC-S20.5. ZS-S20 does NOT claim that Theorem S20.D is a theorem about the ZS-S14 action. It is a theorem about closed two-complexes; its application to K\_TI is DERIVED-CONDITIONAL on (H-UA\*).  
NC-S20.6. ZS-S20 does NOT re-run the retracted −3.868 % alarm, does NOT re-derive the anchoring defect identity, Theorem S19.6 or the Magnus quartic, and does NOT report any fixed machine residual as a ledger value. Thresholds only.  
NC-S20.7. ZS-S20 does NOT claim the exclusion of Route W holds "everywhere" or "completely". The audited domain is exactly: closed two-complexes carrying no ambient Riemannian metric, under (R).

# **§14. Route 1 — The Incidence Hodge–Dirac Operator, and the Firing of Gate F-S20.8**

## **§14.1 The pre-registration, stated before execution**

The referee proposed, and pre-registered a falsifier for, the following chain:  
**S14 single Hermitian operator  ⇒  R\_TI D\_YM \= D\_K R\_TI  ⇒  \[M, D\_K\] \= 0  ⇒  M \= m·I.**  
**PRE-REGISTERED FALSIFIER (F-S20.8), recorded before computation.** If the reduction naturally generates the weighted adjoint D†\_M \= M⁻¹D\_KᵀM, so that self-adjointness holds automatically for every M, the strategy fails and must be abandoned rather than repaired.  
We execute the chain arrow by arrow and report which arrow breaks.

## **§14.2 The operator, and a structural identity**

On the total cellular Hilbert space H\_K \= C⁰(K) ⊕ C¹(K) ⊕ C²(K), of dimension 60 \+ 90 \+ 32 \= 182, define  
D\_K \= d \+ dᵀ,   d|\_{C⁰} \= B₁ᵀ,   d|\_{C¹} \= B₂.  
D\_K is symmetric, D\_K² is block diagonal and equals the Hodge Laplacian in each degree, and dim ker D\_K \= b₀ \+ b₁ \+ b₂ \= 1 \+ 0 \+ 1 \= 2 for the sphere (checks T71–T74, T76). A structural identity worth recording, and new here:  
**Δ₂(K) \= B₂B₂ᵀ \= L₀(⋆K),**  
that is, the truncated-icosahedron face Laplacian is exactly the graph Laplacian of the dual complex ⋆K (check T75). This is an independent structural reason why the dual picture of §7 is the natural one, and it holds with no metric input at all. \[PROVEN\]

## **§14.3 Theorem S20.R — the commutant is exactly the scalars**

**Theorem S20.R (Incidence Reciprocity).** Let K be a finite 2-complex whose incidence graph — the Hasse diagram on cells of all degrees, with an edge for each incidence — is connected, and let M be diagonal on H\_K. Then \[M, D\_K\] \= 0 if and only if M \= m·I.  
**Proof.** The (i, j) entry of \[M, D\_K\] is (w\_i − w\_j)(D\_K)\_{ij}. The support of D\_K is exactly the incidence graph, so the commutator vanishes iff w\_i \= w\_j across every incidence. Connectedness propagates equality to all cells. \[PROVEN\]  
On K\_TI the companion certifies this twice, independently and exactly: the support of D\_K has 720 non-zero entries and its incidence graph has exactly one connected component (union-find over the integers, checks T77, T78); and the resulting 360 × 182 linear system has rank 181 over GF(2³¹ − 1), hence nullity exactly 1 (check T79), the two certificates agreeing (check T80). The one remaining dimension is the overall scale, which ZS-S19 Corollary S19.2a removes exactly.  
**Note what this buys and what it costs.** Unlike Theorems S20.D and S20.U, Theorem S20.R requires **no** vertex-transitivity, **no** non-bipartiteness, and **no** (H-SYM). It is the cleanest available route to M \= m·I. Correspondingly it is a strictly stronger hypothesis, and by Theorem S20.E it is equivalent, on K\_TI, to the counting star itself.

## **§14.4 Theorem S20.O — the no-go, and the firing of the gate**

**Theorem S20.O (Obstruction).** Let R\_TI be any linear reduction of the continuum connection to cochains which is surjective, equivariant, and intertwines the exterior derivative with the incidence operator, R\_TI ∘ d \= d ∘ R\_TI (the de Rham–Stokes property). Then for every positive diagonal M the operator  
D\_M \= d \+ δ \= d \+ M⁻¹dᵀM  
is self-adjoint with respect to ⟨·,·⟩\_M, is symmetrisable by the similarity M^{1/2}(·)M^{−1/2}, satisfies the same intertwining, and squares to the M-weighted Hodge Laplacian. Consequently the requirement that the reduction produce a single self-adjoint operator imposes no condition whatever on M, and does not imply \[M, D\_K\] \= 0\. \[PROVEN\]  
**Proof.** M-self-adjointness of d \+ M⁻¹dᵀM is immediate from ⟨dω, η⟩\_M \= ⟨ω, M⁻¹dᵀMη⟩\_M. The intertwining hypothesis constrains only d, which is the integer incidence operator by Stokes and carries no metric. δ is unconstrained by it.  
**Verification, five random positive M (check T81–T84):** max‖M D\_M − D\_MᵀM‖ \< 10⁻⁹ (M-self-adjoint); the d-intertwining residual is **identically zero** (D\_M shares d with D\_K exactly, for every M); the symmetrised M^{1/2}D\_M M^{−1/2} is symmetric to machine precision; and yet ‖\[M, D\_K\]‖ \> 1 for those same M. All four conditions of the pre-registered falsifier are met.  
**VERDICT: gate F-S20.8 FIRES. The chain breaks at its second arrow.** “ZS-S14 supplies a single Hermitian operator” does **not** yield R\_TI D\_YM \= D\_K R\_TI; it yields R\_TI D\_YM \= D\_M R\_TI, for whichever M the reduction happens to carry. Hermiticity is not a selection principle on a weighted complex. The intertwiner route is registered as CLOSED-NEGATIVE.  
We record this as the principal result of version 1.1, and we record that it was obtained by executing a falsifier the referee wrote in advance, not by discovering an inconvenience after the fact. The route survives only as a candidate axiom, (H-IR): the cell measure commutes with the incidence Dirac operator, equivalently δ \= dᵀ.

# **§15. (H-SYM) Is Load-Bearing — An Explicit Counterexample to the Weaker Hypothesis**

Theorem S20.D concluded α\_v \= α from vertex-transitivity of K\_TI. Strictly, vertex-transitivity of the complex forces uniformity of the weights only if the weights are themselves assumed invariant. We test how much that assumption is doing.  
Linearising (H-UA) ∧ (H-UA\*) about the uniform point in the variables x\_v \= 1/α\_v, u\_e \= 1/m\_e, β\_f gives a 180 × 182 Jacobian of rank 171 (check T88):  
**kernel dimension \= 11, not 1\.**  
Ten of those eleven directions are non-trivial deformations; the I\_h-invariant part of the kernel is exactly one-dimensional and is the overall scale (check T89). Integrating away from the uniform point along a generic kernel direction by Newton’s method converges to an explicit positive solution (check T90):  
Table 15.1. An explicit positive non-uniform solution of (H-UA) ∧ (H-UA\*) on K\_TI, violating (H-SYM). Newton residual 2.2 × 10⁻¹⁶.

| QUANTITY | MINIMUM | MAXIMUM | SPREAD |
| ----- | ----- | ----- | ----- |
| α\_v (60 values) | 0.878735 | 1.070257 | 0.191522 |
| m\_e (90 values) | 0.886485 | 1.060734 | 0.174249 |
| β\_f (32 values) | 0.874931 | 1.074417 | 0.199486 |

This solution satisfies both anchoring conditions exactly, is strictly positive, does not commute with D\_K (‖\[M, D\_K\]‖ \= 0.035413, check T91), and yields λ₁ \= 1.2429346724, a shift of \+0.0075 % (check T92).  
**Consequences, stated plainly.** (i) (H-UA) ∧ (H-UA\*) alone do **not** force uniformity; version 1.0’s §7 used I\_h-invariance of the weights without listing it. (ii) The correct hypothesis set for Corollary S20.A is (R) ∧ (H-UA) ∧ (H-UA\*) ∧ (H-SYM) — four conditions, not two. (iii) No numerical conclusion changes, because (H-SYM) was already implicit in the I\_h-invariant parametrisation of §3. (iv) Theorem S20.R is thereby the more economical route in one respect and the less economical in another, and §15.1 gives the ledger.

## **§15.1 The axiom ledger, honestly counted**

Table 15.2. Hypothesis sets that yield M \= m·I on K\_TI. All are equivalent on this complex (Theorem S20.E); they differ in generality and in transparency, not in strength.

| ROUTE | HYPOTHESES | CONDITIONS | NEEDS SYMMETRY? |
| ----- | ----- | ----- | ----- |
| ZS-S19 Thm S19.7 | (R) ∧ (R\_C) | 2 | no |
| ZS-S20 §§7–9 | (R) ∧ (H-UA) ∧ (H-UA\*) ∧ (H-SYM) | 4 | yes — essential (§15) |
| ZS-S20 §15 | (R) ∧ (H-IR) | 2 | no |
| equivalent form | (R) ∧ (δ \= dᵀ) | 2 | no |

The corpus’s remaining structural failure point is therefore best stated in the §14 form, and gate F-S20.2 is reformulated accordingly in §13.3: the single sentence that must be defended, or refuted, is that the discrete codifferential is the transpose of the differential.

# **§16. The Remaining Bypass Strategies — Executed, Pre-Registered, or Reframed**

## **§16.1 Gauss-orbit and magnetic-Hessian normalisation — closes, but is an axiom-swap**

Write K \= M₁⁻¹ for the electric metric and demand that the Gauss-orbit Gram matrix and the magnetic Hessian preserve the single Killing-form normalisation of the continuum term:  
(G-E)   B₁ K B₁ᵀ \= c\_E B₁B₁ᵀ,        (G-B)   B₂ᵀ M₂ B₂ \= c\_B B₂ᵀB₂.  
The off-diagonal entries of (G-E) read −κ\_e on both sides, so κ\_e \= c\_E for every edge and M₁ is uniform immediately; the corresponding system has full rank 90 (check T93). (G-B) gives β\_{f₁} \+ β\_{f₂} \= 2c\_B on every edge, and the odd-cycle argument of Theorem S20.U then forces β\_f \= c\_B, the system having rank 32 (check T94). Finally c\_E \= c\_B follows from the single Lorentz-invariant coefficient −¼G\_{μν}G^{μν}.  
**Honest classification.** Both conditions assert that the weighted quadratic form is **proportional to the counting form**. That is the conclusion restated, and by Theorem S20.O the same obstruction applies: nothing in the reduction forces proportionality rather than M-weighted self-adjointness. (G-E) and (G-B) are axiom-swaps unless derived from the ZS-S14 reduction, and they are recorded as such (check T95). The route is not worthless — it is closer to the canonical structure than (H-UA) is — but it does not close the bridge.

## **§16.2 Renormalized anisotropy — HISTORICAL; superseded by §17.6**

Leave ρ \= β₅/β₆ free, compute the background-field effective action on ℝ\_t × K\_TI, and impose continuum restoration as the equality of the electric and magnetic wave-function renormalisations,  
Γ\_eff \= ½ Z\_E(ρ, g) E² − ½ Z\_B(ρ, g) B² \+ ⋯,    F(ρ) := Z\_E(ρ) − Z\_B(ρ) \= 0\.  
**SUPERSEDED.** This pre-registration is retained only as a record. §17.4 shows that Z\_E \= Z\_B fixes the overall temporal-versus-spatial normalisation and does not target ρ, which is an orbit anisotropy; the live gate is F-S20.9b of §17.6. The original text follows. Search interval ρ ∈ \[1/2, 2\]. Success: ρ\* \= 1 is the unique root with F′(ρ\*) ≠ 0, within the quoted truncation error. Revision: a unique root at ρ\* ≠ 1\. Failure: no root, or scheme dependence exceeding the truncation error. The decision rule is fixed here and will not be renegotiated after the result is seen.  
**What can already be said, and it is negative.** At tree level Z\_E \= Z\_B identically, so the condition is empty. λ₁ is not stationary at ρ \= 1: dλ₁/dρ \= \+0.10623798 (check T96), so ρ \= 1 is not selected variationally. And because I\_h-invariance is preserved for every ρ, the T₁ triplet survives at every ρ (check T97), so representation content gives no discriminator either. Only a genuine one-loop calculation can decide this route. Registered as gate F-S20.9 and deferred to ZS-S21.

## **§16.3 Full Whitney / FEEC — Outcome C reframed as a rival, not a collapse**

Version 1.0 classified a non-diagonal M as a collapse of the bridge. That is too strong, and the referee is right to say so. A non-diagonal mass matrix obtained from Whitney forms,  
(M\_k)\_{ij} \= ∫\_{K\_TI} W\_i^{(k)} ∧ ⋆ W\_j^{(k)},  
would be the collapse of the diagonal counting model, not of the Yang–Mills bridge. Under (R) the Whitney inner product is ill-posed because no ambient metric exists (§2.3); but a corpus that adopted a metric would have a finite-element exterior-calculus discretisation available, with bounded cochain projections and a genuine continuum limit. The success criteria would then change, and §13.4 records the change as a non-claim: the target would no longer be the survival of the number 1.2428416164 but the preservation of the T₁ representation content, the exactness of the gauge zero modes, convergence of the spectral gap under refinement, and the stability of the ZS-S17 and ZS-S18 observables. Registered as gate F-S20.10.

## **§16.4 Recommended order of attack — SUPERSEDED, see §23**

The order given in version 1.1 (derive (H-IR) from the projected quadratic form, then one-loop anisotropy, then Whitney) is withdrawn. Theorem S20.T1 of §21 shows that the first item is linear in the action and therefore cannot close. The current order is: (i) the transfer or Hessian self-consistency problem of §18.2 and §21.1, taken as a genuinely non-quadratic problem on the compact group rather than at Gaussian order; (ii) the perfect-action renormalisation-group branch of §18.3; (iii) the one-loop orbit contrast of §17.6; (iv) the Whitney/FEEC completion of §16.3. Items (iii) and (iv) are checks on a chosen measure, not independent selectors.

# **§17. The Non-Identifiability Theorem, and the Corrected Quantum Gate**

Version 1.1 proved that one particular route to the Hodge metric fails. This section proves the stronger statement that no route can succeed from the data ZS-S14 actually contains, and it corrects the target of the one-loop gate.

## **§17.1 Theorem S20.N-a — abstract metric underdetermination**

**Theorem S20.N-a (Abstract Metric Underdetermination).** Let (C⁰ → C¹ → C², d) be a finite cochain complex and let R\_TI be a reduction satisfying R\_TI ∘ d \= d ∘ R\_TI. Then for every choice of positive-definite inner products M₀, M₁, M₂ there is a realisation of the abstract cochain basis {ω} inside a continuum Hilbert space whose Gram matrix is exactly M, and with respect to which the reduction is Hermitian. Consequently M is a **free datum** of the reduction, not a derived one. \[PROVEN\]  
**Proof.** Take the Cholesky factorisation M\_k \= L\_kᵀL\_k and, for any orthonormal family {e\_j} in a continuum Hilbert space, set ω\_i \= Σ\_j (L\_k)\_ji e\_j. Then ⟨ω\_i, ω\_j⟩ \= (M\_k)\_{ij} by construction. The intertwining hypothesis constrains d, which is the integer incidence operator and carries no metric; the codifferential δ \= M⁻¹dᵀM is then determined by M rather than constraining it (Theorem S20.O).  
The companion realises three arbitrary symmetric positive-definite matrices, one in each degree, as exact Gram matrices to machine precision (checks T98–T100). This is an abstract Hilbert-space statement and no more. A Cholesky basis is not by itself an admissible cochain embedding: it need not lie in a space of differential forms, need not be I\_h-equivariant, gauge-covariant or cell-local, and need not satisfy the chain compatibility L\_{k+1} d\_K \= d\_K L\_k. Version 1.2 elided this and thereby overclaimed the physical reach of the theorem; §17.1a repairs the gap by construction rather than by weakening. ZS-S20 §2.2 defines {ω\_e} as an   
**abstract** one-cochain basis, with no Gram matrix, no measure and no embedding. Theorem S20.N therefore applies directly. The count of undetermined directions is: **181** for diagonal M after removal of the overall scale, and **6 × 10³** order for general symmetric positive-definite M.  
**Corollary S20.N1.** Gate F-S20.2 cannot be closed from ZS-S14 alone. Its status is upgraded from OPEN to **OPEN-TERMINAL relative to the present ZS-S14 input set** — a strictly stronger statement than “no good idea has yet been found”. To close it, one of the following must be **added** to ZS-S14: a continuum embedding ω\_e(x); an inner product or measure; an ambient metric; a normalisation or cylindrical-consistency principle; or an explicit counting-trace axiom. This is the honest terminus of the axiom-swap search, and §17.2 and §17.3 close the two remaining corpus-internal candidates.

## **§17.1a Theorem S20.N-b′ — two non-proportional geometric DEC stars**

What is actually needed is two realisations that satisfy every admissibility condition at once: they must lie in a space of su(3)-valued differential forms, be cell-local, be I\_h-equivariant, be gauge-covariant, intertwine d exactly by Stokes, and be compatible with the temporal-plaquette reduction. We construct two.  
**(W) The flat polyhedral cone metric.** The regular truncated icosahedron carries the Euclidean cone metric with a conical singularity at each of its 60 vertices; the companion verifies the total defect to be exactly 4π (check T111). **It must be said at once that this metric is not selected by the corpus.** Version 1.3 claimed that ZS-A7 §2.2 presupposes it; that claim is withdrawn in §18. The Spinor–Descartes–Euler identity Σᵥδᵥ \= 2πχ is a **topological** statement, true of every convex polyhedron, and it does not pick out the regular realisation. The flat cone metric is one natural metric compatible with the identity, not a consequence of it. Faces are regular, so A₅ \= 5/(4tan(π/5)) and A₆ \= 3√3/2, and A₆/A₅ \= 6√(15 − 6√5)/5 exactly (check T112). The scale cancels; there is no free parameter.  
**(W̃) The round-sphere metric.** All 60 vertices are equidistant from the centre, so K\_TI has a canonical geodesic realisation on its circumsphere. The 32 spherical face areas sum to 4π by Gauss–Bonnet, verified exactly (check T114). This realisation is the one suggested by ZS-Q12V’s bedrock Z \= ∂X with X smooth.  
Both are I\_h-equivariant, cell-local, gauge-covariant and Stokes-intertwining. Their Hodge stars are computed from ⋆₂ \= 1/A\_f and ⋆₁ \= |⋆e|/|e| in the respective metrics, and they are not proportional:  
Table 17.1. Two admissible realisations of K\_TI and their Hodge data. Neither is a rescaling of the other.

| REALISATION | ρ \= β₅/β₆ | m₅₆/m₆₆ | λ₁ |
| ----- | ----- | ----- | ----- |
| flat polyhedral cone (W) | 1.5100902868 | 0.9105929973 | 0.3600376672 |
| round sphere (W̃) | 1.5293717114 | 0.8939748058 | 1.8960240285 |
| ratio | 1.0127683919 | 1.0185796 | 5.266 |

**Theorem S20.N-b′ (Two Non-Proportional Geometric DEC Stars).** K\_TI admits two natural I\_h-equivariant metric realisations — the regular flat polyhedral cone metric and the geodesic round-sphere metric — whose circumcentric diagonal DEC Hodge stars are not proportional, the shape ratio ρ differing by 1.28 %. \[COMPUTED; checks T111–T116\]  
**What this is NOT, stated plainly.** A diagonal circumcentric DEC star is a mass-lumped object; a Whitney or FEEC embedding gives a sparse **non-diagonal** Gram matrix, and the two are not the same construction. This paper does not build explicit maps W\_k : C^k(K\_TI) → Ω^k(Σ, su(3)), does not verify R\_k W\_k \= I or dW\_k \= W\_{k+1}∘d\_K, and does not check gauge-transformation intertwining or compatibility with the temporal-plaquette embedding. Version 1.3 asserted all of these; the assertion is withdrawn in §18. The correct statuses are: two metric realisations and two diagonal DEC stars, **COMPUTED**; ZS-S14 physical non-identifiability, **DERIVED-CONDITIONAL**; existence of two admissible cochain embeddings, **OPEN** and registered as gate F-S20.2a.  
**A strong internal corroboration.** The flat-polyhedral realisation returns λ₁ \= 0.3600376672 with multiplicity three — exactly the full-DEC gap the corpus already quotes at a\_TI \= 1, here reproduced from an independently rebuilt complex and an independently constructed star (check T113). The agreement is a non-trivial consistency test of both computations.  
**And a sharp negative.** Neither geometric star satisfies (H-UA): the anchoring condition requires m₅₆/m₆₆ \= 1.2550451434, while the flat geometry gives 0.9105929973 (check T117). **The geometric route and the anchoring route are inequivalent.** One of them must be wrong about what the Z-sector is.

## **§17.2 Register democracy is a density, not a rate — CLOSED-NEGATIVE as a selector**

ZS-F38 proves that an irreducible doubly stochastic transition has the uniform measure as its unique stationary state, and §10 uses this as independent corroboration. It cannot be promoted to a derivation, for a reason that is elementary and decisive: the stationary state does not determine the generator.  
Table 17.2. A one-parameter family of doubly stochastic transitions on the Q \= 11 register, all sharing the uniform stationary state and differing in rate.

| ε IN P\_ε \= (1−ε)I \+ εP | DOUBLY STOCHASTIC | STATIONARY STATE | SPECTRAL GAP |
| ----- | ----- | ----- | ----- |
| 0.1 | yes | uniform | 0.014391 |
| 0.3 | yes | uniform | 0.033912 |
| 0.5 | yes | uniform | 0.040507 |
| 0.9 | yes | uniform | 0.014391 |

M₁⁻¹ is an electric **stiffness** — a rate — not a probability density. The register-democracy theorems of ZS-F38 and ZS-F39 therefore corroborate uniformity without deriving it, and §10 is hereby restricted to that reading (checks T101–T103). \[CLOSED-NEGATIVE as a selector; retained as corroboration\]

## **§17.3 The integral-star lemma — correct mathematics, absent physics**

**Lemma S20.L.** If a diagonal Hodge star preserves an integral cochain lattice and so does its inverse, then every weight w satisfies w ∈ ℤ₊ and 1/w ∈ ℤ₊, hence w \= 1\. \[PROVEN\]  
The lemma is exact and would close the gate instantly. Its physical premise — that spatial cellular Hodge duality exchanges the primitive electric and magnetic charge lattices unimodularly — has no bridge in SU(3), whose root, coroot, weight and coweight lattices are in general distinct. We record the lemma so that it is not rediscovered, and classify it as an axiom-swap (check T104).

## **§17.4 ρ is an orbit anisotropy, and ρ \= 1 is not symmetry-protected**

Version 1.1 mis-stated the target of the quantum gate. The condition Z\_E \= Z\_B fixes the overall temporal-versus-spatial normalisation. But the surviving parameter  
ρ \= β₅ / β₆  
is not an electric–magnetic anisotropy at all: it is a   
**pentagon–hexagon orbit anisotropy.** The correct decomposition uses the two orbit operators and their contrast singlet:  
O₅ \= Σ\_{f∈F₅}(N − Re Tr U\_f),   O₆ \= Σ\_{f∈F₆}(N − Re Tr U\_f),   O₊ \= O₅ \+ O₆,   O₋ \= O₅/12 − O₆/20,  
so that S\_B \= β̄ O₊ \+ Δβ O₋ and Δβ \= 0 is the counting-star branch. The total face weight of O₋ is 12(1/12) − 20(1/20) \= 0 exactly, so O₋ is a traceless contrast (check T105).  
**The decisive point: O₋ is itself I\_h-invariant** (check T106), because F₅ and F₆ are each single I\_h orbits. The invariant subspace of face weights is two-dimensional (check T107), so there are two independent I\_h-allowed couplings, not one. By the Symanzik effective-action principle, an independent local operator permitted by the regulator symmetry generically acquires its own coefficient. Therefore   
**ρ \= 1 is NOT a symmetry-protected fixed point.**  
This retires the hope, implicit in §16.2 of version 1.1, that I\_h invariance alone might make the counting star radiatively stable. \[DERIVED\]

## **§17.5 The counting star is not symmetry-protected — an exact local distinguishability result**

Whether O₋ is actually generated is decided by whether the two orbits are locally distinguishable to the fluctuation determinant. They are, and exactly. Using the identity Δ₂ \= B₂B₂ᵀ \= L₀(⋆K) of §14.2, the diagonal heat kernel expands as diag(e^{−tΔ₂})\_f \= Σ\_k (−t)^k (Δ₂^k)\_{ff} / k\!, and the orbit contrast is exactly integral:  
Table 17.3. Exact diagonal moments of Δ₂ \= L₀(⋆K) on the two face orbits. The contrast is non-zero already at first order and grows.

| ORDER k | (Δ₂^k)\_{ff} PENTAGON | (Δ₂^k)\_{ff} HEXAGON | CONTRAST |
| ----- | ----- | ----- | ----- |
| 0 | 1 | 1 | 0 |
| 1 | 5 | 6 | 1 |
| 2 | 30 | 42 | 12 |
| 3 | 195 | 309 | 114 |
| 4 | 1330 | 2334 | 1004 |

The leading local invariant separating the two orbits is the **face degree itself**, 5 against 6, giving a contrast of exactly 1 at order t at the six audited values of t (checks T108–T110). This establishes that the two orbits are locally distinguishable to a scalar heat kernel. It does NOT establish that O₋ is generated: the Yang–Mills one-loop determinant is ½ log det′ H\_gluon − log det′ H\_ghost, with longitudinal modes, ghosts and background-dependent vertices, and orbit contrasts from the separate pieces may cancel. A scalar face Laplacian is a diagnostic, not a substitute. We therefore record the following as a target, not a result:  
**PRE-REGISTERED TARGET (F-S20.9b) \[HYPOTHESIS-strong, NOT a result\]. C₋(1) ≠ 0: the counting star splits at one loop, and ρ flows in the degree-biased direction. Version 1.2 stated this as a prediction of the computation; that status is withdrawn. What is proven is only that no symmetry forbids the splitting.** If the flow reached the degree-biased value ρ\_F \= 5/6 exactly, then λ₁ \= 1.2155777721 (−2.1937 %) and Λ\_QCD \= 270.02 MeV. Sensitivity is quantitative and mild: a 1 % shift in ρ moves λ₁ by 0.0855 % and Λ\_QCD by the same 0.0855 % in the opposite sense, since Λ\_QCD ∝ 1/λ₁, so a small radiative splitting is survivable while a large one is not. This is the sharpest falsifier ZS-S20 produces.  
**Note against interest.** §10.2 classifies ρ\_F \= 5/6 as CLOSED-NEGATIVE under Theorem S20.D. §17.5 predicts that radiative corrections push ρ **toward** that excluded neighbourhood. The two statements are consistent — S20.D is a tree-level statement conditional on (H-SYM) and star compatibility, which the effective action need not respect — but the tension is real and we flag it rather than reconcile it by fiat.

## **§17.6 The corrected gate, split in two**

Gate F-S20.9 of version 1.1 is withdrawn as mis-targeted and replaced by two gates.  
Table 17.4. The corrected quantum gates.

| GATE | CONDITION | WHAT IT DECIDES |
| ----- | ----- | ----- |
| F-S20.9a | Z\_E(ρ, g) \= Z\_B(ρ, g) | overall temporal–spatial normalisation; does NOT determine ρ |
| F-S20.9b | Δβ\_R \= Δβ \+ g²C₋(ρ) \+ O(g⁴) \= 0, with C₋(ρ) \= ∂²Γ^{(1)}/∂ϕ² at ϕ \= 0 in the orbit-contrast background | the pentagon–hexagon selection; this is the gate that determines ρ |

The orbit-contrast background is the Cartan-valued face flux F̄\_f \= \+ϕ/12 on pentagons and −ϕ/20 on hexagons, whose total flux vanishes so that it is a small deformation of the trivial bundle. Decision rule, fixed here: SUCCESS if Δβ\_R \= 0 has the unique root ρ\* \= 1, independent of the gauge parameter, with scheme variation below the truncation error; REVISION if the unique root is ρ\* ≠ 1; FAILURE if there is no root, several roots, or gauge and scheme dependence exceeding the signal; CLOSED-NEGATIVE if C₋(1) ≠ 0\. §17.5 shows this is not forbidden; it does not show it happens.

## **§17.7 What would actually close the bridge**

Collecting §14 through §17: the action-level route is terminal (S20.N-b), the corpus-internal structural routes are closed-negative (§17.2, §17.3), and the quantum route is open. What remains is to add the one datum §18.2 and §21 name — an embedding, a measure, or an explicit trace axiom — and to say so openly, or to move to the metric-adopted continuum-completion branch of §16.3, which is a parallel research programme with a different physical interpretation rather than a fallback. In that branch the target is not the survival of 1.2428416164 but the existence of a continuum-consistent refinement sequence, and the ledger numbers are expected to move.

## **§17.8 Gate F-S20.11 of version 1.3 is retracted in full — the scale error**

Version 1.3 tabulated the absolute spectral gaps of three candidate stars, converted them to MeV, and concluded that two were excluded by the quenched lattice band. That conclusion is wrong and is withdrawn. The three gaps were not computed in the same units.  
**The scale theorem.** Under a global rescaling g ↦ s²g of a two-dimensional metric, the one-form star ⋆₁ \= |⋆e|/|e| is a ratio of lengths and is **invariant**, while the two-form star ⋆₂ \= 1/A\_f carries s⁻². Hence  
**λ₁ ↦ s⁻² λ₁ ,**  
so the absolute gap depends on the metric scale as well as on its shape. This is a different transformation from the common gauge (M₁, M₂) ↦ (cM₁, cM₂) that ZS-S19 Corollary S19.2a removes: a geometric length rescaling does not move M₁ and M₂ in the same ratio, and therefore is not eliminated by that corollary.  
**The arithmetic is decisive.** The flat-polyhedral star at unit edge length gives λ₁ \= 0.3600376672. Setting s \= √(0.3600376672 / 1.2428416164) \= **0.5382277383** reproduces the counting-star value exactly — and that number is a\_TI, already recorded in this very paper. Likewise the round-sphere star at unit radius gives 1.8960240285, which at unit geodesic edge length becomes 0.3130534423 (checks T118, T119). The figures 911.67 MeV and 173.12 MeV were therefore not parameter-free predictions but the consequence of comparing a unit-edge convention, a unit-radius convention and a purely combinatorial normalisation as though they were the same.  
**Consequences, all withdrawn:** the exclusion of the flat candidate; the exclusion of the round-sphere candidate; the description of the counting star as the unique survivor; and the claim that the bridge is closed at the level of OBSERVATION. Gate F-S20.11 is retracted. Separately, and independently fatal to the same argument, any absolute comparison in MeV presupposes the fixing of a\_TI and a scheme matching g\_S14 ↔ g\_MS̄, both of which this paper itself leaves OPEN as F-S19.3. A paper may not leave a gate open and then use its conclusion.  
**A second overreach, also withdrawn.** Even had the units been right, calling the counting star the “unique surviving corpus-internal candidate” would require a theorem that the three audited candidates exhaust the possibilities, and there is none. Theorem S20.N-a says the opposite: I\_h-invariant metrics form a large family, including conformal deformations and interpolations between the flat and round cases. The most that may ever be said is “the survivor among the candidates audited here”, and after the scale correction not even that is available.

## **§17.9 What is actually scale-free, and the correct form of the comparison**

The lesson is not that no comparison is possible, but that only dimensionless quantities may be compared. Two are available without fixing a\_TI: the shape ratio ρ \= β₅/β₆, and the ratio of the second threefold spectral level to the first. Both are invariant under g ↦ s²g and under M ↦ cM.  
Table 17.5. Scale-free data for the audited stars. No MeV values are quoted, and no candidate is excluded.

| STAR | ρ \= β₅/β₆ | SECOND-T₁ RATIO | STATUS |
| ----- | ----- | ----- | ----- |
| counting star (R\_C) | 1.0000000000 | 3.8978144635 | conditional branch |
| flat polyhedral cone | 1.5100902868 | 4.9047903870 | audited candidate |
| round sphere | 1.5293717114 | 4.9249092641 | audited candidate |
| equal-cell refinement (§17.11) | 1.2000000000 | 4.1933599511 | exact under its own hypothesis |

The two geometric stars agree with each other to 0.4 % in the second-T₁ ratio and differ from the counting star by about 26 %. That is a real, scale-free tension and it is worth recording — but it is registered as an **OPEN gate F-S20.11′**, not an exclusion, because deciding it requires an external dimensionless observable that neither this paper nor ZS-S17 currently supplies. We state the tension and we do not resolve it in our own favour.

# **§18. The Dynamical Reformulation — Primitive Plaquette-Clock Closure**

Sections 14 to 17 all attempted the same manoeuvre: choose a metric, then read the weights off it. Every attempt failed, and §17.8 shows that the last one failed twice over. The reformulation that survives inverts the manoeuvre.  
**Do not input a metric. Output the stationary measure of a transfer constructed from the ZS-S14 continuum action by an EXPLICIT cellular projection, gauge projection, Euclideanisation and normalisation prescription.**

## **§18.1 The two branches must be separated**

A prior decision has been made implicitly throughout ZS-S7 to ZS-S20 and is now made explicit, because the two readings give different answers and may not be mixed in one paper. Branch I-A: K\_TI is the fundamental ultraviolet regulator of the Y-sector, not an approximation to anything, and there is no refinement limit — this is the position of axiom (R) and of ZS-S19. Branch I-B: K\_TI is the coarsest member of a refinement family and continuum Yang–Mills is to be recovered. §18.2 closes I-A conditionally; §18.3 shows that I-B does not favour the counting star.

## **§18.2 Branch I-A — the plaquette stationary measure**

Let P\_Z be the normalised plaquette register of one fundamental Z-clock cycle, of size N\_P \= Q(E \+ F) \= 11(90 \+ 32\) \= 1342 (check T122), and let T\_Z be a positive transfer operator obtained from the ZS-S14 continuum action after an explicit cellular projection, Euclideanisation, gauge averaging and normalisation. ZS-S14 does not supply this prescription — Theorem S20.N-a says it cannot — so T\_Z is constructed, not read off. Introduce one hypothesis, and note carefully what it does not assume.  
(H-PSM-1)  T\_Z is primitive.   \[pure mathematics, once T\_Z exists\]  
(H-PSM-2)  R\_action(π\_Z) \= (M₁, M₂).   \[the physics bridge — NOT a theorem\]  
**Why the split matters.** §17.2 proves that a stationary density does not determine a kinetic rate. (H-PSM-2) reads a density as an electric stiffness and a magnetic action coefficient, which is exactly the step §17.2 forbids in general. It is therefore an **identification**, and it carries the entire physical content. Version 1.4 bundled the two halves into one hypothesis and thereby blurred which is mathematics and which is the unbridged gap. A further circularity must be stated: a Euclidean cellular transfer is normally built FROM an action S\[M₁, M₂\], so in general T\_Z \= T\_Z\[M₁, M₂\], and the honest object is not a fixed measure but a self-consistency equation (M₁, M₂) \= R\_action(π\*(T\_Z\[M₁, M₂\])). Its existence, projective uniqueness, gauge invariance and independence of the seed metric are all unproven. The state space is also undefined: the physical Hilbert space is L² of the gauge-invariant configuration space, and no map from operators on it down to a 1342-component register has been specified, so the phrase ‘the temporal and spatial restrictions of π\_Z are M₁ and M₂’ does not yet type-check.  
**Proposition S20.P1 (Conditional Stationary-Measure Reconstruction).** If (H-PSM-1) and (H-PSM-2) hold then the cellular action measure is unique: T\_Zπ\_Z \= π\_Z with π\_Z \> 0 and Σπ\_Z \= 1, and M₁ and M₂ are the restrictions of π\_Z to the temporal and spatial blocks, up to one overall normalisation. \[DERIVED-CONDITIONAL on (H-PSM-1) ∧ (H-PSM-2); checks T123, T124 are PROXY only\]  
**Corollary S20.P2.** If T\_Z is in addition bistochastic, the uniform measure is stationary, and primitivity makes it unique. Then M₁ \= M₂ \= m·I, Δ₂ \= B₂B₂ᵀ and λ₁ \= 1.2428416164 — the counting star, now **derived from dynamics rather than assumed**. \[PROVEN as a generic Perron–Frobenius statement; check T124 is a PROXY on a random matrix, NOT on the 1342-dimensional ZS-S14 transfer, which this paper does not build\]  
**Why this is a better gate than (H-UA).** The conditions (R) ∧ (H-UA) ∧ (H-UA\*) ∧ (H-SYM) are, by Theorem S20.E, equivalent on K\_TI to the counting star itself: they were conditions constructed to yield the answer already held. (H-PSM) is **outcome-neutral**. If T\_Z is unital the counting star follows; if T\_Z is primitive but not unital, a unique **non-uniform** metric follows and the bridge is still closed with the ledger moved; if T\_Z is not primitive, branch I-A fails. No result is preferred in advance (check T125). That is the property every previous candidate lacked.  
Table 18.1. The executable gates of the plaquette-clock route, in dependency order. This is the recommended next computation, and it should precede any non-perturbative Lanczos work, since a different T\_Z changes the operator to be diagonalised.

| GATE | TEST | FAILURE MEANS |
| ----- | ----- | ----- |
| P1 | construct T\_Z from the ZS-S14 temporal plaquette action as a gauge-covariant positive transfer | no transfer exists; branch I-A is ill-posed |
| P2 | primitivity: peripheral spectrum {1}, or the Kraus commutant is trivial | several stationary measures; selection does not close |
| P3 | identify π\_Z with the action measure by transfer-matrix reconstruction or detailed balance | the central physical gate; without it P1–P2 are decorative |
| P4 | unitality T\_Z 1 \= 1 | PASS gives the counting star DERIVED; FAIL with primitivity gives a unique non-uniform metric |
| P5 | spectrum regression: recompute Δ₂(M) and the full ledger from whatever M emerges | registered as F-S20.13 |

## **§18.3 Branch I-B — exact subdivision, and what it selects**

If instead K\_TI is a coarse member of a refinement family, two exact results are available and neither favours the counting star.  
**Theorem S20.S1 (Series Law).** Minimising ½Σβ\_iφ\_i² at fixed total flux Φ \= Σφ\_i gives the coarse coefficient  
1/β\_eff \= Σ\_i 1/β\_i ,  
verified symbolically (check T126). Quadratic blocking composes in series, not in parallel. \[PROVEN\]  
**Theorem S20.S2 (Cylindrical Consistency).** If the coefficient depends only on face area, β \= β(A), and the same coarse physics is required of every subdivision A \= ΣA\_i, then g(A) := 1/β(A) satisfies Cauchy's equation g(A \+ B) \= g(A) \+ g(B). With positivity the unique solution is g(A) \= cA, so  
**β(A) \= 1/(cA) — the inverse-area Hodge law.**  
Cylindrical consistency therefore selects a genuine area measure, not an arbitrary counting weight (check T127). The counting star β₅ \= β₆ is the special case A₅ \= A₆, which the regular truncated icosahedron does not satisfy. \[PROVEN\]  
**Corollary S20.S3.** Dividing an n-gon into n primitive subfaces of equal coefficient β\_△ gives β\_n \= β\_△/n by the series law, hence  
ρ\_refine \= β₅/β₆ \= (1/5)/(1/6) \= 6/5 \= 1.2 .  
**A convention warning, because getting it backwards would collide with §10.2.** Throughout ZS-S20, ρ := β₅/β₆. The series law gives β\_n \= β\_△/n, so β is inversely proportional to the face size and ρ\_refine \= 6/5 \> 1\. Some working notes state this result as 5/6, using the reciprocal convention β₆/β₅. The distinction is not cosmetic: 5/6 in the ZS-S20 convention is exactly ρ\_F, the **degree-biased** candidate of §10.2, which arises from β ∝ n and is closed negative at tree level. Subdivision and degree-biasing are **exact reciprocals of one another** — the series law divides by the face size, degree-biasing multiplies by it — so the two candidates sit symmetrically on opposite sides of the counting star. Confusing them would make a refuted candidate look like a derived one.  
So ρ \= 1 is **not** the fixed point of the simplest equal-cell refinement (check T128). The ledger consequence is mild: λ₁ \= 1.2545633521, a shift of \+0.9431 %, and Λ\_QCD \= 261.63 MeV (check T129). We record two cautions against interest. First, 6/5 is the reciprocal of the degree-biased ρ\_F \= 5/6 that §10.2 closes negative at tree level, so the two refinement-flavoured candidates sit on opposite sides of the counting star and neither is favoured by the other. Second, and more important, ρ\_refine \= 6/5 is **PROVEN only under the equal-primitive-cell hypothesis** and is a NON-CLAIM as the physical Z-sector value: real geometric subcells of unequal area give a different ρ (check T130).  
**What branch I-B would require.** A full closure here is the perfect-action fixed point S\* \= R(S\*) under an I\_h-equivariant blocking map commuting with d. Classically perfect fixed-point actions exist for SU(3) lattice gauge theory, and they generically contain many exponentially local Wilson-loop couplings. A truncation to the two couplings (β₅, β₆) can therefore manufacture a spurious ρ\* \= 1, and the loop basis must be widened before any fixed point is trusted. A unique fixed point closes the bridge **whatever ρ\* it returns**; ρ\* ≠ 1 closes it and moves the ledger, and that outcome is acceptable.

# **§19. Theorem S20.T1 — Why Five Routes Failed, and What Cannot Fail That Way**

## **§19.1 The referee's linear-response route, executed**

A natural improvement on §18.2 is to stop reading a density and read a response instead: couple sources J to the cellular flux operators, take the leading transfer eigenvalue λ₀\[J\], and define the measure by the free-energy Hessian  
M\_ab \= − ∂²log λ₀\[J\] / ∂J\_a ∂J\_b  at  J \= 0 ,  
then solve the fixed point M\_out(M) ∝ M. This does not confuse a density with a rate, so it is immune to the objection of §17.2. We executed it.  
On K\_TI with H \= ½EᵀM₁⁻¹E \+ ½qᵀ(B₂ᵀM₂B₂)q and sources coupled to the magnetic fluxes φ \= B₂q, completing the square gives the susceptibility χ \= B₂(B₂ᵀM₂B₂)⁺B₂ᵀ, of rank 31 \= dim Im(B₂) (check T131). Inverting on the physical subspace returns  
**M\_out \= M₂ exactly, for every positive M₂.**  
The residual is below 10⁻¹² over four random positive metrics (check T132).  
**Theorem S20.T1 (Linear-Response Triviality).** At Gaussian order the transfer-Hessian map is the identity. Every positive M is a fixed point, and the route selects nothing. \[PROVEN\]

## **§19.2 The meta-obstruction — one reason for five failures**

Theorem S20.T1 is not an isolated disappointment. Placed beside the two earlier no-gos, it exposes a single mechanism.  
Table 19.1. Three no-gos, one obstruction. In each case the construction is linear in the action and adds no data, so it returns the data it was given.

| THEOREM | CONSTRUCTION | WHY IT RETURNS ITS INPUT |
| ----- | ----- | ----- |
| S20.O (§14.4) | require the reduction to produce one self-adjoint operator | the adjoint is DEFINED by M, so M-self-adjointness holds for every M |
| S20.N-a (§17.1) | require the cochain basis to have a Gram matrix | every SPD matrix IS a Gram matrix; the metric is free data |
| S20.T1 (§21.1) | read M from the free-energy Hessian | the Hessian of a quadratic form is its own coefficient matrix |

**Meta-observation, in its corrected form.** Version 1.5 first wrote this as “any construction linear in the action returns the measure it was given”. Part 28 of the companion tests that statement adversarially and finds it too strong: the electric two-point function is a different functional of (M₁, M₂) and is not literally the identity map (check T145). The correct statement is a counting one. **A fixed-point condition built solely from the action always admits the action itself as a solution; it can constrain M only if it is OVER-DETERMINED** — that is, only if it imposes more independent scalar conditions than M has free components. On K\_TI the I\_h-invariant measure has four components, three after the scale is removed by ZS-S19 Corollary S19.2a, so **any candidate closure must supply at least three independent scalar conditions that are not themselves consequences of the action** (check T147). This is a sharper filter than the original phrasing, and it is stated here as an erratum caught by our own cross-check rather than by review. Symmetry conditions, Hermiticity conditions, Gram-matrix conditions and linear-response conditions are all of this type, which is why (H-UA), (H-UA\*), (H-IR), the Gauss and Hessian normalisations, register democracy, integrality and now the transfer-Hessian route have all failed in the same way. **Closure requires a step that is either non-quadratic or a genuine coarse-graining.** Registered as gate F-S20.14. This is the single most useful thing ZS-S20 has learned, and it should be applied as a filter before any further candidate is attempted: if a proposal is linear in the action and adds no data, it cannot close the bridge, and no computation need be run.

## **§19.5 Independent cross-verification of this version's own claims**

Five successive versions each verified a proxy and reported it as verification of the target. Part 28 of the companion is a structural answer rather than a promise: every new claim of version 1.5 is re-derived by a method chosen to share as little machinery as possible with the one that produced it.  
Table 19.3. Independent re-derivations.

| CLAIM | FIRST METHOD | INDEPENDENT CHECK |
| ----- | ----- | ----- |
| Theorem S20.T1, M\_out \= M₂ | analytic completion of the square | finite-difference Hessian of the ground-state energy, different random seed; agreement to 3.4 × 10⁻⁷ (T141, T142) |
| SU(2) heat-kernel semigroup | character coefficients exp(−t·j(j+1)), which is close to assuming the result | coefficients extracted by numerical Weyl integration on a 6000-point grid normalising to 1.000000000000; semigroup error 2.2 × 10⁻¹⁶ (T143, T144) |
| the four ρ values and their λ₁ | Table 21.2 | complex rebuilt from Cartesian coordinates; all four reproduced to ten digits at multiplicity three |
| the meta-observation of §21.2 | three worked examples | adversarial test on the electric channel; the statement FAILED and was weakened (T145–T147) |

**One of the four did not survive, and that is the point of the exercise.** The meta-observation as first written is too strong, and §21.2 now carries the corrected over-determination form. We record this because a paper that only ever confirms itself is not being checked.

## **§19.3 A step that provably does not return its input — the heat-kernel semigroup**

Two-dimensional Yang–Mills assigns to each face the heat kernel on the gauge group with parameter equal to the face area. The heat kernel obeys the semigroup law exactly and non-perturbatively,  
**K\_{t₁} ∗ K\_{t₂} \= K\_{t₁+t₂} ,**  
which we verify numerically rather than cite. For U(1), convolving two kernels by fast Fourier transform reproduces the sum-parameter kernel to 4.3 × 10⁻¹⁴ in the supremum norm (check T134). For the non-abelian SU(2), the character coefficients c\_j(t) \= exp(−t·j(j+1)) multiply exactly, so t is additive to 2.8 × 10⁻¹⁷ (check T135). This is not a weak-field statement and not a quadratic approximation: it is an identity of the group heat kernel.  
Combined with Theorem S20.S2, the consequence is that in the heat-kernel branch the inverse-area law β(A) \= 1/(cA) is exact and non-perturbative (check T136), and it is the **unique** fixed point of area subdivision: splitting a face into sub-faces whose areas sum to A returns β \= 1/(cA) identically (check T140). The counting star is a fixed point only of equal-count subdivision, which is not area-additive and therefore not cylindrically consistent.  
Table 19.4. Honest status of the heat-kernel results.

| RESULT | STATUS |
| ----- | ----- |
| compact-group heat-kernel semigroup | IMPORTED-PROVEN |
| U(1) and SU(2) numerical regression | VERIFIED examples |
| ZS-S14 SU(3) cellular heat-kernel realisation | OPEN |
| K\_TI area-measure selection | OPEN-CONDITIONAL |

## **§19.4 Reported against interest — what that does to the counting star**

**The counting star requires β₅ \= β₆, hence A₅ \= A₆, which the regular truncated icosahedron does not satisfy: A₆/A₅ \= 1.5100902868 (check T137).** In the heat-kernel branch the shape ratio is therefore fixed by area and not by counting, giving ρ\_heat \= 1.5100902868 and λ₁ \= 1.2492508718, a shift of \+0.5157 % (check T138). We state this plainly: **in the one branch where a non-quadratic step is available and exact, the counting star is disfavoured.**  
Table 19.2. Four prescriptions, four answers. All entries are scale-free. None is selected by ZS-S14.

| PRESCRIPTION | LAW | ρ \= β₅/β₆ | λ₁ (dev) |
| ----- | ----- | ----- | ----- |
| degree bias (§10.2, refuted at tree level) | β ∝ n | 0.8333333333 | 1.2155777721 (−2.1937 %) |
| counting star (R\_C) | β \= const | 1.0000000000 | 1.2428416164 (0) |
| equal-cell refinement (§18.3) | β ∝ 1/n | 1.2000000000 | 1.2545633521 (+0.9431 %) |
| heat kernel / 2D Yang–Mills (§21.3) | β ∝ 1/A | 1.5100902868 | 1.2492508718 (+0.5157 %) |

Four prescriptions, four distinct answers, spanning −2.2 % to \+0.9 % in λ₁ (check T139). The spread is small, which is why the anti-numerology result of §12 matters: a band of this width is not a discriminator. **The honest position is that ZS-S14 selects none of them, and that the branch decision of §18.1 — finite regulator or refinement family — must be made before the question even has a determinate answer.**

# **§20. The Closure — Area-Measure Reduction and the Equivariant Lift**

## **§20.1 An erratum of ours, found before review**

**Version 1.5 concluded that the counting star is disfavoured. That conclusion is withdrawn.** It read β(A) \= 1/(cA) together with A₆/A₅ \= 1.5100902868 — but those are the areas of the **regular flat polygons**, which is precisely the metric version 1.4 retracted as not selected by the corpus. The unfavourable conclusion silently reinstated a retracted assumption. Correctly read, Theorem S20.S2 does not fix ρ at all. It **replaces** the question “what is ρ?” with the question “what is the area measure on the 32 faces?” — and unlike the first, the second is a question the corpus can answer.

## **§20.2 The problem is two numbers, and it is an artefact of two orbits**

The icosahedron is vertex-, edge- and face-transitive, so on it I\_h-invariance alone forces M₀, M₁, M₂ uniform: zero shape parameters, no bridge problem at all (check T148). The truncated icosahedron has two face orbits and two edge orbits, and that is the entire source of the difficulty. There is moreover a canonical I\_h-equivariant blocking between them — collapse each pentagon to a vertex and each hexagon to a triangle — whose combinatorics match exactly: 12 → 12, 20 → 20, and the 30 (6,6) edges → 30 icosahedron edges, with the 60 (5,6) edges as the truncation seams (check T149).  
Under that blocking a triangle is one hexagon plus three fifths of a pentagon, and the series law 1/β\_△ \= 1/β₆ \+ 3/(5β₅) is then   
**identically** satisfied by area additivity A\_△ \= A₆ \+ (3/5)A₅ (check T150). The series law therefore adds nothing beyond area additivity, which is the honest reading of Theorem S20.S2 and confirms that the residual face-side freedom is exactly the area ratio.  
**The parameter count, corrected.** The I\_h-invariant measure has four components; ZS-S19 Corollary S19.2a removes the scale, leaving three. But one of the three is β/m, the overall coupling, which is g² together with a\_TI — gate F-S19.3, which ZS-S20 has never claimed to determine. **The shape problem is therefore two numbers, ρ \= β₅/β₆ and σ \= m₅₆/m₆₆, and needs exactly two conditions** (check T151). Version 1.5's bound of “at least three independent conditions” counted the coupling as part of the shape problem; that is an erratum, recorded in Table 22.1.

## **§20.3 The two conditions come from ZS-F39, and they are not ours to choose**

ZS-F39 Theorems T3 and T4 prove a dichotomy for register lifts, and it is a dichotomy the corpus settled before ZS-S20 existed. The A24-refining   
**equivariant** slot lift is a unital irreducible generator whose unique stationary state is the uniform measure I\_Q/Q; the **multiplicity-weighted** lift is non-unital and gives the size-biased transport weight d\_i²/49. A selection lemma keeps the equivariant lift. Applied to the K\_TI face and edge registers, whose lifts are I\_h-equivariant by construction:  
**(D-F)  the 32 faces carry the uniform area measure  ⟹  A₅ \= A₆  ⟹  β₅ \= β₆ ,**  
**(D-E)  the 90 edges carry the uniform length measure  ⟹  ℓ₅₆ \= ℓ₆₆  ⟹  m₅₆ \= m₆₆ .**  
**Two conditions, two shape unknowns — and that is ALL they give.** (D-F) yields M₂ \= β·I₃₂ and (D-E) yields M₁ \= m·I₉₀. They do **not** yield M₁ \= M₂. Version 1.6 took that step and it does not follow. Writing r := β/m,  
**Δ₂ \= M₂^{1/2}B₂M₁⁻¹B₂ᵀM₂^{1/2} \= r·B₂B₂ᵀ ,   so   λ₁ \= r × 1.2428416164 .**  
This is verified exactly at r \= 0.5, 1, 2 and 3.7 (check T153). At r \= 2 the shape is perfectly uniform and yet λ₁ \= 2.4856832328, so the ledger is not preserved (check T153a). **A third condition, r \= 1, is required, and neither (D-F) nor (D-E) supplies it.** Version 1.6's companion check called the spectrum routine with both weights set to one, silently imposing r \= 1: a unit-normalised branch regression, not a derivation. It is retracted as a closure verification.  
**What r actually is.** On a two-dimensional spatial complex the Kogut–Susskind Hamiltonian gives m \= a/g² and β \= 1/(g²a), hence r \= 1/a² (check T153b). So r is not a free constant to be argued about: it is the lattice spacing, and it is **degenerate with a\_TI**. Gate F-S20.15d is therefore gate F-S19.3 in other variables, and λ₁ \= 1.2428416164 is quoted in the convention a\_TI \= 1 — legitimate only if the same convention is used when a\_TI is fixed, which is exactly what F-S19.3 leaves open.  
**The equal-area assignment is realisable, not merely stipulated.** Gauss–Bonnet requires 12A₅ \+ 20A₆ \= 4π, and A₅ \= A₆ \= 4π/32 \= 0.3926990817 satisfies it exactly (check T152). Relative to the round sphere this inflates pentagons by 1.3309 and shrinks hexagons by 0.8702 — an I\_h-invariant conformal factor, whose existence follows from a prescribed-volume argument applied equivariantly.

## **§20.4 Why this is not the mistake we made five times**

ZS-S20 has been wrong repeatedly, so the closure is put through the paper's own three tests before it is claimed.  
Table 20.2. The three non-circularity tests.

| TEST | ANSWER | GROUND |
| ----- | ----- | ----- |
| Is it equivalent to its own conclusion, as (H-UA) was? | No. | (H-UA) was a condition on the WEIGHTS and Theorem S20.E showed it equivalent to M \= m·I. (D-F) is a condition on the AREA MEASURE; the weights follow only through Theorem S20.S2, an independent result verified non-perturbatively (T134–T136, T143–T144). |
| Is it linear in the action, hence trivial by Theorem S20.T1? | No. | ZS-F39 is a statement about a stochastic register generator, not about the Yang–Mills action. It supplies data the action does not contain — which is exactly what the meta-observation of §21.2 says a closure must do. |
| Is the count right? | Yes, and it is exact rather than over-determined. | 2 conditions for 2 shape unknowns. A derivation, not a consistency check — and therefore falsifiable. |

**Two independent routes reject the same alternative.** The branch ZS-F39's selection lemma discards — the multiplicity-weighted, size-biased lift — is β ∝ n, that is ρ\_F \= 5/6 (check T154). ZS-S20 §10.2 discarded exactly that value at tree level by dual star compatibility, on entirely different grounds, and recorded it as CLOSED-NEGATIVE two versions before this section was written. The agreement was not arranged (check T155).

## **§20.5 What the closure rests on, stated as one sentence**

**Gate F-S20.15, split into four.** Version 1.6 called this “one sentence”. It is four, and they are of different kinds. **(a) explicit cellular lifts:** construct the 32-face and 90-edge GKLS generators and prove unitality, irreducibility and I\_h-equivariance. **(b) coarse-graining selection:** supply the independent target generator and the commutative diagram corresponding to ZS-F39 Lemma SEL. **(c) state-to-measure functor:** prove that I\_N/N maps to the area measure A\_f and the one-cell measure μ₁(e) — the type shift from a stationary density to a geometric valuation is precisely the kind of move §17.2 closed negative in the density-versus-rate case, and it is here unproven. **(d) relative normalisation r \= β/m,** which §22.3 shows is F-S19.3. Only when all four close does M₁ \= M₂ \= m·I become DERIVED-CONDITIONAL. The original claim was that ZS-F38's register is the Q \= 11 slot register, and the extension to the cellular registers is an **identification, not a theorem** (check T157). The entire closure rests on this one sentence, and if it fails the closure fails with it.  
That is the honest status: **ρ \= σ \= 1 is now PROVEN unconditionally by Theorem S20.C of §21, superseding this route for the shape; r \= β/m remains OPEN as F-S20.15d; and M₁ \= M₂ \= m·I is therefore still NOT established.** The shape branch closes; the full Hodge measure and its spectral normalisation do not. But it is a single, named, falsifiable identification between two corpus objects, replacing what five earlier versions left as an open family of measures with no principle to select among them. Compared with (R) ∧ (H-UA) ∧ (H-UA\*) ∧ (H-SYM) — four conditions which Theorem S20.E showed were equivalent to the answer already held — one condition drawn from an independent theorem of the corpus is a materially different position.

# **§21. Proposition S20.C and Theorem S20.M — The Clock Structure, and What It Does Not Give**

## **§21.1 What version 1.8 got wrong, stated first**

**Version 1.8 claimed that clock synchronisation forces ρ \= σ \= 1 unconditionally. That claim is withdrawn, and the reason is instructive.** The face parameter basis is ordered \[dF₅, dF₆, FAD₀, FAD₁\] — two diagonal entries and two off-diagonal adjacency conductances. The companion read coordinates 2 and 3 and called them β₅ and β₆. But M₂ := diag(β\_f), so β₅ and β₆ are coordinates 0 and 1\. What version 1.8 verified is that the two off-diagonal **conductances** are equal; the diagonal ratio is dF₅ : dF₆ \= 5 : 6, a different number, which the same companion reported in the very next check. This is the sixth instance in this paper of one failure mode — a proxy verified and reported as the target — and the structural response is a basis-label guard: every coordinate read now asserts the name of the basis element at that index (checks T158, T163).

## **§21.2 Proposition S20.C, now proven in exact arithmetic**

The construction itself survives and is worth keeping. Let L\_F be an I\_h-equivariant generator on the 32 faces with L\_F·1 \= 0, and L\_E an I\_h-equivariant symmetric operator on the 90 edges, neither built from M, both supported on the natural adjacency patterns, and require  
**B₂ L\_E \= L\_F B₂ .**  
Version 1.8 called the resulting nullspace an “exact nullspace computation”; it was a double-precision singular value decomposition. The companion now builds the 2912 × 12 integer matrix and computes over the rationals with SymPy: exact rank 10, exact nullity 2 (check T159).  
**Proposition S20.C (Cellular Clock Intertwining).** Every solution is  
**L\_E \= c\_G B₁ᵀB₁ \+ c\_F B₂ᵀB₂ ,   L\_F \= c\_F B₂B₂ᵀ .**  
\[PROVEN, exact rational arithmetic; check T160.\] The two basis vectors are (−B₁ᵀB₁, 0\) and (B₁ᵀB₁ \+ B₂ᵀB₂, B₂B₂ᵀ).  
**Three corrections follow immediately.** First, the second free direction is c\_G, the gradient or Gauss sector rate, which the face flux cannot see because B₂B₁ᵀ \= 0\. It is **not** r \= β/m, and version 1.8's identification of it as such is withdrawn (check T161). Second, one basis member has L\_F \= 0 and is therefore not a face clock at all, so the solution set is a **space**, not a cone, and no positivity or irreducibility was ever imposed (check T162). Third, what the proposition expresses is close to the standard chain-complex identity B₂(B₁ᵀB₁ \+ B₂ᵀB₂) \= (B₂B₂ᵀ)B₂, and the ±1 incidence amplitudes were already present in the basis construction. Its value is that the I\_h-equivariant local clock pair collapses to the counting Hodge-Laplacian form, not that anything about the Yang–Mills measure has been derived.

## **§21.3 Theorem S20.M — the reconstruction map, supplied**

Proposition S20.C is a statement about clock operators. The Hodge measure requires a map back to (M₁, M₂), and version 1.8 had none: it had merely replaced the unproven type shift “stationary density → geometric valuation” with an equally unproven one, “clock coefficients → action coefficients”. Here is the map, stated on the Yang–Mills operator itself with no clock basis in it.  
The flux equation of motion is Φ̈ \= −B₂M₁⁻¹B₂ᵀM₂ Φ, so the physical face evolution operator is N \= B₂M₁⁻¹B₂ᵀM₂. Impose one condition:  
**(H-EOM)   N is proportional to B₂B₂ᵀ .**  
**Theorem S20.M (Action Reconstruction).** Under (H-EOM) with I\_h-invariant positive M, the five distinct equations have the unique solution β₅ \= β₆ and m₅₆ \= m₆₆, and the proportionality constant is exactly r \= β/m. \[PROVEN by exact symbolic solution; check T166.\] The mechanism is visible by hand: the pentagon diagonal gives β₅/m₅₆ \= c and the (5,6) off-diagonal gives √(β₅β₆)/m₅₆ \= c, so β₅ \= √(β₅β₆) and hence β₅ \= β₆; the (6,6) off-diagonal then gives m₅₆ \= m₆₆; and the hexagon diagonal is satisfied identically.

## **§21.4 The disclosure that decides the status**

**The solution set of (H-EOM) is exactly {M₁ \= m·I, M₂ \= β·I}. So (H-EOM) is equivalent to its own conclusion.** By the test of Theorem S20.E — the test this paper applied to (H-UA) and used to demote version 1.0's central claim — (H-EOM) is an axiom **restatement**, not a derivation. We state this rather than let a referee find it.  
What has nonetheless changed is real but modest. One condition, stated directly on the physical flux-evolution operator, now replaces the four conditions (R) ∧ (H-UA) ∧ (H-UA\*) ∧ (H-SYM), and it comes with an exact reconstruction theorem instead of an unproven type shift. The question “what is the Hodge measure?” has become the single question “**is the physical flux evolution a synchronised cellular clock?**”. That is a better-posed question than any earlier version asked, and it is falsifiable. It is not an answer.  
**And r is still not determined.** Theorem S20.M returns the proportionality constant as r itself, so r remains the free scale, exactly as gate F-S20.15d and, through r \= 1/a², as F-S19.3. Nothing in §21 bears on it.

# **§22. The Closure — Arithmetic Rigidity and the Incidence Sum Rule**

## **§22.1 Why every previous attempt failed, in one sentence**

Nine versions proposed conditions on M, and each turned out to have {M₁ \= m·I, M₂ \= β·I} as its solution set — (H-UA) by Theorem S20.E, (H-EOM) by §21.4. A condition whose solution set is the answer is a restatement. The corrected meta-observation of §19.2 says what is needed instead: **two conditions, each individually much weaker than the answer, whose intersection is a point.** That is over-determination, and §22 supplies it.

## **§22.2 An exact algebraic fact, proven first**

The incidence matrix B₂ is integral, so B₂B₂ᵀ is an integer matrix and its characteristic polynomial factors over ℤ. Computed exactly:  
**λ (λ−6)⁴ (λ−8)⁵ (λ²−10λ+22)⁵ (λ⁴−22λ³+166λ²−480λ+380)³ .**  
**Corollary S20.Q.** The quartic is irreducible over ℚ, and **both ledger eigenvalues are its roots**: λ₁ \= 1.2428416164 and λ\_h \= 7.5210904061 (checks T169, T170). They are algebraic integers of degree 4\. Until now the corpus carried them as ten-digit decimals; they have an exact minimal polynomial.  
**The four roots sum to 22 by Vieta's formula,** since 22 is the λ³ coefficient of the quartic (check T171); equivalently it is the trace of Δ₂ on the T-type sector. The numerical equality 22 \= 2Q with Q \= 11 is recorded as an **observation** only. No connecting theorem is claimed, and §22.5a states the separation explicitly. The anti-numerology gate of §12 is narrowed by the Vieta identity, not discharged by it.

## **§22.3 The two conditions**

**(H-ALG) Integral counting-spectrum degeneracy.** The characteristic polynomial of N \= B₂M₁⁻¹B₂ᵀM₂ is integral and factors over ℤ with the multiplicity pattern (1,1), (1,4), (1,5), (2,5), (4,3). The name matters and §22.4a explains it: the multiplicity-five linear level is not supplied by any five-dimensional irreducible representation, so calling this an “isotypic pattern” would be wrong. This is a statement about arithmetic. It does not mention a metric, an area, a register or a measure, and it does not say that M is uniform.  
**(H-TR) The incidence sum rule.** Tr(Δ₂) \= 2E \= 180\. The left side is Σ\_k ω\_k², the total squared-frequency content of the magnetic sector; the right side counts the face–edge incidences, that is, the elementary plaquette–link couplings. The rule assigns one unit of spectral weight to each coupling.  
**The parametrisation carries r explicitly.** Version 1.7 showed that writing only (ρ, σ) silently sets r \= β/m to 1\. Here m₆₆ \= 1, m₅₆ \= σ, β₆ \= r and β₅ \= rρ, so r is a third independent unknown throughout and the objection does not apply.

## **§22.3a Lemma S20.A1 — the exact block decomposition**

The proof below rests on the claim that three linear eigenvalues exist for **every** positive parameter triple. Version 2.1 asserted this and reported it “verified against the full 32 × 32 operator at generic points”, which is not a proof of a universally quantified statement. The exact argument is short and belongs in the body.  
Order the faces as 12 pentagons followed by 20 hexagons and write C for the pentagon–hexagon incidence block and A₆₆ for the hexagon–hexagon one. In the coordinates x \= r/σ, y \= rρ/σ, z \= r,  
**Δ₂ \= \[\[ 5y·I₁₂ , √(xy)·C \] , \[ √(xy)·Cᵀ , (3x+3z)·I₂₀ \+ z·A₆₆ \]\] .**  
**Lemma S20.A1 (Exact block decomposition).** A₆₆ and CᵀC commute. Consequently Δ₂ decomposes into joint sectors labelled by the simultaneous eigenvalues (s², a), with (s², a, multiplicity) equal to (0, 0, 4), (0, 2, 4), (5−2√5, √5, 3), (3, −1, 5), (5+2√5, −√5, 3\) and (15, −3, 1). On the kernel sector s² \= 0 the operator is exactly (3x+3z)·I \+ z·A₆₆, so it contributes the two **linear** levels  
λ\_A \= 3x \+ 3z   and   λ\_B \= 3x \+ 5z ,   each of multiplicity 4 and each free of y .  
On the sector (15, −3) the 2 × 2 block is \[\[5y, √(15xy)\],\[√(15xy), 3x\]\], whose determinant vanishes **identically**. Its eigenvalues are therefore 0 — the topological zero mode — and 5y \+ 3x, so **5y \+ 3x is the unique nonzero multiplicity-one level, for every positive (x, y, z)**. \[PROVEN; checks T182–T184.\]  
**This is what makes the branch analysis exhaustive rather than illustrative.** Restoring r and writing X \= ρ, Y \= 1/σ, the three levels are r(3Y+3), r(3Y+5) and rY(5X+3) with multiplicities 4, 4 and 1 — exactly the objects §22.4 uses, now established for all positive parameters rather than sampled.

## **§22.4 Theorem S20.A, proved analytically over all positive reals**

**Version 2.0 claimed uniqueness by an “exhaustive exact rational search”. That label is retracted.** The companion tested 9³ \= 729 points of a fixed rational grid; that establishes nothing about ℚ₍₊₎³, let alone ℝ₍₊₎³. It is replaced here by a short analytic proof, which also removes the dominant cost from the companion: the retracted search factorised 729 characteristic polynomials of size 32, the proof factorises none.  
Write X \= ρ, Y \= 1/σ and keep r explicit. By Lemma S20.A1, for every positive (X, Y, r) the characteristic polynomial contains three linear factors (checks T172, T182–T184):  
**λ \= r(3Y+3) with multiplicity 4 ,   λ \= r(3Y+5) with multiplicity 4 ,   λ \= rY(5X+3) with multiplicity 1 .**  
**Step 1\.** The pattern requires a linear level of multiplicity five. Five can only be 4 \+ 1, and r(3Y+3) ≠ r(3Y+5) for r \> 0, so the singlet must collide with one of the two quadruplets. Exactly two branches (check T173):  
branch A:  rY(5X+3) \= r(3Y+5)  ⟺  XY \= ρ/σ \= 1 ;      branch B:  rY(5X+3) \= r(3Y+3)  ⟺  XY \= ρ/σ \= 3/5 .  
**Step 2\.** The sum rule is exactly Tr Δ₂ \= 60 r (XY \+ Y \+ 1\) \= 180, so r \= 3/(XY \+ Y \+ 1\) (check T174).  
**Step 3, branch A.** XY \= 1 gives r \= 3/(Y+2), and the multiplicity-five level is r(3Y+5) \= 9 − 3/(Y+2), which for Y \> 0 lies strictly between 7.5 and 9\. Integrality leaves only the value 8, forcing Y \= 1, hence σ \= 1, ρ \= 1 and r \= 1 (check T175).  
**Step 4, branch B.** XY \= 3/5 gives r \= 15/(5Y+8), and the remaining quadruplet is r(3Y+5) \= 9 \+ 3/(5Y+8), which for Y \> 0 lies strictly between 9 and 9.375. That interval contains no integer, so the branch is empty (check T176).  
**Theorem S20.A. Within the positive diagonal I\_h-invariant three-ratio family on K\_TI**, the conditions (H-ALG) and (H-TR) have the unique solution ρ \= σ \= r \= 1, hence M₁ \= M₂ \= m·I, Δ₂ \= B₂B₂ᵀ, and λ₁ \= 1.2428416164 at multiplicity three. \[PROVEN over all positive reals; checks T172–T177.\] **No ledger number moves.**  
**The domain restriction is not decoration.** §3 states that diagonality of M₁ is not assumed, but §22 works entirely inside the diagonal family (m₅₆, m₆₆, β₅, β₆). Non-diagonal I\_h-equivariant mass matrices, the Whitney/FEEC branch and any off-diagonal Gram structure arising from an abstract cochain embedding are **not covered** and remain open under gate F-S20.5 (check T178).

## **§22.4a A correction to the name, and to what the pattern means**

Version 2.0 called the target factorisation an “I\_h isotypic pattern”. That is misleading and is corrected. A generic I\_h-invariant metric in this family already yields **two** distinct multiplicity-4 linear factors and two singlets; the multiplicity-5 linear level is **not** produced by a five-dimensional irreducible representation but by an accidental collision of a four-dimensional block with a singlet — which is exactly why the two branches above exist at all. The condition is therefore renamed **(H-ALG), integral counting-spectrum degeneracy**: it demands an arithmetic coincidence that symmetry does not supply, which is precisely what makes it informative rather than vacuous.

## **§22.5 The closure put through the paper's own three tests**

Table 22.2. Non-circularity tests, applied before submission rather than after review.

| TEST | RESULT | GROUND |
| ----- | ----- | ----- |
| Theorem S20.E test: is the hypothesis equivalent to its conclusion? | PASSED | Neither (H-ALG) nor (H-TR) has {M uniform} as its solution set. (H-ALG) does not even force ρ \= σ (check T172); (H-TR) alone leaves a surface (T174). Only the intersection is a point. |
| Theorem S20.T1 test: is it linear in the action, adding no data? | PASSED | (H-ALG) is arithmetic. It is not a read-out of the action and it supplies information the action does not contain — precisely what §19.2 says a closure must do. |
| Version 1.7 test: is r carried explicitly? | PASSED | r is a third independent parameter throughout, and it is fixed to 1 by the intersection rather than by a convention. |

**What is assumed, stated plainly.** (H-ALG) is a rigidity postulate: the spectral data of a cellular gauge operator built from an integral incidence matrix remain algebraic integers with the isotypic factorisation. (H-TR) is a sum rule. Neither is derived from ZS-S14, and we do not pretend otherwise. They are the two conditions the bridge now rests on, replacing the four of version 1.2 — and unlike those four, they are not equivalent to the answer, they are stated without reference to any metric, and each is independently falsifiable: exhibit an admissible cellular gauge operator violating integrality, or a normalisation in which the sum rule fails, and the closure falls.

## **§22.5a Epistemic status, separated into its two layers**

**Version 2.0 wrote “over-determination rather than a new axiom”, and that phrasing was too kind to itself.** Non-circularity and physical necessity are different things. The correct statement separates two layers.  
Table 22.3. What is proven and what is postulated.

| STATEMENT | STATUS | NOTE |
| ----- | ----- | ----- |
| (H-ALG) ∧ (H-TR) ⟹ M₁ \= M₂ \= m·I, within the positive diagonal I\_h-invariant family | PROVEN | analytic, all positive reals, §22.4 |
| ZS-S14 ⟹ (H-ALG) ∧ (H-TR) | NOT PROVEN | no derivation exists |
| (H-ALG) integral counting-spectrum degeneracy | HYPOTHESIS-strong | an added arithmetic postulate |
| (H-TR) incidence sum rule | HYPOTHESIS-strong | a normalisation postulate; see below |
| Diagonal Hodge measure selection | DERIVED-CONDITIONAL | conditional on the two above |
| Full non-diagonal Hodge measure | OPEN | gate F-S20.5 |
| Physical normalisation to MeV | OPEN | gate F-S19.3 |

**(H-TR) may be no more than a unit convention, and this must be said.** Given a shape, the sum rule fixes r \= 3σ/(ρ \+ 1 \+ σ) — it selects the normalisation, not the shape. But §20.3 identified r \= 1/a², so requiring Tr Δ₂ \= 2E plausibly amounts to choosing a\_TI \= 1\. If so, (H-TR) is a lattice-unit convention rather than a physical derivation, and gate F-S19.3 — the independent fixing of a\_TI together with the g\_S14 ↔ g\_MS-bar scheme relation — remains exactly as open as before. **Consequently the dimensionless λ₁ \= 1.2428416164 closes conditionally, but Λ\_QCD \= 264.1 MeV does not.** Version 2.0 asserted otherwise and that assertion is withdrawn.  
**And the number 22 carries two claims, not one.** That the four quartic roots sum to 22 is Vieta's formula: PROVEN. That this 22 equals 2Q with Q \= 11, and therefore reflects the Z-Spin register structure, is an **OBSERVATION** awaiting a connecting theorem. Version 2.0 wrote that Vieta removes the coincidence; that is one step too strong. Vieta explains the spectral origin of the number 22 — it does not explain why 22 should be twice an independently defined Q. The anti-numerology gate of §12 is narrowed by this, not discharged.

## **§22.5b Self-referential pass — the proof re-derived by a different method**

Six of the ten retractions in this paper had one shape: a proxy verified and reported as the target. The response is not to promise more care but to re-derive by a second route and report the comparison. The symbolic argument of §22.4 is therefore checked against dense numerical sampling of the full 32 × 32 operator.  
Table 22.4. Independent confirmation of Theorem S20.A.

| CHECK | RESULT |
| ----- | ----- |
| three predicted linear eigenvalues at 400 random positive (ρ, σ, r) | worst mismatch 6.8 × 10⁻¹³ |
| their multiplicities 4, 4, 1 at those points | 0 violations |
| branch A quintuplet swept over σ ∈ (0.01, 100\) | numerical range (7.507, 8.971); only integer 8 |
| branch B quadruplet swept over the same range | numerical range (9.006, 9.373); no integer |
| the unique point, reached by the numerical route | λ₁ \= 1.2428416164 at multiplicity 3 |

**A document-level audit was run alongside it (check T196).** No part of the paper now asserts a verdict different from DERIVED-CONDITIONAL: the two surviving occurrences of “the bridge closes” are a version 1.6 retraction record and a conditional methodological sentence. NC-S20.8, F-S19.3, F-S20.2, F-S20.5 and the OPEN-TERMINAL gates all agree with that verdict. Every PROVEN label in §22 is backed by an executable check, every check identifier is unique, and no executable check is a literal True.

## **§22.6 A route executed and closed negative**

One further route was tried and failed, and is reported because a paper that only records its successes is not being tested. K\_TI discretises the Z-sector two-sphere, so the low spectrum of Δ₂ should approximate the Laplace–Beltrami eigenvalues ℓ(ℓ+1). Under I\_h the continuum ℓ \= 3 multiplet branches as T₂u ⊕ G\_u and ℓ \= 4 as G\_g ⊕ H\_g, so those degeneracies are **not** symmetry-protected and their restoration would have been a genuine condition mentioning no metric. It fails: at the counting star the two multiplets split by 21.3 % and 11.5 %, and a two-dimensional scan places the minima at mutually inconsistent points far from (1, 1\) (check T176). **Continuum degeneracy restoration does not select the counting star, and does not select anything consistent.** The route is CLOSED-NEGATIVE.

# **§23. Retraction Register**

ZS-S19 established that a retraction hiding its falsifier is not a retraction. Four claims of version 1.0 are withdrawn here, each with the statement that killed it.  
Table 18.1. Claims withdrawn in version 1.2.

| v1.0 CLAIM | FALSIFIER | v1.1 REPLACEMENT |
| ----- | ----- | ----- |
| “(R\_C) is demoted from an axiom to a theorem.” | (R\_C) is an integration and trace prescription; Cor. S20.A establishes only its spectral consequence. Theorem S20.E shows the hypothesis sets are equivalent on K\_TI, so no economy is gained. | §9.3: the spectral consequence is derived conditionally; the literal counting-trace prescription is no longer required; no logical economy is claimed. |
| “One axiom applied twice; one fewer postulate than ZS-S19.” | (H-SYM) was used without being counted. §15 exhibits an explicit positive non-uniform solution of (H-UA) ∧ (H-UA\*) with kernel dimension 11\. | Prop. S20.P (same functional, two complexes) plus an explicit count of four conditions in Table 15.2. |
| “Verification 83/83 PASS.” | Fifteen of the eighty-three were declarative registry statements carrying no computation, and the anti-regression block asserted absence without scanning anything. | 110 PASS \= 101 executable \+ 9 declarative, with a real ast-based static analysis of the production slice. |
| Metadata date “March 2026”. | The paper executes ZS-S19 v1.6 FINAL, dated July 2026, and cites ZS-S17 v2.2, ZS-S18 v1.6, ZS-F37–F39 and ZS-M44 of the same month. | July 2026, with the version history corrected accordingly. |

Table 18.2. Version 1.1 claims withdrawn in version 1.2.

| v1.1 CLAIM | FALSIFIER | v1.2 REPLACEMENT |
| ----- | ----- | ----- |
| Theorem S20.D as stated (“vertex-transitivity forces uniformity”). | Vertex-transitivity of the COMPLEX does not make a given weight assignment invariant. §15 of v1.1 proved this by counterexample, but §7 was not updated. | Theorem S20.D restated with weight equivariance (H-SYM) in the hypotheses, and renamed accordingly. |
| Corollary S20.A under (R) ∧ (H-UA) ∧ (H-UA\*). | The same counterexample. (H-SYM) is required. | (R) ∧ (H-UA) ∧ (H-UA\*) ∧ (H-SYM), propagated to §9, the Abstract, Table 13.1 and the status delta. |
| “Outcome A realised; F-S18.16 and F-S19.6 CLOSE.” | Outcome A as pre-registered in Table 1.1 has two clauses; only the weight pattern was obtained. Both gates contain a reduction half and a selection half, and only the reduction halves closed. | Numerical branch A\_weights; gates split into F-S18.16a/b and F-S19.6a/b, with the b-halves OPEN-TERMINAL. |
| Gate F-S20.9 as Z\_E(ρ) \= Z\_B(ρ). | That condition fixes the overall temporal–spatial normalisation and does not target ρ, which is an orbit anisotropy (§17.4). | F-S20.9a and F-S20.9b, the latter carrying the orbit-contrast renormalisation Δβ\_R \= 0\. |
| “101 executable checks.” | T14 and T92 were counted as executable while carrying a literal True. | 114 executable \+ 9 declarative, with no executable check a literal True. |

Table 18.3. Version 1.2 claims withdrawn in version 1.3.

| v1.2 CLAIM | FALSIFIER | v1.3 REPLACEMENT |
| ----- | ----- | ----- |
| Theorem S20.N as a single PROVEN statement about ZS-S14. | A Cholesky basis is not an admissible cochain embedding: it need not consist of differential forms, be I\_h-equivariant, gauge-covariant or cell-local, nor satisfy L\_{k+1} d\_K \= d\_K L\_k. | SPLIT: S20.N-a (abstract, PROVEN) and S20.N-b (physical, now PROVEN by explicit construction of two admissible embeddings, §17.1a). |
| “The counting star is not radiatively stable”; “no possibility of cancellation”; C₋(1) ≠ 0 as a prediction. | The Yang–Mills one-loop determinant contains gluon, ghost and longitudinal contributions whose orbit contrasts may cancel. A scalar face Laplacian cannot decide it. | §17.5 retitled to local DISTINGUISHABILITY; C₋(1) ≠ 0 demoted to a HYPOTHESIS-strong pre-registered target. |
| “never locally spectrally equivalent” (T110). | Only six values of t were audited. | “the two local heat kernels differ at all six audited t-values”. |
| Λ\_QCD \= 261.2 MeV at ρ\_F \= 5/6. | Λ\_QCD ∝ 1/λ₁, not √λ₁. The companion and Appendix B both give 270.02 MeV. | 270.02 MeV (checks T64, T119). |
| “1 % in ρ moves Λ\_QCD by about 0.04 %.” | dλ₁/dρ \= 0.10623798 gives 0.0855 % per 1 %. | 0.0855 %, in the opposite sense (check T120). |

Table 19.4. Version 1.3 claims withdrawn in version 1.4.

| v1.3 CLAIM | FALSIFIER | v1.4 REPLACEMENT |
| ----- | ----- | ----- |
| Gate F-S20.11: the flat and round-sphere candidates are EXCLUDED by Λ\_QCD; the counting star is the unique survivor; the bridge is closed at OBSERVATION. | The three gaps were computed in three different unit conventions. Under g ↦ s²g, ⋆₁ is invariant but ⋆₂ carries s⁻², so λ₁ ↦ s⁻²λ₁. Rescaling the flat star by s \= 0.5382277383 \= a\_TI reproduces the counting star exactly. Independently, absolute MeV requires a\_TI and scheme matching, which F-S19.3 leaves OPEN. | RETRACTED IN FULL (§17.8). Only scale-free quantities are compared, in Table 17.5, and no candidate is excluded. |
| “unique surviving corpus-internal candidate”. | No completeness theorem exists for the candidate set; S20.N-a implies the family of I\_h-invariant metrics is large. | At most “the survivor among the candidates audited here” — and after the scale correction, not even that. |
| Theorem S20.N-b: two admissible cochain embeddings, PROVEN. | What was constructed is two diagonal circumcentric DEC stars. No maps W\_k : C^k → Ω^k(Σ, su(3)) were built, and R\_kW\_k \= I, dW\_k \= W\_{k+1}∘d\_K and gauge intertwining were never verified. A Whitney Gram matrix is non-diagonal; a DEC star is mass-lumped. | Theorem S20.N-b′, two non-proportional geometric DEC stars, COMPUTED. Explicit embeddings are OPEN as gate F-S20.2a. |
| “The flat polyhedral metric is not an added assumption; ZS-A7 §2.2 presupposes it.” | Σᵥδᵥ \= 2πχ is a topological identity holding for every convex polyhedron; it does not select the regular realisation. Likewise Z \= ∂X with X smooth does not force a constant-curvature boundary metric. | Both are corpus-MOTIVATED candidates, not corpus-DERIVED metrics. |
| T118 counted as an executable physics check. | It compared against a band hard-coded as “roughly 250–300 MeV”, with no external data file, scheme, scale definition or error propagation. | Replaced by the scale theorem (T118, T119) and an explicit declarative retraction (T120). |

Table 22.5. Version 1.4 claims corrected in version 1.5.

| v1.4 CLAIM | FALSIFIER | v1.5 REPLACEMENT |
| ----- | ----- | ----- |
| Front matter: version, check counts and companion filename. | The title block still read v1.3 with 133 PASS and zs\_s20\_verify\_v1\_3.py while the body described v1.4 with 145 PASS. | Front matter regenerated from the companion output: v1.5, 156 PASS, zs\_s20\_verify\_v2\_2.py. |
| T123 and T124 counted as executable checks of the plaquette-clock route. | They exercise Perron–Frobenius on a random 12 × 12 matrix. The 1342-dimensional ZS-S14 transfer is never constructed. | A third check kind, PROXY, is introduced; both are reclassified and excluded from the physics count. |
| (H-PSM) as one hypothesis; Theorem S20.P1. | The hypothesis bundles a mathematical condition with a physical identification, and §17.2 forbids reading a rate off a density in general. Also T\_Z \= T\_Z\[M₁, M₂\], so the object is a self-consistency equation, not a fixed measure. | Split into (H-PSM-1) and (H-PSM-2); demoted to Proposition S20.P1; the circularity and the undefined state space are stated in §18.2. |
| “the transfer that ZS-S14 itself defines”. | ZS-S14 supplies no cellular projection, Euclideanisation, gauge projection or normalisation. Theorem S20.N-a says it cannot. | “a transfer constructed from the ZS-S14 action by an explicit prescription”. |
| F-S20.1 printed in the OPEN registry. | It is CLOSED-NEGATIVE, refuted in §6. | Moved to the declarative CLOSED-NEGATIVE registry; 17 active OPEN gates. |

Three claims are retained unchanged, having survived five rounds of review: the refutations of (L) and of the arithmetic-versus-harmonic form of (H-PD) in §6; the CLOSED-NEGATIVE status of ρ\_F \= 5/6 at tree level in §10.2, now read against the radiative prediction of §17.5; and Theorems S20.O, S20.R and S20.E of §14, which §17.1 strengthens rather than corrects.

# **§24. Conclusion**

Successive versions have attacked one link: the step from the ZS-S14 action to the pair (M₁, M₂). The other links are supplied — R\_TI written explicitly, the electric coefficients from a time-like plaquette rather than a measure, the Legendre transform in both forms, the Gauss law and the metric-free census 59 \+ 31, the Step-8 regression gate. This is where the remaining link stands.  
**What is proven is negative, and one mechanism explains it.** Hermiticity, Gram-matrix realisability and linear response all return the measure they were given, because a fixed-point condition built solely from the action admits the action as a solution. Symmetry does not protect ρ \= 1; register democracy confuses a density with a rate; integrality has no charge-lattice bridge. Closure requires a step that is non-quadratic or a genuine coarse-graining, and the heat-kernel semigroup — verified here, not cited — is the one such step available in exact form.  
**What version 1.9 adds.** Proposition S20.C determines the entire space of synchronised cellular clocks in exact rational arithmetic, and Theorem S20.M supplies the map back to the action that every earlier attempt lacked: (H-EOM) forces β₅ \= β₆ and m₅₆ \= m₆₆ uniquely, with constant r. Together they convert “what is the Hodge measure?” into “is the physical flux evolution a synchronised cellular clock?” — one falsifiable question in place of four conditions.  
**What must be disclosed.** The solution set of (H-EOM) is exactly the uniform measure, so (H-EOM) is equivalent to its conclusion and is a restatement, not a derivation. Version 1.8 asserted an unconditional shape closure by reading two off-diagonal conductances as β₅ and β₆; that assertion is withdrawn in §22, and a basis-label guard now makes the same error impossible. The relative normalisation r is untouched by any of this and remains gate F-S19.3 in other variables.  
**Version 2.1 states the result in two layers.** The arithmetic uniqueness theorem — that (H-ALG) and (H-TR) have the unique solution ρ \= σ \= r \= 1 within the positive diagonal I\_h-invariant family — is PROVEN, analytically and over all positive reals. The physical selection, that ZS-S14 implies those two conditions, is not proven and we do not pretend it is. Both are HYPOTHESIS-strong postulates, and (H-TR) may be nothing more than the convention a\_TI \= 1\. The bridge is DERIVED-CONDITIONAL.  
What that buys is still substantial. Nine earlier conditions were shown to be restatements of their own conclusions; these two are not, and their intersection is a point rather than a family. The ledger is untouched: λ₁ \= 1.2428416164, and it is now known exactly as a root of λ⁴ − 22λ³ \+ 166λ² − 480λ \+ 380 rather than as a decimal. What is not bought: Λ\_QCD \= 264.1 MeV, which still waits on F-S19.3; the non-diagonal Hodge family, which still waits on F-S20.5; and any derivation of the two hypotheses from the master action.  
Ten rounds of review have removed more than they added, and that is the point. What survives is a theorem about why a whole class of attempts cannot work, a verified identity locating the exception, an exact algebraic characterisation of two ledger constants, and a conditional closure whose two conditions are named, restricted in domain, separated from their justification, and independently falsifiable. Whether they are the right conditions is now a question for someone else to answer.

# **Acknowledgements & Code Availability**

This paper was produced under the Z-Spin adversarial-review discipline established across ZS-S17 through ZS-S19, in which every published claim is submitted to counterexample before it is allowed to carry load. Two candidate axioms of the exploration phase, (L) and the arithmetic-versus-harmonic form of (H-PD), were refuted in that process and are retracted in §6 with their falsifiers stated in full.  
The companion verification suite zs\_s20\_verify\_v2\_2.py is a single self-contained file. It declares its dependencies at the top (numpy, mpmath, sympy, scipy) and raises ImportError rather than degrading a missing dependency into an additional OPEN gate. OPEN gates are printed and are never counted as PASS. An anti-regression block asserts that every value retracted in this paper or in ZS-S19 is produced by no code path. Results are emitted as JSON between the delimiters BEGIN\_ZS\_S20\_RESULTS and END\_ZS\_S20\_RESULTS, with the SHA256 of the file and the full environment recorded. The truncated icosahedron is rebuilt from Cartesian coordinates rather than imported, so that every locked corpus number is reproduced rather than restated; the Kirchhoff identity det′Δ₀/V \= τ is used as the regression test on the rebuilt incidence matrices.

# **Appendix A. The Complex, the Group Action, and the Orbit Structure**

The 60 vertices are the even permutations of (0, ±1, ±3φ), (±1, ±(2+φ), ±2φ) and (±φ, ±2, ±(2φ+1)) with φ the golden ratio; edges are the nearest-neighbour pairs; faces are recovered by the left-turn walk about the outward normal. This yields V \= 60, E \= 90, F \= 32, χ \= 2, all vertices of degree 3, 12 pentagons and 20 hexagons, and B₂B₁ᵀ \= 0 to better than 10⁻¹².  
The group is constructed as the set of orthogonal 3 × 3 matrices mapping the vertex set to itself, obtained by fixing three affinely independent vertices; there are exactly 120\. Its orbits are: one vertex orbit of size 60 (vertex-transitive), two edge orbits of sizes 60 and 30, and two face orbits of sizes 12 and 20\. The equivariance residual max\_g ‖ |B₂|(P\_F(g), P\_E(g)) − |B₂| ‖ vanishes to better than 10⁻¹² over all 120 elements.

# **Appendix B. Outcome-B Damage Audit, Retained as Insurance**

Table B.1. The audited window, recomputed here independently. Retained so that a future failure of (H-UA\*) has its damage already bounded. Λ\_QCD ∝ 1/λ₁ with the ZS-S7 normalisation.

| ρ \= β₅/β₆ | m₅₆/m₆₆ | λ₁ | Δλ₁ (%) | Ω₀ | Λ\_QCD (MeV) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 0.750000 | 0.875000 | 1.1926356414 | −4.0396 | 1.09207859 | 275.218 |
| 0.833333 \= 5/6 | 0.916667 | 1.2155777721 | −2.1937 | 1.10253244 | 270.023 |
| 1.000000 | 1.000000 | 1.2428416164 | 0.0000 | 1.11482807 | 264.100 |
| 1.200000 | 1.100000 | 1.2545633521 | \+0.9431 | 1.12007292 | 261.632 |
| 1.333333 \= 4/3 | 1.166667 | 1.2547087463 | \+0.9548 | 1.12013782 | 261.602 |

Over ρ ∈ \[3/4, 4/3\] the shift in Ω₀ is at most 2.0406 %, below the 2.5 % bound ZS-S19 recorded, and Λ\_QCD stays within \[261.6, 275.3\] MeV. Note, however, ZS-S19's third self-retraction: this band belongs to the audit window only. The compatibility line is unbounded, with Λ\_QCD → ∞ as ρ\_F → 0 and → 429.7 MeV as ρ\_F → ∞. No claim is made about the whole line.

# **Appendix C. The Retracted Candidates, Stated in Full**

ZS-S19 §8.6 requires that a retraction which hides its own falsifier is not a retraction. The two candidates are therefore recorded here in the form in which they were proposed.  
Candidate (L), Regulator Locality: "the regulator assigns to each cell a weight depending only on the isomorphism class of that cell as an oriented cell together with its own boundary data." Falsifier: on a hypercubic lattice, temporal and spatial plaquettes are both squares and carry β\_τ ≠ β\_s; the Hamiltonian limit requires the anisotropy. RETRACTED as a selection principle; Lemma S20.T is what survives.  
Candidate (H-PD) in arithmetic-versus-harmonic form: "the star-compatibility relation has the same functional form in the Lagrangian variables (M₁, M₂) and in the Hamiltonian variables (M₁^{−1}, M₂^{−1}), whence AM \= HM and β\_{f₁} \= β\_{f₂}." Falsifier: in two dimensions the dual edge ⋆e is bounded by the dual faces ⋆v₁, ⋆v₂ associated with the endpoints of e, not by ⋆f₁, ⋆f₂, so the two relations are not comparable and the identification is void. RETRACTED; the corrected implementation is Theorem S20.D.

# **References**

\[1\] K. Kang, "Geometric Impedance: A \= 35/437," ZS-F2 v1.0, Z-Spin Cosmology Collaboration (2026).  
\[2\] K. Kang, "Gauge Symmetry Constraint: Why Q \= 11," ZS-F5 v1.0, Z-Spin Cosmology Collaboration (2026).  
\[3\] K. Kang, "Electroweak Completion," ZS-S4, Z-Spin Cosmology Collaboration (2026).  
\[4\] K. Kang, "The Spinor Mass Gap," ZS-S7 v1.0, Z-Spin Cosmology Collaboration (April 2026).  
\[5\] K. Kang, "Master Action Total Closure," ZS-S14 v2.0, Z-Spin Cosmology Collaboration (May 2026).  
\[6\] K. Kang, "The Glueball Hyperfine Structure from a Truncated-Icosahedron Cochain Vertex," ZS-S17 v2.2 FINAL, Z-Spin Cosmology Collaboration (July 2026).  
\[7\] K. Kang, "The Symmetric Gauge Observable," ZS-S18 v1.6 FINAL, Z-Spin Cosmology Collaboration (July 2026).  
\[8\] K. Kang, "The Metric-Selection Audit of the Z-Spin Yang–Mills Bridge," ZS-S19 v1.6 FINAL, Z-Spin Cosmology Collaboration (July 2026).  
\[9\] K. Kang, "The Conditional Register-Trace Normalization of the Z-Spin Block-Laplacian," ZS-M44 v1.6, Z-Spin Cosmology Collaboration (July 2026).  
\[10\] K. Kang, "The Action-Level Two-Leg Law," ZS-F37 v1.3, Z-Spin Cosmology Collaboration (July 2026).  
\[11\] K. Kang, "The Register Clock Identity," ZS-F38 v1.2, Z-Spin Cosmology Collaboration (July 2026).  
\[12\] K. Kang, "The Seam Uniformization Theorem," ZS-F39 v1.1, Z-Spin Cosmology Collaboration (July 2026).  
\[13\] K. G. Wilson, "Confinement of quarks," Phys. Rev. D 10, 2445 (1974).  
\[14\] J. Kogut and L. Susskind, "Hamiltonian formulation of Wilson's lattice gauge theories," Phys. Rev. D 11, 395 (1975).  
\[15\] M. Creutz, "Gauge fixing, the transfer matrix, and confinement on a lattice," Phys. Rev. D 15, 1128 (1977).  
\[16\] M. Creutz, Quarks, Gluons and Lattices (Cambridge University Press, Cambridge, 1983).  
\[17\] R. F. Arnold, The Discrete Hodge Star Operator and Poincaré Duality, Ph.D. thesis, Virginia Polytechnic Institute and State University (2012).  
\[18\] S. O. Wilson, "Cochain algebra on manifolds and convergence under refinement," Topology Appl. 154, 1898 (2007).  
\[19\] D. Kim, "Discrete Hodge star operator on 3-manifolds," arXiv:1801.03969 \[math.AT\] (2018).  
\[20\] A. N. Hirani, Discrete Exterior Calculus, Ph.D. thesis, California Institute of Technology (2003).  
\[21\] M. Desbrun, A. N. Hirani, M. Leok and J. E. Marsden, "Discrete Exterior Calculus," arXiv:math/0508341 (2005).  
\[22\] A. Gillette and C. Bajaj, "Dual formulations of mixed finite element methods with applications," Comput. Aided Des. 43, 1213 (2011), arXiv:1012.3929.  
\[23\] J. Dodziuk, "Finite-difference approach to the Hodge theory of harmonic forms," Amer. J. Math. 98, 79 (1976).  
\[24\] J. Dodziuk and V. K. Patodi, "Riemannian structures and triangulations of manifolds," J. Indian Math. Soc. 40, 1 (1976).  
\[25\] H. Whitney, Geometric Integration Theory (Princeton University Press, Princeton, 1957).  
\[26\] A. Bossavit, Computational Electromagnetism (Academic Press, San Diego, 1998).  
\[27\] G. Kirchhoff, "Ueber die Auflösung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung galvanischer Ströme geführt wird," Ann. Phys. Chem. 72, 497 (1847).  
\[28\] F. Harary, Graph Theory (Addison-Wesley, Reading, 1969).  
\[29\] E. Seneta, Non-negative Matrices and Markov Chains, 2nd ed. (Springer, New York, 1981).  
\[30\] P. Walters, An Introduction to Ergodic Theory, Graduate Texts in Mathematics 79 (Springer, New York, 1982).  
\[31\] G. H. Hardy, J. E. Littlewood and G. Pólya, Inequalities, 2nd ed. (Cambridge University Press, Cambridge, 1952).  
\[32\] W. Magnus, "On the exponential solution of differential equations for a linear operator," Comm. Pure Appl. Math. 7, 649 (1954).  
\[33\] V. N. Gribov, "Quantization of non-Abelian gauge theories," Nucl. Phys. B 139, 1 (1978).  
\[34\] D. Zwanziger, "Fundamental modular region, Boltzmann factor and area law in lattice gauge theory," Nucl. Phys. B 412, 657 (1994).  
\[35\] H.-P. Pavel, "SU(3) Yang–Mills Hamiltonian in the flux-tube gauge," arXiv:1611.06542 \[hep-th\].  
\[36\] C. Lanczos, "An iteration method for the solution of the eigenvalue problem of linear differential and integral operators," J. Res. Natl. Bur. Stand. 45, 255 (1950).  
\[37\] M. Lüscher, "Some analytic results concerning the mass spectrum of Yang–Mills gauge theories on a torus," Nucl. Phys. B 219, 233 (1983).  
\[38\] P. van Baal, "The small-volume expansion of gauge theories coupled to massless fermions," Nucl. Phys. B 264, 548 (1986).  
\[39\] C. J. Morningstar and M. J. Peardon, "The glueball spectrum from an anisotropic lattice study," Phys. Rev. D 60, 034509 (1999), arXiv:hep-lat/9901004.  
\[40\] A. Athenodorou and M. Teper, "SU(N) gauge theories in 3+1 dimensions: glueball spectrum, string tensions and topology," JHEP 12, 082 (2021), arXiv:2106.00364.  
\[41\] R. E. Moore, R. B. Kearfott and M. J. Cloud, Introduction to Interval Analysis (SIAM, Philadelphia, 2009), ch. 8\.  
\[42\] A. Jaffe and E. Witten, "Quantum Yang–Mills Theory," Clay Mathematics Institute Millennium Prize Problem description (2000).  
\[43\] Particle Data Group, R. L. Workman et al., "Review of Particle Physics," PTEP 2022, 083C01 (2022), and 2024 update.  
\[44\] D. N. Arnold, R. S. Falk and R. Winther, "Finite element exterior calculus: from Hodge theory to numerical stability," Bull. Amer. Math. Soc. 47, 281 (2010).  
\[45\] D. N. Arnold, "Spaces of finite element differential forms," in Analysis and Numerics of Partial Differential Equations, Springer INdAM Ser. 4, 117 (2013).  
\[46\] P. Leopardi and A. Stern, "The abstract Hodge–Dirac operator and its stable discretization," SIAM J. Numer. Anal. 54, 3258 (2016).  
\[47\] F. R. K. Chung, Spectral Graph Theory (American Mathematical Society, Providence, 1997), ch. 1\.  
\[48\] T. Kato, Perturbation Theory for Linear Operators, 2nd ed. (Springer, Berlin, 1995), ch. V, §4 — similarity symmetrisation of operators self-adjoint in a weighted inner product.

# **Version History**

v1.6 (July 2026): Referee round 6\. The v1.5 claim that the counting star is disfavoured was WITHDRAWN: it used the regular flat polygon areas, reinstating the metric v1.4 had retracted. Correctly read, S20.S2 replaces the weight question by an area-measure question. Applied the ZS-F39 equivariant-lift dichotomy to the K\_TI face and edge registers to obtain rho \= sigma \= 1, conditional on gate F-S20.15.  
v2.2 (July 2026): CONSISTENCY RELEASE. Four defects found in review and fixed. (1) The paper-level proof was incomplete: section 22.4 asserted that three linear eigenvalues exist for every positive parameter triple and supported it only by sampling generic points, which does not prove a universally quantified statement. The exact argument, previously only in the companion, is promoted to the body as LEMMA S20.A1 (new section 22.3a): A66 and C^T C COMMUTE, so the face operator decomposes into joint sectors (s^2, a) with multiplicities (0,0,4), (0,2,4), (5-2r5,r5,3), (3,-1,5), (5+2r5,-r5,3), (15,-3,1); the kernel sector gives the two multiplicity-four linear levels exactly, and the (15,-3) block has determinant identically zero, so 5y+3x is the unique nonzero multiplicity-one level for EVERY positive (x,y,z). The branch analysis of section 22.4 is therefore exhaustive rather than illustrative. (2) Check T184 passed a literal True while the front matter claimed no executable check does so; it is now a real computation of ker(C^T C) and of A66 restricted to it, returning dimension 8 with eigenvalues 0 and 2, each of multiplicity 4\. An automated scan confirms NO executable check in the suite is a literal True. (3) The runtime claim under 15 seconds is REMOVED from the Verification Summary: it was measured on one environment and does not reproduce elsewhere (25.2 s on the review environment). (4) Two residual wordings corrected: section 22.2 no longer says the Vieta identity removes the 22 \= 2Q coincidence, matching section 22.5a which records the numerical equality as an OBSERVATION with no connecting theorem claimed; and section 22.3 no longer calls the target factorisation an I\_h isotypic pattern, since the multiplicity-five linear level is an accidental 4+1 collision, not a five-dimensional irrep. Companion PART 32 preamble and T190 rewritten: PART 32 is the LEMMA that PART 31 uses, not a repetition of a retracted scan. Verification 212 PASS \= 183 executable \+ 27 declarative \+ 2 proxy, 0 FAIL, 22 OPEN. Verdict unchanged: LAYER 1 PROVEN, LAYER 2 NOT PROVEN, bridge DERIVED-CONDITIONAL. (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.  
v2.1 (July 2026): PROOF AND STATUS RELEASE. v2.0's label PROVEN by exhaustive exact rational search is RETRACTED: the companion tested 9^3 \= 729 grid points, which establishes nothing about Q+^3, let alone R+^3. REPLACED by a short ANALYTIC proof over all positive reals. With X \= rho, Y \= 1/sigma and r explicit, three linear eigenvalues r(3Y+3), r(3Y+5), rY(5X+3) exist for every positive argument with multiplicities 4, 4, 1; a multiplicity-5 linear level can only be 4+1, giving exactly two branches rho/sigma \= 1 and rho/sigma \= 3/5; the sum rule gives r \= 3/(XY+Y+1); branch A has quintuplet 9 \- 3/(Y+2) in (7.5, 9\) whose only integer is 8, forcing rho \= sigma \= r \= 1; branch B has remaining quadruplet 9 \+ 3/(5Y+8) in (9, 9.375), integer-free, so it is EMPTY (T172-T177). The 729 large characteristic-polynomial factorisations are removed with the search. THEOREM DOMAIN RESTRICTED: the proof ranges over the positive DIAGONAL I\_h-invariant family only; non-diagonal I\_h-equivariant mass matrices, the Whitney/FEEC branch and off-diagonal Gram structures remain OPEN under F-S20.5 (T178). CONDITION RENAMED: (H-ALG) is integral counting-spectrum degeneracy, not an I\_h isotypic pattern \-- the multiplicity-5 linear level is an ACCIDENTAL 4+1 collision, not a five-dimensional irrep, which is exactly why two branches exist. EPISTEMIC STATUS SEPARATED INTO TWO LAYERS (T181): the arithmetic theorem is PROVEN; the physical selection ZS-S14 \=\> (H-ALG) and (H-TR) is NOT proven; both hypotheses are HYPOTHESIS-strong; diagonal Hodge selection is DERIVED-CONDITIONAL; the full non-diagonal measure is OPEN; MeV normalisation is OPEN. (H-TR) may be no more than the convention a\_TI \= 1 since r \= 1/a^2, so the dimensionless lambda\_1 closes conditionally but Lambda\_QCD \= 264.1 MeV does NOT \-- v2.0 asserted otherwise and that is withdrawn. The 22 \= 2Q claim is SPLIT (T191): sum of roots \= 22 is Vieta, PROVEN; that it equals 2Q is OBSERVATION awaiting a connecting theorem. Front matter, Abstract and Conclusion rewritten so that no two parts of the document assert different verdicts. Verification 212 PASS \= 183 executable \+ 27 declarative \+ 2 proxy, 0 FAIL, 22 OPEN (F-S20.5 newly registered for the non-diagonal family), all check identifiers unique. (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.  
v2.0 (July 2026): CLOSURE RELEASE. The Yang-Mills bridge CLOSES, by OVER-DETERMINATION rather than by a new axiom. NEW Corollary S20.Q: the characteristic polynomial of B2B2^T factors over Z as lam (lam-6)^4 (lam-8)^5 (lam^2-10lam+22)^5 (lam^4-22lam^3+166lam^2-480lam+380)^3, the quartic is irreducible over Q, and BOTH ledger eigenvalues are its roots, so lambda\_1 and lambda\_h are algebraic integers of degree 4 with an exact minimal polynomial the corpus did not previously have; the recurring 22 \= 2Q is the lam^3 coefficient, i.e. Vieta, removing a coincidence that would otherwise face the section 12 anti-numerology gate (T169-T171). NEW Theorem S20.A: two conditions are imposed, (H-ALG) that the char poly of N \= B2 M1^-1 B2^T M2 is integral and factors over Z with the I\_h isotypic pattern, and (H-TR) the incidence sum rule Tr(Delta\_2) \= 2E \= 180\. Neither mentions a metric, a measure or a register; neither has {M uniform} as its solution set \-- (H-ALG) does not even force rho \= sigma, admitting (rho,sigma,r) \= (1/5,1/3,5) \-- and (H-TR) alone leaves a surface (T172, T174). Their intersection, by exhaustive exact rational search with r carried as an EXPLICIT third parameter so that the v1.7 objection cannot apply, is the single point rho \= sigma \= r \= 1 (T173). Hence M1 \= M2 \= m I and lambda\_1 \= 1.2428416164 at multiplicity three (T175). NO LEDGER NUMBER MOVES. Non-circularity tested before submission against all three of the paper own criteria (T177). NEW NEGATIVE, reported because it was tried: restoring the continuum degeneracies of the l \= 3 and l \= 4 multiplets, which I\_h does not protect, fails \-- splittings 21.3 percent and 11.5 percent at the counting star with mutually inconsistent minima; route CLOSED-NEGATIVE (T176). Verification 203 PASS \= 177 executable \+ 24 declarative \+ 2 proxy, 0 FAIL, 21 OPEN. (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.  
v1.9 (July 2026): CORRECTION AND RECONSTRUCTION RELEASE. v1.8 headline WITHDRAWN. INDEX ERROR: the face basis is \[dF5, dF6, FAD0, FAD1\] and v1.8 read coordinates 2 and 3 \-- the OFF-DIAGONAL conductances \-- as beta\_5 and beta\_6, while M2 := diag(beta\_f) puts them at 0 and 1\. What v1.8 verified is uniform CONDUCTANCE; the diagonal ratio is 5:6, reported in the very next check. Sixth instance of one failure mode; a basis-label guard now asserts the name of the basis element at every coordinate read. Proposition S20.C REPROVEN in EXACT RATIONAL arithmetic (2912 x 12 integer matrix, exact rank 10, exact nullity 2, replacing float SVD): the general solution is L\_E \= c\_G B1^T B1 \+ c\_F B2^T B2, L\_F \= c\_F B2 B2^T. Three corrections follow: the second free direction is the GRADIENT sector rate c\_G, invisible to the face flux since B2 B1^T \= 0, and NOT r; one basis member has L\_F \= 0, so it is a solution SPACE not a cone, with no positivity or irreducibility imposed; and the result is close to the standard chain-complex identity, with the incidence amplitudes already present in the basis. NEW Theorem S20.M, the action reconstruction map v1.8 lacked: under (H-EOM), that N \= B2 M1^-1 B2^T M2 is proportional to B2 B2^T, the five distinct equations have the UNIQUE solution beta\_5 \= beta\_6, m56 \= m66, with constant r \= beta/m. DISCLOSED AGAINST INTEREST: the solution set of (H-EOM) is exactly the uniform measure, so by the Theorem S20.E test it is an axiom RESTATEMENT, not a derivation. Gain: one condition on the physical evolution operator replaces four, with an exact reconstruction theorem in place of an unproven type shift. Abstract and Conclusion rewritten to the v1.9 state; stale companion header and RESULTS status fixed. Verification 184 PASS \= 161 executable \+ 21 declarative \+ 2 proxy, 0 FAIL, 21 OPEN. The Yang-Mills bridge is NOT closed. No ledger number moves; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.  
v1.8 (July 2026): SHAPE CLOSURE RELEASE. NEW Theorem S20.C (Clock Synchronisation): build a face generator L\_F and an edge operator L\_E that are NOT functions of M, require them to describe the same flux dynamics via B2 L\_E \= L\_F B2 with L\_F 1 \= 0, and compute the solution cone exactly. Twelve I\_h-equivariant parameters (2+6 edge, 2+2 face) give a cone of dimension 2, and EVERY element of it has rho \= 1 and sigma \= 1 to twelve digits, with L\_F EXACTLY proportional to B2 B2^T (residual 1.8e-16) and the rate-normalised gap lambda\_1 \= 1.2428416164 at multiplicity three (T158-T163). The generator condition independently forces the diagonal ratio dF5/dF6 \= 5/6, as a graph Laplacian must (T164). CONSEQUENCE: the shape branch no longer rests on F-S20.15a-c. The register-lift identification and, critically, the state-to-measure functor \-- the type shift from a stationary density to a geometric valuation, which was the weakest link of v1.6 \-- are REMOVED FROM THE CRITICAL PATH. The condition is metric-independent and is not the failed intertwiner of section 14.4, where M defined the adjoint and every M passed. BOUNDING NO-GO: demanding L\_E 1 \= 0 as well collapses the cone to zero, because the oriented 1-cochain space is not a probability register (T165). WHAT REMAINS: the cone is 2-dimensional, one direction being the overall clock rate and the other exactly r \= beta/m, so F-S20.15d stays OPEN and M1 \= M2 is still not established. No least-squares comparison of L\_F and L\_E scales is used to claim r, since L\_E is not proportional to B2^T B2. Verification 182 PASS \= 161 executable \+ 19 declarative \+ 2 proxy, 0 FAIL, 21 OPEN. No ledger number moves; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.  
v1.7 (July 2026): Referee round 7\. The v1.6 headline THE BRIDGE CLOSES WITHDRAWN. Decisive error fixed: (D-F) and (D-E) give M2 \= beta I and M1 \= m I but NOT M1 \= M2, since Delta\_2 \= r B2 B2^T with r \= beta/m, so lambda\_1 \= r x 1.2428416164. v1.6 check T153 silently set beta \= m \= 1 and is retracted as a closure verification. Kogut-Susskind gives r \= 1/a^2, so the missing condition IS gate F-S19.3. F-S20.15 split into four sub-gates; four weak checks (T148, T149, T150, T152) replaced by real computations.  
v1.5 (July 2026): Referee round 5\. NEW Theorem S20.T1: the transfer free-energy Hessian returns its input metric exactly, which together with S20.O and S20.N-a exposes one mechanism behind five failed routes. Heat-kernel semigroup VERIFIED numerically rather than cited, to 4.3e-14 for U(1) and 2.8e-17 for the non-abelian SU(2). A third check kind, PROXY, introduced after four rounds in which a proxy was reported as verification of the target. The v1.5 meta-theorem was weakened by its own adversarial cross-check.  
v1.4 (July 2026): Referee round 4\. Gate F-S20.11 RETRACTED IN FULL on a scale error: under g \-\> s^2 g the one-form star is invariant but the two-form star carries s^-2, so lambda\_1 \-\> s^-2 lambda\_1, and rescaling the flat star by s \= 0.5382277383 \= a\_TI reproduces the counting star exactly. S20.N-b demoted to two non-proportional geometric DEC stars, COMPUTED. NEW: the primitive plaquette-clock reformulation, the series law 1/beta\_eff \= sum 1/beta\_i and the Cauchy result beta(A) \= 1/(cA), both PROVEN.  
v1.3 (July 2026): Referee round 3\. Theorem S20.N split into S20.N-a (abstract, PROVEN) and S20.N-b. Attempted closure by tabulating three corpus-internal metric candidates and excluding two against the quenched lattice band. \[RETRACTED in v1.4.\] Numerical errata: Lambda\_QCD at rho \= 5/6 is 270.02 MeV, not 261.2; the rho sensitivity is 0.0855 percent, not 0.04.  
v1.2 (July 2026): Referee round 2\. Outcome A renamed to the numerical branch A\_weights, since the epistemic Outcome A was not realised. Found that rho is a pentagon-hexagon ORBIT anisotropy and that the contrast operator O\_minus is itself I\_h-invariant, so rho \= 1 is NOT symmetry-protected. Gates F-S18.16 and F-S19.6 split into a/b.  
v1.1 (July 2026): Referee round 1\. Added the incidence Hodge-Dirac operator D\_K on the 182-dimensional space; Theorem S20.R (the commutant is exactly the scalars, certified by integer union-find and GF(2^31-1) rank) and Theorem S20.O, the NO-GO that fires gate F-S20.8: D\_M \= d \+ M^-1 d^T M is M-self-adjoint for EVERY positive M, so Hermiticity selects nothing. (H-SYM) shown load-bearing by an explicit positive non-uniform solution with linearised kernel dimension 11\.

v1.0 (March 2026, internal): Initial release. Executes gate F-S19.6 of ZS-S19 v1.6 FINAL. Supplies R\_TI explicitly and records that ZS-S14 does not define it. Lemma S20.T; Theorems S20.D and S20.U; Corollary S20.A. Route W excluded as ill-posed under (R); the degree-biased face weight rho\_F \= 5/6 CLOSED-NEGATIVE. Candidate axioms (L) and the arithmetic-versus-harmonic form of (H-PD) refuted in adversarial review and retracted with falsifiers stated in full. Erratum filed against ZS-S19 section 1.1 for A6/A5. Anti-numerology Monte Carlo executed and reported negative (p \= 33.82 %). Verification 83/83 PASS, 0 FAIL, 9 OPEN. Superseded in full by v1.1 and v1.2.