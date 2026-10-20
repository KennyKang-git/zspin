# Rigidity, Stability, and Robust Hardness of Time-Dependent Markovian Embedding for Quantum Channels

**ZS-M76, version 2.5 - October 20, 2026**

## Abstract

Time-independent quantum Markovian embedding is NP-hard. We establish explicit inverse-polynomial interior and exterior promises for embedding into arbitrary integrable time-dependent Lindblad dynamics on the same finite-dimensional system. For channels fixing a complete orthogonal family of pure states, time-dependent embedding is equivalent to a conditionally positive logarithm and hence to homogeneous embedding. We prove square-root stability: if a Markovian endpoint is within diamond distance $\delta\le\min\{c/(2\sqrt d),1/(72d^2)\}$ of such a channel with coherence magnitudes at least $c$, an embeddable pointer-preserving channel lies within $400d^{7/2}\log(2/c)\sqrt\delta$. The proof uses total linear entropy to bound integrated off-frame noise, and controls the moving frame without an exponential Grönwall factor. A bounded-degree logarithm-branch reduction and positivity-preserving rational approximation then give NO instances at distance at least $\nu_d=(4\cdot10^{16}d^7)^{-1}$ from every time-dependent Markovian channel. A small rational depolarizing regularization preserves NO separation of $3\nu_d/4$ and places every YES output inside a full affine Hermiticity-preserving, trace-preserving ball of radius $\nu_d/(1600d^3)$ contained in the time-dependent Markovian set. The centers remain homogeneously embeddable, although their neighboring channels are asserted only to admit time-dependent realizations. Thus the result gives a two-sided robust membership promise for rational Choi inputs and for infinitesimal divisibility. Membership in NP for general inputs, constant-precision hardness, and Lipschitz stability remain open. Finally, we characterize the compatible measurement instruments as positive decompositions of the correlation matrix; this constrains record responses without selecting a microscopic readout.

**Keywords:** quantum Markov dynamics; Lindblad embedding; time-dependent master equations; Schur channels; conditional positivity; computational complexity; quantum instruments.

# 1. Introduction

A channel describes the net transformation of a quantum system, whereas a master equation specifies a continuous dynamical realization. Determining whether the former admits the latter is a problem about both physical modeling and the geometry of completely positive maps. The distinction between a time-independent generator and a time-dependent one is essential: a sequence of admissible generators need not have an admissible logarithm.

This paper identifies a class in which that distinction disappears at the endpoint. Fix a complete orthogonal family of rank-one projections $P_0,\ldots,P_{d-1}$ on $\mathbb C^d$. A channel that fixes every $P_j$ is a Schur multiplier,

$$
\Phi_C(E_{ij})=C_{ij}E_{ij},\qquad C\succeq0,\quad C_{ii}=1.
\tag{1.1}
$$

Here $E_{ij}=|i\rangle\langle j|$. The diagonal probabilities are preserved, while off-diagonal coherences may decay and acquire phases. We call these maps **pointer-preserving channels**. The basis is prescribed; preservation of a basis at the endpoint does not initially impose preservation at intermediate times.

The central question is whether arbitrary time dependence enlarges the set of attainable channels in (1.1). Theorem 3.1 gives a negative answer for integrable generators on the same system space. Exact recovery of all pointer states forces them to remain mutually orthogonal and pure throughout the evolution. Their motion is therefore Hamiltonian. Removing that motion leaves commuting Schur generators, whose integral is an admissible logarithm of the endpoint.

This rigidity does not make the embedding problem computationally easy. The logarithm contains integer cycle choices constrained by a single global positive-semidefinite condition. We give an explicit reduction in which these choices encode a graph orientation with bounded weighted outdegree. The private two-dimensional blocks of the construction have fixed eigenvectors and two selectable eigenvalues. Their Schur complements convert logarithm branches into vertex loads without introducing off-diagonal interference between vertices.

Rigidity is an exact statement, and an exact statement does not by itself control channels that only approximately fix the pointers. Section 7 proves that the rigidity is stable. If a time-dependent Markovian channel is close to a coherent pointer-preserving channel, then a pointer-preserving Markovian channel is close to both, with constants polynomial in the dimension. The argument rests on the irreversibility of distinguishability. The total linear entropy remains small because distinguishability cannot be recovered. Its derivative controls noise variance up to an explicitly bounded nonunital correction. Orthogonalization enters this variance estimate quadratically, giving a square-root channel error and control of the frame motion. Stability converts hardness inside the pointer-preserving class into hardness against all time-dependent Markovian channels.

The results form the following sequence.

1. **Endpoint rigidity:** time-dependent and time-independent embedding are equivalent for pointer-preserving channels (Theorem 3.1).
2. **Invertible closure:** an invertible limit of integrable Lindblad endpoints is itself such an endpoint (Theorem 4.3).
3. **Strong hardness on a promised domain:** a fixed rational logarithmic alphabet suffices for strong NP-completeness on the promised logarithmic input domain, with a constant branch gap (Theorem 5.7).
4. **Constant separation inside the class:** every negative direction of a NO instance is supported on at most seven coordinates, which gives a dimension-independent separation from all embeddable pointer-preserving channels (Corollary 6.3). It survives a positivity-preserving conversion to rational correlation and Choi matrices (Theorem 6.4).
5. **Stability:** a uniform rounding theorem with exponent $1/2$ and constant $400d^{7/2}\log(2/c)$ (Theorem 7.6), which settles the quantitative question left open by Theorem 4.3.
6. **Robust hardness:** Theorem 8.1 gives a homogeneous-YES versus time-dependent-NO gap $\nu_d=(4\cdot10^{16}d^7)^{-1}$. Theorem 8.4 strengthens this to full-dimensional YES balls of radius $\nu_d/(1600d^3)$ and NO separation $3\nu_d/4$ after rational depolarizing regularization. The full YES balls are contained in the time-dependent and infinitesimally divisible sets; homogeneous embedding is asserted for their centers.

Cubitt, Eisert, and Wolf proved that deciding whether a channel is the exponential of a time-independent GKLS generator is NP-hard [1, Theorem 1], and that the classical embedding problem is NP-hard as well [1, Section 6], [17]. They restricted attention explicitly to time-independent generators [1, Section 1.1] and wrote that "the more general time-dependent problem is expected to be harder still" [17]. Later work states that these results "cannot directly be applied to the time-dependent case" [18, Section 1.2] and describes the characterization of time-dependent Markovian channels as a long-standing open problem [19]. Bausch and Cubitt determined the complexity of finite divisibility [20]; that question is different from the time-dependent one. Wolf and Cirac [2] relate infinitesimal divisibility to continuous completely positive evolution and establish determinant estimates used below.

For the class studied here, Helm, Strunz, Rietzler, and Würflinger characterize Markovian phase damping through conditional positivity, assuming that all fractional powers are again phase damping. They explicitly exclude "the rather peculiar case where some dynamics is phase damping for a particular time $t$ only" [10, Section IV]. Theorem 3.1 treats exactly that case, for arbitrary integrable time-dependent generators. The diagonal-noise structure of dephasing semigroups, including the triangle condition on dephasing frequencies, is treated by Fagnola et al. [3, Lemma 14, Remark 18 and Eq. (29)]. Our conditional-positivity preliminaries for Schur generators belong to this established theory; the passage from an unrestricted time-dependent path, or from an arbitrary non-Schur time-independent generator, to a Schur logarithm is the contribution of Theorem 3.1. Theorem 4.3 is the quantum counterpart of Johansen's characterization of embeddable stochastic matrices as limits of finite products [11, Theorem 2.4], whose proof uses Goodman's intrinsic time [12]; it makes rigorous a step that [2] uses without a compactness argument.

The complexity construction uses the weighted-orientation framework of Asahiro et al. [4, Section 5, Lemma 1 and Theorems 6--7]; the NP-hardness of At-most-3-SAT(2L) used there follows from problem [LO1] of Garey and Johnson [16]. Positive-semidefinite matrix signing already has a substantial complexity theory [5]; the present construction must additionally ensure that the entrywise exponential is a valid quantum channel, exclude every unintended logarithm branch, and preserve a channel-space separation under finite precision. These requirements are proved explicitly. No claim is made that matrix signing, weighted orientation, or homogeneous conditional positivity is new. Cubitt, Eisert, and Wolf obtained precision polynomial in the instance size and asked whether a construction with constant precision exists [1, Section 4.2]. Corollary 6.3 gives a constant entrywise gap inside the pointer-preserving class; Theorem 8.1 gives an inverse-polynomial gap against all time-dependent Markovian channels. Neither statement gives constant precision against the full Markovian set.

Shahbeigi et al. [21, Proposition 10 and Appendix D] obtain robust distinguishability and overlap constraints for homogeneous dynamics. The backward overlap estimate used here is the same data-processing principle. Our additional step controls integrated off-frame noise and moving frames to round an arbitrary integrable time-dependent endpoint to a Schur-embeddable channel, with polynomial dimensional dependence. Qualitative existence of Markovian interior points is already established in [1, Corollary 32]; the role of Section 8.2 is an explicit radius that preserves the reduction and its NO gap. We make no unrestricted priority claim for the terminology of Markovianity or its complexity.

Two further distinctions guide the interpretation. First, Theorem 8.1 has exact YES instances; Theorem 8.4 obtains an explicit interior/exterior promise by a further regularization. We state both norm balls and the admissible affine space, without importing convex-body equivalences for this nonconvex set. Second, an averaged channel does not select its measurement instrument. Section 9 gives a finite-rate example with the same dilation and different readouts. Independent variational results for possible record backgrounds are collected in Appendix B; they are not used elsewhere and do not constitute a microscopic derivation of the channels studied here.

# 2. Channels, logarithms, and conditional positivity

## 2.1. Conventions

Write $M_d$ for the complex $d\times d$ matrices. A channel is a completely positive, trace-preserving linear map on $M_d$. The Hilbert--Schmidt norm is $\|X\|_2$, the trace norm is $\|X\|_1$, and the operator norm of a matrix is $\|X\|_{\mathrm{op}}$. For a superoperator we use $\|T\|_{2\to2}$ and the diamond norm $\|T\|_\diamond$. All closures below are in a fixed finite dimension, so the choice of norm does not affect the closure.

A Gorini--Kossakowski--Lindblad--Sudarshan (GKLS) generator has the form

$$
\mathcal L(X)=-i[H,X]+\sum_\alpha\left(K_\alpha X K_\alpha^\dagger-\frac12\{K_\alpha^\dagger K_\alpha,X\}\right),\qquad H=H^\dagger.
\tag{2.1}
$$

Let $\mathfrak T_d$ denote the endpoints $\Lambda_1$ of

$$
\dot\Lambda_t=\mathcal L_t\Lambda_t,\qquad \Lambda_0=\mathrm{id},\qquad
\int_0^1\|\mathcal L_t\|_{2\to2}\,dt<\infty,
\tag{2.2}
$$

where $\mathcal L_t$ is measurable and GKLS almost everywhere. Solutions are understood in the Caratheodory sense. Piecewise-constant approximation gives completely positive propagators between every two times. Every endpoint in $\mathfrak T_d$ is invertible as a linear map, although its inverse need not be positive.

Let $\mathfrak R_d$ be the pointer-preserving channels in the prescribed basis. A matrix $C$ is a correlation matrix if it is positive semidefinite and has unit diagonal. The notation $\exp^{\circ}A$ means entrywise exponentiation; it is not a matrix exponential. Logarithms of $C$ below are also entrywise.

## 2.2. The Schur representation

**Lemma 2.1.** A channel fixes all $P_j$ if and only if it is $\Phi_C(X)=C\odot X$ for a correlation matrix $C$.

*Proof.* Let $\Phi(X)=\sum_\alpha V_\alpha XV_\alpha^\dagger$. If $\Phi(P_j)=P_j$, then

$$
\sum_\alpha |V_\alpha j\rangle\langle V_\alpha j|=P_j.
$$

Every summand is positive, so each vector $V_\alpha|j\rangle$ belongs to the one-dimensional range of $P_j$. Thus every $V_\alpha$ is diagonal. If its diagonal entries are $v_{\alpha j}$, then $C_{ij}=\sum_\alpha v_{\alpha i}\overline{v_{\alpha j}}$ is positive semidefinite, and trace preservation gives $C_{ii}=1$. Conversely, a Gram factorization of $C$ supplies diagonal Kraus operators. $\square$

A Hermitian matrix $\ell$ with zero diagonal is **conditionally positive semidefinite** (CPSD) when

$$
z^\dagger\ell z\ge0\qquad\text{for all }z\in\mathbb C^d\text{ with }\mathbf1^\dagger z=0.
\tag{2.3}
$$

Fix index $0$ and define the anchored matrix

$$
G_{ij}=\ell_{ij}-\ell_{i0}-\ell_{0j},\qquad 1\le i,j<d.
\tag{2.4}
$$

For $w\in\mathbb C^{d-1}$ and $z=(-\sum_iw_i,w_1,\ldots,w_{d-1})$, direct substitution gives

$$
z^\dagger\ell z=w^\dagger Gw.
\tag{2.5}
$$

Consequently $\ell$ is CPSD exactly when $G\succeq0$.

**Lemma 2.2 (explicit generator reconstruction).** If $\ell$ is Hermitian, zero-diagonal, and CPSD, then $\mathcal L_\ell(E_{ij})=\ell_{ij}E_{ij}$ is a GKLS generator.

*Proof.* Factor $G_{ij}=\sum_\alpha k_{\alpha i}\overline{k_{\alpha j}}$ and set $k_{\alpha0}=0$. The diagonal noise operators $K_\alpha=\operatorname{diag}(k_{\alpha0},\ldots,k_{\alpha,d-1})$ produce coefficients

$$
g_{ij}=G_{ij}-\frac{G_{ii}+G_{jj}}2,
\qquad g_{i0}=-\frac{G_{ii}}2.
\tag{2.6}
$$

Here the formula extends $G$ by a zero anchor row and column. Put $a_i=\operatorname{Im}\ell_{i0}$ and $a_0=0$. Since $G_{ii}=-2\operatorname{Re}\ell_{i0}$, (2.4) implies

$$
\ell_{ij}=g_{ij}+i(a_i-a_j).
\tag{2.7}
$$

The last term is the Hamiltonian contribution of $H=-\operatorname{diag}(a_i)$. Hence (2.1) gives the required generator. $\square$

Conversely, a zero-diagonal Hermitian Schur generator must satisfy (2.3): differentiate $z^\dagger\exp^{\circ}(t\ell)z\ge0$ at $t=0$ for $z\perp\mathbf1$. Thus the homogeneous Schur embedding condition is the existence of a CPSD logarithm. The next section proves that an arbitrary time-dependent realization of a pointer-preserving endpoint satisfies exactly this same condition.

# 3. Endpoint rigidity

**Theorem 3.1 (time dependence does not enlarge the endpoint class).** For a correlation matrix $C$, the following statements are equivalent:

(i) $\Phi_C\in\mathfrak T_d$;

(ii) $\Phi_C=e^{\mathcal L}$ for some time-independent GKLS generator;

(iii) there is a Hermitian zero-diagonal CPSD matrix $\ell$ with $e^{\ell_{ij}}=C_{ij}$ for all $i,j$.

In particular, an embeddable $C$ has no zero entries.

*Proof.* Lemma 2.2 gives (iii)$\Rightarrow$(ii), and (ii)$\Rightarrow$(i) is immediate. Assume (i) and set $\rho_j(t)=\Lambda_t(P_j)$.

**Step 1: all intermediate pointers are pure and orthogonal.** For $j\ne k$, contractivity of the trace norm under the remaining propagator gives

$$
2=\|P_j-P_k\|_1
\le\|\rho_j(t)-\rho_k(t)\|_1\le2.
\tag{3.1}
$$

Equality in the distinguishability bound for density matrices means that their supports are orthogonal. There are $d$ nonzero mutually orthogonal supports in a $d$-dimensional space. Each therefore has rank one. Write $\rho_j(t)=|\psi_j(t)\rangle\langle\psi_j(t)|$, where the $\psi_j(t)$ form an orthonormal basis.

**Step 2: the noise is diagonal in the moving basis.** Choose a fixed Hilbert--Schmidt orthonormal traceless operator basis and use the canonical GKLS coefficient matrix $A_t\succeq0$. Its entries and the traceless Hamiltonian are linear functions of $\mathcal L_t$, hence measurable and integrable. A measurable square root of $A_t$ supplies noise operators with integrable squared Hilbert--Schmidt norms. Since $\operatorname{tr}\rho_j(t)^2=1$, almost everywhere

$$
0=\frac{d}{dt}\operatorname{tr}\rho_j^2
=-2\sum_\alpha\left\|(K_\alpha-\langle\psi_j,K_\alpha\psi_j\rangle)\psi_j\right\|^2.
\tag{3.2}
$$

Every summand vanishes. Each $K_\alpha$ is diagonal in the complete orthonormal basis $\{\psi_j(t)\}$ and is therefore normal. Its dissipator vanishes on every $\rho_j(t)$. It follows that

$$
\dot\rho_j=-i[H_t,\rho_j].
\tag{3.3}
$$

**Step 3: remove the Hamiltonian motion.** Let $\dot W_t=-iH_tW_t$, $W_0=I$. Uniqueness in (3.3) gives $\rho_j(t)=W_tP_jW_t^\dagger$. The transformed evolution $\widetilde\Lambda_t=\operatorname{Ad}_{W_t^\dagger}\circ\Lambda_t$ has diagonal noise operators and no Hamiltonian term. Its Schur coefficients are

$$
g_{ij}(t)=\sum_\alpha\left[k_{\alpha i}(t)\overline{k_{\alpha j}(t)}-\frac{|k_{\alpha i}(t)|^2+|k_{\alpha j}(t)|^2}{2}\right].
\tag{3.4}
$$

For $z\perp\mathbf1$,

$$
z^\dagger g(t)z=\sum_\alpha\left|\sum_i\overline{z_i}k_{\alpha i}(t)\right|^2\ge0.
\tag{3.5}
$$

The coefficients are integrable. Schur generators commute at different times, so

$$
\widetilde\Lambda_1(E_{ij})=\exp\left(\int_0^1g_{ij}(t)\,dt\right)E_{ij}.
\tag{3.6}
$$

**Step 4: restore the endpoint phase.** Both the original endpoint and $\widetilde\Lambda_1$ fix the prescribed pointers. Hence $W_1$ is diagonal, say $W_1=\operatorname{diag}(e^{i\vartheta_j})$. Therefore

$$
\ell_{ij}=\int_0^1g_{ij}(t)\,dt+i(\vartheta_i-\vartheta_j)
\tag{3.7}
$$

is a logarithm of $C_{ij}$. The integral is CPSD by (3.5), and the phase-difference term vanishes as a quadratic form on $\mathbf1^\perp$. This proves (iii). $\square$

The theorem constrains the endpoint, not the original path: the intermediate basis may rotate arbitrarily under an integrable Hamiltonian. It also requires a complete rank-one pointer family in the same system dimension. Enlarging the dynamically retained system by an environment changes the problem.

## 3.1. Integer cycles and elementary cases

Represent nonzero off-diagonal entries by rational logarithmic data when available,

$$
C_{ij}=\exp\{\pi(-\beta_{ij}+i\theta_{ij})\},\qquad
\beta_{ji}=\beta_{ij},\quad\theta_{ji}=-\theta_{ij}.
\tag{3.8}
$$

After absorbing anchor branch choices into a diagonal Hamiltonian, the anchored condition becomes

$$
G_{\mathrm{phys}}(K)=\pi\widehat G(K),\qquad
\widehat G(K)=Q+i(\Theta+2K)\succeq0,
\tag{3.9}
$$

where $K$ is an integer skew-symmetric $(d-1)\times(d-1)$ matrix and

$$
\begin{aligned}
Q_{ii}&=2\beta_{i0},& Q_{ij}&=\beta_{i0}+\beta_{j0}-\beta_{ij},\\
\Theta_{ij}&=\theta_{ij}-\theta_{i0}+\theta_{j0}.&&
\end{aligned}
\tag{3.10}
$$

The integer variables describe cycle branches of homogeneous Schur logarithms under a fixed unit-time convention. They do not classify all time-dependent paths or select a physical time unit.

For three pointers, write $\ell_{10}=-a+i\nu_{10}$, $\ell_{20}=-b+i\nu_{20}$, and $\ell_{12}=-c+i\nu_{12}$. With $\Omega=\nu_{12}+\nu_{20}+\nu_{01}$, (2.4) is

$$
G=\begin{pmatrix}2a&a+b-c+i\Omega\\a+b-c-i\Omega&2b\end{pmatrix}.
\tag{3.11}
$$

Thus a branch is admissible precisely when $a,b\ge0$ and

$$
\Omega^2\le4ab-(a+b-c)^2.
\tag{3.12}
$$

For positive real $C$, every logarithm has real part $\log^{\circ}C$. Its imaginary part is skew-symmetric and contributes zero on real vectors. Consequently $C$ is embeddable if and only if the real principal logarithm is CPSD. The same conclusion holds after removing an endpoint diagonal-unitary phase factor.

An arbitrary YES input need not have a positive spectral margin. For example, $\beta_{10}=\beta_{20}=1/2$, $\beta_{12}=2$, and $\theta=0$ give

$$
\widehat G(k)=\begin{pmatrix}1&-1+2ik\\-1-2ik&1\end{pmatrix},\qquad
\lambda_{\min}(\widehat G(k))=1-\sqrt{1+4k^2}.
\tag{3.13}
$$

The branch $k=0$ is positive semidefinite and therefore defines a valid embeddable channel, but no branch has a strictly positive margin. The gaps proved in Sections 5 and 6 are properties of the reduction family.

# 4. Closure and a local-to-global obstruction

## 4.1. A determinant-controlled realization

The determinant below is the determinant of the $d^2$-dimensional superoperator. The following estimate turns an endpoint constraint into a bound on an alternative realizing generator.

**Lemma 4.1.** If $T\in\mathfrak T_d$ and $\det T\ge\eta>0$, then $T$ has a realization on $[0,1]$ satisfying

$$
\|\mathcal L_t\|_{2\to2}\le B(d,\eta)
:=\max\left\{2\left(1-\frac2d\log\eta\right),4\pi\right\}
\quad\text{almost everywhere}.
\tag{4.1}
$$

*Proof.* Use the canonical traceless representation $\mathcal L_t=-i[H_t,\cdot]+\mathcal D_{A_t}$ with $A_t\succeq0$, and remove $H_t$ in the interaction picture. For a Hilbert--Schmidt normalized traceless $F$, the superoperator trace of $\mathcal D[F]$ is $-d$, and

$$
\|\mathcal D[F]\|_{2\to2}\le2\|F\|_{\mathrm{op}}^2\le2.
$$

Diagonalizing $A_t$ and applying Liouville's formula yields the determinant identity and norm estimate underlying [2, Theorem 6]:

$$
\log\det T=-d\int_0^1\operatorname{tr}A_t\,dt,\qquad
a:=\int_0^1\|\mathcal D'_t\|_{2\to2}\,dt\le-\frac2d\log\det T.
\tag{4.2}
$$

Write $T=\operatorname{Ad}_{U_1}\circ X_1$, where $\dot X_t=\mathcal D'_tX_t$. The increasing, absolutely continuous change of variable

$$
s(t)=\frac{t+\int_0^t\|\mathcal D'_r\|_{2\to2}\,dr}{1+a}
\tag{4.3}
$$

has a Lipschitz inverse. The reparametrized dissipative generator is bounded by $1+a$. Execute that path at twice the speed on the first half of $[0,1]$. Choose a Hermitian logarithm $U_1=e^{-iK}$ with $\|K\|_{\mathrm{op}}\le\pi$, and execute $-2i[K,\cdot]$ on the second half. This restores exactly $T$ and has norm at most $4\pi$. Equation (4.1) follows. $\square$

The construction preserves only the endpoint. It does not preserve the original timing, Hamiltonian history, or physical clock.

**Lemma 4.2.** For fixed $d$ and $B$, endpoints of GKLS paths with $\|\mathcal L_t\|_{2\to2}\le B$ form a compact set.

*Proof.* The GKLS cone intersected with the closed norm ball is compact and convex. The associated bounded $L^\infty$ controls are weak-* compact; separability of $L^1([0,1])$ permits subsequence extraction. Their CPTP solutions satisfy

$$
\|\Lambda_t\|_{2\to2}\le\sqrt d,\qquad
\|\dot\Lambda_t\|_{2\to2}\le B\sqrt d.
\tag{4.4}
$$

Arzela--Ascoli gives uniform convergence along a subsequence, while the generators converge weak-*. In the integral equation, decompose

$$
\mathcal L_n\Lambda_n-\mathcal L\Lambda
=\mathcal L_n(\Lambda_n-\Lambda)+(\mathcal L_n-\mathcal L)\Lambda.
\tag{4.5}
$$

The first term tends to zero in integral norm. Testing weak-* convergence against each matrix entry of $\Lambda(t)\mathbf1_{[0,s]}(t)$ handles the second. The limiting control remains in the closed convex GKLS ball and generates the uniform limit. Thus the endpoint set is closed and bounded. $\square$

**Theorem 4.3 (relative closure at invertible endpoints).** With $GL(M_d)$ denoting the invertible linear maps on $M_d$,

$$
\overline{\mathfrak T_d}\cap GL(M_d)=\mathfrak T_d.
\tag{4.6}
$$

*Proof.* If $T_n\to T\in GL(M_d)$ with $T_n\in\mathfrak T_d$, then $\det T_n>0$ and continuity implies $\det T>0$. Eventually $\det T_n\ge\eta>0$. Lemma 4.1 replaces the realizations by uniformly bounded ones, and Lemma 4.2 gives $T\in\mathfrak T_d$. The reverse inclusion holds because every solution of (2.2) is invertible. $\square$

Let $\mathcal I_d$ denote the infinitesimally divisible channels: those admitting, for every $\varepsilon>0$, a finite factorization into channels at distance at most $\varepsilon$ from the identity. The closure of finite products of Markov semigroups equals $\overline{\mathfrak T_d}$ by piecewise-constant approximation. The Markov-product characterization of infinitesimal divisibility in [2, Definition 14 and Theorem 16] therefore gives, on the invertible pointer-preserving locus,

$$
\overline{\mathcal I_d}\cap\mathfrak R_d\cap GL(M_d)
=\{\Phi_C:C\text{ has a CPSD logarithm}\}.
\tag{4.7}
$$

The approximating channels in (4.7) need not preserve the pointer basis.

Invertibility cannot be dropped. For the dephasing projection $\mathcal D(X)=\sum_jP_jXP_j$,

$$
e^{n(\mathcal D-\mathrm{id})}=\mathcal D+e^{-n}(\mathrm{id}-\mathcal D)\longrightarrow\mathcal D.
\tag{4.8}
$$

The limit is singular and hence cannot be an integrable endpoint. Thus the result is relative closure, not closedness of $\mathfrak T_d$ in the entire channel space.

## 4.2. Compatible proper subchannels do not imply a global embedding

**Theorem 4.4.** For every $d\ge3$ there is an invertible pointer-preserving channel such that all proper coordinate restrictions admit mutually compatible homogeneous Markov flows, but the full channel lies outside $\overline{\mathfrak T_d}$.

*Proof.* Choose a real unit vector $v\perp\mathbf1$ with no zero coordinate, and put

$$
\begin{gathered}
P=I-\mathbf1\mathbf1^T/d,\qquad
b=\min_j\frac{v_j^2}{1-1/d},\qquad
1<\alpha<\frac1{1-b},\\
B=P-\alpha vv^T,\qquad
\Gamma_{ij}=\frac{B_{ii}+B_{jj}}2-B_{ij},\qquad
\zeta=1-\alpha(1-b)>0.
\end{gathered}
\tag{4.9}
$$

If $z\perp\mathbf1$ and $z_j=0$, then $z\perp Pe_j$. Projection of $v$ onto that hyperplane gives

$$
|v^\dagger z|^2\le\left(1-\frac{v_j^2}{1-1/d}\right)\|z\|_2^2,
\qquad z^\dagger Bz\ge\zeta\|z\|_2^2.
\tag{4.10}
$$

Since $P\Gamma P=-B$, every proper coordinate restriction of $-\tau\Gamma$ is CPSD. In particular $\Gamma_{ij}\ge\zeta>0$ for $i\ne j$, by using $e_i-e_j$ in (4.10). Choose

$$
\tau\ge\frac{\log(2(d-1))}{\min_{i\ne j}\Gamma_{ij}},\qquad
C_{ij}=e^{-\tau\Gamma_{ij}}.
\tag{4.11}
$$

Every off-diagonal row sum of $C$ is at most $1/2$, so $C\succ0$. All its entries are nonzero, and therefore $\Phi_C$ is invertible. For every proper $S$, the matrices $\exp^{\circ}(-t\tau\Gamma_S)$ are correlation matrices for all $t\ge0$ by Lemma 2.2. Their restrictions agree on all overlaps.

However, every Hermitian logarithm of $C$ has real part $-\tau\Gamma$. Its imaginary part contributes zero on the real vector $v$, and

$$
v^\dagger\ell v=\tau v^TBv=\tau(1-\alpha)<0.
\tag{4.12}
$$

No branch is CPSD. Theorems 3.1 and 4.3 exclude both embedding and approximation by arbitrary channels in $\mathfrak T_d$. $\square$

The restrictions are coordinate subchannels in the prescribed basis, not arbitrary rotated subspaces or tensor subsystems. The obstruction concerns the sufficiency of compatible partial tests.

For an explicit example, take $d=11$; this dimension is chosen only because it admits a two-block vector with small integer entries, and nothing below depends on it. Let

$$
v=\frac{(6,6,6,6,6,-5,-5,-5,-5,-5,-5)}{\sqrt{330}},
\qquad\alpha=\frac{23}{22},\qquad\tau=4.
\tag{4.13}
$$

Then $\Gamma_{ij}=1$ within each block and $97/120$ across blocks. The two nontrivial coherence values are $r=e^{-4}$ and $s=e^{-97/30}$. The global logarithmic witness and every proper conditional margin obey

$$
v^T(\log^{\circ}C)v=-\frac2{11},\qquad
\lambda_{\min}\left((\log^{\circ}C)_S\big|_{\mathbf1_S^\perp}\right)\ge\frac16.
\tag{4.14}
$$

The second inequality follows directly from (4.10), since $b=1/12$ and $4\zeta=1/6$. A Hermitian zero-diagonal logarithmic perturbation $E$ with $\|E\|_{\max}\le0.01$ preserves positivity of the endpoint and satisfies

$$
\begin{aligned}
\lambda_{\min}(C')&\ge1-10e^{-97/30+0.01}>0,\\
\lambda_{\min}\left((\log^{\circ}C+E)_S\big|_{\mathbf1_S^\perp}\right)&\ge\frac1{15},\\
v^T\operatorname{Re}(\log^{\circ}C+E)v&\le-\frac4{55},
\end{aligned}
\tag{4.15}
$$

where $C'=\exp^{\circ}(\log^{\circ}C+E)$. These are explicit bounds inside the Schur class. The qualitative distance from all of $\mathfrak T_{11}$ follows separately from closure; (4.15) does not quantify that larger-space distance.

For two blocks of sizes $p,q\ge2$, with within-block log attenuation $a$ and cross-block attenuation $b$, decomposition into block means and zero-mean parts gives the exact embedding threshold

$$
\frac ba\ge1-\frac{p+q}{2pq}.
\tag{4.16}
$$

This is the same negative-type threshold as the complete bipartite metric calculation in Sanchez [6, Theorem 3.1]. The underlying two-block geometry is thus an application of known negative-type theory. Its role here is an explicit channel obstruction, including exclusion of time-dependent embedding and of invertible Markovian limits.

# 5. A bounded-degree reduction with a constant logarithmic gap

## 5.1. The exact logarithmic input problem

The input consists of $d$ and rational data $\beta_{ij}>0$, $\theta_{ij}$ for $i<j$, extended as in (3.8). It is promised that the entrywise exponential is a correlation matrix. The decision is whether $\Phi_C\in\mathfrak T_d$. The channel need not have rational entries; its finite description is the rational logarithmic data. Reductions to this problem must satisfy the correlation-matrix promise on both YES and NO outputs.

**Proposition 5.1 (membership in NP on the promised domain).** A polynomial-size certificate is an integer skew-symmetric matrix $K$ satisfying (3.9).

*Proof.* Positivity of every $2\times2$ principal submatrix gives

$$
|\Theta_{ij}+2K_{ij}|\le\sqrt{Q_{ii}Q_{jj}},\qquad
2|K_{ij}|\le|\Theta_{ij}|+\sqrt{Q_{ii}Q_{jj}}.
\tag{5.1}
$$

The right side bounds the bit length of each integer by a polynomial in the input length. The resulting Hermitian matrix is over $\mathbb Q(i)$; exact Hermitian elimination, with the zero-pivot case handled by its zero-row requirement, tests positive semidefiniteness in polynomial time. Theorem 3.1 establishes the certificate's equivalence to embedding. $\square$

We next prove hardness directly in a fixed-alphabet subfamily. This simultaneously supplies the finite-precision result and avoids relying on coherences that decay with the input size.

## 5.2. Weighted orientation at maximum degree three

A weighted orientation assigns each edge of a simple graph to its tail. Its load at a vertex is the sum of weights of edges directed out of that vertex. All weights below belong to $\{1,2\}$.

**Lemma 5.2.** Deciding whether every vertex can have load at most $2$ is NP-hard even for simple graphs of maximum unweighted degree $3$.

*Proof.* Use At-most-3-SAT(2L): every clause has one to three literals and each literal occurs at most twice. Its hardness and the weighted-orientation reduction are given in [4, Lemma 1 and Theorems 6--7]. The following private-triangle implementation makes the degree bound explicit.

For each variable, make a positive-literal vertex, a negative-literal vertex, and a weight-$2$ edge between them. Connect each clause vertex to its literal vertices with weight-$1$ edges. For a clause of length $r=1$ or $2$, add a private triangle of three weight-$2$ edges, and join the clause by weight-$1$ edges to $3-r$ distinct triangle vertices. A length-$3$ clause requires no triangle. Duplicate literals are removed, tautological clauses discarded, and empty instances handled directly. These operations do not increase literal multiplicities.

Every clause vertex has degree $3$. A literal vertex has its variable edge and at most two clause edges. A triangle vertex has its two triangle edges and at most one clause attachment. The graph is therefore simple with maximum degree $3$.

Under capacity $2$, the triangle's three weight-$2$ edges must form a directed cycle. Hence each attachment points from the clause into the triangle. On a variable edge, call the tail literal false and the head literal true. A false literal has exhausted its capacity and cannot send an edge to a clause. A clause has three unit-weight incident edges and can send at most two; at least one literal must therefore send an edge into it, certifying a true literal.

Conversely, given a satisfying truth assignment, direct each variable edge from its false literal to its true literal. In each clause choose one true literal to send an edge into the clause and direct its other incident edges outward. The private triangles are directed cycles. A true literal sends at most two clause edges because it appears at most twice. All loads are at most $2$. $\square$

The private triangle is a local implementation of the source reduction, not a claim of an independent new graph-complexity theorem.

## 5.3. The logarithmic gadget

Let $H=(V,E)$ be the graph from Lemma 5.2, let $w_e\in\{1,2\}$, and set

$$
t=\frac1{13},\qquad W_v=\sum_{e\ni v}w_e\le6,\qquad
h_v=\frac{14}{15}t^2(W_v+35).
\tag{5.2}
$$

There is one anchor $0$, one index for each $v\in V$, and two private indices $p_e,q_e$ for each edge. Thus $d=1+|V|+2|E|$. On the nonanchor indices define a Hermitian matrix $\widehat G$ by

$$
\widehat G_{vv}=h_v,\qquad
\widehat G_{p_ep_e}=\widehat G_{q_eq_e}=\frac87,\qquad
\widehat G_{p_eq_e}=i.
\tag{5.3}
$$

For $e=\{a,b\}$ with a fixed ordering $a<b$, put

$$
\begin{pmatrix}\widehat G_{p_ea}\\\widehat G_{q_ea}\end{pmatrix}
=x_e\begin{pmatrix}1\\-i\end{pmatrix},\qquad
\begin{pmatrix}\widehat G_{p_eb}\\\widehat G_{q_eb}\end{pmatrix}
=x_e\begin{pmatrix}1\\i\end{pmatrix},\qquad
x_e=\begin{cases}t,&w_e=1,\\t(1+i),&w_e=2.\end{cases}
\tag{5.4}
$$

All other off-diagonal entries vanish. In particular $|x_e|^2=w_et^2$ exactly. Define the rational logarithmic input by

$$
\begin{aligned}
\beta_{i0}&=\widehat G_{ii}/2,&\theta_{i0}&=0,\\
\beta_{ij}&=(\widehat G_{ii}+\widehat G_{jj})/2-\operatorname{Re}\widehat G_{ij},&
\theta_{ij}&=\operatorname{Im}\widehat G_{ij}.
\end{aligned}
\tag{5.5}
$$

All attenuations are positive. The anchored logarithm is $\pi\widehat G$, and every branch is $\pi(\widehat G+2iK)$. Equations (5.2)--(5.5) use a fixed finite set of Gaussian rational numbers, independent of $|V|$ and $|E|$. The channel is independent of the integer branch.

**Lemma 5.3 (exclusion of unintended branches).** If $\widehat G+2iK$ is positive semidefinite, then its only branch choices are

$$
\widehat G_{p_eq_e}=is_e,\qquad s_e\in\{-1,1\}.
\tag{5.6}
$$

Every other branch has a minimum eigenvalue less than $-0.72$.

*Proof.* All diagonal entries are at most $8/7$. On a private pair, any odd imaginary value other than $\pm1$ has magnitude at least $3$. On every other entry, a nonzero integer shift has magnitude at least $2-\sqrt2t$. The smaller eigenvalue of the corresponding $2\times2$ principal submatrix is at most the average diagonal minus the off-diagonal modulus, hence at most

$$
\frac87-\left(2-\frac{\sqrt2}{13}\right)<-0.72.
\tag{5.7}
$$

Interlacing excludes the full matrix. $\square$

## 5.4. The exact load identity

**Lemma 5.4 (eigenvector attachment).** For each edge, the private block

$$
P_e(s)=\begin{pmatrix}8/7&is\\-is&8/7\end{pmatrix}
\tag{5.8}
$$

has eigenvectors $(1,-i)^T$ and $(1,i)^T$ with eigenvalues $8/7+s$ and $8/7-s$. If $B_e$ denotes the two columns in (5.4), then

$$
B_e^\dagger P_e(s)^{-1}B_e
=\operatorname{diag}\left(\frac{2w_et^2}{8/7+s},\frac{2w_et^2}{8/7-s}\right).
\tag{5.9}
$$

*Proof.* Multiply $P_e(s)$ by the two orthogonal attachment vectors. Their orthogonality eliminates the off-diagonal Schur-complement entry, and their squared norms are $2|x_e|^2$. $\square$

For either sign, one endpoint incurs $14w_et^2$ and the other incurs $(14/15)w_et^2$. Assign the edge to the endpoint receiving the larger contribution, and call the resulting integer load $o_s(v)$. Eliminating all private blocks gives a diagonal Schur complement:

$$
\begin{aligned}
L_v(s)&=\frac{14}{15}t^2\bigl(W_v+14o_s(v)\bigr),\\
h_v-L_v(s)&=\frac{14}{15}t^2\bigl(35-14o_s(v)\bigr).
\end{aligned}
\tag{5.10}
$$

Therefore

$$
\widehat G(s)\succeq0
\quad\Longleftrightarrow\quad
o_s(v)\le\frac52\text{ for all }v
\quad\Longleftrightarrow\quad
o_s(v)\le2\text{ for all }v.
\tag{5.11}
$$

No graph-cycle interference term remains. This is the reason for attaching the two endpoints along different, sign-independent eigenvectors.

## 5.5. A uniform spectral gap

**Lemma 5.5.** Set $\gamma_0=11/1690$. A feasible orientation gives a branch with $\lambda_{\min}(\widehat G)\ge\gamma_0$. If no feasible orientation exists, every branch satisfies $\lambda_{\min}(\widehat G)\le-\gamma_0$.

*Proof.* In the YES case the diagonal Schur residual in (5.10) is at least

$$
m=\frac{98}{15}t^2.
\tag{5.12}
$$

Let $q=\gamma_0=(11/10)t^2$. Every private eigenvalue is at least $1/7$, and $q\le1/14$, so

$$
(P_e-qI)^{-1}\preceq(1+14q)P_e^{-1}.
\tag{5.13}
$$

The private blocks remain positive, and their eigenvectors are unchanged. The shifted Schur residual is thus at least

$$
m-q(1+14h_{\max}),\qquad
h_{\max}=\frac{14\cdot41}{15\cdot169}.
\tag{5.14}
$$

The expression in (5.14) equals $49339/4284150>0$. Hence $\widehat G-qI\succeq0$.

In the NO case, every sign assignment has a vertex $v$ with $o_s(v)\ge3$. In block notation, with private block matrix $P$ and attachment matrix $B$, use the vector

$$
z=\begin{pmatrix}e_v\\-P^{-1}Be_v\end{pmatrix}.
\tag{5.15}
$$

It has $z^\dagger\widehat Gz=h_v-L_v\le-m$. Each incident edge contributes at most $98w_et^2\le196t^2$ to the squared norm of its private component. Since the degree is at most $3$,

$$
\|z\|_2^2\le1+588t^2=\frac{757}{169},\qquad
\frac{z^\dagger\widehat Gz}{\|z\|_2^2}
\le-\frac{98}{11355}<-\frac{11}{1690}.
\tag{5.16}
$$

Lemma 5.3 handles all other integer branches. $\square$

In physical logarithmic units the margin is

$$
\gamma=\pi\gamma_0=\frac{11\pi}{1690}.
\tag{5.17}
$$

The factor $\pi$ is essential when converting logarithmic gaps to channel-entry distances.

## 5.6. Positivity of the channel on every input

The matrix $\widehat G$ is not positive semidefinite on a NO instance. Positivity of its entrywise exponential therefore needs a separate argument.

**Lemma 5.6.** The construction (5.5) always yields a positive-definite correlation matrix, and every coherence satisfies

$$
|C_{ij}|\ge c_*:=e^{-8\pi/7}>\frac1{40}.
\tag{5.18}
$$

*Proof.* Let $D=\operatorname{diag}(e^{-\pi\widehat G_{ii}/2})$ on the nonanchor indices, and let $\mathbf1$ have the corresponding length. Then

$$
C=\begin{pmatrix}1&\mathbf1^TD\\D\mathbf1&D\exp^{\circ}(\pi\widehat G)D\end{pmatrix}.
\tag{5.19}
$$

Its Schur complement at the anchor is $DZD$, where

$$
Z=\exp^{\circ}(\pi\widehat G)-\mathbf1\mathbf1^T.
\tag{5.20}
$$

Zero entries of $\widehat G$ become zero entries of $Z$. Thus $Z$ has exactly the same attachment pattern. Its private blocks are

$$
R_e=\begin{pmatrix}e^{8\pi/7}-1&-2\\-2&e^{8\pi/7}-1\end{pmatrix},\qquad
R_e\succeq r_*I,\quad r_*=e^{8\pi/7}-3>33.
\tag{5.21}
$$

Every attachment entry is $e^z-1$ with $|z|\le\pi\sqrt{w_e}t$, and hence

$$
|e^z-1|\le|z|e^{|z|}.
\tag{5.22}
$$

The sum of absolute entries in either row of the two-endpoint Schur contribution is bounded by

$$
\kappa_*w_et^2,\qquad
\kappa_*:=\frac{4\pi^2e^{2\pi\sqrt2/11}}{r_*}<\frac{27}{10}.
\tag{5.23}
$$

Indeed, each attachment column has norm at most $\sqrt2\pi\sqrt{w_e}t\,e^{\pi\sqrt2/11}$; apply Cauchy--Schwarz and $\|R_e^{-1}\|\le r_*^{-1}$ to both entries of a row. The convenient bound with $1/11$ is larger than the actual value $t=1/13$.

For completeness, the strict constants need no floating-point assumption. The inequalities $157/50<\pi<22/7$, $\sqrt2<99/70$, $e^{2\pi\sqrt2/11}<9/4$, and $e^{8\pi/7}>36$ imply

$$
\kappa_*<\frac{4(22/7)^2(9/4)}{33}=\frac{1452}{539}<\frac{27}{10}.
\tag{5.24}
$$

The two exponential bounds follow from rational Taylor bounds: the degree-$14$ sum for $e^{628/175}$ exceeds $36$, while the degree-$14$ sum for $e^{198/245}$ plus its geometric tail is below $9/4$.

At vertex $v$, the diagonal of $Z$ satisfies

$$
e^{\pi h_v}-1\ge\pi h_v
=\frac{14\pi}{15}t^2(W_v+35)
>\kappa_*t^2W_v.
\tag{5.25}
$$

After eliminating the positive private blocks, (5.25) gives strict Hermitian diagonal dominance. Thus $Z\succ0$ and $C\succ0$.

Finally,

$$
|C_{ij}|=\exp\left[-\pi\left(\frac{\widehat G_{ii}+\widehat G_{jj}}2-\operatorname{Re}\widehat G_{ij}\right)\right].
\tag{5.26}
$$

For two private indices the attenuation is at most $8/7$. For two vertices it is at most $h_{\max}<8/7$. For a vertex and a private index it is at most $(h_{\max}+8/7)/2+t<8/7$, and anchor attenuations are also smaller. This proves (5.18). $\square$

Lemma 5.6 asserts $C\succ0$ but no lower bound on $\lambda_{\min}(C)$ that is uniform in $d$. Finite computations show that $\lambda_{\min}(C)$ decreases with the dimension (for example to about $0.015$ at $d=241$). None of the subsequent arguments uses a uniform spectral lower bound for $C$.

**Theorem 5.7 (fixed-alphabet exact hardness).** On the promised logarithmic input domain of Section 5.1, pointer-preserving Markovian embedding is NP-complete under promise-preserving polynomial reductions. Its hardness already holds when the rational logarithmic coefficients belong to a fixed finite alphabet, so it is strong in the numerical-encoding sense. On the reduction family:

$$
\begin{array}{ll}
\mathrm{YES}:&\exists K\quad\lambda_{\min}(G_{\mathrm{phys}}(K))\ge\gamma,\\[2pt]
\mathrm{NO}:&\forall K\quad\lambda_{\min}(G_{\mathrm{phys}}(K))\le-\gamma,
\end{array}
\qquad \gamma=\frac{11\pi}{1690},\quad |C_{ij}|\ge c_*.
\tag{5.27}
$$

*Proof.* Proposition 5.1 gives membership. Lemma 5.2 gives a polynomial reduction to degree-three orientation, (5.11) identifies its answer with branch positivity, and Lemma 5.3 excludes all extra branches. Lemma 5.6 ensures that the channel promise holds on every output. Lemma 5.5 supplies (5.27). The number of indices is linear in the graph size; only the dimension grows, not the coefficient alphabet. Apply Theorem 3.1. $\square$

The statement concerns a family with unbounded dimension. It does not assert hardness at a fixed dimension, such as the eleven-dimensional example in Section 4, and it does not turn a promised transcendental channel representation into exact rational channel data. The latter requires the construction in the next section.

# 6. Channel-space separation and rational input

## 6.1. From a logarithmic gap to an entrywise distance

For correlation matrices use $\|C-D\|_{\max}=\max_{ij}|C_{ij}-D_{ij}|$.

**Lemma 6.1 (logarithmic perturbation).** Suppose $\min_{ij}|C_{ij}|\ge c_0>0$ and every physical anchored logarithm of $C$ has minimum eigenvalue at most $-\gamma$. Then every embeddable pointer-preserving $D$ satisfies

$$
\|C-D\|_{\max}\ge
\min\left\{\frac{c_0}{2},\frac{\gamma c_0}{6(d-1)}\right\}.
\tag{6.1}
$$

If instead some branch of $C$ has minimum eigenvalue at least $\gamma$, every correlation matrix sufficiently close by the strict inequality in (6.1) is embeddable.

*Proof.* Set $\delta=\|C-D\|_{\max}<c_0/2$. Then $D$ has no zero entry, and the principal logarithm near $1$ satisfies

$$
\left|\operatorname{Log}\frac{D_{ij}}{C_{ij}}\right|\le\frac{2\delta}{c_0}.
\tag{6.2}
$$

If $\ell_D$ is a CPSD logarithm of $D$, define

$$
(\ell_C)_{ij}=(\ell_D)_{ij}-\operatorname{Log}(D_{ij}/C_{ij}).
\tag{6.3}
$$

It is a Hermitian zero-diagonal logarithm of $C$. Each anchored entry is a sum of three logarithmic terms, so

$$
\|G_C-G_D\|_{\mathrm{op}}
\le\frac{6(d-1)\delta}{c_0}.
\tag{6.4}
$$

Because $G_D\succeq0$, Weyl's inequality contradicts the assumed negative margin if the right side is smaller than $\gamma$. The positive-margin case follows by starting with the admissible logarithm of $C$ and adding the same local logarithmic perturbation. $\square$

Entrywise separation also bounds channel distance. Applying $\Phi_C-\Phi_D$ to $|+_{ij}\rangle\langle+_{ij}|$, with $|+_{ij}\rangle=(|i\rangle+|j\rangle)/\sqrt2$, gives

$$
\|\Phi_C-\Phi_D\|_\diamond\ge|C_{ij}-D_{ij}|.
\tag{6.5}
$$

Lemma 6.1 alone gives an inverse-linear radius. With $\gamma=11\pi/1690$ and $c_0=c_*$ it yields, for every NO output of Theorem 5.7 and every $\Phi_D\in\mathfrak R_d\cap\mathfrak T_d$,

$$
\|C-D\|_{\max}\ge\varepsilon_d:=\frac{11\pi e^{-8\pi/7}}{10140(d-1)},
\qquad \varepsilon_d\approx\frac{9.40194\times10^{-5}}{d-1}.
\tag{6.6}
$$

On YES outputs, the same radius $\varepsilon_d$ is an embeddable neighborhood relative to correlation matrices. The factor $d-1$ in (6.4) is the price of controlling an operator norm by entrywise perturbations. On the NO side it can be removed, because the negative directions produced by the reduction are localized.

## 6.2. Localized certificates and a dimension-independent gap

**Lemma 6.2 (localized logarithmic certificates).** Let $C$ be a correlation matrix with $\min_{ij}|C_{ij}|\ge c_0>0$. Suppose that for every Hermitian zero-diagonal logarithm $\ell$ of $C$, the anchored matrix $G(\ell)$ of (2.4) admits a nonzero vector $w\in\mathbb C^{d-1}$ with at most $s$ nonzero coordinates and

$$
w^\dagger G(\ell)w\le-\gamma\|w\|_2^2.
\tag{6.7}
$$

Then every embeddable pointer-preserving $\Phi_D$ satisfies

$$
\|C-D\|_{\max}\ge\min\left\{\frac{c_0}2,\frac{\gamma c_0}{6s}\right\}.
\tag{6.8}
$$

*Proof.* Let $\varepsilon=\|C-D\|_{\max}<c_0/2$ and let $\ell_D$ be a CPSD logarithm of $D$. Define $L_{ij}=\operatorname{Log}(D_{ij}/C_{ij})$ with the principal branch. Since $|D_{ij}/C_{ij}-1|\le\varepsilon/c_0\le1/2$, we have $|L_{ij}|\le2\varepsilon/c_0$, $L$ is Hermitian, and $L_{ii}=0$. Then $\ell_C=\ell_D-L$ is a Hermitian zero-diagonal logarithm of $C$. Let $w$ be its certificate from (6.7). The anchored matrices satisfy $G(\ell_D)=G(\ell_C)+E$ with $E_{ij}=L_{ij}-L_{i0}-L_{0j}$, so $|E_{ij}|\le6\varepsilon/c_0$. By Cauchy--Schwarz on the support of $w$,

$$
0\le w^\dagger G(\ell_D)w\le-\gamma\|w\|_2^2+\frac{6\varepsilon}{c_0}\|w\|_1^2
\le\left(-\gamma+\frac{6s\varepsilon}{c_0}\right)\|w\|_2^2 .
\tag{6.9}
$$

Hence $\varepsilon\ge\gamma c_0/(6s)$. $\square$

The hypothesis concerns all logarithms of $C$, not only the principal one. In the reduction of Section 5, every Hermitian zero-diagonal logarithm has anchored matrix $\pi(\widehat G+2iK)$ for an integer skew-symmetric $K$ (Section 3.1), so the branch analysis of Lemmas 5.3 and 5.5 applies.

**Corollary 6.3 (constant in-class separation).** Every NO output of Theorem 5.7 satisfies, for every $\Phi_D\in\mathfrak R_d\cap\mathfrak T_d$,

$$
\|\Phi_C-\Phi_D\|_\diamond\ge\|C-D\|_{\max}\ge\varepsilon_*:=\frac{7\pi e^{-8\pi/7}}{34065}\approx1.78095\times10^{-5}.
\tag{6.10}
$$

The bound is independent of $d$; it exceeds $\varepsilon_d$ of (6.6) whenever $d\ge7$.

*Proof.* Fix a branch $K$. If $K$ is not of the form (5.6), the proof of Lemma 5.3 exhibits a $2\times2$ principal submatrix of $\widehat G+2iK$ whose smaller eigenvalue is below $-0.72$; its eigenvector is a certificate with $s=2$. If $K$ has the form (5.6), the NO case of Lemma 5.5 gives a vertex $v$ with $o_s(v)\ge3$ and the vector $z$ of (5.15). The column $Be_v$ is supported on the private indices of the at most three edges incident to $v$, and $P^{-1}$ preserves each private pair. Hence $z$ has at most $1+2\cdot3=7$ nonzero coordinates, and (5.16) gives $z^\dagger\widehat Gz\le-(98/11355)\|z\|_2^2$. In physical units both cases satisfy (6.7) with $s=7$ and $\gamma=98\pi/11355$. Lemma 6.2 with $c_0=c_*$ gives

$$
\frac{\gamma c_*}{42}=\frac{98\pi e^{-8\pi/7}}{476910}=\frac{7\pi e^{-8\pi/7}}{34065}<\frac{c_*}{2}.
$$

The diamond bound follows from (6.5). $\square$

The YES side is different. A dense entrywise perturbation of size $\varepsilon$ can lower the smallest anchored eigenvalue by order $d\varepsilon$, so the embeddable neighborhood of a YES output is only guaranteed with radius $\varepsilon_d$. The resulting promise problem therefore has exact membership on the YES side and a constant entrywise gap on the NO side.

## 6.3. Rational correlation and Choi matrices

**Theorem 6.4 (rational-channel promise hardness).** It is NP-hard to distinguish the following promised cases for a correlation matrix $\widetilde C$ with rational real and imaginary entries:

$$
\begin{array}{ll}
\mathrm{YES}:&\Phi_{\widetilde C}\in\mathfrak T_d,\\[2pt]
\mathrm{NO}:&\displaystyle\inf_{\Phi_D\in\mathfrak R_d\cap\mathfrak T_d}
\|\widetilde C-D\|_{\max}\ge\frac1{80000}.
\end{array}
\tag{6.11}
$$

The reduction outputs satisfy $|\widetilde C_{ij}|\ge1/50$, with $O(\log d)$ bits per rational entry. The same hardness holds for the corresponding rational Choi representation. In the NO case the stated lower bound also holds in diamond distance to pointer-preserving embeddable channels.

*Proof.* Begin with the output $C$ of Theorem 5.7. Since $c_*>1/40$ and $\gamma>1/50$, define

$$
e_d=\frac1{12000(d-1)}<\varepsilon_d,
\qquad \eta_d=\frac{e_d}{32d}.
\tag{6.12}
$$

Construct a Hermitian rational matrix $R$ with $R_{ii}=1$ and $|R_{ij}-C_{ij}|\le\eta_d$. A common rational grid with real and imaginary errors at most $\eta_d/2$ suffices. The operator error is at most $d\eta_d$. Thus

$$
\widetilde C=\frac{R+d\eta_d I}{1+d\eta_d}\succeq0,
\qquad \widetilde C_{ii}=1.
\tag{6.13}
$$

The diagonal correction is necessary: unconstrained rounding of a correlation matrix need not preserve positivity. For the off-diagonal error, $|C_{ij}|\le1$ gives

$$
\|\widetilde C-C\|_{\max}
\le\frac{(d+1)\eta_d}{1+d\eta_d}\le\frac{e_d}{16}.
\tag{6.14}
$$

On a YES instance, carry its positive-margin branch through the local logarithm. By (6.4), the physical anchor changes by less than $\gamma/16$, so $\widetilde C$ still has a CPSD logarithm. On a NO instance, Corollary 6.3 gives, for every embeddable pointer-preserving $D$,

$$
\|\widetilde C-D\|_{\max}
\ge\varepsilon_*-\frac{e_d}{16}\ge\varepsilon_*-\frac1{192000}>\frac1{80000},
\tag{6.15}
$$

because $\varepsilon_*-1/192000>1.2601\times10^{-5}>1.25\times10^{-5}$. Lemma 6.1 alone gives the weaker NO bound $1/(24000(d-1))$, since $\varepsilon_d-e_d/16>e_d/2$; the constant bound in (6.11) is stronger for $d\ge5$. Also $|\widetilde C_{ij}|\ge c_*-e_d/16>1/50$.

Because the logarithmic coefficients belong to a fixed finite alphabet, rational interval approximations to $\exp\{\pi(-\beta+i\theta)\}$ with error $O(d^{-2})$ are computable in polynomial time. Taylor bounds for the exponential and trigonometric functions, together with a rational approximation to $\pi$, provide such a procedure. A grid denominator polynomial in $d$ suffices; (6.13) preserves $O(\log d)$ bit length. There are $d^2$ entries. The unnormalized Choi matrix is

$$
J(\Phi_{\widetilde C})=\sum_{i,j}\widetilde C_{ij}|ii\rangle\langle jj|,
\tag{6.16}
$$

which is rational; dividing it by $d$ gives the normalized convention. $\square$

This theorem does not assert NP membership for exact embeddability of arbitrary rational Choi matrices, where logarithmic branch data are no longer rational input. Its NO case, taken alone, concerns pointer-preserving embeddable channels; the extension to all of $\mathfrak T_d$ requires the stability theorem of Section 7 and is proved in Section 8.

The worst-case hardness excludes a deterministic polynomial-time algorithm unless $\mathrm P=\mathrm{NP}$. A bounded-error randomized algorithm would instead imply $\mathrm{NP}\subseteq\mathrm{BPP}$, and a bounded-error quantum algorithm would imply $\mathrm{NP}\subseteq\mathrm{BQP}$. These are separate assumptions; none of the results determines average-case difficulty for a particular physical ensemble.

# 7. Approximate pointer recovery and stability of the rigidity theorem

Exact rigidity uses vanishing distinguishability loss and vanishing noise variance. This section proves that both survive approximately with polynomial dependence on the dimension. Sections 7.1 and 7.2 give a dissipation budget and a pointwise frame. Section 7.3 adds dynamical estimates, and Section 7.4 combines them into a uniform rounding theorem: every time-dependent Markovian channel close to a coherent pointer-preserving channel is close to a pointer-preserving Markovian channel.

## 7.1. A polynomial realization budget near a coherent channel

**Proposition 7.1.** Let $\Phi_C\in\mathfrak R_d$ with $\min_{ij}|C_{ij}|\ge c>0$. If $T\in\mathfrak T_d$ satisfies

$$
\|T-\Phi_C\|_\diamond\le\delta\le\frac{c}{2\sqrt d},
\tag{7.1}
$$

then $T$ has a GKLS realization bounded almost everywhere by

$$
B_{d,c}=\max\{2+4d\log(2/c),4\pi\}.
\tag{7.2}
$$

*Proof.* For every $X$, the inequalities $\|Y\|_2\le\|Y\|_1$ and $\|X\|_1\le\sqrt d\|X\|_2$ imply

$$
\|T-\Phi_C\|_{2\to2}\le\sqrt d\|T-\Phi_C\|_\diamond.
\tag{7.3}
$$

The singular values of the Schur superoperator are $|C_{ij}|$. Singular-value perturbation therefore gives $s_{\min}(T)\ge c/2$. As $T\in\mathfrak T_d$, its determinant is positive and

$$
\det T\ge(c/2)^{d^2}.
\tag{7.4}
$$

Insert (7.4) into Lemma 4.1. $\square$

Although the determinant lower bound is exponentially small in $d^2$, its logarithm controls the noise budget. The resulting replacement generator has norm $O(d\log c^{-1})$.

The stability argument below does not use the replacement generator. It uses only the reparametrization-invariant **dissipation budget** of an arbitrary realization. For a realization in canonical traceless form, $\mathcal L_t=-i[H_t,\cdot]+\sum_\alpha\mathcal D[K_\alpha(t)]$ with $\operatorname{tr}K_\alpha(t)=0$ and $\sum_\alpha\|K_\alpha(t)\|_2^2=\operatorname{tr}A_t$, Liouville's formula (4.2) gives

$$
\kappa(T):=\int_0^1\sum_\alpha\|K_\alpha(t)\|_2^2\,dt=-\frac1d\log\det T\le d\log\frac2c
\tag{7.4a}
$$

under (7.1). The value $\kappa(T)$ depends only on $T$, not on the realization; it is the quantum counterpart of Goodman's intrinsic time for stochastic matrices [12].

## 7.2. Intermediate states remain close to a pure orthogonal frame

**Proposition 7.2.** Let $\Lambda_t$ be a CP-divisible path on $M_d$ with $\Lambda_0=\mathrm{id}$ and

$$
\|\Lambda_1(P_j)-P_j\|_1\le\delta\qquad(0\le j<d).
\tag{7.5}
$$

Define

$$
E=2d(d-1)\delta,\qquad
\alpha=\frac{(d-1)\sqrt{2\delta}}{1-E}=\frac{\sqrt{E(d-1)/d}}{1-E},
\tag{7.6}
$$

and assume $E\le1/3$, so that $\alpha<\sqrt E/(1-E)\le\sqrt3/2<1$. For each $t$, there are rank-one orthogonal projections $Q_j(t)$ summing to $I$ such that

$$
\max_j\|\Lambda_t(P_j)-Q_j(t)\|_1\le2E+2\alpha.
\tag{7.7}
$$

*Proof.* Put $\rho_j=\Lambda_t(P_j)$. Trace-distance contractivity and (7.5) give $D(\rho_j,\rho_k):=\frac12\|\rho_j-\rho_k\|_1\ge1-\delta$. For root fidelity $f(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1$, the Fuchs--van de Graaf inequality [7, Theorem 1] gives $D\le\sqrt{1-f^2}$. Hence

$$
\operatorname{tr}(\rho_j\rho_k)\le f(\rho_j,\rho_k)^2\le2\delta\qquad(j\ne k).
\tag{7.8}
$$

For $S=\sum_j\rho_j$, $\operatorname{tr}S=d$ implies $\operatorname{tr}S^2\ge d$. Expanding this square yields

$$
\sum_j\bigl(1-\operatorname{tr}\rho_j^2\bigr)
\le\sum_{j\ne k}\operatorname{tr}(\rho_j\rho_k)\le E.
\tag{7.9}
$$

Let $\lambda_j$ be the largest eigenvalue of $\rho_j$ and $v_j$ a normalized corresponding eigenvector. Since $\lambda_j\ge\operatorname{tr}\rho_j^2\ge1-E$,

$$
\|\rho_j-v_jv_j^\dagger\|_1=2(1-\lambda_j)\le2E,
\qquad
|\langle v_j,v_k\rangle|^2\le\frac{2\delta}{(1-E)^2}.
\tag{7.10}
$$

Let $V$ have columns $v_j$. Gershgorin's bound gives $\|V^\dagger V-I\|_{\mathrm{op}}\le\alpha$. Thus $V$ is invertible and its polar factor $W=V(V^\dagger V)^{-1/2}$ is unitary. Its singular values imply

$$
\|V-W\|_{\mathrm{op}}
\le\frac{\alpha}{1+\sqrt{1-\alpha}}\le\alpha.
\tag{7.11}
$$

Use the columns of $W$ to define $Q_j$. The trace norm between two rank-one projectors is at most twice the Euclidean distance between their normalized vectors. Combine this with (7.10) and (7.11). $\square$

This is a pointwise statement at every time. It does not by itself bound the derivative of the chosen frame. The condition $E\le1/3$ cannot be weakened to $E<1/2$ without assuming $\alpha<1$ separately: for $d=3$ and $E=0.49$ one gets $\alpha\approx1.12$. The proof uses (7.8)--(7.11) at every time, and Section 7.4 uses the same facts.

## 7.3. Dynamical estimates

An inverse-polynomial separation from arbitrary channels in $\mathfrak T_d$ follows from a uniform rounding statement of the following form: for some absolute $a>0$ and explicit polynomial $p$,

$$
\begin{gathered}
\|T-\Phi_C\|_\diamond\le\delta,\qquad T\in\mathfrak T_d,\qquad
\min_{ij}|C_{ij}|\ge c>0\\
\Longrightarrow\quad
\exists\Phi_{C'}\in\mathfrak R_d\cap\mathfrak T_d:
\|C-C'\|_{\max}\le p(d,c^{-1})\delta^a.
\end{gathered}
\tag{7.12}
$$

Propositions 7.1 and 7.2 alone do not give (7.12). The missing step is control of the accumulated channel error caused by noise that is off-diagonal in the instantaneous pointer frame, and by the motion of that frame. Neither a small state error nor a projection of the generator onto diagonal noise supplies this control by itself. The overlap identity below supplies one bound. A sharper purity-production estimate makes the frame mismatch quadratic and yields square-root stability. The eigenprojection and polar-frame lemmas then control the speed of the frame.

Throughout this subsection, let $\Lambda_t$ solve (2.2) and write its generator in canonical traceless form $\mathcal L_t=-i[H_t,\cdot]+\sum_\alpha\mathcal D[K_\alpha(t)]$, where $\mathcal D[K]X=KXK^\dagger-\frac12\{K^\dagger K,X\}$. Let $\dot W_t=-iH_tW_t$, $W_0=I$, and pass to the Hamiltonian interaction picture,

$$
\widetilde\Lambda_t=\operatorname{Ad}_{W_t^\dagger}\circ\Lambda_t,\qquad
\frac{d}{dt}\widetilde\Lambda_t=\sum_\alpha\mathcal D[\widetilde K_\alpha(t)]\,\widetilde\Lambda_t,\qquad
\widetilde K_\alpha=W_t^\dagger K_\alpha W_t .
\tag{7.13}
$$

The norms of $\widetilde K_\alpha$ equal those of $K_\alpha$, so (7.4a) applies to them. Put $\widetilde\rho_j(t)=\widetilde\Lambda_t(P_j)$.

**Lemma 7.3 (overlap identity).** The function $S(t)=\sum_{j\ne k}\operatorname{tr}\bigl(\widetilde\rho_j(t)\widetilde\rho_k(t)\bigr)$ is absolutely continuous, equals the same sum in the original picture, and satisfies almost everywhere

$$
\frac{dS}{dt}=\sum_{j\ne k}\mathcal B_t(\widetilde\rho_j,\widetilde\rho_k),\qquad
\mathcal B_t(X,Y)=\sum_\alpha\operatorname{tr}\Bigl(\mathcal D[\widetilde K_\alpha](X)\,Y+X\,\mathcal D[\widetilde K_\alpha](Y)\Bigr).
\tag{7.14}
$$

For every orthonormal basis $\{q_j\}$ with $Q_j=q_jq_j^\dagger$,

$$
\sum_{j\ne k}\mathcal B_t(Q_j,Q_k)=2N_q(t),\qquad
N_q(t):=\sum_\alpha\sum_{j\ne k}\bigl|\langle q_k|\widetilde K_\alpha(t)|q_j\rangle\bigr|^2,
\tag{7.15}
$$

and for all operators $X,Y$,

$$
|\mathcal B_t(X,Y)|\le4\sum_\alpha\|\widetilde K_\alpha(t)\|_{\mathrm{op}}^2\,\|X\|_1\|Y\|_{\mathrm{op}}.
\tag{7.16}
$$

*Proof.* Unitary conjugation preserves $\operatorname{tr}(\rho_j\rho_k)$, and in the interaction picture no Hamiltonian term remains, which gives (7.14). For $j\ne k$, $Q_jQ_k=0$, so the anticommutator terms vanish and $\operatorname{tr}(\mathcal D[K](Q_j)Q_k)=|\langle q_k|K|q_j\rangle|^2$. Summing over ordered pairs gives (7.15). Finally $\|\mathcal D[K]\|_{1\to1}\le2\|K\|_{\mathrm{op}}^2$ and $\|\mathcal D[K](Y)\|_{\mathrm{op}}\le2\|K\|_{\mathrm{op}}^2\|Y\|_{\mathrm{op}}$, which give (7.16). $\square$

At an exactly pure orthonormal configuration, $N_q(t)$ is the noise variance appearing in (3.2). Lemma 7.3 thus turns the exact purity argument into an integrated inequality: off-frame noise increases the pairwise overlaps at a rate $2N_q$, and the total overlap at the end is small.

**Lemma 7.3a (purity production and quadratic frame transfer).** In the interaction picture (7.13), let $\Pi_j=v_jv_j^\dagger$ be the dominant eigenprojection of $\widetilde\rho_j$, put $e_j=1-\lambda_{\max}(\widetilde\rho_j)$, and define

$$
F(t)=\sum_j(1-\operatorname{tr}\widetilde\rho_j^2),\quad
\mathcal V=\int_0^1\sum_{\alpha,j}\|(I-\Pi_j)\widetilde K_\alpha v_j\|^2dt.
\tag{7.16a}
$$
If the endpoint recovers each pointer within trace distance $\delta$ as in (7.5), and $E,\alpha$ obey Proposition 7.2, then

$$
\mathcal V\le\frac{d\delta}{2}+8E\kappa,\qquad
\int_0^1N_q(t)dt\le d\delta+16E\kappa+8d\alpha^2\kappa
\tag{7.16b}
$$
for the Löwdin frame of Proposition 7.2.

*Proof.* At every time, $\sum_je_j\le F(t)\le E$ by (7.9) and $\lambda_{\max}(\rho)\ge\operatorname{tr}\rho^2$. For one normalized dominant eigenvector $v$ and $\Pi=vv^\dagger$,

$$
\operatorname{tr}(\Pi\mathcal D[K](\Pi))=-\|(I-\Pi)Kv\|^2,
\qquad \|\rho-\Pi\|_1=2e.
$$
The induced trace and operator norms of $\mathcal D[K]$ are at most $2\|K\|_{\mathrm{op}}^2$. Expand the two factors of $\operatorname{tr}(\rho\mathcal D[K](\rho))$ successively to obtain

$$
\left|\operatorname{tr}(\rho\mathcal D[K](\rho))-
\operatorname{tr}(\Pi\mathcal D[K](\Pi))\right|
\le8e\|K\|_{\mathrm{op}}^2.
$$
Thus, writing $V(t)$ for the integrand defining $\mathcal V$ and $k(t)=\sum_\alpha\|\widetilde K_\alpha\|_{\mathrm{op}}^2$,

$$
|\dot F(t)-2V(t)|\le16E k(t).
\tag{7.16c}
$$
There is no purity-monotonicity assumption. The correction controls possible purification in a nonunital path. At the endpoint, in the original picture $\langle j|\rho_j(1)|j\rangle\ge1-\delta/2$, whence $1-\operatorname{tr}\rho_j(1)^2\le\delta$. Therefore $F(1)\le d\delta$, $F(0)=0$, and $\int k\le\kappa$ gives the first inequality of (7.16b).

For the normalized columns $q_j$ of the Löwdin frame, $\|v_j-q_j\|\le\alpha$ and $\|\Pi_j-Q_j\|_{\mathrm{op}}\le\|v_j-q_j\|$. Hence

$$
\|(I-Q_j)Kq_j-(I-\Pi_j)Kv_j\|\le2\alpha\|K\|_{\mathrm{op}}.
$$
Squaring via $(x+y)^2\le2x^2+2y^2$, summing and integrating gives $\int N_q\le2\mathcal V+8d\alpha^2\kappa$, as claimed. $\square$

**Lemma 7.4 (speed of a dominant eigenprojection).** Let $\rho(t)$ be an absolutely continuous path of density matrices with $\dot\rho=\sum_\alpha\mathcal D[K_\alpha(t)]\rho$ and largest eigenvalue $\lambda_1(t)\ge1-E$, where $E<1/2$. Let $\Pi(t)$ be the corresponding rank-one spectral projection and $v(t)$ a unit vector in its range. Then $\Pi$ is absolutely continuous and almost everywhere

$$
\|\dot\Pi\|_{\mathrm{op}}\le\frac1{1-2E}\sum_\alpha\Bigl[\|K_\alpha\|_{\mathrm{op}}\Bigl(\tfrac32\|r_\alpha\|+\tfrac12\|u_\alpha\|\Bigr)+2E\|K_\alpha\|_{\mathrm{op}}^2\Bigr],
\tag{7.17}
$$

where $r_\alpha=(I-\Pi)K_\alpha v$ and $u_\alpha=(I-\Pi)K_\alpha^\dagger v$.

*Proof.* The other eigenvalues of $\rho$ are at most $E<1/2<1-E$, so $\Pi$ is the Riesz projection of $\rho$ along a fixed circle of radius $1/2$ about $1$, an analytic function of $\rho$ on this region. Hence $\Pi$ is absolutely continuous, $\dot\Pi$ is block off-diagonal with respect to $\Pi$, and first-order perturbation theory [13, Chapter II] gives $\|\dot\Pi\|_{\mathrm{op}}\le\|(I-\Pi)\dot\rho\,v\|/(\lambda_1-\lambda_2)$ with $\lambda_1-\lambda_2\ge1-2E$. Write $\rho=\lambda_1\Pi+\rho_r$ with $\rho_r=(I-\Pi)\rho(I-\Pi)$ and $\operatorname{tr}\rho_r\le E$. For one jump operator $K$ with $k=\langle v,Kv\rangle$, a direct expansion gives

$$
(I-\Pi)\mathcal D[K](\Pi)v=\bar k\,r-\tfrac12k\,u-\tfrac12(I-\Pi)K^\dagger r,
\tag{7.18}
$$

whose norm is at most $\|K\|_{\mathrm{op}}(\frac32\|r\|+\frac12\|u\|)$. Also $\|\mathcal D[K](\rho_r)\|_{\mathrm{op}}\le\|\mathcal D[K](\rho_r)\|_1\le2E\|K\|_{\mathrm{op}}^2$. Since $\lambda_1\le1$, summing over $\alpha$ gives (7.17). $\square$

**Lemma 7.5 (Löwdin frame).** Let $V(t)$ be an absolutely continuous $d\times d$ matrix with unit columns and $\|V^\dagger V-I\|_{\mathrm{op}}\le\alpha<1$. Then $Y=V(V^\dagger V)^{-1/2}$ is an absolutely continuous unitary and

$$
\|\dot Y\|_{\mathrm{op}}\le C_\alpha\|\dot V\|_{\mathrm{op}},\qquad
C_\alpha=(1-\alpha)^{-1/2}+(1+\alpha)(1-\alpha)^{-3/2}.
\tag{7.19}
$$

*Proof.* Let $S=V^\dagger V$, whose spectrum lies in $[1-\alpha,1+\alpha]$. Then $\dot Y=\dot VS^{-1/2}+V\,\frac{d}{dt}S^{-1/2}$ and $\|\dot S\|\le2\sqrt{1+\alpha}\,\|\dot V\|$. By the Daleckii--Krein formula [14, Section V.3], the derivative of $S\mapsto S^{-1/2}$ in a Hermitian direction $H$ is $-M\circ H$, where the Schur product is taken in the eigenbasis of $S$ and $M_{ij}=[\sqrt{\lambda_i\lambda_j}(\sqrt{\lambda_i}+\sqrt{\lambda_j})]^{-1}$. The matrix $M$ is positive semidefinite: $(\sqrt\lambda+\sqrt\mu)^{-1}=\int_0^\infty e^{-s\sqrt\lambda}e^{-s\sqrt\mu}\,ds$ is a Gram kernel, and the remaining factor has rank one. Writing $M_{ij}=\sum_km_{ik}\overline{m_{jk}}$ shows $M\circ H=\sum_kD_kHD_k^\dagger$ with $D_k=\operatorname{diag}(m_{1k},\ldots,m_{dk})$; this map is positive, so its norm on the operator norm equals $\|\sum_kD_kD_k^\dagger\|=\max_iM_{ii}\le\frac12(1-\alpha)^{-3/2}$. Combining the three estimates gives (7.19). $\square$

## 7.4. Uniform rounding

Set

$$
\delta_d(c)=\min\left\{\frac{c}{2\sqrt d},\frac1{72d^2}\right\}.
\tag{7.20}
$$

**Theorem 7.6 (square-root uniform rounding; (7.12) with $a=1/2$).** Let $d\ge2$ and let $C$ be a correlation matrix with $\min_{ij}|C_{ij}|\ge c>0$. If $T\in\mathfrak T_d$ satisfies $\|T-\Phi_C\|_\diamond\le\delta\le\delta_d(c)$, then there is a correlation matrix $C''$ with a CPSD logarithm, so that $\Phi_{C''}\in\mathfrak R_d\cap\mathfrak T_d$, and

$$
\|C-C''\|_{\max}\le\|\Phi_C-\Phi_{C''}\|_\diamond\le400d^{7/2}\log\frac2c\;\sqrt\delta.
\tag{7.21}
$$

More precisely, with $E,\alpha$ from (7.6), $\varepsilon_0=2E+2\alpha$, $g=1-2E$ and $\kappa=\kappa(T)$,

$$
\|\Phi_C-\Phi_{C''}\|_\diamond\le(1+\sqrt{2d})(\delta+\tau),\qquad
\tau\le4\sqrt{\kappa\mathcal N}+2\mathcal N+\frac{2C_\alpha}{g}\Bigl[2\sqrt d\sqrt{\kappa\mathcal N}+(6\alpha+2E)d\kappa\Bigr],
\tag{7.22}
$$

where $\mathcal N\le d\delta+16E\kappa+8d\alpha^2\kappa$.

*Proof.* **Step 0: regime.** Since $\delta\le1/(72d^2)$, we have $E\le1/36$, $g\ge17/18$, and by (7.6) $\alpha\le\frac{36}{35}\sqrt2\,(d-1)\sqrt\delta\le0.1715$, so $C_\alpha\le2.66$. Also $2E=4d(d-1)\delta\le0.472(d-1)\sqrt\delta$, hence $\varepsilon_0\le3.39(d-1)\sqrt\delta$. Since $\delta\le c/(2\sqrt d)$, (7.4a) gives $\kappa\le d\log(2/c)$.

**Step 1: a moving frame.** By contractivity of the remaining propagator, every $t$ satisfies the hypotheses of Proposition 7.2 with the same $\delta$; unitary conjugation does not change them, so they hold for $\widetilde\rho_j(t)$. Hence every $\widetilde\rho_j(t)$ has a simple largest eigenvalue $\lambda_j(t)\ge1-E$, with spectral projection $\Pi_j(t)$, absolutely continuous by Lemma 7.4. Choose unit vectors $v_j(t)\in\operatorname{ran}\Pi_j(t)$ by parallel transport, $\dot v_j=\dot\Pi_jv_j$, $v_j(0)=e_j$; this keeps $v_j$ in the range and gives $\|\dot v_j\|\le\|\dot\Pi_j\|_{\mathrm{op}}$. Let $V_t$ have columns $v_j(t)$. By (7.10)--(7.11), $\|V_t^\dagger V_t-I\|\le\alpha$ and $\|v_j-q_j\|\le\alpha$, where $q_j$ are the columns of the Löwdin unitary $Y_t=V_t(V_t^\dagger V_t)^{-1/2}$. Thus $Y_0=I$, $Y_t$ is absolutely continuous by Lemma 7.5, and $Q_j(t)=Y_tP_jY_t^\dagger$ satisfies $\|\widetilde\rho_j(t)-Q_j(t)\|_1\le\varepsilon_0$ by (7.7). Let $N(t)=N_q(t)$ for this frame and $\mathcal N=\int_0^1N(t)\,dt$.

**Step 2: integrated off-frame noise.** Lemma 7.3a gives the two quantitative bounds

$$
\mathcal V\le\frac{d\delta}{2}+8E\kappa,
\tag{7.23}
$$

$$
\mathcal N\le2\mathcal V+8d\alpha^2\kappa
\le d\delta+16E\kappa+8d\alpha^2\kappa.
\tag{7.24}
$$

The nonorthogonal eigenvectors are used before orthogonalization, so their purity error is $O(\delta)$ and the orthogonalization error enters only through $\alpha^2=O(\delta)$.

**Step 3: speed of the frame.** Apply Lemma 7.4 to each $\widetilde\rho_j$. Replacing $v_j$ by $q_j$ in $r$ and $u$ changes each by at most $3\|\widetilde K_\alpha\|_{\mathrm{op}}\alpha$, and $\sum_j\|(I-Q_j)\widetilde K_\alpha q_j\|^2=\sum_j\|(I-Q_j)\widetilde K_\alpha^\dagger q_j\|^2=\|O_q(\widetilde K_\alpha)\|_2^2$, where $O_q$ denotes the part off-diagonal in the frame. By Cauchy--Schwarz over $j$,

$$
\sum_j\|\dot\Pi_j\|_{\mathrm{op}}\le\frac1g\sum_\alpha\Bigl[2\sqrt d\,\|\widetilde K_\alpha\|_{\mathrm{op}}\|O_q(\widetilde K_\alpha)\|_2+(6\alpha+2E)d\,\|\widetilde K_\alpha\|_{\mathrm{op}}^2\Bigr].
\tag{7.25}
$$

Integrating, using $\sum_\alpha\|O_q(\widetilde K_\alpha)\|_2^2=N$ and Cauchy--Schwarz in $(t,\alpha)$, and then Lemma 7.5 with $\|\dot V\|_{\mathrm{op}}\le\|\dot V\|_2\le\sum_j\|\dot\Pi_j\|_{\mathrm{op}}$,

$$
\int_0^1\|\dot Y_t\|_{\mathrm{op}}\,dt\le\frac{C_\alpha}{g}\Bigl[2\sqrt d\sqrt{\kappa\mathcal N}+(6\alpha+2E)d\kappa\Bigr].
\tag{7.26}
$$

**Step 4: comparison with a Schur flow.** In the doubly rotated picture $\widehat\Lambda_t=\operatorname{Ad}_{Y_t^\dagger}\circ\widetilde\Lambda_t$, the generator is

$$
\widehat{\mathcal L}_t=\sum_\alpha\mathcal D[\widehat K_\alpha]+[\,\cdot\,,Y_t^\dagger\dot Y_t],\qquad
\widehat K_\alpha=Y_t^\dagger\widetilde K_\alpha Y_t .
\tag{7.27}
$$

Split $\widehat K_\alpha=\Delta_\alpha+O_\alpha$ into its diagonal and off-diagonal parts in the fixed basis; then $\sum_\alpha\|O_\alpha\|_2^2=N(t)$. The diagonal parts generate a Schur flow with coefficients $g_{ij}(t)$ given by (3.4), which is CPSD at every $t$ by (3.5). Let $C'=\exp^{\circ}\!\int_0^1g(t)\,dt$. Since
$\|\mathcal D[\Delta+O]-\mathcal D[\Delta]\|_\diamond\le4\|\Delta\|_{\mathrm{op}}\|O\|_{\mathrm{op}}+2\|O\|_{\mathrm{op}}^2$ and $\|X\mapsto[X,A]\|_\diamond\le2\|A\|_{\mathrm{op}}$, the Duhamel formula, contractivity of all completely positive trace-preserving propagators, and Cauchy--Schwarz give

$$
\tau:=\|\widehat\Lambda_1-\Phi_{C'}\|_\diamond\le4\sqrt{\kappa\mathcal N}+2\mathcal N+2\int_0^1\|\dot Y_t\|_{\mathrm{op}}\,dt .
\tag{7.28}
$$

**Step 5: the endpoint frame.** If $\tau+\delta\ge2$, the claim holds with $C''$ the all-ones matrix, since any two channels are at diamond distance at most $2$. Otherwise let $U=W_1Y_1$, so $T=\Lambda_1=\operatorname{Ad}_U\circ\widehat\Lambda_1$. Then $\|UP_jU^\dagger-P_j\|_1\le\|\Phi_{C'}(P_j)-\widehat\Lambda_1(P_j)\|_1+\|T(P_j)-P_j\|_1\le\tau+\delta$. For pure states this gives $|U_{jj}|^2\ge1-(\tau+\delta)^2/4$. Let $D'=\operatorname{diag}(U_{jj}/|U_{jj}|)=\operatorname{diag}(e^{i\varphi_j})$. Each column satisfies $\|(U-D')e_j\|^2\le2(1-|U_{jj}|^2)$, so $\|U-D'\|_{\mathrm{op}}\le\sqrt{d/2}\,(\tau+\delta)$ and $\|\operatorname{Ad}_U-\operatorname{Ad}_{D'}\|_\diamond\le\sqrt{2d}\,(\tau+\delta)$. Put $C''_{ij}=e^{i(\varphi_i-\varphi_j)}C'_{ij}$, so that $\operatorname{Ad}_{D'}\circ\Phi_{C'}=\Phi_{C''}$. The logarithm $\int_0^1g\,dt+i(\varphi_i-\varphi_j)$ of $C''$ is CPSD. Finally

$$
\Phi_C-\Phi_{C''}=(\Phi_C-T)+\operatorname{Ad}_U\circ(\widehat\Lambda_1-\Phi_{C'})+(\operatorname{Ad}_U-\operatorname{Ad}_{D'})\circ\Phi_{C'}
$$

gives (7.22), and $\|C-C''\|_{\max}\le\|\Phi_C-\Phi_{C''}\|_\diamond$ by (6.5).

**Step 6: explicit constants.** Put $\bar\kappa=d\log(2/c)\ge\kappa$. Since $c\le1$ and $d\ge2$, $\bar\kappa>1$. The regime gives

$$
E\le1/36,\quad g\ge17/18,\quad
\alpha\le\tfrac32d\sqrt\delta<1/5,\quad
C_\alpha\le3,\quad C_\alpha/g<16/5,\quad
2E\le\tfrac12d\sqrt\delta.
$$
Using $d\ge2$ in (7.24),

$$
\mathcal N\le d\delta+32d^2\bar\kappa\delta+18d^3\bar\kappa\delta
\le36d^3\bar\kappa\delta.
\tag{7.29}
$$
Consequently $\sqrt{\kappa\mathcal N}\le6d^{3/2}\bar\kappa\sqrt\delta$ and $(6\alpha+2E)d\kappa\le(19/2)d^2\bar\kappa\sqrt\delta$. Equation (7.26) gives

$$
\int_0^1\|\dot Y_t\|_{\mathrm{op}}dt
\le\frac{16}{5}\left(12+\frac{19}{2}\right)d^2\bar\kappa\sqrt\delta
=\frac{344}{5}d^2\bar\kappa\sqrt\delta.
$$
The first two terms in (7.28) are bounded by $17d^2\bar\kappa\sqrt\delta$ and $(17/2)d^2\bar\kappa\sqrt\delta$, respectively; here $\sqrt\delta\le1/(\sqrt{72}d)$. Also $\delta\le d^2\bar\kappa\sqrt\delta$, so $\tau+\delta\le165d^2\bar\kappa\sqrt\delta$. Finally $1+\sqrt{2d}\le(3/\sqrt2)\sqrt d$ yields

$$
(1+\sqrt{2d})(\tau+\delta)
\le\frac{495}{\sqrt2}d^{7/2}\log(2/c)\sqrt\delta
<400d^{7/2}\log(2/c)\sqrt\delta.
$$
For $\delta=0$ exact rigidity applies. $\square$

Only the determinant-controlled dissipation budget is global; no pointwise rate bound or unitality assumption is used. Completely positive propagators make the Duhamel comparison contractive. The quadratic frame transfer in Lemma 7.3a eliminates the extra square-root loss of the overlap-only argument. The older bound $120d^4\log(2/c)\delta^{1/4}$ also follows in the stated regime, since the ratio of the new bound to the old one is at most $10/(3\cdot72^{1/4}d)<1$ for $d\ge2$. A Lipschitz bound with exponent $1$ remains open; finite sample behavior cannot establish it.

# 8. Robust hardness against all time-dependent Markovian channels

The previous sections combine into a statement that no longer refers to the pointer-preserving class on the NO side.

**Theorem 8.1 (robust hardness of time-dependent Markovian membership).** Let

$$
\nu_d=\frac{1}{4\cdot10^{16}d^7}.
\tag{8.1}
$$

Given the rational Choi matrix of a channel $\Phi$ on $M_d$, with $O(\log d)$ bits per entry, it is NP-hard to distinguish

$$
\begin{array}{ll}
\mathrm{YES}:&\Phi=e^{\mathcal L}\ \text{for a time-independent GKLS generator }\mathcal L,\ \text{in particular }\Phi\in\mathfrak T_d,\\[2pt]
\mathrm{NO}:&\displaystyle\inf_{T\in\mathfrak T_d}\|\Phi-T\|_\diamond\ge\nu_d .
\end{array}
\tag{8.2}
$$

*Proof.* Use the outputs $\widetilde C$ of Theorem 6.4. On YES instances, $\Phi_{\widetilde C}\in\mathfrak R_d\cap\mathfrak T_d$, and Theorem 3.1 gives a time-independent generator. On NO instances, suppose that some $T\in\mathfrak T_d$ satisfies $\|T-\Phi_{\widetilde C}\|_\diamond=\delta<\nu_d$. Since $|\widetilde C_{ij}|\ge1/50$ and $\nu_d<1/(72d^2)\le1/(100\sqrt d)$ for $d\ge2$, Theorem 7.6 applies with $c=1/50$. It yields $\Phi_{C''}\in\mathfrak R_d\cap\mathfrak T_d$ with

$$
\|\widetilde C-C''\|_{\max}\le400d^{7/2}\log(100)\sqrt\delta<\frac{400\log100}{2\cdot10^8}<10^{-5}<\frac1{80000},
$$

contradicting (6.11). The elementary bound $\log100<5$ follows from $\sum_{k=0}^6 5^k/k!>100$. $\square$

Because the YES instances lie in the smallest of the three natural sets and the NO instances are far from the largest, the same reduction proves hardness simultaneously for three questions:

1. **Homogeneous embedding:** is $\Phi=e^{\mathcal L}$ for a time-independent GKLS generator?
2. **Time-dependent embedding:** is $\Phi\in\mathfrak T_d$?
3. **Infinitesimal divisibility:** is $\Phi\in\overline{\mathfrak T_d}$? Finite products of Markovian channels lie in $\mathfrak T_d$, and every element of $\mathfrak T_d$ belongs to a continuous completely positive evolution. By [2, Definition 14 and Theorem 16], the closure of such products, the set of elements of continuous completely positive evolutions, and the set of infinitesimally divisible channels coincide. Hence $\overline{\mathfrak T_d}$ is exactly the set of infinitesimally divisible channels.

The distance from the NO instances to $\overline{\mathfrak T_d}$ equals their distance to $\mathfrak T_d$. Hence, unless $\mathrm P=\mathrm{NP}$, no polynomial-time algorithm can approximate $\inf_{T\in\mathfrak T_d}\|\Phi-T\|_\diamond$ on rational inputs to an additive accuracy smaller than $\nu_d/2$.

Theorem 8.1 has an exact YES promise. The next subsection makes the YES side robust in all channel directions, with a smaller explicit radius. Membership in NP for arbitrary rational channels remains open. The inverse-polynomial precision is a complexity statement and is not a claim of experimentally useful noise tolerance.

## 8.2. Quantitative interior regularization

Let $\Omega(X)=\operatorname{tr}(X)I/d$ and $D_p=(1-p)\mathrm{id}+p\Omega$, $0<p\le1/8$. Use the unnormalized Choi convention $J(F)=\sum_{ij}E_{ij}\otimes F(E_{ij})$, let $|\omega\rangle=\sum_j|jj\rangle$, and put $Q=I-|\omega\rangle\langle\omega|/d$. The real affine space of Hermiticity-preserving and trace-preserving linear maps is denoted $\mathcal A_d$.

**Lemma 8.2 (a homogeneous ball near depolarization).** If $A\in\mathcal A_d$ and $\|A-D_p\|_\diamond\le p/(4d^2)$, then $A=e^L$ for a GKLS generator $L$. Complete positivity follows from the conclusion and need not be assumed.

*Proof.* Set $\eta=\|A-D_p\|_\diamond$ and $t=-\log(1-p)\ge p$. Since $\Omega^2=\Omega$,

$$
L_0=\log D_p=t(\Omega-\mathrm{id}),\qquad QJ(L_0)Q=\frac{t}{d}Q.
\tag{8.3}
$$
Both $B=A-\mathrm{id}$ and $B_0=D_p-\mathrm{id}$ have diamond norm at most $r=2p+\eta<1/2$. The series $L=\sum_{n\ge1}(-1)^{n+1}B^n/n$ converges in norm, preserves Hermiticity and annihilates the trace. Noncommutative telescoping gives $\|B^n-B_0^n\|_\diamond\le nr^{n-1}\eta$, so

$$
\|L-L_0\|_\diamond\le\frac{\eta}{1-r}\le2\eta,
\qquad QJ(L)Q\succeq\left(\frac{t}{d}-2d\eta\right)Q\succeq\frac{p}{2d}Q.
\tag{8.4}
$$
We used $\|J(F)\|_{\mathrm{op}}\le\|J(F)\|_1\le d\|F\|_\diamond$.

The conditional Choi criterion yields the GKLS form [1, Lemma 9]. For completeness, factor $QJ(L)Q$ into vectors orthogonal to $\omega$, identify them with traceless Kraus operators $K_\alpha$, and subtract the corresponding CP map. The remaining Hermitian Choi matrix has zero $Q$--$Q$ block, so its map is $RX+XR^\dagger$ for some $R$. Trace annihilation gives $R+R^\dagger=-\sum K_\alpha^\dagger K_\alpha$, and the anti-Hermitian part supplies $-iH$. Finally $\exp(\log A)=A$ near the identity. $\square$

**Theorem 8.3 (quantitative interior regularization).** For $T\in\mathfrak T_d$ set $M=\|T^{-1}\|_\diamond$. Then

$$
\left\{S\in\mathcal A_d:\ \|S-D_p\circ T\|_\diamond\le\frac{p}{4d^2M}\right\}\subset\mathfrak T_d.
\tag{8.5}
$$
If $T=e^{\mathcal L}$ for a unital GKLS generator, its center is homogeneously embeddable:

$$
D_p\circ T=e^{\mathcal L+t(\Omega-\mathrm{id})}.
\tag{8.6}
$$

*Proof.* An invertible HP TP map has an HP TP inverse. For $A=S\circ T^{-1}$ the hypothesis gives $\|A-D_p\|_\diamond\le p/(4d^2)$. Lemma 8.2 implies $A=e^G$ with $G$ GKLS; concatenate the old path for $T$ with this constant-generator segment and rescale time to $[0,1]$. Integrability is preserved. For the homogeneous statement, $\mathcal L(I)=0$ and trace annihilation imply $\mathcal L\Omega=\Omega\mathcal L=0$. Thus the two generators commute. $\square$

It follows that interior points are dense in $\mathfrak T_d$: $D_p\circ T\to T$ as $p\downarrow0$. The relevant quantitative feature is the explicit inverse-condition factor $M$. No assertion of convexity or of a homogeneous realization for the whole ball is made. Taking the logarithm of the short correction avoids exponential-map resonances at the original endpoint.

**Theorem 8.4 (two-sided robust time-dependent membership).** Put

$$
p_d=\nu_d/8,\qquad \rho_d=\frac{\nu_d}{1600d^3}=\frac{1}{64\cdot10^{18}d^{10}}.
\tag{8.7}
$$
It is NP-hard, given a rational Choi matrix with $O(\log d)$ bits per entry, to distinguish

$$
\begin{array}{ll}
\mathrm{YES}:&\Psi=e^{\mathcal L}\text{ for some GKLS }\mathcal L,\quad
B_\diamond(\Psi,\rho_d)\cap\mathcal A_d\subset\mathfrak T_d,\\[2pt]
\mathrm{NO}:&\operatorname{dist}_\diamond(\Psi,\mathfrak T_d)\ge3\nu_d/4.
\end{array}
\tag{8.8}
$$
The same interior/exterior promise is hard for $\overline{\mathfrak T_d}$, the infinitesimally divisible channels.

*Proof.* For the rational output $\Phi=\Phi_{\widetilde C}$ of Theorem 6.4, output $\Psi=D_{p_d}\circ\Phi$. Since $|\widetilde C_{ij}|\ge1/50$, $\|\Phi^{-1}\|_{2\to2}\le50$ and $\|\Phi^{-1}\|_\diamond\le50d$. The norm inequality $\|F\|_\diamond\le d\|F\|_{2\to2}$ follows by stabilizing with a $d$-dimensional ancilla and using $\|Y\|_1\le d\|Y\|_2$ and $\|X\|_2\le\|X\|_1$. On YES inputs, Theorem 8.3 gives radius $p_d/(200d^3)=\rho_d$. The reconstructed Schur generator is unital, so the center is homogeneous.

On NO inputs, $\|D_{p_d}\circ\Phi-\Phi\|_\diamond\le2p_d$, whence the distance is at least $\nu_d-2p_d=3\nu_d/4$. The output is rational and strictly positive in Choi form:

$$
J(\Psi)=(1-p_d)J(\Phi)+\frac{p_d}{d}I_{d^2}.
\tag{8.9}
$$
Its entry bit lengths remain $O(\log d)$. The transformation does not require knowledge of a satisfying assignment. Distance to a set equals distance to its closure, giving the final statement. $\square$

For this nonconvex set, (8.8) is the precise interior/exterior membership promise. It also yields hardness at a common tolerance $\rho_d$, because $3\nu_d/4>\rho_d$. In unnormalized Choi Frobenius norm, $\|F\|_\diamond\le\|J(F)\|_1\le d\|J(F)\|_F$ gives a YES radius $\rho_d/d$ and NO separation $3\nu_d/(4d)$ within the TP affine space. Normalizing Choi matrices divides those radii once more by $d$. These statements establish neither NP membership for general inputs nor constant-precision hardness. The full YES ball is not asserted to lie in the homogeneous set.

# 9. An embedding does not select a measurement instrument

A quantum instrument is a family of completely positive maps $\{\mathcal I_r\}$ whose sum is a channel. Its outcome probabilities are $\operatorname{tr}\mathcal I_r(\rho)$. The averaged channel and even a prescribed dilation do not determine these probabilities without a readout choice.

Fix $0<c<1$, let $Z=\operatorname{diag}(1,-1)$, and define

$$
a=\sqrt{\frac{1+c}{2}},\qquad b=\sqrt{\frac{1-c}{2}},\qquad
|e_0\rangle=a|0\rangle+b|1\rangle,\quad
|e_1\rangle=a|0\rangle-b|1\rangle.
\tag{9.1}
$$

The isometry $V|j\rangle=|j\rangle|e_j\rangle$ induces the dephasing channel with coherence multiplier $c$. It is the time-one map of

$$
\mathcal L(\rho)=\frac{-\log c}{2}(Z\rho Z-\rho).
\tag{9.2}
$$

Measuring the environment in its computational basis gives Kraus operators $aI,bZ$ and probabilities $a^2,b^2$, independent of the pointer label. Measuring in the $X$ basis gives

$$
M_\pm=\frac{aI\pm bZ}{\sqrt2}.
\tag{9.3}
$$

For the two pointer inputs, the outcome probabilities are interchanged:

$$
p_\pm(0)=\frac{(a\pm b)^2}{2},\qquad
p_\pm(1)=\frac{(a\mp b)^2}{2}.
\tag{9.4}
$$

Their total variation distance is

$$
\frac12\sum_{r=\pm}|p_r(0)-p_r(1)|=2ab=\sqrt{1-c^2}.
\tag{9.5}
$$

More generally, an environment projective measurement along a unit Bloch vector $n$ has pointer contrast $|n_x|\sqrt{1-c^2}$. The same finite-rate channel and the same isometry therefore admit a continuous range of readout information, including zero. This is a direct consequence of standard measurement theory, not a new measurement postulate. It identifies the additional physical input that an embedding theorem does not provide.


## 9.1. Compatible instruments as positive decompositions

The readout ambiguity can be characterized exactly. Throughout this section the outcome set is finite. Write $\Phi_C(X)=C\circ X$, where $C\succeq0$ and $C_{jj}=1$.

**Proposition 9.1 (instrument fibre of a Schur channel).** The instruments whose nonselective channel is $\Phi_C$ are exactly

$$
\mathcal I_r(X)=C^{(r)}\circ X,
\qquad C^{(r)}\succeq0,
\qquad \sum_r C^{(r)}=C.
\tag{9.6}
$$

Consequently their response probabilities on the pointer inputs are

$$
p(r\mid j)=C^{(r)}_{jj},
\tag{9.7}
$$

and a prescribed stochastic response matrix $p(r\mid j)$ is implementable if and only if the semidefinite feasibility problem

$$
C^{(r)}\succeq0,
\quad \sum_r C^{(r)}=C,
\quad C^{(r)}_{jj}=p(r\mid j)
\tag{9.8}
$$

has a solution.

*Proof.* Use the unnormalized Choi matrix. The Choi matrix of $\Phi_C$ is

$$
J_C=\sum_{ij}C_{ij}|ii\rangle\langle jj|,
\tag{9.9}
$$

supported on $\mathcal D=\operatorname{span}\{|jj\rangle\}$. If $\sum_r\mathcal I_r=\Phi_C$, then $0\preceq J_r\preceq J_C$. For every $v\in\mathcal D^\perp$, positivity gives $\langle v,J_rv\rangle=0$ and hence $J_rv=0$. Thus each $J_r$ is supported on $\mathcal D$, has the displayed Schur form for a positive matrix $C^{(r)}$, and the sum condition follows. Conversely positive matrices of this form define CP maps; their sum is the trace-preserving map $\Phi_C$, so each is trace nonincreasing. The formula for the response follows by evaluation on $|j\rangle\langle j|$. $\square$

This is the Schur-channel form of the standard instrument--channel compatibility theorem. In a minimal dilation $V|j\rangle=|j\rangle|e_j\rangle$, with $\langle e_j|e_i\rangle=C_{ij}$, the same fibre is parametrized by environment POVMs $\{F_r\}$ through

$$
C^{(r)}_{ij}=\langle e_j|F_r|e_i\rangle,
\qquad F_r\succeq0,
\qquad \sum_rF_r=I_E.
\tag{9.10}
$$

For a fixed minimal dilation the POVM corresponding to an instrument is unique; the endpoint channel does not select which POVM is physically implemented. See [22, Proposition 15].

## 9.2. A complete qubit readout test and a record-error bound

Every compatible response satisfies

$$
|C_{ij}|\le \sum_r\sqrt{p(r\mid i)p(r\mid j)}.
\tag{9.11}
$$

Indeed $|C^{(r)}_{ij}|^2\le C^{(r)}_{ii}C^{(r)}_{jj}$ by positivity of its $2\times2$ principal minor, followed by the triangle inequality.

**Proposition 9.2 (complete binary-pointer criterion).** For a qubit Schur channel with off-diagonal multiplier $c$, two prescribed probability distributions $p_r=p(r\mid0)$ and $q_r=p(r\mid1)$ are compatible with the channel if and only if

$$
|c|\le B(p,q):=\sum_r\sqrt{p_rq_r}.
\tag{9.12}
$$

*Proof.* Necessity is the previous inequality. If $B>0$, set

$$
z_r=\frac{c}{B}\sqrt{p_rq_r},
\qquad C^{(r)}=\begin{pmatrix}p_r&z_r\\\overline z_r&q_r\end{pmatrix}.
\tag{9.13}
$$

The assumed inequality gives $|z_r|^2\le p_rq_r$, hence every $C^{(r)}$ is positive and their sum is $C$. If $B=0$, feasibility requires $c=0$ and the diagonal choices suffice. $\square$

For equal prior probabilities, let $P_{\rm err}$ be the smallest pointer-label error attainable by postprocessing a compatible readout. Writing $D_{\rm TV}(p,q)=\tfrac12\sum_r|p_r-q_r|$, Cauchy--Schwarz gives

$$
D_{\rm TV}(p,q)
\le\frac12\left[\sum_r(\sqrt p_r-\sqrt q_r)^2\right]^{1/2}
       \left[\sum_r(\sqrt p_r+\sqrt q_r)^2\right]^{1/2}
=\sqrt{1-B(p,q)^2}
\le\sqrt{1-|c|^2}.
\tag{9.14}
$$

Therefore

$$
P_{\rm err}\ge \frac{1-\sqrt{1-|c|^2}}{2}.
\tag{9.15}
$$

This lower bound is attained by the $X$ readout of (9.3) after a harmless environment phase convention for complex $c$. It is the usual two-pure-state Helstrom bound in the present channel variables [23, Eq. (12)], not a new discrimination principle. At a finite time $t$ of the dephasing semigroup with $c(t)=e^{-\gamma t}$, $\gamma>0$, this yields

$$
P_{\rm err}^{\min}(t)=\frac{1-\sqrt{1-e^{-2\gamma t}}}{2}>0.
\tag{9.16}
$$

In particular, achieving $P_{\rm err}\le\epsilon<1/2$ requires

$$
t\ge\frac{1}{2\gamma}\log\frac{1}{4\epsilon(1-\epsilon)}.
\tag{9.17}
$$

This is a bound on identifying a prepared pointer label from the environment record while retaining the specified averaged channel. It is not a theorem that individual detector outcomes cannot be definite, and it does not derive Born weighting. The environmental measurement and the standard quantum probability rule are inputs.

More generally, for a deterministic coarse pointer label $\ell(j)$, perfect readout is compatible with $\Phi_C$ if and only if

$$
C_{ij}=0\quad\text{whenever }\ell(i)\ne\ell(j).
\tag{9.18}
$$

Necessity follows from disjoint support of the response distributions. For sufficiency, use the principal blocks of $C$ on the label classes as the matrices $C^{(r)}$. Thus a nontrivial perfect pointer record is incompatible with an invertible Schur endpoint having all coherences nonzero, although approximate records and singular limits remain possible.

Pairwise tests are insufficient for three or more pointers. For example, let

$$
C=\begin{pmatrix}1&-1/2&-1/2\\-1/2&1&-1/2\\-1/2&-1/2&1\end{pmatrix}\succeq0
\tag{9.19}
$$

and prescribe four outcomes $r=0,1,2,3$ with $p(0\mid j)=1/2$, $p(j\mid j)=1/2$ and all other probabilities zero, for $j=1,2,3$. Every pair has $B=1/2=|C_{ij}|$. Nevertheless positivity forces all $C^{(r)}$ for $r=1,2,3$ to be diagonal, leaving

$$
C^{(0)}=C-\tfrac12 I,
\tag{9.20}
$$

whose smallest eigenvalue is $-1/2$. No such instrument exists. This is a concrete reason to retain the full semidefinite condition rather than replacing it by pairwise visibility bounds.

## 9.3. Interpretation and remaining selector

These results turn a qualitative ambiguity into an explicit feasibility region and operational falsifier. A microscopic proposal that prescribes a channel and record responses must satisfy the positive-decomposition test. A proposal that claims a more accurate binary pointer record than the above bound while keeping the same averaged channel is inconsistent with the stated quantum-instrument model. Conversely, satisfying these tests establishes compatibility only: it does not explain why a particular decomposition, environment POVM, or outcome is selected by a Z-Spin action.


# 10. Discussion

A complete orthogonal pointer family makes exact endpoint embeddability rigid: arbitrary integrable time dependence adds no endpoints to the Schur-embeddable class. The determinant controls the integrated dissipative budget even when Hamiltonian motion and instantaneous rates are large. Together with the entropy-production estimate, this yields square-root stability with polynomial dimensional dependence.

The computational obstruction is carried by coherence cycles rather than population transport. The fixed-alphabet, bounded-degree construction has constant-sized negative certificates, and a rational positivity-preserving approximation retains the separation. The square-root rounding theorem transfers that separation to all time-dependent Markovian channels at scale $d^{-7}$. Depolarizing regularization then gives explicit full-dimensional YES balls at scale $d^{-10}$ while retaining the NO separation. This resolves the one-sided robustness limitation without assuming a nonsingular exponential derivative at an unknown logarithm branch.

The principal remaining mathematical questions are a Lipschitz rounding bound, dimension-independent precision against the unrestricted Markovian set, membership in NP for arbitrary rational inputs, and fixed-dimension complexity for arbitrary time dependence. The present regularization does not establish homogeneous embedding for every channel in its YES ball. Singular Schur endpoints with zero coherences require separate analysis; singularity of the correlation matrix itself is different, as the all-ones matrix induces the identity channel.

The instrument results specify the admissible record responses and expose failures of pairwise compatibility tests in dimension three. They are applications of standard quantum measurement theory. A compatible positive decomposition does not select its physical implementation, create a definite event, or derive Born weighting. In a Z-Spin application, the microscopic action must still determine the subsystem, environment, coupling and readout; the present channel theorems do not identify a physical clock or an absolute scale.

# Appendix A. Exact checks and numerical implementation

## A.1. Restricting conditional positivity to the correct subspace

Let $Q$ be a $d\times(d-1)$ matrix with $Q^\dagger Q=I$ and $Q^\dagger\mathbf1=0$. The correct finite-dimensional test is

$$
\lambda_{\min}(Q^\dagger\ell Q)\ge0.
\tag{A.1}
$$

The compression $P\ell P$, $P=I-\mathbf1\mathbf1^T/d$, has a known zero mode. That mode need not be its smallest eigenvalue, so deleting the smallest eigenvalue is not a valid substitute for (A.1).

For example, set

$$
\ell=\begin{pmatrix}
0&-4&-9/5&-9/5\\
-4&0&-9/5&-9/5\\
-9/5&-9/5&0&-4\\
-9/5&-9/5&-4&0
\end{pmatrix},\qquad h=(1,1,-1,-1)^T.
\tag{A.2}
$$

The correlation matrix $C=\exp^{\circ}\ell$ has eigenvalues $1-e^{-4}$ twice and $1+e^{-4}\pm2e^{-9/5}$, all positive. Yet

$$
h^T\ell h=-\frac85,
\qquad\operatorname{spec}(P\ell P)=\{-2/5,0,4,4\}.
\tag{A.3}
$$

Thus the example is a valid channel with a genuinely negative conditional direction. Because its entries are positive real, Section 3.1 also excludes all other logarithm branches.

## A.2. Scope of the computational supplement

The arguments in the main text are analytical. The accompanying scripts check exact fixed-size identities and deterministic finite controls: the anchored quadratic form, the private-block Schur complement, rational constants in the gap estimates, positivity-preserving rounding, and the two instruments in Section 9. Finite graph checks compare capacity-two orientations with anchored positivity, including exhaustive orientation assignments for small unsatisfiable formulas. These computations check implementation and signs; they are not proofs of the universal reductions or the compactness theorem.

The supplement retains the finite checks of localized certificates, logarithmic branch gadgets, and the earlier stability estimates. It adds exact rational controls for the square-root constant chain and depolarizing Choi slack; finite numerical tests of the entropy derivative, frame transfer and nonunital time-dependent paths; perturbations in the HP TP affine space with a computable Choi-norm upper bound; and exact instrument-feasibility examples. The negative controls include purification under amplitude damping, showing why monotonicity of linear entropy cannot be assumed, and an anti-depolarizing map, showing why strict conditional positivity is needed.

High-precision floating calculations are labelled numerical, not exact certificates. Optimization that fails to locate an embeddable point supplies a search diagnostic, not a certified global distance lower bound. The inherited quick regression omits the slow adversarial path optimizer; that omission is recorded in the run output. Executable rows do not formally certify the universal theorems, whose proofs are given in the main text. The supplement records the actual environment, exact commands, finite ranges, tolerances, output classes and limitations.

# Appendix B. Variational results for two-vector record backgrounds

This appendix is independent of the rest of the paper and is not used in any proof above. Stable classical backgrounds and channel embedding are different mathematical problems. This appendix gives two complete variational calculations for prescribed two-vector potentials. They provide possible background models; no reduced quantum channel or measurement instrument is derived from them.

For $u,w:\mathbb R\to\mathbb R^n$, $n\ge2$, define

$$
\mathcal G(u,w)=|u|^2|w|^2-(u\cdot w)^2,\qquad
\mathcal E[u,w]=\int_{\mathbb R}\left[\frac{|u'|^2+|w'|^2}{2}+V(u,w)\right]dz.
\tag{B.1}
$$

The boundary condition is convergence to the two vacuum components, with the direction at either end free. Energy infima under this convention are not existence assertions for arbitrary fixed endpoint directions.

## B.1. A sharp threshold for separated radial potentials

Take $a,b,\lambda_u,\lambda_w>0$ and $\epsilon>0$, with

$$
V_\epsilon=\frac{\lambda_u}{2}(|u|^2-a^2)^2
+\frac{\lambda_w}{2}(|w|^2-b^2)^2+\epsilon\mathcal G(u,w).
\tag{B.2}
$$

The vacuum components are $\mathcal M_\pm=\{(a\nu,\pm b\nu):\nu\in S^{n-1}\}$. Put

$$
\begin{aligned}
\sigma_u&=\frac43\sqrt{\lambda_u}a^3,&
\sigma_w&=\frac43\sqrt{\lambda_w}b^3,\\
\epsilon_u&=\frac{\lambda_u a^2(a^2+b^2)}{2b^4},&
\epsilon_w&=\frac{\lambda_w b^2(a^2+b^2)}{2a^4}.
\end{aligned}
\tag{B.3}
$$

**Theorem B.1.** If $\sigma_\epsilon$ is the infimum between $\mathcal M_-$ and $\mathcal M_+$, then

$$
\sigma_\epsilon=\min(\sigma_u,\sigma_w)
\quad\Longleftrightarrow\quad
\epsilon\ge\min(\epsilon_u,\epsilon_w).
\tag{B.4}
$$

Above the threshold the cheaper radial kink attains the infimum. If $\sigma_w<\sigma_u$, every minimizer, up to a common rotation and translation, is

$$
u(z)=a\nu,\qquad
w(z)=b\tanh(\sqrt{\lambda_w}b(z-z_0))\nu.
\tag{B.5}
$$

No uniqueness assertion is made when the two radial tensions agree.

*Proof.* Suppose $\sigma_w\le\sigma_u$; the other case is symmetric. Radial projection onto $|u|\le a$ and $|w|\le b$ is $1$-Lipschitz. It decreases the separated radial terms and multiplies $\mathcal G$ by nonnegative factors at most one. Thus it cannot increase the energy and preserves the vacuum endpoints.

On the clipped region define

$$
\rho=\frac{a^2}{b^2},\quad x=\frac{|u|^2}{a^2},\quad
y=\frac{|w|^2}{b^2},\quad q=\frac{u\cdot w}{ab},
\qquad
F=\sqrt{\lambda_w}b^3\left[\frac{(3-x-y)q}{2}+\frac{q^3}{6}\right].
\tag{B.6}
$$

An exact polynomial identity is

$$
\begin{aligned}
2V_\epsilon-|\nabla F|^2
={}&b^4\frac{\lambda_w(4\rho+4-\rho x-y)}{4\rho}(x+y-1-q^2)^2\\
&+b^4\left(\lambda_u\rho^2-\frac{\lambda_w}{\rho}\right)(1-x)^2
+2(\epsilon-\epsilon_w)\mathcal G(u,w).
\end{aligned}
\tag{B.7}
$$

To check it without Cartesian expansion, set $f=F/(\sqrt{\lambda_w}b^3)$. The chain rule gives

$$
\frac{|\nabla F|^2}{\lambda_wb^4}
=\frac{4x}{\rho}f_x^2+4yf_y^2
+\left(\frac y\rho+x\right)f_q^2
+4q\left(\frac{f_xf_q}{\rho}+f_yf_q\right),
\tag{B.8}
$$

where $f_x=f_y=-q/2$ and $f_q=(3-x-y+q^2)/2$. Substitution proves (B.7).

On $x,y\le1$, its first coefficient is positive. The second is nonnegative exactly when $\lambda_u a^6\ge\lambda_w b^6$, equivalent to $\sigma_u\ge\sigma_w$. For $\epsilon\ge\epsilon_w$ all terms are therefore nonnegative. Completing the square,

$$
\mathcal E=\int\left[\frac12|(u,w)'-\nabla F|^2
+V_\epsilon-\frac12|\nabla F|^2\right]dz
+F(+\infty)-F(-\infty)\ge\sigma_w.
\tag{B.9}
$$

Here $F|_{\mathcal M_\pm}=\pm(2/3)\sqrt{\lambda_w}b^3$. The kink (B.5) attains equality. If the radial tensions are unequal, equality in (B.7) forces $x=1$ and $y=q^2$, hence collinearity; equality in (B.9) then gives $q'=\sqrt{\lambda_w}b(1-q^2)$. This proves the stated classification.

It remains to prove strict inequality below threshold. In the coordinate $\zeta=\sqrt{\lambda_w}bz$, set $e=\epsilon/\lambda_w$, $T=\tanh\zeta$, and $e_w=(1+\rho)/(2\rho^2)$. For each transverse direction the dimensionless Hessian of (B.5) is

$$
L_e=-\partial_\zeta^2+2e
\begin{pmatrix}T^2&-\sqrt\rho T\\-\sqrt\rho T&\rho\end{pmatrix}
-2\operatorname{sech}^2\zeta\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\tag{B.10}
$$

The symmetric matrix

$$
W=\begin{pmatrix}T/\rho&-1/\sqrt\rho\\-1/\sqrt\rho&T\end{pmatrix}
\quad\text{satisfies}\quad
L_{e_w}=(-\partial_\zeta+W)(\partial_\zeta+W).
\tag{B.11}
$$

Let $k=1+1/\rho$, $\phi(\zeta)=\rho^{-1}\int_0^\zeta\operatorname{sech}^k s\,ds$, and

$$
\psi_*(\zeta)=\begin{pmatrix}\sqrt\rho\phi(\zeta)\\T\phi(\zeta)+\operatorname{sech}^k\zeta\end{pmatrix}.
\tag{B.12}
$$

Direct differentiation gives $(\partial_\zeta+W)\psi_*=0$. The vector is bounded, and for $v=(T,-\sqrt\rho)^T$,

$$
L_e=L_{e_w}+2(e-e_w)vv^T,\qquad
v^T\psi_*=-\sqrt\rho\operatorname{sech}^k\zeta.
\tag{B.13}
$$

Choose a smooth cutoff $\chi_R$ equal to one on $[-R,R]$, zero outside $[-2R,2R]$, with derivative $O(R^{-1})$. Then

$$
\begin{aligned}
\langle\chi_R\psi_*,L_e\chi_R\psi_*\rangle
={}&\int|\chi_R'|^2|\psi_*|^2d\zeta\\
&+2(e-e_w)\rho\int\chi_R^2\operatorname{sech}^{2k}\zeta\,d\zeta.
\end{aligned}
\tag{B.14}
$$

For $e<e_w$, the first term tends to zero and the second to a strictly negative finite number. A compactly supported transverse variation therefore lowers the kink energy. Finally $\epsilon_u/\epsilon_w=\sigma_u^2/\sigma_w^2$, so the cheaper kink has the smaller threshold. This proves (B.4) without assuming the existence of a noncollinear minimizer below threshold. $\square$

The completion-of-squares method is classical; related Bogomolny arguments for complex-field walls appear in [8]. The calculation above specifies the clipping domain, the two competing radial tensions, and the exact full-vector threshold. It does not apply to an arbitrary nonseparable or Yukawa-corrected potential.

## B.2. An exchange-symmetric mixed radial potential

Let $a>0$, $\lambda>|\kappa|$, and $\epsilon>0$. Consider

$$
V=\frac\lambda2\bigl[(|u|^2-a^2)^2+(|w|^2-a^2)^2\bigr]
+\kappa(|u|^2-a^2)(|w|^2-a^2)+\epsilon\mathcal G(u,w).
\tag{B.15}
$$

Set $\Lambda=\lambda+\kappa>0$ and $h=\lambda-\kappa>0$.

**Theorem B.2.** The minimum tension between $\{(a\nu,-a\nu)\}$ and $\{(a\nu,a\nu)\}$ is

$$
\sigma(\epsilon)=\mathcal S(\min\{\epsilon,h\}),
\tag{B.16}
$$

where

$$
\mathcal S(g)=\min_{r,s\ge0}\int_{\mathbb R}\left[
\frac{r'^2+s'^2}{2}+\frac\Lambda4(r^2+s^2-2a^2)^2+gr^2s^2\right]dz,
\tag{B.17}
$$

with endpoints $(\sqrt2a,0)$ and $(0,\sqrt2a)$. For $g>0$ the minimum exists and $\mathcal S(g)$ is strictly increasing. The global plateau and the full-field linear stability of the collinear minimizing branch have the same threshold $\epsilon=h$.

*Proof.* The orthogonal variables $x=(u+w)/\sqrt2$, $y=(u-w)/\sqrt2$ preserve the kinetic energy and give

$$
V=\frac\Lambda4(|x|^2+|y|^2-2a^2)^2
+\epsilon|x|^2|y|^2+(h-\epsilon)(x\cdot y)^2.
\tag{B.18}
$$

For $r=|x|$, $s=|y|$, the kinetic energy is at least $(r'^2+s'^2)/2$. If $h\ge\epsilon$, fixed orthogonal directions attain the angular minimum. If $h\le\epsilon$, fixed parallel directions attain it. Both lifts are admissible because the endpoint directions are free. This proves (B.16).

The substitution $r=\sqrt2aR$, $s=\sqrt2aS$, $\xi=\sqrt{2\Lambda}az$ reduces the scalar Euler--Lagrange system to the coupled Gross--Pitaevskii domain-wall problem with parameter $1+2g/\Lambda>1$. Its variational existence and endpoint decay follow from [9, Theorems 1.1 and 2.1]. The nonnegative minimizing amplitudes are strictly positive at every finite point by ODE uniqueness. Thus, for $g_2>g_1>0$ and a minimizer at $g_2$,

$$
\mathcal S(g_2)\ge\mathcal S(g_1)+(g_2-g_1)\int r_{g_2}^2s_{g_2}^2dz
>\mathcal S(g_1).
\tag{B.19}
$$

Let $(r_0,s_0)$ minimize (B.17) at $g=h$ and lift it with parallel fixed directions. This is a stationary collinear branch for every $\epsilon$. For $\epsilon\ge h$ it is globally minimizing and its second variation is nonnegative. If $\epsilon<h$, rotate only the $y$ direction by a small angle $\tau\chi_R(z)$. The exact second variation is

$$
\delta^2\mathcal E=\int s_0^2(\chi_R')^2dz
-2(h-\epsilon)\int r_0^2s_0^2\chi_R^2dz
\longrightarrow-2(h-\epsilon)\int r_0^2s_0^2dz<0.
\tag{B.20}
$$

The cutoff keeps the endpoints fixed. This proves the stability threshold. $\square$

At $g=\Lambda$, the explicit profile is

$$
r=\frac a{\sqrt2}\bigl[1-\tanh(a\sqrt\Lambda z)\bigr],\qquad
s=\frac a{\sqrt2}\bigl[1+\tanh(a\sqrt\Lambda z)\bigr],\qquad
\mathcal S(\Lambda)=\frac43a^3\sqrt\Lambda.
\tag{B.21}
$$

It is the standard parameter-$3$ Gross--Pitaevskii wall [9, equation (5)]. The additional vector calculation is the exact angular minimization and the coincidence of the plateau and stability thresholds. Neither theorem in this appendix establishes domain-wall formation, cosmological lifetime, an informative readout, or a preferred time scale.

# Data, code, and AI assistance

The accompanying source package contains the editable manuscript, LaTeX source, local verification scripts, run outputs, source-comparison ledger and research report. Numerical checks have only the limited role stated in Appendix A. No public archival DOI or repository release is asserted.

Anthropic Claude contributed earlier endpoint rigidity, eigenvector-attachment, localized-certificate and quarter-power stability arguments. OpenAI Codex contributed the determinant-budget and bounded-degree routes in earlier versions, and the square-root purity argument, quantitative interior regularization, strengthened rational-input promises and instrument exposition in this version. Codex reviewed the inherited Claude proofs; separate Codex agents reconstructed and attacked the new proofs, sharing model lineage and therefore providing low-independence review. The finite executable checks are disclosed separately from proof review. AI assistance is not authorship or human peer review. No qualified human review or machine-checked formal proof is claimed; scientific responsibility and external release remain with the human researcher.

# References

[1] T. S. Cubitt, J. Eisert, and M. M. Wolf, "The complexity of relating quantum channels to master equations," *Communications in Mathematical Physics* **310**, 383--418 (2012). [arXiv:0908.2128](https://arxiv.org/abs/0908.2128).

[2] M. M. Wolf and J. I. Cirac, "Dividing quantum channels," *Communications in Mathematical Physics* **279**, 147--168 (2008). [arXiv:math-ph/0611057](https://arxiv.org/abs/math-ph/0611057).

[3] F. Fagnola, J. E. Gough, H. I. Nurdin, and L. Viola, "Mathematical models of Markovian dephasing," *Journal of Physics A: Mathematical and Theoretical* **52**, no. 38 (2019). [doi:10.1088/1751-8121/ab38ec](https://doi.org/10.1088/1751-8121/ab38ec); [arXiv:1811.11784](https://arxiv.org/abs/1811.11784).

[4] Y. Asahiro, J. Jansson, E. Miyano, H. Ono, and K. Zenmyo, "Approximation algorithms for the graph orientation minimizing the maximum weighted outdegree," *Journal of Combinatorial Optimization* **22**, 78--96 (2011). [Author-hosted manuscript](https://www.math.ucdavis.edu/~saito/data/graph-ori/asahiro-etal_approx-graph-ori-min-max-outdegs.pdf).

[5] C. Carlson, K. Chandrasekaran, H.-C. Chang, and A. Kolla, "Invertibility and largest eigenvalue of symmetric matrix signings," arXiv:1611.03624 (2016; revised 2017). [arXiv:1611.03624](https://arxiv.org/abs/1611.03624).

[6] S. Sanchez, "On the supremal $p$-negative type of a finite metric space," arXiv:1108.0451 (2011). [arXiv:1108.0451](https://arxiv.org/abs/1108.0451).

[7] C. A. Fuchs and J. van de Graaf, "Cryptographic distinguishability measures for quantum-mechanical states," *IEEE Transactions on Information Theory* **45**, 1216--1227 (1999). [arXiv:quant-ph/9712042](https://arxiv.org/abs/quant-ph/9712042).

[8] S. R. Woodford and I. V. Barashenkov, "Stability of the Bloch wall via the Bogomolnyi decomposition in elliptic coordinates," arXiv:0803.2299 (2008). [arXiv:0803.2299](https://arxiv.org/abs/0803.2299).

[9] S. Alama, L. Bronsard, A. Contreras, and D. E. Pelinovsky, "Domain walls in the coupled Gross--Pitaevskii equations," *Archive for Rational Mechanics and Analysis* **215**, 579--610 (2015). [arXiv:1309.1222](https://arxiv.org/abs/1309.1222).

[10] H. Helm, W. T. Strunz, S. Rietzler, and L. E. Würflinger, "Characterization of decoherence from an environmental perspective," arXiv:1012.4685 (2010). [arXiv:1012.4685](https://arxiv.org/abs/1012.4685).

[11] S. Johansen, "The imbedding problem for Markov chains," Preprint 1973 No. 10, Institute of Mathematical Statistics, University of Copenhagen (1973); see also S. Johansen, "A central limit theorem for finite semigroups and its application to the imbedding problem for finite state Markov chains," *Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete* **26**, 171--190 (1973). [Preprint](https://www.math.ku.dk/bibliotek/arkivet/preprints-fra-ims/1973/preprint_1973_-_no_10_johansen__s_ren_-_the_imbedding_problem_for_markov_chains.pdf).

[12] G. S. Goodman, "An intrinsic time for non-stationary finite Markov chains," *Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete* **16**, 165--180 (1970).

[13] T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed. (Springer, Berlin, 1976).

[14] R. Bhatia, *Matrix Analysis*, Graduate Texts in Mathematics **169** (Springer, New York, 1997).

[15] M. Grötschel, L. Lovász, and A. Schrijver, *Geometric Algorithms and Combinatorial Optimization* (Springer, Berlin, 1988).

[16] M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (W. H. Freeman, San Francisco, 1979).

[17] T. S. Cubitt, J. Eisert, and M. M. Wolf, "Extracting dynamical equations from experimental data is NP hard," *Physical Review Letters* **108**, 120503 (2012). [arXiv:1005.0005](https://arxiv.org/abs/1005.0005).

[18] M. C. Caro and B. Graswald, "Necessary criteria for Markovian divisibility of linear maps," *Journal of Mathematical Physics* **62**, 042203 (2021). [arXiv:2009.06666](https://arxiv.org/abs/2009.06666).

[19] E. Onorati, T. Kohler, and T. S. Cubitt, "Fitting time-dependent Markovian dynamics to noisy quantum channels," arXiv:2303.08936 (2023). [arXiv:2303.08936](https://arxiv.org/abs/2303.08936).

[20] J. Bausch and T. Cubitt, "The complexity of divisibility," *Linear Algebra and its Applications* **504**, 64--107 (2016). [arXiv:1411.7380](https://arxiv.org/abs/1411.7380).

[21] F. Shahbeigi, C. T. Chubb, R. Kukulski, Ł. Pawela, and K. Korzekwa, "Quantum-embeddable stochastic matrices," arXiv:2305.17163v2 (2024). [arXiv:2305.17163](https://arxiv.org/abs/2305.17163).

[22] T. Heinosaari, T. Miyadera, and D. Reitzner, "Strongly incompatible quantum devices," *Foundations of Physics* **44**, 34--57 (2014). [arXiv:1209.1382](https://arxiv.org/abs/1209.1382).

[23] S. M. Barnett and S. Croke, "Quantum state discrimination," *Advances in Optics and Photonics* **1**, 238--278 (2009). [arXiv:0810.1970](https://arxiv.org/abs/0810.1970).
