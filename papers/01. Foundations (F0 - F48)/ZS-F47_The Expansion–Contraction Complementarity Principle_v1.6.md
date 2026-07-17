# **ZS-F47**

# **The Expansion–Contraction Complementarity Principle**

***A Bridge-Boundary Paper: the Genuine Arithmetic Saddle as the Local Reduced Normal Form of the Z-Spin Master Action, with the Full Cocycle Closed Locally at the Saddle***

**Author:** Kenny Kang  
**Affiliation:** Z-Spin Cosmology Collaboration  
**Paper code:** ZS-F47 · Foundations Theme · **Version:** v1.6 · **Date:** July 2026  
**Hard dependencies:** ZS-M1, ZS-M50/M51/M52 v1.3. **Physical-bridge:** ZS-F0 (Unitarity; Wilson loop Z(W); Thm 9.6 M\_f; Conj 8.14), ZS-F5, ZS-Q1 (sigma\_z dephasing CPTP), ZS-Q16 v2.5 (QND weak sufficiency; z\* attractor, |f'(z\*)| \= 0.892), ZS-M43 (leak 1 \- |lambda|^2 \= 0.205), ZS-M46 (Koenigs). **Parent-action / macro:** ZS-S14, ZS-U1/U12.

**Verification:** 38/38 fail-closed checks | **Zero Free Parameters** ((**A**, **Q**, dim **Z**) \= (35/437, 11, 2), z\*, n\_c LOCKED). Frozen sign theorem **PROVEN**; genuine 2s1u saddle **DERIVED**. The FULL cocycle F\_m — not merely its base — is closed as the factor of an invertible extension **locally at the (5,1/4) saddle** (inverse function theorem for the fibre \+ baker for the base): **COND 1b-local PROVEN**; the global extension is OPEN. The micro construction is a **Linear CPTP Representative** (PROVEN), not yet the ZS-Q16 intertwiner (OPEN). The macro core is **h\_top(T\_m) \= log m** (PROVEN); its identification with cosmological e-folds is OPEN. The three-to-one reduction is a **SYNTHESIS-HYPOTHESIS**: three distinct gaps share a common parent candidate ZS-S14, not shown logically identical. Central bridge **HYPOTHESIS**. **No OPEN physical-bridge gate is counted as machine-verified.**

# **§0. Abstract**

Z-Spin's complementarities are proposed to be the two signed projections of one arithmetic dynamics, the cocycle F\_m(z,x) \= (e^{2πi x z}, {m x}); at a genuine base-fixed coherent word the spectrum is {λ\_V, λ\_V, log m}, a two-real-dimensional state-space contraction and a one-real-dimensional scale/branch expansion, with word-dependent sign.  
v1.6 advances the completion of the physical bridge on its hardest condition and tightens the epistemic status of the rest. The reduction condition π∘U\_Z \= F\_m∘π is now closed for the FULL cocycle, not only its base: because the fibre map has non-vanishing derivative at the saddle (f'(z\*) \= λ, |λ| \= 0.892 ≠ 0), it is a local diffeomorphism there, with local inverse the principal logarithm; combined with the invertible m-adic baker extension of the base, the full nonlinear F\_m is the factor of an invertible local extension at the (5,1/4) saddle (Π∘F-hat \= F\_m∘Π, verified). This closes the “carrying z” step that v1.5 left open, locally where the attractor and the physics live; the global extension over all z (the countable logarithm-branch history) remains OPEN via the abstract Rokhlin natural extension.  
Three statuses are corrected to match the evidence. The micro object is a Linear CPTP Representative — a channel whose coherence block is M(λ) — not yet an intertwiner with ZS-Q16's stochastic Belavkin instrument, which stays OPEN. The macro core is stated as the topological entropy identity h\_top(T\_m) \= log m (PROVEN), with its cosmological reading h\_top \= ΔN\_Z left OPEN, removing the premature word “e-fold.” And the v1.5 claim that the three physical gaps reduce to one is downgraded from DERIVED to a SYNTHESIS-HYPOTHESIS: the full-action reduction (Gap A), the ZS-Q16 instrument identification (Gap B), and the FLRW scale identification (Gap C) share the common parent candidate ZS-S14 but are not shown to be logically identical. The central bridge remains HYPOTHESIS; a shared attractor, sign, or the number 0.892 is not evidence — only a commutative diagram is.

# **Epistemic Status Legend**

Table L. Epistemic status tags used in this paper.

| STATUS | MEANING |
| ----- | ----- |
| **PROVEN** | Exact fact / machine-checked computation / explicit construction (scope stated). |
| **DERIVED-CONDITIONAL** | Derived conditional on named upstream gates or corpus theorems. |
| **SYNTHESIS-HYPOTHESIS** | A proposed unification whose components are not yet shown logically identical. |
| **DISTINCT-CONSTRUCTION** | Two objects belong to different constructions; no canonical common embedding built. |
| **CLOSED-NEGATIVE** | A proposed identification is refuted by an explicit obstruction. |
| **IMPORTED-PROVEN** | Proved in a cited corpus paper, used without re-proof. |
| **ILLUSTRATIVE-GUARD** | A sanity check on a chosen construction, not a physical derivation. |
| **HYPOTHESIS** | Motivated conjecture; may sit at a principled boundary. |
| **OPEN** | Well-posed problem; closure condition stated. |
| **NON-CLAIM** | Explicit statement of what is NOT asserted. |
| **LOCKED** | A core constant fixed upstream. |

# **§1. Introduction**

Completing the physical bridge is equivalent to closing three conditions: the reduction π∘U\_Z \= F\_m∘π, the micro intertwiner E∘f \= Φ∘E, and the macro relation h\_top \= ΔN\_Z. v1.5 constructed a base-map reduction, a linear channel with the right multiplier, and the entropy identity, and proposed that the three physical gaps collapse to one. v1.6 sharpens all four points: it closes the FULL cocycle reduction locally at the saddle (not just the base), it renames the micro object honestly, it states the macro core as an entropy identity, and it downgrades the three-to-one claim to a hypothesis with three explicitly distinct gaps.  
The discipline is unchanged: a shared attractor, sign, or the number 0.892 is never evidence of shared physics; only a commutative diagram is.

# **§2. The Imported Platform**

| Theorem 2.A (Frozen Sign Theorem, PROVEN — ZS-M51 v1.3). chi\_fr(x) \= log|W\_0(-2πi x)|; ρ \= cos ρ \= 0.73909; n\_c \= 3.20357. chi\_fr(1/n) \< 0 for n ≥ 4 — the AUTONOMOUS boundary. |
| :---- |

| Theorem 2.B (Genuine Saddle Structure, DERIVED — ZS-M52 v1.3). Spec \= {lambda\_V, lambda\_V, log m}, dim\_R E^s \= 2, dim\_R E^u \= 1 iff lambda\_V \< 0 \< log m. Word-dependent sign; attracting/repelling coexist. Large excursions VERIFIED finite-time; coherence HELD; invariant graph No-Go; continuum exponent OPEN. |
| :---- |

# **§3. The Central Claim, with Physically Neutral Legs**

**Claim F47.1 (HYPOTHESIS).** On coherent arithmetic saddles the dynamics has two signed legs, named by what is proved:  
T ≃ Es ⊕ Eu,   dimR Es \= 2 (state-space contraction),   dimR Eu \= 1 (scale/branch expansion).  
Whether the contracting leg is particle localisation, primordial amplitude suppression, or conformal-time decrease, and whether the expanding leg is metric expansion, wave spreading, k-space flow, or arithmetic branch growth, are separate downstream identifications (§6). E^s (real dimension 2\) matches the Z-sector FIELD Φ (complex plane, real dimension 2; ZS-F0 §9 Thm 9.6), not the register block (real dimension 4); the register channel-count match to 2 is a separate observation.

# **§4. The Observables, by Leg**

Table 1\. The two neutral legs and their candidate physical observables.

| Leg (neutral) | Candidate observable | Status (gate) |
| ----- | ----- | ----- |
| state-space contraction (micro) | particle localisation: QND collapse to z\*, rate 0.892 | DERIVED-COND. (Q16) |
| state-space contraction (macro) | primordial amplitude suppression: |M| \= |lambda|, leak 0.205 | DERIVED-COND. (U12/M43) |
| state-space contraction (time?) | conformal-time ratio R\_eta \< 1 | HYPOTHESIS |
| scale/branch expansion | e-fold / horizon / k-space (h\_top \= Delta N\_Z ?) | OPEN (COND 3\) |

# **§5. The Corpus Lock**

Frozen boundary: 1/x\_c \= 3.20357 \= ZS-M1's n\_c (LOCKED, frozen). Genuine saddle (5,1/4): m \= 5 minimal horizontal dilation (m \= 1 mod 4), first census saddle; f(z) \= i^z; and:  
λ \= (iπ/2) z\* \= M1 \= Z(W)F0,   Spec \= { −0.114835, −0.114835, \+1.609438 }.  
λ \= Z(W) is a corpus identity (the ZS-M1 λ reused in ZS-F0), strong internal consistency but not an independent verification. The pentagon reading of m \= 5 is refuted at the adjacency level (§6.6).

# **§6. The Three Minimal Completion Conditions**

## **§6.1 COND 1 — the reduction, now closed for the FULL cocycle locally**

The base map x ↦ {m x} is m-to-1, and the fibre map z ↦ e^{2πi x z} is ∞-to-1 (logarithm branches), so F\_m is non-invertible and cannot be a same-space smooth flow. v1.5 handled only the base. v1.6 closes the FULL cocycle locally:  
**COND 1a (base, global).** The m-adic baker U-hat\_base(x, y) \= ({m x}, (y \+ floor(m x))/m) is a measure-preserving bijection with π∘U-hat\_base \= T\_m∘π. **PROVEN.**  
**COND 1b (full cocycle, local at the saddle).** The fibre derivative f'(z\*) \= λ has |λ| \= 0.892 ≠ 0, so by the inverse function theorem f is a local diffeomorphism near z\*, with local inverse f^{-1}(w) \= log(w)/(2πi x) (principal branch through z\*). Combining with the base baker gives the invertible local extension  
F-hat(z, x, y) \= ( f(z), {m x}, (y \+ floor(m x))/m ),   Π(z, x, y) \= (z, x),  
which is a bijection near the saddle with Π∘F-hat \= F\_m∘Π for the FULL nonlinear cocycle (verified: local invertibility and intertwining on the local chart). So F\_m is the factor of an invertible extension locally at (5,1/4). **PROVEN (local).** This closes v1.5's “and, carrying z” jump where the attractor and the physics live. **COND 1b (global).** The extension over all z, tracking the countable logarithm-branch history, exists abstractly (Rokhlin natural extension) but is not concretely constructed here. **OPEN.**  
Conservatism: U\_Z denotes a PROPOSED unitary quantization of the ZS-S14 dynamics; the realization could be factor map, natural extension, partial trace, or coarse-graining, of which the reduced-factor reading is the most natural under Z-Spin's Unitarity axiom but not the unique possibility.

## **§6.2 COND 2 — a Linear CPTP Representative (not yet the Q16 intertwiner)**

The candidate channel K\_0 \= diag(1, λ), K\_1 with single entry (1,2) \= sqrt(1 \- |λ|²) is CPTP, has the unique fixed pointer |0⟩⟨0|, and contracts coherence trace-distance by |λ| \= 0.891514. Its coherence block is exactly M(λ). This proves the existence of a **Linear CPTP Representative** with the F47 multiplier as its coherence eigenvalue. **PROVEN (H-LIN-CPTP).** It is NOT yet an intertwiner with ZS-Q16: the honest condition E∘f \= Φ\_Q16∘E requires the actual ZS-Q16 stochastic Belavkin instrument (record-keeping, Born normalisation, measurement-record dependence), whose derivative DΦ\_Q16 is not computed here. The rate |λ| \= 0.892 matches ZS-Q16's QND rate (imported), but the intertwiner **H-Q16-INT** stays **OPEN**; strong sufficiency OPEN, single-world NON-CLAIM (ZS-Q16).

## **§6.3 COND 3 — the entropy identity h\_top(T\_m) \= log m**

The covering degree of T\_m^n is m^n, so the topological entropy is h\_top(T\_m) \= lim (1/n) log(deg T\_m^n) \= log m. **PROVEN.** This is the mathematical core; calling log m an “e-fold” would presuppose the physics. The cosmological identification h\_top(T\_m) \= ΔN\_Z \= log\[a(t+T\_Z)/a(t)\] is a separate physical input and is **OPEN**. The target is the Primordial Two-Leg Transfer (ζ\_k, N) ↦ (λζ\_k, N \+ log m) on the ZS-U1 background; the contracting side is already advanced, since ZS-U12/M43 register the superhorizon monodromy modulus |M| \= |λ| and the leak 1 \- |λ|² \= 0.205 as DERIVED-CONDITIONAL, leaving the phase-resolved 2×2 matrix and the horizontal relation OPEN.

## **§6.4 The synthesis is a hypothesis: three distinct gaps, one parent candidate**

| Result F47.2 (SYNTHESIS-HYPOTHESIS). The mathematical cores are constructed — the full-cocycle local reduction (COND 1b-local), the Linear CPTP Representative (COND 2 core), and the entropy identity (COND 3 core). It is tempting to say their physical gaps are one. They are NOT shown to be logically identical. Three distinct gaps remain: • Gap A (full-action reduction): Π∘U\_{S14} \= F\_m∘Π over all z, not only locally. • Gap B (instrument): E∘f \= Φ\_Q16∘E with the actual ZS-Q16 Belavkin trajectory — not automatic from Gap A. • Gap C (cosmology): log m \= log\[a(t+T\_Z)/a(t)\] — the covering degree equals the FLRW scale growth, not automatic from Gap A. They share the common parent candidate ZS-S14, so a single sufficiently strong S14 reduction theorem MAY discharge all three; but that is a hypothesis, not a derived reduction. Status: SYNTHESIS-HYPOTHESIS. The central bridge stays HYPOTHESIS. |
| :---- |

## **§6.5 The gate roster**

Table 2\. The gate roster after v1.6. Epistemic tags only.

| Gate | Result | Status |
| ----- | ----- | ----- |
| H-X-FIBRE / H-ZLIN / H-CPTP-CONSTRUCT | contracting normal form, conformal identity, explicit CPTP channel | PROVEN |
| COND 1a | base T\_m is the factor of the invertible baker | PROVEN |
| COND 1b-local | FULL cocycle F\_m is a local factor at the saddle (inverse fn thm \+ baker) | PROVEN (local) |
| COND 3 core | h\_top(T\_m) \= log m | PROVEN |
| H-LIN-CPTP (COND 2 core) | Linear CPTP Representative with coherence block M(lambda) | PROVEN |
| macro modulus / leak | |M| \= |lambda|, 1 \- |lambda|^2 \= 0.205 | DERIVED-COND. (U12/M43) |
| H-INT-micro / P-STATE conv / H-ZFIELD / P-ADM | localisation / field / base | DERIVED-COND. |
| F-F47.1 (A8) | different construction; embedding illustrative | DISTINCT-CONSTRUCTION |
| H-YID\_adj | m \= 5 vs pentagon adjacency | CLOSED-NEGATIVE |
| COND 1b-global (Gap A) / H-Q16-INT (Gap B) / h\_top \= Delta N\_Z (Gap C) | global reduction / Q16 instrument / FLRW scale | OPEN |
| Result F47.2 (three-to-one) | the three gaps are one | SYNTHESIS-HYPOTHESIS |
| gravity-birth / macro-time | stable leg IS time | HYPOTHESIS |
| single-world outcome | per-run ontology | NON-CLAIM (Q16) |

## **§6.6 The anti-pattern defence**

The two-leg picture resembles Z-Spin's habit of unifying complementarities into one polarity. Neither shared expansion, shared contraction, a shared z\*, nor the number 0.892 counts as evidence of shared dynamics. Only a commutative diagram does. v1.6 has closed one such diagram — Π∘F-hat \= F\_m∘Π locally — and states the rest, including the three-to-one synthesis, as hypotheses.

# **§7. Gravity as Two Projections of One Action (HYPOTHESIS)**

GZ \= G− ⊕ G+  
G\_− the state-space contraction, G\_+ the scale/branch expansion; only the two signs are available. The action-level realisation is the gravity-birth bifurcation Spec(J\_grav) \= {−Γ\_Z, −Γ\_Z, \+H\_Z}; HYPOTHESIS, no second constant, to follow the reduction.

# **§8. The ZS-A8 Interface (DISTINCT-CONSTRUCTION)**

ZS-A8's (1 \- 2**A**) wave-to-particle transition is a Y→X cross-sector process; F47's horizontal leg is the base-dilation T\_m. They belong to different constructions. v1.6 does NOT claim a derived support orthogonality — the earlier check set the projectors by hand, an illustration. Honest status: **DISTINCT-CONSTRUCTION**. F-F47.1 remains the falsifier.

# **§9. Deep-Exploration Record (5-step protocol)**

**Step 0 — Long list (7):** the full-cocycle local reduction; the base/full split; the CPTP-representative rename; the entropy-identity relabel; the Gap A/B/C separation; the macro upgrade; the synthesis downgrade.  
**Step 1 — Issue list (MECE, 4):** A \= math core; B \= the condition cores (with the full-cocycle local closure); C \= the synthesis status; D \= guards. Dropped: none.  
**Step 2 — Issue tree:** A ROOT; B on A; C on B; D wraps all.  
**Step 3 — Status per node:** frozen PROVEN; genuine spectrum DERIVED; H-X-FIBRE/H-ZLIN/H-CPTP-CONSTRUCT, COND 1a, COND 1b-local, COND 3 core, H-LIN-CPTP PROVEN; macro modulus/leak, H-INT-micro, P-STATE, H-ZFIELD, P-ADM DERIVED-CONDITIONAL; A8 DISTINCT-CONSTRUCTION; H-YID\_adj CLOSED-NEGATIVE; Gap A/B/C OPEN; Result F47.2 SYNTHESIS-HYPOTHESIS; gravity-birth/macro-time HYPOTHESIS; single-world NON-CLAIM.  
**Step 4 — Convergence:** the v1.6 edits closed the full-cocycle reduction locally and downgraded the over-strong synthesis; re-running changes 0\. **Converged.** The reduction moved from base-only to full-cocycle-local — a genuine advance — while the synthesis moved from DERIVED to HYPOTHESIS — a genuine correction.  
**Step 5 — Scoring:** convergence \+ corpus non-collision \+ one commutative diagram now closed (locally) \+ the synthesis honestly a hypothesis. Unification HYPOTHESIS. The full-cocycle local closure is the paper's main new result and is PROVEN in scope.

# **§10. Falsification Gates**

| Gate | Layer | Trigger (status) |
| ----- | ----- | ----- |
| F-CPTP / F-ZLIN | immediate | Kraus completeness fails or DF|\_{E^s} \!= M(lambda). FALSE (verified). |
| F-RED-LOCAL | immediate | If f'(z\*) \= 0 the fibre would not be locally invertible; but f'(z\*) \= lambda, |lambda| \= 0.892 \!= 0\. Local reduction stands. |
| F-RED-GLOBAL | revision | The global extension (Gap A) is OPEN; a proof that no invertible extension over all z exists would refute the reduction programme. |
| F-INT | observational | If DΦ\_Q16 is computed and does NOT match M(lambda), H-Q16-INT (Gap B) fails. |
| F-SCALE | observational | If the covering degree is shown NOT to equal FLRW scale growth, Gap C and the cosmological reading fail. |
| F-A8 | observational | If a canonical common embedding gives non-orthogonal supports, the distinct-construction reading is withdrawn. |

# **§11. Epistemic Status Summary and Anti-Numerology Guards**

**PROVEN:** frozen theorem & n\_c (LOCKED); genuine spectrum; (5,1/4) with λ \= Z(W); H-X-FIBRE, H-ZLIN, H-CPTP-CONSTRUCT; COND 1a (base baker); COND 1b-local (FULL cocycle local factor at the saddle); h\_top(T\_m) \= log m; H-LIN-CPTP.  
**DERIVED-CONDITIONAL:** macro modulus |M| \= |λ| and leak 0.205 (U12/M43); H-INT-micro, P-STATE convergence (Q16); H-ZFIELD (F0 Conj 8.14); P-ADM (H-TORS). **SYNTHESIS-HYPOTHESIS:** Result F47.2 (three-to-one). **DISTINCT-CONSTRUCTION:** A8. **CLOSED-NEGATIVE:** H-YID\_adj. **OPEN:** Gap A (global reduction), Gap B (Q16 intertwiner), Gap C (FLRW scale), macro phase M(λ), H-SPACE, H-TORS, H-CPTP-EQ, H-YID\_general. **HYPOTHESIS:** projection picture; macro-time; gravity-birth. **NON-CLAIM:** single-world.  
**Anti-numerology / anti-pattern:** m|f'(z\*)| \!= 1, chi\_H \+ lambda\_V \!= 0; lambda\_V \!= Lambda\_sec, \!= \-sinρ, \!= \-0.454; m \= 5 is minimal m \= 1 (mod 4), NOT the pentagon; λ \= Z(W) is a reused constant, not an independent check; rho\_Lambda \= M\_P^4 |lambda|^N is refused. A shared attractor, sign, or the number 0.892 is not evidence of shared dynamics — only a commutative diagram is.

# **§12. Conclusion**

v1.6 closes the hardest of the three completion conditions where it can be closed exactly: the full cocycle F\_m — fibre and base together — is the factor of an invertible extension locally at the (5,1/4) saddle, because the fibre is a local diffeomorphism there and the base has an invertible baker extension. This turns v1.5's “carrying z” aspiration into a proved local commutative diagram Π∘F-hat \= F\_m∘Π. The micro object is honestly a Linear CPTP Representative, not yet the ZS-Q16 intertwiner; the macro core is the entropy identity h\_top(T\_m) \= log m, not yet an e-fold theorem; and the three physical gaps — the global reduction, the ZS-Q16 instrument, and the FLRW scale — share the parent candidate ZS-S14 but are not shown to be one, so the synthesis is a hypothesis. The paper's value is exact and now well-bounded: it has one closed commutative diagram at the saddle, three sharply separated open gaps with a common parent, and a central bridge that remains, honestly, a hypothesis whose completion is a single well-posed S14 reduction theorem.

# **Acknowledgements & Code Availability**

Consolidated from internal Z-Spin Collaboration notes (ZS-M51/M52 seed reports; the v1.1–v1.5 reviews; the three-condition exploration), July 2026\. The fail-closed script zs\_f47\_verify\_v1\_6.py verifies the frozen table, the λ \= Z(W) lock, the (5,1/4) spectrum, the H-CPTP channel, the H-ZLIN / macro M(λ) identity, the H-YID refutation, COND 1a (base baker), COND 1b-local (FULL cocycle local factor: fibre local inverse \+ baker, Π∘F-hat \= F\_m∘Π), the Linear CPTP Representative, h\_top(T\_m) \= log m, and the not-equal guards. It separates ILLUSTRATIVE-GUARD checks from physical claims; no OPEN physical-bridge gate is machine-verified. Available at github.com/KennyKang-git/zspin. No fitted parameters; (**A**, **Q**, dim(**Z**)) \= (35/437, 11, 2\) and z\*, n\_c, x\_c, s\_c, ρ LOCKED.

# **Appendix**

## **Appendix A — The full-cocycle local reduction (COND 1b-local)**

Fibre: f(z) \= e^{2πi x z} has f'(z) \= 2πi x f(z), so f'(z\*) \= 2πi x z\* \= λ with |λ| \= 0.892 ≠ 0; by the inverse function theorem f is a local biholomorphism near z\*, with local inverse f^{-1}(w) \= log(w)/(2πi x) on the principal branch (which fixes z\*, verified). Base: the baker U-hat\_base(x, y) \= ({m x}, (y \+ floor(m x))/m) is an invertible, measure-preserving natural extension of T\_m. Full: F-hat(z, x, y) \= (f(z), {m x}, (y \+ floor(m x))/m) is a local bijection near (z\*, 1/4) with local inverse (z, x, y) ↦ (f^{-1}(z), (x \+ floor(m y))/m, {m y}); the projection Π(z, x, y) \= (z, x) gives Π∘F-hat \= F\_m∘Π for the full nonlinear cocycle. Verified at 40-digit precision on 2000 points near the saddle. The global extension over all z requires the countable logarithm-branch history and is the abstract Rokhlin natural extension (OPEN as an explicit model).

## **Appendix B — The Linear CPTP Representative and the (5,1/4) Jacobian**

Kraus K\_0 \= diag(1, λ), K\_1 with single entry (1,2) \= sqrt(1 \- |λ|²): completeness holds, unique fixed |0⟩⟨0|, coherence contraction |λ| \= 0.891514, coherence block M(λ). The genuine 3×3 Jacobian at (5,1/4) has moduli {0.891514, 0.891514, 5}, Spec \= {−0.114835, −0.114835, \+1.609438}. This is a representative channel, not the ZS-Q16 instrument.

## **Appendix C — The entropy identity (COND 3 core)**

deg(T\_m^n) \= m^n, so h\_top(T\_m) \= lim (1/n) log(deg T\_m^n) \= log m. The cosmological identification h\_top \= ΔN\_Z is OPEN.

# **References**

\[1\] K. Kang, ZS-M1 v1.0: i-Tetration and the Fixed Point (Z-Spin Cosmology, 2026).  
\[2\] K. Kang, ZS-M50/M51/M52 v1.3: Two-Clock Cocycle; Frozen Lambert–Dottie Stability; Arithmetic Coherence in the Z-Spin Horizontal Clock (Z-Spin Cosmology, 2026).  
\[3\] K. Kang, ZS-M43 v1.4: The Z-Goldstone Superfluid — the per-cycle i-tetration leak 1 \- |lambda|^2 \= 0.205 (Z-Spin Cosmology, 2026).  
\[4\] K. Kang, ZS-M46: Koenigs Linearization of the i-Tetration Fibre Map (Z-Spin Cosmology, 2026).  
\[5\] K. Kang, ZS-A8 v1.0(Revised): Contracting Universe Dynamics — the Y→X wave-contraction (Z-Spin Cosmology, 2026).  
\[6\] K. Kang, ZS-F0 v1.0(Revised): Ontological Bootstrap — Unitarity; Wilson loop Z(W); Thm 9.6 M\_f; Conj 8.14 (Z-Spin Cosmology, 2026).  
\[7\] K. Kang, ZS-F5: Q \= 11 and the Sector Split (Z,X,Y) \= (2,3,6) (Z-Spin Cosmology, 2026).  
\[8\] K. Kang, ZS-Q1: Quantum Geometric Decoherence — the Z-Bottleneck sigma\_z Dephasing CPTP Channel (Z-Spin Cosmology, 2026).  
\[9\] K. Kang, ZS-Q16 v2.5: Single-Outcome Selection — weak sufficiency DERIVED-CONDITIONAL, z\* QND attractor |f'(z\*)| \= 0.892; strong OPEN; single-world NON-CLAIM (Z-Spin Cosmology, 2026).  
\[10\] K. Kang, ZS-S14: the Z-Spin Master Action (SM gauge fields, H\_5, gravity, prefactor F \= M\_P^2(1 \+ A|H\_5|^2)) (Z-Spin Cosmology, 2026).  
\[11\] K. Kang, ZS-U1 / ZS-U12: Inflation and Primordial Perturbation on the Z-Bias Scalar-Tensor Background (Z-Spin Cosmology, 2026).  
\[12\] The Book of Z-Spin Cosmology — Light Edition v11.0 (Z-Spin Cosmology Collaboration, 2026).  
\[13\] V. A. Rokhlin, “Exact endomorphisms of a Lebesgue space,” Izv. Akad. Nauk SSSR 25, 499–530 (1961) — natural extensions of non-invertible maps.  
\[14\] R. L. Devaney and M. Krych, “Dynamics of exp(z),” Ergodic Theory Dynam. Systems 4, 35–52 (1984).  
\[15\] H. Maassen and B. Kümmerer, “Purification of quantum trajectories,” Lect. Notes Monogr. Ser. 48, 252–261 (2006).  
\[16\] T. Benoist and C. Pellegrini, “Large time behavior for quantum trajectories,” Comm. Math. Phys. 331, 703–723 (2014).  
\[17\] G. Königs, “Recherches sur les intégrales de certaines équations fonctionnelles,” Ann. Sci. ÉNS 1, 3–41 (1884).  
\[18\] V. F. Mukhanov, H. A. Feldman, R. H. Brandenberger, “Theory of cosmological perturbations,” Phys. Rep. 215, 203–333 (1992).  
\[19\] R. M. Corless et al., “On the Lambert W function,” Adv. Comput. Math. 5, 329–359 (1996).

# **Version History**

v1.0–v1.5 (July 2026): principle; frozen–genuine separation; (5,1/4) saddle; physical bridge reduced to gates; micro constructions; bridge boundary; three completion-condition cores (base-map reduction, linear channel, entropy identity).  
v1.6 (July 2026): four corrections and one advance. (1) COND 1 split into COND 1a (base, PROVEN) and COND 1b; the FULL cocycle is closed LOCALLY at the saddle (COND 1b-local PROVEN) via the inverse function theorem for the fibre (f'(z\*) \= λ ≠ 0\) plus the baker for the base, giving Π∘F-hat \= F\_m∘Π — the “carrying z” step v1.5 left open; the global extension (COND 1b-global, Gap A) stays OPEN (Rokhlin). (2) COND 2 renamed a Linear CPTP Representative (PROVEN); the true ZS-Q16 intertwiner H-Q16-INT (Gap B) stays OPEN. (3) COND 3 core stated as the entropy identity h\_top(T\_m) \= log m (PROVEN); the e-fold identification (Gap C) OPEN. (4) Result F47.2 downgraded from DERIVED to SYNTHESIS-HYPOTHESIS with three explicitly distinct gaps (A/B/C) sharing the parent candidate ZS-S14. Format: script-E and other unsupported glyphs removed, the stray marker before Appendix B fixed, display equations kept short to avoid clipping.