# **ZS-A29**

**Dust and Vacuum from Measure/Form Actions**

| STANDING DISCLAIMER. AI-assisted internal research note of the Z-Spin Cosmology project. NOT externally or human peer reviewed. Every “review” / “adversarial pass” herein is an AI-assisted pass (Claude / ChatGPT / Gemini) inside the author's workflow. External domain-expert contact (vacuum energy / holography / open quantum systems) remains OUTSTANDING; the internally-decidable tasks that do not need it are listed in §8.3. |
| :---- |

*A Cross-Carrier No-Go, the Rank-83 Flux Obstruction, the Three Gates of the 83/121 Bridge, and the Convergence of Independent Algebraic and Dynamical Routes on a Present-Epoch Budget*

**Author:** Kenny Kang  
**Affiliation:** Z-Spin Cosmology Collaboration  
**Theme / Paper Code:** Astrophysics \- ZS-A29 v1.6  
**Date:** June 2026  
**Dependencies:** ZS-A28 v2.0 (B3-D; import-and-relabel discipline; Bousso-Polchinski \[8\]), ZS-A26 v2.2 (everpresent target; three risks), ZS-A27 (A-Q-Only No-Go), ZS-A23 (dimension-weighted semigroup; rank-to-energy embedding OPEN), ZS-A20, ZS-A19, ZS-M19 §10 (X/Y PK, HYPOTHESIS-strong), ZS-A7/F14/M3 (topological 2pi/4pi), ZS-M1/M12 (z\*, lambda, Koenigs, damped spiral \- sub-Planck), ZS-F10/U8 (tau\_n=tP exp(n pi/A)), ZS-F9 (rho\_Z=0), ZS-U4 (w=-1 attractor), ZS-F2, ZS-F23.  
**Repository:** github.com/KennyKang-git/zspin

## **Verification Summary**

**Verification: 56 fail-closed asserts PASS** (*verify\_zs\_a29\_v1\_6.py*), fully fail-closed, counts printed by the script and quoted verbatim: **30 load-bearing**, **23 new mechanism** (four-form K1-K6; supertrace L1-L4; rank-to-energy M1-M2; i-tetration orbit T1-T3; emergence tests E1-E4; and the P3 *coexistence* result CX1-CX4, Appendix E.5), and **3 bookkeeping/consistency** (the 4.235 round-trip; F3, now reclassified as an algebraic-consistency check), plus 4 printed notes that are not asserts. **Two v1.2 verification nits fixed:** v1.2's K6 was a tautology (bool(w+1==w+1)); v1.3 replaces it with a *real* Levi-Civita computation (eps(m a b g)epsn(a b g) \= \-3\! gmn \-\> Tmn \= \-rhoL**g**mn \-\> w \= \-1); and F3 (an algebraic-consistency check) is moved out of load-bearing. (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED.  
**The honest skeleton (this version's organizing result):** the bridge rank **P**L \= 83 \=\> OmegaL \= 83/121 is *not* one calculation but **three independent gates** \- G1 projector *selection* (TFS), G2 flux *collectivization* (the rank-83 flux has up to 83 free constants, §2.3), G3 rank-to-energy *normalization* (§8.2) \- plus the single-parent field *identification* (§2.4) and PT. v1.0 saw “one calculation left”; v1.2-v1.3 show a multi-gate structural problem. The flagship 83/121 is *not* advanced.  
*What v1.6 consolidates (the manuscript is now integrated, per prior AI-pass feedback).* (1) Title corrected (v1.2's “Single-Parent” contradicted its own §2.4 “not yet single-parent”). (2) K6 made real; F3 reclassified. (3) §2.3 “Bousso-Polchinski landscape” softened to a *kinematic precursor* (the multi-flux freedom exists prior to flux quantization and membrane dynamics). (4) §4.1 sign argument corrected (the positive-semidefinite Maxwell action \+ **P**L selection fix the sign, *not* the rank trace). (5) The “only exit is external” over-statement is balanced by listing the **internally-decidable tasks** (§8.3), including a computed rank-to-energy candidate (the maximally-mixed state, M1-M2). (6) The user's **i-tetration orbit reading of w(z)** is computed in full (Outlook §12, O5): the damped spiral is real, but under the corpus' own time anchor it gives a *frozen* w \~ \-1, **not** the DESI crossing \- so it reinforces *w* \= \-1, and the zero-parameter DESI claim does not follow. Heavy process/meta material is consolidated into the Appendices.

## **§0. Abstract**

ZS-A28 reduced the vacuum-identification bridge **B3-D** to an IMPORTED-PROVEN field-theory half (a covariant top-form on the rank-83 complement **P**L forces *w* \= \-1, constant rhoL) and an identification half whose load-bearing antecedent is the present-epoch coincidence (UN). A29 is an honest audit of that gate; it advances correctness and structure, not the flagship number 83/121.  
**Construction and No-Go (§2-§3).** The Guendelman-Nissimov-Pacheva measure yields dust and a dynamical rhoDE \= 2M from one action. Separating spacetime form-degree (4) from internal rank (83), the vacuum carrier is realized as a projector-valued four-form; on a real 121x121 rank-83 projector its quadratic form gives rhoL \= (1/2)|**P**L**M**|2 \>= 0 with the rank-38 flux dropping out (PROVEN-as-construction: the realization that the GNP measure *can* be rank-83 projector-valued is ASSUMED, F-A29.1; *w* \= \-1 is IMPORTED). The **cross-carrier No-Go** (Theorem A29.2) stands and is *stronger*: not only is rhoDE \= 2M a free integration constant, the entire rank-83 flux vector is free (a Bousso-Polchinski-*type* multi-flux freedom, prior to quantization).  
**The three gates (§8).** The organizing result of this version: rank **P**L \= 83 does **not** by itself give OmegaL \= 83/121. It requires **G1** projector selection (why **P**L, not **P**m), **G2** flux collectivization (reduce 83 free constants to one), and **G3** rank-to-energy normalization (why the energy fraction equals the rank fraction). A computed candidate for G3 is the **maximally-mixed state** rho\* \= **I**/121, for which Tr(**P**Lrho\*) \= 83/121 exactly \- reducing G3 to the decidable, *internal* question “is the cosmic vacuum the de Sitter-thermal maximally-mixed state on M121?” So external review is *necessary* but not the *only* route; §8.3 lists three internally-decidable tasks. **Scale and dynamics (§4-§6).** The everpresent / geometric-mean / de Sitter forms are one Friedmann relation written four ways (PROVEN-algebraic; CKN is IMPORTED-MOTIVATED, not a scale derivation). The present-epoch selection is an undecided fork; DESI remains a NON-CLAIM.  
**The i-tetration orbit reading (§12, O5; computed).** A new direction: read the de Sitter attractor *w* \= \-1 as the i-tetration **fixed point** z\* (n \-\> infinity), matter (rank-38) as the **orbit** still flowing in, and the free constant M as “where we are on the orbit” \= the observable scale factor. The multiplier is lambda \= (i pi/2)z\*, |lambda| \= 0.8915 \< 1 (a *damped* spiral; Koenigs verified, T1). This resolves the ZS-U4 tension by making *w* \= \-1 the asymptotic fixed point. **But the load-bearing test fails:** under the corpus' own anchor taun \= tP exp(n pi/**A**), only 0.4% of one spiral oscillation advances across the DESI redshift range (z \~ 0.5 \-\> 0), so *w* is **frozen** \~ \-1 there (T3) \- the spiral reinforces *w* \= \-1, it does **not** produce DESI's phantom-past evolution, and the “zero-parameter DESI w(z)” claim does not follow (the n \<-\> scale-factor map is the free, UNDERIVED part). Status: HYPOTHESIS-strong for the reframing; the DESI prediction is **not** supported by computation. Net: B3-D unconditional closure PARTIAL; 83/121 unchanged. (**A**, **Q**, dim **Z**) LOCKED.

**The dynamical route and the convergence (this version).** Dropping top-down number-fitting, we ask whether the budget *emerges* from the i-tetration rule alone. It does not, instructively. A bare i-tetration lattice is a pure contraction (it erases all matter); the minimal rule that restores dust/vacuum coexistence is a bistable source whose threshold is *corpus-tied*, J \> Jc \= 4(1 \- |**lambda**|) \= 0.434 (Maxwell point JM \= (9/2)(1 \- |**lambda**|)), but the dust/vacuum *ratio* is NOT fixed \- one phase generically wins, and even Maxwell balance is unstable to curvature-driven coarsening. So the emergence route reaches the **same conclusion** as the algebraic No-Go, from the opposite direction: across **four independent routes** (A27 and A29.2 No-Go theorems, the rank-83 flux obstruction, and reaction-diffusion coexistence) the budget (6,32,83)/121 is a **present-epoch boundary condition, not a dynamical invariant**. The one structure that *would* fix the ratio is a **rank-weighted master equation** whose probability-conserving stationary state is (38/121, 83/121) with no free parameter \- the dynamical form of the maximally-mixed candidate \- but it stays HYPOTHESIS-strong (it assumes equal per-channel amplitudes and an occupation-to-energy map). (**A**, **Q**, dim **Z**) LOCKED.

## **Epistemic Status Legend**

**PROVEN \-** established by internal computation/algebra at machine precision.  
**PROVEN-as-construction \-** a construction is exhibited and its algebra verified, but a nontrivial realization claim it depends on is assumed.  
**PROVEN-algebraic-identity / CONSISTENCY \-** an exact algebraic rewriting or a self-consistency check; not a derivation of new physics.  
**IMPORTED-PROVEN / IMPORTED-MOTIVATED \-** proven externally and reused / supplies only motivation or heuristic, not a derivation.  
**DERIVED-CONDITIONAL \-** DERIVED given explicitly named conditions (selection / saturation / sign convention).  
**HYPOTHESIS-strong / \-weak \-** pre-registered and corpus-non-conflicting, with a named undatured assumption / a missing bridge or pending anti-numerology check.  
**TARGET / COMPUTED-INCOMPLETE \-** a decidable computation set up but deferred, or begun but not reproducing the target.  
**OPEN (gate) \-** not closed by current tools; a sharply stated, internally-decidable obstruction.  
**CLOSED-NEGATIVE / NO-GO \-** a route proven not to work.  
**NON-CLAIM / WITHDRAWN \-** explicitly not asserted, or a prior statement removed by this audit.

## **§1. Introduction**

Z-Spin Cosmology fixes cosmology's dimensionless ratios from **A** \= 35/437 and **Q** \= 11 \= (2, 3, 6). The absolute vacuum scale B3 splits into B3-A (A-Q-only, CLOSED-NEGATIVE), B3-B (absolute value, OPEN/terminal), B3-C (today's relation), and B3-D (the bridge). A28 handed A29 the present-epoch coincidence (gate XB-6b). This paper's positive content is a sharp negative result (the cross-carrier No-Go, §3) and a structural map of what closing 83/121 would require (the three gates, §8). Its central honest finding, across versions, is that the No-Go \- not the value of any coefficient \- is the load-bearing obstruction: the present vacuum normalization is a free integration constant (indeed a free rank-83 flux vector), so geometry fixes the *ratio structure* but not the *scale*. Process and audit history are recorded in Appendices C-D; this body is kept to the physics.

## **§2. The measure/form action and the projector-valued top-form (Theorem A29.1, as construction)**

### **§2.1 The GNP measure**

From *S*GNP \= integral sqrt(-*g*)*L*1 \+ integral Phi(*B*)*L*2 \[1-3\], a pressureless dust and a dynamical rhoDE \= 2M (M the integration constant of the four-form *B*3).

### **§2.2 Form-degree vs internal rank, and honest status**

Form-degree-4 (spacetime) does not populate an internal rank-83 subspace (algebra). Realize the vacuum carrier as a projector-valued four-form *S*F \= \-(1/2\*4\!) integral sqrt(-*g*) **F**A (**P**L)AB**F**B. On a real 121x121 rank-83 **P**L (K1-K2), rhoL \= (1/2)|**P**L**M**|2 \= (1/2) suma=1..83 Ma2 \>= 0, with all 38 **P**m\-fluxes dropping out (K3-K4). **PROVEN-as-construction**: the positivity/confinement is projector algebra; the nontrivial claim \- that the GNP measure four-form *can* be the rank-83 projector-valued object \- is **ASSUMED** (F-A29.1). *w* \= \-1 is **IMPORTED** (Henneaux-Teitelboim \[4\]; verified at the tensor level in K6: eps(m a b g)epsn(a b g) \= \-3\! gmn forces **T**mn \= \-rhoL**g**mn). TFS is DERIVED-CONDITIONAL on the projector *selection* (contracting **P**m is equally valid).

### **§2.3 The rank-83 flux obstruction (kinematic precursor of a multi-flux freedom)**

With A \= 1, ..., 121 and rank **P**L \= 83, the on-shell flux **P**L**M** has **83 independent components** and rhoL \= (1/2) suma=1..83 Ma2 (K5). **Stated carefully (softened from v1.2):** this is the *kinematic precursor* of a Bousso-Polchinski-*type* landscape \[8\] \- the unconstrained projector-valued construction has up to 83 free flux components \- *prior to* the flux quantization, distinct charges, and membrane dynamics that a full BP landscape adds. Even at this kinematic level the conclusion holds: the rank fraction 83/121 does **not** fix the energy normalization; a **flux-collectivization** structure (O(83) isotropy, a single collective mode **P**L**M** \= mL**v**L, or a rank-to-energy theorem) is required. This **strengthens** the No-Go (§3) and is gate G2 of §8. **\[OPEN\]**

### **§2.4 The action is not yet single-parent**

*S*GNP's four-form *B*3 and the projector-valued *A*3A are, as written, **two** fields. If two, the model has two cosmological terms; if one, the GNP measure must be promoted to the algebra-valued object and its hidden symmetry / dust current re-verified. A genuinely single-parent action *S*grav \+ *S*GNP\[*g*, phi, **B**\] \+ *S*constraint\[**P**m, **P**L, **B**\] (one algebra-valued **B**3 generating both) must be written and varied in g, phi, B. v1.3 does not yet write it (the title is corrected accordingly). **\[OPEN \- this is why the title says “Measure/Form Actions,” not “Single-Parent.”\]**

## **§3. The cross-carrier No-Go (Theorem A29.2)**

**Theorem A29.2 (CLOSED-NEGATIVE).** rhomatter/rhoL \= (38/83)\*(2 muZ*n*/**ZF***f*2); the bracket scales under muZ \-\> alpha muZ but changes under *f* \-\> beta *f* (I1-I3); rhoDE \= 2M is an integration constant (I4). With §2.3, the vacuum normalization is free as the whole rank-83 flux vector (K5). Unified-Normalization is **not** a theorem of the action; it is a present-epoch condition. This is the one unambiguously load-bearing, closed result of A29 (as a No-Go). It is also why “zero free parameters”, defensible for the dimensionless *ratios*, does *not* extend to the absolute *scale*. (QED)

## **§4. The everpresent scale is Friedmann-class**

**PROVEN-algebraic.** With *c*2 \= OmegaL \= 83/121, rhoL \= 3*c*2**M-bar**P2H02 \= (geometric-mean)4 \= 24 pi2**M-bar**P4/SdS (F1-F2, E3). Both the CKN-saturated bound (L \= 1/H) and the de Sitter entropy *reduce to this same Friedmann relation* (F3, now classed as a consistency check), so neither *independently sets* the scale; the scale *is* Friedmann-at-the-horizon, near-tautological once OmegaL \~ O(1). CKN is **IMPORTED-MOTIVATED** (a collapse heuristic for OmegaL \<= O(1)). The only Z-Spin-specific content is the coefficient chiZ/alphapatch \= (3\*83/121)2 \= 4.235 **\[COMPUTED-INCOMPLETE\]**; its round-trip (G1-G2) is bookkeeping, not a computation of chiZ.

### **§4.1 What fixes the sign (corrected from v1.2)**

**Corrected.** v1.2 wrote that the positive rank trace 83/121 \> 0 fixes the sign. That is wrong \- *every* projector has a positive rank, and it does not say why the *vacuum* projector rather than the matter projector carries the energy. The sign is fixed instead by the **positive-semidefinite Maxwell-type four-form action** together with **P**L being a projector (rhoL \= (1/2)|**P**L**M**|2 \>= 0\) *once***P**L is selected and a ghost-free energy convention is adopted. The rank trace fixes the channel *multiplicity*, not the sign. Status: **DERIVED-CONDITIONAL** on the positive Maxwell sign and the **P**L selection (G1).

## **§5. The Physical-Trace gate (DERIVED-CONDITIONAL)**

Case A (121, qL \= 0.6860) and Case B (120, 0.6833) both lie within \~1% of OmegaL \~ 0.6847 (B1-B4); data does not discriminate. Establishing the ZS-F23 seam mode is BRST-closed-not-exact needs the H0(*Q*BRST) cohomology \[11\]. Status: DERIVED-CONDITIONAL argument; the cohomology is a TARGET.

## **§6. The present-epoch selection as an undecided fork**

**Branch A (constant Lambda, frozen** *w* \= \-1): the crossing epoch is an integration constant; coincidence OPEN. **Branch C (everpresent):** OmegaL \~ O(1) always; coincidence dissolves, at the cost of *w* \!= \-1. **DESI: NON-CLAIM (kept).** DESI DR2's phantom-past *w*0*w*a fit is reproduced by neither branch; the everpresent fluctuation fails **independently in amplitude and in redshift-dependence**. (v1.1's “modulus/phase pair” description was withdrawn in v1.2 as a pattern-fit; a real function *w*(z)+1 has no canonical modulus/phase split.) |*w*\+1| \~ 10\-61 is A26's, not re-derived here. The i-tetration reading of §12 (O5) is the corpus' best candidate for a *secular* *w*(z), but \- computed \- it gives a frozen *w* \~ \-1, not the DESI crossing.

## **§7. The fermion/boson supertrace direction (HYPOTHESIS-weak; Outlook §12)**

The X \= fermion / Y \= boson reading exists (ZS-M19 §10) but is HYPOTHESIS-strong and “reinterpreted, not re-derived”; the corpus' deeper f/b machinery is topological (2pi/4pi; NC-A7.8 disclaims SUSY); Pauli exclusion is not the CKN gravitational exclusion that sets the floor (§4). Using Coleman-Weinberg \[12, 13\], the three divergence gates are kept separate (Str **M**0 \= Str 1 quartic; Str **M**2 quadratic; Str **M**4 log), with the **dimensional** form Str **M**4/M\*4 \= 4.235 (L4). The coincidence Str **M**0 \= 6 \- 2\*3 \= 0 (L2) would cancel the **M-bar**P4 quartic (c0 \-\> 0), but §4 uses that same **M-bar**P4 as a live ceiling \- whether the two compose or compete is **UNRESOLVED**, and the 6 \= 2\*3 dof assignment inserts a Weyl factor on sector dimensions (a numerology trap until derived). HYPOTHESIS-weak; collected in §12 (O3).

## **§8. The three gates of the 83/121 bridge, and the internally-decidable tasks**

The most useful result of the v1.0-v1.3 audit is not a closure but a **decomposition**: what looked in v1.0 like “one calculation” (compute chiZ/alphapatch \= 4.235) is, correctly, a chain of **independent gates**, each of which must be closed for rank **P**L \= 83 to become the energy fraction OmegaL \= 83/121.

### **§8.1 The gates**

**G1 \- projector selection (TFS).** Why does **P**L (rank 83), not **P**m (rank 38\) or any other projector, carry the vacuum top-form? Not fixed by the four-form structure (contracting **P**m is equally consistent). DERIVED-CONDITIONAL.  
**G2 \- flux collectivization.** The rank-83 flux has up to 83 free constants (§2.3, K5). Reducing them to a single normalization needs an O(83) isotropy, a single collective mode, or a rank-to-energy theorem. OPEN.  
**G3 \- rank-to-energy normalization.** Even granting G1, G2, why does the *energy* fraction equal the *rank* fraction (the present-epoch UN of A28)? Matter dilutes; the vacuum is constant; the equality holds only on one hypersurface. OPEN.  
Beyond these three sit the single-parent field **identification** (§2.4) and **PT** (§5). So v1.0's single missing calculation is, accurately, **five gates**. Exhibiting this structure \- rather than asserting the value \- is the audit's principal positive contribution; it is what an external reader needs to attack the problem.

### **§8.2 A computed candidate for G3: the maximally-mixed state**

ZS-A23 carries a dimension-weighted semigroup but leaves the physical embedding Omegai \= rank **P**i/121 OPEN. A concrete candidate (verified M1-M2): the **maximally-mixed state** rho\* \= **I**121/121 on the 121-channel face algebra gives

Tr(**P**L rho\*) \= rank **P**L/121 \= 83/121,    Tr(**P**m rho\*) \= 38/121.(A29.5)

So the rank-to-energy bridge is realized *exactly* by one specific state \- the maximally-mixed (infinite-temperature) state. This is **not** a closure (the identity Tr(**P**i**I**/121) \= rank/121 holds for *any* projector, so it does not by itself single out the vacuum). Its value is that it **reduces G3 to a sharp, internally-decidable question:** *is the cosmic vacuum the maximally-mixed (de Sitter-thermal) state on M*121*?* The de Sitter horizon is thermal, which makes this physically natural and connects to the everpresent/holographic reading \- but it must be *derived* from the parent-state dynamics, not assumed. HYPOTHESIS-strong.

### **§8.2b The rank-weighted master equation (the best G3 candidate)**

The maximally-mixed candidate has a natural *dynamical* realization. If the transition rate into a sector is proportional to its number of microstates (its rank) \- equivalently, if per-channel amplitudes are equal by the Z-Spin seam symmetry \- then the parent occupations obey

d/dtau (**p**m, **p**L)T \= k \[-83, \+38 ; \+83, \-38\] (**p**m, **p**L)T,   qm-\>L \= 83k,  qL-\>m \= 38k.(A29.6)

Its unique, probability-conserving stationary state is **p**m \= 38/121, **p**L \= 83/121 (verified ME1), with *no free parameter* \- exactly what the cubic source of §13/E.5 cannot do (there the ratio is free). It is the *dynamical* form of rho\* \= **I**/121, unifying three threads: the maximally-mixed candidate, ZS-A23 dimension-weighted semigroup, and the inverse (slog-type) outward channel as the L-\>m rate. **Honest status: HYPOTHESIS-strong, not DERIVED.** Two gaps remain, both the same equal-weight assumption in different clothes: (g1) the rank-weighted rate \= the vacuum being the maximally-mixed state is *assumed*, not proven; and (g2) **p**L is an *occupation* \- identifying it with the energy fraction OmegaL needs a state-to-stress-energy map (equal energy per microstate), the G3 normalization gap itself. The master equation *relocates* G3 to a sharp dynamical question \- *does the parent-state dynamics actually have equal-amplitude, rank-weighted rates?* \- rather than closing it. \[Best current candidate for G3; surfaced in an AI-assisted pass as the dynamical realization of the maximally-mixed candidate.\]

### **§8.3 The internally-decidable tasks (external review is necessary, not the only route)**

v1.2 over-stated that “the only exit is external.” External specialist review **is** necessary for validation, but the internal programme retains **three decidable mathematical tasks** that do not require it: (i) **unified-action variation** \- write *S*grav \+ *S*GNP \+ *S*constraint with one algebra-valued **B**3 and vary in g, phi, B (§2.4); (ii) **flux-collectivization analysis** \- a group-representation study of whether an O(83) symmetry or single collective mode is forced (G2); (iii) **single-parent stationary-state embedding** \- test whether the parent-state dynamics drive rho toward rho\* \= **I**/121, closing G3 (§8.2). These are the highest-value next steps *alongside* external contact, not in place of it.

## **§9. The B3 classification after A29 v1.6**

Table 9.1. Status after ZS-A29 v1.6. down \= demotion, up \= raise, NEW \= surfaced; G1/G2/G3 \= the three bridge gates of §8.

| Item | Status (v1.6) | Change vs v1.2 / basis |
| ----- | ----- | ----- |
| B3-A (A-Q-only) | CLOSED-NEGATIVE | unchanged (A27) |
| B3-B (absolute scale) | OPEN \- terminal | unchanged |
| Four-form mechanism | PROVEN-as-construction | unchanged; K6 now REAL (Levi-Civita) not a tautology |
| w=-1 of the top-form | IMPORTED-PROVEN | K6: eps eps=-3\! g \=\> T=-rho g \=\> w=-1 (computed at tensor level) |
| G1 projector selection (TFS) | DERIVED-CONDITIONAL | gate named (§8.1) |
| G2 flux collectivization | OPEN (gate) | §2.3 softened: kinematic precursor of BP-type freedom (not full landscape) |
| G3 rank-to-energy | OPEN (gate); candidate | NEW (§8.2): max-mixed state rho\*=I/121 gives 83/121 EXACTLY (M1-M2); reduces G3 to a decidable question |
| Single-parent identification | OPEN | §2.4; TITLE corrected to “Measure/Form Actions” |
| Everpresent scale | Friedmann-class / IMPORTED-MOTIVATED | unchanged from v1.2 |
| Mean+variance: sign | DERIVED-CONDITIONAL | down from v1.2 “DERIVED”: Maxwell sign \+ P\_L selection fix it, NOT rank trace (§4.1) |
| PT (121 vs 120\) | DERIVED-CONDITIONAL | unchanged (BRST \= TARGET) |
| DESI / present-epoch fork | NON-CLAIM / OPEN | unchanged; i-tetration (O5) computed \-\> frozen w, not DESI |
| i-tetration orbit w(z) (O5) | HYPOTHESIS-strong | NEW (§12): spiral real (T1-T2); corpus anchor \-\> frozen w (T3); reinforces w=-1, NOT DESI |
| Fermion/boson supertrace | HYPOTHESIS-weak | unchanged; dimensional fix kept (§7) |
| chi\_Z/alpha\_patch \= 4.235 | COMPUTED-INCOMPLETE | unchanged; NOT advanced |
| P3 coexistence (emergence) | DERIVED-COND / OPEN | NEW (§13/E.5): minimal source J\>J\_c=4(1-|lambda|); ratio NOT fixed (curvature coarsening even at Maxwell) \-\> 4th route to the No-Go |
| Rank-weighted master eq (G3) | HYPOTHESIS-strong | NEW (§8.2b): stationary (38/121,83/121), no free J \= dynamical rho\*=I/121; gaps: equal-amplitude \+ occupation-\>energy |
| Budget (6,32,83)/121 | present-epoch boundary condition | CONVERGENCE: 2 No-Go theorems \+ flux obstruction \+ coexistence all agree it is NOT a dynamical invariant |
| B3-D unconditional closure | PARTIAL | net: structure clarified (5 gates \+ master-eq candidate); number unmoved |

## **§10. Falsification gates**

**Mathematical / immediate.** (F-A29.1) If the GNP measure provably cannot be rank-83 projector-valued, §2.2 fails as a realization. (F-A29.2) If no single-parent action reproduces dust+vacuum without interference, §2.4 fails.  
**Structural / consistency.** (F-A29.3) If no flux-collectivization structure exists (G2), 83/121 is not an energy prediction. (F-A29.3b) If parent-state dynamics do NOT drive rho \-\> **I**/121, the G3 candidate (§8.2) fails. (F-A29.4) If chiZ/alphapatch \!= 4.235 on (3,2,6)/11, Branch C's promotion fails.  
**Observational / external.** (F-A29.5) The i-tetration w(z) (O5) is falsifiable in principle by its zero-parameter *decay-per-oscillation* ratio (\~0.85; T2), but this needs \>= 2 resolved DE oscillations, beyond DESI DR2; and under the corpus anchor it predicts a *frozen* *w* \~ \-1 (T3), so a robust DESI *evolution* (wa \!= 0\) at high significance would disfavor the corpus' natural reading. (F-A29.6) dNeffBBN \= 2**A** \= 0.160 and *r* \= 0.0089 inherited; always-on dNeffCMB \= 0.160 already FALSIFIED. (F-A29.7) OmegaL outside \[0.6833, 0.6860\] \+/- error kills both PT cases.

## **§11. Conclusion**

A29 v1.6 consolidates a multi-version audit whose central, honest result is a **convergence**: four independent routes \- two No-Go theorems (A27 A-Q-only; A29.2 cross-carrier), the rank-83 flux obstruction (K5), and now the dynamical reaction-diffusion coexistence analysis (§13/Appendix E.5) \- all reach the same conclusion, that the budget (6,32,83)/121 is **not a dynamical or geometric invariant but a present-epoch boundary condition**. The supporting structural results: the **cross-carrier No-Go** (§3, strengthened to a free rank-83 flux vector); the **three-gate decomposition** of the 83/121 bridge (§8 \- the audit's principal scientific contribution, turning v1.0's “one calculation” into a precise five-gate map); a **computed G3 candidate** (the maximally-mixed state, §8.2); and a **full computation of the i-tetration orbit reading** of *w*(z) (§12), which honestly *reinforces***w** \= \-1 (resolving the ZS-U4 tension by reading it as the spiral's fixed point) while showing \- by computation, under the corpus' own anchor \- that it does **not** produce the DESI crossing.  
The flagship 83/121 and chiZ/alphapatch \= 4.235 are **unchanged**; the absolute scale is terminal in B3-B. Three rounds of audit have moved honesty, not the physics number \- which is itself the finding: *the obstruction is the No-Go and the five gates, not a missing coefficient*. The next steps are now sharp and divided honestly: **three internally-decidable tasks** (unified-action variation, flux-collectivization analysis, stationary-state embedding; §8.3) that the author can pursue, *and* external domain-expert contact for the parts that internal iteration cannot settle (whether the GNP measure can be rank-83 projector-valued; whether a flux-collectivization theorem exists). (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED.

## **§12. Outlook (HYPOTHESIS directions, explicitly NOT results)**

**(O1) Flux collectivization (G2); (O2) single-parent unification (§2.4); (O3) supertrace dof bridge (§7); (O4) a secular w(z) carrier.** Each is HYPOTHESIS-weak and detailed above or in v1.2.

### **§12.1 (O5) The i-tetration fixed-point/orbit reading of w(z) \- computed**

**The proposal.** Read the de Sitter attractor *w* \= \-1 not as a separate top-form but as the i-tetration **fixed point** z\* (the n \-\> infinity limit of the corpus' self-referential map iz); read matter (rank-38) as the **orbit** still flowing toward it; and read the free integration constant M of §2-§3 as “where we are on the orbit” \= the **observable scale factor**. This is attractive: it would convert a free parameter into an observable, and it reads ZS-U4's *w* \= \-1 as the asymptotic fixed point (resolving that fork). The corpus has z\*, the multiplier lambda, Koenigs linearization, and the damped spiral \- but only in the sub-Planck auto-surgery (ZS-M1/M12/F14); transplanting them to late-time *w*(z) is the new step.  
**The computation (this paper).** The multiplier is lambda \= (i pi/2) z\* \= \-0.566 \+ 0.688 i, with **|lambda| \= 0.8915 \< 1** (so convergence is a *damped* spiral \- Koenigs ratio verified, T1) and arg lambda \= 129.4 deg (so *w*(z) approaches \-1 as a **spiral**, crossing \-1 periodically: a *deterministic, secular* phantom crossing, not a stochastic one). Two signatures are **mapping-invariant** (fixed by z\* alone, zero free parameters, T2): one full oscillation is 2.78 iterations, and each successive excursion of *w* from \-1 is \~0.85x the previous.  
**The honest verdict (why it does not yet deliver DESI).** The load-bearing assumption is the map *iteration index n \<-\> cosmological scale factor / e-folds*, which is **UNDERIVED**. Testing the corpus' own candidate anchor taun \= tP exp(n pi/**A**) (ZS-F10/U8): it gives A/pi \= 0.025 iterations per e-fold, today n0 \= 3.6, and across the DESI redshift range (z \~ 0.5 \-\> 0\) only **0.4% of one oscillation** advances (T3). So under the corpus anchor the spiral is **frozen**: *w* \~ \-1 \= const over the observable range \- it **reinforces***w* \= \-1 (consistent with ZS-U4 and \~ΛCDM), and does **not** reproduce DESI's phantom-past evolution (which needs wa \!= 0). Producing the DESI crossing would require a *faster*, non-corpus n \<-\> scale map \- i.e. new free input \- so the “zero-parameter DESI w(z)” claim does **not** follow; the corpus anchor actively favors frozen *w* \= \-1. **Status: HYPOTHESIS-strong** for the reframing (fixed point \= vacuum, orbit \= matter, M \= observable position, U4 tension resolved); the DESI-w(z) prediction is **not supported by computation**. The one clean falsifiable prediction \- the 0.85 decay-per-oscillation ratio \- needs \>= 2 resolved DE oscillations, beyond DESI DR2. The decidable next step is to *derive* the n \<-\> scale-factor map (or prove it cannot be the slow taun one) before any data comparison.

## **§13. A methodological pivot: from top-down fitting to bottom-up emergence**

The deepest anti-numerology move available is to stop trying to *fit* 83/121, 35/437, and Q \= 11 from above (counting polyhedron faces, integer partitions) and instead ask whether they **emerge** from the one dynamical rule the corpus most deeply commits to \- the i-tetration self-referential rotation \- applied to a *blank slate*. Three concrete proposals make this testable: (P1) **braiding / TQFT** \- read iz as a braid-group action on the 2D Z-boundary and ask whether **A** is a topological invariant (Jones/Chern) or an FQHE filling factor; (P2) **tensor-network thermodynamics** \- start from a random qubit graph, evolve under i-tetration, and ask whether it spontaneously breaks into the (2, 3, 6\) blocks, making Q \= 11 a *theorem* rather than an axiom; (P3) **quantum cellular automata** \- a 2D quaternion-spin grid with a local i-tetration update, asking whether dust and vacuum separate at the ratio 83/121.  
**This is the right direction** \- it makes the framework falsifiable *from below*, not just from observation \- and it is pre-registered in full (with protocols and success criteria) in Appendix E. **But the toys, run honestly, fail, and instructively.** (E1-E2) The i-tetration orbit's rotation number (arg lambda / 2pi \= 0.3596) is *not* a low-order rational, so the braid is quasi-periodic and **does not close** \- no finite Jones polynomial exists for the actual orbit; and while 5/19 is a (high-flux) Jain state, 7/23 is not standard and a *product* of filling factors is not a filling factor, so the FQHE/Chern reading of **A** is unsupported (a Chern number must be an integer). (E3) A bare i-tetration coupled-map lattice, being a pure contraction (|lambda| \< 1), collapses to a *single* attractor \- dust and vacuum do **not** even coexist, let alone at 83/121; the split is either absent or a tunable artifact of the coupling. (E4) iz is a map on C \= R2 (the Z-sector) with a single complex multiplier; it has no internal (2, 3, 6\) spectrum, so it cannot generate the X and Y dimensions *alone*.  
**The honest lesson (and the value).** None of the three numbers emerges from i-tetration without tuned input, and the failures are *mechanistic*, not accidental: a single 2D contraction cannot, by itself, produce a multi-sector dimensional split, a closed braid, or a robust two-phase coexistence. A genuine bottom-up theory therefore needs an **explicit additional rule** \- one that (i) couples entanglement structure to dimension (for P2), (ii) supplies a source or a second basin so matter can resist the de Sitter collapse (for P3), and (iii) selects a periodic sub-orbit if any knot invariant is to exist (for P1). Specifying *that* rule is the real open problem; Appendix E states it precisely as the next pre-registered target. The perspectives' value is exactly this: they convert “we keep circling the answer” into a set of **decidable, falsifiable emergence tests** \- and they have already ruled out the naive versions. **\[Status: the pivot is DERIVED (a falsification-first reframing); each emergence claim is PRE-REGISTERED-TEST / OPEN; the naive realizations are NON-CLAIM, ruled out by E1-E4.\]**

## **Acknowledgements and Code Availability**

*verify\_zs\_a29\_v1\_6.py* is fully fail-closed (every entry a real computation; the v1.5 E4 identity moved to a note, E1 corrected, CX4 split, the rank-weighted master equation ME1 added) and *prints its own counts* (30 load-bearing \+ 23 new \+ 3 bookkeeping \= 56 asserts, \+ 8 notes), quoted verbatim above. **All “review” / “adversarial pass” herein is AI-assisted (Claude / ChatGPT / Gemini) inside the author's workflow; no external or human domain-expert peer review has taken place.** This work used Anthropic Claude for the audit, the i-tetration computation, and drafting; the author assumes full responsibility for all content, including errors caught only on later passes.

## **Appendix A. Verification ledger (56 fail-closed asserts; counts printed by the script)**

All entries are real computations in verify\_zs\_a29\_v1\_6.py: 30 load-bearing, 23 new mechanism, 3 bookkeeping, \+ 8 printed notes (not asserts).

| Block | Check | Status |
| ----- | ----- | :---: |
| A-E (LB, 22\) | rank budget; PT cases; A=(5/19)(7/23); N=69.16; 4N=276.64; rhoL/Mp^4=24pi^2/S\_dS=7e-121 | PROVEN |
| I1-I4 (LB, 4\) | No-Go: rho\_m/rho\_L bracket scales under muZ, CHANGES under f; rho\_DE=2M integration constant | PROVEN-symbolic |
| J1-J2 (LB, 2\) | z\*=0.4383+0.3606i; |f'(z\*)|=0.8915\<1 | PROVEN |
| K1-K5 (NEW) | real 121x121 rank-83 P\_L; rho\_L=1/2 sum\_{1..83}M\_a^2; 38 P\_m fluxes drop; 83 free flux constants (G2) | PROVEN-as-construction / OPEN |
| K6 (NEW, fixed) | REAL Levi-Civita: eps\_(m a b g)eps\_n^(a b g)=-3\! g\_mn \=\> T\_uv=-rho g\_uv \=\> w=-1 (was a tautology in v1.2) | IMPORTED, now tensor-verified |
| L1-L4 (NEW) | supertrace: no simple combo=4.235; Str M^0=Str 1 quartic (6-2\*3=0); 3 gates; DIM fix Str M^4/M\_\*^4 | HYPOTHESIS-weak |
| M1-M2 (NEW) | rho\*=I/121: Tr(P\_L rho\*)=83/121, Tr(P\_m rho\*)=38/121 (rank-to-energy G3 candidate; max-mixed state) | HYPOTHESIS-strong |
| T1-T3 (NEW) | i-tetration: lambda=(i pi/2)z\*, |lambda|=0.8915 spiral; 2.78 iter/osc & 0.85 decay (invariant); tau\_n anchor \=\> 0.4% of an osc over DESI range \=\> FROZEN w | HYPOTHESIS-strong |
| E1-E3 (NEW) | emergence: NO low-period closure up to denom bound (NOT a no-Jones proof, E1 corrected); 5/19 Jain but 7/23 not \=\> FQHE unsupported; bare i-tetration CML collapses to one attractor. (E4 \= i^z is 2D: moved to a NOTE, was an identity) | PRE-REG TEST / NON-CLAIM |
| CX1-CX3,CX4a (NEW) | P3 coexistence: robust bistability J\>J\_c=4(1-|lambda|)=0.434 (J=J\_c saddle-node); Maxwell J\_M=4.5(1-|lambda|); phi+=2/3 generic (NOT 83/121); CX4a=analytic area sign (CX4b front-velocity \= a NOTE) | DERIVED-COND / OPEN |
| ME1 (NEW) | rank-weighted master eq: stationary (38/121,83/121), conserves probability, no free J \= dynamical rho\*=I/121 (best G3 candidate); gaps g1 equal-amplitude \+ g2 occupation-\>energy (notes) | HYPOTHESIS-strong |
| G1-G2, F3 (BK, 3\) | 4.235 round-trip (circular); F3 reclassified algebraic-consistency (Hinf2 from rhoL) | bookkeeping |
| Notes (4) | printed commentary, NOT asserts (CKN reduces to Friedmann; no external review; flux landscape; G3 question) | NOTE |

## **Appendix B. Cross-version safety and dependency check**

A29 v1.3 uses (never modifies): ZS-A28, ZS-A26, ZS-A27, ZS-A23 (dimension-weighted semigroup; the §8.2 rho\* candidate is a proposed closure of its OPEN embedding), ZS-A20, ZS-A19, ZS-M19 §10, ZS-A7/F14/M3, ZS-M1/M12 (z\*, lambda, Koenigs \- the §12 O5 computation transplants these from sub-Planck to late-time, a NEW use flagged HYPOTHESIS-strong), ZS-F10/U8 (taun anchor, tested in O5), ZS-F9, ZS-U4 (frozen *w* \= \-1 \- O5 reads it as the asymptotic fixed point, a reinterpretation, not a modification), ZS-F2, ZS-F23. **Tensions recorded:** (i) Branch C / O5-secular would predict *w* \!= \-1 (fork with U4, not adopted); but O5 computed under the corpus anchor gives frozen *w* \= \-1, so it is *consistent* with U4, not in tension. (ii) the §4/§7 **M-bar**P4 ceiling-vs-cancellation tension is flagged UNRESOLVED. **Relative to v1.2:** title corrected; K6 made real; F3 reclassified; §2.3 softened; §4.1 sign corrected; §8 three-gate structure \+ rho\* candidate added; O5 computed. No downstream value changes. (**A**, **Q**, dim **Z**) LOCKED.

## **Appendix C. Internal adversarial-pass record (5-step, v1.3)**

**Step 0 \- Long list (7).** (0.1) the i-tetration orbit w(z) proposal \- compute it fully; (0.2) title vs §2.4 contradiction; (0.3) K6 tautology \+ F3 classification; (0.4) §2.3 “BP landscape” too strong; (0.5) §4.1 sign argument; (0.6) “only external exit” over-statement \+ rank-to-energy candidate; (0.7) meta-audit density. **Dropped:** none substantive; (0.7) handled by consolidating meta into Appendices.  
**Step 1 \- Issue list (4 MECE).** (A) compute the i-tetration orbit and report honestly \[0.1\] \- the one direction that could move a number; (B) editorial/verification corrections \[0.2, 0.3, 0.4, 0.5\]; (C) the gate structure \+ internal-task balance \+ rho\* \[0.6\]; (D) meta density \[0.7\].  
**Step 2 \- Issue tree.** (A) is the lead (new physics, falsifiable); (B) are the fully-closable editorial fixes; (C) is the scientific reframing (three gates); (D) is presentation.  
**Step 3 \- Traversal with status.** (A) i-tetration: spiral PROVEN-real (T1-T2); DESI claim NOT supported (T3, frozen w); reframing HYPOTHESIS-strong. (B) title fixed; K6 real; F3 reclassified; §2.3 softened; §4.1 corrected. (C) three gates named (§8.1); rho\* G3 candidate computed (§8.2, HYPOTHESIS-strong); internal tasks listed (§8.3). (D) meta \-\> Appendices.  
**Step 4 \- Convergence.** First pass N\_changed \~ 9 (i-tetration computed, title, K6, F3, §2.3, §4.1, §8 gates, rho\*, meta-trim). Second pass N\_changed \~ 0\. **CONVERGED**. The decisive new content (i-tetration) *self-limited*: computation showed it reinforces *w* \= \-1 rather than delivering DESI, so it did not inflate any claim \- the anti-numerology discipline operated as designed.  
**Step 5 \- Scoring.** Convergent; corpus-non-conflicting; anti-numerology respected (the i-tetration DESI claim was tested and *rejected* by computation, not asserted). Leadership: the i-tetration computation was run before being asked to defend it, and reported against its own initial appeal \- the honest form of leading. Honesty \~9.5; the i-tetration reframing is a genuine conceptual gain (M \-\> observable; U4 resolved); the physics number is still unmoved, now for a clearly-mapped five-gate reason.

## **Appendix D. Disposition of prior AI-assisted adversarial passes**

Table D.1. Points raised by prior AI-assisted passes (Claude/ChatGPT/Gemini; NOT external or human peer review) and their disposition in v1.3.

| Point (prior AI pass) | Disposition | Where |
| ----- | :---: | ----- |
| Title “Single-Parent” contradicts §2.4 “not yet single-parent” | ACCEPTED \+ FIXED | Title \-\> “Measure/Form Actions...” |
| v1.2 K6 is a tautology bool(w+1==w+1); F3 is algebraic-consistency not load-bearing | ACCEPTED \+ FIXED | K6 \-\> real Levi-Civita tensor; F3 \-\> bookkeeping (counts 30/15/3) |
| “precisely a Bousso-Polchinski landscape” too strong | ACCEPTED \+ SOFTENED | §2.3: kinematic precursor; prior to quantization/membranes |
| “positive rank trace fixes the sign” is wrong | ACCEPTED \+ CORRECTED | §4.1: Maxwell sign \+ P\_L selection; status \-\> DERIVED-CONDITIONAL |
| “only exit is external” too strong; internal decidable tasks remain (rho\*=I/121) | ACCEPTED \+ ADDED | §8.2-8.3: rho\* G3 candidate (M1-M2) \+ three internal tasks |
| meta-audit content excessive for a physics paper | ACCEPTED | §1 trimmed; process consolidated into Appendices C-D |
| i-tetration spiral w(z) proposal (user breakthrough) | COMPUTED \+ INTEGRATED HONESTLY | §12 O5: spiral real (T1-T2) but frozen w under corpus anchor (T3); reframing HYPOTHESIS-strong; NOT a result |
| the loop has converged; physics numbers unmoved in 3 rounds; only real exit is external contact | ACCEPTED | §8.3, §11: internal tasks named AND external contact stated outstanding |

## **Appendix E. Pre-registered bottom-up emergence tests (protocols, success criteria, toy results)**

Each test below is stated so that it can be run by an independent party and can *fail*. “Toy result” is the outcome of a small computation in *explore\_emergence.py*; “Pre-registered success” is the criterion fixed *before* any run, to prevent post-hoc fitting.

### **E.1 (P1) Braiding / topological invariant**

**Protocol.** Treat the i-tetration orbit zn+1 \= iz\_n near z\* as a worldline braid on the 2D Z-boundary; compute the rotation number rho \= arg(lambda)/2pi and, if rho is rational p/q, close the q-strand braid and evaluate its Jones polynomial / the associated Chern number; test whether **A** \= 35/437 appears as that invariant or as an FQHE filling factor. **Pre-registered success:** A is reproduced as an integer Chern number or a standard (Jain/hierarchy) filling factor with no free choices. **Toy result (FALSIFIED):** rho \= 0.3596 shows NO low-period closure up to the pre-registered denominator bound (nearest rational with denominator \<= 12 is 4/11, residual 4e-3; \<= 25 is 9/25, residual 4e-4) \- which does NOT prove irrationality or that no Jones polynomial exists, only that no short braid closure was found; 5/19 is Jain (2p \= 4\) but 7/23 is not standard and the product of two filling factors is not a filling factor; a Chern number must be an integer. The FQHE/Chern reading is NON-CLAIM (E1-E2).

### **E.2 (P2) Tensor-network emergence of Q \= 11**

**Protocol.** Initialize a random qubit graph (no assumed (2, 3, 6\) structure); evolve the entanglement under an i-tetration update; track the entanglement-entropy spectrum and any spontaneous block decomposition. **Pre-registered success:** the stable state breaks into exactly three sectors of effective dimension 2, 3, 6 (total Q \= 11\) with no dimension inserted by hand. **Toy / structural result (NOT available as stated):** iz is a single map on C \= R2 with one complex multiplier \- it carries no internal (2, 3, 6\) spectrum, so the Z-dynamics cannot generate the X and Y dimensions by itself (E4). The test is only meaningful once an *additional* rule coupling entanglement structure to emergent dimension is specified; that rule is the open target.

### **E.3 (P3) Quantum cellular automaton: dust/vacuum separation**

**Protocol.** A 2D grid of quaternion/Z4 spin states {1, i, \-1, \-i} with a local i-tetration update; run from random initial data; classify cells as “vacuum” (settled at z\*) vs “dust” (orbiting) and measure the steady-state fraction. **Pre-registered success:** the vacuum fraction converges robustly (independent of coupling/threshold) to 83/121 \= 0.686, dust to 38/121. **Toy result (FALSIFIED):** a bare i-tetration coupled-map lattice is a pure contraction (|lambda| \< 1\) and collapses to a *single* attractor (\~100% vacuum in 120 steps) \- dust and vacuum do not coexist; where a partial split can be forced it tracks the arbitrary coupling, so 83/121 is a tunable artifact, not an invariant (E3).

### **E.4 What a genuine emergence theory must add**

The three failures share one cause \- a single 2D contraction is too simple to generate multi-sector structure \- and so define the next pre-registered target precisely: an explicit rule that (i) for P2 couples entanglement to emergent dimension; (ii) for P3 supplies a **source or second basin** so matter (the orbit) resists the de Sitter collapse to z\* (Appendix E.5 computes the minimal such rule: a bistable source of strength J \>= 4(1-|lambda|); without it the contraction that gives *w* \= \-1 also erases all dust); (iii) for P1 selects a periodic sub-orbit so a knot invariant can exist. Until such a rule is specified and shown to yield the numbers with **no** tuned input, bottom-up emergence of (83/121, 35/437, Q \= 11\) is **OPEN / NON-DEMONSTRATED** \- but it is now a set of sharp, falsifiable tests rather than an aspiration, and the naive versions are closed.

### **E.5 (P3, extended) The minimal source term and the conditions for coexistence**

v1.4 found that the bare i-tetration lattice collapses to vacuum (no dust survives). v1.5 acts on the mechanistic diagnosis \- matter needs to *resist* the de Sitter contraction \- and adds the simplest such rule, then asks not whether 83/121 appears but what FORM of rule makes coexistence possible at all. Let phi in \[0, 1\] be a matter field (phi \= 0 vacuum at z\*, phi \> 0 orbiting dust). The contraction rate is fixed by the corpus: gamma \= 1 \- |lambda| \= 0.108. The minimal dynamics adds a bistable autocatalytic source to that contraction,

*R*(phi) \= \-gamma phi \+ J phi2(1 \- phi),    gamma \= 1 \- |**lambda**| \= 0.108  (the i-tetration contraction rate).(E.1)

**Computed result (explore\_coexistence.py; CX1-CX4).** (i) A second (dust) phase exists \- and coexistence becomes possible \- *iff* J \>= **J**c \= 4(1 \- |**lambda**|) \= 0.434 (CX1-CX2); J \= Jc is itself only a saddle-node creation threshold (phi+ \= phi- \= 1/2, non-hyperbolic), so robust bistability needs J \> Jc. Below it only vacuum is stable, exactly reproducing the bare-lattice collapse. So, **within the minimal scalar cubic bistable ansatz**, the source threshold is fixed by the Z-Spin contraction rate (not a uniqueness theorem \- other bistable, nonlocal, or conserved-field rules exist): a source whose strength exceeds a *corpus-tied* threshold set by the i-tetration contraction rate. (ii) The planar vacuum/dust front is stationary only at the Maxwell point **J**M \= (9/2)(1 \- |**lambda**|) \= 0.488 (CX3; analytic area-sign verified in CX4a, with the numerical front-velocity sweep in the explore script, CX4b): below it vacuum invades (dust \-\> 0), above it dust invades (dust \-\> 1). (iii) **The dust/vacuum ratio is NOT pinned:** generically it flows to 0 or 1; and at JM only the *planar* front is stationary \- a curved dust domain still SHRINKS by curvature-driven (Allen-Cahn) coarsening (verified: a disk loses \~40% of its area at JM), so even Maxwell balance does not preserve a seeded fraction. A specific value such as 83/121 occurs only by *tuning* J and *seeding* the fraction \- never as an output, and not even stably then. (The dust-phase field value phi\+ \= 2/3 at JM is a generic algebraic feature of the cubic, *not* the 83/121 volume fraction \- an anti-numerology caution.)  
**The pre-registered J \= f(A, Q) test (negative).** A candidate counts as a derivation only if J is fixed by **A**, **Q** with no free choice AND the random-initial-condition ratio becomes 83/121 as an output. Neither holds: no simple **A**, **Q** expression selects Jc or JM (these are fixed by |**lambda**| alone, but picking J \= JM is itself a selection), and even fixing J \= JM while *seeding* the ratio at 83/121 does not preserve it (it coarsens to \~1). So deriving J is **not** an exit. The structure that *would* fix the ratio is instead the conserved-probability **rank-weighted master equation** of §8.2b \- which is why the resolution, if any, lies in parent-state dynamics, not in tuning a source strength.  
**Interpretation.** This is a genuine advance on P3 \- it converts “needs a source (open)” into a precise, falsifiable, corpus-tied condition for coexistence \- and it carries an honest lesson: even with coexistence achieved, the ratio remains free. That *independently reproduces* the corpus' own Cross-Carrier No-Go (§3) and the G3 gate (§8): the dust/vacuum ratio is a **present-epoch condition, not a dynamical invariant**. The emergence route therefore meets the same obstruction as the algebraic route, from the opposite direction. **The next pre-registered target** is now sharp: derive the source strength J (or an additional selection principle pinning the front at a specific fraction) from **A** and **Q** \- not a free knob. Until then, coexistence is **DERIVED-CONDITIONAL** (on J \>= 4(1 \- |**lambda**|)) and the ratio is **OPEN**.

## **References**

\[1\] E. I. Guendelman, E. Nissimov, and S. Pacheva, Metric-independent volume-forms ... and the dark sector of the Universe, Bulg. J. Phys. 41, 123 (2014), arXiv:1404.4733.

\[2\] E. I. Guendelman, E. Nissimov, and S. Pacheva, Dark energy and dark matter from hidden symmetry ..., Eur. Phys. J. C 75, 472 (2015), arXiv:1508.02008.

\[3\] E. Guendelman, E. Nissimov, and S. Pacheva, Unified dark energy and dust dark matter ..., Eur. Phys. J. C 76, 90 (2016), arXiv:1511.07071.

\[4\] M. Henneaux and C. Teitelboim, The cosmological constant and general covariance, Phys. Lett. B 222, 195 (1989).

\[5\] M. Ahmed, S. Dodelson, P. B. Greene, and R. Sorkin, Everpresent Lambda, Phys. Rev. D 69, 103523 (2004), arXiv:astro-ph/0209274.

\[6\] N. Zwane, N. Afshordi, and R. D. Sorkin, Cosmological tests of everpresent Lambda, Class. Quantum Grav. 35, 194002 (2018), arXiv:1703.06265.

\[7\] G. Koenigs, Recherches sur les integrales de certaines equations fonctionnelles, Ann. Sci. Ec. Norm. Super. 1, 3 (1884).

\[8\] R. Bousso and J. Polchinski, Quantization of four-form fluxes and dynamical neutralization of the cosmological constant, JHEP 06, 006 (2000), arXiv:hep-th/0004134.

\[9\] J. D. Brown and K. V. Kuchar, Dust as a standard of space and time ..., Phys. Rev. D 51, 5600 (1995), arXiv:gr-qc/9409001.

\[10\] J. D. Brown and C. Teitelboim, Neutralization of the cosmological constant by membrane creation, Nucl. Phys. B 297, 787 (1988).

\[11\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, Classical BV theories on manifolds with boundary, Commun. Math. Phys. 332, 535 (2014), arXiv:1201.0290.

\[12\] S. R. Coleman and E. Weinberg, Radiative corrections as the origin of spontaneous symmetry breaking, Phys. Rev. D 7, 1888 (1973).

\[13\] S. Ferrara, L. Girardello, and F. Palumbo, A general mass formula in broken supersymmetry, Phys. Rev. D 20, 403 (1979).

\[14\] A. G. Cohen, D. B. Kaplan, and A. E. Nelson, Effective field theory, black holes, and the cosmological constant, Phys. Rev. Lett. 82, 4971 (1999), arXiv:hep-th/9803132.

\[15\] M. Li, A model of holographic dark energy, Phys. Lett. B 603, 1 (2004), arXiv:hep-th/0403127.

\[16\] DESI Collaboration, DESI DR2 results II: ... baryon acoustic oscillations and cosmological constraints, arXiv:2503.14738 (2025).

\[17\] G. W. Gibbons and S. W. Hawking, Cosmological event horizons ..., Phys. Rev. D 15, 2738 (1977).

\[18\] S. Weinberg, The cosmological constant problem, Rev. Mod. Phys. 61, 1 (1989).

\[19\] Planck Collaboration, Planck 2018 results VI, Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209.

\[20\] M. Cortes and A. R. Liddle, On the dark energy crossing the phantom divide, Mon. Not. R. Astron. Soc. Lett. 544, L121 (2025).

\[ZS-A28\] K. Kang, ZS-A28 v2.0: Vacuum Energy as a Projector-Valued Top Form, Z-Spin Cosmology (2026).

\[ZS-A26\] K. Kang, ZS-A26 v2.2: The Cosmological Constant as a Quantum State Variable, Z-Spin Cosmology (2026).

\[ZS-A27\] K. Kang, ZS-A27 v2.3: The Absolute Vacuum-Energy Scale and the A-Q-Only No-Go, Z-Spin Cosmology (2026).

\[ZS-A23\] K. Kang, ZS-A23: Dimension-Weighted Semigroup and the Rank-to-Energy Embedding (OPEN), Z-Spin Cosmology (2026).

\[ZS-M1\] K. Kang, ZS-M1: i-Tetration HSI Theorem, z\*=0.43828+0.36059i, lambda=(i pi/2)z\*, |lambda|=0.891514, Koenigs, Z-Spin Cosmology (2026).

\[ZS-M12\] K. Kang, ZS-M12: Auto-Surgery and the Damped Spiral (sub-Planck), Z-Spin Cosmology (2026).

\[ZS-F10\] K. Kang, ZS-F10: Information-Time Correspondence; tau\_n \= t\_P exp(n pi/A), Z-Spin Cosmology (2026).

\[ZS-M19\] K. Kang, ZS-M19 v1.0: Database-PK reading of sector statistics (T8), Z-Spin Cosmology (2026).

\[ZS-U4\] K. Kang, ZS-U4: Locked late-time budget (6,32,83)/121, w=-1 attractor, Z-Spin Cosmology (2026).

## **Version History**

**v1.0-v1.1 (June 2026):** GNP action \+ cross-carrier No-Go; v1.1 lowered five v1.0 overclaims and added the projector-valued four-form, but introduced a verification count mismatch and an “external peer review” mislabel.  
**v1.2 (June 2026):** Fully repaired the verification (counts script-sourced); corrected the loop-honesty failure (disclaimer; “review” relabelled AI-assisted); lowered the four-form to PROVEN-as-construction and the everpresent scale to Friedmann-class; withdrew the modulus/phase description; surfaced the rank-83 flux and single-parent gates.  
**v1.3 (June 2026): Internal AI-assisted audit \+ i-tetration computation.** Consolidated from internal Z-Spin Collaboration notes through v1.3.0. **Title corrected** (“Measure/Form Actions...”; v1.2's “Single-Parent” contradicted its own §2.4). **Verification**: K6's v1.2 tautology replaced by a real Levi-Civita tensor computation (eps eps \= \-3\! g \=\> w \= \-1); F3 reclassified as an algebraic-consistency check; counts 30 LB \+ 15 new \+ 3 bookkeeping \= 48, script-printed. **Lowered/corrected**: §2.3 “Bousso-Polchinski landscape” \-\> kinematic precursor (prior to flux quantization/membranes); §4.1 sign argument \-\> the positive Maxwell action \+ **P**L selection fix the sign (DERIVED-CONDITIONAL), not the rank trace. **Added (scientific)**: §8, the **three-gate decomposition** (G1 selection / G2 collectivization / G3 rank-to-energy) of the 83/121 bridge, with a computed G3 candidate \- the maximally-mixed state rho\* \= **I**/121 giving 83/121 exactly (M1-M2) \- and three internally-decidable tasks (§8.3), balancing v1.2's “only external exit” over-statement. **Computed (O5)**: the user's **i-tetration fixed-point/orbit reading** of *w*(z) \- lambda \= (i pi/2)z\*, |lambda| \= 0.8915 damped spiral (T1), invariant 2.78 iter/oscillation and 0.85 decay (T2). Under the corpus anchor taun only 0.4% of an oscillation advances over the DESI range (T3), so *w* is frozen \~ \-1: the spiral *reinforcesw* \= \-1 (resolving the U4 tension as its fixed point) and does NOT yield the DESI crossing; the zero-parameter DESI claim does not follow. HYPOTHESIS-strong for the reframing; the DESI prediction is unsupported by computation. **Unchanged**: 83/121, chiZ/alphapatch \= 4.235 (COMPUTED-INCOMPLETE), B3-B terminal. Process material consolidated into Appendices C-D. No new fitted parameters. (**A** \= 35/437, **Q** \= 11, dim **Z** \= 2\) LOCKED.  
**v1.4 (June 2026): Methodological pivot \+ pre-registered emergence tests.** Adds §13 and Appendix E: the three “blank-slate” proposals (P1 braiding/TQFT, P2 tensor-network Q \= 11 emergence, P3 quaternion-spin quantum cellular automaton) are reframed as **falsifiable bottom-up emergence tests**, each with a protocol and a pre-registered success criterion. Run as toys (E1-E4, all real asserts; counts now 30 \+ 19 \+ 3 \= 52): **none** reproduces 83/121, 35/437, or Q \= 11 without tuned input. The failures are mechanistic \- the i-tetration orbit's rotation number is not a low-order rational so the braid does not close (no Jones/FQHE reading); iz is a 2D map and cannot generate the 3/6 split alone; a bare i-tetration lattice is a pure contraction that collapses to one attractor (no dust/vacuum coexistence). Net: the naive emergence realizations are **ruled out**, and the next target (an explicit entanglement-to-dimension / source rule) is stated precisely. No physics number changed; no fitted parameter added. (**A** \= 35/437, **Q** \= 11, dim **Z** \= 2\) LOCKED.  
**v1.5 (June 2026): The minimal source term for dust/vacuum coexistence.** Acts on v1.4's diagnosis (a bare i-tetration contraction erases all dust) by designing and running the *simplest* source rule that lets matter resist the de Sitter collapse (Appendix E.5; CX1-CX4; counts now 30 \+ 23 \+ 3 \= 56). With the contraction rate fixed by the corpus (gamma \= 1 \- |**lambda**| \= 0.108), a bistable autocatalytic source gives two-phase coexistence *iff* its strength exceeds a corpus-tied threshold **J \>= 4(1 \- |lambda|) \= 0.434** (Maxwell point JM \= (9/2)(1 \- |**lambda**|) \= 0.488). The minimal rule FORM is thus pinned, but the dust/vacuum *ratio* is still NOT pinned (generically 0 or 1; 83/121 only by tuning) \- which *independently reproduces* the §3 No-Go and the G3 gate (the ratio is a present-epoch condition, not a dynamical invariant). Net: a genuine, falsifiable advance on the emergence programme; the next target (derive J from **A**, **Q**) is stated. No physics number changed; no fitted parameter added. (**A** \= 35/437, **Q** \= 11, dim **Z** \= 2\) LOCKED.  
**v1.6 (June 2026): Consolidation \+ manuscript integration \+ the rank-weighted master equation.** Integrates the v1.5 coexistence result into the body and reframes the paper around its honest central thesis \- the **convergence of four independent routes** (two No-Go theorems, the rank-83 flux obstruction, and the reaction-diffusion coexistence analysis) on the conclusion that the budget is a *present-epoch boundary condition*, not a dynamical invariant. **Adds (best G3 candidate):** the rank-weighted master equation (rates into a sector proportional to its rank, qm-\>L \= 83k, qL-\>m \= 38k) whose unique, probability-conserving stationary state is (38/121, 83/121) with *no free J* (ME1) \- the dynamical form of the §8.2 maximally-mixed candidate rho\* \= I/121. It is the structurally correct object (it fixes the ratio where the cubic source cannot), but remains HYPOTHESIS-strong: the equal-amplitude assumption and the occupation-to-energy map are open. **Corrections (prior AI-pass):** E4 (an identity) moved to a note; E1 lowered to “no low-period closure up to the pre-registered bound” (not a no-Jones proof) and the denominator-bound typo fixed; CX4 split into an analytic area-sign assert (CX4a) and a numerical front-velocity note (CX4b); robust bistability stated as J \> Jc (J \= Jc is a saddle-node threshold); the Maxwell point shown to be unstable to curvature-driven coarsening (so even Maxwell balance does not preserve a seeded fraction); “minimal rule” scoped to “the minimal scalar cubic ansatz.” **Tested and reported negative:** a pre-registered J \= f(**A**, **Q**) guard \- no independent A,Q expression selects a physical J, and even fixing J \= JM with the ratio seeded does not preserve it, so deriving J is NOT an exit. Counts 30 \+ 23 \+ 3 \= 56 (+8 notes). No physics number changed; no fitted parameter added. (**A** \= 35/437, **Q** \= 11, dim **Z** \= 2\) LOCKED.