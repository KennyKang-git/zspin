**ZS-S17**  
**The Glueball Hyperfine Structure from a Truncated-Icosahedron Cochain Vertex**

***A Closed Two-T₁ Active Space, a Casimir-Coproduct Layer-Lift, and the Remaining Hessian Gate***

Kenny Kang · Z-Spin Cosmology Collaboration  —  Standard Model  |  ZS-S17 v2.2 FINAL  |  July 2026  
Locked inputs: A \= 35/437, Q \= 11, dim Z \= 2, v \= 245.93 GeV, λ₁ \= 1.2428, g² \= 4π(11/93) \= 1.49; no new fitted parameters  
**Verification: 21/21 computed & proof checks PASS; 2 OPEN gates pre-registered (not counted)  |  Zero Fitted Parameters**  
Companions (run from any single folder): zs\_s17\_verify\_v2\_2.py, zs\_s17\_active\_space.py, zs\_s17\_wp\_results.json

**§0. Abstract**  
**The hyperfine coefficient g\_hf itself is DERIVED-CONDITIONAL, not DERIVED: what this paper closes is the geometric and representation-theoretic bridge, and what it leaves open is a single normalization.** Three results stand. **(1) The active space.** The Yang-Mills-relevant alternating cochain vertex maps T₁(λ₁ \= 1.2428) ⊕ T₁(λ\_h \= 7.5211) into itself with zero leakage over *all four* input pairs. Gap-only leakage is 7.14% (correcting the 23% carried since v1.6), split 92.8605% / 7.1395% between the two copies. The closure is a property of the *alternating* vertex specifically: the full non-antisymmetrized bilinear leaks 29.5%. With the copies aligned by the icosahedral intertwiner under the signed face action, all eight coefficients c\_{rst} are exactly ε-proportional, confirming dim Hom\_I(T₁⊗T₁, T₁) \= 1\. **(2) The reduced field has spurious zeros.** A resultant computation gives the global count in the hedgehog sector: three nontrivial real zeros, one at |q\*|² \= 81.6 (Krawczyk-certified enclosure) and two at |q\*|² ≈ 10⁶–10⁷. The near one survives the six-mode lift essentially unmoved, so it is not an artifact of the crudest truncation; but the 32 face holonomies there give |tr W|/3 \= 0.40–0.49, so it is not pure gauge. It is a spurious vacuum of the polynomial reduction, which is why the unrestricted reduced model is not a usable approximation. **(3) The Layer-Lift is an operator identity.** On T₁ the Casimir is C₂ \= 2I, so L₂|\_{T₁} \= (λ₁/2)C₂, and the coproduct defect is I\_Z \= λ₁ S₁·S₂ exactly. With Q\_Z \= ¼(I\_Z \+ 2λ₁I) this gives M(2⁺⁺)²/M(0⁺⁺)² \= 1 \+ 3λ₁/4, R \= 1.3900. The one remaining physical step is whether the S14 mass-squared Hessian is exactly Q\_Z — that factor of 1/4 is gate F-S17.7.

**Epistemic Status Legend**  
**PROVEN**  — exact identity or theorem, verified to machine precision.  
**COMPUTED / CERTIFIED**  — numerical result; CERTIFIED adds an interval enclosure (existence and local uniqueness), conditional on the computed inputs and on floating-point interval evaluation.  
**DERIVED / DERIVED-CONDITIONAL**  — from PROVEN inputs / modulo one explicitly named open normalization.  
**CLOSED-NEGATIVE**  — settled, and the answer is that the route fails.  
**RETRACTED / CORRECTED**  — previously claimed here; withdrawn or fixed, with the reason stated.  
**OPEN**  — well-posed, not settled; pre-registered as a gate.

**§1. The Active Space, and the Exact Scope of its Closure**  
The truncated-icosahedron face Laplacian has two T₁ eigenvalues in play, the gap λ₁ \= 1.2428 and λ\_h \= 7.5211. Forming the alternating cup product of the gap edge potentials a\_α \= B₂ᵀu\_α/λ gives a face 2-cochain that decomposes as  
Table 1\. Power decomposition of the alternating curvature built from gap potentials.

| eigenspace | T₁(λ₁ \= 1.2428) | T₁(λ\_h \= 7.5211) | all others |
| ----- | ----- | ----- | ----- |
| **power fraction** | **92.8605%** | **7.1395%** | **|rest| \< 2.4 × 10⁻¹⁴** |

So the gap-only leakage is **7.14%, correcting the 23% quoted from v1.6 through v2.0**. Extending the test to all four input pairs (s,t) ∈ {0,1}², the leakage out of the six-mode space is zero to machine precision. **\[PROVEN\]**

| The scope of “exactly closed”.  This closure is a property of the antisymmetric — that is, Yang-Mills-relevant — vertex, and of nothing more. The full, non-antisymmetrized bilinear built from the same potentials leaks 29.54% out of the six-mode space. The correct statement is therefore: the two-T₁ space is exactly closed under the alternating vertex. It is not closed under general bilinears, and this paper claims only the former. |
| :---- |

Face 2-cochains carry orientation, so the icosahedral group acts by a *signed* face permutation; with that action \[L₂,P\] \= 0 exactly, the intertwiner between the two T₁ copies is one-dimensional (Schur), and alignment is exact to 10⁻¹⁵. In the aligned bases the six-mode magnetic field is  
**B\_{r,i}^a \= Ω\_r q\_{r,i}^a \+ (g/2) Σ\_{s,t} c\_{rst} f^{abc}ε\_{ijk} q\_{s,j}^b q\_{t,k}^c ,**  
and all eight c\_{rst} are exactly ε-proportional (max residual 8 × 10⁻¹⁵), confirming dim Hom\_I(T₁⊗T₁, T₁) \= 1: c₀₀₀ \= −0.175800, c₀₀₁ \= −0.002311, c₀₁₁ \= 0.000242, c₁₀₀ \= −0.048746, c₁₀₁ \= 0.011002, c₁₁₁ \= 0.001943 (the overall sign of the r \= 1 row is the arbitrary high-T₁ basis orientation). **\[PROVEN\]**

**§2. The Spurious Zeros of the Reduced Field**  
For the hedgehog q\_{r,i}^a \= v\_rδ\_i^a along an su(2) subalgebra, ε\_{ijk}f^{abc}δ\_j^bδ\_k^c \= 2δ\_i^a, and B \= 0 becomes two coupled quadratics. Eliminating v₁ by the resultant gives a quartic in v₀, so the count below is **global, not the output of a search**:  
Table 2\. All nontrivial real zeros of the reduced magnetic field in the hedgehog sector.

| zero (v₀, v₁) | |q\*|² | remark |
| ----- | ----- | ----- |
| **(5.187, 0.555)** | **81.6** | **Krawczyk-certified; three-mode value was (5.2015, —), |q\*|² \= 81.2** |
| (−22.39, −917.7) | 2.5 × 10⁶ | far outside any meaningful truncation |
| (191.5, −3582.7) | 3.9 × 10⁷ | far outside any meaningful truncation |

This corrects v2.1, which reported a single zero: that count came from an fsolve grid too small to reach the two distant roots. **The relevant root is the near one, and it barely moves between the three-mode and the exactly-closed six-mode space, so it is not an artifact of the crudest truncation.** Its status is COMPUTED / CERTIFIED rather than PROVEN: a Krawczyk operator on the box v₀ ∈ \[5.18682, 5.18722\], v₁ ∈ \[0.55432, 0.55492\] maps strictly inside it (det J \= −3.224), certifying existence and local uniqueness — conditional on the numerically computed c\_{rst} and on ordinary floating-point interval evaluation. Uniqueness in the full 48-coordinate active space is not claimed.

| It is not a Gribov copy (retained from v2.1).  Reconstructing A\_e \= Σ q\_{r,i}^a a\_r(e)\_i T^a and U\_e \= exp(iA\_e), the holonomy around each of the 32 faces gives |tr W|/3 \= 0.398–0.485, nowhere near the unity required of a pure-gauge configuration. Vanishing of the projected curvature does not imply vanishing of the full lattice curvature. The zero is a spurious vacuum of the polynomial reduction rather than a gauge copy — a worse diagnosis, since a genuine copy would be physically harmless. Accordingly what is CLOSED-NEGATIVE is the unrestricted polynomial reduced model as a physical approximation; the gauge-reduced bottom-up route remains OPEN, and the honest way to it is a Faddeev-Popov measure on the fundamental modular region rather than a larger Fock cutoff \[4,5\]. The attribution of the SU(2) scalar collapse to localization on this zero likewise remains HYPOTHESIS-strong: no wavefunction-localization or tunnelling-density computation has been performed. |
| :---- |

**§3. The Layer-Lift as a Casimir-Coproduct Operator Identity**  
On the gap representation T₁ the quadratic Casimir is C₂ \= Σ\_i J\_i² \= 2I exactly, so L₂ restricted to T₁ equals (λ₁/2)C₂. For a two-body state Δ(J\_i) \= J\_i⊗I \+ I⊗J\_i, and the coproduct defect is  
**I\_Z \= (λ₁/2)\[Δ(C₂) − C₂⊗I − I⊗C₂\] \= λ₁ Σ\_i J\_i⊗J\_i \= λ₁ S₁·S₂ ,**  
with eigenvalues −2λ₁, −λ₁, \+λ₁ on T₁⊗T₁ \= A\_g ⊕ T₁ ⊕ H. Referring to the ground state via Q\_Z \= ¼(I\_Z \+ 2λ₁I) gives Q\_Z \= 0 on A\_g and 3λ₁/4 on H (verified spectrum {0, 0.3107, 0.9321}), hence  
**M(2⁺⁺)² / M(0⁺⁺)² \= 1 \+ 3λ₁/4   ⇒   R \= 1.3900 .**  
This is representation theory, not arithmetic substitution, and the operator identity itself is **DERIVED**. One gate separates it from a derived physical prediction: restricting the S14 master action to Sym²(T₁) and canonically normalizing, is δ²S/δ(q⊗q)² exactly ¼(I\_Z \+ 2λ₁I)? If yes, g\_hf \= λ₁ becomes DERIVED; until then R \= 1.390 is **DERIVED-CONDITIONAL** on that single factor. **\[gate F-S17.7\]**  
The second gate is external. Define g\_hf(N) \= (4/3)\[(M(2⁺⁺)/M(0⁺⁺))² − 1\] from the continuum SU(N) lattice spectra and fit g\_hf(N) \= g\_∞ \+ a/N² \+ b/N⁴. The Layer-Lift predicts g\_∞ \= λ₁ \= 1.2428 and **a \= 0**. (The v2.0 leading-order discriminator was retracted in v2.1: at fixed ’t Hooft coupling g²C\_A \= g²N is N-independent, so only the subleading slope has power.) **\[gate F-S17.6\]**

**§4. Final Status**  
With g\_hf \= λ₁: m(0⁺⁺) \= **vA/Q** \= 1.791 GeV and m(2⁺⁺) \= 1.390·**vA/Q** \= 2.489 GeV, both within about 1σ of lattice SU(3) \[6\]; the λ₁ band retains its exact toy-ensemble frequency 89/3600 \= 2.47%.  
Table 3\. Claim-by-claim final status.

| claim | status |
| ----- | ----- |
| TI representation structure (T₁, A\_g ⊕ T₁ ⊕ H, J \= 2 → E ⊕ T₂) | CLOSED |
| signed color factor −C\_A; sign unobservable in R (parity theorem) | CLOSED / PROVEN |
| two-T₁ active space closed under the alternating YM vertex (all pairs) | CLOSED / PROVEN |
| gap-only leakage \= 7.14%, not 23% | CORRECTED / PROVEN |
| all c\_{rst} ∝ ε; dim Hom\_I(T₁⊗T₁,T₁) \= 1 | CLOSED / PROVEN |
| nontrivial hedgehog zero; survives the six-mode lift; global count \= 3 | COMPUTED / CERTIFIED |
| Gribov-copy reading of that zero | RETRACTED |
| unrestricted polynomial reduced model as a physical approximation | CLOSED-NEGATIVE |
| scalar collapse caused by localization on the zero | HYPOTHESIS-strong |
| v1.9 Richardson extrapolation; v2.0 SU(N) leading discriminator | RETRACTED |
| Casimir-coproduct Layer-Lift operator identity I\_Z \= λ₁ S₁·S₂ | DERIVED |
| R \= 1.390 as a physical prediction | DERIVED-CONDITIONAL |
| mass-Hessian 1/4 normalization (F-S17.7) | OPEN |
| 1/N² slope test g\_∞ \= λ₁, a \= 0 (F-S17.6) | OPEN (pre-registered) |
| gauge-reduced bottom-up dynamics (FP measure on the FMR) | OPEN |
| full physical bridge | OPEN |

The conclusion of S17 is deliberately narrow. **The geometric and representation-theoretic bridge is closed; the physical mass normalization is isolated to one explicit S14 Hessian gate.** Why the scalar/tensor structure arises, why the ε tensor is forced, which active space closes exactly, what the signed color factor is, why the bottom-up polynomial reduction cannot be trusted, and from which operator identity g\_hf \= λ₁ follows — these are settled here. The two remaining questions are not version revisions of this paper but separate problems: an action-reduction calculation (F-S17.7) and an external lattice fit (F-S17.6). This version is final.

**Appendix A. Verification Ledger**  
Table A1. Fail-closed ledger; each entry asserts on a computed number read from the companion JSON.

| \# | check | tag | \# | check | tag |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | λ₁ \= 1.2428, λ\_h \= 7.5211 | C | 12 | Krawczyk enclosure certified | CT |
| 2 | 92.8605 / 7.1395 / |rest| \< 2.4e-14 | PR | 13 | |q\*|² \= 81.6 vs 81.2 | C |
| 3 | all-pairs alternating leakage \= 0 | PR | 14 | holonomy 0.40–0.49: not a copy | RT |
| 4 | full bilinear leaks 29.5% (scope) | C | 15 | projected B \= 0 ⇸ F\_full \= 0 | D |
| 5 | signed action; 1-dim intertwiner | C | 16 | fixed ’t Hooft: g²C\_A N-indep. | RT |
| 6 | all c\_{rst} ∝ ε | PR | 17 | C₂(T₁) \= 2I | PR |
| 7 | c₀₀₀, c₁₀₀, c₁₁₁ values | C | 18 | I\_Z \= λ₁S₁·S₂; Q\_Z spectrum | PR |
| 8 | three-mode zero 5.2015 | C | 19 | R \= 1.3900 operator identity | D |
| 9 | six-mode zero (5.187, 0.555) | C | 20 | m(0⁺⁺), m(2⁺⁺) | A |
| 10 | global count \= 3 (resultant) | C | 21 | anti-numerology 89/3600 | C |
| 11 | two extra zeros at |q|² \~ 1e6–1e7 | C | — | F-S17.6, F-S17.7 registered | OPEN |

**References**  
\[1\] K. Kang, ZS-S7; ZS-S14; ZS-F48; ZS-M53 (Z-Spin Cosmology, 2026).  
\[2\] V. N. Gribov, Nucl. Phys. B 139, 1 (1978).  
\[3\] D. Zwanziger, Nucl. Phys. B 412, 657 (1994); B. Simon, Ann. Phys. 146, 209 (1983).  
\[4\] H.-P. Pavel, “SU(3) Yang-Mills Hamiltonian in the flux-tube gauge: strong coupling expansion and glueball dynamics,” arXiv:1611.06542 \[hep-th\].  
\[5\] H.-P. Pavel, “Low-energy spectrum of SU(3) Yang-Mills quantum mechanics,” arXiv:2112.06248 \[hep-th\].  
\[6\] C. J. Morningstar, M. J. Peardon, Phys. Rev. D 60, 034509 (1999); A. Athenodorou, M. Teper, JHEP 11, 172 (2020), arXiv:2007.06422; JHEP 12, 082 (2021), arXiv:2106.00364.  
\[7\] R. E. Moore, R. B. Kearfott, M. J. Cloud, Introduction to Interval Analysis (SIAM, 2009), ch. 8 (Krawczyk operator).  
\[8\] A. N. Hirani, Discrete Exterior Calculus, Ph.D. thesis, California Institute of Technology (2003).

**Version History**  
**v2.2 FINAL (July 2026):** Closing revision in response to the v2.1 review; no new physics. Scope fix: the closure test now runs over all four (s,t) pairs and the claim is limited to the alternating Yang-Mills vertex — the full non-antisymmetrized bilinear leaks 29.5%, so “exactly closed” is not said of the bilinear. Correction: the resultant gives the global count of nontrivial hedgehog zeros as THREE, not the one reported in v2.1 (whose fsolve grid was too small); the two extra zeros lie at |q\*|² ≈ 10⁶–10⁷. Rigour: the relevant zero is downgraded from PROVEN to COMPUTED and now carries a Krawczyk-certified enclosure (existence and local uniqueness). Accounting: the OPEN slope gate is no longer counted as a PASS — 21/21 computed and proof checks pass, with F-S17.6 and F-S17.7 registered separately. Reproducibility: the companion writes and the verifier reads the JSON next to the scripts, with no absolute paths. Presentation: the negative floating-point residual is reported as |rest| \< 2.4 × 10⁻¹⁴, the flux-tube-gauge reference is completed (Pavel, not Reinhardt), and the title now says “hyperfine structure” since the coefficient remains DERIVED-CONDITIONAL. S17 is closed at this version; F-S17.6 and F-S17.7 are successor problems.  
**v2.1:** two-T₁ active space; leakage corrected 23% → 7.14%; Gribov-copy and SU(N) discriminator retracted; Casimir-coproduct Layer-Lift. **v2.0:** parity theorem for the color sign; second zero. **v1.9–v1.0:** DEC metric γ\_Z \= 0.115; block Lanczos; Galerkin theorem; earlier retractions.