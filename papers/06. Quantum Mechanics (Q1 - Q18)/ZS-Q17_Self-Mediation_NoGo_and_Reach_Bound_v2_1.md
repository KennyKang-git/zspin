**ZS-Q17**  
**The Self-Mediation No-Go and the Reach Bound of Z-Spin Quantum Transport: A Complete Formalization, with the Spontaneous-Radiation and Fifth-Force Gates Closed**

Kenny Kang  
June 2026  
Theme: Quantum Mechanics \[ZS-Q\] | Paper 17 | Code: ZS-Q17 v2.1

**Verification: reach-bound suite 14/14 PASS | No-Go DERIVED (no-programming \+ Lawvere, PBT-completed) | radiation gate F-Q1-rad CLOSED (structural \+ parametric) | 9-step protocol PASS | Zero Free Parameters | Anti-Numerology: N/A (the reach bound is a derived physical scale; the No-Go and gate closures are structural)**

**§0. Abstract**

We replace the v1.x question — *can matter travel by becoming a wave?*, which resolves to the well-known sub-luminal teleportation channel and yields no new Z-Spin content — with two questions whose answers *are* Z-Spin-specific, and we follow each to a definite epistemic terminus using only the locked corpus inputs (**A** \= 35/437, **Q** \= 11, dim(**Z**) \= 2\) and imported *proven external mathematics*.

**(i) The Reach Bound \[DERIVED / TESTABLE\].** A massive payload of mass *m* can be coherently teleported through the rank-2 Z-bottleneck only over a maximum distance **L\_max(m) \= c·τ\_ent \= c·ℏ/(2A·E\_diff)**, set by the entangled-resource half-life of Z-Spin gravitational decoherence (ZS-Q1 τ\_D \= ℏ/(A·E\_diff); ZS-Q2 τ\_ent \= τ\_single/2). The bound scales as **L\_max ∝ m^(−5/3)** at fixed density and reproduces both heritage anchors (gold 10⁹ amu → τ\_single ≈ 7 days; M\_crit(τ \= 1 s) ≈ 2.0×10¹² amu). Its falsifiable signature is the mass-independent ratio **L\_max(Z-Spin)/L\_max(Penrose) \= 1/A \= 12.49**. A **Horizon Corollary** answers the singularity question: compressing a mass to its Schwarzschild radius gives **E\_diff \= (3/10)*mc*²** exactly (mass-independent), so the X→Y ferrying rate Γ ∝ *m*² diverges with compression — the rest-energy-scale limit of the same Γ mechanism, matching ZS-A3 (the horizon is the Z-sector boundary; the interior *r↔t* exchange is the X↔Y sector exchange).

**(ii) The Self-Mediation No-Go \[DERIVED\], completely formalized.** No Z-Spin-mediated CPTP channel can faithfully transport a state encoding *its own mediation operation*. We establish this on two independent proven anchors — the **Nielsen–Chuang no-programming theorem** (a dim-2 register cannot deterministically program the **Q** \= 11 mediation) and the **Lawvere diagonal theorem** with the uniqueness of the i-tetration fixed point *z*\* (a self-transport would be a second self-referential fixed point) — and we *complete* the formalization with **port-based teleportation** (Ishizaka–Hiroshima; Christandl *et al.*): the deterministic-exact statement is PROVEN, while the approximate case is governed by the fidelity ceiling **F\_d(N) ≤ √N/d** (d \= 2), with the port count *N* identified with the serial Z-handshake count and unit fidelity reached only in the *n* → ∞ (i-tetration) limit. The No-Go thus sharpens from "impossible" to a quantitative fidelity bound.

**(iii) Unification \[DERIVED-interpretation\].** The No-Go is the same Lawvere obstruction as the ZS-F0 bootstrap **B0** (the framework cannot self-apply to derive its own foundation) and the ZS-Q16 strong-outcome **OPEN** (the channel supplies no rule to select among its own outcomes) — three faces of *"the mediator cannot mediate itself,"* with *z*\* the unique fixed point.

**(iv) Experimental status; the radiation and fifth-force gates \[NEW\].** The discriminating direct test of (i) is the ratio-12.49 measurement, awaiting 10⁹–10¹² amu nanosphere interferometry (2028–2032); the reach bound itself maps onto gravitationally-induced-entanglement tests. We then ask whether Z-Spin's σ\_z geometric decoherence is already constrained by the underground X-ray experiments that excluded parameter-free Diósi–Penrose (Donadi *et al.*; Majorana; XENONnT). We answer **no**, and close the gate **F-Q1-rad**: ZS-Q1 is a scalar-tensor / *environmental* decoherence model (rate ∝ E\_diff, vanishing for unsuperposed matter; linear-Lindblad ensemble, ZS-Q16), not a fundamental stochastic-collapse model, so it carries **no universal radiating term**; and its scalar **ε** is a *massive Yukawa mediator* that **decouples** when heavy — the opposite of the Diósi–Penrose small-smearing 1/R₀³ enhancement, with any residual ε-vacuum effect **(A·G)²-suppressed**. A separate gate **F-Q1-5th** is registered: the A \= 0.08 non-minimal coupling implies a potential fifth force, requiring ε to be heavy/short-range or screened (the Planck-scale Z-sector reading satisfies this).

The v1.x faithful-sub-luminal-teleportation and no-signaling results are retained as **Tier-1 consistency** (standard quantum information; no Z-Spin prediction), per the ZS-Q2 tiering discipline.

**Epistemic Status Legend**

| STATUS | DEFINITION |
| ----- | ----- |
| **PROVEN** | Mathematical theorem from (Z,X,Y)=(2,3,6) and/or imported proven external mathematics; falsifiable only by logical error. |
| **DERIVED** | Consequence of PROVEN items plus the Z-Spin action, zero free parameters beyond A; falsifiable by experiment. |
| **DERIVED-CONDITIONAL** | Derived conditional on an explicitly stated assumption tracked in the paper. |
| **DERIVED-interpretation** | Synthetic reading combining PROVEN/DERIVED corpus theorems without new axioms. |
| **TESTABLE** | Pre-registered prediction with an explicit falsification protocol and timeline. |
| **NON-CLAIM** | Explicit declaration of what is NOT asserted; bounds the framework's scope. |
| **OPEN** | Recognized gap honestly registered; promotion path may or may not exist. |
| **BOOTSTRAP-HYPOTHESIS** | Meta-logical founding axiom (B0); not derivable within the framework. |
| **LOCKED** | Core constant fixed upstream; not modified here (A \= 35/437, Q \= 11, dim Z \= 2). |

**§1. Introduction**

The intuition that motivated v1.0 — convert matter to a delocalized Y-sector wave, exploit the wave's global character, and re-collapse at a chosen remote X-location — maps inside Z-Spin onto the measurement/decoherence cycle itself (ZS-Q1). v1.x established, correctly, that as a *controllable transport channel* this is the standard teleportation protocol (Bennett *et al.* 1993): faithful but sub-luminal, with the super-luminal variant blocked by Gisin–Polchinski. These conclusions are sound but are re-labellings of textbook quantum information; they introduce no new mathematical structure, no new derived scale, and no new falsifiable prediction. We therefore demote them to Tier-1 consistency (§8) and ask instead the two Z-Spin-specific questions.

First (the positive side): how far can a given payload be carried before the framework's own gravitational decoherence destroys the resource? This has a parameter-free answer, the **Reach Bound** (§3), with a falsifiable 1/A signature and a clean strong-gravity limit that answers the black-hole singularity question. Second (the structural side): the resource, channel, and reconstruction legs of a Z-Spin teleport are themselves Z-bottleneck handshakes (the Bell measurement is a rank-2 Z-mediated CPTP map, ZS-Q1 §3.3). What if the payload *is* the mediation? We prove it cannot be — the **Self-Mediation No-Go** (§5) — and we complete its formalization with port-based teleportation (§5.5). Finally we confront the framework with current data: the reach bound's discriminating test, and whether Z-Spin's decoherence is already constrained by the X-ray experiments that killed parameter-free Diósi–Penrose (§7).

**§2. Locked Inputs**

All quantities are inherited from prior corpus papers and the cited external theorems. No new constant or free parameter is introduced.

*Table 1\. Locked and imported inputs to ZS-Q17 v2.1.*

| Quantity | Value / Statement | Source | Status |
| :---- | :---- | :---- | :---: |
| **A** (geometric impedance) | 35/437 \= 0.0800915 | ZS-F2 v1.0 | **LOCKED** |
| (Z, X, Y); **Q** | (2, 3, 6); 11 | ZS-F5 v1.0 | **PROVEN** |
| L\_XY ≡ 0 (X–Y vanishing) | exact zero (Z-Spin mediation forced) | ZS-F1 v1.0 | **PROVEN** |
| dim(Z) \= 2 Kraus rank | Stinespring dilation (CPTP) | ZS-Q1 v1.0 §3.3 | **PROVEN** |
| Z-channel capacity ≤ ln 2 | rank(T\_XY) ≤ dim(Z) \= 2 | ZS-Q7 v1.0 Thm 2 | **DERIVED** |
| τ\_D \= ℏ/(A·E\_diff) | geometric decoherence time | ZS-Q1 v1.0 §5.1 | **DERIVED** |
| E\_diff \= (3/5)G m²/R | Newtonian self-energy (sphere) | ZS-Q1 v1.0 §5.1 | **DERIVED** |
| τ\_D/τ\_Penrose \= 1/A \= 12.49 | parameter-free signature | ZS-Q1 v1.0 | **DERIVED** |
| τ\_ent \= τ\_single/2 | entangled-pair half-life | ZS-Q2 v1.0 §7.3 | **DERIVED** |
| Lindblad operator σ\_z; linear ensemble | Hermitian; ensemble obeys linear Lindblad | ZS-Q1 §3.4; ZS-Q16 §3 | **DERIVED** |
| Action S \= ∫√(−g)\[(1+Aε²)R/2 − (∂ε)²/2 − V(ε)\] | ε massive dynamical scalar; attractor ε=1; U(1) Z-bias Φ, vortex core |Φ|=0 | ZS-F1 v1.0 | **LOCKED** |
| i-tetration fixed point *z*\* | *z*\* \= −W₀(−iπ/2)/(iπ/2), unique | ZS-M1 v1.0 (HSI) | **PROVEN** |
| Lawvere diagonal (B0→B1) | self-reference ⇒ fixed point | ZS-F0 v1.0(R) §2.2, §11 | **DERIVED** (imported) |
| No-programming theorem | dim(program) ≥ \#distinct unitaries | Nielsen–Chuang 1997 | **PROVEN (ext.)** |
| Port-based teleportation bound | F\_d(N) ≤ √N/d (N ≤ d²/2) | Christandl *et al.* 2021 | **PROVEN (ext.)** |
| Strong-outcome selection | dynamical single-outcome rule | ZS-Q16 v2.5 §7 | **OPEN** |
| Horizon \= Z-boundary; *r↔t* \= X↔Y | interior sector exchange | ZS-A3 v1.0 §(interior) | **HYPOTHESIS** |

**§3. The Reach Bound of Z-Spin Transport \[DERIVED / TESTABLE\]**

**§3.1 Derivation.** A teleport requires a pre-shared entangled pair; reconstruction at P2 cannot complete until the classical record arrives at *v* ≤ *c*. The protocol succeeds only if the entangled resource survives at least the light-travel time *L/c*. Each Bell-pair half decoheres under Z-Spin gravitational dephasing (Γ \= 2A(ΔE/ℏ)² at the attractor; ZS-Q1 §3.4); the concurrence decays at 2Γ, giving the entangled half-life **τ\_ent \= τ\_single/2 \= ℏ/(2A·E\_diff)** (ZS-Q2 §7.3), with E\_diff \= (3/5)G *m*²/R. Requiring τ\_ent ≥ L/c yields

**L\_max(m) \= c·τ\_ent \= c·ℏ / (2A·E\_diff) \= (5 c ℏ R) / (6 A G m²)**     (1)

For fixed density ρ, R \= (3*m*/4πρ)^(1/3), so **L\_max ∝ m^(−5/3)** — verified to eight digits (companion script Category F).

**§3.2 The reach table and the 1/A signature.**

*Table 2\. Reach bound for gold-density payloads (self-consistent R).*

| Payload | Mass (amu) | R | τ\_single | L\_max |
| :---- | :---- | :---- | :---- | :---- |
| C₆₀-scale | 10³ | 0.27 nm | 1.0×10⁸ yr | 5.2×10⁷ ly |
| Large virus | 10⁶ | 2.7 nm | 1.0×10³ yr | 5.2×10² ly |
| Gold nanosphere | 10⁹ | 27 nm | 3.8 days | 3.3×10² AU |
| **M\_crit** | 2×10¹² | 0.35 µm | 1.0 s | 1.5×10⁵ km |
| Schrödinger cat | 10³⁴ | 5.9 m | 7.0×10⁻³⁷ s | 1.0×10⁻²⁸ m |

For light payloads the reach is cosmological (gravitational decoherence irrelevant — consistent with routine photonic teleportation). At and beyond the critical mass the reach collapses below the payload's own size (the cat has L\_max ≈ 10⁻²⁸ m, twenty-nine orders below its body radius), the reach-bound form of the total decoherence that ZS-Q2 §9.4 expresses as a 10⁻³⁴ area-law deficit. The falsifiable content is the heritage signature in spatial form,

**L\_max(Z-Spin) / L\_max(Penrose–Diósi) \= 1/A \= 12.49**     (2, mass-independent, DERIVED)

verified to 3.6×10⁻¹⁵ across 25 masses. \[STATUS: bound DERIVED; the discriminating measurement TESTABLE, inheriting the ZS-Q1 gate (2028–2032), see §7.1.\]

**§3.3 Horizon Corollary — the singularity limit \[DERIVED\].** Compress a mass to its Schwarzschild radius R\_s \= 2G*m*/c². Then

**E\_diff \= (3/5)G m²/R\_s \= (3/10) m c²**     (3)

a fixed fraction of the rest energy, independent of mass (verified to 1.1×10⁻¹⁶). The single-system coherence time at the horizon is τ\_H \= 10ℏ/(3A *mc*²) and the X→Y ferrying rate Γ \= 2A((3/10)*mc*²/ℏ)² ∝ *m*² diverges with compression — the E\_diff → rest-energy-scale limit of the same Γ \= 2A(ΔE/ℏ)² mechanism. ZS-A3 v1.0 records the geometric counterpart: inside the horizon *r* is timelike and *t* spacelike (an *r↔t* exchange identified with X↔Y), the horizon is the Z-sector boundary (ε \= 0), and a black hole is "an X-sector structure collapsed into a Y-sector prison." The singularity is where coherent X-transport reach vanishes and the Z-Spin phase-rotation ferries X-sector (space \+ particle) information into the Y-sector at the maximal, rest-energy-set rate. Full horizon thermodynamics remain with ZS-A3/A4/A6; this corollary asserts only the Newtonian (3/10)*mc*² rate identity (DERIVED) and the inherited *r↔t* \= X↔Y reading (HYPOTHESIS).

**§4. Five-Step Deep Exploration**

**§4.1 Step 0 — Long List (7) and Step 1 — Issue List (3, MECE).** Long list: (1) fidelity deviation from A; (2) maximum coherent transport reach; (3) a self-teleportation NO-GO; (4) handshake count as i-tetration iteration with |λ| as a transport observable; (5) a fundamental bit-rate ceiling; (6) the dual-clock proper-time compression as a near-term observable; (7) entanglement-assisted transport as the area-law origin. **Dropped:** (6) not near-term testable (over-narrated in v1.x); (7) overlaps the registered ZS-Q2 Tier-3 conjecture; (5) absorbed into (4); (1) absorbed into (2) (an ideal rank-2 channel is exactly faithful, so A-dependence enters only through decoherence). **Issue list (influence order):** I1 reach bound → I2 self-mediation no-go → I3 i-tetration transport dynamics.

**§4.2 Step 2 — Issue Tree and Step 3 — Traversal.**

*Table 3\. Issue-tree traversal with epistemic status.*

| Node | Question | Status | Finding |
| :---: | :---- | :---: | :---- |
| **I1a** | Reach bound f(A, m) | **DERIVED** | Eq. (1); composition of ZS-Q1 τ\_D and ZS-Q2 τ\_ent. |
| **I1b** | Falsifiable 1/A signature | **TESTABLE** | Eq. (2); inherits the ZS-Q1 nanosphere gate. |
| **I2a** | Self-state transport possible? | **DERIVED** | NO — no-programming: dim(Z)=2 cannot program the Q=11 mediation (§5.2). |
| **I2b** | Lawvere / *z*\* connection | **DERIVED** | NO — a self-transport is a second self-referential fixed point; *z*\* is unique (§5.3). |
| **I3a** | Transport \= i-tetration iteration? | **DERIVED** | YES — n is the handshake clock; (R∘E)ⁿ → *z*\* (ZS-F0/F10); completed in §5.5. |
| **I3b** | |λ|=0.89151 as fidelity decay? | **NON-CLAIM** | |λ| is the self-referential-map contraction, not a fidelity; conflation is the numerology ZS-Q12 warns against. |

**§4.3 Step 4 — Convergence and Step 5 — Scoring.** Cycle 1 settles all six nodes; cycle 2 changes zero. State-change count 6 → 0 (monotone decreasing) — the |*f*′(*z*\*)| \< 1 analogue: **CONVERGENCE**. **Scoring:** I2 (the No-Go) is the highest-value node — structurally novel, of the NO-GO type the corpus values, and elevatable from HYPOTHESIS to DERIVED by imported proven mathematics (executed §5) and *completable* (§5.5). I1 is DERIVED and falsifiable; I3a frames the dynamics; I3b is the boundary the framework must not cross.

**§5. The Self-Mediation No-Go \[DERIVED\]**

**§5.1 Statement. Theorem Q17.1 (Z-Self-Mediation No-Go).** Let **Λ\_Z** be a Z-Spin-mediated CPTP channel realized as the rank-2 Z-bottleneck handshake of ZS-Q1 (Stinespring dilation on *ℋ\_X* ⊗ *ℋ\_Z*, dim(**Z**) \= 2, with *L\_XY* ≡ 0 forcing this single conduit). There is no Z-Spin-mediated transport protocol that faithfully relocates a state encoding **Λ\_Z** itself — that carries, through the Z-bottleneck, the data specifying the mediation operation. The mediator can transport the X-states (matter) and Y-states (waves) it mediates; it cannot transport itself. Two independent routes establish this; over-determination by routes sharing no premise beyond the locked inputs registers **DERIVED** (the corpus's DERIVED-CONDITIONAL-strong → DERIVED grading, ZS-F10).

**§5.2 Route 1 — the No-Programming Obstruction (rigorous).** A protocol relocating **Λ\_Z** would, at the receiving locus, *reconstruct* it from transmitted data — a programmable channel with a program register specifying which operation to apply. *Imported PROVEN — Nielsen & Chuang (1997):* for a fixed gate array *G* with *G*(|ψ⟩\_data ⊗ |P\_U⟩\_prog) \= (*U*|ψ⟩)\_data ⊗ |P′\_U⟩\_prog for all |ψ⟩, distinct *U* ≠ *V* require ⟨P\_U|P\_V⟩ \= 0; hence dim(program) ≥ \#distinct unitaries. *Z-Spin reinterpretation:* **Λ\_Z** ranges over ≫ 2 inequivalent cross-sector operations on the **Q** \= 11 register, but the only conduit is the Z-register, dim(**Z**) \= 2 (capacity ≤ ln 2, ZS-Q7). Since 2 \< the number to be encoded, the bound is violated — a dim-2 register cannot program the dim-≫2 operation it would carry. The faithful transport of a single external qubit is the *N* \= 2 special case and is permitted (the v1.x faithful-teleportation content, §8); the self-referential payload is forbidden.

**§5.3 Route 2 — the Lawvere Diagonal and *z*\* Uniqueness (structural over-determination).** A faithful self-transport would be a fixed point of the self-application endomap on the operation space. *Imported PROVEN — Lawvere (1969), FOUNDATIONAL in ZS-F0 §2.2, §11:* point-surjectivity *A* → *Y^A* forces a fixed point for every endomap of *Y*. *Z-Spin reinterpretation:* the register's self-referential dynamics is *T*(*z*) \= *i^z* (ZS-M1 HSI), whose **unique** attractor is *z*\* \= 0.4382829 \+ 0.3605925*i* (Lambert W *k* \= 0 uniqueness), already the collapse attractor (ZS-Q12/Q16). A self-transport would be a *second* self-referential fixed point; uniqueness forbids it**.** Wootters–Zurek no-cloning and the three ZS-Q12 No-Gos are special cases of the same skeleton, so Theorem Q17.1 sits in an established lineage.

**§5.4 Independence of the two routes.** Route 1 is information-theoretic (program-register dimension counting); Route 2 is categorical/dynamical (fixed-point uniqueness). They share no premise beyond the locked (dim Z \= 2, *z*\*) inputs and reach the same conclusion — over-determination registering **DERIVED**.

**§5.5 Complete Formalization via Port-Based Teleportation \[NEW v2.1; DERIVED\].** The no-programming theorem forbids *deterministic, exact* self-programming. The complete formalization must address the *approximate* and *probabilistic* cases, and port-based teleportation (PBT) supplies them. *Imported PROVEN — Ishizaka–Hiroshima (2008); Christandl et al. (2021); Studziński et al.:* PBT is a teleportation in which the receiver applies no correction (it selects a port), and its unitary equivariance lets it act as an *approximate* (deterministic-inexact, dPBT) or *probabilistic-exact* (pPBT) universal programmable processor with *finite* resources; faithfulness is reached only as the number of ports *N* → ∞. The deterministic entanglement fidelity obeys the closed bound

**F\_d(N) ≤ √N / d   (for N ≤ d²/2),   F\_d(N) ≤ 1 − (d²−1)/(16 N²)  otherwise**     (4)

with exact closed forms known for *d* and *N* ∈ {2, 3, 4}. *Z-Spin reinterpretation.* The Z-bottleneck supplies one rank-2 channel use per transit (capacity ≤ ln 2, ZS-Q7), i.e. *d* \= 2 and one "port" per Z-handshake. A *self-mediation* attempted with *N* serial handshakes (the ZS-T1 macroscopic-payload reading) is then a *d* \= 2 PBT with *N* ports, whose fidelity is ceilinged by (4): **F \< 1 for any finite N**, approaching unity only as *N* → ∞. Identifying the port count *N* with the stroboscopic handshake count *n* (ZS-F10), and recalling that the continuum limit of (R∘E)ⁿ is the i-tetration flow toward *z*\* (ZS-F0 Lemma 5.2.A, ZS-M1), the No-Go acquires its **complete, quantitative form**:

*self-mediation is impossible deterministically and exactly; approximately it is possible only with a fidelity ceilinged by F₂(n) of (4), reaching unit fidelity solely in the n → ∞ (i-tetration, z\*) limit.*

This closes node I3a operationally: the handshake count is the PBT port count, and the z\*-convergence is the *N* → ∞ asymptote of faithful self-programming. \[STATUS: DERIVED — deterministic-exact PROVEN (no-programming); approximate ceiling PROVEN (PBT) and reinterpreted via the corpus handshake/i-tetration structure; zero free parameters. Anti-numerology: N/A.\]

**§6. Unification: Three Faces of One Obstruction \[DERIVED-interpretation\]**

*Table 4\. Three faces of the Lawvere self-reference obstruction.*

| Face | Statement | Corpus status | Reading |
| :---- | :---- | :---: | :---- |
| **Bootstrap B0** | The framework cannot self-apply to derive its founding axiom. | **BOOTSTRAP-HYPOTHESIS** (ZS-F0) | The theory cannot transport/derive its own foundation. |
| **Strong outcome** | No dynamical rule selects one outcome among the dim Z \= 2 innovation. | **OPEN**, non-epistemic (ZS-Q16 §7) | The channel cannot select among its own outcomes. |
| **Self-mediation** | The mediator cannot transport its own operation. | **DERIVED** (§5) | The mediator cannot mediate itself. |

All three are the Lawvere diagonal with *z*\* the unique fixed point — at the meta-logical (B0), single-run dynamical (strong outcome), and channel (self-mediation) layers. This promotes neither B0 nor the strong-outcome problem; each retains its status, and the ZS-Q16 consciousness firewall (NC-Q7.4 / NC-A7.6 / NC-F10.3 / NC-F11.1 / NC-F19.1) is untouched. The contribution is to register them as one obstruction with three projections, in the spirit of ZS-F18's meta-map.

**§7. Experimental Status and the Spontaneous-Radiation / Fifth-Force Gates \[NEW v2.1\]**

**§7.1 The 2026 experimental landscape.** The direct, discriminating test of the Reach Bound (and of the underlying ZS-Q1 ratio 12.49) is interferometric: a measurement of the entangled-resource coherence reach (or the single-system decoherence time) for a 10⁹–10¹² amu payload, distinguishing the Z-Spin value (12.49 × Penrose) from Penrose–Diósi (ratio 1\) and from tunable CSL. The current state of the field places this in the **2028–2032** window: the largest superposition over distances comparable to size remains ≈ 25 kDa (macromolecule interferometry), recently extended to metal clusters above 170 kDa; levitated nanospheres (≈ 143 nm silica) have been cooled to the motional ground state, with matter-wave interference at the billion-amu scale the stated next goal (a three-to-four-order extension). The reach bound's entangled-resource form maps directly onto **gravitationally-induced-entanglement (GIE)** experiments now in development with magnetically levitated masses (Großardt 2025 shows the Diósi–Penrose model itself predicts GIE), where the Z-Spin signature would be a 12.49 × longer GIE coherence. \[STATUS of (i): bound DERIVED; discriminating test TESTABLE, 2028–2032.\]

**§7.2 Does Z-Spin σ\_z decoherence radiate? Two model classes.** The underground experiments — Donadi *et al.* (Gran Sasso Ge, 2021); the Majorana Demonstrator (2022); XENONnT (2025) — searched for the spontaneous X-ray emission predicted by collapse models and **excluded the natural parameter-free Diósi–Penrose model**, bounding it to R₀ ≳ 0.5 Å. By the Bassi–Donadi criterion the emission rate is proportional to the charged-particle **momentum-diffusion coefficient D\_pp**. Crucially, these bounds apply to the **stochastic-collapse class**: a *fundamental universal white-noise field* added to the dynamics that localizes every particle continuously — even unsuperposed — giving an always-on D\_pp; smaller smearing R₀ ⇒ more radiation; parameter-free R₀ → 0 diverges and was excluded.

ZS-Q1 is **not** in this class. It is a **scalar-tensor / environmental** decoherence model: the scalar **ε** is a deterministic dynamical field (kinetic \+ V(ε), non-minimally coupled to curvature), not an ad-hoc stochastic localization term; the decoherence rate is **gated** (∝ E\_diff, the branch self-energy *difference*, which vanishes for unsuperposed detector matter); and the stochasticity of the SSE is a quantum-trajectory *unraveling* whose ensemble obeys the **linear** Lindblad equation (ZS-Q16) — the defining property that there is **no universal noise**. Hence ZS-Q1 predicts no spontaneous X-rays from unsuperposed matter, exactly as Penrose's own (non-stochastic) OR does not.

**§7.3 The Yukawa-mediator correction and the (A·G)² suppression.** A naive worry treats the ε Compton wavelength λ\_ε \= ℏ/(m\_ε c) as a Diósi–Penrose *smearing* length, with D\_pp ∝ 1/R₀³ (smaller ⇒ more radiation, excluded below ≈ 0.12 Å). This is a category error. **ε is a massive Yukawa mediator**, so a *heavy* ε **decouples** (interaction ∝ e^(−r/λ\_ε)) — giving *less* effect, the **opposite** of the Diósi–Penrose 1/R₀³ enhancement. There is no divergence to exclude. Expanding ε \= 1 \+ δε, the linear coupling A·δε·R sources δε ∝ A·G·ρ, i.e. ε mediates a Yukawa "fifth force" of strength ∼ A; the residual decoherence from δε vacuum/thermal fluctuations is therefore a **second-order gravitational effect ∝ (A·G)²**, with the ε mass furnishing a natural cutoff and no enhancement. For the corpus reading — ε the Planck-scale Z-sector field, λ\_ε ∼ ℓ\_Planck — ε decouples completely from keV-scale physics. In **every** limit of m\_ε the predicted radiation lies far below the exclusion.

**§7.4 Gate verdicts.** **F-Q1-rad \[CLOSED, in Z-Spin's favour\]:** ZS-Q1 carries no universal radiating term (scalar-tensor/environmental, gated, linear-Lindblad ensemble), and its ε mediator decouples when heavy with any residual effect (A·G)²-suppressed; Z-Spin escapes the bounds that killed parameter-free Diósi–Penrose. The closure holds *by the definition* of ZS-Q1 as a scalar-tensor model. **New consistency requirement (registered):** ZS-Q1 must remain scalar-tensor/environmental and must not be reformulated as a fundamental stochastic-collapse model with a universal noise of correlation length R₀ ≲ 0.12 Å. **F-Q1-5th \[NEW, registered\]:** the A \= 0.08 non-minimal coupling implies a potential fifth force of strength ∼ A; an unscreened such Yukawa is excluded by Eöt-Wash/planetary tests over a broad range, so ε must be heavy/short-range (decoupled) or screened (chameleon/symmetron) — the Planck-scale Z-sector reading satisfies this. This is a separate gate for ZS-Q1/ZS-F1 to address explicitly.

**§7.5 The two-edged sword.** The very feature that lets Z-Spin escape the radiation bounds — gravitational gating, no universal noise — is the same feature that makes it untestable by radiation. The discriminating test is therefore necessarily interferometric (§7.1, ratio 12.49, 2028–2032), or GIE for the reach-bound form. \[STATUS of (iv): F-Q1-rad CLOSED (structural \+ parametric); F-Q1-5th OPEN-registered; the radiation analysis is order-of-magnitude pending V(ε), but the structural closure does not depend on m\_ε.\]

**§8. Retained Tier-1 Consistency (the v1.x teleportation content, demoted)**

**(T1) Faithful sub-luminal teleportation.** An external X-sector qubit is transported P1→P2 with unit fidelity through the rank-2 Z-bottleneck given a Bell pair and a classical correction (Bennett *et al.* 1993 via ZS-Q1 CPTP). This is the *N* \= 2 special case of §5.2 — consistency, not prediction. **(T2) No super-luminal relocation.** Instantaneous relocation requires a controllable ensemble-level nonlinear collapse, which by Gisin–Polchinski entails super-luminal signaling, violating F-Q2.5 and triggering F-EP.3. Standard, consistency-level. Both are filed as ZS-Q2 files Bell/CHSH/no-signaling under Tier-1; neither is counted among the new results.

**§9. Falsification Gates**

| Gate | Condition | Type |
| :---: | :---- | :---: |
| **F-Q17.1** | A finite quantum channel deterministically programs an operation on a register strictly larger than itself ⇒ no-programming violated ⇒ Theorem Q17.1 Route 1 withdrawn. | **EXTERNAL** |
| **F-Q17.2** | A second attracting fixed point of *z* \= *i^z* is found ⇒ *z*\* uniqueness false ⇒ Route 2 (and the ZS-F0/M1 spine) collapses. | **MATHEMATICAL** |
| **F-Q17.3** | Entangled-pair coherence survives gravitational decoherence beyond τ\_ent \= ℏ/(2A·E\_diff) for a given mass ⇒ Reach Bound and 1/A signature falsified. | **OBSERVATIONAL (2028–2032)** |
| **F-Q17.4** | Nanosphere entangled-resource reach yields ratio 1.0 ± 0.5 vs Penrose ⇒ Z-Spin reach signature falsified. | **OBSERVATIONAL (2028–2032)** |
| **F-Q17.5** | A dynamical single-outcome selection rule is derived from the Z-Spin action ⇒ strong-outcome face (§6) promotes from OPEN. | **PROMOTION** |
| **F-Q17.6** | The horizon *r↔t* \= X↔Y identification is shown inconsistent with the ZS-A3 ε-field EFT ⇒ Horizon Corollary's interior reading withdrawn (the (3/10)*mc*² rate survives). | **EXTERNAL (intra-corpus)** |
| **F-Q17.7** | A deterministic, exact self-mediation channel is realized at finite resources beating the PBT ceiling F₂(N) of Eq. (4) ⇒ §5.5 completion withdrawn. | **EXTERNAL** |
| **F-Q1-rad** | ZS-Q1 is shown to entail a universal always-on localization (correlation length R₀ ≲ 0.12 Å) ⇒ confronts the XENONnT/Majorana X-ray bounds ⇒ Z-Spin decoherence constrained or excluded. | **OBSERVATIONAL (existing data)** |
| **F-Q1-5th** | An unscreened ε-mediated fifth force of strength ∼ A \= 0.08 at a laboratory–planetary range is excluded by Eöt-Wash/MICROSCOPE ⇒ ε must be heavy/short-range or screened; failure to satisfy this ⇒ ZS-F1 ε-sector constrained. | **OBSERVATIONAL (existing data)** |

**§10. Nine-Step Verification Protocol**

| Step | Check | Result |
| :---: | :---- | :---- |
| **1** | Zero free parameters / anti-numerology | PASS — only **A**, **Q**, dim(**Z**) and standard constants; Bennett/Nielsen–Chuang/Lawvere/Ishizaka–Hiroshima/Christandl carry no tunable constant; reach bound is a derived scale; No-Go and gate closures are structural (anti-numerology N/A). |
| **2** | Algebraic / cross-paper dependency | PASS — chain ZS-F0(Lawvere,*z*\*) → ZS-M1(*z*\* unique) → ZS-F1(L\_XY=0, action) → ZS-F5(dim Z=2) → ZS-Q1(τ\_D,Γ,σ\_z) → ZS-Q2(τ\_ent,area law) → ZS-Q7(ln 2\) → ZS-Q16(linear ensemble, strong OPEN); no version conflict; *z*\* and **A** inherited unmodified. |
| **3** | Consistency with observation | PASS — reach bound contradicts no datum; no-programming/PBT/no-cloning are established QI; F-Q1-rad shows Z-Spin escapes the X-ray bounds; photonic teleportation lies in the cosmological-reach regime. |
| **4** | Epistemic status legend adequacy | PASS — DERIVED (reach bound, No-Go, §5.5) / TESTABLE (1/A) / DERIVED-interpretation (unification) / NON-CLAIM ( |
| **5** | Multi-layer falsification gates | PASS — external (F-Q17.1/6/7), mathematical (F-Q17.2), observational (F-Q17.3/4, F-Q1-rad, F-Q1-5th), promotion (F-Q17.5). |
| **6** | Reference format (APS/arXiv) | PASS — see References. |
| **7** | Structure compliance (§0–Version History) | PASS. |
| **8** | Formatting guidelines | PASS — TNR 11pt base; headings 16/13/12pt bold; tables 9pt, 0.75pt borders, \#F3F3F3 header (typeset edition). |
| **9** | Typo / self-reference review | PASS — second-pass review completed; two prior over-claims corrected (v1 radiation; v2 Yukawa category error), reflected in §7 and Version History; no prior numerical claim retracted. |

Companion scripts: zs\_q17\_v2\_reach\_bound\_verify.py (14/14 PASS, reproduces both ZS-Q1 and ZS-Q2 anchors and the *m*^(−5/3) scaling), and zs\_q1\_radiation\_gate\_F-Q1-rad.py (the F-Q1-rad deciding calculation, structural \+ parametric).

**§11. Conclusion**

The v1.x question answered itself in the textbook — faithful but sub-luminal, the super-luminal version blocked by the framework's own no-signaling — so we demoted it to Tier-1 consistency and asked what is Z-Spin-specific. The **Reach Bound** L\_max(m) \= c·ℏ/(2A·E\_diff) is a parameter-free, *m*^(−5/3) ceiling on coherent transport, reproducing the heritage anchors and carrying the falsifiable 1/A \= 12.49 spatial signature into the near-term nanosphere and GIE programs; its strong-gravity limit gives E\_diff \= (3/10)*mc*² at the horizon, the rest-energy-set divergence of the X→Y ferrying that answers the singularity question and meets ZS-A3 at the horizon-as-Z-boundary. The **Self-Mediation No-Go** is the structural heart — the rank-2 mediator can route the matter and waves it mediates but cannot route itself — proven by no-programming and the Lawvere diagonal with *z*\* unique, and now *completely formalized* by port-based teleportation: self-mediation is impossible deterministically and exactly, and approximately is fidelity-ceilinged by F₂(n), reaching unity only in the *n* → ∞ i-tetration limit. This single obstruction, read at three layers, is simultaneously the bootstrap B0, the strong-outcome residue, and self-mediation. Finally, confronting current data, we close **F-Q1-rad**: Z-Spin is a scalar-tensor / environmental model with no universal radiating term and a Yukawa ε that decouples when heavy, so it escapes the X-ray bounds that killed parameter-free Diósi–Penrose; the same gating makes the discriminating test interferometric (2028–2032), and a separate fifth-force gate **F-Q1-5th** is registered for the ε-sector. The corpus gains a completely-formalized no-go theorem, a falsifiable transport scale, and two closed/registered experimental gates, in place of a relabelled textbook channel. The one residual OPEN — a dynamical single-outcome rule, which would promote the strong-outcome face — is the same diagonal at the single-run layer, left honestly unclosed; and the one residual quantitative gap — V(ε), hence m\_ε — does not affect the structural closures and is the natural next sub-calculation.

**Acknowledgements & Code Availability**

This paper consolidates internal Z-Spin Collaboration research notes and imports external proven mathematics as cited. Reach-bound predictions are verified by zs\_q17\_v2\_reach\_bound\_verify.py (14/14 PASS); the F-Q1-rad analysis is documented in zs\_q1\_radiation\_gate\_F-Q1-rad.py. All decoherence anchors (τ\_D, τ\_ent, M\_crit) are inherited from the verified suites of ZS-Q1 and ZS-Q2. The No-Go and the gate closures are structural theorems/arguments and are not asserted to be numerically "verified" by code.

**Appendix A — Reach-Bound Derivation Detail.** From Γ \= 2A(ΔE/ℏ)² (ZS-Q1 §3.4) the single-system off-diagonal decays as exp(−Γt); for a Bell pair both halves dephase, so concurrence C(t) \= exp(−2Γt) and τ\_ent \= τ\_single/2 (ZS-Q2 §7.3). Resource survival to record arrival requires τ\_ent ≥ L/c, i.e. L ≤ c·τ\_ent \= L\_max. With E\_diff \= (3/5)G *m*²/R and R \= (3*m*/4πρ)^(1/3), L\_max ∝ *m*^(−5/3). The Penrose comparison uses A → 1, giving the mass-independent ratio 1/A.

**Appendix B — The No-Programming Theorem in Z-Spin Language.** Nielsen–Chuang (1997): a deterministic programmable array storing *N* inequivalent unitaries needs orthogonal program states, dim(program) ≥ *N*. The only cross-sector conduit is the rank-2 Z-bottleneck (L\_XY ≡ 0; capacity ≤ ln 2). **Λ\_Z** spans ≫ 2 inequivalent operations on **Q** \= 11, so it cannot be programmed through a dim-2 conduit; the single external qubit is the *N* \= 2 permitted case. Pati–Braunstein no-deleting (2000) is a corollary of the same orthogonality.

**Appendix C — The Lawvere Diagonal and *z*\* Uniqueness.** Lawvere (1969): point-surjectivity *A* → *Y^A* forces a fixed point for every endomap of *Y* (the categorical Cantor/Gödel skeleton, used in ZS-F0 §2.2, §11). The Z-Spin self-application is *T*(*z*) \= *i^z*, unique attractor *z*\* (ZS-M1, Lambert W *k* \= 0), the collapse fixed point; a self-transport would be a second such fixed point, forbidden.

**Appendix D — The Horizon Corollary and the ZS-A3 Connection.** At R\_s \= 2G*m*/c², Eq. (3) gives E\_diff \= (3/10)*mc*², so τ\_H \= 10ℏ/(3A*mc*²) and Γ\_H ∝ *m*². ZS-A3 v1.0: inside the horizon *r* is timelike and *t* spacelike (an *r↔t* exchange identified with X↔Y), the horizon is the Z-sector boundary (ε \= 0), a black hole an X-structure collapsed into a Y-prison. This appendix asserts only the Newtonian (3/10)*mc*² identity (DERIVED) and the inherited *r↔t* \= X↔Y reading (HYPOTHESIS).

**Appendix E — Port-Based Teleportation and the Complete Formalization \[NEW v2.1\].** PBT (Ishizaka–Hiroshima 2008\) realizes an approximate (dPBT) or probabilistic-exact (pPBT) universal programmable processor with finite resources, faithful only as *N* → ∞ (forced by the no-programming theorem). The deterministic entanglement fidelity obeys F\_d(N) ≤ √N/d (N ≤ d²/2), 1 − (d²−1)/(16N²) otherwise (Christandl *et al.* 2021), with closed forms for *d* and small *N* (Studziński *et al.*). For *d* \= 2 and *N* serial Z-handshakes, self-mediation fidelity is ceilinged below unity for finite *N*, reaching unity only as *N* → ∞; identifying *N* with the handshake count *n* (ZS-F10), this *N* → ∞ asymptote is the i-tetration convergence to *z*\* (ZS-F0/M1). Self-mediation is impossible deterministically and exactly; approximately it is bounded by F₂(n).

**Appendix F — The F-Q1-rad Deciding Calculation \[NEW v2.1\].** Radiation rate ∝ momentum diffusion D\_pp (Bassi–Donadi). The X-ray experiments bound the stochastic-collapse class (universal white noise; smaller smearing ⇒ more radiation; R₀ → 0 excluded). ZS-Q1 is scalar-tensor/environmental: ε is a deterministic massive field, decoherence ∝ E\_diff (gated, \= 0 unsuperposed), ensemble linear (ZS-Q16) — no universal noise. ε is a Yukawa mediator: heavy ⇒ decouples (e^(−r/λ\_ε)), opposite to the DP 1/R₀³ enhancement; the residual ε-vacuum effect is (A·G)²-suppressed second order with the ε mass as natural cutoff. The naive "λ\_ε as smearing length" worry is a category error. Hence F-Q1-rad closes for all m\_ε. A separate fifth-force gate F-Q1-5th follows from the A-strength Yukawa, requiring heavy/screened ε.

**References**

\[1\] C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A. Peres, W. K. Wootters, Phys. Rev. Lett. **70**, 1895 (1993).  
\[2\] W. K. Wootters, W. H. Zurek, Nature **299**, 802 (1982).  
\[3\] M. A. Nielsen, I. L. Chuang, "Programmable quantum gate arrays," Phys. Rev. Lett. **79**, 321 (1997).  
\[4\] F. W. Lawvere, "Diagonal arguments and Cartesian closed categories," Lecture Notes in Math. **92**, 134 (1969); repr. Repr. Theory Appl. Categ. **15**, 1 (2006).  
\[5\] A. K. Pati, S. L. Braunstein, "Impossibility of deleting an unknown quantum state," Nature **404**, 164 (2000).  
\[6\] S. Ishizaka, T. Hiroshima, "Asymptotic teleportation scheme as a universal programmable quantum processor," Phys. Rev. Lett. **101**, 240501 (2008).  
\[7\] M. Christandl, F. Leditzky, C. Majenz, G. Smith, F. Speelman, M. Walter, "Asymptotic performance of port-based teleportation," Commun. Math. Phys. **381**, 379 (2021).  
\[8\] N. Gisin, Phys. Lett. A **143**, 1 (1990).  
\[9\] J. Polchinski, Phys. Rev. Lett. **66**, 397 (1991).  
\[10\] R. Penrose, "On gravity's role in quantum state reduction," Gen. Relativ. Gravit. **28**, 581 (1996).  
\[11\] L. Diósi, "Models for universal reduction of macroscopic quantum fluctuations," Phys. Rev. A **40**, 1165 (1989).  
\[12\] S. Donadi, K. Piscicchia, C. Curceanu, L. Diósi, M. Laubenstein, A. Bassi, "Underground test of gravity-related wave function collapse," Nature Phys. **17**, 74 (2021).  
\[13\] I. J. Arnquist *et al.* (Majorana Collaboration), "Search for spontaneous radiation from wave function collapse in the Majorana Demonstrator," Phys. Rev. Lett. **129**, 080401 (2022); Erratum **130**, 239902 (2023).  
\[14\] XENON Collaboration, "Challenging spontaneous quantum collapse with XENONnT," arXiv:2506.05507 (2025).  
\[15\] A. Großardt, "The Diósi–Penrose model of classical gravity predicts gravitationally induced entanglement," Phys. Rev. D **111**, L121101 (2025).  
\[16\] Y. Y. Fein *et al.*, "Quantum superposition of molecules beyond 25 kDa," Nature Phys. **15**, 1242 (2019); and Nature **638** (2026), quantum interference of sodium nanoparticles beyond 170 kDa.  
\[17\] J. G. Lee, E. G. Adelberger, T. S. Cook, S. M. Fleischer, B. R. Heckel, "New test of the gravitational 1/r² law at separations down to 52 μm," Phys. Rev. Lett. **124**, 101101 (2020).  
\[18\] W. F. Stinespring, Proc. Am. Math. Soc. **6**, 211 (1955).  
\[19\] R. M. Corless, G. H. Gonnet, D. E. G. Hare, D. J. Jeffrey, D. E. Knuth, Adv. Comput. Math. **5**, 329 (1996).  
\[20\] Z-Spin Cosmology (2026): ZS-F0 (bootstrap; Lawvere; FFPP), ZS-F1 (action; L\_XY ≡ 0; U(1) Z-bias Φ), ZS-F2 (**A** \= 35/437), ZS-F5 (**Q** \= 11; dim Z \= 2), ZS-M1 (HSI; *z*\*), ZS-Q1 (geometric decoherence; τ\_D), ZS-Q2 (entanglement; τ\_ent; area law), ZS-Q7 (Z-bottleneck; ≤ ln 2), ZS-Q12 (self-referential collapse; *z*\*), ZS-Q16 (outcome problem; linear ensemble; strong OPEN), ZS-T1 (information routing; serial handshakes), ZS-A3 (black-hole ε-field; horizon \= Z-boundary), ZS-F18 (meta-map).

**Version History**

v2.1 (June 2026): Adds the **complete formalization of the Self-Mediation No-Go** via port-based teleportation (§5.5, Appendix E): deterministic-exact PROVEN, approximate fidelity ceiling F\_d(N) ≤ √N/d (d \= 2\) with the port count identified as the serial handshake count and unit fidelity only in the *n* → ∞ (i-tetration *z*\*) limit. Adds **§7 (experimental status and gates)**: the 2026 interferometry/GIE landscape for the ratio-12.49 test; the deciding analysis closing **F-Q1-rad** (ZS-Q1 is scalar-tensor/environmental with no universal radiating term, and ε is a Yukawa mediator that decouples when heavy — escaping the X-ray bounds that excluded parameter-free Diósi–Penrose); and the new **F-Q1-5th** fifth-force gate (Appendix F). Honest corrections incorporated: the v1-era radiation over-claim (a dimensionally-suspect quadratic rate) and a v2-era category error (ε Compton wavelength mistaken for a Diósi–Penrose smearing length) are corrected and reflected in §7; no prior numerical claim retracted. New gates F-Q17.7, F-Q1-rad, F-Q1-5th. New companion script zs\_q1\_radiation\_gate\_F-Q1-rad.py. (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED unchanged; zero free parameters.

v2.0 (June 2026): Major reorientation. Demoted the v1.x faithful-sub-luminal-teleportation \[DERIVED\] and FTL \[NON-CLAIM\] to Tier-1 consistency (§8). Introduced the **Reach Bound** \[DERIVED/TESTABLE\] with *m*^(−5/3) scaling, both heritage anchors, the 1/A \= 12.49 spatial signature, and the Horizon Corollary (§3); and the **Self-Mediation No-Go** \[DERIVED\] via no-programming \+ Lawvere/*z*\* (§5), unified with the ZS-F0 bootstrap B0 and the ZS-Q16 strong-outcome OPEN (§6). Companion script zs\_q17\_v2\_reach\_bound\_verify.py (14/14 PASS).

v1.2 / v1.1 / v1.0 (June 2026): \[SUPERSEDED\] Teleportation framing; faithful sub-luminal \[DERIVED\], FTL \[NON-CLAIM\]; inter-cell L\_XY closure; dual-frame proper-time-compression reading. The dual-frame §6.2–6.3 content is relocated to ZS-F19; the observer/outcome content is subsumed by ZS-Q16 v2.5. Retained only as Tier-1 consistency (§8).  
