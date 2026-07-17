**ZS-F45**  
**The Seam Null-Power Route — A B3 Negative Audit: the Null-Power Reduction Theorem, with Three Reusable Tools**

Kenny Kang — Z-Spin Cosmology Program (independent) · July 2026 · Foundations Series · Paper code **ZS-F45** · Version 1.4. B3 route-audit paper. Consumes ZS-M1, ZS-M3/F10, ZS-M44, ZS-M46, ZS-M47, ZS-F30–F43, ZS-A17, ZS-A23–A32.

**Verification: 47/47 PASS \+ 12/12 guards** (zs\_f45\_verify\_v1\_4.py; fail-closed, exits non-zero on any theorem-tier failure) | **5 firewalled observations** printed separately, never counted as PASS | **Zero fitted parameters** | (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) **LOCKED**.

**§0. Abstract**

This is an *audit*, not a closure attempt. It opened the Planck-power / null-boundary route against barrier B3 as a candidate for the sole reopening gate F-F40.6, drove it to its honest terminus, and records the verdict: **the null-power attack reduces to exactly the same charge-unit residual ê₆ ≡ E\_len(seam) that ZS-F33/F42/F43 already localized** (Theorem F45.R). The route does not close B3. Its surviving value is (i) the audit verdict — a fourth, independent line reaches the same wall — and (ii) three reusable tools that outlive the negative verdict.

**Theorem F45.R (Null-Power Reduction).** Under the registered null-power postulate AX-PP and the (2+1) transplant, the value-carrying content of the null-power route reduces to the pre-existing ê₆ ≡ E\_len(seam) residual: the two value-gates G-PP2b and G-PP4 both terminate there — the first at the F-F42.36 charge-unit wall, the second at the ZS-M47 Parent-Factor residual — so the route supplies no new metric-side datum. \[DERIVED; §3.\]

**The three exported tools.** **(T1)** *Planck-Power/Frozen-Gas Identity* \[IDENTITY\]: ρ\_Λ \= η\_Z·L\_P/(c·A\_∂), A\_∂ \= 4π(c/H\_∂)², is an identity-level rewrite of the ZS-F42 IR ledger with **η\_Z \= (3/2)Ω\_Λ,0 \= 249/242 \= (1/4)c\_χω²** exactly (ω² cancels rationally), plus the two-ledger reading (N \= 3 ⇔ dim X: the IR ledger is the ℏ-free (G,c) ledger, unit L\_P, mirror to the G-free charge unit q\_P). **(T2)** *Seam-as-Null-Energy Channel* \[DERIVED-CONDITIONAL on KH1–KH4\]: composing ZS-M46 Theorem C (GLW U(1)-current net) with the Morinelli–Tanimoto–Wegener null-plane HSMI theorem and the Ceyhan–Faulkner ANEC/QNEC theorem shows the seam generator **P** is the averaged-null-energy operator of a null-cut inclusion — reusable by any future seam-energy argument. **(T3)** *A-vs-ω Holonomy Discriminator* \[DERIVED\]: in the ISO(2,1) Chern–Simons reading a deficit is a per-cycle *additive* increment, so of the corpus's two holonomy-like numbers only the telomere drift **A** qualifies (d/dn\[n**A**\] \= **A**), while ω \= 2.2592 is a constant reassigned to its ZS-M46 role as the helical twist Re τ\_K \= 0.35957.

**Barrier B3 is not closed; F-F40.6 armed, not fired; Ω\_Λ,0 \= 83/121 and U\_N untouched.** The absolute-scale question is handed to the sequestering execution ZS-F46 (radiative-stability face) and stays, for its residual-value face, the documented B3-B frontier. Verification: 47/47 PASS \+ 12/12 guards; zero fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED.

**Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| **IDENTITY** | True by construction/definition; recorded so it is not mistaken for evidence. |
| **DERIVED** | Follows from corpus axioms/locked constants by explicit steps. |
| **DERIVED-CONDITIONAL** | Derived contingent on explicitly listed, falsifiable conditions. |
| **IMPORTED-PROVEN** | External theorem with published proof, consumed as-is (Deser–Jackiw–'t Hooft; Ashtekar–Varadarajan; Achúcarro–Townsend; Witten; Borchers; Ceyhan–Faulkner; Morinelli–Tanimoto–Wegener; Eckmann–Lim). |
| **NON-CLAIM** | Explicit registration that a statement is not being made (here: the axiom AX-PP; the absolute value). |
| **OPEN / OPEN-TERMINAL** | Well-posed and unresolved / unresolvable with current corpus tools. |
| **NO-GO / CLOSED-NEGATIVE** | Proven impossibility / a route proven not to work under its pre-registered rule. |

**§1. The inherited terminus and the audit mandate**

The B3 mechanism arc ended before this paper. ZS-F40 v1.2 closed all three determinant/clock routes negatively (the √2 Refusal, the OPS exclusion, the θ₁ exclusion), recorded the mechanism programme TERMINAL, and left exactly one reopening trigger, **F-F40.6**, which demands a *new axiom-level input*. ZS-F41 supplied the lattice half as a candidate and installed the Terminal Stopping Rule. ZS-F42 delivered the frozen-gas hierarchy theorem and terminated at the NON-CLAIM that the membrane charge e₆ cannot be fixed by (**A**, **Q**) and topology (gate F-F42.36). ZS-F43 re-typed the residual: by Stone–von Neumann–Mackey the charge unit is invisible from inside the Z-sector algebra, the well-posed target is the dimensionless ê₆, and **Theorem T1b** proved any successful execution lands at ê₆ requiring exactly one metric-side datum.

The present paper asks one question: *does a null-boundary power principle on the seam supply that datum?* The answer, established through this paper's four theorems and executed gates, is **no — it reduces to the same ê₆**. That negative answer, precisely located, is the paper's contribution, together with three tools produced along the way. The discipline is the predecessors': no value of ρ\_Λ, ê₆, or ℓ is evaluated; no depth mechanism is promoted; every load-bearing external ingredient is an imported theorem or explicitly tagged partial.

Notation: ê₆ := e₆/M̄\_P², A\_∂ \= 4π(c/H\_∂)² (Hubble-sphere convention). Terminology follows the corpus: *Z-sector* names the stage (dim **Z** \= 2), *Z-Spin* the action on it. All numerical claims are reproduced by zs\_f45\_verify\_v1\_4.py (47/47 PASS \+ 12/12 guards); scale-bearing numbers appear only in firewalled context. The full v1.0–v1.2 registration abstract is retained for provenance in Appendix D.

**§2. The three exported tools**

**2.1 Tool T1 — the Planck-Power/Frozen-Gas Identity.** \[IDENTITY / DERIVED.\] Fix A\_∂ \= 4π(c/H\_∂)² and L\_P \= c⁵/G. Then ρ\_Λ \= η\_Z·L\_P/(c·A\_∂) reproduces the frozen-gas density ρ\_Λ \= 3Ω\_Λ,0·M̄\_P²·H\_∂² iff **η\_Z \= (3/2)Ω\_Λ,0 \= 3·83/(2·11²) \= 249/242 \= (1/4)c\_χω²** (exact). The last equality is rational-exact: c\_χ ≡ 498/(121ω²) by the ZS-F42 pre-registration, so c\_χ·ω² \= 498/121 with ω² cancelling before any evaluation (checks A2–A3; numeric echo D7). The dimensional algebra L\_P/(c·A\_∂) \= 2M̄\_P²H\_∂² is verified with arbitrary units (check A4). The identity carries **no new empirical content** (the ZS-F43 §6.4 non-novelty pattern) — recorded as IDENTITY so it cannot be mistaken for evidence.

*Two-ledger corollary.* \[Dimensional identity DERIVED; Z-Spin reading OBSERVATION.\] The Planck force reads F\_pl \= G^{2/(1−N)}c^{(5+N)/(N−1)}h^{(3−N)/(1−N)}; the ℏ-exponent vanishes **iff N \= 3** (checked N \= 2…9, check A5), giving F\_pl \= c⁴/G, unit c⁵/G (check A6). So the IR frozen-gas ledger (ρ\_Λ ∝ H²/G, ℏ-free) is the *classical (G, c) ledger*, unit L\_P, mirror to the *G-free quantum* charge unit q\_P (ZS-F42 Cor. F42.11); ℏ crosses between them exactly once (ZS-F43 T4). That the ℏ-free ledger exists iff the spatial dimension equals dim **X** \= 3 is an alignment observation, not a derivation.

**2.2 Tool T2 — the Seam-as-Null-Energy Channel.** \[DERIVED-CONDITIONAL on KH1–KH4.\] The seam standard-pair generator **P** is physically a null-energy operator, not an inert translation, by a three-theorem composition. (i) ZS-M46 Theorem C fixes the seam realization to the Guido–Longo–Wiesbrock U(1)-current net. (ii) Morinelli–Tanimoto–Wegener prove that for the free scalar the null-plane one-particle structure decomposes into lightlike fibres, the modular operator decomposes accordingly, and null-plane inclusions *are* half-sided modular inclusions whose translation generator is the integrated null energy. (iii) Ceyhan–Faulkner prove the half-sided generator is the averaged null energy and reproduces the shape derivative of relative entropy (QNEC-from-ANEC), given finite averaged null energy. Composing: **P** is the averaged-null-energy operator of a null-cut HSMI (checks E1–E2). The residual is the model-fix release (KH1–KH4): the free-field realization is established; a corpus-intrinsic realization is the honest residual (check E3).

**2.3 Tool T3 — the A-vs-ω Holonomy Discriminator.** \[DERIVED.\] In the ISO(2,1) Chern–Simons formulation a point source's physical attribute is the rotation angle √(w²) of its holonomy conjugacy class, which accumulates *additively* under loop composition (the Deser–Jackiw–'t Hooft rule adds conical rotations). A deficit is therefore a per-cycle *additive* increment. Of the corpus's two holonomy-like numbers, the derivative test is decisive (checks F1–F2): d/dn\[n**A**\] \= **A** (additive → deficit candidate), while d/dk\[2πk \+ ω\] \= 2π with ω dropping out (a constant, not an increment). ω is already claimed elsewhere — it is the ZS-M46 helical internal twist Re τ\_K \= ω/2π \= 0.35957 (check F3). Hence **A** is the *unique* per-cycle rotation-part holonomy, and the identification A \= 8πG₃E\_cycle is a derived selection, introducing no new constant (checks F4–F5).

**§3. The Null-Power Reduction Theorem (F45.R)**

**3.1 Statement.** \[DERIVED.\] Under the registered null-power postulate AX-PP (per-tick seam power ≤ c⁵/4G, one tick \= ℏ; §4) and the (2+1) transplant (§3.4), the value-carrying content of the null-power route reduces to the pre-existing ê₆ ≡ E\_len(seam) residual. Concretely, the two value-carrying gates both terminate at that single datum: **G-PP2b** at the F-F42.36 charge-unit wall, **G-PP4** at the ZS-M47 Parent-Factor residual. The route therefore supplies no new metric-side datum; it re-expresses the standing one in null-power language.

**3.2 G-PP2b terminates at the charge-unit wall.** \[OPEN.\] The (H-DEF) normalization A \= 8πG₃E\_cycle splits into (N1) the geometric leg — Kaluza–Klein reduction G₃ \= G₄/ℓ\_⊥, IMPORTED-PROVEN, giving E\_cycle \= **A**ℓ\_⊥/(8πG₄) (check G1a) — and (N2) the charge-quantum leg. (N2) is definitional: reconstructing 8πG₃·E\_cycle returns **A** identically (check G1b), with the per-cycle angle 2π/N\_2π \= **A** by construction (check G1c). So (N2) does not derive E\_cycle; it defines it through **A**. An independent fix of E\_cycle would fix ℓ\_⊥, hence the modulus ℓ \= M\_K⁻¹, hence ê₆ — exactly the charge unit F-F42.36 (and the ZS-F33 Charge-Unit Obstruction) proves cannot be fixed by (**A**, **Q**) and topology. **G-PP2b is OPEN: the geometric leg is proven, the normalization leg is the charge-unit wall in new coordinates** (check G1d). No ℓ\_⊥, E\_cycle, or ê₆ value is evaluated (guard G12).

**3.3 G-PP4 terminates at the Parent-Factor residual.** \[OPEN-TERMINAL.\] A Wieland-type discrete→continuous transition of the tick-power e^{2πt} rescale at t\* \= **Q** is not constructible with current tools: the corpus discrete/continuum distinction is controlled by *sector dimension* (ZS-M6 §5.5 — X-sector truncated octahedron tiles ℝ³, continuum emerges; Y-sector truncated icosahedron and dim **Z** \= 2 do not tile, spectra discrete), **not by depth**; t\* \= **Q** is a depth *selection* (ZS-F38), not a transition *generator* (checks H1–H2). The residual is the ZS-M47 Parent-Factor Realization Problem, identified by ZS-F43 §4.3 with the E\_len(seam) OPEN. Partial positive: the mediation channel rank ≤ dim **Z** \= 2 (ZS-Q7/T12) gives an ln 2 information ceiling on any transition threshold (check H3). **G-PP4 is OPEN-TERMINAL — reopenable only through the ZS-M47 Parent-Factor Realization, i.e. the same axiom-level input F-F40.6 already names.**

**3.4 The (2+1) transplant re-bases the value leg on a theorem — but its normalization is exactly G-PP2b.** \[general IMPORTED-PROVEN; instance DERIVED-CONDITIONAL on (H-DEF) ∧ (H-TICK).\] dim **Z** \= 2 makes the seam world-volume (2+1)-dimensional, where the contested 3+1 maximum-luminosity conjecture is *not needed*: by Deser–Jackiw–'t Hooft and Ashtekar–Varadarajan a point source carries deficit α \= 8πG₃m with Σα ≤ 2π, hence **M ≤ 1/(4G₃)**; by Achúcarro–Townsend and Witten the (2+1) theory is Chern–Simons, so deficit *is* rotation-holonomy — the phase-vs-metric gap closes by theorem in the seam's own dimension. Under (H-DEF) (tool T3), the cumulative deficit reaches 2π at N\_2π \= 2π/**A** \= 874π/35 \= 78.4500565… cycles — the corpus's frozen winding rule — with ΣE \= 1/(4G₃): **the winding change is bound saturation** (check C2). Under (H-TICK) (G₃ \= G₄/ℓ\_⊥, t\_tick \= ℓ\_⊥/c) the per-tick bound is **P\_max \= c⁵/(4G₄)** with ℓ\_⊥ cancelling identically (checks C3a–C3b), the coefficient 1/4 imported. The rate leg costs nothing: the Borchers relation Δ^{it}U(a)Δ^{−it} \= U(e^{∓2πt}a) is exact in ZS-M46 (check B4) and HSMI saturate the modular-chaos bound. **But the transplant's normalization is exactly G-PP2b (§3.2)** — the theorem re-bases the *epistemic status* of the value leg (conjecture → theorem) without moving its terminus, which remains the charge-unit wall. This is why F45.R holds: the strongest available formulation of the null-power value leg still reduces to ê₆.

**3.5 The audit verdict.** \[DERIVED.\] Both value-gates reduce to the same single dimensionful residual ê₆ ≡ E\_len(seam) that ZS-F43 localized. The null-power route is thus a *fourth* independent line — after the determinant/clock terminus (F40), the frozen-gas terminus (F42), and the unit-invisibility terminus (F43) — reaching the same wall. Per the deep-exploration protocol, a convergent search whose value-carrying nodes remain OPEN confirms "the residual cannot be closed with current corpus tools," and a fourth route landing on the same terminus is positive structural evidence that the terminus is real, not a single-tool artifact.

**§4. The registered axiom AX-PP (retained as NON-CLAIM)**

\[NON-CLAIM — registration only.\] For provenance and for downstream gates, the candidate datum audited above is the two-clause postulate: **(PP-1)** the per-tick power transported by Z-Spin mediation through the seam null boundary is bounded by **c⁵/(4G)**, with the register's topological phase transition at saturation; **(PP-2)** one register tick carries one quantum of action **ℏ**. Consequence (bookkept, not evaluated): PP-1 ∧ PP-2 give t\_tick \= 2t\_P (check C5), the O(1) \= 2 from the imported 1/4; ℏ enters the sector exactly once, realizing the ZS-A25 "exactly one dimensionful datum" no-go. AX-PP is **not** a claim that B3 is closed, **not** a derivation of e₆ (F-F42.36 respected), **not** a promotion of the depth mechanism (guard G5). The audit (§3) shows AX-PP, even granted, supplies no new datum — which is precisely why the route is recorded negative.

**§5. Falsification gates and ledger**

Table 1\. Gate statuses after the audit.

| Gate | Status |
| ----- | ----- |
| **G-PP1** (seam **P** \= null-energy operator) | DERIVED-CONDITIONAL on KH1–KH4 (tool T2) |
| **G-PP2a** ((H-DEF) discriminator: **A** selected) | DERIVED (tool T3) |
| **G-PP2b** ((H-DEF) normalization) | **OPEN** — F-F42.36 charge-unit wall (§3.2) |
| **G-PP3** (clock discharge via ZS-F39 frozen rule) | registered; not evaluated (risk R5) |
| **G-PP4** (depth transition at t\*=**Q**) | **OPEN-TERMINAL** — ZS-M47 residual (§3.3) |
| **G-PP5** (C\_UV band; automatic) | evaluated only after G-PP2a/b |
| **G-PP6** (scope honesty; U\_N untouched) | active |

Table 2\. Reduction ledger.

| Item | Status |
| ----- | ----- |
| η\_Z \= 249/242 \= (1/4)c\_χω² identity (T1) | **IDENTITY / DERIVED** |
| seam **P** \= averaged-null-energy operator (T2) | **DERIVED-CONDITIONAL on KH1–KH4** |
| (H-DEF) discriminator — **A** unique (T3) | **DERIVED** |
| (2+1) chain (DJt'H × CS × Gauss–Bonnet) | **IMPORTED-PROVEN** |
| saturation identity; P\_max \= c⁵/4G₄ | **DERIVED-CONDITIONAL on (H-DEF) ∧ (H-TICK)** |
| **Theorem F45.R: route reduces to ê₆ ≡ E\_len(seam)** | **DERIVED** (§3) |
| AX-PP (PP-1, PP-2) | **NON-CLAIM** |
| barrier B3 | **NOT closed**; F-F40.6 armed, not fired |
| Ω\_Λ,0 \= 83/121; U\_N | **untouched** |

**§6. Conclusion**

The null-power route is a clean negative result: audited to its terminus, it reduces to the same charge-unit residual ê₆ ≡ E\_len(seam) that three prior routes already reached (Theorem F45.R). What survives is not a datum but three reusable tools — the η\_Z \= 249/242 identity, the seam-as-null-energy channel, and the A-vs-ω discriminator — plus the structural fact that under (H-DEF) the corpus's frozen winding rule N\_2π \= 2π/**A** *is* the Deser–Jackiw–'t Hooft saturation condition. The absolute-scale question passes to the sequestering execution ZS-F46, which addresses the radiative-stability face while leaving the same residual as a calibrated boundary datum. B3 is not closed; F-F40.6 armed, not fired; Ω\_Λ,0 \= 83/121 and U\_N untouched.

**Acknowledgements & Code Availability**

Verification code: zs\_f45\_verify\_v1\_4.py (Python 3; mpmath 50 dps; exact Fraction arithmetic; SymPy; NumPy). Fail-closed; prints the firewalled block under an explicit banner, never counting it as PASS. Result: 47/47 PASS \+ 12/12 guards; 5 firewalled observations. Developed under the corpus session protocol with multi-AI adversarial review for circularity detection.

**Appendix A. Numerical dictionary (reproduced digits)**

| Quantity | Value | Check |
| ----- | ----- | ----- |
| **A**; **Q**; (dim X, Z, Y) | 35/437; 11; (3,2,6) | LOCKED |
| ω; κ\_λ; |λ\*| | 2.2592495540; 0.1148346250; 0.8915 | K1–K3 |
| Ω\_Λ,0; 3Ω\_Λ,0 | 83/121; 249/121 | D6 |
| c\_χ \= 498/(121ω²) | 0.8063350941 | A1 |
| **η\_Z \= 249/242** | **1.0289256198** | A2–A4, D7 |
| ‖Π − D‖\_F/√**Q** (any diagonal D) | √2 | B1–B2 |
| N\_2π \= 2π/**A** \= 874π/35 | 78.4500565496 | C1 |
| ΣE(N\_2π) | 1/(4G₃) | C2 |
| P\_max; ∂P\_max/∂ℓ\_⊥ | c⁵/(4G₄); 0 | C3a–C3b |
| t\_tick (PP-1 ∧ PP-2) | 2t\_P | C5 |
| d/dn\[n**A**\]; d/dk\[2πk+ω\] | **A**; 2π (ω drops) | F1–F2 |
| ω/2π \= Re τ\_K | 0.3595707342 | F3 |
| ê₆ \= 2π e^{−4π**Q**} | 5.829×10⁻⁶⁰ | D4 |

Firewalled (never PASS): H\_∂/M̄\_P \= 5.9009×10⁻⁶¹ (O-1); C\_UV \= 1.244 (O-2); GW150914/bound \= 4.0×10⁻³ (O-4); √e₆ \= 5.879 meV (O-5).

**Appendix B. Deep-exploration record (condensed)**

The value-gate execution (Records 3–5 of the v1.0–v1.2 line) converged 5→3→1→0 to genuine OPEN: G-PP2b to the F-F42.36 charge-unit wall, G-PP4 to the ZS-M47 residual, both reducing to ê₆. The self-reference check refused the over-read "seam \= null energy ⇒ closed": G-PP1 is held to DERIVED-CONDITIONAL because the ZS-M46 realization is model-fixed; the γ \= √3 numerological temptation is blacklisted (guard G4). The elevation route (external PROVEN mathematics: Morinelli–Tanimoto–Wegener; Ceyhan–Faulkner; Deser–Jackiw–'t Hooft; ISO(2,1) Chern–Simons) supplies the tools T2–T3, not a new axiom. Full node-by-node records are preserved in the v1.2 archive.

**Appendix C. Dependency table**

No upstream value or status is changed by this paper (guard G6; re-audited against The Book v11.0). Consumed: ZS-M1 (z\*, PROVEN); ZS-M46 v1.5 (standard pair, **P**≥0, Borchers, Thm C; PROVEN/DERIVED-CONDITIONAL); ZS-M47 v2.0 (Parent-Factor Realization, OPEN); ZS-F38 v1.2 (Q-chain, t\*=**Q**); ZS-F40 v1.2 (terminal verdict; √2/OPS/θ₁; F-F40.6); ZS-F42 v1.9 (c\_χ; F-F42.36); ZS-F43 v1.1 (T1b, ê₆, one metric-side datum); ZS-A25 v1.6 (\[Λ̂,T̂₄\]=iℏ); ZS-A30 v2.1 (Ω\_Λ,0=83/121); ZS-A32 v1.1 (MC p=0.50%, firewalled).

**Appendix D. Provenance — the v1.0–v1.2 registration abstract (retained verbatim)**

*The following is the original registration abstract, retained unedited for provenance; its claims are superseded in framing (registration → audit) but not in content by §0.*

ZS-F40 v1.2 recorded the B3 determinant/clock mechanism programme TERMINAL and left exactly one reopening gate, F-F40.6, which demands a new axiom-level input. ZS-F43 v1.1 then proved (Theorem T1b) that any successful execution necessarily lands at the dimensionless ê₆ and requires exactly one metric-side datum. This paper does not fire the gate. It registers a candidate for that datum — a null-boundary power principle on the Z-Spin seam — in four theorems: T1 (the Planck-power/frozen-gas identity η\_Z \= 249/242 \= (1/4)c\_χω², IDENTITY/DERIVED, with the N \= 3 ⇔ dim X two-ledger classification); T2 (the CRT-4a insertion point and √2/OPS/θ₁ disjointness, DERIVED); T3 (the Deser–Jackiw–'t Hooft (2+1) transplant — general IMPORTED-PROVEN, instance DERIVED-CONDITIONAL on (H-DEF) ∧ (H-TICK) — with the saturation identity N\_2π \= 2π/**A** ↔ ΣE \= 1/4G₃ and the ℓ\_⊥-cancelling per-tick bound P\_max \= c⁵/4G); and T4 (the registered two-clause axiom, NON-CLAIM, with consequence t\_tick \= 2t\_P). v1.1 discharged G-PP1 (seam **P** \= averaged-null-energy via M46.C ∘ Morinelli–Tanimoto–Wegener ∘ Ceyhan–Faulkner; DERIVED-CONDITIONAL) and G-PP2a ((H-DEF) A-vs-ω discriminator; **A** selected uniquely; DERIVED). v1.2 executed the value gates: G-PP2b OPEN (definitional normalization → F-F42.36 wall) and G-PP4 OPEN-TERMINAL (sector-dimensional, not depth-indexed; \= ZS-M47 residual), both reducing to the same ê₆. Barrier B3 NOT closed; F-F40.6 armed, not fired; Ω\_Λ,0 \= 83/121 and U\_N untouched.

**Version History**

**v1.4 (July 2026):** Compression \+ consolidation of the audit. No theorem, gate, or verification result changed; the paper is reduced \~40% from v1.3. Changes of record: (i) the audit framing is now the whole paper, with the central result named **Theorem F45.R (Null-Power Reduction)** — the route reduces to the pre-existing ê₆ ≡ E\_len(seam) residual; (ii) the full v1.0–v1.2 registration abstract is moved from body §0.1 to **Appendix D** (provenance), restoring reading flow; (iii) body §1–§6 condensed, the three exported tools foregrounded in §2, the value-gate executions summarized in §3; (iv) the verification file is copied to **zs\_f45\_verify\_v1\_4.py** (header updated to v1.4; content identical to the v1.2 suite — 47/47 PASS \+ 12/12 guards), removing the v1.3 filename mismatch. Re-audited against The Book v11.0; no upstream value or status moved. Barrier B3 NOT closed; F-F40.6 armed, not fired; Ω\_Λ,0 \= 83/121 and U\_N untouched.

**v1.3 (July 2026):** Repositioning from "registration" to "audit"; three reusable tools foregrounded; hand-off to ZS-F46 directed. (Full v1.0–v1.2 history preserved in the v1.2 archive: v1.0 registration of AX-PP in four theorems; v1.1 discharge of G-PP1/G-PP2a; v1.2 execution of the value gates to genuine OPEN.)  
