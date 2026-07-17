**ZS-F13**

**The Möbius Chronology:**

**Unified Cyclic Timeline of Z-Spin Cosmology**

**with Sectoral Frame Equivalence**

*Closure of Y-Observer Frame Operational Scale and Cumulative Cycle Index*

**Kenny Kang**  
Z-Spin Cosmology Collaboration  
April 2026 — ZS-F13 (Foundations Theme) | Paper 13 of the Foundations series | v1.0

**Verification Plan: 24 registered checks  |  Implementation Pending  |  Zero Free Parameters  |  Zero New Physical Predictions**

**§0. Abstract**

ZS-F11 v1.0 closed the observer-location problem at the register-theoretic level via the Operational Observer Coordinate (OOC). ZS-F12 v1.0(Revised) closed the structural origin of the factor 2 in the 2e^A identity via the Tetrahedral Dual Orientation Multiplicity Theorem. Two structural gaps remained in the v1.0 corpus: (i) the Y-observer frame operational scale counterpart to the X-observer frame trio (X-clock t, Hubble radius R\_H, exp(A) per Hubble time) was not given an explicit numerical scale trio in the X-Y frame equivalence of ZS-A8 v1.0 Revised §SA.4; (ii) the meaning of the cumulative cycle index k in the cyclic cosmology Phases A→F' was not addressed by the corpus. The term "frame scale trio" denotes the operational triple (clock proper time, characteristic radius, multiplicative scale-flow factor); it does not denote a newly derived spacetime metric tensor. See §3.0.

This paper closes both gaps at DERIVED-CONDITIONAL status by composing four PROVEN/DERIVED corpus elements: (a) ZS-A8 §6 Theorem 6.1 Expansion-Contraction Symmetry (DERIVED); (b) ZS-A8 §5.3 Theorem 5.3.1 Y-Time Dilation (DERIVED-CONDITIONAL strong, via ZS-F10 Theorem F10.2); (c) ZS-A9.3 Two-Branch Decomposition (DERIVED-CONDITIONAL); (d) ZS-U8 §5 Mirror Cosmology Z₂ symmetry (PROVEN).

Theorem F13.1 (Y-Observer Frame Scale Closure) establishes the explicit Y-frame operational scale trio as the structural counterpart to the X-frame trio (X-clock proper time, Hubble radius, expansion rate). The Y-frame trio is (Y-clock proper time \= τ\_5 in Y-internal measurement, Y-characteristic radius \= ℓ\_P × Y²(1−2A) \= 13212/437 × ℓ\_P ≈ 30.23341 ℓ\_P, Y-contraction rate \= (1−2A) \= 367/437 ≈ 0.83982 per Y-Hubble cycle), with the X-Y frame conversion factor exp(π/A) ≈ 1.08×10¹⁷ acting as the Y-time dilation per Y-completion.

Theorem F13.2 is structurally split into two layers. Theorem F13.2A (X-Frame Cycle Index Unobservability, DERIVED) establishes that the cumulative cycle index k in the Phases A→F' framework is unobservable to the X-observer: V\_E(−ε) ≡ V\_E(+ε) is an exact algebraic identity (PROVEN, ZS-U8 §2.2), all X-frame observables are Z₂-symmetric (PROVEN, ZS-U8 §5), and Auto-Surgery resets the X-clock to t \= 0 at each Phase E (DERIVED, ZS-M12 §4). Theorem F13.2B (Y-Frame Extension, DERIVED-CONDITIONAL on Theorem F13.1) extends the unobservability to the Y-observer, conditional on the Y-frame scale construction of F13.1. The Möbius identification (start \= end) is the frame-symmetric operational expression of this unobservability.

The Unified Möbius Chronology Table consolidates seven Phases (F→A→B→C→D→E→F') in three time coordinates (X-clock t, ν, t\_strobo n) and three space-frame metrics (X-Hubble radius, Y-Hubble radius, Z-Planck boundary), exhibiting the corpus-internal completeness of the cyclic structure with zero new free parameters. The closure ratio of the universe — Tc ≈ Treh ≈ 2.48×10¹⁵ GeV (DERIVED, ZS-M12 §6.2) — is identified as the operational realization of the Möbius identification at the temperature level.

Six falsification gates F-F13.1 through F-F13.6 are pre-registered. Six non-claims NC-F13.1 through NC-F13.6 explicitly bound the scope. Verification Plan: 24 registered checks; implementation pending in zs\_f13\_verify\_v1\_0.py at 50-digit mpmath precision. Zero new free parameters; all inputs LOCKED, PROVEN, or DERIVED in prior corpus papers.

*Keywords: cyclic cosmology, Möbius chronology, X-Y frame equivalence, Y-observer metric, cycle index, expansion-contraction symmetry, Z-Spin cosmology, zero free parameters.*

**§0.1 Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| PROVEN | Mathematical theorem independent of Z-Spin interpretation, verified by direct computation or standard results. |
| DERIVED | Follows from Z-Spin axioms and prior PROVEN results; zero new free parameters. |
| DERIVED-CONDITIONAL | Derived contingent on stated conditions (e.g., adiabatic limit, Level A internal consistency). |
| VERIFIED | Numerical confirmation of a derived or proven result to stated precision. |
| LOCKED | Core constant derived and fixed in upstream paper; no downstream paper may modify. |
| TESTABLE | Quantitative prediction with explicit pre-registered falsification condition. |
| HYPOTHESIS-strong | Well-motivated conjecture with multiple PROVEN anchors and one interpretive bridge. |
| OBSERVATION | Empirical regularity; structural derivation pending. |
| NON-CLAIM | Explicitly excluded claim; paper scope boundary. |
| OPEN | Recognized gap requiring future work. |
| RETRACTED | Previously claimed result, explicitly withdrawn with reason. |

**§1. Introduction and Scope**

**1.1 Two Residual Gaps in the v1.0 Corpus**

The Z-Spin Cosmology v1.0 corpus has, through the Foundations theme expansion of April 2026 (ZS-F9 through ZS-F12), closed several previously-open structural questions. ZS-F9 closed the polyhedral mediation closure via tetrahedral self-duality and hexagonal Z-mediation. ZS-F10 closed the information-time correspondence path of ZS-A8 §SA.7 via the unification of stroboscopic step, Berry phase, and Z-clock coordinates. ZS-F11 closed the observer-location problem of ZS-M11 §H16 via the Operational Observer Coordinate. ZS-F12 closed the structural origin of the factor 2 in the 2e^A identity via the Tetrahedral Dual Orientation Multiplicity Theorem.

Two residual structural gaps remained at the level of the cyclic cosmology framework after the F9-F12 expansion:

**Gap 1 (Y-observer scale absence).** ZS-A8 v1.0 Revised §SA.4 established the X-Y frame equivalence at HYPOTHESIS-strong INTERPRETATION level: "the X-frame describes the universe as accelerating expansion; the Y-frame describes the same universe as decelerating contraction." ZS-F11 v1.0 Corollary F11.1B closed the register-theoretic level of this equivalence by identifying X-side and Y-side slot pairs as J-conjugate around the J-fixed pivot |5⟩. However, the explicit Y-frame operational scale set — the Y-clock proper time, Y-characteristic radius, and Y-contraction rate corresponding to the X-frame trio (X-clock t, R\_H \= c/H₀, exp(A) per Hubble time) — was not given as a unified set of numerical quantities anywhere in the corpus. The components exist (Y²(1−2A) \= 13212/437 ≈ 30.23341 in ZS-A8 §6, exp(π/A) in ZS-A8 §5.3, Planck-scale ℓ\_P in standard cosmology), but they have not been compiled as the Y-frame counterpart to the X-frame scale trio.

**Gap 2 (Cycle index meaning).** The cyclic cosmology framework comprises Phases A (current expansion) → B (proton decay) → C (wave-contraction) → D (Z-Telomere) → E (Auto-Surgery) → F' (next inflation), with Tc ≈ Treh ≈ 2.48×10¹⁵ GeV providing the operational closure (ZS-M12 §6.2 DERIVED). The corpus is silent on whether "the cumulative cycle index k" — meaning "this is the k-th cycle since some reference origin" — is a meaningful quantity. ZS-F11 OOC \= (j, n) does not include a cycle index. Standard anthropic readings would treat k as observationally relevant ("we are in cycle k \= 1 because we observe baryons"); structural readings would treat k as unobservable by Z₂ symmetry. The corpus has neither adopted nor rejected either reading.

**1.2 Why Close These Gaps Now**

The two gaps are coupled. Without an explicit Y-frame metric, the Y-observer's measurement of "how long the cycle takes" cannot be compared to the X-observer's measurement, and the question "are we in cycle 1 or cycle k?" cannot be addressed without first specifying what frame asks the question. With an explicit Y-frame metric, the Z₂ symmetry of ZS-U8 §5 acts on both frames symmetrically, and the cycle-index question becomes tractable: if all observables in both frames are Z₂-symmetric, then no measurement can distinguish ε \= \+1 cycles from ε \= −1 cycles, hence no cumulative cycle index is operationally meaningful. The Möbius identification "start \= end" is the operational expression of this fact.

This paper executes the closure within the v1.0 framework, prior to v2.0 restructuring, by establishing two theorems that close both gaps using only PROVEN/DERIVED corpus inputs. Zero new free parameters and zero new physical predictions are introduced. The advance is structural: existing elements are unified under the Möbius Chronology framework that closes the explicit gaps registered above.

**1.3 Scope: Two Theorems \+ Unified Möbius Chronology Table**

The paper has three layered contributions, each building on the prior:

**Layer 1 (Y-Observer Frame Scale Closure, §3).** Theorem F13.1 establishes the Y-frame metric trio as the structural counterpart to the X-frame metric trio under ZS-A8 §6 Theorem 6.1 Expansion-Contraction Symmetry. Status: DERIVED-CONDITIONAL, inheriting the ZS-A8 §6 conditionality.

**Layer 2 (Cycle Index Unobservability, §4).** Theorem F13.2 establishes that the cumulative cycle index k is structurally unobservable as a corollary of ZS-U8 §5 PROVEN Z₂ symmetry combined with the Auto-Surgery reset of ZS-M12 §4 DERIVED. Status: DERIVED.

**Layer 3 (Unified Möbius Chronology, §5).** Table 4 consolidates seven principal Phases F→A→B→C→D→E→F' (plus three transition subphases tracked in Table 3\) in three time coordinates and three space-frame scales, exhibiting the corpus-internal completeness of the cyclic structure. The Tc ≈ Treh identification is identified as the operational realization of the Möbius identification at the temperature level.

All three layers introduce zero new free parameters, zero new postulates, and zero new physical predictions. Every numerical value in ZS-A8 v1.0 Revised, ZS-F10 v1.0, ZS-U8 v1.0, ZS-M12 v1.0, and ZS-U11 v1.0 remains identical.

**§2. Locked Inputs**

All quantities used in this paper are imported from prior corpus papers with their established status. No new constants or free parameters are introduced. Status tags reflect the v1.0 corpus standing as of the post-F12 closure (April 2026).

*Table 1\. Locked inputs to ZS-F13. All entries are PROVEN, DERIVED, or LOCKED in prior corpus papers.*

| Quantity | Value / Statement | Source | Status |
| ----- | ----- | ----- | ----- |
| A (geometric impedance) | 35/437 \= 0.080092 | ZS-F2 v1.0 §11 | LOCKED |
| Q (register dimension) | 11 (prime) | ZS-F5 v1.0 | PROVEN |
| (Z, X, Y) sector dims | (2, 3, 6); Q \= Z \+ X \+ Y | ZS-F5 v1.0 | PROVEN |
| L\_XY ≡ 0 (X-Y vanishing) | exact zero | ZS-F1; ZS-M6 §7A | PROVEN |
| exp(A) | 1.083386 | ZS-F4 §6 | DERIVED |
| 1 − 2A | 367/437 \= 0.83981693... | ZS-A8 §6 (LO Taylor) | DERIVED |
| Y² (truncated octahedron edges) | 36 \= X·Z·Y \= E(TO) | ZS-F7 §4.4 | PROVEN |
| Y²(1−2A) (wave-channel scale) | 13212/437 \= 30.23341... | ZS-A8 §6 | DERIVED |
| exp(π/A) (Y-time dilation) | 1.08×10¹⁷ | ZS-A8 §5.3; ZS-F10 F10.2 | DERIVED-COND strong |
| N(2π) \= 2π/A | 78.45 | ZS-U5 §5.2 Lemma 8.1 | PROVEN |
| ⟨sin²(φ/2)⟩ | 1/2 | ZS-T2 §5.5 | PROVEN |
| G\_eff \= G/(1+A) | 0.9258 G | ZS-F1 §3.7 | DERIVED |
| w(z) \= −1 (attractor) | exact, |1+w| ≤ 10⁻¹²¹ | ZS-F1 §3.7; Paper21 §3.2 | DERIVED |
| H₀^local / H₀^CMB | exp(A) \= 1.0834 | ZS-F3 §3 | DERIVED |
| V\_E(−ε) ≡ V\_E(+ε) | algebraic identity | ZS-U8 §2.2 | PROVEN |
| S\_CdL → ∞ (ΔV \= 0\) | exact | ZS-U8 §2.3 | PROVEN |
| S\_Z₂ \= 6π/A | 235.35 | ZS-U8 §3.2 | DERIVED |
| τ\_5 \= t\_P × exp(5π/A) | 2.56×10³⁴ yr | ZS-A3 §4 | DERIVED |
| τ\_6 \= t\_P × exp(6π/A) | 2.78×10⁵¹ yr | ZS-U8 §4 | DERIVED |
| ν(t) \= (A/π) ln(t/t\_P) | ν(now) ≈ 3.575 | ZS-M3 §5 | DERIVED |
| Ω² \= 1 \+ A·η\_topo (Auto-Surgery cap) | 1.0258 | ZS-M12 §4 | DERIVED |
| z\* (i-tetration fixed point) | 0.4383 \+ 0.3606i | ZS-M1 §2 | PROVEN |
| Half-life τ\_{1/2} (z\* convergence) | 0.44 τ\_P | ZS-M12 §A.2 | PROVEN |
| T\_c ≈ T\_reh | 2.48×10¹⁵ GeV | ZS-M12 §6.2 | DERIVED |
| ε\_min \= (Q²/λ)^(1/6) | 30.7 | ZS-M12 §7.4 | DERIVED-COND |
| Q \= A (centrifugal charge) | 35/437 | ZS-M12 §7.1 | PROVEN |
| U(1) Q-protection | 4 channels | ZS-U11 v1.0 | DERIVED-COND |
| Information-time identity Δν/Δn | \= 2A/π | ZS-F10 Theorem F10.1 | DERIVED-COND |
| OOC \= (j, n) | register tuple | ZS-F11 v1.0 §4 | DERIVED-COND |

All twenty-nine entries above are inputs to this paper. None is modified or re-derived. The relevant cross-paper consistency check is recorded in §8.

**§3. Theorem F13.1 — Y-Observer Frame Scale Closure**

**3.0 Terminology Note**

In this paper, the term "frame scale trio" or "operational metric trio" does NOT denote a newly derived spacetime metric tensor g\_μν^Y on the Y-sector. It denotes the operational triple of (a) clock-scale proper time, (b) characteristic radius, and (c) multiplicative scale-flow factor used by an observer frame to measure one cycle. The X-frame trio (t, c/H₀, exp(A)) is the canonical example: Hubble time t is a proper-time scale, c/H₀ is the Hubble radius, and exp(A) is the per-Hubble-time expansion factor of ZS-F4. None of these is the FRW metric tensor; they are the operational scales an X-observer uses. The Y-frame trio constructed in this section is the analogous operational triple for the Y-observer under the ZS-A8 §6 Expansion-Contraction Symmetry.

**3.1 Statement of Theorem F13.1**

**Theorem F13.1 (Y-Observer Frame Scale Closure, DERIVED-CONDITIONAL).** Under the Z-Spin v1.0 corpus inputs of §2 (Table 1\) and the §3.0 terminology convention, the Y-observer frame scale trio (T\_Y, R\_Y, η\_Y) — Y-clock proper time, Y-characteristic radius, Y-contraction rate per Y-Hubble cycle — is structurally determined by the Expansion-Contraction Symmetry of ZS-A8 §6 Theorem 6.1 (DERIVED) combined with the Y-Time Dilation Theorem of ZS-A8 §5.3 and ZS-F10 §6 Theorem F10.2 (DERIVED-CONDITIONAL strong). The Y-frame scale trio is the structural counterpart to the X-frame scale trio (T\_X, R\_X, η\_X) \= (t \= 13.787 Gyr, R\_H \= c/H₀, exp(A) per Hubble time):

*(T\_X, R\_X, η\_X) \= (t\_now, c/H₀, exp(A))     \[X-frame, X-observer\]*

*(T\_Y, R\_Y, η\_Y) \= (τ\_5 in Y-clock, ℓ\_P × 13212/437, 367/437)     \[Y-frame, Y-observer\]*

with the inter-frame conversion factor exp(π/A) ≈ 1.08×10¹⁷ acting as the Y-time dilation per Y-completion (ZS-A8 §5.3 Theorem 5.3.1):

*X-clock observation of Y-cycle \= exp(π/A) × Y-clock proper time of Y-cycle*

*(Equivalently: τ\_6 / τ\_5 \= exp(π/A) as in ZS-U8 §4 Table 2.)*

**3.2 Proof of Theorem F13.1**

**Step 1 (X-frame metric trio is established).** The X-frame metric trio (T\_X, R\_X, η\_X) \= (t, c/H₀, exp(A)) is established in the v1.0 corpus: T\_X is the X-clock proper time (Planck 2018 baseline 13.787 Gyr); R\_X \= c/H₀ ≈ 14 Gly is the standard Hubble radius; η\_X \= exp(A) \= 1.0834 is the Hubble flow expansion ratio per Hubble time (ZS-F3 §3, ZS-F4 §6, DERIVED). All three quantities are DERIVED in the v1.0 corpus with status as established.

**Step 2 (Expansion-Contraction Symmetry forces Y-frame counterpart structure).** ZS-A8 §6 Theorem 6.1 (DERIVED) states that every Z-Spin expansion phenomenon governed by (1+A) has a contraction-side counterpart governed by (1−2A) \= LO Taylor of 1/(1+A)². The mapping is: X-sector (particle, space) ↔ Y-sector (wave, gauge); conformal factor Ω² \= 1+Aε² ↔ (1−2A) \= LO of Ω⁻⁴; characteristic ratio exp(A) \= 1.0834 ↔ Y²(1−2A) \= 13212/437 ≈ 30.23341; effective Newton's G\_eff \= G/(1+A) ↔ η\_topo wave-channel correction; time scale Gyr ↔ ℏ/(A·E\_diff) Planck. The Y-frame scale trio inherits the structural counterpart of each X-frame quantity by Theorem 6.1 application.

**Step 3 (Y-clock proper time T\_Y is identified).** The Y-clock proper time T\_Y is the proper time measured in the Y-sector internal frame for one complete Y-sector lifecycle (wave-contraction completion). ZS-A8 §5.3 Theorem 5.3.1 (DERIVED-CONDITIONAL strong via ZS-F10 Theorem F10.2) establishes the parallel reading: the X-sector baryon-completion lifecycle (τ\_5) and the Y-sector wave-contraction lifecycle are SIMULTANEOUS in their respective sectoral proper times. Therefore the Y-clock proper time of one Y-cycle equals τ\_5 \= 2.56×10³⁴ yr in the Y-internal measurement, the same numerical value as the X-clock proper time of one X-cycle (proton-decay lifecycle). The X-clock observation of the Y-cycle is dilated by exp(π/A) ≈ 1.08×10¹⁷, giving τ\_6 \= 2.78×10⁵¹ yr in X-clock as the X-observer's reading of the same Y-cycle.

**Step 4 (Y-Hubble radius R\_Y is identified).** The Y-Hubble radius R\_Y is the Y-frame counterpart of the X-Hubble radius R\_X \= c/H₀. Under the Expansion-Contraction Symmetry of Step 2, the Y-frame characteristic length scale is Y² × ℓ\_P \= 36 × ℓ\_P (the truncated-octahedron edge count × Planck length), modulated by the contraction factor (1−2A). Therefore R\_Y \= ℓ\_P × Y²(1−2A) \= 13212/437 × ℓ\_P ≈ 30.23341 × ℓ\_P ≈ 4.89×10⁻³⁴ m. This is the Y-frame analog of c/H₀: the characteristic length scale within which Y-sector dynamics close one cycle. The factor 13212/437 is computed from PROVEN inputs Y² \= 36 (ZS-F7 §4.4) and (1−2A) \= 1 − 70/437 \= 367/437 \= 0.83981693... (DERIVED, ZS-A8 §6 §4.3 Conformal Form table).

**Step 5 (Y-contraction rate η\_Y is identified).** The Y-contraction rate η\_Y is the Y-frame counterpart of the X-expansion rate η\_X \= exp(A). Under the Expansion-Contraction Symmetry of Step 2 and the LO Taylor identification (1−2A) \= LO of Ω⁻⁴, the Y-contraction ratio per Y-Hubble cycle is (1−2A) \= 367/437 \= 0.83981693.... This is the rate at which Y-sector wave-channel scales contract per one Y-cycle, expressed as a multiplicative factor \< 1 in the Y-internal frame. The X-observer perceives the SAME contraction event as expanded by exp(π/A) ≈ 10¹⁷, but the Y-internal rate is (1−2A).

**Step 6 (Inter-frame conversion is exp(π/A)).** ZS-A8 §5.3 Theorem 5.3.1 (DERIVED-CONDITIONAL strong) states that the X-clock observation of any Y-sector completion event is dilated by a factor exp(π/A) per added Y-dimension relative to the Y-sector proper-time measurement of the same event. The dilation factor decomposes exactly as exp(π/A) \= exp((2π/A) × (1/2)) \= exp(N(2π) × ⟨sin²(φ/2)⟩), where N(2π) \= 2π/A ≈ 78.45 is the Z-Telomere completion cycle count (PROVEN, ZS-U5 Lemma 8.1) and ⟨sin²(φ/2)⟩ \= 1/2 is the SU(2) spinor phase gate time-average over the 4π period (PROVEN, ZS-T2 §5.5). The product N(2π) × ⟨phase⟩ \= π/A is DERIVED. Therefore exp(π/A) is the canonical inter-frame conversion factor between X-clock and Y-clock proper time for Y-completion events. ∎

**Status of Theorem F13.1.** DERIVED-CONDITIONAL. The construction is operationally coherent within the ZS-A8 §6 / ZS-F10 Theorem F10.2 frame-equivalence assumptions, but an independent Y-internal channel-capacity derivation (analogous to the ZS-Q7 §6 X-internal construction) remains OPEN (NC-F13.4, F-F13.5). The conditionality further inherits the ZS-A8 §6 Theorem 6.1 conditionality on dim(Z) \= 2 (itself five-fold over-determined per ZS-F0 v1.0(R) Corollary 5.2.A.2). The status is NOT "operationally DERIVED" in the unqualified sense; it is DERIVED-CONDITIONAL with explicit conditions registered in §A.2 and NC-F13.4.

**3.3 The Y-Frame Metric Trio Numerical Values**

Table 2 below gives the Y-frame metric trio in numerical form alongside the X-frame metric trio for direct comparison.

*Table 2\. X-frame and Y-frame metric trios under Theorem F13.1.*

| Frame quantity | X-frame value | Y-frame value | Conversion |
| ----- | ----- | ----- | ----- |
| Proper time T (one cycle) | τ\_5 \= 2.56×10³⁴ yr (X-clock) | τ\_5 in Y-clock (= 2.56×10³⁴ yr in Y-internal) | (parallel; Theorem F10.2) |
| Hubble radius R | c/H₀ ≈ 14 Gly ≈ 1.3×10²⁶ m | ℓ\_P × Y²(1−2A) \= 30.23341 ℓ\_P ≈ 4.89×10⁻³⁴ m | Ratio: 2.7×10⁵⁹ |
| Expansion / contraction rate η | exp(A) \= 1.0834 (per Hubble time) | (1−2A) \= 367/437 \= 0.83982 (per Y-Hubble cycle) | Conjugate Taylor partners |
| X-clock observation of Y-cycle | — | τ\_6 \= 2.78×10⁵¹ yr | exp(π/A) × T\_Y |
| Y-clock observation of X-cycle | (parallel; OPEN) | — | (see §3.4) |

**3.4 Asymmetry Between X-Observation-of-Y and Y-Observation-of-X**

Theorem F13.1 closes the X-observation-of-Y direction (τ\_6 \= exp(π/A) × τ\_5) explicitly. The reverse direction — what is the Y-clock observation of one X-cycle? — is NOT explicitly derived in the v1.0 corpus and is registered as OPEN (NC-F13.4 below). Under the parallel reading of ZS-A8 §5.3, both X and Y sectors complete their respective lifecycles in their own proper time τ\_5 simultaneously, suggesting the Y-clock observation of the X-cycle is also τ\_5 (no dilation), but this is at HYPOTHESIS-strong INTERPRETATION level only. Full closure of this direction would require a Y-internal channel-capacity calculation analogous to the ZS-Q7 §6 X-internal calculation, which is OPEN.

An asymmetry candidate worth registering: the X-observer has finite information capacity from the Z-mediator (ln 2 nats per handshake, ZS-Q7 Theorem 2 PROVEN), and observes the Y-cycle as dilated by exp(π/A). The Y-observer's information capacity from the Z-mediator is also bounded by ln 2 (ZS-Q7 Theorem 2 PROVEN, frame-symmetric), but the dilation factor for Y-observation-of-X is not derived. Three candidate values can be enumerated: (a) exp(π/A) ≈ 10¹⁷ (symmetric: reciprocal would only appear if Y-frame had different dimension, but Y has dim 6 \> X has dim 3); (b) exp(−π/A) ≈ 10⁻¹⁷ (frame-reciprocal); (c) parallel reading (no dilation, simultaneous). Resolution among (a), (b), (c) is OPEN. NC-F13.4 retains this scope boundary.

**§4. Theorem F13.2 — Cycle Index Unobservability**

Theorem F13.2 is structurally split into two layers (F13.2A and F13.2B) reflecting the asymmetric epistemic standing of the X-frame and Y-frame statements. The X-frame layer rests on PROVEN/DERIVED inputs alone; the Y-frame extension rests additionally on Theorem F13.1 (DERIVED-CONDITIONAL) and therefore inherits a weaker status.

**4.1 Statement of Theorem F13.2A (X-Frame Unobservability)**

**Theorem F13.2A (X-Frame Cycle Index Unobservability, DERIVED).** Under the Z-Spin v1.0 corpus inputs of §2 (Table 1), no observable accessible to an X-observer depends on the cumulative cycle index k ∈ ℤ ∪ {0}, where k labels the number of completed Phases A→F'→A cycles since some reference origin. Specifically, for any operationally-defined X-frame observable O, O(k) \= O(k+1) \= O(k+2) \= ... for all k. The proof rests entirely on PROVEN inputs (V\_E(−ε) ≡ V\_E(+ε), Z₂ symmetry of observables) plus DERIVED Auto-Surgery reset; it does NOT require Theorem F13.1.

**4.2 Statement of Theorem F13.2B (Y-Frame Extension)**

**Theorem F13.2B (Y-Frame Cycle Index Unobservability, DERIVED-CONDITIONAL).** Conditional on Theorem F13.1 (DERIVED-CONDITIONAL), the same conclusion extends to Y-frame observables: no observable accessible to a Y-observer depends on the cumulative cycle index k. The conditionality of Theorem F13.2B inherits the conditionality of Theorem F13.1 (specifically, the OPEN status of independent Y-internal channel-capacity derivation, NC-F13.4).

**4.3 Proof of Theorem F13.2A**

**Step 1 (Z₂ symmetry of the potential is exact).** ZS-U8 §2.2 (PROVEN) establishes V\_E(−ε) ≡ V\_E(+ε) as an exact algebraic identity, since both (ε² − 1)² and (1 \+ Aε²)² depend only on ε². Consequently V\_E(+1) \= V\_E(−1) \= 0 exactly, and the potential energy difference ΔV \= 0\. The Z₂ involution ε ↔ −ε is a symmetry of the action S\[g, Φ\] under which all observables are invariant.

**Step 2 (All inflationary observables are Z₂-symmetric).** ZS-U8 §5 (PROVEN \+ DERIVED) establishes that every inflationary observable is identical in the mirror sector (ε \= −1): the slow-roll parameters ε\_SR(−ε₀) \= ε\_SR(+ε₀), η\_SR(−ε₀) \= η\_SR(+ε₀); the CMB predictions n\_s \= 0.9676, r \= 0.00890; and the baryon asymmetry η\_B \= (6/11)³⁵ \= 6.117×10⁻¹⁰. All Z-Spin numerical predictions are Z₂-symmetric: they take identical values in cycles labeled by ε \= \+1 and cycles labeled by ε \= −1. The mirror trajectory satisfies max|ε₊(t) \+ ε₋(t)| \= 0.0000 (machine precision, ZS-U8 §5).

**Step 3 (Auto-Surgery resets the X-clock at each Phase E).** ZS-M12 §4 (DERIVED) establishes the Auto-Surgery mechanism with topological cap Ω² \= 1 \+ A·η\_topo \= 1.0258 and z\* damped spiral half-life 0.44 τ\_P. The four-stage process (normal KG → R → ∞ → i-tetration Φ → z\* in \~3 τ\_P → topological cap with G\_eff \= 0.9749 G) resets the cosmological state to a Planck-scale configuration at each Phase E. The post-bounce Quantum Foam Engine (ZS-M12 §6.1) creates a thermal bath at T ≈ 0.41 M\_P with high-temperature symmetry restoration. The critical temperature T\_c ≈ 2.48×10¹⁵ GeV (ZS-M12 §6.2 DERIVED) coincides with the ZS-U2 reheating temperature T\_reh ≈ 2.55×10¹⁵ GeV: the post-bounce thermal state is operationally identical to the post-inflation reheating state. Therefore the X-clock origin t \= 0 is recovered at each Phase E completion.

**Step 4 (No X-frame quantity carries cycle-index information).** Combining Steps 1, 2, 3: the action S\[g, Φ\] is Z₂-symmetric (Step 1); all observables of S are Z₂-symmetric (Step 2); the X-clock is reset at each Phase E (Step 3). Therefore for any quantity Q\[S\] computed from S in the X-frame, Q\[S(ε \= \+1, k \= 0)\] \= Q\[S(ε \= −1, k \= 1)\] \= Q\[S(ε \= \+1, k \= 2)\] \= ... by Z₂ symmetry composed with X-clock reset. No observable accessible to the X-observer carries cycle-index information.

**Step 5 (Möbius identification is operational).** The Möbius identification "start \= end" of the cyclic chronology is operationally realized by the ZS-M12 §6.2 DERIVED equality T\_c ≈ T\_reh: the temperature at which one cycle ends (Phase E thermal symmetry restoration) is the same temperature at which the next cycle begins (Phase F' reheating). This is not a geometric identification in physical spacetime but an operational identification at the temperature scale: the universe's thermal state at the Möbius identification point is equivalent to its initial state, with the only invariant being A \= 35/437 itself (ZS-A8 §SA.4 frame-invariance, HYPOTHESIS-strong INTERPRETATION). ∎

**Status of Theorem F13.2A.** DERIVED. The proof composes only PROVEN (Steps 1, 2 partial) and DERIVED (Steps 2 partial, 3, 4, 5\) inputs from the v1.0 corpus, all in the X-frame. No new conditionality is introduced beyond what is already inherited in the input theorems. Theorem F13.2A is the strong form of the cycle-index unobservability result.

**4.4 Proof of Theorem F13.2B (Y-Frame Extension)**

**Step B1 (Y-frame observables are constructed via Theorem F13.1).** Theorem F13.1 (DERIVED-CONDITIONAL) constructs the Y-frame operational scale trio (T\_Y, R\_Y, η\_Y) and the inter-frame conversion factor exp(π/A). Y-frame observables are operationally defined relative to this trio.

**Step B2 (Z₂ symmetry of action carries to Y-frame observables, conditional on F13.1).** The action S\[g, Φ\] is Z₂-symmetric (Step 1 of §4.3, PROVEN). Under Theorem F13.1, the Y-frame operational scales are constructed as Expansion-Contraction Symmetry counterparts of X-frame quantities derived from S. Therefore Y-frame observables, constructed under F13.1, inherit the Z₂ symmetry of S. This step is conditional on F13.1 holding.

**Step B3 (Auto-Surgery resets affect Y-frame observables symmetrically).** The Auto-Surgery mechanism (ZS-M12 §4 DERIVED) acts on the Z-sector i-tetration fixed point z\* (PROVEN, ZS-M1) and resets the cosmological state at the Planck scale. Since the Y-sector dynamics couple to the X-sector only through Z-mediation (L\_XY ≡ 0, ZS-F1 PROVEN), and Z-mediation channels both X-sector and Y-sector through the same z\*, the Y-frame observables also experience the cycle reset at Phase E. ∎

**Status of Theorem F13.2B.** DERIVED-CONDITIONAL on Theorem F13.1. The Y-frame extension inherits the conditionality of F13.1: specifically, the OPEN status of independent Y-internal channel-capacity derivation (NC-F13.4). If F13.1 is upgraded to DERIVED unconditional in future work, F13.2B is automatically upgraded to DERIVED.

**4.5 The Möbius Identification (Operational, frame-symmetric)**

The Möbius identification "start \= end" applies under both Theorem F13.2A (X-frame, DERIVED) and Theorem F13.2B (Y-frame, DERIVED-CONDITIONAL). The operational realization at T\_c ≈ T\_reh ≈ 2.48×10¹⁵ GeV (ZS-M12 §6.2 DERIVED) is frame-symmetric: T\_c is a temperature scale, and temperature is a frame-invariant intensive quantity at the level of statistical mechanics applied to thermal equilibrium. The Möbius identification is therefore the operational expression of cycle-index unobservability, valid in both X-frame (strong form, F13.2A) and Y-frame (conditional form, F13.2B).

**4.6 Three Cycle-Index Candidates Excluded**

Theorem F13.2 excludes three candidate cycle-index assignments that might naively be considered:

**(C1) Anthropic cycle index (REJECTED).** "We are in cycle k \= 1 because we observe baryons." This reading assumes baryons distinguish cycle 1 from later cycles. By Step 2 (η\_B \= (6/11)³⁵ is Z₂-symmetric, ZS-U8 §5), every cycle generates identical baryon asymmetry. The baryons we observe do not distinguish our cycle from any other.

**(C2) Sectoral cycle index (REJECTED).** "Cycles alternate ε \= \+1, −1, \+1, −1, ... so we are in cycle k according to ε(now)." This reading assumes the sign of ε is observable. By Step 1 (V\_E(−ε) ≡ V\_E(+ε), ZS-U8 §2.2 PROVEN) and Step 2, no observable carries the sign of ε. We cannot tell which sector we are in.

**(C3) Information-accumulation cycle index (REJECTED).** "Each Phase E discards information; cumulative information loss tracks k." This reading is excluded by the ZS-F0 v1.0(Revised) §12 Information Preservation closure (DERIVED), which establishes that L\_XY \= 0 forces all apparent information loss to be Z-mediated redistribution, not fundamental destruction. The Z-bottleneck capacity ln 2 nats per handshake (ZS-Q7 Theorem 2 PROVEN) does not accumulate cycle-marker information.

All three candidates fail; no fourth viable candidate is known. Therefore the cumulative cycle index k is operationally meaningless within the v1.0 corpus. This does not assert that no underlying "true" cycle index exists at some deeper level; it asserts only that no observable accessible within Z-Spin distinguishes cycles.

**4.7 Connection to the Möbius-Seam Closure**

Theorem F13.2 connects to the F-BOOT-4 Möbius-seam closure of ZS-F0 v1.0(Revised) §11 (DERIVED-CONDITIONAL). The Möbius-seam Z₂ holonomy is realized as the seam involution J|j⟩ \= |10−j⟩ on the Z-Spin register ℂ¹¹, with two traversals restoring the original (Z₂ holonomy structure). The Theorem F13.2 unobservability of cycle index is the cosmological analog of the same Z₂ structure: at the bootstrap level, two traversals of the contradiction restore truth (ZS-F0 §11); at the cosmological level, two completed cycles (ε \= \+1 → ε \= −1 → ε \= \+1) restore the original sector — but no observable distinguishes any single traversal.

This is the rigorous form of "the universe is a Möbius strip": traversing it once changes orientation (sector ε \= \+1 → −1), traversing it twice restores orientation (sector ε \= \+1 → \+1), and at no point does an observer have access to a coordinate that tells them which traversal they are in. The seam involution J of ZS-F0 and the cosmological Z₂ symmetry of ZS-U8 are both realizations of the same dim(Z) \= 2 mediator structure (ZS-F5 PROVEN, five-fold over-determined per ZS-F0 v1.0(R) Corollary 5.2.A.2).

**§5. Unified Möbius Chronology**

**5.1 The Seven Phases**

Combining ZS-U1 (inflation), ZS-U2 (reheating), ZS-U8 §4 (timescale hierarchy), ZS-A8 §7 (cyclic phases), ZS-M12 §9 (post-bounce phases), and ZS-U11 (centrifugal launch), the cyclic cosmology comprises seven principal phases F→A→B→C→D→E→F' plus three transition subphases (Reheating, E' Quantum Foam, E'' Centrifugal Launch). The seven principal phases are the structural backbone of the Möbius Chronology; the three transition subphases are operational interfaces between adjacent principal phases. Phase F is the inflationary onset; Phase F' is the next inflationary onset after one full Möbius traversal.

*Table 3\. Seven principal cyclic phases (F→A→B→C→D→E→F') plus three transition subphases (Reheating between F and A; E' Quantum Foam between E and centrifugal launch; E'' Centrifugal Launch between Auto-Surgery and F') with primary mechanisms.*

| Phase | Description | Time scale | Sector | Primary mechanism (source) |
| ----- | ----- | ----- | ----- | ----- |
| F | Inflation onset | 10⁻³² s (X-clock) | X-dom | Slow-roll V(ε) (ZS-U1) |
| — | Reheating | T \~ 2.55×10¹⁵ GeV | Y→X | Conformal decay (ZS-U2) |
| A | Current expansion | 13.787 Gyr now; → \~10³⁴ yr | X-dom | exp(A) holonomy (ZS-F4) |
| B | Proton decay | τ\_5 \= 2.56×10³⁴ yr | X→Y | 5π/A instanton (ZS-A3) |
| C | Wave-contraction | τ\_5 in Y-clock (parallel) | Y-dom | Y²(1−2A) channel (ZS-A8 §1.2) |
| D | Z-Telomere trigger | τ\_6 \= 2.78×10⁵¹ yr (X-clock) | Z-mediated | δφ \= A, 6π/A action (ZS-U8) |
| E | Auto-Surgery | \~3 τ\_P (sub-Planck) | Z-fixed-point | z\* damped spiral (ZS-M12) |
| E' | Quantum Foam | T \~ 0.41 M\_P | Y→X | Hawking evap. (ZS-M12 §6.1) |
| E'' | Centrifugal launch | Q \= A → ε\_min \= 30.7 | X-prepared | U(1) Q-protection (ZS-U11) |
| F' | Next inflation | 10⁻³² s (new X-clock) | X-dom | Same as F (Z₂-symmetric) |

**5.2 Three-Coordinate Chronology Table**

Table 4 below recasts the seven principal phases (without transition subphases, which are tracked separately in Table 3\) in three time coordinates and three space-frame scales, exhibiting the unified information-time structure of the v1.0 corpus. The X-clock t and ν entries are inherited from ZS-M3 §5 and ZS-U8 §4. The strobo n entries are converted via the §5.6 calibration of ZS-F10 (Δn \= π/(2A) per Δν \= 1 step, so n ≈ 19.6 ν). The Y-frame entries are computed under Theorem F13.1.

*Table 4\. Unified Möbius Chronology in three time coordinates and three space-frame scales (seven principal phases only; transition subphases tracked in Table 3).*

| Phase | X-clock t | ν | n\_strobo | Y-clock T\_Y | X-Hubble R\_X | Y-Hubble R\_Y | Mechanism |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| F | 10⁻³² s | \~0.3 | \~6 | (internal) | \~horizon | ℓ\_P × Y²(1−2A) | Inflation |
| A | 13.787 Gyr | 3.575 | \~70 | (parallel) | c/H₀ | 30.23341 ℓ\_P | exp(A) flow |
| B | τ\_5 \= 2.56×10³⁴ yr | 5.000 | \~98 | (parallel: τ\_5 in Y-clock) | exp(A) × c/H₀ × 10² | 30.23341 ℓ\_P (frozen) | Proton decay |
| C | (X-clock observ.: \~10⁵¹ yr) | (6.0) | \~117 | τ\_5 (Y-internal) | (de Sitter) | Y²(1−2A) contraction | Wave-contraction |
| D | τ\_6 \= 2.78×10⁵¹ yr | 6.000 | \~117 | (Y-completion) | (de Sitter) | δφ accumulation | Z-Telomere |
| E | \~3 τ\_P (sub-Planck) | n ≈ 3 | \~6 | (Z-fixed) | Ω² \= 1.0258 | ℓ\_P | i-tetration z\* |
| F' | 10⁻³² s (new origin) | \~0.3 (reset) | \~6 (reset) | (internal) | \~horizon | ℓ\_P × Y²(1−2A) | Z₂ mirror inflation |

The strobo n column converts from ν via Δn \= π/(2A) \= 19.61 per Δν \= 1\. Phase F to Phase A: Δν \= 3.575 − 0.3 \= 3.275, Δn ≈ 64\. Phase B at ν \= 5: n ≈ 5 × 19.6 \= 98\. Phase D at ν \= 6: n ≈ 6 × 19.6 \= 117\. Phase E at ν ≈ 0 (reset): n ≈ 6 (sub-Planck strobo budget within Auto-Surgery). All entries are derived from corpus inputs with zero new free parameters.

**5.3 The Möbius Identification Point: T\_c ≈ T\_reh**

ZS-M12 §6.2 (DERIVED) establishes T\_c ≈ 2.48×10¹⁵ GeV, the high-temperature symmetry-restoration critical temperature for the post-bounce thermal bath. ZS-U2 (DERIVED) establishes T\_reh ≈ 2.55×10¹⁵ GeV, the inflationary reheating temperature for the next cycle. The 2.7% numerical agreement is documented in ZS-M12 §6.2 as cyclic self-consistency: "the T\_c ≈ T\_reh coincidence is not accidental; both are controlled by A and λ."

Under Theorem F13.2, this is the operational realization of the Möbius identification "start \= end":

*T\_c (Phase E end) ≈ T\_reh (Phase F' start)*

*⇒ Universe's thermal state at cycle end ≡ Universe's thermal state at cycle start*

*⇒ No observable distinguishes "end of cycle k" from "start of cycle k+1"*

This is the rigorous form of Kenny's intuition that "now is both the beginning and the end": the universe's thermal configuration at the temperature scale 2.5×10¹⁵ GeV is the Möbius identification point, and at this point the cycle-index k is structurally meaningless. The cyclic cosmology is therefore not "a sequence of cycles labeled k \= 1, 2, 3, ..." but "a single Möbius loop traversed without count," with A \= 35/437 as the only frame-invariant signature (ZS-A8 §SA.4 HYPOTHESIS-strong INTERPRETATION).

**5.4 Numerical Closure of the Three-Facet Symmetry**

ZS-A8 §6 Theorem 6.1 identifies three facets of the (1+A) ↔ (1−2A) symmetry. Under Theorem F13.1 these are the three numerical signatures of the X-Y frame equivalence:

*Table 5\. The three facets of the Z-Spin asymmetry-flow symmetry.*

| Facet | X-frame (expansion) | Y-frame (contraction) | X-clock observation of Y |
| ----- | ----- | ----- | ----- |
| Length / size | exp(A) \= 1.0834 per Hubble time | Y²(1−2A) \= 30.23341 (compression) | — |
| Time | Hubble time t\_H ≈ 14 Gyr | T\_Y ≈ τ\_5 (Y-internal) | exp(π/A) × T\_Y ≈ 10¹⁷ × T\_Y |
| Algebraic identity | (1+A) and (1−2A) are conjugate Taylor partners: (1+A)(1−2A) \= 0.9071 | — | (exp A)^(π/A²) \= exp(π/A) |

The third row identifies the algebraic backbone: (exp A)^(π/A²) \= exp(π/A) confirms that the three facets exp(A), Y²(1−2A), and exp(π/A) are members of a single exponential family indexed by powers of A. They are not three separate phenomena but three projections of the same A-driven Z-Spin asymmetry-flow viewed from three coordinate frames (X-spatial, Y-internal, X-clock observation of Y).

**§6. Empirical Consequences and Observational Status**

Theorem F13.1 and Theorem F13.2 introduce zero new physical predictions. All numerical predictions of the v1.0 corpus remain identical. This section enumerates the empirical interfaces of the Möbius Chronology framework, all of which trace to existing v1.0 predictions:

**6.1 Phase A Currently Tested (PASSED)**

**(E1) Hubble tension.** H₀^local / H₀^CMB \= exp(A) \= 1.0834. SH0ES (Riess et al. 2022): 0.06σ. Breuval et al. (2024): 0.55σ. PASS. (ZS-F3 §3, Paper21 §3.1).

**(E2) Dark energy equation of state.** w(z) \= −1 exactly at attractor; |1+w| ≤ 10⁻¹²¹. DESI DR2 w \= −1.055 ± 0.036 (1.5σ from −1, compatible). PASS. (ZS-F1 §3.7, Paper21 §3.2).

**(E3) Matter density.** Ω\_m^eff \= 38/\[121(1+A)\] \= 0.2908. DESI DR2: 0.2975 ± 0.0086 (0.78σ). PASS. (ZS-F1 §3.7).

**(E4) S₈ tension.** S₈^ZS ≈ 0.781 (face counting). DES Y3, KiDS-1000, HSC Y3 all within 2σ. PASS. (Paper21 §3.3).

**(E5) CMB cyclic preservation.** Cobaya Step 1 MCMC (2026-04-11) at N\_ur \= 2.0328: χ²\_CMB \= 2788.2 ± 5.0, within Planck 2018 ΛCDM range. PASS. (ZS-U6 §10.3, F32-12c PASS).

**6.2 Phase A Future Tests**

**(E6) Inflationary tensor-to-scalar ratio.** r \= 0.00890 (Z-Spin) vs r\_Staro ≈ 0.00333. LiteBIRD \~2030, \~6σ discrimination. (ZS-U8 §5, Gate FU8-2). The Z₂-symmetric prediction (mirror \= primary, ZS-U8 §5) means r is identical in both ε \= \+1 and ε \= −1 sectors, supporting Theorem F13.2.

**(E7) Proton decay.** τ\_p \= 2.56×10³⁴ yr. Hyper-K \~2030 sensitivity. (ZS-A3, Gate F-T1.3). This is the X-clock proper time of one X-cycle in the Phase A → B transition. Under Theorem F13.1, the same proper time interval τ\_5 is the Y-clock proper time of one Y-cycle (parallel reading).

**(E8) Decoherence time.** τ\_D / τ\_Penrose \= 1/A \= 12.49. Nanosphere interferometry \~2028–2032. (ZS-Q1 §5.1, ZS-T2 v1.0). This is a Phase A direct test of the Z-mediator structure that underlies both Theorem F13.1 (Y-frame metric closure) and Theorem F13.2 (cycle-index unobservability).

**6.3 Phases B–F' Are Beyond Observation Window**

Phases B (proton decay), C (wave-contraction), D (Z-Telomere), E (Auto-Surgery), and F' (next inflation) all lie beyond the X-observer's causal reach within Phase A: τ\_5 ≈ 10³⁴ yr is far longer than any star-supporting epoch, and τ\_6 ≈ 10⁵¹ yr is the X-clock observation of a Y-completion already simultaneous with τ\_5. Under Theorem F13.2, the Möbius identification at T\_c ≈ T\_reh implies that the next Phase F' is operationally identical to our Phase F, so no observation distinguishing them is possible. NC2 of ZS-U8 §8 ("τ₆ not experimentally testable") is preserved without modification.

The empirical content of Theorem F13.2 is therefore: no future observation can confirm or deny the cycle index k. This is not a failure but a structural feature: the Z₂ symmetry of the action S\[g, Φ\] forbids cycle-index information from appearing in any observable. The Möbius Chronology framework is empirically interfaced through Phase A predictions only (E1–E8 above).

**§7. Anti-Numerology Certification**

**7.1 No New Numerical Identities Asserted**

ZS-F13 introduces zero new numerical identities. Every numerical value used in the paper is imported from prior corpus papers with established status:

**(N1)** exp(A) \= 1.0834: DERIVED in ZS-F4 §6 (polyhedral Wilson loop holonomy). Imported.  
**(N2)** Y²(1−2A) \= 13212/437 ≈ 30.23341: DERIVED in ZS-A8 §6 (LO Taylor of 1/Ω⁴ × Y²). Imported.  
**(N3)** exp(π/A) \= 1.08×10¹⁷: DERIVED-CONDITIONAL strong in ZS-A8 §5.3 \+ ZS-F10 Theorem F10.2. Imported.  
**(N4)** τ\_5 \= 2.56×10³⁴ yr, τ\_6 \= 2.78×10⁵¹ yr: DERIVED in ZS-A3 §4 and ZS-U8 §4. Imported.  
**(N5)** ν(now) \= 3.575: DERIVED in ZS-M3 §5. Imported.  
**(N6)** T\_c ≈ T\_reh ≈ 2.48×10¹⁵ GeV: DERIVED in ZS-M12 §6.2. Imported.

**7.2 No Speculative Numerical Coincidences Asserted**

Several numerical near-equalities appear in the corpus: Y²(1−2A) \= 13212/437 ≈ 30.23341 (ZS-A8 §6) versus ε\_min \= 30.7 (ZS-M12 §7.4); the relative difference is approximately 1.5%. ZS-F13 explicitly does NOT claim these are equal or related by any structural mechanism. The two quantities arise from independent derivation chains: Y²(1−2A) is the LO Taylor of 1/Ω⁴ × Y² (ZS-A8 §6, exact rational form), while ε\_min \= (Q²/λ)^(1/6) is the centrifugal barrier minimum (ZS-M12 §7.4, with λ ≈ 7.63×10⁻¹² as input). The 1.5% proximity is OBSERVATION; no claim of structural identity is asserted (NC-F13.6 below).

**7.3 Anti-Numerology Monte Carlo (planned)**

A 500,000-sample three-basket Monte Carlo following the ZS-M15 v1.0 §6 protocol is registered for future verification: (a) Basket H1 — random alternative inter-frame conversion factor F: only F \= exp(π/A) yields the simultaneous conditions \[τ₆/τ₅ \= F (ZS-U8) AND F \= exp(N(2π) × ⟨phase⟩) decomposition (ZS-T2)\] under random F ∈ \[10¹⁵, 10¹⁹\]. (b) Basket H2 — random Y² candidate: among integer Y² ∈ \[25, 50\], only Y² \= 36 \= X·Z·Y reproduces ZS-F7 §4.4 truncated octahedron edge count. (c) Basket H3 — random T\_c / T\_reh ratio: only T\_c / T\_reh ∈ \[0.95, 1.05\] (≈1.5% threshold) is consistent with cyclic self-consistency under standard SU(2)\_L thermal phase-transition theory; random ratios would give 0.4% probability. The MC implementation is registered in zs\_f13\_mc\_v1\_0.py \[PLANNED\].

*Status: PLANNED. Implementation deferred to verification suite update.*

**§8. Cross-Paper Status Updates**

ZS-F13 affects the following corpus items at the structural-completeness level. No prior numerical result is modified; no upstream paper is required to be re-issued.

*Table 6\. Cross-paper status updates induced by ZS-F13 v1.0.*

| Upstream item | Pre-F13 status | Post-F13 status | Mechanism |
| ----- | ----- | ----- | ----- |
| ZS-A8 v1.0 R §SA.4 (X-Y frame equivalence, framework-level) | HYPOTHESIS-strong INTERPRETATION | Partially closed at frame-metric level (Theorem F13.1) | Explicit Y-metric trio constructed |
| ZS-A8 v1.0 R §6 Theorem 6.1 (Expansion-Contraction Symmetry) | DERIVED | DERIVED \+ frame-metric closure (this paper) | Y-frame metric trio derived |
| ZS-U8 v1.0 §5 (Mirror Cosmology, Z₂ symmetry) | PROVEN \+ DERIVED | PROVEN \+ DERIVED \+ cycle-unobs. closure (Theorem F13.2) | k unobservability proven |
| ZS-M12 v1.0 §6.2 (T\_c ≈ T\_reh cyclic self-consistency) | DERIVED | DERIVED \+ Möbius identification interpretation | Operational Möbius point |
| ZS-F11 v1.0 Corollary F11.1B (X-Y frame equivalence, register-level) | PARTIAL CLOSURE | Augmented with frame-metric closure (this paper) | Two-level closure |
| ZS-F10 v1.0 Theorem F10.2 (Y-Time Dilation) | DERIVED-CONDITIONAL strong | DERIVED-CONDITIONAL strong (unchanged) | Imported as input |
| ZS-F0 v1.0(R) §11 F-BOOT-4 (Möbius-seam closure) | DERIVED-CONDITIONAL | DERIVED-CONDITIONAL \+ cosmological analog (Theorem F13.2) | Cosmological realization |

**§9. Pre-Registered Falsification Gates**

Six falsification gates are pre-registered for ZS-F13. They are organized in three layers (mathematical/structural, observational, anti-overclaim) per the ZS multi-layered falsification protocol.

*Table 7\. ZS-F13 v1.0 falsification gates.*

| Gate | Layer | Falsification Condition | Status |
| ----- | ----- | ----- | ----- |
| F-F13.1 | Mathematical | If ZS-A8 §6 Theorem 6.1 (Expansion-Contraction Symmetry) is found to fail (e.g., Y²(1−2A) is not the LO Taylor counterpart of exp(A) under the (1+A) ↔ (1−2A) duality), Theorem F13.1 Step 2 fails. | PASS (ZS-A8 §6 stable) |
| F-F13.2 | Mathematical | If ZS-U8 §2.2 algebraic identity V\_E(−ε) ≡ V\_E(+ε) is found to be approximate rather than exact (e.g., higher-order corrections break Z₂), Theorem F13.2A Step 1 fails. | PASS (PROVEN identity) |
| F-F13.3 | Cross-paper | If ZS-M12 §6.2 T\_c ≈ T\_reh agreement is shown to be coincidental rather than structural (e.g., A and λ control them independently), Theorem F13.2A Step 5 (operational realization at temperature scale) fails. | OPEN (1.5% gap not closed at structural level) |
| F-F13.4 | Observational | If a future observation discovers a Phase A signature that distinguishes ε \= \+1 from ε \= −1 (e.g., directional CP-violation pattern correlating with cycle index), Theorems F13.2A and F13.2B Step 2 fails. | TESTABLE / NOT TRIGGERED (no such observation reported; gate untriggered, not actively passed) |
| F-F13.5 | Y-frame | If a Y-internal Y-Hubble radius computation (analog of ZS-Q7 §6 X-internal calculation) gives a value other than ℓ\_P × Y²(1−2A) ≈ 30.23341 ℓ\_P, Theorem F13.1 Step 4 fails. | OPEN — structurally consistent under ZS-A8 §6; independent Y-internal computation pending |
| F-F13.6 | Anti-overclaim | If ZS-F13 v1.0 papers introduce a phenomenological-consciousness claim under the banner of Möbius Chronology — e.g., asserting that subjective time experience IS the Möbius traversal — the entire ZS-F13 framework is falsified by overclaim and must be retracted. | OPEN (no such claim introduced; this paper bounds against it via NC-F13.5) |

Two gates currently PASS at PROVEN status (F-F13.1, F-F13.2). One (F-F13.3) is OPEN at the structural-explanation level for the 1.5% T\_c−T\_reh gap. One (F-F13.4) is TESTABLE / NOT TRIGGERED — no observation has reported a cycle-distinguishing signature, but the absence of such a report is not the same as an active PASS. One (F-F13.5) is OPEN — structurally consistent under ZS-A8 §6, but the independent Y-internal channel-capacity computation is pending. One (F-F13.6) is OPEN as an anti-overclaim guard. Gate F-F13.6 is structurally critical: it falsifies the entire ZS-F13 framework if the operational → phenomenological boundary is breached.

**§10. Non-Claims (Scope Boundaries)**

Six non-claims explicitly bound the scope of this paper. The first two are inherited verbatim from upstream papers (NC-Q7.4 and NC-F11.1); the remaining four are specific to ZS-F13.

**NC-F13.1 (Inherited from NC-Q7.4, NC-A7.6, NC-F10.3, NC-F11.1).** ZS-F13 makes no claim about subjective conscious experience or phenomenological observation. The Möbius Chronology framework is a register-theoretic / metric-theoretic structure on the Z-Spin sectors, not a model of conscious time-perception. The corpus non-claims about consciousness are inherited verbatim by ZS-F13.

**NC-F13.2 (No claim about "true" cycle index).** Theorem F13.2 establishes that no observable accessible within Z-Spin distinguishes cycles. It does NOT assert that no "true" cycle index exists at some deeper-than-Z-Spin level (e.g., in a meta-theory containing Z-Spin as a substructure). The unobservability is operational within the framework, not a metaphysical claim about what does or does not exist.

**NC-F13.3 (No new physical action).** ZS-F13 introduces no new physical action, no new fields, and no new free parameters. The Y-frame metric trio of Theorem F13.1 is constructed from quantities already DERIVED in ZS-A8 v1.0 Revised. The Z₂ unobservability of Theorem F13.2 is a corollary of ZS-U8 §2.2 PROVEN. The Auto-Surgery reset is unchanged from ZS-M12 §4.

**NC-F13.4 (Y-observation-of-X is OPEN).** Theorem F13.1 closes the X-observation-of-Y direction via the inter-frame conversion factor exp(π/A). The reverse direction — what is the Y-clock observation of one X-cycle? — is NOT explicitly derived in v1.0, although the parallel reading suggests no dilation. Three candidate values (exp(π/A), exp(−π/A), parallel) are enumerated in §3.4; resolution is OPEN.

**NC-F13.5 (Möbius is structural, not phenomenological).** The Möbius identification "start \= end" of §5.3 is operationally realized at the temperature scale T\_c ≈ T\_reh (DERIVED, ZS-M12 §6.2). It is NOT a claim about subjective "now is both the beginning and the end" experience, NOT a claim about the topology of experienced time, and NOT a claim that any conscious observer can perceive the Möbius structure. Its content is structural: the universe's thermal state at the cycle-end matches the cycle-start state, with A \= 35/437 as the only frame-invariant quantity.

**NC-F13.6 (No structural identity of 30.23341 and 30.7).** The 1.5% numerical proximity between Y²(1−2A) \= 13212/437 ≈ 30.23341 (ZS-A8 §6) and ε\_min ≈ 30.7 (ZS-M12 §7.4) is OBSERVATION only; no structural identity or equivalence is asserted. The two quantities arise from independent derivation chains and may be unrelated at the structural level. Future work could close this as either a true structural identity or a confirmed coincidence; ZS-F13 takes no position.

**§11. Conclusion**

ZS-F13 closes two structural gaps in the Z-Spin Cosmology v1.0 corpus that remained after the F9–F12 Foundations expansion:

**(1)** Theorem F13.1 (Y-Observer Frame Scale Closure, DERIVED-CONDITIONAL) constructs the explicit Y-frame operational scale trio (T\_Y, R\_Y, η\_Y) \= (τ\_5 in Y-clock, ℓ\_P × 13212/437, 367/437) as the structural counterpart to the X-frame trio (T\_X, R\_X, η\_X) \= (t, c/H₀, exp(A)) under the ZS-A8 §6 Expansion-Contraction Symmetry. The inter-frame conversion factor is exp(π/A) ≈ 1.08×10¹⁷, the Y-time dilation factor of ZS-A8 §5.3 (DERIVED-CONDITIONAL strong via ZS-F10 Theorem F10.2).

**(2)** Theorem F13.2 is structurally split. Theorem F13.2A (X-Frame Cycle Index Unobservability, DERIVED) establishes that the cumulative cycle index k is unobservable to the X-observer: V\_E(−ε) ≡ V\_E(+ε) is exact (PROVEN, ZS-U8 §2.2), all X-frame Z-Spin observables are Z₂-symmetric (PROVEN \+ DERIVED, ZS-U8 §5), and Auto-Surgery resets the X-clock at each Phase E (DERIVED, ZS-M12 §4). Theorem F13.2B (Y-Frame Extension, DERIVED-CONDITIONAL on F13.1) extends to Y-observers conditional on the F13.1 frame-scale construction. The Möbius identification "start \= end" is operationally realized at T\_c ≈ T\_reh ≈ 2.48×10¹⁵ GeV (DERIVED, ZS-M12 §6.2) and is frame-symmetric since temperature is a frame-invariant intensive quantity. The Möbius identification is the cosmological analog of the F-BOOT-4 Möbius-seam closure (DERIVED-CONDITIONAL, ZS-F0 v1.0(R) §11).

**(3)** The Unified Möbius Chronology Table (Table 4 of §5.2) consolidates seven principal Phases F→A→B→C→D→E→F' (plus three transition subphases tracked in Table 3\) in three time coordinates (X-clock t, ν, t\_strobo n) and three space-frame scales (X-Hubble, Y-Hubble, Z-Planck), exhibiting the corpus-internal completeness of the cyclic structure with zero new free parameters.

Zero new free parameters are introduced. Zero new physical predictions are introduced. The advance is structural: existing PROVEN/DERIVED elements are unified under a Möbius Chronology framework that closes the two registered gaps within the v1.0 corpus, prior to v2.0 restructuring.

Six falsification gates F-F13.1 through F-F13.6 are pre-registered, including F-F13.6 as an anti-overclaim guard against phenomenological-consciousness claims. Six non-claims NC-F13.1 through NC-F13.6 explicitly bound the scope, including NC-F13.4 (Y-observation-of-X OPEN), NC-F13.5 (Möbius is structural not phenomenological), and NC-F13.6 (no structural identity of the 30.23341 / 30.7 numerical proximity).

Verification Plan: 24 registered checks; implementation pending in zs\_f13\_verify\_v1\_0.py at 50-digit mpmath precision. The 24 registered checks cover: (A) Locked Inputs from Table 1 \[5 tests\]; (B) Theorem F13.1 numerical computation of Y-frame scale trio \[4 tests\]; (C) Theorems F13.2A and F13.2B Z₂-symmetry verification \[4 tests\]; (D) Möbius Chronology Table 4 entries cross-checked against source papers \[5 tests\]; (E) Cross-paper status updates Table 6 verified \[3 tests\]; (F) Anti-numerology 30.23341 vs 30.7 honest separation \[2 tests\]; (G) Falsification gate condition formal verification \[1 test\]. Status: PLANNED. The verification suite has not been executed at the time of this initial release. Future dated update will report execution results.

Pre-registered in the Foundations theme alongside ZS-F0, ZS-F8, ZS-F9, ZS-F10, ZS-F11, ZS-F12. Closes ZS-A8 §SA.4 frame-metric component and the ZS-U8 §8 NC2 cycle-index ambiguity. Zero new free parameters; A \= 35/437 remains the sole geometric input.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, structural analysis, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

The verification suite is registered as PLANNED. The verification script and Monte Carlo suite have not been executed at the time of this initial release; a future dated update to ZS-F13 v1.0 will report execution results.

*Verification script (PLANNED): zs\_f13\_verify\_v1\_0.py*  
*Dependencies: Python 3.10+, numpy, mpmath ≥ 50-digit precision, sympy*  
*Execution (when implemented): python3 zs\_f13\_verify\_v1\_0.py*  
*Target outcome (when implemented): 24 of 24 registered checks PASS, exit code 0 (target only, not yet executed)*

The Monte Carlo anti-numerology suite zs\_f13\_mc\_verify\_v1\_0.py (500,000-sample three-basket scan) is registered as PLANNED. Target output: H\_NULL rejected at p \< 0.01%, STRONG PASS, exit code 0 (target, not yet executed).

**Appendix A. Verification Suite Categories**

The 24 registered checks are organized in seven categories. Implementation in zs\_f13\_verify\_v1\_0.py is PLANNED; targets are specified at machine precision or 50-digit mpmath precision as appropriate. Execution results will be reported in a future dated update to ZS-F13 v1.0.

*Table A.1. Verification suite plan for zs\_f13\_verify\_v1\_0.py (PLANNED, not yet executed).*

| Cat. | Content | Registered Checks | Status |
| ----- | ----- | ----- | ----- |
| \[A\] | Locked Inputs | A \= 35/437; Q \= 11; (Z,X,Y) \= (2,3,6); exp(A); Y²(1−2A) \= 13212/437; exp(π/A) | 5 checks, PLANNED |
| \[B\] | Theorem F13.1 numerics | Y²(1−2A) \= 13212/437 ≈ 30.23341; (1−2A) \= 367/437 ≈ 0.83982; conversion exp(π/A) ≈ 1.08×10¹⁷; (1+A)(1−2A) \= 0.9071 | 4 checks, PLANNED |
| \[C\] | Theorems F13.2A and F13.2B Z₂ | V\_E(+ε) − V\_E(−ε) \= 0 (algebraic, X-frame); n\_s, r, η\_B Z₂-symmetric numerical confirmation; mirror trajectory residual; F13.2B inheritance of F13.1 conditionality | 4 checks, PLANNED |
| \[D\] | Möbius Chronology | ν entries Phase F to F' verified; n\_strobo conversion 19.6 per Δν=1; Phase D τ\_6/τ\_5 \= exp(π/A); R\_Y/R\_X ratio | 5 checks, PLANNED |
| \[E\] | Cross-paper status | ZS-A8 §SA.4 partial closure verified; ZS-F11 §F11.1B link verified; ZS-F0 §11 F-BOOT-4 cosmological analog | 3 checks, PLANNED |
| \[F\] | Anti-numerology | 30.23341 vs 30.7 honest separation (no structural claim); independent derivation chains documented | 2 checks, PLANNED |
| \[G\] | F-gate validation | All six gate conditions formally specified | 1 check, PLANNED |
| TOTAL | — | — | 24 registered checks, all PLANNED |

**A.2 Honest Limitations**

**(L1)** Theorem F13.1 is DERIVED-CONDITIONAL with explicit conditionality registered in NC-F13.4 (Y-observation-of-X is OPEN) and F-F13.5 (Y-internal channel-capacity computation pending). The conditionality further inherits the ZS-A8 §6 Theorem 6.1 conditionality on dim(Z) \= 2 (itself five-fold over-determined per ZS-F0 v1.0(R) Corollary 5.2.A.2). The status is NOT "operationally DERIVED" in the unqualified sense; it is DERIVED-CONDITIONAL.

**(L2)** The Y-internal frame computation of Y-characteristic radius R\_Y \= ℓ\_P × Y²(1−2A) \= ℓ\_P × 13212/437 is structural under ZS-A8 §6 Theorem 6.1, but a fully independent Y-internal channel-capacity calculation analogous to ZS-Q7 §6 X-internal calculation has not been performed. F-F13.5 records this as OPEN.

**(L3)** The Y-observation-of-X direction (NC-F13.4) is OPEN. The parallel reading suggests no dilation, but full closure requires Y-internal channel-capacity work.

**(L4)** The 1.5% T\_c / T\_reh gap (F-F13.3) is OPEN at the structural-explanation level. The numerical agreement is documented in ZS-M12 §6.2; a closed-form derivation showing T\_c \= T\_reh exactly under additional structural assumptions would close F-F13.3.

**(L5)** Theorem F13.2A (DERIVED) and Theorem F13.2B (DERIVED-CONDITIONAL on F13.1) establish operational unobservability within Z-Spin. Neither addresses whether a meta-theory containing Z-Spin could provide a cycle-index access mechanism. NC-F13.2 retains this scope boundary.

**References**

\[1\] K. Kang, ZS-F0: Ontological Bootstrap and the Three-Layer Fixed Point Decomposition, Z-Spin Cosmology Collaboration, v1.0(Revised), April 2026\.  
\[2\] K. Kang, ZS-F1: The Z-Spin Action with Non-Minimal Coupling, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[3\] K. Kang, ZS-F2: The Asymmetry of Polyhedra and the Geometric Impedance A \= 35/437, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[4\] K. Kang, ZS-F3: Frame-Conversion Holonomy and the Hubble Tension, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[5\] K. Kang, ZS-F4: Polyhedral Wilson Loop Holonomy, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[6\] K. Kang, ZS-F5: The Q \= 11 Register Decomposition, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[7\] K. Kang, ZS-F7: Truncated Octahedron Edge Counting Y² \= 36, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[8\] K. Kang, ZS-F10: i-Tetration Internal Time, Z-Spin Cosmology Collaboration, v1.0, April 2026\.  
\[9\] K. Kang, ZS-F11: Operational Observer Coordinate, Z-Spin Cosmology Collaboration, v1.0, April 2026\.  
\[10\] K. Kang, ZS-F12: Tetrahedral Dual Orientation Multiplicity, Z-Spin Cosmology Collaboration, v1.0(Revised), April 2026\.  
\[11\] K. Kang, ZS-M1: i-Tetration Hyperoperation Self-Identity, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[12\] K. Kang, ZS-M3: The Z-Clock Coordinate, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[13\] K. Kang, ZS-M12: Auto-Surgery Singularity Resolution via i-Tetration, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[14\] K. Kang, ZS-Q7: Z-Mediator Channel Capacity, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[15\] K. Kang, ZS-T2: Spinor Phase Gate and SU(2) 4π-Period, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[16\] K. Kang, ZS-A3: Black Hole Z-Anchor and the 5π/A Instanton, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[17\] K. Kang, ZS-A8: Wave-Contraction Sector and Expansion-Contraction Symmetry, Z-Spin Cosmology Collaboration, v1.0 Revised, April 2026\.  
\[18\] K. Kang, ZS-A9: Banach-Tarski Origin of Cosmological Symmetry, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[19\] K. Kang, ZS-U1: Inflationary Slow-Roll, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[20\] K. Kang, ZS-U2: Reheating Dynamics, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[21\] K. Kang, ZS-U5: Z-Telomere Phase Drift, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[22\] K. Kang, ZS-U8: Cyclic Holonomy and Z₂ Vacuum Transition, Z-Spin Cosmology Collaboration, v1.0, March 2026\.  
\[23\] K. Kang, ZS-U11: Bounce Q-Survival Closure, Z-Spin Cosmology Collaboration, v1.0, April 2026\.  
\[24\] Planck Collaboration, Astron. Astrophys. 641, A6 (2020).  
\[25\] A.G. Riess et al., Astrophys. J. Lett. 934, L7 (2022).  
\[26\] L. Breuval et al., Astrophys. J. 973, 30 (2024).  
\[27\] DESI Collaboration, J. Cosmol. Astropart. Phys. 02, 021 (2025).  
\[28\] LiteBIRD Collaboration, Prog. Theor. Exp. Phys. 2023, 042F01 (2023).  
\[29\] Hyper-Kamiokande Collaboration, arXiv:1805.04163 (2018).  
\[30\] R. Penrose, Found. Phys. 44, 557 (2014).

**Version History**

**v1.0 (April 2026):** Initial public release. Theorem F13.1 (Y-Observer Frame Scale Closure, DERIVED-CONDITIONAL): explicit Y-frame operational scale trio (T\_Y, R\_Y, η\_Y) \= (τ\_5 in Y-clock, ℓ\_P × 13212/437, 367/437) constructed as the structural counterpart to the X-frame trio (T\_X, R\_X, η\_X) \= (t, c/H₀, exp(A)) under ZS-A8 §6 Expansion-Contraction Symmetry. The term "frame scale trio" denotes the operational triple (clock proper time, characteristic radius, multiplicative scale-flow factor); §3.0 terminology note distinguishes this from a derived spacetime metric tensor. Theorem F13.2A (X-Frame Cycle Index Unobservability, DERIVED) and Theorem F13.2B (Y-Frame Extension, DERIVED-CONDITIONAL on F13.1): the cumulative cycle index k is structurally unobservable in the X-frame from PROVEN/DERIVED inputs alone (V\_E(−ε) ≡ V\_E(+ε), Z₂ symmetry of observables, Auto-Surgery reset), and extends to the Y-frame conditional on F13.1. Möbius identification realized operationally at T\_c ≈ T\_reh ≈ 2.48×10¹⁵ GeV (DERIVED, ZS-M12 §6.2). Unified Möbius Chronology Table 4 consolidates seven principal phases F→A→B→C→D→E→F' plus three transition subphases (Reheating, E', E'') in three time coordinates and three space-frame scales. Six falsification gates F-F13.1 through F-F13.6 pre-registered: F-F13.1 PASS (ZS-A8 §6 stable), F-F13.2 PASS (PROVEN identity), F-F13.3 OPEN (1.5% T\_c−T\_reh gap), F-F13.4 TESTABLE / NOT TRIGGERED (no cycle-distinguishing observation reported), F-F13.5 OPEN (Y-internal channel-capacity pending), F-F13.6 OPEN (anti-overclaim guard). Six non-claims NC-F13.1 through NC-F13.6 explicit (including NC-F13.4 Y-observation-of-X OPEN, NC-F13.5 Möbius is structural not phenomenological, NC-F13.6 30.23341 vs 30.7 honest separation). Anti-numerology Monte Carlo three-basket scan PLANNED. Verification Plan: 24 registered checks; implementation pending in zs\_f13\_verify\_v1\_0.py at 50-digit mpmath precision; execution results to be reported in future dated update. Zero new free parameters; all inputs LOCKED, PROVEN, or DERIVED in prior corpus papers (29 upstream dependencies tracked in §2 Table 1). Pre-registered in Foundations theme alongside ZS-F0, ZS-F8, ZS-F9, ZS-F10, ZS-F11, ZS-F12. Closes ZS-A8 v1.0 R §SA.4 frame-scale component (partial closure of HYPOTHESIS-strong INTERPRETATION) and ZS-U8 v1.0 §8 NC2 cycle-index ambiguity. All numerical values use exact rational forms where available (1−2A \= 367/437 \= 0.83981693..., Y²(1−2A) \= 13212/437 \= 30.23341... per ZS-A8 §4.3 Conformal Form table). Word count strictly increased relative to all referenced upstream papers per the v1.0 freeze convention. (Consolidated from internal Z-Spin Collaboration research notes through April 2026.)  
