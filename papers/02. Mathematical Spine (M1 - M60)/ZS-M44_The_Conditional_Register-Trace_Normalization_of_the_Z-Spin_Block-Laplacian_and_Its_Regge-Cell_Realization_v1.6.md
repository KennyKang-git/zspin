# **ZS-M44**

# **The Conditional Register-Trace Normalization of the Z-Spin Block-Laplacian and Its Regge-Cell Realization: Exact Removal of a Spurious Sector Asymmetry and the Open Regge-Hessian Gate**

**Author:** Kenny Kang  
**Date:** July 2026  
**Theme / Code:** Math Spine / ZS-M44 · Companion to ZS-M6 · Upstream of ZS-F36  
**Verification:** 19/19 PASS | **Zero fitted parameters** | corrects the a0/a1 conflation; establishes the **normalized-trace bridge** 2=A,⟨a|Q|a⟩=A/Q (with Q=IQ/Q) **DERIVED-CONDITIONAL** on that register-scalar density; integrates ZS-M45’s Regge-cell lemma (§6), whose global operator RIQ is **OPEN**; the R-2 **perturbation-artifact correction** (§10.4 0.855​​X/Y trap) stands as the firm result | (**A**, **Q**, dim **Z**) \= (**35/437**, **11**, **2**) **LOCKED**.  
---

## **§0. Abstract**

ZS-M6 proved 2=A/Q=35/4807 under three honest caveats — **R-1** (the 1-loop Regge-lattice derivation was heuristic), **R-2** (the register-scalar assumption), **R-3** (rank-1 from the action). This paper’s firm result is narrower and honest: it **exactly removes a spurious sector-asymmetry artifact** (PROVEN), reduces 2=A/Q to a single **register-trace normalization** (Q=IQ/Q; DERIVED-CONDITIONAL), and — via the integrated ZS-M45 Regge-cell lemma and a **graph-Laplacian coordinate diagnostic** (§6.3) — shows the local cell deficit is sector-uniform while the **global register-scalar operator** RIQ **remains OPEN**. The diagnostic (coordinate Rayleigh quotients 0.600 vs 0.244; graph eigenvalue triples 2−2 vs 0.243) gives *evidence* the sector diagonals differ, but is **not** the genuine BWhingeB Regge Hessian; it narrows the residual to the action-level selection of a register measure (mode-count and metric being two benchmarks), with the a0 heat-trace coefficient arguing for the democratic mode-count reading but not deriving it.  
**R-1 (Register-Trace Normalization, M44.T1) \[DERIVED-CONDITIONAL\].** In the finite-matrix heat trace Tr,e−tL=a0−a1t+, the *mode count* is a0=dim=Q (leading rank coefficient) — **not** a1=Tr,L (which equals 13.30Q). The per-mode normalization is the **normalized trace** Q=Q−1Tr. With the Gilkey product coupling A=XY (PROVEN) *and the assumption that* A *distributes via the maximally-mixed register density* \=IQ/Q, the per-mode cross-coupling is 2=A,Q-projected=A/Q. The value is correct; but \=IQ/Q is *asserted* (as the symmetry-natural / democratic state), **not derived from the action** — so R-1 is DERIVED-CONDITIONAL on this register-trace normalization, and merges with R-2. (A separate, genuine fact from ZS-M6 §4.3: a1=Tr,L is coupling-immune, since V is off-diagonal — this preserves the *mode count* but does not by itself fix the democratic *distribution*.)  
**R-2 (democratic normalization).** The register-scalar assumption splits into (a) **within-irrep** constancy and (b) **cross-sector** democratic normalization. R-2(a) is DERIVED: a G-equivariant coupling is a scalar on each irrep (Schur), and all three targets are dimension-3 irreps of the polyhedral symmetries (Oh for X, Ih for Y). R-2(b) is **constrained** by an **exact arrowhead inverse-eigenvalue solve** of the ZS-M6 §2.3 spectrum (a *consistency* check, not an action-independent forward derivation): the recovered couplings are gX2/2=2.996, gY12/2=2.989, gY22/2=3.021 — **democratic to 0.45%** (input-precision-limited), decisively excluding the sector-weighted alternative (gX2/gY2=X/Y=0.865, a 13.5% gap). The exact solve also **corrects ZS-M6 §10.4**: the reported ratios 2.61,3.05,3.13 are an artifact of the 2nd-order formula g2=−0, which happens to mimic X/Y — a genuine trap that could be misread as sector-weighting.  
**R-3** is DERIVED-CONDITIONAL (on mediator Hom-multiplicity-one) from ZS-M6 §7A (all-orders LXY=0 \+ Schur); the intertwiner multiplicities dimHomGVX,VZ, dimHomGVZ,VY are not computed here.  
**Result (honest).** The firm result is the **R-2 perturbation-artifact correction** (§5.4): the ZS-M6 §10.4 “\~15% asymmetry” is a 2nd-order-perturbation artifact spuriously mimicking X/Y; the exact arrowhead solve gives democratic g2/23. The **register-scalar normalization** (2=A/Q, and greg2=6A/Q) is **DERIVED-CONDITIONAL on register-trace normalization** — the assumption that A distributes via \=IQ/Q, which R-2(a) Schur constrains within each irrep but which is not derived from the action across sectors. The arrowhead inversion (§5.3) and the 50-digit recompute (§5.5) are **consistency checks** (they use, or reconstruct with, the democratic ansatz), *not* a fully action-independent forward derivation. Consequently the ZS-F36 Gs=1 normalization is **DERIVED-CONDITIONAL on register-trace normalization**, not “discharged.” The metric-scale no-go (MUV) is untouched. Verification 19/19 \+ 14/14 PASS.  
---

## **Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| **PROVEN** | Explicit proof or exact machine verification; no undischarged assumption. |
| **DERIVED** | Follows from PROVEN results by stated steps; no new parameter. |
| **DERIVED-BY-INHERITANCE** | Uses an upstream corpus result, not re-proven; inherits its (now-discharged) caveats. |
| **CONFIRMED-NUMERICALLY** | Established by an exact computation to a stated, input-limited precision. |
| **IMPORTED-PROVEN / STANDARD** | Established externally (Gilkey heat-kernel theory, Schur’s lemma). |
| **IDENTITY** | Arithmetic consistency; no new physical content. |
| **OPEN** | A genuine remaining gap. |

---

## **§1. Introduction**

ZS-M6 constructed the 1111 register Block-Laplacian L=LXLZLY+CXZ+CZY with rank-1, 0-selected cross-coupling \=A/Q, proved 2=A/Q (Register-Total Normalization) and g2=dim2 (Dimensional Coupling Norm), and flagged **R-1** (heuristic 1-loop normalization), **R-2** (register-scalar assumption), **R-3** (rank-1 from the action). ZS-M44 v1.0–v1.1 addressed these; **the current version corrects the** a0/a1 **conflation and honestly re-scopes the result**: the firm advance is the R-2 perturbation-artifact correction; the register-trace normalization 2=A/Q is DERIVED-CONDITIONAL on the register-scalar density \=IQ/Q.  
Locked inputs: X=5/19 (truncated octahedron, Oh), Y=7/23 (truncated icosahedron, Ih), A=XY=35/437, Q=11, Z,X,Y=2,3,6.  
---

## **§2. Heat-kernel setup and the finite-register heat-trace moments**

The 1-loop effective action is \=12TrCQlogL=−120dttTr,e−tL, with Tr,e−tL=a0−a1t+a2t2−, a0=dim, a1=Tr,L, a2=12TrL2. Writing L=L0+V (V the unit rank-1 0-selected structure coupling 0 to the nine target modes — X triplet, Y triplets T1u,T2u — with the Z2-odd mode decoupled):  
a0=dim=Q=11 (mode count \= leading rank coeff),  a1=Tr,L=13.30 a1=0, coupling-immune,  a2=122TrV2.  
**Correction (external review 1.2):** the mode count is a0=dim=Q, the *leading* coefficient — not a1. a1=Tr,L=13.30Q; its coupling-immunity (a1=0, since V is off-diagonal) is a *separate* fact that preserves the mode count but does not fix the democratic distribution. The “/Q” is the **normalized trace** Q=Q−1Tr (with Q=a0). *(Verified: a0=Q=11, a1=Tr≠Q, tau\_Q normalization.)*  
---

## **§3. R-1: the Register-Trace Normalization Theorem (M44.T1)**

**Theorem M44.T1 (Register-Trace Normalization). \[DERIVED-CONDITIONAL\]** *If the register-scalar coupling* A *distributes over the register via the maximally-mixed density* \=IQ/Q *(the register-trace normalization), then the per-mode cross-coupling is* 2=A/Q*, with* Q=a0=dim *(the normalized-trace rank) and* A=XY *(Gilkey product).*  
*Proof (conditional).* **(i)** The normalized trace on CQ is Q=Q−1Tr, with rank a0=Q. **(ii)** By the Gilkey product theorem on XY (using su2X,su2Y=0), the effective coupling is eff=XY=A (PROVEN); it multiplies the register norm ||2 in ZS-F1’s 1+A||2R. **(iii)** Assuming A acts through the maximally-mixed density \=IQ/Q, the single-mode cross-coupling is 2=A⟨a||a⟩=A/Q. ;▫ **The undischarged step is (iii):** \=IQ/Q is the *symmetry-natural* / maximal-entropy state, but is **not derived from the parent action**. So M44.T1 closes the *arithmetic* of the register-trace distribution, not a full action-level heat-kernel derivation.  
The “/Q” is the normalized-trace rank a0=Q — well-defined and exact. What remains conditional is the *democratic distribution* (=IQ/Q): why A is spread uniformly rather than sector-weighted. This is the genuine content, addressed (within irreps, and corrected of a false counter-signal) in §5. *(Verified: κ²=A/a0=A/Q arithmetic, rho=I\_Q/Q asserted not derived.)*  
---

## **§4. Consistency: a2=92**

For the rank-1 0-selected structure, TrV2=18 (nine off-diagonal pairs), so a2=92=9A/Q=315/4807=0.06552943, matching ZS-M6 (4.3.1) exactly; the factor 9=33 is (three target irreps)(dimension 3), both PROVEN (ZS-F2 §4.2A). (a2=92 is a *forward consequence* of 2 and TrV2=18; the a2=12TrL2 convention is unaffected by the a0/a1 correction.) *(Verified: Δa2=9κ²=315/4807.)*  
---

## **§5. R-2: the register-scalar embedding (within-irrep resolved, cross-block open)**

### **§5.1 The split**

The register-scalar assumption R-2 — that A acts as A,IQ — decomposes into two logically distinct claims:

* **R-2(a) within-irrep:** the coupling is constant on each target irrep (no splitting within a triplet).

* **R-2(b) cross-sector:** the *same* 2 applies to all sectors (X2=Y12=Y22), i.e. g2=dim2 is democratic — as opposed to sector-weighted (2sector).

R-1 (§3) supplies the register *average* A/Q; it does not by itself fix the per-sector breakdown, which is R-2(b).

### **§5.2 R-2(a) — within-irrep constancy \[DERIVED\]**

The register carries the polyhedral symmetries Oh (X) and Ih (Y). The non-minimal coupling 1+A||2R is built from the G-invariant register norm ||2 and the G-invariant register curvature, hence the coupling operator is G-equivariant. By **Schur’s lemma**, a G-equivariant operator restricted to an irreducible representation is a scalar. All three targets are **dimension-3 irreps** (T1 of Oh; T1u,T2u of Ih; ZS-F2 §4.2A Adjoint Obstruction, PROVEN). Therefore the coupling is constant within each target — R-2(a) is **DERIVED**.  
**Crucial limitation (review error 4).** Schur equivariance under OhIh gives only *block* scalarity: the density is forced to the form \=cZIZcXIXcY1IY1cY2IY2 (one constant per irreducible block), **not** the equality cZ=cX=cY1=cY2 that \=IQ/Q requires. Closing the latter needs one of: (i) a larger symmetry acting transitively across blocks, (ii) a unique KMS state, (iii) an entropy-extremizing state-selection action, or (iv) an explicit Regge-Hessian computation showing all block weights equal (§6.3). None is supplied here — so the *cross-block* equality is the residual OPEN item, not a Schur consequence. *(Verified: dim-3 irreps \=\> Schur scalar; block weights c\_Γ not forced equal.)*

### **§5.3 R-2(b) — democratic across sectors \[CONFIRMED-NUMERICALLY, exact diagonalization\]**

R-2(b) is examined by inverting the ZS-M6 §2.3 spectrum exactly (a consistency check on the democratic ansatz). Because 0 couples only to the three targets, the coupled modes live in a 44 **arrowhead** submatrix with 0-diagonal 1 and target diagonals d=2.0556,2.2778,2.7658; its four eigenvalues are the shifted modes \=0.9517,2.0736,2.2952,2.7787. The arrowhead inverse-eigenvalue formula recovers the physical couplings **exactly** (no perturbation theory):  
c2=g2=−kk−djdj−d.  
The result:

| target | g2/2 (exact) | democratic | sector-weighted |
| ----- | ----- | ----- | ----- |
| X | **2.996** | 3.000 | 3X/‾ |
| Y1 | **2.989** | 3.000 | 3.000 |
| Y2 | **3.021** | 3.000 | 3.000 |

The recovered couplings are democratic to a **0.45% spread** — at the 4-decimal input precision of the §2.3 spectrum. The decisive discriminator: cX2/cY12=1.002, matching democratic (1.000) and **excluding** the sector-weighted prediction X/Y=0.865 by 13.5%. So R-2(b) is **democratic at the consistency level** (the sector-weighted 0.865 is excluded *given* the arrowhead structure). This does **not** by itself close R-2: an action-independent forward derivation, and the global operator RIQ (§6), remain required. *(Verified: g\_Γ²/κ²≈3, spread 0.45%, c\_X²/c\_Y1²=1.002 not 0.865; consistency-level.)*

### **§5.4 Correction to ZS-M6 §10.4 \[honest amendment\]**

ZS-M6 §10.4 reported gX2/2,gY12/2,gY22/22.61,3.05,3.13 — a “\~15% asymmetry” attributed to “4-decimal rounding.” The exact solve identifies the precise mechanism: those numbers come from the **2nd-order perturbation formula** g2=−0, which at this coupling strength (|0|=0.048) carries a 13 error on the X channel. Reproducing that formula gives 2.61,3.05,3.13 and cX2/cY12=0.855 — which **spuriously coincides with** X/Y=0.865. This is a genuine trap: the perturbation artifact *looks like* sector-weighting. The exact arrowhead solve removes the artifact and yields the democratic 2.996,2.989,3.021. The amendment strengthens ZS-M6’s conclusion (democratic g2=32) while correcting its diagnosis (perturbation error, not merely rounding, and a X/Y-mimicking trap). *(Verified: 2nd-order reproduces 2.61, 2nd-order ratio 0.855 mimics dX/dY.)*

### **§5.5 The 50-digit closure \[CONFIRMED-NUMERICALLY, residual eliminated\]**

The v1.1 confirmation was limited to 0.45% by the 4-decimal §2.3 input. This is now removed. Build L at 50-digit precision from ingredients derived **independently of the spectrum**: the sector eigenvalues from the polyhedra graph Laplacians (X=19/18, Y1=23/18, Y2=5−522318); the magnitude 2=A/Q (§3, normalized trace \+ Gilkey); the democratic per-target norm g2=dim2=32=105/4807 (§5.2, Schur \+ Dimensional Coupling Norm); and the rank-1 0-selected structure (§6, R-3). Diagonalizing the resulting arrowhead at 50 digits gives, at \=1:  
\=0.95169951, 2.07357649, 2.29524490, 2.77865788,  
which rounds **exactly** to the ZS-M6 §2.3 values 0.9517,2.0736,2.2952,2.7787 on all four modes. Inverting this 50-digit spectrum via (5.1) recovers  
gX2/2=gY12/2=gY22/2=3.000 max deviation 2.210−58.  
So the exactly-democratic coupling **reproduces §2.3** to 50 digits, and the v1.1 0.45% spread was the 4-decimal rounding of §2.3. **Honest limitation (external review 1.3):** this is a *consistency check*, not a fully action-independent forward derivation. The construction *inputs* the democratic per-target norm g2=32; and the ZS-M6 §2.3 target spectrum may itself have been generated with democratic coupling. A genuinely independent forward computation would build L from the ZS-F1/S14 action and the polyhedral incidence matrices, compute each coupling *without* the democratic ansatz, and only then forward-diagonalize. That computation is **not** performed here. What is established: the democratic ansatz is *internally consistent* with §2.3 to machine precision, and the sector-weighted alternative is excluded *given* the arrowhead structure. *(Verified: 50-digit spectrum rounds to 2.3, inversion g²/κ²=3, positive-definite; consistency-level, not independence.)*  
**Deepest item — see §6.** The one item beyond §5 (an explicit lattice/Regge realization of the register-scalar operator RIQ) is treated in the integrated **§6** (Regge-cell realization). Result: the primitive-cell deficit is sector-uniform (§6.1, DBI), but the global operator equality remains **OPEN** (§6.3, the Regge-Hessian gate). So Q=IQ/Q and hence 2=A/Q remain DERIVED-CONDITIONAL.  
---

## **§6. Regge-cell realization (integrated from ZS-M45)**

This section integrates ZS-M45 v1.1. It addresses the same residual as §5: whether the register-scalar density Q=IQ/Q (equivalently RIQ) can be grounded geometrically, rather than assumed. The honest result is a **partial** advance: local uniformity holds; the global operator equality does not follow.

### **§6.1 Uniform primitive-cell deficit \[DERIVED-BY-INHERITANCE\]**

The ZS-M3 Regge-Holonomy framework gives the holonomy deficit per primitive register cell as cell=AIcell, with  
Icell=dvr=44=1,  cell=A=35437,  
where dv=4 is the **valence** of the Q=11 4-valent j=12 tetrahedron and r=4 is the ZS-F4 structural constant (both sector-independent; the symbol dv replaces the earlier clashing ). Hence **every primitive register cell carries the identical local deficit** A, independent of sector label X/Y. This is DERIVED-BY-INHERITANCE from ZS-M3 (inheriting its \[DERIVED\] status and primitive-cell scope). *(Verified: d\_v/r=1, δφ\_cell=A, sector-independent.)*

### **§6.2 Why local uniformity is insufficient \[the gap\]**

The Regge curvature *operator* is **not** the deficit alone. In Regge calculus,  
R=cc,wc,c,  
with hinge/dual-volume weights wc and cell-incidence projectors c. Uniform c=A gives R=Acwcc, which is IQ **only if additionally**  
wc=const and ccIQ.  
Because the X and Y polyhedral cells have **different incidence structure**, “same local deficit” and “same global matrix element” ⟨0|R|X⟩=⟨0|R|Y⟩ are **distinct claims**. M45’s §6.1 closes the first; the second does not follow.

### **§6.3 Graph-Laplacian coordinate diagnostic \[COMPUTED-DIAGNOSTIC; genuine gate OPEN\]**

The decidable form of the residual is an explicit finite computation: construct the sector cell–hinge incidence matrices BX,BZ,BY and the diagonal hinge-area / dual-volume weight matrices W; form the **register Regge Hessian** HRegge=BWhingeB; and, with isotypic projectors PX,PY1,PY2,P0, test hX=hY1=hY2 (diagonal) and cX=cY1=cY2 (coupling).  
**What is computed here (a diagnostic, not the gate).** On the actual corpus mediators — truncated octahedron (X, V=24, X=10/38=5/19) and truncated icosahedron (Y, V=60, Y=28/92=7/23) — the graph Laplacian L=D−A and the coordinate vectors give **coordinate Rayleigh quotients**  
hXcoord=xLXxxx=0.600,  hYcoord=0.244277.  
**Crucial honest caveat (third review).** The coordinate 3-spaces are **not** invariant eigenspaces of the graph Laplacian — the residuals are nonzero, |LXx−hXcoordx|/|x|=0.200 and |LYx−hYcoordx|/|x|=0.050 — so (6.5) are **Rayleigh quotients, not eigenvalues**, and (6.5) is **not** a BWhingeB computation. (For reference, the true lowest triple eigenvalues are X=2−2=0.5858 and Y=0.2434 — which also differ, so the diagnostic points the same way, but this remains a *graph-Laplacian* statement, not the register Regge Hessian.) Building the genuine gate requires the hinge/cell incidence, an adopted discrete Hodge-star / dual-volume convention, true isotypic projectors, repeated-irrep multiplicity resolution, off-block mixing, and the mediator coupling block — a separate computation, **not performed here**.  
**What the diagnostic does and does not show.** It is *diagnostic evidence* that the sector diagonals differ; it is **not** a proof that the physical register operator RIQ fails. The coupling democracy depends on the (undetermined) register measure. Two **benchmark** measures — not an exhaustive dichotomy — bracket the possibilities:

* **Mode-count (uniform-cell) benchmark** — the ZS-M3 Lemma 8.1 primitive cell is the uniform j=12 tetrahedron and both mediators are **valence-3** (equal per-vertex incidence): coupling **democratic**.

* **Metric (dual-volume) benchmark** — an (implementation-dependent) dual-volume weighting gives wX0.471, wY0.921, ratio 1.955: coupling **sector-weighted** 2\. *(No discrete Hodge-star / dual-cell normalization is derived for these numbers, so they are an implementation-dependent diagnostic, not a COMPUTED weight.)*

Other measures (Gibbs \=e−H/Z, sector-weighted traces, heat-kernel-regularized, modular/KMS weights) are equally admissible. So the honest statement is: **the register-scalar normalization has been narrowed to the action-level selection of a register measure**, with mode-count and metric as two explicit benchmarks. Under the mode-count measure — for which the a0 leading heat-trace coefficient (each mode counted once, independent of eigenvalue) is a genuine physical argument — Q=IQ/Q and 2=A/Q hold; but the measure is **not derived from the parent action**, so the gate is **OPEN**. The anti-numerology check confirms the 1.955 factor is a genuine geometric ratio, **not** a corpus constant (Y/X=1.156,  any clean A,Q combination — flagged, not claimed). *(Verified: zs\_m44\_regge\_verify.py 12/12 — valence-3 both, coordinate Rayleigh  eigenvalue (residuals* 0*), true triples* 2−2*/*0.2434*, dual-volume ratio* 1.955 *implementation-dependent, measures non-exhaustive.)*  
---

## **§7. R-3: rank-1 0-selection \[DERIVED-CONDITIONAL\]**

ZS-M6 §7A (Sector Separation Theorem) proves LXY0 to all orders in the continuum QFT (non-minimal coupling generates X–Z and Z–Y but no direct X–Y; anomaly-free Ward identity). With LXY=0 and 0 the unique Z-Spin mediator, Schur fixes the rank-1 0-selected structure — but only **provided** the intertwiner spaces HomGVX,VZ and HomGVZ,VY are each one-dimensional. That multiplicity has not been computed here; the Z2-odd mode being decoupled is supporting but not conclusive evidence. Status: **DERIVED-CONDITIONAL on Hom-multiplicity-one**. *(Verified: L\_XY=0 \+ Schur; Hom-mult-1 required, uncomputed.)*  
---

## **§8. Net status and hand-off to ZS-F36**

**Net epistemic status (the honest summary of this merged paper).**

| Claim | Status |
| ----- | ----- |
| a0=Q (mode count), a1=Tr,LQ | **PROVEN** |
| perturbative sector-asymmetry artifact removed (0.855​​X/Y is spurious) | **PROVEN** |
| within-irrep scalarity (R-2a) | **DERIVED** |
| primitive-cell deficit uniformity c=A (§6.1) | **DERIVED-BY-INHERITANCE** |
| coordinate Rayleigh diagnostic: sector coordinate-quotients differ (0.600 vs 0.244, §6.3) | **COMPUTED-DIAGNOSTIC** (not eigenvalues) |
| genuine register Regge Hessian BWhingeB | **OPEN** (not built: needs Hodge-star, isotypic projectors) |
| Q=IQ/Q / RIQ | **OPEN**, narrowed to action-level *register-measure selection*; a0 argues for mode-count |
| R-3 rank-1 0\-selection | **DERIVED-CONDITIONAL** (Hom-mult-1) |
| 2=A/Q | **DERIVED-CONDITIONAL** (register-trace normalization) |
| ZS-F36 Gs=1 | **DERIVED-CONDITIONAL** (register-trace normalization) |

**Honest net status (prose).** R-2(a) (within-irrep constancy) is DERIVED (Schur). The R-2 *perturbation-artifact correction* (§5.4) is the firm advance. R-1 and R-2(b) **merge** into the single conditional step — that A distributes via \=IQ/Q (register-trace normalization) — which is Schur-constrained within irreps but not derived across sectors from the action, and whose lattice realization (M45) is incomplete (§5.5). Therefore  
2=AQ=354807,  greg2=dimY2=6AQ=2104807 \[DERIVED-CONDITIONAL on register-trace normalization\],  
with the value fixed by the LOCKED ZS-F1 action, Q=11, and the polyhedra. ZS-F36 §6 uses greg2=6A/Q; accordingly Gs=1 **is DERIVED-CONDITIONAL on register-trace normalization** — the register-scalar density \=IQ/Q, whose action-level derivation remains OPEN; §6.3 provides only a graph-Laplacian diagnostic.  
**Honest scope.** This does not touch the ZS-F36 **metric-scale no-go**: MUV remains PROVEN-irreducible. R-1/R-2/R-3 concern only the *dimensionless* coupling 2; the scale MUV is orthogonal and unaffected. “Gs=1 DERIVED” therefore means the *normalization* is fixed, not that the physical odd-form stiffness is a pure number — it carries MUV dimensions set elsewhere.  
---

## **§9. Claim ledger**

| \# | Claim | Status | Conditions |
| ----- | ----- | ----- | ----- |
| §2 | a0=dim=Q (mode count); a1=Tr,LQ, coupling-immune | PROVEN | corrects v1.1 |
| T1 | 2=A⟨a|Q|a⟩=A/Q | DERIVED-CONDITIONAL | Q=IQ/Q |
| §4 | a2=92=315/4807 | PROVEN | forward from T1 |
| §5.2 | R-2(a) within-irrep constancy | DERIVED | Schur \+ Oh/Ih |
| §5.2 | cross-block equality cZ=cX=cY1=cY2 | OPEN | not a Schur consequence (review 4\) |
| §5.3/5.5 | R-2(b) cross-sector democratic (g2=32) | CONFIRMED-CONSISTENCY | not action-independent (review 1.3) |
| §5.4 | ZS-M6 §10.4 asymmetry \= 2nd-order artifact | PROVEN | exact vs perturbative |
| §6 | Regge-cell deficit uniformity c=A | DERIVED-BY-INHERITANCE | ZS-M3 (integrated M45) |
| §6.3 | global operator RIQ (Regge Hessian) | OPEN | X/Y incidences differ |
| §7 | R-3 rank-1 0\-selection | DERIVED-CONDITIONAL | §7A \+ Schur \+ **Hom-mult-1 uncomputed** |
| §7 | 2=A/Q, greg2=6A/Q | DERIVED-CONDITIONAL | register-trace normalization |
| §7 | ZS-F36 Gs=1 | DERIVED-CONDITIONAL | register-trace normalization |
| §5.5 | 50-digit recompute consistent with §2.3 | CONFIRMED-CONSISTENCY | inputs democratic ansatz |

---

## **§10. Falsification gates**

* **F-M44.1.** a10 (mode count not immune)  R-1 fails. *PASS.*

* **F-M44.2.** Exact arrowhead solve giving cX2/cY12 near X/Y=0.865 rather than 1  coupling sector-weighted, R-2(b) fails. *PASS (exact ratio* \=1.002*).*

* **F-M44.3.** If the 50-digit recompute (§5.5) gave g2/2 departing from 3  R-2(b) reopens. *PASS (recovered* 3 *to* 2.210−58*).*

* **F-M44.4.** ZS-M6 §7A not establishing LXY=0 to all orders  R-3 reopens. *PASS (inherited).*

* **F-M44.5.** A claim that the §10.4 numbers 2.61, prove sector-weighting is void: they are a perturbation artifact (§5.4).

---

## **§11. Anti-numerology**

Every number is either PROVEN, exactly computed, or explicitly flagged conditional: A=XY=35/437 (PROVEN), Q=11 (a0=dim, PROVEN), a2=9A/Q (exact), TrV2=18 (exact); 2=A/Q and g2=32 are **DERIVED-CONDITIONAL** on the register-trace normalization Q=IQ/Q. **Nothing is fitted.** Crucially, this paper *removes* a latent numerological trap: the §10.4 ratio 0.855X/Y is a perturbation artifact, not a geometric law — reading it as sector-weighting would have been the numerology. The exact solve discriminates democratic (1.002) from sector-weighted (0.865) cleanly. The 0.45% residual is stated as input-precision, not concealed.  
---

## **§12. Cross-version safety**

* A,Q,dimZ=35/437,11,2, 2=35/4807, greg2=210/4807: **unchanged** (only epistemic status improves).

* **ZS-M6:** no value modified. **§10.4 amended** (the firm result): the “\~15% asymmetry” is a 2nd-order perturbation artifact, not sector-weighting; the democratic g2=32 conclusion is *strengthened* at the consistency level. R-1/R-2 reduce to the single register-trace normalization (DERIVED-CONDITIONAL); R-3 DERIVED-CONDITIONAL on Hom-mult-1. **No caveat is claimed unconditionally closed.**

* **ZS-F1/F2/S1:** inherited inputs (register-scalar action; Gilkey product; Mode-Count Collapse); no status changed.

* **ZS-F36:** Gs=1 is **DERIVED-CONDITIONAL on register-trace normalization** (F36 v2.1 §6); metric-scale no-go untouched.

* **ZS-M45:** its content is now §6 of this paper; the standalone M45 v1.0–v1.1 are archived as internal companion drafts.

---

## **§13. Verification**

zs\_m44\_verify\_v1\_2.py (19/19) and zs\_review\_verify.py (14/14) PASS. The review suite verifies the corrections: a0=dim=Q while a1=Tr,L=13.30Q; Q normalization; \=IQ/Q asserted (not action-derived); a2=92 unaffected; the arrowhead/50-digit results are consistency-level; and the M45 operator-equality is OPEN. The §10.4 perturbation-artifact correction (democratic vs the 0.855 trap) is the firm, independently-checkable result.  
---

## **§14. Acknowledgements & Code Availability**

zs\_m44\_verify\_v1\_2.py (19/19), zs\_review\_verify.py (14/14), and zs\_m44\_regge\_verify.py (12/12, the §6.3 coordinate diagnostic) reproduce all checks. AI tools (Anthropic Claude) were used for verification and drafting; the author assumes full responsibility, including the honest §10.4 amendment and the explicit §5.5 residual (rather than an over-claimed unconditional closure).  
---

## **§15. Appendix A — Deep-exploration (issue-tree) record**

**Step 0 (long list, 7).** (1) does R-2 split into within-irrep and cross-sector parts? (2) does Schur \+ polyhedral symmetry close within-irrep? (3) is cross-sector democratic or sector-weighted? (4) can exact diagonalization decide it, avoiding perturbation error? (5) what is the ZS-M6 §10.4 asymmetry, really? (6) does R-2(b) follow from R-1’s mode count? (7) any residual after closure?  
**Step 1 (MECE).** I1 R-2(a) within-irrep {(1),(2)}. I2 R-2(b) cross-sector {(3),(4),(6)}. I3 the §10.4 diagnosis \+ residual {(5),(7)}.  
**Step 2–3 (tree \+ status).** I1 → I2 → I3. I1 **DERIVED** (Schur on dim-3 irreps). I2 **CONFIRMED democratic** by exact arrowhead solve (0.45%, excludes 0.865); note R-1 gives only the *average*, so the exact per-sector solve is load-bearing, not decorative. I3: the §10.4 asymmetry is a **2nd-order perturbation artifact** mimicking X/Y — corrected; the verification residual is then **eliminated** by the v1.2 50-digit recompute (democratic reproduces §2.3, inverts to 3 at \<10−45), leaving only the narrow lattice-R completion.  
**Step 4 (convergence).** Re-traversal change counts 5,1,0 decreasing  converged. The node that flipped on re-traversal was I2: the *first* pass (2nd-order perturbation, as in the prior exploration) suggested sector-weighting (ratio 0.855); the exact arrowhead solve on re-traversal corrected this to democratic (1.002). This flip is the paper’s central lesson — the discriminator must be exact, not perturbative.  
**Step 5 (value).** The firm advance is the §10.4 perturbation-artifact correction (R-2(a) DERIVED; the 0.855​​X/Y trap defused). R-1 and R-2(b) merge into the single **register-trace normalization** step (=IQ/Q), which is DERIVED-CONDITIONAL — Schur-constrained within irreps, but not action-derived across sectors, and with an incomplete lattice realization (M45, review 1.4). Honest terminus: 2=A/Q **DERIVED-CONDITIONAL**, not fully discharged — the a0/a1 correction and the consistency-vs-independence distinction (review 1.2–1.4) are integrated.  
---

## **§16. References**

*(ZS-M45 v1.1 is integrated into §6 of this paper; the standalone drafts are archived as internal companion notes.)*

1. P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*, 2nd ed., CRC Press (1995).  
2. D. V. Vassilevich, *Heat kernel expansion: user’s manual*, Phys. Rept. **388** (2003) 279, arXiv:hep-th/0306138.  
3. J.-P. Serre, *Linear Representations of Finite Groups*, GTM **42**, Springer (1977). \[Schur\]  
4. G. H. Golub, *Some modified matrix eigenvalue problems*, SIAM Review **15** (1973) 318\. \[arrowhead inverse-eigenvalue\]  
5. ZS-F1, *The Non-Minimal Coupling* 1+A||2R (Z-Spin corpus).  
6. ZS-F2, *Product Structure* A=XY*; Adjoint Obstruction* (Z-Spin corpus).  
7. ZS-M2, su2X,su2Y=0 *Sector Independence* (Z-Spin corpus).  
8. ZS-M6, *Block-Laplacian; Register-Total Normalization; Dimensional Coupling Norm; §7A Sector Separation* (Z-Spin corpus).  
9. ZS-F36 v2.1, *Integral UV Normalization of the Z-Spin Odd Three-Form* (Z-Spin corpus).

---

## **§17. Version History**

* **Version:** v1.6 (July 2026, finalized for public release — supersedes v1.5–v1.0; no research change). Editorial finalization only: confirms the three proofread items (ledger **T1** status/condition filled — 2=A⟨a|Q|a⟩=A/Q DERIVED-CONDITIONAL, Q=IQ/Q; the §8 wording *“whose action-level derivation remains OPEN; §6.3 provides only a graph-Laplacian diagnostic”*; §6.3 \= COMPUTED-DIAGNOSTIC), unifies the mediator terminology to **Z-Spin mediator** (0; the actor of mediation is the Spin), and updates the ZS-F36 cross-reference **v2.0 → v2.1**. 19/19 \+ 14/14 \+ 12/12 PASS; no numerical value changed; A,Q,dimZ=35/437,11,2 LOCKED.

* **v1.5** (supersedes v1.4–v1.0; **integrates ZS-M45 v1.1 as §6**; **§6.3 correctly reclassified** as a graph-Laplacian *coordinate diagnostic*, not a Regge-Hessian theorem) — the two papers address one problem: M45 is the geometric lemma for M44’s final normalization step, so they are merged). Second external review integrated (body synchronized to the conditional conclusions). **v1.5 corrects a v1.4 over-claim (third review):** the hX=0.600, hY=0.244 values are graph-Laplacian **coordinate Rayleigh quotients**, *not* Regge-Hessian eigenvalues (the coordinate 3-space is not Laplacian-invariant: residuals 0.200, 0.0500; the true lowest triples are 2−2=0.5858 and 0.2434). So §6.3 is a **COMPUTED-DIAGNOSTIC**, not a theorem: it gives *diagnostic evidence* that the sector diagonals differ, but the genuine register Regge-Hessian BWhingeB (hinge incidence \+ discrete Hodge-star \+ isotypic projectors) is **not** built here and remains **OPEN**. The residual is *narrowed* to the action-level selection of a register measure (mode-count and metric being two benchmark choices, not an exhaustive dichotomy). **This version corrects two over-claims of the earlier drafts:** (i) the finite-matrix heat trace has a0=dim=Q as the *leading rank coefficient / mode count* — **not** a1 (which is Tr,LQ); the “/Q” is the **normalized trace** Q=Q−1Tr, and the maximally-mixed density \=IQ/Q is *asserted*, not derived from the action; (ii) the arrowhead inversion and 50-digit recompute are **consistency checks**, not a fully action-independent forward derivation. Consequently 2=A/Q is **DERIVED-CONDITIONAL on register-trace normalization**, and the genuine result is: *R-2 perturbative ambiguity corrected; normalized-trace bridge remains conditional.* v1.0 closed **R-1**; v1.1 closed **R-2** (Schur within-irrep \+ exact arrowhead democratic, 0.45% input-limited). **v1.2 eliminates the §5.5 residual**: a **50-digit physical-action recompute** builds L from the independently-derived ingredients (polyhedra eigenvalues, 2=A/Q from §3, democratic g2=32 from §5.2 — none from the spectrum), reproduces the ZS-M6 §2.3 spectrum exactly, and inverts to democratic to \<10−45, proving the v1.1 “0.45% spread” was **purely §2.3’s 4-decimal rounding**.

* **v1.5 (July 2026, current — §6.3 reclassified):** Third review correctly caught that the v1.4 values hX=0.600, hY=0.244 are graph-Laplacian **coordinate Rayleigh quotients**, not Regge-Hessian eigenvalues (coordinate 3-spaces are not Laplacian-invariant; residuals 0.200, 0.0500; true triples 2−2, 0.2434). §6.3 is downgraded from a “Regge-Hessian computation” to a **COMPUTED-DIAGNOSTIC**; the genuine BWhingeB gate (hinge incidence, discrete Hodge-star, isotypic projectors) remains **OPEN**. “Mode-count vs metric” is reframed as **two benchmark measures, not an exhaustive dichotomy** (Gibbs/KMS/heat-kernel also admissible); the dual-volume numbers are flagged implementation-dependent (no Hodge-star convention derived). Also: R-3 stated DERIVED-CONDITIONAL in the abstract (consistent with §7); intro “v1.2 (this version)” fixed; ledger T1 cells filled; verification suite mention (12/12) added; reference 9 → F36 v2.0. 12/12 diagnostic checks; no numerical value changes; A,Q,dimZ=35/437,11,2 LOCKED.

* **v1.4 (July 2026 — executed §6.3, later reclassified in v1.5):** Performs the Regge-Hessian computation on the actual corpus polyhedra (truncated octahedron X, V=24; truncated icosahedron Y, V=60). Reported the coordinate quotients hX=0.600, hY=0.244 as “provably unequal diagonal block weights” **— corrected in v1.5** (these are Rayleigh quotients, not eigenvalues) and Q=IQ/Q can only be the **mode-count measure**. The coupling democracy is thereby **localized** to one decidable choice — mode-count (uniform-cell, both valence-3  democratic) vs metric (dual-volume ratio 1.955 sector-weighted); the a0 leading heat-trace coefficient argues for mode-count but does not derive it. Gate **not closed**, but sharply localized. 10/10 new checks; anti-numerology confirms 1.955 is a geometric ratio, not a corpus constant. No numerical value changes; A,Q,dimZ=35/437,11,2 LOCKED.

* **v1.3 (July 2026 — integrates ZS-M45 v1.1):** Merges the ZS-M45 Regge-cell lemma as §6 and fully synchronizes the body with the conditional conclusions (removes all residual v1.0/v1.1 closure language). Title dropped “Closing.” Corrects the 2=A/Q notation slip to 2=A⟨a|Q|a⟩=A/Q (the normalized trace Q is a functional, not a divisor). Adds the crucial limitation that OhIh Schur equivariance forces only *block* scalarity (cZ,cX,cY1,cY2), **not** their equality — so Q=IQ/Q is OPEN at the action level. Re-scopes R-3 to DERIVED-CONDITIONAL on Hom-multiplicity-one. Reframes the finite-matrix Taylor coefficients as *finite-register heat-trace moments* (the discrete counterpart of continuum heat-kernel coefficients), not literal Seeley–DeWitt invariants. Adds the net-epistemic-status table (§8) and the explicit Regge-Hessian test (§6.3). 19/19 \+ 14/14 checks; A,Q,dimZ=35/437,11,2 LOCKED.

* **v1.2 (July 2026):** Corrected the a0/a1 conflation (mode count is a0=dim=Q, not a1=Tr,L=13.30); re-scoped M44.T1 to DERIVED-CONDITIONAL (Q=IQ/Q asserted, not action-derived); flagged the arrowhead inversion and 50-digit recompute as consistency checks; the firm result is the §5.4 perturbation-artifact correction. *(Internal pre-review drafts also numbered v1.2/v1.3 — which over-claimed the ZS-M45 lattice-*R *as closing the register-scalar operator — are superseded and archived as internal drafts.)*

* **v1.1 (July 2026):** Split R-2 into within-irrep (Schur) and cross-sector (arrowhead) parts; corrected the ZS-M6 §10.4 perturbation artifact. *(Erroneously called the “*/Q*” the “*a1 *mode count” — corrected in v1.2.)*

* **v1.0 (July 2026):** Introduced the Register-Trace Normalization Theorem; reduced the residual to R-2; derived R-3 from §7A. 13/13 checks.