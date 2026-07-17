# **ZS-F36**

**The Integral UV Normalization of the Z-Spin Odd Three-Form: Exact Meff Reduction, Wrapped-Brane Charge Pairing on the Koenigs Torus, and the Metric-Scale Gate**

**Author:** Kenny Kang  
**Date:** July 2026  
**Theme / Code:** Foundations / ZS-F36 · Companion to ZS-F33 / ZS-F34 / ZS-F35 · Register normalization from ZS-M6 · Cosmological hand-off ZS-A31

**Verification:** 56/56 (zs\_f36\_verify\_v2\_1.py) \+ 14/14 (zs\_f36\_review\_verify.py) PASS | **Zero fitted parameters** | primitive charge \=1 and dimensionless WZ phase 2 **PROVEN** (Smith form); dimensionful ce=2 **DERIVED-CONDITIONAL** on UV=1; Gs=1 **DERIVED-CONDITIONAL** on register-trace normalization (ZS-M6/M44 v1.2); Cnorm=1 **DBI** at register tree level, **OPEN** at full parent 1PI; MUV **PROVEN-irreducible** | (**A**, **Q**, dim **Z**) \= (**35/437**, **11**, **2**) **LOCKED**.

---

## **§0. Abstract**

ZS-F35 reduced the Z-Spin odd-sector vacuum susceptibility to −s=dimY2,A/Q,Cnorm,MUV4=1260/4807,Cnorm,MUV4, Cnorm=Gs−1ce/22, and left a dimensionless gate (Gs=1 ASSUMPTION, ce=2 HYPOTHESIS-strong) and one dimensionful scale MUV. Following the principle that only the field-redefinition invariant es2/Zsphys is physical, this paper **organizes their normalization, topological quantization, and residual obstruction within a common parent-action template** — the honest current state is a *template*, not a completed parent-action computation (Gs conditional on register-trace normalization, ce on UV=1, CUV OPEN at full 1PI, MK an independent scale).

**(NG1) \[PROVEN\]** Under A3A3: ZsZs/2, eses/; the invariant is es2/Zs, and Cnorm is invariant, so Gs=1 and ce=2 are **not independent** — two projections of one convention.

**(T1) \[PROVEN\]** On Y6=M42: Zsphys=K/g62; for the unit-period form K=A−1 (**inverse** area — correcting the V symbol). Gs=1g62=greg2K.

**(Cycle \+ T2/T3) \[PROVEN / DERIVED-CONDITIONAL\]** The internal cycle is the **corpus-forced Koenigs torus** 2=E\* (F34: the canonical rank-one homology generator, b2=1; unique up to homology). E\*=T2 is parallelizable, so w1=w2=0 (spin), W3=0 (Freed–Witten), Tor,H•=0, p1T2=0: **no *intrinsic* shift from the internal tangent bundle**. The full flux-quantization shift is **DERIVED-CONDITIONAL** on the vanishing of the relevant *ambient* shifted classes (gravY6|W5=0, H|W5=0, W3NW5=0), which the internal p1T2=0 does not by itself establish. The wrapped-brane charge pairing has Smith normal form 1 (primitive), so the minimal charge is one unit and the *dimensionless* WZ phase is exactly 2 (**PROVEN**). The *dimensionful* ce=2 then holds **iff** UV=1 (review 1.5); since UV=1 is not separately derived from the action, ce=2 is **DERIVED-CONDITIONAL**.

**(T4) \[T4a PROVEN / T4b–T4c DERIVED-CONDITIONAL\]** Full-flux partition matching splits into: **T4a** theta-series rigidity — *if* ZEFT=Zreg then Zsphys=1/greg2 (PROVEN, Fourier rigidity); **T4b** whether the register action *generates* that theta series (DERIVED-CONDITIONAL on register-trace normalization); **T4c** Gs=1 (DERIVED-CONDITIONAL). The **algebraic back-definition is avoided** (greg2=6A/Q is upstream ZS-M6, not back-defined), **but the register-trace bridge remains conditional** — per ZS-M44 v1.5, Q=IQ/Q is asserted, not action-derived (§6).

**(T5) \[DBI at tree level / OPEN at full 1PI\]** Threshold audit Zsphys=Ztree+bulk+brane+ct: at the **register tree level**, bulk=0 (the Z2-odd slot is decoupled, ZS-M6 §10.3) and the register branch is DBI. **But (review 1.6) the full parent 1PI is OPEN:** F4F4 is gauge-invariant and seam-even, so gauge invariance \+ seam parity do **not** forbid the ct counterterm, and the absence of a propagating 4D 3-form mode does not prevent heavy parent fields from renormalizing the F42 coefficient. So: register tree branch DBI; full parent 1PI **OPEN**; instanton residual brane=Oe−Sinst **HYPOTHESIS/EXPECTED**.

**(Collapse) \[DERIVED, with caveat\]** −s=g2; adopting Cnorm=1 is the *definition* MUV4 := 4807/1260g2 (a canonical reparameterization, review 1.7), so −s=1260/4807Meff4 with Meff := CUV1/4MK is an **IDENTITY / canonical reparameterization** (not a DERIVED prediction); CUV (true 1PI matching) and MK (metric scale) remain the physical content.

**(T6/T7) \[PROVEN\]** The Koenigs *shape* (modulus \=+i/2) is M1-fixed, but the physical area A=ℓ2,Im, needs the linearizing length ℓ=MUV−1; radion stabilization (Veff=cflux/a+cbranea, minimum a\*=cflux/cbrane) relocates MUV onto the parent scale M\*. By Buckingham-π no dimensionless datum fixes a scale — the F-sector instance of the ZS-A27 A–Q-Only No-Go, consistent with ZS-A28 / ZS-F33.

**Result (honest terminus).** −s=12604807,CUV,MK4 where 1260/4807=dimY2A/Q is the **register structural factor** (DERIVED-CONDITIONAL on register-trace normalization, ZS-M44 v1.5); the primitive-charge lattice and Koenigs complex structure are **closed**; CUV is **conditional on full parent 1PI matching** (OPEN, review 1.6); MK is the **independent Kähler/metric scale**; and MK/MP is a **genuine OPEN** (the metric-scale gate). Setting CUV=1 and MK=MUV recovers the canonical form. **ZS-A31** consolidates the scale: ,Z/Meff4=121260/48072 (a definitional identity, since Meff := CUV1/4MK), regression fixing Meff2.48 meV; the hierarchy MK/M‾P=?e−2Q is OPEN (the 2 Borchers–Wiesbrock-forced modular-depth frontier, ZS-M46/M47). Verification 56/56 \+ 14/14 PASS.

---

## **Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| **PROVEN** | Explicit proof or exact machine verification; no undischarged assumption. |
| **IMPORTED-PROVEN** | Proven in external literature and used without re-proof; cited. |
| **DERIVED** | Follows from PROVEN results by stated steps; no new parameter. |
| **DERIVED-BY-INHERITANCE** | Uses an upstream corpus result (here ZS-M6), not re-proven; inherits its caveats. |
| **DERIVED-CONDITIONAL** | Derived modulo explicitly named, falsifiable conditions. |
| **COMPUTED** | A finite decidable computation carried out; result reported as-is. |
| **HYPOTHESIS-strong** | Structurally motivated; a key value not yet proven. |
| **NO-GO** | A proven impossibility/non-uniqueness disciplining the program. |
| **PROVEN-irreducible** | Proven that the quantity cannot be fixed by the stated inputs. |
| **CLOSED-NEGATIVE** | A route proven not to work (a no-go), possibly scope-limited. |
| **IDENTITY / REGRESSION** | An arithmetic or cross-version consistency; no new physical content. |
| **NON-CLAIM** | Explicitly outside the scope of this paper. |
| **OPEN** | Conceptually unresolved; a genuine gap. |

---

## **§1. Introduction: the inherited ZS-F35 frontier and the parent-action mandate**

ZS-F33 gave ,Z=12−2 and the **Charge-Unit Obstruction** (−=e−2/42Z−, unit not fixed by flux integrality). ZS-F34 isolated the unit under Y6=M42 and identified the rank-one homology generator as the **Koenigs torus** E\* (dim Z=2, b2=1, unique up to homology; F33.2B PROVEN). ZS-F35 collapsed the normalizations into Gs (Zsphys=Gs/greg2), proved c=, s2=6=dimY, and reached

−s=dimY2,AQ,Cnorm,MUV4=12604807,Cnorm,MUV4, Cnorm=Gs−1ce/22.

**Mandate (F36).** Do not declare Gs=1, ce=2, MUV separately; by NG1 only es2/Zsphys is physical. Organize it within a common parent-action template, on the corpus-forced cycle, with every normalization traced to an upstream corpus result, flagged conditional, or proven irreducible. v1.2 completes this: the cycle is E\* (not a free ansatz); the charge and anomaly structure are *computed* on it; the register normalization is *inherited* from ZS-M6; and the residual scale is proven irreducible and localized to the loxodromic linearizing length.

Locked data: A=35/437, Q=11, Z,X,Y=2,3,6, 2=A/Q=35/4807, greg2=dimY2=210/4807, \=2.2592495540, \=−ln|\*|=0.1148346250, z\*=0.43828+0.36059,i.

---

## **§2. The Normalization-Covariance Theorem (F36.NG1)**

S4=−Zs2M4F4F4+esW3A3,  F4=dA3.

**Theorem F36.NG1. \[PROVEN\]** *Under* A3A3*:* ZsZs/2*,* eses/*;* es2/Zs *is invariant,* −s=es2/42Zsphys *is the unique odd-sector field-redefinition invariant, and* Cnorm=Gs−1ce/22 *is invariant.*

*Proof.* Substituting A3=A3′/ gives the transformations; then es′2/Zs′=es2/Zs, and with Gs=Zsphysgreg2, ce=es/sMUV2, Cnorm=−s/greg2s2MUV4. ;

Exhibiting Gs=1 and ce=2 separately does *not* exclude a compensating field redefinition; the only meaningful target is Cnorm, computed in one fixed normalization (§§3–7). The split of CnormMUV4 into “Cnorm” and “MUV” is a convention (the seed of §8). *(Verified: T1 e\_s²/Z\_s invariant, T1 C\_norm field-redef invariant.)*

---

## **§3. The compact parent action and the exact reduction (F36.T1)**

Y6=M42, C5=A3−2, G6=dC5=F4−2, 22=1,

S6=−12g62Y6G66G6;+;2iN​W5Č5;+;Smetric+Sstab+Sct,

Č5 a differential-cohomology character \[Hopkins–Singer\], W5=W32. **Scope caveat (ZS-F33):** the “6” is a rank-2 internal fibre over the 4D base, not fundamental 6D spacetime.

**Theorem F36.T1 (Exact reduction). \[PROVEN\]** *For the product metric,* 6F42=4F422*, the integral factorizes, and*

Zsphys=Kg62, K := 2222=A−1 inverse area, Gs=1g62=greg2K.

With 2=vol/A one keeps A=∫vol2 (area), ∫2=1 (period), K=A−1 (kinetic factor) **distinct**; the ZS-F33/F34 V is K=A−1, an *inverse* area — conflation would invert the MUV power. *(Verified on* SR2*; the same identity holds on any connected oriented* 2*, in particular* E\**: T2a, T2b, T2b’.)*

---

## **§4. Wrapped-brane charge and the 2 (F36.T2)**

exp​2iN​W5Č5, Č5=Ǎ3̌2, 2̌2=1;;2iN​W3Ǎ3.

The minimal charge coefficient of the dimensionless integral field is 2 (large-gauge / generalized Dirac). Writing A3=UVMUV2a3: e6=2/UVMUV2, so

,ce=2UV=1,,

the **same** normalization as Gs=1. That the minimal charge is exactly one unit (hence coefficient 2, not a fraction) is *proven* by the charge pairing of §5. *(Verified: T2-NS c\_e=2π ⟺ α\_UV=1.)*

---

## **§5. The Koenigs cycle 2=E\*: charge pairing and anomaly gates (F36.T3)**

The internal cycle is not a free choice: ZS-F34 proves the rank-one generator of H2 carrying the bivector 2-form is the Z-sector **Koenigs torus** E\*=C\*/⟨\*⟩ (dim Z=2, b2=1; F33.2B). We compute the charge and anomaly structure on it. As a smooth manifold E\*=T2, which is **parallelizable**.

**Charge pairing (Smith normal form). \[PROVEN\]** The cellular chain complex of T2 (one vertex, two edges, one face, all boundary maps zero) gives Betti 1,2,1, torsion-free, with H2T2,Z=Z=⟨2⟩. The wrapped-brane flux pairing ⟨2,2⟩=22=1 has Smith normal form 1 — **primitive** — so the minimal wrapped charge is qmin=1 (**PROVEN**) and the *dimensionless* WZ phase SWZ=2i∫Ǎ3 is exactly 2 (**PROVEN in integral normalization**). The *dimensionful* ce=2 then holds **iff** UV=1 — **DERIVED-CONDITIONAL** (review error 3). The H1 intersection form is the unimodular symplectic 0 1 −1 0  (self-dual lattice). *(Verified: M2a–M2e.)*

**Anomaly gates. \[DERIVED-CONDITIONAL on ambient and normal-bundle classes\].** Because T2 is parallelizable, wTT2=1, so:

* **A1 (bulk shift):** p1T2=0 (flat) removes the *intrinsic* internal-tangent contribution only; full unshifted flux quantization additionally requires the ambient class gravY6|W5=0, on which flux 2Z. *(Verified: M3e.)*

* **A2 (Freed–Witten):** w2=0 (spin) W3=w2=0; with trivial normal bundle and no worldvolume H-flux, W3normal+H|W5=0 — anomaly-free, no worldvolume gauge field forced. *(Verified: M3a–M3c.)*

* **A3 (torsion):** Tor,H•T2,Z=0  trivial linking pairing, no charge shift. *(Verified: M3d.)*

**Upgrade over v1.1.** In v1.1 these gates were conditional on a *free* S2 ansatz. Now 2=E\* is corpus-forced and the classes are computed exactly on it; the only residual conditions are the *ambient* and *normal-bundle* shifted classes (gravY6|W5=0, H|W5=0, W3NW5=0) — genuine physical conditions on the brane embedding, not an ansatz choice; the internal p1T2=0 discharges only the intrinsic internal-tangent piece.

---

## **§6. Gs=1 by full-flux partition matching: theta-rigidity PROVEN, physical matching conditional (F36.T4)**

On compact Euclidean M4 (M4F4=2n), Sn=22Zsphysn2/V4, so

ZEFT=ne−22Zsphysn2/V4+in,  Zreg=ne−22n2/greg2V4+in.

**Theorem F36.T4 (split into three honest tiers).**

* **T4a (theta-series rigidity) \[PROVEN\].** *If the two theta series are equal,* ZEFT=Zreg *for all* n,,V4*, then* Zsphys=1/greg2*.* This is pure Fourier rigidity (below).

* **T4b (physical partition matching) \[DERIVED-CONDITIONAL\].** *Does the register action actually generate the EFT theta series?* This is the register-trace normalization bridge — conditional on Q=IQ/Q (ZS-M44 v1.3 §3/§6).

* **T4c (normalization) \[DERIVED-CONDITIONAL\].** Gs=1, conditional on T4b and register-trace normalization.\*

*Proof.* (T4a only.) Both are theta series ne−an2+in; the \-Fourier coefficient at mode n is e−an2, so equality for all  needs a=b already at n=1 — **no rescaling freedom**. This rigidity is PROVEN. Whether the register action *produces* this series (T4b) rests on the register-trace normalization, so Gs=1 (T4c) is **DERIVED-CONDITIONAL**. ;▫ *(Verified: T4a–T4d.)*

**Algebraic back-definition avoided; register-trace bridge conditional.** The matching avoids circular back-definition only if greg2 is an *independent* upstream quantity. It is: **ZS-M6 Theorem 2.2.1 (Register-Total Normalization)** derives 2=A/Q from the 10-step chain C1–C10 (non-minimal coupling, Regge discretization, Mode-Count Collapse, Gilkey heat kernel, spectral asymmetry, Peter–Weyl/Schur), and **ZS-M6 Theorem 2.2.2 (Dimensional Coupling Norm)** gives g2=dim2, whence

greg2=dimY2=6,AQ=2104807,  1greg2=4807210.

This is a *projection* from the register Block-Laplacian, provenance {Peter–Weyl, Schur, rank-1 0-selection} — independent of the F35 target. **Status after review (ZS-M44 v1.5, integrating M45):** the firm advance is the R-2 perturbation-artifact correction (the 0.855​​X/Y trap defused; democratic within irreps via Schur). **But the register-scalar normalization is not fully discharged:** (a) the “/Q” is the normalized-trace rank a0=dim=Q — *not* a1=Tr,L (the earlier “a1 mode count” was an error); (b) the maximally-mixed density \=IQ/Q underlying the democratic distribution is *asserted*, not action-derived; (c) ZS-M44 v1.5 §6.3 provides a graph-Laplacian **coordinate diagnostic** (Rayleigh quotients 0.600 vs 0.244; these are *not* eigenvalues, and *not* the genuine BWhingeB Regge Hessian, which remains OPEN) — evidence the sector diagonals differ, narrowing the residual to the action-level selection of a register measure (a0 mode-count vs metric being two benchmarks). Hence Gs=1 is **DERIVED-CONDITIONAL on register-trace normalization**. This still upgrades ZS-F35’s S3 from ASSUMPTION, and is **scale-free** (MUV never appears). *(Verified: M1a–M1d; ZS-M44 v1.5 19/19 \+ 14/14 \+ 12/12.)*

---

## **§7. The 1PI threshold audit, with bulk-vanishing grounded in ZS-M6 (F36.T5)**

Zsphys=K/g62⏟Ztree+bulk+brane+ct.

**Theorem F36.T5. \[register tree DBI / full 1PI OPEN\]**

* ct=0 **\[DERIVED-CONDITIONAL, review 1.6\].** At the register tree level the 4D 3-form has no local propagating bulk degree (F4=f, f constant). **However, this does not close the full 1PI:** F4F4 is gauge-invariant and seam-even, so gauge invariance \+ seam parity alone do **not** forbid a ct counterterm, and heavy parent fields may renormalize the F42 coefficient even absent a propagating 3-form. So ct=0 holds for the register tree branch (DBI); the full parent 1PI is **OPEN**.

* bulk=0 **\[DERIVED-BY-INHERITANCE\].** In the ZS-M6 register Block-Laplacian, the Z2-**odd** mode (slot 1 — the odd singlet) has eigenvalue shift \=0 under the rank-1 0-selected cross-coupling: it is **completely decoupled** (ZS-M6 §10.3, hand-proven; matches the ZS-S1 §5.2 Z2-projection). This is the register shadow of the parent statement that no charged mode couples locally to the odd singlet at p=0; the full parent statement carries a residual DERIVED-CONDITIONAL on the (unspecified) heavy odd content. *(Verified: M6a, M6b.)*

* brane=Oe−Sinst **\[HYPOTHESIS/EXPECTED\].** Membrane-nucleation corrections e−TmemA are *expected* to be exponentially small, but the instanton solution and its fluctuation determinant are **not computed** here — so this is EXPECTED, not COMPUTED.

Under the canonical branch (ZS-F33.6, b2n=0), the **register tree branch** gives Zsphys=Ztree and

Cnormreg,tree=1 \[DBI\],  CUV1PI=1+bulk+ct+brane \[OPEN\].

So Cnorm=1 holds **only for the register tree branch (DBI)**; the **full parent 1PI** CUV **is OPEN** (ct not forbidden, brane EXPECTED not computed). Any gate failure would be reported as a *computed* CUV1 — which would be a *more* valuable result than matching 1 (review §2.3). *(Verified: T5a, T5b, T5c.)*

---

## **§8. The residual collapse: −s=g2**

With Gs=1 (§6) and ce=2 (§4–5) in one normalization, write A3=c,a3 (a3 the integral field, coupling g2): Zsphysc2=1/g2, esc=2, so

−s=es242Zsphys=2/c2421/g2c2=g2,

the conversion c (hence Gs, ce separately) cancels. Cross-check with (1.1): −s=s2greg2CnormMUV4=g2. Defining the **effective scale** Meff := CUV1/4MK gives the canonical *reparameterization* Meff4 := 4807/1260g2 — the definition of Meff does **not** require adopting CUV=1. **The convention-dependent split (**Gs**,** ce**) collapses to the invariant** g2**, but the physical parameterization retains two residuals:** CUV **(OPEN, full 1PI) and** MK **(independent scale).** *(Verified: RC chi=g̃², RC C\_norm c-independent.)* **\[DERIVED as a reparameterization identity; the physical content** CUV,MK **is OPEN.\]**

---

## **§9. The Koenigs modulus, radion stabilization, and the sharpened scale gate (F36.T6)**

**Shape is fixed by M1; scale is not. \[PROVEN\]** The Koenigs torus E\*=C/2iZ+log\*Z has modulus

\=log\*2i=+i2,  Im,=2\>0,

fixed by the loxodromic multiplier \*=f′z\* of ZS-M1 (|\*|=0.89151, \=0.11483, \=2.2592). Thus the **shape** and the **dimensionless** fundamental-domain area are M1-determined. But the **physical** area is A=ℓ2,Im,, where ℓ is the physical size of the loxodromic linearizing coordinate — an undetermined length, ℓ=MUV−1. Topology \+ M1 fix everything *except* ℓ. *(Verified: M4a–M4d.)*

**Theorem F36.T6 (Radion relocation). \[DERIVED-CONDITIONAL\]** *On* T2 *the curvature term vanishes by Gauss–Bonnet (*\=0*), so stabilization is flux-versus-tension:*

Veffa=cfluxa+cbrane,a,  a\*=cflux/cbrane,  Veff″a\*\>0

*(a genuine minimum, no tachyonic radion). But* cfluxg6−2n2 *and* cbraneT4 *are parent scales, so* MUV=M\*,hcouplings*: stabilization relocates the scale onto* M\**, it does not create one.* *(Verified: M5a–M5d.)* If T4/M\* is external, MUV is DERIVED-CONDITIONAL, never DERIVED-from-A,Q.

---

## **§10. The F-sector Scale No-Go, final susceptibility, and firewall (F36.T7)**

**Theorem F36.T7 (F-sector Scale No-Go). \[PROVEN\]** g2=−s *(equivalently* MUV*) is not a function of the locked dimensionless data* A,Q,dimZ,s2,,,z\*, *\+ flux integrality \+ differential-cohomology normalization alone.*

*Proof.* By NG1 the physical content is the invariant −s of dimension mass4; by T1–T5 every dimensionless input is a pure number and the topology contributes only integers and 2\. Buckingham-π forbids a dimensionful function of dimensionless inputs. The §9 Koenigs analysis exhibits the missing datum **concretely**: the physical size ℓ of the loxodromic linearizing coordinate — invisible to cohomology (which fixes b2=1) and to M1 (which fixes the shape ). ; *(Verified: M4d, M5c, M5d.)*

This is the odd-three-form realization of the **ZS-A27 A–Q-Only Scale-Generation No-Go**, consistent with **ZS-A28** (internal scale generation closed-negative) and **ZS-F33** (Charge-Unit Obstruction), and *strengthens* F33: the full differential-cohomology parent normalization \+ partition matching \+ threshold audit \+ Koenigs modulus still cannot fix the scale.

**Routes to** f=MUV/M‾P **(non-exhaustive, ZS-A27 §7).** With the one anchor M‾P: **(i)** target-fit exponent — NUMEROLOGY, barred; **(ii)** transmutation −=M‾Pe−82/b0g−2, b0=113C2G−−23fTRf−16sTRs — LEGITIMATE only if G− and g−20=greg2 are corpus-forced; ZS-F33 leaves G− unspecified  **CLOSED-NEGATIVE-within-corpus**; **(iii)** 3H — dynamical DE (w−1), contradicting ZS-F33.7/A28  **NON-CLAIM**. Within the corpus, MUV is **PROVEN-irreducible**.

**Final susceptibility — physical general form and canonical reparameterization (IDENTITY):**

;−s=12604807,CUV,MK4; (physical general form; CUV OPEN at full 1PI, MK independent Kähler scale),

Meff := CUV1/4MK,  −s=12604807,Meff40.2621,Meff4⏟IDENTITY / canonical reparameterization — not a DERIVED prediction,  ,Z=12−s2.

The second line is a **definitional identity**, not an extra prediction; calling Meff “MUV” is permitted, but then the ZS-A31 one-parameter reduction is an *effective parameterization*, not a physical closure.

w=−1 is **DERIVED-BY-INHERITANCE within the frozen/canonical branch** (ZS-F33.7/A28) — not an observationally proven theorem. The frozen branch remains observationally viable, although **DESI DR2 combinations show dataset-dependent preferences for evolving dark energy** relative to flat CDM (BAO+CMB 3.1; adding SNe 2.8–4.2 depending on the sample), so this is a genuine falsification channel, not merely “not excluded.”

**Anti-numerology firewall.** Code split derivation/{parent\_action, charge\_pairing, stiffness, partition\_match, threshold, stabilization} **⟂** regression/{observed\_rho\_lambda}; loading observation before derivation fails the gate (M7a, M7b). Post-firewall, matching (10.1) to the inferred dark-energy density 1/42.3 meV fixes Meff2.5 meV — a **REGRESSION on one input, not a prediction**. The length ℓ=MK−180,m follows **only** on the canonical register-tree branch CUV=1 (there MK=Meff), and MK/M‾P10−30 is then the metric-scale gate. Cosmological consolidation → **ZS-A31**.

---

## **§11. Claim ledger**

| \# | Claim | Status | Confidence | Conditions |
| ----- | ----- | ----- | ----- | ----- |
| NG1 | es2/Zs, Cnorm field-redef invariant; Gs,ce one convention | PROVEN | — | none |
| T1 | Zsphys=K/g62; K=A−1 | PROVEN | — | product metric |
| Cyc | 2=E\* (rank-one H2 generator, b2=1) | DERIVED-BY-INHERITANCE | — | F34 / F33.2B |
| CP | Smith form 1, qmin=1, dimensionless WZ phase 2 | PROVEN | — | none |
| CP′ | physical ce=2 | DERIVED-CONDITIONAL | — | UV=1 |
| T3 | anomaly gates (W3=0, torsion \=0, p1=0) on E\* | DERIVED-COND | 80% | gravY6|W5=0, H|W5=0, W3NW5=0 |
| T2-NS | dimensionless WZ phase 2 PROVEN; ce=2UV=1 | DERIVED-CONDITIONAL | — | UV=1 |
| T4a | theta-series rigidity (ZEFT=ZregZsphys=1/greg2) | PROVEN | — | Fourier rigidity |
| T4b/c | register generates the series; Gs=1 | DERIVED-CONDITIONAL | 72% | register-trace normalization (ZS-M44 v1.5) |
| T5 | Cnormreg,tree=1 DBI; CUV1PI **OPEN**; brane EXPECTED not computed | DBI / OPEN | 55% | full parent 1PI matching |
| Coll | −s=g2; convention split (Gs,ce) collapses to invariant g2, but CUV,MK remain | DERIVED | 90% | NG1–T5 |
| Canon | −s=1260/4807Meff4, Meff := CUV1/4MK | IDENTITY / REPARAMETERIZATION | — | definitional |
| T6 | radion minimum a\*=cflux/cbrane; relocation | DERIVED-COND | 65% | stable minimum; parent scales |
| Mod | Koenigs shape  M1-fixed; physical ℓ free | PROVEN | — | none |
| T7 | MUV not fixed by dimensionless data \+ topology | PROVEN-irreducible | 90% | Buckingham-π \+ §9 |
| §10 | Meff2.5 meV | REGRESSION | — | firewalled, not a prediction |
| §10 | ℓ=MK−180,m | DERIVED-CONDITIONAL | — | CUV=1 (canonical register-tree branch) |

---

## **§12. Falsification gates**

* **F-F36.1.** If A3A3 fails to give ZsZs/2, eses/, NG1 fails. *PASS.*

* **F-F36.2.** If KA−1 or the reduction sign is wrong, T1 fails. *PASS (symbolic).*

* **F-F36.3.** If the E\* charge pairing were non-primitive (Smith form 1), or if W30 / torsion 0 on the forced cycle, ce2. *PASS (computed).*

* **F-F36.4.** If ZS-M6’s greg2=dimY2 were back-defined rather than projected from the Block-Laplacian, T4 is circular. *Guarded by ZS-M6 C1–C10 provenance; R-1/R-2/R-3 flagged.*

* **F-F36.5.** If a charged bulk mode coupled to the odd singlet at p=0 (contra ZS-M6 §10.3), or a kinetic counterterm were symmetry-allowed, or an instanton unsuppressed, Cnorm1.

* **F-F36.6.** A dimensionful MUV as a function of A,Q \+ integers alone would violate Buckingham-π — impossible; any such claim is numerology.

* **F-F36.7.** A computed  inconsistent with observation once MUV is fixed by an *independent* UV input falsifies the identification (no retuning). w−1 at high significance forces the dynamical branch (NON-CLAIM here).

---

## **§13. Anti-numerology**

Claimed numbers: (i) 1260/4807=dimY2A/Q, locked, inherited PROVEN; (ii) s2=6 (ZS-F35 T1); (iii) 2=A/Q, greg2=62 (ZS-M6, DERIVED upstream); (iv) ce=2 (charge-pairing Smith form, PROVEN); (v) Gs=1 (partition matching \+ ZS-M6); (vi) Cnorm=1 (a normalization \= the definition of MUV). **No coefficient fit to data.** MUV is explicitly not computed from A,Q; its irreducibility is PROVEN, and the missing datum is localized to the loxodromic length ℓ. The Meff2.5 meV value is loaded only behind the derivation/⟂regression/ firewall. The pre-registered gate (no fitted exponent / half-weight / base-10 coincidence / back-solved scale) passes by construction.

---

## **§14. Cross-version safety**

* A,Q,dimZ=35/437,11,2, greg2=210/4807, 2=35/4807, \=2.2592495540, \=0.1148346250, z\*=0.43828+0.36059i: **unchanged**.

* **ZS-M1:** used only via (a) the exponential-homomorphism uniqueness \=ex (flux gluing, F33.4B-ii) and (b) the loxodromic multiplier \*=f′z\* fixing the Koenigs modulus  (§9). |f′z\*|=|lni||z\*|=0.89151\<1 (attracting), matching $^*$. Fixed point untouched. **M1 → S1 → U1 chain safe.*** (Verified: M1, M1b, M4a, M4b.)\*

* **ZS-M6:** newly load-bearing. greg2=dimY2 (Thm 2.2.1/2.2.2) discharges the §6 non-circularity; the odd-mode decoupling (§10.3) grounds the §7 bulk-vanishing. No ZS-M6 result is modified.

* **ZS-M44 (v1.5, integrates ZS-M45):** corrects the a0/a1 conflation (Q=a0=dim, *not* a1=Tr,L); the firm advance is the R-2 perturbation-artifact correction (§10.4 trap defused, democratic within irreps via Schur). The register-scalar density \=IQ/Q is asserted, not action-derived, so 2=A/Q and thus Gs=1 are **DERIVED-CONDITIONAL on register-trace normalization** (§6).

* **ZS-M45 (integrated into ZS-M44 v1.5 §6):** cell-coefficient sector-independence (cell=A); the genuine register Regge Hessian BWhingeB is uncomputed (§6.3 gives only a coordinate diagnostic). Operator equality **OPEN**.

* **ZS-A31 (v1.4):** consolidates the *effective* scale Meff=CUV1/4MK (observation fixes Meff2.48 meV only); the MK/M‾P hierarchy is OPEN, with the modular-depth e−2Q frontier (2 Borchers–Wiesbrock-forced) the pre-registered candidate, scoped to ZS-M46/M47.

* **ZS-F33:** Charge-Unit Obstruction preserved and strengthened; frozen w=−1 and the canonical branch (F33.6) used. No status reversed.

* **ZS-F34:** master form unmodified; F36 supplies Gs,ce and the K=A−1 correction; the 2=E\* identification is used verbatim. G-Outer-Physical inherited OPEN.

* **ZS-F35:** (1.1), s2=6 used verbatim; S3 → DERIVED-BY-INHERITANCE, S4 → PROVEN; F-F35.5/F-F35.7 closed/sharpened.

* **ZS-A27 / A28:** T7 is the F-sector instance of the A27 A–Q-Only No-Go, consistent with A28. No cosmological status altered; scale handed to ZS-A31.

---

## **§15. Verification**

zs\_f36\_verify\_v2\_1.py (SymPy; checks identical to v2.0 — the v2.1 edits are text-only), **56/56 PASS**, three blocks:

* **Core (17):** structural factor 36A/Q=1260/4807; greg2=210/4807, s2=6; NG1 invariances; T1 K=A−1 on SR2; collapse −s=g2; M1 |f′z\*|=0.89151; convergence 5,1,0.

* **v1.1 (13):** T4 theta-matching (mode-1 forces a=b; Zsphys=4807/210; full spectrum); T5 threshold; 2 no-go b2g=1; ce=2UV=1.

* **Companion / parent-action (26):** register projection greg2=dimY2 (M1a–d); charge pairing on T2 — Betti 1,2,1, torsion-free, Smith form 1, unimodular intersection form (M2a–e); anomaly gates w=1, W3=0, torsion \=0, p1=0 (M3a–e); Koenigs modulus  M1-fixed, physical ℓ free (M4a–d); radion minimum a\*=cflux/cbrane, V″\>0, relocation (M5a–d); odd-mode decoupling (M6a–b); firewall (M7a–b).

The verification is a **consistency \+ no-go certificate, not a closure certificate for** MUV — by design. The six companion modules of the pre-registered architecture (f36\_register\_projection, f36\_charge\_pairing, f36\_anomaly\_gates, f36\_koenigs\_modulus, f36\_radion\_stabilization, f36\_final\_firewall) are now **executed**, not deferred.

---

## **§16. Acknowledgements & Code Availability**

Consolidates internal Z-Spin Collaboration deep-exploration notes following ZS-F35 v1.5 and the pre-registered issue-tree architecture (Appendix A), including the parent-action module suite. zs\_f36\_verify\_v2\_1.py (SymPy) reproduces all 56 checks (identical to v2.0; the v2.1 edits are text-only). This work used AI tools (Anthropic Claude) for verification and drafting; the author assumes full responsibility, including the K=A−1 correction, the S2E\* cycle correction, and the honest ZS-M6 and non-perturbative caveats.

---

## **§17. Appendix A — Deep-exploration (issue-tree) record**

**Step 0 (long list, 7).** (1) normalization-covariance; (2) exact reduction \+ K; (3) the 2; (4) Gs=1 via partition matching / Hessian; (5) anomaly gates; (6) MUV via stabilization/transmutation; (7) scale no-go.

**Step 1 (MECE).** I1 \= (1); **I2 \= {(2)+(3)+(5)+(4-partition)+(4-threshold)}** (all load-bearing); I3 \= {(6) vs (7)}. Dropped: branch-ratio (tautological); dynamical-w (NON-CLAIM). *v1.2 parent-action sub-tree:* the cycle is forced to E\* (not a free node); charge pairing, anomaly classes, register normalization, and odd-mode decoupling become *computed/inherited* nodes rather than assumptions.

**Step 2–3 (tree \+ status).** NG1 PROVEN; T1 PROVEN; Cyc DERIVED-BY-INHERITANCE (F34); qmin=1 \+ dimensionless 2 PROVEN, dimensionful ce=2 **DERIVED-CONDITIONAL** (UV=1); T3 DERIVED-COND; **T4a PROVEN (theta rigidity), T4b/T4c DERIVED-CONDITIONAL (register-trace)**; **T5 register-tree DBI, full 1PI** CUV **OPEN**; Mod PROVEN; T7 metric scale OPEN under second-scale dynamics.

**Step 4 (convergence).** Re-traversal change counts 5,1,0 strictly decreasing  converged. v1.2 note: the parent-action expansion **discharged** two previously-conditional nodes (partition non-circularity → ZS-M6; anomaly ansatz → forced E\*) and **grounded** one (bulk-vanishing → ZS-M6 §10.3) *without* opening new OPEN nodes — a genuine convergence check (the decomposition tightened, it did not diverge).

**Step 5 (value).** Versus v1.1: ce=2 DERIVED → PROVEN; anomaly cycle forced; Gs=1 DERIVED-COND → DERIVED-BY-INHERITANCE; bulk=0 register-grounded; the scale no-go sharpened to the loxodromic length ℓ. Converged \+ corpus-non-collision (M1/M6/F33/A27/A28) \+ anti-numerology passed. **This is convergence with three frontier nodes precisely OPEN** — physical ce (conditional on UV=1), register-trace normalization / CUV (full 1PI OPEN), and the metric scale MK/MP (OPEN under second-scale dynamics). Terminus: an **honest conditional template**, not a closure — matching the corpus pattern that internal iteration converges to honesty, not to closure.

---

## **§18. References**

1. M. J. Hopkins, I. M. Singer, *Quadratic functions in geometry, topology, and M-theory*, J. Diff. Geom. **70** (2005) 329, arXiv:math/0211216.

2. E. Witten, *On flux quantization in M-theory and the effective action*, J. Geom. Phys. **22** (1997) 1, arXiv:hep-th/9609122.

3. D. S. Freed, E. Witten, *Anomalies in string theory with D-branes*, Asian J. Math. **3** (1999) 819, arXiv:hep-th/9907189.

4. J. D. Brown, C. Teitelboim, *Neutralization of the cosmological constant by membrane creation*, Nucl. Phys. **B297** (1988) 787\.

5. R. Bousso, J. Polchinski, *Quantization of four-form fluxes and dynamical neutralization of the cosmological constant*, JHEP **06** (2000) 006, arXiv:hep-th/0004134.

6. N. Kaloper, L. Sorbo, *Of pNGB quintessence and the cosmological constant*, Phys. Rev. Lett. **102** (2009) 121301\.

7. N. Kaloper, A. Padilla, *Sequestering the standard model vacuum energy*, Phys. Rev. Lett. **112** (2014) 091304\.

8. E. Buckingham, *On physically similar systems; illustrations of the use of dimensional equations*, Phys. Rev. **4** (1914) 345\.

9. J. Milnor, J. Stasheff, *Characteristic Classes*, Ann. Math. Studies **76**, Princeton (1974). \[Stiefel–Whitney / Wu classes; parallelizability of T2\]

10. Planck Collaboration, *Planck 2018 results VI: Cosmological parameters*, arXiv:1807.06209.

11. ZS-M1, *The i-Tetration Fixed Point and the Exponential-Homomorphism Uniqueness* (Z-Spin corpus).

12. ZS-M6, *The Block-Laplacian, the Register-Total Normalization Theorem (*2=A/Q*), and the Dimensional Coupling Norm* (Z-Spin corpus).

13. ZS-F33, *The Conditional UV Reduction of the Z-Spin Odd Three-Form — the Charge-Unit Obstruction* (Z-Spin corpus).

14. ZS-F34 v1.8, *The Six-Dimensional Charge Unit of the Z-Spin Three-Form* (Z-Spin corpus).

15. ZS-F35 v1.5, *The Multiplicity-Free Duality-Singlet Theorem and the Structural Dimensionless Factor* (Z-Spin corpus).

16. ZS-A27 v2.3, *The Z-Spin Vacuum-Energy Scale — A Dimensional No-Go, the Four-Root Map, and the Closure Frontier* (Z-Spin corpus).

17. ZS-A28 v2.0, *Vacuum Energy as a Projector-Valued Top Form — Conditional Closure of B3-D* (Z-Spin corpus).

---

## **§19. Version History**

* **v1.0 (July 2026):** NG1, T1 (+K=A−1), T2, anomaly gates, residual collapse, scale no-go, conditional closure. 17/17 checks.

* **v1.1 (July 2026):** Restored the two load-bearing computations under-developed in v1.0: full-flux partition matching (F36.T4) and the 1PI threshold audit (F36.T5); added the 2 cohomological no-go and the necessary-and-sufficient ce=2UV=1. 30/30 checks.

* **v1.2 (July 2026):** *Parent-action deep exploration executed.* **(1)** Fixes the internal cycle to the **corpus-forced Koenigs torus** 2=E\* (F34/F33.2B), correcting v1.1’s free S2 ansatz. **(2)** Computes the wrapped-brane **charge pairing** on T2 (cellular complex; Betti 1,2,1; torsion-free; flux-pairing Smith normal form 1; unimodular intersection form), upgrading ce=2 from DERIVED to **PROVEN**. **(3)** Computes the **anomaly gates** on E\* (T2 parallelizable w=1, W3=0, torsion \=0, p1=0), removing the ansatz-dependence (now conditional only on a trivial normal bundle). **(4)** Discharges the partition-matching **non-circularity** via **ZS-M6** (Register-Total Normalization 2=A/Q \+ Dimensional Coupling Norm greg2=dimY2), upgrading Gs=1 to **DERIVED-BY-INHERITANCE** (under ZS-M6 R-1/R-2/R-3). **(5)** Grounds the threshold **bulk-vanishing** in the ZS-M6 §10.3 odd-mode decoupling (slot 1=0). **(6)** Sharpens the scale no-go: the Koenigs **shape** \=+i/2 is M1-fixed, but the physical area A=ℓ2Im, needs the loxodromic length ℓ=MUV−1 — the missing datum, now explicit. **(7)** Executes the six pre-registered companion modules (charge pairing, anomaly gates, register projection, Koenigs modulus, radion, firewall), previously deferred. Verification 30 → **56/56**. Zero fitted parameters; A,Q,dimZ=35/437,11,2 LOCKED. **(v1.2 was later found to over-claim; see v1.8.)**

* **v1.3 (July 2026):** *Propagates the ZS-M44 result.* The companion Math-Spine paper ZS-M44 (*The Register-Trace Normalization Theorem*) closes ZS-M6’s **R-1** caveat — proving the “/Q” in 2=A/Q is the a1 Seeley–DeWitt mode count (PROVEN \=Q, coupling-immune), not a heuristic — and derives **R-3** from ZS-M6 §7A. Consequently the Gs=1 status (§6) tightens from “DERIVED-BY-INHERITANCE under R-1/R-2/R-3” to “**under the residual R-2 only**” (the register-scalar lattice embedding). Ledger T4, §14, and the abstract updated accordingly. **No numerical value changes**, and the metric-scale no-go (MUV PROVEN-irreducible) is untouched — R-1/R-2/R-3 concern only the dimensionless coupling. Verification unchanged at 56/56 (ZS-M44 carries its own 13/13).

* **v1.4 (July 2026):** *Propagates ZS-M44 v1.1 (R-2 closure).* The companion paper now discharges **all three** ZS-M6 caveats: R-1 (a1 mode-count normalization), R-3 (§7A), and **R-2** — split into R-2(a) within-irrep constancy (DERIVED, Schur \+ polyhedral symmetry) and R-2(b) cross-sector democratic normalization (CONFIRMED to 0.45% by an exact arrowhead inverse-eigenvalue solve, excluding sector-weighting X/Y=0.865, and correcting the ZS-M6 §10.4 “\~15% asymmetry” as a 2nd-order perturbation artifact). Consequently Gs=1 (§6) tightens from “under R-2 only” to **“all named caveats discharged”** (DERIVED-BY-INHERITANCE); the sole residual is a verification-level 50-digit spectral recompute. Ledger T4 (82→88%), abstract, §14 updated. **No numerical value changes**; the metric-scale no-go (MUV irreducible) is untouched. Verification 56/56 (ZS-M44 v1.1 carries 20/20).

* **v1.3–v1.7 (July 2026, superseded):** Propagation drafts (ZS-M44 v1.1→v1.2, ZS-M45, ZS-A31) that progressively claimed Gs=1 had “no undischarged rigor item.” **These over-claims are withdrawn in v1.8.**

* **v1.6 (July 2026):** *Propagates ZS-M45 \+ ZS-A31.* **ZS-M45** closes the last M-sector item (the cell-by-cell lattice-R): the ZS-M3 uniform holonomy deficit cell=A (Icell=/r=4/4=1, sector-independent) realizes the register-scalar curvature operator without Schur, so Gs=1 has no residual rigor item. **ZS-A31** consolidates the metric scale: the F33–F36 line reduces to one free dimensional parameter MUV (,Z/MUV4=121260/48072=0.669 DERIVED; MUV2.48 meV, ℓ80,m by regression; irreducible by ZS-A17/A27/A28; the H0/MP debt OPEN per A22 B3). **No numerical value changes**; the metric-scale no-go is untouched. Verification 56/56 (ZS-M45 6/6, ZS-A31 6/6).

* **v1.7 (July 2026):** *Notes the ZS-A31 v1.1 B3 deep exploration.* The last genuine OPEN of the F33–F36 line — the H0/MP10−61 action-level mechanism (A22 barrier B3) — was deep-explored in ZS-A31 v1.1 §8. Verdict: **still OPEN** (no mechanism in the current corpus), but materially sharpened: (i) B3 reduces to the single number MUV/MP2.010−31; (ii) it is a **debt, not a no-go** (the ratio is dimensionless; ZS-A27/A28 do not strictly forbid it); (iii) the coincidence MUV/MPA|VY−FY|=A28 (1.7%) is registered HYPOTHESIS-weak (30%, no mechanism, anti-numerology caveats explicit); (iv) closure needs the ZS-A17 emergent-metric advance, beyond current tools. **No F36 numerical value changes**; the metric-scale no-go is untouched. Verification 56/56 (ZS-A31 v1.1 carries 12/12).\# **The Integral UV Normalization of the Z-Spin Odd Three-Form: Exact** C5​​A3 **Reduction, Wrapped-Brane Charge Pairing on the Koenigs Torus, and the Metric-Scale Gate**

* **v1.8 (July 2026, review-corrected):** Integrates external review and cleans the version structure. **Honest downgrades:** (1) Gs=1 → **DERIVED-CONDITIONAL on register-trace normalization**, following the ZS-M44 v1.2 a0/a1 correction (the “/Q” is the normalized-trace rank a0=dim=Q, not a1=Tr,L; the density \=IQ/Q is asserted, not action-derived) and ZS-M45 v1.1 (uniform cell deficit gives cell-coefficient uniformity, not the register-scalar operator RIQ). (2) Dimensionful ce=2 → **DERIVED-CONDITIONAL on** UV=1 (only the primitive charge \=1 and dimensionless 2 are PROVEN). (3) Cnorm=1 → register tree branch **DBI**, full parent 1PI **OPEN** (F4F4 gauge-invariant and seam-even, so not forbidden by gauge invariance \+ seam parity). (4) Honest terminus −s=1260/4807,CUV,MK4 with the **metric-scale gate OPEN**; the closing path is the modular-depth e−2t\* frontier (ZS-M46/M47/A31 v1.2). Ledger T4 (90→72%), T2-NS, T5 downgraded; verification 56/56 \+ review 14/14. **No numerical value changes**; A,Q,dimZ=35/437,11,2 LOCKED. **F36 now terminates honestly at “metric-scale gate OPEN,” pending ZS-M46/M47.**

* **v1.9 (July 2026, current — body synchronized):** Second review found v1.8’s metadata honest but the body still carrying v1.2 closure language. v1.9 synchronizes throughout: **(a)** abstract “computes … from one parent action” → “organizes … within a common parent-action **template**”; **(b)** T4 split into **T4a theta-rigidity (PROVEN)** / **T4b physical partition matching (DERIVED-CONDITIONAL)** / **T4c** Gs=1 **(DERIVED-CONDITIONAL)**; **(c)** §5 charge pairing → qmin=1 and dimensionless 2 **PROVEN**, dimensionful ce=2 **DERIVED-CONDITIONAL** on UV=1; **(d)** §7 T5 body no longer reverses the top verdict — Cnormreg,tree=1 **DBI**, CUV1PI **OPEN**, brane **EXPECTED not COMPUTED**; **(e)** §10 separates the physical general form −s=1260/4807CUVMK4 from the canonical reparameterization Meff := CUV1/4MK; **(f)** w=−1 → **DERIVED-BY-INHERITANCE within the frozen branch** (not IMPORTED-PROVEN), with updated DESI DR2 language (3.1 BAO+CMB, 2.8–4.2 with SNe); **(g)** Appendix epistemic tree updated to **convergence with three frontier OPEN nodes** (physical ce, register-trace/CUV, metric scale). Honest terminus: −s=1260/4807CUVMK4, **metric-scale gate OPEN**; path via modular depth (ZS-M46/M47/A31). **No numerical value changes**; A,Q,dimZ=35/437,11,2 LOCKED. Cross-refs: ZS-M44 **v1.4** (integrates ZS-M45; executes §6.3).

* **v1.9 (July 2026):** Synchronized the body to the v1.8 metadata (T4 split into T4a PROVEN / T4b–T4c conditional; ce split; T5 register-tree DBI vs full-1PI OPEN; w=−1 frozen-branch DBI; Appendix tree \= convergence with three frontier OPEN nodes). *(Some ledger/anomaly conflicts remained — fixed in v2.0.)*

* **v2.0 (July 2026, terminal):** Third review integrated — removes the last status conflicts. Abstract/§6 no longer say “Gs=1 DERIVED-BY-INHERITANCE”/“non-circularity discharged” (now: algebraic back-definition avoided, register-trace bridge conditional). Claim-ledger **CP** split (Smith form/qmin/dimensionless 2 PROVEN; physical ce=2 DERIVED-CONDITIONAL); **Coll** row corrected (convention split collapses to g2, but CUV,MK remain); canonical −s=1260/4807Meff4 relabeled **IDENTITY / reparameterization**. **Anomaly** condition strengthened: internal p1T2=0 gives no *intrinsic* shift, but the full flux-quantization shift is **DERIVED-CONDITIONAL** on the ambient shifted classes (gravY6|W5, H|W5, W3NW5). b2=1 reworded as “rank-one H2 generator, unique up to homology” (not “the only 2-cycle”). Cross-refs updated to ZS-M44 v1.5, ZS-A31 v1.4. **No numerical value changes**; A,Q,dimZ=35/437,11,2 LOCKED. **Terminal version: the three OPEN items (**CUV**, register measure,** MK/M‾P**) are separate research programmes.**

* **v2.1 (July 2026, terminal — final synchronization):** Removes the last four residual old-version statements flagged in the fourth review; **no new research, no numerical value changes** (A,Q,dimZ=35/437,11,2 LOCKED; verification identical, 56/56 \+ 14/14). **(1)** §5 anomaly body reconciled with the v2.0 abstract: the **A1** clause now states that the internal p1T2=0 removes only the *intrinsic* internal-tangent contribution, while unshifted flux quantization additionally requires the ambient class gravY6|W5=0; the “Upgrade over v1.1” residual is restated as the full ambient \+ normal-bundle set (gravY6|W5=0, H|W5=0, W3NW5=0), and the **claim-ledger T3** condition column updated to match (was “trivial normal bundle”). **(2)** §8: the Meff := CUV1/4MK definition no longer says “Adopting CUV=1” — the definition is CUV-agnostic. **(3)** §10: the regression sentence now fixes only Meff2.5 meV (ZS-A31 v1.4), with ℓ=MK−180,m flagged **DERIVED-CONDITIONAL on** CUV=1; the redundant “−s=1260/4807MUV4 DERIVED” ledger row is deleted, and the closing rows now read Meff2.5 meV (REGRESSION) and ℓ80,m (DERIVED-CONDITIONAL on CUV=1). **(4)** Abstract A31 hand-off aligned to ZS-A31 v1.4: ,Z/Meff4=121260/48072 (identity), hierarchy frontier MK/M‾P=?e−2Q. Per the review directive, **F36 is now closed to further revision**; the three genuine OPEN items (CUV full-1PI, action-derived register measure, MK/M‾P) remain separate research programmes.

* **Version:** v2.1 (supersedes v1.0–v2.0; integrates external review; version structure cleaned). **v2.1 completes the honest synchronization** (the third and fourth reviews found and cleared the residual T4/CP/collapse/anomaly status conflicts). This is the **terminal version** of the F33–F36 charge-unit line; the three genuine OPEN items (CUV full-1PI, action-derived register measure, metric scale MK/M‾P) are each a *separate research programme*, not a further F36 revision. Now uniformly: (i) following the ZS-M44 v1.2 a0/a1 correction and ZS-M45 v1.1, Gs=1 is **DERIVED-CONDITIONAL on register-trace normalization**, not “no undischarged rigor item”; (ii) the *dimensionful* ce=2 is **DERIVED-CONDITIONAL on** UV=1 (only the primitive charge \=1 and the *dimensionless* WZ phase 2 are PROVEN); (iii) Cnorm=1 holds at the **register tree level (DBI)** but the **full parent 1PI matching is OPEN** — F4F4 is gauge-invariant and seam-even, so gauge invariance \+ seam parity do not forbid the counterterm. The honest terminus is −s=1260/4807,CUV,MK4 with the **metric-scale gate OPEN**; the path to close it (modular depth e−2t\*) is scoped to ZS-M46/M47/A31.