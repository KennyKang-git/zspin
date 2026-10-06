# ZS-M69 — Boundary-smeared qubit response: spatial regularity, oscillatory ultraviolet asymptotics, and controlled finite-time records

**Version:** v2.0 · **Date:** 2026-09-07 · **Programme:** Z-Spin · **Human author:** not assigned by this artifact; authorship and submission require the responsible researcher's review.

**Current form:** RESEARCH NOTE in research-paper format, prepared for an external research-grade audit. **PAPER QUALIFICATION: HOLD. TARGET GRADE: 3. RESEARCH GRADE: UNASSESSED for the central contribution.** This version supplies replacement proofs and a new, explicitly scoped mathematical synthesis. It does not award itself research grade 3. **OUTPUT ROLE: SUPPORT + METHOD; CORE: NO; RQ3: OPEN.**

The v1.9 artifact remains correctly recorded as **AUDIT-RESEARCH-REOPEN / highest S3 / PAPER QUALIFICATION FAIL**. The present version is a major research revision. The old version's verdict is neither overwritten nor treated as the verdict on this different artifact.

## 0. 한국어 연구 요약과 외부 감사 요청

v1.9 감사의 F01–F10을 전부 반영했다. 경계조건의 완전성, 임의 포락에서의 면적 하나로 결정되는 UV 법칙, 고정 운동량 부분계의 물리적 폐쇄, 적합 절편으로 얻은 시간창, 최소 폭의 전역 최적성, 에너지 문턱만으로 판단한 누설을 철회하거나 정확한 범위로 교체한다. 각 처분은 §10의 감사 대응표에 연결되어 있다.

이번 판본의 중심은 철회 목록에 머물지 않는다.

1. **정확한 공간 정칙성 조건(T2).** 정상화된 접선 밀도에 대해 광자 결합의 제곱적분가능성을 판정하는 조건은 밀도의 L²나 유한 유효면적과 동치가 아니다. 선언한 법선 포락 아래에서는 **밀도 ∈ H⁻¹ᐟ²**가 필요충분조건이다. 정상화는 되지만 이 조건을 만족하지 않는 예와, 이 조건은 만족하지만 밀도 L²는 아닌 예를 모두 구성한다.
2. **진동을 보존하는 UV 분해(T3).** 법선 근처의 방사와 접선 근처의 방사를 별도로 적분한다. 매끄러운 포락뿐 아니라 원판처럼 Fourier 꼬리가 계속 진동하고 영점도 갖는 경우를 포함한다. free/PEC에서는 꼬리 지수 3, PMC에서는 5가 두 기여의 경계가 된다. 세 모형의 접선 방사 계수가 같기 때문에, PMC를 택해도 공간 형상에 따라 기대한 두 차수의 개선이 사라질 수 있다.
3. **실제 유한시간 구간(T4–T6).** 공명점 근처의 대칭 이차 차분을 사용해 적합 없이 2차 응답의 오차를 제한한다. 여기에 진공 Bose 장에 대한 4차 이상 나머지의 상계를 결합한다. 따라서 선언된 정지 qubit–장 모형에서 **정확한 응답과 선형 신호의 상대오차가 지정한 δ보다 작은 구간**을 구성한다. Gaussian 예에서는 이 구간을 유리수 구간연산으로 인증한다.
4. **물리 연결의 구체화와 한계(T7–T8).** 운동량에 의존하는 band 전류의 gauge-invariant 행렬곱을 제시한다. 양의 에너지 edge→bulk+photon 채널에서는 접선 운동량까지 포함한 금지 정리를 증명한다. 그러나 이동하는 fermion 파속, 점유상태, 벌크 전류 행렬원소, Coulomb 항과 instrument까지 닫았다고 하지 않는다.

**다른 감사자가 우선 판단할 질문:** T2–T3의 공간·경계별 분류와 T4–T6의 결합이 최근접 선행연구의 통상적 특수화에 모두 포섭되는가, 아니면 정확하고 외부에서 재사용할 의미가 있는 추가 연구 기여인가? 특히 §9에서 공개한 Bingham–Goldie–Omey와 Liu–Lu의 강한 선행 결과를 대조해야 한다. ‘찾지 못함’과 검증행 수는 신규성의 근거로 쓰지 않는다.

## 1. Abstract and research question

A spatially extended qubit coupled to a free transverse field need not have an ultraviolet spectrum determined solely by its inverse participation area. We study a normalized tangential density combined with an exponentially localized normal density, first for three explicitly specified Maxwell mode families and then for a general integrable normal multiplier. We prove a necessary and sufficient negative-Sobolev regularity criterion for finite vacuum coupling norm. For radial tangential profiles, we obtain an additive high-frequency expansion that separates normal and grazing radiation and permits an oscillating tangential Fourier tail with zeros. The result identifies when changing the boundary mode family improves ultraviolet decay and when a common grazing contribution prevents that improvement. A frequency-domain second-difference bound controls the finite-time second-order response without fitting an asymptotic offset. A vacuum Dyson estimate then yields a nonempty parameter window in which the exact polarization is approximated by its secular coefficient with a prescribed relative error. We provide an exact-arithmetic Gaussian witness. These results concern declared stationary detector Hamiltonians. A momentum-resolved band-current tensor and an energy–momentum exclusion result clarify the additional work needed to apply them to the ZS-M67 carrier. Physical subsystem selection, fermionic occupation, moving-wavepacket dynamics and the measurement instrument remain open.

The precise question is: **which spatial regularity and spectral hypotheses are enough to predict ultraviolet behavior and certify a nonzero finite-time qubit polarization, and which of those statements survive a proposed boundary-carrier interpretation?**

This is a major revision of one paper code, not a new paper code. Existing finite-qubit results are retained in Appendices A–C with explicit assumptions and corrected scope. The old source and verifier are preserved as historical inputs in the accompanying package; their previous PASS counts do not certify the replacement theorems.

### 1.1 Contribution and dependency map

| Claim | Exact obligation | Mathematical status in this version | Novelty treatment | Evidence |
|---|---|---|---|---|
| T1 | Spectral matrix and three specified mode families | Proved under the declared field model | SPECIALIZED; no exhaustive boundary classification | §3; C01–C02, C24, V11, W23, W28 |
| T2 | Sharp H⁻¹ᐟ² criterion for vacuum coupling norm | Proved; necessity and sufficiency | Explicit spatial mapping; external novelty remains to be assessed | §4; C03, C06, V16, W17 |
| T3 | Normal-plus-grazing asymptotics with bounded uniformly continuous oscillating amplitude | Proved under stated tail hypotheses | Scope-specific extension compared with additive-tail methods; OPEN-NOVELTY | §5; C04–C06, V12, W13–W14, V15, W41 |
| T4 | All-time second-order remainder bound | Proved under a symmetric Dini condition | Quantitative specialization of approximate-identity analysis | §6; C07, V18, W19, V42 |
| T5 | Vacuum Dyson fourth-order error bound | Proved for the stated Fock Hamiltonian | Standard analytic-vector method; not presented as a new perturbation principle | §7; C08, V20, V42 |
| T6 | Exact-dynamics controlled window and rational witness | Proved for a stationary detector | Synthesis whose external significance/novelty needs audit | §7; C09–C10 |
| T7 | Momentum-resolved band-current tensor and nonclosure distinction | Algebra proved; physical kernel still open | SPECIALIZED Pauli-projector algebra | §8; C21, W22, C30 |
| T8 | Positive-band emission excluded with full planar momentum conservation | Proved for the stated free dispersions and channel | SPECIALIZED kinematics; not a discovery claim | §8; C25, V26, W27 |
| L1–L3 | Earlier collision, precession and matrix-analyser mathematics | Retained in explicit declared models | Specialist analysis; no automatic grade-3 credit | Appendices A–C; C31–C37, V32, W34, V35 |

“Proved” refers to the written arguments below. The executable ledger has **P=0**: it supplies exact subchecks, numerical cross-checks and counterexamples, not a formal proof object for every quantifier. No other AI or qualified human has audited the v2.0 proofs as part of this authoring task.

## 2. Definitions, model declaration and source freeze

We use natural units ℏ=c=1. Frequencies, the inverse normal length a, the gap h and the vacuum coupling norm have mass dimension 1; lengths and times have dimension −1. The coupling q is dimensionless. No value of q, a or the tangential profile is derived from an observation or selected to fit a Z-Spin numerical target.

Let ρ∈L¹(ℝ²) be a nonnegative tangential density with ∫ρ(x)d²x=1. It is a **declared stationary smearing density**, not automatically the transition density of a moving electron. Define

\[
\widehat\rho(p)=\int_{\mathbb R^2}\rho(x)e^{-ip\cdot x}\,d^2x,
\qquad \rho_a(z)=ae^{-az}\mathbf1_{z\ge0},\quad a>0. \tag{2.1}
\]

Thus |ρ̂|≤1, ρ̂ is continuous and ρ̂(0)=1. If ρ is radial, write g(p)=|ρ̂(p)|², p≥0. When ρ∈L², and only then within this definition, let

\[
0<A_{\rm eff}:=\left(\int\rho^2\right)^{-1}<\infty,
\qquad A_g:=\int_0^\infty p g(p)\,dp=\frac{2\pi}{A_{\rm eff}}. \tag{2.2}
\]

The second identity is radial Plancherel with the Fourier convention (2.1). Outside L², we do not insert the extended value A_eff=0 into a theorem requiring a positive finite area. A qubit state wavefunction ψ∈L², its density |ψ|²∈L², and the photon form factors f_a∈L² are three different conditions.

The **stationary detector** is a qubit with a fixed right-handed frame (e₁,e₂,e₃), Pauli operators σ₁,σ₂,σ₃, and

\[
H_S=\frac h2 n\cdot\sigma,
\quad h>0,\quad |n|=1,\quad \kappa=n\cdot e_3.
\tag{2.3}
\]

If |κ|<1, choose the tangential unit vector m along n_parallel and m_perp=e₃×m. At |κ|=1 any oriented tangential pair may be chosen. The field interaction and initial state are

\[
H(q)=H_S+H_F+q\sum_{a=1}^2\sigma_a\otimes\Phi(f_a),
\quad H_F=d\Gamma(\omega),\quad
\Phi(f)=a(f)+a^\dagger(f),\quad
\rho_0=\frac{I_2}{2}\otimes|0\rangle\langle0|.
\tag{2.4}
\]

Our convention for the form factors is fixed by

\[
\langle0|\Phi_a(t)\Phi_b(0)|0\rangle
 =\int_0^\infty\mathsf J_{ab}(\omega)e^{-i\omega t}\,d\omega,
\quad \mathsf J=\mathsf J^\dagger\succeq0,
\quad \|f_a\|^2=\int_0^\infty\mathsf J_{aa}(\omega)d\omega.
\tag{2.5}
\]

For finitely many modes Φ_a=Σ_j(λ_aj b_j+λ̄_aj b_j†), this means J_ab=Σ_jλ_ajλ̄_bjδ(ω−ω_j). **q² is outside J in all v2.0 formulas.** This removes a possible ambiguity with historical conventions in which the coupling was absorbed into J.

The observable controlled in T4–T6 is the **energy-axis polarization**

\[
R(T;q)=\operatorname{Tr}[(n\cdot\sigma)\rho_S(T;q)]. \tag{2.6}
\]

For n=±e₃ it is, up to that sign, the grading-axis record. For a tilted n, controlling R alone does not bound every component of the grading-axis signal: an additional perpendicular contribution must be included. Appendix C records the corresponding older second-order statement and its assumptions.

The spectral calculation uses a free Maxwell field in Coulomb gauge with the domain and modes explicitly selected below. It does not derive a gauge-invariant charged-fermion subsystem Hamiltonian from the Z-Spin action. In particular, this is an **explicit relaxation of M67 A4**, which excludes gauge backgrounds. M67 A2 constrains the spinor and does not select the Maxwell boundary domain. The qubit–Fock tensor factorization in (2.4) is declared here; K17/K18 are not solved by declaring it.

**Dependency freeze.** The immediate historical inputs are the uploaded `ZS-M69_v1_9.md`, SHA-256 `124135f325056ec711ba5f24e2b373ac1306effb5a37d8f09886a39d5209ab6a`, and the v1.9 audit report, SHA-256 `457801208802a100a45eddc925d9140d28361a69a77acc0cc1ab6deae6a3d554`. M67 v3.4.1 and S14 v2.1 were checked using the directly obtained text snapshots retained in the audit package. T1–T6 require no assertion that their models are physically selected by those upstream documents. The Constants/Lemmas and Debt/Retraction role indices were re-fetched; their available August snapshots do not include the later M67–M69 developments. Their silence is not evidence of novelty. The supplied Mission v1.6 and history through H-0321 provide the current project-side context. No remote SSOT or history is changed by this revision.

## 3. T1 — specified Maxwell mode families and the spectral matrix

### 3.1 Mode calculation and boundary scope

There are three **comparison models**, not a claim that only three boundary theories exist:

| Label | Normal tangential-field amplitude after smearing | B_a(k)=squared amplitude |
|---|---|---|
| free | a/(a−ik) | a²/(a²+k²) |
| PEC | √2 ak/(a²+k²) | 2a²k²/(a²+k²)² |
| PMC | √2 a²/(a²+k²) | 2a⁴/(a²+k²)² |

The amplitudes are the integrals of ρ_a against the full-space exponential and the normalized half-line sine/cosine modes. The √2 factors are essential when expressing the half-space result in the full-sphere convention used below.

For example, take tangential momentum along x, magnitude p, normal momentum k>0 and ω²=p²+k². The tangential TE amplitude lies along y. A TM mode has tangential amplitude k/ω along x. In the PEC family its x and z components are proportional to

\[
\left(\frac{k}{\omega}\sin kz,
\; i\frac{p}{\omega}\cos kz\right),
\]

and in the PMC family to

\[
\left(\frac{k}{\omega}\cos kz,
\; -i\frac{p}{\omega}\sin kz\right).
\]

Both satisfy ipA_x+∂_zA_z=0. Their tangential polarization sum is diag(k²/ω²,1), namely the tangential restriction of δ_ab−n_a n_b. This checks that the scalar sine/cosine smearing weight does not silently replace the tangential projector. The boundary labels refer to these perfect-conductor mode realizations and their specified gauge convention.

The Maxwell variation has a surface pairing involving F^{3a}δA_a. Its vanishing does not require all tangential components to make the same D/N choice. For any orthogonal projector P,

\[
P\delta A=0,\qquad(I-P)F^{3\parallel}=0
\quad\Longrightarrow\quad (F^{3\parallel})^T\delta A=0. \tag{3.1}
\]

Intermediate-rank P gives mixed conditions. Additional gauge, symmetry and operator-domain requirements would have to be stated and proved to exclude them. General boundary actions, Robin conditions supported by boundary terms, edge degrees of freedom and Chern–Simons terms are outside the three models. We do not use a model from those larger classes as a counterexample to a class that excludes it.

### 3.2 Theorem T1 (matrix spectrum, positivity and radial reduction)

For each of the three specified mode families,

\[
\boxed{\displaystyle
\mathsf J_{ab}(\omega)=\frac{\omega}{16\pi^3}
\int_{S^2}(\delta_{ab}-n_a n_b)
|\widehat\rho(\omega n_\parallel)|^2B_a(\omega n_3)\,d\Omega,
\qquad a,b\in\{1,2\}.}
\tag{3.2}
\]

Here the subscript on B_a denotes the inverse length parameter, not a matrix index. The matrix is real symmetric and positive definite for every ω>0. It need not be a scalar matrix. If ρ is radial,

\[
\mathsf J(\omega)=J_B(\omega)I_2,
\qquad
J_B(\omega)=\frac{\omega}{8\pi^2}
\int_0^1(1+u^2)g(\omega\sqrt{1-u^2})B_a(\omega u)\,du.
\tag{3.3}
\]

For a general normal multiplier B≥0, (3.2) defines a positive spectral model; strict positivity requires a positive-measure overlap with nonzero smearing. The strict statement just made holds for the three displayed B_a, not every possible multiplier.

**Proof.** The mode normalization d³k/[2(2π)³ω_k] and the polarization sum give (3.2) after the δ(ω−|k|) shell integral. Each integrand is positive semidefinite. Because ρ̂ is continuous and ρ̂(0)=1, it is bounded away from zero in some neighborhood of p=0. For any fixed ω>0, a sufficiently small cap around either normal direction lies in this neighborhood; there the tangential projector is positive definite, and the three B_a are strictly positive. The integral is therefore positive definite. This proof is independent of rotational symmetry. For a radial profile the azimuthal integral kills the off-diagonal entry and gives π(1+u²) for each diagonal entry; the two hemispheres give (3.3). ∎

Consequently every nonzero analyser vector has positive intensity at any h>0 in each comparison model. This is a quantified statement for those models, rather than an inference from sampled θ values. It does not close the question of which environment the action selects.

Continuity at zero and dominated convergence give the low-frequency laws

\[
J_{\rm free}\sim\frac{\omega}{6\pi^2},\qquad
J_{\rm PEC}\sim\frac{2\omega^3}{15\pi^2a^2},\qquad
J_{\rm PMC}\sim\frac{\omega}{3\pi^2}. \tag{3.4}
\]

Only normalization is needed for these leading coefficients. Normalization does not provide the ultraviolet hypotheses of the next sections.

## 4. T2 — the sharp spatial norm condition

Fix an arbitrary reference momentum μ>0. Define the inhomogeneous negative-Sobolev finiteness condition by

\[
\rho\in H^{-1/2}(\mathbb R^2)
\quad\Longleftrightarrow\quad
\int_{\mathbb R^2}\frac{|\widehat\rho(p)|^2}
{\sqrt{\mu^2+|p|^2}}\,d^2p<\infty.
\tag{4.1}
\]

Its finiteness is independent of μ. The definition does not require ρ to be an L² function.

### Theorem T2 (necessity and sufficiency)

Let ρ satisfy (2.1), and let B be an even, nonnegative, nonzero L¹(ℝ) function. Define J by (3.2) with B replacing B_a. Then

\[
\boxed{\displaystyle
\int_0^\infty\operatorname{tr}\mathsf J(\omega)\,d\omega<\infty
\quad\Longleftrightarrow\quad
\rho\in H^{-1/2}(\mathbb R^2).}
\tag{4.2}
\]

For radial ρ this is equivalent to ∫₁^∞g(p)dp<∞. For the three B_a, this condition also implies ∫₀^∞tr J(ω)/ω dω<∞. Hence the form factors in (2.4) have both the vacuum L² norm and the infrared weighted norm required by T5.

**Proof.** Tonelli's theorem applies even when the integrals are infinite. Undoing the shell integration in the trace gives

\[
\int_0^\infty\operatorname{tr}\mathsf J(\omega)d\omega
=\frac1{2(2\pi)^3}\int_{\mathbb R^2}d^2p\,|\widehat\rho(p)|^2
\int_{\mathbb R}dz\,
\frac{1+z^2/(|p|^2+z^2)}{\sqrt{|p|^2+z^2}}B(z).
\tag{4.3}
\]

The projector trace factor lies between 1 and 2. Write L=∫ℝB(z)dz, and choose R>0 with M_R=∫_{−R}^RB(z)dz>0. For p=|p|≥max(R,μ), the inner integral K_B(p) obeys

\[
\frac{M_R}{\sqrt2\,p}\le K_B(p)\le\frac{2L}{p}. \tag{4.4}
\]

The upper bound uses √(p²+z²)≥p; the lower bound restricts to |z|≤R. Thus the high-p contribution is finite exactly when the high-p part of (4.1) is finite. At small p, |ρ̂|≤1 and

\[
\int_0^{p_0}\frac{p\,dp}{\sqrt{p^2+z^2}}
=\sqrt{p_0^2+z^2}-|z|\le p_0.
\]

This bounds the remaining part of (4.3) by a constant times L. The radial statement follows from d²p=2πpdp. Finally, each B_a is bounded near zero, so (3.2) gives tr J(ω)=O(ω) in the infrared. Above ω=1, division by ω only decreases an L¹ integrand. ∎

For radial profiles the normalization in (4.3) specializes to

\[
\int_0^\infty J_B(\omega)d\omega
=\frac1{8\pi^2}\int_0^\infty p g(p)dp
\int_0^\infty
\frac{1+z^2/(p^2+z^2)}{\sqrt{p^2+z^2}}B(z)dz.
\tag{4.5}
\]

This is the formula used for the independent momentum-space mass check V16.

### 4.1 Constructed examples separating the three norms

For every β>0, the positive normalized density

\[
\rho_\beta(x)=\frac1{\Gamma(\beta/4)}
\int_0^\infty t^{\beta/4-1}e^{-t}
\frac{e^{-|x|^2/(4t)}}{4\pi t}\,dt
\tag{4.6}
\]

is a Gamma mixture of normalized two-dimensional Gaussians. Tonelli proves normalization. Its Fourier transform and squared modulus are

\[
\widehat\rho_\beta(p)=(1+p^2)^{-\beta/4},\qquad
 g_\beta(p)=(1+p^2)^{-\beta/2}. \tag{4.7}
\]

Therefore

| β range | ρβ normalized in L¹ | ρβ in L² | finite vacuum coupling norm |
|---|---|---|---|
| 0<β≤1 | YES | NO | NO |
| 1<β≤2 | YES | NO | YES |
| β>2 | YES | YES | YES |

These conclusions follow from the integrals ∫gβ(p)dp and ∫p gβ(p)dp, whose large-p powers differ by one. At β=1 the first diverges logarithmically; at β=2 the second does. At β=2, explicitly ρ₂(r)=e^{−r}/(2πr), so a singular normalized density can have a finite vacuum coupling norm while its density is not in L². This example is not asserted to have finite kinetic energy as an electron wavefunction.

For β>2, A_g=1/(β−2) and A_eff=2π(β−2). Conversely, normal localization alone does not suffice: tangential point sampling has g≡1 and fails (4.2). It is a distributional limiting comparison, not an L¹ density.

A Gaussian density ρ_ℓ=(2πℓ²)⁻¹exp(−r²/2ℓ²) has A_eff=4πℓ². Its point limit ℓ↓0 sends the area to **zero**; delocalization ℓ↑∞ sends it to infinity. Neither endpoint may be silently inserted into a theorem for a fixed normalized L¹ density with positive finite area.

## 5. T3 — normal and grazing ultraviolet contributions

### 5.1 A decomposition that keeps both ends of the radiation shell

For ω>0 put c=ω/√2. Changing coordinates in (3.3) gives the exact identity

\[
\begin{aligned}
J_B(\omega)&=J_B^N(\omega)+J_B^G(\omega),\\
J_B^N(\omega)&=\frac1{8\pi^2}\int_0^c
\frac pz\left(1+\frac{z^2}{\omega^2}\right)g(p)B(z)dp,
\quad z=\sqrt{\omega^2-p^2},\\
J_B^G(\omega)&=\frac1{8\pi^2}\int_0^c
\left(1+\frac{z^2}{\omega^2}\right)
 g(\sqrt{\omega^2-z^2})B(z)dz.
\end{aligned}\tag{5.1}
\]

N denotes the cap near the normal direction; G denotes the belt near grazing propagation. This partition is a mathematical device, not an additional physical cutoff.

### Theorem T3 (additive expansion, including oscillatory tails)

Assume B≥0 is integrable on [0,∞), is bounded on compact intervals, and

\[
B(z)=b z^{-s}+o(z^{-s}),\quad b>0,\quad s>1,
\qquad L_B=\int_0^\infty B(z)dz.
\tag{5.2}
\]

Let g≥0 be bounded on compact intervals and suppose, for some β>0,

\[
g(p)=p^{-\beta}\{H(p)+r(p)\},\qquad r(p)\to0,
\tag{5.3}
\]

where H is bounded, nonnegative and uniformly continuous on a terminal half-line. H is allowed to oscillate and vanish.

If β>2, A_g=∫₀^∞p g(p)dp<∞ and

\[
\boxed{\displaystyle
J_B(\omega)=
\frac{bA_g}{4\pi^2}\omega^{-(s+1)}
+\frac{L_B}{8\pi^2}H(\omega)\omega^{-\beta}
+o(\omega^{-(s+1)})+o(\omega^{-\beta}).}
\tag{5.4}
\]

If 0<β≤2, the cap is o(ω⁻β) and

\[
J_B(\omega)=\frac{L_B}{8\pi^2}H(\omega)\omega^{-\beta}
+o(\omega^{-\beta}). \tag{5.5}
\]

The two remainders in (5.4) refer to the two separately defined integrals in (5.1). This is an **absolute expansion**. It does not assert a relative error at zeros of H, nor does it determine the next surviving order along such a sequence.

**Proof.** On the normal cap, z≥ω/√2. For sufficiently large ω, (5.2) bounds B(z) by Cz⁻s throughout that cap. At each fixed p,

\[
\omega^{s+1}\frac pz
\left(1+\frac{z^2}{\omega^2}\right)B(z)
\longrightarrow 2bp.
\]

The integrand is bounded by a constant times p g(p). If β>2 this is integrable, so dominated convergence, with the indicator p≤ω/√2 included, gives

\[
\omega^{s+1}J_B^N(\omega)\longrightarrow\frac{bA_g}{4\pi^2}.
\tag{5.6}
\]

If 0<β<2, boundedness in (5.3) instead gives J_B^N=O(ω^{1−s−β})=o(ω⁻β). At β=2 the bound is O(ω^{−s−1}logω)=o(ω⁻²).

On the grazing belt p=√(ω²−z²)≥ω/√2. For each fixed z,

\[
\omega-p=\frac{z^2}{\omega+p}\to0,
\qquad (\omega/p)^\beta\to1.
\]

Uniform continuity gives H(p)−H(ω)→0 even though H(ω) itself need not converge. Subtract H(ω) inside the scaled belt integrand. The difference tends to zero for each fixed z and is bounded by CB(z), since p≥ω/√2 and H,r are bounded at large p. The omitted tail H(ω)∫_c^∞B tends to zero as well. Dominated convergence therefore gives

\[
\omega^\beta J_B^G(\omega)-\frac{L_B}{8\pi^2}H(\omega)\to0.
\tag{5.7}
\]

Combining the cap and belt statements proves (5.4)–(5.5). ∎

A rapidly decaying g is covered by H=0 and any β>s+1 for which g=o(p⁻β). Equation (5.4) then recovers a normal-cap law. Finite A_eff alone does not impose this tail condition.

### 5.2 Consequences for the three comparison models

Direct integration gives

\[
L_{\rm free}=L_{\rm PEC}=L_{\rm PMC}=\frac{\pi a}{2},
\quad (b,s)=(a^2,2),(2a^2,2),(2a^4,4).
\tag{5.8}
\]

Thus their grazing term has the **same coefficient** aH(ω)/(16π). For a nonoscillatory tail H(ω)→C>0, the leading powers are:

| Tangential tail exponent | free | PEC | PMC |
|---|---|---|---|
| 0<β<3 | β | β | β |
| β=3 | 3; both terms contribute | 3; both terms contribute | 3; grazing term |
| 3<β<5 | 3 | 3 | β |
| β=5 | 3 | 3 | 5; both terms contribute |
| β>5, including sufficiently rapid decay | 3 | 3 | 5 |

The entries mean J∼constant·ω⁻exponent under C>0; β≤1 also fails the finite-norm criterion for this nonoscillatory family. Oscillatory profiles are governed by (5.4), not by a blanket two-sided power estimate at every frequency.

When the normal cap dominates and ρ∈L², (5.4) yields the familiar-looking coefficients

\[
J_{\rm free}\sim\frac{a^2}{2\pi A_{\rm eff}\omega^3},\quad
J_{\rm PEC}\sim\frac{a^2}{\pi A_{\rm eff}\omega^3},\quad
J_{\rm PMC}\sim\frac{a^4}{\pi A_{\rm eff}\omega^5}.
\tag{5.9}
\]

Their hypotheses are now explicit: for example, g=o(p⁻³) with a suitable bounded tail envelope suffices for the first two, and g=o(p⁻⁵) for the third within T3. They are not laws for every finite-area density.

### 5.3 A compact-edge family and the audited counterexamples

For ν>−1 set

\[
\rho_\nu(r)=\frac{\nu+1}{\pi}(1-r^2)^\nu\mathbf1_{r<1}.
\tag{5.10}
\]

This is normalized. Integrating the J₀ power series term by term against r(1−r²)^ν and using the beta integral gives

\[
\widehat\rho_\nu(p)
=2^{\nu+1}\Gamma(\nu+2)\frac{J_{\nu+1}(p)}{p^{\nu+1}}.
\tag{5.11}
\]

The standard large-argument Bessel expansion, [DLMF §10.17(i), Eq. 10.17.3](https://dlmf.nist.gov/10.17#E3), gives (5.3) with

\[
\beta=2\nu+3,
\quad H(p)=\frac{2^{2\nu+3}\Gamma(\nu+2)^2}{\pi}
\cos^2\!\left(p-\frac{\pi(\nu+1)}2-\frac\pi4\right).
\tag{5.12}
\]

For ν>−1/2, A_eff=π(2ν+1)/(ν+1)² and A_g=2(ν+1)²/(2ν+1). All ν>−1 have β>1 and therefore finite coupling norm by T2, including part of the family outside density L².

For the **uniform disk**, ν=0, a=1, T3 yields

\[
\begin{aligned}
\omega^3J_{\rm free}(\omega)&=
\frac{1+\cos^2(\omega-3\pi/4)}{2\pi^2}+o(1),\\
\omega^3J_{\rm PEC}(\omega)&=
\frac{2+\cos^2(\omega-3\pi/4)}{2\pi^2}+o(1),\\
\omega^3J_{\rm PMC}(\omega)&=
\frac{\cos^2(\omega-3\pi/4)}{2\pi^2}+o(1).
\end{aligned}\tag{5.13}
\]

The first coefficient has two different subsequential limits; finite area A_eff=π does not rescue the v1.9 universal constant. The third formula does not assert ω⁻⁵ behavior at the zeros of its leading term.

For the **continuous cap**, ν=1/2, A_eff=8π/9 and g(p)=9(sinp−pcosp)²/p⁶. In the PMC model,

\[
\omega^4J_{\rm PMC}(\omega)=\frac9{16\pi}\cos^2\omega+o(1).
\tag{5.14}
\]

Thus continuity of the density is not enough for the purported universal PMC exponent 5.

### 5.4 Assumption ablation and scope

Uniform continuity of H cannot be dropped from the proof. For the nonnegative spectral multiplier

\[
g(p)=(1+p^2)^{-3/4}\frac{1+\tfrac12\cos p^2}{3/2},
\]

the phase difference along the grazing belt is p²−ω²=−z², which does not tend to zero for fixed z. Along ω_n²=2πn, the scaled grazing coefficient is

\[
\frac1{8\pi^2}\int_0^\infty B(z)
\frac{1+\tfrac12\cos z^2}{3/2}\,dz,
\]

strictly below L_B/(8π²) for the displayed positive B. W41 evaluates the gap. This is an ablation within T3's general class of nonnegative spectral multipliers; we do not assert that this particular g is the squared Fourier transform of a nonnegative real-space density.

T3 does not cover arbitrary anisotropic tails, nonintegrable B, a point-supported transverse density, or a frequency-dependent boundary action unless its actual kernel satisfies the assumptions. These are precise boundaries of the theorem, not unexamined universal extensions.

## 6. T4 — A finite-time estimate from local spectral regularity

### 6.1 Matrix spectrum and the two transition orientations

Choose an oriented orthonormal frame (e₁,e₂,n) around the energy axis. If n=(√(1−κ²),0,κ), take e₁=(κ,0,−√(1−κ²)) and e₂=(0,1,0). The two tangential components of e₁+ie₂ form u_κ=(κ,i)ᵀ. For a general azimuth rotate both components by the same real planar rotation. Put

\[
 f_-(\omega)=u_\kappa^\dagger J(\omega)u_\kappa,
 \qquad f_+(\omega)=u_\kappa^T J(\omega)\overline{u_\kappa}.
\tag{6.1}
\]

Both are nonnegative. They coincide for the real symmetric matrices of §3, but need not coincide for a complex Hermitian spectrum. Replacing both by a single contraction in that general case would give an incorrect counter-rotating term. Longitudinal matrix elements change no energy-axis polarization at this order from the maximally mixed qubit.

For T≥0 define

\[
 F_T(x)=\frac{1-\cos(xT)}{x^2},\quad F_T(0)=\frac{T^2}{2}.
\tag{6.2}
\]

Its full-line integral is πT. A direct second-order expansion, or a sum of the two transition probabilities starting with equal level populations, gives

\[
 R_2(T;q)=-2q^2\int_0^\infty
 \{f_-(\omega)F_T(h-\omega)-f_+(\omega)F_T(h+\omega)\}\,d\omega.
\tag{6.3}
\]

The downward vacuum transition has squared amplitude f₋ and raises the ground-state population, explaining the minus sign in R. The upward counter-rotating vacuum transition has squared amplitude f₊. Each time integral squared is 2F_T. The initial population 1/2 and polarization change 2 yield (6.3). This derivation fixes the normalization independently of a late-time rate approximation. V42 compares both orientations with direct finite-mode propagation, including complex off-diagonal spectra and negative κ.

### 6.2 The bounded-remainder theorem

**T4.** Let h>0, f₋,f₊∈L¹(0,∞) be nonnegative, and let f₋ have a representative with f_h=f₋(h)>0. Suppose its symmetric second difference obeys

\[
 D_h=\int_0^h\frac{|f_-(h+x)+f_-(h-x)-2f_h|}{x^2}\,dx<\infty.
\tag{6.4}
\]

Endpoint values at x=h are irrelevant. Define the finite constant

\[
 E_h=2D_h+2\int_h^\infty\frac{f_-(h+x)}{x^2}\,dx
       +\frac{4f_h}{h}
       +2\int_0^\infty\frac{f_+(\omega)}{(h+\omega)^2}\,d\omega.
\tag{6.5}
\]

Then for every T≥0,

\[
 \boxed{|R_2(T;q)+2\pi q^2f_hT|\le 2q^2E_h.}
\tag{6.6}
\]

**Proof.** Write A=∫₀∞f₋(ω)F_T(h−ω)dω. Pair the positive and negative frequency offsets up to h, and use ∫ℝF_T=πT:

\[
 A-\pi T f_h=
 \int_0^h[f_-(h+x)+f_-(h-x)-2f_h]F_T(x)dx
 +\int_h^\infty[f_-(h+x)-2f_h]F_T(x)dx.
\tag{6.7}
\]

The first absolute value is ≤2D_h since 0≤F_T(x)≤2/x². The second is at most 2∫_h∞f₋(h+x)/x²dx+4f_h/h. The counter-rotating integral is bounded by 2∫₀∞f₊(ω)/(h+ω)²dω. Substitute in (6.3). All integrals at infinity converge by L¹ and h>0. □

Local C¹,α regularity for any α>0 is sufficient for (6.4): the linear terms cancel and the second difference is O(x¹⁺ᵅ). A C² bound |f₋″|≤M₂ on [0,2h] gives D_h≤M₂h. C² regularity is convenient, not necessary. The Gaussian spectra in §7 satisfy it by differentiation of a compact angular integral.

Mere L¹ integrability, even together with continuity at h, is insufficient for a bounded offset. A compactly supported spectrum agreeing with 1+√|ω−h| near h has an additional resonant integral proportional to √T. In (6.7), the cusp contributes a positive multiple of

\[
 \sqrt T\int_0^{hT}(1-\cos y)y^{-3/2}dy,
\]

whose integral tends to √(2π). With a symmetric cusp of unit coefficient the resulting R₂ correction is −4q²√(2πT)+O(q²). W19 checks this behavior. The defect is local spectral regularity, not failure of the spatial coupling norm. Fitting a constant to a few large times cannot repair it.

The bound does not assume an absolutely integrable first time moment of a response kernel. It also does not guarantee a nonzero *exact* response by itself: a bound on terms beyond second order is still required.

## 7. T5–T6 — From a response coefficient to a controlled exact record

### 7.1 Hamiltonian domain and vacuum Dyson expansion

Consider a finite-dimensional system with bounded H_s and

\[
 H(q)=H_s\otimes I+I\otimes d\Gamma(\omega)
       +q\sum_{a=1}^{d}S_a\otimes\Phi(f_a),
 \qquad \Phi(f)=a(f)+a^\dagger(f),\quad\|S_a\|\le1.
\tag{7.1}
\]

Here d is finite, the one-particle multiplication operator ω is nonnegative, f_a and f_a/√ω belong to the one-particle Hilbert space, and

\[
 F=\sum_{a=1}^d\|f_a\|<\infty.
\tag{7.2}
\]

The notation Φ(f) fixes the creation/annihilation convention; complex coefficients in a mode expansion obey the Hermitian relation used in §2. The field estimate

\[
 \|a(f)\psi\|\le\|f/\sqrt\omega\|\,
       \|d\Gamma(\omega)^{1/2}\psi\|,
\quad
 \|a^\dagger(f)\psi\|\le\|f/\sqrt\omega\|\,
       \|d\Gamma(\omega)^{1/2}\psi\|+\|f\|\,\|\psi\|
\tag{7.3}
\]

makes the interaction infinitesimally bounded relative to the free Hamiltonian. Kato–Rellich therefore supplies a self-adjoint, bounded-below H(q) on the free domain. This is standard Pauli–Fierz analysis; compare Dereziński–Jakšić, Proposition 5.2 [R3], accounting for their field normalization. No positive photon mass gap is imposed here. For the three spectra of §3, T2 controls ∫trJ, and their infrared O(ω) behavior also controls ∫trJ/ω; these are the two different norms required by (7.3).

**T5.** Start with any system density matrix and the field vacuum. Let O be a bounded system observable with ||O||≤1 whose free-time expectation is R₀(T). If the vacuum parity leaves the initial state and O invariant, all odd powers of q vanish. For

\[
 y=2\sqrt2\,|q|FT\le1,
\tag{7.4}
\]

the exact expectation satisfies

\[
 \boxed{|R_{\rm exact}(T;q)-R_0(T)-R_2(T;q)|
       \le64q^4F^4T^4.}
\tag{7.5}
\]

R₂ denotes the full second-order coefficient multiplied by q², not an independently Markov-approximated expression. In the application O=n·σ and the system input I/2, R₀=0 and R₂ is (6.3).

**Proof, including convergence.** Purify the system state using a finite ancillary space on which the Hamiltonian is the identity. Interaction-picture fields preserve their one-particle norms. A vector with at most j photons obeys

\[
 \Big\|\sum_a S_a(t)\Phi(f_a(t))\psi\Big\|
 \le 2F\sqrt{j+1}\,\|\psi\|.
\]

Consequently the norm of the order-n vacuum Dyson vector, including qⁿ and its time simplex, is at most (2|q|FT)ⁿ/√n!. The sum converges for every finite T and q. This estimate can first be applied with a frequency cutoff ω∈[1/N,N] and a photon-number cutoff L. These give bounded interactions. It is uniform in N and L, since projection does not increase the one-particle norm or the displayed ladder bounds. For a fixed order n, the particle cutoff becomes irrelevant once L≥n. Frequency cutoff convergence follows from f_{a,N}→f_a in both ordinary and ω⁻¹-weighted L². The field estimate (7.3) gives convergence of the Hamiltonians on the free finite-particle energy core, hence strong resolvent convergence and strong convergence of their unitary groups at fixed time. Removing the particle cutoffs on the same core and using the uniform summable vacuum-series tails identifies the convergent Dyson series with the exact vacuum evolution. Thus a finite oscillator truncation is not being substituted for the continuum argument.

Let x=2|q|FT. For total degree n in the bra–ket expectation, the sum of bounds is

\[
 x^n\sum_{j=0}^n\frac1{\sqrt{j!(n-j)!}}
 \le x^n\sqrt{\frac{(n+1)2^n}{n!}}
 =y^n\sqrt{\frac{n+1}{n!}}.
\tag{7.6}
\]

This is Cauchy–Schwarz and ∑_j binom(n,j)=2ⁿ. Field parity sends q to −q while fixing the initial state and O, so odd total degrees vanish exactly. For even n≥4 the ratio of consecutive even majorants is

\[
 y^2\sqrt{\frac{n+3}{(n+1)^2(n+2)}}\le\frac14\qquad(y\le1).
\]

The first is √(5/24)y⁴<y⁴/2, so their sum is <(2/3)y⁴≤y⁴. Since y⁴=64q⁴F⁴T⁴, (7.5) follows. C08 checks the polynomial inequality in n; the sum, domain argument and all-time quantifiers reside in this proof. □

This is a deliberately conservative analytic-vector bound. General Dyson/Wick error estimates for harmonic baths predate this paper; Liu–Lu [R4] is a particularly relevant comparison. We claim neither optimal constants nor a new principle for controlling Dyson expansions.

### 7.2 Controlled-window theorem

**T6.** In the stationary qubit model, suppose T4 and T5 hold with f_h>0 and F>0. Then, whenever y≤1,

\[
 \frac{|R_{\rm exact}(T;q)+2\pi q^2f_hT|}
 {2\pi q^2f_hT}
 \le \frac{E_h}{\pi f_hT}
       +\frac{32q^2F^4T^3}{\pi f_h}.
\tag{7.7}
\]

For any prescribed 0<δ<1, the sufficient conditions

\[
 T\ge T_{\min}=\frac{2E_h}{\delta\pi f_h},
\qquad
 0<|q|\le\min\left\{
 \frac1{2\sqrt2FT},
 \sqrt{\frac{\delta\pi f_h}{64F^4T^3}}
 \right\}
\tag{7.8}
\]

make the relative error at most δ and imply R_exact<0. Equivalently, at fixed q the certified time interval is

\[
 T\in\left[T_{\min},\,
 \min\left\{\frac1{2\sqrt2|q|F},
 \left(\frac{\delta\pi f_h}{64q^2F^4}\right)^{1/3}\right\}\right]
\tag{7.9}
\]

provided the upper endpoint is at least T_min. This interval is nonempty for sufficiently small nonzero |q|. The claim follows by adding the two error bounds and dividing by the positive secular signal. No limit T→∞ at fixed q is taken. □

The statement concerns energy-axis polarization. For n=±e₃, the grading-axis record is R_J=±R_exact and is also nonzero. For tilted n, R_J=κR_exact+e₃·r_perp. Controlling only R_exact does not rule out cancellation by r_perp. An additional perpendicular-response bound is needed before promoting (7.7) to a grading-record certificate in that case. Neither case constructs a POVM, an instrument, an outcome record or a Born-rule derivation.

### 7.3 A rationally certified continuum example

Set a=h=ℓ=1 in the free branch, use the normalized Gaussian ρ(x)=(2π)⁻¹e^{−|x|²/2}, and align n=e₃. Here f₋=f₊=2J and I=∫₀∞J(ω)dω. The momentum formula of §4 and 1+z²/(p²+z²)≤2 give

\[
 I\le\frac1{4\pi^2}\int_0^\infty e^{-p^2}dp
              \int_0^\infty\frac{dz}{1+z^2}
   =\frac1{16\sqrt\pi}.
\tag{7.10}
\]

There are two field components, each of norm √I. Thus F=2√I and F⁴≤1/(16π). The angular formula also gives

\[
 \frac{e^{-1}}{6\pi^2}\le f_h\le\frac1{3\pi^2},
 \qquad \|f\|_1\le\frac1{8\sqrt\pi}.
\tag{7.11}
\]

For the lower bound use e^{−(1−u²)}≥e⁻¹ and 1/(1+u²)≥1/2 in the angular integral, retaining ∫₀¹(1+u²)du=4/3. This is intentionally loose. For 0≤ω≤2 the differentiated integrand has |f″(ω)|≤M₂=100/(3π²). One elementary derivation writes P(ω,u)=e^{−ω²(1−u²)}B(ωu). Uniformly, |B|≤1, |∂ωB|≤2, |∂ω²B|≤10, |∂ω e^{−ω²(1−u²)}|≤4 and |∂ω² e^{−ω²(1−u²)}|≤18. Hence |P′|≤6 and |P″|≤44; differentiating ωP and integrating gives the stated M₂. C10 records these inequalities.

Equation (6.5) is therefore bounded without oscillatory numerical integration by

\[
 E_h\le 2M_2+4\|f\|_1+4f_h\le 7.171935280.
\tag{7.12}
\]

Choose **T=1600, q=1/2,000,000 and δ=1/2**. The verifier constructs rational lower and upper bounds on π using Machin's identity π=16 arctan(1/5)−4 arctan(1/239), with alternating-series enclosures of 40 and 12 terms. It encloses e⁻¹ by an alternating Taylor sum and √π by integer square roots. All comparisons establishing the following bounds are exact `Fraction` operations; the displayed decimals are rounded outward:

| Quantity | Certified bound |
|---|---:|
| E_h/(πf_hT) | < 0.229675 |
| 32q²F⁴T³/(πf_h) | < 0.033403 |
| Sum, bounding the exact relative error | **< 0.263077 < 0.5** |
| y² | < 0.000000723 |

Thus this is a continuum exact-dynamics witness, not a fit of R₂ and not a finite-mode approximation used as a proof. Its small q and long T are a mathematical existence choice. It supplies no prediction that a Z-Spin carrier realizes these parameters, and no claim of an experimentally resolvable absolute signal. C09 outputs a positive rational lower bound on −R_exact as well as the relative-error bounds. Altering q above the certified ceiling invalidates this certificate; it does not prove that the exact response itself disappears.

## 8. Physical bridge: what a boundary carrier would actually require

### 8.1 T7 — Momentum-dependent band vertices

In an oriented boundary Pauli frame, let the declared one-particle edge Hamiltonian be

\[
 H_{\rm edge}(k)=k_x\sigma_x+k_y\sigma_y+M\sigma_z,
 \quad E(k)=\sqrt{|k|^2+M^2},
 \quad P_s(k)=\tfrac12[I+s\,d(k)\cdot\sigma/E(k)].
\tag{8.1}
\]

This is the M67-type free dispersion used for the bridge test, not a derivation of the full interacting action. For E(k)>0, choose local normalized eigenvectors U_s(k). A plane-wave photon with planar momentum p changes k to k′=k+p. A projected current vertex has the structure

\[
 V_a(s',k';s,k;k_3)=qF_a(k_3)\,
 \delta^{(2)}(k'-k-p)\,U_{s'}(k')^\dagger\Gamma_aU_s(k).
\tag{8.2}
\]

The overall continuum delta normalization follows the chosen plane-wave convention; (8.2) exhibits its support and spinor dependence. The free normal smearing factor is a/(a−ik₃), and the other declared mode families use the amplitudes in §3.1. The carrier matrices Γ_a are fixed in the atlas frame; their matrix elements between band eigenvectors are not fixed as k varies.

For Γ_a=σ_a, a phase-independent product is available. Let v=s d(k)/E(k) and u=s′d(k′)/E(k′). Pauli multiplication gives

\[
 \boxed{\operatorname{tr}[P_{s'}(k')\sigma_aP_s(k)\sigma_b]
 =\tfrac12\{(1-u\cdot v)\delta_{ab}
       +u_av_b+u_bv_a+i\epsilon_{abc}(u_c-v_c)\}.}
\tag{8.3}
\]

**Proof.** Expand both projectors. The two-Pauli trace is 2δ_ab, the three-Pauli trace 2iε_abc, and the four-Pauli trace is 2(δ_iaδ_jb−δ_ijδ_ab+δ_ibδ_aj). Collecting the four terms gives (8.3). C21 checks all nine components symbolically for independent u,v; normalization of Bloch vectors is not needed for that algebraic identity. For normalized pure bands it is exactly the product of transition matrix elements, and therefore independent of the separate band-vector phases. □

This tensor is a concrete replacement for calling a fixed Pauli vertex an exact moving-band vertex. To obtain the bath spectrum for a wavepacket one must integrate products of (8.2) with its momentum amplitudes, the photon modes, time-dependent band phases and the occupied fermionic state. The scalar |ρ̂(p)|² of §§3–7 cannot generally absorb all these factors.

### 8.2 Projection, packet spreading and the unresolved carrier model

A compressed Hamiltonian PHP generates a closed subsystem only when QHP=0, with Q=I−P, or when an explicit approximation bounds the omitted dynamics. Photon momentum transfer violates invariance of a fixed-k subspace. For example p=3 maps k=2 to k′=5. This is not repaired by evaluating a vertex at the central momentum. Nor does zero group velocity at a band minimum imply a stationary packet.

For M>0, the quadratic band-bottom approximation E(k)=M+|k|²/(2M) and the normalized momentum density |ψ(k)|²=(ℓ²/π)e^{−ℓ²|k|²} give the demodulated overlap

\[
 C(T)=\int |\psi(k)|^2e^{-i|k|^2T/(2M)}d^2k
      =\left(1+\frac{iT}{2M\ell^2}\right)^{-1}.
\tag{8.4}
\]

It has a finite scale Mℓ² although ∇E(0)=0. Equation (8.4) is exact for the quadratic dispersion, not for the full relativistic band at arbitrary momenta. C30 checks the integral; W22 checks momentum dependence and nonclosure. The old packet-width objective is not globally monotone even in its algebraic surrogate (W29); this version asserts neither a global optimum nor that the smallest admitted width is optimal.

A valid moving-carrier extension of T6 must specify its initial fermionic state, prove a uniform packet/recoil error on the same interval, bound edge–bulk couplings and Coulomb contributions, and propagate all those errors to the intended record. This is an explicit open proof obligation. The stationary detector results remain meaningful as a SUPPORT/METHOD result independently of its eventual success.

### 8.3 T8 — A precisely scoped energy–momentum exclusion

Let the bulk mass satisfy m>|M|. Consider only a transition from a **positive-energy** edge particle with momentum k to a **positive-energy** bulk particle plus one emitted vacuum photon. Assume planar translation invariance and the free dispersions

\[
 E_b(k)=\sqrt{|k|^2+M^2},\quad
 E_{\rm bulk}=\sqrt{|k-p|^2+m^2+k_{zb}^2},\quad
 \omega=\sqrt{|p|^2+k_{z\gamma}^2}.
\tag{8.5}
\]

Then this channel cannot conserve energy for any k,p,k_zb,k_zγ:

\[
 E_{\rm bulk}+\omega
 \ge\sqrt{|k-p|^2+m^2}+|p|
 \ge\sqrt{|k|^2+m^2}
 >E_b(k).
\tag{8.6}
\]

**Proof.** The first inequality drops nonnegative normal momenta. The second is the Euclidean triangle inequality for (k−p,m)+(p,0)=(k,m). The last is strict because m>|M|. □

Thus E_b=m is not an opening threshold for this channel. The older E_b<m test was only a sufficient energy-only exclusion. When M≠0, κ=M/E_b gives the correct signed statement

\[
 E_b<m\ \Longleftrightarrow\ |k|<\sqrt{m^2-M^2}
 \ \Longleftrightarrow\ |\kappa|>|M|/m.
\tag{8.7}
\]

The κ=0, M=0, E_b=0 corner needs its own gapless treatment; dividing by M or applying T4 with h=0 is invalid.

An on-shell exclusion is not an invariant-subspace theorem. A finite-time first-order transition amplitude has a probability contribution of the form

\[
 4q^2\int |V(\lambda)|^2
 \frac{\sin^2[\Delta(\lambda)T/2]}{\Delta(\lambda)^2}\,d\lambda.
\tag{8.8}
\]

It can be nonzero for every energy mismatch Δ≠0. On an initial planar momentum support |k|≤K, this channel has

\[
 \Delta\ge\Delta_K=\sqrt{K^2+m^2}-\sqrt{K^2+M^2}>0.
\]

The monotonic decrease of the displayed difference with |k| establishes the uniform lower bound. If the actual vertex is square integrable, (8.8) is at most 4q²||V||²/Δ_K². No bulk-vertex norm has been evaluated in this paper; the bound is conditional and concerns only the leading transition term. Occupied negative bands, thermal absorption, many-body processes, broken planar translation symmetry and modified dispersions are outside T8. W27 explicitly preserves a nonzero off-shell finite-time example rather than incorrectly declaring P invariant.

## 9. Prior-art confrontation and the research-grade question

### 9.1 Closest mathematical, methodological and physical baselines

The following comparison separates statements read in the source from our inference about their relation to this paper. It is not a claim that a literature search proves absence. Source access and searches were performed on 2026-09-07. The search axes included spatial smearing and spin-boson form factors, extended-source emission, convolution-tail asymptotics, spectral approximate identities, and rigorous harmonic-bath error bounds. Exact locators and access limitations are included below.

| Baseline and inspected location | Source assumptions and conclusion relevant here | Correspondence and actual remaining difference |
|---|---|---|
| Bingham–Goldie–Omey [R1], Theorem 1.1 and its two-part convolution proof; Theorems 2.1 and 3.1 | Regularly varying probability densities have an additive convolution-tail law; further results treat faster and bounded-comparison tails. | Splitting the domain and applying dominated convergence is an established method. T3's normal/grazing split is an adaptation of this idea to a shell kernel with a projector and Jacobian. Its displayed oscillatory amplitude permits persistent zeros, outside the direct positive regularly varying hypothesis of Theorem 1.1. The anisotropic T2 norm equivalence and Maxwell threshold map are not statements of that theorem. Whether the extra work is a substantive research contribution, rather than a routine extension of tail asymptotics, remains the strongest novelty challenge. |
| Carminati–Gurioli [R2], §II and Eqs. (11)–(13) | Extended coherent sources require a spatially nonlocal emission kernel; interference is governed by a cross density of states. | Spatial extent and interference affecting emission are already known. We do not claim this physical mechanism as new. T2–T3 concern a particular half-space smearing family, its sharp spatial norm criterion, and absolute oscillatory high-frequency terms; they do not replace a general photonic Green-tensor calculation. |
| Dereziński–Jakšić [R3], §4 field estimates and Proposition 5.2 | Weighted one-particle form-factor norms control relative boundedness and self-adjointness of Pauli–Fierz Hamiltonians. | The Hamiltonian construction in §7.1 is a specialization. T2 identifies the real-space H⁻¹ᐟ² criterion associated with the declared planar/normal profile. It is not a new self-adjointness theorem for UV-singular form factors. |
| Liu–Lu [R4], §2 Dyson/Wick setup; Theorem 1, Eq. (22), and §3 proof organization | Observable changes induced by changes of harmonic-bath correlations admit explicit bounds from diagrammatic/combinatorial estimates. | Controlled harmonic-bath perturbation theory is already available, and may give sharper bounds than T5. T5 uses a simple vacuum particle-number majorant. T6 combines that conservative bound with a frequency-local remainder and a spatially calculable certificate. No priority is claimed for Dyson control, Gaussian-bath expansions, or weak-coupling limits. |
| Tjoa–Gray [R5], §2.4, Eqs. (29)–(38), and Assumption 1 | Detector smearing, ultraviolet regularity and infrared weighted norms must be distinguished when constructing an interacting model. | This is a conceptual and operator-domain baseline. T2 supplies a necessary-and-sufficient planar density criterion for the stated normal multiplier. Ground-state infrared representation issues are not settled merely by our finite-time vacuum norm and self-adjointness argument. |
| Lill–Lonigro [R6], §1, Eq. (11), Case 0/Case 1 and Theorem 1.3 | Weighted spaces distinguish ordinary and mildly singular form factors; the singular-model theorem has its own hypotheses. | Eq. (11) does not identify finite participation area with spectral L¹. The incorrect v1.9 attribution is removed. Their singular extension is not imported as a massless all-profile construction in this paper. |
| NIST DLMF [R7], Eq. 10.17.3 | Fixed-order Bessel functions have a standard large-argument cosine expansion. | The oscillatory H for the compact-edge family follows from this established formula. The claimed addition is the shell integral and boundary-dependent classification, not the Bessel asymptotic itself. |

A further methodological baseline is Davies's weak-coupling-limit work [R10]. Its publisher abstract was inspected, but the full theorem was not successfully retrieved in this task. No theorem from it is imported here, and no novelty claim about the existence of a weak-coupling approximation is made. Pan–Gover [R9] was inspected at abstract level only; its Eq. (18) is **not certified as read** and is not a dependency of T1–T8. Chen–Chuu [R8], especially Eq. (16), supplies a useful correction to the old argument: momentum-resolved excitonic emission can be nonzero within its light cone. It does not justify the assertion that a sharp planar momentum state never radiates. Its exciton model is different from the specific free positive-band channel in T8.

The strongest overlap is methodological: a reader familiar with additive-tail expansions and rigorous spin-boson bounds may regard much of T2–T6 as a calculable specialization. The paper makes that comparison testable rather than declaring every auxiliary estimate novel. The central candidate is the **combined regularity/oscillatory-tail classification**, with the finite-time certificate as a concrete use. No external priority claim is made for T1, T4, T5, T7, T8 or Appendices A–C individually.

### 9.2 What the result changes for an external reader

The following decisions can be made without adopting Z-Spin cosmology:

- Given an ordinary normalized planar density, T2 distinguishes a well-defined vacuum coupling from a merely normalized source. The family in §4 has a finite coupling norm for β>1 even when its participation area is undefined because β≤2.
- Given an oscillating radial Fourier tail, T3 identifies a common grazing term that can defeat the anticipated PMC ultraviolet improvement. The disk and continuous cap distinguish this from a Gaussian-only calculation and give counterexamples to using area or continuity alone as a UV predictor.
- Given a positive resonant spectrum, T4 identifies a local regularity condition needed for a bounded second-order offset. T5–T6 then turn that estimate into a verified exact-dynamics interval; the numerical offset need not be fitted.

These are concrete mathematical uses. The paper does not establish their importance by counting pages, calculations or PASS rows. External significance beyond these examples and the extent to which prior work already supplies the classification still require critical assessment.

### 9.3 Four mandatory qualification axes

The governing definition is *Z-Spin Research Mission v1.6*, §1.4, preserved in the source package. Grade 3 requires an accurate new central result with substantive meaning. It does not require that every lemma be new, that the entire cosmological mission be closed, or that a human author hold a particular degree. Conversely, a corrected calculation or many agreeing AI reviews do not automatically meet it.

| Axis | Evidence prepared here | Author-side status at freeze |
|---|---|---|
| Correctness | Explicit assumptions and proofs T1–T8; counterexamples; symbolic and numerical checks; mathematical/physical scope separated | No known unresolved S2+ defect in the declared central model after these checks; independent proof acceptance pending |
| Novelty | Source-level confrontation above, including the strongest overlap; persistent-zero case and spatial threshold mapped explicitly | **HOLD / OPEN-NOVELTY** for the central synthesis; no self-awarded novelty PASS |
| Significance | Three reproducible external uses in §9.2 and a continuum error certificate | Concrete use demonstrated; broader field assessment open |
| Verification evidence | Executable ledger, frozen inputs, development failures disclosed, proofs reconstructible, author-side adversarial checklist | Reproducible author-side evidence; independent v2.0 audit absent; qualified-human anchor: **NONE** |

**Overall PAPER QUALIFICATION: HOLD. RESEARCH GRADE: UNASSESSED for the central contribution; TARGET GRADE: 3.** The retained standard/specialized parts are not claimed to exceed grade 2 on their own. This is the precise reason the current artifact is managed as a RESEARCH NOTE in paper format under Mission §1.4.3. It does not prevent another auditor from awarding grade 3 if the central result actually satisfies all four axes. There is no claim that such an audit has occurred.

A grade-3 decision should identify at least one central result, its closest prior theorem, the additional proved content and the changed decision in §9.2. If it is fully subsumed, give that mapping and retain the work as a specialized note. If a proof fails, report the exact hypothesis or counterexample and reopen the affected dependencies. A generic impression that the mathematics is easy or that Z-Spin remains unproved is not a substitute for either assessment.

## 10. Complete audit disposition, mission accounting and preservation

### 10.1 Every v1.9 finding has a current disposition

The integrated audit is `M69_v1_9_Audit_Report_KO.md`, SHA-256 `457801208802a100a45eddc925d9140d28361a69a77acc0cc1ab6deae6a3d554`. It recorded highest severity S3 and a qualification FAIL for v1.9. The following table is a disposition ledger, not a claim that the same author independently re-audited v2.0.

| Finding | Fault in v1.9 | v2.0 disposition | Remaining gate |
|---|---|---|---|
| F01 | Three branches called exhaustive admissible boundaries | Removed exhaustiveness; §3 declares and constructs exactly three mode families. Mixed projector pairing retained as an explicit counterexample, C24/W23. | Other boundary actions/conditions need their own mode derivation. |
| F02 | Universal area-only UV constants/exponents | Replaced by T3 with two endpoints and explicit oscillatory hypotheses; disk and cap retained, W13/W14. | Arbitrary anisotropic tails and other multipliers outside the hypotheses are not classified. |
| F03 | Normalization, area, spectral L¹ and O(1) remainder conflated | T2 gives the sharp coupling-norm criterion; A_eff requires positive finite density L²; T4 adds the missing local condition; W17/W19. | No inference from density normalization alone. |
| F04 | A fixed Pauli matrix promoted to an exact band vertex and closed subsystem | T7 provides the momentum-resolved projector product and makes recoil explicit; W22. | Physical moving-band kernel, state and projection error remain OPEN. |
| F05 | Fitted offset and unsupported packet-width optimum used to certify a record window | T4–T6 provide proved bounds and a rational stationary-model witness; W29/C30 retain the failures of the old optimum/spreading argument. | No carrier packet optimum or moving-packet window claimed. |
| F06 | Energy-only bulk threshold treated as opening/invariance | T8 proves a stronger, precisely scoped on-shell exclusion using planar momentum; finite-time leakage is treated separately, W27. | Actual bulk vertex and finite-time many-body leakage remain OPEN. |
| F07 | Negative κ omitted | Signed branches and |κ| are explicit in (8.7), C25; both transition orientations tested in V42. | Gapless M=0/h=0 cases excluded from the gapped theorems. |
| F08 | Verifier row descriptions exceeded their executable content | Standalone v2.0 registry; each row has class, claim and scope; P=0. Functional counterexamples and ledger mutations are explicit. | Numerical checks do not replace textual proof or scientific novelty review. |
| F09 | External citations and locators overstated | §9 and References correct the Lill–Lonigro and Chen–Chuu imports; Pan–Gover Eq. (18) marked unread. Stronger methodological overlap added. | OPEN-NOVELTY retained where justified. |
| F10 | History digest mismatch, stale version cards and divergent companion claims | Old files preserved byte-for-byte as historical inputs; fresh v2.0 companions and a manifest generated only after freeze. | No old manifest is silently repaired and no unconfirmed history sequence number is assigned. |

There are no inherited “unchanged” theorem assumptions that a reader must guess. The finite-qubit model is stated in Appendix A; the field model is stated in §§2–3 and §7. Old valid results have a current location below. False universal assertions are archived as historical statements with explicit replacement, not reintroduced in an appendix.

### 10.2 Preservation map for the earlier research

| Earlier material | Current treatment |
|---|---|
| Affine collision law, proper signed SVD, cofactor drift, rank classification, resonance determinant | Appendix A.1–A.3, re-stated with assumptions and proof route; C31/C33/V32 |
| Rank-two transfer, fixed-point/convergence distinction, singular weak-collision limit, resource backaction, M68 sign and alignment scaling | Appendix A.3–A.5; W34 and stated algebraic derivations |
| Precession-aware Dyson response, exact two-qubit blocks, tilted resonance, KMS scope | Appendix B and C.3; V35, with no Markov-to-exact promotion |
| Dirac atlas and vector/tensor distinction | Appendix B.3; explicit table and normalization, not reselected action |
| Matrix spectrum, elliptical analyser, null class, identity resource term, Gauss/Coulomb obstruction | Appendix C.1–C.4; C36/C37, physical obligations remain open |
| v1.9 spatial/boundary additions and proposed physical window | Replaced by §§3–8 with the audit disposition in §10.1 |
| Full original text, original verifier/JSON/log/manifest/session/history | Included under `historical_v1_9/` in the package, unmodified; not imported by the new verifier |
| Earlier audit reports and independent counterchecks | Preserved under `audit_inputs/`; evidence of the earlier faults, not independent acceptance of v2.0 |

The archive preserves long original derivations and historical identifiers. The present paper supplies the definitions and arguments needed for the current claims. It does not imply that every historical sentence remains endorsed or that 139 former rows have been rerun as the v2.0 theorem census.

### 10.3 Mission bridge states and actual deliverable

| Logical step | Before | After this revision |
|---|---|---|
| Declared stationary spatial density → finite field-coupling norm | Sufficiency and area confusion | T2 necessary-and-sufficient criterion in its declared class |
| Declared radial density and normal multiplier → UV spectrum | False universal constants | T3 conditional classification including oscillatory leading terms |
| Declared stationary detector → nonzero exact energy-axis polarization | Second-order calculation and fitted window | T4–T6 controlled exact-dynamics interval under explicit assumptions |
| M67 action/current → selected moving fermionic subsystem and state | OPEN | OPEN, with the missing band kernel and projection obligations made explicit |
| Physical detector polarization → grading outcome/instrument/Born record | OPEN | OPEN; even a nonzero Bloch component is not an instrument |
| Z-dynamics → spacetime, carrier parameters and observation | OPEN | No claim of closure |

**OUTPUT ROLE: SUPPORT + METHOD; CORE: NO. FQ2 and RQ3 remain OPEN.** The first three changes are local mathematical progress; they are not zero progress merely because the physical bridge remains open. But they do not establish a Z-Spin-specific action-to-record arrow. The declared q, smearing and state are inputs, not outputs of the cosmological theory. No target fitting, dimensionality selection or physical constant extraction is performed.

The source freeze includes the supplied book, initial-idea document, operations/deep-search/breakthrough/kernel/manuscript/verification/audit rules, Mission v1.6, the 11D seed report and history through H0321. Available constants and debt indices were also inspected for internal duplication; the retrieved index snapshots did not provide an M67–M69 entry. That limited result is not evidence of global internal novelty. Proposed later history entries are not presumed to be merged into the authoritative history. The new history companion is a proposal without a reserved H-number.

### 10.4 Concrete next discriminating work, with stop conditions

1. **External theorem comparison.** Try to derive T3, including its persistent-zero amplitude and explicit shell coefficients, from the closest established oscillatory/regular-variation theorem. A complete matching derivation would narrow or eliminate the novelty claim. An unmatched statement is not automatically novel; document the real additional proof obligation.
2. **Sharp finite-time improvement.** Replace the coarse T5 majorant by a bath-correlation/Wick bound while retaining T4's explicit spectral error. Demonstrate a wider certified interval for the same continuum example, with fixed tolerances and no fitted offset. Stop if the change only repackages an existing bound without a useful improvement.
3. **One physical bridge, if pursuing CORE.** Construct the occupied-state, momentum-resolved current kernel from (8.2), and bound packet/recoil/bulk errors uniformly on a common interval. If they exceed the signal, report the resulting exclusion or insufficient control. Do not reuse the stationary certificate as its answer.

These are reopening conditions, not tasks claimed completed in v2.0. The present release is the concrete paper/script requested for an external audit; it does not require a promise that a future audit will pass.

## 11. Reproduction and author-side adversarial checks

Run the script in a directory containing the manuscript:

```bash
python zs_m69_verify_v2_0.py --paper ZS-M69_v2_0.md
```

The script requires Python 3.10+ with NumPy, SciPy and SymPy. It has no network calls, no import of an older verifier and no hidden input data. `--out-dir` changes the JSON output directory. The archive supplies the exact package versions used in the final run. JSON records script SHA-256, environment, class census, every Boolean and its evidence. The final run log, JSON and package manifest are companions, not silently embedded proof claims.

The 42 executable rows are classified as **C=18** exact symbolic/rational subchecks, **V=10** numerical comparisons, **W=11** counterexamples or assumption witnesses, **R=2** functional regressions, and **G=1** registry gate. **P=0.** C means the specified computational identity or certificate, not a formal verification of every theorem using it. V and W disclose finite sample ranges, quadrature estimates and finite-mode limitations in their JSON evidence. R/G do not contribute to scientific proof strength.

The mathematical theorem count is T1–T8 plus retained L1–L3 families. It is not 42 independently proved research results. Internal comparisons use separately implemented formulas where indicated, but were designed by the same authoring assistant; this is not an independent AI audit.

| Required attack perspective | Author-side action and remaining scope |
|---|---|
| Claim | Abstract traces to T2–T6; no action-derived detector or grade PASS stated. |
| Type | Density, Fourier multiplier, matrix spectrum, band vertex, projection and instrument kept distinct. |
| Quantifier | Three declared boundaries; T3 tail hypotheses; T4 local condition; y≤1 and h>0; sampled checks not universal proofs. |
| Proof/computation | Both endpoint proofs, symmetric-difference identity, vacuum majorant and rational witness reconstructed; counterexamples retained. |
| Dependency | Source-level comparisons and explicit field-domain hypotheses; historical PASS counts not imported. |
| Selection/physical | Fixed-k and packet closure challenged; actual carrier kernel and state remain OPEN. |
| Anti-numerology | No observational targets fitted; example parameters stated as arbitrary mathematical choices. |
| Reproducibility | Fresh run, machine-readable evidence, duplicate deterministic replay and manifest checks supplied at freeze. |
| Prior art | Strongest tail and harmonic-bath baselines named; unread source portions not certified. |
| Refutation | Mixed boundary, disk, cap, cusp, chirped multiplier, nonclosure, negative κ and finite-time off-shell witnesses. |
| Internal consistency | Current metadata checked from registry; package hashes generated after companion completion. |
| Value/release | Four qualification axes separated; HOLD, SUPPORT/METHOD and no external review preserved. |

During development, three initial row failures were retained in `development_validation.md`: a finite-frequency disk tolerance, a symbolic Boolean conversion, and a symbolic integral's conditional representation. Their specific repairs are documented. Numerical thresholds are finite-run checks, not hidden estimates of an asymptotic theorem remainder. A later complex-spectrum check passed for both frequency orientations. Final mutation checks also exercise missing/invalid manuscript metadata and require a nonzero exit status with an explicit package failure.

<!-- M69-VERIFICATION-METADATA
{"version":"v2.0","rows":42,"census":{"C":18,"G":1,"R":2,"V":10,"W":11},"P":0}
-->

## 12. Conclusions

For the stated planar/normal field smearing, finite coupling norm is equivalent to a negative-Sobolev condition, not finite participation area. The high-frequency spectrum has separate normal and grazing contributions; the latter can preserve oscillations and prevent the expected boundary-induced UV improvement. A local symmetric-Dini condition and a vacuum Dyson estimate give a controlled finite-time exact polarization for a declared stationary qubit, including an exact-arithmetic continuum example. The moving-band and measurement bridges require further physical input and error control. These are the results and boundaries submitted for external research-grade assessment.

## Appendix A. L1 — Retained finite-collision mathematics, with full model assumptions

### A.1 Model, orientations and exact affine law

This appendix has a separate coupling convention from §§2–8: the entire real tensor G is included in the Hamiltonian, and α is the collision duration/strength. Let two qubits have Pauli frames σ and B, input states ρ=(I+r·σ)/2 and τ=(I+m·B)/2 with |r|,|m|≤1, and

\[
 H_G=\sum_{a,b=1}^3G_{ab}\sigma_a\otimes B_b,
 \quad U_\alpha=e^{-i\alpha H_G},
 \quad\Lambda(\rho)=\operatorname{tr}_R[U_\alpha(\rho\otimes\tau)U_\alpha^\dagger].
\tag{A.1}
\]

There are no one-body free terms during this collision. The initial state is a product. Iteration of the same channel means a fresh reference τ for each collision; it does not mean reusing an already correlated reference.

Choose a **proper signed SVD** G=R_E diag(g₁,g₂,g₃)R_Rᵀ with R_E,R_R∈SO(3). At least one signed g_i must carry a negative determinant if detG<0; replacing all signed values by their magnitudes loses physical orientation information. Let s_i=sin(2αg_i), c_i=cos(2αg_i),

\[
 S=R_E\operatorname{diag}(s_i)R_R^T,\quad
 C_E=R_E\operatorname{diag}(c_i)R_E^T,\quad
 C_R=R_R\operatorname{diag}(c_i)R_R^T.
\]

For a matrix A, cof(A) is its cofactor matrix, not its adjugate; for a vector v, [v]_×w=v×w. The exact Bloch map is

\[
 r'=Mr+b,\qquad
 b=\operatorname{cof}(S)m,\qquad
 M=\operatorname{cof}(C_E)+[Sm]_\times C_E.
\tag{A.2}
\]

**Proof.** In the diagonal frame the three operators σ_iB_i commute. Conjugating σ_e successively by their exponentials, using the two anticommuting components and then taking the product-state expectation, gives for cyclic (e,f,g)

\[
 r'_e=c_fc_gr_e-c_fs_gr_fm_g+s_fc_gr_gm_f+s_fs_gm_e.
\tag{A.3}
\]

Its constant and linear coefficients are precisely (A.2) in that frame. Proper rotations are covered by local SU(2) conjugations; covariance of cofactors under proper rotations gives the displayed frame-free law. V32 independently propagates 4×4 unitaries for both determinant orientations and compares their reduced states. □

The transported commutator identity

\[
 G[v]_\times G^T=[\operatorname{cof}(G)v]_\times
\tag{A.4}
\]

follows by the cross-product determinant identity, or by equality of its polynomial entries (C31). Consequently

\[
 b=4\alpha^2\operatorname{cof}(G)m+O(\alpha^4),\qquad b(-\alpha)=b(\alpha).
\tag{A.5}
\]

For rank G=2, choose jointly oriented null vectors n_L∈kerGᵀ and n_R∈kerG with cofG=g₁g₂n_Ln_Rᵀ, g₁,g₂>0. Then b=sin(2αg₁)sin(2αg₂)(n_R·m)n_L for every α. Rank≤1 gives b=0 identically; rank 3 and m≠0 give a nonzero second-order coefficient. The variety rank≤1 has dimension 5 and codimension 4 in the unrestricted nine-dimensional real tensor space. This codimension is not a probability distribution over physically selected actions and not a uniqueness theorem for a measurement selector.

### A.2 Resonance, uniqueness and its weak-collision limit

In the diagonal frame set d_e=1−c_fc_g. Expansion of the 3×3 determinant gives

\[
 \det(I-M)=d_1d_2d_3+\sum_e d_ec_fc_gs_e^2m_e^2.
\tag{A.6}
\]

C33 checks the polynomial identity. If rankG≥2 and 0<|α|<π/(4g_max), all c_i>0 and all d_e>0, so det(I−M)>0 for every allowed m. The channel then has exactly one fixed point. For rank≤1 the coupling-axis Bloch vector is fixed by M, and b=0, so the fixed point is never unique. These statements do not require a nonzero leading α⁴ determinant coefficient.

Indeed, with λ_i the eigenvalues of GᵀG and m_i in its eigenbasis,

\[
 \Delta_G(m)=\sum_{i<j}\lambda_i\lambda_j(m_i^2+m_j^2)
 =\operatorname{tr}(GG^T)|Gm|^2-|G^TGm|^2,
\]

and det(I−M)=8α⁴Δ_G(m)+O(α⁶). If Gm=0, the leading term is instead

\[
 \det(I-M)=8\alpha^6\prod_{i<j}(\lambda_i+\lambda_j)+O(\alpha^8).
\tag{A.7}
\]

Thus Δ=0 does not imply nonuniqueness. For Δ>0,

\[
 r_*(\alpha)\longrightarrow
 \frac{2\det G\,|m|^2}{\Delta_G(m)}Gm.
\tag{A.8}
\]

To see this, expand I−M=−2α[Gm]_×+2α²(trGGᵀI−GGᵀ)+O(α³). The transverse restriction of [Gm]_× is invertible; since channel fixed points lie in the unit Bloch ball, the transverse component is O(α). Projection along Gm then yields (A.8) using (Gm)·cofGm=detG|m|². Rank 2 with Gm≠0 consequently has r_*→0. The null-resource rank-two case must be evaluated separately in A.3; division by Δ is invalid there.

### A.3 Rank-two transfer and the stationary manifold

For m=μn_R, x=2αg₁, y=2αg₂ and D=1−cosxcosy, the canonical-frame map is

\[
 M=\operatorname{diag}(\cos y,\cos x,\cos x\cos y),\qquad
 b=\mu\sin x\sin y\,e_3.
\tag{A.9}
\]

If D≠0, r_*=μ(sinx siny/D)n_L is a fixed point. It is unique exactly when (1−cosx)(1−cosy)D≠0, and iteration converges to it from every state exactly when |cosx|<1 and |cosy|<1. The example x=π,y=π/2 has M=diag(0,−1,0), a unique fixed point 0, and a two-cycle; W34 preserves it.

At cosx=1, cosy≠1 the stationary set is the second coordinate axis inside the Bloch ball; exchange x,y for the first axis. When both are 1 every state is fixed. At cosx=cosy=−1, the stationary set is the n_L axis. These follow directly from the three decoupled fixed-point equations.

For D>0, ε=sinx siny/D obeys |ε|≤1 because D∓sinx siny=1−cos(x∓y). Equality occurs on the two respective ridges x∓y∈2πℤ, excluding D=0. As α→0, ε→2g₁g₂/(g₁²+g₂²). The drift resolves the two frequencies 2(g₁−g₂) and 2(g₁+g₂) only if μ≠0 and the observation interval resolves them; this is not an unconditional experimental prediction.

### A.4 One-collision backaction and the M68 sign convention

Swapping the two qubits gives the exact one-collision resource update

\[
 m'=\operatorname{cof}(S^T)r+
 [\operatorname{cof}(C_R)+[S^Tr]_\times C_R]m.
\tag{A.10}
\]

The joint output is generally correlated. Equations (A.2) and (A.10) cannot be iterated as two independent state updates for reference reuse.

For G=diag(1,−χ,0), χ=±1, write m=(m_K,m_K′,m_J) in the M69 canonical frame and D̂=1−(1−m_K²−m_K′²)cos2α. Then b=−χm_Jsin²2α e₃ and, off the resonance denominators,

\[
 r_x^*=\frac{m_Jm_{K'}\sin2\alpha}{\widehat D},\quad
 r_y^*=\frac{\chi m_Jm_K\sin2\alpha}{\widehat D},\quad
 r_z^*=-\frac{\chi m_J(1-\cos2\alpha)}{\widehat D}.
\tag{A.11}
\]

Substitution into (A.3) proves the signs. The archived M68 comparison used m_can=(m_K,−m_K′,m_J) to relate its printed component convention. This is a component mapping, not silent editing of M68. The paired null-vector convention also carries χ; nonnegative singular values alone do not determine the record sign.

### A.5 Alignment scaling

For G=diag(a,b,0), a,b>0, and m=(δ,0,μ), direct solution gives

\[
 r_z^*=\frac{\mu\sin(2\alpha a)\sin(2\alpha b)}
 {1-\cos(2\alpha a)\cos(2\alpha b)
 +(1+\cos(2\alpha a))\cos(2\alpha b)\delta^2}.
\tag{A.12}
\]

At fixed δ≠0 this tends to zero. At δ=kα it tends to 2abμ/(a²+b²+k²), while r_y^* tends to −(k/a) times that value. These follow by Taylor expansion and the second fixed-point equation. No action or state-selection mechanism is asserted to choose δ=kα. This collision scaling is distinct from the spatially smeared field window in T6.

## Appendix B. L2 — Precession, exact two-qubit blocks and the boundary atlas

### B.1 The second-order commutator source

For a qubit initially I/2 and a product environment state, let the interaction picture coupling be q∑_a σ_a(t)Φ_a(t). Writing σ_a(t)=v_a(t)·σ, the Schrödinger-picture Bloch response is obtained by rotating back the interaction-picture vector

\[
 \delta r^{(2)}=-2iq^2\sum_{a,b}\int_0^Tdt\int_0^t ds\,
 [v_a(t)\times v_b(s)]\,
 \langle[\Phi_a(t),\Phi_b(s)]\rangle.
\tag{B.1}
\]

It follows from the double commutator in the Dyson expansion and the identity [v·σ,w·σ]=2i(v×w)·σ. With no free system evolution, v_a=e_a. On a constant short window, Φ_a=∑_bG_abB_b and q absorbed in G, it reduces to (A.5). For a linear free Bose field the commutator is a scalar, independent of the field state. This proves state independence of this **second-order source from I/2**, not state independence of all higher-order dynamics or stationary polarization.

### B.2 Exact parity blocks and tilted-axis limits

Take H_s=h_Eσ_z/2, H_R=h_RB_z/2 and a real transverse 2×2 coupling G (again including its strength in G). Let the reference state be (I+m_JB_z)/2 and the carrier initially I/2. Put S=||G||_F², d=detG,

\[
 w_-=S+2d,\quad w_+=S-2d,\quad
 \Delta=h_E-h_R,\quad\Sigma=h_E+h_R.
\]

The total Hamiltonian preserves σ_zB_z. Its two 2×2 blocks have transition probabilities

\[
 P_-=\frac{w_-}{w_-+\Delta^2/4}
       \sin^2\!\left(T\sqrt{w_-+\Delta^2/4}\right),\quad
 P_+=\frac{w_+}{w_++\Sigma^2/4}
       \sin^2\!\left(T\sqrt{w_++\Sigma^2/4}\right),
\tag{B.2}
\]

with continuous zero-frequency interpretations. Direct evolution in each block gives

\[
 b_z=m_J(P_--P_+),\quad b_x=b_y=0,
 \qquad r'_z=(1-P_--P_+)r_z+m_J(P_--P_+).
\tag{B.3}
\]

The z equation holds for arbitrary carrier input because block transitions involve its diagonal populations and the reference is diagonal; off-diagonal carrier entries do not contribute to z. At second order b_z=2m_J[w_-F_T(Δ)−w_+F_T(Σ)]. V35 compares the block formula with the full 4×4 unitary for general transverse G. It is not valid merely by replacing m_J with a tilted state's z component.

For axes n_E,n_R, choose proper energy-frame rotations R_E,R_R and transform K=R_EᵀGR_R. The transverse block K_perp controls the resonant coefficient. With P_E=I−n_En_Eᵀ and P_R similarly,

\[
 w_\mp(K_\perp)=\|P_EGP_R\|_F^2
                 \pm2n_E^T\operatorname{cof}(G)n_R.
\tag{B.4}
\]

This is the cofactor/minor identity in the rotated frame. If the reference is (I+p_Rn_R·B)/2, the leading T² coefficient at h_E=h_R≠0 is p_Rw_-(K_perp)n_E; at h_E=−h_R≠0 it is −p_Rw_+(K_perp)n_E. Its grading projection acquires n_E·e₃. Time averaging keeps K₃₃ as a zero-frequency term, but its commutator contribution on I/2 vanishes; it is incorrect to say that every longitudinal coupling oscillates away. General mixed longitudinal/transverse terms destroy the exact parity solution, so (B.2) is not an exact formula for the tilted problem.

A band population pushforward p_R=−tanh(E′/(2Θ)) and the Gibbs state of H_R=E′n_R·B, p_R=−tanh(E′/Θ), are different at the same Θ. The latter Hamiltonian has gap 2E′. Their relation requires an occupation-to-qubit and temperature identification; it cannot be repaired by a one-sided z projection.

### B.3 Typed Dirac embedding and the sixteen bilinears

The following is an algebraic carrier atlas retained from the audited construction. Use η=diag(+,-,-,-), Dirac γ matrices, γ₅=iγ⁰γ¹γ²γ³, N=γ⁰γ³ and B_θ=iγ³e^{−iθγ₅}. Let

\[
 e_-=2^{-1/2}(0,1,0,-1)^T,\quad
 e_+=2^{-1/2}(1,0,1,0)^T,\quad
 \Psi_\theta=[(I+B_\theta)e_-,(I+B_\theta)e_+],\quad
 \iota=\Psi_\theta/\sqrt2.
\]

Here J_E=diag(−1,+1), X_θ=−sinθ σ_x+cosθ σ_y and Y_θ=cosθ σ_x+sinθ σ_y form the oriented Pauli frame (X_θ,Y_θ,J_E). The identities B_θ†=B_θ, B_θ²=I and {B_θ,N}=0 give Ψ†Ψ=2I, Ψ†NΨ=0 and ι†ι=I. The γ⁰-transport basis on the negative N eigenspace gives B_θ|_{E₊}=i e^{−iθJ_E}. Direct multiplication also gives Ψ†γ₅Ψ=0 and Ψ†γ⁰e^{iθ_mγ₅}Ψ=2sin(θ+θ_m)J_E. Thus the signed M67 mass datum is M=m sin(θ+θ_m), when that upstream dispersion is adopted.

Define σ^{μν}=(i/2)[γ^μ,γ^ν]. The entries below are **Ψ†γ⁰ΓΨ**; divide all by two for the normalized ι embedding.

| Γ | Bilinear | Γ | Bilinear |
|---|---|---|---|
| I | 2sinθ J_E | iγ₅ | 2cosθ J_E |
| γ⁰ | 2I | γ¹ | 2X_θ |
| γ² | 2Y_θ | γ³ | 0 |
| γ⁰γ₅ | 0 | γ¹γ₅ | 0 |
| γ²γ₅ | 0 | γ³γ₅ | 2J_E |
| σ⁰¹ | −2sinθ Y_θ | σ⁰² | 2sinθ X_θ |
| σ⁰³ | 2cosθ I | σ¹² | 2sinθ I |
| σ¹³ | 2cosθ X_θ | σ²³ | 2cosθ Y_θ |

These equations follow by substitution in the displayed 4×2 embedding, so no unspecified “admissible representative” is needed to use the table. The four tangential tensor entries are not unit flip elements at angle 2θ: their normalized squares are sin²θ I or cos²θ I. The archived upstream Lemma 38.0 wording conflicts with them; that conflict remains reported, not merged into the upstream source. The vector entries alone give a pointwise compressed coupling q(A₀I+A₁X_θ+A₂Y_θ). They do not prove a tensor-factor subsystem, a moving-band matrix element, q=g_eff, or a selected environment. The normal exponential and the band spinors in §8 are additional objects. This atlas is preserved specialist algebra and is not counted as a new T2–T6 contribution or as a newly registered full-atlas proof row.

## Appendix C. L3 — Matrix analyser, remainder scope and the scalar-channel obstruction

### C.1 Positivity, null class and the meaning of rank

Write a Hermitian PSD tangential spectrum as J=S+iA with S real symmetric and A real antisymmetric. In the u_κ=(κ,i) frame,

\[
 f_-=\kappa^2S_{11}+S_{22}-2\kappa A_{12},\quad
 f_+=\kappa^2S_{11}+S_{22}+2\kappa A_{12}.
\tag{C.1}
\]

The analyser W=u_κu_κ† has rank one and eigenvalues 0,1+κ². This is a two-level transition property, not a proof that the field has one mode. Positivity implies

\[
 (1+\kappa^2)\lambda_{\min}(J)\le f_-\le
 (1+\kappa^2)\lambda_{\max}(J),\quad
 f_-=0\ \Longleftrightarrow\ Ju_\kappa=0.
\tag{C.2}
\]

The equivalence follows from f_-=||J^{1/2}u||². For κ≠0, solving the two complex equations Ju=0 gives exactly

\[
 S_{12}=0,\quad S_{22}=\kappa^2S_{11},\quad A_{12}=\kappa S_{11},
 \qquad
 J=c\begin{pmatrix}1&i\kappa\\-i\kappa&\kappa^2\end{pmatrix},\quad c\ge0.
\tag{C.3}
\]

C36 checks both directions algebraically. At κ=0, the condition is S₂₂=0 and PSD then forces the off-diagonal entry to vanish; S₁₁ can remain nonzero. For parity-even J and κ≠0, f_-=0 requires J=0. A positive-definite J makes f_->0 for every κ. Summing independent PSD spectral contributions cannot cancel f_-; the sum is null exactly when every summand is null. Correlated sources must first be combined into their full spectral matrix rather than treated as independent summands.

The secular grading coefficient −2πq²κf_- has κ times that coefficient ≤0; a strict sign requires κ≠0 and f_->0. Three distinct bath modes with collinear coupling vectors can still have rank-one J and lie in (C.3). The observed coupling span, not the number of species or bulk dimension, determines this rank.

### C.2 Exact time remainder and perpendicular response

With the q-independent response kernel defined by

\[
 N_\parallel(\tau)=\int_0^\infty
 [f_-(\omega)\cos((h-\omega)\tau)
 -f_+(\omega)\cos((h+\omega)\tau)]d\omega,
\]

one has R₂=−2q²∫₀ᵀ(T−τ)N_parallel(τ)dτ. If the improper integrals I₀=∫₀∞N_parallel and I₁=∫₀∞τN_parallel both converge, algebra gives

\[
 R_2=-2q^2TI_0+2q^2I_1+epsilon(T),\quad
 \epsilon=2q^2\left[T\int_T^\infty N_\parallel d\tau
                    -\int_T^\infty\tau N_\parallel d\tau\right].
\tag{C.4}
\]

When J is integrable and continuous at h>0, approximate-identity analysis identifies the linear coefficient as I₀=πf_h if I₀ exists. Absolute convergence of ∫τ|N| is sufficient for |ε|≤4q²∫_T∞τ|N|, but is not necessary; oscillatory cancellation can make I₁ converge conditionally. Conversely, the cusp in §6 need not have a bounded offset. T4 is an alternative set of directly verifiable frequency-domain sufficient conditions, not an inference that all integrable spectra satisfy (C.4) with a constant remainder.

For completeness, a perpendicular second-order bound can be derived without assuming a stationary grading axis. Define χ_ab(τ)=i〈[Φ_a(τ),Φ_b(0)]〉 and ||χ||₁=∫₀∞∑_{a,b}|χ_ab(τ)|dτ. In a precession frame the source has the form −2q²R_n(−ht)∫₀ᵗN(τ)dτ, with ||N(τ)||≤∑|χ_ab(τ)|. On the plane perpendicular to n, an antiderivative of R_n(−ht) has norm 1/|h|. Integrating by parts gives the conservative bound

\[
 |\delta r_\perp^{(2)}(T)|\le\frac{4q^2}{|h|}\|\chi\|_1
 \le\frac{6q^2}{|h|}\|\chi\|_1.
\tag{C.5}
\]

The last, looser constant preserves the earlier bound under this explicit entry-sum norm. It requires h≠0 and χ∈L¹, and is not uniform as h→0. It is only a second-order statement; a tilted grading-record certificate must also budget higher orders. Vanishing J(h) kills the linear resonant coefficient, not the full bounded or sublinear finite-time response.

### C.3 KMS, relaxation and the secular approximation

Assume a field KMS state at temperature Θ and a valid secular weak-coupling generator. With Γ_ab(ω)=∫ℝe^{iωt}〈Φ_a(t)Φ_b(0)〉dt, its transition rates obey Γ_up=e^{−h/Θ}Γ_down. If the transition contraction is nonzero, the stationary energy-axis polarization of this generator is −tanh(h/(2Θ)). A stationary non-equilibrium bath does not in general satisfy this relation. On the spectral null class both rates vanish at this order and their ratio does not select a unique population.

For linear free fields, Γ(h)−Γᵀ(−h)=2πJ(h), giving rate difference 2πq²f_h and rate sum 2πq²f_h coth(h/(2Θ)). Longitudinal pure dephasing depends on the bath's zero-frequency spectrum as well as the tilt. A secular Lamb-shift Hamiltonian commutes with H_s and does not rotate its axis; discarded cross-Bohr terms in an unsecularized equation can do so. None of these generator statements proves the exact long-time equilibrium of (7.1), a Davies limit under unstated hypotheses, or the M67 population pushforward discussed in B.2. They are retained standard conditional context, not new grade-3 evidence.

### C.4 Identity-on-qubit terms and Gauss/Coulomb operators

Adding I⊗Φ₀ to the coupling produces no second-order Bloch drift from I/2. A nested commutator containing it has either a commuting system identity or the trace of an environment commutator, which vanishes under the stated domain/integrability conditions; C37 checks the finite-dimensional algebra. For a linear Bose field, a drive by Φ₀ can instead be absorbed in an environment displacement. It shifts another field by the c-number

\[
 f_a(t)=i\int_0^t[\Phi_0(s),\Phi_a(t)]ds.
\]

Commutator zero for all relevant times is a sufficient exact decoupling condition, not a proved necessary one. A nonzero displacement can change higher-order response. In the centered vacuum/maximally mixed setting the odd total orders vanish by parity, so this does not generate a missing second-order polarization.

A Gauss-law/Coulomb term built from a matter density operator is a different type of object; it cannot generally be represented as I⊗Φ₀. Even if a first density compression is scalar,

\[
 P\rho\rho P=P\rho P\rho P+P\rho Q\rho P
\tag{C.6}
\]

contains an omitted-sector contribution. Hence the compressed Coulomb interaction, induced boundary terms, effective coupling g_eff and the K17/K18 subsystem/instrument obligations remain open. None is closed by the pointwise atlas or the stationary detector certificate.

## References and source-access ledger

Primary references used for the current central proofs or their closest comparison are listed with the inspected locations. URLs identify the actual source. These sources are not represented as endorsing Z-Spin or the research grade of this manuscript.

- **[R1]** N. H. Bingham, C. M. Goldie and E. Omey, *Regularly Varying Probability Densities*, Publications de l'Institut Mathématique 80(94), 47–57 (2006). [Author-hosted full text](https://www.ma.imperial.ac.uk/~bin06/Papers/bgo.pdf). Inspected Theorems 1.1, 2.1, 3.1 and the split-convolution proof.
- **[R2]** R. Carminati and M. Gurioli, *Purcell effect with extended sources: The role of the cross density of states*, Optics Express 30, 16174–16183 (2022). [Full text, arXiv:2107.13980](https://arxiv.org/pdf/2107.13980). Inspected §II, Eqs. (11)–(13), and their surrounding physical interpretation.
- **[R3]** J. Dereziński and V. Jakšić, *Spectral theory of Pauli-Fierz Hamiltonians I* (1999 preprint). [Author/institute full text](https://www.maphysto.dk/publications/MPS-RR/1999/3.pdf). Inspected §4 field estimates, including Eq. (4.73), and Proposition 5.2. Field normalization differs by √2 from (7.1).
- **[R4]** K. Liu and J. Lu, *Error Bounds for Open Quantum Systems with Harmonic Bosonic Bath*, Quantum 9, 1896 (2025). [Published full text](https://quantum-journal.org/papers/q-2025-10-28-1896/pdf/) and [arXiv v3 HTML](https://arxiv.org/html/2408.04009v3). Inspected §2, Theorem 1/Eq. (22), and §3 proof setup.
- **[R5]** E. Tjoa and F. Gray, *The Unruh-DeWitt model and its joint interacting Hilbert space*, J. Phys. A: Math. Theor. 57, 325301 (2024). [Full text v2](https://arxiv.org/html/2402.05795v2). Inspected §2.4, Eqs. (29)–(38), Assumption 1 and surrounding UV/IR distinctions.
- **[R6]** S. Lill and D. Lonigro, *Self-adjointness and domain of generalized spin-boson models with mild ultraviolet divergences* (2025 revised version). [Full text v2](https://arxiv.org/html/2307.14727v2). Inspected §1, Eq. (11), Case 0/Case 1 and Theorem 1.3; no area-equivalence theorem imported.
- **[R7]** NIST Digital Library of Mathematical Functions, [Eq. 10.17.3](https://dlmf.nist.gov/10.17#E3), large-argument asymptotic expansion of J_ν. Used for the compact-edge example after deriving its Fourier transform.
- **[R8]** Y. N. Chen and D. S. Chuu, [arXiv:cond-mat/0108332, full text](https://arxiv.org/pdf/cond-mat/0108332). Inspected Eq. (16) and related light-cone discussion, with Eqs. (26)–(27), during the integrated audit. Used to correct a prior citation, not to prove T8 for a different model.
- **[R9]** Y. Pan and A. Gover, [arXiv:1805.08210](https://arxiv.org/abs/1805.08210). Abstract inspected; full-text Eq. (18) not independently inspected here. Not a dependency of the replacement theorems.
- **[R10]** E. B. Davies, *Markovian master equations*, Communications in Mathematical Physics 39, 91–110 (1974). [Publisher page](https://link.springer.com/article/10.1007/BF01608389). Abstract inspected; full theorem not retrieved in this task. Listed as a methodological baseline, not an imported proof.

Internal primary inputs are supplied in the archive under `project_sources/`: the synthesis book v13.2, initial-idea note v1.3, seven project rule modules v2.3 including audit, Mission v1.6, 11D seed report v1.4 and history H0001–H0321. The operations module is included among those seven rules. The exact paths and hashes are in `release_manifest_v2_0.json`. Original M69 v1.9 and its companions are under `historical_v1_9/`; the audit report and independently implemented v1.9 counterchecks are under `audit_inputs/`. Remote indices are read-only snapshots, not confirmation that later proposed history records were merged.

## Availability, authorship and version record

The companion `zs_m69_verify_v2_0.py` is a standalone reproducibility script. Its JSON and log state the actual checks. The research package contains this paper, the script, outputs, dependency versions, development repair notes, prior-art ledger, proposed history/session companions, the audit inputs and an integrity manifest. No external observational data were used. Neither human authorship, institutional affiliation nor human peer review has been invented. The manuscript, derivations, implementation and author-side tests were prepared with AI assistance; **independent v2.0 AI audit: NONE; qualified-human anchor: NONE**.

**Version delta v1.9 → v2.0:** F01–F10 fully dispositioned; false universal statements replaced; T2 sharp spatial criterion and T3 oscillatory classification developed; T4–T6 finite-time error control and rational witness added; T7 momentum vertex and T8 scoped kinematics supplied; earlier valid mathematics retained; standalone evidence registry and new integrity manifest supplied. Historical files and verdicts remain unchanged. This artifact is ready for the external audit requested by the user, with research qualification explicitly pending the remaining scientific judgments.
