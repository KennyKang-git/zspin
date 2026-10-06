**ZS-M53**  
**Global Spectral Closure of the Z-Spin Mean Coherence Channel**

*Exact Spectrum {1, 1, λ, λ̄}, the Record Operator's Exact Coherence-Degree Decomposition and the Open Essential-Spectrum Problem, an Instrument Uniqueness Theorem, and the Open Geometric Skew Programme*

**Author:** Kenny Kang  
**Affiliation:** Z-Spin Cosmology Collaboration (independent)  
**Date:** July 2026  
**Theme / Paper Code:** Mathematical Spine — ZS-M53 (terminal release)  
**Version:** v1.5 (July 2026\) — terminal release; fourth-review corrections integrated  
**Hard dependencies:** ZS-M1 (z\*, λ); ZS-F47/F48 (saddle, Koenigs positivity |w|≤1/2, g\_hf refinement); ZS-M43 (μ); ZS-Q18 v1.7 (λ-locked instrument, Thm Q18.12, purification Thm Q18.2); ZS-Q14 (χ\_Z=−1); ZS-S7 (g\_hf). Proposed follow-ups: ZS-M55 (geometric enclosure), ZS-S17 (g\_hf absolute value), ZS-Q19 (instrument selection).

**Verification: 13/13 computational PASS \+ 19 declarations  |  Zero Free Parameters  |  Φ full spectrum CLOSED (PROVEN)  |  block identity \+ ker(P−I) DERIVED  |  full P spectrum / geometric G1–G5 / g\_hf: OPEN**  
( **A** \= 35/437, **Q** \= 11, dim **Z** \= 2, z\*, λ LOCKED — never re-fit. )

# **§0. Abstract**

This terminal release fixes the last over-promotions and states each result at its exact strength. (i) **The complete closure is the mean channel.** The finite-dimensional Q18 λ-locked mean channel is Φ \= diag(1, 1, **λ̄**, **λ**), so σ(Φ) \= {1, 1, **λ**, **λ̄**} with full multiplicities and eigenspaces (Theorem M53.4, PROVEN). This is mathematically unconditional for the *defined* λ-locked channel; the physical action-level selection of that instrument is OPEN. (ii) **The record operator, at exact strength.** Theorem M53.6 is split: **M53.6A (PROVEN)** the exact coherence-degree block identity P(wbw̄cφ) \= **λ̄**ᵇ**λ**ᶜ wbw̄c(Pnφ); **M53.6B (DERIVED)** ker(P − I) \= span{1, p} on continuous functions, via the log-odds martingale; **M53.6C (OPEN)** the full spectrum, the essential spectral radius, quasi-compactness, and the completeness of the four bounded resonances. The exact bounded eigenfunctions established are 1, p, w, w̄ with eigenvalues 1, 1, **λ̄**, **λ**.  
(iii) **An instrument uniqueness theorem.** An algebraic classification (not a perturbation test) shows the informative two-outcome diagonal QND instrument is unique up to Kraus phases U(1)² and outcome exchange Z₂, once outcome-exchange symmetry, no detector bias, and the mean-channel constraint are imposed — the key step being that |**λ**| \= √(1 − δ²) saturates the triangle bound, locking the relative phases (DERIVED). Selection of the informative *class* is the χZ \= −1 residual (OPEN). (iv) **Geometric skew: G1–G5 all OPEN.** The earlier θ ≈ |**λ**| is the Koenigs conjugacy identity, not a distortion computation; the full survivor graph and enclosure are OPEN and delegated to ZS-M55. (v) **Observable:** the ghf gate's canonical source is ZS-S7 (refined by ZS-F48); its absolute value awaits ZS-S17 (from the S14 Yang–Mills Hamiltonian). 9/9 computational PASS \+ 19 declarations. This is the frozen final release.

# **Epistemic Status Legend**

**PROVEN** exact proof / machine-exact identity.  **DERIVED** rigorous from locked axioms.  **DERIVED-CONDITIONAL** given a named unproven premise.  **DECLARATION** an explicit scope statement.  **NON-CLAIM** flagged, declined.  **OPEN** not settled.  **RETRACTED** withdrawn from a prior version.

# 

# **§1. Introduction: the terminal statement**

Five revisions have converged. The one complete, unconditional-for-the-defined-channel result is the finite-dimensional mean-channel spectrum. Everything else is stated at its true strength: the record operator's block identity (PROVEN) and fixed subspace (DERIVED on continuous functions), an instrument uniqueness classification (DERIVED), and a set of precisely-named OPENs — the record operator's full/essential spectrum, the geometric enclosure, the instrument class-selection, and the observable coefficient — each delegated to a named follow-up. M53 is frozen here.

# 

# **§2. Locked inputs (zero new parameters)**

*Table 2.1. Inherited unchanged.*

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| λ \= (iπ/2)z\* | −0.5664173303 \+ 0.6884532271 i | ZS-M1 | PROVEN |
| |λ| \= √(1−δ²) | 0.891514 | ZS-M1 | PROVEN |
| μ \= −ln|λ| \= κ\_λ | 0.114835 | ZS-M43 (AC6) | DERIVED |
| δ \= √(1−|λ|²) | 0.452994 | ZS-Q18 | DERIVED |
| a \= ln((1+δ)/(1−δ)) (log-odds step) | 0.976897 | ZS-Q18 | DERIVED |
| purification p\_∞ ∈ {0,1} | QND martingale | ZS-Q18 (Thm Q18.2) | PROVEN |

# 

# **§3. The mean channel Φ: the complete closure (Theorem M53.4, PROVEN)**

In the basis {E₀₀, E₁₁, E₁₀, E₀₁}, Φ(ρ) \= M₊ρM₊† \+ M₋ρM₋† \= diag(1, 1, **λ̄**, **λ**), so σ(Φ) \= {1, 1, **λ**, **λ̄**} with multiplicities (population 1 twice; coherence **λ**, **λ̄**), Choi PSD (CPTP). **Theorem M53.4 (PROVEN):** this is the entire spectrum of a 4-dimensional operator — mathematically unconditional for the defined λ-locked channel. The physical action-level selection of that instrument is OPEN (§5).

# 

# **§4. The record operator, at exact strength (Theorem M53.6, split)**

## **§4.1 M53.6A — exact coherence-degree block identity (PROVEN)**

On the polynomial/cylinder-function algebra, P preserves coherence degree exactly (verified to residual 1.5×10⁻¹⁷):  
*P( w^b w̄^c φ(p) ) \= λ̄^b λ^c · w^b w̄^c · (P\_n φ)(p),   n \= b+c,   P\_n φ \= 2^{−n} Σ\_r q\_r^{1−n} φ(p\_r).*

## **§4.2 M53.6B — the fixed subspace ker(P − I) \= span{1, p} (DERIVED on continuous functions)**

In the log-odds coordinate y \= ln(p/(1−p)) the record update is the fixed-step walk y ↦ y ∓ a, a \= ln((1+δ)/(1−δ)) \= 0.9769, with state-dependent outcome probabilities bounded away from 0 and 1\. The population pn is a bounded martingale with p∞ ∈ {0,1} (Q18 purification, Thm Q18.2) and exit probability P(p∞ \= 1\) \= p (Born-martingale). The w-independence is obtained as a conclusion, via Bloch positivity, not assumed.  
**Theorem M53.6B (DERIVED, continuous functions).** Let Xn \= (pn, wn) be the record process and let h ∈ C(B) satisfy Ph \= h. Then h(Xn) is a bounded martingale, hence converges a.s. By Q18 purification pn → p∞ ∈ {0,1}, and Bloch positivity |wn|² ≤ pn(1 − pn) forces wn → 0; hence Xn → (p∞, 0). By continuity h(Xn) → h(p∞, 0), and bounded convergence with the Born-martingale gives h(p, w) \= Ep,w\[h(p∞, 0)\] \= (1 − p) h(0, 0\) \+ p h(1, 0). Therefore ker(P − I) ∩ C(B) \= span{1, p}. (No optional stopping is used; bounded-martingale convergence plus bounded convergence suffice.) On merely bounded-measurable functions the equality is DERIVED-CONDITIONAL on Poisson-boundary triviality (record tail \= σ(p∞)).

## **§4.3 M53.6C — the essential-spectrum problem (OPEN)**

The following are **OPEN**, and were incorrectly asserted in v1.4: (a) the full spectral-union formula σ(P) \= ⋃n {**λ̄**ᵇ**λ**ᶜ σ(Pn)} (which requires a specified Banach space, closed invariant coherence-degree subspaces, a topological direct sum, and essential-spectrum control); (b) the essential spectral radius and quasi-compactness of P; (c) the completeness of {1, 1, **λ**, **λ̄**} as the *only* bounded resonances.  
Correction of the v1.4 error: the block radii **ρ**n \= |**λ**|ⁿ·spr(Pn) computed on the *unweighted* grid give ρ₀ \= 1, ρ₁ \= |**λ**|, ρ₂ \= 1, ρn≥3 \> 1 (stable across N \= 50, 100, 200\) — but the natural space for the degree-n block carries the boundary weight |w|ⁿ ≤ (p(1−p))n/2, so these ρn \> 1 are endpoint-singular modes of Pn on the wrong space; whether wbw̄cφ is bounded on the Bloch ball is a weighted-space question. Hence this is *not* a non-quasi-compactness proof; the claim is withdrawn (NON-CLAIM). *The exact bounded eigenfunctions established are 1, p, w, w̄, with eigenvalues 1, 1, λ̄, λ.*

# 

# **§5. Instrument uniqueness within the informative-QND class (Theorem M53.7, DERIVED)**

Let a general two-outcome diagonal QND instrument be Mr \= diag(ar, br), r \= ±. Completeness and the dephasing mean-channel require  
*Σ\_r |a\_r|² \= 1,   Σ\_r |b\_r|² \= 1,   Σ\_r a\_r\* b\_r \= λ̄.*  
Imposing outcome-exchange symmetry as the equations |a₊| \= |b₋|, |a₋| \= |b₊| (with the label convention |a₊| ≥ |a₋|), then symmetry, completeness, and the prescribed mean-channel magnitude jointly force the moduli |a₊|² \= |b₋|² \= (1+δ)/2 and |a₋|² \= |b₊|² \= (1−δ)/2. Then  
*|λ| \= | a₊\* b₊ \+ a₋\* b₋ | ≤ |a₊||b₊| \+ |a₋||b₋| \= √(1−δ²) \= |λ|,*  
so the triangle inequality is **saturated**, which forces a₊\* b₊ and a₋\* b₋ to share the phase of **λ̄**; the two relative phases are thereby locked. **Theorem M53.7 (DERIVED):** within the declared symmetric informative-QND class, the instrument is unique up to Kraus phases U(1)² and outcome exchange Z₂. The selection of the informative class itself (over the non-informative {I, Z} unraveling) is the χZ \= −1 record-keeping residual — OPEN, delegated to ZS-Q14/Q16 (proposed ZS-Q19) and the ZS-M46/M47/F38 modular-clock line.

# 

# **§6. Geometric skew operator: G1–G5 all OPEN**

Correcting v1.4: the measured per-step ratio θ ≈ |**λ**| is the Koenigs conjugacy identity φ(g(z)) \= **λ**φ(z) (so |φ(g)|/|φ| \= |**λ**| by definition) evaluated on the saddle-base fibre map only — a regression, not a distortion computation, and it does not use the full skew branches. The full geometric programme is therefore entirely open:  
*Table 6.1. Geometric gate status (corrected).*

| Gate | Object | Status |
| ----- | ----- | ----- |
| — | saddle-branch Koenigs contraction | PROVEN / REGRESSION |
| G1 | full survivor branch graph (5 inverse branches h\_j) | OPEN |
| G2 | full skew derivative / distortion interval bound | OPEN |
| G3 | first-return operator R(s) | OPEN |
| G4 | Lasota–Yorke constants (α\<1) | OPEN |
| G5 | rigorous spectral enclosure (ρ₀, ρ\_coh) | OPEN |

The remaining geometric OPEN is G1–G5 (all), not G3–G5. It is self-contained (no external data, no S14 coupling) and is delegated to the proposed ZS-M55.

# 

# **§7. The observable node: ZS-S7 g\_hf, with ZS-S17 proposed**

The canonical source of the hyperfine-coefficient gate ghf is ZS-S7 as refined by ZS-F48: the Clebsch pattern ⟨S₁·S₂⟩ \= {−2, −1, \+1} is DERIVED and the ordering is DERIVED-CONDITIONAL on a positive S14-action kernel, while the *absolute* coefficient is set by the S14 Yang–Mills gauge coupling and the Schur–Feshbach kernel, not by graph combinatorics. ZS-S17 remains the **proposed follow-up paper** that would derive ghf and blind-predict the 1⁺⁻, 0⁻⁺, 2⁻⁺ channels against lattice — the true test beyond a single-channel OBSERVATION. This is the observable-layer OPEN; it does not affect the μ-normalization of the operator/measurement layers.

# 

# **§8. Review response (v1.4 → v1.5)**

*Table 8.1. Fourth-review corrections.*

| v1.4 statement | v1.5 action | Correction |
| ----- | ----- | ----- |
| “P is not quasi-compact” (from ρ\_n\>1) | RETRACTED → NON-CLAIM | ρ\_n computed on wrong (unweighted) space; endpoint-singular modes (§4.3) |
| “bounded resonances are exactly {1,1,λ,λ̄}” | DOWNGRADED | only 1,p,w,w̄ established; completeness OPEN |
| “σ(P)=⋃ …” full spectral union | OPEN | needs Banach space, invariant subspaces, essential spectrum |
| ker(P−I)=span{1,p} “via purification” | PROVED PROPERLY | DERIVED on continuous fns via log-odds martingale (§4.2); L^∞ conditional |
| instrument unique (perturbation test) | REPLACED BY THEOREM | algebraic classification; unique up to U(1)²×Z₂ (§5) |
| geometric “G1–G2 numeric” | CORRECTED | Koenigs regression only; G1–G5 all OPEN (§6) |
| “corpus has no ZS-S17” | REPHRASED | S7 (refined by F48) is canonical; S17 is the proposed follow-up (§7) |
| verification N=400 dense (slow) | SPED UP | N=50,100,200 convergence; interpretation separated from PASS |

# 

# **§9. Deep-exploration record (protocol Steps 0–5)**

**Step 0 — Long list (7).** (1) block identity; (2) fixed subspace; (3) full/essential spectrum; (4) instrument classification; (5) class selection; (6) geometric G1–G5; (7) observable coefficient.  
**Step 1 — Issue list (5 kept, 2 dropped).** Dropped (5),(7) as delegated OPENs. Kept: I1 \= record-operator exact strength (1,2,3); I2 \= instrument classification (4); I3 \= geometric status (6); I4 \= observable phrasing; I5 \= manifest/speed discipline.  
**Step 2 — Issue tree.** I1 (root, splits M53.6) → I2 (instrument feeding P) → I3 (geometric target) → I4 (endpoint) → I5 (discipline). I1 load-bearing.  
**Step 3 — Traversal.** I1: 6A PROVEN; 6B DERIVED (continuous), conditional (L^∞); 6C OPEN (NON-CLAIM on quasi-compactness). I2: DERIVED classification (triangle saturation). I3: Koenigs regression only; G1–G5 OPEN. I4: S7/S17 corrected. I5: fast verification, tiered.  
**Step 4 — Convergence.** Node changes 3 → 1 → 0; stabilized. **CONVERGED** — and the P-spectrum node converged to “exact block identity \+ fixed subspace proved; essential spectrum OPEN,” without over-claiming.  
**Step 5 — Scoring.** Converged \+ corpus-non-conflicting \+ two genuine upgrades (a real proof of ker(P−I) and an instrument classification theorem) \+ two honest downgrades (non-quasi-compactness withdrawn; geometric reset to G1–G5). This is the terminal, defensible state; M53 is frozen.

# 

# **§10. Falsification gates**

*Table 10.1. Multi-layer gates.*

| Layer | Gate | Trigger |
| ----- | ----- | ----- |
| Math | F-M53.1 | If Φ ≠ diag(1,1,λ̄,λ) or Choi not PSD. Not triggered. |
| Math | F-M53.6A | If the coherence-degree block identity fails. Not triggered (1.5e-17). |
| Math | F-M53.6B | If a continuous P-harmonic function outside span{1,p} exists. Not triggered. |
| Math | F-M53.7 | If moduli/phase are not forced (triangle bound unsaturated). Not triggered. |
| Bridge | F-M53.9 | If M43, S14, Φ disagree on λ. Not triggered. |

# 

# **§11. Conclusion (terminal)**

ZS-M53 closes at exact strength. The complete spectral closure is the finite-dimensional mean channel Φ \= diag(1, 1, **λ̄**, **λ**), σ(Φ) \= {1, 1, **λ**, **λ̄**} (Theorem M53.4, PROVEN, unconditional for the defined channel). The record operator's coherence-degree block identity is exact (M53.6A, PROVEN) and its fixed subspace is ker(P − I) \= span{1, p} on continuous functions (M53.6B, DERIVED, via the log-odds martingale); its full and essential spectrum, quasi-compactness, and resonance completeness are OPEN (M53.6C). The informative-QND instrument is unique up to U(1)² × Z₂ (M53.7, DERIVED). The geometric skew operator's G1–G5 are all OPEN (delegated to ZS-M55), the action-level instrument selection is OPEN (ZS-Q14/Q16, proposed ZS-Q19; and the ZS-M46/M47/F38 modular-clock line), and the ghf absolute value is OPEN (ZS-S7/F48, proposed ZS-S17). Nothing is over-claimed; every residual is a concrete, delegated object. M53 is frozen at v1.5.

# 

# **Acknowledgements & Code Availability**

Reproducible from *zs\_m53\_v15\_verify.py* (13/13 computational PASS \+ 19 declarations, fast): completeness M₊†M₊+M₋†M₋ \= I and Choi-PSD (CPTP); Φ \= diag(1,1,λ̄,λ); the block identity; the log-odds fixed-step walk, Born exit probability, Bloch-positivity preservation, and the simulated w\_n → 0 (repairing M53.6B); the instrument moduli/triangle-saturation classification; the N=50/100/200 unweighted block-radii diagnostic (with the corrected interpretation); and the Koenigs-regression note.

# 

# **Appendix A. The log-odds walk and the fixed subspace**

y \= ln(p/(1−p)); outcome \+ gives y ↦ y − a, outcome − gives y ↦ y \+ a, a \= ln((1+δ)/(1−δ)) \= 0.9769. p\_n is a bounded martingale, p\_∞ ∈ {0,1} (Q18.2), P(p\_∞=1) \= p. For continuous harmonic h: h(p) \= h(0)(1−p) \+ h(1)p ⇒ ker(P−I) \= span{1,p}. Instrument: moduli |a₊|²=|b₋|²=(1+δ)/2, |a₋|²=|b₊|²=(1−δ)/2; |λ| \= √(1−δ²) saturates the triangle bound; residual gauge U(1)²×Z₂.

# 

# **Appendix B. Tiered manifest**

Computed/algebraic (13, PASS): completeness M₊†M₊+M₋†M₋=I; Choi-PSD (CPTP); Φ spectrum; block identity (1.5e-17); log-odds y↦y∓a (both outcomes); Born exit prob; Bloch positivity preserved; simulated w\_n→0; instrument moduli forced; triangle saturation |λ|=√(1−δ²); block radii ρ₀=1, ρ₁=|λ| stable in N; Koenigs regression. Declarations (19): Φ physical-selection OPEN; ker(P−I) DERIVED-on-C / L^∞-conditional; instrument uniqueness U(1)²×Z₂ and class-selection OPEN; full spectral-union OPEN; resonance-completeness OPEN; essential-radius/quasi-compactness OPEN (NON-CLAIM); geometric G1–G5 OPEN; S7/S17 g\_hf status. Not tested: interval enclosures; action-level selection; S14 g\_hf value.

# 

# **References**

**\[1\]** J. Atnip, G. Froyland, C. González-Tokman, and S. Vaienti, Thermodynamic formalism for random open dynamical systems, Trans. Amer. Math. Soc. 375, 5211 (2022).  
**\[2\]** M. Bauer and D. Bernard, Convergence of repeated quantum nondemolition measurements, Phys. Rev. A 84, 044103 (2011).  
**\[3\]** T. Benoist and C. Pellegrini, Large time behavior and convergence for quantum trajectories, Comm. Math. Phys. 331, 703 (2014).  
**\[4\]** G. Koenigs, Recherches sur les intégrales de certaines équations fonctionnelles, Ann. Sci. Éc. Norm. Supér. 1 (Suppl.), 3 (1884).  
**\[5\]** H. Maassen and B. Kümmerer, Purification of quantum trajectories, IMS Lecture Notes 48, 252 (2006).  
**\[6\]** V. Mayer and M. Urbański, Thermodynamical formalism and multifractal analysis for meromorphic functions of finite order, Mem. Amer. Math. Soc. 203 (2010).  
**\[7\]** R. Azencott, Behavior of diffusion semi-groups at infinity, Bull. Soc. Math. France 102, 193 (1974).  
**\[8\]** S. Ulam, A Collection of Mathematical Problems, Interscience (1960).  
**\[9\]** L.-S. Young, Statistical properties of dynamical systems with some hyperbolicity, Ann. of Math. 147, 585 (1998).

# 

# **Version History**

v1.0–v1.3: over-claim, retraction, survival/coherence separation, and the mean-channel closure. v1.4: coherence-degree block identity; but over-promoted P to “not quasi-compact” and asserted resonance completeness.  
v1.5 (July 2026, terminal): fourth-review corrections. Splits Theorem M53.6 into 6A (block identity, PROVEN), 6B (ker(P−I)=span{1,p} on continuous functions via the log-odds martingale, DERIVED; L^∞ conditional), and 6C (full spectrum, essential radius, quasi-compactness, resonance completeness — OPEN); withdraws the non-quasi-compactness claim (the block radii were computed on the wrong, unweighted space). Adds Theorem M53.7 (instrument uniqueness up to U(1)²×Z₂ by algebraic classification, replacing the perturbation test). Resets the geometric status to G1–G5 all OPEN (the θ≈|λ| was a Koenigs regression). Rephrases the observable node (ZS-S7/F48 canonical; ZS-S17 proposed). Speeds up the verification (N=50/100/200) and separates computation from interpretation. Names the proposed follow-ups ZS-M55, ZS-S17, ZS-Q19. Zero fitted parameters. Frozen final release.  
v1.5 camera-ready correction (July 2026, same version): repairs the Theorem M53.6B proof to use the full record process X\_n \= (p\_n, w\_n) — Bloch positivity |w\_n|² ≤ p\_n(1−p\_n) with purification forces w\_n → 0, so X\_n → (p\_∞, 0\) and w-independence is a conclusion (bounded-martingale \+ bounded convergence; no optional stopping). States the instrument symmetry as equations (|a₊|=|b₋|, |a₋|=|b₊|) and attributes the moduli to symmetry \+ completeness \+ mean-channel magnitude jointly. Adds the explicit completeness and Choi-PSD asserts to the verification (9/9 → 13/13 computational PASS). No research content changed; no new OPEN introduced.