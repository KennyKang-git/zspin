# **ZS-M58**

# **Boundary-Frame Covariance, Pointed-Dilation Non-Identifiability, and the Character Reduction of the Z-Spin Primitive Event**

## 

## **With a holonomy–expansion determination of the quarter-turn, and the reduction of F-M54-16′ to one unknown physical structure**

*Target selection  physical realization: what ZS-M58 closes, and what it hands to ZS-S28*  
---

**Author:** Kenny Kang · **Affiliation:** Z-Spin Cosmology Collaboration **Theme:** Mathematical Spine · **Paper code:** ZS-M58 · **Version:** 1.7 — **TERMINAL** **Date:** July 2026 **Supersedes:** v1.6, v1.5, v1.4, v1.3, v1.2, v1.1, v1.0.  
**Audit history.** Seven external rounds, **34 items, all upheld, none contested**.

| Round | On | Total items | Errors / over-statements | Constructive mandates |
| ----- | ----- | ----- | ----- | ----- |
| 1 | v1.0 | 6 | 6 | 0 |
| 2 | v1.1 | 3 | 2 | 1 |
| 3 | v1.2 | 6 | 5 | 1 |
| 4 | v1.3 | 6 | 4 | 2 |
| 5 | v1.4 | 5 | 4 | 1 |
| 6 | v1.5 | 5 | 5 | 0 |
| 7 | v1.6 | 3 | 3 | 0 |
| **Total** |  | **34** | **29** | **5** |

Rounds 4–6 found six verified code defects; round 7 found **a mathematical error in a theorem registered PROVEN**, plus three ledger-reporting errors. All are reproduced and corrected.  
**Parents:** ZS-M54 v2.2; ZS-M56 v1.8; ZS-M57 v1.8 **Dependencies:** ZS-M1; ZS-M46 v1.5; ZS-M51 v1.3; ZS-M53 v1.5; ZS-Q18 v1.7; ZS-F0 v1.0(R); ZS-F1; ZS-F5; ZS-F47 v1.6; ZS-F48 v1.6; ZS-S14 v2.0; ZS-S20–S24; ZS-S27 **Successors, in order:** **ZS-S28** (exact Lorentzian one-event reduction)  **ZS-M60** (the pointer-preserving S14–carrier intertwiner, top priority)  ZS-M61 (H-ZSQ)  ZS-M59  ZS-Q19, ZS-F49  
---

**Verification: 173/173 PASS** (92 ANALYTIC · 27 REGRESSION · 30 GUARD · 4 PROXY · 20 DECLARATION) **| Zero Free Parameters**  
**Fixed-size, fail-closed ledger.** The suite now emits **exactly 173 rows in every scenario**, including those in which required evidence is absent; missing evidence produces explicit FAIL rows rather than skipped rows. Verified across seven regression runs (§15.2), each returning exit code 1\.  
Two files: zs\_m58\_expansion\_construct\_v1\_7.py (-blind construction; whole-file firewall; script-relative artifact carrying its own source hash) and zs\_m58\_verify\_v1\_7.py (comparison; recomputes the payload digest, re-runs a pristine copy of the construction source and compares the regenerated payload byte-for-byte, and runs two end-to-end firewall attacks as subprocesses).  
---

## **§0. Abstract**

ZS-M54 reduced the Z-Spin measurement bridge to one identification, **F-M54-16′**: is the ZS-S14 one-event slab the Zpath-QND channel whose coherence multiplier is the i-tetration derivative ? Seven audits have corrected this paper twenty-nine times. The terminal verdict is two-layered and must not be compressed into one:

**ZS-M58 closes the mathematical target-selection and character-reduction layers, including a complementary holonomy–expansion determination of the quarter-turn generator. It does not close the ZS-S14 physical realization of the channel. The remaining bridge is an action-derived, pointer-preserving complete-order intertwiner between the S14 pointer process and the ZS-Q18 full-state QND carrier — one unknown physical structure, not one unknown number.**

**The correction of round 7, and it is a genuine mathematical error.** The Four-Datum Separation, registered PROVEN since v1.4, stated the wrong relations among its own data. Three faults, all confirmed:  
*First,* its certificate — “the three branches all exponentiate to the same ” — proves that an **endpoint does not determine a lift**, not that a lift fails to determine an endpoint. The true direction is the opposite: given a branch L, the value a=eL is determined (check Z34, residual 1.410−15). v1.6 labelled this certificate as establishing D3⇏D1 when what it establishes is D1⇏D3.  
*Second,* for a nonvanishing path with **fixed** endpoints, the endpoint-fixed homotopy class and the logarithm branch are **the same datum**. Since exp:CC is the universal cover, both are classified by the same integer:  
ℓk = 01aa ds = Loga+2ik,  
verified exactly for k=−2,,2 (Z35, residual 1.810−15), with the class-to-lift map injective at minimum gap exactly 2 (Z36). v1.6 asserted “D2D3 but not conversely”; in fact D2D3.  
*Third,* the datum was typed as a U1 frame-transport path while the certificate integrated a C multiplier path. A U1 path has constant modulus (Z38, residual 4.410−16) and cannot carry the modulus evolution that the C path exhibits over the range 0.891514, 1 (Z39, guard). These are different objects.  
The theorem is accordingly restated as **M58.5″ — Endpoint–Lift–Intertwiner Separation \[PROVEN\]** with **three** layers, the middle one having three equivalent descriptions:  
L1 endpoint; L2 lift = endpoint-fixed homotopy class = logarithm branch = winding integer; L3 intertwiner, with L2L1, L1⇏L2, and L1L2⇏L3. The count drops from four data to three layers, and the physical consequence is unchanged: **the phase half of F-M54-16′ and the discrete clock gate are coupled through shared data, not identical.**  
**Three ledger-reporting corrections.** v1.6 reported “156/166” for the artifact-deleted regression, but the actual output was TOTAL 160 — six artifact-dependent rows had simply not been emitted. The ledger now has a **fixed size**: missing evidence produces explicit FAIL rows, so every scenario reports out of the same total. Payload tampering is detected by **Z20d and Z24**; **Z25 is a negative-control digest-sensitivity guard and correctly PASSES**, so it should not be listed as a tamper detector. And **Z31’s claim is lowered**: it guards against the *inference* that pointer preservation follows automatically from complete-order equivalence; it does not and cannot detect condition (P) being dropped from a manuscript or a successor construction.  
**What is closed, unchanged.** The target algebra; the scalar characteristic function with complete non-unitarity discharged; the boundary-frame covariance law; the endpoint–lift–intertwiner separation; the unpointed-dilation no-go; the OS-real reality obstruction; and the Character Reduction — under gluing additivity, holomorphy and a normalisation, the boundary map is ecz=iz and its linearisation at the fixed point is c z\*, a product of two single-valued numbers and hence branch-free. The generator is c=i/2, with two algebraically distinct determinations: forward from ZS-F5’s dimZ=2 with ZS-M1’s phase budget, and reverse from ZS-M51’s fixed-point census, which places the **first contracting saddle at** m,x0=5,14 while consuming **no Z-Spin constant at all**, in a firewalled, provenance-bound module whose only permitted input is the Dottie number.  
**What is not closed, unchanged.** Order-4 holonomy covariance does not imply QND (M58.21), so (H-PROC) needs a conserved current. (G1) remains **TYPE-UNDETERMINED**. M58.22A requires the pointer-preservation condition (P) (guards Z31, Z32). ZS-F48 supplies an amplitude-damping **precursor**; the carrier is ZS-Q18 Theorem Q18.12’s Efullp,w (M58.24). The two-gate intersection GctrGfirst={2} is an **exact conditional discriminator**, not evidence for its own hypotheses.  
**F-M54-16′ remains REFORMULATED / DECOMPOSED — OPEN.** ZS-M58 closes at v1.7.  
---

## **Epistemic Status Legend**

| Status | Meaning here |
| ----- | ----- |
| **PROVEN** | Complete finite-dimensional or analytic proof; machine-checkable. M58.1–M58.3, M58.4A, **M58.5″**, M58.6, M58.8, M58.12, M58.14, M58.16, M58.21, M58.23, and **the implication of M58.22A**. |
| **IMPORTED-PROVEN** | Proved externally or in a parent, at exactly the stated scope. Sz.-Nagy–Foiaș; Stinespring/Choi; Choi–Effros / Kadison at the stated type premises; the Poisson model; **the covering-space classification of** exp:CC; holomorphic-character uniqueness; Lindeberg–Feller; ZS-M51 T1, T2, T5–T6; ZS-F48’s AD intertwiner; ZS-Q18 Thm Q18.12. |
| **DERIVED** | From locked corpus objects plus PROVEN steps; zero new parameters. M58.11A, M58.15, M58.17A, M58.20, M58.24. |
| **DERIVED-CONDITIONAL** | Exact under named unresolved hypotheses carried in the theorem line. M58.13; M58.22B; M58.17B on (H-MIN); M58.18/19 on (H-ZSQ)(H-MIN); M58.7, M58.9′, M58.10′ on theirs. |
| **BYPASS-CONDITIONAL** | A route that renders other hypotheses unnecessary without proving them, and whose own antecedent is open. **The application of M58.22A to S14**, because the existence of J and of (P) is OPEN. *(The implication itself is PROVEN; the two labels attach to different objects — see §13.2.)* |
| **CLOSED-NEGATIVE-CONDITIONAL** | The OS-real transfer subclass under (H-OSR). |
| **REFORMULATED / DECOMPOSED** | A prior gate shown not to be one well-posed question and re-expressed in type-correct parts, **without** being answered. F-M54-16′. |
| **TYPE-UNDETERMINED** | A proposition whose statement is not yet fixed in the relevant category. **(G1).** |
| **OPEN / NON-CLAIM / RETRACTED / PROXY** | As before. |

---

## **Pre-registered outcome table**

**A–C are as publishable as D.**

| Outcome | Trigger | Conclusion |
| ----- | ----- | ----- |
| A | pointer eigenvalue degenerate, or several admissible frame paths | UNDERDETERMINED |
| B | CS14 fails CPTP / QND / equalizer / rank-2 | F-M54-16′ CLOSED-NEGATIVE |
| C | structure passes but aS14 | i-tetration channel identification RETRACTED |
| D | structure passes  pointer-preserving intertwiner  aS14= | F-M54-16′ DERIVED-CLOSED |
| N / P / R | not one well-posed question / reduces to numberless hypotheses / a load-bearing input cross-fixed | REFORMULATED — OPEN / CONDITIONALLY CLOSED / cross-fixed |

**N, P and R have fired. A–D require ZS-S28 and remain open.**  
---

## **What changed in v1.7**

**Three findings from audit round 7, all upheld.**  
**H1 — M58.5′ stated the wrong relations.** Three faults, each confirmed numerically: the certificate’s direction was inverted; the homotopy class and the logarithm branch are one datum, not two; and the datum’s type was U1 while the proof used C. Restated as **M58.5″** with three layers (§5). New checks Z34–Z40.  
**H2 — the ledger changed size under regression.** With the artifact absent, six artifact-dependent rows were not emitted, so v1.6’s “156/166” was really 156 of 160\. The ledger is now **fixed at 173 rows in every scenario** (§15.2).  
**H3 — two guard roles were misdescribed.** Payload tampering is caught by **Z20d and Z24**; **Z25** is a negative-control digest-sensitivity guard that correctly passes. And **Z31** guards the *inference* that pointer preservation follows from complete-order equivalence — nothing more (§13.2, §15.2).  
---

# **§1. The residue after M54–M57**

ZS-M54 v2.2 gives LXY=0, rankGXYdimZ=2, 2=A/Q, and Theorem M54.23, ⟨W1W0⟩=, true by construction (its own correction T5). The gate is

	F-M54-16′​:  CS14 =? 00⟩⟨00+11⟩⟨11+ 00⟩⟨11+‾ 11⟩⟨00.	(1.1)

ZS-M56 v1.8 obstructs the graded tensor subsystem. ZS-M57 v1.8 supplies the pointer-domain corrections, the real multiplier of a grading-symmetric collision, the branch structure M57.T.2′, the event/metric clock split, the c.n.u. requirement, Route S, the trap F-M57.2, and \=−W0−logi PROVEN.  
ZS-M1 proves Tz=iz (principal branch, kW=0), z\*, \=i/2z\*, the phase budget, and nc=3.2036 LOCKED. **ZS-M51 v1.3**, standalone dynamics consuming no Z-Spin constant: **(T1)** fs′zs\*=W0−is; **(T2)** \=cos, sc=esin, nc=2/sc; **(T5–T6)** the census Nm=⌈xcm−1⌉−1, first contracting saddle 5,14. **ZS-F47 v1.6** records that saddle with f=iz and htop=logm, marks its **central bridge HYPOTHESIS**, and warns that \=ZW is a reused constant and that m=5 is minimal m1 (mod 4), **not the pentagon**.  
**Locked constants.**  
z\*=0.4382829367270321116+0.3605924718713854860 i,  =i/2z\*,  
\=0.8915135657760470, arg=2.2592495539025985=2+argz\*,  
\=0.1148346249960096, =0.4529939977938757,  
\=0.7390851332151606, sc=1.9613088464594559, nc=3.2035675148878049, xc=0.3121519978438856.  
**Firewall.** No S14 channel is constructed here; no aS14 is computed; no S14 cellular data is loaded (W02).  
---

# **§2–§4. Algebra, characteristic function, frame covariance**

**M58.1 — Factor–Correspondence Separation \[PROVEN\].** A tensor-factor no-go needs dimension arithmetic plus a grading multiplicity; a Choi rank-r correspondence needs only C≽0 of rank r with TroutC=I. Different categories. Q=11 is prime, so C11 admits no nontrivial factorisation (K01), yet the rank-two C exists (K02). Appendix A.1.  
**M58.2 — QND–Equalizer Equivalence \[PROVEN\].** Pj=Pj diagonal Kraus operators exist suppCZ=span{00⟩,11⟩}. Three negative controls (E05–E07). Appendix A.2.  
**M58.3 — Scalar Characteristic Reduction \[PROVEN\].** For 0\<a\<1 the coherence contraction is automatically completely non-unitary — the ZS-M57 hypothesis is **discharged** — the defect indices are 1,1, and az=z−a/1−a‾z is inner of degree one with unique zero a. Checks F01–F08; Appendix C.  
**M58.4A — Boundary-Frame Covariance \[PROVEN\].** Under F=U1inU1out,

	aS14 ↦ e iout−in aS14,	(4.1)

so a is invariant, the orbit is the full circle, and  is covariant, not invariant. **\[R1, audit 1\]** This is **not** ZS-M53’s Kraus-phase U12, under which KrKr and hence a are unchanged (N01, residual 1.110−16). **M58.4B \[OPEN\]** — whether (4.1) is a physical *gauge* depends on (H-GAUGE).  
---

# **§5. Theorem M58.5″ — Endpoint–Lift–Intertwiner Separation**

**\[H1, audit 7 — the v1.4–v1.6 Four-Datum Separation is superseded.\]** Its relations were wrong in three ways; the corrected statement follows, and the three faults are recorded explicitly in §5.3 so that the earlier version cannot be cited.

## **5.1 The three layers**

**L1 — endpoint.** The terminal datum of the boundary transport, R1U1, equivalently argaS14 modulo 2 via (4.1).  
**L2 — lift.** One datum with three equivalent descriptions: the **endpoint-fixed homotopy class** of the action-derived nonvanishing multiplier path a:0,1C with a0=1, a1=aS14; the **branch of** logaS14; and the **winding integer** kZ.  
**L3 — intertwiner.** The ZS-M46 event-step intertwiner, in the pointed and filtered form (7.3).

## **5.2 Statement \[PROVEN\]**

L2L1,  L1⇏L2,  L1L2⇏L3.  
Moreover the three descriptions of **L2** are in canonical bijection with each other and with Z.  
**Proof.** Since exp:CC is the universal covering map, path-lifting gives a bijection between endpoint-fixed homotopy classes of paths in C from 1 to a and the fibre exp−1a={Loga+2ik:kZ}; the bijection is realised by the lift

	ℓ = 01asas ds = Loga+2ik.	(5.1)

L2L1: from a branch ℓ the value is recovered as a=eℓ, hence so is arga and therefore the endpoint. L1⇏L2: the fibre over a single a is infinite, so one endpoint is compatible with every k. L1L2⇏L3: by M58.6 the unpointed minimal unitary dilation is the same for every strict scalar contraction, so no amount of endpoint and lift data identifies the shift with the M46 seam. ▫  
**Machine checks.** (5.1) holds exactly for k=−2,,2 (Z35, residual 1.810−15); the class-to-lift map is injective with minimum gap exactly 2 (Z36, residual 0); expℓ=a for every branch (Z34, residual 1.410−15); and one endpoint carries lifts differing by 2i (Z37, guard; the historical N02/N03 pair records the same fact).

## **5.3 The three faults corrected, recorded so the old version cannot be cited**

**(i) Direction inverted.** v1.6’s certificate observed that the three branches with imaginary parts −4.0239357, 2.2592496, 8.5424349 all exponentiate to the same , and labelled this D3⇏D1. It establishes the *opposite*: **endpoint does not determine lift**. The direction L2L1 holds, so no separation claim in that direction was ever available.  
**(ii) Two data collapsed into one.** v1.6 claimed “D2D3 but not conversely”. For **endpoint-fixed** paths the converse holds too, by (5.1); the homotopy class and the branch are the same integer. v1.6’s own guard B06 — “a different action path gives a different branch” — supports the bijection rather than a one-way implication.  
**(iii) Type mismatch.** v1.6 typed the middle datum as a U1 frame transport while integrating a C multiplier path. A U1 path has constant modulus (Z38, residual 4.410−16); the C path’s modulus runs over 0.891514, 1 (Z39, guard). **L2 is defined on the** C **multiplier path**, and the modulus evolution it carries is invisible to any U1 transport — a separate remark, not part of the separation claim.  
**What is unchanged.** The physical consequence stands: the phase half of F-M54-16′ and the discrete clock gate are **coupled through shared data, not identical**, because L3 is independent of L1 and L2 while all three constrain the same transport family. Nothing in §§11–13 depended on the mis-stated directions.  
---

# **§6–§7. The dilation layer**

**M58.6 — Unpointed Dilation Non-Identifiability \[PROVEN\].** With Pa=1−a2/1−a‾2 and da=Pa dm, multiplication by  on L2T,a is a unitary dilation of a with ⟨1,Mn1⟩=an; since Pa\>0 a.e., Pa is unitary L2aL2m and intertwines M with M. The parameter migrates entirely into the cyclic vector. Hence **every** strict scalar contraction has the same unpointed multiplicity-one bilateral shift. Checks P01–P05; Appendix D. Unitary conjugation preserves unitarity, so WVS14W=UM461 is ill typed for an isometric V (V01, V02).  
**M58.7 — Pointed Filtered Event-Clock Intertwiner \[DERIVED-CONDITIONAL on (H-PTR); OPEN\].** Physical identification requires **jointly**

	WUS14W=UM461, WS14=M46, WPS14W=PM46, WApastW=N, WAfullW=M,	(7.3)

with U the minimal **unitary** dilation, plus WRrecordW=RM46 if a record algebra is claimed.  
---

# **§8–§10. Clocks, reality, Route S**

**M58.8 — Clock-Layer Separation \[PROVEN\].** *Certificate:* n↦Un is a Z-action determined by the one-step operator alone and never forms a generator; a continuous flow requires a logarithm, supplied for a scalar path only by (5.1). Hence channel equality and discrete event equivalence require no metric duration and no continuous branch; exact continuous modular equality requires the lift plus the CRT-4 cocycle conditions. ▫ The lift is fixed **by the path**, i.e. by layer L2 — verified at B04 (2.510−16), B05, B06. **NC-M58.1:** no Z follows from a per-event equality.  
**M58.10′ — OS-Real Reality Obstruction \[CLOSED-NEGATIVE-CONDITIONAL on (H-OSR)\].** **\[R4, audit 1\]** Positivity alone does not force reality: T=1 ic −ic 1  has eigenvalues 1c\>0, real basis vectors, purely imaginary off-diagonal (N05, N06). *Certificate under (H-OSR):* an antiunitary JOS with JOSTJOS=T fixing the pointer pair pins ⟨j,Tk⟩ to its own conjugate, hence real; the doubled compression inherits reality; a real symmetric PSD 22 block has real off-diagonal; a1 by Cauchy–Schwarz. Therefore aS14R and

	0min=minaRa−=Im=0.6884532271.	(9.1)

▫ Checks H01–H03, N07; corroborated by ZS-M57’s grading-symmetric collision (H04) and ZS-S27. **The phase of , if physical, is a real-time rotation, not a Euclidean amplitude** — consistent with the purely imaginary generator of §§11–12.  
**M58.9′ — Route-S Diffusion Limit \[DERIVED-CONDITIONAL\].** **\[R5, audit 1\]** Lindeberg–Feller is asymptotic (N08). *Certificate:* annealed independence makes the n-cycle multiplier the n-th power of the one-cycle characteristic function, matching the corpus n law and excluding quenched noise at n=2 (S04, S05); under (H-CLT) the k-fold sum converges weakly to a Gaussian, so aS14expim−2/2 **in the refinement limit**; exactness at finite refinement needs (H-WIENER). ▫ CLT residuals fall to 3.710−5 at k=64 (S06); k=1 fails (S07). **F-M57.2 honoured:** fitting m,2 to  carries **zero evidential content** (S08, S09).  
---

# **§11. The Character Reduction**

## **11.1 Lemma M58.11A — the generator, forward route \[DERIVED\]**

	c=2idimZ2=i2.	(11.1)

**\[C2, audit 2 — retained.\]** “dimZ=2 alone” is **withdrawn**: two corpus inputs are used, ZS-F5’s dimZ=2 and ZS-M1’s phase budget. The family cd=2i/d2 for d2 is a **diagnostic specialisation introduced by this paper** under (H-ZSQ), not a ZS-M1 result; the imported-proven object is ZS-M51 T1’s Lambert curve (Y22). And (11.1) already couples ordH=4 to dimZ2=4 — the phase budget **is** (H-ZSQ) at dimZ=2. §12 breaks that coupling.

## **11.2 Theorem M58.12 — Character Reduction \[PROVEN\]**

**(G1)** *\[TYPE-UNDETERMINED\]* TS14z1+z2=TS14z1TS14z2 in the physical Z-boundary log-coordinate. **(G2)** holomorphy there. **(G3)** DTS140=c.  
Under (G1)(G2)(G3): TS14z=ecz=iz — the ZS-M1 map **recovered, not assumed** — the fixed point is the locked z\*, and since DT=cT,

	DTS14z\*=cTS14z\*=c z\*=i2z\*=.	(11.2)

*Proof.* z2=0 gives T0=1; differentiating (G1) at z2=0 with (G2) gives T′=cT, whose unique holomorphic solution is ecz (holomorphy excludes the z‾-dependent continuous characters); (G3) fixes c; ZS-M1 supplies z\*. ▫ Checks Q03–Q08, closure identity at 8.510−20.  
**\[D2, audit 3 — (G1) re-typed.\]** Cobordism gluing supplies KW2W1=KW2KW1, a composition of **maps**; (G1) asserts a character law of C,+. These coincide only if the physical boundary coordinate is a log-coordinate in which composition becomes addition *and* the boundary map acts by multiplication — a coordinate theorem nobody has proved. **(G1)’s type is not yet fixed**, and it heads the ZS-S28 list.

## **11.3 Theorem M58.14 — Branch Freedom \[PROVEN\]**

a=c z\* is a product of two single-valued numbers, containing no logarithm, so M57.T.2′’s branch ambiguity — an ambiguity of layer **L2** — does not touch the *value* (Q09). **Scope (audit 2):** the character normalisation supplies R0 only; propagating to s=1 is (G2), and the lift remains L2.

## **11.4 Theorem M58.13 — Boundary-Response Closure \[DERIVED-CONDITIONAL\]**

**(H-PROC)** the S14 one-event process, on an action-derived pointer pair, is CPTP, Zpath-QND, Choi rank two. **(H-BR)** aS14=DTS14z\*. **(G3**​S14**)** the S14 boundary Hessian at the empty cobordism gives DTS140=i/2.  
Under **(H-PROC)(H-BR)(G1)(G2)(G3**​S14**)**, aS14=, CS14=C, and F-M54-16′ closes.  
**Motivation for (H-BR), as motivation only.** aS14 is the connected two-boundary CTP response; the BFV boundary map’s linearisation is zout/zin; M58.2 supplies a Ward-type restriction making them plausibly equal. **Not a derivation.** The influence functional may also carry higher connected boundary correlators, accumulated environment effects, gauge/ghost determinants, non-linear coarse-graining, leakage out of the pointer sector, and population mixing — each of which breaks (H-BR).

## **11.5 What ZS-S28 must settle, \-blind**

**(G1)** first, because its type is undetermined (F-M58.22). Then **(G2)**; **(G3**​S14**)**, the boundary Hessian at the identity — the single number (F-M58.23); **(H-PROC)** via a conserved current, since by **M58.21** covariance is insufficient (F-M58.37); **(P)**, the pointer identification (F-M58.43); **(H-BR)** the Ward identity (F-M58.21). Orbit-weight dependence is **absorbed into** (G1) and (G3​S14).  
---

# **§12. The holonomy–expansion gate**

**M58.20 — recognition of the threshold \[DERIVED\].** v1.1’s bisected “neutral point” c=1.9613088 **is** the locked sc=esin of ZS-M51 Theorem T2 (Y04, residual 4.610−10). Hence the contraction gate is a corpus theorem:

	fs′zs\*=W0−is,  contractions\<sc2s\>nc.	(12.1)

Reverified against direct iteration at four values of s (Y05, 10−15), consistent with \=−W0−logi (Y06, 8.510−20).  
**M58.16 — primitive holonomy order \[PROVEN\].** On Tmx={mx} the fixed points are xj=j/m−1; at the primitive interior one, H=e2i/m−1 has exact order m−1 since gcd1,m−1=1 (Y07, 10−25 over m=311).  
**M58.17A \[DERIVED from IMPORTED-PROVEN ZS-M51 T5–T6\].** Nm=⌈xcm−1⌉−1 vanishes for m4 and equals 1 at m=5, so the **first contracting saddle is** 5,14, whence

	c=i2, T=ecz=iz, H=i, ordH=4, W0−i/2=0.8915135658, htopT5=log5.	(12.2)

**No Z-Spin constant is consumed** (Y08–Y14; independently reproduced by the firewalled, provenance-bound module, Z27–Z29).  
**M58.17B \[DERIVED-CONDITIONAL on (H-MIN)\].** The ZS-S14 primitive event *realizes* that saddle. **(H-MIN) is ZS-F47’s central bridge, marked HYPOTHESIS there.** M58.17A is mathematics; M58.17B is physics. *Closure route:* prove Seff1m\>Seff15 for every contracting m\>5 on the exact S14 one-event action; or establish a **category equivalence** between “minimal positive contracting admissible return” and the existing S14 primitive-event definition.  
**M58.18 \[DERIVED-CONDITIONAL on (H-ZSQ)(H-MIN)\].** Under (H-ZSQ), ordHZ=dimZ2, order 4 gives dimZ2=4 and dimZ=2, independently recovering ZS-F5. (H-ZSQ) is not a general theorem — an order-4 complex structure exists in every even real dimension — it is the ZS-M1 phase budget in holonomy-order form, unproved from the S14 BFV algebra. Handed to **ZS-M61**.  
**M58.23 — realizability and the single-cycle obstruction \[PROVEN\].** *(i)* For Ud=diag1,,,d−1 with  a primitive d2-th root, ordAdUd=d2 for d=2,3,4 (Z14); at d=2 this forces \=i. *(ii)* But Ad of **any** diagonal unitary fixes every Ejj, so it fixes d of the d2 matrix units and **single-cycle transitivity is impossible** (Z15) — **correcting audit 3’s proposed mechanism**. *(iii)* The correct mechanism is **faithfulness of a cyclic order-**d2 **adjoint action**.  
**M58.19 — the two-gate intersection \[DERIVED-CONDITIONAL\].** With xd=1/d2, md=d2+1:

| d | md | |W0−isd| | contraction | ordH |
| ----- | ----- | ----- | ----- | ----- |
| 1 | 2 | **1.6445567** | **no** | 1 |
| **2** | **5** | **0.8915136** | **yes — first** | **4** |
| 3 | 10 | 0.5429705 | yes, later | 9 |
| 4 | 17 | 0.3503940 | yes, later | 16 |

Gctr: d2. Gfirst: d=2. GctrGfirst={2} (Y15–Y17). d=1 is excluded twice (Y18).  
**\[D3, audit 3 — exact strength.\]** Because md=d2+1 is *supplied by* (H-ZSQ), this is an **exact conditional discriminator** — a consequence of (H-ZSQ)(H-MIN) — **not** evidence for them. Against interest: contraction alone passes d=2,3,4,5 (Y19). The v1.1 Monte Carlo (p=0.01215) remains **PROXY** (Q14).  
**\[D4, audit 3.\]** Route A and Route B are **two algebraically distinct determinations of** c**, independent with respect to the input** dimZ**, but not yet independently connected to ZS-S14**: both end in the same family fsz=eisz, and Route B reaches ZS-S14 only through (H-MIN). Route B does *output* the holonomy order that Route A must assume.  
---

# **§13. The intertwiner layer**

## **13.1 Theorem M58.21 — the charge grading and its limit \[PROVEN\]**

Under UH=diag1,i acting by conjugation,

	A0=span{E00,E11},  A−1=CE01,  A+1=CE10,	(13.1)

so a covariant channel cannot mix the coherence line with the population line, nor E01 with E10 — **but it can mix** E00 **with** E11**.**  
**Counterexample.** 00=1−p00+p11, 11=p00+1−p11, 01=a01, with p=0.18, a=0.6+0.3i: CP (Choi min eigenvalue 0.1492; Z03), TP (Z04), covariant to residual 0 (Z05), and **not QND**, P0−P0=0.18 (Z06, guard).  
**Consequence.** **(H-PROC) cannot be obtained from holonomy covariance.** It needs an S14 boundary Noether or BFV charge.

## **13.2 Theorems M58.22A / M58.22B**

### **M58.22A — Channel-Intertwiner Closure**

**Status, stated once.** *The implication is PROVEN. Its application to S14 is BYPASS-CONDITIONAL, because the existence of* J *and of (P) is OPEN.*  
**Type premises.** AS14ptr is a **unital C\*-algebra** with a fixed identification :AS14ptrM2C; J and J−1 are **unital and completely positive**.  
**Hypotheses.**

	J S14 J−1=Df1/4z\*, ZpathQND,	(13.2)

	(P)  JZptrS14=Zpath.@EQN:13.2P	(13.2P)

**Statement.** Under the type premises, J−1=AdV for a unitary V. Then **(13.2) alone** gives S14≅QND, i.e. **unitary equivalence**, with QND holding in the *transported* frame VZpathV; and **(13.2)(P)** gives the transported identity

	J S14 J−1=, ZpathQND,	(13.3)

which, **because** J **is pointer-preserving, *is* the fixed-pointer realization required by F-M54-16′.** F-M54-16′ then closes. **(G1), (G2), (G3**​S14**) and (H-BR) become UNNECESSARY — bypassed, not derived.**  
*Proof.* A unital complete order isomorphism between C\*-algebras is a Jordan isomorphism (Kadison) and, being completely positive in both directions, a \*-isomorphism (Choi–Effros); every \*-automorphism of M2C is inner, so J−1=AdV. Conjugation by a unitary transports complete positivity, trace preservation, Choi rank and the multiplier, and transports the QND property *along with the pointer*. Condition (P) pins the transported pointer to Zpath; ZS-M51 supplies Df1/4z\*=. ▫  
**Machine check, and what the guard actually guards.** With V a random unitary and J=AdV: CP (Z08), TP 2.310−16 (Z09), QND w.r.t. the **rotated** pointer 3.310−16 (Z10), rank two (Z11), multiplier 4.010−16 (Z12). With the same V, fixed-frame QND fails at residual 0.626 (**Z31**). With a pointer-preserving V=diag1,ei, i.e. under (P), fixed-frame QND holds at 1.110−16 (Z32).  
**\[H3, audit 7 — Z31’s role, lowered.\]** Z31 **permanently guards against the inference that pointer preservation follows automatically from complete-order equivalence.** It does *not* take the manuscript’s condition (P) as input, and it cannot detect (P) being dropped in a successor construction. The earlier phrasing “the pointer condition dropped  ledger red” is withdrawn.  
**\[E1, audit 4 — retained.\]** M58.22A does **not** shorten the closure distance. It **re-packages** F-M54-16′ as a commutative-diagram existence problem: the five-hypothesis character route is *replaced by one equivalent-strength channel-realization problem*. The object it names is **one unknown physical structure**.

### **M58.22B — Germ-Level Intertwiner \[DERIVED-CONDITIONAL; antecedent OPEN\]**

If, on a neighbourhood of the fixed point, J TS14z J−1=f1/4z, then **(G2) and (G3**​S14**) do follow**: holomorphy transports through a holomorphic local conjugacy, and tangent intertwining at the identity gives DTS140=i/2. Strictly stronger than (13.2); **OPEN**.

## **13.3 Theorem M58.24 — the Carrier Ledger \[DERIVED\]**

**ZS-F48 supplies a precursor, not the carrier.** Its intertwiner ADEw=Ew holds for the **amplitude-damping** representative, which ZS-F48 itself states is *not* a QND/Belavkin instrument. Verified at residual 1.110−16, with the map first **linearised** (Z17, linearity residual 1.810−15; Z18).  
**ZS-Q18 supplies the actual carrier.** Theorem Q18.12’s full-state embedding

	Efullp,w=1−p w w‾ p ,  dephEfullp,w=Efullp,w,	(13.5)

verified at residual 0 over three populations and three coherences (Z18b). Jacobian rank in Bloch coordinates: the F48 manifold has rank 2, Efull has rank 3 (Z18c); the gap is exactly the population coordinate.  
**Consequence.**

**F-M54-16′ reduces to one unknown physical structure: an action-derived, pointer-preserving complete-order intertwiner between** AS14ptr **and the ZS-Q18 full-state QND carrier.**

## **13.4 The concrete proof order for ZS-S28 / ZS-M60**

1. **Construct the Lorentzian one-event CTP process** and obtain CS14. CP and TP must emerge from the CTP/Stinespring structure — never by projection, clipping or per-input renormalisation (F-M58.12).  
2. **Decompose by holonomy charge:** M2=A0A+1A−1.  
3. **Prove QND from a conserved current** (M58.21). Core of (H-PROC).  
4. **Fix the pointer, not merely a pointer:** establish (P).  
5. **Charge-one Ward identity:** prove aS14=Df1/4z\*.  
6. **Compare only at the end:** Df1/4z\*=i/2z\*=.

Steps 2–5 together *are* the pointer-preserving intertwiner of M58.22A; step 6 is one line.  
---

# **§14. Ledger, non-claims, and the deep-exploration record**

## **14.1 Theorem M58.15 — status of F-M54-16′ \[DERIVED\]**

**Unconditional: REFORMULATED / DECOMPOSED — OPEN.** **Route 1:** CLOSED on (H-PROC)(H-BR)(G1)(G2)(G3​S14). **Route 2:** CLOSED on the existence of J satisfying (13.2)(P) with the M58.22A type premises — a shorter critical path, **not** a shorter distance. **Auxiliary:** c=i/2 has two algebraically distinct determinations; dimZ=2 is additionally selected under (H-ZSQ)(H-MIN).

## **14.2 Component ledger**

| Component | Status |
| ----- | ----- |
| target algebra; characteristic function; unpointed no-go; covariance law; **endpoint–lift–intertwiner separation**; character reduction; branch freedom; holonomy order; charge grading; single-cycle obstruction; **the M58.22A implication** | **PROVEN** |
| contraction gate \= ZS-M51 T1–T2; first saddle 5,14; carrier ledger; forward generator | **DERIVED** |
| S14 realizes the saddle | **DERIVED-CONDITIONAL** on (H-MIN) |
| dimZ=2 by two-gate intersection | **DERIVED-CONDITIONAL** on (H-ZSQ)(H-MIN) |
| germ-level intertwiner  (G2),(G3) | **DERIVED-CONDITIONAL**, antecedent OPEN |
| application of M58.22A to S14 | **BYPASS-CONDITIONAL** |
| **(G1)** | **TYPE-UNDETERMINED** |
| (G2), (G3​S14), (H-PROC), (H-BR), (H-ZSQ), (H-MIN), (H-GAUGE), existence of J, condition (P) | **OPEN** |
| AS14ptr; the morphism J; aS14 | **NOT CONSTRUCTED** |
| OS-real transfer subclass | **CLOSED-NEGATIVE-CONDITIONAL** on (H-OSR) |
| CRT-4/H-CLK discrete and continuous | **OPEN** |
| S14=QND unconditionally | **NON-CLAIM** |
| **v1.4–v1.6 Four-Datum Separation** | **SUPERSEDED by M58.5″** |

## **14.3 Non-claims**

NC-M58.1 no Z. NC-M58.2 no unconditional identification. NC-M58.3 the frame U1 and the cyclic-vector U1 are not one object. NC-M58.4 no instrument selected. NC-M58.5 no claim about the S14 boundary spectrum. NC-M58.6 no hypothesis is verified here. NC-M58.7 dimZ=2 is not proved from dynamics; it *would be*, conditionally. NC-M58.8 m=5 is not “the pentagon”. NC-M58.9 the 173 checks verify the target algebra, the conditional implications, the M51 arithmetic and the firewalled, provenance-bound construction — **they are not 173 verifications of an S14 channel**. NC-M58.10 M58.22A asserts the *consequences* of J, not its existence. NC-M58.11 M58.22A relocates the closure distance rather than shortening it. NC-M58.12 ZS-F48’s intertwiner is for an amplitude-damping representative. NC-M58.13 (13.2) without (P) establishes unitary equivalence only. NC-M58.14 the suite cannot verify ZS-M51’s theorems; they are imported at their stated strength. **NC-M58.15** *\[NEW\]* **Z31 guards an inference, not a manuscript condition**: no check in this suite can detect (P) being dropped from a successor paper.

## **14.4 Gate F-M58-2 — the Wilson-loop cross-check**

ZS-F0 Thm 8.9 gives ZW=; ZS-F47 records it as a *reused* constant. **The Wilson-loop identity remains an optional post-closure cross-check and is barred as a premise.**

## **14.5 Deep exploration — eighth cycle**

**Issue list (MECE, by influence).** **Q1** Are the relations among the transport data stated correctly? **Q2** Is the middle datum one object or two? **Q3** Is the ledger size invariant under regression? **Q4** Does each guard’s stated role match what it computes?  
**Tree and statuses.**  
Q1 relation directions  
 |-- Q1a  v1.6 certificate proves ENDPOINT \=/=\> LIFT   REFUTED (mislabelled)  
 |-- Q1b  LIFT \=\> ENDPOINT holds: a \= exp(L)           PROVEN  (Z34)  
Q2 identity of the middle datum  
 |-- Q2a  exp: C \-\> C^\* is the universal cover         IMPORTED-PROVEN  
 |-- Q2b  endpoint-fixed class \<=\> branch \<=\> k in Z   PROVEN  (Z35, Z36)  
 |-- Q2c  v1.6's "not conversely" was false            REFUTED  
 |-- Q2d  U(1) transport \=/= C^\* multiplier path       PROVEN  (Z38, Z39)  
Q3 ledger invariance  
 |-- Q3a  v1.6 shrank to 160 rows with no artifact     REFUTED  
 |-- Q3b  fixed 173 rows in all seven scenarios        PROVEN  (regression)  
Q4 guard roles  
 |-- Q4a  Z25 is a negative control, not a detector    PROVEN  
 |-- Q4b  Z31 guards an inference only                 PROVEN  (NC-M58.15)  
**Convergence.** 1220\. Cycle 2 changed only Q1b/Q2b (promoted after the covering-space argument was written) and Q1a/Q2c/Q3a (**three demotions** — the tree refuted three of this paper’s own claims, one of them a theorem registered PROVEN). **CONVERGES.**  
**Self-reference check across seven rounds.** The failure mode is now fully characterised, and round 7 fits it exactly. **Almost every error has sat at a boundary — between a structure and its coordinates, between an object and its provenance, or between the two directions of an implication.** A Kraus phase confused with a boundary frame; a covariance with a gauge; a channel fixed up to conjugacy with one fixed in a frame; a file matching its own hash with a file its neighbour produced; and now a certificate proving X⇏Y cited as proving Y⇏X, with two descriptions of one integer counted as two independent data. The countermeasure remains mechanical: each relation now carries its direction explicitly, each datum its type, each guard a statement of exactly what it guards, and the ledger a fixed size so that absent evidence cannot masquerade as passing evidence.  
---

# **§15. Zero free parameters and anti-circularity**

## **15.1 Parameter audit**

Inputs: A=35/437, Q=11, dimZ=2, z\*, , sc, nc, xc — all LOCKED in ZS-M1/ZS-M51, none introduced here. Route B’s chain is strictly  
scncxccensus5,14cizz\*,  
consuming **no Z-Spin constant** and producing  as an output (Z30).

## **15.2 The two-file firewall — fail-closed, provenance-bound, fixed-size**

**Seven verified code defects across audits 4–7, all reproduced and closed.**

| \# | Defect in the prior version | Fix | Guard |
| ----- | ----- | ----- | ----- |
| 1 | v1.3 scanner truncated its own source | whole-file scan over ten fragment-assembled tokens | Z26 |
| 2 | v1.3 digest never recomputed | payload/envelope, one canonical serialisation, recomputed | Z24 |
| 3 | v1.4 missing artifact recorded as a declaration | artifact **required** | Z20 |
| 4 | v1.4 missing source made the guard PASS | source **required**; residual 1.0 | Z20b |
| 5 | v1.4 firewall guard was a string tautology | mutated copy **executed as a subprocess** | Z26, Z26b |
| 6 | v1.5 verified integrity, not provenance | source\_sha256 in the envelope; module tag read; **pristine copy re-run and payload compared byte-for-byte** | Z20c–Z20f |
| 7 | **v1.6 ledger shrank when evidence was absent** | artifact-dependent rows emitted as explicit **FAIL** rows; ledger size is now invariant | Z24, Z25, Z27–Z30 |

**Regression, re-verified. The total is 173 in every row — that is the point.**

| Scenario | Result | Failing checks |
| ----- | ----- | ----- |
| clean pipeline | **173/173 PASS**, exit 0 | — |
| artifact deleted | 163/173, FAIL 10, exit 1 | Z20, Z20d–Z20f, Z24, Z25, Z27–Z30 |
| v1.4-generated artifact beside the v1.7 source | 170/173, FAIL 3, exit 1 | Z20d, Z20e, Z20f |
| valid artifact beside a two-line stub source | 169/173, FAIL 4, exit 1 | Z20c–Z20f |
| source edited (comment appended) after generation | 172/173, FAIL 1, exit 1 | Z20f |
| payload tampered, hash left stale | 171/173, FAIL 2, exit 1 | **Z20d and Z24** |
| construction source deleted | 166/173, FAIL 7, exit 1 | Z20b, Z20c–Z20f, Z26, Z26b |

**\[H2, audit 7.\]** v1.6 reported the artifact-deleted case as “156/166”; the actual output was TOTAL 160, PASS 156\. Six rows had not been emitted. Fixed.  
**\[H3, audit 7.\]** Payload tampering is caught by **Z20d and Z24**. **Z25 is a negative-control digest-sensitivity guard** — it verifies that mutating a payload changes its digest — and it correctly **PASSES** in the tampered scenario. The v1.6 phrasing “tampered payload (Z24/Z25)” is corrected throughout.  
**Direct firewall attack.** Injecting LAMBDA \= 123 into the construction body yields FIREWALL VIOLATION \-- forbidden token present: LAMBDA, exit code 1, no artifact. The construction module writes its artifact **script-relative**.  
**Binding on ZS-S28 / ZS-M60,** four files: cellular action; boundary frame; CTP Choi; and only the last may load . The same whole-file scan, canonical-hash discipline, required-evidence policy, clean-regeneration provenance binding, subprocess attack tests **and fixed-size ledger** apply, and aS14 must be a **certified complex interval with an analytic tail bound** (F-M58.27).

## **15.3 Check taxonomy**

**A** analytic, **R** regression, **X** guard, **P** proxy, **D** declaration; no check returns a literal boolean. **A** \= **92, R** \= **27, X** \= **30, P** \= **4, D** \= **20; total 173; PASS 173; FAIL 0\.**  
Per NC-M58.9 these verify the target algebra, the conditional implications, the M51 arithmetic and the firewalled, provenance-bound construction. **None verifies an S14 channel.**  
Among the thirty guards, **eighteen enforce refutations of earlier versions of this paper** — N06, N08, B06, G03, G08, Z06, Z20, Z20b, Z20c–Z20f, Z25, Z26, Z26b, Z37, Z39, and the six FAIL-row guards of the fixed ledger — one (Z15) refutes a mechanism proposed by audit 3, and one (Z31) refutes v1.4’s reading of M58.22A.  
---

# **§16. Falsification gates**

**Mathematical.** F-M58.1–F-M58.7; F-M58.25 Kraus phases shown to move a; F-M58.29 orde2i/m−1m−1; F-M58.35 a unital, completely positive, complete-order-isomorphic map of M2 that is not a \*-isomorphism; F-M58.36 a covariant CPTP channel automatically QND; F-M58.39 a one-event channel intertwiner shown to imply (G2) or (G3); F-M58.42 a complete-order intertwiner shown to preserve the pointer automatically; **F-M58.46** *\[NEW\]* an endpoint datum shown to determine the lift, or an endpoint-fixed homotopy class shown not to determine the branch — either refutes M58.5″. **F-M58.26 is RETIRED**: it asked for “an endpoint shown to determine winding”, which is now the content of F-M58.46 stated correctly.  
**Construction (binding on ZS-S28/M60).** F-M58.8–F-M58.15, F-M58.27, F-M58.30; F-M58.37 QND from covariance rather than a conserved current; F-M58.40 AS14ptr not a unital C\*-algebra isomorphic to M2C; F-M58.43 the action-derived pointer maps to a rotate of Zpath.  
**Character reduction.** F-M58.21 (H-BR) fails; F-M58.22 (G1) fails **or is shown not to be well-typed**; F-M58.23 (G3​S14) i/2; F-M58.24 two action families with different lifts.  
**Holonomy–expansion.** F-M58.31 (H-ZSQ) fails; F-M58.32 (H-MIN) fails; F-M58.33 the census is corrected away from 5,14; F-M58.34 the gates intersect in 1 integer; F-M58.38 a **non-diagonal** holonomy with d2-cycle transitivity would **reopen an alternative (H-ZSQ) mechanism without refuting M58.23(ii)**.  
**Suite integrity, provenance and reporting.** F-M58.41 the scan misses a banned token, or the recomputed digest fails to detect tampering; F-M58.44 the suite PASSES with any required evidence absent; F-M58.45 an artifact is accepted that the current source cannot reproduce byte-for-byte; **F-M58.47** *\[NEW\]* the ledger row count is shown to vary between scenarios, or a guard’s stated role is shown to differ from what it computes.  
**Class and clock.** F-M58.16–F-M58.20.  
**Status.** No falsification triggered.  
---

# **§17. Corrections and dependency audit**

## **17.1 Cumulative audit response**

| Round | On | Items | Errors | Mandates | Principal actions |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | v1.0 | 6 | 6 | 0 | R1–R5 retractions; status downgrade |
| 2 | v1.1 | 3 | 2 | 1 | C1–C3; §12 built |
| 3 | v1.2 | 6 | 5 | 1 | D1–D6; compression theorem built |
| 4 | v1.3 | 6 | 4 | 2 | E1–E6; two firewall exploits closed |
| 5 | v1.4 | 5 | 4 | 1 | F1–F5; condition (P); end-to-end attacks |
| 6 | v1.5 | 5 | 5 | 0 | G1–G5; provenance binding |
| 7 | v1.6 | 3 | 3 | 0 | **H1 M58.5″; H2 fixed ledger; H3 guard roles** |
| **Total** |  | **34** | **29** | **5** | one correction returned to audit 3 (M58.23(ii)) |

## **17.2 Retraction register (cumulative)**

| Statement | Treatment |
| ----- | ----- |
| v1.0: the frame group is ZS-M53’s Kraus U12 | **RETRACTED (R1)** |
| v1.0: argaS14 is pure gauge | **RETRACTED (R2)** |
| v1.0: frame element  Abel step  branch | **RETRACTED (R3)** |
| v1.0: the entire Euclidean class is closed negative | **RETRACTED (R4)** |
| v1.0: the one-event measure *is* a wrapped Gaussian | **RETRACTED (R5)** |
| v1.0: F-M54-16′ RETIRED-BY-RESOLUTION | **RETRACTED** |
| v1.1: conditions are (H-BR)(G1)(G2) | **CORRECTED (C1)** |
| v1.1: c=i/2 from dimZ=2 alone | **RETRACTED (C2)** |
| v1.1: the cd family is a ZS-M1 family | **CORRECTED (C2)** |
| v1.1: orbit weights are dissolved | **SOFTENED** |
| v1.1: T0=1 supplies R | **SOFTENED** |
| v1.1: the MC is ANALYTIC evidence | **RECLASSIFIED (C3)** |
| v1.2: M58.17 as a single theorem | **SPLIT (D1)** |
| v1.2: (G1) is well-typed | **RE-TYPED (D2)** |
| v1.2: Y17 is primary anti-numerology evidence | **RELABELLED (D3)** |
| v1.2: two independent determinations | **RESTATED (D4)** |
| v1.2: the script firewall protects Route B | **CORRECTED (D5)** |
| v1.3: five hypotheses “follow” from a channel intertwiner | **RETRACTED (E1)** |
| v1.3: J=AdV with no type premises | **CORRECTED (E2)** |
| v1.3: F-M54-16′ is “one morphism wide” | **RETRACTED (E1)** |
| v1.3: F48’s Ew is the carrier | **CORRECTED (E3)** |
| v1.3: the module has a self-scanning firewall | **RETRACTED (E4)** |
| v1.3: the artifact is hash-protected | **RETRACTED (E4)** |
| v1.3: full proofs are in Appendices A–D | **CORRECTED (E5)** |
| v1.4: (13.2) alone gives the fixed-frame identity | **CORRECTED (F1)** |
| v1.4: both code exploits are now guards | **CORRECTED (F4)** |
| v1.4: the class of failure cannot recur without turning the ledger red | **RETRACTED (F2, F3)** |
| v1.4: verifier terminal report | **CORRECTED (F5)** |
| v1.5: the artifact is provenance-protected | **RETRACTED (G1)** |
| v1.5: audit-item arithmetic | **CORRECTED (G2)** |
| v1.5: S14=QND as a literal identity | **CORRECTED (G3)** |
| v1.5: M58.5′ “none determining another” | **CORRECTED (G4)** — and now superseded entirely |
| v1.5: M58.22A listed under two statuses | **CORRECTED (G5)** |
| **v1.4–v1.6: the Four-Datum Separation** | **SUPERSEDED (H1)** — the certificate’s direction was inverted, the homotopy class and the branch are one datum, and the datum’s type was wrong. Replaced by M58.5″ |
| **v1.6: “156/166” for the artifact-deleted regression** | **CORRECTED (H2)** — the ledger had shrunk to 160 rows; the size is now fixed at 173 |
| **v1.6: “tampered payload (Z24/Z25)”** | **CORRECTED (H3)** — Z20d and Z24 detect it; Z25 is a negative control that passes |
| **v1.6: “pointer condition dropped  ledger red”** | **RETRACTED (H3)** — Z31 guards an inference only (NC-M58.15) |
| Inherited: tensor no-go  CP no-go; transfer matrix selects weights; \=ZW closes the channel; unpointed dilation identifies the contraction | RETRACTED / BARRED / CLOSED-NEGATIVE |

## **17.3 Version-to-version impact**

No locked number is moved. ZS-M1, ZS-M51, ZS-F47, ZS-F5, ZS-F0, ZS-F1, ZS-M46, ZS-M53, ZS-M56, ZS-M57, ZS-U12 are consumed at their stated strengths, none strengthened or weakened. **ZS-F48**: scope narrowed *in this paper’s use of it* — an amplitude-damping precursor. **ZS-Q18**: Theorem Q18.12 is load-bearing and verified here (Z18b). **ZS-M57**: its M57.T.2′ branch structure is now correctly located in layer L2 of M58.5″; no ZS-M57 claim changes. **ZS-M54**: F-M54-16′ is re-typed as REFORMULATED / DECOMPOSED — OPEN with two conditional routes; no theorem touched. **ZS-S14 / S20–S24**: ZS-S28 must settle (G1) first, then (G2), (G3​S14), (H-PROC), **(P)**, and (H-BR); or build J with (P) directly. **No downstream paper is invalidated**; in particular nothing in §§11–13 depended on the mis-stated directions of the superseded Four-Datum Separation.

## **17.4 Observational consistency**

Nothing here touches an observable. Planck 2018 CDM fits and all ZS-A/ZS-U predictions are untouched by construction.  
---

# **§18. Conclusion**

Seven audits. Thirty-four items, all upheld, twenty-nine of them errors. Among them: a group misidentified, a covariance mistaken for a gauge, a positivity argument a 22 matrix refutes, a condition list contradicting the paper’s own register, a statistic counted as analysis, a compression presented as a reduction, a carrier lineage run together, a channel equivalence mistaken for a pointer identification, a source scanner that scanned part of its file, a hash nobody checked, two verification paths that passed when the evidence was absent, a report contradicting the paper printing it, an artifact matching its own hash while produced by a different program, a ledger that quietly shrank so that a failure could be reported against a smaller denominator, and — in the last round — a theorem registered PROVEN whose certificate proved the converse of what it claimed, while counting two descriptions of one integer as two independent data.  
Read together they have one shape. Almost every error sat at a boundary: between a structure and its coordinates, between an object and its provenance, or between the two directions of an implication. A phase belonging to an instrument confused with a phase belonging to a boundary; a channel fixed up to conjugacy with one fixed in a frame; a fixed point with the path reaching it; a file that hashes correctly with a file its neighbour produced; and a proof that X⇏Y read as a proof that Y⇏X. The countermeasure is mechanical rather than rhetorical: every relation now carries its direction, every datum its type, every guard a statement of exactly what it guards, and the ledger a fixed size in every scenario so that missing evidence cannot be reported as a smaller failure. Eighteen of the thirty guards in this suite exist for no purpose other than to keep an earlier version of this paper from being believed.  
What ZS-M58 closes is a selection problem, and it closes it well. If the primitive-event boundary map composes multiplicatively in a boundary log-coordinate and is holomorphic there, it is an exponential with one complex generator, and its linearisation at the fixed point is c z\* — a product of two single-valued numbers, no logarithm, hence no lift ambiguity. That generator is i/2, and it is no longer one corpus line: ZS-M51’s fixed-point census, whose only numerical input is the Dottie number, places the first contracting saddle at 5,14, where the map *is* iz, the primitive holonomy *is* i, its order *is* four, and the multiplier modulus *is* . That computation runs in a module which cannot name dimZ, z\* or ; whose refusal behaviour is tested by executing a poisoned copy of itself; and whose output the comparison layer will not accept unless it can regenerate it, byte for byte, from the source standing beside it.  
What ZS-M58 does not close is the realization. Order-4 covariance is not enough for the pointer property, so the process gate needs a conserved current, not a symmetry. The right-hand side of the required diagram exists, but it is ZS-Q18’s full-state carrier and not ZS-F48’s amplitude-damping precursor, and the two differ by exactly one real coordinate, measured by a Jacobian rank rather than asserted. The compression theorem bypasses four hypotheses rather than deriving them, and relocates the burden into a single object — which must also carry the pointer, since a complete-order isomorphism can put it anywhere on its orbit.  
So the terminal statement is:

**ZS-M58 closes the mathematical target-selection and character-reduction layers, including a complementary holonomy–expansion determination of the quarter-turn. It does not close the ZS-S14 physical realization of the channel. The remaining bridge is an action-derived, pointer-preserving complete-order intertwiner between the S14 pointer process and the ZS-Q18 full-state QND carrier — one unknown physical structure, not one unknown number.**

**F-M54-16′ remains open.** It passes to ZS-S28 and ZS-M60. **ZS-M58 closes at v1.7.**  
---

# **Acknowledgements & Code Availability**

This terminal version integrates seven external audit rounds; all thirty-four items are upheld and none contested. Every counterexample and all seven code defects are reproduced as machine checks; the fail-closure, provenance binding and fixed ledger size are demonstrated by seven regression runs (§15.2). Audit 7’s correction to M58.5′ — a theorem this paper had registered PROVEN — is adopted in full and the superseded statement is recorded in §5.3 so that it cannot be cited. ZS-M51 v1.3, ZS-F47 v1.6, ZS-F48 v1.6 and ZS-Q18 v1.7 are load-bearing; their open bridges are named (H-MIN) and (H-ZSQ) and carried at their own strength.  
**zs\_m58\_expansion\_construct\_v1\_7.py** — \-blind construction layer. Permitted input: . Ten banned tokens assembled from fragments, whole-file scan, abort with exit code 1 on any hit; artifact written script-relative as a {payload, sha256, source\_sha256} envelope under one canonical serialisation. **zs\_m58\_verify\_v1\_7.py** — comparison layer. Requires the artifact (Z20) and the source (Z20b); re-runs a pristine copy and compares byte-for-byte (Z20c, Z20d); checks the module tag (Z20e) and the bound source hash (Z20f); recomputes the payload digest (Z24); runs two subprocess firewall attacks (Z26, Z26b); verifies the corrected endpoint–lift relations (Z34–Z40); guards the pointer inference (Z31, Z32); emits a **fixed 173 rows in every scenario**; and makes the single target comparison at Z30. Neither computes a candidate aS14; neither loads ZS-S14 data. Requires numpy, scipy, mpmath.  
Ledger: **173/173 PASS** (92 A · 27 R · 30 X · 4 P · 20 D), 0 FAIL. Zero fitted parameters; A,Q,dimZ=35/437,11,2, z\*, , sc, nc, xc LOCKED and unmodified.  
---

# **Appendix A — Full proofs of M58.1 and M58.2**

**A.1.** A grading-preserving embedding HSHE↪Hreg requires dimHSdimHEdimHreg **and** a multiplicity match between JSJE and JR|; ZS-M56 M56.21′ shows the latter fails at Q=11 (qR=1 versus dimE2). A Choi rank-r correspondence requires only C≽0 of rank r with TroutC=Iin — a condition on a cone in a Hom-space. Q=11 prime is the counterexample in the forbidden direction. ▫  
**A.2.** 21: if every Ki=diagki0,ki1 then Pj=ikij2Pj, and iKiKi=I forces the coefficient to 1\. 13: 1 fixes C00,00=C11,11=1 and C01,01=C10,10=0; for C≽0 with Cjj=0 the 22 principal minor on {j,k} equals −Cjk20, forcing Cjk=0; so rows and columns 01,10 vanish and suppCZ. 32: eigenvectors of C lie in span{00⟩,11⟩}, each yielding a diagonal Kraus operator. ▫  
---

# **Appendix B — The boundary-frame group; and what it is not**

U=diag1,ei commutes with Zpath. The multiplier law is read from the defining matrix element: substituting the rephased frame vectors into a=⟨0out0in⟩⟨1in1out⟩, the bra contributes e−iin and the ket e+iout, giving (4.1). Z is spanned by coordinate vectors, so QND survives (G05); Trout is unchanged on the diagonal, so TP survives (G06). A Kraus rephasing leaves every channel term unchanged, hence a unchanged (N01).  
---

# **Appendix C — Defect and characteristic-function calculations**

DT=DT\*=1−a2; d+,d−=1,1; a0=−a; aa=0; a1 on T; deg=1 by winding. At : \=0.4529939978; Choi nonzero spectrum {1.8915135658, 0.1084864342}; Liouville spectrum {1,1,,‾}. Pre-registered residuals: mod (frame-free); 0 (report only alongside the transport used); r at a radius fixed before unblinding.  
---

# **Appendix D — Poisson dilation and the universality no-go**

Pa=1−a2/1−a‾2; ⟨1,Mn1⟩a=an for four values of a and n5 (residual 5.610−16). Pa\>0 a.e. Pa is unitary and intertwines M with M; the parameter migrates to a=Pa, and the two cyclic vectors differ (P05, guard).  
---

# **Appendix E — The endpoint–lift correspondence, worked**

For a=, Log=−0.11483462499600948+2.2592495539025985 i, and

| k | ℓk=01a/a ds | Log+2ik | |ℓk−Log+2ik| | |eℓk−| |
| ----- | ----- | ----- | ----- | ----- |
| −2 | −0.114834625−10.307121060 i | same | 0 | 7.110−16 |
| −1 | −0.114834625−4.023935753 i | same | 0 | 5.010−16 |
| 0 | −0.114834625+2.259249554 i | same | 0 | 2.510−16 |
| \+1 | −0.114834625+8.542434861 i | same | 1.810−15 | 1.710−15 |
| \+2 | −0.114834625+14.825620168 i | same | 1.810−15 | 1.410−15 |

Minimum pairwise gap \=2 exactly, so the class-to-lift map is injective; every ℓk exponentiates to the same , so the endpoint does not determine k. Modulus behaviour: a U1 transport path has as1 (variation 4.410−16); the C multiplier path has as running over 0.891514, 1.  
---

# **Appendix F — The Character Reduction and the holonomy gate, worked**

**F.1** Forward generator c=2i/dimZ2=i/2=1.5707963267948966 i. **F.2** (G1) at z2=0 gives T0=1; with (G2), T′=cT, unique solution ecz; eiz/2=iz (1.110−41); z\* recovered at 5.410−20; DTz\*=c z\*= at 8.510−20. **F.3** Thresholds \=0.7390851332151606417, sc=1.9613088464594559402, nc=3.2035675148878048513, xc=0.3121519978438855970. **F.4** Multipliers: x=13 (m=4) 1.03304205, repelling; x=121.24631415; x=14 (m=5) 0.891513566, **contracting**; x=190.542970469. **F.5** Census Nm=0 for m4, 1 at m=5, 2 at m=8. Holonomy order m−1 exact for m=311 (10−25). **F.6** Firewalled artifact: m=5, x0=0.25, c=1.570796326794896619 i, H=i of order 4, mult=0.8915135657760470429, htop=1.6094379124341004; digest recomputed at Z24, payload regenerated and compared at Z20d, source hash bound at Z20f.  
---

# **Appendix G — The intertwiner and suite-integrity blocks, worked**

**Charge grading.** Addiag1,i: E00↦E00, E11↦E11, E01↦−iE01, E10↦+iE10.  
**Non-QND counterexample.** p=0.18, a=0.6+0.3i: Choi min eigenvalue 0.1492\>0; TP residual 0; covariance residual 0; QND residual 0.18.  
**Channel intertwiner and the pointer condition.** J=AdV, V random: CP 2.510−17; TP 2.310−16; QND (rotated pointer) 3.310−16; rank 2; multiplier 4.010−16. Fixed-frame QND residual 0.626 (Z31). With V=diag1,ei, fixed-frame QND holds at 1.110−16 (Z32).  
**Single-cycle test.** d=2,3,4: ordAdUd=4,9,16=d2; diagonal matrix units fixed 2,3,4 — never a single cycle.  
**Carrier ledger.** AD linearity 1.810−15; ADEw=Ew at 1.110−16; dephEfullp,w=Efullp,w at residual 0; Jacobian ranks 2 and 3\.  
**Suite integrity and provenance.** Artifact and source required (Z20, Z20b); clean regeneration runs and emits (Z20c); payload and digest match byte-for-byte (Z20d); module tag correct (Z20e); bound source hash matches (Z20f); payload digest recomputed (Z24); digest sensitivity negative control (Z25); two subprocess attacks refused (Z26, Z26b).  
---

# **Appendix H — Verification ledger summary**

| Block | Tags | Class mix |
| ----- | ----- | ----- |
| Locked constants | C01–C08 | 2A, 5R, 1X |
| Target algebra | T01–T09 | 8A, 1R |
| QND–Equalizer | E01–E08 | 5A, 3X |
| Characteristic function | F01–F08 | 8A |
| Boundary-frame covariance | G01–G10 (13 rows) | 10A, 2X, 1D |
| OS-real reality | H01–H04 | 2A, 2R |
| Poisson universality | P01–P06 | 4A, 1X, 1D |
| Type guard | V01–V03 | 1A, 1X, 1D |
| Route S | S01–S10 | 3A, 2R, 2X, 1P, 2D |
| Branch / lift (historical) | B01–B07 | 3A, 1R, 2X, 1D |
| Factor separation | K01–K03 | 2A, 1D |
| Audit-1 controls | N01–N08 (7 rows) | 5A, 2X |
| Character Reduction | Q01–Q15 | 9A, 3R, 2P, 1D |
| Holonomy–expansion | Y01–Y22 | 10A, 7R, 2X, 1P, 2D |
| Intertwiner, carrier, pointer, suite integrity, provenance, **endpoint–lift relations** | Z01–Z40 (46 rows) | 19A, 6R, 14X, 7D |
| Firewall self-scan | W01–W04 | 1A, 3D |

**Total 173; PASS 173; FAIL 0** — and 173 rows in every regression scenario.  
---

# **Appendix I — Label map across versions**

| v1.0 | v1.1 | v1.2 | v1.3 | v1.4 | v1.5 | v1.6 | v1.7 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| M58.1–M58.3 | same | same | same | same | same | same | **unchanged** |
| M58.4 | M58.4A/4B | same | same | same | same | same | **unchanged** |
| M58.5 | M58.5′ | same | same | \+ cert. | same | wording fix | **SUPERSEDED by M58.5″ (H1)** |
| M58.6–M58.8 | same | same | same | \+ (7.3) | same | same | **unchanged** |
| M58.9 | M58.9′ | same | same | \+ cert. | same | same | **unchanged** |
| M58.10 | M58.10′ | same | same | \+ cert. | same | same | **unchanged** |
| M58.11 | M58.15 | same | same | same | \+ route 2 | same | **unchanged** |
| — | M58.11 | M58.11A | same | \+ (11.1) | same | same | **unchanged** |
| — | M58.12–14 | same | same | same | same | same | **unchanged** |
| — | — | M58.16–20 | 17 split | same | same | same | **unchanged** |
| — | — | — | M58.21 | same | same | same | **unchanged** |
| — | — | — | M58.22 | split A/B | \+ (P) | re-typed | **Z31 role lowered (H3)** |
| — | — | — | M58.23–24 | lineage | same | same | **unchanged** |

---

# **References**

\[1\] W. F. Stinespring, *Proc. Amer. Math. Soc.* **6**, 211–216 (1955). \[2\] A. Jamiołkowski, *Rep. Math. Phys.* **3**, 275–278 (1972). \[3\] M.-D. Choi, *Linear Algebra Appl.* **10**, 285–290 (1975). \[4\] M.-D. Choi and E. G. Effros, “Injectivity and operator spaces,” *J. Funct. Anal.* **24**, 156–209 (1977). \[5\] R. V. Kadison, “Isometries of operator algebras,” *Ann. of Math.* **54**, 325–338 (1951). \[6\] V. I. Paulsen, *Completely Bounded Maps and Operator Algebras* (Cambridge, 2002), ch. 13. \[7\] B. Sz.-Nagy and C. Foiaș, *Harmonic Analysis of Operators on Hilbert Space* (North-Holland, 1970); rev. ed. Springer, 2010\. \[8\] A. Hatcher, *Algebraic Topology* (Cambridge, 2002), §1.3. — path lifting and the universal cover exp:CC. \[9\] K. Kraus, *States, Effects, and Operations*, LNP **190** (Springer, 1983). \[10\] E. B. Davies and J. T. Lewis, *Commun. Math. Phys.* **17**, 239–260 (1970). \[11\] K. Osterwalder and R. Schrader, *Commun. Math. Phys.* **31**, 83–112 (1973); **42**, 281–305 (1975). \[12\] M. Lüscher, *Commun. Math. Phys.* **54**, 283–292 (1977). \[13\] H.-J. Borchers, *J. Math. Phys.* **41**, 3604–3673 (2000); H.-W. Wiesbrock, *Commun. Math. Phys.* **157**, 83–92 (1993). \[14\] S. Attal and Y. Pautrat, *Ann. Henri Poincaré* **7**, 59–104 (2006). \[15\] V. P. Belavkin, *J. Multivariate Anal.* **42**, 171–201 (1992). \[16\] G. Koenigs, *Ann. Sci. École Norm. Sup.* (3) **1**, Suppl. 3–41 (1884). \[17\] G. Szekeres, *Acta Math.* **100**, 203–258 (1958). \[18\] W. Feller, *An Introduction to Probability Theory and Its Applications* II, 2nd ed. (Wiley, 1971), ch. VIII. \[19\] A. S. Holevo, *Probl. Peredachi Inf.* **9**, 3–11 (1973). \[20\] H. Ollivier, D. Poulin and W. H. Zurek, *Phys. Rev. Lett.* **93**, 220401 (2004). \[21\] H. Maassen and B. Kümmerer, *IMS Lecture Notes Monogr. Ser.* **48**, 252–261 (2006). \[22\] E. Hille and R. S. Phillips, *Functional Analysis and Semi-Groups*, AMS Colloq. Publ. **31** (1957), ch. VII. \[23\] R. Remmert, *Classical Topics in Complex Function Theory* (Springer, 1998), ch. 2. \[24\] R. P. Feynman and F. L. Vernon, *Ann. Phys.* **24**, 118–173 (1963). \[25\] A. O. Caldeira and A. J. Leggett, *Physica A* **121**, 587–616 (1983). \[26\] R. M. Corless *et al.*, *Adv. Comput. Math.* **5**, 329–359 (1996). \[27\] C. Walkden and T. Withers, *Nonlinearity* **31**, 2726–2755 (2018). \[28\] M. Urbański and A. Zdunik, *Ergodic Theory Dynam. Systems* **24**, 279–315 (2004). \[29\] K. Kang, *ZS-M1 v1.0* (Z-Spin Cosmology, 2026). \[30\] K. Kang, *ZS-M51 v1.3: Lambert–Dottie Stability of the Exponential Fixed-Point Family, with a Fixed-Point Census* (2026). \[31\] K. Kang, *ZS-F47 v1.6: The Expansion–Contraction Complementarity Principle* (2026). \[32\] K. Kang, *ZS-F48 v1.6: The Local Skew Normal Form and the Global Transfer Programme* (2026). \[33\] K. Kang, *ZS-Q18 v1.7 FINAL: The Dephasing Representative and the Born Rule from i-Tetration* (2026). \[34\] K. Kang, *ZS-F0 v1.0(R)*; \[35\] *ZS-F1 v1.0*; \[36\] *ZS-F5 v1.0*; \[37\] *ZS-M46 v1.5*; \[38\] *ZS-M53 v1.5*; \[39\] *ZS-M54 v2.2 FINAL*; \[40\] *ZS-M56 v1.8 FINAL*; \[41\] *ZS-M57 v1.8*; \[42\] *ZS-S14 v2.0*; \[43\] *ZS-S20 v2.2*; \[44\] *ZS-S21 v1.2 TERMINAL*; \[45\] *ZS-S22 v1.5*; \[46\] *ZS-S23 v1.3*; \[47\] *ZS-S24 v1.9*; \[48\] *ZS-S27*; \[49\] *ZS-U12 v2.3* (all Z-Spin Cosmology, 2026). \[50\] K. Kang, *The Book of Z-Spin Cosmology — Light Edition v12.1* (July 2026).  
---

# **Version History**

**v1.0 (July 2026).** Initial release. Ledger 83/83. **v1.1.** Audit 1, six items: R1–R5 plus the status downgrade. Added the Character Reduction. 105/105. **v1.2.** Audit 2, three items: C1–C3. Built §12, including the recognition that v1.1’s neutral point is the locked sc. 127/127. **v1.3.** Audit 3, six items: D1–D6. Built the compression theorem. 150/150. **v1.4.** Audit 4, six items: E1–E6. Two firewall exploits closed. 156/156. **v1.5.** Audit 5, five items: F1–F5. Condition (P); end-to-end subprocess attacks; script-relative artifact; LaTeX. 162/162. **v1.6.** Audit 6, five items: G1–G5. Artifact–source provenance binding; transported identity; status hygiene. 166/166.  
**v1.7 (July 2026): TERMINAL.** Audit 7, three items, all upheld — one of them a **mathematical error in a theorem registered PROVEN**.  
*Corrected.* **(H1)** the v1.4–v1.6 **Four-Datum Separation is SUPERSEDED** by **M58.5″, Endpoint–Lift–Intertwiner Separation**, with three faults recorded in §5.3 so the old statement cannot be cited: its certificate proved *endpoint* ⇏ *lift* while being labelled the converse (the true direction is **lift  endpoint**, since a=eℓ, check Z34); for endpoint-fixed paths the homotopy class and the logarithm branch are **one datum**, both classified by the same integer because exp is the universal cover of C (Z35, Z36), so v1.6’s “D2D3 but not conversely” was false; and the datum was typed as a U1 transport while the proof integrated a C multiplier path, which carries modulus evolution a U1 path cannot (Z38, Z39). Four data become **three layers**, with L2L1, L1⇏L2, L1L2⇏L3. New gate F-M58.46; F-M58.26 retired as mis-stated. Nothing in §§11–13 depended on the erroneous directions. **(H2)** the ledger **no longer changes size**: with the artifact absent, v1.6 emitted only 160 rows, so its reported “156/166” was wrong; artifact-dependent checks are now emitted as explicit FAIL rows and the total is **173 in all seven regression scenarios**. New gate F-M58.47. **(H3)** two guard roles corrected: payload tampering is detected by **Z20d and Z24**, while **Z25 is a negative-control digest-sensitivity guard that correctly PASSES**; and **Z31 guards only the inference** that pointer preservation follows from complete-order equivalence — it cannot detect (P) being dropped elsewhere (NC-M58.15).  
*Terminal verdict.* ZS-M58 closes the mathematical target-selection and character-reduction layers, including a complementary holonomy–expansion determination of the quarter-turn. It does **not** close the ZS-S14 physical realization. The remaining bridge is an action-derived, **pointer-preserving** complete-order intertwiner between the S14 pointer process and the ZS-Q18 full-state QND carrier — **one unknown physical structure, not one unknown number**.  
*Ledger.* **173/173 PASS** (92 ANALYTIC \+ 27 REGRESSION \+ 30 GUARD \+ 4 PROXY \+ 20 DECLARATION), 0 FAIL, with a **fixed row count in every scenario**. Thirty guards, of which eighteen enforce refutations of earlier versions of this paper. Companions zs\_m58\_expansion\_construct\_v1\_7.py and zs\_m58\_verify\_v1\_7.py. Zero free parameters; A,Q,dimZ=35/437,11,2, z\*, , sc, nc, xc LOCKED. **ZS-M58 CLOSES at v1.7.**