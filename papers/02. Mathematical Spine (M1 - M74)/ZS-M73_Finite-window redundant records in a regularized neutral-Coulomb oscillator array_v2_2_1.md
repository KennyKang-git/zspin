# ZS-M73 v2.2.1

# Finite-window redundant records in a regularized neutral-Coulomb oscillator array

## A square-root-logarithmic record theorem for the full model, and a one-way continuum reduction of the source-edge problem

**Version:** 2.2.1, 24 September 2026 (KST). A correction-only release of v2.2 that follows the frozen cross-family audit of v2.2 (Appendix S). No theorem is added, and no theorem statement or constant of v2.2 is changed. In the proof of Theorem NP-SQRTLOG one quantifier of the tail step is narrowed and notes are added (F32-03), without changing the logic; the prior-art comparison for Lemma SR is narrowed in two places (F32-04). No v2.2 text is removed except the short fragments listed in Appendix S.4. **Language:** English. **Output form:** RESEARCH PAPER, internal; neither published nor submitted. This follows the separate assessor card of Section 16.0, which gives paper qualification PASS, research grade 3, and grade 4 as a candidate not established. The author does not self-grade. The frozen audit of v2.2 (Codex/GPT; Section 16.0S and Appendix S) re-evaluated the cumulative contribution as research grade 4, restricted to a project-internal mathematical and method contribution. Both assessments are recorded, and v2.2.1 changes neither. **Mission role:** SUPPORT + METHOD, FQ2/RQ3. **Lineage:** fully integrated revision of v2.1, following its frozen audit (Appendix R). The v2.1 and earlier releases are preserved unchanged in `provenance/`. The new research is in Sections 8.17 and 8.18. It is not a v2.1.1 patch.

| Release field | Current status |
|---|---|
| Strongest full-model theorem (new) | Theorem NP-SQRTLOG, Section 8.17: $\Omega_R=10^4\sqrt{1+\log\lceil R^{1/3}\rceil}$ and $D_j(t)\ge.98853$. It holds for every $R\ge2$, every memory and the whole $I_R$, for the exact non-convex Hamiltonian with the P1 preparation. Interval certificate over $\ell\in[1+\log2,10^{15}]$ and a monotone tail |
| Previous full-model theorem | NP-LOG, $\Omega_R=10^4(1+\log n)$, retained and now superseded in rate |
| Key new tools | Growing-threshold comparators (Theorem L-hat$_Y$), Lemmas LOC-A$_Y$ and LOC-B$_Y$, and refined $L^2$ majorants (Lemma SQ-L2) |
| Source-edge problem (new) | Theorem CR and Corollary CR-R, Section 8.18. Lattice responses for any smooth drive, including the actual S9 source row, converge weakly to the continuum solution. Continuum unboundedness near an edge forces lattice unboundedness and record failure at fixed confinement. One-way reduction |
| EG and source transfer | The lattice source-transfer step is closed by Theorem CR. The remaining statement is Hypothesis EG-C (continuum edge unboundedness), which is OPEN. EG (the lattice rate $n^\gamma$) is still unproved and is not needed for the obstruction |
| Retained results | COMP-SQRTLOG, RD-V, SRX, WO; DF, EL, SRC, W, Q-prime, LN; all earlier theorems as corrected in Appendices Q and R |
| Frozen v2.1 audit | AUDIT-PASS-MINOR, highest severity S1; META REPLAN (the sub-log obstacle had been misattributed to the model instead of the fixed comparator threshold). Appendix R |
| Frozen v2.2 audit and v2.2.1 | AUDIT-PASS-MINOR, highest severity S1, TERMINAL-IN-SCOPE recommended; no S2+ defect (Codex/GPT, cross-family, not blind). Five minor findings F32-01…05 (a tail-row class, the certificate's acceptance gate, the scope of a monotonicity sentence, a prior-art comparison, and stale pointers and margins) are corrected in v2.2.1 without changing any theorem or constant. Appendix S |
| Grade / qualification | Frozen v2.2 audit (Section 16.0S, Appendix S): research grade **4** for the cumulative contribution, restricted to a project-internal mathematical and method contribution; candidate grade NONE; PAPER QUALIFICATION PASS, RESEARCH PAPER. The auditor states that an increment-only assessment of 3 is also defensible. From the separate assessor card, Section 16.0, which assessed the increment: research grade **3**, candidate 4. Grade 4 is NOT ESTABLISHED under Mission §1.4, although alternative (ii) of the user-operationalized criterion is met literally. PAPER QUALIFICATION PASS gives the output form RESEARCH PAPER (internal). The author did not adjudicate |
| Primary-source status | The named Van Bladel, Mantič–París–Berger and Meixner 1972 texts remain unread at equation level (re-attempted; Section 15.12). They concern the continuum edge exponent, not Theorems NP-SQRTLOG or CR |
| Evidence | The v2.1 driver was rerun: 75/75 PASS. The new rows cover the interval covering, tail, comparator, LOC-A, coincidence, fault injections and continuum-reduction diagnostics (Section 12.8). No row proves EG-C or grades the research |
| Independence | v2.1 was authored by Codex/GPT. The audit and the v2.2 research were done by Claude with the v2.1 reports visible, so they are not blind. The new proofs were attacked by a separate Claude referee instance, which found no S2+ defect and eleven S0/S1 items, all integrated. The qualified-human anchor is NONE |

## Abstract

We study redundant records in a regularized neutral-Coulomb oscillator array with the S9 geometry and an observation window growing as $R^2$. We ask how strongly a trap must confine the array for every memory to carry a readable record of the source throughout the window.

The previous full-model result required logarithmic confinement. The obstruction to anything faster was attributed to global localization errors that grow with the volume. We show that this growth came from a fixed coincidence threshold in the comparison potential. We let the threshold grow like $(\log R)^{1/4}$ and keep the comparison potential uniformly convex. The probability that any site leaves the coincidence region is then polynomially small with arbitrary power. Combined with a variance readout and refined $L^2$ covariance majorants, this proves that $\Omega_R=10^4\sqrt{1+\log\lceil R^{1/3}\rceil}$ suffices. For the exact non-convex Hamiltonian and its switched-off ground state, the trace-distance readout is at least $.98853$ for every $R\ge2$, every memory and every time in the window. The constants are certified by outward interval arithmetic on a covering of all sizes up to $\ell=10^{15}$ and by a monotone tail argument. The square-root law is the limit of every argument that bounds a convex comparator's Hessian by absolute dipolar row sums.

For the exactly solvable quadratic model we prove a one-way lattice-to-continuum reduction of the source-edge problem. The lattice response to any smooth drive, including the actual source row, converges weakly to the solution of the continuum volume-integral equation of a uniaxial dielectric cube. If that solution is unbounded near an edge, the lattice source factor diverges and the record property fails at every such fixed confinement. Whether the continuum solution is unbounded (Hypothesis EG-C) remains open. A log-scale heuristic reproduces the edge exponent and identifies the single scalar condition that a bounded solution would have to satisfy. The frozen audit of the previous version, its corrections and the verification boundaries are included.

## 1. Question, contract and contribution

### 1.1 The question that is answered

How strongly must a declared trap confine a regularized neutral-Coulomb oscillator array to create $R$ simultaneously readable records during the prescribed window? We keep the spatial family, coupling scaling, observable and time window fixed. Within that family we improve the sufficient confinement estimate and identify what prevents a fixed confinement. Two declared preparations are used: the common Gaussian $\Phi$, and the switched-off interacting ground state P1 (Theorems NP-P1, NP-LOG and NP-SQRTLOG). In this family the source distance increases with $R$, the memory displacement decreases with $R$, $T_R=O(R^2)$ and the source–memory signal is $O(R^{-2})$. The improved trap law is not a constant total resource cost.

### 1.2 Exact theorem contract

| Item | Contract |
|---|---|
| Systems and space | $N=R+1$ binary registers and scalar oscillators on $(\mathbb C^2)^{\otimes N}\otimes L^2(\mathbb R^N)$ |
| Quantifiers | Every integer $R\ge2$, every memory, both source labels, every $t\in[.99t_*,1.01t_*]$ |
| Model | The exact regularized neutral Coulomb interaction and S9 geometry of Section 2. No wall, no finite-range cut, no multipole truncation |
| Numerical units | $\hbar=m=a=g=1$ |
| Preparation | Either the common oscillator ground state $\Phi$ of $H_A$, independent of labels (Theorems LC-prime, NP-G), or the exact ground state $\Psi_0$ of $H_{\rm MC}(0)$ (Theorems NP-P1, NP-LOG, NP-SQRTLOG; Section 7.3). Memories start in $\vert+x\rangle^{\otimes R}$ |
| Confinement | $\Omega_R=10^4\sqrt{1+\log n}$ (NP-SQRTLOG); $\Omega_R=10^4(1+\log n)$ (NP-LOG); $\Delta_R=10^4n^{3/5}$ (NP-G), $10^4n^{1/2}$ (NP-P1), $10^4n^{4/3}$ (LC-prime), with $\Omega_R^2=\Delta_R^2+8+\delta_c$ |
| Conclusion | $D_j(t)\ge.98853$ with $\Omega_R\le10^4\sqrt{1.4621+\tfrac13\log R}$ (NP-SQRTLOG); $D_j(t)\ge.9885$ with $\Omega_R\le10^4(1.4621+\tfrac13\log R)$ (NP-LOG); $D_j(t)\ge.9885$ with $\Omega_R<13196R^{1/5}$ (NP-G) or $<12600R^{1/6}$ (NP-P1); $D_j(t)\ge.98538$ with $\Omega_R<18518R^{4/9}$ (LC-prime) |
| Quadratic-model statements | Uniform first-order bound on every S9 set (DF); exact second-order edge and corner logarithms (EL); smooth-drive transfer at second order (SRC); exact Schur source formula (SRX); whole-window obstruction (WO); one-way continuum reduction and conditional record failure (CR, CR-R) |
| Proof chain (NP-SQRTLOG) | Growing-threshold convex comparators; log-Sobolev localization of the exact non-convex spectrum (LOC-A$_Y$, LOC-B$_Y$); site-resolved Euclidean covariance with refined $L^2$ majorants; source coefficient at every shift; variance readout; interval covering with a monotone tail |
| Limits | No fixed-confinement theorem and no law below $\sqrt{\log R}$ for the full model. Hypothesis EG-C is open, so no fixed-confinement no-go is proved. No logarithmic Gaussian-preparation law. No derived physical instrument, trap or clock |
| Kill tests | Failure of a comparator Hessian bound (L-hat$_Y$), of the pointwise bound LOC-A$_Y$, of a log-Sobolev or covariance step, or of an interval enclosure. A growing certificate term in the tail. A lattice–continuum mismatch in Lemma CR-1. Prior-art subsumption without the added proof work |

### 1.3 The retained certificates and the remaining obligations

The static energy decomposition and the earlier parity estimate remain

$$
E_0(z)=\mu_z-e_2(z)+r_z,\qquad
|c_3(z)|\le\sigma_e\kappa^2+2\sigma\kappa_e\kappa. \tag{1.1}
$$

The earlier right side carries $N^{3/2}$. Version 1.5 reduced the global Hessian bound to $O(n)$ and identified the cubic term as the remaining obstruction to its square-root certificate. Theorem LC and Theorem LC-prime then changed the sufficient exponent to $4/9$ without a linked-cluster assumption. Version 1.7 bounded the label flips of the exact branch energies non-perturbatively under global convexity (Section 8.12), with the binding costs being preparation echo and convexity (Theorems NP-G, NP-P1 and the barrier NP-B). Version 1.8 added full-displacement stability (Theorem ST). Version 1.9 removed the convexity requirement for P1 with a convexified comparator and log-Sobolev localization (Theorem NP-LOG, Section 8.14). Version 2.0 decided the coefficientwise signed-kernel question (Theorems DF and EL, Proposition W). Version 2.1 corrected several implications and proved the comparator theorem COMP-SQRTLOG (Section 8.16).

Version 2.2 makes two changes.

1. **The full-model localization obstacle was a threshold artifact.** Lemmas LOC-A and LOC-B were proved with the coincidence threshold $|u_a|\le\tfrac15$ fixed. With that threshold their volume-times-tail errors grow at every sub-logarithmic law. Section 8.17 lets the threshold grow like $\ell^{1/4}$ and controls the Coulomb cores that then enter the comparator. It also replaces pointwise by $L^2$ majorants where Lemma SR allows it. The outcome is Theorem NP-SQRTLOG for the exact model.
2. **The lattice part of the source-edge question is removed.** Section 8.18 proves that lattice unboundedness for the actual S9 source row follows from unboundedness of one continuum solution (Theorem CR), and that this implies record failure at fixed confinement (Corollary CR-R). The open question is thereby reduced to Hypothesis EG-C.

The contributions submitted for assessment are Theorem NP-SQRTLOG with its certificate, and Theorem CR with Corollary CR-R. The earlier contributions are retained as stated in their sections. Standard tools retain their attribution: Gaussian interpolation, spectral perturbation theory, log-Sobolev semiboundedness (Federbush, Gross), Bakry–Émery, Helffer–Sjöstrand, Poisson summation, weak compactness and the volume-integral formulation of dielectric scattering.

### 1.4 Integration and provenance

The frozen v2.1 manuscript has SHA-256 `1274abb23ade8c2a83e909a702c755039ca607fe1ca92c958ca9984a4a866c0e`; the v2.1 release ZIP has SHA-256 `6c9a352592cfbe9eefebd4ba83a7f78f06e62d962b24aa6ae3aab5d51ed9e39b` and is preserved byte-identical as `provenance/ZS-M73_v2_1_release.zip`. Its 17 manifest entries match. The v2.0 release, its provenance chain and all earlier originals are nested inside it. The new history file extends the latest project history (H-0413) by H-0414. A timestamp discrepancy between two copies of H-0409 is reported, not repaired (Appendix R, F31-05).

This manuscript retains the inherited mathematical development. v2.2 changes are integrated in the release table, abstract, Sections 1, 8.16.6 (note), 8.17, 8.18, 12.8, 13.13, 15.12, 16.0, 17 and Appendix R. v2.2.1 corrections are in the front matter, Sections 8.14.2, 8.14.3, 8.17.5, 12.8, 12.9 (new), 15.9, the references of Section 15, 16.0, 16.0S (new), 17 and Appendix S (new); Appendix S.4 lists every change. Older verification narratives describe their original sessions.

## 2. Model, preparation and geometry

### 2.1 The neutral regularized interaction

Let $z_a\in\{-1,1\}$, $a=0,\ldots,R$, be declared QND labels, with $a=0$ the source. Let $x_a\in\mathbb R$ and $p_a=-i\partial_{x_a}$. All displacement axes are the same spatial unit vector $e_z$. Put

$$
u_a=x_a+\lambda_a z_a,\qquad d_{ab}=r_b-r_a,
$$

Here $u_a$ is the shifted coordinate. Define

$$
f_c(r)=\frac{\operatorname{erf}(r/c)}r
 =\frac{2}{\sqrt\pi}\int_0^{1/c}e^{-t^2r^2}\,dt,
\qquad f_c(0)=\frac{2}{\sqrt\pi c},
\qquad \phi_{ab}(s)=f_c(|d_{ab}+se_z|). \tag{2.1}
$$

The four-charge neutral pair interaction is

$$
V_{ab}(u_a,u_b)
=g\{\phi_{ab}(u_b-u_a)-\phi_{ab}(-u_a)-\phi_{ab}(u_b)+\phi_{ab}(0)\}
=-g\int_0^{u_a}\!du\int_0^{u_b}\!dv\,\phi_{ab}''(v-u). \tag{2.2}
$$

Writing $V=\sum_{a<b}V_{ab}$ and $\Lambda=\operatorname{diag}(\lambda_a)$, the branch Hamiltonian is

$$
H_{\rm MC}(z)=H_0+V(x+\Lambda z),\qquad
H_0=\frac{|p|^2}2+\frac{\Omega^2|x|^2}2. \tag{2.3}
$$

The interaction is smooth and bounded for fixed $N,c>0$. Hence $H_{\rm MC}(z)$ is self-adjoint on $D(H_0)$ and has compact resolvent. This concrete bounded-perturbation argument is the domain justification. A generic assertion that a residual has quadratic growth would not suffice to establish self-adjointness on $D(H_A)$.

The Gaussian profile can be represented by a classical Coulomb convolution of two densities $\rho_\sigma(r)=(\pi\sigma^2)^{-3/2}e^{-|r|^2/\sigma^2}$, with $\sigma=c/\sqrt2$. This identifies a possible profile for (2.1), not a quantum carrier, action or preparation mechanism. The main theorem fixes $c>0$; it does not take a point-charge or radiation-field limit.

### 2.2 Two different quadratic objects

For $a\ne b$, define

$$
K_{ab}=\frac{1-3(d_{ab}\cdot e_z)^2/|d_{ab}|^2}{|d_{ab}|^3},
\qquad K^{(c)}_{ab}=-\phi_{ab}''(0),
\qquad K_{aa}=K^{(c)}_{aa}=0. \tag{2.4}
$$

The unsmeared dipole Hamiltonian is

$$
H_G(z)=H_0+\frac g2(x+\Lambda z)^TK(x+\Lambda z).
$$

Its exact square completion uses $A_G=\Omega^2I+gK$, $F_G=gK\Lambda$ and

$$
C_G=g\Lambda K\Lambda-F_G^TA_G^{-1}F_G.
$$

The regularized reference used for the main Coulomb proof is instead

$$
A=\Omega^2I+gK^{(c)},\qquad
H_A=\frac{|p|^2}2+\frac{x^TAx}2,
\qquad E_A=\tfrac12\operatorname{tr}\sqrt A. \tag{2.5}
$$

These matrices must not be interchanged. Write $\Phi$ for the positive normalized ground state of $H_A$ and

$$
\Sigma=\mathbb E_\Phi[XX^T]=\tfrac12A^{-1/2},\qquad
Q=I-|\Phi\rangle\langle\Phi|,\qquad
\mathcal R=(H_A-E_A)^{-1}Q. \tag{2.6}
$$

The symbol $R$ always counts memories; $\mathcal R$ is the reduced resolvent. The quadratic model $H_G$ is exactly solvable and is used in Section 13.3 (Theorem Q) as a comparison model with its own common preparation $\Phi_G$, the ground state of $\tfrac12|p|^2+\tfrac12x^TA_Gx$.

### 2.3 The S9 family

Let $n=\lceil R^{1/3}\rceil$. Take the first $R$ sites of the cubic grid $\{0,\ldots,n-1\}^3$ in lexicographic order of $(i,j,k)$, with $k$, the $e_z$ index, varying fastest. Subtract $(n-1)/2$ in every coordinate, multiply by $a$, and translate by $Le_z$, where the source is at the origin and

$$
L=20an,\quad \lambda_0=\frac a{1000},\quad
\chi_{\rm design}=5\times10^{-7},\quad
\lambda_e=\lambda_0\frac{\chi_{\rm design}}{n^3}
=\frac{5\times10^{-10}a}{n^3},\quad c=\frac a{20}. \tag{2.7}
$$

Every memory uses $\lambda_j=\lambda_e$. Set

$$
t_* =\frac{\pi L^3}{8g\lambda_0\lambda_e}
=\frac{2\pi\,10^{15}a}{g}n^6,\qquad
T=1.01t_*,\qquad I_R=[.99t_*,1.01t_*]. \tag{2.8}
$$

Then $r_{0j}\ge19.5an$. With $\eta=1/40$, define

$$
f_- =\frac{1+2\eta}{(1+2\eta+3\eta^2)^{5/2}}>\frac{37}{40},
\qquad f_+=(1-\eta)^{-3}<1.079.
$$

The dipole signal has negative sign and satisfies

$$
\frac{2f_-}{L^3}\le |K_{0j}|\le\frac{2f_+}{L^3}. \tag{2.9}
$$

For every $R\ge2$, $n\ge2$ and

$$
n^3\le4R,
\quad 4[(n-1)^3+1]-n^3=3n(n-2)^2\ge0. \tag{2.10}
$$

Two geometric facts about the transverse structure are used by Theorem L. Every site of the array lies on a *column* (a line parallel to $e_z$); a column contains at most $n$ memories. Because the $e_z$ index varies fastest, every column of the memory set is an interval that begins at the layer nearest the source, and at most one column is partial; Theorem DF uses this. Two sites on different columns have transverse separation $|d_{ab}^\perp|\ge a$ (memories) or $|d_{ab}^\perp|\ge a/\sqrt2$ (a memory and the source, $n$ even); the source is collinear with the central column exactly when $n$ is odd.

### 2.4 Preparation and the measured quantity

Initialize the memories in $|+x\rangle^{\otimes R}$ and the oscillators in the same $\Phi$ for every branch. Fixing a memory $j$, write the other labels as $z'$. Let $\psi_{s,\pm,z'}(t)=e^{-itH_{\rm MC}(s,\pm,z')}\Phi$, and define

$$
\mathcal A_{s,z'}(t)=\langle\psi_{s,-,z'}(t),\psi_{s,+,z'}(t)\rangle,
\qquad
D_j(t)=\frac12\left|\mathbb E_{z'}\mathcal A_{+,z'}(t)-\mathbb E_{z'}\mathcal A_{-,z'}(t)\right|. \tag{2.11}
$$

This is the trace distance between the two conditional single-memory density matrices. It establishes simultaneous individual readability, not a full spectrum-broadcast structure or a derived measurement instrument. The oscillator state is not secretly replaced by a branch-dependent exact ground state.

The following exact Walsh decomposition of the readout is used repeatedly in Sections 8 and 13. If every echo equals a pure phase, $\mathcal A_{s,z'}=e^{-it\,\Delta_jE(s,z')}$ for some label energy $E$, write $\Delta_jE(s,z')=\alpha(z')+s\beta(z')$ with $\alpha$ the part even in $s$ and $\beta$ the part odd in $s$. Then

$$
D_j(t)=\left|\mathbb E_{z'}\left[e^{-it\alpha(z')}\sin(t\beta(z'))\right]\right|. \tag{2.12}
$$

A $z'$-independent constant in $\alpha$ is a global phase and does not affect $D_j$. Only the $z'$-dependence of $\alpha$ and the value of $\beta$ enter.

## 3. Constants, units and evidence conventions

From this section onward, every explicit numerical certificate uses $a=g=\hbar=m=1$ unless a formula explicitly retains $a,g$. In these units a frequency or gap has dimension length$^{-2}$; for a general length scale use $\widetilde\Delta=a^2\Delta$, $\widetilde L=L/a$ and $\widetilde g=ga$.

| Symbol | Definition or certified bound |
|---|---|
| $b,b',d_*$ | $b=1/8$, $b'=b+\lambda_0=.126$, $d_*=2b'=.252$ |
| $D_2$ | $4/(3\sqrt\pi c^3)=6018.0222\ldots$ for $c=.05$ |
| $C_2,C_3,C_4$ | Dimensionless global derivative coefficients; $C_2=4/(3\sqrt\pi)<.752253$, $C_3<1.102$, $C_4=24/(5\sqrt\pi)<2.709$ |
| $S_3(n)$ | At most $26.41(1+\log n)$ |
| $S_4^U,S_8^U$ | $219.79$, $2355.72$, bounding row sums of $M_3$ and $M_3^2$ |
| $S_5^U,S_6^{\rm lat,U}$ | $845.21$, $41.03$, bounding fourth-derivative rows and the shifted sixth-power memory lattice sum |
| $Z_\perp,Z_\perp^{1/2}$ | Two-dimensional lattice sums $\sum_{m\in\mathbb Z^2\setminus0}\vert m\vert^{-3}<9.04$ and $\sum_{m\in(\mathbb Z+1/2)^2}\vert m\vert^{-3}<16.53$ (Theorem L) |
| $S_K(n)$ | $\max_j\sum_{a\ne j}\vert K_{aj}\vert\le48(1+\log n)+5$ over the array (Lemma 4.3) |
| $\delta_c$ | A bound on $\Vert K^{(c)}-K\Vert$; at most $426e^{-400}/c^3$ |
| $\Delta$ | $\sqrt{\Omega^2-(8+\delta_c)}$, a lower bound on every frequency of $H_A$ |
| $h_N,h'_N,g_0$ | $h_N=3D_2R$ (v1.4), $h'_N=18090\,n$ (Theorem L), $g_0=\sqrt{\Omega^2-\min(h_N,h'_N)}$ |
| $\gamma_p$ | $((p-1)!!)^{1/p}$ for positive even integer $p$ |
| $\sigma,F_4,\kappa$ | Uniform $L^2$ perturbation, $L^4$ perturbation and $L^4$ reduced-resolvent bounds |
| $\sigma_e,F_{4,e},\kappa_e$ | The corresponding bounds for the spatially even component |
| $\mathcal D_j,\mathcal D_{jk}$ | Centered single-flip and mixed-flip $L^2$ bounds, not the readout $D_j(t)$ |
| $G_{\rm loc},m$ | Per-site gradient bound and the row-sum norm of $\vert A/\Delta^2-I\vert$ used by Theorem LOC-2 |
| $H(s),\mathcal E(s),\nu_s,m(s)$ | Shifted Hamiltonian, its ground energy, ground-state measure and mean displacement (Section 8.12); $E_0(z)=\mathcal E(\Lambda z)$ |
| $g_0$ in Section 8.12 | $g_0^2=\Omega^2-h'_N$; every shifted potential has Hessian at least $g_0^2$ |
| $\bar\mu,b_1,P_B$ | $\sup\vert m\vert_\infty\le10^{-6}$; $b_1=1/8-10^{-6}$; $\nu_s(\max_a\vert x_a-m_a\vert>b_1)\le P_B\le2Ne^{-\Delta/65}$ |
| $\Phi_M,\Phi_S,\Psi$ | Memory and source Hessian-row norms and the Hessian-fluctuation norm under $\nu_s$ (Lemma NP-5) |
| $\rho_{\rm NP},\mathcal Q,T_3$ | Source-coefficient relative error, memory-pair excess and three-label derivative bounds (Lemmas NP-6, NP-7) |
| $S_{M2}(n)$ | $\max_a\sum_bM_2(d_{ab})\le4.7793[24(1+\log n)+2.4041]$ (Appendix L) |
| $\widehat M_2,\widehat M_3,\widehat S_2,\widehat h_N,\widehat g_0$ | Saturated pair majorants, hat row sum $\le48.0048\ell_n+438.09$, hat Hessian bound $3\widehat S_2$, and $\widehat g_0^2=\Omega^2-\widehat h_N$ (Section 8.14) |
| $K,\Gamma,\bar M$ | Entrywise Hessian majorant, $\Gamma=(\Omega^2-K)^{-1}$ and $L^2$ majorants of Hessian entries in Lemma SR and Lemmas SC–PC |
| $K$ in Section 8.15, $h_S$ | The dipole kernel (2.4), not the Hessian majorant of Lemma SR; $h_S=K\mathbf 1_S$ with $-7.905\le h_S\le15.663$ on every S9 set (Theorem DF) |
| $w,g_\rho,e_\rho,E_*,\varphi$ | End-point field $w(\rho,H)=H(\rho^2+H^2)^{-3/2}$, $g_\rho(t)=(\rho^2+t^2)^{-1/2}$, midpoint remainder $e_\rho$, $E_*\le2.7104$, and the Poisson bound $\varphi(\tfrac12)<.594$ (Lemmas DF-1, DF-2) |
| $\lambda_1,\lambda_2,C_{\rm src}$ | Relative gradient bounds of the source row, $\lambda_1=.17945$; the constant of Lemma SRC (not explicit) |
| $\varepsilon(\Omega),\nu,\gamma(\Omega)$ | Uniaxial permittivity $1+4\pi\alpha/(1-4\pi\alpha/3)$, $\alpha=g/\Omega^2$; edge exponent root of (8.W1); $\gamma=1-\nu$, $\gamma\Omega^4\to2$ (Proposition W) |
| ${\rm LF}_j,\rho_{\rm tol}$ | Local-field factor $\Omega^2[(\Omega^2+gK)^{-1}\mathbf 1]_j$; admissible relative error of the source coefficient (Section 8.15.4) |
| $y_c,Y,\widehat Y,\ell_*$ | Coincidence threshold, cap and saturation value of the growing comparators, and the switch point $\ell_*=100$ (8.SQ0) |
| $\widehat M_2^Y,\widehat S^Y,S_{\rm env},P_{\rm off}$ | Pointwise core-including majorant, its row sum and envelope (8.SQ1); off-event probability of Lemma SQ-L2 |
| $f'_{\max},D_2$ | $<193.58$ and $4/(3\sqrt\pi c^3)$ by the Hermite bound (Section 8.17.1) |

Several letters are reused locally and declared at each use. Inside Lemma LC-A, $a,e,H,H_e$ denote derivative norms, $r$ a contraction rate, $s$ a covariance norm and $P_t$ a semigroup; in Section 8.12, $m(s)$ is a mean displacement and $B$ a matrix. A displayed interval for an evaluated lattice majorant is not a narrow interval for the actual infinite lattice sum. A computational PASS validates only its stated check. The analytic arguments in this manuscript are not formal proof-assistant objects; the executable ledger has $P=0$.

## 4. Coulomb, lattice and pair-energy estimates

### 4.1 Global control and the quadratic gap: Theorem L

Let $f_{\max}=2/(\sqrt\pi c)$ and $B_N=2g f_{\max}N(N-1)$. Four terms per neutral pair give $\|V\|\le B_N$. Differentiating the Gaussian integral gives $|\phi''|\le D_2$; the maximum of $|f_c''|$ is attained at $r=0$ with value $4/(3\sqrt\pi c^3)$, the second critical value (at $r\approx1.61c$) being below $.235c^{-3}$. Version 1.4 summed the collinear worst case over all $R$ partners of a site,

$$
\|\nabla^2V\|_{\rm op}\le h_N=3gD_2R, \tag{4.1}
$$

and this bound alone forced $\Omega^2\gtrsim R$ through the convexity gap. The geometry of the S9 family does not allow all partners to reach the collinear worst case.

**Theorem L (line-geometry Hessian bound).** In the S9 family with $c=a/20$, for every configuration $x\in\mathbb R^N$ and every label vector $z$,

$$
\|\nabla^2V(x+\Lambda z)\|_{\rm op}\le h'_N:=\frac{3g}{a^3}\Bigl[n\widetilde D_2+(1+10^{-78})(nZ_\perp+2\sqrt2)\Bigr]<\frac{18090\,g}{a^3}\,n,
\qquad \widetilde D_2=\frac{4}{3\sqrt\pi}\Bigl(\frac ac\Bigr)^3=6018.0222\ldots,
\quad Z_\perp=\sum_{m\in\mathbb Z^2\setminus\{0\}}|m|^{-3}<9.04. \tag{4.1L}
$$

Consequently $h_N^{(L)}:=\min\{3gD_2R,\;h'_N\}$ may replace $h_N$ wherever it is used, and $g_0=\sqrt{\Omega^2-h_N^{(L)}}$ is a lower bound for the convexity gap of every branch and of every interpolation member of Section 8.2.

*Proof.* The Hessian of $V$ with respect to $x$ has entries $H_{ab}=-g\phi_{ab}''(u_b-u_a)$ for $a\ne b$ and $H_{aa}=\sum_{b\ne a}g[\phi_{ab}''(u_b-u_a)-\phi_{ab}''(-u_a)]$. Since the matrix is symmetric, its operator norm is at most the maximal absolute row sum, and each row satisfies

$$
|H_{aa}|+\sum_{b\ne a}|H_{ab}|\le 3g\sum_{b\ne a}\sup_{s\in\mathbb R}|\phi_{ab}''(s)|. \tag{4.1a}
$$

Write $d_{ab}=(d_{ab}^\perp,d_{ab}^z)$ with $d_{ab}^\perp\in\mathbb R^2$ the transverse part. *Collinear pairs* ($d_{ab}^\perp=0$): $\phi_{ab}(s)=f_c(|d^z_{ab}+s|)$ and $\sup|\phi_{ab}''|\le D_2$. *Transverse pairs* ($D:=|d_{ab}^\perp|>0$): $\phi_{ab}(s)=F(d^z_{ab}+s)$ with $F(u)=f_c(\sqrt{D^2+u^2})$. For $D\ge a/\sqrt2=10\sqrt2\,c$ the regularization is negligible: $f_c(\rho)=\rho^{-1}-\operatorname{erfc}(\rho/c)/\rho$ and the second term and its first two derivatives are bounded, relative to $\rho^{-3}$, by $(4/\sqrt\pi)(\rho/c)^3e^{-(\rho/c)^2}$, which is below $8.9\times10^{-84}$ at $\rho=10\sqrt2\,c$ (including the lower-order terms $(4/\sqrt\pi)(\rho/c)e^{-(\rho/c)^2}+2\operatorname{erfc}(\rho/c)$ the relative second derivative there is $8.88\times10^{-84}$) and decreases in $\rho$. For the unregularized part, $F_0(u)=(D^2+u^2)^{-1/2}$ has

$$
F_0''(u)=\frac{2u^2-D^2}{(D^2+u^2)^{5/2}},\qquad
\sup_{u\in\mathbb R}|F_0''(u)|=\frac1{D^3},
$$

because with $v=u/D$ the inequality $|2v^2-1|\le(1+v^2)^{5/2}$ is equivalent to $(1+v^2)^5-(2v^2-1)^2=v^{10}+5v^8+10v^6+6v^4+9v^2\ge0$, an exact polynomial identity with nonnegative coefficients; equality holds only at $u=0$. Hence $\sup|\phi_{ab}''|\le(1+10^{-78})D^{-3}$ for every transverse pair, uniformly in $D\ge a/\sqrt2$.

Counting for a memory row $a$: the collinear partners are the other memories of its column, at most $n-1$, plus the source when $n$ is odd and the column is central, in total at most $n$; each contributes at most $D_2$. The transverse memory partners lie on the other columns, indexed by $m\in\mathbb Z^2\setminus\{0\}$ with $|d^\perp|=a|m|$, at most $n$ per column, contributing at most $n\sum_{m\ne0}(a|m|)^{-3}=nZ_\perp a^{-3}$. The source, when not collinear, has $|d^\perp|\ge a/\sqrt2$ and contributes at most $2\sqrt2a^{-3}$. For the source row: at most $n$ collinear partners (odd $n$) and transverse partners on the columns of the $n\times n$ transverse grid, at most $n\,Z_\perp a^{-3}$ (odd $n$) or $n\,Z_\perp^{1/2}a^{-3}$ (even $n$, half-integer offsets, $Z_\perp^{1/2}<16.53$); both are below the memory-row bound because $D_2\gg Z_\perp^{1/2}a^{-3}$. Multiplying (4.1a) out, retaining the factor $1+10^{-78}$ for transverse pairs, gives (4.1L). The lattice sums are enclosed by exact enumeration of $|m|_\infty\le800$ plus the tail $\sum_{k>800}8k\cdot k^{-3}\le 8/800$, since the $8k$ points with $|m|_\infty=k$ satisfy $|m|\ge k$; the Epstein closed form $4\zeta(3/2)\beta(3/2)=9.0336\ldots$ is a diagnostic. The printed constant follows from $3[6018.03+(1+10^{-78})9.04]n+(1+10^{-78})8.49<18090n$ for $n\ge1$. $\square$

The verifier rows `LINE-HESSIAN-CONSTANTS` and `LINE-HESSIAN-GEOMETRY` certify the constants and check the count against an exact enumeration of the S9 geometry for $n\le7$ and for partially filled cubes; for full cubes the brute-force row bound is $18077,\,54211,\,54243,\,90372,\,90407,\,126535$ for $n=2,\ldots,7$, against $h'_N=36180,\ldots,126630$ and $h_N=1.4\times10^5,\ldots,6.2\times10^6$. Only at $R=2$ is the old bound $3D_2R=36108$ smaller than $h'_N=36180$, which is why the certified quantity is the minimum $h_N^{(L)}$. The enumerated quantity is the classification bound evaluated on the actual geometry ($D_2$ for collinear, $D^{-3}$ for transverse pairs), not a numerical supremum over configurations.

*Consequences.* The certificate condition $h_N\le.002\Delta^2$ of (8.27) becomes $18090\,n\le .002\Delta^2$, i.e. $\Delta\ge3008\sqrt n$; along the HP-prime curve $\Delta_R=10^4n^{3/2}$ one has $h'_N/\Delta^2\le 4.5225\times10^{-5}$ for every $n$ (was $1.8054\times10^{-4}$). Along the LC-prime curve $10^4n^{4/3}$ the bound is $5.698\times10^{-5}$, along the NP-G curve $10^4n^{3/5}$ it is $1.575\times10^{-4}$, and along the NP-P1 curve $10^4n^{1/2}$ it is $1.809\times10^{-4}$. In every case the gap fraction $g_0/\Delta\ge\sqrt{1-2\times10^{-4}}$ improves on the printed $.9989$, which is retained. At a fixed $\Delta$ the global convexity gap now holds for every $n\le1.1\times10^{-7}\Delta^2$, i.e. for $\Delta=10^5$ up to $R\approx1.3\times10^9$ instead of $R\approx1.1\times10^3$. Theorem L alone did not change the v1.5 exponent; Theorem LC now removes the third-order extensive-norm obstruction. The v1.4 sentence "the present bound $h_N=O(R)$ imposes a square-root requirement on this particular convexity majorant" is withdrawn as overstated (F24-03): the convexity majorant imposes only $\Omega=O(R^{1/6})$.

The elementary bounded-perturbation gap is $\Omega-2B_N$. The sharper gap used below is $g_0=\sqrt{\Omega^2-h_N^{(L)}}$ when $\Omega^2>h_N^{(L)}$, from strong convexity and the gap comparison detailed in Appendix C.

For separated parallel dipoles,

$$
-\frac8{a^3}I\le K\le\frac{16}{a^3}I. \tag{4.2}
$$

An explicit field-energy argument is in Appendix B; the numerical extreme eigenvalues of $K$ over the full cubes $n\le16$ are $-5.30$ and $9.54$, consistent with (4.2). Gaussian regularization contributes a row-sum correction bounded by a convergent shell series,

$$
\delta_c\le \frac{425}{c^3}\sum_{k\ge0}8^k e^{-4^k(a/c)^2}
\le\frac{426}{c^3}e^{-400}\quad(a/c=20). \tag{4.3}
$$

Consequently

$$
A\ge\Delta^2I,\qquad
\omega_{\max}^2\le\Omega^2+g(16/a^3+\delta_c). \tag{4.4}
$$

**Lemma 4.3 (absolute row sums of the dipole kernel).** Over the S9 array, $S_K(n):=\max_j\sum_{a\ne j}|K_{aj}|\le48(1+\log n)+5$ (units $a=1$). *Proof.* The $24k^2+2$ lattice points with $|m|_\infty=k$ satisfy $|m|\ge k$ and $|K|\le2|m|^{-3}$; hence $\sum_{k=1}^{n-1}(24k^2+2)\cdot2k^{-3}\le48(1+\log n)+4\zeta(3)<48(1+\log n)+5$; the source adds at most $2f_+/L^3$. $\square$ The signed row sums $h_S(j)=\sum_aK_{aj}$ are bounded uniformly on every S9 set, $-7.905\le h_S\le15.663$ (Theorem DF, Section 8.15). The earlier numerical value $\le2.92$ for $n\le16$ holds on full cubes only; partial S9 sets reach $-3.334$ (Appendix P, F29-01). Uniform boundedness does not extend to the second iterate $K^2\mathbf 1$ (Theorem EL).

### 4.2 Exact pairwise energies and the corrected sign

Let $E_{\rm cl}(z)=V(\Lambda z)$. Each summand depends on two binary labels, so its Walsh expansion has degree at most two. The pair coefficient is exactly

$$
\begin{aligned}
J_{ab}
&=-\frac g4\int_{-\lambda_a}^{\lambda_a}\!du
           \int_{-\lambda_b}^{\lambda_b}\!dv\,\phi_{ab}''(v-u)\\
&=+\frac g4\{\phi_{ab}(\lambda_b-\lambda_a)-\phi_{ab}(-\lambda_b-\lambda_a)
-\phi_{ab}(\lambda_b+\lambda_a)+\phi_{ab}(\lambda_a-\lambda_b)\}.
\end{aligned} \tag{4.5}
$$

The plus sign before the four-corner bracket is essential. Let

$$
\overline E(z)=\mathbb E_\Phi V(X+\Lambda z)-\frac g2\mathbb E_\Phi[X^TK^{(c)}X]. \tag{4.6}
$$

This energy is also exactly pairwise. The second term is label-independent. With $Y=X_b-X_a$ and $\mathbb E Y^2\le1/\Delta$, its pair coefficient is

$$
\overline J_{ab}
=-\frac g4\int_{-\lambda_a}^{\lambda_a}\!du
             \int_{-\lambda_b}^{\lambda_b}\!dv\,\mathbb E\phi_{ab}''(Y+v-u)
=+\frac g4\mathbb E[\phi(Y+\lambda_b-\lambda_a)-\phi(Y-\lambda_b-\lambda_a)
-\phi(Y+\lambda_b+\lambda_a)+\phi(Y+\lambda_a-\lambda_b)]. \tag{4.7}
$$

Both frozen and averaged formulas use the same sign convention. Single-register and constant Walsh terms are allowed; they do not spoil the pair readout formula below.

For the S9 source pairs, the frozen/dipole relative error is below $\rho_{47}=.001$. For the Gaussian average,

$$
\left|\frac{\overline J_{0j}}{J_{0j}}-1\right|
\le\frac{15}{\Delta L^2},\qquad \Delta\ge10^4. \tag{4.8}
$$

Here is the tail-sensitive argument. Expand the centered Gaussian expectation of $\phi''(Y+w)$ at $Y=0$, where $|w|\le\lambda_0+\lambda_e$. Split at $|Y|\le r/8-(\lambda_0+\lambda_e)$. Throughout this region $|d+(w+\theta Y)e_z|\ge7r/8$. The fourth derivative is at most $24(1+\Theta_4)/(7r/8)^5$. The linear term has zero full expectation; use a symmetric cutoff and control the complementary pieces with the global derivative bound and the Gaussian tail. After division by the source lower bound in (2.9), the local coefficient is below $14.369/(\Delta L^2)$; the tail fits the remaining margin to 15. The shift $w$ is indispensable in defining the cutoff.

For memory pairs, the same method gives

$$
|\overline J_{jk}|\le\frac{3g\lambda_e^2}{r_{jk}^3}
\quad\hbox{if}\quad \Delta\ge2200. \tag{4.9}
$$

Version 1.4 stated the condition as $\Delta\ge\Delta_{\rm tail}(n):=1750+384\log(1.733n)$, inherited from an earlier derivation that took a union over pairs. The proof below is per pair and needs only $\Delta\ge2200$; the logarithmic $n$-dependence is removed (F24-02). Set $h=r/8-2\lambda_e$; then $h^2/2\ge r^2/129$ for $r\ge1$ in S9. Splitting $\mathbb E|\phi''(Y+w)|$ at this cutoff gives

$$
r^3\mathbb E|\phi''(Y+w)|
\le2.0002(8/7)^3+2(C_2/c^3)r^3e^{-\Delta r^2/129}<3.
$$

Indeed, $r^3e^{-\Delta r^2/129}$ decreases on $r\ge1$ as soon as $\Delta>193.5$; substitution at $r=1$, $C_2<.752253$, $c=.05$, $\Delta=2200$ gives $2.98620<3$ (verifier row `TAIL-DOMAIN`). Multiplying by $g\lambda_e^2$ proves (4.9). A box estimate alone does not justify either full Gaussian expectation.

For an explicit source-tail bound, when $h\ge\sqrt v$,

$$
\mathbb E[Y^2\mathbf1_{|Y|>h}]\le(h\sqrt v+v)e^{-h^2/(2v)}
\le(h+1)e^{-\Delta h^2/2}.
$$

After division by the frozen source signal, its contribution is at most
$C_4L^3(h+1)e^{-\Delta h^2/2}/[4f_-(.999)c^5]$.
The local coefficient is bounded explicitly by

$$
\frac{6(1+4.2\times10^{-90})(8/7)^5}{(.975)^5(37/40)(.999)}<14.369.
$$

At $L\ge40$, $h\ge .975L/8-.001001$ and $\Delta\ge10^4$, the normalized tail decreases with both $L$ and $\Delta$ and is below $10^{-50000}/(\Delta L^2)$. This leaves more than the needed margin to 15.

### 4.3 The pairwise readout budget

For any real pairwise label energy with source–memory coefficients $J_{0j}^{\rm pw}$ and memory coefficients $J_{jk}^{\rm pw}$, the uniform memory preparation gives

$$
D_j^{\rm pw}(t)=|\sin(2tJ_{0j}^{\rm pw})|\prod_{k\ne0,j}|\cos(2tJ_{jk}^{\rm pw})|. \tag{4.10}
$$

The Chebyshev-shell identity $24k^2+2$ and $|m|\ge|m|_\infty$ give

$$
\sum_{m\in\mathbb Z^3\setminus\{0\}}|m|^{-6}
\le24\zeta(4)+2\zeta(6)<29.
$$

Put

$$
\Lambda_3=\frac{1.01^2\pi^2\,20^6\chi_{\rm design}^2\,29}{8},\qquad
\frac94\Lambda_3<.0014. \tag{4.11}
$$

A combined source relative error $\rho$ implies

$$
e_* =\max\{1-.99f_-(1-\rho),\;1.01f_+(1+\rho)-1\},
\qquad
D_j^{\rm pw}\ge\cos(\pi e_*/2)-\frac94\Lambda_3. \tag{4.12}
$$

Relative errors multiply. For the final static route use

$$
\rho=(1+.001)(1+.0001)(1+5\times10^{-6})-1
=.0011051055005<.0011053. \tag{4.13}
$$

Then $e_*<.091$. Subtracting a total dynamical/energy error of $.003$ leaves

$$
D_j(t)\ge\cos(\pi\cdot.091/2)-.0014-.003
>.98540>.98538. \tag{4.14}
$$

The published conclusion keeps the slightly weaker $.98538$ margin.

### 4.4 Force, Hessian and summable local derivatives

Let $G_z=\nabla V(\Lambda z)$. For S9,

$$
\|G_z\|\le A_R:=3g\left(\frac{\lambda_0\sqrt R}{r_{\min}^3}
+\frac{\lambda_e\sqrt R S_3(n)}{a^3}
+\frac{\lambda_e R}{r_{\min}^3}\right),\qquad r_{\min}=19.5an. \tag{4.15}
$$

With $\ell=1+\log n$, a convenient all-$R$ bound is

$$
A_R\le\frac g{a^2}\left[\frac{3\cdot10^{-3}}{19.5^3}n^{-3/2}
+3(5\cdot10^{-10})26.41\ell n^{-3/2}
+\frac{3(5\cdot10^{-10})}{19.5^3}n^{-3}\right]
\le4.45\cdot10^{-7}\frac{g\ell}{a^2n^{3/2}}. \tag{4.16}
$$

The same computation bounds the force on a *single* site: a memory row feels at most $3g(\lambda_0/r_{\min}^3+\lambda_eS_3(n)/a^3)$, the source row at most $3g\lambda_eR/r_{\min}^3$; these per-site quantities enter $G_{\rm loc}$ in Theorem LOC-2.

For $a=g=1$ and all shifted separations in the box, use

$$
M_2(d)=\frac{2.0002}{(d-.252)^3},\qquad
M_3(d)=\frac{6.0006}{(d-.252)^4},\qquad
M_4(d)=\frac{24.0024}{(d-.252)^5}. \tag{4.17}
$$

Uniform row bounds are $\sum M_3\le S_4^U$, $\sum M_3^2\le S_8^U$ and $\sum M_4\le S_5^U$. Let $m_s=6.0006/(19.3n)^4$. The Hessian difference $H_z^{\rm rem}=\nabla^2V(\Lambda z)-gK^{(c)}$ obeys

$$
\begin{aligned}
\|H_z^{\rm rem}\|_F^2\le D_R^2:={}&R(\lambda_e S_4^U+\lambda_0m_s)^2
+(\lambda_e Rm_s)^2+4R\lambda_e^2S_8^U\\
&+2R(\lambda_0+\lambda_e)^2m_s^2.
\end{aligned} \tag{4.18}
$$

This follows from off-diagonal bounds $g(\lambda_a+\lambda_b)M_3(d_{ab})$ and diagonal bounds $\sum_b g\lambda_bM_3(d_{ab})$, squaring each entry before summing. Thus $D_R=O(R^{-1/2})$. Gaussian vector moments require the Frobenius norm for the fluctuating term and the operator/row norm only for a deterministic shift.

### 4.5 Certified lattice majorants

Enumerate the $531440$ nonzero integer points in $[-40,40]^3$, grouping exactly by squared Euclidean distance. For exponent $p>3$, $d=.252$, $u=40.5-d$, a convex-midpoint tail bound is

$$
\sum_{k>40}\frac{24k^2+2}{(k-d)^p}
\le\frac{24}{(p-3)u^{p-3}}+
\frac{48d}{(p-2)u^{p-2}}+
\frac{24d^2+2}{(p-1)u^{p-1}}. \tag{4.19}
$$

Each term of the positive decomposition is convex; summing its midpoint inequality proves (4.19). Source contributions are included explicitly. The current interval computation encloses the **finite partial sum plus a proved tail and source allowance**, denoted $Q_p$:

| Quantity being bounded | Evaluated majorant, rounded upward | Upper constant used in the proof |
|---|---:|---:|
| $\sup_a\sum_b M_3(d_{ab})$ | $Q_4<219.785079$ | $219.79$ |
| $\sup_a\sum_b M_4(d_{ab})$ | $Q_5<845.203887$ | $845.21$ |
| $\sum_{m\ne0}(\vert m\vert-.252)^{-6}$ | $Q_6<41.026777$ | $41.03$ |
| $\sup_a\sum_b M_3(d_{ab})^2$ | $Q_8<2355.710322$ | $2355.72$ |

The actual infinite sums lie between a finite partial sum and the corresponding majorant. They do not lie in the tiny numerical enclosure of $Q_p$ merely because $Q_p$ was evaluated accurately.

### 4.6 Global third and fourth derivatives

Differentiating (2.1) along the displacement direction produces Gaussian Hermite factors. For the third derivative,

$$
h_3(y)=(8y^3-12y)e^{-y^2},\qquad
h_3'(y)e^{y^2}=-4(4y^4-12y^2+3).
$$

Its nonnegative squared critical coordinates are $(3\pm\sqrt6)/2$. Comparing the critical values and the zero limit at infinity gives

$$
\sup_s|\phi'''(s)|\le C_3c^{-4},\qquad
C_3=\frac{\max|h_3|}{2\sqrt\pi}<1.102. \tag{4.20}
$$

For the fourth derivative,

$$
h_4(y)=(16y^4-48y^2+12)e^{-y^2},\qquad
h_4'(y)e^{y^2}=-8y(4y^4-20y^2+15).
$$

The exhaustive critical set is $y=0$ and $y^2=(5\pm\sqrt{10})/2$. The latter absolute values are below 12, whereas $h_4(0)=12$. Thus

$$
\sup_s|\phi''''(s)|\le\frac{24}{5\sqrt\pi}c^{-5}<2.709c^{-5}. \tag{4.21}
$$

These are analytic critical-point arguments with interval comparisons, not grid maxima. The point-Coulomb fourth derivative is bounded by $24/r^5$ using the Legendre polynomial $|P_4|\le1$. The relative regularization tail is at most

$$
\Theta_4(x)\le\frac1{12\sqrt\pi}\int_x^\infty(16u^8+48u^6+12u^4)e^{-u^2}\,du. \tag{4.22}
$$

Starting from $I_0\le e^{-x^2}/(2x)$ and iterating
$I_k=x^{k-1}e^{-x^2}/2+(k-1)I_{k-2}/2$ gives $\Theta_4(14.96)<4.137\times10^{-90}$. Since $(1-.252)/.05=14.96$, (4.17) follows with ample margin. The analogous third-derivative tail gives the factor $1.0001$ in $M_3$.

### 4.7 Full-displacement stability without global convexity

The negative Hessians in Theorem O do not imply that the nonlinear array loses stability at fixed confinement. The following statement applies to the exact interaction (2.2), for arbitrary positions, displacements and finite $N$. It makes no lattice, small-displacement or separation assumption.

**Theorem ST (positive field energy with exact self-energy subtraction).** Let $g,c>0$, $D_2=4/(3\sqrt\pi c^3)$, and $u\in\mathbb R^N$. Then

$$
V(u)=\frac g2\mathcal D(q_u,q_u)
       -g\sum_a\{f_c(0)-f_c(|u_a|)\},\qquad
q_u(r)=\sum_a[\rho_\sigma(r-r_a-u_ae_z)-\rho_\sigma(r-r_a)],
\quad \sigma=c/\sqrt2,                                      \tag{4.ST1}
$$

where $\mathcal D(q,q)=\iint q(r)q(r')/|r-r'|\,dr\,dr'\ge0$. Consequently

$$
V(u)\ge-g\sum_a\min\{f_c(0),D_2u_a^2/2\}
\ge-gNf_c(0),\qquad
V(u)\ge-\frac{gD_2}2|u|^2.                                \tag{4.ST2}
$$

In units $m=\hbar=1$, set $k=gD_2$. If $\Omega^2>k$ and $\alpha=\Omega^2-k$, then for every shift $s$

$$
H(s)\ge\frac{|p|^2}2+
\frac\alpha2\left|x-\frac{k}{\alpha}s\right|^2
-\frac{k\Omega^2}{2\alpha}|s|^2,\qquad
E_0(s)\ge\frac N2\sqrt\alpha-\frac{k\Omega^2}{2\alpha}|s|^2.
                                                               \tag{4.ST3}
$$

*Proof.* The Coulomb convolution of two profiles in Section 2.1 is $f_c$. Expanding $\mathcal D(q_u,q_u)$ gives exactly (2.2) in the cross terms. The self term of dipole $a$ is $2[f_c(0)-f_c(|u_a|)]$. Positivity follows, for example, from the nonnegative Fourier multiplier $4\pi/|\xi|^2$; these smooth neutral Gaussian charge distributions have finite Coulomb energy. Finally

$$
0\le f_c(0)-f_c(r)
=\frac2{\sqrt\pi}\int_0^{1/c}(1-e^{-t^2r^2})\,dt
\le\frac{2r^2}{3\sqrt\pi c^3}=\frac{D_2}2r^2.
$$

This proves (4.ST2). Completing the square in $\Omega^2|x|^2/2-k|x+s|^2/2$ gives (4.ST3), as an operator form inequality. $\square$

The first lower bound is extensive at any fixed $\Omega>0$; the quadratic comparison uses the stronger sufficient condition $\Omega^2>gD_2$, independent of $N$. Neither condition is a lower bound on the spectral gap. Ordering individual eigenvalues against a harmonic oscillator does not order their differences: $A=\operatorname{diag}(0,1)$ and $Q=\operatorname{diag}(1-\epsilon,0)\ge0$ have $\operatorname{gap}(A)=1$ but $\operatorname{gap}(A+Q)=\epsilon$ for $0<\epsilon<1$. Thus ST removes a stability concern without closing the non-convex gap or record problem.

The positive-field method is established prior art (Section 15.8); this full-displacement specialization is an addition to the M73 derivation, not a claim to a new general stability principle. Appendix B retains the different, sharper small-displacement dipole-matrix bound.


## 5. Gaussian analysis and the moving quadratic reference

### 5.1 Residual decomposition

Define

$$
\overline e_z=\mathbb E_\Phi[V(X+\Lambda z)-E_{\rm cl}(z)-G_z\cdot X-\tfrac g2X^TK^{(c)}X],
$$

and

$$
H_Q(z)=H_A+G_z\cdot x+E_{\rm cl}(z)+\overline e_z,\qquad
W_z=H_{\rm MC}(z)-H_Q(z),\qquad \mathbb E_\Phi W_z=0. \tag{5.1}
$$

The label-dependent constant in $H_Q$ is the exact Gaussian pair energy $\overline E(z)=E_{\rm cl}(z)+\overline e_z$. Write $d_z=-A^{-1}G_z$. The exact coherent orbit starting at the undisplaced Gaussian has

$$
x_z(t)=(I-\cos(\sqrt A\,t))d_z,\qquad
\sup_t|x_z(t)|\le\xi_R:=\frac{2A_R}{\Delta^2},\qquad
\sup_t|\dot x_z(t)|\le\frac{\omega_{\max}A_R}{\Delta^2}. \tag{5.2}
$$

Conjugating by the Weyl displacement associated with this orbit, and extracting its scalar phase, reduces the problem to $H_A+W_z(x+x_z(t))$. Let

$$
m_z(t)=\mathbb E_\Phi W_z(X+x_z(t)),\qquad
F_{z,t}(x)=W_z(x+x_z(t))-m_z(t). \tag{5.3}
$$

The mean $m_z(t)$ may depend on all labels because the displacement does. Section 7 controls this phase globally.

### 5.2 Three Gaussian estimates

On $L^2(\mu_0)$, $d\mu_0=\Phi^2dx$, ground-state conjugation gives the real Ornstein–Uhlenbeck operator

$$
\mathcal L=\Phi^{-1}(H_A-E_A)\Phi
=-\tfrac12\Delta_x+(\sqrt A\,x)\cdot\nabla,\qquad
\langle g,\mathcal Lf\rangle_{\mu_0}=\tfrac12\langle\nabla g,\nabla f\rangle_{\mu_0}. \tag{5.4}
$$

The Dirichlet-form identity on the right is used by Theorem LOC-2 and by the identity (8.13b). For centered real $F$ and $A\ge\Delta^2I$,

$$
\|F\|_2\le\frac{\|\,|\nabla F|\,\|_2}{\sqrt{2\Delta}},\qquad
\|F\|_4\le\frac{(\pi/2)\gamma_4}{\sqrt{2\Delta}}\|\,|\nabla F|\,\|_4. \tag{5.5}
$$

The first is Gaussian Poincare; the second is the Gaussian $L^4$ Poincare/Pisier bound after the covariance change of variables. We use the displayed conservative constant, not an asserted optimal constant.

The reduced inverse satisfies

$$
\|\mathcal L^{-1}F\|_4
\le\frac{\log3}{2\Delta}\|F\|_4+\frac1\Delta\|F\|_2. \tag{5.6}
$$

To prove (5.6), use $\mathcal L^{-1}F=\int_0^\infty e^{-t\mathcal L}F\,dt$. On $[0,t_0]$, $t_0=\log3/(2\Delta)$, the semigroup contracts $L^4$. On the remaining interval, factor $e^{-t_0\mathcal L}$, use its $L^2\to L^4$ contraction and the centered $L^2$ decay $e^{-\Delta(t-t_0)}$. Integrating gives (5.6). This proof uses the Gaussian semigroup, not an operator-norm bound on the unbounded multiplication operator $F$.

Finally, for a centered Gaussian vector $X$ of covariance at most $(2\Delta)^{-1}I$, any deterministic $y$ with $|y|\le\xi$, and $p=2,4$,

$$
\|B(X+y)\|_{L^p(\ell^2)}
\le\frac{\gamma_p\|B\|_F}{\sqrt{2\Delta}}+\|B\|_{\rm op}\xi. \tag{5.7}
$$

For $p=4$, expand the Gaussian fourth moment of $|BX|^2$ and bound it by three times the square of its second moment. This proves the Frobenius dependence directly.

### 5.3 Full-space gradient norms

Taylor expansion gives

$$
\nabla W_z(y)=H_z^{\rm rem}y+R_{3,z}(y),\qquad
|R_{3,z,a}(y)|\le\frac g2\sum_{b\ne a}m_{3,ab}(y)
\{(y_b-y_a)^2+y_a^2\}. \tag{5.8}
$$

Inside $\max_a|y_a|\le b$, take $m_{3,ab}\le M_3(d_{ab})$; outside, take $m_{3,ab}\le C_3/c^4$. With $\xi<b$, the Gaussian union bound is

$$
P_\xi:=\Pr(\max_a|X_a+y_a|>b)\le2N\exp[-\Delta(b-\xi)^2]. \tag{5.9}
$$

For $p=2,4$, define

$$
q_p(\xi)=\frac12\left[(\gamma_{2p}\Delta^{-1/2}+2\xi)^2
+(\gamma_{2p}(2\Delta)^{-1/2}+\xi)^2\right],
$$

$$
d_p(\xi)=\left[(gS_4^U q_p(\xi))^p+
\left(\frac{g(N-1)C_3}{c^4}q_{2p}(\xi)\right)^p\sqrt{P_\xi}\right]^{1/p},
$$

$$
B_p(\xi)=\sqrt N\,d_p(\xi)+\frac{\gamma_pD_R}{\sqrt{2\Delta}}+\delta_H\xi. \tag{5.10}
$$

Here $\delta_H\ge\sup_z\|H^{\rm rem}_z\|_{\rm op}$; by (4.18) the choice $\delta_H=D_R$ is admissible, and the historical tables of Appendix H report their own value. Minkowski over sites and pairs, followed by Holder on the exceptional event, proves $\|\,|\nabla W_z(X+y)|\,\|_p\le B_p(\xi)$. The factor $N$ in the tail and the factor $\sqrt N$ in the vector estimate are both retained. At $\xi=0$, $q_p(0)=3\gamma_{2p}^2/(4\Delta)$. The quantity $d_p(\xi)$ is a *per-site* bound: it bounds $\|R_{3,z,a}(X+y)\|_p$ for each fixed $a$, and the factor $\sqrt N$ is the Minkowski sum over sites. Theorem LOC-2 works with the per-site quantity and never forms that sum.

The concrete residual has bounded derivatives plus an explicit polynomial contribution. Consequently the displayed Gaussian moments are finite; approximation by smooth cutoffs justifies the conjugation, differentiation and integration-by-parts steps used below. No whole-space expectation is replaced by a box-only bound.

## 6. Theorem A: the dressed Duhamel state estimate

Consider the centered moving-frame equation with perturbation $F_t$. Let

$$
\sigma(t)=\|F_t\Phi\|_2,\quad F_4(t)=\|F_t\|_{L^4(\mu_0)},\quad
\Gamma'(t)=\|\dot F_t\Phi\|_2,
$$

and let $\chi_t=-\mathcal R F_t\Phi$. The trial vector $\Phi+\chi_t$, after the extracted scalar phase, has residual $i\dot\chi_t-F_t\chi_t$. Duhamel with the exact unitary propagator therefore gives

$$
\eta(t)\le\frac{\sigma(t)+\sigma(0)}\Delta
+\int_0^t\left(\frac{\Gamma'(s)}\Delta+Q_2(s)\right)ds,
\qquad Q_2=\|F_s\mathcal R F_s\Phi\|_2. \tag{6.1}
$$

The two endpoint terms compare the actual initial and final reference vectors with the dressed trial. They cannot be removed by checking only the intermediate dressed vector.

By Holder and (5.6),

$$
Q_2\le F_4\left(\frac{\log3}{2\Delta}F_4+\frac\sigma\Delta\right),
\quad \sigma\le\frac{B_2(\xi_R)}{\sqrt{2\Delta}},
\quad F_4\le\frac{(\pi/2)\gamma_4B_4(\xi_R)}{\sqrt{2\Delta}},
$$

$$
\Gamma'\le\frac{\omega_{\max}A_R}{\Delta^2}B_2(\xi_R). \tag{6.2}
$$

The last estimate uses $\dot F_t=\dot x_z(t)\cdot\nabla W_z(X+x_z(t))$ minus its mean; centering does not increase its $L^2$ norm. Equation (6.1) contains $\Gamma'/\Delta$ exactly once.

Theorem A remains useful because it controls a state-vector approximation in a specified coherent frame. Its usefulness does not require that it outperform a simpler spectral proof of the scalar readout theorem.

## 7. Theorem B: the moving-reference record route

### 7.1 Reference echo and the full phase

Completing the square in $H_Q$ gives a coherent ground-state displacement. Its overlap error is at most $A_R^2/(2\Delta^3)$. The common-preparation echo lemma in Appendix A therefore contributes at most $4A_R^2/\Delta^3$.

The extra scalar energy/phase relative to $\overline E(z)$ consists of the square-completion shift and the moving average in (5.3). The fundamental theorem of calculus and (5.10) yield the global readout-phase budget

$$
\varepsilon_{\rm ph}\le\frac{TA_R^2}{\Delta^2}
+\frac{4TA_RB_2(\xi_R)}{\Delta^2}. \tag{7.1}
$$

This replaces the withdrawn local Walsh classification of a displacement depending on the entire label vector. It also preserves the exact Gaussian source coupling in (4.7).

### 7.2 Finite-$R$ sufficient conditions

Suppose the kernel and Gaussian conditions of Section 4 hold, $\xi_R<b$, and the state, coherent-echo and phase errors together are at most $.003$. One conservative allocation is $2\sup_{t\le T}\eta(t)\le .002$, with the remaining coherent and phase contributions included in a $.001$ allowance. Then (4.14) proves $D_j(t)\ge .98538$ on $I_R$.

The corrected historical all-$R$ moving-reference choice is

$$
\Delta_R=1.37\times10^6n^{9/4}. \tag{7.2}
$$

The v1.3 source reports a corrected state majorant $.00195725575519790870033\ldots$ and phase majorant $8.3869817563\ldots\times10^{-7}$ for its 4845-term envelope. These are retained as historical comparison values, not relabeled as a fresh rerun. The central result does not rely on these numerical values: Section 8 closes its own static certificate with a portable implementation.

### 7.3 P1 preparation

An alternative preparation is the exact ground state of $H_{\rm MC}(0)$, where zero means all displacement controls switched off, not a binary register value. To compare it with $\Phi$, use the convex interpolation and spectral-location proof in Section 8.2. It gives infidelity below $4\sigma_0^2/g_0^2$ when the residual is $\sigma_0<g_0/4$. A residual divided by a gap alone would not establish that the trial vector is near the ground state; it could be near an excited state.

Replacing the common preparation introduces the appropriate trace-distance or vector-distance budget, generally proportional to the square root of the preparation infidelity. It is not free and is not assumed in the numerical HP theorem.

## 8. Theorems S, E2, HP and HP-prime: the static route

### 8.1 Centered branch objects

Let

$$
\mu_z=\langle\Phi,H_{\rm MC}(z)\Phi\rangle=E_A+\overline E(z),
\quad U_z=H_{\rm MC}(z)-H_A-(\mu_z-E_A),\quad \mathbb E U_z=0. \tag{8.1}
$$

Thus $U_z=G_z\cdot x+W_z$. Every $U_z$ is a sum of centered pair terms: $U_z=\sum_{a<b}u_{ab}(z)$ with $u_{ab}(z)=V_{ab}(x_a+\lambda_az_a,x_b+\lambda_bz_b)-gK^{(c)}_{ab}x_ax_b-\mathbb E[\cdots]$, a function of the two coordinates $(x_a,x_b)$ only; this pair structure is the input of Theorem LOC-2. The uniform bounds used in this section are

$$
\sigma=\frac{A_R+B_2(0)}{\sqrt{2\Delta}},\qquad
F_4=\frac{(\pi/2)\gamma_4[A_R+B_4(0)]}{\sqrt{2\Delta}},
\qquad
\kappa=\frac{\log3}{2\Delta}F_4+\frac\sigma\Delta. \tag{8.2}
$$

For each branch put

$$
\chi_z=-\mathcal R U_z\Phi,\quad q_z=\|\chi_z\|^2\le\frac{\sigma^2}{\Delta^2},
\quad e_2(z)=\langle U_z\Phi,\mathcal R U_z\Phi\rangle\in[0,\sigma^2/\Delta],
\quad c_3(z)=\langle\chi_z,U_z\chi_z\rangle. \tag{8.3}
$$

By (5.6), $\|\chi_z/\Phi\|_4\le\kappa$ and $|c_3|\le\sigma\kappa^2$. The refined estimate below replaces only the cubic majorant; it does not assert that $c_3$ vanishes.

### 8.2 Spectral location and Theorem S

Interpolate

$$
H_\theta=H_A+(\mu_z-E_A)+\theta U_z,\qquad0\le\theta\le1. \tag{8.4}
$$

In the S9 regime $h_N^{(L)}$ dominates $g(8+\delta_c)$, so the potential Hessian of every interpolation member is at least $g_0^2I$ with $g_0^2=\Omega^2-h^{(L)}_N$ (Theorem L). Its ground state is simple and its gap is at least $g_0$. Suppose $\sigma<g_0/4$.

At $\theta=0$ the ground energy equals $\mu_z$. It cannot first cross $\mu_z-g_0/2$: at such a crossing every spectral point would be at distance at least $g_0/2$ from $\mu_z$, while the trial residual is $\|\theta U_z\Phi\|\le\sigma<g_0/4$. Spectral continuity and this contradiction give

$$
E_0(z)>\mu_z-g_0/2,\qquad E_1(z)-\mu_z>g_0/2. \tag{8.5}
$$

Projecting the trial residual above the ground state then gives

$$
\varepsilon_z:=1-|\langle\Phi,\Omega_z\rangle|^2
<\frac{4\sigma^2}{g_0^2}, \tag{8.6}
$$

where $\Omega_z$ is the exact ground state. Let $D_j^{E_0}$ denote the phase-only readout constructed from the exact ground energies but the same uniform label preparation. The common-vector echo lemma proves the all-time statement

$$
|D_j(t)-D_j^{E_0}(t)|\le\varepsilon_S:=\frac{32\sigma^2}{g_0^2}. \tag{8.7}
$$

This is Theorem S. It uses the same initial $\Phi$ for every branch; the distinct-preparation lemma has a different error order. The quantity $\varepsilon_S$ is extensive, $\sigma^2=O(N)$: it is the fidelity between the common Gaussian and an $N$-body ground state, and it is the one $R$-dependence of the certificate that no locality argument on energies removes (Theorem N).

### 8.3 Theorem E2: an explicit energy sandwich

Use the normalized trial vector $(\Phi+\chi_z)/\sqrt{1+q_z}$. The cancellation

$$
(H_{\rm MC}-\mu_z)(\Phi+\chi_z)=U_z\chi_z \tag{8.8}
$$

gives Rayleigh value

$$
\eta_z=\mu_z+\frac{-e_2(z)+c_3(z)}{1+q_z}. \tag{8.9}
$$

Suppose $|c_3|\le M\le g_0/4$. Equations (8.5) and (8.9) imply $E_1-\eta_z>g_0/4$. The norm of the trial residual is at most $\|U_z\chi_z\|\le F_4\kappa$. The variational upper bound and Temple lower bound yield

$$
E_0(z)=\mu_z-e_2(z)+r_z,
\qquad
-M-\frac{4F_4^2\kappa^2}{g_0}\le r_z
\le\frac{\sigma^4}{\Delta^3}+M. \tag{8.10}
$$

Define the uniform interval length

$$
\widehat r_{\rm len}=\frac{\sigma^4}{\Delta^3}+2M+\frac{4F_4^2\kappa^2}{g_0}. \tag{8.11}
$$

Only differences of branch remainders enter the echo. Since every $r_z$ belongs to the same interval, replacing $E_0$ by $\mu-e_2$ changes the readout by at most $t\widehat r_{\rm len}$, not a separately guessed pairwise phase. The term $\sigma^4/\Delta^3$ arises from $q_ze_2$, the product of two extensive second-order quantities; its flip is local in the exact energy but not in this bound, which is the origin of the fourth-order pin $4/3$ in Theorem N.

### 8.4 Abstract parity lemma HP-A and Gaussian lemma HP

Let a probability space have a measure-preserving involution $\Pi$. Assume the positive reduced operator $\mathcal L$ commutes with $\Pi$, preserves the real subspace and has a bounded inverse on centered functions in the norms used. Let real centered $U=U_e+U_o$ and

$$
f=-\mathcal L^{-1}U=f_e+f_o,
\qquad U_e=\tfrac12(U+\Pi U),\quad U_o=\tfrac12(U-\Pi U). \tag{8.12}
$$

Odd integrands integrate to zero, so exactly

$$
c_3=\mathbb E[Uf^2]
=\mathbb E\{U_e(f_e^2+f_o^2)+2U_of_ef_o\}. \tag{8.13}
$$

For the Gaussian operator (5.4) the Dirichlet-form identity gives the equivalent gradient form

$$
c_3=-\mathbb E_{\mu_0}\bigl[f\,|\nabla f|^2\bigr]
=-\mathbb E\{f_e(|\nabla f_e|^2+|\nabla f_o|^2)+2f_o\,\nabla f_e\cdot\nabla f_o\}, \tag{8.13b}
$$

since $U=-\mathcal Lf$ and $\mathbb E[(\mathcal Lf)f^2]=\tfrac12\mathbb E[\nabla f\cdot\nabla f^2]$. The gradient form is used in Theorem LC to close the third-order locality obligation.

Because $f_e^2+f_o^2$ is the even projection of $f^2$, its $L^2$ norm is at most $\|f\|_4^2$. Parity projections contract $L^p$. Holder therefore gives

$$
|c_3|\le\sigma_e\kappa^2+2\sigma_o\kappa_e\kappa
\le\sigma_e\kappa^2+2\sigma\kappa_e\kappa=:M_{\rm par}. \tag{8.14}
$$

Here $\sigma_e\ge\|U_e\|_2$, $\kappa_e\ge\|\mathcal L^{-1}U_e\|_4$ and $\sigma_o\le\sigma$. In the oscillator problem $\Pi x=-x$ preserves $\mu_0$ and commutes with $\mathcal L$ for every positive $A$, even when the physical site geometry is not inversion-symmetric. This spatial parity is not a spin flip or a derived physical Z-register symmetry.

A pure odd perturbation has $c_3=0$. A general perturbation does not. Under a standard normal measure, take $U=\operatorname{He}_1+10^{-3}\operatorname{He}_2$, with $\mathcal L\operatorname{He}_k=k\operatorname{He}_k$. Exact rational integration gives

$$
c_3=.004000002,\quad
\mathbb E[U_e(f_e^2+f_o^2)]=.002000002,\quad
2\mathbb E[U_of_ef_o]=.002. \tag{8.15}
$$

The cross term is almost equal to the even term, not twice it. Omitting it gives a false identity and an invalid majorant. Substituting $M=M_{\rm par}$ in (8.10) is Theorem E2-prime.

### 8.5 Lemma HP-G: the even component gains a half power

The even component of the centered perturbation satisfies

$$
\nabla U_{e,z}(x)=\tfrac12[\nabla V(\Lambda z+x)-\nabla V(\Lambda z-x)]-gK^{(c)}x
=H_z^{\rm rem}x+R_{e,z}(x), \tag{8.16}
$$

with

$$
|R_{e,z,a}(x)|\le\frac g6\sum_{b\ne a}m_{4,ab}(x)
\{|x_b-x_a|^3+|x_a|^3\}. \tag{8.17}
$$

The constant force and the quadratic Taylor term cancel in the odd difference of the gradients. Equation (8.17) follows by integrating the Taylor remainder along the straight segment; it requires fourth derivatives, not an unsupported parity cancellation of the whole perturbation.

Let $P=2N e^{-\Delta/64}$, an upper bound on the box complement at zero mean. Define, for $p=2,4$,

$$
q_{3,p}=\frac{\gamma_{3p}^3(1+2^{-3/2})}{6\Delta^{3/2}},
\quad
d_{e,p}=\left[(S_5^U q_{3,p})^p+
\left(\frac{(N-1)C_4}{c^5}q_{3,2p}\right)^p\sqrt P\right]^{1/p}, \tag{8.18}
$$

$$
B_{e,p}=\sqrt N\,d_{e,p}+\frac{\gamma_pD_R}{\sqrt{2\Delta}},\quad
\sigma_e=\frac{B_{e,2}}{\sqrt{2\Delta}},\quad
F_{4,e}=\frac{(\pi/2)\gamma_4B_{e,4}}{\sqrt{2\Delta}},\quad
\kappa_e=\frac{\log3}{2\Delta}F_{4,e}+\frac{\sigma_e}{\Delta}. \tag{8.19}
$$

These follow from the same Gaussian moment, Holder and union-tail steps as (5.10), now with cubic coordinate moments and $M_4$. They are full-space estimates. Along the chosen confinement family, the leading nonlinear terms have $\sigma=O(\sqrt N\Delta^{-3/2})$ and $\sigma_e=O(\sqrt N\Delta^{-2})$.

### 8.5b Theorem LC: a parity-local third-order bound

The cubic coefficient can be bounded without taking three extensive function norms. We retain spatial parity and apply Gaussian covariance interpolation to its gradient representation. The resulting estimate is linear in the number of coordinates when the derivative sums are extensive. Gaussian interpolation and Mehler commutation are standard tools; the assertion here is their quantitative combination for the coefficient and the full-space S9 interaction.

**Lemma LC-A (derivative form).** Let $A$ be a real symmetric positive matrix, $A\ge\Delta^2I$, and let $\mu_0=N(0,\Sigma)$ with $\Sigma=\tfrac12A^{-1/2}$. Set $\mathcal L=-\tfrac12\sum_i\partial_i^2+\sqrt A\,x\cdot\nabla$. Let $U$ be real, centered, twice differentiable, with the derivative moments below finite, and put $f=-\mathcal L^{-1}U$. Spatial parity defines $U_e,U_o,f_e,f_o$ as in (8.12). Assume

$$
m:=\|\,|A/\Delta^2-I|\,\|_{\infty}<\frac23,
\qquad r:=1-\frac{m}{2(1-m)}>0. \tag{8.L1}
$$

Absolute values inside the matrix norm are entrywise; the norm is the maximum row sum. Define

$$
G_4=\max_i\|\partial_iU\|_4,\quad G_{e,4}=\max_i\|\partial_iU_e\|_4,
\quad h_2=\frac1N\sum_{j,k}\|\partial_j\partial_kU\|_2,
\quad h_{e,2}=\frac1N\sum_{j,k}\|\partial_j\partial_kU_e\|_2.
$$

Then

$$
|c_3|\le
\frac{N}{2(1-m)r^3\Delta^4}
\left[2G_{e,4}G_4h_2+(G_{e,4}^2+G_4^2)h_{e,2}\right]. \tag{8.L2}
$$

*Proof.* Write $s=\|\,|\Sigma|\,\|_\infty$ and
$a=\max_i\|\partial_if_o\|_4$, $e=\max_i\|\partial_if_e\|_4$,
$H=\sum_{j,k}\|\partial_j\partial_kf_o\|_2$, $H_e=\sum_{j,k}\|\partial_j\partial_kf_e\|_2$.
Both $f_e$ and $f_o$ are centered. Apply Lemma GI to the three covariances in (8.13b), differentiate the products, and use Holder with exponents $(4,4,2)$. The two Gaussian arguments in GI have the same marginal law, so independence of the three differentiated factors is not required. Symmetry of $|\Sigma|$ bounds its column sums by $s$. The first covariance is bounded by $2s(e^2H_e+eaH)$; the covariance containing $2f_o$ is bounded by $2s(a^2H_e+aeH)$. Consequently

$$
|c_3|\le2s\{2eaH+(e^2+a^2)H_e\}. \tag{8.L3}
$$

For clarity, a term in the first bound has the form
$\sum_{i,j,k}|\Sigma_{ij}|\|\partial_if_e\|_4\|\partial_kf_o\|_4\|\partial_j\partial_kf_o\|_2$;
the sum over $i$ costs $s$, leaving the single extensive Hessian sum. This is the step that avoids a third factor $\sqrt N$.

Put $E_t=e^{-t\sqrt A}$ and $P_t=e^{-t\mathcal L}$. Differentiating the Mehler formula once and twice gives

$$
\nabla P_tU=E_tP_t\nabla U,\qquad
\nabla^2P_tU=E_t(P_t\nabla^2U)E_t. \tag{8.L4}
$$

Lemma OU (stated in Section 8.6b and proved in Appendix I, including the pointwise form (8.24c′)) gives $s\le[2\Delta(1-m)]^{-1}$ and $\|\,|E_t|\,\|_\infty\le e^{-r\Delta t}$. Since $P_t$ contracts every $L^p(\mu_0)$, integration in $t$ yields

$$
a\le\frac{G_4}{r\Delta},\qquad e\le\frac{G_{e,4}}{r\Delta},\qquad
H\le\frac{Nh_2}{2r\Delta},\qquad H_e\le\frac{Nh_{e,2}}{2r\Delta}.
$$

For $H$, summing both external indices in (8.L4) costs two row sums of $|E_t|$, hence the integral $1/(2r\Delta)$. The odd projection of each Hessian and the appropriate parity projection of each gradient are contractions; the full $U$ bounds therefore also control $U_o$. Substitution in (8.L3) proves (8.L2). Smooth approximation and dominated convergence extend the calculation from bounded smooth functions to the stated finite-moment class. In the present model all needed derivatives have polynomial growth. $\square$

**Theorem LC (S9 coefficient).** For the complete, untruncated S9 model in units $a=g=1$, for every $R\ge2$ and every label vector, choose
$\Delta=10^4n^{4/3}$, $n=\lceil R^{1/3}\rceil$. Then

$$
\boxed{\displaystyle\sup_z|c_3(z)|\le9\times10^8\,N\Delta^{-7}.} \tag{8.L5}
$$

This is stronger than the v1.5 hypothesis (13.6) on the design curve needed for its application: it has no logarithmic factor. It is a bound on the third perturbative coefficient, not an all-orders convergence or an interacting LPPL theorem.

*Proof and full-space constants.* The quantities $D_R,d_p,d_{e,p}$ retain their definitions from Sections 5 and 8.5. The force at the expansion point satisfies

$$
F_{\rm site}:=\frac{3\lambda_0}{r_{\min}^3}
+3\lambda_e S_3(n)+\frac{3\lambda_eR}{r_{\min}^3}
\ge\max_i|\partial_iU(0)|.
$$

The Frobenius bound $\|H_z^{\rm rem}\|_F\le D_R$ controls every Euclidean row norm. A Gaussian linear form with row $v$ has $L^4$ norm at most $\gamma_4|v|/\sqrt{2\Delta}$. Therefore

$$
G_4\le F_{\rm site}+\frac{\gamma_4D_R}{\sqrt{2\Delta}}+d_4,
\qquad G_{e,4}\le\frac{\gamma_4D_R}{\sqrt{2\Delta}}+d_{e,4}. \tag{8.L6}
$$

Using a replicated maximum absolute Hessian row here would lose the needed even-gradient scaling. The Frobenius estimate already established in (4.18) avoids that loss.

Here are the additional Hessian bounds, with $P=2Ne^{-\Delta/64}$ as before:

$$
\begin{aligned}
h_2&\le D_R+\frac{2+2^{-1/2}}{\sqrt\Delta}
\left[S_4^U+(N-1)\frac{C_3}{c^4}\gamma_4P^{1/4}\right],\\
h_{e,2}&\le D_R+\frac5{4\Delta}
\left[\gamma_4^2S_5^U+(N-1)\frac{C_4}{c^5}\gamma_8^2P^{1/4}\right]. \tag{8.L7}
\end{aligned}
$$

To verify these bounds, subtract $H_z^{\rm rem}$ from the Hessian of $U$. An off-diagonal entry is bounded on the box by $M_3(d_{ab})|X_b-X_a|$; the corresponding diagonal summand is bounded by $M_3(d_{ab})(|X_b-X_a|+|X_a|)$. Since $\operatorname{Var}(X_b-X_a)\le1/\Delta$ and $\operatorname{Var}X_a\le1/(2\Delta)$, summing diagonal and off-diagonal contributions gives $S_4^U(2+2^{-1/2})/\sqrt\Delta$ per row. For the even Hessian, the first Taylor term cancels: replace each difference by one half of $M_4$ times its square. The $L^2$ norm of a squared Gaussian is $\gamma_4^2$ times its variance, giving $\tfrac12(2+\tfrac12)\gamma_4^2S_5^U/\Delta$. On the box complement use global derivatives $C_3/c^4,C_4/c^5$, the $L^4$ moments, and Holder's factor $P^{1/4}$. Finally $\sum_{j,k}|(H_z^{\rm rem})_{jk}|\le N\|H_z^{\rm rem}\|_F\le ND_R$. These steps give (8.L7) without dropping the Gaussian tail or imposing a wall.

Insert the constants of Sections 3 and 5 into (8.L6)–(8.L7). For the $\sqrt P$ in $d_4,d_{e,4}$ use $e^{-y}\le(32/e)^{32}y^{-32}$ with $y=\Delta/128$. For the $P^{1/4}$ in (8.L7) the existing power 16 with $y=\Delta/256$ suffices. Both inequalities follow by maximizing $y^ke^{-y}$ at $y=k$, and both retain $2N\le2(n^3+1)$. The positive monomial envelope of Section 8.9 certifies, for every real $n\ge2$,

| Scaled quantity | Enclosed upper value, rounded upward | Bound used in the proof |
|---|---:|---:|
| $\Delta G_4$ | $527.680$ | $528$ |
| $\Delta^{3/2}G_{e,4}$ | $1925.462$ | $1926$ |
| $\sqrt\Delta\,h_2$ | $594.996$ | $595$ |
| $\Delta h_{e,2}$ | $1829.936$ | $1830$ |
| $m$ | $2.241\times10^{-7}$ | $10^{-6}$ |

In particular $r\ge.999999$ and $\Delta>25000$. The bracket in (8.L2), after multiplication by $\Delta^3$, is at most

$$
2(1926)(528)(595)+\left(528^2+\frac{1926^2}{25000}\right)1830.
$$

Dividing this number by $2(1-10^{-6})(.999999)^3$ gives a value below $9\times10^8$, completing the proof. All powers of $n$ in the scaled envelopes are nonincreasing or have their explicit logarithmic stationary-point bound; no finite-size extrapolation is used. The row `LC-S9-CONSTANTS` evaluates this exact rounded inequality and the five all-$n$ envelopes. $\square$

**Quantifier guard.** Equation (8.L5) is specialized to the stated confinement curve. It must not be read as a $\Delta$-uniform claim at fixed $n$. For one oscillator with $U=\tfrac h2(x^2-1/(2\Delta))$, direct Gaussian integration gives $c_3=h^3/(32\Delta^5)$; a nonzero label-induced quadratic remainder cannot in general obey a constant times $\Delta^{-7}$ for every arbitrarily large $\Delta$. Lemma LC-A remains valid in its full stated domain and retains that quadratic contribution.

The exact correlated two-coordinate checks use $\sqrt A=\left(\begin{smallmatrix}2&1/10\\1/10&2\end{smallmatrix}\right)$, rational Wick moments, and $U=-\mathcal Lf$ for mixed even/odd polynomials. They independently check the sign, parity cross term and normalization of (8.L3); they are finite algebraic checks of the proof mechanism, not replacements for the dimension-independent proof.


### 8.6 Lemma F: flip structure of the second-order energy

Write $\mathcal B(f,g)=\langle f,\mathcal L^{-1}g\rangle_{\mu_0}$ for centered real functions. For a label flip $\Delta_j$, let

$$
\mathcal D_j\ge\sup_z\|\Delta_jU_z\|_2,\qquad
\mathcal D_{jk}\ge\sup_z\|\Delta_k\Delta_jU_z\|_2. \tag{8.20}
$$

If $\overline{\Delta_jU}$ denotes the average over the two values of label $k$, and $\overline U$ the average over the four $(j,k)$ corners, polarization gives the exact identity

$$
\Delta_k\Delta_j e_2
=2\mathcal B(\overline{\Delta_jU},\overline{\Delta_kU})
 +2\mathcal B(\overline U,\Delta_k\Delta_jU).
$$

Consequently

$$
\|\Delta_k\Delta_j e_2\|_\infty
\le\frac{2\mathcal D_j\mathcal D_k+2\sigma\mathcal D_{jk}}\Delta. \tag{8.21}
$$

Averaging cannot increase the uniform $L^2$ bounds, and $\|\mathcal L^{-1}\|_{2\to2}\le1/\Delta$ proves the inequality. Note that $\Delta_k\Delta_jU_z=\Delta_k\Delta_ju_{jk}$ is a function of the two coordinates $(x_j,x_k)$ alone, because only the pair $(j,k)$ depends on both labels, whereas $\overline U$ is a sum over all pairs. The factor $\sigma=\|\overline U\|_2=O(\sqrt N)$ in (8.21) is therefore a pairing of a local function with an extensive one; Theorem LOC-2 replaces it by a per-site quantity.

For a concrete bound, set

$$
\omega_a^{(p)}=(\gamma_p/\sqrt{2\Delta}+\lambda_a)(\gamma_p/\sqrt{2\Delta})
+\lambda_j(\gamma_p/\sqrt{2\Delta}+\lambda_a)
+\tfrac12(\gamma_p/\sqrt{2\Delta}+\lambda_a)^2.
$$

Taylor expansion of the neutral force, followed by the same box/tail split, gives

$$
\mathcal D_j\le2g\lambda_j\left[
\frac{\|K^{(c)}_{j,\cdot}\|_2}{\sqrt{2\Delta}}
+\sum_{a\ne j}\left(M_3(d_{aj})\omega_a^{(4)}+
\frac{C_3}{c^4}P^{1/4}\omega_a^{(8)}\right)\right], \tag{8.22}
$$

$$
\mathcal D_{jk}\le4g\lambda_j\lambda_k
\left[M_2(d_{jk})+\frac{C_2}{c^3}\sqrt P\right]. \tag{8.23}
$$

To see (8.22) directly, integrate the force over the flip interval and use
$\phi'(y-u)-\phi'(y)+u\phi''(0)=-u[\phi''(y)-\phi''(0)]+u^2\phi'''(\xi_1)/2$.
The linear term after Gaussian centering is $2\lambda_jg\sum_aK^{(c)}_{aj}X_a$.
The remainder is bounded by $2\lambda_jg m_3[|u_a|(|X_j|+\lambda_j)+u_a^2/2]$.
Holder with fourth moments controls the box term; eighth moments and $P^{1/4}$ control its complement. The mixed flip is the centered integral of $-g\phi''$ over the two flip intervals; the same split yields (8.23). Differentiating once more under the flip integrals gives the gradient bounds used by Theorem LOC-2,

$$
\|\partial_j\Delta_k\Delta_jU_z\|_2,\ \|\partial_k\Delta_k\Delta_jU_z\|_2
\le4g\lambda_j\lambda_k\left[M_3(d_{jk})+\frac{C_3}{c^4}\sqrt P\right], \tag{8.23b}
$$

with $M_3$ and $C_3/c^4$ in place of $M_2$ and $C_2/c^3$. For a memory row, $\|K^{(c)}_{j,\cdot}\|_2\le2\sqrt{30}$; for the source row it is at most $(2\cdot1.079/8000)n^{-3/2}$. The memory sum of $M_2^2$ is bounded using **$4.00080004 S_6^{\rm lat,U}$**, because $4(1+10^{-4})^2=4.00080004$. The smaller number $4.0008$ is inadmissible.

### 8.6b Theorem LOC-2: locality of the second-order cross terms

Two standard Gaussian facts, proved in Appendix I, are combined.

**Lemma GI (Gaussian covariance interpolation).** Let $X\sim N(0,\Sigma)$ on $\mathbb R^N$, let $Y$ be an independent copy and $X_t=tX+\sqrt{1-t^2}\,Y$. For $F,G\in C^1$ of polynomial growth,

$$
\operatorname{Cov}(F(X),G(X))=\int_0^1\mathbb E\bigl[\nabla F(X)^T\Sigma\,\nabla G(X_t)\bigr]dt,
\qquad
|\operatorname{Cov}(F,G)|\le\sum_{a,c}|\Sigma_{ac}|\,\|\partial_aF\|_2\|\partial_cG\|_2. \tag{8.24a}
$$

**Lemma OU (gradient commutation and locality of $\mathcal L^{-1}$).** With $\mathcal L$ as in (5.4) and $\mu_0=N(0,\tfrac12A^{-1/2})$, the Mehler formula $(e^{-t\mathcal L}F)(x)=\mathbb E[F(e^{-t\sqrt A}x+G_t)]$ holds with $G_t$ a centered Gaussian, and

$$
\partial_c\,e^{-t\mathcal L}F=\sum_b(e^{-t\sqrt A})_{bc}\,e^{-t\mathcal L}\partial_bF,
\qquad
\|\partial_c\mathcal L^{-1}F\|_2\le\sum_bW_{bc}\|\partial_bF\|_2,
\quad W:=\int_0^\infty|e^{-t\sqrt A}|\,dt, \tag{8.24b}
$$

for centered $F$, where $|\cdot|$ is the entrywise absolute value. Write $A=\Delta^2(I+M)$ with $M\ge0$ and let $m:=\max_a\sum_b|M_{ab}|$. If $m<2/3$ then, entrywise and in the row-sum norm $\|\cdot\|_{\infty\to\infty}$,

$$
|\Sigma|\le\frac{(I-|M|)^{-1}}{2\Delta},\quad
W\le\frac{(I-\widetilde M)^{-1}}{\Delta},\quad
\widetilde M:=\tfrac12|M|(I-|M|)^{-1},\qquad
\|\,|\Sigma|\,\|\,\|W\|\le\frac{1}{2\Delta^2(1-3m/2)}. \tag{8.24c}
$$

Pointwise in time, $|e^{-t\sqrt A}|\le e^{-t\Delta}e^{t\widetilde B}$ entrywise with $\widetilde B=\tfrac\Delta2|M|(I-|M|)^{-1}$, so
$$
\|\,|e^{-t\sqrt A}|\,\|_{\infty\to\infty}\le e^{-r\Delta t},\qquad r=1-\frac{m}{2(1-m)}. \tag{8.24c′}
$$

In the S9 model $M=(8+\delta_c+gK^{(c)})/\Delta^2$, so by Lemma 4.3 (the engine uses the slightly more conservative $(109+48\log n)/\Delta^2$)

$$
m\le\frac{61+48\log n}{\Delta^2},\qquad
\frac1{1-3m/2}\le1+2m\quad(m\le1/6); \tag{8.24d}
$$

**Theorem LOC-2 (bilinear locality).** Let $F=\sum_pF_p$ be a centered sum of pair functions and $G$ a centered function. Then

$$
|\mathcal B(F,G)|=|\operatorname{Cov}(F,\mathcal L^{-1}G)|
\le\sum_{a,b}\|\partial_aF\|_2\,(|\Sigma|W)_{ab}\,\|\partial_bG\|_2
\le\frac{G_F\,\|\nabla G\|_{2,1}}{2\Delta^2(1-3m/2)}, \tag{8.24e}
$$

where $G_F:=\max_a\|\partial_aF\|_2\le\max_a\sum_{p\ni a}\|\partial_aF_p\|_2$ and $\|\nabla G\|_{2,1}:=\sum_b\|\partial_bG\|_2$.

*Proof.* $\mathcal L^{-1}G$ is centered, so $\mathcal B(F,G)$ is a covariance; apply (8.24a), then (8.24b) to $\partial_c\mathcal L^{-1}G$, sum over $c$, and bound $\sum_a\|\partial_aF\|(|\Sigma|W)_{ab}$ by $G_F$ times the column sum of $|\Sigma|W$, which is at most $\|\,|\Sigma|\,\|_{\infty\to\infty}\|W\|_{\infty\to\infty}$ because both matrices are symmetric. The matrix bounds (8.24c) follow from $\Sigma=(2\Delta)^{-1}(I+M)^{-1/2}$, $\sqrt A=\Delta I+B$ with $B=\Delta[(I+M)^{1/2}-I]$, the binomial coefficients $|\binom{-1/2}{k}|\le1$, $|\binom{1/2}{k}|\le\tfrac12$, the entrywise bound $|e^{-tB}|\le e^{t|B|}$ and $\int_0^\infty e^{-t\Delta}e^{t|B|}dt=(\Delta I-|B|)^{-1}$. $\square$

*Comparison with (8.21).* The old bound pairs $\|\overline U\|_2=\sigma=O(\sqrt N)$ with $\|\Delta_k\Delta_jU\|_2$; the new bound pairs the per-site quantity $G_{\rm loc}:=G_{\overline U}$ with the gradient norm of the local double flip. By Poincare, $\|\nabla G\|_{2,1}\approx\sqrt{2\Delta}\|G\|_2$ and $G_{\rm loc}\approx\sqrt{2\Delta}\,\sigma/\sqrt N$, so the ratio of the new to the old bound is $O(N^{-1/2})$ with no loss of a power of $\Delta$. In the S9 model,

$$
G_{\rm loc}\le\frac{3g\lambda_0}{r_{\min}^3}+\frac{3g\lambda_eS_3(n)}{a^3}+\frac{3g\lambda_eR}{r_{\min}^3}
+\frac{(3\lambda_eS_4^U+3\lambda_0m_s)+(\lambda_0+2\lambda_e)Rm_s}{\sqrt{2\Delta}}+d_2(0), \tag{8.24f}
$$

the three groups being the per-site force, the per-site Hessian-difference row and the per-site Taylor remainder of (5.10); at $n=2$, $\Delta=10^4\cdot2^{3/2}$ (HP-prime curve) this gives $G_{\rm loc}\le.0101$ while $\sigma\le1.28\times10^{-4}$.

**Corollary LOC-2 (local replacements).** With $\delta_{0j}:=\Delta_0\Delta_jU_z$ and $\delta_{jk}:=\Delta_k\Delta_jU_z$,

$$
|\mathcal B(\overline U,\delta_{0j})|\le\mathcal B^{\rm loc}_{0j}:=\frac{G_{\rm loc}(1+2m)}{2\Delta^2}\cdot8g\lambda_0\lambda_e\Bigl[m_s+\frac{C_3}{c^4}\sqrt P\Bigr],\qquad
\Bigl(\sum_{k\ne0,j}|\mathcal B(\overline U,\delta_{jk})|^2\Bigr)^{1/2}\le\frac{G_{\rm loc}(1+2m)}{2\Delta^2}\cdot8\sqrt2\,g\lambda_e^2\Bigl[\sqrt{S_8^U}+\sqrt R\,\frac{C_3}{c^4}\sqrt P\Bigr], \tag{8.24g}
$$

by (8.23b) and $\sum_kM_3(d_{jk})^2\le S_8^U$. Substituting into (8.25)–(8.26) below gives $\widehat\eta_j^{\rm loc}$ and $\rho^{e_2,{\rm loc}}$ with the extensive factor removed. The verifier evaluates both: along the HP-prime curve $\Delta=10^4n^{3/2}$, $\rho^{e_2,{\rm loc}}<5.53\times10^{-8}$ (old $6.62\times10^{-8}$), $T\widehat\eta_j^{\rm loc}<2.01\times10^{-9}$ (old $2.52\times10^{-9}$) and $m\le1.78\times10^{-7}$; along the LC-prime curve $10^4n^{4/3}$ the corresponding bounds are $7.043\times10^{-8}$, $2.583\times10^{-9}$ and $m\le2.241\times10^{-7}$; the certificate with the local replacements is $.001283274989$ (row `LOC2-S9-ENVELOPE`). The numerical change is negligible because the dominant terms of $\rho^{e_2}$ and $\widehat\eta_j$ are the star–star pairings, not the $\sigma$ terms (Theorem N); the structural change is that no bulk-extensive factor remains in the second-order Walsh corrections.

**Finite exact model.** Row `LOC2-FINITE-MODEL` evaluates (8.24e) in an exactly computable Gaussian model (a chain of $N$ sites, $A=\Delta^2I+\epsilon K_d$ with $K_{d,ij}=|i-j|^{-3}$, degree-three pair polynomials with $|i-j|^{-4}$ weights, $\mathcal L^{-1}$ computed exactly in the Hermite basis where $\mathcal L=\sum_{ij}(\sqrt A)_{ij}a_i^\dagger a_j$). For $\Delta=6$, $\epsilon=4$ and the nearest-neighbour double flip: the exact $|\mathcal B|$ equals $9.145\times10^{-4}$ for $N=4,8,12$ (also $N\le24$ in the exploratory run), the old bound $\sigma\|\delta\|/\Delta$ grows as $3.0,4.6,5.8\times10^{-3}$ and the LOC-2 bound stays at $1.14,1.27,1.28\times10^{-2}$ with $G$ converging to $.778$. The inequality holds with margin and the $N$-uniformity is exactly what the lemma predicts; the crossover beyond which the local bound is numerically smaller occurs near $N\approx56$ in this deliberately strongly coupled toy ($m\approx.24$–$.26$ in the reported runs), and at $N\approx3$ in the S9 regime where $m\sim10^{-7}$.

*What Theorem LOC-2 does not do.* It does not localize the third-order coefficient or the Temple remainder; there the extensive functions enter quadratically and the single interpolation step is insufficient. Theorem LC (Section 8.5b) supplies that second application of Lemmas GI and OU, through the Dirichlet-form identity (8.13b), and Section 13.4 records the resulting closure of C1.

### 8.7 Lemma ES: local phase control without false pairwise reduction

Since $U_z$ has Walsh degree at most two and $\mathcal L$ is label-independent,

$$
\widehat e_2(S)=\sum_{A\triangle B=S}\mathcal B(\widehat U(A),\widehat U(B)),
\qquad \deg e_2\le4. \tag{8.24}
$$

Degree four can occur: $U=(z_0z_1+z_2z_3)\operatorname{He}_1$ gives $e_2=2+2z_0z_1z_2z_3$. Thus one must not call $e_2$ pairwise.

For a fixed readout memory $j$, split its flip as

$$
\Delta_j e_2(s,z')=2\widehat e_2(\{j\})+2s\widehat e_2(\{0,j\})+\rho_j(s,z'),
\qquad \mathbb E_{z'}\rho_j=0.
$$

Efron–Stein on the independent binary memory labels gives
$\operatorname{Var}f\le\tfrac14\sum_k\mathbb E(\Delta_kf)^2$. Together with (8.21), this yields the uniform bound

$$
\mathbb E|\rho_j|\le\widehat\eta_j:=
\frac{\sqrt R\,\mathcal D_{\rm mem}^2+
\sigma\left(\sum_{k\ne0,j}\mathcal D_{jk}^2\right)^{1/2}}\Delta,
\qquad
\widehat\eta_j^{\rm loc}:=\frac{\sqrt R\,\mathcal D_{\rm mem}^2}\Delta+\Bigl(\sum_{k\ne0,j}(\mathcal B^{\rm loc}_{jk})^2\Bigr)^{1/2}. \tag{8.25}
$$

The source–memory pair correction satisfies

$$
\rho^{e_2}:=\frac{|\widehat e_2(\{0,j\})|}{|\overline J_{0j}|}
\le\frac{\mathcal D_{\rm mem}\mathcal D_0+\sigma\mathcal D_{0j}}
{2\Delta\,\overline J_{\min}},
\qquad
\rho^{e_2,{\rm loc}}\le\frac{\mathcal D_{\rm mem}\mathcal D_0/\Delta+\mathcal B^{\rm loc}_{0j}}{2\overline J_{\min}},
\quad
\overline J_{\min}=\lambda_0\lambda_e\frac{2f_-}{L^3}(.999)(.9999). \tag{8.26}
$$

For this one readout, compare with the pairwise energy

$$
E_j^{\rm ref}(z)=\mu_z-\widehat e_2(\{0,j\})z_0z_j
-\widehat e_2(\{j\})z_j-\widehat e_2(\varnothing).
$$

Then $|D_j^{\mu-e_2}-D_j^{E_j^{\rm ref}}|\le t\widehat\eta_j$. The reference may depend on which memory is being estimated. This does not assert the existence of one global pairwise Hamiltonian replacing $e_2$ for every observable. It suffices for the simultaneous collection of individual inequalities in the theorem. The remaining $R$-dependence of $\rho^{e_2}$ at fixed $\Delta$ sits in the star–star term $\mathcal D_{\rm mem}\mathcal D_0$, more precisely in the coherent source component of $\mathcal D_0$, which scales as $\lambda_0Rm_s\propto n^{-1}$ and produces the pin $p=1$ of Theorem N; The row-sum estimates do not decide whether this is a loss of the majorant or of the quantity (Section 13.5, F25-04). In the convex regime, Lemma NP-6 shows that the exact source coefficient carries no such loss.

### 8.8 Finite-$R$ Theorems E and HP

Assume

$$
\begin{gathered}
h^{(L)}_N\le .002\Delta^2,\quad g_0\ge .9989\Delta,\quad
\sigma<g_0/4,\quad M\le g_0/4,\\
\Delta\ge\max(10^4,2200),\qquad
\rho^{e_2}\le5\times10^{-6},\qquad
15/(\Delta L^2)\le10^{-4},\\
\operatorname{Cert}:=\frac{32\sigma^2}{g_0^2}
+T\left(\frac{\sigma^4}{\Delta^3}+2M+\frac{4F_4^2\kappa^2}{g_0}+\widehat\eta_j\right)\le .003.
\end{gathered} \tag{8.27}
$$

Theorem E takes $M=\sigma\kappa^2$; Theorem HP takes $M=M_{\rm par}$; either $\widehat\eta_j$ or $\widehat\eta_j^{\rm loc}$, and either $\rho^{e_2}$ or $\rho^{e_2,\rm loc}$, may be used. The proof is the triangle inequality combining (8.7), (8.10), (8.25), (8.26) and the pair readout budget (4.14). It proves $D_j(t)\ge .98538$ for every memory throughout $I_R$.

### 8.9 Infinite-domain envelope and Theorem HP-prime

Every nonnegative expression in (8.27) is majorized by a finite sum of monomials

$$
K n^{-p}(1+\log n)^q,\qquad K\ge0,
\quad p,q\in\mathbb Q,\quad q\ge0. \tag{8.28}
$$

Use $R\le n^3$, $N\le n^3+1$, $\sqrt N\le\sqrt{9/8}\,n^{3/2}$, and the printed decimal constants as exact interval inputs. Positive sums and products are expanded and equal exponent pairs combined. Roots use $(\sum a_i)^{1/k}\le\sum a_i^{1/k}$. Gaussian tails are bounded algebraically by

$$
e^{-x}\le(k/e)^k x^{-k},\qquad x>0,\quad k=16. \tag{8.29}
$$

In particular, $\sqrt P\le\sqrt{2N}e^{-\Delta/128}$ and $P^{1/4}\le(2N)^{1/4}e^{-\Delta/256}$ retain the full union factor before (8.29) is applied.

For $p>0$, a monomial in (8.28) attains its maximum on $n\ge2$ at $n=2$ when $p(1+\log2)\ge q$, otherwise at $n=\exp(q/p-1)$. The latter value is $K e^{p-q}(q/p)^q$. A positive term with $p<0$, or $p=0,q>0$, is unbounded; $p=q=0$ is constant. These exact exponent rules prove coverage of all real $n\ge2$, hence all integer $R\ge2$. No finite-$R$ extrapolation or floating-point argmax is used.

**Theorem HP-prime.** In the model and protocol of Section 2, with $a=g=1$, choose

$$
\Delta_R=10^4n^{3/2},\qquad
\Omega_R=\sqrt{10^8n^3+8+\delta_c}. \tag{8.30}
$$

Then every condition in (8.27) holds, and

$$
\Omega_R<20001\sqrt R,\qquad D_j(t)\ge .98538
\quad(R\ge2,\;1\le j\le R,\;t\in I_R). \tag{8.31}
$$

The portable interval envelope gives the following upward-rounded bounds:

| Quantity | Bound valid for all $n\ge2$ | Required bound |
|---|---:|---:|
| $\operatorname{Cert}_{\rm HP}$ | $.001284$ | $.003$ |
| $\varepsilon_S$ | $6.500\times10^{-16}$ | included above |
| $T[\sigma^4/\Delta^3+4F_4^2\kappa^2/g_0]$ | $2.794\times10^{-9}$ | included above |
| $2TM_{\rm par}$ | $.001283271$ | included above |
| $T\widehat\eta_j$ | $2.519\times10^{-9}$ | included above |
| $\rho^{e_2}$ | $6.614\times10^{-8}$ | $5\times10^{-6}$ |
| $4\sigma/g_0$ | $1.803\times10^{-8}$ | $1$ |
| $4M_{\rm par}/g_0$ | $2.237\times10^{-25}$ | $1$ |
| $15/(\Delta L^2)$ | $3.315\times10^{-7}$ | $10^{-4}$ |
| $h'_N/\Delta^2$ (Theorem L) | $4.5225\times10^{-5}$ | $.002$ |
| $h_N/\Delta^2$ (v1.4, superseded) | $.000180541$ | $.002$ |

More precisely, the computed majorant is below $.001283275501$. The single printed bound $.001284$ is the canonical numerical claim. The current engine combines equal monomials and has 461 terms for this certificate; counts from other algebraic representations need not match.

At $n=2$, $\Delta=10000\,2^{3/2}>28284$; the memory-pair tail condition is $\Delta\ge2200$, independent of $n$. Moreover, $\sqrt{1-.002}>.9989$, so the stated gap fraction is conservative, and with Theorem L it is very conservative. Finally, (2.10) and the negligible positive $\delta_c$ imply (8.31) with considerable margin in the additive constant.

A second run with looser input constants $S_5^U=1000$ and $C_4=9$ gives a majorant below $.001877030$, also within budget. Dropping parity in the same $\Delta=10^4n^{3/2}$ envelope produces a positive term proportional to $n^{3/4}$ and fails the infinite-domain test (row `NO-PARITY-CONTROL`). Lowering the exponent to $p=1.49$ with parity retained produces exactly one growing term, the third-order term $2TM_{\rm par}\propto n^{7/100}$, while all other terms remain bounded (row `NO-LOCALITY-CONTROL`). Both are negative controls on the chosen majorant, not lower bounds on the physically necessary confinement.

The exact frequency relation is

$$
\log_{10}\Omega_R=4+\tfrac32\log_{10}n
+\tfrac12\log_{10}\left(1+\frac{8+\delta_c}{10^8n^3}\right). \tag{8.32}
$$

### 8.9b Theorem LC-prime: the improved all-R record certificate

Theorem HP-prime remains valid as a historical comparison. The strongest certificate of v1.6 is the following; Theorems NP-G and NP-P1 are the stronger retained v1.7 results, and Theorem NP-LOG (Section 8.14) is the strongest current P1 result.

**Theorem LC-prime.** In the exact model and protocol of Section 2, in units $\hbar=m=a=g=1$, let

$$
\Delta_R=10^4n^{4/3},\qquad
\Omega_R=\sqrt{10^8n^{8/3}+8+\delta_c},\qquad n=\lceil R^{1/3}\rceil. \tag{8.L8}
$$

Then, for every integer $R\ge2$, every memory $1\le j\le R$ and every $t\in I_R$,

$$
\boxed{\Omega_R<18518\,R^{4/9},\qquad D_j(t)\ge.98538.} \tag{8.L9}
$$

*Proof.* In the energy sandwich (8.10) use $M=M_{\rm lc}:=9\times10^8N\Delta^{-7}$ from Theorem LC. Use Theorem L for $g_0$ and Theorem LOC-2 for the second-order flip bounds. Every other model parameter, common preparation and time window is unchanged. The resulting positive all-$n$ envelope gives:

| Quantity | Upward-rounded uniform bound | Required budget |
|---|---:|---:|
| $\varepsilon_S+T[\sigma^4/\Delta^3+2M_{\rm lc}+4F_4^2\kappa^2/g_0+\widehat\eta_j^{\rm loc}]$ | $.001020$ | $.003$ |
| $2TM_{\rm lc}$ | $.001019960$ | included above |
| $T[\sigma^4/\Delta^3+4F_4^2\kappa^2/g_0]$ | $8.142\times10^{-9}$ | included above |
| $T\widehat\eta_j^{\rm loc}$ | $2.583\times10^{-9}$ | included above |
| $\varepsilon_S$ | $1.159\times10^{-15}$ | included above |
| $\rho^{e_2,\rm loc}$ | $7.043\times10^{-8}$ | $5\times10^{-6}$ |
| $4\sigma/g_0$ | $2.407\times10^{-8}$ | $1$ |
| $4M_{\rm lc}/g_0$ | $1.996\times10^{-25}$ | $1$ |
| $15/(\Delta L^2)$ | $3.721\times10^{-7}$ | $10^{-4}$ |
| $h_N^{(L)}/\Delta^2$ | $5.698\times10^{-5}$ | $.002$ |

The unrounded total is below $.001019970249$. Thus all conditions of (8.27) hold. The same pair geometry and readout calculation that proves (8.31) gives $D_j\ge.98538$. From $n^3\le4R$, $R\ge2$ and $8+\delta_c<9$,

$$
\frac{\Omega_R^2}{R^{8/9}}
\le10^8\,4^{8/9}+\frac9{2^{8/9}}<18518^2,
$$

which proves the frequency estimate. $\square$

The leading cubic secular term is now $TN/\Delta^7=O(n^{9-7p})$ at $\Delta=Cn^p$. The unchanged quartic sandwich term is $TN^2/\Delta^9=O(n^{12-9p})$ and sets the new sufficient threshold $p=4/3$, or $\Omega=O(R^{4/9})$. Its strictly positive coefficient is why this particular certificate cannot be extended to $p<4/3$ by merely shrinking the cubic constant. This is an obstruction for the displayed majorant, not a physical lower bound. Relative to the v1.5 design, the chosen frequencies satisfy
$\Omega_{\rm LC}/\Omega_{\rm HP}\sim n^{-1/6}\sim R^{-1/18}$ along full cubes. This is an asymptotic resource improvement under the same window and geometry, not a change of model.


### 8.10 Comparison routes and what their exponents mean

The same positive-envelope construction with $M=\sigma\kappa^2$ closes Theorem E at

$$
\Delta_R=1.24\times10^4n^{21/13},\qquad
\operatorname{Cert}_{E}<.002975320, \tag{8.33}
$$

which is rerun in the portable verifier. It yields $\Omega=O(R^{7/13})$. Without retaining $e_2$, the simpler static comparison $|E_0-\mu|\le2\sigma^2/g_0$ gives the sufficient readout budget

$$
\frac{32\sigma^2}{g_0^2}+\frac{2T\sigma^2}{g_0}. \tag{8.34}
$$

Its historical all-$R$ choice is $\Delta=6.67\times10^5n^{9/4}$, with source-reported majorant $.0029473012263\ldots$. This standard spectral route has the same $R^{3/4}$ exponent as the dressed Duhamel route and a smaller reported constant.

| Route | Leading secular majorant | Sufficient exponent in $R$ | Present evidence |
|---|---|---:|---|
| Scalar product-vacuum comparison | Coarse full potential/variance bounds | $4$ | Analytic legacy construction, Section 9 |
| First quadratic Duhamel | $T\sqrt N/\Delta^{3/2}$ | $5/3$ | Analytic legacy construction |
| Dressed Duhamel / first static spectral | $TN/\Delta^4$ | $3/4$ | Proof formulas retained; old optimized constants not freshly rerun |
| Static second order | $TN^{3/2}/\Delta^{13/2}$ | $7/13$ | Current interval rerun of (8.33) |
| Parity-refined static | $TN^{3/2}/\Delta^7$ | $1/2$ | Current interval rerun of (8.30) |
| Parity-local third order (Theorems LC and LC-prime) | $TN/\Delta^7$ then $TN^2/\Delta^9$ | $4/9$ | Complete derivative proof and current all-$n$ interval certificate |
| Non-perturbative convex route, common Gaussian (Theorem NP-G) | preparation fidelity $N\Delta^{-5}$ | $1/5$ | Complete proof (Section 8.12) and all-$n$ interval certificate |
| Non-perturbative convex route, P1 preparation (Theorem NP-P1) | global convexity $h'_N/\Delta^2$ | $1/6$ | Complete proof and all-$n$ interval certificate; optimal order, on full cubes, for arguments requiring global strong convexity (Corollary NP-B) |
| Convexified comparator + RD-V, common comparator ground state (COMP-SQRTLOG) | Source response and variance; full-model transfer is OPEN | $\sqrt{\log R}$ | Comparator theorem only (Section 8.16.5); changed Hamiltonian and preparation |
| Convexified comparison + localization + site-resolved covariance, P1 (Theorem NP-LOG) | $\widehat h_N/\Omega^2$, $r_{\rm SR}$ and $L^{\log}_{\rm pair}$; no growing term | $\log R$ | Complete proof (Section 8.14) and all-$n$ interval certificate; exact non-convex Hamiltonian |
| Exactly solvable quadratic model (Theorem Q) | none | $0$ up to $\log R$ | Exact computation, Section 13.3 |
| Quadratic model, signed first order (Corollary Q-prime) | Neumann radius $gS_K<\Omega_0^2$; numerator uniform (Theorem DF) | $\sqrt{\log R}$ (sufficient; same order as (13.2), coefficient of $\log n$ in $\Omega_0^2$ lowered from about $5.6\times10^5$ to $48$); $R\le10^{2\times10^7}$ at fixed $\Omega_0^2=8\times10^8$ | Complete proof and interval constants (Section 8.15.4); $(\log R)^{1/4}$ necessary if Hypothesis EG holds and transfers to the source row (not proved) |

This is a ladder of sufficient estimates under one resource contract. It is not a hierarchy of lower bounds, research grades or universal limits of standard perturbation theory. With Theorem L, the convexity majorant imposes only $\Omega=O(R^{1/6})$; the square root in the older certificate was imposed by the extensive-norm bound on $c_3$ (Theorem N). Theorem LC removes that loss, and the remaining fourth-order majorant sets $4/9$. Section 8.12 leaves the ladder altogether: its exponents are set by the preparation ($1/5$) and by convexity ($1/6$), not by an order of the anharmonic expansion. Section 8.14 removes the convexity requirement for P1 and reaches $\log R$. Section 8.15 decides the signed-kernel input of the next step order by order; for the quadratic model it moves the logarithm into the Neumann radius and, conditionally on Hypothesis EG and its transfer to the source row, places the necessary law at $(\log R)^{1/4}$. Section 13 distinguishes further possible improvements from proved results.

### 8.11 Standard Feshbach–Schur rederivation

Let $P=|\Phi\rangle\langle\Phi|$, $A_Q=Q(H_A-E_A)Q$, $B_Q=QU_zQ$ and $\delta=E_0-\mu_z$. The compressed inverse

$$
R_E=(A_Q+B_Q-\delta)^{-1}
$$

exists in the form sense in the present gapped regime. If $\varepsilon_z$ is the ground-state infidelity, then for $v\perp\Phi$,
$\langle v,(H-E_0)v\rangle\ge g_0(1-\varepsilon_z)\|v\|^2$. Hence $\|R_E\|\le[(1-\varepsilon_z)g_0]^{-1}$.

The exact Schur equation and one resolvent identity on each side give

$$
\delta(1+q_z)=-e_2+c_3-w_z,\qquad
w_z=\langle(B_Q-\delta)\chi_z,R_E(B_Q-\delta)\chi_z\rangle\ge0. \tag{8.35}
$$

This can also be obtained by eliminating the $Q$ component of the ground-state eigenvector and using $A_Q\chi_z=-QU_z\Phi$. It explains the signs of the second- and third-order terms and the normalization factor $1+q_z$ independently of the Rayleigh computation.

Using $|\delta|\le2\sigma^2/g_0$, the small-overlap bound and Holder yields the conservative estimate

$$
w_z\le\frac{4F_4^2\kappa^2}{g_0}
+\frac{16\sigma^6}{g_0^3\Delta^2}. \tag{8.36}
$$

It reproduces a slightly widened form of the energy sandwich. The cleaner bound (8.10) follows directly from Temple and is the one used in the certificate. The finite-matrix check in the verifier tests the exact identity (8.35), not the entire unbounded-operator proof. The standard Schur route can incorporate the same parity information; it is a strong alternative explanation of the method, not an adversary excluded by restricting attention to bounded perturbations.

### 8.12 A non-perturbative convex-regime route: Theorems NP-G and NP-P1

The certificates of Sections 8.8–8.9b expand the exact branch ground energy around the common Gaussian and place the remainder in one global interval. Each order of that expansion carries its own extensive loss; this is why the ladder of Section 8.10 advanced one order at a time. The readout needs only label flips of the exact energies. This section bounds those flips directly, at all orders in the Coulomb anharmonicity, under a hypothesis that Theorem L makes available: uniform convexity of every branch potential. Theorem O shows that no fixed $\Omega$ can supply that hypothesis on full cubes, so the route has an intrinsic barrier, which Theorem NP-P1 attains.

**Shift family.** For $s\in\mathbb R^N$ put
$$
H(s)=\tfrac12|p|^2+W_s(x),\qquad W_s(x)=\tfrac12\Omega^2|x|^2+V(x+s),\qquad
\mathcal E(s)=\inf\operatorname{spec}H(s). \tag{8.NP0}
$$
The branch Hamiltonians are $H(\Lambda z)$, and $\mathcal E(\Lambda z)=E_0(z)$. Every flip rectangle used below lies in the box $\mathcal S=\prod_a[-\lambda_a,\lambda_a]$. Throughout, $h'_N\le.002\Delta^2$ and
$$
g_0^2:=\Omega^2-h'_N\ge(.9989\Delta)^2 .
$$
The symbol $V_{ab\cdots}$ denotes $\partial_a\partial_b\cdots V(x+s)$, and $F_a:=V_a-\mathbb E_{\nu_s}V_a$.

**Lemma NP-1 (strong log-concavity of every shifted ground state).** For every $s\in\mathbb R^N$, $H(s)$ has a simple ground state $\psi_s>0$, and $\psi_s(x)=e^{-g_0|x|^2/2}\varphi_s(x)$ with $\varphi_s$ log-concave. Hence $\nu_s:=\psi_s^2\,dx=e^{-U_s}dx$ with $\nabla^2U_s\ge2g_0I$.

*Proof.* By Theorem L, $\nabla^2(W_s-\tfrac12g_0^2|x|^2)=(\Omega^2-g_0^2)I+\nabla^2V(x+s)\ge(h'_N-\|\nabla^2V\|_{\rm op})I\ge0$, so $W_s$ is a harmonic potential of frequency $g_0$ plus a convex function. Brascamp and Lieb [BL76, Theorem 6.1] prove that the ground state of a Schrödinger operator with convex potential is log-concave; the harmonic-plus-convex factorization used here follows from the same semigroup argument, which is given in full. Conjugation by $e^{-g_0|x|^2/2}$ maps $H(s)-\tfrac N2g_0$ to $\mathcal L_{g_0}+\widetilde W$ on $L^2(e^{-g_0|x|^2}dx)$, with the Ornstein–Uhlenbeck generator $\mathcal L_{g_0}=-\tfrac12\Delta_x+g_0x\cdot\nabla$ and convex $\widetilde W=W_s-\tfrac12g_0^2|x|^2$. The Mehler semigroup and multiplication by $e^{-t\widetilde W}$ preserve log-concavity by Prékopa's theorem. Trotter–Kato and the positivity-improving property of the semigroup then give the ground state as a limit of log-concave functions. Simplicity follows from positivity improvement; the gap is Lemma NP-2(a). $\square$

**Lemma NP-2 (the Gaussian toolbox under $\nu_s$).** Let $\nu=\nu_s$ and let $\mathbf L=\psi_s^{-1}(H(s)-\mathcal E(s))\psi_s$ act on $L^2(\nu)$, so that $\langle f,\mathbf Lg\rangle_\nu=\tfrac12\mathbb E_\nu[\nabla f\cdot\nabla g]$.

(a) *Brascamp–Lieb.* $\operatorname{Var}_\nu F\le\mathbb E_\nu|\nabla F|^2/(2g_0)$. Consequently the first spectral gap of $H(s)$ is at least $g_0$, and $\|\mathbf L^{-1}F\|_2\le\|F\|_2/g_0$ for centered $F$.

(b) *Caffarelli.* $\nu=T_\#\gamma$ for $\gamma=N(0,(2g_0)^{-1}I)$ and a 1-Lipschitz map $T$. Hence the Gaussian $L^p$ Poincaré bound (5.5) holds with $\Delta$ replaced by $g_0$: $\|F-\mathbb E_\nu F\|_p\le(\pi/2)\gamma_p(2g_0)^{-1/2}\|\,|\nabla F|\,\|_p$. Every 1-Lipschitz $F$ satisfies $\nu(|F-\mathbb E_\nu F|\ge r)\le2e^{-g_0r^2}$.

(c) *Bakry–Émery.* $|\nabla e^{-t\mathbf L}F|\le e^{-g_0t}e^{-t\mathbf L}|\nabla F|$ pointwise. Hence $\|\,|\nabla\mathbf L^{-1}F|\,\|_p\le\|\,|\nabla F|\,\|_p/g_0$ for centered $F$ and every $p\ge1$.

These are standard consequences of $\nabla^2U_s\ge2g_0I$ ([BL76] Theorem 4.1, [Caf00], [BGL14]). Part (c) follows from the synchronous coupling of $dX=-\tfrac12\nabla U_s(X)dt+dB$, which contracts at rate $g_0$. After the replacement $\Delta\to g_0$ the constants coincide with those used for $\mu_0$ in Section 5. The matrix-valued Lemmas GI and OU are *not* transferred; only scalar inequalities are.

**Lemma NP-3 (trap work and the exact response equation).** Let $m(s)=\mathbb E_{\nu_s}[x]$. Then $\mathcal E\in C^\infty(\mathbb R^N)$ and
$$
\partial_b\mathcal E(s)=\mathbb E_{\nu_s}[V_b]=-\Omega^2m_b(s). \tag{8.NP1}
$$
Let $H_m:=\nabla^2V(m+s)$ and let $\rho_b(x):=V_b(x)-\partial_bV(m+s)-\sum_c(H_m)_{bc}(x_c-m_c)$ be the Taylor remainder of the force at the mean. Put $c^{(a)}_b:=\operatorname{Cov}_\nu(\rho_b,\mathbf L^{-1}F_a)$. Then
$$
(\Omega^2I+H_m)\,\partial_am=-\mathbb E_\nu[\nabla V_a]+2c^{(a)},\qquad
\partial_a\partial_b\mathcal E=\bigl[B\,(\mathbb E_\nu\nabla V_a-2c^{(a)})\bigr]_b,\qquad B:=\Omega^2(\Omega^2I+H_m)^{-1}. \tag{8.NP2}
$$
Moreover, with $C_{ab,c}:=\operatorname{Cov}_\nu(V_{ab},\mathbf L^{-1}F_c)$ and $T_{abc}:=\mathbb E_\nu[(\mathbf L^{-1}F_a)F_b(\mathbf L^{-1}F_c)]$,
$$
\partial_a\partial_b\partial_c\mathcal E=\mathbb E_\nu V_{abc}-2(C_{ab,c}+C_{bc,a}+C_{ca,b})+2(T_{abc}+T_{bca}+T_{cab}). \tag{8.NP3}
$$

*Proof.* For fixed $N$, the difference $V(x+s)-V(x+s')$ is a bounded multiplication operator whose $s$-derivatives of every order are bounded. The ground state is isolated by Lemma NP-2(a), so $\mathcal E$ and $\psi_s$ are smooth, with $\partial_a\psi_s=-\mathcal R_sF_a\psi_s$. In the ground-state representation this gives $\partial_a\mathbb E_\nu[G_s]=\mathbb E_\nu[\partial_aG_s]-2\operatorname{Cov}_\nu(G_s,\mathbf L^{-1}F_a)$ for every $G_s$ of polynomial growth. The first equality in (8.NP1) is Hellmann–Feynman. For the second, the ground state is stationary under the generator of translations: $\langle\psi_s,[\partial_b,H(s)]\psi_s\rangle=0$, i.e. $\mathbb E_\nu\partial_bW_s=0$, which reads $\Omega^2m_b+\mathbb E_\nu V_b=0$.

Differentiating this relation in $s_a$ gives $\Omega^2\partial_am_b+\mathbb E_\nu V_{ab}-2\operatorname{Cov}_\nu(V_b,\mathbf L^{-1}F_a)=0$. The constant $\partial_bV(m+s)$ has zero covariance, and $\operatorname{Cov}_\nu(x_c,\mathbf L^{-1}F_a)=-\tfrac12\partial_am_c$. Hence $\operatorname{Cov}_\nu(V_b,\mathbf L^{-1}F_a)=-\tfrac12(H_m\partial_am)_b+c^{(a)}_b$, which is (8.NP2). The matrix $\Omega^2+H_m\ge g_0^2$ is invertible, and $\partial_a\partial_b\mathcal E=-\Omega^2\partial_am_b$.

(8.NP3) is the multi-parameter third-order Rayleigh–Schrödinger formula for $H(s)$, written in the ground-state representation. It follows by differentiating $\partial_a\partial_b\mathcal E=\mathbb E_\nu V_{ab}-2\langle F_a,\mathbf L^{-1}F_b\rangle_\nu$ once more. $\square$

The flip energy of a memory is therefore the work done against the trap by the mean displacement of its own oscillator. Equation (8.NP2) contains every order of the anharmonic interaction. Its only nonlinear input is the covariance vector $c^{(a)}$, and the Brascamp–Lieb inequality controls that vector in $\ell^2$ without any expansion. Row `NP-FINITE-IDENTITIES` is a regression test of the algebra of (8.NP1)–(8.NP3) and of Lemma NP-2(a) in a truncated, weakly anharmonic three-oscillator model; deliberate sign and factor errors in these identities are detected. Its convexity sampling ($\lambda_{\min}$ of the potential Hessian at 343 bulk points) is a consistency check, not a check of global log-concavity.

**Lemma NP-4 (localization of the shifted ground states).** For $s\in\mathcal S$,
$$
\bar\mu:=\sup_{s\in\mathcal S}|m(s)|_\infty\le\frac{(h'_N/3)\bigl(\lambda_0+(2g_0)^{-1/2}\bigr)}{\Omega^2-h'_N/3}, \tag{8.NP4}
$$
which is below $4.2\times10^{-7}<10^{-6}$ on the curves of Theorems NP-G and NP-P1. Put $b_1=1/8-10^{-6}$ and $B_s=\{\max_a|x_a-m_a|\le b_1\}$. On $B_s$ every shifted coordinate satisfies $|x_a+s_a|\le b'$, so the majorants (4.17) apply. Off $B_s$, $\nu_s(B_s^c)\le P_B:=2Ne^{-g_0b_1^2}\le2Ne^{-\Delta/65}$.

*Proof.* From (2.2), $\partial_{u_a}V_{ab}=-g\int_0^{u_b}\phi_{ab}''(v-u_a)dv$, so $|V_a(u)|\le\sum_bg\sup|\phi_{ab}''|\,|u_b|$. The classification in the proof of Theorem L bounds $\sum_bg\sup|\phi''_{ab}|$ by $h'_N/3$. With (8.NP1) and $\mathbb E|x_b-m_b|\le(2g_0)^{-1/2}$ this gives $\Omega^2|m_a|\le(h'_N/3)(\bar\mu+(2g_0)^{-1/2}+\lambda_0)$. The tail bound is Lemma NP-2(b) with a union over the $N$ coordinates, and $.9989\,b_1^2>1/65$. $\square$

**Lemma NP-5 (row, fluctuation and covariance norms).** Let $s\in\mathcal S$, let $j$ be a memory, and take all norms in $L^p(\nu_s)$. Write $\ell_p:=(\pi/2)\gamma_p(2g_0)^{-1/2}$ ($\ell_2=(2g_0)^{-1/2}$ by Lemma NP-2(a)).

- The Hessian row of $j$ satisfies $\Phi_j:=\|\,|\nabla V_j|\,\|_2\le\Phi_M$ with
$$
\Phi_M:=\sqrt{4.00080004\,S_6^{\rm lat,U}}+M_2(r_{\min})+S_4^U(\ell_2+10^{-6}+\lambda_e)+M_3(r_{\min})(\lambda_0+10^{-6})+h'_N\sqrt{P_B}.
$$
The term $M_2(r_{\min})$ bounds the source entry $V_{j0}$ of the row. Its $L^4$ analogue $\Phi_M^{(4)}$ replaces $\ell_2$ by $\ell_4$ and $\sqrt{P_B}$ by $P_B^{1/4}$.
- The source row satisfies $\Phi_0\le\Phi_S:=\sqrt R\,M_2(r_{\min})+RM_3(r_{\min})(\ell_2+10^{-6}+\lambda_e)+h'_N\sqrt{P_B}$, and similarly $\Phi_S^{(4)}$.
- The Hessian fluctuation satisfies
$$
\Psi:=\bigl\|\,\|\nabla^2V(x+s)-H_m\|_{\rm op}\bigr\|_2\le5S_4^U\sqrt{3(1+\log n)/g_0}+2h'_N\sqrt{P_B}. \tag{8.NP5}
$$
- The covariance vector satisfies
$$
\|c^{(j)}\|_{\ell^2}\le\frac{\Phi_j\Psi}{2g_0^2},\qquad |c^{(j)}_0|\le\frac{\|\,|\nabla\rho_0|\,\|_2\,\Phi_j}{2g_0^2}. \tag{8.NP6}
$$
Here $\|\,|\nabla\rho_0|\,\|_2\le\sqrt R\,M_3(r_{\min})g_0^{-1/2}+(\mathbb E|\nabla V_{00}|^2/(2g_0))^{1/2}+R[\tfrac34M_4(r_{\min})g_0^{-1}+(4D_2+2C_3c^{-4})\sqrt{P_B}]+2D_2\sqrt{RP_B}$, and $\mathbb E|\nabla V_{00}|^2\le RM_3(r_{\min})^2+[RM_4(r_{\min})(\ell_2+10^{-6}+\lambda_e)]^2+5R^2(C_3c^{-4})^2P_B$.

*Proof.* On $B_s$ the entries of $\nabla^2V(x+s)$ obey the pair majorants (4.17) at the shifted separations. Off $B_s$ use $\|\nabla^2V\|_{\rm op}\le h'_N$ and the global bounds (4.20)–(4.21).

For (8.NP5): on $B_s$ every absolute row sum of $\nabla^2V(x+s)-H_m$ is at most $5S_4^U\max_a|x_a-m_a|$. By Lemma NP-2(b), $\mathbb E\max_a|x_a-m_a|^2\le(1+\log2N)/g_0\le3(1+\log n)/g_0$.

For the first part of (8.NP6): $\sum_b\operatorname{Cov}(\rho_b,f)^2=\sup_{|w|=1}\operatorname{Cov}(w\cdot\rho,f)^2\le\operatorname{Var}f\,\sup_w\operatorname{Var}(w\cdot\rho)$. Here $\nabla(w\cdot\rho)=(\nabla^2V(x+s)-H_m)w$, so Lemma NP-2(a) gives $\operatorname{Var}(w\cdot\rho)\le\Psi^2/(2g_0)$. Also $\operatorname{Var}(\mathbf L^{-1}F_j)\le\|F_j\|_2^2/g_0^2\le\Phi_j^2/(2g_0^3)$.

The source component is handled row by row. The off-diagonal entries of row $0$ of $\nabla^2V(x+s)-H_m$ are bounded by $M_3(r_{0b})|(x_b-m_b)-(x_0-m_0)|$ on $B_s$. For the diagonal entry, Lemma NP-2(a) is applied to the single function $V_{00}(x)$ itself, and its mean is compared with $V_{00}$ at the mean by a second-order Taylor bound. A triangle inequality over the $R$ partners at this step would cost a factor $\sqrt R$ and make the source coefficient $R$-dependent. $\square$

**Lemma NP-6 (the exact source–memory coefficient).** For $s\in\mathcal S$ and every memory $j$,
$$
|\partial_0\partial_j\mathcal E(s)-\partial_0\partial_jV(s)|\le\rho_{\rm NP}\,|\partial_0\partial_jV(s)|,\qquad
\rho_{\rm NP}:=(r_1+r_2+r_3+r_4)(1+2h_{00})+2h_{00}. \tag{8.NP7}
$$
Here $\kappa_s:=2(37/40)(.999)/L^3\le|\partial_0\partial_jV(s)|$ and $h_{00}:=RM_3(r_{\min})(\lambda_e+10^{-6})/\Omega^2$. The four relative errors are:

- $r_1$, the fluctuation of the direct term, equal to $\kappa_s^{-1}$ times $[6.0006(19.3n)^{-4}\,2\bar\mu+12.0012(17.0625n)^{-5}(g_0^{-1}+4\bar\mu^2)+2(2D_2+1)e^{-\Delta/130}]$;
- $r_2=\|\,|\nabla\rho_0|\,\|_2\Phi_M/(g_0^2\kappa_s)$;
- $r_3=M_2(r_{\min})(1+2h_m/\Omega^2)W_1/(\Omega^2\kappa_s)$;
- $r_4=\sqrt R\,M_2(r_{\min})(1+2h_m/\Omega^2)\Phi_M\Psi/(g_0^2\Omega^2\kappa_s)$.

In $r_3$ and $r_4$, $h_m\ge\|H_m\|_{\infty\to\infty}$ and $W_1\ge\|\mathbb E_\nu\nabla V_j\|_{\ell^1}$ are the explicit logarithmic row sums of Appendix L.

*Proof.* Apply (8.NP2) with $a=j$, $b=0$ and $w=\mathbb E_\nu\nabla V_j-2c^{(j)}$. The identity $B=I-(H_m/\Omega^2)B$ separates the diagonal entry exactly:
$$
\partial_0\partial_j\mathcal E\,\bigl(1+(H_m)_{00}/\Omega^2\bigr)=w_0-\Omega^{-2}\sum_{b\ne0}(H_m)_{0b}(Bw)_b .
$$
The direct part $\mathbb E_\nu V_{0j}=-g\,\mathbb E_\nu\phi''_{0j}(Y+w_{0j})$, with $Y=x_j-x_0$ and $w_{0j}=s_j-s_0$, is compared with $-g\phi''_{0j}(w_{0j})=\partial_0\partial_jV(s)$. The comparison uses a second-order Taylor expansion on $\{|Y-\mathbb EY|\le r/8\}$, where the separations are at least $7r/8$, $|\mathbb EY|\le2\bar\mu$ and $\operatorname{Var}Y\le1/g_0$, together with the concentration tail; this is the argument of (4.8) with a mean shift. This gives $r_1$, and (8.NP6) gives $r_2$.

The classical off-diagonal sum is at most $M_2(r_{\min})\|B\|_{1\to1}\|\mathbb E_\nu\nabla V_j\|_{\ell^1}$, which gives $r_3$. The covariance part is at most $\|(H_m)_{0,\ne0}\|_{\ell^2}\|B\|_{\rm op}\,2\|c^{(j)}\|_{\ell^2}$, which gives $r_4$. Finally, $|\partial_0\partial_jV(s)|\ge\kappa_s$ because the pointwise drift of $\phi''_{0j}$ over $|w_{0j}|\le\lambda_0+\lambda_e$ is below $10^{-4}$ in relative terms (row `NP-TAIL-DOMAIN`). $\square$

**Lemma NP-7 (memory pairs and three-label terms).**

(a) For memories $j\ne k$ and $s\in\mathcal S$, $|\mathbb E_{\nu_s}V_{jk}|\le2.9858\,r_{jk}^{-3}$.

(b) Fix a label vector $z$. Let $s^{(jk)}$ differ from $\Lambda z$ only in coordinates $j,k$, with values in $[-\lambda_e,\lambda_e]$. Then
$$
|\partial_j\partial_k\mathcal E(s^{(jk)})|\le2.9858\,r_{jk}^{-3}+Q_{jk},\qquad
\Bigl(\sum_{k\ne0,j}Q_{jk}^2\Bigr)^{1/2}\le\mathcal Q:=2\|c\|+\frac{h_m(1+2h_m/\Omega^2)(W_2+2\|c\|)}{\Omega^2}+4\lambda_e\sqrt R\,T_3^{\rm rep}. \tag{8.NP8}
$$
Here $\|c\|$ is the bound (8.NP6) and $W_2\ge\|\mathbb E_\nu\nabla V_j\|_{\ell^2}$.

(c) For three distinct labels, $|\partial_a\partial_b\partial_j\mathcal E|\le T_3^{\rm mem}$ when $a,b$ are memories and $\le T_3^{\rm src}$ when $a=0$. For repeated memory indices the bound is $T_3^{\rm rep}$. The explicit expressions are in Appendix L. $T_3^{\rm src}=O(n^{-3/2})$, while $T_3^{\rm mem}$ and $T_3^{\rm rep}$ are bounded uniformly in $n$.

*Proof.* (a) is (4.9) with $\Delta$ replaced by $g_0$, the mean shift absorbed in $h=r/8-2\lambda_e-2\bar\mu$, and Lemma NP-2(b). Since $h^2/2\ge r^2/129.1$ for $r\ge1$, one gets $r^3\mathbb E|\phi''|\le2.0002(8/7)^3+2(C_2/c^3)r^3e^{-g_0r^2/129.1}<2.9858$ (row `NP-TAIL-DOMAIN`).

(b) At the common point $\Lambda z$, (8.NP2) gives $\partial_j\partial_k\mathcal E=\mathbb E V_{jk}-2c_k-(H_mBw)_k/\Omega^2$, and Lemma NP-5 bounds the last two terms in $\ell^2$. The transfer from $\Lambda z$ to $s^{(jk)}$ costs at most $2\lambda_e(|\partial_j^2\partial_k\mathcal E|+|\partial_j\partial_k^2\mathcal E|)\le4\lambda_eT_3^{\rm rep}$. The common point matters: the $\ell^2$ bound holds for one measure, whereas the rectangles for different $k$ lie at different points.

(c) Use (8.NP3). For three distinct labels $\mathbb E_\nu V_{abj}=0$, because $V$ is a sum of pair terms. Lemma NP-2(a) gives $|C_{ab,c}|\le\|\nabla V_{ab}\|_2\Phi_c/(2g_0^2)$. Hölder with exponents $(4,2,4)$ and Lemma NP-2(b,c) give $|T_{abc}|\le K_4\Phi^{(4)}_a\Phi_b\Phi^{(4)}_cg_0^{-7/2}$, $K_4=((\pi/2)\gamma_4)^2/(2\sqrt2)$. Every term that contains the source label carries $\Phi_S$, $\Phi_S^{(4)}$ or $\nabla V_{0k}=O(n^{-4})$. $\square$

**Theorem NP-G (common Gaussian preparation).** Use the exact model, preparation $\Phi$, geometry, window and observable of Section 2, in units $\hbar=m=a=g=1$. Let
$$
\Delta_R=10^4n^{3/5},\qquad\Omega_R=\sqrt{10^8n^{6/5}+8+\delta_c},\qquad n=\lceil R^{1/3}\rceil. \tag{8.NP9}
$$
Then, for every integer $R\ge2$, every memory $j$ and every $t\in I_R$,
$$
\boxed{\Omega_R<13196\,R^{1/5},\qquad D_j(t)\ge.9885.}
$$

**Theorem NP-P1 (switched-off interacting ground-state preparation).** Replace $\Phi$ by the exact ground state $\Psi_0$ of $H_{\rm MC}(0)$, the Hamiltonian with every displacement control switched off (Section 7.3). Keep everything else. Let
$$
\Delta_R=10^4n^{1/2},\qquad \Omega_R=\sqrt{10^8n+8+\delta_c}. \tag{8.NP10}
$$
Then, for every $R\ge2$, every memory and every $t\in I_R$,
$$
\boxed{\Omega_R<12600\,R^{1/6},\qquad D_j(t)\ge.9885.}
$$

*Proof of both theorems.*

*Step 1 (preparation).* For $\Phi$, Theorem S gives $|D_j-D_j^{E_0}|\le\varepsilon_S=32\sigma^2/g_0^2$; its conditions are checked below.

For $\Psi_0$, interpolate $H(0)+\theta(V(x+\Lambda z)-V(x))$. Every member has potential Hessian at least $g_0^2$. At $\theta=0$ the trial vector is the exact ground state. The residual is $\sigma_{\rm P1}=\sup_z\operatorname{Var}_{\nu_0}(V(x+\Lambda z)-V(x))^{1/2}$, and Lemma NP-2(a) and Lemma NP-4 bound it by
$$
\sigma_{\rm P1}^2\le\frac{1}{2g_0}\Bigl[R\bigl(M_2(r_{\min})\lambda_0+(S_{M2}(n)+27.7)\lambda_e\bigr)^2+\bigl(RM_2(r_{\min})\lambda_e+.126\,RM_3(r_{\min})\lambda_0\bigr)^2+h_N'^2(\lambda_0^2+R\lambda_e^2)P_B\Bigr].
$$
The spectral-location argument of Section 8.2 and the common-vector echo lemma then give $|D_j-D_j^{E_0}|\le\varepsilon_{\rm P1}=32\sigma_{\rm P1}^2/g_0^2$.

*Step 2 (exact Walsh reading).* Write $\Delta_jE_0=2\widehat E_0(\{j\})+2s\widehat E_0(\{0,j\})+\sum_k2z_k\widehat E_0(\{j,k\})+\rho_j$ as in (13.1). The pairwise part is read by (4.10). Replacing the phase by its pairwise part changes $D_j^{E_0}$ by at most $T\max_s\mathbb E_{z'}|\rho_j|$.

The Boolean second-order Efron–Stein inequality gives $\mathbb E_{z'}\rho_j^2\le2\sum_{a<b}\sup(\tfrac14\Delta_a\Delta_b\Delta_jE_0)^2$. Each triple flip satisfies $|\tfrac14\Delta_a\Delta_b\Delta_jE_0|\le2\lambda_a\lambda_b\lambda_e\sup_{\mathcal S}|\partial_a\partial_b\partial_j\mathcal E|$. Lemma NP-7(c) then gives
$$
T\max_s\mathbb E_{z'}|\rho_j|\le\sqrt2\,(2T\lambda_e^2)\bigl[\lambda_0\sqrt R\,T_3^{\rm src}+R\lambda_eT_3^{\rm mem}/\sqrt2\bigr]=:H_3.
$$

*Step 3 (pairwise readout).* Integrating (8.NP7) over the four-corner rectangle gives $|\widehat E_0(\{0,j\})-J_{0j}|\le\rho_{\rm NP}|J_{0j}|$. Hence (4.12) applies with $\rho=1.001(1+\rho_{\rm NP})-1$. Lemma NP-7(a,b), Jensen's inequality over the flip rectangles and Minkowski's inequality give
$$
\tfrac12\sum_k(2t\widehat E_0(\{j,k\}))^2\le L_{\rm pair}:=\tfrac12(2T\lambda_e^2)^2\bigl(2.9858\sqrt{29}+\mathcal Q\bigr)^2 .
$$
Here $2T\lambda_e^2=2(1.01)\pi/2000$ exactly, and $L_{\rm pair}$ replaces the allowance $\tfrac94\Lambda_3<.0014$.

*Step 4 (all-$n$ envelope).* Every quantity above is a finite sum of positive monomials $Kn^{-p}(1+\log n)^q$. Gaussian tails use $e^{-y}\le(64/e)^{64}y^{-64}$ with the full union factor $2N$. The exact exponent rules of Section 8.9 give the following upward-rounded bounds, valid for all real $n\ge2$ (rows `NP-G-ALLR`, `NP-P1-ALLR`):

| Quantity | NP-G ($p=3/5$) | NP-P1 ($p=1/2$) | Requirement |
|---|---:|---:|---|
| $\rho_{\rm NP}$ | $1.866\times10^{-6}$ | $2.070\times10^{-6}$ | $\le1.05\times10^{-4}$ |
| $L_{\rm pair}$ | $1.30147\times10^{-3}$ | $1.30147\times10^{-3}$ | $<.0014$ |
| $H_3$ | $1.62\times10^{-16}$ | $1.86\times10^{-16}$ | in $.003$ |
| echo ($\varepsilon_S$ or $\varepsilon_{\rm P1}$) | $1.471\times10^{-14}$ | $1.11\times10^{-25}$ | in $.003$ |
| $4\sigma/g_0$ or $4\sigma_{\rm P1}/g_0$ | $8.58\times10^{-8}$ | $2.36\times10^{-13}$ | $<1$ |
| $\bar\mu$ | $3.55\times10^{-7}$ | $4.20\times10^{-7}$ | $\le10^{-6}$ |
| $h'_N/\Delta^2$ | $1.575\times10^{-4}$ | $1.809\times10^{-4}$ | $\le.002$ |
| $\mathcal Q$ | $1.386\times10^{-5}$ | $1.602\times10^{-5}$ | enters $L_{\rm pair}$ |

With these values, $\rho\le.0010021$ and $e_*<.090883$. Hence
$$
D_j(t)\ge\cos(\pi e_*/2)-L_{\rm pair}-H_3-\varepsilon_{\rm echo}>.98852 .
$$
The frequency bounds follow from $n^3\le4R$ and $8+\delta_c<9$:
$$
\Omega_R^2/R^{2/5}\le10^84^{2/5}+9/2^{2/5}<13196^2,\qquad
\Omega_R^2/R^{1/3}\le10^84^{1/3}+9/2^{1/3}<12600^2 . \qquad\square
$$

**Corollary NP-B (the two barriers of the route are attained).**

(i) Any argument that requires global strong convexity of every branch potential needs $\Omega^2>gD_2n$ on full cubes (Theorem O(2)). It therefore cannot give a confinement of smaller order than $(gD_2)^{1/2}R^{1/6}$. Theorem NP-P1 attains this order.

(ii) For the common Gaussian preparation the echo term of Theorem S is $32\sigma^2/g_0^2\asymp N\Delta^{-5}$ in the displayed majorant. Along $\Delta=10^4n^p$ the displayed envelope with this preparation therefore closes if and only if $p\ge3/5$. For $p>3/5$, every term of the envelope is, at fixed $n\ge2$, a positive combination of nonnegative powers of $\Delta^{-1}$ and of Gaussian tails decreasing in $\Delta$, so it is bounded by its value at $p=3/5$. For $p<3/5$, the echo term grows; row `NP-ROUTE-BARRIERS` exhibits the growing term at $p=1/2$.

(iii) On the domain $p\ge1/2$ of Lemma NP-1, every energy-flip error majorant of the route ($\rho_{\rm NP}$, $\mathcal Q$, $H_3$) is bounded with a wide margin, and the classical pair part $2.9858\sqrt{29}$ of $L_{\rm pair}$ is bounded; the decay exponents at $p=1/2$ are $1/4$ for $\rho_{\rm NP}$ and $1/2$ for $H_3$ (row `NP-EXPONENTS`). Within this route the binding costs are therefore the preparation and convexity, not the anharmonic energy flips. The row also records formal zero-decay points of the displayed majorants ($2/5$ for $\rho_{\rm NP}$, $1/4$ for $H_3$). They are computed with $\bar\mu$ frozen at $10^{-6}$ and lie outside the domain of Lemma NP-1, so they are not thresholds of any valid argument.

These are statements about the route and its majorants, not lower bounds on the confinement that records physically require.

*What the route does not do.* It proves no fixed-$\Omega$ theorem and no optimal exponent beyond the two route statements above. It does not treat arbitrary preparations. It does not derive the P1 preparation physically; the ground state of $H_{\rm MC}(0)$ is a declared input, like $\Phi$. It uses Theorem L's configuration-uniform Hessian bound, so it gives nothing below the convexity threshold; Section 8.14 goes below it for P1 by a different argument. The energy-flip analysis of Lemmas NP-3–NP-7 does not depend on the preparation; only Step 1 does.

### 8.13 Comparing relative evolutions before taking norms

The extensive ground-state-overlap estimate is a sufficient proof device. It need not measure the error of a local echo. The following identities expose the cancellation that a future fixed-confinement proof must retain.

**Lemma ER (relative-evolution Duhamel identity).** For self-adjoint finite matrices $H_\pm=\widetilde H_\pm+W_\pm$, let
$E(t)=e^{itH_-}e^{-itH_+}$ and $\widetilde E(t)=e^{it\widetilde H_-}e^{-it\widetilde H_+}$. For $t\ge0$,

$$
E(t)-\widetilde E(t)=i\int_0^t e^{i(t-s)H_-}
 [W_-\widetilde E(s)-\widetilde E(s)W_+]
 e^{-i(t-s)H_+}\,ds.                                      \tag{8.ER1}
$$

For a unit vector $\phi$, this implies

$$
|\langle\phi,(E-\widetilde E)\phi\rangle|
\le\int_0^t\|[W_-\widetilde E(s)-\widetilde E(s)W_+]
 e^{-i(t-s)H_+}\phi\|\,ds.                               \tag{8.ER2}
$$

*Proof.* Differentiate $e^{i(t-s)H_-}\widetilde E(s)e^{-i(t-s)H_+}$; the endpoints are $E(t)$ and $\widetilde E(t)$ and its derivative is $-i$ times the integrand. Unitarity and Cauchy--Schwarz give (8.ER2). The same argument holds for unbounded operators when a common invariant domain supports this differentiation and the displayed state norm is integrable; otherwise an appropriate limiting argument must first be supplied. $\square$

If $W_-=W_+=W$, the defect is $[W,\widetilde E(s)]$. A perturbation that commutes with the reference relative evolution cancels exactly, irrespective of its size. Replacing this commutator by $2\|W\|$ can destroy the whole advantage. In the S9 comparison with a quadratic reference, some residuals are unbounded. No global operator-norm bound or unproved domain transfer is asserted here; obtaining (8.ER2) on the occupied evolving states with the required $T_R$ dependence is an OPEN obligation.

**Lemma OB (an occupied-band sufficient criterion).** Let $P$ reduce $H_-$, let $\phi$ be a unit vector, and suppose

$$
\epsilon=1-\|P\phi\|^2<1,\qquad
\|(H_+-H_--\delta)P\|\le\kappa,\quad\delta\in\mathbb R. \tag{8.OB1}
$$

For bounded operators, or on a domain where the Duhamel formula below is justified,

$$
|\langle\phi,e^{itH_-}e^{-itH_+}\phi\rangle e^{it\delta}-1|
\le |t|\kappa+2\sqrt\epsilon.                            \tag{8.OB2}
$$

*Proof.* Put $\chi=P\phi/\|P\phi\|$. Since $P$ reduces $H_-$, the Duhamel formula comparing $H_+$ and $H_-+\delta$ on $\chi$ is bounded by $|t|\kappa$. The trace-norm distance between the pure states of $\chi$ and $\phi$ is $2\sqrt\epsilon$, which bounds the change in the expectation of the unitary echo. $\square$

This permits many occupied states and imposes no ground-state-overlap condition. It is a sufficient criterion, not a construction of such a $P$ for S9. In particular, the width must satisfy $T_R\kappa_R\ll1$ in the prescribed growing window. A scalar $\delta_j$ used as a record reference must also have its source dependence and memory-label phase budget checked; choosing phases freely cannot certify a record.

**Proposition SP (spectator cancellation).** Suppose $H_\pm=K_\pm\otimes I+I\otimes B_M$ and $\phi=\phi_A\otimes\chi_M$. Then the echo is exactly

$$
\langle\phi,e^{itH_-}e^{-itH_+}\phi\rangle
=\langle\phi_A,e^{itK_-}e^{-itK_+}\phi_A\rangle,           \tag{8.SP1}
$$

for every $M$ and time. If $B_M$ is a sum of $M$ independent oscillators and each factor of $\chi_M$ is a fixed squeezed Gaussian with squared ground-state overlap $q\in(0,1)$, the global overlap contains $q^M\to0$ while (8.SP1) is unchanged. The proof is tensor factorization of both propagators. This is an exact counterexample to inferring local echo loss from global infidelity alone, including Gaussian preparations. It is not a counterexample to an S9 theorem: S9 does not consist of decoupled spectators. No general obstruction to Gaussian S9 records follows from this example either.


### 8.14 Beyond global convexity: a logarithmic-confinement record theorem (P1 preparation)

Corollary NP-B(i) shows that every argument which needs global strong convexity of the exact branch potentials must pay $\Omega^2>gD_2n$ on full cubes, hence $\Omega\gtrsim R^{1/6}$. This section keeps the exact non-convex Hamiltonians and removes that requirement. Three steps replace it: a convexified comparison potential that coincides with the exact one near the origin (Theorem L-hat), an exponentially accurate comparison of energies, gaps and ground states (Lemmas LOC-A and LOC-B), and a site-resolved covariance inequality for the comparison ground states (Lemma SR). The readout is then assembled with a source coefficient controlled uniformly at every shift (Lemma RD), which removes the extensive Efron–Stein source term. Throughout, units are $\hbar=m=a=g=1$, $c=1/20$, and
$$
\ell_n:=1+\log n,\qquad \Omega_R:=10^4\,\ell_n,\qquad n=\lceil R^{1/3}\rceil. \tag{8.LG0}
$$
All other data (geometry, $\lambda_0$, $\lambda_e$, $L$, window $I_R$, observable $D_j$) are those of Section 2. The preparation is P1: the exact ground state $\Psi_0$ of $H_{\rm MC}(0)$ with the controls switched off. Its existence and simplicity at the frequencies (8.LG0) are part of Lemma LOC-B.

#### 8.14.1 The convexified comparison potential

Let $S:\mathbb R\to[0,1]$ be the standard $C^\infty$ step $S(t)=e^{-1/t}/(e^{-1/t}+e^{-1/(1-t)})$ on $(0,1)$, $S=0$ on $(-\infty,0]$, $S=1$ on $[1,\infty)$; it satisfies $S(t)+S(1-t)=1$. Define the odd $C^\infty$ function
$$
\tau(y)=\operatorname{sgn}(y)\Bigl[\min(|y|,\tfrac25)+\tfrac15\int_0^{(|y|-2/5)_+/(1/5)}\bigl(1-S(t)\bigr)\,dt\Bigr].
$$
Then $\tau(y)=y$ for $|y|\le2/5$, $0\le\tau'\le1$, and $|\tau|\le\tfrac25+\tfrac15\int_0^1(1-S)=\tfrac12$. For every pair put
$$
\psi_{ab}:=\phi_{ab}''\circ\tau,\qquad
\widehat V_{ab}(u_a,u_b):=-g\int_0^{u_a}\!du\int_0^{u_b}\!dv\,\psi_{ab}(v-u),\qquad
\widehat V:=\sum_{a<b}\widehat V_{ab}. \tag{8.LG1}
$$
This is (2.2) with $\phi''_{ab}$ replaced by $\psi_{ab}$. Equivalently $\widehat V_{ab}=g\{\Psi_{ab}(u_b-u_a)-\Psi_{ab}(-u_a)-\Psi_{ab}(u_b)+\Psi_{ab}(0)\}$ with $\Psi_{ab}''=\psi_{ab}$ and $\Psi_{ab}=\phi_{ab}$ on $[-\tfrac25,\tfrac25]$. For $s\in\mathcal S$ define $\widehat H(s)=\tfrac12|p|^2+\tfrac12\Omega^2|x|^2+\widehat V(x+s)$, its ground energy $\widehat{\mathcal E}(s)$, ground state $\widehat\psi_s>0$, measure $\widehat\nu_s=\widehat\psi_s^2dx$ and generator $\widehat{\mathbf L}_s=\widehat\psi_s^{-1}(\widehat H(s)-\widehat{\mathcal E}(s))\widehat\psi_s$.

Put $\widehat M_2(d)=2.0002\,(d-\tfrac12)^{-3}$ and $\widehat M_3(d)=6.0006\,(d-\tfrac12)^{-4}$ for $d\ge1$.

**Theorem L-hat (convexified Hessian).** For every $x\in\mathbb R^N$, $s\in\mathbb R^N$ and every pair,
$$
|\psi_{ab}|\le\widehat M_2(|d_{ab}|),\quad |\psi'_{ab}|\le\widehat M_3(|d_{ab}|),\quad
|\partial_a\partial_b\widehat V|\le\widehat M_2(|d_{ab}|),\quad
\partial_a^2\widehat V\ge-2\sum_{b\ne a}\widehat M_2(|d_{ab}|). \tag{8.LG2}
$$
Consequently $\|\nabla^2\widehat V\|_{\rm op}\le\widehat h_N:=3\widehat S_2(n)$, where on the S9 family
$$
\widehat S_2(n):=\max_a\sum_{b\ne a}\widehat M_2(|d_{ab}|)\le48.0048\,\ell_n+438.09,\qquad
\widehat h_N\le144.015\,\ell_n+1314.3. \tag{8.LG3}
$$
Moreover $\widehat V_{ab}=V_{ab}$ whenever $|u_a|,|u_b|\le\tfrac15$, and $|\widehat V_{ab}|\le\widehat M_2(|d_{ab}|)|u_a||u_b|$ everywhere.

*Proof.* Since $|\tau|\le\tfrac12$ and $|d_{ab}|\ge1$, the argument of $\phi_{ab}''$ in $\psi_{ab}$ is a point at distance $\rho\ge|d_{ab}|-\tfrac12\ge\tfrac12=10c$ from the fixed charge. There the point-Coulomb Legendre bounds $|\partial_z^k\rho^{-1}|\le k!\rho^{-k-1}$ hold, and the Gaussian regularization changes them by a relative amount below $(4/\sqrt\pi)10^5e^{-100}<10^{-38}$. This gives the first two bounds (using $0\le\tau'\le1$). The Hessian entries of (8.LG1) are $\partial_a\partial_b\widehat V=-\psi_{ab}(u_b-u_a)$ and $\partial_a^2\widehat V=\sum_b[\psi_{ab}(u_b-u_a)-\psi_{ab}(-u_a)]$, exactly as for $V$. The operator norm is at most the maximal absolute row sum. The lattice bound uses the $24k^2+2$ offsets with $|m|_\infty=k$ and $|m|\ge k$:
$$
\sum_{k=1}^{n-1}\frac{24k^2+2}{(k-\frac12)^3}=24\sum_{k=1}^{n-1}\frac1k+\sum_{k=1}^{n-1}\frac{36k^2-16k+3}{k(k-\frac12)^3}\le24\ell_n+E_2,\qquad E_2<219.022,
$$
with $E_2$ enclosed by summing $k\le4000$ in interval arithmetic and bounding the tail by $36\cdot\tfrac{4001}{4000.5}/3999.5$. The source contributes $\widehat M_2(19.5n)\le\widehat M_2(39)$ to a memory row, and the source row is below $n^3\widehat M_2(19.5n)<1.2\times10^{-3}$. If $|u_a|,|u_b|\le\tfrac15$, every argument $v-u$ in (8.LG1) has modulus at most $\tfrac25$, where $\tau$ is the identity. The last bound is the double integral of $|\psi_{ab}|\le\widehat M_2$. $\square$

The contrast with Theorem O(2) is exact in the collapse configuration of its proof. At $n=2$, $Q=60$ the verifier finds $\lambda_{\min}(\nabla^2V)=-12037.8\approx-D_2n$ while $\lambda_{\min}(\nabla^2\widehat V)=-13.98\ge-\widehat h_N=-1558.1$ (row `LHAT-STRUCTURE`). The logarithm in (8.LG3) is the absolute dipolar row sum in three dimensions; the signed kernel is bounded (4.2), but the sufficient estimates below use absolute values.

Write $\widehat g_0^2:=\Omega^2-\widehat h_N$. By Lemma NP-1 applied verbatim to $\widehat H(s)$ (its only input is the global lower bound on the potential Hessian), every $\widehat\nu_s$ is strongly log-concave: $\widehat\nu_s=e^{-U}$ with $\nabla^2U\ge2\widehat g_0$. Lemma NP-2(a)–(c) holds with $g_0\to\widehat g_0$. The smoothness step of Lemma NP-3 must be replaced, because $\widehat V(x+s)-\widehat V(x+s')$ is not a bounded operator: $\nabla\widehat V$ grows linearly. Instead, $|\widehat V(u)|\le\tfrac12\widehat S_2|u|^2$ and $|\partial_s^\alpha\widehat V(x+s)|\le C_\alpha(1+|x+s|)^{(2-|\alpha|)_+}$ show that $s\mapsto\widehat V(\cdot+s)$ is a $C^\infty$ family of $H_0$-bounded operators with relative bound at most $\widehat h_N/\Omega^2<10^{-5}$. So $\widehat H(s)$ is self-adjoint on $D(H_0)$ and has compact resolvent. The ground state is isolated by the gap $\widehat g_0$, the Riesz projection is $C^\infty$ in $s$, and $\widehat{\mathcal E}\in C^\infty$. Hence the trap-work identity, the response equation, the second-order formula and (8.NP3) hold for $\widehat H(s)$. The function $\tau$ is $C^\infty$ but not analytic, so this argument does not use analytic perturbation theory. By Bakry–Émery [BGL14] the measure also satisfies the logarithmic Sobolev inequality
$$
\operatorname{Ent}_{\widehat\nu_s}(f^2)\le\widehat g_0^{-1}\,\mathbb E_{\widehat\nu_s}|\nabla f|^2. \tag{8.LG4}
$$
The analogue of Lemma NP-4 reads $\Omega^2|m_a|=|\mathbb E\widehat V_a|\le\sum_b\widehat M_2(|d_{ab}|)\mathbb E|u_b|$, hence
$$
\widehat\mu:=\sup_{s\in\mathcal S}|m(s)|_\infty\le\frac{\widehat S_2(n)\bigl(\lambda_0+(2\widehat g_0)^{-1/2}\bigr)}{\Omega^2-\widehat S_2(n)}. \tag{8.LG5}
$$

#### 8.14.2 Localization of the exact branch Hamiltonians

Fix $s\in\mathcal S$, write $u=x+s$, $Z_s(x):=V(u)-\widehat V(u)$, and call a label $a$ *out* if $|u_a|>\tfrac15$ and *in* otherwise.

**Lemma LOC-A (pointwise lower bound).** With $\ell=U+\tfrac15$, define for $U>\tfrac15$
$$
\begin{aligned}
P_{\rm near}(U)&=27f'_{\max}+53.64(3\ell+.8661)+68.38(2\ell+.8661)+\tfrac{2\ell}{39}f'_{\max}+\tfrac{\ell}{907}+.001,\\
P_{\rm far}(U)&=16.0016\,U\,(24\ell_n+2.4047),\\
y(U)&=f_c(0)+\tfrac15\bigl[P_{\rm near}(U)+P_{\rm far}(U)\bigr]+\tfrac15\widehat S_2U+\tfrac12\widehat S_2U^2,
\end{aligned}
$$
where $f'_{\max}=\max_\rho|f_c'(\rho)|\le172.09$ (a grid value, F31-03; *v2.2.1 pointer, F32-05:* Section 8.17.1 proves $f'_{\max}<193.58$, and the current calculations of Section 8.17 use that proved bound). Then, for every $x$,
$$
Z_s(x)\ge-\sum_{a\ \rm out}y(|u_a|). \tag{8.LG6}
$$

*Proof.* Split $V$ and $\widehat V$ into in–in, in–out and out–out pair sums. In–in terms coincide by Theorem L-hat.

*Out–out, exact.* Restrict the positive field-energy identity of Theorem ST to the out dipoles: $V_{OO}=\tfrac12\mathcal D(q_O,q_O)-\sum_{a\in O}[f_c(0)-f_c(|u_a|)]\ge-f_c(0)|O|$.

*Out–out and in–out, convexified.* By $|\widehat V_{ab}|\le\widehat M_2|u_a||u_b|$ and the Schur test, $-\widehat V_{OO}\ge-\tfrac12\widehat S_2\sum_O u_a^2$ and $-\widehat V_{IO}\ge-\tfrac15\widehat S_2\sum_O|u_a|$.

*In–out, exact.* Integrating $\partial_{u_b}V_{ab}$ from $u_b=0$ gives $V_{ab}=g\int_0^{u_b}[\phi'_{ab}(v-u_a)-\phi'_{ab}(v)]\,dv$. Fix an out label $a$, $U=|u_a|$, and in partners $b$ ($|u_b|\le\tfrac15$). If $|d_{ab}|\ge2\ell$, the difference is at most $U\sup_{|w|\le\ell}|\phi''_{ab}(w)|\le16.0016\,U|d_{ab}|^{-3}$, and $\sum|d_{ab}|^{-3}\le24\ell_n+2\zeta(3)+.0006$ (the last term covers the source, and a source row) gives $P_{\rm far}$. If $|d_{ab}|<2\ell$, use $|\phi'_{ab}(w)|\le\min(f'_{\max},\rho^{-2})$ with $\rho$ the distance from site $b$ to the moving charge of $a$, which lies on a segment of length $\tfrac25$ centred at $r_a+u_ae_z$. At most $27$ lattice points lie within $1.2$ of that centre. For the others, compare each point with its unit cube: $(\rho-\tfrac15)^{-2}\le(1.2+\sqrt3/2)^2|y-c|^{-2}<4.2685|y-c|^{-2}$ on the cube, and $\int_{|y-c|\le3\ell+.8661}|y-c|^{-2}dy=4\pi(3\ell+.8661)$. The fixed-charge term is bounded by $(1+\sqrt3/2)^2(.8)^{-2}4\pi(2\ell+.8661)<68.38(2\ell+.8661)$ in the same way. The source, if it is a near partner, adds the two small terms. Multiplying by $|u_b|\le\tfrac15$ and adding the four contributions proves (8.LG6). $\square$

The out–out step is where positive field energy is used essentially: a pairwise bound would give $-2f_c(0)$ for each pair of out labels, which is extensive in $|O|$.

**Lemma LOC-B (energies, gap and ground states).** Let $\chi$ be the $C^1$ ramp $3t^2-2t^3$, $t=(U-.15)/.05$ clipped to $[0,1]$, and write $y(U)\le Y_0+Y_1U+Y_2U^2$. Put $h(U)=\chi(U)\sqrt{Y_0+Y_1U+Y_2U^2}$, $C_h=\sup|h'|$, $\theta(\eta)=2C_h^2/(\eta\widehat g_0^2)$, $\mu_*=\lambda_0+\widehat\mu$, $r_0=.15-\mu_*$, $r_1=\tfrac15-\mu_*$, and
$$
E_1:=2e^{-\widehat g_0r_0^2}\Bigl[Y_0+.15Y_1+.0225Y_2+\frac{Y_1+2Y_2\mu_*}{2\widehat g_0r_0}+\frac{Y_2}{\widehat g_0}\Bigr],\quad
\delta_E(\eta)=\frac{NE_1}{1-\theta(\eta)},\quad
\zeta=N\bigl(2f_c(0)Ne^{-\widehat g_0r_1^2}+E_1\bigr).
$$
(*v2.2.1 pointer, F32-05:* this first term of $\zeta$ is the historical v2.1 form. By F31-04 the correct count is $4f_c(0)N$ in place of $2f_c(0)N$; all current calculations use (8.SQ2) of Section 8.17.3. NP-LOG is unaffected at the $10^{-141}$ level.)

If $\theta(\tfrac12)<1$, then for every $s\in\mathcal S$:

1. $\widehat{\mathcal E}(s)-\delta_E(1)\le\mathcal E(s)\le\widehat{\mathcal E}(s)+\zeta$;
2. $H(s)$ has a simple ground state and $\mathcal E_1(s)-\mathcal E(s)\ge\gamma_*:=\tfrac12\widehat g_0-\delta_E(\tfrac12)-\zeta$;
3. $1-|\langle\psi_s,\widehat\psi_s\rangle|^2\le\varepsilon_{\rm loc}:=(\delta_E(1)+\zeta)/\gamma_*$.

*Proof.* Put $\widetilde Y(x)=\sum_ah(|x_a+s_a|)^2$, so $Z_s\ge-\widetilde Y$ by (8.LG6). For $\varphi=\widehat\psi_sf$ in the form domain, the ground-state representation gives $\langle\varphi,(\widehat H-\widehat{\mathcal E})\varphi\rangle=\tfrac12\mathbb E|\nabla f|^2$. The entropy (Gibbs) variational inequality and (8.LG4) give, for $\varepsilon=2/(\eta\widehat g_0)$,
$$
\mathbb E[\widetilde Yf^2]\le\frac1\varepsilon\bigl[\operatorname{Ent}(f^2)+\mathbb E[f^2]\log\mathbb Ee^{\varepsilon\widetilde Y}\bigr]
\le\frac\eta2\mathbb E|\nabla f|^2+\frac{\eta\widehat g_0}2\log\mathbb Ee^{\varepsilon\widetilde Y}\;\mathbb E[f^2].
$$
This is the classical log-Sobolev semiboundedness mechanism (Federbush, Gross [Gro75]). To bound the exponential moment, let $F=\varepsilon\widetilde Y$. Then $|\nabla F|^2=\varepsilon^2\sum_a4h^2h'^2\le4\varepsilon C_h^2F$, and (8.LG4) applied to $e^{\lambda F/2}$ gives $\lambda\Lambda'-\Lambda\le\theta\lambda^2\Lambda'$ for $\Lambda(\lambda)=\log\mathbb Ee^{\lambda F}$, with $\theta=\varepsilon C_h^2/\widehat g_0=\theta(\eta)$. Integrating $(\Lambda/\lambda)'\le\theta\Lambda'$ over $(0,1]$ gives $\Lambda(1)\le\mathbb E F/(1-\theta)$; all moments are finite because $\widehat\nu_s$ is dominated by a Gaussian of variance $(2\widehat g_0)^{-1}$ and $F$ grows with coefficient $\varepsilon Y_2\ll\widehat g_0$. Hence
$$
\langle\varphi,(H-\widehat{\mathcal E})\varphi\rangle\ge\tfrac12(1-\eta)\mathbb E|\nabla f|^2-\frac{\mathbb E\widetilde Y}{1-\theta(\eta)}\|\varphi\|^2. \tag{8.LG7}
$$
Under $\widehat\nu_s$, $x_a-m_a$ is $1$-Lipschitz, so $\widehat\nu_s(|x_a-m_a|\ge r)\le2e^{-\widehat g_0r^2}$. A layer-cake integration of $h^2\le1\{|u_a|\ge.15\}(Y_0+Y_1|u_a|+Y_2u_a^2)$ gives $\mathbb Eh(|u_a|)^2\le E_1$, hence $\mathbb E\widetilde Y\le NE_1$. With $\eta=1$, (8.LG7) proves the lower bound in 1. For the upper bound use $\widehat\psi_s$ as a trial vector: $\mathcal E\le\widehat{\mathcal E}+\mathbb E_{\widehat\nu}Z_s$. Here $|Z_s|\le\sum_{a\ {\rm out}}[f_c(0)N+y(|u_a|)]$, because $|V_{ab}|\le2f_c(0)$ for every pair and the remaining terms are those of Lemma LOC-A (*v2.2.1 pointer, F32-05:* by F31-04, $|V_{ab}|\le2f_c(0)$ gives $2f_c(0)N$, not $f_c(0)N$, per out label, hence the $4f_c(0)N$ of (8.SQ2), which all current calculations use). Integration gives $\mathbb E|Z_s|\le\zeta$. For 2, take $\eta=\tfrac12$ and $\varphi\perp\widehat\psi_s$; then $f$ is centred and Lemma NP-2(a) gives $\tfrac12\mathbb E|\nabla f|^2\ge\widehat g_0\|\varphi\|^2$. Min–max gives $\mathcal E_1\ge\widehat{\mathcal E}+\tfrac12\widehat g_0-\delta_E(\tfrac12)$, and 1 bounds $\mathcal E$ from above. For 3, write $\widehat\psi_s=\alpha\psi_s+\varphi$ with $\varphi\perp\psi_s$. Then $\gamma_*\|\varphi\|^2\le\langle\widehat\psi_s,(H-\mathcal E)\widehat\psi_s\rangle=\widehat{\mathcal E}+\mathbb EZ_s-\mathcal E\le\delta_E(1)+\zeta$. $\square$

Lemma LOC-B is an exponentially accurate statement about the exact non-convex operator. It uses only static quantities; the growing window enters later through $T_R$ times an energy error. A finite check of the log-Sobolev chain (row `LOC-SEMIBOUND`) finds, for a one-dimensional reference with $\omega=100$, a true downward shift $.022015$ against the bound $.034240$. The first-order value $.021914$ alone would fail; the controlled fault `loc-no-herbst` detects this.

#### 8.14.3 A site-resolved Euclidean covariance bound

The ground-state representation of the convexified model involves $U=-2\log\widehat\psi_s$, whose Hessian is controlled only from below. Its off-diagonal decay is not available. The Euclidean path measure has an explicit Hessian instead, and this suffices.

**Lemma SR.** Let $\widehat W\in C^\infty(\mathbb R^N)$ have bounded derivatives of order at least two, with $\nabla^2\widehat W\ge\widehat g_0^2>0$. Suppose a symmetric matrix $K\ge0$ (entrywise) satisfies, for all $x$, $|\partial_a\partial_b\widehat W(x)|\le K_{ab}$ for $a\ne b$ and $\partial_a^2\widehat W(x)\ge\Omega^2-K_{aa}$, and $\max_a\sum_bK_{ab}<\Omega^2$. Put $\Gamma:=(\Omega^2I-K)^{-1}$, which is entrywise nonnegative. Let $\psi,\nu,\mathbf L$ be the ground state, ground-state measure and ground-state generator of $\tfrac12|p|^2+\widehat W$. Then for $A,B\in C^1$ with bounded gradients,
$$
\bigl|\operatorname{Cov}_\nu\bigl(A,\mathbf L^{-1}(B-\mathbb E_\nu B)\bigr)\bigr|
\le\frac12\sum_{a,b}\|\partial_aA\|_{L^2(\nu)}\,\Gamma_{ab}\,\|\partial_bB\|_{L^2(\nu)}. \tag{8.LG8}
$$

*Proof.* By truncation ($A\mapsto\lambda\tanh(A/\lambda)$, $\lambda\to\infty$) it suffices to treat bounded $A,B$. For $\beta>0$ and $M\ge3$ slices, $\epsilon=\beta/M$, let $\mu$ be the probability measure on $(\mathbb R^N)^{\mathbb Z_M}$ proportional to $e^{-S}$,
$$
S(X)=\sum_{k\in\mathbb Z_M}\Bigl[\frac{|x_{k+1}-x_k|^2}{2\epsilon}+\epsilon\widehat W(x_k)\Bigr].
$$
The Trotter product formula and the Gaussian kernel of $e^{-\epsilon|p|^2/2}$ show that slice correlations of $\mu$ converge, as $M\to\infty$, to thermal time-ordered correlations. In particular $\operatorname{Cov}_\mu(A(x_0),\epsilon\sum_kB(x_k))\to\int_0^\beta C_\beta(t)\,dt$, and the one-slice marginal $\mu_1$ converges to the thermal diagonal. Because the ground state is simple and isolated (gap $\ge\widehat g_0$), as $\beta\to\infty$ these converge to $2\int_0^\infty\langle(A-\mathbb EA)\psi,e^{-t(H-E)}(B-\mathbb EB)\psi\rangle dt=2\operatorname{Cov}_\nu(A,\mathbf L^{-1}\widetilde B)$ and to $\nu$ [Sim05; GJ87]. For bounded $A,B$ with bounded gradients the convergence of both sides is dominated uniformly in $\beta$. Indeed $|C_\beta(t)|\le\|A\|_\infty\|B\|_\infty\,(e^{-\gamma t}+e^{-\gamma(\beta-t)}+e^{-\gamma\beta/2})$ for $\beta$ large, where $\gamma\ge\widehat g_0$ is the gap. The functions $|\partial_aA|^2$ are bounded and continuous, so the weak convergence of $\mu_1$ passes to the right side. It therefore suffices to prove, for every $\beta$ and $M$,
$$
|\operatorname{Cov}_\mu(A(x_0),\epsilon\textstyle\sum_kB(x_k))|\le\sum_{a,b}\|\partial_aA\|_{L^2(\mu_1)}\Gamma_{ab}\|\partial_bB\|_{L^2(\mu_1)}. \tag{8.LG9}
$$
The measure $\mu$ is strongly log-concave, since $\nabla^2S\ge\epsilon\widehat g_0^2$. The Helffer–Sjöstrand representation [HS94; Hel02] gives $\operatorname{Cov}_\mu(\Phi,\Psi)=\mathbb E_\mu\langle\nabla\Phi,G\rangle$ with $G=(\mathcal L\otimes I+\nabla^2S)^{-1}\nabla\Psi$ and $\mathcal L=-\Delta+\nabla S\cdot\nabla$. Group the components $G_{a,k}$ by site $a$. The block of $\nabla^2S$ at site $a$ is the $M\times M$ matrix $T_a(X)=\epsilon^{-1}\mathrm{Lap}+\epsilon\,\mathrm{diag}_k\,\partial_a^2\widehat W(x_k)$, where $\mathrm{Lap}$ is the periodic discrete Laplacian. The couplings between sites are $O_{ab}(X)=\epsilon\,\mathrm{diag}_k\,\partial_a\partial_b\widehat W(x_k)$. Hence
$$
(\mathcal L+T_a(X))G_a=f_a-\sum_{b\ne a}O_{ab}(X)G_b,\qquad f=\nabla\Psi .
$$
Let $T_{*a}=\epsilon^{-1}\mathrm{Lap}+\epsilon(\Omega^2-K_{aa})I$; it is a positive definite Z-matrix, and $T_a(X)-T_{*a}$ is diagonal and nonnegative. The Markov semigroup $e^{-t\mathcal L}$ is positivity preserving and $e^{-tT_{*a}}$ is entrywise nonnegative. By the Trotter product formula, $|e^{-t(\mathcal L+T_a(X))}h|\le e^{-t(\mathcal L+T_{*a})}|h|$ componentwise; integrating in $t$ gives $|G_a|\le(\mathcal L+T_{*a})^{-1}(|f_a|+\epsilon\sum_bK_{ab}|G_b|)$. For vector functions put $\mathcal N(h)=\max_k\|h_k\|_{L^2(\mu)}$. Since $e^{-t\mathrm{Lap}/\epsilon}$ is doubly stochastic and $e^{-t\mathcal L}$ contracts $L^2(\mu)$, $\mathcal N((\mathcal L+T_{*a})^{-1}|h|)\le\mathcal N(h)/(\epsilon(\Omega^2-K_{aa}))$. With $g_a:=\mathcal N(G_a)<\infty$ this gives $(\Omega^2-K)g\le\epsilon^{-1}\mathcal N(f)$ componentwise, and the M-matrix property gives $g\le\epsilon^{-1}\Gamma\mathcal N(f)$. For $\Phi=A(x_0)$, $\Psi=\epsilon\sum_kB(x_k)$ one has $\mathcal N(f_b)=\epsilon\|\partial_bB\|_{L^2(\mu_1)}$ by time-translation invariance. Then $|\operatorname{Cov}_\mu(\Phi,\Psi)|\le\sum_a\|\partial_aA\|_{L^2(\mu_1)}g_a$, which is (8.LG9). $\square$

The positivity step can be replaced by an $L^2$ energy estimate: pairing the block equation with $G_a$ gives $\epsilon(\Omega^2-K_{aa})\|G_a\|\le\|f_a\|+\epsilon\sum_bK_{ab}\|G_b\|$ for time-averaged norms, and averaging $A$ over time slices leaves the covariance unchanged by translation invariance. The hypothesis $\nabla^2\widehat W\ge\widehat g_0^2$ is implied by the others through Gershgorin; it is kept for the ground-state gap used in the limit.

For quadratic $\widehat W=\tfrac12x^TAx$ the left side of (8.LG9) equals $(A^{-1})_{ab}$ for every slicing, so (8.LG8) reduces to $\tfrac12|A^{-1}|\le\tfrac12(\Omega^2-K)^{-1}$ entrywise. In the covariance setting this inequality is of Otto–Reznikoff type [OR07; Men14]. They prove $|\operatorname{Cov}_\mu(f,g)|\lesssim(A^{-1})_{ij}\|\nabla_if\|\|\nabla_jg\|$ for classical Gibbs measures, with conditional spectral gaps on the diagonal. Lemma SR is its quantum ground-state, resolvent-integrated analogue, obtained through the Euclidean discretization. Observables of several coordinates are not a difference (*v2.2.1 correction, F32-04*): Menz's Brascamp–Lieb-type covariance estimate [Men14b, Theorem 2.3, Eq. (2.4)] already gives $|\operatorname{cov}_\mu(f,g)|\le\sum_{i,j}(A^{-1})_{ij}\|\nabla_if\|_{L^2(\mu)}\|\nabla_jg\|_{L^2(\mu)}$ for smooth $f,g$ of all coordinates, for a classical Gibbs measure on a product of Euclidean blocks with conditional Poincaré constants $\varrho_i=A_{ii}$, mixed-Hessian bounds $\kappa_{ij}=-A_{ij}$ and $A$ positive definite. What Lemma SR adds is the transfer to the quantum ground-state resolvent, which produces the factor $\tfrac12$, and its use for the exact model. Rows `SR-COVARIANCE` and `SR-DOMINATION` test it in anharmonic three-oscillator ground states and check the matrix facts used. The observed ratios of the two sides are $.003$–$.71$; the harmonic case reproduces $\tfrac12(A^{-1})_{ab}$ to $10^{-9}$. The controlled fault `sr-diagonal-gamma`, which keeps only the diagonal of $\Gamma$, fails as it must.

#### 8.14.4 Flip coefficients of the convexified energy

Let $K$ be the matrix of (8.LG2): $K_{ab}=\widehat M_2(|d_{ab}|)$ for $a\ne b$ and $K_{aa}=2\sum_{b\ne a}\widehat M_2(|d_{ab}|)$. Its row sums are at most $\widehat h_N$, so Lemma SR applies to $\widehat W=\tfrac12\Omega^2|x|^2+\widehat V(x+s)$ with $\Gamma=(\Omega^2-K)^{-1}$. Every column sum of $\Gamma$ is at most $(\Omega^2-\widehat h_N)^{-1}$. For $b\ne0$ the source row satisfies
$$
\Gamma_{0b}\le\frac{\widehat M_2(r_{\min})}{(\Omega^2-K_{00})(\Omega^2-\widehat h_N)},
$$
by the row-0 equation $\Gamma_{0b}=\sum_{c\ne0}K_{0c}\Gamma_{cb}/(\Omega^2-K_{00})$. Uniform $L^2(\widehat\nu_s)$ majorants of Hessian entries follow from (8.LG2) and the mean value theorem, with $\|u_b\|_2\le\lambda_b+\widehat\mu+(2\widehat g_0)^{-1/2}$:
$$
\bar M_{ab}=\widehat M_2(|d_{ab}|)\ (a\ne b),\quad
\bar M_{jj}=\widehat S_3\bigl(\lambda_e+\widehat\mu+(2\widehat g_0)^{-1/2}\bigr)+\widehat M_3(r_{\min})\bigl(\lambda_0+\widehat\mu+(2\widehat g_0)^{-1/2}\bigr),\quad
\bar M_{00}=R\,\widehat M_3(r_{\min})\bigl(\lambda_e+\widehat\mu+(2\widehat g_0)^{-1/2}\bigr),
$$
where $\widehat S_3=\max_a\sum_b\widehat M_3<2701.9$ and $\widehat S_{22}=\max_a\sum_b\widehat M_2^2<6696.8$.

**Lemma SC (source coefficient at every shift).** For every $s\in\mathcal S$ and memory $j$,
$$
|\partial_0\partial_j\widehat{\mathcal E}(s)-\partial_0\partial_jV(s)|\le(r_1+r_{\rm SR})\,|\partial_0\partial_jV(s)|, \tag{8.LG10}
$$
$$
r_{\rm SR}=\frac{\widehat M_2(r_{\min})}{\kappa_s}\frac{\bar M_{jj}+\widehat S_2}{\Omega^2-\widehat h_N}
+\frac{\bar M_{00}}{\kappa_s}\Bigl[\frac{\widehat M_2(r_{\min})}{\Omega^2-\widehat h_N}+\frac{\widehat M_2(r_{\min})(\bar M_{jj}+\widehat S_2)}{(\Omega^2-K_{00})(\Omega^2-\widehat h_N)}\Bigr],
$$
and $r_1$ is the direct-term bound defined in the proof. Here $\partial_0\partial_jV(s)$ is the classical Hessian entry at displacement $s$, and $\kappa_s=2(37/40)(.999)/L^3\le|\partial_0\partial_jV(s)|$ as in Lemma NP-6.

*Proof.* Second-order perturbation theory in the ground-state representation gives
$\partial_0\partial_j\widehat{\mathcal E}=\mathbb E\widehat V_{0j}-2\operatorname{Cov}(\widehat V_0,\widehat{\mathbf L}^{-1}F_j)$ with $F_j=\widehat V_j-\mathbb E\widehat V_j$.
Apply Lemma SR with $A=\widehat V_0$ and $B=\widehat V_j$, whose gradients are Hessian rows. Split $a\ne0$, where $\bar M_{0a}\le\widehat M_2(r_{\min})$ and the column sums of $\Gamma$ are used, from $a=0$, where the source-row bound on $\Gamma$ is used. This gives the $r_{\rm SR}$ term. For the direct term let $Y=x_j-x_0$ and $w=s_j-s_0$. On $\{|Y|\le\tfrac15\}$, $\psi_{0j}=\phi''_{0j}$; expand to second order with $|\phi'''|\le6.0006(r-.21)^{-4}$ and $|\phi''''|\le24.0024(r-.21)^{-5}$. Use $|\mathbb EY|\le2\widehat\mu$, $\mathbb EY^2\le\widehat g_0^{-1}+4\widehat\mu^2$ and the complement probability $P_1\le2e^{-\widehat g_0(.2-2\widehat\mu)^2/2}$ ($Y$ is $\sqrt2$-Lipschitz). This gives
$$
r_1=\kappa_s^{-1}\Bigl[m_3\bigl(2\widehat\mu+\sqrt{\mathbb EY^2}\sqrt{P_1}\bigr)+\tfrac12m_4\,\mathbb EY^2+2\widehat M_2(r_{\min})P_1\Bigr]. \qquad\square
$$

This replaces the $\ell^2$ covariance bounds of Lemma NP-6. There the source-row norm $\|(H_m)_{0,\ne0}\|_{\ell^2}\asymp\sqrt R\,L^{-3}$ was paired with $\|c^{(j)}\|_{\ell^2}$, producing the growing residue (13.L1). In (8.LG10) the source row is paired with column sums of $\Gamma$ and a row of $\bar M$, both of order $\ell_n/\Omega^2$.

**Lemma PC (memory pairs).** For every $s\in\mathcal S$ and memories $j\ne k$, $|\partial_j\partial_k\widehat{\mathcal E}(s)|\le2.9858\,r_{jk}^{-3}+q_k$ with $q_k=(\bar M\Gamma\bar M)_{kj}$ and
$$
\Bigl(\sum_kq_k^2\Bigr)^{1/2}\le\mathcal Q_{\log}:=\frac{(\bar M_{jj}+\widehat S_2)\sqrt{\bar M_{jj}^2+\widehat S_{22}}}{\Omega^2-\widehat h_N}. \tag{8.LG11}
$$

*Proof.* The direct term is Lemma NP-7(a) with $\widehat g_0$. On $\{|Y-\mathbb EY|\le\min(r/8,\tfrac25)-2\lambda_e-2\widehat\mu\}$ the argument stays where $\psi=\phi''$ and $\rho\ge7r/8$; off it $|\psi|\le\widehat M_2(r)\le16.0016r^{-3}$. This gives $r^3\mathbb E|\psi|\le2.98573$. The covariance term is Lemma SR with $A=\widehat V_k$, $B=\widehat V_j$. The $\ell^2$ norm over $k$ of $\bar M\Gamma\bar Me_j$ is at most $\|\bar M\|_{\rm op}\|\Gamma\|_{\rm op}\|\bar Me_j\|$, with $\|\bar M\|_{\rm op}$ bounded by its maximal row sum. $\square$

**Lemma TC (three memory labels).** For distinct memories $a,b,j$ and every $s\in\mathcal S$,
$$
|\partial_a\partial_b\partial_j\widehat{\mathcal E}(s)|\le T_3^{\log}:=\frac{3\sqrt2\,\widehat M_3(1)\widehat h_N}{\widehat g_0^2}+\frac{3(\pi/2)^2\sqrt3\,\widehat h_N^3}{\sqrt2\,\widehat g_0^{7/2}}. \tag{8.LG12}
$$

*Proof.* Use (8.NP3) for $\widehat H$. The expectation of a third derivative with three distinct labels vanishes by the pair structure. The covariance terms are bounded by Brascamp–Lieb, $|\operatorname{Cov}(\widehat V_{ab},\widehat{\mathbf L}^{-1}F_c)|\le\|\nabla\widehat V_{ab}\|\|\nabla\widehat V_c\|/(2\widehat g_0^2)$, with pointwise $|\nabla\widehat V_{ab}|\le\sqrt2\widehat M_3(1)$ and $|\nabla\widehat V_c|\le\widehat h_N$. The triple terms use Hölder $(4,2,4)$, the Caffarelli $L^4$ Poincaré inequality and Bakry–Émery. $\square$

Rows `NP-LOG-FORMULAS` recheck the second- and third-order formulas against finite differences in an independent code base. The third-order agreement is $6.7\times10^{-7}$ on a value $-6.22\times10^{-4}$; dropping the triple terms (fault `np3-drop-T`) produces an $88\%$ discrepancy.

#### 8.14.5 A readout without the source Efron–Stein term

**Lemma RD.** Let a real label energy $E(s,z_j,z')$ be given, with $\Delta_jE=\alpha(z')+s\beta(z')$ as in (2.12). Let $\beta_*\ne0$ and $\rho\ge0$ satisfy $|\beta(z')-\beta_*|\le\rho|\beta_*|$ for all $z'$. Write $\alpha=\alpha_0+\sum_kz_k\alpha_k+\rho^\alpha$ for any real coefficients. Then for $|t|\le T$,
$$
\Bigl|\mathbb E_{z'}\bigl[e^{-it\alpha}\sin(t\beta)\bigr]\Bigr|\ge|\sin(t\beta_*)|\prod_k|\cos(t\alpha_k)|-T|\beta_*|\rho-T\,\mathbb E_{z'}|\rho^\alpha|. \tag{8.LG13}
$$
If $\alpha_k$ are the Walsh coefficients, $\mathbb E(\rho^\alpha)^2\le\sum_{a<b}\sup(\tfrac14\Delta_a\Delta_b\alpha)^2$.

*Proof.* Replace $\sin(t\beta)$ by $\sin(t\beta_*)$ at cost $t|\beta-\beta_*|$ and $e^{-it\rho^\alpha}$ by $1$ at cost $t|\rho^\alpha|$. Then use $\mathbb Ee^{-it\sum z_k\alpha_k}=\prod\cos(t\alpha_k)$. The last statement follows because $\mathbb E(\tfrac14\Delta_a\Delta_bf)^2=\sum_{S\supseteq\{a,b\}}\widehat f(S)^2$, and summing over pairs counts every $|S|\ge2$ at least once. $\square$

For the convexified energy $\widehat E_0(z)=\widehat{\mathcal E}(\Lambda z)$,
$$
\beta(z')=\tfrac12\int_{-\lambda_0}^{\lambda_0}\!d\sigma_0\int_{-\lambda_e}^{\lambda_e}\!d\sigma_j\,\partial_0\partial_j\widehat{\mathcal E}(\sigma_0,\sigma_j,\lambda_ez').
$$
The classical Hessian entry $\partial_0\partial_jV(\sigma)=-\phi''_{0j}(\sigma_j-\sigma_0)$ depends only on $(\sigma_0,\sigma_j)$, has a fixed sign on the rectangle and integrates to $\beta_*=2J_{0j}$. Lemma SC therefore gives $|\beta(z')-2J_{0j}|\le\rho_\beta|2J_{0j}|$ with $\rho_\beta=r_1+r_{\rm SR}$, *uniformly in all other labels*. The source-dependent three-label terms that the Efron–Stein step of Theorem NP-P1 had to sum ($\lambda_0\sqrt R\,T_3^{\rm src}$, which grows like $n^{1/2}\widehat g_0^{-5/2}$ at fixed confinement) do not appear. Only the memory triples enter $\rho^\alpha$. Each Walsh pair coefficient satisfies $|\alpha_k|\le2\lambda_e^2\sup|\partial_j\partial_k\widehat{\mathcal E}|$. Row `NP-LOG-READOUT` checks (8.LG13) and the Boolean inequality on random instances; the fault `readout-drop-beta` fails on the uniformly shifted instance $\beta\equiv\beta_*(1-\rho)$.

#### 8.14.6 Theorem NP-LOG

**Theorem NP-LOG (logarithmic confinement, P1 preparation).** Use the exact model, geometry, window and observable of Section 2, the P1 preparation $\Psi_0$ (exact ground state of $H_{\rm MC}(0)$), and
$$
\Omega_R=10^4\bigl(1+\log\lceil R^{1/3}\rceil\bigr)\;\le\;10^4\bigl(1.4621+\tfrac13\log R\bigr).
$$
Then for every integer $R\ge2$, every memory $j$ and every $t\in I_R$,
$$
\boxed{D_j(t)\ge.9885.}
$$

*Proof.* Let $E_0(z)=\mathcal E(\Lambda z)$ and $\widehat E_0(z)=\widehat{\mathcal E}(\Lambda z)$.

*Step 1 (preparation, exact model).* By the Fubini–Study triangle inequality,
$$
\varepsilon_z:=1-|\langle\Psi_0,\psi_{\Lambda z}\rangle|^2\le\bigl(2\sqrt{\varepsilon_{\rm loc}}+\sqrt{\widehat\varepsilon}\bigr)^2 .
$$
Here $\varepsilon_{\rm loc}$ is Lemma LOC-B(3) at $s=0$ and at $s=\Lambda z$. The quantity $\widehat\varepsilon<4\widehat\sigma^2/\widehat g_0^2$ is the spectral-location bound of Section 8.2 for the convex interpolation $\widehat H(0)+\theta(\widehat V(x+\Lambda z)-\widehat V(x))$, with
$$
\widehat\sigma^2\le\frac{R(\widehat h_N\lambda_e+\widehat M_2(r_{\min})\lambda_0)^2+(R\widehat M_2(r_{\min})(2\lambda_0+\lambda_e))^2}{2\widehat g_0}.
$$
The common-vector echo lemma (A.1) gives $|D_j-D_j^{E_0}|\le8\max_z\varepsilon_z$, uniformly in time.

*Step 2 (energies).* Lemma LOC-B(1) gives $|E_0(z)-\widehat E_0(z)|\le\delta_3:=\delta_E(1)+\zeta$, hence $|D_j^{E_0}-D_j^{\widehat E_0}|\le2T\delta_3$.

*Step 3 (readout).* Apply Lemma RD to $\widehat E_0$ with $\beta_*=2J_{0j}$ and $\rho=\rho_\beta$. Lemma PC bounds the pair coefficients. Lemma TC, with the Boolean inequality over the $\binom{R-1}2$ memory pairs, gives $T\,\mathbb E|\rho^\alpha|\le H_3^{\log}:=\sqrt2(T\lambda_e^2)(R\lambda_e)T_3^{\log}$. As in (4.12), with the frozen/dipole error $.001$ only, $|\sin(2tJ_{0j})|\ge\cos(\pi e_*/2)$ with $e_*=1.01f_+(1.001)-1<.090792$. Also $T|2J_{0j}|\le1.01(\pi/2)f_+(1.001)<1.71342$. Therefore
$$
D_j(t)\ge\cos\frac{\pi e_*}2-L_{\rm pair}^{\log}-1.71342\,\rho_\beta-H_3^{\log}-2T\delta_3-8\max_z\varepsilon_z,
$$
where $L^{\log}_{\rm pair}=\tfrac12(2T\lambda_e^2)^2(2.9858\sqrt{29}+\mathcal Q_{\log})^2$.

*Step 4 (all-$n$ envelope).* Treat $n\ge2$ as real and $\ell=\ell_n\ge1+\log2$. Individual factors such as $C_h$ or $\bar M_{00}/\kappa_s$ increase. After the following regrouping, however, every error term is a product of nonnegative factors, each nonincreasing in $\ell$:

| Term | Regrouped factors, each nonincreasing |
|---|---|
| $\widehat h_N/\Omega^2$, $\widehat S_2/\Omega^2$ | $(a+b\ell)/(10^8\ell^2)$; hence $\widehat g_0/\ell=10^4(1-\widehat h_N/\Omega^2)^{1/2}$ is nondecreasing |
| $\widehat\mu$ | $\frac{\widehat S_2}{\ell^2}\cdot\bigl(\lambda_0+(2\widehat g_0)^{-1/2}\bigr)\cdot\bigl(10^8-\widehat S_2/\ell^2\bigr)^{-1}$ |
| $\bar M_{jj}$ | affine in $\lambda_e,\widehat\mu,\widehat g_0^{-1/2}$ with coefficients $\widehat S_3$ and $\widehat M_3(19.5n)$ |
| $r_{\rm SR}$, first part | $\frac{\widehat M_2(19.5n)}{\kappa_s}\cdot\frac{(\bar M_{jj}+\widehat S_2)/\ell^2}{10^8-\widehat h_N/\ell^2}$, with $\widehat M_2(19.5n)/\kappa_s\propto n^3(19.5n-\tfrac12)^{-3}$ |
| $r_{\rm SR}$, source part | $\frac{n^3\widehat M_3(19.5n)\widehat M_2(19.5n)}{\kappa_s}\propto\frac{n^6}{(19.5n-\frac12)^7}$, times $(\lambda_e+\widehat\mu+(2\widehat g_0)^{-1/2})$ and the two $\Gamma$ factors |
| $r_1$ | $n^3(19.5n-.21)^{-4}$, $n^3(19.5n-.21)^{-5}$, $\widehat\mu$, $\widehat g_0^{-1}$, $P_1$ |
| $\mathcal Q_{\log}$ | $\frac{\bar M_{jj}+\widehat S_2}{\ell}\cdot\sqrt{\bar M_{jj}^2+\widehat S_{22}}\cdot\bigl(\tfrac{\Omega^2-\widehat h_N}{\ell}\bigr)^{-1}$ |
| $T_3^{\log}$, $H_3^{\log}$ | $\frac{\widehat h_N/\ell^2}{(\widehat g_0/\ell)^2}$ and $\frac{(\widehat h_N/\ell)^3\ell^{-1/2}}{(\widehat g_0/\ell)^{7/2}}$; $R\lambda_e\le5\times10^{-10}$ |
| $\widehat\varepsilon$ | $\frac{(\widehat h_N/\ell)^2\ell^2}{n^3}$, the cross term $\frac{\widehat h_N}{\ell}\cdot\ell\,\widehat M_2(19.5n)$, $\frac{n^3}{(19.5n-\frac12)^6}$ and constants, each divided by $\widehat g_0^3$ |
| $\theta(\eta)$ | $2(C_h/\ell)^2/(\eta(\widehat g_0/\ell)^2)$; each summand of $C_h$ divided by $\ell$ is nonincreasing because $Y_1,Y_2$ are affine in $\ell$ |
| $N E_1$, $\zeta$, $2T\delta_3$ | $e^{(12-\kappa_0)\ell}\times$(polynomial of degree $\le1$ in $\ell$), with $\kappa_0=(\widehat g_0/\ell)r_0^2\ge220$ and $r_0$ nondecreasing |
| $\varepsilon_{\rm loc}$ | numerator as above, divided by $\gamma_*$, which is increasing |

The last row uses $d/d\ell\,[(12-\kappa_0)\ell+\log P(\ell)]\le12-\kappa_0+1/\ell<0$. The supremum over all real $n\ge2$ is therefore the interval value at $n=2$. Row `NP-LOG-ALLR` also re-evaluates the direct expressions at eleven values of $\ell$ up to $10^4$ as a check on the regrouping; an independent scan at 58 values found no increase. The certified values are:

| Quantity | Upper bound, all $n\ge2$ | Role |
|---|---:|---|
| $\widehat h_N/\Omega^2$ | $5.44\times10^{-6}$ | convexity of the comparison model |
| $\widehat\mu$ | $1.17\times10^{-8}$ | mean displacements |
| $r_{\rm SR}$ | $2.27\times10^{-6}$ | site-resolved source polarization |
| $r_1$ | $2.82\times10^{-7}$ | direct source term |
| $\mathcal Q_{\log}$ | $1.55\times10^{-4}$ | pair covariance, enters $L^{\log}_{\rm pair}$ |
| $L^{\log}_{\rm pair}$ | $1.30149\times10^{-3}$ | memory-pair phases |
| $H^{\log}_3$ | $2.6\times10^{-15}$ | memory triples |
| $\theta(\tfrac12)$ | $1.39\times10^{-2}$ | modified Herbst constant |
| $2T\delta_3$ | $1.8\times10^{-141}$ | exact-versus-convexified energies over $T_R$ |
| $8\max_z\varepsilon_z$ | $1.5\times10^{-24}$ | P1 echo |
| $\gamma_*$ (lower) | $8465$ | gap of every exact branch |

With $\cos(\pi e_*/2)>.989847$ the certified lower bound is $D_j(t)>.98854$. The frequency bound uses $n^3\le4R$. $\square$

**Corollary NP-LOG-B (the convexity barrier is crossed).** Along $\Omega_R=10^4\ell_n$ the sufficient condition $\Omega^2>h'_N$ of Theorem L fails for $n>1.26\times10^6$. For full cubes with $n>4.42\times10^6$ ($R>8.6\times10^{19}$) the exact branch potentials are not globally convex, since $D_2n>\Omega_R^2$ and Theorem O(2) applies. Theorem NP-LOG nevertheless holds for all $n$. The order $R^{1/6}$ in Corollary NP-B(i) is therefore a limitation of arguments that require global strong convexity, as stated there, and not of the record problem with the P1 preparation. Row `NP-LOG-BARRIER` records both crossings on powers of two ($2^{21}$ and $2^{23}$); the fault `log-no-hat`, which reinstates the global-convexity requirement, fails.

#### 8.14.7 Scope

Theorem NP-LOG changes the sufficient P1 design law from $O(R^{1/6})$ to $O(\log R)$. It keeps the full non-convex Coulomb Hamiltonian, the growing window $T_R\asymp R^2$, every memory and both source labels. The following remain as they were.

- *Gaussian preparation.* Theorem S needs the global fidelity $32\sigma^2/g_0^2\asymp N\Delta^{-5}$, which no energy locality removes. Theorem NP-G ($R^{1/5}$) is unchanged, and fixed or polylogarithmic confinement for $\Phi$ stays OPEN.
- *Fixed confinement.* Two logarithms remain. The absolute dipolar row sum $\widehat S_2\asymp\log n$ must stay below $\Omega^2$, and the union over $N$ sites in $\delta_3$ must beat $T_R N$. Whether a signed-kernel version of Lemma SR and a flip-local version of Lemma LOC-B remove both is OPEN. Section 8.15 decides the first input: the signed bound holds at first order and fails at second order near horizontal edges (Theorems DF and EL), so a signed Lemma SR can gain at most the first order. Section 13.12 re-types the target.
- *Physical status.* P1 is a declared preparation. The instrument, carrier, trap and clock bridges are unchanged (Section 14).
- *Proof status.* All analytic steps are proofs in the stated generality. The constants are interval-certified. The limits $M\to\infty$ and $\beta\to\infty$ in Lemma SR are standard Feynman–Kac–Trotter facts, cited rather than reproved. No proof assistant was used.
- *v2.2 note.* The second logarithm, the union over $N$ sites in $\delta_3$, came from the fixed threshold of (8.LG1). Section 8.17 removes it with a growing threshold and proves Theorem NP-SQRTLOG at $\Omega\asymp\sqrt{\log R}$. The first logarithm, the absolute dipolar row sum, is what limits that route.

### 8.15 The signed dipole kernel: first-order uniformity, a second-order edge logarithm and the uniaxial edge exponent

Section 8.14.7 left two logarithms between Theorem NP-LOG and fixed confinement. One of them is the absolute dipolar row sum $\widehat S_2\asymp\log n$ used in Lemma SR and in Theorem Q. The obvious way to remove it is to keep the signs of the kernel. Its first nontrivial input is an $n$-uniform $\ell^\infty$ bound on the response of the array to a uniform drive: on $(\Omega^2+gK)^{-1}\mathbf 1$ and on the Neumann terms $K^k\mathbf 1$. This section decides that input order by order. The non-perturbative part, the behaviour of $(\Omega^2+gK)^{-1}\mathbf 1$ at a fixed $\Omega$ as $n\to\infty$, is stated as Hypothesis EG and is not proved.

The answer depends on the order.
- **First order: bounded.** The first-order signed response is bounded on every S9 set (Theorem DF).
- **Second order: diverges.** On full cubes, the second-order response diverges logarithmically at horizontal edges and corners, with exact coefficients $2$ and $\tfrac32$ (Theorem EL).
- **Interpretation.** The continuum edge exponent of the uniaxial polarizable medium that the array approximates on large scales has the same leading coefficient (Proposition W). We read the lattice logarithm as the perturbative trace of that singular edge mode. Only the agreement of the coefficient is proved.

For the exactly solvable quadratic model this has three consequences:
- **Corollary Q-prime.** For the S9 source row, the logarithm of Theorem Q moves from the numerator to the Neumann radius, and the sufficient range improves.
- **Proposition LN.** For the S9 source row the logarithm appears at order $\Omega^{-4}$, at horizontal mid-edges and corners of full cubes. Lemma SRC transfers Theorem EL from the uniform drive to the smooth source row.
- **Hypothesis EG.** It is conjectured that the local-field factor grows without bound at any fixed confinement.

Throughout, $a=g=1$ and $K(d)=(|d|^2-3d_z^2)|d|^{-5}$ is the kernel (2.4). The memory set $S$ of Section 2.3 is written in integer coordinates $\{0,\ldots,n-1\}^3$ with the third axis along $e_z$. The lexicographic filling runs over $(i,j,k)$ with $k$, the $e_z$ index, varying fastest (as in every geometry routine of the verifier). Consequently every column of $S$ parallel to $e_z$ is an interval beginning at $k=0$, and at most one column is partial. For a function $f$ on $S$ write $(Kf)(j)=\sum_{a\in S\setminus\{j\}}K(a-j)f(a)$ and $h_S:=K\mathbf 1_S$. At first order the regularized kernel $K^{(c)}$ changes the statements by at most its row-sum distance $\delta_c<7\times10^{-168}$ of (4.3). At second order the change is at most $\delta_c(\|h\|_\infty+S_K+\delta_c)$, which is below $10^{-158}$ throughout the range $1+\log n\le1.7\times10^7$ used below.

#### 8.15.1 First order: a telescoped solid angle

Put $w(\rho,H):=H(\rho^2+H^2)^{-3/2}$ and $g_\rho(t):=(\rho^2+t^2)^{-1/2}$. Since $K=-\partial_z^2(1/r)$ away from the origin, $K(p,q,t)=-g_\rho''(t)$ with $\rho^2=p^2+q^2$.

**Lemma DF-1 (column telescoping).** For $\rho\ge1$ and integers $t_1\le t_2$,
$$
\sum_{t=t_1}^{t_2}K(p,q,t)=w(\rho,t_2+\tfrac12)+w(\rho,\tfrac12-t_1)-\sum_{t=t_1}^{t_2}e_\rho(t),\qquad
|e_\rho(t)|\le\bigl(\rho^2+(|t|-\tfrac12)_+^2\bigr)^{-5/2}, \tag{8.DF1}
$$
where $e_\rho(t):=g_\rho''(t)-g_\rho'(t+\tfrac12)+g_\rho'(t-\tfrac12)$.

*Proof.* $g'_\rho(t+\tfrac12)-g'_\rho(t-\tfrac12)=\int_{-1/2}^{1/2}g_\rho''(t+u)\,du$. Expanding $g''_\rho$ to second order about $t$, the linear term integrates to zero, so $|e_\rho(t)|\le\frac1{24}\max_{|u|\le1/2}|g_\rho''''(t+u)|$. The Legendre form $\partial_z^4(1/r)=24P_4(\cos\theta)r^{-5}$ with $|P_4|\le1$ gives $|g''''_\rho(s)|\le24(\rho^2+s^2)^{-5/2}$. Finally $-g'_\rho(s)=w(\rho,s)$ and $w$ is odd in $s$. $\square$

Each column sum is therefore a pair of end terms, discrete Poisson kernels of the horizontal faces seen from the site, plus a remainder that is summable over columns. The sum of the end terms over a face is a discrete solid angle.

**Lemma DF-2 (lattice Poisson sums).** For every $H\ge\tfrac12$, $\;0\le\sum_{m\in\mathbb Z^2\setminus\{0\}}w(|m|,H)\le2\pi$.

*Proof.* The planar Fourier transform of $w(|x|,H)$ is $2\pi e^{-H|\xi|}$ (the Poisson kernel of a half-space). Poisson summation gives $\sum_{m\in\mathbb Z^2}w(|m|,H)=2\pi\sum_{k\in\mathbb Z^2}e^{-2\pi H|k|}$. The $8r$ points with $|k|_\infty=r$ satisfy $|k|\ge r$, so the $k\ne0$ part is at most $16\pi e^{-2\pi H}(1-e^{-2\pi H})^{-2}=H^{-2}\varphi(H)$. Here $\varphi(H):=16\pi H^2e^{-2\pi H}(1-e^{-2\pi H})^{-2}$ is decreasing on $[\tfrac12,\infty)$, and $\varphi(\tfrac12)<.594$. Removing the $m=0$ term $H^{-2}$ proves the claim. $\square$

**Theorem DF (first-order uniformity of the signed kernel).** For every $R\ge2$ and every memory $j$ of the S9 set $S$,
$$
-7.905\le h_S(j)=\sum_{a\in S\setminus\{j\}}K(a-j)\le15.663. \tag{8.DF2}
$$
For the S9 source row $v_a:=K_{0a}$ (Section 2.3),
$$
\Bigl|\sum_{a\in S\setminus\{j\}}K(a-j)\,v_a\Bigr|\le24.28\,|v_j|. \tag{8.DF3}
$$

*Proof.* In integer coordinates every column of $S$ is an interval that begins in the lowest layer. All columns except at most one (the partial column of the lexicographic filling) end in the top layer $n-1$. Fix $j$ and apply (8.DF1) to every column $c$ other than the column of $j$. Here $\rho_c\ge1$ is the transverse distance, $t_1=-j_z$, and $t_2$ is the top of $c$ minus $j_z$. The contributions are as follows.
- **Bottom end terms.** $w(\rho_c,j_z+\tfrac12)$ are nonnegative and sum to at most $2\pi$ (Lemma DF-2 with $H=j_z+\tfrac12\ge\tfrac12$).
- **Top end terms of full columns.** $w(\rho_c,n-\tfrac12-j_z)$ also lie in $[0,2\pi]$ in total.
- **Partial column.** If it is not the column of $j$, it contributes one top term with $|w|\le\max_s s(1+s^2)^{-3/2}\rho^{-2}=\tfrac{2}{3\sqrt3}\rho^{-2}\le.3850$.
- **Column of $j$.** It contributes $-2\sum|t|^{-3}\in[-4\zeta(3),0]=[-4.8083,0]$.
- **Remainders.** They are bounded in modulus by
$$
E_*:=\sum_{m\in\mathbb Z^2\setminus0}\ \sum_{t\in\mathbb Z}|e_{|m|}(t)|\le2.7104 .
$$
The bound combines three pieces (row `DF-CONSTANTS`):
- exact interval evaluation for $|m|_\infty\le6$, $|t|\le60$;
- the $t$-tail $(T_0-\tfrac12)^{-4}/2$ for each of these columns;
- for $|m|_\infty=k\ge7$, the column majorant $3k^{-5}+\tfrac43k^{-4}$ obtained from Lemma DF-1 with $\rho\ge k$, times the $8k$ columns of the shell.

The exact value is about $2.574$.

Adding these gives $h_S(j)\le4\pi+.3850+2.7104<15.663$ and $h_S(j)\ge-4.8083-.3850-2.7104>-7.905$.

For (8.DF3) we need three facts.
- The continuous array lies at distance at least $L-(n-1)/2\ge19.5n$ from the source.
- $|\nabla K(r)|\le6|r|^{-4}$. On the unit sphere $|\nabla K|^2=45\cos^4\theta-18\cos^2\theta+9\le36$.
- $|v_j|\ge2f_-/L^3$.

Hence $|v_a-v_j|\le.17945\,|a-j|\,|v_j|/n$. Since $\sum_{a\in S\setminus j}|K(a-j)||a-j|\le2\sum_{k=1}^{n-1}(24k^2+2)k^{-2}\le48n$, the sum $\sum_aK(a-j)(v_a-v_j)$ is at most $8.614|v_j|$ in modulus. Adding $|v_j||h_S(j)|$ gives (8.DF3). $\square$

Theorem DF replaces the remark after Lemma 4.3. That remark checked the signed row sums numerically on full cubes with $n\le16$; its value "$\le2.92$" is not valid on partial sets, where values down to $-3.33$ occur. The theorem covers every $n$ and every S9 set. On full cubes with $n\le224$ the computed values lie in $[-2.63,3.19]$, and on partial S9 sets with $n\le32$ in $[-3.33,3.07]$. The first-order polarization of the array is therefore uniformly bounded, as the classical solid-angle picture of a uniformly polarized body suggests. In the continuum, the $zz$ component of the demagnetizing (or gravity-gradient) tensor of a uniformly polarized rectangular prism is a sum of face solid angles, while the off-diagonal components carry logarithms at edges (Newell, Williams and Dunlop 1993; Smith et al. 2010; the polyhedral form in Ren et al. 2018). Theorem DF is the uniform-in-$n$ lattice version for S9 sets, with the column telescoping replacing the continuum face integral; Section 15.10 records the comparison.

#### 8.15.2 Second order: an exact logarithm at horizontal edges and corners

**Theorem EL (edge and corner logarithms).** Let $B_n=\{0,\ldots,n-1\}^3$ be a full cube, $n\ge16$, and write $K^2\mathbf 1:=Kh_{B_n}$.

1. *Horizontal edges.* For $j=(m,0,0)$ with $n/4\le m\le3n/4$,
$$
(K^2\mathbf 1)_j=2\log n+O(1). \tag{8.EL1}
$$
2. *Corners.* $(K^2\mathbf 1)_{(0,0,0)}=\tfrac32\log n+O(1)$.
3. *Upper bound on every S9 set.* $|(K^2\mathbf 1_S)_j|\le15.663\,S_K(n)\le15.663\,[48(1+\log n)+5]$ for every $j$.

Here $O(1)$ is a quantity bounded in modulus by a constant independent of $n$ and $m$. By the reflections of the cube and the exchange of the two transverse axes, (1) holds at the corresponding points of all eight horizontal edges and (2) at all eight corners. In particular $\sup_j(K^2\mathbf 1)_j$ is of exact order $\log n$: the $n$-uniform $\ell^\infty$ bound holds for $K\mathbf 1$ and fails for $K^2\mathbf 1$.

Statement (3) is immediate from Theorem DF and Lemma 4.3. The proof of (1) uses two notions on the near region $N:=\{a\in B_n:\ |a_x-m|\le n/8,\ a_y\le n/8,\ a_z\le n/8\}$.
- A function $\lambda$ on $N$ is *local* if $|\lambda(a)|\le C[(1+a_y)^{-1}+(1+a_z)^{-1}]$.
- A function $\sigma$ is *slow* if $|\sigma|\le C$ and $|\sigma(a)-\sigma(a')|\le C(1+|a-a'|)/n$.

The constants $C$ never depend on $n$ or $m$. Write $Y=a_y+\tfrac12$, $H=a_z+\tfrac12$ and $\Phi(a):=2\arctan(Y/H)$.

**Lemma EL-1 (the depolarization field near a horizontal edge).** On $N$,
$$
h_{B_n}(a)=\Phi(a)+c_0+\lambda(a)+\sigma(a), \tag{8.EL2}
$$
with an absolute constant $c_0$, a local $\lambda$ and a slow $\sigma$.

*Proof.* All columns of $B_n$ are full. Applying (8.DF1) to every column other than that of $a$ gives
$$
h(a)=T_b(a)+T_t(a)+O(a)-\sum_{c\ne a_\perp}\ \sum_{t=-a_z}^{n-1-a_z}e_c(t).
$$
Here $T_b=\sum_{c\ne a_\perp}w(\rho_c,H)$, $T_t=\sum_{c\ne a_\perp}w(\rho_c,n-\tfrac12-a_z)$ and $O(a)=-2\sum_{t=1}^{a_z}t^{-3}-2\sum_{t=1}^{n-1-a_z}t^{-3}$. We treat the four pieces in turn.

(a) $O(a)=-4\zeta(3)+2\sum_{t>a_z}t^{-3}+2\sum_{t>n-1-a_z}t^{-3}$. The middle term is local and the last is slow.

(b) On $N$ the top height is at least $7n/8-\tfrac12$. $T_t$ is a fixed column sum minus the slow term $(n-\tfrac12-a_z)^{-2}$. It is at most $2\pi$, and its gradient in the continuous variable $a$ is $O(1/n)$. So $T_t$ is slow.

(c) Write $T_b=\sum_{c\in F}w(|c-a_\perp|,H)-H^{-2}$ with $F=\{0,\ldots,n-1\}^2$; the term $-H^{-2}$ is local. Let $P=\mathbb Z\times\mathbb Z_{\ge0}$. The points of $P\setminus F$ lie at transverse distance $\ge n/8$ from $a_\perp$, and their sum is slow (value $\le\sum_{\rho\ge n/8}H\rho^{-3}\le CH/n$, gradient $O(1/n)$). On $P$, Poisson summation in $c_x$ (with $a_x\in\mathbb Z$) gives
$$
\sum_{c_x\in\mathbb Z}w=W(c_y-a_y)+\omega(c_y-a_y),
$$
where $W(u)=2H(u^2+H^2)^{-1}$ and $\omega(u)=8\pi Hb^{-1}\sum_{k\ge1}kK_1(2\pi kb)$ with $b=\sqrt{u^2+H^2}\ge\tfrac12$. The function $\omega$ is exponentially small in $b$. Its sum over all $u\in\mathbb Z$ is a function of $H$ alone, and the part with $u<-a_y$ is exponentially small in $Y$; both are local.

For the midpoint sum of $W$ we compare it with the integral:
$$
\sum_{c_y\ge0}W(c_y-a_y)=\int_{-1/2}^\infty W(y-a_y)\,dy+\mu(a)=\pi+\Phi(a)+\mu(a).
$$
Over all of $\mathbb Z$ the corresponding midpoint error is $4\pi e^{-2\pi H}(1-e^{-2\pi H})^{-1}$ (Poisson again), which is local. The cells with $c_y\le-1$ contribute at most $\tfrac1{24}\sum_{c\le-1}\max_{\rm cell}|W''|$. With $|W''(u)|\le12H(u^2+H^2)^{-2}$ this is at most $1.8\,(Y^2+H^2)^{-1}$, which is local.

(d) Sum each remainder over all of $\mathbb Z$ and subtract the tails. The telescoping part vanishes, so $\sum_{t\in\mathbb Z}e_\rho(t)=\sum_tg''_\rho(t)=-16\pi^2\sum_{k\ge1}k^2K_0(2\pi k\rho)=:G(\rho)$ (Poisson), exponentially small in $\rho$. Hence $\sum_{c\in F\setminus a_\perp}G(\rho_c)$ equals the absolute constant $G_\infty:=\sum_{m\ne0}G(|m|)$ minus a sum over missing columns. Those lie at distance $\ge Y$ or $\ge n/8$, so this correction is local plus slow.

For the tails, if $(k-\tfrac12)^2\ge a_z^2$ then $(\rho^2+(k-\tfrac12)^2)^{-5/2}\le(\rho^2+a_z^2)^{-3/2}(\rho^2+(k-\tfrac12)^2)^{-1}$. Therefore
$$
\sum_c\sum_{t<-a_z}|e_c(t)|\le\tfrac\pi2\sum_{m\ne0}(|m|^2+a_z^2)^{-3/2}\le C(1+a_z)^{-1},
$$
which is local, and the top tails are $O(1/n)$, which is slow. $\square$

**Lemma EL-2 (summability).** Three sums are bounded:
- $\sum_{d\in\mathbb Z^3\setminus0}|K(d)|\,[(1+|d_y|)^{-1}+(1+|d_z|)^{-1}]<\infty$;
- $\sum_{0<|d|_\infty<n}|K(d)||d|\le48n$;
- $\sum_{|d|\ge n/8,\ |d|_\infty<n}|K(d)|\le C$.

*Proof.* For fixed $d_y\ne0$, $\sum_{d_x,d_z}|K|\le\sum2(\rho^2+d_y^2)^{-3/2}\le C/|d_y|$. For $d_y=0$ the planar sum is at most $2\sum_{\mathbb Z^2\setminus0}|m|^{-3}<18.1$. The same holds with $y$ and $z$ exchanged. The last two bounds use $|K|\le2|d|^{-3}$ and shell counting. $\square$

*Proof of Theorem EL(1).* Split $B_n=N\cup N^c$ and note that $|a-j|\ge n/8$ on $N^c$.
- **Far region.** By Theorem DF and Lemma EL-2, $\bigl|\sum_{N^c}K(a-j)h(a)\bigr|\le C$.
- **Near region, non-principal parts.** On $N$ insert (8.EL2). The constant $c_0+\sigma(j)$ multiplies $\sum_NK(a-j)=h(j)-\sum_{N^c}K(a-j)=O(1)$. The slow increments contribute $O(1)$ by the second bound of Lemma EL-2, and the local part contributes $O(1)$ by the first.
- **Principal term.** It remains to evaluate $M:=\sum_{a\in N\setminus j}K(a-j)\Phi(a)$.

Sum over $d_x$ first. For $(a_y,a_z)\ne0$, Poisson summation gives
$$
\sum_{|d_x|\le n/8}K(d)=K_2(a_y,a_z)+O(e^{-2\pi\sqrt{a_y^2+a_z^2}})+O(n^{-2}),\qquad K_2(y,z):=\int_{\mathbb R}K(x,y,z)\,dx=\frac{2(y^2-z^2)}{(y^2+z^2)^2}.
$$
The row $(a_y,a_z)=0$ contributes $\le2\zeta(3)\pi$. Hence
$$
M=\sum_{(y,z)\in Q\setminus0}K_2\Phi+O(1),\qquad Q:=\{0,\ldots,\lfloor n/8\rfloor\}^2 .
$$
Now $Q$ is invariant under $(y,z)\mapsto(z,y)$, $K_2$ is antisymmetric and $\Phi(y,z)+\Phi(z,y)=\pi$. Therefore
$$
\sum K_2\Phi=\sum_{Q\setminus0}q,\qquad q(y,z):=K_2(y,z)\Bigl[2\arctan\frac{y+1/2}{z+1/2}-\frac\pi2\Bigr]\ge0 .
$$
In polar coordinates $y=\rho\cos\psi$, $z=\rho\sin\psi$, compare with the homogeneous function $q_c=2\cos2\psi\,(\tfrac\pi2-2\psi)\rho^{-2}$. The shift by $\tfrac12$ changes the bracket by at most $\sqrt2/\rho$, so $|q-q_c|\le2\sqrt2\rho^{-3}$, which is summable. Since $|\nabla q_c|\le C\rho^{-3}$, the lattice sum of $q_c$ differs from its integral over the cells by $O(1)$. The square and the quarter disk of radius $n/8$ differ by a region of logarithmic measure $O(1)$. Hence
$$
M=\log(n/8)\int_0^{\pi/2}2\cos2\psi\,(\tfrac\pi2-2\psi)\,d\psi+O(1)=2\log n+O(1). \qquad\square
$$

*Proof of Theorem EL(2).* Put $j=0$, $N=\{a\in B_n:|a|_\infty\le n/8\}$ and $X=a_x+\tfrac12$. Call $\lambda$ local if $|\lambda(a)|\le C\sum_{i\in\{x,y,z\}}(1+a_i)^{-1}$. Lemma EL-2 holds with $d_x$ in place of $d_y$ by the same proof, so local functions contribute $O(1)$ to $(Kh)(0)$, exactly as slow ones do.

(a) *Representation.* Steps (a), (b) and (d) of Lemma EL-1 carry over verbatim. The missing columns now fill the two half-planes $c_x<0$ and $c_y<0$, and their $G$-terms are exponentially small in $X$ or $Y$. For the bottom sum write $T_b+H^{-2}=\sum_{c\in\mathbb Z_{\ge0}^2}w(|c-a_\perp|,H)$ plus a slow term, and apply the one-dimensional midpoint comparison twice.
- **Sum over $c_x\ge0$ at fixed $c_y$.** It equals $\int_{-1/2}^\infty w\,dx$ plus two corrections. The full-line remainder $\omega$ is exponentially small in $b=\sqrt{(c_y-a_y)^2+H^2}$ (at most $C\sqrt be^{-2\pi b}$). The boundary correction is at most $\tfrac1{24}\sum_{c_x\le-1}\max_{\rm cell}|\partial_x^2w|\le CH(X^2+b^2)^{-2}$.
- **Summing these corrections over $c_y\ge0$.** This gives local terms, bounded by $C\sqrt He^{-2\pi H}$ and by $C(X^2+H^2)^{-1}$ respectively.
- **Integrated rows.** They are $W_1(c_y-a_y)$ with
$$
W_1(u)=\frac H{b^2}\Bigl(1+\frac X{\sqrt{X^2+b^2}}\Bigr),\qquad b^2=u^2+H^2,\qquad |W_1''(u)|\le CHb^{-4}.
$$
Hence the full-line midpoint error of $\sum_{c_y}W_1$ is at most $CH^{-2}$, and the boundary correction at $c_y\le-1$ is at most $C(Y^2+H^2)^{-1}$; both are local.
- **Principal term.** $\int_{-1/2}^\infty\!\int_{-1/2}^\infty w=\Omega_q(X,Y,H)$, the solid angle of the quadrant $\{c_x,c_y\ge-\tfrac12\}$ seen from $a$:
$$
\Omega_q=\tfrac\pi2+\arctan\frac XH+\arctan\frac YH+\arctan\frac{XY}{Hr},\qquad r=\sqrt{X^2+Y^2+H^2}.
$$

Hence $h(a)=\Omega_q(X,Y,H)+c_0'+\lambda(a)+\sigma(a)$ on $N$, with $\lambda$ local and $\sigma$ slow.

(b) *Principal sum.* It remains to evaluate $M_c=\sum_{a\in N\setminus0}K(a)\Omega_q(a+\tfrac12)$. On the closed octant $O=[0,\infty)^3\setminus\{0\}$ put $F(y)=K(y)\Omega_q(y+\tfrac12)$. There $y_z+\tfrac12\ge\tfrac12$, so $F$ is smooth. The gradient of the solid angle of a planar region is at most $C$ divided by the distance to its boundary, so
$$
|\nabla F(y)|\le C|y|^{-4}+C|y|^{-3}\bigl(\tfrac12+d(y)\bigr)^{-1},
$$
where $d(y)$ is the distance from $y$ to the two coordinate rays $\{y_y=y_z=0\}$ and $\{y_x=y_z=0\}$. Summing over $y_x$ first gives $\sum_{y_x}|y|^{-3}\le C(1+\rho)^{-2}$ with $\rho=\sqrt{y_y^2+y_z^2}$, and $\sum(1+\rho)^{-2}(\tfrac12+\rho)^{-1}<\infty$ over the planar lattice.

The lattice sum over $N\setminus0$ therefore differs from $\int_{O\cap[0,n/8]^3,\,|y|\ge1}F$ by $O(1)$. The boundary faces of $O$ also contribute $O(1)$, because a face carries $O(\rho)$ lattice points on the shell of radius $\rho$ and $|F|\le C\rho^{-3}$ there. Two more replacements each cost $O(1)$:
- replacing $\Omega_q(y+\tfrac12)$ by $\Omega_q(y)$ inside $O$ (the difference is at most $C\min(1,d(y)^{-1})$, integrable against $|K|$ by the same estimate);
- replacing the cube $[0,n/8]^3$ by the ball of radius $n/8$ (logarithmic measure $O(1)$).

Since $K(y)\Omega_q(y)$ is homogeneous of degree $-3$, $M_c=\log n\cdot\int_{S^2_{+++}}(1-3\cos^2\theta)\,\Omega_q\,d\omega+O(1)$.

(c) *Angular integral.* The term $\pi/2$ integrates to zero, because the octant average of $1-3\cos^2\theta$ vanishes. On the octant use $x=\sqrt{1-y^2}\cos\psi$, $z=\sqrt{1-y^2}\sin\psi$ with $y,\psi\in(0,1)\times(0,\tfrac\pi2)$; then $d\omega=dy\,d\psi$ and $\int_0^1(1-3z^2)\,dy=\cos2\psi$.
- **The term $\arctan(x/z)=\tfrac\pi2-\psi$.** It gives $\int_0^{\pi/2}(\tfrac\pi2-\psi)\cos2\psi\,d\psi=\tfrac12$. The term $\arctan(y/z)$ gives the same by the symmetry $x\leftrightarrow y$.
- **The last term.** Write $c=\cos\theta$ and $I(u)=\int_0^{\pi/2}\arctan(u\sin2\varphi)\,d\varphi$ with $u=(1-c^2)/(2c)$. The last term is $\int_0^1(1-3c^2)\,I(u(c))\,dc$. Integrating by parts, and using that $(c-c^3)I(u(c))$ vanishes at both ends, gives $-\int_0^1(c-c^3)I'(u)u'(c)\,dc$. Differentiating under the integral and substituting $\cos\varphi$ gives $I'(u)=\operatorname{artanh}(u/\sqrt{1+u^2})/(u\sqrt{1+u^2})$. With $\sqrt{1+u^2}=(1+c^2)/(2c)$ and $\operatorname{artanh}((1-c^2)/(1+c^2))=-\log c$ this yields $I'(u)u'(c)=2\log c/(1-c^2)$. The term is therefore $-2\int_0^1c\log c\,dc=\tfrac12$.

The total is $\tfrac32$. $\square$

The octant integrals were also checked to thirty digits (row `EL-ANGULAR`).

**Remark EL-V (vertical edges; argument sketched, not part of Theorem EL).** At vertical mid-edges $j=(0,0,m)$, $n/4\le m\le3n/4$, the computed values of $(K^2\mathbf 1)_j$ converge (table below; the approach is like $C-25/n$). An argument along the lines of Lemma EL-1 indicates why. On the region within $n/8$ of $j$ both horizontal faces are at distance at least $n/8$. The end terms $T_b,T_t$ are then Riemann sums of face solid angles seen from height at least $n/8$, and $O(a)$ and the remainder tails are slow. The sums of $G$ over missing columns are exponentially small in the transverse distances $1+a_x$, $1+a_y$, hence local in the sense of Lemma EL-2 with $x$ in place of $z$. No analogue of the principal term $\Phi$ occurs, and the summation of the proof of Theorem EL(1) gives $O(1)$. Physically, the vertical edge is parallel to the polarization and $\int_{\mathbb R}K(x,y,z)\,dz=0$. This sketch was added after the referee passes and has not been independently reviewed, so the statement is recorded as a remark and its status is numerical.

Two numerical observations complement Theorem EL. Neither is proved here.
- **The logarithm is carried by a tube around each horizontal edge**, not only by the edge line. At the site $(m,6,0)$, $(K^2\mathbf 1)-2\log n$ equals $13.75,13.85,13.84,13.75$ for $n=32,48,64,96$. The same argument with the near region recentred suggests $2\log(n/(1+r))+O(1)$ at distance $r$ from the edge. The largest values occur on the bottom face near the corners, for example $23.60$ at $(8,8,0)$ for $n=96$. The excess $\sup_j(K^2\mathbf 1)_j-2\log n$ decreases slowly, from $14.47$ at $n=96$ to $14.26$ at $n=224$ (evidence file `el_big.json`).
- **Partial S9 sets behave like full cubes at large scales.** A partial S9 set is a box plus a partial slab one site thick plus one partial column, so its step is a straight edge. At the step of a partial set the growth per unit $\log n$ is again $2.0$ ($n=48\to96$).

The FFT evaluation on full cubes (row `EL-EDGE`) gives the following values:

| $n$ | $(K^2\mathbf 1)_{\rm mid\,edge}-2\log n$ | $(K^2\mathbf 1)_{\rm corner}-\tfrac32\log n$ | $(K^2\mathbf 1)$ at a vertical mid-edge |
|---:|---:|---:|---:|
| 8 | 6.939 | 6.472 | 5.876 |
| 32 | 8.118 | 7.069 | 8.659 |
| 64 | 8.196 | 7.118 | 9.066 |
| 128 | 8.207 | 7.133 | 9.265 |
| 224 | 8.203 | 7.136 | 9.349 |

The remainders converge. The vertical mid-edge values also converge (Remark EL-V). For the S9 source row the second-order ratio $(K^2v)_j/v_j$ at the bottom and top horizontal mid-edges behaves in the same way. For $n=16,\ldots,128$, $(K^2v)_j/v_j-2\log n$ is $8.54,8.76,8.80,8.78$ and $7.12,7.46,7.58,7.62$ respectively (row `EL-SOURCE`). Lemma SRC below proves that these remainders stay bounded.

#### 8.15.3 The uniaxial edge exponent

On scales large compared with the lattice spacing, the array with on-site stiffness $\Omega^2$ is a uniaxial dielectric. Only $z$-displacements polarize. The polarizability per site is $\alpha=g/\Omega^2$; the Lorentz sum of a cubic lattice vanishes, so the Clausius–Mossotti relation holds; hence
$$
\varepsilon_{zz}=\varepsilon(\Omega):=1+\frac{4\pi\alpha}{1-4\pi\alpha/3},\qquad\varepsilon_{xx}=\varepsilon_{yy}=1 .
$$
A horizontal edge is a right-angle wedge of this medium, and edges of dielectrics carry singular field modes (Meixner's edge condition). The following computation identifies the mode for the present anisotropy. The method, a coordinate stretch that reduces an anisotropic transmission problem at a multi-material corner to Laplace's equation, is standard (Mantič, París and Berger 2003; the Mellin framework of Nicaise and Sändig); we did not find the uniaxial right-angle case with the expansion (8.W2) stated in the sources we could open (Section 15.10).

**Proposition W (uniaxial right-angle wedge).** Fill $Q_+=\{y>0,z>0\}$ with permittivity ${\rm diag}(\varepsilon_{yy},\varepsilon_{zz})=(1,\varepsilon)$, $\varepsilon>1$, and leave the other three quadrants in vacuum. Look for potentials $\psi=r^\nu f(\phi)$ that satisfy $\nabla\!\cdot(\varepsilon\nabla\psi)=0$, continuity of $\psi$, continuity of $\partial_y\psi$ across $\{y=0\}$ and continuity of $\varepsilon_{zz}\partial_z\psi$ across $\{z=0\}$.
1. For $\nu\ne0$, such a solution exists if and only if $F(\nu,\varepsilon)=0$, where
$$
F(\nu,\varepsilon)=\sqrt\varepsilon+\tfrac12\varepsilon^{\nu/2}(c_1-c_2)-\varepsilon^{(\nu+1)/2}(c_1+c_2)+\tfrac12\varepsilon^{\nu/2+1}(c_1-c_2)+\varepsilon^{\nu+1/2},\qquad c_1=\cos\pi\nu,\ c_2=\cos2\pi\nu. \tag{8.W1}
$$
2. $\nu=1$ is a root for every $\varepsilon$: the uniform field along $y$, which the medium does not polarize.
3. For $\varepsilon=1+\delta$ with small $\delta>0$ there is a second root
$$
\nu(\varepsilon)=1-\frac{\delta^2}{8\pi^2}+\frac{\delta^3}{8\pi^2}+O(\delta^4). \tag{8.W2}
$$
The corresponding field $\nabla\psi\sim r^{\nu-1}$ is singular at the edge.

*Proof.* Inside $Q_+$ the stretch $\zeta=z/\sqrt\varepsilon$ turns the equation into Laplace's equation. Separation then gives $f=A\cos\nu\phi+B\sin\nu\phi$ inside and $g=C\cos\nu(\phi-\tfrac\pi2)+D\sin\nu(\phi-\tfrac\pi2)$ on $[\tfrac\pi2,2\pi]$ outside. On $\{y=0\}$ the physical radius is $\sqrt\varepsilon$ times the stretched one; on $\{z=0\}$ they agree. The four interface conditions are therefore
$$
f(\tfrac\pi2)=\varepsilon^{\nu/2}g(\tfrac\pi2),\quad f'(\tfrac\pi2)=\varepsilon^{(\nu-1)/2}g'(\tfrac\pi2),\quad f(0)=g(2\pi),\quad\sqrt\varepsilon f'(0)=g'(2\pi).
$$
The determinant of this $4\times4$ system is $\nu^2\varepsilon^{-1/2}F(\nu,\varepsilon)$, and substituting $\nu=1$ gives $F(1,\varepsilon)=0$. With $\nu=1-x$,
$$
F=\tfrac{x}{32}\bigl[128\pi^2x-16\delta^2+O(|x|\delta+\delta^3)\bigr],
$$
and the implicit function theorem applied to $F/x$ gives the leading term of (8.W2). Carrying the expansion one order further gives the $\delta^3$ term, since the coefficients of $x\delta^3$ and $x^3$ vanish. $\square$

Row `W-EXPONENT` evaluates the root of (8.W1) near $1$ at 35 digits:

| $\Omega^2$ | 6 | 10 | 20 | 100 | $10^4$ | $10^6$ |
|---|---:|---:|---:|---:|---:|---:|
| $\gamma:=1-\nu$ | $4.616\times10^{-2}$ | $1.590\times10^{-2}$ | $4.273\times10^{-3}$ | $1.922\times10^{-4}$ | $1.9992\times10^{-8}$ | $1.99999\times10^{-12}$ |
| $\gamma\,\Omega^4$ | 1.662 | 1.590 | 1.708 | 1.922 | 1.99916 | 1.99999 |

Since $\delta=4\pi/\Omega^2+O(\Omega^{-4})$, (8.W2) gives $\gamma\Omega^4\to16\pi^2/(8\pi^2)=2$. This limit equals the edge coefficient of Theorem EL(1). The two numbers are computed by unrelated means: an exact lattice sum at second order, and the exponent of a continuum transmission problem. Their agreement is the expected consistency. A mode $(r/n)^{-\gamma}$, excited with amplitude of order one at the box scale, contributes $\gamma\log n=2\log n\,\Omega^{-4}+O(\Omega^{-6}\log n)$ to the local field at the edge. That is exactly the term $g^2(K^2\mathbf 1)_j\Omega^{-4}$ of the Neumann series.

#### 8.15.4 Consequences for the exactly solvable quadratic model

For the quadratic model of Section 13.3 the source–memory coefficient carries the factor
$$
\frac{C_{G,0j}}{g\lambda_0\lambda_eK_{0j}}=1-\frac{g(KA_G^{-1}K)_{0j}}{K_{0j}} .
$$
For a uniform drive it reduces to the local-field factor ${\rm LF}_j:=\Omega^2[(\Omega^2+gK)^{-1}\mathbf 1]_j$.

**Corollary Q-prime (the logarithm moves to the Neumann radius).** If $\Omega_0^2>g[48(1+\log n)+5]$, then
$$
\rho_{\rm pol}\le\frac{28.33\,g}{\Omega_0^2-g[48(1+\log n)+5]}. \tag{8.Qp}
$$
At $\Omega_0^2=8\times10^8$ this is at most $10^{-4}$ whenever $1+\log n\le1.666\times10^7$. Hence $D^G_j\ge.98538$ for every $R\le10^{2\times10^7}$; Theorem Q gave $R\le10^{1800}$.

*Proof.* Write $K_m$ for the memory block of $K$ and $u=Ke_0$. The memory part of $u$ is the source row $v$, and $u_0=0$. Then $y:=K^2e_0$ has $y_a=(K_mv)_a$ on memories and $y_0=|v|^2$. By (8.DF3), $|(K_mv)_a|\le24.28|v_a|$. Moreover $|v_a|\le2f_+/L^3\le(f_+/f_-)|v_j|$ and $f_+/f_-\le1.1665$. Together, $|y_a|\le28.33|K_{0j}|$ on memories. The entry $y_0\le N(2f_+/L^3)^2$ is at most $4\times10^{-4}|K_{0j}|$, since $N\le n^3+1$ and $L=20n$.

The expansion $A_G^{-1}=\sum_{k\ge0}(-g)^kK^k\Omega_0^{-2(k+1)}$ converges in the row-sum norm because $gS_K<\Omega_0^2$, where $S_K$ includes the source row (Lemma 4.3). Since $(K^{k+2})_{0j}=(K^ky)_j$,
$$
|(KA_G^{-1}K)_{0j}|\le\sum_k g^k\Omega_0^{-2(k+1)}S_K^k\|y\|_\infty=\frac{\|y\|_\infty}{\Omega_0^2-gS_K}.
$$
The remaining terms of Theorem Q ($\Lambda_3$, $.66/\Delta_G^4$, $\varepsilon_Q$) are uniform in $n$. $\square$

**Lemma SRC (a smooth drive changes the second order by a bounded amount).** Let $S$ be an S9 set, $j\in S$ and $v$ the S9 source row, and put $\varphi_a:=v_a/v_j-1$. Then $|(K^2\varphi)_j|\le C_{\rm src}$ with an absolute constant. Consequently
$$
\frac{(K^2v)_j}{v_j}=(K^2\mathbf 1_S)_j+O(1)\quad\text{for every memory }j .
$$

*Proof.* On the continuous array the function $v/v_j$ has bounded derivatives:
$$
|\nabla\varphi|\le\lambda_1/n,\qquad|\nabla^2\varphi|\le\lambda_2/n^2 .
$$
Here $\lambda_1=.17945$, and $\lambda_2$ is absolute; both follow from the homogeneity of $K$ and the distance $\ge19.5n$ to the source, as in (8.DF3). Write $K\varphi=\varphi h+b$ with $b(x):=\sum_{a\in S\setminus x}K(a-x)(\varphi_a-\varphi_x)$. Then
$$
(K^2\varphi)_j=\sum_{x\ne j}K(x-j)\varphi_xh(x)+b(j)h(j)+\sum_{x\ne j}K(x-j)\bigl(b(x)-b(j)\bigr).
$$
We bound the three terms in turn.
- **First term.** It is at most $15.663\,(\lambda_1/n)\sum|K(x-j)||x-j|\le15.663\cdot48\lambda_1$.
- **Second term.** Taylor's formula gives $b(x)=\nabla\varphi(x)\cdot V(x)+B_2(x)$. Here $V(x):=\sum_{a\in S\setminus x}K(a-x)(a-x)$ satisfies $|V|\le\sum2|d|^{-2}\le48n$. The remainder $B_2(x)=\sum K(a-x)R_2(a,x)$ has $|R_2|\le\lambda_2|a-x|^2/(2n^2)$, so $|B_2|\le\lambda_2n^{-2}\sum_{|d|_\infty<n}|d|^{-1}\le13\lambda_2$. Hence $|b(j)|\le48\lambda_1+13\lambda_2$.
- **Third term, first ingredient.** The vector kernel $k(d)=K(d)d$ is homogeneous of degree $-2$ with $|\nabla k|\le C|d|^{-3}$. Splitting the sum at $|a-x|=2r$ gives, for $|x-x'|=r$,
$$
|V(x)-V(x')|\le Cr\bigl(1+\log(n/r)\bigr),
$$
for any finite $S$ of diameter $\le\sqrt3n$.
- **Third term, second ingredient.** Since $\partial_xR_2=-\nabla^2\varphi(x)(a-x)$, we have $|\partial_x(K(a-x)R_2(a,x))|\le C\lambda_2n^{-2}|a-x|^{-2}$. Split at $|a-x|=2r$ as for $V$: the far part gives $C\lambda_2r\,n^{-2}\sum_{|d|\le\sqrt3n}|d|^{-2}\le C\lambda_2r/n$, and the near part gives $C\lambda_2n^{-2}\sum_{|d|\le3r}|d|^{-1}\le C\lambda_2r^2/n^2$. Hence $|B_2(x)-B_2(x')|\le C\lambda_2r/n$.
- **Third term, combined.** Together, with $r=|x-j|$,
$$
|b(x)-b(j)|\le|\nabla\varphi(x)-\nabla\varphi(j)||V(x)|+|\nabla\varphi(j)||V(x)-V(j)|+|B_2(x)-B_2(j)|\le C(\lambda_1+\lambda_2)\,\frac rn\Bigl(1+\log\frac nr\Bigr).
$$
Hence the third term is at most
$$
C\sum_{x\ne j}|x-j|^{-3}\frac{|x-j|}n\Bigl(1+\log\frac n{|x-j|}\Bigr)\le\frac Cn\sum_{r\le\sqrt3n}\Bigl(1+\log\frac nr\Bigr)\le C' .
$$

The second statement follows because $K^2v=v_j(K^2\mathbf 1_S+K^2\varphi)$. $\square$

The mechanism is the same as in Theorem EL. The constant part of a drive is handled by the signed first-order bound, and only variations are summed in absolute value; for a smooth drive the variations are small enough. Numerically $(K^2v)_j/v_j-(K^2\mathbf 1)_j\approx\pm.58$ at the bottom and top mid-edges (row `EL-SOURCE`).

**Proposition LN (the logarithm at order $\Omega^{-4}$).** (i) For the uniform drive, ${\rm LF}_j$ is analytic in $\Omega^{-2}$ for $\Omega^2>16g$:
$$
{\rm LF}_j=1-g\,h_j\,\Omega^{-2}+g^2(K^2\mathbf 1)_j\,\Omega^{-4}-\cdots,
$$
with $|h_j|\le15.663$ (Theorem DF) and $(K^2\mathbf 1)_j=2\log n+O(1)$ at horizontal mid-edges of full cubes (Theorem EL). If moreover $\Omega^2\ge5\times10^4g(1+\log n)$, then at those memories
$$
{\rm LF}_j-1+g\,h_j\,\Omega^{-2}\ge g^2(\log n-C)\,\Omega^{-4}
$$
with an absolute $C$.

(ii) For the quadratic model of Section 13.3 with the S9 source, the source-coefficient factor $C_{G,0j}/(g\lambda_0\lambda_eK_{0j})$ is analytic in $\Omega_0^{-2}$ for $\Omega_0^2>16g$. Its $\Omega_0^{-2}$ coefficient is bounded by $24.28g$ (Theorem DF). Its $\Omega_0^{-4}$ coefficient equals $g^2[(K_m^2v)_j/v_j+|v|^2]=g^2(2\log n+O(1))$ at horizontal mid-edges of full cubes.

*Proof.* The operator norm of $K$ is at most $16$ by (4.2), which gives analyticity. By Lemma 4.3, $S_K\le53(1+\log n)$. Every term beyond the second satisfies $|(K^k\mathbf 1)_j|\le S_K^{k-1}\|h\|_\infty$, so the tail is at most
$$
g^3S_K^2\cdot15.663\,\Omega^{-6}(1-gS_K/\Omega^2)^{-1}.
$$
In the stated range, $15.663\,gS_K\le15.663\cdot53\,g(1+\log n)\le.01661\,\Omega^2$ and $gS_K/\Omega^2\le.00106$. Hence the tail is at most $.01663\,g^2S_K\Omega^{-4}\le.882\,g^2(1+\log n)\Omega^{-4}$. Subtracting it from $g^2(2\log n-C_{\rm EL})\Omega^{-4}$ proves (i). For (ii), $(K^3)_{0j}=(K_m^2v)_j+v_j|v|^2$ as in the proof of Corollary Q-prime. Lemma SRC and Theorem EL give the coefficient, and $|v|^2\le N(2f_+/L^3)^2<10^{-7}$. $\square$

Proposition LN answers the question left open in Theorem Q. At the order where (13.2) places it ($\Omega_0^{-2}$), the logarithm is an artifact of absolute values: the true coefficient is bounded by $24.28g$. One order later it is not. It belongs to the exact quadratic readout with the S9 source, and it sits near horizontal edges and corners. The second coefficient of the $\Omega_0^{-2}$-expansion of the source coefficient is unbounded in $n$ there. So neither Theorem Q nor Corollary Q-prime can be improved to an $n$-uniform expansion of order two.

The higher coefficients grow as well; this is numerical and not proved here. At the mid-edge, $K^3\mathbf 1$ grows at about $10.7$ and $K^4\mathbf 1$ at about $106$ per unit $\log n$ for $n\le96$.

**Hypothesis EG (non-perturbative edge growth).** For every fixed $\Omega^2$ above the lattice instability threshold, the exact local-field factor at horizontal-edge midpoints of full cubes satisfies ${\rm LF}_j(n)\asymp n^{\gamma(\Omega)}$ with $\gamma(\Omega)=1-\nu(\varepsilon(\Omega))$ of Proposition W. In particular $\sup_j{\rm LF}_j(n)\to\infty$.

*Evidence.* EG is a hypothesis: it is supported but not proved.
- **First coefficient.** The first logarithmic coefficient is proved and coincides with $\lim\gamma\Omega^4=2$.
- **Lattice growth.** For the exact lattice problem the local growth exponents at the mid-edge, $\log({\rm LF}(n_2)/{\rm LF}(n_1))/\log(n_2/n_1)$, increase monotonically towards $\gamma$ from $n\approx32$ on, with no sign of saturation. Below $n\approx32$ they first decrease; at $\Omega^2=6$ the exponent for $8\to16$ is $.0546$. Values were computed by FFT conjugate gradients at relative tolerance $10^{-11}$; row `EG-LATTICE` recomputes the $n\le64$ entries.

| $\Omega^2$ | $32\to64$ | $64\to96$ | $96\to128$ | $128\to160$ | $160\to192$ | $\gamma(\Omega)$ |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | .04355 | .04399 | .04439 | .04468 | .04488 | .04616 |
| 10 | .01339 | .01427 | .01468 | .01492 | .01507 | .01590 |
| 20 | .00273 | .00334 | .00359 | .00373 | .00382 | .00427 |

- **Growth of the factor itself.** At $\Omega^2=6$ the mid-edge factor rises from $1.031$ ($n=8$) to $1.195$ ($n=192$). The vertical mid-edge and face values converge.
- **Corners.** The corner is not used as evidence. Its perturbative coefficient is $\tfrac32$ rather than $2$ (Theorem EL(2)), and its local exponents (for example $.0457$ at $\Omega^2=6$) are governed by a vertex problem that is not analysed here.
- **Related observations.** Discrete-dipole error theory assumes a smooth internal field and so excludes edge singularities (Yurkin, Maltsev and Hoekstra 2006). Finite cubic dipole lattices with sharp edges have been reported not to approach homogenized behaviour (Makarenko, Yurkin, Shcherbakov and Lapine 2025). Neither states an edge growth law; they are qualitative context, not evidence for the exponent.
- **What is missing.** A proof that the lattice problem inherits the continuum singular mode on all scales is not available here.

*Corrected conditional consequence (v2.1).* EG and a suitable nonperturbative transfer to the actual S9 source drive would imply failure of the whole-window record property at fixed uniformly stable $\Omega$, by Proposition SRX and Lemma WO in Section 8.16. The former fixed-time threshold and the inferred necessary/sharp $(\log R)^{1/4}$ law are withdrawn. Phase revivals invalidate the first argument, and fixed-$\Omega$ asymptotics do not control the joint limit needed for the second. The proven sufficient quadratic law remains $O(\sqrt{\log R})$.

#### 8.15.5 Scope

The following are proved:
- Theorem DF, Lemma EL-1, Lemma EL-2, Theorem EL, Proposition W, Corollary Q-prime, Lemma SRC and Proposition LN. Theorem EL, Lemma SRC and Proposition LN are stated with non-explicit constants; Theorem DF and Corollary Q-prime are interval-certified.

The following is not proved:
- Hypothesis EG, together with its consequence for fixed confinement.

For the full Coulomb model the implications are these.
- **Theorem NP-LOG is unchanged.** At $\Omega_R=10^4\ell_n$ the edge term satisfies $g^2|(K^2\mathbf 1)_j|\Omega^{-4}\le15.663(48\ell_n+5)\,10^{-16}\ell_n^{-4}\le1.7\times10^{-14}$ by Theorem EL(3). It is already inside the absolute bounds of Section 8.14.
- **The coefficientwise signed bound fails at second order.** Theorem EL rules out a uniformly bounded second Taylor coefficient near horizontal edges. It does not exclude nonperturbative cancellations or every signed-response method. The union over sites in LOC-B remains a full-model obstacle (Section 8.16.6).
- **Relation to non-absolute LSI criteria.** The covariance criteria used in Section 8.14 (Otto–Reznikoff, Menz) need absolute row sums or $|i-j|^{-d-\alpha}$ decay with $\alpha>0$; the three-dimensional dipole kernel has $\alpha=0$. The spectral criterion of Bauerschmidt and Bodineau (2019) avoids absolute summability, but it yields a log-Sobolev inequality, not the pointwise $\ell^\infty$ response bounds needed here. Section 8.15 shows that the second Taylor coefficient of the pointwise response is unbounded at edges, so any route to an $n$-uniform pointwise bound there must be non-perturbative in $\Omega^{-2}$.
- **Fixed confinement remains open.** EG alone is insufficient. The conditional quadratic obstruction additionally requires divergence of the driven source factor and an echo bound, as specified in Section 8.16.2. Neither a full-model lower bound nor a sharp resource law follows.
- *v2.2 note.* Section 8.18 replaces the lattice source-transfer premise by a continuum statement. By Theorem CR, unboundedness of the continuum source solution near an edge (Hypothesis EG-C) implies lattice unboundedness and, by Corollary CR-R, record failure at fixed confinement. EG-C is open.

### 8.16 Source response, the whole-window obstruction, and a variance readout

This section separates three questions that must not be identified: a continuum corner exponent, a driven finite-lattice resolvent, and the nonlinear record observable. It supplies an exact reduction of the second question and a readout improvement for the convexified model. It does not prove Hypothesis EG or a sub-logarithmic theorem for the full Coulomb model.

#### 8.16.1 Exact reduction of the source row

Here $K_m$ is the dipole matrix restricted to the memories, $v_j=K_{0j}<0$, $w=\Omega^2$, and $g>0$. These are the unregularized quadratic-model objects of Section 2.2; they are not the nonnegative matrix majorants also denoted by $K$ in Lemma SR. Write
$$
B=wI+gK_m,\qquad
A=\begin{pmatrix}w&gv^T\\gv&B\end{pmatrix},\qquad
q=\frac{g^2v^TB^{-1}v}{w}.
$$

**Proposition SRX (exact Schur source formula).** If $w>8g$, then
$$
F_j:=\frac{C_{0j}}{g\lambda_0\lambda_e v_j}
=\frac{w(B^{-1}v)_j}{v_j(1-q)},\qquad
0\le q\le\frac{g^2\|v\|_2^2}{w(w-8g)}.                 \tag{8.SRX1}
$$
For S9, with $f_+=(40/39)^3$,
$$
\|v\|_2^2\le\frac{f_+^2}{16\cdot10^6}\,n^{-3}.
                                                               \tag{8.SRX2}
$$
Consequently $q=O_w(n^{-3})$ at fixed $w>8g$. The unresolved source-transfer problem is the pointwise response $w(B^{-1}v)_j/v_j$, including its amplitude. It is not the feedback through the single source oscillator.

*Proof.* The inherited spectral bound $K\ge-8I$ applies to the full matrix and its principal memory submatrix. Thus $A,B>0$, and their Schur complement $s=w-g^2v^TB^{-1}v=w(1-q)>0$. From the definition of the effective coefficient matrix,
$$
\Lambda^{-1}C\Lambda^{-1}=gK-g^2KA^{-1}K=wI-w^2A^{-1}.
$$
Block inversion gives $(A^{-1})_{0j}=-g(B^{-1}v)_j/s$, proving (8.SRX1). Positivity and $\|B^{-1}\|\le(w-8g)^{-1}$ give the bound on $q$. Finally $|v_j|\le2f_+/(20n)^3$ and $R\le n^3$ give (8.SRX2). $\square$

The identity was checked against direct evaluation of $K-K(wI+K)^{-1}K$ on cubes $n=2,3,4$, for $w=10,20,100$. The largest absolute factor discrepancy was $1.34\times10^{-15}$. This is a finite algebra check, not an asymptotic theorem.

For larger cubes the actual S9 drive was solved as well as the uniform drive. The sites below are horizontal mid-edges in the nearest and farthest $z$ layers; $\mathrm{LF}_j=w(B^{-1}\mathbf1)_j$.

| $w$ | $n$ | $\mathrm{LF}_j$ | $F_j$, near layer | $F_j$, far layer |
|---:|---:|---:|---:|---:|
| 10 | 16 | 0.973094 | 0.960696 | 0.985943 |
| 10 | 32 | 0.981159 | 0.969472 | 0.993308 |
| 10 | 64 | 0.990312 | 0.979035 | 1.002085 |
| 20 | 16 | 0.965515 | 0.958649 | 0.972649 |
| 20 | 32 | 0.966469 | 0.960059 | 0.973150 |
| 20 | 64 | 0.968299 | 0.962176 | 0.974708 |

FFT matrix products and conjugate gradients use relative tolerance $2\times10^{-12}$. The residual divided by $w-8$ gives an analytic solution-error estimate, provided that residual is exact. The implementation also propagates its effect on $q$; FFT roundoff is not interval-enclosed, so these remain diagnostics. Observed source/uniform factors differ by about one percent. No lower bound uniform in $n$ on the driven singular-mode amplitude follows from these data or from Lemma SRC.

#### 8.16.2 A correct whole-window obstruction

**Lemma WO (window obstruction).** Suppose a pairwise-energy readout satisfies
$D_j(t)\le|\sin(\beta_jt)|+2\varepsilon$ on $[(1-\eta)t_*,(1+\eta)t_*]$, with $\eta>0$. Define
$$
M(a)=\begin{cases}\cos a,&0\le a\le\pi/2,\\0,&a\ge\pi/2.\end{cases}
$$
Then
$$
\inf_{t\in I_R}D_j(t)\le M(\eta|\beta_j|t_*)+2\varepsilon.
                                                               \tag{8.WO1}
$$
For the S9 quadratic model, $|\beta_j|t_*=(\pi/2)f_j|F_j|$, where $f_j=-L^3K_{0j}/2\ge37/40$ and $\eta=.01$. If $D_j(t)\ge d>2\varepsilon_Q$ throughout the window, necessarily
$$
|F_j|\le\frac{2\arccos(d-2\varepsilon_Q)}{\pi\eta f_j}.          \tag{8.WO2}
$$
For $d=.9885$, $\varepsilon_Q=0$ and $f_j=37/40$, the right side is less than $10.448$.

*Proof.* An interval of phases of length $2a\ge\pi$ contains a zero of $|\sin|$. For $a<\pi/2$, the largest possible minimum of $|\sin|$ over an interval of length $2a$ occurs when that interval is centered at a maximum, and equals $\cos a$. One can see this without optimization: every component of $\{|\sin x|>\cos a\}$ has length $2a$, so a closed interval of that length cannot lie in such a component. This proves (8.WO1); its inversion gives (8.WO2). In the quadratic model the other memory factors are products of cosines of modulus at most one, and Lemma Q2 supplies $2\varepsilon_Q$. $\square$

**Conditional consequence.** At a fixed $w>8g$, if $|w(B^{-1}v)_j/v_j|\to\infty$ along horizontal-edge sites of full cubes, then the all-memory, whole-window record property fails along those cubes. Indeed (8.SRX1) implies $|F_j|\to\infty$, while (13.4) gives $\varepsilon_Q=O_w(n^{-3})$. Eventually (8.WO1) is at most $2\varepsilon_Q\to0$. Hypothesis EG by itself concerns $B^{-1}\mathbf1$ and does not supply the premise about $B^{-1}v$.

This repairs the v2.0 fixed-time argument. Its expression $\cos(\pi\rho/2)$ omitted an absolute value and the geometric factor $f_j$. Even after inserting the absolute value, a large $\rho$ does not force small readout at $t_*$: for the simplified central phase, $\rho=2$ gives $|\sin(3\pi/2)|=1$, whereas the old upper bound was $\cos\pi=-1$; $\rho=4$ is another revival. A local first-lobe threshold is not an eventual-in-size failure theorem. Lemma WO uses the whole required window and therefore does not make that mistake.

#### 8.16.3 The double-limit debt

Fixed-$\Omega$ asymptotics, even if proved for both drives, do not establish a law along $\Omega=\Omega_n\to\infty$. To make the quantifier issue explicit, consider the positive scalar function
$$
G(n,\Omega)=\left(1+ne^{-\Omega^8}\right)^{2/\Omega^4}.
                                                               \tag{8.JL1}
$$
For every fixed $\Omega$, $G(n,\Omega)\sim e^{-2\Omega^4}n^{2/\Omega^4}$. Its exponent therefore obeys exactly $\gamma\Omega^4=2$. Along $\Omega_n=(2\log n)^{1/8}$, however,
$$
\log G(n,\Omega_n)=\frac{2}{\Omega_n^4}\log(1+n^{-1})\longrightarrow0.
$$
Thus $G\to1$ on a confinement curve smaller than $(\log n)^{1/4}$. This is a logical counterexample to the inference from pointwise asymptotics; it is not a counterexample to EG in the actual lattice. A joint-limit lower bound needs control of the amplitude, onset and remainder uniformly in $\Omega$. A matching sufficient law additionally needs upper estimates at every memory, rather than at one edge. The necessity and sharpness claims attached to $(\log R)^{1/4}$ in v2.0 are withdrawn. That exponent remains a heuristic candidate.

Likewise an unbounded second Taylor coefficient does not alone prove unbounded real-axis response at a fixed nonzero coupling. For example $1+\sin^2(t\sqrt{\log n})$ is bounded for real $t$, although its $t^2$ coefficient is $\log n$. Theorem EL rules out a coefficientwise uniform second-order bound; it does not rule out all nonperturbative cancellations.

#### 8.16.4 Variance readout without a triple-label remainder

**Lemma RD-V (variance readout).** Let the independent memory signs $z'$ be uniform and let $\alpha(z'),\beta(z')$ be arbitrary real functions. Suppose $|\beta-\beta_*|\le\rho|\beta_*|$. Then
$$
\left|\mathbb E e^{-it\alpha}\sin(t\beta)\right|
\ge |\sin(t\beta_*)|\left(1-\frac{t^2}{2}\operatorname{Var}\alpha\right)
-|t\beta_*|\rho .                                            \tag{8.RV1}
$$
With $D_kf=(f(z')-f(z'^{(k)}))/2$,
$$
\operatorname{Var}\alpha\le\sum_k\mathbb E(D_k\alpha)^2.       \tag{8.RV2}
$$
No Walsh-degree assumption is made.

*Proof.* Replacing the sine by $\sin(t\beta_*)$ costs at most $|t\beta_*|\rho$. Multiplication by $e^{it\mathbb E\alpha}$ preserves the modulus, while
$$
\left|\mathbb E e^{-it(\alpha-\mathbb E\alpha)}\right|
\ge\mathbb E\cos(t(\alpha-\mathbb E\alpha))
\ge1-\tfrac12t^2\operatorname{Var}\alpha.
$$
This holds also when the last expression is negative. For (8.RV2), write the Walsh expansion. The variance is $\sum_{S\ne\varnothing}\widehat\alpha(S)^2$, and the right side is $\sum_S|S|\widehat\alpha(S)^2$. $\square$

For the ground energy $\widehat{\mathcal E}(s)$, $\alpha$ is the source-even part of the $j$-flip. The fundamental theorem of calculus on each $(j,k)$ rectangle gives
$$
|D_k\alpha|\le2\lambda_e^2\sup_{s\in\mathcal S}|\partial_j\partial_k\widehat{\mathcal E}(s)|.
$$
The majorants of Lemma PC are uniform in $s$. Minkowski's inequality and $\sum_{k\ne j}r_{jk}^{-6}<29$ therefore yield
$$
\operatorname{Var}\alpha\le4\lambda_e^4
\left(2.9858\sqrt{29}+\mathcal Q_{\log}\right)^2.                \tag{8.RV3}
$$
Lemma SC controls $\beta$ at every shift, as before. Consequently
$$
D_j^{\widehat E_0}(t)\ge
\cos(\pi e_*/2)-L_{\rm pair}^{\log}-1.71342(r_1+r_{\rm SR}).   \tag{8.RV4}
$$
The term $H_3^{\log}$ is absent because the variance includes all memory-label degrees at once. This is not an assertion that the higher derivatives or higher Walsh terms vanish. The standard characteristic-function inequality and the Boolean Poincaré inequality are imported elementary tools; the contribution is their use with the existing shift-uniform PC and SC estimates.

#### 8.16.5 A square-root-log theorem for the convexified comparator

**Theorem COMP-SQRTLOG.** Use $\widehat H(s)$ of (8.LG1), the S9 controls and observation window, and the common switched-off ground state $\widehat\psi_0$. Put
$$
\Omega_R=10^4\sqrt{\ell_n},\qquad \ell_n=1+\log\lceil R^{1/3}\rceil.
$$
For every $R\ge2$, every memory $j$ and every $t\in I_R$,
$$
\widehat D_j(t)\ge .9885390>.9885.                            \tag{8.CS1}
$$
Here the hat on $D$ is essential: the Hamiltonian and its common preparation are those of the convexified comparator, not the full Coulomb model.

*Proof.* Set $S=48.0048\ell+438.09$, $h=3S$, $g_*=(10^8\ell-h)^{1/2}$ and use these upper/lower envelopes in the definitions of $\widehat\mu,\bar M,r_1,r_{\rm SR},\mathcal Q_{\log}$ in Section 8.14. Then $h/\Omega^2<9.203\times10^{-6}$ for all $n\ge2$. The proofs of L-hat, SR, SC and PC require this comparison gap and their displayed concentration bounds, rather than the special law (8.LG0). They therefore apply at the new law after their constants are checked below.

For the preparation, Step 1 of Theorem NP-LOG restricted to the comparator gives $\widehat\varepsilon\le4\widehat\sigma^2/g_*^2$, with
$$
\widehat\sigma^2\le
\frac{n^3(h\lambda_e+\widehat M_2(19.5n)\lambda_0)^2+
(n^3\widehat M_2(19.5n)(2\lambda_0+\lambda_e))^2}{2g_*}.
$$
The required smallness $\widehat\sigma/g_*<3.213\times10^{-13}$ holds. Appendix A contributes $8\widehat\varepsilon$. Combining this with (8.RV4) gives the bound certified below. No LOC-A, LOC-B or TC estimate is used.

For completeness, the all-$n$ enclosure is analytic, not a finite scan. $S/\ell=48.0048+438.09/\ell$ decreases; hence $h/\Omega^2$ decreases and $g_*/\sqrt\ell$ increases. The following regrouping shows that every error term is nonincreasing for real $n\ge2$.

| Quantity | Nonincreasing factors or reduction |
|---|---|
| $\widehat\mu$ | $(S/\ell)(\lambda_0+(2g_*)^{-1/2})/(10^8-S/\ell)$ |
| $\bar M_{jj}$ | Positive sums of decreasing $\lambda_e,\widehat\mu,g_*^{-1/2},\widehat M_3(19.5n)$ |
| First part of $r_{\rm SR}$ | $\widehat M_2/\kappa_s$, $(\bar M_{jj}+S)/\ell$, $(10^8-h/\ell)^{-1}$ |
| Source part of $r_{\rm SR}$ | $n^3\widehat M_3\widehat M_2/\kappa_s\propto n^6/(19.5n-.5)^7$, decreasing displacement factors, $g_*^{-2}$ and $(\Omega^2-K_{00})^{-1}(\bar M_{jj}+S)/g_*^2$ |
| $r_1$ | $n^3/(19.5n-.21)^4$, $n^3/(19.5n-.21)^5$, $\widehat\mu$, $g_*^{-1}$, and $P_1=2e^{-g_*(.2-2\widehat\mu)^2/2}$ |
| $\mathcal Q_{\log}$ | $((\bar M_{jj}+S)/\ell)\sqrt{\bar M_{jj}^2+6696.8}/(10^8-h/\ell)$ |
| $\widehat\varepsilon$ | Expanding its numerator gives $h^2/n^3$, $h\widehat M_2$, $n^3\widehat M_2^2$ and $n^6\widehat M_2^2(2\lambda_0+\lambda_e)^2$, all divided by $g_*^3$. For the first, use $(h/\ell)^2(\ell^{1/2}/n^3)/(g_*/\sqrt\ell)^3$; $\ell^{1/2}/n^3$ decreases. The cross term reduces similarly with $\ell^{-1/2}\widehat M_2$. |

$K_{00}\le2n^3\widehat M_2(19.5n)$ decreases, so $\Omega^2-K_{00}$ increases. All distances and concentration cutoffs in SC and PC stay positive. In particular the direct PC majorant
$$
2.0002(8/7)^3+16(2.0002)e^{-g_*(.125-2\lambda_e-2\widehat\mu)^2/2}
<2.985722<2.9858
$$
holds at $n=2$ and decreases. Also $T\lambda_e^2=1.01\pi/2000$ is constant. Thus the worst endpoint is $n=2$. Outward interval evaluation at 50 decimal digits, using the printed conservative constants, gives:

| Quantity | Safe bound, every $n\ge2$ |
|---|---:|
| $h/\Omega^2$ | $<9.203\times10^{-6}$ |
| $\widehat\mu$ | $<2.209\times10^{-8}$ |
| $r_{\rm SR}$ | $<3.844\times10^{-6}$ |
| $r_1$ | $<3.678\times10^{-7}$ |
| $\mathcal Q_{\log}$ | $<2.645\times10^{-4}$ |
| $L_{\rm pair}^{\log}$ | $<.001301507$ |
| $8\widehat\varepsilon$ | $<3.304\times10^{-24}$ |
| Full right side, with unrounded interval factors | $>.9885390698$ |

The final line uses the exact interval value $T|\beta_*|\le1.01(\pi/2)(40/39)^3(1.001)$; replacing it by $1.71342$ preserves the stated rounded theorem. $\square$

#### 8.16.6 Why this is not the requested full-model breakthrough

There are two distinct issues in the old route census. First, retaining TC at $\Omega=C\ell^p$ gives
$$
H_3^{\log}\ \text{contains a positive majorant term of order}\quad
\ell^{3-7p/2},\qquad p\ge\tfrac12.                           \tag{8.TC1}
$$
At $p=1/2$ this is $\ell^{5/4}$ and eventually diverges, however small its coefficient. Thus the v2.0 assertion that removing global localization would leave only the Hessian constraint omitted a growing term. RD-V now removes this specific bottleneck.

Second, LOC-B still compares global energies and states. Its displayed errors include volume factors multiplying concentration tails, and the energy error is multiplied by $T\asymp n^6$. At a sub-logarithmic law, expressions of the form
$$
n^q\operatorname{poly}(\ell)\exp[-cC\ell^p],\qquad q,c>0,\quad p<1,
                                                               \tag{8.LOC1}
$$
are unbounded, because $\log n=\ell-1$ dominates $\ell^p$. These are failing sufficient upper bounds, not lower bounds on the actual error and not a no-go theorem for full-model records.

An exact sufficient remaining target can be stated without guessing a cluster theorem. For $E_0$ and $\widehat E_0$ at the new law define
$$
\delta_{\mathrm{flip}}=
\sup_{z,j}|\Delta_j(E_0-\widehat E_0)(z)|,
\qquad e_{\mathrm{echo}}=
\sup_{j,t\in I_R}|D_j(t)-D_j^{E_0}(t)|.
$$
If full-model ground energies exist and
$$
e_{\mathrm{echo}}+T\delta_{\mathrm{flip}}\le3.8\times10^{-5}    \tag{8.FT1}
$$
uniformly in $R$, (8.RV4) and the comparator constants imply the full-model lower bound $.9885$. Indeed each source-conditioned phase echo changes by at most $T\delta_{\mathrm{flip}}$, and the normalized difference has the same bound. No ground-state overlap between the two models need be postulated in this formulation. Neither term in (8.FT1) has been proved at the new law. A flip-local energy estimate alone would leave the full-model common-preparation echo unresolved.

The research outcome is therefore partial: SRX isolates the driven resolvent, WO repairs the conditional no-record implication, and RD-V closes the memory-triple obstacle, proving COMP-SQRTLOG for the comparator. Neither alternative in the user's grade-4 criterion is established.

*v2.2 note (Appendix R, F31-01 and F31-02).* The frozen audit of v2.1 found that the growth in (8.LOC1) is a property of the fixed coincidence threshold $\tfrac15$ of (8.LG1), not of the model. Section 8.17 lets that threshold grow and proves Theorem NP-SQRTLOG for the full model. The sufficient budget (8.FT1) was also stronger than the readout needs. $\delta_{\rm flip}$ contains label-independent and first-order parts, and the readout ignores label-independent phases. What enters are only the mixed second differences $\Delta_0\Delta_j$ and $\Delta_j\Delta_k$. (8.FT1) was stated for the fixed-threshold comparator, and for that comparator it is not shown. For the growing-threshold comparator of Section 8.17 its analogue holds with a large margin: the global energy error gives $T\delta_{\rm flip}\le2T\delta_3<10^{-102}$, and the echo term is below $3.4\times10^{-24}$. The paragraphs above are retained as the v2.1 record of the route state.

### 8.17 A square-root-logarithmic record theorem for the full model (P1 preparation)

Section 8.16.6 attributed the failure of Lemma LOC-B at sub-logarithmic confinement to volume factors multiplying concentration tails. The frozen audit of v2.1 (Appendix R, finding F31-01) located the source of that growth. It comes from the fixed coincidence threshold $|u_a|\le\tfrac15$ of the comparison potential (8.LG1), a design choice rather than a property of the model. The probability that a site leaves a region of fixed size is $e^{-c\Omega}$, which no power of $n$ can beat when $\Omega\asymp\sqrt{\log n}$. The probability that it leaves a region of size $\asymp\ell^{1/4}$ is $e^{-c\,\Omega\,\ell^{1/2}}=n^{-c'}$, with $c'$ as large as needed. The threshold may therefore grow slowly with $n$. The comparison potential then acquires the Coulomb cores of nearby sites in the same column, but it stays uniformly convex: at $\Omega^2=10^8\ell$ the trap dominates even the core curvature $D_2\approx6018$.

This section carries out that change. The readout part is the square-root-log argument of Section 8.16. The new ingredients are a family of comparison potentials, the corresponding forms of Lemmas LOC-A and LOC-B, and a refined $L^2$ majorant that keeps the pair covariances bounded once cores enter the comparator. Units are $\hbar=m=a=g=1$, $c=\tfrac1{20}$, $\ell=\ell_n=1+\log n$, $n=\lceil R^{1/3}\rceil$, and

$$
\Omega_R=10^4\sqrt{\ell_n},\qquad \ell_*:=100,\qquad
y_c(\ell):=\begin{cases}\tfrac15,&\ell\le\ell_*,\\[2pt]\tfrac15(\ell/\ell_*)^{1/4},&\ell\ge\ell_*,\end{cases}\qquad
Y:=2y_c,\quad \widehat Y:=Y+\tfrac1{10}. \tag{8.SQ0}
$$

All other data are those of Section 2, and the preparation is P1, the exact ground state $\Psi_0$ of $H_{\rm MC}(0)$.

#### 8.17.1 Growing-threshold comparison potentials

**Kernel bounds.** From $f_c(r)=\frac2{\sqrt\pi}\int_0^{1/c}e^{-t^2r^2}dt$ and $\partial_z^ke^{-t^2r^2}=(-t)^kH_k(tz)e^{-t^2r^2}$, every directional derivative satisfies
$$
|\partial_z^kf_c|\le\frac2{\sqrt\pi}\,\frac{M_k}{(k+1)c^{k+1}},\qquad M_k=\sup_u|H_k(u)|e^{-u^2},\quad M_1=\sqrt2e^{-1/2},\ M_2=2 .
$$
Hence $f'_{\max}:=\max|f_c'|<193.58$ and $\max|\partial_z^2f_c|=D_2=4/(3\sqrt\pi c^3)<6018.03$, the latter attained at $r=0$. Also $0\le\operatorname{erf}x-\tfrac{2x}{\sqrt\pi}e^{-x^2}\le1$ gives $|f_c'(\rho)|\le\rho^{-2}$. For $\rho\ge\tfrac12=10c$ the point-Coulomb Legendre bounds hold up to the relative error $10^{-38}$ used in Theorem L-hat. The value $193.58$ replaces the grid value $172.09$ of Section 8.14 by a bound with a one-line proof; the true maximum is about $171.2$.

**The comparators.** Let $S$ be the smooth step of Section 8.14.1 and put
$$
\tau_Y(y)=\operatorname{sgn}(y)\Bigl[\min(|y|,Y)+\tfrac15\int_0^{5(|y|-Y)_+}\bigl(1-S(t)\bigr)\,dt\Bigr].
$$
Then $\tau_Y(y)=y$ for $|y|\le Y$, $0\le\tau_Y'\le1$, $|\tau_Y(y)|\le\min(|y|,\widehat Y)$. At $y_c=\tfrac15$ this is the function $\tau$ of (8.LG1). Define $\psi^Y_{ab}=\phi''_{ab}\circ\tau_Y$ and $\widehat V^Y$ by (8.LG1) with $\psi^Y$ in place of $\psi$. For a pair with transverse separation $\rho\ge0$ and axial offset $t$ write
$$
{\rm dist}_Y(d)=\min_{|s|\le\widehat Y}|d+se_z|=\bigl(\rho^2+(|t|-\widehat Y)_+^2\bigr)^{1/2},\qquad
\widehat M_2^Y(d)=\begin{cases}2.0002\,{\rm dist}_Y(d)^{-3},&{\rm dist}_Y(d)\ge\tfrac12,\\ D_2,&\text{otherwise.}\end{cases}
$$

**Theorem L-hat$_Y$.** For every $x$, $s$ and pair, $|\psi^Y_{ab}|\le\widehat M_2^Y(d_{ab})$, the Hessian of $\widehat V^Y$ has the entries of Theorem L-hat with $\psi^Y$, and $|\widehat V^Y_{ab}|\le\widehat M^Y_2|u_a||u_b|$. If $|u_a|,|u_b|\le y_c$ then $\widehat V^Y_{ab}=V_{ab}$. On the S9 family
$$
\widehat S^Y:=\max_a\sum_{b\ne a}\widehat M_2^Y(d_{ab})\le S_{\rm env}(\ell):=2.0002\bigl[16\ell+9.04(2\widehat Y+3)\bigr]+2D_2\bigl(\widehat Y+\tfrac12\bigr)+33.67, \tag{8.SQ1}
$$
and $\|\nabla^2\widehat V^Y\|_{\rm op}\le\widehat h^Y:=3\widehat S^Y$.

*Proof.* The bound on $\psi^Y$ is the definition of ${\rm dist}_Y$ with the kernel bounds, since $\tau_Y$ takes values in $[-\widehat Y,\widehat Y]$. Coincidence follows because every argument $v-u$ in the double integral has modulus at most $|u_a|+|u_b|\le Y$, where $\tau_Y$ is the identity. For (8.SQ1) group the partners of $a$ by columns. A column at transverse distance $\rho\ge1$ has ${\rm dist}_Y\ge\rho\ge\tfrac12$. At most $2\widehat Y+1$ of its sites have $|t|\le\widehat Y$, each contributing at most $\rho^{-3}$. On each side, the remaining offsets are $\theta+i$ with $\theta\in(0,1]$, $i\ge0$, and contribute at most $\rho^{-3}+\int_0^\infty(\rho^2+x^2)^{-3/2}dx=\rho^{-3}+\rho^{-2}$. Summing over the columns $m\in\mathbb Z^2\setminus0$ with $|m|_\infty<n$ uses $\sum|m|^{-3}<9.04$ and $\sum|m|^{-2}\le8H_{n-1}\le8\ell$. The column of $a$ has, on each side, at most $\widehat Y+\tfrac12$ offsets with ${\rm dist}_Y<\tfrac12$; the rest contribute at most $2.0002\,[8+(7\zeta(3)-8)]<16.831$. The source contributes less than $4\times10^{-5}$ at $n=2$ and less than $10^{-120}$ for $\ell\ge\ell_*$, inside the slack $33.67-2(2.0002)(7\zeta(3))>.009$. The operator norm is at most the largest absolute row sum of the Hessian, $2\widehat S^Y+\widehat S^Y$. $\square$

For $\ell\le\ell_*$ the comparator is exactly that of Sections 8.14 and 8.16.5, and the sharper (8.LG3) is used. For $\ell\ge\ell_*$ the envelope (8.SQ1) is used even where $\widehat Y<\tfrac12$ would allow less; it charges one core per side from the start. Row `SQ-LHAT` checks, on $n=2,3$ and $y_c\in\{.2,.35,.6,1.1\}$, that $\lambda_{\min}(\nabla^2\widehat V^Y)\ge-\widehat h^Y$ on column-collapse and random configurations; the largest negative eigenvalue found, $-1.65\times10^4$ at $y_c=1.1$, lies within $-1.02\times10^5$. The coincidence $\widehat V^Y_{ab}=V_{ab}$ for $|u_a|,|u_b|<y_c$ is checked by direct double integration of $\psi^Y$ (largest difference $2.8\times10^{-12}$, within the quadrature tolerance), and the out-region primitive against the same double integral (largest difference $2.1\times10^{-11}$ in the verifier run).

#### 8.17.2 The pointwise lower bound with a general threshold

Call a label *out* if $|u_a|>y_c$. For an out label with $U=|u_a|$ put $\ell'=U+y_c$ and
$$
\begin{aligned}
P^Y_{\rm near}(U)&=N_Bf'_{\max}+4\pi(1.8661+y_c)^2(3\ell'+.8661)+N'_Bf'_{\max}+4\pi c_2(2\ell'+.8661)+2f'_{\max},\\
P_{\rm far}(U)&=16.0016\,U\,(24\ell+2.4047),\\
y_Y(U)&=f_c(0)+y_c\bigl[P^Y_{\rm near}(U)+P_{\rm far}(U)\bigr]+y_c\widehat S^YU+\tfrac12\widehat S^YU^2 ,
\end{aligned}
$$
with $N_B=27$ for $y_c=\tfrac15$ and $N_B=(3+2y_c)^3$ otherwise, and $(c_2,N'_B)=\bigl((1.8661/(1-y_c))^2,0\bigr)$ for $y_c\le\tfrac12$, $\bigl(3.7322^2,(4y_c+1)^3\bigr)$ for $y_c>\tfrac12$.

**Lemma LOC-A$_Y$.** For every $x$ and $s$, $Z^Y_s(x):=V(u)-\widehat V^Y(u)\ge-\sum_{a\ \rm out}y_Y(|u_a|)$.

*Proof.* In–in pairs coincide by Theorem L-hat$_Y$. Out–out exact pairs are bounded below by $-f_c(0)|O|$ through the positive field energy of Theorem ST, exactly as in Lemma LOC-A. Convexified out–out and in–out pairs obey $|\widehat V^Y_{ab}|\le\widehat M_2^Y|u_a||u_b|$, and the Schur test gives the last two terms of $y_Y$. For an exact in–out pair with $b$ in, $V_{ab}=\int_0^{u_b}[\phi'_{ab}(v-u_a)-\phi'_{ab}(v)]dv$ and $|\phi'_{ab}|\le\min(f'_{\max},\rho^{-2})$.

- *Far partners* ($|d_{ab}|\ge2\ell'$). The mean-value theorem gives $|V_{ab}|\le y_c\,U\,16.0016|d_{ab}|^{-3}$, because every relevant distance is at least $|d_{ab}|/2\ge\tfrac12$. The lattice sum $\sum|d|^{-3}\le24\ell+2.4047$ includes the source.
- *First term, near partners.* The distance from site $b$ to the segment of half-length $y_c$ centred at $P=r_a+u_ae_z$ controls the first term. At most $N_B$ lattice points lie within $1+y_c$ of $P$. For the others and $y$ in the unit cube of $b$, this distance is at least $|y-P|/(1+y_c+\sqrt3/2)$. The cubes lie within $3\ell'+\sqrt3/2$ of $P$, and $\int_{|y|<\varrho}|y|^{-2}dy=4\pi\varrho$.
- *Second term.* This distance is at least $|d_{ab}|-y_c$. When $y_c\le\tfrac12$ it is at least $(1-y_c)|d_{ab}|$ for every lattice partner. When $y_c>\tfrac12$ the at most $N'_B$ partners with $|d_{ab}|<2y_c$ are bounded by $f'_{\max}$, and the others have distance at least $|d_{ab}|/2$. The same cube comparison, now within $2\ell'+\sqrt3/2$ of $r_a$, gives $4\pi c_2(2\ell'+.8661)$.
- *The source.* If it is a near partner it adds at most $2f'_{\max}$.

Multiplying by $|u_b|\le y_c$ proves the lemma. $\square$

At $y_c=\tfrac15$ the lattice constants reduce to those of Lemma LOC-A: $27$, $4\pi(2.0661)^2<53.65$ and $4\pi(1.8661/0.8)^2<68.38$. The source term is handled differently: when the source is an in-partner it contributes at most $y_c\cdot2f'_{\max}$, and when the source is the out label its partners are memories on a translate of $\mathbb Z^3$, so the lattice argument applies unchanged. (The inherited term $(2\ell'/39)f'_{\max}$ is not needed and is not claimed to be smaller.) Row `SQ-LOCA` evaluates both sides on 200 random and near-collision configurations of $n=2,3$ arrays for the four thresholds above; the smallest observed margin $Z^Y_s+\sum y_Y$ is $1290$. The bound has large slack, so this row is a sanity check that cannot discriminate small errors (an independent adversarial run found $\max(-Z/\sum y_Y)=1.3\times10^{-3}$).

#### 8.17.3 Energies, gap and ground states

**Lemma LOC-B$_Y$.** Lemma LOC-B holds for $\widehat H^Y(s)$, with the following changes. Write $y_Y(U)=Y_0+Y_1U+Y_2U^2$. The ramp $\chi$ rises on $[r_c,y_c]$, $r_c=\tfrac34y_c$, and $r_0=r_c-\mu_*$, $r_{\rm out}=y_c-\mu_*$ (written $r_1$ in Lemma LOC-B; renamed to avoid a clash with the direct-term error $r_1$ of Lemma SC). Moreover
$$
C_h\le\frac6{y_c}\sqrt{y_Y(y_c)}+\sqrt{Y_2+\frac{Y_1}{4r_c}},\qquad
E_1=2e^{-\widehat g_0r_0^2}\Bigl[Y_0+r_cY_1+r_c^2Y_2+\frac{Y_1+2Y_2\mu_*}{2\widehat g_0r_0}+\frac{Y_2}{\widehat g_0}\Bigr],\qquad
\zeta=N\bigl(4f_c(0)Ne^{-\widehat g_0r_{\rm out}^2}+E_1\bigr). \tag{8.SQ2}
$$

*Proof.* The proof of Lemma LOC-B applies verbatim to the convex comparator $\widehat H^Y(s)$, whose ground-state measure is strongly log-concave with constant $2\widehat g_0$, $\widehat g_0^2=\Omega^2-\widehat h^Y$. The bound on $C_h$ uses $|\chi'|\le6/y_c$ on the ramp. Beyond the ramp it uses
$$
\frac{(Y_1+2Y_2U)^2}{4(Y_1U+Y_2U^2)}=Y_2+\frac{Y_1^2}{4U(Y_1+Y_2U)}\le Y_2+\frac{Y_1}{4U}\qquad(U\ge r_c).
$$
In $\zeta$ the inherited proof used $f_c(0)N$ per out label, whereas $|V_{ab}|\le2f_c(0)$ over at most $N$ partners gives $2f_c(0)N$. The corrected value is used here (finding F31-04; the inherited certificate is unaffected at its $10^{-141}$ level). $\square$

An earlier form of this certificate used $\sqrt{Y_2+Y_1^2/(4Y_0)}$ for the second term. That form grows like $\ell^{3/4}$; by point evaluation it pushes $\theta(\tfrac12)$ above $\tfrac12$ at $\ell\approx3.01\times10^8$ and above $1$ at $\ell\approx1.16\times10^9$. The failure was found by the interval covering below and is retained as a fault-injection row.

#### 8.17.4 Refined $L^2$ majorants

Lemma SR needs a *pointwise* majorant matrix $K$ for the Hessian, to build $\Gamma=(\Omega^2-K)^{-1}$. Its right side, however, contains only *$L^2(\widehat\nu_s)$ norms* of the gradients of the two observables. Sections 8.14 and 8.16 used the pointwise majorants for both. With cores in the comparator this would make the squared row sum of Lemma PC grow like $D_2^2\widehat Y$ and $\mathcal Q_{\log}$ grow like $\ell^{1/8}$. The cores matter only on events of probability $e^{-c\Omega}$, and their $L^2$ weight is correspondingly small.

**Lemma SQ-L2.** Let $\ell\ge\ell_*$, $s\in\mathcal S$ and $P_{\rm off}:=4e^{-\widehat g_0(1/4-\mu_*)^2}$. Write $\widehat M_2^{(0)}(d)=2.0002(d-\tfrac12)^{-3}$ and $\eta=(2\widehat g_0)^{-1/2}$. For memories $a\ne b$ and every memory $j$,
$$
\|\partial_a\partial_b\widehat V^Y\|_{L^2(\widehat\nu_s)}\le\widehat M_2^{(0)}(d_{ab})+\widehat M_2^Y(d_{ab})\sqrt{P_{\rm off}},
$$
$$
\|\partial_j^2\widehat V^Y\|_{L^2(\widehat\nu_s)}\le2701.9\,(\lambda_e+\widehat\mu+\eta)+\widehat M_3^Y(r_{\min})(\lambda_0+\widehat\mu+\eta)+2\widehat S^Y\sqrt{P_{\rm off}},
$$
with $\widehat M_3^Y(r)=6.0006(r-\widehat Y)^{-4}$ for the source. The source entries keep their pointwise majorants $\widehat M_2^Y(r_{\min})=2.0002(r_{\min}-\widehat Y)^{-3}$ and $\widehat M_3^Y(r_{\min})$.

*Proof.* On the event $\{|u_a|,|u_b|\le\tfrac14\}$ every argument of $\psi^Y$ and its derivative has modulus at most $\tfrac12$, so $|\tau_Y|\le\tfrac12$ and the distance to the other charge is at least $|d|-\tfrac12$. There the old majorants $\widehat M_2^{(0)}$ and $6.0006(d-\tfrac12)^{-4}$ apply. The latter's row sum is the $2701.9$ of Section 8.14.4, applied with the mean value in $u_b$. The complementary event has probability at most $P_{\rm off}$ by Gaussian concentration under $\widehat\nu_s$. On it the pointwise majorants apply, and the diagonal entry is a difference of two values of $\psi^Y$. $\square$

Consequently Lemmas SC and PC hold for $\widehat H^Y$ with the following replacements:

- $\Gamma$ is built from the pointwise $K$, so $\widehat h^Y=3\widehat S^Y$ and $K_{00}\le2n^3\widehat M_2^Y(r_{\min})$;
- the $L^2$ row sum is $S_{L2}:=48.0048\ell+438.09+\widehat S^Y\sqrt{P_{\rm off}}$;
- the squared row sum is $S_{22}:=\bigl(\sqrt{6696.8}+\sqrt{D_2\widehat S^Y}\sqrt{P_{\rm off}}\bigr)^2$, by Minkowski's inequality and $\widehat M_2^Y\le D_2$;
- in the direct constant $2.9858$ of Lemma PC the off-event term becomes $2D_2(\widehat Y+\tfrac12)^3e^{-\widehat g_0(1/8-2\lambda_e-2\widehat\mu)^2/2}$, since $r^3\widehat M_2^Y(r)\le D_2(\widehat Y+\tfrac12)^3$.

All distances and cutoffs in Lemma SC concern the source pair, which stays at distance at least $19.5n-\widehat Y$, and are unchanged.

#### 8.17.5 Theorem NP-SQRTLOG

**Theorem NP-SQRTLOG (square-root-logarithmic confinement, full model, P1 preparation).** Use the exact regularized neutral-Coulomb Hamiltonian, the S9 geometry, window and observable of Section 2, the P1 preparation $\Psi_0$ (exact ground state of $H_{\rm MC}(0)$) and
$$
\Omega_R=10^4\sqrt{1+\log\lceil R^{1/3}\rceil}\;\le\;10^4\sqrt{1.4621+\tfrac13\log R}.
$$
Then for every integer $R\ge2$, every memory $j$ and every $t\in I_R$,
$$
\boxed{D_j(t)\ge.98853>.9885.}
$$

*Proof.* Fix $R$ and use the comparator $\widehat V^{Y}$ with $y_c=y_c(\ell_n)$ of (8.SQ0). Put $E_0(z)=\mathcal E(\Lambda z)$ and $\widehat E_0(z)=\widehat{\mathcal E}^Y(\Lambda z)$.

*Step 1 (echo).* As in Step 1 of Theorem NP-LOG,
$$
\varepsilon_z\le\bigl(2\sqrt{\varepsilon_{\rm loc}}+\sqrt{\widehat\varepsilon}\bigr)^2,
$$
with $\varepsilon_{\rm loc}$ from Lemma LOC-B$_Y$(3). Here $\widehat\varepsilon<4\widehat\sigma^2/\widehat g_0^2$ is the convex-interpolation bound of Section 8.2 with the majorants of Theorem L-hat$_Y$. Appendix A gives $|D_j-D_j^{E_0}|\le8\max_z\varepsilon_z$ for all $t$.

*Step 2 (energies).* Lemma LOC-B$_Y$(1) gives $|D_j^{E_0}-D_j^{\widehat E_0}|\le2T\delta_3$ with $\delta_3=\delta_E(1)+\zeta$.

*Step 3 (readout).* Lemma RD-V and Lemmas SC and PC give (8.RV4) for $\widehat E_0$ (for $\ell\ge\ell_*$, in the form of Section 8.17.4). Therefore
$$
D_j(t)\ge\cos\frac{\pi e_*}2-L_{\rm pair}^{\log}-1.71342\,(r_1+r_{\rm SR})-2T\delta_3-8\max_z\varepsilon_z . \tag{8.SQ3}
$$

*Step 4 (all-$n$ certificate).* Treat $n=e^{\ell-1}\ge2$ as real. Every quantity in (8.SQ3) and in the side conditions ($\theta(\tfrac12)<1$, $\gamma_*>0$, $\widehat\sigma<\widehat g_0/4$, direct PC constant $\le2.9858$) is an explicit elementary function of $\ell$. After the powers of $n$ are cancelled analytically, it is evaluated in outward interval arithmetic (40 digits) with $\ell$ itself an interval. Each enclosure is therefore valid for every real $\ell$ in its subinterval.

- *Covering.* 7077 subintervals cover $[1+\log2,10^{15}]$: ratio $1.002$ up to $10^6$, ratio $1.02$ up to $10^9$ and ratio $1.2$ up to $10^{15}$. Regime A (the fixed comparator of Section 8.16.5) is used on $[1+\log2,100]$ and regime B (8.SQ0) above.
- *Beyond $10^{15}$.* For $\ell\ge10^{15}$ every readout error term is a product of nonnegative factors, each nonincreasing in $\ell$ (*v2.2.1 correction, F32-03:* v2.2 stated this for $\ell\ge\ell_*$; see the note after this list):
  - $S_{\rm env}/\ell$, $S_{L2}/\ell$ and $\widehat h^Y/\Omega^2$ decrease, and $\widehat g_0/\sqrt\ell$ increases.
  - $\widehat S^Y\sqrt{P_{\rm off}}$ decreases, since $d\log$ of it is at most $1/\ell-70/\sqrt\ell<0$.
  - $\widehat M_2^Y(r_{\min})/\kappa_s\propto(19.5-\widehat Y/n)^{-3}$ decreases.
  - The source products $n^3\widehat M_3^Y\widehat M_2^Y/\kappa_s\propto n^{-1}(19.5-\widehat Y/n)^{-7}$ decrease.
  - $C_h^2/\ell$ decreases and $\widehat g_0^2/\ell$ increases, so $\theta$ decreases.
  - $\widehat g_0r_0^2\ge22.1\,\ell$, hence $\log(2T\delta_3)\le c_0+\log{\rm poly}(\ell)-13\ell$, and $\gamma_*$ increases.
  - In $\widehat\sigma^2$, $n^3(\widehat h\lambda_e+\widehat M_2^Y\lambda_0)^2\propto\ell^2e^{-3\ell}$ and $(n^3\widehat M_2^Y)^2\propto(19.5-\widehat Y/n)^{-6}$ decrease, while $\widehat g_0$ increases; so $\widehat\sigma/\widehat g_0$, $\widehat\varepsilon$ and the echo term decrease.
  - The off-event part of the PC constant has $\frac{d}{d\ell}\log[(\widehat Y+\tfrac12)^3e^{-\widehat g_0c}]\le\frac3{4\ell}-\frac{10^4c}{2\sqrt\ell}<0$.

  Row `SQ-TAIL` evaluates all these factors at $\ell=10^9,10^{11},\dots,10^{19}$ and finds each nonincreasing, with $\log_{10}(2T\delta_3)/\ell\approx-5.86$. This row is a numerical diagnostic (class V, F32-01), not a proof; the proof is the list above.

  So on $[10^{15},\infty)$ every term is bounded by its value on the last subinterval.

  *v2.2.1 note (F32-03).* v2.2 stated the list above for all $\ell\ge\ell_*$. That is too broad. At $y_c=\tfrac12$, i.e. $\ell=100\cdot2.5^4=3906.25$, the pair $(c_2,N'_B)$ of Lemma LOC-A$_Y$ changes branch: $c_2$ is continuous there, but $N'_B$ jumps from $0$ to $27$. Hence $Y_0$ jumps from $6657.15$ to $9270.43$, and $\theta(\tfrac12)$ rises from $7.7709\times10^{-4}$ at $\ell=3906.249$ to $7.8133\times10^{-4}$ at $\ell=3906.251$. The theorem is unaffected. The interval $[\ell_*,10^{15}]$ is covered by the certificate, whose enclosures use no monotonicity. On the subinterval that straddles the switch the code uses the $y_c>\tfrac12$ form, which is also a valid, weaker bound for $y_c\le\tfrac12$: for $|d_{ab}|\ge2y_c$ the distance $|d_{ab}|-y_c$ is at least $|d_{ab}|/2$, and $N'_B\ge0$. For $\ell\ge10^{15}$, $y_c=\tfrac15(\ell/100)^{1/4}>355$, so no branch switches there (row `V221-TAIL-SCOPE`). The frozen v2.2 audit also reconstructed this tail from the explicit formulas, without sampled extrapolation, and obtained $D>.98854476310$ on $[10^{15},\infty)$ (Appendix S.2).

The worst values over all $\ell\ge1+\log2$ occur on the first subinterval:

| Quantity | Certified bound, every $R\ge2$ |
|---|---:|
| $\widehat h/\Omega^2$ | $<9.206\times10^{-6}$ |
| $r_{\rm SR}$, $r_1$ | $<3.845\times10^{-6}$, $<3.678\times10^{-7}$ |
| $\mathcal Q_{\log}$, $L^{\log}_{\rm pair}$ | $<2.646\times10^{-4}$, $<1.30151\times10^{-3}$ |
| direct PC constant | $<2.985722$ |
| $\theta(\tfrac12)$ | $<.02796$ |
| $\gamma_*$ (lower) | $>6506$ |
| $2T\delta_3$ | $<10^{-102.88}$ |
| $8\max_z\varepsilon_z$ | $<3.31\times10^{-24}$ |
| right side of (8.SQ3) | $>.98853906781$ with the exact factor $1.7134107\ldots$ of the code; $>.98853906777$ with the printed coefficient $1.71342$ (v2.2.1, F32-02) |

The frequency bound uses $n^3\le4R$. $\square$

In the fixed-threshold regime $\ell\le\ell_*$ the comparator part of the bound reproduces the v2.1 value $\widehat D\ge.9885390698$ (Theorem COMP-SQRTLOG) from independently written code. The covering therefore also certifies COMP-SQRTLOG on $[1+\log2,100]$ without its monotonicity argument. The energy term $2T\delta_3$ is largest at $n=2$; its exponent $9\ell-\widehat g_0r_0^2\approx9\ell-225\sqrt\ell$ is convex, so on that range it is maximal at an end point. Rows `SQ-CERT` (covering), `SQ-TAIL` (the monotone factors at $10^{15}$) and `SQ-FAULTS` record the checks. The fault injections behave as they must:

- keeping $y_c=\tfrac15$ for all $\ell$ fails at $\ell\approx5.9\times10^2$ (the energy term $2T\delta_3$ exceeds the margin);
- the old $C_h$ form makes $\theta(\tfrac12)\ge1$ at $\ell\approx1.16\times10^9$;
- pointwise instead of $L^2$ majorants make $\mathcal Q_{\log}$ grow, from $4.0\times10^{-3}$ at $\ell=10^4$ to $7.3\times10^{-2}$ at $10^{15}$, against a constant $3.93\times10^{-5}$ for the refined form;
- dropping the core term $2D_2(\widehat Y+\tfrac12)$ from (8.SQ1) violates the Hessian bound in row `SQ-LHAT` at $y_c=.6$ and $1.1$.

*v2.2.1 note (F32-02).* The v2.2 row `SQ-CERT` accepted a subinterval when the lower enclosure of the right side of (8.SQ3) exceeded $.9885$, which is weaker than the stated $.98853$. It started the covering at the double-precision value of $1+\log2$, which exceeds the exact value by $8.8\times10^{-17}$, so the point $\ell=1+\log2$ ($n=2$) was formally outside the covering. It also used the exact factor $1.01\cdot\tfrac\pi2(40/39)^3\cdot1.001=1.7134107\ldots$ where (8.SQ3) prints $1.71342$. A PASS of that row therefore did not by itself certify the stated constant. Row `V221-SQ-CERT-98853` reruns the 7077 subintervals with the gate $.98853$, the outward lower enclosure of $1+\log2$ as first end point and the printed coefficient $1.71342$, together with all side conditions. It passes. The minimum, on the first subinterval, is $>.98853906777$, so the margin above the stated $.98853$ is at least $9.06\times10^{-6}$; the margin above $.9885$ is $3.9\times10^{-5}$. Row `V221-SQ-GATE-FAULT` lowers the right side by $2\times10^{-5}$ on the first subinterval: the old gate accepts the result and the new gate rejects it. The theorem and its constants are unchanged.

#### 8.17.6 Scope

- *What is proved.* A sub-logarithmic ($\sqrt{\log R}$) confinement law with $D_j\ge.9885$ holds for the exact non-convex Coulomb Hamiltonian, the P1 preparation, every memory, both source labels and the whole growing window. This is the second alternative of the user-fixed grade-4 criterion (Section 13.12).
- *Why $\sqrt{\log}$ is the limit of this route.* The comparator must be uniformly convex, so its absolute dipolar Hessian row sum, of order $16\ell$ in (8.SQ1), must stay below $\Omega^2$. Any argument that bounds the Hessian of a convex comparison potential by absolute values therefore needs $\Omega\gtrsim\sqrt\ell$. Within this route a faster law would need signed estimates (Sections 8.15 and 8.18); other routes are not excluded. The heuristic $(\log R)^{1/4}$ of Section 8.16.3 remains unproved in either direction.
- *Not changed.* The Gaussian preparation is untouched: Theorem NP-G ($R^{1/5}$) is unchanged, and no polylogarithmic law is claimed for $\Phi$. P1 remains a declared preparation, and the physical bridges of Section 14 are unchanged.
- *Proof status.* All analytic steps are proofs in the stated generality, together with the standard Feynman–Kac–Trotter limits cited in Lemma SR. The choice $\ell_*=100$ and the growth exponent $\tfrac14$ are design parameters fixed before the certificate was run. The constants are interval-certified. No proof assistant was used.

### 8.18 A one-way reduction of the source-edge problem to a continuum edge statement

Section 8.16.1 reduced the source coefficient of the quadratic model to the driven resolvent $w(B^{-1}v)_j/v_j$. It left open how that response relates to the uniform-drive factor ${\rm LF}_j$ and to Hypothesis EG. This section removes the lattice-specific part of the question. Weak compactness and uniqueness show that the lattice response for *any* smooth drive, in particular the actual S9 source row, is unbounded near an edge whenever the corresponding continuum solution is. The lattice transfer between drives, the source-oscillator feedback and the all-scale lattice analysis therefore drop out. A single classical statement about a uniaxial dielectric cube therefore *suffices*. The reduction is one-way: if the continuum solution were bounded, nothing would follow for the lattice, because a weak limit does not see boundary layers one lattice spacing thick.

**Setting.** Consider the quadratic model of Section 13.3 on full cubes $R=n^3$ at a fixed $w=\Omega_0^2>8g$. Take cells $C_a=a/n+[0,1/n)^3$ with centres $\xi_a=(a+\tfrac12\mathbf 1)/n$ in $Q=[0,1]^3$. The memory position relative to the source is exactly $r_a=n(\xi_a-\tfrac12\mathbf 1+20e_z)$, so by homogeneity
$$
v_a=K_{0a}=-\frac{2}{L^3}f(\xi_a),\qquad f(\xi):=-\tfrac{20^3}{2}K\bigl(\xi-\tfrac12\mathbf 1+20e_z\bigr),
$$
with $f$ real-analytic and positive on $\overline Q$; its range on $\overline Q$ is $[.9252,1.0790]$, the maximum $8000/19.5^3$ being attained at $\xi=(\tfrac12,\tfrac12,0)$. For a drive $u\in\{f,\mathbf 1\}$ put $y^{(n)}:=w(wI+gK_m)^{-1}u(\xi_\cdot)$. Then ${\rm LF}_j=y_j$ for $u=\mathbf 1$ and $F_j=y_j/(f(\xi_j)(1-q))$ for $u=f$, by (8.SRX1).

**Continuum operator.** For $P\in L^2(Q)$ let $T_QP=\mathbf 1_QT(\mathbf 1_QP)$, where $T$ is the principal-value convolution with $K(d)=(1-3\cos^2\theta)/|d|^3$. Its Fourier multiplier is $4\pi(\xi_z^2/|\xi|^2-\tfrac13)\in[-\tfrac{4\pi}3,\tfrac{8\pi}3]$. Hence $w+gT_Q\ge w-\tfrac{4\pi}3g>0$, and $P_u:=w(w+gT_Q)^{-1}u$ is the unique $L^2(Q)$ solution. It is the polarization of a uniaxial Clausius–Mossotti cube, $\varepsilon_{zz}=\varepsilon(\Omega_0)$ of Section 8.15.3, in the external field $u$. The volume-integral-operator formulation and its spectral theory are standard (Costabel, Darrigrand and Sakly 2012 for smooth interfaces); only the elementary coercivity bound is used here.

**Lemma CR-1 (lattice sums of test functions).** For $\varphi\in C_c^\infty({\rm int}\,Q)$,
$$
\sup_{a\in\mathbb Z^3}\Bigl|\sum_{b\ne a}K(b-a)\varphi(\xi_b)-(T\varphi)(\xi_a)\Bigr|\le\frac{C_\varphi}n .
$$

*Proof.* Since $\varphi(\xi_b)=0$ for $b\notin B_n$, the sum runs over the full lattice, and $K(b-a)=n^{-3}K(\xi_b-\xi_a)$. Fix $r_0>0$ and split the lattice into the ball $\{|b-a|<nr_0\}$ and its complement; split the continuum integral at $|\eta-\xi_a|=r_0$ correspondingly.

- *Complement.* Here the summand $n^{-3}K(\xi_a-\eta)\varphi(\eta)$ is sampled at $\eta=\xi_b$, a smooth compactly supported function of $\eta$ on $\{|\eta-\xi_a|\ge r_0\}$. The midpoint rule gives error $O(1/n)$, and the cells cut by the sphere contribute $O(n^2)\cdot n^{-3}$.
- *Ball.* Write $\varphi(\xi_b)=\varphi(\xi_a)+\nabla\varphi(\xi_a)\cdot(\xi_b-\xi_a)+R_a(\xi_b)$ with $|R_a(\eta)|\le C|\eta-\xi_a|^2$ and $|\nabla R_a|\le C|\eta-\xi_a|$. The constant and linear sums over the lattice ball vanish exactly, by invariance of the lattice ball and of $K$ under permutations of the coordinates (giving $\sum K=0$) and by parity. The corresponding principal-value integrals over the continuum ball also vanish.
- *Remainder in the ball.* The function $g(\eta)=K(\xi_a-\eta)R_a(\eta)$ obeys $|g|\le C|\eta-\xi_a|^{-1}$ and $|\nabla g|\le C|\eta-\xi_a|^{-2}$. Its midpoint sum over the cells with $|\xi_b-\xi_a|\ge2/n$ differs from the integral by at most $Cn^{-1}\int_{|\eta-\xi_a|<r_0}|\eta-\xi_a|^{-2}d\eta=O(1/n)$. The cells within $2/n$, including the omitted self-cell, contribute $O(n^{-2})$ to both sides.

The constants depend only on $\varphi$ and $r_0$. $\square$

**Theorem CR (continuum reduction).** Let $w>8g$ and $u\in\{f,\mathbf 1\}$, and let $P_n:=\sum_ay^{(n)}_a\mathbf 1_{C_a}$.

1. $P_n\rightharpoonup P_u$ weakly in $L^2(Q)$.
2. Let $U\subset\mathbb R^3$ be open. If $P_u$ is not essentially bounded on $U\cap Q$, then $\max\{|y^{(n)}_a|:C_a\cap U\ne\varnothing\}\to\infty$ as $n\to\infty$.

*Proof.* (1) The memory block satisfies $K_m\ge-8I$ (Appendix B). Hence
$$
\|P_n\|_{L^2(Q)}^2=n^{-3}\|y^{(n)}\|^2\le\frac{w^2}{(w-8g)^2}\max_{\overline Q}|u|^2 .
$$
Let $P$ be a weak limit along a subsequence and $\varphi\in C_c^\infty({\rm int}\,Q)$. Pairing $(wI+gK_m)y=wu$ with the samples of $\varphi$ and using the symmetry of $K$ gives
$$
\int_QP_n\,\Bigl(w\bar\varphi_n+g\,\overline{K\varphi}_n\Bigr)=n^{-3}\sum_a\varphi(\xi_a)wu(\xi_a),
$$
where the bars denote step functions of the samples. Lemma CR-1 and the smoothness of $T\varphi$ (a Calderón–Zygmund image of a test function; $T_Q\varphi=T\varphi$ on $Q$) make the bracket converge uniformly to $w\varphi+gT_Q\varphi$. In the limit $\int_QP(w\varphi+gT_Q\varphi)=\int_Qwu\varphi$. By the symmetry of $T_Q$, $(w+gT_Q)P=wu$ a.e., so $P=P_u$. Every subsequence has the same limit, which proves (1).

(2) Suppose instead that a subsequence satisfies $|y^{(n)}_a|\le M$ on the cells meeting $U$. Then $P_n\mathbf 1_{U\cap Q}$ has a weak-$*$ limit in $L^\infty$ of norm at most $M$. By (1) it coincides with $P_u$ on $U\cap Q$, a contradiction. $\square$

**Corollary CR-R (record failure at fixed confinement, conditional on the continuum).** Suppose that for some $w=\Omega_0^2>8g$ the continuum source solution $P_f$ is essentially unbounded near some point of $\overline Q$. Then there is $n_0$ with the following property. For every full cube $R=n^3$ with $n\ge n_0$, the quadratic model with common preparation $\Phi_G$ at this fixed confinement has a memory $j$ and a time $t\in I_R$ with
$$
D^G_j(t)\le2\varepsilon_Q=O_w(n^{-3}).
$$
The same hypothesis for $P_{\mathbf 1}$ gives $\sup_j|{\rm LF}_j(n)|\to\infty$.

*Proof.* By Theorem CR, $\max_j|y_j|\to\infty$. With $f_j=-L^3K_{0j}/2=f(\xi_j)$, one has $f_j|F_j|=|y_j|/(1-q)\ge|y_j|$, and $q=O_w(n^{-3})$ by (8.SRX1). Once $f_j|F_j|\ge1/\eta=100$, the phase interval of Lemma WO has half-length at least $\pi/2$ and $M=0$. Estimate (13.4), valid because $\Delta_G^2=w-8g>0$, bounds $\varepsilon_Q$. $\square$

**Hypothesis EG-C (continuum edge unboundedness).** For every $w>8g$, the solution $P_f$ of $(w+gT_Q)P=wf$ is essentially unbounded near the midpoint of at least one horizontal edge of $Q$.

Theorem CR shows that EG-C implies lattice unboundedness for the actual S9 source row, and Corollary CR-R shows that it implies record failure at every fixed confinement. EG-C does not give the rate $n^{\gamma}$ of Hypothesis EG, and EG itself (a lattice rate statement for the uniform drive) is neither implied nor needed for that consequence. Heuristically, in the language of edge asymptotics, EG-C would follow if the coefficient $c(x)$ of the singular transmission mode $r^{\nu}$ of Proposition W, excited by the external field $f$, did not vanish near the midpoint of a horizontal edge. That translation assumes an edge expansion for the cube, which is not proved here: Proposition W treats an infinite two-dimensional wedge, and the cube also has corners. The vertical edges carry no such mode, because the cross-sectional medium there is isotropic. The corners carry a vertex problem not analysed here.

**Remark CR-H (a log-scale reduction; heuristic, not a proof).** Near an interior point $x_0$ of a horizontal edge, describe $P_f$ at transverse scale $r$ by an angular profile $\Theta_r(\psi)$, $\psi\in(0,\tfrac\pi2)$. Split $T_QP$ at that scale into three parts:

- a far-field constant $C_{\rm far}$;
- the accumulated contribution $\int_r^{r_0}m(r')\,dr'/r'$ of the intermediate scales, where $m(r')=\langle k,\Theta_{r'}\rangle$ and $k(\psi)=2\cos2\psi$ is the angular part of the kernel integrated along the edge. This is the mechanism behind Theorem EL.
- a same-scale operator $\widehat T_0\Theta_r$.

With $C(r)=C_{\rm far}+\int_r^{r_0}m\,dr'/r'$ the angular equation reads $(w+g\widehat T_0)\Theta_r\approx f(x_0)-gC(r)$. Hence
$$
\Theta_r\approx\bigl(f(x_0)-gC(r)\bigr)\Theta_0,\qquad \Theta_0:=(w+g\widehat T_0)^{-1}\mathbf 1,\qquad
\frac{dC}{d\log(1/r)}\approx A_0\bigl(f(x_0)-gC\bigr),\quad A_0=\langle k,\Theta_0\rangle .
$$
Since $\langle k,\mathbf 1\rangle=0$ and $\langle k,\widehat T_0\mathbf 1\rangle=2$ (the constant of Theorem EL(1)), $A_0=-2g/w^2+O(g^2/w^3)$. Therefore $f(x_0)-gC(r)\propto r^{-\gamma}$ with $\gamma=-gA_0=2g^2/w^2+O(g^3/w^3)$, which reproduces $\gamma\Omega^4\to2$ of Proposition W. The amplitude is proportional to $f(x_0)-gC(r_0)$. A bounded solution would require the single scalar identity $gC(r_0)=f(x_0)$ up to the accumulated corrections. With $|h_S|\le15.663$ the far field is heuristically of order $15.7gf/w$, which suggests EG-C at least for $w\gtrsim16g$. A proof would need three estimates that are not supplied:

- (L1) a quantitative bound for $T_Q$ acting on profiles that vary slowly in $\log r$;
- (L2) control of the variation along the edge (a commutator with a cutoff in $x$);
- (L3) a bound on $C_{\rm far}$ from the global $L^2$ estimate.

Status: [가설].

**What Section 8.18 changes.** Before it, the actual source row required an all-scale lattice amplitude estimate for $B^{-1}v$, separately from $B^{-1}\mathbf 1$ (Section 8.16.1). After it, any continuum unboundedness statement transfers to the lattice for every smooth drive, and the obstruction consequence follows. Row `CR-WEAK` illustrates the weak convergence: the $4^3$ coarse averages of $y^{(n)}$ for the actual source at $w=10$ change by $6.4\times10^{-3}$ from $n=16$ to $32$ and by $3.5\times10^{-3}$ from $32$ to $64$. The maximum over the two edge-adjacent rows grows slowly ($1.349,1.372,1.390$). These are finite diagnostics, not evidence for EG-C beyond what Section 8.15 already reports. EG-C itself, with or without a rate, remains open.

## 9. Earlier scalar and first-Duhamel certificates

**Theorem C, quadratic first Duhamel.** Replace the dressed state estimate by

$$
\|(U_{\rm MC}(t)-U_{Q+m}(t))\Phi\|\le t\sup_{s\le t}\|F_s\Phi\|.
$$

The global phase correction (7.1), Gaussian signal correction (4.8) and full-space tail bounds are still required. Since the leading residual standard deviation is $O(\sqrt N\Delta^{-3/2})$, the condition $2T\sup\sigma_W\le\varepsilon_d$ admits $\Omega=O(R^{5/3})$.

The original seed expression already contained a Frobenius Hessian term:

$$
\sigma_W^2\le\frac1{2\Delta}\left[2N(gS_4)^2m_4+
\frac{\|H_z^{\rm rem}\|_F^2}{\Delta}+2\|H_z^{\rm rem}\|^2\xi_R^2\right]+\tau_{\rm tail}. \tag{9.1}
$$

Here $m_4$ is the fourth coordinate moment bound and $\tau_{\rm tail}$ the exceptional-event contribution. Version 1.0 replaced the Frobenius structure by a replicated row estimate; that change caused F20-01. The present Section 5 restores the correct structure and extends it to $L^4$.

**Theorem D, scalar product-vacuum comparison.** Let $\Phi_\Omega$ be the product ground state of $H_0$, compare with $H_0+E_{\rm cl}(z)$, and put

$$
Q_N=\frac{h^{(L)}_N\sqrt{N(N+2)}}4,\qquad
r_\Omega=\frac{A_R}{\sqrt{2\Omega}}+\frac{Q_N}{\Omega}.
$$

A sufficient coarse choice is

$$
\Omega_R=\max\left\{4B_N,\;B_N(1+2/\varepsilon_p),\;
\frac{8T^2A_R^2}{\varepsilon_d^2},\;
\frac{4TQ_N}{\varepsilon_d}\right\}. \tag{9.2}
$$

The branch gap is at least $\Omega_R/2$. For the switched-off interacting ground preparation, the bounded-perturbation comparison gives $q\le B_N/(\Omega-B_N)$; for the product vacuum set $q=0$. Then

$$
|D_j-D_j^{\rm cl}|\le2q+2tr_\Omega. \tag{9.3}
$$

Choosing the preparation and Duhamel allowances within the readout margin yields $D_j>.984$. With $h^{(L)}_N=O(R^{1/3})$ the $Q_N$ term improves, but $B_N=O(N^2)$ still makes (9.2) an $O(R^4)$ choice; the coarse route is not sharpened further here. This proof uses the frozen pair energy and therefore only its frozen/dipole error, not an omitted Gaussian energy term.

The historical finite-$R$ Duhamel and Monte Carlo comparisons are retained in Appendix H as source-reported diagnostics. They neither establish the all-$R$ theorem nor validate a regime in which the theorem's assumptions fail.

## 10. Simultaneous scaling and sudden preparation in auxiliary models

### 10.1 A convex dipole model

Consider $H_{\rm cv}=H_G+W_{\rm cv}(x)$ with label-independent convex $W_{\rm cv}$ and a uniform positive gap $\Delta$. For a multiplication operator $X$, the oscillator sum rule is

$$
\sum_{m>0}(E_m-E_0)|\langle m|X|0\rangle|^2
=\tfrac12\langle|\nabla X|^2\rangle. \tag{10.1}
$$

Differentiating the positive ground state along a control path and applying the gap twice gives
$\|\partial_s\psi_s\|^2\le\sup|\nabla\partial_sH|^2/(2\Delta^3)$.
For S9 the label force obeys

$$
\|F_Gz\|\le M_R=
\frac{g\lambda_0\sqrt R}{n^3}\left(\frac{2f_+}{20^3a^3}+\frac{16\chi_{\rm design}}{a^3}\right).
$$

The infidelity from the common switched-off ground state is at most $M_R^2/(2\Delta^3)$. Appendix A yields

$$
\sup_{t,z,j}|\mathcal A_j(t)e^{i\Delta E_jt}-1|
\le\frac{4M_R^2}{\Delta^3}=O(R^{-1}) \tag{10.2}
$$

at fixed positive $\Delta$. This compares with the exact ground-energy phase. It does not establish that this phase writes a readable record. Theorem Q in Section 13.3 supersedes this remark for the purely quadratic case $W_{\rm cv}=0$: there the echo and the readout are computed exactly.

### 10.2 The hard-wall auxiliary model

For $|x_a|<b$ with Dirichlet boundary, let $b'=b+\lambda_{\max}$, $a-2b'\ge2c$, and define

$$
E_3\le\frac{4500(1+\theta_c)b'}{a^4(1-2b'/a)^4},\quad
\kappa_{\rm box}=16/a^3+\delta_c+E_3,\quad
\Delta_{\rm box}^2=\Omega^2-g(8/a^3+\delta_c+E_3)>0. \tag{10.3}
$$

Here $\theta_c$ is a third-derivative regularization allowance; $.0001$ suffices in the S9 box. Put

$$
m_R=\frac{6(1+\theta_c)}{(r_{\min}-2b')^4},\qquad
k_R=\frac2{r_{\min}^3}+3.4c^{-3}e^{-r_{\min}^2/c^2}+2b'm_R,
$$

$$
q_R=\sqrt{(b'Rm_R)^2+Rk_R^2},\qquad
M_R^{\rm box}=g(\lambda_0q_R+\kappa_{\rm box}\lambda_e\sqrt R).
$$

The same argument gives an all-time echo error at most
$4(M_R^{\rm box})^2/\Delta_{\rm box}^3=O(R^{-2/3})$. This auxiliary theorem has hard walls; it is not substituted for the wall-free theorem. At fixed single-coordinate Gaussian tail probability $p>0$, even the uncoupled vacuum has
$\Pr(\exists a:|X_a|>b)=1-(1-p)^N\to1$. Removing the walls therefore needs the full-space analysis, not an informal claim that every coordinate is individually well confined.

### 10.3 Occupied-spectrum finite-window criterion

If an occupied spectral distribution has weights $p_m$ and phase-frequency deviations $\delta_m$ from a chosen reference, then

$$
\left|\sum_m p_m(e^{-it\delta_m}-1)\right|
\le |t|\left(\sum_m p_m\delta_m^2\right)^{1/2}. \tag{10.4}
$$

This follows from $|e^{-iu}-1|\le|u|$ and Cauchy–Schwarz. It is a finite-window criterion for the actually occupied spectrum, not an all-time claim that small frequency errors cannot accumulate. Here $p_m\ge0$ and $\sum_m p_m=1$ are hypotheses. They are not automatic for a noncommuting pair of Hamiltonians, whose exact double-spectral coefficients can be complex. The supplied seed's preserved lineage contains S19-R in Section 8 and S19-FW in Section 10, including equations (S19R.3) and (S19FW.1); these are internal proposition labels, not the separate corpus paper ZS-S19. If a matched occupied-spectrum expansion obeys $|A(t)e^{it\delta}-\sum_mp_me^{-it\delta_m}|\le\eta$, the restored criterion is

$$
|A(t)e^{it\delta}-1|
\le\eta+\sum_m p_m\min\{2,T|\delta_m|\}
\le\eta+T\left(\sum_m p_m\delta_m^2\right)^{1/2},\quad |t|\le T. \tag{10.FW1}
$$

For finite spectra, one sufficient matching error is $\eta=\sum_{m,n}|q_{mn}-p_n\delta_{mn}|$, where $q_{mn}$ are the exact double-spectral coefficients after choosing a pairing of eigenstates. This does not assume exact simultaneous diagonalization. The triangle inequality proves the claim; infinite spectra additionally require the relevant absolute convergence. The phase $\delta$ and the differences $\delta_m$ must be tied to the physical branch flips. This criterion is inherited from the supplied seed, not a new v1.8 theorem.

## 11. Preparation, ramps and cooling

### 11.1 Convexity gaps

The Hessian condition in (10.3) gives a gap at least $\Delta_{\rm box}$ by the one-dimensional comparison and Riccati argument in Appendix C. For the wall-free model and interpolation (8.4), use the modulus $\Omega^2-h^{(L)}_N$ and exhaust the whole space by convex domains. Compact-resolvent convergence and the min–max principle pass the first two eigenvalues to the limit. The argument keeps the factor of two from $2H=-\Delta_x+2U$ explicit.

### 11.2 Pre-event branch-dependent preparations

If the preparation vectors differ between the two memory branches, set
$\varepsilon_\pm=1-|\langle\Omega_\pm,\Phi_\pm\rangle|^2$ and let $\widehat\Phi_\pm$ be the normalized ground projections with compatible phases. Appendix A-prime proves

$$
\left|\mathcal A(t)e^{i(E_+-E_-)t}-\langle\widehat\Phi_-,\widehat\Phi_+\rangle\right|
\le s+s^2,\qquad s=\sqrt{\varepsilon_-}+\sqrt{\varepsilon_+}. \tag{11.1}
$$

The former $O(\varepsilon)$ distinct-vector assertion is withdrawn. A two-dimensional example at $t=0$ violates it by about a factor 35.2. For S9 auxiliary pre-event preparations with $\varepsilon=O(R^{-1})$, the general comparison is $O(R^{-1/2})$. Exact harmonic branch ground preparations have zero such projection error, but their cross-branch overlap still belongs in the formula. None of these branch-dependent protocols is silently used by Theorem HP-prime.

### 11.3 A phase-sensitive adiabatic bound

Let $H(s)$, $0\le s\le1$, have a common self-adjoint domain, a positive normalized simple ground state, gap at least $\Delta$, and bounded norm-continuous first two derivatives. Write $M_1=\sup\|H'\|$, $M_2=\sup\|H''\|$. For physical duration $\tau$,

$$
\left\|U(\tau)\psi(0)-e^{-i\tau\int_0^1E(s)ds}\psi(1)\right\|
\le\frac{C_{\rm ad}}\tau,\qquad
C_{\rm ad}=\frac{2M_1+M_2}{\Delta^2}+\frac{9M_1^2}{\Delta^3}. \tag{11.2}
$$

The positive real gauge has zero Berry connection. With the reduced inverse $\mathcal R_s$, $\psi'=-\mathcal R_sH'\psi$. The trial correction $(i/\tau)\mathcal R_s\psi'$ cancels the leading derivative; bounding its derivative and both endpoints gives (11.2) by unitary Duhamel. This is an explicit adiabatic integration-by-parts specialization, not a new general adiabatic principle.

For the box path $h(s)=r(s)(0,\lambda_ez')$, $r(s)=3s^2-2s^3$, take

$$
U_1=g\kappa_{\rm box}b'\lambda_e\sqrt{RN},\qquad U_2=g\kappa_{\rm box}\lambda_e^2R,
\quad M_1\le\tfrac32U_1,\quad M_2\le6U_1+\tfrac94U_2. \tag{11.3}
$$

The output dynamical phase can contain many-label Walsh components. Its acceptable record budget must be proved separately.

### 11.4 Harmonic ramps and environment Gram matrices

For a harmonic normal mode of frequency $\omega_k$ and varying force $f_k(t)$,

$$
Q_{\rm ramp}=\sum_k\frac1{2\omega_k^3}
\left|\int\dot f_k(t)e^{i\omega_kt}\,dt\right|^2,
\qquad \text{infidelity}=1-e^{-Q_{\rm ramp}}. \tag{11.4}
$$

A normalized Gaussian switching profile of temporal width $\sigma_t$, truncated at $L_t\sigma_t$, obeys

$$
Q_{\rm ramp}\le Q_{\rm sudden}
\left[e^{-\sigma_t^2\Delta^2/2}+\frac{2p}{1-p}\right]^2,
\qquad p=\operatorname{erfc}(L_t/\sqrt2). \tag{11.5}
$$

The two terms separately control Fourier suppression and truncation/renormalization. In the nontrivial regime $Q_{\rm sudden}/\varepsilon$ sufficiently large, choosing both errors of order $\sqrt{\varepsilon/Q_{\rm sudden}}$ gives support duration
$O(\Delta^{-1}\log(Q_{\rm sudden}/\varepsilon))$. This scaling is for the specified harmonic ramp, with its gap and force assumptions.

For a pure branch-output Stinespring map

$$
|z\rangle|\Phi\rangle\longmapsto e^{i\theta_z}|z\rangle|\Omega_z\rangle|e_z\rangle,
\qquad G_{zz'}=\langle e_{z'}|e_z\rangle,
$$

the environment adds no loss of label coherence, up to calibratable phases, exactly when its unit-diagonal Gram matrix has rank one:

$$
G_{zz'}=e^{i(\alpha_z-\alpha_{z'})}. \tag{11.6}
$$

The all-ones matrix is one special case. The matrices $\mathbf1\mathbf1^T$, $I_2$, and
$\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ have ranks **1, 2, 1**, respectively. The last has eigenvalues 0 and 2. Its half-mixture with the all-ones matrix is $I_2$, which has rank two. The criterion concerns additional environment dephasing under the stated pure branch-output map; oscillator overlaps and the intended joint output must still be accounted for. It is not a universal preservation criterion for arbitrary mixed channels. The underlying corpus result is inherited from ZS-M72 v1.8, **Appendix S6.10** (relaxation Gram matrix K1, the exact transformation K3 $\sigma_\infty=[a_j\mathbf1\mathbf1^T+(1-a_j)G]\odot\sigma$, and the cooling/record separation K4), not from its Section 10.6, which is the Ornstein–Uhlenbeck diffusive-window theorem; the locator printed in v1.4 was wrong (F24-01). M72 exhibits the rank-one case $G=\mathbf1\mathbf1^T$ as giving the ideal record; the reformulation of the criterion as rank one with unimodular entries is this manuscript's, and it is not counted as a new M73 theorem.

## 12. Reproducibility and verification boundaries

### 12.1 Earlier frozen targets and inherited evidence

This subsection preserves the v1.7 record of earlier reruns; those v1.5/v1.6 executions were not repeated in the present session. Section 12.4 reports the actual new v1.7 and v1.8 executions.

The submitted v1.6 manuscript and its complete ZIP were frozen before v1.7, with SHA-256 values `62943c16e17b4b645cd067b06406b71cb373c710e6b519f28e7dcd880487b6f9` and `25448f179388051453b7617ec8d4309c6bfcb12f548580eca4ed1d146ce8b7f9`. The untouched `PORTABLE-LC-33` verifier was rerun: 33 PASS, 0 FAIL, 0 SKIPPED, C=15, V=13, R=4, G=1, P=0. The rerun used Python 3.11.15, NumPy 2.4.4 and mpmath 1.4.1, which differ from the recorded environment; the scientific details matched apart from last-digit float noise in `LOC2-FINITE-MODEL`.

The submitted v1.5 manuscript and its complete ZIP were frozen before editing. Their SHA-256 values are respectively `ad2b54039048fdaf0c3cc3d5121d7ef8e02e2da0b54a9cb4c390b4c4a7dccdf6` and `a29538a8084b0cb0d31d02934d00abe2faf3bc43ca0082ddb3327411b12e180e`. The ZIP manuscript and research record match the separately attached files byte for byte. The untouched `PORTABLE-HP-29` verifier was rerun: 29 PASS, 0 FAIL, 0 SKIPPED, C=12, V=13, R=3, G=1, P=0. This reproduces its encoded claims; it does not prove the former hypothesis (13.6) or cure the textual findings in Appendix K.

The earlier v1.3 FULL-35 missing-module incident and v1.4 portable reproduction remain historical evidence. The v1.5 source-scope record reports the 238-file Repo 2 enumeration and the missing eleven legacy modules. That inventory was not repeated in this revision, and no legacy Coulomb/Fock run is claimed. The original v1.5 package, fresh rerun and its frozen verdict are preserved as provenance.

### 12.2 Historical v1.7 portable profile

Historical commands, run after extracting the preserved v1.7 ZIP into its own directory:

```bash
python -m pip install -r requirements_v1_7.txt
python zs_m73_verify_v1_7.py --output zs_m73_verify_v1_7.json
```

The v1.7 full profile was `PORTABLE-NP-39`: 39 rows, C=18, V=15, R=5, G=1, P=0. It retains the 33 rows of the v1.6 profile `PORTABLE-LC-33` unchanged in scope and adds six rows for Section 8.12: `NP-FINITE-IDENTITIES`, `NP-TAIL-DOMAIN`, `NP-G-ALLR`, `NP-P1-ALLR`, `NP-ROUTE-BARRIERS` and `NP-EXPONENTS`. All registered rows execute; any exception or failed assertion is a FAIL and produces a nonzero exit. The options `--only-new` (`LC-DELTA-5`) and `--only-np` (`NP-DELTA-6`) are explicitly labelled delta profiles, not the full release profile. Seven fault injections have separate result files: three inherited ones and four new ones (`np-trap-sign`, `np-response-factor`, `np-rs3-factor`, `np-gaussian-at-half`).

Interval precision is 50 decimal digits. Rational polynomial checks are exact; inherited finite matrix, Hermite solve and split-operator rows retain their numerical tolerances. The scalar and envelope implementations share part of the expression graph. Timings are informational and may vary; scientific results are compared separately from timing and runtime metadata. The verifier depends on Python, `mpmath`, `numpy`, and, for the finite three-oscillator row only, `scipy` and `sympy`. It also needs the included `loc2_toy.py` and `np_toy.py`.

### 12.3 Retained proof-to-code map and limits

| Scientific object | Evidence and scope |
|---|---|
| Coulomb derivatives, lattice majorants and geometry | Inherited kernel, lattice, rounding, geometry and tail rows; Theorem L constants and finite geometry checks |
| Parity, Walsh flips and Schur/Temple algebra | Inherited exact/finite rows with their original classifications and limitations |
| Earlier sufficient routes | `HALF-ALLR`, `CONSERVATIVE-ALLR`, `STATIC-7-13`; negative controls retain their historical majorants |
| Lemma LC-A normalization and cross term | `LC-GAUSSIAN-IDENTITIES`: separate rational Wick-moment calculation for two correlated Gaussian polynomial cases |
| Theorem LC full-space constants | `LC-S9-CONSTANTS`: all-real-$n\ge2$ positive envelopes and the rounded coefficient inequality |
| Theorem LC-prime | `LC-RECORD-ALLR`: coefficient check, energy/readout/gap budgets, frequency conversion and the surviving quartic obstruction |
| Theorem O | `LPPL-OBSTRUCTION-IDENTITIES`: bond limit constants and exact column-Laplacian identities; the all-size limiting argument is in the text |
| Quantifier and phase attacks | `LC-SCOPE-CONTROLS`: exact quadratic $\Delta^{-5}$ coefficient and the missing zero-point-phase counterexample |
| LOC-2, quadratic comparison and echo | Inherited `LOC2-FINITE-MODEL`, `LOC2-S9-ENVELOPE`, `QUADRATIC-MODEL`, `COHERENT-ECHO-1D` |
| Lemmas NP-1–NP-3 | `NP-FINITE-IDENTITIES`: exact truncated three-oscillator checks of (8.NP1)–(8.NP3), the Brascamp–Lieb inequality and $\lambda_{\min}\nabla^2(-\log\psi)\ge g_0$; the imported theorems themselves are not re-proved |
| Lemmas NP-4–NP-7, Theorems NP-G and NP-P1 | `NP-TAIL-DOMAIN`, `NP-G-ALLR`, `NP-P1-ALLR`: all-real-$n\ge2$ envelopes, readout assembly and frequency conversion |
| Corollary NP-B | `NP-ROUTE-BARRIERS`, `NP-EXPONENTS`: the growing preparation term at $p=1/2$, the convexity failure below $p=1/2$ and the pins of every NP term |
| Language and structure | `ENGLISH-MATH-INTEGRITY`, plus a separate complete LaTeX rendering/parser check; these are integrity checks |

The analytic proofs remain mathematical text, not proof-assistant objects. In particular, the covariance inequality for arbitrary dimension, derivative estimates, operator domains and imported spectral comparisons are not inferred from a finite test or a PASS count. No row certifies novelty, importance, research grade or a physical carrier. The manifest records the frozen inputs, actual current census, row provenance and companion hashes.

### 12.4 The v1.8 reproduction (historical)

The frozen v1.7 manifest was checked: all 46 listed hashes match. The separately attached manuscript and research record match their ZIP copies. An untouched rerun with the declared dependencies completed with 39 PASS, 0 FAIL, P=0. An earlier diagnostic using mpmath 1.3.0 failed on a Fraction/mpf comparison; that version does not satisfy the declared `mpmath==1.4.1` requirement, and the failure is not counted against the frozen release. The v1.8 comparison converts the interval endpoint to an exact rational before comparing it, without weakening the inequality.

To reproduce the frozen v2.0 release, extract its preserved ZIP and run inside that extracted directory:

```bash
python -m pip install -r requirements_v1_8.txt
python zs_m73_verify_v1_8.py --output zs_m73_verify_v1_8.json
```

The full profile is `PORTABLE-M73-49`: C=18, V=21, R=9, G=1, P=0. Ten added rows in `m73_v18_checks.py` cover ST's field decomposition and square completion, a noncommuting ER identity, the OB bound, spectator cancellation, exact time powers, the probability saturation control, the scalar-locality residue, spectral matching, and Theorem Q's sufficient domain. Their scope is finite regression, exact algebra or route falsification; no new row is a formal proof of an infinite-dimensional theorem. The preserved 39 rows retain their original mathematical scope. `--only-v18` is explicitly a ten-row diagnostic profile, not the full release. `--only-new` and `--only-np` retain their earlier limited meanings.

Four new fault injections (`st-self-sign`, `er-drop-right`, `ob-phase-sign`, `ts-drop-time`) must each cause a nonzero exit in the v1.8 profile; the seven inherited injections are rerun in their relevant delta profiles. Injection outputs are expected-failure controls. All ordinary release rows must pass. The release includes the original v1.7 ZIP, the untouched designated-environment rerun, frozen hash evidence, the current JSON, fault-control results and a LaTeX syntax check. Reproducibility does not adjudicate novelty, grade, physics or operator-domain hypotheses.

### 12.5 The v1.9 reproduction (historical)

The frozen v1.8 release was rerun without modification in a Python 3.12.3 environment with the pinned mpmath 1.4.1, NumPy 2.5.3, SciPy 1.18.1 and SymPy 1.12: 49 PASS, 0 FAIL, 0 SKIPPED. Forty-seven detail objects are identical to the shipped JSON. `LOC2-FINITE-MODEL` and `NP-FINITE-IDENTITIES` agree to floating-point noise; their scientific conclusions are unchanged.

Historical commands, run after extracting the preserved v1.9 ZIP into its own directory:

```bash
python -m pip install -r requirements_v1_9.txt
python zs_m73_verify_v1_9.py --output zs_m73_verify_v1_9.json
```

The full profile is `PORTABLE-M73-59`: the 39 inherited rows, the 10 v1.8 rows and 10 v1.9 rows. That release's recorded run gives 59 PASS, 0 FAIL, 0 SKIPPED, with C=20, V=28, R=10, G=1, P=0. Of the 49 inherited and v1.8 rows, 48 have scientific detail objects identical to an unmodified v1.8 run in the same environment; the manuscript-integrity row differs because the manuscript changed. The v1.9 rows are the following.

| Row | Class | Object and scope |
|---|---|---|
| `LHAT-CONSTANTS` | C | Interval constants $f'_{\max}$, $E_2$, $\widehat S_3$, $\widehat S_{22}$; enumerated hat row sums for full cubes $n\le7$ against (8.LG3); regularization tail at $10c$ |
| `LHAT-STRUCTURE` | V | $\widehat V=V$ in the box; the global majorants of (8.LG2) on grids; $|\widehat V_{ab}|\le\widehat M_2|u_a||u_b|$ (tight to $0.9991$); Theorem O versus Theorem L-hat at the collapse configuration |
| `LOC-POINTWISE` | V | (8.LG6) and its out–out and in–out components on random and adversarial S9 configurations ($n=2,3$), including collinear landing, head-on out pairs and the collapse configuration; near/far lattice sums against $P_{\rm near}$, $P_{\rm far}$ |
| `LOC-SEMIBOUND` | V | The log-Sobolev + entropy + modified Herbst chain of Lemma LOC-B on one- and two-dimensional DVR references |
| `SR-COVARIANCE` | V | Lemma SR in anharmonic three-oscillator DVR ground states; the harmonic case against $\tfrac12(A^{-1})_{ab}$ |
| `SR-DOMINATION` | V | Z-matrix exponential domination, $\Gamma\ge0$, its row sums and source-row bound on S9 cubes, and the exact Euclidean zero-frequency identity |
| `NP-LOG-FORMULAS` | V | Second- and third-order ground-energy formulas against finite differences (independent code) |
| `NP-LOG-READOUT` | V | The Boolean second-order Efron–Stein inequality and (8.LG13) on random instances |
| `NP-LOG-ALLR` | C | The Theorem NP-LOG envelope at $n=2$ with its side conditions, and a direct re-evaluation at eleven values of $\ell_n$ up to $10^4$ |
| `NP-LOG-BARRIER` | R | The line-bound route fails and full cubes become non-convex along $\Omega_R=10^4\ell_n$, while $\widehat h_N<\Omega^2$ throughout |

`--only-v19` runs these ten rows. It is a delta profile, not the full release. Nine fault injections must each fail their targeted row:

| Fault injection | Targeted row |
|---|---|
| `lhat-half-majorant` | `LHAT-STRUCTURE` |
| `loc-drop-near` | `LOC-POINTWISE` |
| `loc-no-herbst` | `LOC-SEMIBOUND` |
| `sr-diagonal-gamma` | `SR-COVARIANCE` |
| `sr-gamma-rowsum` | `SR-DOMINATION` |
| `np3-drop-T` | `NP-LOG-FORMULAS` |
| `readout-drop-beta` | `NP-LOG-READOUT` |
| `log-coefficient-1000` | `NP-LOG-ALLR` |
| `log-no-hat` | `NP-LOG-BARRIER` |

The eleven inherited injections are unchanged. The results are included in `evidence/`.

The analytic lemmas remain mathematical text. In particular, the Euclidean limits in Lemma SR and the imported Brascamp–Lieb, Caffarelli, Bakry–Émery, Helffer–Sjöstrand and log-Sobolev facts are not certified by code. The finite rows are regressions of exact statements in small models. No row certifies novelty, significance or a research grade.

### 12.6 Frozen v2.0 reproduction (historical release profile)

In the v2.0 session, the v1.9 release ZIP was checked against its recorded SHA-256 before edits. That original v1.9 ZIP remains in the nested provenance of the preserved v2.0 archive. This paragraph records the v2.0 assembly, not the current v2.1 file layout.

To reproduce the frozen v2.0 release, extract its preserved ZIP and run inside that extracted directory:

```bash
python -m pip install -r requirements_v2_0.txt
python zs_m73_verify_v2_0.py --output zs_m73_verify_v2_0.json
```

The full profile is `PORTABLE-M73-67`: the 39 inherited rows, the 10 v1.8 rows, the 10 v1.9 rows and 8 v2.0 rows. That release's recorded run gives 67 PASS, 0 FAIL, 0 SKIPPED, with C=21, V=35, R=10, G=1, P=0. Of the 59 inherited rows, 55 have scientific detail objects identical to the shipped v1.9 JSON. The manuscript-integrity row differs because the manuscript changed. `LOC-SEMIBOUND`, `SR-COVARIANCE` and `NP-LOG-FORMULAS` agree to floating-point noise; their finite-difference entries agree to their own discretization noise. The v2.0 rows are in `m73_v20_checks.py`.

| Row | Class | Object and scope |
|---|---|---|
| `DF-CONSTANTS` | C | Interval certificate (30 digits) of $E_*\le2.7104$ by the three-piece procedure of Theorem DF, of $\varphi(\tfrac12)$ and the monotonicity used in Lemma DF-2, of the constants $15.663$, $-7.905$, $\lambda_1$, $8.614$, $24.28$, $f_+/f_-$, $28.33$, the Corollary Q-prime threshold $1.666\times10^7$ and source-entry ratio $4\times10^{-4}$, the arithmetic of Proposition LN, and the NP-LOG edge term $1.7\times10^{-14}$. Lemma DF-2 is checked against direct lattice sums at four heights |
| `DF-LATTICE` | V | Exact signed row sums on 17 full and partial S9 sets ($n\le16$): the bounds (8.DF2), the Lipschitz part of (8.DF3), the first-order source bound $24.28$, and the telescoped identity (8.DF1) at random sites |
| `EL-EDGE` | V | $(K^2\mathbf 1)_j$ by FFT on full cubes $n=8,16,32,64$: mid-edge minus $2\log n$, corner minus $\tfrac32\log n$, convergence of both remainders, boundedness of the vertical mid-edge, and the reflection symmetries |
| `EL-ANGULAR` | V | The angular integrals of Theorem EL at 20–30 digits: the edge coefficient $2$, the octant integrals $0,\tfrac12,\tfrac12$ and the identity $I'(u)u'(c)=2\log c/(1-c^2)$ |
| `EL-SOURCE` | V | Lemma SRC witness: $(K^2\varphi)_j$ with the S9 source row for $n=16,32,64$, bounded and converging; source-row remainders at the bottom and top mid-edges |
| `W-EXPONENT` | V | Proposition W: the $4\times4$ determinant against $\nu^2\varepsilon^{-1/2}F$ at 50 digits, $F(1,\varepsilon)=0$, the root near $1$ for six values of $\Omega^2$, $\gamma\Omega^4\to2$ and the $\delta^3$ coefficient |
| `EG-LATTICE` | V | Evidence for Hypothesis EG: exact local-field factors by conjugate gradients at $\Omega^2=6,10$, $n=16,32,64$; the $32\to64$ exponent lies in $[.8\gamma,1.02\gamma]$ and the vertical mid-edge converges. The entries $n\ge96$ of the EG table are recorded in `evidence/lf_big_*.json`, not recomputed by the verifier |
| `QPRIME-FINITE` | V | The exact polarization correction $\rho_{\rm pol}$ on seven full and partial S9 geometries at $\Omega_0^2=200,1000$ against (8.Qp) and (13.2) |

`--only-v20` runs these eight rows. It is a delta profile, not the full release. Eight fault injections must each fail their targeted row and no other:

| Fault injection | Targeted row | Fault |
|---|---|---|
| `df-estar-half` | `DF-CONSTANTS` | Halve the certified $E_*$ (caught by the float cross-check) |
| `df-poisson-pi` | `DF-CONSTANTS` | Replace the bound $2\pi$ of Lemma DF-2 by $\pi$ |
| `df-drop-remainder` | `DF-LATTICE` | Drop the midpoint remainders $e_\rho(t)$ from the telescoped identity |
| `df-no-lipschitz` | `DF-LATTICE` | Set the Lipschitz allowance of (8.DF3) to zero |
| `el-coefficient-1` | `EL-EDGE` | Edge coefficient $1$ instead of $2$ |
| `el-corner-2` | `EL-EDGE` | Corner coefficient $2$ instead of $\tfrac32$ |
| `w-no-stretch` | `W-EXPONENT` | Omit the anisotropic stretch factors from the interface conditions |
| `eg-gamma-double` | `EG-LATTICE` | Compare the lattice exponent with $2\gamma$ |

The twenty inherited injections are unchanged. They were rerun in their delta profiles (`--only-new`, `--only-np`, `--only-v18`, `--only-v19`), and each exits nonzero. The v2.0 injections were run in `--only-v20`, and each fails exactly its targeted row. The results are included in `evidence/`. The large-$n$ lattice data behind Sections 8.15.2 and 8.15.4 ($n\le224$ for $K^2\mathbf 1$, $n\le192$ for the local-field factor) were produced by the FFT scripts listed in the README and are shipped as evidence files. They are finite computations and do not certify an asymptotic statement.

The analytic proofs of Section 8.15 remain mathematical text. In particular, the asymptotic statements of Theorem EL, the constant of Lemma SRC and the continuum statement of Proposition W are not certified by code, and Hypothesis EG is not proved by any row. No row certifies novelty, significance or a research grade.

### 12.7 v2.1 verification and reproducibility

The v2.0 archive was frozen before edits. All 60 manifest entries match; the inherited verifier was rerun without source modifications and returned 67 PASS, 0 FAIL, 0 SKIPPED. This is a reproduction under a different dependency environment, not a byte-identical recreation of the original run. The audit used Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0 and SymPy 1.12. The original release reports Python 3.12.3, NumPy 2.5.3, SciPy 1.18.1 and mpmath 1.4.1. Runtime and timing differences are retained.

The new driver extracts the unchanged baseline archive into a temporary directory, runs its verifier there, and evaluates the v2.1 checks. Its inherited manuscript-integrity row concerns the frozen v2.0 manuscript. The release manifest separately hashes the integrated v2.1 files.

```bash
python -m pip install -r requirements_v2_1.txt
python zs_m73_verify_v2_1.py --output zs_m73_verify_v2_1.json
```

`--delta-only` runs the new checks without rerunning the baseline; it does not report the inherited rows as freshly passed. The result JSON identifies the exact profile used. The full profile has the inherited 67 rows and the following eight new rows:

| Row | Class | Evidence and limit |
|---|---|---|
| `V21-SCHUR` | V | Direct dense effective coefficient versus Schur formula, nine finite cases |
| `V21-SOURCE-FINITE` | V | Actual S9 source and uniform drives, $n=16,32,64$, $w=10,20$, two edge layers; not an all-$n$ or interval result |
| `V21-WEDGE-TRANSFER` | V | Independent $2\times2$ sector-transfer determinant against the inherited characteristic expression at nine high-precision points |
| `V21-RDV` | V | Exact enumeration of nine Boolean examples containing third and higher Walsh degrees; checks variance, Boolean Poincaré and readout bounds |
| `V21-COMP-SQRTLOG` | C | Outward interval constants at $n=2$, side conditions and diagnostic scans; the all-$n$ monotonicity proof is in Section 8.16.5 |
| `V21-WINDOW-REVIVAL` | R | Exact rejection of the old cosine upper bound and verification of a phase revival; continuous-window proof remains mathematical text |
| `V21-TC-POWER` | C | Exact exponent $3-7p/2$, value $5/4$ at $p=1/2$, threshold $6/7$ for the old positive majorant |
| `V21-JOINT-LIMIT` | R | Explicit positive family with the prescribed fixed-parameter exponent but no growth on a smaller diagonal; not an actual-lattice counterexample |

There is no executable proof row for EG, source transfer, the full-model sub-log theorem or source novelty. The new proofs are author-derived and author-reviewed. A finite PASS supports the stated check only. The original fault-injection reports are preserved but were not all rerun in this audit; the two new rejection rows execute the concrete failed implications directly.

### 12.8 v2.2 verification and reproducibility

The v2.1 release ZIP was frozen before any edit: SHA-256 `6c9a352592cfbe9eefebd4ba83a7f78f06e62d962b24aa6ae3aab5d51ed9e39b`, 17 manifest entries matching. Its unchanged driver was rerun in the audit and returned 75 PASS, 0 FAIL, 0 SKIPPED (C23/V39/R12/G1). The run took 219 s under Python 3.11.15, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0 and SymPy 1.12. v2.1 recorded Python 3.12.14 with the same package versions.

The v2.2 driver extracts the v2.1 ZIP into a temporary directory and runs its driver there. That driver extracts and reruns the frozen v2.0 verifier. The v2.2 driver then runs fourteen new rows.

```bash
python -m pip install -r requirements_v2_2.txt
python zs_m73_verify_v2_2.py --output zs_m73_verify_v2_2.json
```

`--delta-only` runs the fourteen new rows without the inherited 75 and says so in its profile name.

| Row | Class | Evidence and limit |
|---|---|---|
| `V22-SQ-CERT` | C | Outward interval enclosures of every term of (8.SQ3) and of the side conditions on 7077 subintervals covering $\ell\in[1+\log2,10^{15}]$. Valid for all real $\ell$ in each subinterval, for the formulas as coded. Its acceptance gate was $.9885$; the stated $.98853$ is certified by `V221-SQ-CERT-98853` (F32-02) |
| `V22-SQ-TAIL` | V (emitted as C by the v2.2 driver; reclassified in v2.2.1, F32-01) | Spot values of all factors at $\ell=10^9,\dots,10^{19}$, nonincreasing. A diagnostic at six points, not a certificate of the infinite tail. The tail proof is the monotonicity argument of Section 8.17.5, used only for $\ell\ge10^{15}$ |
| `V22-SQ-COMP-REPRO` | V | Independent code reproduces the v2.1 comparator value $.9885390698$ at $n=2$ |
| `V22-SQ-LHAT` | V | $\lambda_{\min}(\nabla^2\widehat V^Y)\ge-\widehat h^Y$ on collapse and random configurations, $n=2,3$, four thresholds |
| `V22-SQ-CORE-FAULT` | R | Dropping the core term from (8.SQ1) violates that bound at $y_c=.6,1.1$ |
| `V22-SQ-LOCA` | V | Lemma LOC-A$_Y$ on random and near-collision configurations. Large slack; a sanity check only |
| `V22-SQ-COINC` | V | $\widehat V^Y_{ab}=V_{ab}$ inside the coincidence region, by direct double integration of $\psi^Y$; primitive versus double integral outside. Tolerance $10^{-10}$ (see below) |
| `V22-SQ-FAULTS` | R | Three wrong variants fail as required: fixed threshold at $\ell\approx5.9\times10^2$, old $C_h$ at $\ell\approx1.16\times10^9$, pointwise $L^2$ majorants with growing $\mathcal Q_{\log}$ |
| `V22-CR-GEOM` | V | Exact position identity $r_a=n(\xi_a-\tfrac12\mathbf 1+20e_z)$, the range of $f$, and the multiplier range $[-4\pi/3,8\pi/3]$ |
| `V22-CR-LEMMA1` | V | Cauchy test of Lemma CR-1 at common cell centres for $n=12,36,108$ |
| `V22-CR-WEAK` | V | Weak-convergence diagnostics for the actual source drive at $w=10$, $n=16,32,64$. Not evidence for EG-C |
| `V22-AUDIT-FT1` | R | A label-independent constant in $\alpha$ changes the (8.FT1) budget but not $D_j$ |
| `V22-AUDIT-ZETA` | R | A pair energy $-43.1<-f_c(0)$ shows that $f_c(0)N$ per out label is insufficient in Lemma LOC-B; $2f_c(0)N$ is used |
| `V22-HISTORY` | G | The new history file equals the project's latest (H-0413) plus H-0414; the only difference from the v2.1 copy is the H-0409 timestamp |

### 12.9 v2.2.1 correction rows

**Census of v2.2.** The released v2.2 run (`PORTABLE-M73-89`) gave 89 PASS, 0 FAIL, 0 SKIPPED, with classes C25/V46/R16/G2 as emitted by its driver. The frozen audit reproduced it unchanged under Python 3.12.14. After the reclassification of `V22-SQ-TAIL` (F32-01) the effective classes are C24/V47/R16/G2. The release note of Section 16.0 refers to this census; v2.2 recorded it in `README_v2_2.md` and `zs_m73_verify_v2_2.json`, not in Section 12.8 (editorial item E-01 of Appendix S.3).

**The v2.2.1 driver.** `zs_m73_verify_v2_2_1.py` extracts the byte-identical v2.2 release ZIP (SHA-256 `80a13ed6…2f08`) into a temporary directory and runs its unchanged driver, which in turn reruns the v2.1 and v2.0 verifiers. It then reports `V22-SQ-TAIL` with its effective class and runs eight correction rows. The frozen v2.2 code is not modified; the corrected gate is implemented in the new rows (`v221/checks.py`).

```bash
python -m pip install -r requirements_v2_2_1.txt
python zs_m73_verify_v2_2_1.py --output zs_m73_verify_v2_2_1.json
```

`--delta-only` runs only the eight new rows.

| Row | Class | Evidence and limit |
|---|---|---|
| `V221-SQ-CERT-98853` | C | All 7077 subintervals with the gate $.98853$, the outward lower enclosure of $1+\log2$ as first end point, the printed coefficient $1.71342$ and all side conditions of (8.SQ3). Minimum $>.98853906777$. For the formulas as coded; the analytic steps are text |
| `V221-SQ-GATE-FAULT` | R | Lowering the right side of (8.SQ3) by $2\times10^{-5}$ on the first subinterval passes the old gate $.9885$ and fails $.98853$ |
| `V221-BRANCH-JUMP` | R | $\theta(\tfrac12)$ increases across $y_c=\tfrac12$ ($\ell=3906.25$), which refutes the v2.2 wording of monotonicity for all $\ell\ge\ell_*$; both values are below $1$ |
| `V221-TAIL-SCOPE` | V | Exact switch point $\ell=15625/4$; $y_c>355$ for $\ell\ge10^{15}$; the straddling subinterval passes with the $y_c>\tfrac12$ form, which dominates the other form on $[\tfrac15,\tfrac12]$ (exact rational grid) |
| `V221-TAIL-AUDIT-REPRO` | V | Re-executes the frozen audit's exact-arithmetic checks of its tail reconstruction: nonnegative coefficients and degrees at most $6$ and $4$; rounded tail budget $>.98854476$. The inequalities that connect them to the tail are in the audit report, Appendix A |
| `V221-PRESERVATION` | G | The edit register applied to the v2.2 manuscript reproduces this manuscript byte for byte, and applied in reverse reproduces v2.2 (SHA-256 `324f4d48…3998`). Lists every removed fragment |
| `V221-HISTORY` | G | The history file is the v2.2 history (up to H-0414) followed by exactly H-0415 and H-0416 |
| `V221-PROVENANCE` | G | SHA-256 of the v2.2 release ZIP and of the audit evidence ZIP; the audit's input release equals the v2.2 release |

The released v2.2.1 run (`PORTABLE-M73-97`) gave 97 PASS, 0 FAIL, 0 SKIPPED under Python 3.11.15, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0 and SymPy 1.12, with effective classes C25/V49/R18/G5. The 89 inherited rows reproduce the v2.2 results unchanged, and the eight new rows all pass. The run time is recorded in the JSON. No row certifies EG-C, novelty, significance or a grade.

## 13. Beyond the convex-regime certificates: the remaining locality problem

Theorem N below preserves the v1.5 majorant classification for comparison. In the LC-prime certificate its cubic row is replaced by Theorem LC; Section 8.9b gives the binding exponent of that certificate. Section 8.12 bypasses this ladder, Section 8.14 removes the convexity requirement for P1, and Sections 13.9–13.11 record what remains. Section 13.12 records the fixed-confinement target after the v2.0 analysis of the signed dipole kernel. Throughout, $\Delta=Cn^p$ with $C=10^4$ unless stated, and "the older certificate" means the positive-monomial majorant of (8.27) with $M=M_{\rm par}$.

### 13.1 Theorem N: the older majorant and the new binding term

**Theorem N (v1.5 majorant, scoped to the verified exponent ranges).** Write each term of (8.27) as a positive monomial sum in $n$ for $\Delta=Cn^p$. The leading (smallest) $n$-exponent of every term is an affine function of $p$, exactly as follows, where "pin" is the value of $p$ at which the term becomes bounded in $n$:

| Term | Decay exponent $p'$ (term $\asymp n^{-p'}$) | Pin | Origin of the $R$-dependence |
|---|---|---:|---|
| $2TM_{\rm par}$ (third order) | $7p-21/2$ | $3/2$ | Extensive norms $\sigma_e\kappa^2$, $\sigma\kappa_e\kappa$: $N^{3/2}$ where Theorem LC supplies an $O(N)$ coefficient bound on its design curve; uniform flip bounds remain open |
| $T(\sigma^4/\Delta^3+4F_4^2\kappa^2/g_0)$ (fourth order) | $9p-12$ | $4/3$ | $q_ze_2$ and the Temple residual: products of two extensive second-order quantities |
| $\rho^{e_2}$ (second-order source correction) | $2p-2$ | $1$ | The coherent source-star component $\lambda_0Rm_s\propto n^{-1}$ of $\mathcal D_0$ paired crudely with $\mathcal D_{\rm mem}$ |
| $T\widehat\eta_j$ (non-pairwise second order) | $2p-3/2$ | $3/4$ | Efron–Stein $\sqrt R$ and, before LOC-2, the factor $\sigma$ |
| $\varepsilon_S$ (common-preparation fidelity) | $5p-3$ | $3/5$ | $\sigma^2/g_0^2=O(N/\Delta^5)$: the fidelity of one Gaussian with an $N$-body ground state |
| $h_N/\Delta^2$ (v1.4 gap) | $2p-3$ | $3/2$ | Collinear worst case counted for all partners |
| $h'_N/\Delta^2$ (Theorem L gap) | $2p-1$ | $1/2$ | One collinear column and a convergent transverse sum |

The affine rules hold exactly for $p\in[9/10,3/2]$ for the first two terms, where at $p\le3/4$ the algebraic tail majorant (8.29) takes over, and for all $p\in[1/2,3/2]$ for the others; all pins lie in the ranges where the rules hold. Exactness on an interval follows from finitely many checks because the decay exponent of a finite positive monomial sum is the minimum of finitely many affine functions of $p$, hence concave and piecewise affine: agreement with one of its affine pieces at two points of an interval implies agreement on the whole interval. Consequently: (i) the older certificate closes for $\Delta=10^4n^p$ if and only if $p\ge3/2$; (ii) for $p\in[4/3,3/2)$ the third-order term is the only growing term of (8.27) with $h_N^{(L)}$; (iii) with Theorem L the gap condition is non-binding for every $p\ge1/2$; (iv) after any improvement of the third-order majorant to $O(N)$ the binding term becomes the fourth-order remainder at $p=4/3$, i.e. $\Omega=O(R^{4/9})$; (v) if in addition the fourth-order term were $O(N)$, the extensive cubic secular term $TN\Delta^{-7}\propto n^{9-7p}$ of Theorem LC would pin the certificate at $p=9/7$, i.e. $\Omega=O(R^{3/7})$. Only after a further flip-local treatment of that cubic term would the certificate be pinned at $p=1$ by $\rho^{e_2}$, then at $p=3/4$ by the Efron–Stein term $\sqrt R\,\mathcal D_{\rm mem}^2$ of $\widehat\eta_j$. After a further, still unproved localization of both star–star pairings it would be pinned at $p=3/5$ by the fidelity $\varepsilon_S$, i.e. $\Omega=O(R^{1/5})$. The v1.5 and v1.6 statements of (v) omitted the extensive cubic term (F26-01). Theorem NP-G reaches the fidelity threshold $3/5$ directly, without any of these intermediate steps.

*Proof.* The engine represents every quantity as an exact finite sum of monomials $Kn^{-p'}(1+\log n)^{q'}$ with rational exponents, so the leading exponent is an exact rational function of $p$; row `EXPONENT-LADDER` verifies the seven affine rules at $p\in\{3/2,149/100,4/3,1,9/10,3/4,3/5,1/2\}$ (the first two terms for $p\ge9/10$) and row `NO-LOCALITY-CONTROL` verifies (ii) at $p=149/100$. Statement (i) is Theorem HP-prime for $p=3/2$, the monotone decrease of every certificate term in $\Delta$ at fixed $n$ (all terms are positive combinations of powers of $1/\Delta$ and of Gaussian tails decreasing in $\Delta$) for $p>3/2$, and the growth of the third-order term for $p<3/2$; (iii) is the rule $2p-1$; (iv) follows by replacing the third-order row with the $O(N)$ bound of Theorem LC, whose exponent is $7p-9$. (v) follows by also replacing the fourth-order row with a hypothetical $O(N)$ bound, of exponent $9p-9$, while keeping the Theorem LC row, whose pin $9/7$ then binds; the subsequent pins are those of the remaining rows. The origins in the last column are read off the defining formulas (8.2), (8.10), (8.19), (8.22), (8.25)–(8.26). $\square$

Theorem N is a statement about the older displayed majorants, not about the true readout error, and not a lower bound on the confinement physically required. Its value is that the $R$-dependence of every term is now attributed to a specific inequality in which a local flip quantity was bounded by an extensive norm (or, for $\varepsilon_S$, to the fidelity of the common preparation).

### 13.2 What is local and what is extensive: the Walsh reading of the readout

By (2.12), only three kinds of quantities enter $D_j$: the source-odd coefficient $\beta$, the $z'$-dependence of $\alpha$, and the echo deviation. For the exact ground energy $E_0(z)$, expand the flip in Walsh form,

$$
\Delta_jE_0(s,z')=2\widehat E_0(\{j\})+2s\,\widehat E_0(\{0,j\})+\sum_{k\ne0,j}2z_k\widehat E_0(\{j,k\})+\rho_j^{E_0}(s,z'),
\qquad \mathbb E_{z'}\rho_j^{E_0}=0. \tag{13.1}
$$

The constant $2\widehat E_0(\{j\})$ is a global phase. The readout is controlled by: (a) the relative error of $\widehat E_0(\{0,j\})$ against the frozen dipole coefficient; (b) the memory-pair coefficients $\widehat E_0(\{j,k\})$ against the $\Lambda_3$ budget; (c) $T\,\mathbb E_{z'}|\rho_j^{E_0}|$; (d) the echo deviation $\sup_t|D_j-D_j^{E_0}|$. Items (a)–(c) are flip quantities of the exact energy: each carries at least one factor $\lambda_e\propto n^{-3}$ and (a) carries $\lambda_0\lambda_e/L^3$, the same scaling as the signal, so their *relative* sizes are $n$-independent whenever the exact energy responds locally to the flip of a label. The certificate of Section 8 proves (a)–(c) to second order with the flip bounds of Lemmas F and ES, and bounds the third- and higher-order contributions to (a)–(c) by the *global* interval length $\widehat r_{\rm len}$, which is where the extensive norms enter. Item (d) is bounded by $\varepsilon_S$, the global fidelity.

### 13.3 Theorem Q: the exactly solvable quadratic model has no square root

Consider the quadratic dipole model $H_G(z)$ of Section 2.2 with common preparation $\Phi_G$, the ground state of $\tfrac12|p|^2+\tfrac12x^TA_Gx$, $A_G=\Omega_0^2I+gK$, $\Delta_G^2:=\Omega_0^2-8g>0$, and the S9 geometry, shifts and window of Section 2.3.

**Lemma Q1 (exact energies and a conditional row-sum bound).** $E_0(z)=E_{A_G}+\tfrac12z^TC_Gz$ with $C_G=g\Lambda K\Lambda-F_G^TA_G^{-1}F_G$; the pair coefficients are $C_{G,ab}$, exactly pairwise, and the exact ground state is $\Omega_z=W(d_z,0)\Phi_G$ with $d_z=-A_G^{-1}F_Gz$. When $\Omega_0^2>gS_K(n)$, the *polarization correction* of the source–memory coefficient satisfies

$$
\rho_{\rm pol}:=\max_j\left|\frac{C_{G,0j}}{g\lambda_0\lambda_eK_{0j}}-1\right|
=\max_j\frac{g|(KA_G^{-1}K)_{0j}|}{|K_{0j}|}
\le\frac{f_+}{f_-}\cdot\frac{gS_K(n)}{\Omega_0^2-gS_K(n)}
\le\frac{1.1665\,[48(1+\log n)+5]}{\Omega_0^2-48(1+\log n)-5}. \tag{13.2}
$$

*Proof.* Square completion gives the first statements. For (13.2): $|(KA^{-1}K)_{0j}|\le\sum_a|K_{0a}|\sum_b|(A^{-1})_{ab}||K_{bj}|$; entrywise $|A^{-1}|\le\Omega_0^{-2}(I-g|K|/\Omega_0^2)^{-1}$ by the Neumann series, valid because the row-sum norm of $g|K|$ is at most $gS_K(n)<\Omega_0^2$; the column sums of $(I-g|K|/\Omega_0^2)^{-1}|K|$ are at most $S_K(n)/(1-gS_K/\Omega_0^2)$; finally $|K_{0a}|\le2f_+/L^3$ and $|K_{0j}|\ge2f_-/L^3$, and Lemma 4.3 bounds $S_K(n)$. $\square$

**Lemma Q2 (exact echo).** Let $H_\pm$ be two displaced harmonic Hamiltonians with the same $A_G$ and equilibria $d_\pm=d_c\mp\delta$, $\omega_{\max}^2=\|A_G\|$. For the common preparation $\Phi_G$ and every $t$,

$$
\Bigl|\langle e^{-itH_-}\Phi_G,e^{-itH_+}\Phi_G\rangle\,e^{it(E_+-E_-)}-1\Bigr|
\le2\omega_{\max}|d_c||\delta|+4\omega_{\max}|\delta|^2. \tag{13.3}
$$

*Proof (Appendix J).* Weyl calculus gives $e^{-itH_\pm}\Phi_G=e^{-itE_\pm}e^{i\Theta_\pm(t)}W(\eta_\pm(t))\Phi_G$ with $\eta_\pm(t)=((I-\cos\sqrt A\,t)d_\pm,\;\sqrt A\sin(\sqrt A\,t)d_\pm)$ and $\Theta_\pm(t)=-\tfrac12d_\pm^T\sqrt A\sin(\sqrt A\,t)d_\pm$. The symplectic form of $\eta_-$ and $\eta_+$ vanishes because all matrices commute, the overlap of the two coherent states is $\exp(-\tfrac14\|\eta_+-\eta_-\|_A^2)$ with $\|(\xi,\pi)\|_A^2=\xi^T\sqrt A\xi+\pi^TA^{-1/2}\pi$, and $\|\eta_+-\eta_-\|_A^2=8\delta^T\sqrt A(I-\cos\sqrt A\,t)\delta\le16\omega_{\max}|\delta|^2$, while $\Theta_+-\Theta_-=2d_c^T\sqrt A\sin(\sqrt A\,t)\delta$. $\square$ Row `COHERENT-ECHO-1D` reproduces the modulus and phase formulas numerically to better than $4\times10^{-7}$ and $4\times10^{-6}$ respectively in a one-dimensional split-operator propagation.

For the flip of memory $j$: $\delta=\lambda_eA_G^{-1}Ke_j$, so $|\delta|\le2\sqrt{30}\,\lambda_e/\Delta_G^2$, and $|d_c|\le16(\lambda_0+\sqrt R\lambda_e)/\Delta_G^2$ by (4.2). Hence

$$
\varepsilon_Q:=\sup_{t,z,j}\bigl|\mathcal A_j^Ge^{it\Delta_jE_0}-1\bigr|\le\frac{\omega_{\max}\lambda_e}{\Delta_G^4}\bigl[351(\lambda_0+\sqrt R\lambda_e)+480\lambda_e\bigr]. \tag{13.4}
$$

**Theorem Q (sufficient-domain form).** In the quadratic dipole model with common preparation $\Phi_G$, fix $R\ge2$ and $\Omega_0$ such that $\Delta_G^2>0$, $\Omega_0^2>gS_K(n)$ and $e_*(\rho_Q)\le1$, with $\rho_Q$ defined below. Then for every memory $j$ and every $t\in I_R$,

$$
D_j^G(t)\ge\cos\Bigl(\frac{\pi e_*(\rho_Q)}2\Bigr)-\frac94\Lambda_3-\frac{.66}{\Delta_G^4}-2\varepsilon_Q,
\qquad \rho_Q=(1+.001)(1+\rho_{\rm pol})-1, \tag{13.5}
$$

with $e_*(\rho)$ from (4.12). In particular, at $\Omega_0^2=8\times10^8$ (the $n=2$ value of Theorem HP-prime), $D_j^G\ge.98538$ for every $R\le10^{1800}$; the residual obstruction in this particular sufficient bound is the logarithmic absolute dipole-row majorant in (13.2). No necessity of that logarithm for the exact quadratic readout is claimed.

*Proof.* By Lemma Q1 the echo phases are exactly pairwise, so (2.12) and Lemma Q2 give $|D_j^G-D_j^{\rm pw}(C_G)|\le2\varepsilon_Q$. The pairwise readout is (4.10) with the exact coefficients: the source coefficient has relative error at most $\rho_Q$ (frozen/dipole $.001$ times polarization), and the memory coefficients are $g\lambda_e^2K_{jk}$ (within the $\Lambda_3$ budget of (4.11), since $|K_{jk}|\le2/r^3\le3/r^3$) plus polarization corrections whose squared sum obeys $\sum_k(2tC^{\rm pol}_{G,jk})^2\le4(1.01t_*\lambda_e^2)^2\|gKA_G^{-1}K\|^2\le4(1.5865\times10^{-3})^2(256/\Delta_G^2)^2<.66/\Delta_G^4$, using $t_*\lambda_e^2=\pi\cdot5\times10^{-4}$ exactly, independent of $n$. The two phase contributions are combined through $(\theta+\theta')^2\le2\theta^2+2\theta'^2$ and $\prod|\cos|\ge1-\tfrac12\sum(\theta+\theta')^2$, so the bare part costs at most $2\Lambda_3\le\tfrac94\Lambda_3$ (with $|K_{jk}|\le2/r^3$ instead of $3/r^3$) and the polarization part at most $.66/\Delta_G^4$. At $\Omega_0^2=8\times10^8$, (13.2) gives $\rho_{\rm pol}\le10^{-4}$ for $\log n\le1427$, hence $\rho_Q\le1.001\cdot1.0001-1=.0011001<.0011053$, $e_*<.091$ and $D_j^G\ge.9884$. Row `QUADRATIC-MODEL` computes the exact quantities for $n=2,3,4$: $\rho_{\rm pol}\le2.7\times10^{-9}$ (bound (13.2): $1.75\times10^{-7}$), $\varepsilon_Q\le2.2\times10^{-25}$, and $\min D_j^G$ over the window (21 equally spaced times in $I_R$) $\ge.9941$. $\square$

The exact identities of Lemmas Q1 and Q2 still hold whenever $A_G>0$. The row-sum upper bound (13.2) and the positive cosine-lobe readout bound have the additional domain just stated. At other parameters one must use exact coefficients and a valid phase envelope; the bare cosine is not a universal lower envelope once $e_*>1$. The explicit $R\le10^{1800}$ application remains inside the sufficient domain. Theorem Q is an exact computation in a linear model and claims no novelty; exactly solvable Gaussian environments are the standard setting of quantum-Darwinism calculations (Section 15). Its role here is diagnostic: with the same geometry, shifts, window and a fixed trap, the quadratic model records for all practical $R$, while the older square-root certificate loses size factors in its anharmonic remainder estimates. The logarithm belongs to the stated quadratic majorant; neither its necessity nor an intrinsic square-root cost follows from this comparison.

*v2.0 update.* The proof above derives $D_j^G\ge.9884$, which implies the stated $.98538$ (Appendix P, F29-04). Corollary Q-prime (Section 8.15.4) moves the logarithm of (13.2) from the numerator to the Neumann radius and extends the explicit range at $\Omega_0^2=8\times10^8$ to $R\le10^{2\times10^7}$. Proposition LN shows that the exact source coefficient has an $\Omega_0^{-2}$ coefficient bounded by $24.28g$ but an $\Omega_0^{-4}$ coefficient equal to $g^2(2\log n+O(1))$ at horizontal mid-edges and corners of full cubes. Whether the logarithm controls the exact readout at a fixed $\Omega_0$ depends on Hypothesis EG and its transfer to the source row, neither of which is proved.

### 13.4 The former C1 hypothesis is closed; C2 remains a sufficient conditional criterion

**Corollary C1 (proved in v1.6).** In the exact S9 family, on $\Delta=10^4n^{4/3}$, Theorem LC implies

$$
\sup_z|c_3(z)|\le C_{\rm lc}N\Delta^{-7}(1+\log n),\qquad C_{\rm lc}=9\times10^8<10^9. \tag{13.6}
$$

Indeed (8.L5) is stronger because $1+\log n>1$. Theorem LC-prime therefore proves the $R^{4/9}$ consequence that was conditional in v1.5. The old conditional envelope bound $.002169$ is superseded by the proved, log-free bound $.001020$. The covariance and derivative bookkeeping is fully carried out in Section 8.5b; no statement that unspecified triples merely “count as $O(N)$” is used as a proof.

**Theorem C2 (gap and four readout budgets: sufficient, not necessary).** Fix $\Delta\ge10^4$ and use the same S9 geometry, shifts, preparation and window. Suppose that, uniformly for all $R\ge2$, memories and labels:

(H0) every branch has a simple ground state with gap at least $g_*>0$;

(H1) $|\widehat E_0(\{0,j\})-\overline J_{0j}|\le\rho_3|\overline J_{0j}|$, with $\rho_3\le5\times10^{-6}$;

(H2) $\sum_{k\ne0,j}(2t\widehat E_0(\{j,k\}))^2\le\tfrac92\Lambda_3$ for $t\in I_R$;

(H3) $T\,\mathbb E_{z'}|\rho_j^{E_0}|\le\varepsilon_3$, uniformly also in the source sign;

(H4) $\sup_{t\in I_R}|D_j(t)-D_j^{E_0}(t)|\le\varepsilon_4$,

where $\varepsilon_3+\varepsilon_4\le.003$. Then $D_j(t)\ge.98538$ for every $R$ with this fixed $\Delta$.

*Proof.* Use the exact Walsh flip decomposition (13.1). The constant term is a common phase; (H1) controls the source coefficient, (H2) bounds the loss from memory-pair phases by the same product-cosine inequality as in Section 4, and (H3) controls the remaining phase by $|e^{ia}-e^{ib}|\le|a-b|$. Add (H4). The condition $\Delta\ge10^4$ ensures the Gaussian pair-reference and tail conditions used in (4.12)–(4.14), so $\rho=(1.001)(1.0001)(1+\rho_3)-1$ and the $.003$ total error reproduce the stated numerical readout. (H0) supplies a gapped ground-state setting; once the four readout budgets themselves are assumed, the numerical implication does not use the gap independently. $\square$

No converse has been proved: the readout guarantee does not require each separate budget to hold, and it does not imply a uniform spectral gap. In particular, the equivalence wording in the v1.5 README and history is corrected by this one-way implication. Conditions (H1)–(H3) concern specified energy-flip aggregates; they are not equivalent to decay estimates for every Walsh coefficient at every diameter. A suitable locality theorem could help prove them, but that additional implication needs proof. Likewise equilibrium ground-state locality does not, by itself, supply (H4) for a common noneigenstate over the growing time window.

Along the curves of Section 8.12 the hypotheses of Theorem C2 are verified rather than assumed. With the P1 preparation on $\Delta=10^4n^{1/2}$: (H0) is Lemma NP-2(a); (H1) holds with $\rho_3\le2.8\times10^{-6}$, by Lemma NP-6 combined with (4.8), since $(\rho_{\rm NP}+15/(\Delta L^2))/(1-15/(\Delta L^2))<2.74\times10^{-6}$; (H2) holds by Lemma NP-7 with $\sum_k(2t\widehat E_0(\{j,k\}))^2\le2L_{\rm pair}<2.6030\times10^{-3}<\tfrac92\Lambda_3=2.6277\ldots\times10^{-3}$; (H3) holds with $\varepsilon_3\le2\times10^{-16}$; and (H4) holds with $\varepsilon_4\le1.2\times10^{-25}$. With the Gaussian preparation the same holds on $\Delta=10^4n^{3/5}$, with $\rho_3<2.5\times10^{-6}$ and $\varepsilon_4\le1.5\times10^{-14}$. The fixed-$\Delta$ statement that C2 addresses remains open, because Lemma NP-1 needs $\Omega^2>h'_N$. Section 8.14 verifies the corresponding budgets for P1 at logarithmic confinement, with (H1) read at every shift (Lemma RD); a fixed-$\Delta$ version is still not proved.

### 13.5 Fixed confinement: rigorous obstructions to two direct proof routes

**Theorem O (bond norms and full-space convexity).** Keep $c>0$, $a,g>0$ fixed and retain all oscillator coordinates on the real line.

1. For a collinear pair with $d_{ab}=\ell e_z$, the multiplication operator defined by (2.2) satisfies

$$
\|V_{ab}\|\ge g\{f_c(0)+f_c(|\ell|)\}>g f_c(0). \tag{13.O1}
$$

Consequently no bound $\|V_{ab}\|\le C(1+|r_a-r_b|)^{-\alpha}$ with fixed $C$ and $\alpha>0$ can hold for all pairs of the S9 family. This conclusion is unchanged by the label-dependent coordinate translations.

2. For full cubes $R=n^3$, every label vector satisfies

$$
\inf_x\lambda_{\min}\bigl(\nabla^2V(x+\Lambda z)\bigr)
\le-gD_2n. \tag{13.O2}
$$

In particular, for any fixed $\Omega$, the full branch potential fails to be globally convex for all sufficiently large full cubes. The $O(n)$ order of Theorem L's full-space Hessian bound is therefore sharp in order, although its coefficient is not claimed optimal.

*Proof.* For (13.O1), choose $u_a=s+\ell/2$ and $u_b=s-\ell/2$. As $s\to\infty$, the mobile-mobile separation tends to zero exactly, the two mobile-fixed terms tend to zero, and $V_{ab}\to g(f_c(0)+f_c(|\ell|))$. A continuous multiplication operator has norm equal to its essential supremum, so this limit gives the bound. In units $c=.05,g=1$, its distance-independent part exceeds $22.56$.

For (13.O2), set $u_a=Q-r_a\cdot e_z$ for every site, including the source. All mobile charges then have the same axial height $Q$. For each fixed finite array, the mobile-fixed second derivatives tend to zero as $Q\to\infty$. At the limiting mobile-mobile configuration, write $D_{ab}=|d_{ab}^{\perp}|$ and $w_{ab}=-g\phi_{ab}''(-d_{ab}\cdot e_z)$. The Gaussian integral (2.1) gives $w_{ab}>0$; for collinear pairs it equals $gD_2$, and for transverse pairs it equals $-g f_c'(D_{ab})/D_{ab}>0$. The limiting Hessian is the negative weighted graph Laplacian:

$$
v^TH_\infty v=-\sum_{a<b}w_{ab}(v_a-v_b)^2.
$$

Choose a unit vector supported on one full memory column and with zero sum on its $n$ sites. The complete collinear subgraph contributes exactly $-gD_2n$, and every other edge contributes a nonpositive amount. Passing to the Rayleigh-quotient limit proves (13.O2). If $gD_2n>\Omega^2$, the Hessian of the total potential is negative in some direction for sufficiently large finite $Q$. $\square$

These are route-specific negative results. They do not show that the interacting spectral gap closes, or that fixed-confinement records are impossible. The configurations used in the proof lie far from the Gaussian concentration region; a spectral localization argument may still exclude their influence on low energies. They do prove that uniform global convexity and a naive distance-decaying operator-norm decomposition cannot supply the desired result.

The second-order star localization suggested in v1.5 remains a possible improvement, but its entrywise assertion $(|\Sigma|W)_{j0}\lesssim |K_{j0}|/\Delta^4$ was not proved. A row-sum Neumann estimate does not imply that entrywise bound: matrix powers sum paths through intermediate sites, and the absolute $1/r^3$ kernel is marginal in three dimensions. No fixed-$\Delta$, all-$n$ conclusion is drawn from that assertion here. At fixed $\Delta$, the sufficient estimate $m\le(109+48\log n)/\Delta^2$ also eventually leaves the range $m<2/3$ required by Lemma LC-A. This loss of a sufficient estimate is not a proof that the actual covariance becomes nonlocal.

The remaining fixed-confinement task is therefore substantive: establish ground-state and label-flip locality in a norm appropriate to low-energy oscillator states, control the higher ground-energy remainder with the $T_R=O(R^2)$ window, and separately bound the common-preparation echo. Equilibrium LPPL alone does not imply the long-time echo estimate (H4). Version 1.6 proved Theorem LC and the route obstructions above. Version 1.7 proves the convex-regime Theorems NP-G and NP-P1, and Theorem O(2) marks the exact limit of that route (Corollary NP-B). Neither version proves an LPPL theorem for the exact interacting array at fixed confinement or solves a recognized public open problem. Version 1.9 proves the P1 record theorem at logarithmic confinement without global convexity (Section 8.14); it also does not claim a general LPPL theorem. Version 2.0 decides the signed-kernel input order by order (Section 8.15) and re-types the fixed-confinement target (Section 13.12); it proves no fixed-confinement theorem.

### 13.6 Historical witnesses and their limits

The supplied lineage describes a short oscillator chain with $\Omega=1$, $g=.1$, $\lambda=.15$, $c=a/4$, $R=2,\ldots,5$. Over times extending from 40 to 400, the discrepancy from a quadratic-plus-mean reference grew to about $.29$, while a comparison using exact ground-energy phases remained around $4\times10^{-4}$ to $1.2\times10^{-3}$. These are source-reported finite-truncation witnesses, not rerun in this release. They illustrate secular reference-frequency error and motivate (H1)–(H4); they are not S9, not an all-$R$ result, and not evidence for permanent records or research grade 4.

### 13.7 Withdrawal of the Gaussian-preparation obstruction inference

Version 1.7 labelled Heuristic D as a hypothesis, but then used it to favor P1 over the Gaussian preparation and suggested a necessary exponent between $1/7$ and $1/5$. That inference is withdrawn. Its assumptions were (D1), excited probability at least $cN\Delta^{-5}$ with a size-independent $c>0$, and (D2), a proposed scale of excitation-dependent flip shifts. There are two distinct problems.

First, along full cubes $N=n^3+1$ and $\Delta=Cn^p$, (D1) exceeds one eventually whenever $p<3/5$. In particular it cannot hold in the proposed $p=3/7$ asymptotic regime. A low-excitation expansion can only be used while its probability remains small; extending it into its saturation regime is invalid. Replacing $cN\Delta^{-5}$ by a saturated probability does not preserve the inferred $N\Delta^{-7}$ loss or prove any positive power-law floor.

Second, an excitation probability and a frequency scale alone give no lower bound on local record loss. The actual occupied weights, phase cancellations, reference phase and spectral matching must be controlled. Proposition SP supplies an exact general counterexample to the overlap-only inference. It does not settle the coupled S9 array. The seed's finite-chain witness, with fixed short time and different parameter scaling, settles neither growing-window alternative.

The proved Gaussian result remains Theorem NP-G. Its $N\Delta^{-5}$ *upper majorant* has a route floor at $p=3/5$; this is not a lower bound on the physical preparation cost. Both Gaussian and P1 fixed- or polylogarithmic-confinement record conjectures are OPEN. Neither preparation is excluded or certified below its current design curve.

### 13.8 The seed's missing time factor: a precise certificate test

In units $a=g=1$, the unchanged S9 parameters give the exact identities

$$
T_R=1.01\,2\pi\,10^{15}n^6,\qquad
\lambda_e=5\times10^{-10}n^{-3},\qquad L=20n,
\qquad T_R\lambda_e^2=1.01\pi/2000.                     \tag{13.T1}
$$

**Proposition TS (power count of a specified positive certificate).** Consider a direct Duhamel upper majorant $B_R=T_RC\lambda_e^m\Omega^{-3/2}$ with fixed positive $C$. On $\Omega=C_\Omega n^p$, its power of $n$ is $6-3m-3p/2$. Hence this majorant is bounded only if $p\ge4-2m$. In particular:

| Residual rate in the assumed bound | Remaining time factor | Confinement needed to bound this certificate |
|---|---|---|
| $C\Omega^{-3/2}$ after removing $\sqrt N$ | $n^6$ | $p\ge4$, or $\Omega$ of order at least $R^{4/3}$ |
| $C\lambda_e\Omega^{-3/2}$ | $n^3$ | $p\ge2$, or $R^{2/3}$ |
| $C\lambda_e^2\Omega^{-3/2}$ | constant | fixed $\Omega$ can suffice for this term |
| $C\lambda_e L^{-3}\Omega^{-3/2}$ | constant | fixed $\Omega$ can suffice for this term |

*Proof.* Substitute (13.T1) and collect powers; $n\asymp R^{1/3}$. $\square$ The same count with the original $\sqrt N\asymp n^{3/2}$ gives $p\ge5$, recovering the seed's $R^{5/3}$ route. These are limits of specified positive upper bounds, never necessity claims for the dynamics. Oscillatory integration may avoid a factor $T_R$ and is explicitly allowed.

Thus merely removing $\sqrt N$ from the seed's $T_R\sqrt N\Omega^{-3/2}$ estimate does not prove its fixed-confinement conjecture. The seed correctly identifies the potential value of a local record theorem, but its claim that only one extensive norm needs repair is not a complete sufficient reduction. The time factor, branch-flip factors and phase reference must be part of the locality statement.

### 13.9 Non-convex localization is not the only missing estimate (v1.8 analysis, completed in v1.9)

Theorem ST proves full-space stability even though Theorem O rules out size-independent global convexity. It supplies no size-independent gap or spatial response decay. Moreover, granting a hypothetical non-convex scalar variance inequality is insufficient to carry over the displayed NP certificate unchanged.

To see the algebraic obstruction, suppress tails and optimistically retain bounded $B_\infty$ and $\Phi_M$ in the positive $r_4$ majorant of Lemma NP-6. Its factors are:
- $\sqrt R$;
- $M_2(r_{\min})/\kappa_s\asymp1$;
- $\Psi\asymp\Delta^{-1/2}\sqrt{1+\log n}$;
- $g_0^{-2}\asymp\Delta^{-2}$ and $\Omega^{-2}\asymp\Delta^{-2}$.

The displayed bound therefore still contains a positive contribution of order

$$
n^{3/2}\Delta^{-9/2}\sqrt{1+\log n}.                    \tag{13.L1}
$$

This residue is not the only one in the displayed majorant, and it is not the first to grow. The exponent engine applied to the v1.7 expressions at $\Delta=10^4n^p$ (Appendix O, F28-02) gives three growing terms:
- $r_2$ has decay exponent $0$ at $p=2/5$ and grows below it. Its source-row factors are $\sqrt R\,M_3(r_{\min})g_0^{-1/2}$ and $R\,M_4(r_{\min})g_0^{-1}$ inside $\|\nabla\rho_0\|_2$.
- $r_4$ has exponent $0$ at $p=1/3$; this is (13.L1).
- The Efron–Stein source term $\lambda_0\sqrt R\,T_3^{\rm src}$ of $H_3$ has exponent $0$ at $p=1/4$.

All three come from pairing a source-row quantity of $\ell^2$ size $\sqrt R\,L^{-3}$, or a sum over $R$ partners, with a label-uniform bound. For any fixed power $q$, substituting $\Delta=C(\log n)^q$ into these majorants diverges. These are algebraic tests of the *existing estimates*, outside the established domain of Lemma NP-1, not physical no-go statements.

Version 1.9 removes all three: Lemma SC pairs the source row with column sums of the site-resolved matrix $\Gamma$, and Lemma RD reads the source coefficient at every shift so that no source Efron–Stein sum is formed. The v1.8 statement that a time-dependent occupied-state estimate "remains a separate obligation" is corrected for P1 (F28-01). For P1 the echo is controlled uniformly in time by the common-vector lemma once the infidelities are small, and Lemma LOC-B makes them small for the exact non-convex Hamiltonians. Lemmas ER and OB remain relevant to the Gaussian preparation.

### 13.10 The grade-4 target and the outcome of the v1.8 routes (historical)

The v1.8 target was the seed's full nonlinear S9 record theorem at fixed or polylogarithmic confinement, with all its original quantifiers and a declared preparation. A qualifying proof had to meet four conditions:
- state an explicit design law and a lower readout bound uniform in $R$, every memory and the whole $I_R$;
- identify the external limitation it overcomes;
- not silently replace the full Coulomb potential, shorten the window or choose branch-dependent preparations;
- not fit parameters after observing the answer.

| Route attempted in v1.8 | Result obtained | Status after v1.9 |
|---|---|---|
| Replace configuration convexity by positive field energy | Theorem ST: exact full-displacement energy lower bounds | Used in Lemma LOC-A (out–out dipoles). Operator ordering does not yield the gap; Lemma LOC-B obtains it by comparison with a convex model instead |
| Replace global state comparison by relative evolution | Lemma ER and Proposition SP: common errors can cancel exactly | Not needed for P1 (time-uniform echo). Still relevant for the Gaussian preparation |
| Use occupied bands or matched spectra and retain all time factors | Lemma OB; restored S19-FW criterion; Proposition TS | Not needed for P1. Still relevant for the Gaussian preparation and for seed Duhamel routes |

### 13.11 The v1.9 outcome and the remaining obligations

The v1.9 target was fixed by preparation before the work began:
1. *P1:* a logarithmic or polylogarithmic record law with the exact non-convex Hamiltonian. This was the static critical path: exponential localization plus spatially resolved response.
2. *Gaussian:* a local echo estimate. This was not attempted beyond the retained v1.8 criteria.

The decisive kill tests were specified before the proofs were completed:
- a configuration violating (8.LG6);
- a finite ground state violating (8.LG8);
- a growing envelope term at $\Omega=10^4\ell_n$;
- a certified readout below $.98$.

None occurred; the rows are listed in Section 12.5. Outcome: Theorem NP-LOG. The table records the state after v1.9; Section 13.12 updates the fixed-confinement rows.

| Question | State after v1.9 |
|---|---|
| P1 records at logarithmic confinement | PROVEN (Theorem NP-LOG), with constants certified for every real $n\ge2$ |
| P1 records at fixed confinement | OPEN. The absolute dipolar row sum $\widehat S_2\asymp\log n$ and the union over $N$ sites in Lemma LOC-B each force a logarithm. A signed-kernel Lemma SR and a flip-local LOC-B are the identified missing objects. The coefficientwise second-order bound is false; the nonperturbative response remains open (Sections 8.15–8.16) |
| Gaussian records at fixed or polylogarithmic confinement | OPEN. Theorem S's global fidelity $N\Delta^{-5}$ is the only available echo control. Proposition SP shows that global infidelity alone does not imply record loss, but no local echo bound for S9 is proved |
| Uniform gap of the exact branch Hamiltonians | PROVEN at $\Omega_R=10^4\ell_n$: at least $\tfrac12\widehat g_0-o(1)$ (Lemma LOC-B). Not proved at fixed $\Omega$ |
| General LPPL for the exact array | Not claimed. Theorem NP-LOG proves only the flip and response statements its readout needs |

### 13.12 The fixed-confinement target after the v2.1 audit

The user-fixed grade-4 target is unchanged: either prove EG together with nonperturbative source-row transfer, or prove a fixed/sub-logarithmic record theorem in the full model. Both retain the S9 geometry, every memory, the entire growing observation window and a common preparation. The requested primary-text comparison is a separate outstanding requirement.

| Question | Current state |
|---|---|
| Signed first-order response | PROVEN coefficientwise on every S9 set (DF) |
| Uniform second Taylor coefficient | FALSE on full cubes: edge $2\log n$, corner $(3/2)\log n$ (EL, SRC) |
| Nonperturbative edge growth EG | OPEN; continuum mode and finite lattice values do not close it |
| Source-row transfer | OPEN; SRX gives an exact reduction to $B^{-1}v$ and bounds the source feedback |
| Quadratic fixed-confinement obstruction | CONDITIONAL on divergence of the actual source factor; WO proves failure somewhere in the prescribed window at a fixed uniform gap |
| Quadratic sufficient law | Retained $O(\sqrt{\log R})$ (Q/Q-prime) |
| Sharp $(\log R)^{1/4}$ law | HEURISTIC; neither necessity in the joint limit nor all-memory sufficiency has been proved |
| Convexified comparator, its common ground state | PROVEN $O(\sqrt{\log R})$, $\widehat D\ge.9885390$ (COMP-SQRTLOG) |
| Full nonlinear model, P1 | Retained $O(\log R)$ (NP-LOG); fixed or sub-logarithmic law OPEN |
| Gaussian preparation | No new bound; inherited obligations unchanged |

Three research rounds were executed. The source round derived SRX and solved the actual S9 drive; it did not obtain an all-scale amplitude estimate. The nonlinear-route round found that TC alone would grow like $\ell^{5/4}$ at square-root-log confinement, then removed that term with RD-V; the full-model localization and echo remained unresolved. The uniformity/literature round rebuilt the wedge transfer determinant, constructed an explicit counterexample to the pointwise-to-joint-limit inference, and attempted the named original texts. It did not obtain the requested original-text closure.

The precise remaining proof tasks are:

1. Establish or refute a lattice corner asymptotic with a nonzero driven amplitude for the actual S9 source. If a sharp growth law is claimed, make the remainder, onset and amplitude uniform in the joint $(n,\Omega)$ regime.
2. Prove full-model common-preparation echo and flip-local energy control at sub-logarithmic confinement, for example the sufficient budget (8.FT1). Removing only an extensive energy error is insufficient.
3. Complete the specified primary-source equation comparison. The continuum wedge calculation cannot be advertised as externally novel until that collision is resolved.

The failure of the present positive localization envelope is not a no-go theorem. Theorem EL likewise does not preclude every signed or nonperturbative response estimate. These distinctions preserve the original scientific question rather than replacing it with an easier model.

### 13.13 The target after v2.2

The user-fixed grade-4 target was: either prove EG together with nonperturbative source-row transfer, or prove a fixed or sub-logarithmic record theorem in the full model. Both retain the S9 geometry, every memory, the whole growing window and a common preparation.

| Question | State after v2.2 |
|---|---|
| Full nonlinear model, P1, sub-logarithmic law | PROVEN at $\Omega_R=10^4\sqrt{\ell_n}$, $D_j\ge.98853$ (Theorem NP-SQRTLOG) |
| Full model below $\sqrt{\log R}$ or fixed | OPEN. The absolute dipolar row sum bounds the convex-comparator route at $\sqrt{\log}$ |
| Lattice transfer from continuum to lattice, including the actual S9 source row | PROVEN one-way (Theorem CR) |
| Record failure at fixed confinement (quadratic model) | CONDITIONAL on Hypothesis EG-C (Corollary CR-R) |
| Hypothesis EG-C (continuum edge unboundedness) | OPEN. Log-scale heuristic in Remark CR-H; three missing estimates L1–L3 |
| Hypothesis EG (lattice rate $n^\gamma$) | OPEN, and no longer needed for the obstruction |
| Sharp $(\log R)^{1/4}$ law | HEURISTIC |
| Gaussian preparation | Unchanged (NP-G) |
| Named primary-source comparison | Still incomplete (Section 15.12) |

Alternative (ii) of the user's criterion is met by Theorem NP-SQRTLOG. Alternative (i) is not: its lattice half is closed, but the continuum half, EG-C, is not proved.

## 14. Mission relation and physical obligations

The relevant mission question is FQ2, the emergence of state, event and record; the immediate frontier is RQ3. The theorem supplies a controlled downstream record calculation for a declared Hamiltonian. It does not derive the instrument, the pointer basis, the registers, the trap, or the physical time parameter. Its role remains SUPPORT + METHOD before a completed measurement branch of the programme spine. Theorems L, LOC-2, LC, LC-prime, NP-G, NP-P1, N, Q, C1, C2, O, the v1.9 Theorem NP-LOG and the v2.0 Theorems DF and EL, Proposition W and Corollary Q-prime sharpen the mathematics of that calculation and its open problem; none of them changes an FQ/RQ bridge state. The v2.2 Theorems NP-SQRTLOG and CR and Corollary CR-R are in the same position: they sharpen the declared-model calculation and do not derive an instrument, trap, preparation or clock. Hypothesis EG is a mathematical conjecture about the declared model, not a physical prediction. The P1 preparation of Theorem NP-P1 is a declared input exactly like $\Phi$; it is not derived from an action, and its advantage is mathematical.

A physical transplant would require a concrete isometry or encoding

$$
\mathcal I:(\mathbb C^2)^{\otimes N}\otimes L^2(\mathbb R^N)\longrightarrow\mathcal H_{\rm physical},
$$

a compressed action-derived Hamiltonian agreeing with $H_{\rm MC}$ up to a controlled error, a leakage bound on the observation window, and a readout map relating (2.11) to actual observables. The scalar convolution in Section 2.1 supplies none of those maps by itself. In particular, the S14 H5 singlet must not be identified with a charged internal binary register without an explicit construction. The corpus gate "a nonzero stationary Bloch component is not an instrument" (ZS-M69 registry) and the commutative-carrier no-record theorem (ZS-M68 Theorem 5.1) were reported as re-read in the v1.5 source record: the oscillator-coordinate coupling is non-commutative on the recorded side, so the latter does not exclude the construction, and the former is respected by not calling $D_j\ge.98538$ a Born record.

| Existing obligation | Status and exact reason |
|---|---|
| D-M69-MOVING | OPEN: the moving physical mechanism is not derived by this oscillator calculation |
| D-M69-INSTRUMENT | OPEN: a state-selecting instrument and its relation to records remain to be constructed |
| K17, K18 | OPEN inherited obligations; the tensor factorization memory $\otimes$ source is declared, not realized |
| D-S14-EVENT-001 | OPEN: the event/carrier bridge is not supplied |
| D-HCLK-001 | OPEN: the physical clock and dimensionful time normalization are not derived; the window $I_R$ is a model time |

The v1.5 source-scope record reports that the connected manifest, constants/lemmas index, dependency graph, physics/mathematics claim ledgers and debt index were consulted (Repo 3 at Corpus-OS v1.1/v1.1.1, plus the M70–M72 manifest log). No applicable asset was found within that reported index scope; the corpus items actually reused are M69 Theorem T5 (field-parity selection, as precedent), M71 Lemmas L3–L6 (discrete oscillator inequality and IMS localization, as the only in-house localization precedent), M72 Appendix S6.10 (as inherited), and the M72 Section 12.7 comparison structure (as the format of Section 15.5). No new debt identifier, mission axiom or paper-code family is introduced; the manifest, reusable-lemma and debt indexes and M70–M72 manifest log were refreshed in v1.6 before external source retrieval. These indexes do not yet incorporate the submitted M73 v1.5; their silence is not a novelty proof.

The chosen constants and geometry are design parameters for a sufficient example. There is no fit to cosmological data or claim that these numbers are selected by a Z-Spin action. The observable improvement is an explicit resource guarantee inside the declared family, now with an exact statement of what mathematical object would remove its residual $R$-dependence. The corresponding kill test is failure of that guarantee or failure to build the required physical maps when a physical interpretation is proposed.

## 15. Prior art, provenance and comparison

### 15.1 Primary-source comparison retained from v1.4

The following comparisons distinguish facts read in the sources from our application to the present model. A familiar identity or standard tool is not counted as new because it has been expressed in Z-Spin notation.

| Source and locator | Relationship to this manuscript |
|---|---|
| [Dusson–Sigal–Stamm, *The Feshbach–Schur map and perturbation theory*, Section 1, assumptions (A)–(C), Theorem 1.1, equations (1.2)–(1.8), higher-order Remark 3 in the PDF accessed for the v1.4 audit](https://arxiv.org/pdf/2105.02058) | Covers symmetric form-bounded perturbations and explicit eigenvalue/eigenvector estimates; higher-order refinements are available. It is a close standard alternative. Our mapping in Section 15.4 retains its form-bounded setting. |
| [Gong–Yoshioka–Shibata–Hamazaki, Theorem 1, equations (6)–(9)](https://arxiv.org/pdf/2001.03421) | Provides observable-error bounds for constrained dynamics with bounded perturbations. Its endpoint-plus-secular structure is related to Theorem A. |
| [Banerjee–Griffiths–Widom, Section IV A, equations (27)–(30)](https://arxiv.org/pdf/cond-mat/0012280) | Supplies the positive field-energy stability method underlying the dipole matrix bound of Appendix B. |
| [Andrews–Clutterbuck, Theorems 1.3 and 1.5](https://arxiv.org/pdf/1006.1686) | Supplies the modulus-of-convexity spectral comparison and ground-state log-concavity framework of Appendix C; Theorem L improves only the input modulus. |
| [Jentschura–Surzhykov–Zinn-Justin, equations (15a)–(16d)](https://arxiv.org/pdf/0901.4964) | Perturbative expansions for anharmonic oscillators; parity-sensitive perturbation structure is established background. |
| [Riedel–Zurek–Zwolak, introduction, equation (1), and the spin-environment model](https://arxiv.org/pdf/1205.3197) | Redundancy and its loss through environment interactions; motivates the physical question. |

### 15.2 Primary-source collision with locality and linked-cluster results

The load-bearing locality comparison has been upgraded from the v1.5 abstract-only survey to the following source-level checks. Each mapping assessment is this manuscript's inference from the cited hypotheses, not a claim made by the cited authors about S9.

| Primary source and exact locator | Verified scope | Mapping to the present task |
|---|---|---|
| [Henheik–Teufel–Wessel, Section 2, Definition 1 and Theorem 3; proof via Theorem 7](https://arxiv.org/pdf/2106.13780) | Possibly infinite-dimensional site spaces and unbounded gapped on-site terms are allowed. Interactions have a fixed finite range and small uniform operator norm. | The v1.5 finite-dimensional exclusion was false. The actual missing hypotheses are a suitable interaction structure and norm control; Theorem O obstructs the direct full-bond mapping. |
| [De Roeck–Schutz, Section 2 and Theorem 3.2](https://arxiv.org/pdf/1501.04571) | Finite-dimensional local spaces, a decaying interaction norm and a uniformly isolated spectral sector along the perturbation path give local operators relating eigenvectors. | No corresponding uniformly gapped path or suitable decay norm is proved for the exact oscillator array. A label flip changes a star of pairs, not a fixed-support perturbation as supplied. |
| [Wang–Hazzard, Section II, equations (6), (16) and Table I](https://arxiv.org/pdf/2208.13057) | The response argument uses a uniform gap along the perturbation path. Its power-law specialization requires operator-norm decay with $\alpha>D$. Section II A itself does not require finite local dimension. | For the harmonic kernel $\alpha=D=3$; for the exact full-space bonds even the decaying norm hypothesis fails. These facts obstruct this specialization, not all possible state-dependent extensions. |
| [Nachtergaele–Raz–Schlein–Sims, equations (3.1), (4.1), Theorem 4.1 and Theorem 5.2](https://arxiv.org/pdf/0712.3820) | Oscillator Hilbert spaces are admitted. The displayed anharmonic model has nearest-neighbor harmonic couplings and on-site perturbations satisfying Fourier-integrability conditions. Theorem 5.2 gives clustering with an additional gap assumption. | Neither the long-range harmonic array nor the two-coordinate Coulomb remainder is the displayed model. The v1.5 statement that this source contains no ground-state result was too broad. It does not furnish the missing uniform gap or (H4). |
| [Chatterjee, Theorem 2.2 and Lemma 5.3 with its proof](https://arxiv.org/pdf/0705.1224) | Gaussian interpolation, integration by parts and gradient/Hessian control yield second-order Poincare normal-approximation bounds. | These analytic tools are imported background. The added calculation is the parity-resolved bound for $\mathbb E[U(\mathcal L^{-1}U)^2]$, with explicit Coulomb derivative and tail constants; no claim to invent Gaussian covariance interpolation is made. |
| [Bravyi–DiVincenzo–Loss, Section 4.1, Theorem 1 and Section 4.3 Theorem 2](https://arxiv.org/pdf/1105.0675) | The many-body setting uses an on-site reference, bounded-degree two-spin interactions and a tensor-product low-energy sector; the linked-cluster theorem restricts effective terms to connected clusters. | S9 uses a correlated quadratic reference and full-space interactions on a growing-degree graph. The general linked-cluster principle is known; Theorem LC supplies an explicit derivative-norm estimate that does not require this direct product-reference mapping. |
| [Blume-Kohout–Zurek, equations (1)–(6) and the Hamiltonian (4)](https://arxiv.org/pdf/0704.3615) | Quantum Brownian motion with a harmonic oscillator bath; redundancy is measured through mutual information of environment fragments, and linear evolution preserves Gaussianity. | This is the relevant Gaussian physical baseline. M73's individual binary-register trace distance and its anharmonic error certificate are different objects. Theorem Q claims no novelty. |
| [*Local observable errors from truncating interaction tails in gapped quantum lattice systems*, Section II A and Proposition IV.1](https://arxiv.org/html/2608.15576v1) | The displayed setting has finite-dimensional local algebras, a summable weighted interaction norm with exponent above dimension, and a uniform gap along interpolation. | This recent alternative also does not supply the full-space, marginal-range, common-preparation theorem needed here. It is a checked competing route, not an imported proof. |

The comparison identifies actual hypothesis mismatches and the extra proof in Theorem LC. It does not assert that the entire published literature has been exhausted, or that no stronger Gaussian or spectral method can reproduce the new bound. No result is classified as a public-open-problem solution from a search returning no match. The still-unread Bachmann–Michalakis–Nachtergaele–Sims paper listed in v1.5 remains background only; no theorem from it is imported in this revision.

### 15.3 Corpus and inherited comparisons

The lineage reports comparisons with M31 Section 4.4, M69 Theorem T5 and M72. M31 contains an erroneous intermediate algebraic line (line 221 of the source, asserting $PK^-P=\tfrac12K^-$ before line 222 correctly gives $0$); only the conclusion of Theorem M31.4, which stands, may be used. M69 already uses parity to remove certain odd-order terms, so parity itself is not new to this corpus. M72 supplies the cooling/Gram caution at Appendix S6.10. The S19-R/FW attribution is now resolved in the supplied seed's preserved lineage (Section 8, S19-R, and Section 10, S19-FW). These are internal proposition labels; searching only for the corpus paper ZS-S19 used the wrong identifier. Section 10.3 restores the spectral-matching error and positive-weight hypotheses. The locator repair is not a novelty claim. ZS-M68 Theorem 5.1 (commutative carrier gives no record) and ZS-M65 (Bayesian posterior record law) were read to confirm that the present record notion (a single-shot trace distance) is a different object from the corpus record law and is typed as such.

The prior manuscript also cited Porras–Cirac, Bravyi–DiVincenzo–Loss, Liu–Lu, Jansen–Ruskai–Seiler, Bachmann–De Roeck–Fraas, De Roeck–Schutz and Wang–Hazzard. Bravyi–DiVincenzo–Loss, De Roeck–Schutz and Wang–Hazzard are now checked at source level in Section 15.2; the remaining names are retained as inherited background, not freshly verified exclusions.

### 15.4 Explicit mapping to the closest form-bounded alternative

For the present application, choose

$$
H_0^{\rm DSS}=H_A-E_A+\beta I,\quad \beta=\Delta,
\quad W=U_z,\quad\lambda_0=\beta,\quad\gamma_0\ge\Delta,
\quad\lambda_*=\beta+\gamma_0,\quad PWP=0. \tag{15.1}
$$

Our off-diagonal form estimate is

$$
\|QWP\|_{H_0^{\rm DSS}}\le\frac\sigma{\sqrt{\beta(\beta+\gamma_0)}},
\qquad \Phi(W)\le\frac{\sigma^2}{\gamma_0}\le\frac{\sigma^2}{\Delta}. \tag{15.2}
$$

Thus its direct second-order bound has the expected $O(\sigma^2/\Delta)$ scale. This is our substitution into the source's notation, not an additional theorem asserted by that source for S9. A crude sufficient estimate of the complementary form norm in our model is

$$
\|Q U_z Q\|_{H_0^{\rm DSS}}
\le\frac{2B_N}{\Delta}
+\frac{2\|gK^{(c)}\|}{\Delta^2}\left(1+\frac{E_A}{\Delta}\right). \tag{15.3}
$$

Both terms must be budgeted. A sufficiently large $O(R^2)$ choice satisfies this crude substitution. It is **not** a necessary confinement bound for the DSS method and is not a proved limitation of the strongest standard theory. Section 8.11 shows explicitly that a Schur argument can use the same sharper structure and parity estimate.

### 15.5 Matched comparison of the new coefficient estimate

| Baseline | Same-object added work | Consequence and attribution |
|---|---|---|
| v1.5 Section 13.4: (13.6) unproved, $M_{\rm par}=O(N^{3/2}\Delta^{-7})$ | Lemma LC-A and full-space S9 bounds (8.L6)–(8.L7), including label Hessians and Gaussian tails | $9\times10^8N\Delta^{-7}$ and the proved $R^{4/9}$ certificate under the unchanged contract |
| Chatterjee's Gaussian interpolation and derivative method | Parity expansion of the resolvent coefficient, Holder exponents $(4,4,2)$ and an entrywise Hessian sum | A quantitative coefficient estimate, not a new Gaussian interpolation principle |
| Bravyi–DiVincenzo–Loss linked-cluster theorem | Correlated oscillator reference, derivative-moment control and explicit full-space constants rather than a bounded-degree product-reference substitution | General extensivity is known; its stated Coulomb bound requires the additional work here |
| DSS Theorem 1.1 and higher-order Remark 3 | The same spectral machinery can accept the sharper coefficient estimate | No claim that Feshbach–Schur theory cannot produce $R^{4/9}$; its crude norm substitution is not a lower bound |
| Published LPPL and Gaussian record calculations | Exact model and observable hypotheses compared in Section 15.2; Theorem O tests two direct routes | No fixed-confinement theorem imported by analogy |

The strongest overlap objection is that this is a quantitative application of established Gaussian and spectral methods. The text answers by exposing the exact extra estimate and its resource consequence, not by claiming that those methods were previously incapable of it. The proven change is the elimination of the cubic $\sqrt N$ loss for this full-space model and a strictly smaller sufficient exponent. Whether this is significant enough for the requested internal grade is a separate contribution judgment, not an automatic consequence of the exponent changing.

### 15.6 Provenance and independence

The supplied history reports a Codex-generated v1.6 and a Claude-generated v1.7. It also reports three Claude re-derivations of the v1.6 central estimates and a same-family hostile check of v1.7. Those are preserved historical reports, not new independent checks performed in the present session. The frozen v1.7 files contain the original details and limitations.

In the historical v1.8 session, its audit, proofs, code and integration were produced by one Codex agent. The following sentences describe that session; current independence is recorded in Section 16.0. No sub-agent, human reviewer or independent proof service checked the new results in this session. The original v1.7 verifier was rerun without modification in its declared dependency environment. The new identities received direct derivations, finite noncommuting matrix diagnostics and explicit fault controls, all within the generating lineage. They are not independently adjudicated by these procedures. Earlier independence limits are not reset by a version increment. qualified-human anchor: NONE.

### 15.7 Primary-source collision for the non-perturbative route

The route of Section 8.12 imports three functional-analytic theorems. It was compared with the dimension-uniform ground-state literature, which the v1.6 comparison had not covered. The table preserves the v1.7 source-access record, except for the explicitly identified primary-source upgrade for Sjostrand I in v1.8. Where only a citation record or secondary locator was confirmed, that limitation is retained.

| Source and locator | What it proves | Relation to Section 8.12 |
|---|---|---|
| [BL76] Brascamp–Lieb, J. Funct. Anal. 22 (1976) 366–389, Theorem 6.1 and Theorem 4.1 | Log-concavity of the ground state for a convex potential (Theorem 6.1); variance inequality for log-concave measures (Theorem 4.1). The locator of Theorem 6.1 was confirmed through a secondary citation (arXiv:2606.23614, Section 3.1), not by re-reading the primary text in this revision; the harmonic-plus-convex factorization is proved directly in Lemma NP-1 | Imported as Lemma NP-1 and Lemma NP-2(a). The new input is the modulus $g_0^2=\Omega^2-h'_N$ from Theorem L |
| [Caf00] Caffarelli, Commun. Math. Phys. 214 (2000) 547–563 (erratum 225 (2002) 449–450) | The Brenier map from a Gaussian to a more log-concave measure is 1-Lipschitz | Imported as Lemma NP-2(b). Citation confirmed; the statement was checked through a published proof note |
| [BGL14] Bakry–Gentil–Ledoux, *Analysis and Geometry of Markov Diffusion Operators* (2014), chapters on curvature bounds, Poincaré, Brascamp–Lieb and log-Sobolev | Gradient commutation and functional inequalities under a curvature bound | Imported as Lemma NP-2(c) (synchronous-coupling form) |
| [Sjöstrand, *Potential wells in high dimensions I* (1993), Theorem 6.2, printed p. 40](https://www.numdam.org/article/AIHPA_1993__58_1_1_0.pdf) | A single-well Dirichlet realization on a product domain, under the stated (B)--(D) structure/smallness assumptions and the dimension restriction (0.4), $N\le C h^{-N_0}$, has a simple low eigenvalue and a gap of order $h$ | Primary theorem read in this revision. It is not an arbitrary-$N$, fixed-$h$, full-space S9 gap theorem. Boundary conditions, dimension regime and derivative assumptions require an explicit transfer. The earlier combined references to the 1992 paper and Part II are retained as research leads, not as newly verified theorem imports |
| Helffer–Sjöstrand, Astérisque 210 (1992) 135–181; Helffer, J. Funct. Anal. 155 (1998) 571–586 and Ann. IHP Prob. Stat. 35 (1999) 483–508 | Semiclassical expansions of the thermodynamic limit; Witten-Laplacian covariance representations; uniform log-Sobolev inequalities and decay of correlations | Background for extensivity and for going beyond convexity (Sections 8.14 and 15.9); no theorem imported |
| Bach–Jecko–Sjöstrand, Ann. Henri Poincaré 1 (2000) 59–100; Bach–Møller, J. Funct. Anal. 203 (2003) 93–148 | Correlation decay at low temperature for non-convex Hamilton functions | Candidate tools for the non-convex step. Their hypotheses (classical lattice systems, local structure) have not been verified for S9 |
| Blume-Kohout–Zurek, arXiv:0704.3615; Tuziemski–Korbicz, EPL 112 (2015) 40008 | In quantum Brownian motion, redundancy grows with initial squeezing; spectrum broadcast structures appear | Physical baselines. No law relating trap resources to the number of records was found (NOT_FOUND, not ABSENT) |

*The v1.7 contribution claim and the strongest overlap objection.* The v1.7 manuscript proposed three additions beyond its imported tools:

1. the reduction of every record-relevant energy flip to the trap work of mean displacements, (8.NP1);
2. the exact response equation with an explicit covariance remainder bounded in $\ell^2$, (8.NP2), together with its source-row refinement (Lemma NP-5);
3. the resulting all-$R$ certificates, with explicit constants, for a marginal dipolar array. They are resolved by preparation and attain the convexity barrier of Theorem O.

The strongest objection is that this is a direct application of standard log-concavity machinery. That is correct for the tools, which are attributed as imported. The claimed addition is the flip reduction and the certificate. In the checked sources, neither a record certificate of this kind nor the response equation in this form was found. Hellmann–Feynman and stationarity themselves are textbook facts. The novelty classification is therefore IMPORTED for Lemmas NP-1 and NP-2, SPECIALIZED for Lemma NP-3, and OPEN-NOVELTY for the certificates of Theorems NP-G and NP-P1.

### 15.8 Source collision for the v1.8 additions

The new proofs do not acquire external novelty merely by receiving M73 labels.

| Addition | Closest checked baseline and access | Difference and current novelty status |
|---|---|---|
| ST | [Banerjee--Griffiths--Widom, *Thermodynamic limit for dipolar media*, Section IV A, equations (28)--(30)](https://arxiv.org/pdf/cond-mat/0012280): nonnegative total field energy minus self energies; primary PDF read | Exact application to the full four-charge Gaussian-smeared interaction and arbitrary displacements. SPECIALIZED; no new general stability method claimed |
| ER, OB | Duhamel differentiation, reducing subspaces and pure-state trace distance; full derivations in Section 8.13 | Standard identities organized around the measured relative evolution. SPECIALIZED; no all-$R$ S9 locality bound yet |
| SP | Exact tensor factorization; [Lidar--Chuang--Whaley (1998)](https://arxiv.org/abs/quant-ph/9807004) is an established decoherence-free-subspace baseline, whose primary abstract was checked | The spectator example is simpler than the cited theory, and is not attributed as that paper's theorem. It defeats the v1.7 overlap-only inference; it is not a novel protection mechanism |
| TS and the $r_4$ residue | Exact S9 time and shift scaling; the existing NP expression | Internal correction and route falsification; no physical lower bound or externally new no-go theorem |
| S19-FW | Supplied seed lineage, equations (S19R.3), (S19FW.1) | REUSED; restores a missing error term and its precise application conditions |

The checked primary [Henheik--Teufel--Wessel Theorem 3](https://arxiv.org/html/2106.13780v3) retains its Section 15.2 scope: possibly infinite-dimensional on-site systems, weak bounded finite-range interactions, and a suitably relatively bounded perturbation. The full S9 interaction has neither the required finite range nor the necessary decaying full bond norm (Theorem O). [Wang--Hazzard](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.020348) requires its power-law locality and gapped-path conditions; it is not a growing-time sudden-echo theorem for the present marginal dipolar array. These are actual transfer failures, not proof that a suitable state-dependent theorem is impossible. The newer tail-truncation source already listed in Section 15.2 was retrieved at its original [arXiv identifier](https://arxiv.org/html/2608.15576v1); its existence does not remove the hypothesis mismatch.

The bounded source search supports only the comparisons above. No claim of exhaustive absence is made. Sources previously disclosed as abstract-only, secondary-locator-only or citation-only remain at that evidence level unless explicitly upgraded here.

### 15.9 Source collision for the v1.9 additions

The load-bearing tools of Section 8.14 are compared below with their closest checked sources. Novelty classes follow the manuscript rules: IMPORTED, SPECIALIZED, EXTENDED, NEW, OPEN-NOVELTY. The search was bounded. It covered web searches for decay of correlations of quantum anharmonic crystals, Helffer–Sjöstrand covariance representations, Otto–Reznikoff covariance estimates and log-Sobolev semiboundedness, plus the primary sources listed. NOT_FOUND is not ABSENT.

| Addition | Closest checked source and access | Difference and class |
|---|---|---|
| Lemma SR | [Menz, *The approach of Otto–Reznikoff revisited*, Proposition 3.3](https://arxiv.org/pdf/1309.0862) (statement read): for classical Gibbs measures with conditional Poincaré constants $\varrho_i$, $|\nabla_i\nabla_jH|\le\kappa_{ij}$ and a strictly diagonally dominant $A$, $|\operatorname{cov}(f(x_i),g(x_j))|\lesssim(A^{-1})_{ij}\|\nabla_if\|\|\nabla_jg\|$ ([Otto–Reznikoff, J. Funct. Anal. 243 (2007)](https://www.sciencedirect.com/science/article/pii/S0022123606004058), record only). Helffer–Sjöstrand representation and Witten-Laplacian correlation methods ([Helffer, J. Funct. Anal. 1998](https://www.sciencedirect.com/science/article/pii/S0022123697932390), record only). Closest, added in v2.2.1 (F32-04): [Menz, *A Brascamp–Lieb type covariance estimate*, Theorem 2.3, Eq. (2.4)](https://arxiv.org/pdf/1402.5160) (read): the same $L^2$-gradient covariance bound for smooth observables of all coordinates, on products of Euclidean blocks, for classical Gibbs measures | Quantum ground state, resolvent-integrated covariance, diagonal convexity instead of conditional gaps, explicit factor $\tfrac12$. Obtained by applying the classical mechanism to the Trotter path measure with one time line per site. EXTENDED; the mechanism is known. *v2.2.1 (F32-04):* v2.2 also listed multi-site observables as a difference; Menz's Theorem 2.3 already covers them. Following the audit, the difference is limited to the transfer to the quantum ground-state (zero-temperature) resolvent through the Euclidean discretization, where diagonal convexity and the factor $\tfrac12$ enter, and to the application to the exact model |
| Lemma LOC-B | Log-Sobolev semiboundedness of Schrödinger forms (Federbush; [Gross, Amer. J. Math. 97 (1975)]; [Rothaus, J. Funct. Anal. 42 (1981)](https://www.sciencedirect.com/science/article/pii/0022123681900501), record only). Bakry–Émery LSI [BGL14]. Herbst's argument | The tools are standard. Two things are added here: a *localized* lower bound on $V-\widehat V$ that is a sum of single-coordinate functions supported off the box, obtained from positive field energy of the out-dipoles and near/far lattice counting; and a modified Herbst bound for $|\nabla F|^2\le CF$. Together they give an exponentially small, non-extensive comparison of energies, gaps and ground states. SPECIALIZED (tools) / NEW for this object (the localized bound) |
| Theorem L-hat | Standard cut-off and convexification of pair potentials | SPECIALIZED |
| Lemmas SC, PC, TC | Lemma NP-3 identities (v1.7), Lemma SR | SPECIALIZED |
| Lemma RD | Boolean Efron–Stein and Walsh algebra | SPECIALIZED; the application (no source Efron–Stein sum) is internal |
| Theorem NP-LOG | v1.7 Theorems NP-G/NP-P1 and Corollary NP-B (internal barrier). External locality theorems: [Henheik–Teufel–Wessel Thm 3](https://arxiv.org/pdf/2106.13780), [De Roeck–Schutz Thm 3.2](https://arxiv.org/pdf/1501.04571), [Wang–Hazzard](https://arxiv.org/pdf/2208.13057), [arXiv:2608.15576 Prop. IV.1](https://arxiv.org/html/2608.15576v1). Quantum-crystal Euclidean Gibbs measures: [Albeverio–Kondratiev–Kozitsky–Röckner, Ann. IHP Prob. Stat. (2001)](https://eudml.org/doc/77683) (Dobrushin uniqueness, small mass; record only), [Kozitsky–Pasurek](https://arxiv.org/html/math-ph/0509036) (existence and uniqueness; no decay theorem found in the text read), [Amour–Cancelier–Lévy-Bruhl–Nourrigat, Ann. Henri Poincaré (2007)](https://link.springer.com/content/pdf/10.1007/s00023-007-0343-7.pdf) (high-temperature exponential decay, exponentially decaying interactions) | The locality theorems need finite range or decaying bounded bond norms, a uniform gap along a path, or finite local dimension; Theorem O(1) excludes the full S9 bonds from those hypotheses. The quantum-crystal results treat thermal states or small mass with different interaction classes. No record-resource law or logarithmic confinement theorem for this model was found. OPEN-NOVELTY externally (bounded search), NEW relative to the corpus and to the internal barrier |

*Strongest overlap objection.* Every ingredient is a known technique, so the theorem could be read as a routine combination. The answer is partial. The ingredients are indeed known, and Lemma SR in particular is classified EXTENDED rather than new. What is not routine within this problem is the configuration of the argument. The exact Hamiltonian is not convex (Theorem O). Its bonds do not have decaying norms (Theorem O(1)). The obstruction of Corollary NP-B is sharp for convexity arguments. The previous certificate carried three growing source-row residues (Section 13.9). The new argument removes each of these without changing the model, window or observable. Whether this crossing is a significant change of the solvable problem class is a judgement recorded in Section 16, by an agent other than the generator.

Additional references for Section 8.14: [HS94] B. Helffer, J. Sjöstrand, J. Stat. Phys. 74 (1994) 349–409. [Hel02] B. Helffer, *Semiclassical Analysis, Witten Laplacians, and Statistical Mechanics* (World Scientific, 2002). [OR07] F. Otto, M. Reznikoff, J. Funct. Anal. 243 (2007) 121–157. [Men14] G. Menz, Electron. J. Probab. 19 (2014). [Men14b] G. Menz, *A Brascamp–Lieb type covariance estimate*, arXiv:1402.5160 (2014), Theorem 2.3, Eq. (2.4) (read in v2.2.1). [Gro75] L. Gross, Amer. J. Math. 97 (1975) 1061–1083. [Sim05] B. Simon, *Functional Integration and Quantum Physics*, 2nd ed. (AMS Chelsea, 2005). [GJ87] J. Glimm, A. Jaffe, *Quantum Physics: A Functional Integral Point of View*, 2nd ed. (Springer, 1987). The locators [HS94], [Hel02], [Gro75], [Sim05] and [GJ87] are cited as standard references for the stated classical facts and were not re-read in this revision.

### 15.10 Source collision for the v2.0 additions (historical search record)

In the v2.0 session, a separate agent instance ran a bounded novelty sweep of Section 8.15 with web search and primary-source retrieval. The following records that session; v2.1 upgrades and limitations are in Section 15.11. It also independently recomputed Proposition W from the stated interface conditions and the two angular constants of Theorem EL. The sweep's own checks were these:
- the root expansion $\nu=1-\delta^2/(8\pi^2)+\delta^3/(8\pi^2)+\ldots$ at $\delta=.3,.1,.03,.01$, including the sign of the $\delta^3$ term;
- the isotropic right-angle wedge, for comparison, which gives $\gamma\approx\delta/(2\pi)$, first order in the contrast;
- the edge constant $2$, analytically;
- the corner constant $\tfrac32$, by a $1500\times1500$ quadrature ($1.4999975$).

Novelty classes follow Section 15.9. NOT_FOUND is not ABSENT. The uniaxial-wedge search was the thinnest part of the sweep.

| Addition | Closest checked source and access | Difference and class |
|---|---|---|
| Theorem DF | Continuum prism tensor: [Newell, Williams and Dunlop, J. Geophys. Res. 98 (1993) 9551](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/93JB00694) (metadata only); [Smith et al., J. Appl. Phys. 107 (2010) 103910](https://www.academia.edu/57056885/The_demagnetizing_field_of_a_nonuniform_rectangular_prism), Eq. A8 versus A12 (read): diagonal terms are face arctangents (solid angles), off-diagonal terms carry edge logarithms. Polyhedral gravity-gradient tensor: [Ren et al., Surv. Geophys. 39 (2018) 901](https://scispace.com/pdf/gravity-gradient-tensor-of-arbitrary-3d-polyhedral-bodies-usu4rhsekp.pdf), App. B (read). Planewise Poisson summation of dipole lattices: Nijboer and de Wette, Physica 24 (1958) 422, and de Wette and Schacher, Phys. Rev. 137 (1965) A78 (not opened) | Continuum fact IMPORTED. The lattice theorem, a uniform-in-$n$ certified bound on every S9 set by column telescoping, was not found: EXTENDED, thin; a referee could call it SPECIALIZED |
| Theorem EL | The same prism and polyhedron tensors (edge logarithms of off-diagonal components); expansion of a Meixner power law $r^{\nu-1}$ in the contrast | Mechanism known: EXTENDED. The second iterate of the $zz$ kernel and the constants $2$ and $\tfrac32$ (with the numerically observed boundedness at vertical edges) were not found in lattice or continuum form: OPEN-NOVELTY. The constant $2$ is not independent of Proposition W |
| Lemma SRC | Taylor and commutator estimates for a multiplier varying on scale $n$ | SPECIALIZED; not searched specifically |
| Proposition W | Anisotropic multi-material corners: [Mantič, París and Berger, Int. J. Solids Struct. (2003)](https://www.sciencedirect.com/science/article/abs/pii/S0020768303002920) (not opened); Barroso, Mantič and París, Int. J. Fract. 119 (2003) 1–23 (not opened); [Nicaise and Sändig, *General interface problems I*](https://www.academia.edu/31513297/General_interface_problems_I) (read; Mellin framework). Isotropic edge condition: Meixner, IEEE Trans. Antennas Propag. 20 (1972) 442; Bach Andersen and Solodukhov (1978); Van Bladel (1991), *Singularities at an edge* (not opened or not rendered) | Stretch-to-Laplace method and characteristic equation: SPECIALIZED. The root $\nu=1$ together with the second root $1-\delta^2/(8\pi^2)$, i.e. a shift second order in the contrast, was not found: OPEN-NOVELTY, minor. Van Bladel and the anisotropic-corner papers are the most likely places for the explicit formula |
| Corollary Q-prime, Proposition LN | Internal (Theorem Q, Theorem DF, Neumann series). Site-resolved local fields on finite lattices: [Rahmani, Chaumet and Bryant, Astrophys. J. 607 (2004) 873](https://www.fresnel.fr/perso/chaumet/articlepdf/astro_04.pdf) (read; deviations from Clausius–Mossotti near interfaces, no edge growth reported); [Twengström et al., Phys. Rev. Materials 1 (2017) 044406](https://arxiv.org/html/1701.07648) (read; uniaxial moments in cubes, no edge analysis) | SPECIALIZED as mathematics. The physical statement, an $\Omega^{-4}\log n$ term of the local-field factor at horizontal edges, was not found |
| Hypothesis EG | Meixner edge scaling $(a/L)^{\nu-1}$ (isotropic example: arXiv:2607.11613, read). [Yurkin, Maltsev and Hoekstra, J. Opt. Soc. Am. A 23 (2006) 2578](https://scattering.ru/papers/Yurkin%20et%20al.%20-%202006%20-%20Convergence%20of%20the%20discrete%20dipole%20approximation%201.pdf), Sec. 2.D (read; smooth-field assumption excludes edges). Makarenko, Yurkin, Shcherbakov and Lapine, Phys. Rev. B (2025), arXiv:2509.14690 (read; sharp-edged discrete cubes do not approach homogenized behaviour) | Conjecture only. Mechanism IMPORTED; lattice growth law NOT_FOUND |
| Signed-kernel context | [Otto–Reznikoff, J. Funct. Anal. 243 (2007), Theorem 1](https://webdoc.sub.gwdg.de/ebook/serien/e/sfb611/274.pdf) (preprint read): absolute couplings $\kappa_{ij}\ge\vert\nabla_i\nabla_jH\vert$. [Menz, Electron. J. Probab. 19 (2014), Theorem 1.7](https://ar5iv.labs.arxiv.org/html/1309.0862) (read): (1.4) diagonal dominance in absolute values; (1.10) decay $\vert i-j\vert^{-d-\alpha}$, $\alpha>0$. [Menz and Nittka, J. Stat. Phys. 156 (2014) 239](https://arxiv.org/abs/1309.0857): one dimension. [Bauerschmidt and Bodineau, J. Funct. Anal. 276 (2019) 2582, Theorem 1](https://arxiv.org/html/1712.03676) (read): spectral-width condition, unbounded spins allowed | The three-dimensional dipole kernel has $\alpha=0$ and absolute row sums $\asymp\log n$, so the Otto–Reznikoff/Menz conditions fail. Bauerschmidt–Bodineau avoids absolute summability but yields a log-Sobolev inequality, not pointwise $\ell^\infty$ response or covariance bounds. The question decided in Section 8.15 lies outside all four. NOT_FOUND for a signed pointwise extension |

The sweep could not open, or saw only metadata for, the following. On demagnetizing factors and prisms: Joseph and Schlömann (1965), Aharoni (1998), Chen–Pardo–Sanchez, and Tsoulis and Petrović (2001). On surface and edge modes: Dobrzynski–Maradudin (1976) and Boardman et al. (1985). On edge and corner singularities: the Van Bladel chapter, a J. Elasticity multimaterial-wedge paper, and Mateu–Orobitg–Verdera (2009, abstract only). The full text of Menz–Nittka was also unavailable. Helsing and Perfekt (2013) and Costabel, Darrigrand and Sakly (2012) were opened but contain no uniaxial edge exponent.

*Strongest overlap objection.* In the continuum, Theorem DF is the classical statement that the $zz$ demagnetizing field of a uniformly polarized box is a sum of face solid angles. The edge logarithm of Theorem EL is also expected from the edge logarithms of the off-diagonal prism tensor. The objection is correct for the mechanisms, and they are attributed. The claimed additions are narrower. First, a uniform lattice bound on every S9 set, which the partial sets require. Second, the exact second-order constants at horizontal edges and corners. Third, the observation that the uniaxial edge exponent is second order in the contrast, so that the lattice logarithm appears only at order $\Omega^{-4}$. Fourth, the resulting decision on the signed-kernel input of the record problem. Whether these are significant is judged in Section 16 by an agent other than the generator.

### 15.11 Primary-source comparison in the v2.1 audit

Access was checked on 23–24 September 2026 (UTC/KST). A bibliographic record, publisher abstract, indexed first-page excerpt and full mathematical text are different evidence levels. The requested comparison is **INCOMPLETE**. No inability to retrieve a source is treated as evidence of absence or novelty.

| Source | Material actually accessible | Comparison that is justified; remaining debt |
|---|---|---|
| J. Van Bladel, *Singular Electromagnetic Fields and Sources*, Clarendon (1991); Wiley reprint (1996), chapter on edges | [Publisher record and contents](https://www.wiley.com/en-us/Singular+Electromagnetic+Fields+and+Sources-p-9780780360389). Publisher sample PDF did not open (HTTP 403) | Scope locator only. No equation-level claim about its anisotropic wedge formula or second-order exponent is justified. Obtain the edge chapter and its interface/anisotropy treatment |
| V. Mantič, F. París, J. Berger, “Singularities in 2D anisotropic potential problems in multi-material corners. Real variable approach,” *Int. J. Solids Struct.* 40 (2003), 5197–5218, [DOI](https://doi.org/10.1016/S0020-7683(03)00292-0) | Publisher abstract/introduction snippets and indexed first page. Publisher full text was blocked; the indexed PDF mirror timed out/returned 502; ResearchGate offers a full-text request rather than the paper | The abstract establishes prior use of transfer matrices for anisotropic scalar corner eigen-equations. Exact reduction to this manuscript's tensor and the coefficient $1/(8\pi^2)$ remain unverified against that original |
| J. Meixner, “The behavior of electromagnetic fields at edges,” *IEEE Trans. Antennas Propag.* 20(4) (1972), 442–446, [DOI](https://doi.org/10.1109/TAP.1972.1140243) | Citation record and abstract. IEEE document route returned robot verification; PDF routes returned HTTP 418 | Equation-level comparison is blocked. The same-title 1954 report and later lecture reproductions were not substituted for the 1972 article |
| A. Barroso, V. Mantič, F. París, “Singularity analysis of anisotropic multimaterial corners,” *Int. J. Fracture* 119 (2003), 1–23, [DOI](https://doi.org/10.1023/A:1023937819943) | [Author-uploaded full text](https://www.researchgate.net/publication/227175950_Singularity_analysis_of_anisotropic_multimaterial_corners), especially Section 3, Eqs. (24)–(29), and Section 8 | The text composes sector transfer matrices and imposes a closed-corner characteristic determinant. It treats elasticity. This confirms prior continuum methodology, not the scalar paper's exact formula, a finite dipole-lattice theorem or excitation by S9 |

The requested scalar mapping, still to be performed against the unavailable originals, is explicit: exterior isotropic coefficient $I$, interior coefficient $\operatorname{diag}(1,\varepsilon)$, interior angle $\pi/2$, continuity of potential and normal flux, and the second root near $\nu=1$. The comparison must track tensor orientation, the potential-versus-field exponent, coordinate stretch, admissible energy and the distinction between an available local mode and a mode excited by a prescribed boundary/source field.

The audit independently rebuilt the two-sector algebra. With $a=\tfrac12\log\varepsilon$, $R(\theta)=\begin{pmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{pmatrix}$, $D_1=\operatorname{diag}(e^{a\nu},e^{a(\nu-1)})$ and $D_0=\operatorname{diag}(1,e^a)$, the potential/angular-derivative matching determinant is
$$
\det\left[R(3\pi\nu/2)D_1^{-1}R(\pi\nu/2)-D_0\right]
=e^{a(1-\nu)}\left[2\cosh(a\nu)+(\cosh a-1)\cos\pi\nu-(\cosh a+1)\cos2\pi\nu\right].
$$
The bracket is the inherited $F(\nu,\varepsilon)/\varepsilon^{(\nu+1)/2}$. Expansion of the two-by-two determinant gives the identity; a separate 60-digit evaluation at nine points agreed within $1.9\times10^{-60}$. This checks the manuscript's algebra. It cannot replace original-text comparison or prove that the formula is new.

Novelty treatment for the v2.1 additions is conservative: SRX is a SPECIALIZED Schur-complement identity; WO and RD-V specialize elementary interval and variance inequalities; COMP-SQRTLOG is a new internal consequence of the retained estimates, with external significance/novelty not adjudicated. A comparator-only improvement and a repaired implication do not satisfy either user-defined grade-4 alternative.

### 15.12 Prior-art collision for the v2.2 additions

A search on 24 September 2026 covered log-Sobolev semiboundedness and ground-state localization for non-convex potentials, quantum-Darwinism record theorems in oscillator environments, convergence theory for the discrete dipole approximation, and volume-integral operators on polyhedra. The closest items located, and their relation to the new claims, are listed below. The search was not exhaustive, and NOT_FOUND is not evidence of absence.

| Ingredient or claim | Closest located prior work | Classification |
|---|---|---|
| Log-Sobolev semiboundedness and the Herbst bound in Lemmas LOC-B, LOC-B$_Y$ | Federbush; Gross [Gro75]; Bakry–Émery [BGL14] | IMPORTED tools |
| Growing-threshold convex comparator with core control and $L^2$-refined site-resolved covariances | No located source gives this combination for a non-convex Coulomb ground state. Weak-semiconvexity and log-Sobolev results for Schrödinger potentials (e.g. arXiv:2301.00083) concern different objects | SPECIALIZED construction from standard tools; external novelty not adjudicated |
| Theorem NP-SQRTLOG (records at $\sqrt{\log R}$ confinement in the full model) | Quantum-Darwinism studies of oscillator environments (Blume-Kohout and Zurek, quantum Brownian motion, arXiv:0704.3615; surveys by Zurek) give model calculations. None located proves an all-$R$ confinement law for a non-convex interacting environment. The method-level comparisons with covariance and log-Sobolev criteria (Menz, Otto–Reznikoff, Bauerschmidt–Bodineau, Henheik–Teufel–Wessel, Sjöstrand, Bach–Møller, AKKR) are those of Sections 15.7–15.10, with their theorem locators and the hypotheses that fail for S9 | Author's classification: OPEN-NOVELTY (conservative); the closest comparison is internal (NP-LOG, COMP-SQRTLOG). The separate assessor of Section 16.0 reclassified the central theorem as NOVELTY PASS (bounded). The qualification in Section 16.0 follows the assessor, and the difference is recorded here rather than resolved by the author |
| Lemma CR-1 and Theorem CR (discrete-dipole lattice to volume integral equation, weak limit) | Yurkin, Maltsev and Hoekstra 2006 (DDA convergence under smooth-field assumptions); Costabel, Darrigrand and Sakly, C. R. Math. 350 (2012) 193–197 (essential spectrum of the volume integral operator for smooth interfaces); Schlömerkemper, Arch. Ration. Mech. Anal. 176 (2005) 227–269, and Schlömerkemper and Schmidt, Arch. Ration. Mech. Anal. 192 (2009) 589–611 (rigorous discrete-to-continuum limits of dipolar lattice sums on Bravais lattices, with local surface terms from short-range effects under regularity assumptions) | Standard compactness method (SPECIALIZED). Theorem CR uses only interior test functions, so no surface term arises; its use to remove the S9 source-transfer step is internal |
| Hypothesis EG-C and Remark CR-H | Edge-singularity theory of dielectric wedges (Meixner; Van Bladel; Mantič–París–Berger for anisotropic corners; Nicaise–Sändig). None located states nonvanishing of the excited coefficient for a uniaxial cube | OPEN |

Re-attempt of the named sources, 24 September 2026:

- Mantič–París–Berger 2003: publisher page only (ScienceDirect abstract).
- Meixner 1972: no open full text found.
- Van Bladel: not retried beyond the v2.1 record.

The equation-level comparison therefore remains incomplete. It bears on Proposition W and EG-C, not on Theorems NP-SQRTLOG or CR.

## 16. Research-grade and qualification card

The governing criteria are those of Mission 1.7 (§1.4, §5.6) and ACTIVE ZSPIN-RULES-2 minor 2.4. A target, a candidate and an achieved grade are distinct. The generating agent does not adjudicate its own output.

### 16.0 v2.2 status: separate assessor card (retained unchanged; the current status after the frozen v2.2 audit is Section 16.0S)

| Field | Assessment |
|---|---|
| TARGET / VERSION / HASH | Target grade 4. This is an ambition, not evidence. Assessed `ZS-M73_v2_2.md` with §16.0 PENDING, SHA-256 `6598625e…8677f37c`; `v22/npsqrt.py` `bed67d7a…385377cf`; `v22/checks.py` `3b72451e…e3c37c`. Filling this section changes the manuscript hash |
| CENTRAL CONTRIBUTION | Theorem NP-SQRTLOG (§8.17.5): for the exact non-convex Coulomb Hamiltonian with S9 and P1, and $\Omega_R=10^4\sqrt{1+\log\lceil R^{1/3}\rceil}$, $D_j(t)\ge.98853$ for every $R\ge2$, every memory and every $t\in I_R$. Supporting: Theorem CR and Corollary CR-R (§8.18). Hypothesis EG-C is open |
| CLOSEST PRIOR RESULT / EXACT LOCATOR | Internal: NP-LOG §8.14.6 (log law, same model, preparation, window and observable); COMP-SQRTLOG §8.16.5 (comparator only); the v2.1 obstruction (8.LOC1) and §13.12 task 2; Theorem Q/Q-prime ($\sqrt{\log}$, quadratic model). External, by method (§§15.7–15.12): Menz Prop. 3.3, Otto–Reznikoff Thm 1, Bauerschmidt–Bodineau Thm 1, Henheik–Teufel–Wessel Thm 3, Sjöstrand 1993 Thm 6.2, Bach–Møller, AKKR. Physics: Blume-Kohout–Zurek. For CR: Yurkin et al. 2006 |
| NEW RESULT / ASSUMPTIONS / PROOF LOCATOR | (8.SQ0)–(8.SQ3); L-hat$_Y$, LOC-A$_Y$, LOC-B$_Y$, SQ-L2; `npsqrt.py`; rows V22-SQ-*. Assumptions: those of §2, a declared P1 and fixed $c$. The Euclidean limits of Lemma SR are cited, not reproved. CR concerns the quadratic model on full cubes at fixed $w>8g$ |
| SUBSTANTIVE DIFFERENCE / WHY IT MATTERS | Everything is held fixed except the sufficient law, which drops from $\log R$ to $\sqrt{\log R}$. The full model now matches the quadratic model's law, so non-convexity and Coulomb cores are not the bottleneck. On this route the residual $\sqrt{\log}$ comes from the absolute dipolar row sum, a linear-response quantity. CR turns any continuum edge-unboundedness result into a lattice record no-go for the actual source row |
| CORRECTNESS: PASS | I re-derived the following: the Hermite bounds ($D_2$, $f'_{\max}<193.58$); the near/far counting and cube comparison of LOC-A$_Y$; the $C_h$ identity (remainder $Y_1^2/(4U(Y_1+Y_2U))$); the $\zeta$ correction; the event split and Minkowski step of SQ-L2; the multiplier $4\pi(\xi_z^2/\lvert\xi\rvert^2-\tfrac13)$, from $\partial_z^2(1/r)={\rm PV}-\tfrac{4\pi}3\delta$; and the weak-limit identification and contradiction in CR. I also re-implemented the LOC-B$_Y$ energy and $\theta$ chain from the text alone. It gives $\widehat g_0r_0^2/\ell\ge22.2$ and $\log_{10}(2T\delta_3)/\ell=-5.860654035$ at $\ell=10^9$, the same as the code. I found no S2+ defect. The margin above $.9885$ is $3.9\times10^{-5}$ |
| NOVELTY: PASS (bounded) | §15.12 labels NP-SQRTLOG OPEN-NOVELTY. I reclassify it. The cumulative sweep maps the general external lines with theorem locators and records why each fails for S9: finite range or decaying bond norms, absolute summability with $\alpha>0$, classical or thermal settings, dimension restrictions. My three queries found nothing closer: non-convex correlation decay, quantum-Darwinism record scaling and quantum anharmonic crystals. The v2.2 delta over NP-LOG adds proof and construction; it is not a substitution. The tools are IMPORTED and the construction is SPECIALIZED. CR is SPECIALIZED. Its uncited neighbours are discrete-to-continuum dipolar lattice sums (Schlömerkemper, ARMA 2005; Schlömerkemper–Schmidt, ARMA 2009) |
| SIGNIFICANCE: PASS (narrow) | NP-SQRTLOG resolves the open sub-log question for the full model and refutes the bottleneck v2.1 had designated. It discharges §13.12 task 2 and closes the full-versus-quadratic gap. CR removes the lattice source-transfer obligation. The meaning is internal to the model; no external reuse is demonstrated |
| VERIFICATION BASIS: PASS | An outward interval covering (7077 subintervals) with an analytic tail. The referee re-implementation matched to 12 digits at six values of $\ell$. My delta rerun gave 14/14 PASS (`V22-DELTA-14`). The fault injections behave as stated. COINC: the stored FAIL (in-region $2.77\times10^{-12}$ against $10^{-12}$, which is below the $10^{-11}$ quadrature tolerances) is a tolerance artifact. The corrected code passes on identical seeded data. S1 release condition: the stored JSON is stale (88/89, profile `-88` against driver `-89`), so rerun the full profile and fill §12.8. S0: §8.17.1 quotes $4.5\times10^{-11}$ out-region, while the rows give $\le2.1\times10^{-11}$ |
| TARGET / RESEARCH / CANDIDATE GRADE | 4 / **3** / 4 |
| GRADE 4–5 ADDITIONAL EVIDENCE | User criterion: (ii) is MET literally. (i) is NOT MET, because EG-C is open and CR is one-way. Mission criteria: the locator and before/after comparison are MET. The changed judgement is PARTLY met: the full model reaches the quadratic law, but fixed confinement stays open in both directions, the Gaussian preparation is unchanged, and the gain is a $\sqrt{\log R}$ factor in a sufficient condition. Adversarial review is MET within the same model family. That the prior limit is internal matters little, because the problem is project-defined. What matters more is that the frozen audit (F31-01) showed the log barrier to be an artifact of a fixed design parameter, removed by a standard growing-cutoff device. Under §1.4, grade 4 is **NOT ESTABLISHED**; it is a candidate. Whether the user's bar overrides §1.4 is a decision for the user |
| EXTERNAL REVIEW / human anchor | NONE / NONE. Not used as a reason for any rating |
| VERIFICATION METHODS / COVERED CLAIMS / LIMITATIONS | As above; covers NP-SQRTLOG and CR. Inherited chain rests on prior audits; EG-C untested |
| PAPER QUALIFICATION | **PASS**. All four axes pass |
| OUTPUT FORM | **RESEARCH PAPER**, subject to the S1 rerun |
| MISSION ROLE / FQ-RQ / BEFORE-AFTER | SUPPORT + METHOD; FQ2/RQ3. No bridge changes, so not CORE (§1.4.4) |
| STRONGEST OBJECTION / RESIDUAL UNCERTAINTY | See below. The margin is thin and P1 is declared |
| EVIDENCE NEEDED FOR PROMOTION / REVERSAL TRIGGER | See below |

**Strongest objection.** v2.2 removes a limitation that the project's own earlier proof created, using a standard device. The result is a $\sqrt{\log R}$ sufficient law in a model the project defined, with a declared preparation. It brings the full model only up to the law already known for the quadratic model. It leaves the real question, fixed confinement in either direction, as open as before. A stricter reading of "field-level meaning", the one the v1.9 card applied, would make Significance HOLD, and the result would then be a RESEARCH NOTE. I depart from that reading because §1.4.2 counts discharged proof obligations and changed judgements, and v2.2 supplies both concretely. Evidence for promotion to grade 4: a proof of EG-C, which with CR gives a fixed-confinement no-go; a law below $\sqrt{\log R}$ for the full model; or the growing-threshold localization stated generally and applied to an externally studied model. Evidence for reversal: a counterexample to LOC-A$_Y$ or SQ-L2; a text–code mismatch or inherited constant that consumes the $3.9\times10^{-5}$ margin; a prior theorem that covers the result; or a failure in the regenerated full verification.

**Independence disclosure.** I am the same model family (Claude) as the v2.2 author and the Appendix R referee, in a separate context, and did not write the work. I had the manuscript, the referee summary, the verification JSON and code, and the Mission excerpt. No ratings were negotiated with the author. The grade-4 target was known to me and was not used as evidence.

*Author's release note (does not change any rating).* The S1 release condition has been discharged: the full profile was rerun after the tolerance correction, and the census is in Section 12.8. The S0 item (the out-region difference quoted in Section 8.17.1) is corrected. The two uncited discrete-to-continuum references named by the assessor are added in Section 15.12. The assessed hash in the table above refers to the pre-card draft. The released manuscript hash is recorded in `release_manifest_v2_2.json`.

*v2.2.1 note (F32-05).* The card's margin $3.9\times10^{-5}$ is measured from $.9885$. Measured from the stated constant $.98853$ of Theorem NP-SQRTLOG, the certified margin is at least $9.06\times10^{-6}$ (row `V221-SQ-CERT-98853`, Section 8.17.5). A reversal trigger that "consumes the margin" therefore refers to $9.06\times10^{-6}$ for the stated constant. The card's text above is unchanged.

### 16.0S Current v2.2.1 status: the frozen v2.2 audit

The v2.2 release was audited by Codex/GPT: cross-family, since the v2.2 proofs were generated by Claude, but not blind, and earlier M73 versions contain GPT-lineage contributions. The audit event is `AUDIT-M73-v22-20260924` (2026-09-24 08:06:52 UTC). The auditor re-evaluated the whole integrated paper, not only the v2.1→v2.2 increment. Its card is recorded here as frozen. v2.2.1 only applies its minor corrections, and the author does not adjudicate between the two cards.

| Field | Frozen audit of v2.2 |
|---|---|
| AUDIT / TERMINAL | AUDIT-PASS-MINOR; highest severity S1 (F32-01…04; F32-05 is S0); TERMINAL-IN-SCOPE recommended |
| CENTRAL CONTRIBUTION | Theorem NP-SQRTLOG for the exact S9/P1 model, including its globally non-convex regime; the cumulative construction is Sections 8.14–8.17 |
| RESEARCH GRADE | **4**, a project-internal mathematical and method contribution, assessed on the cumulative contribution |
| CANDIDATE GRADE | NONE (no grade-5 candidacy) |
| CORRECTNESS | PASS. The central proof chain and the strengthened numerical budget were checked; no open S2+ defect |
| NOVELTY | PASS, bounded. Awarded not for the tools but for the exact-model record theorem, which required additional proof. The novelty of Proposition W is not promoted |
| SIGNIFICANCE | PASS. The same universal record contract is realized beyond the barrier of the globally convex route; the confinement changes from polynomial (NP-P1, $R^{1/6}$) to $\sqrt{\log R}$, a ratio growing like $\sqrt{n/(1+\log n)}$ |
| VERIFICATION BASIS | PASS. Cross-family review; source comparison (Menz arXiv:1402.5160 Thm 2.3; Menz arXiv:1309.0862; Henheik–Teufel–Wessel arXiv:2106.13780 Thm 3; Blume-Kohout–Zurek arXiv:0704.3615; Yurkin–Maltsev–Hoekstra arXiv:0704.0033); unmodified 89/89 rerun; seven additional deterministic checks and fault attacks |
| PAPER QUALIFICATION / FORM | PASS / RESEARCH PAPER (internal) |
| MISSION ROLE | SUPPORT + METHOD, FQ2/RQ3; no CORE or observational promotion |
| DIFFERENCE FROM SECTION 16.0 | The card of Section 16.0 assessed the increment and gave 3. The audit assessed the cumulative contribution and gave 4, and it states that an increment-only 3 is also defensible. Both records are preserved |
| EXTERNAL REVIEW / HUMAN | None / qualified-human anchor NONE |
| STRONGEST OBJECTION | A careful combination of standard tools in a project-defined model, which settles neither a physical device nor fixed confinement. The auditor holds that this blocks grade 5, physical CORE and any universal record principle, but not the grade-4 basis |
| REOPEN TRIGGERS | A counterexample to LOC-A$_Y$ or SQ-L2; a violated assumption in the transfer of the Euclidean limit of Lemma SR; a constant error that breaks the $.98853$ budget; a closer prior theorem that contains the central result without additional proof; a mismatch between frozen files and certificates |
| OPEN, outside scope | EG-C; a fixed-confinement theorem or an unconditional no-go; laws below $\sqrt{\log R}$ and optimal rates; the same law for the Gaussian preparation; derivation of carriers, devices, preparation and clock; the equation-level comparison for Proposition W |

**Re-audit status of v2.2.1.** Its five corrections are listed in Appendix S. Under the audit rule for re-audits, the wording changes (F32-03, F32-04, F32-05) are delta items, while the new verification rows (F32-01, F32-02) change code, for which a targeted re-audit is the appropriate check. No re-audit has been run; v2.2.1 is not itself audited.

### 16.0a The v2.1 card (historical; superseded by 16.0)

| Axis | Frozen v2.0 | Integrated v2.1 |
|---|---|---|
| Correctness | MAJOR REVISION, S2: invalid fixed-time implication, nonuniform asymptotic inference and an omitted growing TC term | Those implications are corrected. SRX, WO, RD-V and COMP-SQRTLOG have proofs and computational checks. New material has author self-review only |
| Novelty | HOLD; requested closest original texts had not been read | HOLD; related original upgraded, named-source equation comparison still incomplete. Standard tools retain attribution |
| Significance | No proof of either user-defined grade-4 alternative | Partial internal advance: comparator square-root-log theorem and repaired conditional obstruction. No full-model improvement beyond NP-LOG |
| Verification basis | 60 manifest entries match; original 67 rows rerun PASS in a disclosed different environment | New finite, exact-arithmetic and interval checks accompany proofs; no executable row proves asymptotic transfer or novelty |
| Research grade | Grade 4 NOT ESTABLISHED; original achieved grade was UNASSESSED | Grade 4 NOT ESTABLISHED; achieved grade UNASSESSED. Inherited candidate 3 remains a candidate only |
| Paper qualification / form | HOLD | HOLD / RESEARCH NOTE |
| Mission | SUPPORT + METHOD, FQ2/RQ3 | Unchanged; no CORE or physical bridge promotion |

The audit of v2.0 is performed by a different model family from its disclosed generator, but the earlier reports were visible. It is not described as a blind independent review. No subagents were used for v2.1. Its author does not give the new contribution an independent grade. Absence of a human review is not the reason for withholding grade 4: the specified mathematical alternatives and source comparison remain incomplete.

This status does not retract NP-LOG or every inherited theorem. It narrows the corrected implications and reports the exact new result in its comparator scope. A future grade claim requires the missing mathematics and source evidence, not additional verification rows or a renamed output.


### 16.1 The v2.0 card (historical; superseded for current correctness)

The historical card below was produced in the v2.0 session by a separate agent instance with no generation context. Its provisional correctness PASS and highest-S1 findings are superseded by the frozen v2.0 audit in Appendix Q; its wording is retained as a record of the earlier assessment. That instance had four inputs: the draft manuscript, the two referee reports on Section 8.15, the novelty sweep and the frozen route card. It reproduced the decision-critical constants and asymptotics with its own scripts. It was told that the requested target was grade 4, and that this target must not influence its judgement in either direction. The referee, the novelty sweep and the assessor are three separate instances of the same model family.

The generator did not ask for any rating to be reconsidered. The card is reproduced verbatim. It refers to the draft, in which the verifier gate `ENGLISH-MATH-INTEGRITY` failed and the census placeholder of Section 12.6 was unfilled (finding A6). After the assessment, the generator repaired findings A1–A6 by narrowing or relabelling claims (Appendix P.5). The released verifier run passes all 67 rows. The card was not re-issued after these repairs. The repairs do not add any result, so they cannot raise a rating.

```text
RESEARCH-GRADE CARD — ZS-M73 v2.0, central contribution (separate-agent assessment)
TARGET / VERSION: Requested target is grade 4 (ambition only, not used as evidence). Assessed: the ZS-M73 v2.0
  draft, Section 8.15 and its integration (release table, abstract, Section 1.3, Section 13.12, Section 15.10,
  Section 17, Appendix P).
CENTRAL CONTRIBUTION: An order-by-order decision on the n-uniform signed l-infinity input that a signed-kernel
  Lemma SR would need.
  - Theorem DF: -7.905 <= sum_a K_aj <= 15.663 on every S9 set; for the source row, |(K_m v)_j| <= 24.28|v_j|.
  - Theorem EL: (K^2 1)_j = 2 log n + O(1) at horizontal mid-edges and (3/2) log n + O(1) at corners of full cubes.
  - Supporting results: Lemma SRC (transfer to the source row), Proposition W (uniaxial right-angle wedge,
    gamma = delta^2/(8 pi^2) - delta^3/(8 pi^2) + O(delta^4)), Corollary Q-prime and Proposition LN (quadratic model).
  - Hypothesis EG: a conjecture, not proved.
CLOSEST PRIOR RESULT / LOCATOR:
  Internal:
  - v1.9 Sections 8.14.7 and 13.11: the signed-kernel Lemma SR is named as the way to remove S2-hat ~ log n;
    the question is left OPEN.
  - v1.9 remark after Lemma 4.3: signed row sums "<= 2.92", numerical only, full cubes with n <= 16; false on
    partial sets (F29-01).
  - Theorem Q, (13.2): absolute-row-sum polarization bound; R <= 10^1800 at Omega_0^2 = 8e8.
  External:
  - Continuum prism and polyhedron tensors: Newell–Williams–Dunlop 1993; Smith et al. 2010, Eqs. A8/A12;
    Ren et al. 2018, App. B. The zz component is a sum of face solid angles; off-diagonal components carry edge logs.
  - Meixner edge-singularity theory; anisotropic multi-material corners (Mantic–Paris–Berger 2003;
    Nicaise–Sandig). The sources most likely to hold the uniaxial formula were not opened.
  - Context: Otto–Reznikoff 2007 Thm 1; Menz 2014 Thm 1.7; Bauerschmidt–Bodineau 2019 Thm 1.
NEW RESULT / PROOF LOCATOR:
  - Section 8.15.1: (8.DF1)–(8.DF3).
  - Section 8.15.2: Lemmas EL-1 and EL-2, Theorem EL, and the corner proof.
  - Section 8.15.3: (8.W1)–(8.W2).
  - Section 8.15.4: (8.Qp), Lemma SRC, Proposition LN, Hypothesis EG.
  - Code rows DF-CONSTANTS … QPRIME-FINITE in m73_v20_checks.py.
  - Assumptions: the kernel (2.4); lexicographic filling with the e_z index fastest; Theorem EL for full cubes only.
    Theorem EL, Lemma SRC and Proposition LN have non-explicit constants.
SUBSTANTIVE DIFFERENCE:
  - BEFORE (v1.9): it was hypothesized that the signed kernel is bounded, so a signed Lemma SR might remove log n.
  - AFTER, first order: true, uniformly on every S9 set, with certified constants.
  - AFTER, second order: false. The second Neumann iterate carries an exact geometric log at horizontal
    edges and corners. So any n-uniform pointwise bound must be non-perturbative in Omega^-2.
  - Quadratic model: the log moves to the Neumann radius. This is the same O(sqrt(log R)) law already implied by
    Theorem Q; the constant improves (range 10^1800 -> 10^(2e7) at Omega_0^2 = 8e8). The Omega_0^-4 Taylor
    coefficient of the exact source coefficient is 2 log n + O(1) at horizontal mid-edges of full cubes.
  - Unchanged: Theorem NP-LOG, the full-model fixed-confinement question, and every proved lower bound (there is none).
CORRECTNESS: PASS (provisional).
  - Two hostile referee passes found no error in the numbered results after repair.
  - My independent checks:
    - E_* ~ 2.574 <= 2.7104, and the sums 15.662 / -7.904.
    - Theorem DF on random partial S9 sets up to n=32: values in [-2.95, 3.06].
    - The Theorem EL table reproduced by FFT (n = 16..96). Mid-edge and corner remainders converge like 1/n.
    - The angular constants 2 and 1.5000000 by quadrature.
    - Proposition W rebuilt from the interface conditions: the determinant equals nu^2 eps^-1/2 F; F(1,eps) = 0;
      the delta^3 term and the gamma table confirmed.
    - Corollary Q-prime proof checked, and the bound holds against exact rho_pol on 7 geometries.
    - The coefficient identity of Proposition LN(ii) and the arithmetic of LN(i) checked; lambda_min(K) ~ -5.35,
      so Omega^2 = 6 in the EG data is stable.
    - Two EG lattice exponents reproduced.
  - Hypothesis EG is labelled unproved throughout. No numbered result depends on it.
  - Open findings are at most S1 (see below). One of them attributes an unproved claim to Theorem EL.
NOVELTY: HOLD.
  - Theorem DF: the continuum fact is IMPORTED; the lattice form is thin EXTENDED, arguably SPECIALIZED.
  - Theorem EL: the mechanism is known (edge singularities, expansion of a power law in the contrast). The lattice
    statement with constants 2 and 3/2 is OPEN-NOVELTY; the constant 2 is fixed by the continuum exponent.
  - Proposition W: the method is standard; the expansion is minor OPEN-NOVELTY, and the literature search for it
    was thin (Van Bladel, Mantic et al. and Meixner 1972 were not opened).
  - Corollary Q-prime, Lemma SRC and Proposition LN: SPECIALIZED.
  - The core result is OPEN-NOVELTY, which the rules map to HOLD. No subsumption was found, so not FAIL.
SIGNIFICANCE: HOLD.
  - What is decided: a non-trivial internal question, at the perturbative level. The v1.9 BEFORE hypothesis is
    refuted beyond first order, and one route to fixed confinement is shown to be limited.
  - What does not change: the target-level judgement. Fixed-confinement failure rests on EG plus an unproved
    transfer to the source row at fixed Omega.
  - The quadratic-model gain is a constant, not a change of law.
  - No external reuse or meaning outside the project is demonstrated.
VERIFICATION BASIS: PASS (minimal).
  - Present: an adversarial two-pass review with its own scripts; a bounded source sweep with independent
    recomputation; deterministic verifier rows with 8 fault injections; this assessor's reproductions.
  - Limits: independence is within the same model family only. The current run log shows 66 PASS / 1 FAIL; the
    failing gate is cosmetic (see A6).
TARGET GRADE: 4
RESEARCH GRADE: UNASSESSED.
  - The central Theorem EL is correct (provisionally) and is more than a routine application: no positive evidence
    of routineness, so grade 2 is not supported.
  - Novelty (OPEN, with the likely subsuming continuum sources unread) and meaning beyond a model-internal,
    perturbative route decision are not established, so grade 3 is not confirmed.
GRADE 4-5 ADDITIONAL EVIDENCE:
  (i) Partly met. Locators of the prior limitation are exact (v1.9 Sections 8.14.7/13.11, Lemma 4.3 remark,
      Theorem Q (13.2)), and the before/after comparison is explicit. But the limitation is internal and is not
      overcome; it is only characterized perturbatively.
  (ii) Not met at the target level. What can now be judged: pointwise n-uniform bounds must be non-perturbative;
      the log in (13.2) is an absolute-value artifact at order Omega^-2 but not at Omega^-4.
      What still cannot be judged: whether fixed confinement holds or fails in either model.
  (iii) Partly met. The referee passes covered counterexamples. The duplication review is thin exactly where
      subsumption is most likely (the anisotropic-wedge and edge-singularity sources).
      Alternative explanation for EG: over n = 32..192 the exponents are 0.004–0.045, so n^gamma growth and slow
      saturation are only weakly separated; the monotone rise of the local exponents is the only discriminant.
CANDIDATE GRADE: 3. Missing evidence:
  (a) Full-text checks of Van Bladel 1991 (edge chapter), Mantic–Paris–Berger 2003, Meixner 1972 and the
      literature on Neumann–Poincare expansions on polyhedra, showing that the uniaxial second-order exponent
      and the second-order edge log are not already stated.
  (b) Demonstrated meaning beyond the project. Examples: a proof of EG, or reuse of the DF/EL lattice estimates
      in an external problem (DDA edge error, local fields of dipolar lattices).
GRADE 4 STATUS: NOT ESTABLISHED, and not a current candidate. It would require one of the following, each with
  a before/after comparison against Theorem Q / NP-LOG:
  - a proof of EG together with the source-row transfer and a readout argument, giving a proved failure of fixed
    confinement and a matching (log R)^(1/4) law in the quadratic model; or
  - a fixed or sub-logarithmic confinement theorem for the full model.
EXTERNAL REVIEW / qualified-human anchor: NONE. All reviewers are same-family separate instances (disclosure only;
  not a blocking condition and not a reason for any rating here).
PAPER QUALIFICATION: HOLD (Novelty, Significance). No axis FAILs.
OUTPUT FORM: The integrated research manuscript is retained. The v2.0 addition is at research-note / support-lemma
  level (HOLD). The signed-kernel theorems are suitable as a proved obstruction-to-a-route supplement, not as a
  target result.
MISSION ROLE: SUPPORT + METHOD (FQ2/RQ3). No FQ/RQ bridge state changes; CORE is not supported. This matches
  the manuscript's own declaration.
STRONGEST OBJECTION: The proved content is perturbative and model-internal.
  - Theorem DF is the lattice version of the classical face-solid-angle fact.
  - Theorem EL's log is the expected second-order trace of a known edge-singularity mechanism, with its constant
    dictated by the continuum.
  - The quadratic-model consequences are a constant improvement (same O(sqrt(log R)) law as Theorem Q) and a
    statement about Taylor coefficients.
  - The only statement that would move the target (EG, and EG => record failure) is unproved. The re-typing of
    the target (Section 13.12) is motivated by that unproved hypothesis.
REVERSAL TRIGGERS:
  Toward promotion:
  - a proof of EG with the source-row transfer and the readout-lobe step;
  - full-text confirmation that the uniaxial exponent expansion and the lattice edge log are absent from the
    edge-singularity literature;
  - external reuse.
  Toward demotion:
  - the uniaxial right-angle expansion or a second-order edge log found in prior literature (EL and W become
    SPECIALIZED/IMPORTED);
  - a counterexample to (8.DF2) on some S9 set;
  - a non-local, non-slow term in the (8.EL2) representation;
  - saturation of the edge local-field factor at larger n (this refutes EG and reverses the re-typing, but not
    DF or EL).
WHOLE-MANUSCRIPT NOTE: v2.0 does not change the v1.9 assessment.
  - Theorem NP-LOG is unchanged (Theorem EL(3) keeps the edge term at or below 1.7e-14).
  - The manuscript as a whole stays UNASSESSED / candidate 3 / Significance HOLD.
  - v2.0 does not supply the evidence the v1.9 card named as missing: external significance or reuse, a general
    SR / LOC-B, or fixed confinement.
  - It sharpens the open problem: one of the two logs cannot be removed perturbatively.
  - Grade 4 for the manuscript remains NOT ESTABLISHED.
```

The requested grade 4 was not achieved. Theorems DF and EL, Proposition W, Corollary Q-prime, Lemma SRC and Proposition LN are proved in their stated scope. Hypothesis EG is not proved.

The grade outcome is evidential, not a mathematical failure. The unmet evidence is named on the card:
- a full-text novelty check of the edge-singularity literature most likely to contain the uniaxial expansion;
- demonstrated meaning beyond a model-internal, perturbative route decision.

For grade 4, the card further requires a proved change at the level of the target, for example a proof of Hypothesis EG with its transfer to the source row, or a fixed or sub-logarithmic confinement theorem for the full model. The absence of human review played no part in any rating.

### 16.2 The v1.9 card (historical)

The v1.9 card below was produced by a separate agent instance with no generation context, after a hostile proof review of Section 8.14 and a bounded primary-source novelty sweep; the sweep was run by a third instance. All three are the same model family.

In a first pass the assessor gave research grade 2 together with a Novelty HOLD. The generator pointed out that grade 2 requires positive evidence of routineness. The assessor then withdrew that grade as a rule error; it did not raise any rating because of the request. The generator's intervention is disclosed here.

```text
RESEARCH-GRADE CARD — ZS-M73 v1.9, central contribution (separate-agent assessment)
TARGET / VERSION: target grade 4 (Section 13.11); assessed v1.9 Section 8.14
CENTRAL CONTRIBUTION: Theorem NP-LOG — D_j(t) >= .9885 for every R>=2, memory and t in I_R,
  exact non-convex S9 Hamiltonian, P1 preparation, Omega_R = 10^4(1+log ceil(R^(1/3)));
  Lemmas L-hat, LOC-A/B, SR, SC, PC, TC, RD
CLOSEST PRIOR RESULT / LOCATOR: internal — v1.7 Theorem NP-P1 (R^(1/6)) and Corollary NP-B(i);
  external mechanism — Menz 2014 Prop. 3.3 / Otto–Menz covariance estimate (classical),
  Helffer–Sjostrand representation; Federbush/Gross log-Sobolev semiboundedness, Herbst;
  locality theorems (Henheik–Teufel–Wessel Thm 3, De Roeck–Schutz Thm 3.2, Wang–Hazzard),
  whose hypotheses are excluded by Theorem O(1); quantum-crystal stabilization line (Kozitsky et al.)
NEW RESULT / PROOF LOCATOR: Section 8.14, (8.LG0)–(8.LG13); certificate m73_v19_log.py
SUBSTANTIVE DIFFERENCE: design law R^(1/6) -> log R without global convexity (potentials provably
  non-convex for large full cubes); three growing source-row residues removed; uniform gap of every
  exact branch; the R^(1/6) order shown to be an artifact of the proof method
CORRECTNESS: PASS (provisional) — one hostile re-derivation of every lemma with independent numerics,
  no S2+ remaining; Euclidean limits cited, inherited constants not re-derived; margin 4.2e-5
NOVELTY: PASS (bounded) — closest classical results read in full text are classical-only; the strongest
  quantum line (thermal, bilinear ferromagnetic summable couplings) cannot cover S9 on its stated
  hypotheses; no record-resource law found. Lemma SR classified EXTENDED. Residual lemma-level risk:
  AKKR 2009 monograph, arXiv:0710.2303 §4.4–4.5, Minlos–Verbeure–Zagrebnov, Hel02
SIGNIFICANCE: HOLD — a non-trivial question solved with an internal limit crossed, but meaning for the
  wider field, an external question answered, or reuse outside the project is not demonstrated
VERIFICATION BASIS: PASS (minimal) — adversarial review, deterministic reruns, bounded source comparison,
  fault controls; same-family independence only
TARGET GRADE: 4
RESEARCH GRADE: UNASSESSED (evidence shows more than routine work, not field-level meaning)
GRADE 4-5 ADDITIONAL EVIDENCE: not met — (i) the limitation overcome is internal; published LPPL theorems
  are sidestepped for one model, not overcome generally; (ii) the proved change is model-specific;
  (iii) duplication review partial
CANDIDATE GRADE: 3 — missing: demonstrated external significance or reuse (e.g. SR/LOC-B stated generally
  and applied to a second model), and the remaining lemma-level source checks
GRADE 4 STATUS: NOT ESTABLISHED and not a current candidate; would require fixed confinement, or the
  Gaussian preparation, or a general signed-kernel SR plus flip-local LOC-B beyond S9, each with a
  before/after comparison
EXTERNAL REVIEW / qualified-human anchor: NONE (same-family separate instances; disclosure only)
PAPER QUALIFICATION: HOLD (Significance)
OUTPUT FORM: integrated research manuscript retained as RESEARCH NOTE-level qualification (HOLD)
MISSION ROLE: SUPPORT + METHOD; no FQ/RQ bridge state changes
STRONGEST OBJECTION: every tool is known and the model is project-defined; thin margin; one reviewer
REVERSAL TRIGGERS: counterexample to (8.LG6) or (8.LG8); an inherited constant consuming the margin;
  a prior quantum ground-state covariance theorem covering SR
HISTORY: v1.8 card — grade-4 achievement NOT ESTABLISHED; new v1.8 artifact UNASSESSED; HOLD
```

The requested grade 4 was not achieved. Proving the central theorem is a mathematical outcome. The HOLD and the ungraded status are evidential. Neither is caused by the absence of human review or publication, which the Mission does not require. The concrete missing evidence is listed on the card and in Section 13.11.

## 17. Conclusion

For the exact non-convex Coulomb model with the switched-off ground-state preparation, confinement growing like $\sqrt{\log R}$ now suffices for every memory to record the source throughout the growing window, with readout at least $.98853$ (Theorem NP-SQRTLOG). Previously only a logarithmic law was proved. The obstacle that v2.1 had located in the full-model localization came from holding the comparison threshold fixed. A slowly growing threshold, core control and $L^2$-refined covariance majorants remove it, and an interval covering certifies the constants for every size. The remaining $\sqrt{\log}$ is the absolute dipolar row sum that any convex comparator must pay.

For the quadratic model the source-edge question has been moved off the lattice. Weak compactness shows that the lattice response to any smooth drive, including the actual source row, inherits any continuum edge unboundedness, and record failure at fixed confinement then follows. Whether the continuum polarization of the uniaxial cube is unbounded at its horizontal edges (Hypothesis EG-C) is not proved. A log-scale heuristic identifies the exponent and the one scalar condition a bounded solution would need.

Of the user's two grade-4 alternatives, the full-model sub-logarithmic theorem is proved, while EG together with source transfer is proved only up to the continuum statement EG-C. A separate assessor instance (Section 16.0) rates the achieved research grade as 3 and grade 4 as a candidate that is not established under Mission §1.4. It judges the paper qualification PASS. Whether the user's operational criterion, of which alternative (ii) is met literally, should override that reading is a decision left to the user. The mission role stays SUPPORT + METHOD, and no physical bridge is promoted.

*v2.2.1.* The frozen cross-family audit of v2.2 (Section 16.0S, Appendix S) found no S2+ defect. It rated the cumulative contribution research grade 4, restricted to a project-internal mathematical and method contribution, confirmed paper qualification PASS, and recommended TERMINAL-IN-SCOPE with the verdict AUDIT-PASS-MINOR. This release corrects its five minor findings without changing any theorem statement or constant. The stated constant $.98853$ is now certified with that gate, with a margin of at least $9.06\times10^{-6}$. The assessment of Section 16.0 (grade 3, on the increment) is retained, and the open problems are unchanged.

## Appendix A. The common-preparation echo lemma

Let $H_\pm$ have normalized ground states $\Omega_\pm$, ground energies $E_\pm$, and let the same normalized $\Phi$ have infidelities $\varepsilon_\pm$. Decompose its excited component with $Q_\pm=I-|\Omega_\pm\rangle\langle\Omega_\pm|$ and set

$$
u_\pm(t)=e^{iE_\pm t}e^{-itH_\pm}\Phi=\Phi+d_\pm(t),
\qquad d_\pm=(e^{-it(H_\pm-E_\pm)}-I)Q_\pm\Phi.
$$

Then $\|d_\pm\|\le2\sqrt{\varepsilon_\pm}$ and
$|\langle\Phi,d_\pm\rangle|\le2\varepsilon_\pm$, because only the excited component contributes to that inner product. Expanding $\langle u_-,u_+\rangle$ gives

$$
|\mathcal A(t)e^{i(E_+-E_-)t}-1|
\le2(\varepsilon_-+\varepsilon_+)+4\sqrt{\varepsilon_-\varepsilon_+}
\le8\max(\varepsilon_-,\varepsilon_+). \tag{A.1}
$$

The bound is uniform in time and compares the echo with the exact ground-energy phase. Its quadratic overlap order relies on the common vector and on retaining the linear inner-product estimates, not merely the vector norms. Because $\varepsilon_\pm$ is a global fidelity, this lemma is the source of the pin $3/5$ in Theorem N; a local echo statement (H4) would have to bypass it.

## Appendix A-prime. Distinct preparations and a sharp-order counterexample

For different $\Phi_\pm$, choose ground-state phases so that
$\Phi_\pm=a_\pm\widehat\Phi_\pm+r_\pm$, with
$a_\pm=\sqrt{1-\varepsilon_\pm}$ and $\|r_\pm\|=\sqrt{\varepsilon_\pm}$. Evolve the orthogonal residuals and extract $E_\pm$. Expanding the overlap bounds its difference from
$\langle\widehat\Phi_-,\widehat\Phi_+\rangle$ by

$$
(1-a_-a_+)+a_-\sqrt{\varepsilon_+}+a_+\sqrt{\varepsilon_-}
+\sqrt{\varepsilon_-\varepsilon_+}\le s+s^2,
\quad s=\sqrt{\varepsilon_-}+\sqrt{\varepsilon_+}. \tag{A.2}
$$

For the order obstruction, let $\widehat\Phi_-=\Phi_-=(1,0)$,
$\widehat\Phi_+=(1,1)/\sqrt2$, and
$\Phi_+=\cos\delta\,\widehat\Phi_++\sin\delta\,(1,-1)/\sqrt2$.
At $t=0$, the overlap difference is
$(\cos\delta+\sin\delta-1)/\sqrt2=O(\delta)$, while
$\varepsilon_+=\sin^2\delta=O(\delta^2)$ and $\varepsilon_-=0$.
For $\delta=.01$ the former is about $.0070356$ and the proposed old upper bound $2\sin^2\delta$ is about $.00019999$. Thus an $O(\varepsilon)$ bound fails even at zero time. The repaired $s+s^2$ bound accommodates both.

## Appendix B. Dipole matrix stability from positive field energy

Place disjoint uniformly polarized spheres of radius $a/2$ at sites separated by at least $a$. Give sphere $a$ signed dipole moment $p_ae_z$. Outside each sphere its field is exactly the point-dipole field, and its self-energy is $p_a^2/[2(a/2)^3]$. Positivity of the full field energy therefore gives

$$
\frac12p^TKp+\frac{4}{a^3}\sum_ap_a^2\ge0,
$$

hence $K\ge-8a^{-3}I$ for arbitrary real amplitudes, not only equal moments. Use a limiting radius below $a/2$ if spheres touch. For the three coordinate-axis kernels, $K_x+K_y+K_z=0$. Applying the lower bound to the other two axes gives $K_z\le16a^{-3}I$. This is the specific matrix application of the established positive-field-energy stability method; see the [BGW field-energy construction](https://arxiv.org/pdf/cond-mat/0012280).

## Appendix C. Harmonic comparison and the Riccati step

For $2H=-\Delta_x+2U$ with $\nabla^2U\ge\gamma^2I$, the modulus comparison uses the one-dimensional operator $-d^2/ds^2+\gamma^2s^2$ on a symmetric Dirichlet interval. The [Andrews–Clutterbuck comparison theorems](https://arxiv.org/pdf/1006.1686) justify this reduction and the passage through smooth convex domains.

Let $\varphi>0$ be the even one-dimensional ground state, with eigenvalue $E>\gamma$ on a finite interval. Define $r=-\varphi'/\varphi$ and $q=r'-\gamma$. The equation gives

$$
r'=r^2+E-\gamma^2s^2,\qquad q(0)=E-\gamma>0.
$$

If $q$ first reached zero at $s>0$, then $r(s)>\gamma s$ because $q>0$ before that point, while
$q'=2rr'-2\gamma^2s=2\gamma(r-\gamma s)>0$ at the crossing. This contradicts a first downward crossing. Hence $-(\log\varphi)''=r'\ge\gamma$. The weighted one-dimensional Poincare inequality for $\varphi^2$ gives gap at least $2\gamma$ for $2H$ and therefore at least $\gamma$ for $H$.

For a box, approximate from inside by smooth convex domains and use form-core/min–max convergence. For the whole-space confining potential, exhaust outward by bounded convex domains and use compact-resolvent convergence. With Theorem L the modulus is $\gamma^2=\Omega^2-h^{(L)}_N$.

## Appendix D. Mixed-difference sign derivation

For a single pair, the mixed Walsh coefficient is one quarter of the alternating sum of its four label values. The two single-coordinate terms and the constant in (2.2) cancel from that alternating sum. The surviving values are

$$
\phi(\lambda_b-\lambda_a)+\phi(\lambda_a-\lambda_b)
-\phi(-\lambda_b-\lambda_a)-\phi(\lambda_b+\lambda_a).
$$

This proves the positive $g/4$ prefactor in (4.5). Equivalently, integrating $-\phi''(v-u)$ over the symmetric rectangle produces that same bracket. Gaussian expectation commutes with the finite alternating sum, proving (4.7) with exactly the same sign. The verifier checks both a rational polynomial Gaussian example and a signed high-precision regularized Coulomb example; a magnitude-only test would miss the original error.

## Appendix E. Correction register for the frozen v1.4 target

Severity labels follow the audit rules: S1 is a local inconsistency, precision or scope correction; S2 affects a claimed proof, comparison or reproducibility obligation. In that v1.5 audit of the frozen v1.4, no S2 finding and no counterexample to the stated concrete HP theorem was found; the v1.4 portable profile was reproduced (19/19).

| ID | Severity | Frozen v1.4 defect | Integrated repair |
|---|---|---|---|
| F24-01 | S1, source locator | Section 11.4 attributed the Gram-matrix/cooling statement to Section 10.6 of M72; in ZS-M72 v1.8 that section is the Ornstein–Uhlenbeck diffusive-window theorem and the Gram result is Appendix S6.10 (K1–K4) | Section 11.4 corrected; M72 exhibits the rank-one all-ones case, the rank-one reformulation is M73's own |
| F24-02 | S1, superfluous hypothesis | The memory-pair Gaussian bound (4.9) was stated under $\Delta\ge\Delta_{\rm tail}(n)=1750+384\log(1.733n)$, although the given proof needs only $\Delta\ge2200$; the logarithm entered (8.27) | Condition replaced by $\Delta\ge2200$ in (4.9), (8.27) and the verifier |
| F24-03 | S1, overstated limitation | Section 8.10 stated that "the present bound $h_N=O(R)$ imposes a square-root requirement on this particular convexity majorant" | Theorem L: the convexity majorant requires only $\Omega=O(R^{1/6})$; the sentence is withdrawn and Theorem N attributes the square root to the third-order term |
| F24-04 | S1, evidence status | Section 12.1 said the eleven legacy modules were "not recovered in the accessible results" | Exhaustive enumeration of Repo 2 (238 files) and Drive-wide title search: absent there; still not a proof of global nonexistence |
| F24-05 | S1, table | Section 13.1 growth table listed "Crude full-space convexity loss $h_N=O(R)$" | Replaced by Theorem N with the two gap rows and the exact pins |
| F24-06 | S1, corpus locator | Section 10.3 attributed the finite-window criterion to "S19-R/FW" | Historical v1.5 action: marked open. Resolved in v1.8 in the supplied seed lineage, not under the separate paper ZS-S19; see Section 10.3 |

## Appendix F. Earlier correction lineage retained

| Earlier finding | Scientific content retained from v1.5 |
|---|---|
| F20-01 | Frobenius rather than replicated worst-row control; Sections 4.4 and 5.3 |
| F20-02 | Exact Gaussian mean energy and its source signal; Section 4.2 |
| F20-03 | Global moving-phase budget and full Gaussian tails; Sections 5.3 and 7.1 |
| F20-04 | Retraction of the distinct-preparation quadratic error; Section 11.2 and Appendix A-prime |
| F20-05 | Actual-reference state comparison and exactly one division of $\Gamma'$ by $\Delta$; Section 6 |
| F20-06 | Multiplicative source-error budgets; Section 4.3 |
| F20-07 | v1.0 grade-4/PASS declaration remains retracted; Section 16 |
| F20-08 | Spectral location before a residual/gap ground-state conclusion; Section 8.2 |
| F21-01 to F21-07 | Corrected historical certificate, signed four-corner coefficient, product of relative errors, units, exact decimal inputs, standard alternative, Gram rank/cutoff/domain/locators |
| F22-01 to F22-06, C22-01 | Source completeness, unbounded Schur/DSS comparison, $4.00080004$, Gaussian-tail exponents, provenance counts, no artificial gates, M31 intermediate algebra not a dependency |
| F23-01 to F23-13 | Package reproducibility, reality hypothesis of HP-A, Gaussian sign, reference-matrix types, power counting, Gram rank, interval semantics, exact rounding, arithmetic/notation, DSS comparison, open-target scope, value gate, source locator |
| HP1–HP13 supplement | Parity identity, cross term, fourth-derivative/even bounds, Temple sandwich, flip control, all-$R$ envelope, Schur identity and limits integrated into Section 8 |

The historical sequence is seed v1.7–v1.8, v1.0 and its audit, v1.1 and its audit, v1.2 and its audit/parity supplement, v1.3, v1.4 (English integration and portable profile), and v1.5 (structural results L, LOC-2, N, Q, C1–C2 and corrections F24-01–06). The parity-half result originated before v1.4; the v1.5 results originated in that revision. Version 1.6 adds Theorems LC, LC-prime and O, closes C1, and corrects the scope findings in Appendix K. Version 1.7 adds the non-perturbative route (Section 8.12, Appendix L), Corollary NP-B, Section 13.7 and the frozen-v1.6 audit with corrections F26-01–F26-16 (Appendix M).

## Appendix G. Historical scientific coverage map from v1.4 to v1.5

| v1.4 location or topic | v1.5 location and treatment |
|---|---|
| Release table, abstract, Section 1 | Updated for the new results; central theorem and status unchanged |
| Section 2 | Unchanged; transverse-structure remark added to 2.3; Walsh reading (2.12) added to 2.4 |
| Section 3 | Constants $Z_\perp$, $S_K$, $h'_N$, $G_{\rm loc}$, $m$ added |
| Section 4.1 | Theorem L with proof and consequences; Lemma 4.3 |
| Section 4.2 | (4.9) with the $n$-independent condition $\Delta\ge2200$ (F24-02) |
| Sections 4.3–4.6, 5–7 | Unchanged apart from the per-site remarks used by LOC-2 |
| Section 8 | 8.2, 8.8 use $h^{(L)}_N$; 8.4 adds the gradient form (8.13b); 8.6 adds (8.23b); new 8.6b (Theorem LOC-2); 8.7 adds the local replacements; 8.9 table with both gap rows; 8.10 ladder extended |
| Sections 9–11 | Unchanged apart from $h^{(L)}_N$ and the M72 locator (F24-01) |
| Section 12 | v1.5 profile, Repo 2 enumeration (F24-04), extended proof-to-code map |
| Section 13 | Rewritten: Theorems N, Q, C1, C2, missing-object signature, locality reading |
| Sections 14–16 | Debt board unchanged; locality literature and same-example comparison added; grade card in Mission 1.7 format |
| Appendices A–D, F–H | Retained; E is the v1.4 correction register (F24); new Appendices I and J |

## Appendix H. Historical numerical tables and diagnostics

The following values are copied from the supplied v1.3 scientific tables with English headings. They are **historical, rounded, source-reported diagnostics**, not current verification output. Their missing generating modules prevent a fresh reproduction of the finite-geometry optimization. They are preserved for continuity and must not be substituted for the universal certificate (8.30).

### Historical moving-reference values

| R | n | lambda_e | T | A_R | S4 finite | S8 finite | D_R | delta_H | log10 Omega_D | Delta | sigma max | F4 max | Q2 max | B2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | $6.25\times 10^{-11}$ | $4.06\times 10^{17}$ | $7.8\times 10^{-8}$ | 19.2 | 367 | $7.8\times 10^{-9}$ | $8.6\times 10^{-9}$ | 6.163 | $1.45\times 10^{6}$ | $1.7\times 10^{-8}$ | $6.6\times 10^{-8}$ | $2.5\times 10^{-21}$ | 3.0e-05 |
| 8 | 2 | $6.25\times 10^{-11}$ | $4.06\times 10^{17}$ | $1.6\times 10^{-7}$ | 68.6 | 1.14e+03 | $2.4\times 10^{-8}$ | $1.9\times 10^{-8}$ | 6.559 | $3.62\times 10^{6}$ | $2.7\times 10^{-8}$ | $1.0\times 10^{-7}$ | $2.5\times 10^{-21}$ | 7.4e-05 |
| 27 | 3 | $1.85\times 10^{-11}$ | $4.63\times 10^{18}$ | $8.9\times 10^{-8}$ | 164 | 2.35e+03 | $1.5\times 10^{-8}$ | $1.3\times 10^{-8}$ | 7.136 | $1.37\times 10^{7}$ | $1.6\times 10^{-8}$ | $6.0\times 10^{-8}$ | $2.2\times 10^{-22}$ | 8.3e-05 |
| 64 | 4 | $7.81\times 10^{-12}$ | $2.60\times 10^{19}$ | $5.9\times 10^{-8}$ | 175 | 2.35e+03 | $1.1\times 10^{-8}$ | $9.5\times 10^{-9}$ | 7.429 | $2.68\times 10^{7}$ | $9.3\times 10^{-9}$ | $3.6\times 10^{-8}$ | $3.8\times 10^{-23}$ | 6.8e-05 |
| 125 | 5 | $4.00\times 10^{-12}$ | $9.92\times 10^{19}$ | $4.3\times 10^{-8}$ | 188 | 2.35e+03 | $7.9\times 10^{-9}$ | $7.6\times 10^{-9}$ | 7.662 | $4.59\times 10^{7}$ | $6.3\times 10^{-9}$ | $2.4\times 10^{-8}$ | $1.0\times 10^{-23}$ | 6.0e-05 |

### Historical general-static values

| R | n | log10 Omega_S | Delta | g0 | sigma | F4 | kappa | D_mem | D_source | eta_hat | r_length | T eta_hat | rho_e2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | 4.000 | $1.00\times 10^{4}$ | $9.998\times 10^{3}$ | $3.05\times 10^{-5}$ | $1.17\times 10^{-4}$ | $9.45\times 10^{-9}$ | $2.08\times 10^{-12}$ | $6.27\times 10^{-10}$ | $9.3\times 10^{-28}$ | $5.45\times 10^{-21}$ | $3.8\times 10^{-10}$ | $4.31\times 10^{-8}$ |
| 8 | 2 | 4.345 | $2.22\times 10^{4}$ | $2.21\times 10^{4}$ | $5.74\times 10^{-5}$ | $2.19\times 10^{-4}$ | $8.02\times 10^{-9}$ | $1.98\times 10^{-12}$ | $8.43\times 10^{-10}$ | $9.9\times 10^{-28}$ | $7.39\times 10^{-21}$ | $4.0\times 10^{-10}$ | $2.68\times 10^{-8}$ |
| 27 | 3 | 4.797 | $6.27\times 10^{4}$ | $6.26\times 10^{4}$ | $5.10\times 10^{-5}$ | $1.95\times 10^{-4}$ | $2.52\times 10^{-9}$ | $5.00\times 10^{-13}$ | $2.73\times 10^{-10}$ | $4.1\times 10^{-29}$ | $6.49\times 10^{-22}$ | $1.9\times 10^{-10}$ | $8.74\times 10^{-9}$ |
| 64 | 4 | 5.009 | $1.02\times 10^{5}$ | $1.02\times 10^{5}$ | $3.97\times 10^{-5}$ | $1.52\times 10^{-4}$ | $1.21\times 10^{-9}$ | $1.59\times 10^{-13}$ | $1.39\times 10^{-10}$ | $3.7\times 10^{-30}$ | $1.15\times 10^{-22}$ | $9.6\times 10^{-11}$ | $4.73\times 10^{-9}$ |
| 125 | 5 | 5.180 | $1.51\times 10^{5}$ | $1.51\times 10^{5}$ | $3.30\times 10^{-5}$ | $1.26\times 10^{-4}$ | $6.77\times 10^{-10}$ | $6.58\times 10^{-14}$ | $8.16\times 10^{-11}$ | $5.7\times 10^{-31}$ | $3.03\times 10^{-23}$ | $5.7\times 10^{-11}$ | $2.91\times 10^{-9}$ |

### Historical parity-static values

| R | n | log10 Omega_HP | Delta | sigma | sigma_even | F4 | F4_even | kappa | kappa_even | M_par | sigma kappa^2 / M_par | S5 finite | 2 T M_par | rho_e2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | 4.000 | $1.00\times 10^{4}$ | $3.05\times 10^{-5}$ | $1.10\times 10^{-6}$ | $1.17\times 10^{-4}$ | $5.91\times 10^{-6}$ | $9.45\times 10^{-9}$ | $4.34\times 10^{-10}$ | $3.48\times 10^{-22}$ | 7.8 | 102.5 | $2.83\times 10^{-4}$ | $4.31\times 10^{-8}$ |
| 8 | 2 | 4.189 | $1.55\times 10^{4}$ | $9.83\times 10^{-5}$ | $2.67\times 10^{-6}$ | $3.76\times 10^{-4}$ | $1.44\times 10^{-5}$ | $1.97\times 10^{-8}$ | $6.85\times 10^{-10}$ | $3.69\times 10^{-21}$ | 10.3 | 344.9 | $3.00\times 10^{-3}$ | $5.96\times 10^{-8}$ |
| 27 | 3 | 4.605 | $4.03\times 10^{4}$ | $9.90\times 10^{-5}$ | $1.57\times 10^{-6}$ | $3.78\times 10^{-4}$ | $8.46\times 10^{-6}$ | $7.62\times 10^{-9}$ | $1.54\times 10^{-10}$ | $3.24\times 10^{-22}$ | 17.7 | 777.9 | $3.00\times 10^{-3}$ | $2.34\times 10^{-8}$ |
| 64 | 4 | 4.800 | $6.31\times 10^{4}$ | $8.19\times 10^{-5}$ | $1.00\times 10^{-6}$ | $3.13\times 10^{-4}$ | $5.39\times 10^{-6}$ | $4.03\times 10^{-9}$ | $6.29\times 10^{-11}$ | $5.77\times 10^{-23}$ | 23.0 | 798.9 | $3.00\times 10^{-3}$ | $1.37\times 10^{-8}$ |
| 125 | 5 | 4.955 | $9.02\times 10^{4}$ | $7.17\times 10^{-5}$ | $7.02\times 10^{-7}$ | $2.74\times 10^{-4}$ | $3.78\times 10^{-6}$ | $2.46\times 10^{-9}$ | $3.08\times 10^{-11}$ | $1.51\times 10^{-23}$ | 28.7 | 823.5 | $3.00\times 10^{-3}$ | $8.98\times 10^{-9}$ |

### Other retained historical diagnostics

- The first-quadratic-Duhamel frequency logarithms at $R=2,8,27,64,125$ were reported as 15.0, 15.6, 16.7, 17.3 and 17.8; the coarse product-vacuum route gave approximately 27.3 to 31.6. These do not supply lower bounds.
- At $\Omega=4000$, $b=1/8$ and 20000 Monte Carlo samples, the inherited residual standard deviations were reported as $(1.00,1.96,3.91,6.20,8.92)\times10^{-5}$, with ratios to the stated upper bounds falling from .029 to .004. The old $\Omega=10$ exploration is outside the certified regime and is not evidence for the theorem.
- A finite Fock $R=2$ geometry with $\Omega=1$, $g=200$, shifts $(2,.3,.3)$, $c=1$ and cutoff 10, together with two nearby parameter sets, was reported to show residual improvements of 16–22 relative to the scalar reference. These are truncated-model diagnostics, not continuum certification.
- The supplied lineage reports rational checks, four small Fock parameter sets, a 35-row FULL run and 20 one-failure injection runs. This release does not possess their complete source/ledger package and does not attest to those counts as newly reproduced.

## Appendix I. The two Gaussian lemmas of Theorem LOC-2

**Proof of Lemma GI.** Let $X\sim N(0,\Sigma)$, $Y$ an independent copy, $X_t=tX+\sqrt{1-t^2}\,Y$, so that $X_t\sim N(0,\Sigma)$ and $\operatorname{Cov}(X,X_t)=t\Sigma$. Put $\psi(t)=\mathbb E[F(X)G(X_t)]$; then $\psi(1)=\mathbb E[FG]$ and $\psi(0)=\mathbb E F\,\mathbb EG$. Differentiating,

$$
\psi'(t)=\mathbb E\Bigl[F(X)\,\nabla G(X_t)\cdot\Bigl(X-\frac{t}{\sqrt{1-t^2}}Y\Bigr)\Bigr].
$$

Gaussian integration by parts, $\mathbb E[X_ih(X,Y)]=\sum_j\Sigma_{ij}\mathbb E[\partial_{X_j}h]$ and $\mathbb E[Y_ih(X,Y)]=\sum_j\Sigma_{ij}\mathbb E[\partial_{Y_j}h]$, applied to $h=F(X)\partial_iG(X_t)$ gives

$$
\mathbb E[F\,\partial_iG(X_t)X_i]=\sum_j\Sigma_{ij}\mathbb E[\partial_jF\,\partial_iG(X_t)]+t\sum_j\Sigma_{ij}\mathbb E[F\,\partial_j\partial_iG(X_t)],
\qquad
\mathbb E[F\,\partial_iG(X_t)Y_i]=\sqrt{1-t^2}\sum_j\Sigma_{ij}\mathbb E[F\,\partial_j\partial_iG(X_t)],
$$

so the second-derivative terms cancel and $\psi'(t)=\mathbb E[\nabla F(X)^T\Sigma\nabla G(X_t)]$. Integrating over $[0,1]$ gives the identity; Cauchy–Schwarz in each $(a,c)$ term, with $X$ and $X_t$ equal in law, gives the bound. Polynomial growth of $F,G$ and their derivatives justifies the differentiation under the expectation. $\square$

**Proof of Lemma OU.** The Ornstein–Uhlenbeck process $dX_t=-\sqrt A\,X_tdt+dB_t$ has generator $\tfrac12\Delta-\sqrt A\,x\cdot\nabla=-\mathcal L$ and invariant measure $N(0,\tfrac12A^{-1/2})=\mu_0$; its transition law from $x$ is $N(e^{-t\sqrt A}x,\Sigma_t)$ with $\Sigma_t=\tfrac12A^{-1/2}(I-e^{-2t\sqrt A})$, which is the Mehler formula. Differentiating $F(e^{-t\sqrt A}x+G_t)$ in $x_c$ gives $\sum_b(e^{-t\sqrt A})_{bc}(\partial_bF)(e^{-t\sqrt A}x+G_t)$, whence the commutation identity. For centered $F$, $\mathcal L^{-1}F=\int_0^\infty e^{-t\mathcal L}F\,dt$ converges in $L^2(\mu_0)$ because $\|e^{-t\mathcal L}F\|_2\le e^{-\Delta t}\|F\|_2$; differentiating under the integral and using that $e^{-t\mathcal L}$ is an $L^2(\mu_0)$ contraction on all functions gives $\|\partial_c\mathcal L^{-1}F\|_2\le\sum_b\int_0^\infty|(e^{-t\sqrt A})_{bc}|dt\,\|\partial_bF\|_2$.

For the matrix bounds write $A=\Delta^2(I+M)$ with $M=A/\Delta^2-I\ge0$ (because $A\ge\Delta^2I$). Then $\Sigma=\tfrac12A^{-1/2}=(2\Delta)^{-1}\sum_{k\ge0}\binom{-1/2}{k}M^k$ and $|\binom{-1/2}{k}|=\binom{2k}{k}4^{-k}\le1$, so entrywise $|\Sigma|\le(2\Delta)^{-1}\sum_k|M|^k=(2\Delta)^{-1}(I-|M|)^{-1}$, the series converging when the row-sum norm $m$ of $|M|$ is below one. Next $\sqrt A=\Delta I+B$ with $B=\Delta\sum_{k\ge1}\binom{1/2}{k}M^k$ and $|\binom{1/2}{k}|\le\tfrac12$, so $|B|\le\tfrac{\Delta}2|M|(I-|M|)^{-1}$. Since $\Delta I$ commutes with $B$, $e^{-t\sqrt A}=e^{-t\Delta}e^{-tB}$ and $|e^{-tB}|\le\sum_kt^k|B|^k/k!=e^{t|B|}$ entrywise, hence $W\le\int_0^\infty e^{-t\Delta}e^{t|B|}dt=(\Delta I-|B|)^{-1}=\Delta^{-1}(I-|B|/\Delta)^{-1}$ when the spectral radius of $|B|$ is below $\Delta$, which holds when $\widetilde M=\tfrac12|M|(I-|M|)^{-1}$ has row-sum norm $\tfrac12m/(1-m)<1$. Row-sum norms: $\|\,|\Sigma|\,\|\le(2\Delta)^{-1}/(1-m)$ and $\|W\|\le\Delta^{-1}/(1-\tfrac12m/(1-m))=\Delta^{-1}(1-m)/(1-3m/2)$, whose product is $(2\Delta^2)^{-1}/(1-3m/2)$. In the S9 model $M=(8+\delta_c+gK^{(c)})/\Delta^2$, so $m\le(8+\delta_c+gS_K(n))/\Delta^2$ by Lemma 4.3. $\square$

**Exact finite model.** In coordinates $y=\Sigma^{-1/2}x$ the measure is standard normal and $\mathcal L=\sum_{ij}(\sqrt A)_{ij}a_i^\dagger a_j$ with $a_j=\partial_{y_j}$, $a_i^\dagger=y_i-\partial_{y_i}$, because $\Sigma^{1/2}$ commutes with $\sqrt A$. On multivariate Hermite polynomials $a_j\operatorname{He}_\alpha=\alpha_j\operatorname{He}_{\alpha-e_j}$ and $a_i^\dagger\operatorname{He}_\alpha=\operatorname{He}_{\alpha+e_i}$, so $\mathcal L$ preserves the total degree and its restriction to degree $d$ is a finite matrix whose eigenvalues are sums of $d$ eigenvalues of $\sqrt A$, all at least $d\Delta$. The companion script `loc2_toy.py` builds the pair polynomials in $x$, converts them to the Hermite basis, solves $\mathcal L h=\delta$ exactly on each degree block, evaluates $\mathcal B(U,\delta)=\langle U,h\rangle_{\mu_0}$ by Hermite orthogonality, and compares with the bounds; the residual $\|\mathcal Lh-\delta\|_2$ is below $10^{-16}$ in the runs reported in Section 8.6b.

## Appendix J. Weyl calculus for the quadratic model

Let $W(\xi,\pi)=\exp(i(\pi\cdot x-\xi\cdot p))$, so that $W(a)W(b)=e^{i\sigma(a,b)/2}W(a+b)$ with $\sigma((\xi,\pi),(\xi',\pi'))=\pi\cdot\xi'-\xi\cdot\pi'$, and $W(\xi,\pi)^*xW(\xi,\pi)=x+\xi$, $W^*pW=p+\pi$. Let $h(d)=\tfrac12|p|^2+\tfrac12(x-d)^TA(x-d)$, whose ground state is $\Omega_d=W(d,0)\Phi_G$ with $\Phi_G$ the ground state of $h(0)$; $\Phi_G=W(-d,0)\Omega_d$.

The Heisenberg evolution under $h(d)$ is linear: with $C_t=\cos(\sqrt A\,t)$ and $S_t=\sin(\sqrt A\,t)$,

$$
e^{-ith}x\,e^{ith}=d+C_t(x-d)-A^{-1/2}S_tp,\qquad
e^{-ith}p\,e^{ith}=\sqrt A\,S_t(x-d)+C_tp.
$$

Therefore $e^{-ith}W(-d,0)e^{ith}=\exp\bigl(i\,d\cdot(\sqrt AS_t(x-d)+C_tp)\bigr)=W(-C_td,\sqrt AS_td)\,e^{-i\,d^T\sqrt AS_td}$, and applying this to $\Omega_d=W(d,0)\Phi_G$ and combining the Weyl operators,

$$
e^{-ith(d)}\Phi_G=e^{-itE_A^{G}}e^{i\Theta_d(t)}\,W\bigl((I-C_t)d,\;\sqrt AS_td\bigr)\Phi_G,\qquad
\Theta_d(t)=-\tfrac12\,d^T\sqrt A\,S_t\,d, \tag{J.1}
$$

where $E_A^{G}=\tfrac12\operatorname{tr}\sqrt A$ is the zero-point energy, and the factor $\tfrac12$ arises from $-d^T\sqrt AS_td+\tfrac12\sigma((-C_td,\sqrt AS_td),(d,0))=-d^T\sqrt AS_td+\tfrac12d^T\sqrt AS_td$. For $H=h(d)+E_0-E_A^{G}$, including the branch ground energy gives $e^{-itH}\Phi_G=e^{-itE_0}e^{i\Theta_d(t)}W(\eta_d(t))\Phi_G$ with $\eta_d(t)=((I-C_t)d,\sqrt AS_td)$.

For two branches $d_\pm=d_c\mp\delta$ with the same $A$: $\langle W(\eta_-)\Phi_G,W(\eta_+)\Phi_G\rangle=e^{i\sigma(-\eta_-,\eta_+)/2}\langle\Phi_G,W(\eta_+-\eta_-)\Phi_G\rangle$, and $\sigma(\eta_-,\eta_+)=d_-^T\sqrt AS_t(I-C_t)d_+-d_-^T(I-C_t)\sqrt AS_td_+=0$ because all the matrices are functions of $A$. The Gaussian expectation of a Weyl operator in the ground state of $h(0)$ is real and equals $\exp(-\tfrac14(\xi^T\sqrt A\xi+\pi^TA^{-1/2}\pi))$; with $\eta_+-\eta_-=-2((I-C_t)\delta,\sqrt AS_t\delta)$ the exponent is $\delta^T\sqrt A[(I-C_t)^2+S_t^2]\delta=2\delta^T\sqrt A(I-C_t)\delta\le4\omega_{\max}|\delta|^2$. Finally $\Theta_+-\Theta_-=-\tfrac12[(d_c-\delta)^TQ(d_c-\delta)-(d_c+\delta)^TQ(d_c+\delta)]=2d_c^TQ\delta$ with $Q=\sqrt AS_t$, $|Q|\le\omega_{\max}$. Combining, $|\mathcal Ae^{it(E_+-E_-)}-1|\le|\Theta_+-\Theta_-|+1-e^{-\|\eta_+-\eta_-\|_A^2/4}\le2\omega_{\max}|d_c||\delta|+4\omega_{\max}|\delta|^2$, which is (13.3). The one-dimensional split-operator check (row `COHERENT-ECHO-1D`, $\omega=3$, $d_c=.4$, $\delta=.15$) reproduces $|\mathcal A|=\exp(-(\omega\Delta\xi^2+\Delta\pi^2/\omega)/4)$ to $4\times10^{-7}$ and $\arg\mathcal A=2d_c\omega\sin(\omega t)\delta$ to $4\times10^{-6}$ at $t=.3,1.1,2.0$, confirming the factor $\tfrac12$ in (J.1) and the sign conventions.


## Appendix K. Audit of the frozen v1.5 and integration in v1.6

The frozen-source verdict is **AUDIT-MAJOR-REVISION**, highest severity S2. The original square-root certificate survives and its 29-row profile reproduces. The findings below concern theorem scope, external mappings and local corrections; the proved v1.6 cubic estimate is a new result, not a retroactive v1.5 achievement.

| Finding | Severity | Frozen-v1.5 issue | Integrated resolution |
|---|---|---|---|
| F25-01 | S2 | C2 is described as equivalent to fixed confinement; only a sufficient implication is proved. The aggregate Walsh budgets also do not assert general diameter decay. | Section 13.4: State a gap plus four sufficient budgets; remove the converse and the claimed equivalence with general coefficient locality. |
| F25-02 | S2 | The stated finite-dimensional-site exclusion is false: Section 2 explicitly permits infinite-dimensional site spaces and unbounded on-site Hamiltonians. | Section 15.2: Replace the exclusion with the actual finite-range and small-interaction-norm conditions, checked against Definition 1 and Theorem 3. |
| F25-03 | S2 | The blanket assertion of no ground-state result misses Theorem 5.2, which proves clustering assuming a gap. | Section 15.2: Identify the nearest-neighbor/on-site model, the Fourier condition, and the assumed gap; do not import an unproved gap or echo theorem. |
| F25-04 | S2 | The entrywise covariance/resolvent decay used for the proposed fixed-confinement star estimate is not a consequence of the proved row-sum bounds; no convolution estimate is supplied. | Section 13.5, Theorem O: Withdraw the unproved quantitative inference from the proved layer, retain the research route as open, and give the actual bond-norm and convexity obstructions. |
| F25-05 | S1 | The standalone propagator omits exp(-it E_A). Setting d=0 leaves a missing nontrivial ground-state phase. | Appendix J; LC-SCOPE-CONTROLS: Insert the zero-point phase and specify H=h(d)+E_0-E_A. The common phase cancels in the already stated branch echo. |
| F25-06 | S1 | The symbolic transverse upper bound drops the factor 1+10^-78 introduced by its regularization estimate. | Section 4.1: Retain the factor explicitly. The ample numerical slack leaves 18090 n unchanged. |
| F25-07 | S2 | The affine rules are asserted for all p>=9/10 although finite checks support a bounded interval. At p=4 the quartic exponent is 20, not 24; the cubic exponent is 29/2, not 35/2. | Section 13.1; deterministic counterexample in the research record: Restrict the affine statement to the justified intervals. Use monotonicity, not affine extrapolation, to retain closure above p=3/2. Restrict the fidelity floor to its stated majorant. |
| F25-08 | S1 | The Delta quantifier is not explicit. A Delta-independent Delta^-7 estimate at fixed nonzero quadratic remainder is not a valid general statement. | Theorem LC and Corollary C1: Specify the required design curve; prove the stronger log-free bound there. Preserve the fully general derivative inequality with all terms. |
| F25-09 | S1 | The logarithmic majorant and the comparison with the quadratic model are described as intrinsic obstructions more strongly than the estimates establish. | Abstract and Section 13.3: State that the logarithm is a limitation of the displayed sufficient bound; do not infer necessity for the exact readout. |
| F25-10 | S2 | Fixed Delta is not numerically restricted even though the proof uses the Gaussian pair-reference and tail budgets. | Section 13.4: Require Delta>=10000, sufficient for the imported numerical budgets, and make source-sign uniformity in H3 explicit. |

The complete report and research record disclose the twelve audit passes, source locators, deterministic attacks, current proof cards and the unresolved grade adjudication. The exact original bytes are preserved. No claim that the initial v1.5 verdict was PASS is created by these repairs.

## Appendix L. Constants of the non-perturbative envelope

All quantities are in units $a=g=1$, $c=1/20$, with $n\ge2$, $R\le n^3$, $N\le n^3+1$, $\lambda_0=10^{-3}$, $\lambda_e=5\times10^{-10}n^{-3}$, $\Delta=10^4n^p$, $g_0\ge.9989\Delta$ and $\Omega^2\ge\Delta^2$. The shorthand is
$$
M_2(r_{\min})\le\frac{2.0002}{(19.3n)^3},\qquad M_3(r_{\min})\le\frac{6.0006}{(19.3n)^4},\qquad M_4(r_{\min})\le\frac{24.0024}{(19.3n)^5},\qquad M_3(1)=\frac{6.0006}{.748^4}.
$$
The Chebyshev-shell bound gives
$$
S_{M2}(n)\le2.0002\cdot2.3894\,[24(1+\log n)+2.4041],
$$
because $(k-.252)^{-3}\le2.3894k^{-3}$ for $k\ge1$ and each shell $|m|_\infty=k$ contains $24k^2+2$ points with $|m|\ge k$. Also $h_m=S_{M2}(n)+M_2(r_{\min})+S_4^U(\lambda_e+10^{-6})+M_3(r_{\min})(\lambda_0+10^{-6})+10^{-3}$, and $\|B\|\le1+2h_m/\Omega^2$ once $h_m/\Omega^2\le1/2$.

Tails use $P_B=2Ne^{-\Delta/65}$, $\sqrt{P_B}\le\sqrt{2N}e^{-\Delta/130}$ and $P_B^{1/4}\le(2N)^{1/4}e^{-\Delta/260}$. Each exponential is replaced by $(64/e)^{64}y^{-64}$. Every such term decays for $p\ge1/5$.

- $W_1=S_{M2}(n)+M_2(r_{\min})+S_4^U(\ell_2+10^{-6}+\lambda_e)+M_3(r_{\min})(\lambda_0+10^{-6})+ND_2P_B+h'_NP_B$.
- $W_2=\sqrt{4.00080004S_6^{\rm lat,U}}+M_2(r_{\min})+S_4^U(\ell_2+10^{-6}+\lambda_e)+M_3(r_{\min})(\lambda_0+10^{-6})+\sqrt ND_2\sqrt{P_B}$.
- $\|\nabla V_{ab}\|_2\le\sqrt2(M_3(1)+C_3c^{-4}\sqrt{P_B})$ for memory pairs and $\le\sqrt2(M_3(r_{\min})+C_3c^{-4}\sqrt{P_B})$ for pairs containing the source.
- $\|\nabla V_{aa}\|_2\le\sqrt{S_8^U}+S_5^U(\ell_2+10^{-6}+\lambda_e)+M_4(r_{\min})(\lambda_0+10^{-6})+2NC_3c^{-4}\sqrt{P_B}$.
- $T_3^{\rm mem}\le3\|\nabla V_{ab}\|_2\Phi_M/g_0^2+6K_4(\Phi_M^{(4)})^2\Phi_Mg_0^{-7/2}$.
- $T_3^{\rm src}\le(2\|\nabla V_{0k}\|_2\Phi_M+\|\nabla V_{jk}\|_2\Phi_S)/g_0^2+2K_4(2\Phi_S^{(4)}\Phi_M^{(4)}\Phi_M+(\Phi_M^{(4)})^2\Phi_S)g_0^{-7/2}$.
- $T_3^{\rm rep}\le M_3(1)+C_3c^{-4}P_B+(\|\nabla V_{jj}\|_2+2\|\nabla V_{jk}\|_2)\Phi_M/g_0^2+6K_4(\Phi_M^{(4)})^2\Phi_Mg_0^{-7/2}$.

Here $K_4=((\pi/2)\gamma_4)^2/(2\sqrt2)<1.512$. The verifier builds exactly these expressions in `np_envelope` and certifies their suprema over all real $n\ge2$ with the exponent rules of Section 8.9. Rows `NP-G-ALLR`, `NP-P1-ALLR` and `NP-EXPONENTS` record the values and the pins.

## Appendix M. Audit of the frozen v1.6 and integration in v1.7

The audit target is ZS-M73 v1.6, manuscript SHA-256 `62943c16e17b4b645cd067b06406b71cb373c710e6b519f28e7dcd880487b6f9` and release ZIP SHA-256 `25448f179388051453b7617ec8d4309c6bfcb12f548580eca4ed1d146ce8b7f9`. The untouched `PORTABLE-LC-33` verifier reproduced 33 PASS and 0 FAIL.

**Frozen verdict: AUDIT-MAJOR-REVISION.** The central Theorems LC and LC-prime survive. The highest severity is S2, confined to the secondary Theorem N(v). The meta-audit finding is that the grade-4 objective was not met.

The meta-audit found that v1.6 closed the v1.5 candidate obligation and advanced the perturbative ladder by one order. The seed's grade-4 criterion, $R$-uniform confinement, was not met. Further order-by-order work would stop at the pins of Theorem N, so the bottleneck was the expansion method itself. The research transferred to a method change (Section 8.12) rather than to package polishing.

| Finding | Severity | Frozen-v1.6 issue | Integrated resolution |
|---|---|---|---|
| F26-01 | S2 | Theorem N(v) says that $O(N)$ third- and fourth-order bounds would pin the certificate at $p=1$. This omits the extensive cubic secular term $TN\Delta^{-7}\propto n^{9-7p}$, whose pin is $9/7$. The error is inherited from v1.5 | Section 13.1: statement and proof corrected; the pin $9/7$ binds until a flip-local cubic bound is supplied |
| F26-02 | S1 | The consequences of Theorem L (Section 4.1) give values on $\Delta=10^4n^{3/2}$ as if current. On the LC-prime curve the value is $5.698\times10^{-5}$ | Section 4.1: values stated for each curve |
| F26-03 | S1 | The LOC-2 numerical values (Section 8.6b) belong to the HP-prime curve and are not labelled as such | Section 8.6b: labelled, with the LC-prime-curve values added |
| F26-04 | S1 | Section 8.6b says that Section 13.4 states the open third-order obligation, which Theorem LC has since closed | Section 8.6b: points to Theorem LC |
| F26-05 | S1 | Section 8.7 keeps the withdrawn inference that the $\rho^{e_2}$ loss is a loss of the majorant "explained" in Section 13.5 (residue of F25-04) | Section 8.7: replaced; Lemma NP-6 shows that the exact source coefficient has no such loss in the convex regime |
| F26-06 | S1 | $\delta_H$ in (5.10) is undefined | Section 5.3: defined |
| F26-07 | S1 | The proof of Lemma LC-A uses a pointwise bound on $\vert e^{-t\sqrt A}\vert$ that is not in the statement of Lemma OU, and cites Lemma OU before it is stated | Lemma OU statement extended; forward reference made explicit |
| F26-08 | S1 | The Theorem Q proof asserts $\rho_Q<.0011$, but $1.001\cdot1.0001-1=.0011001$ | Section 13.3: corrected. The conclusion $e_*<.091$ is unchanged |
| F26-09 | S1 | Appendix E says that no S2 finding was made "in this revision", which conflicts with Appendix K | Appendix E: sentence scoped to the v1.5 audit of v1.4 |
| F26-10 | S1 | The deterministic counterexample promised in the F25-07 resolution appears only in a verifier ledger, not in the research record | The v1.7 research record states it: at $p=4$ the quartic exponent is $20$, not $24$, and the cubic exponent is $29/2$, not $35/2$ |
| F26-11 | S1 | History row H-0405 gives a date without a time of day or time zone | Recorded in H-0406 (append-only); H-0405 is not edited |
| F26-12 | S1 | Theorem N(ii) calls the third-order term the only growing term, but the v1.4 gap row also grows for $p<3/2$ | Section 13.1: scoped to (8.27) with $h_N^{(L)}$ |
| F26-13 | S1 | The source comparison omits the closest dimension-uniform ground-state literature (Sjöstrand; Helffer–Sjöstrand; Brascamp–Lieb) | Section 15.7 |
| F26-14 | S0 | Numerical wording: $\widetilde D_2=6018.0222\ldots$; the tail value $8.9\times10^{-84}$ holds at $\rho=10\sqrt2c$; the toy row-sum norm is $m\approx.24$–$.26$; the distinct-vector factor is about $35.2$ | Sections 4.1, 8.6b and 11.2 corrected |
| F26-15 | S0 | Section 15.3 omits Bravyi–DiVincenzo–Loss from the source-checked list; Section 14 points to Section 15.2 for the M72 comparison format, which Section 15.5 uses; the title of arXiv:2608.15576 is shortened; the letters $a,e,r,s,P,m$ are reused inside the LC proof | Corrected; the notation reuse is declared in Section 3 |
| F26-16 | S0 | The frozen history file `history_h0001-h0405.md` contains byte-identical duplicate rows H-0401 and H-0402 (each appears twice, in the order H-0401, H-0402, H-0401, H-0402) | Recorded in H-0406; the frozen bytes are not edited, and the later copy of each duplicate carries no additional information |

Verification of this audit is the cross-family recheck described in Section 15.6. It includes independent re-derivation of Lemma LC-A and the S9 constants, direct recomputation of every table value of LC-prime, recomputation of the hashes of all 22 package files, and a rerun of the untouched verifier. The frozen verdict and the new v1.7 results are kept separate; the new theorems are not attributed to v1.6.


## Appendix N. Audit of the frozen v1.7 and integration in v1.8

The frozen target is identified in Section 1.4. Its audit verdict is **AUDIT-MAJOR-REVISION**, highest severity **S2**. The central numerical NP certificates reproduce; the findings concern inference, scope, source transfer and target completeness. The current fixes do not retroactively change the frozen verdict.

| ID | Severity | Frozen defect | Integrated resolution |
|---|---|---|---|
| F27-01 | S2 | Heuristic D assumes an excited probability growing above one and infers a Gaussian necessity floor without controlled phases | Section 13.7 withdraws that inference; SP supplies an exact inference counterexample; both preparations remain OPEN |
| F27-02 | S2 | Seed S21-L's removal of $\sqrt N$ is treated as a sufficient reduction while $T_R\asymp n^6$ remains | Proposition TS and the exact factor table in Section 13.8 |
| F27-03 | S2 | Scalar non-convex localization is presented as the remaining methodological step although the existing $r_4$ majorant retains a growing spatial factor | Section 13.9; separate response and occupied-state obligations |
| F27-04 | S2 | Theorem Q's general sufficient claim omits the Neumann-domain and cosine-lobe conditions | Lemma Q1 and Theorem Q explicitly scoped; the quoted finite-range-in-$R$ application survives |
| F27-05 | S1 | S19-R/FW sought under the wrong corpus identifier; positive spectral weights not sufficient by themselves for a general echo | Sections 10.3, 15.3: seed locator and matching error restored |
| F27-06 | S1 | Combined Sjostrand comparison suppresses the specific boundary and dimension restrictions of Theorem 6.2 | Primary-source comparison in Section 15.7; no unverified full-space transfer |
| F27-07 | S1 | LC-prime still called strongest in this revision; P1-only target propagated into abstract and conclusion | Current hierarchy and both preparation statuses synchronized throughout |
| F27-08 | S1 | Grade card risks treating imported tools or significance outside this model as independent mandatory gates | Section 16 uses Mission correctness, novelty and significance criteria; no added human-review requirement |

The v1.6 audit integration is 15/16 complete at the level of the requested textual/code corrections; F26-13 is partial because citations were added without a complete theorem-level source transfer. This is not a count of independently re-proved theorems. F26-10's rational $p=4$ witness is present in the v1.7 research record, and the historical duplicate history rows are preserved. New findings are not silently relabelled as failures of already closed historical corrections.

## Appendix O. Audit of the frozen v1.8 and integration in v1.9

The frozen target is identified in Section 1.4. Its release was rerun without modification in a Python 3.12.3 environment with the pinned mpmath 1.4.1, NumPy 2.5.3, SciPy 1.18.1 and SymPy 1.12. The result was `PORTABLE-M73-49`, 49 PASS, 0 FAIL, 0 SKIPPED. Forty-seven detail objects are identical to the shipped JSON. The two finite-matrix diagnostics `LOC2-FINITE-MODEL` and `NP-FINITE-IDENTITIES` differ only in last-digit floating-point noise.

**Frozen verdict: AUDIT-MAJOR-REVISION, highest severity S2.** The new v1.8 theorems ST, ER, OB, SP and TS were rederived and found correct in their stated scope. The findings concern the selection of the remaining obligations, the completeness of the residue census, and the operational form of the grade-4 target and qualification card. They do not change any v1.8 theorem into a false statement.

| ID | Severity | Frozen defect | Integrated resolution |
|---|---|---|---|
| F28-01 | S2 (meta) | Sections 13.9, 13.10 and 17 present a growing-window occupied-state echo estimate as a remaining obligation for fixed or polylogarithmic confinement for *both* preparations. For P1 the echo is time-uniform (Appendix A, Theorem S) once the infidelities are small, so the obligation is route-specific, not necessary. The three v1.8 routes therefore did not attack the P1 critical path (non-convex localization plus spatial response), although Section 13.9 named part of it | Section 1.3 and Sections 13.9–13.11 restate the obligations by preparation; Section 8.14 closes the P1 static path at logarithmic confinement |
| F28-02 | S1 | Section 13.9 names $r_4$ ($n^{3/2}\Delta^{-9/2}\sqrt{\log n}$, zero-decay at $p=1/3$) as the growing residue. In the same displayed majorant $r_2$ reaches zero decay first, at $p=2/5$, through $\sqrt R\,M_3(r_{\min})g_0^{-1/2}$ and $R\,M_4(r_{\min})g_0^{-1}$ in $\|\nabla\rho_0\|_2$. The Efron–Stein source term of $H_3$ reaches zero decay at $p=1/4$. The inherited exponent engine gives exponents $(r_2,r_4,H_3)=(1/4,3/4,1/2)$ at $p=1/2$, $(0,3/10,3/10)$ at $p=2/5$ and $(-1/6,0,1/6)$ at $p=1/3$. This also makes the v1.8 resolution of F27-03 partial | Section 13.9 lists all three residues; Lemmas SC and RD remove them |
| F28-03 | S1 | Stale cross-references: the Section 13 introduction says Section 13.7 "records what remains", and the Helffer row of Section 15.7 points to Section 13.7 for going beyond convexity. After v1.8, Section 13.7 is the withdrawal of Heuristic D | Both references now point to Sections 13.9–13.11 and 8.14 |
| F28-04 | S0 | Section 1.3 refers to a "second requested candidate", an unexplained internal process term | Removed |
| F28-05 | S1 | The Section 16 card reports only an overall HOLD. The Mission §5.6 fields for correctness, novelty, significance and verification basis, each with PASS/HOLD/FAIL and evidence, are missing | Section 16 uses the full card for the v1.9 central contribution |
| F28-06 | S1 | The grade-4 target in Section 13.10 is not operational. It lacks a split by preparation, a pre-registered kill test for the P1 static path, and the specific external limitation to be overcome | Section 13.11 fixes the target by preparation and pre-registers kill tests. Sections 15.9 and 16 name the internal barrier (Corollary NP-B) and the external hypothesis mismatch (Theorem O(1) versus published LPPL theorems) |
| F28-07 | S0 | The README states that 38 scientific detail objects match the designated-environment v1.7 run exactly. That statement depends on the exact Python build. Under Python 3.12.3 two float diagnostics differ in the last digits | Section 12.5 reports matches "to floating-point noise" and names the rows |

*Integration of the v1.7 audit in v1.8 (user question 1).* All eight findings F27-01–08 are present at the stated locations. F27-01, F27-02 and F27-04–F27-08 are fully resolved in scope. F27-03 is partially resolved (F28-02): the scalar-localization insufficiency was correctly identified, but the census of growing source-row residues was incomplete. As in earlier appendices, this is a count of integrated corrections, not of independently reproved theorems.

*Grade-4 target in v1.8 (user question 2).* The target was stated with its full quantifiers and was correctly kept separate from achievement. It was not operational (F28-06). Its list of remaining obligations included a non-necessary one for P1 and omitted two growing residues (F28-01, F28-02). The v1.9 research used the corrected list. The frozen verdict is not changed by the later results.

## Appendix P. Integration of v2.0: frozen route card, corrections to v1.9 and referee record

### P.1 Frozen route card

The route card was frozen at 2026-09-23 23:55:09 KST, before any external literature was consulted. It was written under ACTIVE ZSPIN-RULES-2 minor 2.4 (kernel and breakthrough modules) with Mission 1.7 loaded, and the budget was three substantive rounds. The card is reproduced here in the manuscript's language.
- **Mission card.** FQ2/RQ3, support for SPINE-L3. Output role SUPPORT + METHOD; no CORE claim.
- **Live debt.** The first nontrivial obligation of the v1.9 fixed-confinement path: an $n$-uniform, sign-preserving $\ell^\infty$ estimate of $(\Omega^2+K)^{-1}\mathbf 1$ and $K^k\mathbf 1$.
- **BEFORE.** Hypothesis of the v1.9 research record: the signed kernel is bounded, so a signed Lemma SR could remove $\widehat S_2\asymp\log n$. Small-$n$ numerics ($n\le16$) suggested convergence of the first-order edge polarization.
- **Decisive kill test.** Growth or boundedness in $n$ of $(K^2\mathbf 1)_j$ at corners and horizontal edges, and of ${\rm LF}_j$ at fixed $\Omega$.
- **HARD.** $K$ and $K^{(c)}$ of (2.4); the S9 shapes; every memory; the window $I_R$; $\Omega$ independent of $R$ in the fixed-confinement question.
- **FORBIDDEN.** Excluding edge or corner memories; per-memory recalibration of the window; truncating the kernel; fitting exponents to lattice data and calling them derived.
- **NO-GO SCOPE.** Every negative statement must state the model (quadratic or full), the order (perturbative coefficient or non-perturbative) and the quantifier (proof or finite witness).
- **Routes carried to construction.**
  - RT-A: order-by-order decision by column telescoping and summation by parts.
  - RT-B: the dielectric edge exponent of the uniaxial medium as the object behind the obstruction.
  - RT-C: re-typing of the fixed-confinement question into its optimal growth law.
- **Deferred route.** RT-D, a flip-local Lemma LOC-B by a path-space cluster expansion, was not constructed and makes no claim (Section 13.12).

The three rounds were used as follows:
1. the signed-kernel decision (Theorems DF and EL, Proposition W);
2. Lemma SRC, which transfers the second-order statement to the S9 source row, in response to referee finding F2;
3. verification, source collision and assessment.

### P.2 Corrections to v1.9 found during the v2.0 work

These findings were made by the generator during the v2.0 research. Finding F29-01 was confirmed numerically by the Section 8.15 referee. This is not a separate frozen audit of v1.9, and the v1.9 verdicts recorded in Appendix O are unchanged.

| ID | Severity | Defect in v1.9 | Integrated resolution |
|---|---|---|---|
| F29-01 | S1 | The remark after Lemma 4.3 states "numerically $\le2.92$ for $n\le16$" for the signed row sums without scope, and calls their uniform boundedness "the classical depolarization statement". The value holds on full cubes with $n\le16$ but not on partial S9 sets: already for $n\le16$ the values reach $2.932$ ($n=16$, $R=3969$) and $-3.334$ ($n=3$, $R=10$), and on partial sets with $n\le32$ they range over $[-3.334,3.071]$. No lattice proof was given | The remark now points to Theorem DF, which proves $-7.905\le h_S\le15.663$ on every S9 set, and to Theorem EL for the second iterate |
| F29-02 | S0 | Section 2.3 says "lexicographic order" without naming the fastest index. The verifier geometry uses the $e_z$ index as fastest, and Theorem DF needs this convention | Section 2.3 states the convention and its column consequences |
| F29-03 | S1 (meta) | Sections 8.14.7 and 13.11 name "a signed-kernel version of Lemma SR" as a candidate for removing $\widehat S_2$. The $n$-uniform signed $\ell^\infty$ input such a lemma needs fails at second order near horizontal edges | Section 8.14.7 and Section 13.11 point to Section 8.15, and Section 13.12 re-types the target. The BEFORE hypothesis of the v1.9 research record is refuted beyond first order |
| F29-04 | S0 | Theorem Q states $D_j^G\ge.98538$, while its proof derives $D_j^G\ge.9884$. Both are valid lower bounds, but the text does not say that the second implies the first | Clarified in the v2.0 note of Section 13.3 |
| F29-05 | S0 | In Section 3, $K$ denotes both the dipole kernel (2.4) and the entrywise Hessian majorant of Lemma SR | Section 3 states which meaning applies in Section 8.15 |

### P.3 Referee record for Section 8.15

A separate Claude agent instance, which did not write the material, reviewed Section 8.15 in two hostile passes. It was given the section, a context excerpt of the model (Sections 2.2, 2.3, 4.2–4.3, 13.3 and Appendix B) and an FFT helper, and it ran its own scripts.

The first pass found no error in the proofs of the formal results. It found one false remark and several overclaims.

| ID | Severity | Finding | Repair |
|---|---|---|---|
| F1 | S3 (no numbered result depends on it) | A remark on re-entrant corners of partial sets with a sector formula was false; the step of a partial S9 set is a straight edge at large scales | Remark deleted; partial sets described correctly; growth rate at the step labelled numerical |
| F2 | S2 | The transfer from the uniform drive to the S9 source row, needed for the Theorem Q statements, was not proved | Lemma SRC and Proposition LN(ii) added |
| F3 | S2 | "Every coefficient beyond the first is unbounded" was stated without proof | Restricted to the second coefficient; higher orders labelled numerical |
| F4 | S2 | "Only at horizontal edges and corners" was false literally; the logarithm is carried by a tube around the edges | "Near" edges; tube and off-edge supremum labelled numerical |
| F5 | S1 | The corner row of the EG evidence table was misleading (coefficient $\tfrac32$, falling local exponents) | Row removed; corner excluded as evidence |
| F6 | S1 | The corner case of Theorem EL was only sketched | Full proof written |
| F7 | S1 | The source-entry bound $10^{-6}\vert K_{0j}\vert$ in the proof of Corollary Q-prime was wrong by a factor of about 300 | Replaced by $4\times10^{-4}$; the result is unaffected |
| F8 | S1 | The framing claimed to decide the non-perturbative input, and "very probably grows" overstated the evidence | Hypothesis EG separated and labelled unproved; only the agreement of the coefficient is claimed |
| F9 | S1 | Theorem DF depends on an unstated filling convention | Stated in Sections 8.15 and 2.3 |
| F10–F13 | S0 | Arithmetic in Proposition LN; hypothesis of (8.Qp); the $E_*$ procedure; $\nu\ne0$ and the $\delta^3$ term in Proposition W | Repaired |
| F14 | S0 | Minor points: the regularization at second order, $\rho_{\rm tol}$ undefined, the NP-LOG edge term, context notes on Theorem Q and Lemma 4.3 | Repaired; the context notes became F29-01 and F29-04 |

The second pass judged F1–F13 repaired and F14 partial. It found the new material correct: the corner proof, Lemma SRC and Proposition LN(ii). Its numerical test of Lemma SRC gives $\max_j|(K^2\varphi)_j|\approx1.73$ at $n=96$, converging, on full and partial sets. Its remaining findings were presentational:
- N1: rigor details of the corner proof;
- N2: constants in Lemma SRC ($13\lambda_2$, near/far split for $B_2$);
- N3: the scope of the Proposition LN bullet;
- N4: the "artifact" sentence;
- N5: the $\delta_c$ bound, now $10^{-158}$;
- N6: arithmetic in Proposition LN;
- N7: qualification of the numerical growth statements;
- N8: Lemma SRC listed with non-explicit constants.

All were repaired in the text of Section 8.15. The partial F14 item, the NP-LOG edge term, is now interval-checked in row `DF-CONSTANTS` ($\le1.65\times10^{-14}$).

### P.4 Process disclosures

The generator coordinated both referee passes and the novelty sweep. It supplied the files and forwarded the revised section, but it did not edit the referee's reports. The referee used the model excerpt rather than the full manuscript. Referee, sweep and assessor are Claude instances of the same model family; qualified-human anchor: NONE. After the referee passes, the generator made three changes:
- it added the prior-art citations of Section 15.10 to Section 8.15;
- it reclassified two rows from C to V, because they use high-precision quadrature and root finding rather than interval arithmetic;
- it added the two interval checks in `DF-CONSTANTS` that are listed above.

None of these changes alters a stated result.

### P.5 Findings of the grade assessment and their repair

The separate-agent assessment (Section 16.1) reported six findings. It judged that none of them affects a numbered result. All six were repaired after the assessment, by narrowing or relabelling claims. No new result was added apart from the sketch in Remark EL-V, which is recorded as unreviewed and numerical.

| ID | Severity | Finding | Repair |
|---|---|---|---|
| A1 | S1 | "Bounded on vertical edges" was attributed to Theorem EL, which does not contain it | Recorded as Remark EL-V (numerical, with an unreviewed argument sketch). All attributions changed accordingly |
| A2 | S1 | $\Omega_0=O(\sqrt{\log R})$ was attributed to Corollary Q-prime, although (13.2) already implies it | Q-prime is now described as a constant improvement: the coefficient of $\log n$ in $\Omega_0^2$ drops from about $5.6\times10^5$ to $48$ |
| A3 | S1 | "If EG holds, fixed confinement fails" omitted the unproved transfer to the S9 source row | The transfer is now stated as an additional assumption everywhere. The readout step is made rigorous: in the quadratic model $D_j^G(t_*)\le\cos(\pi\rho/2)+2\varepsilon_Q$ |
| A4 | S0–S1 | "We decide whether …" and "present in the exact readout" overstated the result | "Order by order in the Neumann expansion"; "the $\Omega_0^{-4}$ Taylor coefficient of the exact source coefficient at horizontal edges and corners" |
| A5 | S0 | "Proposition W explains the failure" | Replaced by "has the same leading coefficient; this agreement suggests, but does not prove, …" |
| A6 | S0 | A Korean status label in Section 8.15 failed `ENGLISH-MATH-INTEGRITY`, and the census placeholder of Section 12.6 was unfilled | Label replaced by English. The census was filled from the final run |

End of the English-only integrated manuscript.

## Appendix Q. Frozen v2.0 audit and v2.1 correction register

**Frozen verdict: AUDIT-MAJOR-REVISION; highest severity S2. Grade 4 NOT ESTABLISHED.** Original hashes are in Section 1.4. The corrections do not retroactively change that verdict or rewrite the original release.

| ID | Severity | Frozen finding | Integrated disposition |
|---|---|---|---|
| F30-01 | S2 | Section 8.15.4 asserts an eventual central-time readout failure from a phase error, omitting the absolute value, the geometry factor and phase revivals | RETRACTED; WO replaces it with a rigorous whole-window conditional obstruction, Section 8.16.2 |
| F30-02 | S2 | Fixed-$\Omega$ EG asymptotics are used to infer a necessary/sharp varying-$\Omega$ law | RETRACTED as an implication; explicit quantifier counterexample in Section 8.16.3; uniformity and sufficiency debts stated |
| F30-03 | S2 | Section 13.12 says flip-local localization leaves only the Hessian condition at square-root-log confinement, omitting TC growth | Corrected census; the old majorant grows as $\ell^{5/4}$. RD-V removes the term and proves a comparator theorem, Sections 8.16.4–8.16.6 |
| F30-04 | S2 (scope) | “Under EG” and “at most first order” language suppresses the source-transfer premise and overstates what a second Taylor coefficient proves | Narrowed throughout current claims; actual source response isolated by SRX; nonperturbative methods are not ruled out |
| F30-05 | S1 / source gate | The requested Van Bladel, Mantič and Meixner 1972 original-text collision is unresolved | Access levels, related primary-text upgrade and exact missing mapping recorded in Section 15.11; no novelty clearance |
| F30-06 | S1 | Release-table wording gives the edge coefficient $2$ for corners as well, although EL assigns $3/2$ there | Current table states edge and corner constants separately; Proposition LN itself stated the coefficient at horizontal mid-edges correctly |
| F30-07 | S1 / qualification | Historical grade and provisional correctness cards risk being read as current adjudication | Current four-axis card and RESEARCH NOTE form added; old cards retained explicitly as history |

The substantive research routes were frozen before their new computations, used for three rounds and terminated with named unresolved obligations. No full-model fixed-confinement no-go theorem, EG proof, source-mode transfer theorem or external novelty proof was obtained. The package contains the route card, original-rerun output, new verification code/results, the Korean audit and research record, and the byte-preserving history extension.

## Appendix R. Frozen v2.1 audit and v2.2 correction register

**Frozen verdict on v2.1: AUDIT-PASS-MINOR; highest severity S1. META VERDICT: REPLAN.** Target: `ZS-M73_v2_1.md`, SHA-256 `1274abb2…6c0e`, release ZIP `6c9a3525…e39b`, 17 manifest entries matching. The audit was a FULL profile, cross-family: v2.1 was authored by Codex/GPT and audited by Claude with the v2.1 reports visible, so it was not blind.

**Reproduction.** The unchanged v2.1 driver returned 75/75 PASS (C23/V39/R12/G1) in 219 s under Python 3.11.15.

**Independent checks.**

- The SRX identity was recomputed by direct inversion inside the rerun.
- The inversion constant of Lemma WO was recomputed: $2\arccos(.9885)/(\pi\cdot.01\cdot.925)=10.447$.
- Lemma RD-V was re-derived: the characteristic-function bound and Efron–Stein.
- The comparator constant of COMP-SQRTLOG was reproduced to 13 digits by independently written code. Its all-$n$ claim on $[1+\log2,100]$ was certified by an interval covering rather than by the monotonicity regrouping.

No mathematical error was found in SRX, WO, RD-V or COMP-SQRTLOG.

**Meta audit.** The strategic question was whether the v2.1 audit–research cycle pursued the most important obstacle. It did not in one respect. It designated the growth of the LOC-B errors as the full-model bottleneck, without testing whether that growth was intrinsic. The coincidence threshold $\tfrac15$ was treated as a HARD fact, although nothing in the model fixes it. REPLAN: v2.2 tests the design choice directly (Section 8.17).

| ID | Severity | Frozen finding | v2.2 disposition |
|---|---|---|---|
| F31-01 | S1 (META) | The abstract, Section 8.16.6 ((8.LOC1)), Section 13.12 task 2 and Section 17 present the growth of the localization errors at sub-logarithmic laws as the full-model obstacle. It is a property of the fixed threshold of (8.LG1) | Tested and removed: Theorem NP-SQRTLOG (Section 8.17). A v2.2 note in Section 8.16.6; v2.1 text retained as record |
| F31-02 | S1 | The "exact sufficient remaining target" (8.FT1) includes the first-order flip difference. That difference carries label-independent phases and first-order terms multiplied by $T\lambda_e\asymp n^3$; the readout needs only mixed second differences. The implication is true, but the target is over-specified and was presented as the bottleneck | Annotated. For the growing-threshold comparator of v2.2 the analogous budget holds, since $2T\delta_3<10^{-102}$; for the fixed comparator it is not shown. Row `V22-AUDIT-FT1` |
| F31-03 | S0 | Section 8.14 uses $f'_{\max}\le172.09$ without proof. The true maximum is $\approx171.2$, so the value is correct | v2.2 proves $f'_{\max}<193.58$ by the Hermite bound for the new lemmas; the inherited value stands |
| F31-04 | S1 | Proof of Lemma LOC-B: $\lvert Z_s\rvert\le\sum_{\rm out}[f_c(0)N+y]$ uses $f_c(0)$ per partner, but $\lvert V_{ab}\rvert$ can reach $2f_c(0)-2$. The first term of $\zeta$ is understated by at most a factor 2 | Corrected to $2f_c(0)N$ (so $4f_c(0)N$ in $\zeta$) in Lemma LOC-B$_Y$. No effect on NP-LOG ($10^{-141}$ level). Row `V22-AUDIT-ZETA` |
| F31-05 | S1 (OPS) | Section 1.4 of v2.1 states that the separately supplied H-0409 file is an exact byte prefix. The project's current history copy differs from the ZIP copy in the H-0409 timestamp (20:03:56 versus 19:03:56 KST). The v2.1 statement concerned the file then supplied | Reported, not repaired. Both copies are preserved. The v2.2 history extends the project's latest file (H-0413) and records the conflict in H-0414 |

**Four axes of the frozen v2.1.**

- Correctness: PASS in its stated scope. No S2+ defect was found; the S1 items concern designation, a proof constant and provenance.
- Novelty: HOLD, as v2.1 itself stated.
- Significance: HOLD. The comparator-only result did not meet either user alternative.
- Verification basis: PASS for the executable scope.

Paper qualification: HOLD, RESEARCH NOTE. Research grade: UNASSESSED. These verdicts concern v2.1 as frozen; the research of v2.2 does not change them retroactively.

**Research after the freeze.** Two routes were run. Each was re-entered with a material change: a new comparator family, and a new method (compactness). The remaining budget for a third round was spent on the adversarial referee pass and on repairs.

1. *Growing threshold (full model).* The kill test was a growing certificate term at $\sqrt{\log}$ with $y_c\propto\ell^{1/4}$. The route passed: Theorem NP-SQRTLOG. The covering found one wrong intermediate bound ($C_h$), which was replaced (Section 8.17.3).
2. *Lattice-to-continuum compactness (source edge).* The kill test was a failure of operator convergence or of uniqueness. The route passed for the reduction (Theorem CR), and not for the continuum statement (EG-C open).

**Referee pass.** A separate Claude instance attacked Sections 8.17–8.18, reading the proofs and code and recomputing independently. It found no S2+ defect and eleven S0/S1 items, all integrated:

- the local proof of Lemma CR-1;
- the range of $f$ and a constant in Corollary CR-R;
- the one-way framing of Section 8.18;
- the tail bullets and row `V22-SQ-TAIL`;
- the wording of the $\sqrt{\log}$ limit;
- the source term in (8.SQ1) at small $n$;
- the source handling in Lemma LOC-A$_Y$;
- the non-tautological coincidence test;
- the exact fault crossings;
- notation.

Its independent evaluation matched the certificate to 12 digits at six values of $\ell$. It is the same model family as the author and is disclosed as such.

## Appendix S. Frozen v2.2 audit and v2.2.1 correction register

### S.1 Frozen verdict

**Frozen verdict on v2.2: AUDIT-PASS-MINOR; highest severity S1; TERMINAL-IN-SCOPE recommended.** The auditor was Codex/GPT, on 2026-09-24 (event `AUDIT-M73-v22-20260924`, 08:06:52 UTC). The target was `ZS-M73_v2_2.md`, 445,901 bytes, SHA-256 `324f4d48cc9c037a7999dc32ba372733cf97eddb29e8cc19e00f3cb4943e3998`, with release ZIP `80a13ed602f3c4e194c3709e10289fb7391e8b26d73133384c4b253cc3b42f08`; all 23 manifest entries matched. The audit applied Mission 1.7 (§§1.4, 5.6) and ZSPIN-RULES-2 minor 2.4 (KERNEL, AUDIT, VERIFY). It is cross-family but not blind, and the qualified-human anchor is NONE. The audit modified neither the manuscript nor the history (`history_mutation: false`). Its full Korean report, code and evidence are preserved byte for byte in `provenance/ZS-M73_v2_2_audit_evidence.zip` (SHA-256 `350fe4673aeb367c3c04a02fc1116a5cf3747d7d611acf78a7ef5b28e2bf3718`).

**Reproduction.** The unchanged v2.2 verifier returned 89 PASS, 0 FAIL, 0 SKIPPED (C25/V46/R16/G2) under Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0 and SymPy 1.12.

**Additional audit checks (seven, all PASS).**

- the unmodified rerun;
- an independent scalar re-implementation of the LOC chain, enclosed by the coded intervals at six values of $\ell$;
- the finite covering with the stated gate $.98853$, an exact start and the printed coefficient: minimum $.98853906777459937$, margin $9.0677746\times10^{-6}$;
- a gate-mutation witness;
- the branch-jump witness at $\ell=3906.25$;
- an exact-arithmetic polynomial check for the tail;
- a rounded tail budget.

The auditor's first diagnostic run failed on its own over-tight tolerance ($10^{-45}$ against constants computed to 40 digits). The corrected criterion, enclosure of the independent value, passed, and the failing JSON is preserved in the evidence ZIP.

### S.2 The audit's grade basis and its analytic tail

The audit's card is reproduced in Section 16.0S. Its main basis for grade 4 is the combination of three steps of the integrated paper. First, the earlier proofs needed polynomial confinement for the exact model (NP-P1, $R^{1/6}$), and NP-B proved a size barrier for routes that require global strong convexity. Second, for the exact, globally non-convex model under the same S9 geometry, P1 preparation, observable and growing window, NP-LOG reaches logarithmic confinement and NP-SQRTLOG then $\sqrt{\log R}$ confinement. Third, the comparator result COMP-SQRTLOG of v2.1 is transferred to the exact model by closing the energy, gap and state errors. The auditor does not recount NP-LOG as new in v2.2 and states that an increment-only assessment of 3, as in Section 16.0, is also defensible.

For $\ell\ge L=10^{15}$ the audit reconstructs the tail without sampled extrapolation (audit report, Appendix A). With $t=y_c$, $\ell=62500t^4$, $t>\tfrac12$ (no branch switch) and the conservative constants $\pi<3.14160$, $D_2<6018.03$, $f'_{\max}<193.58$, $f_c(0)<22.568$, it obtains

- $S\le33\ell$, $Y_0\le\ell$, $Y_1\le27\ell^{5/4}$, $Y_2\le17\ell$;
- $\widehat g_0\ge9999\sqrt\ell$, $\widehat\mu<10^{-9}$, $C_h^2\le20000\ell$ and $\theta(\tfrac12)<.000801$;
- $\widehat g_0(r_c-\mu_*)^2\ge22.1\ell$, $E_1\le4\ell^{3/2}e^{-22.1\ell}$, $\delta_3\le18\ell^{3/2}e^{-19.1\ell}$ and $2T\delta_3\le10^{18}\ell^{3/2}e^{-13.1\ell}<10^{-12}$;
- $r_{\rm SR}<6\times10^{-7}$, $r_1<10^{-12}$, $\mathcal Q<4.1\times10^{-5}$ and $L_{\rm pair}<.001302$;
- $D\ge\cos(\pi e_*/2)-.001302-1.71342(6\times10^{-7}+10^{-12})-2\times10^{-12}>.98854476310$.

These are the auditor's bounds. Row `V221-TAIL-AUDIT-REPRO` re-executes its constant checks; v2.2.1 does not re-derive its inequalities. The manuscript's own tail proof remains the list of Section 8.17.5, now restricted to $\ell\ge10^{15}$.

### S.3 Findings and dispositions

Correction types follow the manuscript rule's Correction Protocol: *Editorial* leaves the science unchanged; *Scope correction* changes a condition, quantifier or status.

| ID | Severity | Frozen finding | Type | v2.2.1 disposition | Rows |
|---|---|---|---|---|---|
| F32-01 | S1 | `V22-SQ-TAIL` was class C, although a monotonicity check at six points does not certify the infinite tail | Editorial (evidence class; the claim is unchanged) | Reclassified V in Section 12.8 and in the effective census (C24/V47/R16/G2 for v2.2). The tail proof is stated to be the analytic list of Section 8.17.5 | `V221-TAIL-SCOPE` |
| F32-02 | S1 | The certificate gate $.9885$ could pass values that fail the stated $.98853$. The start of the covering and the budget coefficient also differed from the text | Editorial (code–statement correspondence) | Section 8.17.5 note and table; Section 12.8; new certificate with the gate $.98853$, an exact start and the printed $1.71342$: minimum $>.98853906777$, margin at least $9.06\times10^{-6}$ | `V221-SQ-CERT-98853`, `V221-SQ-GATE-FAULT` |
| F32-03 | S1 | Section 8.17.5 claimed that every factor is nonincreasing for $\ell\ge\ell_*$; at $y_c=\tfrac12$ a branch of LOC-A$_Y$ switches and $\theta$ jumps up | Scope correction (the quantifier is narrowed to $\ell\ge10^{15}$) | Bullet and note in Section 8.17.5. The theorem is unaffected, because $[\ell_*,10^{15}]$ is covered by interval enclosures | `V221-BRANCH-JUMP`, `V221-TAIL-SCOPE` |
| F32-04 | S1 | The comparison for Lemma SR omitted Menz, arXiv:1402.5160, Theorem 2.3, Eq. (2.4), which already allows observables of several coordinates on finite-dimensional blocks; "multi-site observables" overstated the difference | Scope correction (the difference claim is narrowed) | Sections 8.14.3 and 15.9 and the references. The difference is limited to the transfer to the quantum ground-state resolvent and the application to the exact model. The audit found no subsumption of NP-SQRTLOG | source comparison (the statement of Theorem 2.3 and its label (2.4) were re-read in v2.2.1) |
| F32-05 | S0 | The old $\zeta$ and $f'_{\max}$ of Section 8.14 stand far from their corrections, and the margins above $.98853$ and $.9885$ were not separated | Editorial | Pointers in Section 8.14.2; note after the card of Section 16.0; Section 8.17.5 note | `V221-SQ-CERT-98853` |
| E-01 | S0 (found while correcting) | The release note of Section 16.0 says that the v2.2 census is in Section 12.8, but Section 12.8 lists only rows | Editorial | Census stated in Section 12.9 | — |

### S.4 Text changes

The register `v221/edit_register.json` lists all 24 edits. Each is anchored to a unique string of the v2.2 text. 20 are pure insertions at the character level; one of them (E19) changes a row's evidence class by its inserted words. The replacements remove only the fragments below, shown verbatim (⏎ marks a line break); each fragment's content is either restated in the new text or is the corrected error itself. The last column repeats the comparison at the level of whitespace-separated words. It also shows words that are kept at the character level but split by an insertion, or that gain attached punctuation or text; there, too, no content is lost. Row `V221-PRESERVATION` applies the register to v2.2 and reproduces this manuscript byte for byte, and applies it in reverse to reproduce v2.2 exactly.

| Edit | Finding | Location | Kind | v2.2 text removed (verbatim, character level) | v2.2 words not kept unchanged (word level) |
|---|---|---|---|---|---|
| E01 | release | title | insertion | — | `v2.2` |
| E02 | release | front matter, version line | insertion | — | `2.2,` |
| E03 | grade record | front matter, version line | insertion | — | — |
| E04 | release | front matter, release table | insertion | — | — |
| E05 | grade record | front matter, release table | insertion | — | `16.0:` |
| E06 | release | Section 1 (scope of changes) | insertion | — | — |
| E07 | F32-05 | Section 8.14.2, Lemma LOC-A | insertion | — | `$f'_{\max}=\max_\rho\|f_c'(\rho)\|\le172.09$.` |
| E08 | F32-05 | Section 8.14.2, Lemma LOC-B statement | insertion | — | — |
| E09 | F32-05 | Section 8.14.2, proof of Lemma LOC-B | insertion | — | `LOC-A.` |
| E10 | F32-04 | Section 8.14.3, after Lemma SR | replacement | ` for multi-site observables` | `analogue for multi-site observables,` |
| E11 | F32-04 | Section 15, references for Section 8.14 | insertion | — | — |
| E12 | F32-04 | Section 15.9, Lemma SR row | replacement | `, multi-site observables` | `multi-site observables,`; `known` |
| E13 | F32-03 | Section 8.17.5, tail list | replacement | `\ell_*` | `$\ell\ge\ell_*$`; `$\ell$:` |
| E14 | F32-01 | Section 8.17.5, row SQ-TAIL | insertion | — | — |
| E15 | F32-03 | Section 8.17.5, after the tail list | insertion | — | — |
| E16 | F32-02 | Section 8.17.5, certified table | insertion | — | — |
| E17 | F32-02 | Section 8.17.5, after the fault injections | insertion | — | — |
| E18 | F32-02 | Section 12.8, row V22-SQ-CERT | insertion | — | `coded` |
| E19 | F32-01 | Section 12.8, row V22-SQ-TAIL | insertion (the inserted words change the class from C to V; the original letter is kept in "emitted as C") | — | `8.17.5` |
| E20 | F32-01, F32-02 | Section 12.9 (new) | insertion | — | — |
| E21 | F32-05 | Section 16.0, heading | replacement | ` Current` | `Current` |
| E22 | F32-05, grade record | Section 16.0 (note) and Section 16.0S (new) | insertion | — | — |
| E23 | grade record | Section 17 | insertion | — | — |
| E24 | F32-01…05, grade record | Appendix S (new) | insertion | — | — |

### S.5 What did not change

- The statements and constants of every theorem, lemma and corollary, and their proofs, with two exceptions that leave the logic unchanged: in the proof of Theorem NP-SQRTLOG one quantifier of the tail step is narrowed and notes are inserted (E13–E17, F32-03 and F32-02), and the statements of Lemmas LOC-A and LOC-B carry inserted pointers (E07, E08, F32-05). The results include Theorem NP-SQRTLOG ($\Omega_R=10^4\sqrt{1+\log\lceil R^{1/3}\rceil}$, $D_j\ge.98853$), Theorem NP-LOG, Theorem COMP-SQRTLOG, Theorem CR and Corollary CR-R, and all inherited results.
- The covering itself: 7077 subintervals, the same ratios and regimes.
- The frozen v2.2 code in `v22/`, byte for byte, and every inherited row.
- Hypothesis EG-C (OPEN), the mission role (SUPPORT + METHOD, FQ2/RQ3), the physical bridges, and the card of Section 16.0.
- Every history row up to H-0414.

**Independence.** The corrections were made by Claude, the model family of the v2.2 author, following the Codex/GPT audit. v2.2.1 has not been re-audited (Section 16.0S), and the qualified-human anchor is NONE. No reserved code is assigned. No remote repository was changed and nothing was published externally.
