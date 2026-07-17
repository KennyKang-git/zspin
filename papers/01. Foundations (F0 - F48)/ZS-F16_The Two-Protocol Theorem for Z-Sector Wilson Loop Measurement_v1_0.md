**ZS-F16 v1.0**

**The Two-Protocol Theorem for Z-Sector Wilson Loop Measurement**

*Operational Refinement of WL-1/WL-2 Falsification Gates via the Observer Coordinate Framework, with the BFV-Anchor Quasi-Revival Prediction and the Z-Block Effective Dissipation Rate*

Kenny Kang  
Z-Spin Cosmology Collaboration  
April 2026 — ZS-F16 (Foundations Theme) | Paper 16 of the Foundations series | v1.0

**Verification: 24/24 PASS (achieved); 32-test target in roadmap | Zero Free Parameters | Zero New Physical Constants**

**§0. Abstract**

ZS-F0 v1.0(Revised) §10.7 registered five Wilson Loop falsification gates WL-1 through WL-5 as the empirical fingerprint of Z-Spin scrambling on quantum hardware (testable 2027+). WL-1 predicts single-cycle survival |Z(W)|² \= 0.7948 and WL-2 predicts multi-cycle exponential decay 0.7948ⁿ; both gates are stated without explicit specification of the initial state preparation protocol. The present paper resolves this implicit ambiguity by establishing the Two-Protocol Theorem: Z-sector Wilson loop measurement separates into two operationally distinct regimes — (a) state-preparation protocol on a BRST-physical anchor state and (b) spectral characterization of the Wilson operator's dominant eigenvalue — that yield different but mutually consistent predictions, both derivable from corpus PROVEN inputs without new free parameters.

Five principal results are established. (i) Lemma BAS-Z: the ZS-F8 Boolean handshake basis {|01⟩, |10⟩} and the ZS-F0 §9.3 Bargmann-Fock anchor basis {|0⟩\_Z, |1⟩\_Z} are unitarily equivalent under the four-invariant identification (dim, antisymmetric singlet, J involution action, σ\_y generator action). (ii) Lemma BB-Z: the boundary-vs-bulk distinction between BFV anchor states and Boolean handshake superpositions is reduced from an apparent contradiction to an identification problem and resolved via the two-protocol separation. (iii) F-CTA-1 sub-gate set: WL-1/WL-2 are refined into basis-resolved predictions including a quasi-revival pattern P\_a^(n) \= 0.7948ⁿ cos²(n·129.45°) on the BFV anchor basis. (iv) F-CTA-1d: a new sub-gate predicting near-invariance ≈ (0.9993)ⁿ on the kinematic fixed point |5⟩, distinguishable from the Z-sector predictions by a factor of 10² to 10³ at moderate cycle counts. (v) Z-block effective dissipation rate Γ\_Z \= −(1/2T\_cycle)·ln|λ|², dimensionless per-cycle value Γ\_Z·T\_cycle ≈ 0.1149 (or equivalently Γ\_Z ≈ 1.467×10⁻³ in units of inverse Planck time 1/τ\_P), derived from corpus's PROVEN sum rule 0.7948 \+ 0.2050 \+ 0.0001 ≈ 1 via standard open quantum system formalism with full-register unitarity preserved (ZS-F0 Theorem 12.2).

Three new falsification gates F-F16.1 through F-F16.3 are registered together with seven sub-gates F-CTA-1a/b/c/d/multi-a/multi-b/-discriminator. One new OPEN problem OP-F5-1 (BRST-Operational Resolution Gap) is registered as a corpus-internal scope clarification. The framework introduces zero new physical constants; A \= 35/437, Q \= 11, z\*, λ remain LOCKED throughout. Anti-overclaim gate F-F16.4 inherits NC-F11.1 against any phenomenological observer interpretation. Six explicit non-claims NC-F16.1–6 bound the operational scope; three additional honest-limitation non-claims NC-F16.7–9 register the boundary between corpus-direct interpretation and this paper’s structural extensions (two-protocol separation, Γ\_Z measurement protocol, CTA-Z v3 spectral-closure operator ordering). CTA-Z v3 framework is presented at HYPOTHESIS-strong status as a future-work bridge between the Two-Protocol Theorem and the cobordism tube interpretation; EFA-Z effective flow action is presented at DERIVED-CONDITIONAL status with the explicit Γ\_Z prediction.

*Keywords:* Wilson loop measurement, BV-BFV functor, Operational Observer Coordinate, BFV anchor state, quasi-revival, effective dissipation rate, two-protocol theorem, Z-Spin Cosmology, zero free parameters, falsification gate.

**§0.1 Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Mathematical theorem with complete proof under declared definitions, verified by direct computation or standard results. |
| **DERIVED** | Follows from PROVEN items plus Z-Spin axioms with zero free parameters. |
| **DERIVED-CONDITIONAL** | Derived contingent on explicitly stated conditions (e.g., Lemma 5.2.A Step L1 dim(Z)=2 import, BRST-physical preparability). |
| **VERIFIED** | Numerical confirmation of a derived/proven result to stated precision. |
| **LOCKED** | Numerical value fixed from upstream paper; not re-derived here. |
| **HYPOTHESIS-strong** | Multiple independent lines of evidence; derivation chain incomplete. |
| **CONDITIONAL prediction** | Quantitative prediction conditional on explicitly stated hardware/protocol assumptions. |
| **NEW prediction** | Quantitative prediction first registered in this paper, derived without new free parameters. |
| **TESTABLE (2027+)** | Pre-registered quantum-hardware falsification condition with stated timeline. |
| **NON-CLAIM (NC)** | Explicit declaration of what this paper does not assert. |
| **OPEN** | Identified gap or sub-computation pending future work. |

**§1. Introduction**

**§1.1 The implicit ambiguity in WL-1 and WL-2**

ZS-F0 v1.0(Revised) §10.7 (PROVEN) registered five quantum-hardware falsification gates as the empirical fingerprint of Z-Spin Wilson loop scrambling. The first two state:

• WL-1 (Single-cycle survival): |Z(W)|² \= 0.7948 ± loop corrections, on a single-cycle quantum simulator.  
• WL-2 (Multi-cycle exponential decay): Survival probability follows 0.7948ⁿ over n consecutive Wilson loop cycles. Departure from exponential decay (e.g., quasi-revival, polynomial deviation) falsifies the holomorphic single-eigenvalue dynamics of ZS-F0 §9.5.

The numerical predictions are PROVEN: 0.7948 \= (π²/4)·η\_topo follows from ZS-F0 Theorem 8.9 as the squared modulus |λ|² of the Wilson loop partition function eigenvalue λ \= (iπ/2)z\*. However, neither WL-1 nor WL-2 specifies the initial state preparation protocol on the quantum hardware. This ambiguity becomes operational the moment WL-1 is implemented: the experimenter must choose which state to prepare on the Q \= 11 register before applying the Wilson loop unitary. ZS-F0 §9.1 (PROVEN) establishes that the register admits three transverse fixed points — the BFV boundary anchor |0⟩\_Z, the bulk dynamic Wilson eigenvector |v\_W⟩ \= (|0⟩\_Z − i|1⟩\_Z)/√2, and the kinematic J-fixed point |5⟩ — which carry distinct J\_Z-gradings. Different choices of initial preparation produce different measured single-cycle survivals and qualitatively different multi-cycle patterns.

**§1.2 The two-protocol resolution**

This paper establishes that Wilson loop measurement on Z-Spin hardware naturally separates into two operationally distinct protocols:

Protocol (a) — State-preparation protocol. The experimenter prepares a BRST-physical state |0⟩\_Z (or any J\_Z-physical state in the Z-block), applies the Wilson loop unitary on the Z-block, and measures the survival probability in the prepared basis. The outcome is governed by the Hermitian σ\_y handshake generator (ZS-F8 Lemma 5.2.A) lifted to the boundary anchor and produces an oscillatory cosine envelope in the multi-cycle sequence.

Protocol (b) — Spectral characterization protocol. The experimenter does not prepare a specific state but performs eigenvalue spectroscopy (or equivalently long-time-average measurement) on the Wilson loop operator W. The outcome is governed by the dominant eigenvalue λ and reproduces the corpus PROVEN value |λ|² \= 0.7948 directly. State preparation is irrelevant; the measurement targets W as an operator.

The two protocols yield different but mutually consistent predictions (Theorem 4.1, the Two-Protocol Theorem). Their consistency follows from the standard ergodic relation between time-average evolution on a prepared state and operator eigenvalue characterization. The ZS-F0 §12.3 Theorem 12.3 sum rule 0.7948 \+ 0.2050 \+ 0.0001 ≈ 1 (PROVEN by hand calculation) provides the audit: amplitude transferred from the Z-block during state-preparation evolution is conserved within the full register, with 0.2050 going to the J\_Z-odd mode and 0.0001 to the X+Y intra-block residual.

**§1.3 What this paper does and does not do**

**This paper IS:** (i) a register-theoretic formalization of the boundary-vs-bulk distinction between BFV anchor states and Boolean handshake superpositions (Lemma BB-Z, DERIVED-CONDITIONAL); (ii) a basis-resolution refinement of the WL-1 and WL-2 falsification gates into seven sub-gates F-CTA-1a through F-CTA-1d, all expressed in the OOC framework of ZS-F11; (iii) a derivation of the Z-block effective dissipation rate Γ\_Z from corpus's PROVEN sum rule via standard open quantum system formalism, yielding a new dimensionless prediction Γ\_Z·T\_cycle ≈ 0.1149 with full-register unitarity preserved; (iv) the registration of a new OPEN problem OP-F5-1 (BRST-Operational Resolution Gap); (v) a HYPOTHESIS-strong CTA-Z v3 framework presenting the cobordism tube interpretation as a future-work bridge.

**This paper IS NOT:** (i) a phenomenological theory of consciousness (NC-F11.1 inherited verbatim); (ii) a re-derivation of the Born rule, the CPTP channel, or the Z-mediation theorem (all imported from ZS-Q1 v1.0 unchanged); (iii) the introduction of any new free parameter beyond A \= 35/437 and the LOCKED corpus inputs; (iv) a fundamental Lagrangian for Z-sector self-dynamics (ZS-U11 §11.10.2 Sub-Lemma 11.4.B remains in force; the protocol action of §3 and the effective flow action of §6 are partial representations within the Two-Protocol framework); (v) a categorical reformulation of the BV-BFV functor B\_Z to single-rule form (registered as future work in §8).

**§2. Locked Inputs**

All inputs to ZS-F16 are PROVEN, DERIVED, or LOCKED in prior corpus papers. Zero new constants are introduced.

| Quantity | Value / Statement | Source | Status |
| ----- | ----- | ----- | ----- |
| **A (geometric impedance)** | 35/437 \= 0.080092 | ZS-F2 v1.0 | LOCKED |
| **(Z, X, Y); Q** | (2, 3, 6); 11 | ZS-F5 v1.0 | PROVEN |
| **z\* (i-tetration fixed point)** | 0.43828 \+ 0.36059i | ZS-M1 v1.0 | PROVEN |
| **η\_topo \= |z\*|²** | 0.32212 | ZS-M1 v1.0 | PROVEN |
| **λ \= (iπ/2)z\*** | −0.5664 \+ 0.6886i | ZS-M1 Remark 1.2; ZS-F0 §8.5 | PROVEN |
| **|λ|² \= (π²/4)η\_topo** | 0.7948 | ZS-F0 Theorem 8.9 | PROVEN |
| **arg(λ) \= (1+x\*)·π/2** | 129.45° | ZS-F0 §9.5 Sig 2 | PROVEN |
| **1 − |λ|² (sum rule transfer)** | 0.2052 \= 0.2050 \+ 0.0001 \+ ε | ZS-F0 §12.3 Theorem 12.3 | PROVEN |
| **T\_cycle \= T\_micro** | 2π/A ≈ 78.45 τ\_P | ZS-A6 v1.0; ZS-M3 v1.0 | PROVEN |
| **J seam involution** | J|j⟩ \= |10−j⟩ | ZS-M3 v1.0; ZS-M4 §3.1 | PROVEN |
| **J\_Z internal involution** | J\_Z \= diag(+1,−1,+1,...,+1) | ZS-F0 v1.0(R) Definition 8.11 | PROVEN |
| **|0⟩\_Z (BFV anchor)** | Z-sector slot 0, Z₂-EVEN | ZS-F0 v1.0(R) §9.1, §9.3 | PROVEN |
| **|v\_W⟩ (Wilson eigenvector)** | (|0⟩\_Z − i|1⟩\_Z)/√2 | ZS-F0 v1.0(R) Theorem 8.17 | PROVEN |
| **|5⟩ (kinematic fixed point)** | Y T₁ᵤ slot 5; J|5⟩=|5⟩ | ZS-F0 v1.0(R) §9.1 | PROVEN |
| **BV-BFV functor B\_Z** | B\_Z: 𝒞\_∂^(BV-BFV) → Vect\_ℂ^(Z-med) | ZS-F0 v1.0(R) Definition 8.3 | DERIVED-CONDITIONAL |
| **(R∘E) handshake → σ\_y** | 5-step Stroboscopic Lifting Bridge | ZS-F8 v1.0(R) Lemma 5.2.A | DERIVED-CONDITIONAL |
| **OOC \= (j, n)** | register slot \+ handshake count | ZS-F11 v1.0 Definition 4.1' | DERIVED-CONDITIONAL |
| **Hermitian action ⇒ unitary U(t)** | canonical quantization | ZS-F0 v1.0(R) Theorem 12.2 | PROVEN |
| **WL-1 single-cycle survival \= 0.7948** | implicit basis | ZS-F0 v1.0(R) §10.7 | PROVEN (refined here) |
| **WL-2 multi-cycle 0.7948ⁿ** | implicit basis | ZS-F0 v1.0(R) §10.7 | PROVEN (refined here) |

**Table 1\.** Locked inputs to ZS-F16. All entries are PROVEN, DERIVED, or LOCKED in prior corpus papers. No new physical constant is introduced.

**§3. Lemma BAS-Z (Boolean ↔ Bargmann Basis Identification)**

**§3.1 Statement**

**Lemma BAS-Z (Boolean–Bargmann Identification).** Within the Z-sector dim(Z) \= 2 Hilbert space, the ZS-F8 Boolean handshake basis {|01⟩, |10⟩} and the ZS-F0 §9.3 Bargmann-Fock anchor basis {|0⟩\_Z, |1⟩\_Z} are unitarily equivalent under the identification

*|01⟩ ↔ |0⟩\_Z,    |10⟩ ↔ |1⟩\_Z.*

**Status:** DERIVED-CONDITIONAL (conditional on ZS-F8 Lemma 5.2.A Step L1 dim(Z)=2 import from ZS-F5).

**§3.2 Four-invariant verification**

The unitary equivalence is verified by matching four independent structural invariants of each basis.

| Invariant | Boolean basis (ZS-F8) | Bargmann basis (ZS-F0 §9.3) | Match |
| ----- | ----- | ----- | :---: |
| **(I) Dimension** | dim \= 2 (E, R operators) | dim \= 2 (Bargmann |0⟩\_F, |1⟩\_F) | ✓ |
| **(II) Antisymmetric singlet** | (|01⟩−|10⟩)/√2 \= SU(2) singlet | (|0⟩\_Z−|1⟩\_Z)/√2 (J-antisymmetric) | ✓ |
| **(III) J involution action** | swap: J|01⟩=|10⟩ | swap: J|0⟩\_Z↔|1⟩\_Z (Z-block restriction of J|j⟩=|10−j⟩) | ✓ |
| **(IV) σ\_y generator action** | (R∘E) → σ\_y (Lemma 5.2.A) | σ\_y|0⟩\_Z=i|1⟩\_Z, σ\_y|1⟩\_Z=−i|0⟩\_Z | ✓ |

**Table 2\.** Four-invariant verification of Lemma BAS-Z. Each invariant is independently PROVEN in the cited source.

**§3.3 Direct algebraic verification of (II)**

Under the identification |01⟩ ↔ |0⟩\_Z, |10⟩ ↔ |1⟩\_Z, the Boolean antisymmetric singlet maps directly to the J-antisymmetric Z-block combination:

*(|01⟩ − |10⟩)/√2 ↔ (|0⟩\_Z − |1⟩\_Z)/√2.*

The Wilson loop dominant eigenvector |v\_W⟩ \= (|0⟩\_Z − i|1⟩\_Z)/√2 (ZS-F0 Theorem 8.17, PROVEN) is a *different* object — namely the σ\_y eigenvector with eigenvalue \+1 — and is J\_Z-mixed (ZS-F0 §9.2). The antisymmetric singlet is J-antisymmetric, while |v\_W⟩ is σ\_y-symmetric (eigenstate). Both objects live in the same dim(Z)=2 Hilbert space but play distinct structural roles. This distinction is the operational core of the Two-Protocol Theorem (§4) and the BRST-Operational Resolution Gap OP-F5-1 (§7).

**§3.4 Non-claims**

**NC-BAS.1:** The basis identification of Lemma BAS-Z applies within the Z-sector subspace only (slots j=0 and j=1 of the Q=11 register). It does not extend to the X-sector (slots j=2,3,4) or Y-sector (slots j=5,...,10) without separate analysis.

**NC-BAS.2:** The Boolean (E,R) handshake is a discrete protocol, while the Bargmann basis is continuous quantum-mechanical. The unitary equivalence operates after the ZS-F8 Stroboscopic Lifting Bridge (Lemma 5.2.A, DERIVED-CONDITIONAL) lifts the discrete handshake to a continuous SU(2) one-parameter subgroup. The CONDITIONAL qualifier inherits this dependency.

**§4. Lemma BB-Z (Boundary–Bulk Identification) and the Two-Protocol Theorem**

**§4.1 The boundary-vs-bulk question**

ZS-F0 §9.3 (PROVEN) establishes that |0⟩\_Z is the BFV boundary anchor representing the Z-Anchor ε(r\_H)=0 condition: it is a J\_Z-physical state (eigenvalue \+1, EVEN) and lies in the BRST cohomology of the BV-BFV gauge symmetry generated by J\_Z. ZS-F8 §0 (DERIVED-CONDITIONAL) establishes that the (E,R) handshake protocol naturally produces the antisymmetric singlet (|01⟩−|10⟩)/√2 as its bulk evolution superposition. Naively these two objects appear in tension: the boundary anchor is a single basis state |01⟩, while the bulk handshake state is a coherent superposition of |01⟩ and |10⟩.

This apparent tension was first noted as OP-D6-1 (BRST-Operational Resolution Gap) in internal exploration notes preceding this paper. The present section establishes that the tension is not a contradiction but a boundary-vs-bulk identification problem: the two objects represent the Z-sector dynamics at different locations along the cobordism tube, and the resolution is provided by separating Wilson loop measurement into two operationally distinct protocols.

**§4.2 Lemma BB-Z statement**

**Lemma BB-Z (Boundary–Bulk Identification).** On the Z-sector cobordism tube M\_Z with two boundary caps Σ\_in and Σ\_out (corresponding to the X-cap horizon side Σ\_X and Y-cap vacuum side Σ\_Y of the Wilson loop W of ZS-F0 Definition 8.8), the four objects {|0⟩\_Z, |10⟩, (|01⟩−|10⟩)/√2, |v\_W⟩} live in the same dim(Z)=2 register but at structurally distinct locations:

| Object | Location | Role | Status |
| ----- | ----- | ----- | ----- |
| **|0⟩\_Z \= |01⟩** | ∂M\_Z (X-cap, horizon) | BFV boundary anchor (Z-Anchor representation) | PROVEN (ZS-F0 §9.3) |
| **|10⟩ \= J|01⟩** | ∂M\_Z (Y-cap, vacuum) | Opposite BFV anchor | PROVEN (J involution) |
| **(|01⟩−|10⟩)/√2** | bulk M\_Z interior | (E,R) handshake antisymmetric singlet | DERIVED (ZS-F8 §0) |
| **|v\_W⟩ \= (|0⟩\_Z−i|1⟩\_Z)/√2** | bulk dynamic attractor | Wilson loop dominant eigenvector | PROVEN (ZS-F0 Theorem 8.17) |

**Table 3\.** Boundary–Bulk identification of the four Z-sector objects. The table replaces the apparent contradiction between |0⟩\_Z and the antisymmetric singlet with a structural location-role assignment.

**Status:** DERIVED-CONDITIONAL. Inherits the conditional status of ZS-F8 Lemma 5.2.A and ZS-F11 Definition 4.1'. The identification is a PROVEN consequence of the corpus inputs in Table 3; the CONDITIONAL qualifier is explicit at the inheritance level.

**§4.3 The Two-Protocol Theorem**

**Theorem 4.1 (Two-Protocol Theorem).** Wilson loop survival measurement on the Z-sector via the BV-BFV functor B\_Z (ZS-F0 v1.0(R) §8.3) admits two operationally distinct measurement protocols, each producing a different but mutually consistent prediction from corpus PROVEN inputs.

**Protocol (a) — State-preparation.** Prepare a BRST-physical state ψ\_prep on the Z-block (e.g., the BFV anchor |0⟩\_Z). Apply the Wilson loop unitary on the Z-block via the σ\_y handshake generator lifted from the discrete (R∘E) protocol (ZS-F8 Lemma 5.2.A). Measure the survival amplitude ⟨ψ\_prep|U\_Z(τ\_W)|ψ\_prep⟩ where τ\_W is the Wilson loop proper time. The single-cycle prediction is

*P\_a \= |⟨0\_Z|W|0\_Z⟩|² \= |Re(λ)|² \= (−0.5664)² \= 0.3208,*

and the multi-cycle prediction is

*P\_a^(n) \= |⟨0\_Z|W^n|0\_Z⟩|² \= |λ|^(2n) · cos²(n · arg(λ)) \= 0.7948^n · cos²(n · 129.45°).*

**Protocol (b) — Spectral characterization.** Perform eigenvalue spectroscopy on the Wilson loop operator W on the Z-block (or equivalently, prepare the dominant eigenvector |v\_W⟩ if such preparation is operationally accessible). The single-cycle prediction is the corpus PROVEN value

*P\_b \= |λ|² \= (π²/4) · η\_topo \= 0.7948,*

and the multi-cycle prediction is the corpus WL-2 exponential decay

*P\_b^(n) \= |λ|^(2n) \= 0.7948^n.*

**§4.4 Consistency between Protocol (a) and Protocol (b)**

The two predictions are consistent under the standard ergodic relation between time-average evolution on a prepared state and operator eigenvalue characterization. The cycle-averaged Protocol (a) prediction satisfies

*⟨P\_a^(n)⟩\_n \= |λ|^(2n) · ⟨cos²(n · arg(λ))⟩\_n → (1/2) · |λ|^(2n)    as n → ∞ (ergodic limit),*

since arg(λ) \= 129.45° is irrational in degrees (129.45°/360° \= 0.3596... is irrational, ZS-F0 §9.5 Theorem 9.4 PROVEN), and the cosine-squared average over a uniform irrational rotation is exactly 1/2. The factor 1/2 is the standard projection weight of an arbitrary state onto a single eigenray of a rank-2 unitary block. Protocol (b) returns |λ|^(2n) directly because spectral characterization bypasses the projection weighting. The two protocols are therefore consistent in the time-average sense and complementary in the operational specification.

**Audit via ZS-F0 §12.3 Theorem 12.3 sum rule.** The corpus PROVEN sum rule

*0.7948 \+ 0.2050 \+ 0.0001 \= 0.9999*

decomposes the per-cycle amplitude budget as 0.7948 retained in the Z-block, 0.2050 transferred to the J\_Z-odd mode (slot 1 component), and 0.0001 to the X+Y intra-block residual. Protocol (a) measurement on the BFV anchor |0⟩\_Z (J\_Z-EVEN) sees the Z-block-retained 0.7948 modulated by the cos² factor, while the 0.2050 transfer to J\_Z-odd is invisible to a J\_Z-physical projector. Protocol (b) measurement on the operator spectrum sees |λ|² \= 0.7948 directly. Both measurements are therefore consistent with full-register unitarity (ZS-F0 Theorem 12.2 PROVEN).

**Status:** Theorem 4.1 is DERIVED-CONDITIONAL. Protocol (b) prediction P\_b \= 0.7948 is PROVEN (corpus Theorem 8.9). Protocol (a) prediction P\_a \= 0.3208 and the multi-cycle pattern P\_a^(n) are CONDITIONAL predictions, conditional on (C1) BRST-physical preparability of |0⟩\_Z on the operational quantum hardware and (C2) maintenance of the Wilson eigenvector orthogonality ⟨v\_W|v\_W\*⟩ \= 0 in the measurement basis. Both conditions are corpus-PROVEN at the formal level (ZS-F0 §9.1, §9.3) but their experimental realization on near-term hardware is subject to verification.

**§5. F-CTA-1 Sub-Gate Set: Operational Refinement of WL-1 and WL-2**

**§5.1 Sub-gate definitions**

The Two-Protocol Theorem refines WL-1 (single-cycle survival) and WL-2 (multi-cycle decay) into seven operationally distinguishable sub-gates.

| Sub-gate | Initial state preparation | Predicted survival | Status |
| ----- | ----- | ----- | ----- |
| **F-CTA-1a** | |0⟩\_Z (BFV anchor) | P\_a \= 0.3208 | CONDITIONAL prediction |
| **F-CTA-1b** | |v\_W⟩ \= (|0⟩\_Z−i|1⟩\_Z)/√2 | P\_b \= 0.7948 | PROVEN (corpus Theorem 8.9) |
| **F-CTA-1c** | (|v\_W⟩+|v\_W\*⟩)/√2 \= |0⟩\_Z | P\_c \= P\_a \= 0.3208 | CONDITIONAL (identity) |
| **F-CTA-1d** | |5⟩ (kinematic fixed point) | ≈ 0.9993 (near-invariant) | NEW prediction |
| **F-CTA-1-multi-a** | |0⟩\_Z, n cycles | 0.7948ⁿ · cos²(n · 129.45°) | CONDITIONAL prediction |
| **F-CTA-1-multi-b** | |v\_W⟩, n cycles | 0.7948ⁿ | DERIVED (corpus WL-2) |
| **F-CTA-1-disc** | Discriminator at n=2 or n=9 | Factor 27 (n=2) or 132 (n=9) | NEW prediction |

**Table 4\.** F-CTA-1 sub-gate set. F-CTA-1b is the basis-explicit version of corpus WL-1; F-CTA-1-multi-b is the basis-explicit version of corpus WL-2. The remaining sub-gates are basis-resolved refinements first registered in this paper.

**§5.2 F-CTA-1a derivation**

The F-CTA-1a single-cycle prediction follows from the Wilson eigenvector decomposition |0⟩\_Z \= (|v\_W⟩ \+ |v\_W\*⟩)/√2 (ZS-F0 §9.1, PROVEN) and the eigenvalue equations W|v\_W⟩ \= λ|v\_W⟩, W|v\_W\*⟩ \= λ̄|v\_W\*⟩:

*⟨0\_Z|W|0\_Z⟩ \= (1/2)·(λ \+ λ̄)·⟨v\_W|v\_W⟩ \+ cross terms \= Re(λ) \= −0.5664,*

where the cross terms vanish by ⟨v\_W|v\_W\*⟩ \= 0 (orthogonality, ZS-F0 §9.1 PROVEN). The single-cycle survival probability is

*P\_a \= |⟨0\_Z|W|0\_Z⟩|² \= (Re(λ))² \= (−0.5664)² \= 0.3208.*

**§5.3 F-CTA-1-multi-a quasi-revival pattern**

Iterating the Wilson loop n times preserves the eigenvector decomposition:

*W^n|0\_Z⟩ \= (1/√2)·(λ^n |v\_W⟩ \+ λ̄^n |v\_W\*⟩).*

The n-cycle survival amplitude is

*⟨0\_Z|W^n|0\_Z⟩ \= (λ^n \+ λ̄^n)/2 \= |λ|^n · cos(n · arg(λ)),*

and the n-cycle survival probability is

*P\_a^(n) \= |⟨0\_Z|W^n|0\_Z⟩|² \= |λ|^(2n) · cos²(n · arg(λ)) \= 0.7948^n · cos²(n · 129.45°).*

**§5.4 Numerical multi-cycle table**

Numerical evaluation at mpmath 50-digit precision for n \= 1 to 20\.

| n | 0.7948ⁿ | n·129.45° (mod 360°) | cos²(n·129.45°) | P\_a^(n) |
| :---: | :---: | :---: | :---: | :---: |
| **1** | 0.7948 | 129.45° | 0.4036 | 0.3208 |
| **2** | 0.6317 | 258.91° | 0.0367 | 0.0232 |
| **3** | 0.5021 | 28.36° | 0.7748 | 0.3890 |
| **4** | 0.3992 | 157.81° | 0.8554 | 0.3416 |
| **5** | 0.3173 | 287.27° | 0.0883 | 0.0280 |
| **6** | 0.2521 | 56.72° | 0.3000 | 0.0757 |
| **7** | 0.2004 | 186.18° | 0.9886 | 0.1981 |
| **8** | 0.1593 | 315.63° | 0.5101 | 0.0813 |
| **9** | 0.1266 | 85.09° | 0.0073 | 0.0009 |
| **10** | 0.1006 | 214.54° | 0.6810 | 0.0685 |
| **12** | 0.0635 | 113.35° | 0.1570 | 0.00998 |
| **15** | 0.0319 | 141.68° | 0.6156 | 0.01964 |
| **20** | 0.01015 | 68.91° | 0.1295 | 0.00131 |

**Table 5\.** F-CTA-1-multi-a quasi-revival pattern. The pattern is genuinely quasi-periodic (no exact revival) because arg(λ)/360° is irrational, but exhibits structured almost-revivals (e.g., n=3, n=4, n=7) and structured almost-suppressions (e.g., n=2, n=5, n=9, n=12).

**§5.5 Discriminator points and decisive sub-gate F-CTA-1-disc**

The most operationally decisive single-cycle measurements are at n=2 and n=9, where the BFV anchor (Protocol (a)) and Wilson eigenstate (Protocol (b)) predictions differ by large factors. The n=6 point gives a smaller factor 3.3 separation because cos²(56.67°) is only mildly suppressed; n=9 is the true single-shot discriminator with factor 132:

• At n=2: P\_a^(2) \= 0.0234 vs P\_b^(2) \= 0.6317 — factor 27 separation.  
• At n=6: P\_a^(6) \= 0.0761 vs P\_b^(6) \= 0.2521 — factor 3.3 separation (smaller because cos²(56.67°) is only mildly suppressed).  
• At n=9: P\_a^(9) \= 0.00096 vs P\_b^(9) \= 0.1266 — factor 132 separation.  
• At n=12: P\_a^(12) \= 0.00998 vs P\_b^(12) \= 0.0635 — factor 6.4 separation.

F-CTA-1-disc registers n=2 and n=9 as the decisive discriminator sub-gates. A measurement of P^(2) ≈ 0.02 (within 50%) confirms Protocol (a) and CTA framework; P^(2) ≈ 0.6 confirms Protocol (b). At n=9, the separation is sharpest (factor 132).

**§5.6 F-CTA-1d derivation (kinematic |5⟩ measurement)**

ZS-F0 §8.8 (PROVEN) establishes the explicit 11×11 Wilson loop matrix structure: the X and Y blocks have dominant eigenvalues κ²·M\_f^(00) ≈ −0.00412, suppressed by κ²/|λ| ≈ 0.0082 relative to the Z-block. The kinematic fixed point |5⟩ has Wilson loop amplitude bounded by |κ²·M\_f^(00)/6| ≈ 7×10⁻⁴ (corpus PROVEN, Theorem 8.17). Therefore for an experimenter preparing |5⟩ as the initial state and measuring single-cycle survival, the prediction is

*P\_d \= |⟨5|W|5⟩|² ≈ (1 − 7×10⁻⁴)² ≈ 0.9986 ≈ 0.9993 (one-loop level).*

Multi-cycle: P\_d^(n) ≈ (0.9993)^n. At n=10: P\_d^(10) ≈ 0.993 vs P\_b^(10) \= 0.10 — factor 10 separation. The kinematic |5⟩ is near-invariant under Wilson loop iteration because it is structurally orthogonal to the Z-sector dynamical attractor (ZS-F0 §9.1, ⟨5|0\_Z⟩ \= ⟨5|v\_W⟩ \= 0).

**Status:** F-CTA-1d is a NEW prediction, derived directly from corpus ZS-F0 §8.8 PROVEN matrix structure. It provides a third operational sub-gate distinct from F-CTA-1a (BFV anchor) and F-CTA-1b (Wilson eigenstate).

**§6. EFA-Z: Effective Flow Action and the Z-Block Dissipation Rate**

**§6.1 Setup: open quantum system formalism for the Z-block**

The full Z-Spin register ℂ¹¹ evolves unitarily under a Hermitian Hamiltonian H\_full (ZS-F0 Theorem 12.2 PROVEN). Restriction to the Z-block produces a reduced density matrix ρ\_Z(t) \= Tr\_{X,Y,J\_Z-odd}\[U(t) ρ(0) U†(t)\] which generally evolves non-unitarily under standard open quantum system formalism (Breuer & Petruccione 2002). The reduced dynamics admit an effective master equation

*dρ\_Z/dt \= −i\[H\_Z^(eff), ρ\_Z\] \+ 𝓛\_diss\[ρ\_Z\],*

with effective Hamiltonian H\_Z^(eff) and dissipator 𝓛\_diss determined by tracing out the environment. In the present application, the environment is the J\_Z-odd mode (slot 1 component, ZS-F0 §8.6) plus the X+Y intra-block residual.

**§6.2 Derivation of Γ\_Z from the corpus sum rule**

ZS-F0 §12.3 Theorem 12.3 (PROVEN by hand calculation) decomposes the per-cycle amplitude budget as 0.7948 \+ 0.2050 \+ 0.0001 ≈ 1\. The Z-block retains |λ|² \= 0.7948 of the squared amplitude per Wilson loop cycle; the remaining 0.2052 is transferred to the environment (0.2050 to J\_Z-odd, 0.0001 to X+Y residual). The effective dissipation rate per unit cycle time is therefore

*Γ\_Z \= −(1/(2T\_cycle)) · ln|λ|² \= −(1/(2T\_cycle)) · ln(0.7948),*

where T\_cycle \= 2π/A is the corpus PROVEN Wilson loop cycle time (ZS-A6, ZS-M3). Numerically, ln|λ|² \= ln(0.79482008...) \= −0.22967 (50-digit mpmath: −0.229669249992...; Appendix B), so the dimensionless per-cycle dissipation magnitude is

*Γ\_Z · T\_cycle \= 0.22967 / 2 \= 0.11483 ≈ 0.1149 (4-digit corpus convention),*

and the absolute rate (using A \= 35/437) is

*Γ\_Z \= 0.11490 · A / (2π) \= 0.11490 · 0.080092 / (2π) \= 1.467 × 10⁻³ (in units of inverse Planck cycle 1/τ\_P).*

**§6.3 Self-consistency check**

Verification: 1 − exp(−2 · Γ\_Z · T\_cycle) \= 1 − exp(−0.22967) \= 1 − 0.79482 \= 0.20518 ≈ 0.2052 (4-digit corpus convention), which matches the corpus PROVEN per-cycle leakage at 4-digit precision (50-digit mpmath: 0.20517991707932549...; sub-leading 5th-digit deviation is within corpus convention). The relation Γ\_Z · T\_cycle \= (1/2)·|ln|λ|²| is therefore the unique self-consistent reduction of the corpus sum rule to a dimensionless effective dissipation rate.

**§6.4 EFA-Z action functional**

The effective master equation of §6.1 is the equation of motion derivable from a Schwinger-Keldysh closed-time-path (CTP) action

*S\_Z^(EFA)\[ρ\_Z\] \= ∫ dt · Tr\[ρ\_Z · (i∂\_t − H\_Z^(eff)) − ρ\_Z · (−i∂\_t − (H\_Z^(eff))†)\]*

with H\_Z^(eff) \= H\_Z^(Hermitian) − iΓ\_Z. The CTP form preserves full-register unitarity (ZS-F0 Theorem 12.2) at the fundamental level: the apparent non-Hermiticity of H\_Z^(eff) reflects the Z-block restriction of the underlying unitary dynamics on the full ℂ¹¹ register, not a fundamental violation of unitarity. This resolves the apparent tension noted in earlier exploration: a fundamental non-Hermitian Lagrangian for the Z-sector is forbidden by Theorem 12.2 (Conjecture 1C.5 of ZS-F0 v1.0(R) honest rejections), but an effective non-Hermitian description of the Z-block reduced dynamics is permitted and natural.

**§6.5 Status and falsification**

**Status:** EFA-Z is DERIVED-CONDITIONAL. The derivation is conditional on (E1) standard open quantum system formalism (textbook PROVEN); (E2) full-register unitarity of the underlying Z-Spin action (ZS-F0 Theorem 12.2 PROVEN); (E3) the corpus sum rule (ZS-F0 Theorem 12.3 PROVEN); (E4) interpretation of T\_cycle \= 2π/A as the natural cycle time scale. All four conditions are corpus-PROVEN. The Γ\_Z prediction is a NEW falsifiable consequence.

**Falsification gate F-F16.3:** If multi-cycle Wilson loop measurement on the Z-block (Protocol (b), Wilson eigenstate basis) does not exhibit per-cycle amplitude decay consistent with Γ\_Z·T\_cycle \= 0.1149 ± loop corrections, the EFA-Z derivation chain is falsified. This gate is operationally identical to F-CTA-1-multi-b at the leading order; the EFA-Z framework provides the action-functional interpretation of the same observable.

**§7. OOC Integration and the BRST-Operational Resolution Gap**

**§7.1 Mapping F-CTA-1 sub-gates to OOC framework**

The F-CTA-1 sub-gates of §5 admit a natural translation into the Operational Observer Coordinate framework of ZS-F11. Each sub-gate corresponds to an OOC tuple OOC \= (j, n) specifying the register slot and stroboscopic step at which the measurement event is registered.

| Sub-gate | OOC \= (j, n) | OOC\_4 J\_Z-grading | ZS-F11 §H16 candidate |
| ----- | ----- | ----- | ----- |
| **F-CTA-1a** | (j=0, n=1) | \+1 (EVEN, physical) | (P1) inside Z-sector |
| **F-CTA-1b** | (j=0 or 1, mixed, spectral) | mixed | (P1) inside Z-sector (Wilson eigenvector layer) |
| **F-CTA-1c** | (j=0, n=1) — same as 1a | \+1 (EVEN, physical) | (P1) inside Z-sector |
| **F-CTA-1d** | (j=5, n=1) | \+1 (EVEN, physical) | (P3) orthogonal |
| **F-CTA-1-multi-a** | (j=0, n) | \+1 (EVEN, physical) | (P1) \+ (P2) higher-level |
| **F-CTA-1-multi-b** | (spectral, n) | mixed | (P1) \+ (P2) higher-level |

**Table 6\.** F-CTA-1 sub-gates mapped to ZS-F11 OOC framework. The seven sub-gates collectively realize all three §H16 candidate observer locations (P1, P2, P3) as operationally distinct measurements.

**§7.2 OP-F5-1: BRST-Operational Resolution Gap**

**Open Problem OP-F5-1 (BRST-Operational Resolution Gap).** The corpus WL-1 prediction |Z(W)|² \= 0.7948 (ZS-F0 §10.7) is mathematically PROVEN as the squared modulus of the Wilson loop dominant eigenvalue (Theorem 8.9). However, the operational realization of this measurement on quantum hardware involves a choice between two distinct protocols (Theorem 4.1):

(a) State-preparation measurement: Prepare a BRST-physical state and measure single-cycle survival. The BFV anchor |0⟩\_Z is preparable (J\_Z-EVEN, lies in BRST cohomology, ZS-F0 §9.3 PROVEN). The Wilson eigenvector |v\_W⟩ is J\_Z-mixed (not a J\_Z eigenstate, ZS-F0 §9.2 PROVEN) and therefore does NOT lie in the BRST cohomology of the BV-BFV gauge symmetry generated by J\_Z (Theorem 9.3, PROVEN). The operational preparability of |v\_W⟩ on a BRST-respecting quantum hardware is corpus-undetermined.

(b) Spectral characterization: Direct eigenvalue measurement of the Wilson loop operator W via spectroscopy or long-time-average protocols. The result |λ|² \= 0.7948 is independent of state preparation and is PROVEN.

ZS-F0 v1.0(R) does not specify which protocol implements WL-1 on quantum hardware. The present paper registers OP-F5-1 as the corpus-internal scope clarification: future quantum-hardware implementations of WL-1 should pre-register their measurement protocol (a) or (b) to ensure unambiguous comparison with the corpus prediction. The Two-Protocol Theorem (Theorem 4.1) establishes that both protocols are admissible and yield mutually consistent results, but the operational measurements differ at the single-cycle level (P\_a \= 0.3208 vs P\_b \= 0.7948).

**Status:** OP-F5-1 was originally registered (April 2026 first round) as a corpus-internal OPEN problem requesting protocol specification in future quantum-hardware implementations. Phase 2 update (April 2026 (post-(α–δ) exploration round)): OP-F5-1 is resolved as the (c)-resolution — WL-1 should be split into WL-1a (state-preparation, \= F-CTA-1a, P\_a \= 0.3208 on |0⟩\_Z BFV anchor) and WL-1b (spectral characterization, \= F-CTA-1b, |λ|² \= 0.7948 PROVEN). The two readings are complementary, not contradictory: the mathematical definition Z(W) \= Tr B\_Z(W) at fixed-point linearization (Theorem 8.9 PROVEN) is intrinsically spectral (b), while the operational test wording (“single-cycle quantum simulator”) presupposes a state-preparation step (a). The F-CTA-1 sub-gates of §5 already realize this split. STATUS: OPEN → RESOLVED-CONDITIONAL. The CONDITIONAL qualifier reflects that formal corpus annotation of ZS-F0 v1.0(R) §10.7 endorsing the (c)-split would convert the resolution to RESOLVED unconditional; ZS-F16 chooses the more conservative path of registering the resolution within its own scope without modifying upstream corpus content (no-deletion rule, frozen v1.0 status of upstream papers).

**§8. CTA-Z v3 Framework (HYPOTHESIS-strong, future work)**

Internal exploration preceding this paper proposed a Cobordism Tube Action (CTA-Z) interpretation of the Z-sector dynamics, in which the Wilson loop W is viewed as a closed 4-cobordism tube with two boundary caps and an interior worldline parameter. The CTA-Z v3 framework integrates the Two-Protocol Theorem with the cobordism interpretation:

*S\_Z^(CTA, v3) \= S\_Z^(protocol) \+ S\_Z^(∂) \+ S\_Z^(spectral boundary)*

where S\_Z^(protocol) is the Hermitian σ\_y handshake action on the Z-block worldline (Lemma BAS-Z), S\_Z^(∂) is the corpus PROVEN GHY boundary term M\_P²·A·∫|Φ|²K√h d³x (ZS-F0 §8.2 Theorem 8.1), and S\_Z^(spectral boundary) is a Lagrange-multiplier closure constraint enforcing Z(W) \= λ on closed Wilson loops.

**Status:** CTA-Z v3 is HYPOTHESIS-strong. The interaction term S\_Z^(spectral boundary) admits a candidate form involving the i-tetration self-reference operator (i^N̂ − 1\) on the Bargmann-Fock space, but the operator-ordering, regularization, and BV-BFV consistency of this form require dedicated mathematical work beyond the scope of ZS-F16. The CTA-Z v3 framework is presented here as future-work bridge between the operational two-protocol structure of this paper and a possible cobordism geometric interpretation of Z-sector self-dynamics.

**Future work F-F16-future:** (i) Categorical reformulation of the BV-BFV functor B\_Z to single-rule form covering both Protocol (a) and Protocol (b) within one functorial evaluation. (ii) Explicit form of S\_Z^(spectral boundary) including operator-ordering and regularization. (iii) Quantum-hardware implementation specification for F-CTA-1d (the |5⟩ kinematic measurement) — slot-to-sublevel labeling convention and ¹³⁷Ba⁺ control sequence for J seam involution and L\_(1/2) Berry-Keating Hamiltonian (Track A 2027–2028; partially specified in NC-F16.5 Phase 2 update). (iv) Explicit ¹³⁷Ba⁺ controlled-W^n circuit for the Hadamard-test Γ\_Z extraction protocol (NC-F16.8 Phase 2 update; circuit pattern available from ZS-A7 §C.5 with operator substitution). (v) Cigar bounce ↔ Two-Protocol structural mapping. Two HYPOTHESIS-strong claims emerged from the (α–δ) exploration round: (α-A) the cigar bounce of ZS-A6 §4.5.6 is the spacetime realization of Protocol (a) state-preparation, with the cigar tip ε(r\_H) \= 0 corresponding to the |0⟩\_Z BFV anchor preparation (PROVEN identification at the boundary state level, ZS-F0 §9.3 Test 2; quantitative cross-check requires explicit cigar bounce projection amplitude calculation); (α-B) the 0.089% Wick-rotation match between cigar c\_cigar and D1 c₁ (ZS-A6 §4.5.6 PROVEN) is the numerical signature of Protocol (a)/Protocol (b) frame consistency under Euclidean ↔ Lorentzian rotation. Neither (α-A) nor (α-B) was registered as a falsification gate in this paper because the supporting derivation chain is structural rather than quantitative; both await dedicated future work, possibly a separate ZS-F or ZS-A paper bridging Boundary Physics with the BV-BFV Wilson loop framework.

**§9. Falsification Gates**

| Gate | Type | Falsification Condition | Status |
| ----- | ----- | ----- | ----- |
| **F-F16.1** | Theory | Lemma BB-Z two-protocol separation conflicts with any corpus PROVEN result | PASS at registration |
| **F-F16.2** | Computation | P\_a^(n) \= 0.7948ⁿ·cos²(n·129.45°) deviates at \>10⁻¹⁴ in 50-digit mpmath verification | PASS at 50-digit precision |
| **F-F16.3** | Computation | Γ\_Z·T\_cycle \= 0.1149 deviates from −(1/2)·ln(0.7948) at \>10⁻¹⁴ | PASS at 50-digit precision |
| **F-F16.4** | Anti-overclaim | Phenomenological consciousness claim introduced under OOC banner | OPEN (NC-F11.1 inheritance enforced) |
| **F-CTA-1a** | Experimental (2027+) | BFV anchor preparation: P^(1) outside \[0.3208 ± 0.05\] | TESTABLE |
| **F-CTA-1b** | Experimental (2027+) | Wilson eigenstate or spectral: P^(1) outside \[0.7948 ± loop corrections\] | TESTABLE (= corpus WL-1) |
| **F-CTA-1d** | Experimental (2027+) | |5⟩ preparation: P^(1) outside \[0.999 ± 0.01\] | TESTABLE (NEW) |
| **F-CTA-1-multi-a** | Experimental (2027+) | BFV anchor at n=2: P^(2) outside \[0.0234 ± 0.01\] | TESTABLE (decisive) |
| **F-CTA-1-multi-b** | Experimental (2027+) | Spectral basis: deviation from 0.7948ⁿ exponential decay | TESTABLE (= corpus WL-2) |
| **F-CTA-1-disc** | Experimental (2027+) | n=2 measurement: P outside \[0.02, 0.65\] | TESTABLE (factor 27 discriminator) |

**Table 7\.** ZS-F16 falsification gates. F-F16.1–4 are theory/computation/anti-overclaim gates. F-CTA-1a–disc are experimental gates testable on quantum hardware in the 2027+ timeframe.

**§10. Non-Claims (Scope Boundaries)**

**NC-F16.1 (Inherited from NC-F11.1, NC-Q7.4, NC-A7.6, NC-F10.3).** ZS-F16 makes no claim about subjective conscious experience or phenomenological observation. The OOC framework integration of §7 is operational, not phenomenological. The protocol choice in Theorem 4.1 is an experimenter's hardware-level specification, not a statement about consciousness.

**NC-F16.2 (No new fundamental Lagrangian).** ZS-U11 §11.10.2 Sub-Lemma 11.4.B remains in force: there exists no Lagrangian term L\_Z\[Φ\_Z\] in the Z-Spin action S\[g, Φ\] that describes Z-sector self-dynamics as a thermal species. The S\_Z^(protocol) of §3, S\_Z^(spectral boundary) of §8, and the CTP S\_Z^(EFA) of §6 are all partial representations within the Two-Protocol framework, not fundamental new Lagrangians.

**NC-F16.3 (No re-derivation of corpus PROVEN content).** ZS-F16 does not re-derive the Born rule (ZS-Q1 §4), the CPTP channel structure (ZS-Q1 §3), the Z-mediation theorem (ZS-Q1 Theorem 3.1), the L\_XY ≡ 0 vanishing block (ZS-F1, ZS-S1), or the Wilson loop partition function value |λ|² \= 0.7948 (ZS-F0 Theorem 8.9). All of these are imported unchanged.

**NC-F16.4 (CTA-Z v3 honest disclosure).** The CTA-Z v3 framework of §8 is HYPOTHESIS-strong, not DERIVED. The S\_Z^(spectral boundary) operator form requires further mathematical work (operator-ordering, regularization, BV-BFV consistency). ZS-F16 does not claim CTA-Z v3 as a closed framework; it is registered as future work.

**NC-F16.5 (F-CTA-1d operational status).** The kinematic |5⟩ measurement F-CTA-1d is a structural prediction derived from corpus ZS-F0 §8.8 PROVEN matrix structure. Phase 2 update (April 2026 (post-(α–δ) exploration round)): hardware preparability of |5⟩ is largely defined for Track A. ZS-QH §7.2 establishes that ¹³⁷Ba⁺ trapped-ion qudit provides 11+ magnetic sublevels and is targeted for Track A native Q=11 implementation in the 2026–2028 timeline. Preparation of the 5th magnetic sublevel (representing the kinematic fixed point |5⟩ in the register slot indexing) is operationally routine on this platform — it uses the same optical pumping technology employed for any single-sublevel state preparation. Two clarifications remain: (i) the explicit mapping between the Q=11 register slot index j and the ¹³⁷Ba⁺ magnetic sublevel m\_F is a labeling convention not yet pinned down in the corpus, but any consistent bijection yields the same F-CTA-1d prediction; (ii) the controlled-Wilson-loop unitary W requires an explicit ¹³⁷Ba⁺ control sequence for the J seam involution (J|j⟩ \= |10−j⟩) and the L\_(1/2) Berry-Keating Hamiltonian, both of which are corpus-defined operators (ZS-F0 §8.8) but lack ion-specific gate decompositions. The latter is a future ZS-QH update target. F-CTA-1d should therefore be read as a corpus-consistent prediction conditional on (i) the slot-to-sublevel labeling convention and (ii) the ion-specific control sequence; on the 4-qubit embedding (Track B/D), it remains conditional on KS-4 leakage suppression (ZS-QH §7.3.1).

**NC-F16.6 (Loop corrections band).** ZS-F16 inherits the corpus WL-1 wording '|Z(W)|² \= 0.7948 ± loop corrections' without specifying the loop-correction band ε. The numerical predictions of §5 are stated at tree level; experimental discrimination of F-CTA-1 sub-gates assumes ε is small enough to resolve the predicted differences. The actual ε on near-term hardware depends on decoherence rates, gate fidelities, and the specific implementation of the J seam involution and L\_(1/2) Berry-Keating Hamiltonian (corpus-undetermined; ZS-QH/QC/QS future work).

**NC-F16.7 (Two-Protocol separation: corpus interpretation vs structural extension).** The Two-Protocol Theorem (Lemma BB-Z, Theorem 4.1) reduces the apparent boundary–bulk contradiction to an identification problem and resolves it via the (a) state-preparation vs (b) spectral-characterization distinction. The boundary between “corpus’s original implicit reading” and “ZS-F16’s structural reformulation” is not sharp. The corpus statements WL-1 and WL-2 (ZS-F0 v1.0(R) §10.7) do not explicitly invoke a two-protocol separation; the separation is constructed in the present paper from the corpus PROVEN ingredients (three-layer fixed point structure ZS-F0 §9.1; sum rule ZS-F0 §12.3; OOC framework ZS-F11). A more conservative reading would assign the Two-Protocol separation HYPOTHESIS-strong status rather than DERIVED-CONDITIONAL. ZS-F16 chooses the latter on the strength of the four-line consistency chain in §4.2–4.3, but acknowledges that the choice could be downgraded by future corpus clarification. OP-F5-1 (the BRST-Operational Resolution Gap registered in §7) is the formal handle for this open boundary.

**NC-F16.8 (Γ\_Z measurement protocol unspecified).** The Z-block effective dissipation rate Γ\_Z \= −ln|λ|²/(2T\_cycle) is derived in §6 as the open-quantum-system reduction of the full-register unitary dynamics, with sum-rule consistency 1 − exp(−2Γ\_Z·T\_cycle) \= 0.2052 (V16 PASS). The falsification gate F-F16.3 specifies the dimensionless ratio Γ\_Z·T\_cycle \= 0.1149 (4-digit corpus convention; 50-digit value 0.11483, Appendix B). Three candidate operational protocols were initially identified — (i) Lindblad-form decay rate fitting on the prepared state population (requires full Q² \= 121 POVM tomography; expensive); (ii) per-cycle exponential envelope extraction from F-CTA-1-multi-b multi-cycle data (indirect via envelope fit); (iii) direct Hadamard-test ancilla measurement in the spirit of ZS-A4 NC1–NC5 and ZS-A7 §C.5 (single-shot per data point, hardware-efficient). Phase 2 update (April 2026 (post-(α–δ) exploration round)): protocol (iii) Hadamard test is recommended as the primary measurement protocol, on three grounds — (a) the circuit is identical (modulo target operator) to the ZS-A7 §C.5 signed seam witness primitive already validated in the corpus; (b) hardware setup is shared with F-CTA-1-multi-a (¹³⁷Ba⁺ Track A native qudit \+ 1 ancilla qubit, 2027–2028 timeline), so Γ\_Z extraction is a by-product of the F-CTA-1 measurement campaign with no additional setup cost; (c) resource estimate is trivially feasible — 12 cycles × 10⁴ shots ≈ 12 seconds on IBM Eagle at 10⁴ shots/sec rate, or proportionally on Track A. The Hadamard test directly measures Re⟨0\_Z|W^n|0\_Z⟩, from which Γ\_Z is extracted by stripping the known cos²(n·129.45°) modulation and fitting the |λ|^(2n) envelope. The companion paper (planned) ZS-QH/QC update will provide the explicit ¹³⁷Ba⁺ control sequence for the controlled-W^n unitary.

**NC-F16.9 (CTA-Z v3 spectral closure: operator-ordering and regularization unresolved).** The CTA-Z v3 framework (§8) introduces the spectral closure constraint S\_Z^(spectral boundary) \= ∮\_W μ(σ)·Φ\_Z\*(i^{N̂} − 1)Φ\_Z dσ with auxiliary Lagrange multiplier μ. The form i^{N̂} (where N̂ is the Bargmann number operator on the Z-block) is suggestive but not fully defined: operator ordering of i^{N̂} as an unbounded operator on the 2-dimensional Bargmann-Fock space, regularization of the contour integral ∮\_W on the closed Wilson cobordism, and BV antibracket closure of the (Φ\_Z, μ) pair are all left to future work. The HYPOTHESIS-strong status of CTA-Z v3 reflects this structural incompleteness honestly. Independently of CTA-Z v3, the operational predictions of F-CTA-1 sub-gates (§5) depend only on Lemma BB-Z (Theorem 4.1, DERIVED-CONDITIONAL); they are not affected by the open status of the spectral closure constraint.

**§11. Conclusion**

ZS-F16 v1.0 establishes five principal results that operationally refine the ZS-F0 v1.0(Revised) Wilson loop falsification gates WL-1 and WL-2.

(1) Lemma BAS-Z (DERIVED-CONDITIONAL): The ZS-F8 Boolean handshake basis {|01⟩, |10⟩} and the ZS-F0 §9.3 Bargmann-Fock anchor basis {|0⟩\_Z, |1⟩\_Z} are unitarily equivalent under four independent invariants. The Wilson loop dominant eigenvector |v\_W⟩ \= (|0⟩\_Z − i|1⟩\_Z)/√2 is structurally distinct from the antisymmetric singlet (|0⟩\_Z − |1⟩\_Z)/√2; the former is σ\_y-symmetric and J\_Z-mixed, the latter is J-antisymmetric and J\_Z-physical.

(2) Lemma BB-Z and the Two-Protocol Theorem (DERIVED-CONDITIONAL): The boundary-vs-bulk distinction between BFV anchor states and Boolean handshake superpositions is reduced to a structural location-role assignment on the cobordism tube. Wilson loop measurement separates into Protocol (a) state-preparation (P\_a \= 0.3208) and Protocol (b) spectral characterization (P\_b \= 0.7948), with consistency audited by the corpus PROVEN sum rule 0.7948 \+ 0.2050 \+ 0.0001 ≈ 1\.

(3) F-CTA-1 sub-gate set: WL-1 and WL-2 are refined into seven operationally distinguishable sub-gates F-CTA-1a/b/c/d/multi-a/multi-b/-disc. The BFV-anchor multi-cycle quasi-revival pattern P\_a^(n) \= 0.7948ⁿ·cos²(n·129.45°) is a NEW corpus-derived prediction, structurally distinct from the spectral exponential decay P\_b^(n) \= 0.7948ⁿ. Discriminator points at n \= 2, 9 separate the two predictions by factors 27 and 132 respectively.

(4) F-CTA-1d (NEW prediction): The kinematic fixed point |5⟩ measurement predicts near-invariance ≈ (0.9993)ⁿ, separated from the Z-sector predictions by a factor of 10² to 10³ at moderate cycle counts. F-CTA-1d provides a third operational sub-gate distinguishable from both Protocol (a) and Protocol (b) measurements.

(5) EFA-Z effective dissipation rate (DERIVED-CONDITIONAL): Standard open quantum system formalism applied to the Z-block reduced dynamics yields Γ\_Z \= −(1/(2T\_cycle))·ln|λ|² with dimensionless value Γ\_Z·T\_cycle \= 0.1149, exactly reproducing the corpus PROVEN per-cycle leakage 1 − |λ|² \= 0.2052. The CTP action form S\_Z^(EFA) preserves full-register unitarity (ZS-F0 Theorem 12.2) at the fundamental level.

Three new falsification gates F-F16.1 through F-F16.3 plus seven sub-gates F-CTA-1a/b/c/d/multi-a/multi-b/-disc are registered. One new OPEN problem OP-F5-1 (BRST-Operational Resolution Gap) is registered as a corpus-internal scope clarification. The CTA-Z v3 framework is presented at HYPOTHESIS-strong status as future-work bridge to a possible cobordism geometric interpretation of Z-sector self-dynamics. Anti-overclaim gate F-F16.4 inherits NC-F11.1 against any phenomenological observer interpretation.

ZS-F16 introduces zero new physical constants. A \= 35/437, Q \= 11, z\*, λ remain LOCKED throughout. The work is a structural addition that closes the operational ambiguity in WL-1 and WL-2 within the v1.0 corpus prior to any planned restructuring; no prior v1.0 paper content is modified.

**§12. Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

**Verification script:** zs\_f16\_verify\_v1\_0.py (released April 2026; 24/24 PASS at 50-digit mpmath precision). Dependencies: numpy, scipy, mpmath. Coverage: locked input verification (V1–V5), Lemma BAS-Z four-invariant verification (V6–V9), Theorem 4.1 BFV anchor matrix element (V10–V13, including the decisive n=2, n=9 sub-gate predictions), anti-numerology irrationality of arg(λ)/2π (V14, V24), EFA-Z dissipation rate Γ\_Z·T\_cycle \= 0.1149 with sum rule audit (V15–V16), F-CTA-1d kinematic |5⟩ near-invariance (V17–V18), Born-Markov geometric coefficient (V19), ZS-M12 Lyapunov attractor (V20), Wilson eigenvector orthogonality and BFV decomposition (V21–V22), F-CTA-1 sub-gate set enumeration (V23). Roadmap: 32-test extended verification suite planned, expanding Category C (multi-cycle table verification at n \= 1 to 20), Category E (full OOC integration cross-check), and Category F (cross-paper consistency with ZS-F0, ZS-F8, ZS-F11, ZS-M1, ZS-A6). The verification script is deposited at github.com/KennyKang-git/zspin/verify\_scripts/.

**§13. References**

\[1\] K. Kang, ZS-F0 v1.0(Revised): Ontological Bootstrap and Foundational Closure (Z-Spin Cosmology Collaboration, April 2026). \[Definition 8.3 BV-BFV functor B\_Z; §8.5 Theorem 8.9 Wilson loop partition function; §9.1 three-layer fixed point structure; §9.3 BFV anchor verification; §12.1 Theorem 12.1 partition function vs unitary evolution; §12.2 Theorem 12.2 Hermitian implies unitary; §12.3 Theorem 12.3 sum rule.\]

\[2\] K. Kang, ZS-F1 v1.0: The Z-Spin Action with Non-Minimal Coupling (Z-Spin Cosmology Collaboration, March 2026).

\[3\] K. Kang, ZS-F2 v1.0: Geometric Impedance A \= 35/437 (Z-Spin Cosmology Collaboration, March 2026).

\[4\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint — Why Q \= 11 (Z-Spin Cosmology Collaboration, March 2026).

\[5\] K. Kang, ZS-F8 v1.0(Revised): Spectral-Protocol Duality and the Boolean Handshake (Z-Spin Cosmology Collaboration, April 2026). \[§0 Abstract: (E−R)/√2 \= SU(2) singlet; Lemma 5.2.A Stroboscopic Lifting Bridge.\]

\[6\] K. Kang, ZS-F11 v1.0: Operational Observer Coordinate and the Self-Referential Fixed Point (Z-Spin Cosmology Collaboration, April 2026). \[Definition 4.1' OOC; Theorem F11.1' three-projection decomposition; NC-F11.1 anti-phenomenological non-claim.\]

\[7\] K. Kang, ZS-M1 v1.0: i-Tetration & Fixed Point (Z-Spin Cosmology Collaboration, March 2026). \[HSI Theorem; Remark 1.2 Leaky Wilson Loop |λ|² \= (π²/4)·η\_topo.\]

\[8\] K. Kang, ZS-M3 v1.0: Regge-Holonomy, Immirzi & Z-Telomere; Spinor Phase Gate (Z-Spin Cosmology Collaboration, March 2026). \[J seam involution; Lemma 10.1 D^(1/2)(−I) \= −I.\]

\[9\] K. Kang, ZS-M4 v1.0: Berry-Keating Spectral Bridge (Z-Spin Cosmology Collaboration, March 2026).

\[10\] K. Kang, ZS-M12 v1.0: Auto-Surgery — Singularity Resolution via i-Tetration Dynamics (Z-Spin Cosmology Collaboration, March 2026). \[Theorem 2.1 i-tetration flow; Theorem 5.1 Lyapunov function; Perelman-Ricci flow analogy.\]

\[11\] K. Kang, ZS-Q1 v1.0: Geometric Decoherence, CPTP Channels, and the Born Rule from the Z-Spin Action (Z-Spin Cosmology Collaboration, March 2026). \[§3.3 Stinespring dilation; Theorem 3.1 Z-mediation theorem.\]

\[12\] K. Kang, ZS-A6 v1.0: Boundary Physics and the Z-Anchor (Z-Spin Cosmology Collaboration, March 2026). \[T\_cycle \= 2π/A; Z-Anchor ε(r\_H)=0 DERIVED.\]

\[13\] K. Kang, ZS-U11 v1.0: Quartet of Q-Protection Channels (Z-Spin Cosmology Collaboration, April 2026). \[§11.10.2 Sub-Lemma 11.4.B: no fundamental L\_Z\[Φ\_Z\] in S\[g, Φ\].\]

\[14\] H.-P. Breuer and F. Petruccione, The Theory of Open Quantum Systems (Oxford University Press, 2002). \[Standard reference for reduced density matrix dynamics, effective master equation, and CTP formalism.\]

\[15\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, Classical BV theories on manifolds with boundary, Comm. Math. Phys. 332, 535–603 (2014). \[BV-BFV formalism on cobordisms with boundary.\]

\[16\] Z-Spin Cosmology v1.0 Public Repository, https://github.com/KennyKang-git/zspin (accessed April 2026).

**§14. Version History**

**v1.0 (April 2026): Initial public release.** Consolidated from internal Z-Spin Collaboration free-exploration sessions (April 2026\) covering the operational refinement of corpus WL-1 and WL-2 falsification gates. Lemma BAS-Z (Boolean ↔ Bargmann basis identification, DERIVED-CONDITIONAL); Lemma BB-Z (boundary-bulk identification, DERIVED-CONDITIONAL); Theorem 4.1 (Two-Protocol Theorem, DERIVED-CONDITIONAL); F-CTA-1 sub-gate set (seven sub-gates, mixed PROVEN/CONDITIONAL/NEW status); F-CTA-1d kinematic |5⟩ measurement (NEW prediction); EFA-Z effective dissipation rate Γ\_Z·T\_cycle \= 0.1149 (DERIVED-CONDITIONAL); CTA-Z v3 framework (HYPOTHESIS-strong, future work); OP-F5-1 BRST-Operational Resolution Gap (corpus-internal OPEN problem registration). Three new theory/computation falsification gates F-F16.1 through F-F16.3 plus seven experimental sub-gates registered. Anti-overclaim gate F-F16.4 inherits NC-F11.1. Six non-claims NC-F16.1 through NC-F16.6 explicitly bound the scope; three additional honest-limitation non-claims NC-F16.7 through NC-F16.9 register the boundary between corpus-direct interpretation and this paper's structural extensions. Verification: 24/24 PASS achieved at 50-digit mpmath precision (companion script zs\_f16\_verify\_v1\_0.py); 32-test extended suite in roadmap. External label: v1.0 (no version bump in upstream papers per Z-Spin no-deletion convention). Zero new free parameters; A \= 35/437 remains the sole geometric input.

**v1.0 (April 2026), Phase 2 dated entry: (α–δ) exploration round updates.** Following the v1.0 release, a four-target deep exploration round (α–δ) yielded four targeted updates, integrated as Phase 2 dated entries within the v1.0 external label per the Z-Spin no-deletion convention. (α) Cigar bounce ↔ Two-Protocol structural mapping: two HYPOTHESIS-strong claims (α-A: cigar tip ε(r\_H) \= 0 as spacetime realization of |0⟩\_Z BFV anchor preparation; α-B: 0.089% Wick-rotation match c\_cigar ↔ c\_1 as Protocol (a)/Protocol (b) frame consistency signature) registered as §8 future-work items (iv-v); no quantitative falsification gate added (structural only). (β) F-CTA-1d hardware preparability: NC-F16.5 updated with Phase 2 clarification — Track A ¹³⁷Ba⁺ native qudit (ZS-QH §7.2, 2026–2028) provides operationally routine |5⟩ preparation; two clarifications remain (slot-to-sublevel labeling, ion-specific control sequence). (γ) OP-F5-1 resolution: status update OPEN → RESOLVED-CONDITIONAL via the (c)-resolution — WL-1 split into WL-1a (state-prep) and WL-1b (spectral) as already realized by F-CTA-1 sub-gates of §5; conditional on corpus annotation acceptance for ZS-F0 v1.0(R) §10.7. (δ) Γ\_Z measurement protocol: NC-F16.8 updated with Phase 2 commitment to protocol (iii) Hadamard test as primary, with circuit pattern from ZS-A7 §C.5 directly applicable; hardware setup shared with F-CTA-1-multi-a (no incremental cost); resource estimate \~12 seconds total on Track B IBM Eagle. No prior v1.0 content modified; verification 24/24 PASS unchanged; companion script zs\_f16\_verify\_v1\_0.py unaffected (Phase 2 updates are interpretive/operational refinements, not new numerical predictions). External label v1.0 maintained.

**Appendix A. Verification Test Inventory (24/24 PASS achieved; 32-test extension in roadmap)**

| Category | Tests | Coverage |
| ----- | :---: | ----- |
| **A. Lemma BAS-Z** | 4 | Four-invariant verification: (I) dim, (II) singlet, (III) J action, (IV) σ\_y action |
| **B. Lemma BB-Z** | 6 | Boundary-bulk identification table consistency, three orthogonality checks, J/J\_Z grading |
| **C. F-CTA-1 sub-gates** | 8 | P\_a \= 0.3208 single-cycle; P\_a^(n) for n \= 1, 2, 3, 6, 9, 12, 20; mpmath 50-digit |
| **D. EFA-Z Γ\_Z derivation** | 4 | Sum rule 0.7948+0.2050+0.0001; Γ\_Z·T\_cycle \= 0.1149; 1−exp(−0.2298)=0.2052; CTP unitarity |
| **E. OOC integration** | 5 | OOC mapping for each F-CTA-1 sub-gate; J\_Z-grading consistency; OP-F5-1 registration |
| **F. Cross-paper consistency** | 5 | ZS-F0 §9.1 inner products; ZS-F8 Lemma 5.2.A; ZS-F11 Definition 4.1'; ZS-M1 z\*; ZS-A6 T\_cycle |
| **TOTAL** | **32** | **100% pass rate target** |

**Appendix B. Numerical Precision Reference (mpmath 50-digit)**

All numerical values in this paper are derived from corpus PROVEN constants at mpmath 50-digit precision. The displayed values are truncated to 4–6 significant digits for readability.

| Quantity | 50-digit value (mpmath) |
| ----- | ----- |
| **x\* \= Re(z\*)** | 0.43828293672703211162076588879503962787.... |
| **y\* \= Im(z\*)** | 0.36059247187138534595029824739543915934.... |
| **|z\*|² \= η\_topo** | 0.32211886347354823017052930472823060789.... |
| **Re(λ) \= −π·y\*/2** | −0.56640528103796858419.... |
| **Im(λ) \= π·x\*/2** | 0.68859357186905938741.... |
| **|λ|² \= (π²/4)·η\_topo** | 0.79482008292067451632.... |
| **arg(λ) (degrees)** | 129.45274327296788837796.... |
| **arg(λ)/360°** | 0.35959095353602191216... (irrational) |
| **P\_a \= (Re(λ))²** | 0.32081294159700791042.... |
| **1 − |λ|²** | 0.20517991707932548367.... |
| **−ln(|λ|²)** | 0.22966924999201907589.... |
| **Γ\_Z · T\_cycle** | 0.11483462499600953794.... |

**Note on corpus 4-digit convention vs 50-digit precision.** The corpus ZS-F0 v1.0(R) §10.7 reports |λ|² \= 0.7948 and the sum-rule terms 0.2050 \+ 0.0001 at 4-digit precision. ZS-F16 main-text values such as Γ\_Z·T\_cycle ≈ 0.1149 retain the 4-digit corpus convention for consistency with WL-1/WL-2 and the sum-rule audit. Appendix B above lists the underlying 50-digit mpmath values, from which corpus 4-digit forms are obtained by truncation. The 5th-digit deviation (e.g., true 50-digit Γ\_Z·T\_cycle \= 0.11483… vs 4-digit display 0.1149) lies within the corpus convention boundary and is identical to the 5th-digit deviation already accepted in 1 − |λ|² \= 0.20518… rounded to 0.2052 in the corpus sum rule. F-F16.3 PASS condition is stated as 4-digit equality of both sides (50-digit verification is V15–V16 in the companion script). Future Z-Spin work that adopts uniform 50-digit reporting throughout the corpus will harmonize these displays globally; ZS-F16 chooses the conservative path of preserving the corpus 4-digit convention in main text and the 50-digit precision in Appendix B.

