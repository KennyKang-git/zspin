#!/usr/bin/env python3
"""ZS-M68 v1.4.1 paper-level verifier (Ref_202609060700).

v1.4.1 delta over v1.4 (v1.4 audit AUDIT-PASS-MINOR, S1, 2026-09-06 KST; four local findings, no S2):
  * C20 and C61 claims now carry the SOLDERED-class hypothesis w = ±e_J explicitly (audit F1): the angle-free ceiling
    2 sqrt(1-M_*^2)/(2-M_*^2) and the fixed-angle envelope B(c) are class statements, and the stored claim strings are what a
    downstream reader extracts. The scalar arithmetic of both rows is unchanged.
  * C34's `sp.N(phi**-8) < 1` and C61's `abs(B(c_crit) - T_2) < 1e-28` are replaced by exact certificates (audit F2):
    phi^-8 = (47 - 21 sqrt5)/2 with 47^2 > 21^2*5 > 45^2, and the symbolic identity B(c_crit) = rho together with the exact
    rational comparisons m_max < T_2 < 2 m_max/(1+m_max^2) which place c_crit in (-1, 0). No C row's PASS decision now
    contains a floating-point or tolerance term -- and G69 below checks that mechanically instead of asserting it in prose.
  * new rows: W69 (comparison; general-class counterexample to the ANGLE-FREE ceiling: w = e_K, m = p e_K with p in [M_*,1) gives
    T = p >= M_*, T_w = 0 and |kappa_*| = p faithfully at every admissible angle, so the general-class supremum under the M60 floor
    is 1; the A-derived p = tanh 2eta = 3 sqrt5/7 of Cor 5.12 already exceeds 0.911564753...), C70 (the coherence functionals
    coincide FOR EVERY reference iff w = ±e_J; at a single state they can coincide off that axis -- m = (1/2,0,1/2), w = e_K; audit F3),
    G69 (numeric-purity guard: no C-row PASS-decision clause of THIS script contains sp.N / float / mp.mpf / abs(...)/tolerance tokens).
  * G40's comparison-row list includes W69; G41/G42 name the v1.4.1 objects; G42's stale-token list includes the v1.4 tokens.

v1.4 delta over v1.3 (v1.3 audit AUDIT-MAJOR-REVISION, S2, 2026-09-06 KST, deterministic L5 + L4 source re-entry; two S2 scope defects, five S1 items):
  * new rows: W66 (comparison; the K10 envelope of Cor 7.1 / C61 is a SOLDERED-class (w = ±e_J) statement: in the general Clifford-pair class
    the joint demand T >= M_* and |kappa_*| = T_2 on one reference is attained faithfully at c = 0 > c_crit -- w = e_K, m = T_2 e_K, alpha = pi/4,
    M = 0, kappa_* = -T_2 exactly; audit F2), C67 (the A-derived longitudinal family sigma_q = A^q/tr A^q = (I + tanh(q eta) K)/2 with resource axis
    w = e_K = (2A - 3I)/sqrt5 gives a faithful biased fixed point -chi tanh(q eta), margin sech^2(q eta), at every admissible angle; Lemma 3.3 only
    excludes a J-population of f(A); the v1.3 §6.7 prohibition "must not be a function of A alone" is withdrawn; audit F1), C68 (the conditional
    supremum 2a/(1+a^2) is attained at the endpoints a = |w_K| in {0, 1}; "not attained" needs 0 < a < 1; audit F4).
  * retyped rows: C60 now also tests the NEGATIVE axis w = -e_K (kappa_inf = -chi w_K m_K(0): at w_K = -1, m_K(0) = 1/2, chi = +1 the record is +1/2;
    the v1.3 row tested w_K = +1 only; audit F3); C63 now checks U = -chi Z(x)Z per chirality (the v1.3 row accepted either sign; audit F5);
    C32's endpoint conjunct is exact (the v1.3 row still carried an `or bool(sp.N(...))` clause on that conjunct although the exact branch decided it; audit F7).
  * G40's comparison-row list now includes W66 (seven comparison rows); G41/G42 name the v1.4 objects; G42's stale-token list includes the v1.3 tokens.
v1.3 delta over v1.2 (v1.2 audit AUDIT-MAJOR-REVISION, S2, 2026-09-06, deterministic L5/L4 review):
  * C32 now certifies the strength law EXACTLY with no numerical fallback: the two radicands are shown to be the same polynomial
    1 - 7t + t^2 (t = lambda^-2; e^{2eta} e^{-2eta} = 1, e^{2eta} + e^{-2eta} = 7) so the two parametrisations agree as principal roots;
    the v1.2 row contained an `or all(...)` three-sample fallback that decided the PASS (audit F4). C31's claim string is re-worded to
    what it tests (reference rapidity identity); C54's tautological conjunct is removed.
  * new rows: W59 (Schur-stable channel with one-step trace-distance preservation: Schur stability is not one-step strict contractivity),
    C60 (unconditional limiting record is zero iff w_K m_K(0) = 0; |w_K| = 1 with 0 < |m_K(0)| < 1 gives a faithful biased record),
    C61 (K10 fixed-angle envelope B(c) = m_max(1-c)/(1-m_max^2 c); exclusion iff c > c_crit; cos2alpha >= 0 is sufficient, not necessary),
    C62 (two-return capacity witness 16/19 > T_2 at the finite angle cos2alpha = -3/5 on consecutive points of the pure passive orbit),
    C63 (excluded angles: alpha = pi identity, alpha = pi/2 gives Ad_{J_E}), W64 (the rounded threshold 0.5391 is not the exact boundary),
    C65 (trace-t generalisation of the dephasing factor: f_t = ((t - sqrt(t^2-4))/2)^2; the mechanism is not specific to tr A = 3).
  * G42 now also checks the one-command run line and the banner census against the ledger classes (audit §5.2); it still does not check hashes
    (make_manifest_v1_3.py --check does that after injection).
v1.2 delta over v1.1 (v1.1 audit AUDIT-MAJOR-REVISION, S2, 2026-09-05, different lineage; full v1.0 audit report received):

v1.2 delta over v1.1 (v1.1 audit AUDIT-MAJOR-REVISION, S2, 2026-09-05, different lineage; full v1.0 audit report received):
  * carried rows C01-W39 keep their ids. Retyped/replaced: C13 (quantifier sin2alpha!=0 added to the claim), C19/C20 (now EXACT
    rational comparisons on the locked decimals read as rationals -- class C is retained on that basis; previously 30-digit mpmath
    comparisons), C32 (exact monotonicity certificate instead of sampled derivative signs), C33 (fixed family wording: only the pure
    endpoints are the N=2 extremal orbit), W35 (the v1.1 random-rotation part found 0 fixed vectors and was vacuous; it is now a
    targeted family with found fixed vectors plus the lemma "fixed vector iff R e_K = e_K" checked on random rotations), G40-G42/D43 (v1.2).
  * new rows for every audit counterexample and repair identity: C44 (joint-grading transform sign + symmetry classification),
    W45 (grading-odd frame with w_K = 0 and zero limiting record), W46 (same resource axis, different Hamiltonian/channel),
    W47 (pure pole at |w_K| = 1; zero unconditional bias at m_K(0) = 0), C48 (threshold: supremum not attained, exact gap, inverse angle),
    C49 (alpha = pi/2 channel diag(-1,-1,1), b = 0), C50 (carrier recurrence closed form, exact 4x4 counterexample, failure branch
    stores no transverse expectation), C51 (failure-branch unitary: unital iff V K V^dag = K; det Q(3) = 19/81), C52 (characteristic
    polynomial + Jury identities: Schur stability for every reference), V53 (sequential fresh-copy collisions converge, both readings),
    C54 (unconditional supremum formula), C55 (v1.0 leftovers: H_chi^2 sign, D endpoints, second-bound equality identity),
    W56 (time-dependent unital refresh depletion), V57 (comparison at |w_K| = x(T_2): kappa < T_2 at an admissible angle),
    C58 (maximal-strength failure-state feedback: longitudinal law, fixed point x = 1 for v_K > -1).
Result classes: PASS / FAIL / SKIP.  exit 0 iff 0 FAIL; with --strict, exit 0 iff 0 FAIL and 0 SKIP.

Deterministic L5 checks for the theorem block of ZS-M68 v1.4.1. Rows are typed
  C  exact/symbolic certificate of a stated identity or inequality (NOT a proof of a universal theorem
     unless the check itself is symbolic over free parameters -- see 'universal' flag)
  W  finite witness / counter-witness (specific instance)
  V  numerical reproduction with declared tolerance
  G  guard (structural)
  D  declaration (no evidence)
P = 0: no row is a written proof; proofs are in the manuscript.
Rows tagged comparison=True are the only rows allowed to mention the Z-Spin locked inputs
(T_2, M_*); every construction row is target-blind.
Run:  python3 zs_m68_verify_v1_4_1.py [path/to/ZS-M68_v1_4_1.md] [--strict]  -> writes zs_m68_verify_v1_4_1.json next to the script.
"""
import json, os, sys, hashlib, platform
import sympy as sp
import numpy as np
import mpmath as mp

PAPER = 'ZS-M68 v1.4.1'
SCRIPT = os.path.basename(__file__)
HERE = os.path.dirname(os.path.abspath(__file__))
rows = []
def add(rid, cls, claim, ok, detail='', universal=False, comparison=False):
    res = 'SKIP' if ok is None else ('PASS' if bool(ok) else 'FAIL')
    rows.append({'id': rid, 'class': cls, 'claim': claim, 'result': res,
                 'detail': str(detail), 'universal': bool(universal), 'comparison': bool(comparison)})

# ---------------------------------------------------------------- reference fibre, normal form
I2 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.diag(1, -1)
K = sx; J = sz; Kp = sp.I * J * K                        # K' := iJK
phi = (1 + sp.sqrt(5)) / 2
eta = sp.log(phi**2)                                      # = arcosh(3/2), written so that sympy can simplify exactly
def S(e):
    if isinstance(e, sp.MatrixBase): return e.applyfunc(S)
    return sp.simplify(sp.radsimp(sp.expand(sp.simplify(e.rewrite(sp.exp)))))
def Z(e):   # robust zero test for trig/complex matrix expressions
    if isinstance(e, sp.MatrixBase): return e.applyfunc(Z)
    return sp.simplify(sp.expand(sp.expand(e).rewrite(sp.exp)))
A = sp.cosh(eta) * I2 + sp.sinh(eta) * K                  # A = exp(eta K)

# C01 normal form of the reversible pair
ok = (S(sp.trace(A) - 3) == 0 and S(sp.det(A) - 1) == 0
      and S(J * A * J - A.inv()) == sp.zeros(2, 2)
      and set(S(e) for e in A.eigenvals()) == {S(phi**2), S(phi**-2)}
      and S(sp.exp(eta) - phi**2) == 0 and S(sp.cosh(eta) - sp.Rational(3, 2)) == 0)
add('C01', 'C', 'reversible pair in normal form: A=exp(eta K), tr A=3, det A=1, JAJ=A^{-1}, spec A={phi^2,phi^-2}, e^eta=phi^2, |eig A|!=1',
    ok, f'eta={sp.N(eta,20)}', universal=True)

# C02 oriented odd frame
ok = (Kp == -sy and sp.simplify(Kp.H - Kp) == sp.zeros(2, 2) and sp.simplify(Kp * Kp - I2) == sp.zeros(2, 2)
      and sp.simplify(J * Kp + Kp * J) == sp.zeros(2, 2) and sp.simplify(K * Kp + Kp * K) == sp.zeros(2, 2))
add('C02', 'C', "K'=iJK is self-adjoint for the normal-form h_L (K'^dag=K'), K'^2=I, {J,K'}={K,K'}=0, normal form -sigma_y",
    ok, "K'=" + str(Kp.tolist()), universal=True)

# C03 reversal-blindness: A^n = (L_{2n} I + sqrt5 F_{2n} K)/2 and Tr f(A) J = 0
ok = True
for n in range(1, 8):
    An = S(A**n)
    target = (sp.lucas(2 * n) * I2 + sp.sqrt(5) * sp.fibonacci(2 * n) * K) / 2
    ok &= S(An - target) == sp.zeros(2, 2)
    ok &= S(sp.trace(An * J)) == 0
add('C03', 'C', 'A^n = (L_{2n} I + sqrt5 F_{2n} K)/2 and Tr(A^n J)=0 for n=1..7 (hence Tr f(A)J=0 for polynomial f)', ok, 'n=1..7 exact')

# C04 full Bloch filtering law (symbolic in m and in c=cosh n eta, s=sinh n eta)
mK, mKp, mJ = sp.symbols('m_K m_Kp m_J', real=True)
c, s = sp.symbols('c s', positive=True)
sig = (I2 + mK * K + mKp * Kp + mJ * J) / 2
An = c * I2 + s * K
out = sp.expand(An * sig * An)
tr = sp.simplify(sp.trace(out))
comps = [sp.simplify(sp.trace(out * X) / tr) for X in (K, Kp, J)]
C2, S2 = c**2 + s**2, 2 * c * s                 # cosh 2n eta, sinh 2n eta
pred = [(S2 + mK * C2) / (C2 + mK * S2), mKp / (C2 + mK * S2), mJ / (C2 + mK * S2)]
ok = all(sp.simplify((x - y).subs(s**2, c**2 - 1)) == 0 for x, y in zip(comps, pred))
add('C04', 'C', 'Theorem 4.1: sigma -> A^n sigma A^n / tr gives m_K(n)=(sinh2neta+m_K cosh2neta)/(cosh2neta+m_K sinh2neta), m_J(n)=m_J/(cosh2neta+m_K sinh2neta), same for m_Kp (symbolic in m and n)',
    ok, 'symbolic; c^2-s^2=1 used', universal=True)

# C05 rapidity form
z0, x = sp.symbols('zeta_0 x', real=True)
ok = (sp.simplify(sp.cosh(x) + sp.tanh(z0) * sp.sinh(x) - sp.cosh(z0 + x) / sp.cosh(z0)) == 0
      and sp.simplify((sp.sinh(x) + sp.tanh(z0) * sp.cosh(x)) / (sp.cosh(x) + sp.tanh(z0) * sp.sinh(x)) - sp.tanh(z0 + x)) == 0)
add('C05', 'C', 'rapidity addition: with m_K(0)=tanh zeta_0 and x=2n eta, m_K(n)=tanh(zeta_0+x), m_J(n)=m_J(0) cosh zeta_0 / cosh(zeta_0+x)',
    ok, 'symbolic in zeta_0, x', universal=True)

# C06 return-invariant references: A sigma A ∝ sigma  iff  m = (±1,0,0)
out1 = sp.expand(A * sig * A)
lam = sp.symbols('lambda', positive=True)
eqs = list(out1 - lam * sig)
sols = sp.solve(eqs + [mK**2 + mKp**2 + mJ**2 - 1], [mK, mKp, mJ, lam], dict=True)
inball = sp.solve(eqs, [mK, mKp, mJ, lam], dict=True)
ok = (set((sp.simplify(d[mK]), sp.simplify(d[mKp]), sp.simplify(d[mJ])) for d in inball) == {(1, 0, 0), (-1, 0, 0)})
add('C06', 'C', 'Proposition 4.2: A sigma A ∝ sigma iff m=(±1,0,0) (the two light-cone pure states), so every return-invariant reference has m_J=0',
    ok, f'solutions={[(d[mK],d[mKp],d[mJ]) for d in inball]}', universal=True)

# C07 Stokes boost
nn = sp.symbols('n', positive=True)
Lam = sp.Matrix([[sp.cosh(2*nn*eta), sp.sinh(2*nn*eta), 0, 0], [sp.sinh(2*nn*eta), sp.cosh(2*nn*eta), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
g = sp.diag(1, -1, -1, -1)
# un-normalised Stokes vector S=(tr, tr K, tr K', tr J) of A^n sigma A^n
S_in = sp.Matrix([1, mK, mKp, mJ])
S_out = sp.Matrix([sp.trace(out), sp.trace(out*K), sp.trace(out*Kp), sp.trace(out*J)])
Lam_cs = sp.Matrix([[C2, S2, 0, 0], [S2, C2, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
ok = (sp.simplify(Lam.T * g * Lam - g) == sp.zeros(4, 4)
      and sp.simplify((S_out - Lam_cs * S_in).subs(s**2, c**2 - 1)) == sp.zeros(4, 1))
add('C07', 'C', 'Theorem 4.3: on the un-normalised Stokes 4-vector one transfer is a pure Lorentz boost of rapidity 2n eta along K; S_J is transverse',
    ok, 'symbolic', universal=True)

# C08 universal depletion
ok = (sp.simplify(sp.tanh(z0)**2 + 1/sp.cosh(z0)**2 - 1) == 0
      and S(sp.exp(2*eta) - phi**4) == 0
      and sp.limit(1/sp.cosh(z0 + 2*nn*eta), nn, sp.oo) == 0
      and S(1/sp.cosh(2*eta) - sp.Rational(2, 7)) == 0)
add('C08', 'C', 'Theorem 4.4: m_J(0)^2 <= 1 - tanh^2 zeta_0 = sech^2 zeta_0, hence |m_J(n)| <= sech(zeta_0+2n eta) -> 0 with e^{2eta}=phi^4 per return; sech(2eta)=2/7',
    ok, 'symbolic', universal=True)

# C09 N-return persistence ceiling
ok = (S(1/sp.cosh(eta) - sp.Rational(2, 3)) == 0 and S(1/sp.cosh(2*eta) - sp.Rational(2, 7)) == 0)
# sharpness: pure orbit m_J(n) = sech(x_n) exactly
pure = sig.subs({mK: sp.tanh(z0), mKp: 0, mJ: 1/sp.cosh(z0)})
o = sp.expand(A * pure * A)
mJ1 = sp.trace(o*J)/sp.trace(o)
ok &= S(mJ1 - 1/sp.cosh(z0 + 2*eta)) == 0
ok &= sp.simplify(sp.det(pure)) == 0
add('C09', 'C', 'Theorem 4.5: |m_J|>=r at N consecutive returns forces r <= sech((N-1)eta); N=2: 2/3, N=3: 2/7; sharp on the pure orbit m_J(n)=sech(zeta_0+2n eta)',
    ok, 'sech(eta)=2/3 exact; pure orbit exact', universal=True)

# C10 K12b constant same-axis counterboost
chi = sp.symbols('chi', real=True)
zn = z0 + nn * (2*eta - chi)
sol_chi = sp.solve(sp.Eq(sp.diff(zn, nn), 0), chi)
ok = (len(sol_chi) == 1 and S(sol_chi[0] - 2*eta) == 0)
B = sp.cosh(eta) * I2 - sp.sinh(eta) * K        # exp(-(chi/2) K) at chi = 2 eta
ok &= S(B * A - I2) == sp.zeros(2, 2)
over = sp.limit(1/sp.cosh(zn.subs(chi, 3*eta)), nn, sp.oo)
ok &= over == 0
add('C10', 'C', 'Theorem 6.2: zeta_n = zeta_0 + n(2eta-chi); nonzero asymptotic record iff chi = 2eta; chi=3eta overshoots (sech->0); at chi=2eta the same-axis cycle is the identity map',
    ok, 'symbolic', universal=True)

# C11 replacement channel is CPTP
r = sp.symbols('r', real=True)
sig_r = (I2 + r*J)/2
choi = sp.kronecker_product(I2, sig_r)
ok = set(map(sp.simplify, choi.eigenvals().keys())) == {(1+r)/2, (1-r)/2} and sp.simplify(sp.trace(sig_r) - 1) == 0
add('C11', 'C', 'Proposition 6.3: R_r(X)=Tr(X) sigma_r has Choi matrix I⊗sigma_r >= 0 for |r|<=1 and is trace preserving; it restores m_J=r after every return',
    ok, 'Choi eigenvalues (1±r)/2', universal=True)

# C12 abelian coupling => unital + flip-covariant (symbolic environment of dimension 3)
b1, b2, b3, al = sp.symbols('b1 b2 b3 alpha', real=True)
XE = sx                                            # flip on the carrier
Benv = sp.diag(b1, b2, b3)
U = sp.zeros(6, 6)
for j, bj in enumerate((b1, b2, b3)):
    ej = sp.zeros(3, 3); ej[j, j] = 1
    U += sp.kronecker_product(sp.cos(al*bj)*I2 - sp.I*sp.sin(al*bj)*XE, ej)   # exp(-i alpha X⊗B)
# generic environment state (pure, symbolic amplitudes) -> Kraus E_j = <j|U|psi>
a1, a2, a3 = sp.symbols('a1 a2 a3')
psi = sp.Matrix([a1, a2, a3])
Kraus = []
for j in range(3):
    ej = sp.zeros(3, 1); ej[j] = 1
    Ej = sp.kronecker_product(I2, ej.T) * U * sp.kronecker_product(I2, psi)
    Kraus.append(sp.simplify(Ej))
unital = sp.simplify(sum((E*E.H for E in Kraus), sp.zeros(2, 2)) - sum((E.H*E for E in Kraus), sp.zeros(2, 2)))
inalg = all(sp.simplify(E*XE - XE*E) == sp.zeros(2, 2) for E in Kraus)
rho = sp.Matrix(2, 2, sp.symbols('r11 r12 r21 r22'))
Phi = lambda R: sum((E*R*E.H for E in Kraus), sp.zeros(2, 2))
cov = sp.simplify(Phi(XE*rho*XE) - XE*Phi(rho)*XE)
ok = unital == sp.zeros(2, 2) and inalg and cov == sp.zeros(2, 2)
add('C12', 'C', 'Theorem 5.1: for H=X_E⊗B (any B, any environment state, any alpha) every Kraus operator lies in C[X_E]; the channel is unital (sum EE^dag = sum E^dag E) and Ad_X covariant',
    ok, 'symbolic d_E=3, generic pure environment state, generic alpha', universal=True)

# C13 chiral record-transfer affine map, both chiralities
def chiral_map(chir):
    H = sp.kronecker_product(sx, K) + chir * sp.kronecker_product(sy, Kp)
    Uc = sp.simplify((-sp.I*al*H).exp())
    rx, ry, rz = sp.symbols('r_x r_y r_z', real=True)
    rho2 = (I2 + rx*sx + ry*sy + rz*sz)/2
    R = sp.kronecker_product(rho2, sig)
    o = Uc * R * Uc.H
    red = sp.zeros(2, 2)
    for i in range(2):
        for j in range(2):
            red[i, j] = sum(o[2*i+k, 2*j+k] for k in range(2))
    comps = [sp.simplify(sp.trace(red*X)) for X in (sx, sy, sz)]
    M = sp.Matrix([[sp.simplify(sp.diff(cc, v)) for v in (rx, ry, rz)] for cc in comps])
    bvec = sp.Matrix([sp.simplify(cc.subs({rx: 0, ry: 0, rz: 0})) for cc in comps])
    return sp.simplify(M), sp.simplify(bvec), (rx, ry, rz)
T2 = mK**2 + mKp**2
ok = True; det_ok = True; fp_ok = True
for chir in (1, -1):
    M, bvec, rv = chiral_map(chir)
    b_pred = sp.Matrix([0, 0, -chir * mJ * sp.sin(2*al)**2])
    ok &= sp.simplify(bvec - b_pred) == sp.zeros(3, 1)
    M_pred = sp.Matrix([[sp.cos(2*al), 0, chir*mKp*sp.sin(2*al)],
                        [0, sp.cos(2*al), -mK*sp.sin(2*al)],
                        [-chir*mKp*sp.sin(4*al)/2, mK*sp.sin(4*al)/2, sp.cos(2*al)**2]])
    ok &= sp.simplify((M - M_pred).rewrite(sp.exp)) == sp.zeros(3, 3)
    d = sp.simplify(sp.det(sp.eye(3) - M))
    det_ok &= sp.simplify((d - 2*sp.sin(2*al)**2*sp.sin(al)**2*(1 - (1 - T2)*sp.cos(2*al))).rewrite(sp.exp)) == 0
    rvec = sp.Matrix(rv)
    sol = sp.solve(list(M*rvec + bvec - rvec), rv, dict=True)[0]
    D = 1 - (1 - T2)*sp.cos(2*al)
    pred = {rv[0]: -mJ*mKp*sp.sin(2*al)/D, rv[1]: chir*mJ*mK*sp.sin(2*al)/D, rv[2]: -chir*mJ*(1 - sp.cos(2*al))/D}
    fp_ok &= all(sp.simplify((sol[k] - pred[k]).rewrite(sp.exp)) == 0 for k in rv)
add('C13', 'C', 'Theorem 5.2 (map): H_chi = X_E⊗K + chi Y_E⊗K\' gives an affine Bloch map r -> M r + b with b = -chi m_J sin^2(2alpha) e_J and the full 3x3 matrix M of Theorem 5.2 (M_JJ = cos^2 2alpha, M_KK=M_K\'K\' = cos 2alpha, M_{K J}=chi m_K\' sin2alpha, M_{K\' J}=-m_K sin2alpha, M_{J K}=-chi m_K\' sin4alpha/2, M_{J K\'}=m_K sin4alpha/2); b=0 iff m_J=0 WHEN sin2alpha != 0 (at sin2alpha=0, b=0 for every reference: quantifier added in v1.2) (symbolic in m, alpha, both chiralities)',
    ok, 'symbolic', universal=True)
add('C14', 'C', 'Theorem 5.2 (fixed point): det(I-M) = 2 sin^2(2alpha) sin^2(alpha) (1-(1-T^2)cos 2alpha) so the fixed point is unique iff sin 2alpha != 0; kappa_* = -chi m_J (1-cos2alpha)/(1-(1-T^2)cos2alpha), r_x* = -m_J m_K\' sin2alpha/D, r_y* = chi m_J m_K sin2alpha/D',
    det_ok and fp_ok, 'symbolic', universal=True)

# C15 record amplification bound (replaces the seed inequality |kappa_*| <= |m_J|) -- v1.1: NON-strict form + exact equality conditions
cc, TT2 = sp.symbols('c T2', real=True)
gfun = (1 - cc)/(1 - (1 - TT2)*cc)
dg = sp.simplify(sp.diff(gfun, cc))
sup = sp.simplify(gfun.subs(cc, -1))
ok = (sp.simplify(dg + TT2/(1 - (1 - TT2)*cc)**2) == 0 and sp.simplify(sup - 2/(2 - TT2)) == 0
      and sp.simplify(gfun.subs(TT2, 0) - 1) == 0)
mm = sp.symbols('m', positive=True)
ok &= sp.simplify(2*mm/(1 + mm**2) - 1 + (1 - mm)**2/(1 + mm**2)) == 0
# 2/(2-T^2) - g = T^2 (1+c) / ((2-T^2) D)  -> zero iff T=0 or c=-1 (excluded), positive otherwise
gap = sp.simplify(2/(2 - TT2) - gfun - TT2*(1 + cc)/((2 - TT2)*(1 - (1 - TT2)*cc)))
ok &= gap == 0
add('C15', 'C', 'Theorem 5.3 (v1.1 form): g(c,T^2)=(1-c)/(1-(1-T^2)c), dg/dc=-T^2/D^2<=0, g(.,0)=1, sup_c g=2/(2-T^2); 2/(2-T^2)-g = T^2(1+c)/((2-T^2)D) >= 0, so |kappa_*| <= 2|m_J|/(2-T^2) <= 2|m_J|/(1+m_J^2) <= 1 for EVERY reference, with equality in the first bound iff T=0 or m_J=0 (strict iff m_J!=0 and T>0)',
    ok, 'symbolic', universal=True)
# C15b boundary instances where the v1.0 strict inequality was false
kap_of = lambda mj, mk, mkp, a: mj*(1 - sp.cos(2*a))/(1 - (1 - mk**2 - mkp**2)*sp.cos(2*a))
b1 = kap_of(sp.Rational(3, 5), 0, 0, sp.pi/3)            # T=0: |kappa_*| = |m_J| = bound
b2 = kap_of(0, sp.Rational(1, 2), sp.Rational(1, 3), sp.pi/5)   # m_J=0: kappa_*=0=bound
ok = sp.simplify(b1 - sp.Rational(3, 5)) == 0 and sp.simplify(2*sp.Rational(3,5)/(2 - 0) - sp.Rational(3,5)) == 0 and b2 == 0
add('W15b', 'W', 'boundary instances: (T=0, m_J=3/5) gives |kappa_*| = 3/5 = 2|m_J|/(2-T^2) (equality; the v1.0 strict "<" was false here); (m_J=0) gives kappa_* = 0 = bound',
    ok, f'b1={b1}, b2={b2}')

# W16 counter-witness to |kappa_*| <= |m_J| (seed v1.3 inequality)
mJ0, mK0, a0 = sp.Rational(3, 5), sp.Rational(4, 5), 3*sp.pi/8
kap = (mJ0*(1 - sp.cos(2*a0))/(1 - (1 - mK0**2)*sp.cos(2*a0)))
ok = sp.simplify(kap) > mJ0 and mJ0**2 + mK0**2 == 1
add('W16', 'W', 'counter-witness: pure reference (m_K,m_K\',m_J)=(4/5,0,3/5), alpha=3pi/8 gives |kappa_*| = ' + str(sp.N(kap, 12)) + ' > |m_J| = 0.6 — the seed inequality |kappa_*| <= |m_J| is false for coherent references',
    ok, f'kappa_*={sp.nsimplify(sp.simplify(kap))}')

# V17 independent numerical iteration of the channel (numpy expm, no sympy) reproduces the fixed point
from scipy.linalg import expm
sxn = np.array([[0, 1], [1, 0]], complex); syn = np.array([[0, -1j], [1j, 0]]); szn = np.diag([1., -1]).astype(complex); I2n = np.eye(2)
Kn = sxn; Kpn = 1j*szn@Kn
def apply(rho, sgm, a, chir):
    Hn = np.kron(sxn, Kn) + chir*np.kron(syn, Kpn)
    Un = expm(-1j*a*Hn)
    Rn = Un @ np.kron(rho, sgm) @ Un.conj().T
    return Rn.reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)
mKv, mKpv, mJv, av = 0.5, 0.3, 0.4, 0.7
sgm = (I2n + mKv*Kn + mKpv*Kpn + mJv*szn)/2
rho = I2n/2
for _ in range(400): rho = apply(rho, sgm, av, -1)
rnum = np.array([np.trace(rho@X).real for X in (sxn, syn, szn)])
T2v = mKv**2 + mKpv**2; cv, sv = np.cos(2*av), np.sin(2*av); Dv = 1 - (1 - T2v)*cv
rform = np.array([-mJv*mKpv*sv/Dv, -mJv*mKv*sv/Dv, mJv*(1 - cv)/Dv])
err = float(np.max(np.abs(rnum - rform)))
add('V17', 'V', 'numerical iteration of the chi=-1 channel (numpy/scipy, 400 collisions, mixed reference) converges to the closed-form fixed point within 1e-10',
    err < 1e-10 and np.linalg.norm(rform) < 1, f'max|diff|={err:.2e}, |r*|={np.linalg.norm(rform):.6f}')

# W18 faithfulness witness: random Bloch-ball references, |r*| < 1
rng = np.random.default_rng(20260904)
worst = 0.0
for _ in range(20000):
    v = rng.normal(size=3); v /= np.linalg.norm(v); v *= rng.random()**(1/3)
    a_ = rng.random()*np.pi
    if abs(np.sin(2*a_)) < 1e-6: continue
    mk_, mkp_, mj_ = v; t2 = mk_**2 + mkp_**2; c_ = np.cos(2*a_); s_ = np.sin(2*a_); d_ = 1 - (1 - t2)*c_
    worst = max(worst, np.linalg.norm([-mj_*mkp_*s_/d_, -mj_*mk_*s_/d_, mj_*(1 - c_)/d_]))
add('W18', 'W', 'faithfulness witness: 20000 random (reference, alpha) samples give |r*| < 1 (fixed point strictly inside the Bloch ball)', worst < 1, f'max|r*|={worst:.6f}')

# C28 faithfulness identity (v1.1, Theorem 5.7): 1-|r*|^2 = [T^4 + (1-|m|^2)(T^2(1-c^2)+(1-c)^2)]/D^2 -- exact; both terms >= 0
kap_s = -mJ*(1 - sp.cos(2*al))/(1 - (1 - T2)*sp.cos(2*al)); Ds = 1 - (1 - T2)*sp.cos(2*al)
rxs = -mJ*mKp*sp.sin(2*al)/Ds; rys = mJ*mK*sp.sin(2*al)/Ds
r2s = rxs**2 + rys**2 + kap_s**2
ident = sp.simplify(1 - r2s - (T2**2 + (1 - T2 - mJ**2)*(T2*(1 - sp.cos(2*al)**2) + (1 - sp.cos(2*al))**2))/Ds**2)
add('C28', 'C', 'Theorem 5.7 (faithfulness identity): 1-|r*|^2 = [T^4 + (1-T^2-m_J^2)(T^2 sin^2 2alpha + (1-cos 2alpha)^2)]/D^2 exactly; hence |r*|<1 (faithful fixed point) iff NOT (T=0 and |m_J|=1), and 1-|r*|^2 >= T^4/D^2',
    ident == 0, 'symbolic in m, alpha', universal=True)
# W29 non-faithful boundary: pure diagonal reference (T=0, |m_J|=1) -> fixed point pure
r_pure = [sp.simplify(e.subs({mK: 0, mKp: 0, mJ: 1})) for e in (rxs, rys, kap_s)]
add('W29', 'W', 'non-faithful instance: the pure diagonal reference (T=0, m_J=1) has fixed point r*=(0,0,-1) (|r*|=1): the v1.0 abstract phrase "unique faithful" needed the exclusion of this case',
    r_pure == [0, 0, -1], f'r*={r_pure}')

# C19 record persistence corollary (comparison row: uses locked T_2) -- v1.2: EXACT rational comparison.
#     x(rho) in (2/7, 2/3)  <=>  28/53 < rho < 12/13   (2m/(1+m^2) at m = 2/7, 2/3 is 28/53, 12/13; the map is increasing on [0,1]);
#     the locked decimal T_2 is read as the exact rational 835381287313630/10^15. mpmath is used only to print x(T_2).
T2_lock_q = sp.Rational(835381287313630, 10**15)
mm_ = sp.symbols('m_', nonnegative=True)
f2 = 2*mm_/(1 + mm_**2)
ok = (sp.simplify(f2.subs(mm_, sp.Rational(2, 7)) - sp.Rational(28, 53)) == 0 and sp.simplify(f2.subs(mm_, sp.Rational(2, 3)) - sp.Rational(12, 13)) == 0
      and sp.simplify(sp.diff(f2, mm_) - 2*(1 - mm_**2)/(1 + mm_**2)**2) == 0      # increasing on [0,1]
      and bool(sp.Rational(28, 53) < T2_lock_q) and bool(T2_lock_q < sp.Rational(12, 13))
      and S(1/sp.cosh(eta) - sp.Rational(2, 3)) == 0 and S(1/sp.cosh(2*eta) - sp.Rational(2, 7)) == 0)
mp.mp.dps = 30
T2_lock = mp.mpf('0.835381287313630')
xrho = (1 - mp.sqrt(1 - T2_lock**2))/T2_lock
add('C19', 'C', 'Corollary 5.4 / comparison (EXACT): |kappa_*|>=rho needs |m_J| >= x(rho)=(1-sqrt(1-rho^2))/rho; x(rho) in (2/7,2/3) iff 28/53 < rho < 12/13, and the locked decimal T_2 read as an exact rational satisfies both strict inequalities: a fixed-point capacity of magnitude T_2 survives at most two consecutive passive returns, never three (x(T_2)=' + mp.nstr(xrho, 12) + ')',
    ok, f'T_2 = {T2_lock_q} exactly; 28/53 = {float(sp.Rational(28,53)):.6f}, 12/13 = {float(sp.Rational(12,13)):.6f}; x(T_2)={mp.nstr(xrho,20)}', comparison=True)

# C20 K10 corrected (comparison row: uses locked M_*) -- v1.2: EXACT rational comparison.
#     sqrt(1-M^2) < rho  <=>  1-M^2 < rho^2 ;  rho < 2 sqrt(1-M^2)/(2-M^2)  <=>  rho^2 (2-M^2)^2 < 4(1-M^2)   (all quantities positive)
Mstar_q = sp.Rational(763362818245963536, 10**18)
lhs1 = 1 - Mstar_q**2; rhs1 = T2_lock_q**2
lhs2 = T2_lock_q**2*(2 - Mstar_q**2)**2; rhs2 = 4*(1 - Mstar_q**2)
ok = bool(lhs1 < rhs1) and bool(lhs2 < rhs2)
Mstar = mp.mpf('0.763362818245963536')
bound_old = mp.sqrt(1 - Mstar**2); bound_new = 2*bound_old/(2 - Mstar**2)
add('C20', 'C', 'Corollary 7.1 (K10 re-quantified, EXACT; SOLDERED RESOURCE-AXIS CLASS w = +-e_J with the original J grading fixed, so that the transducer coherence T_w equals the M60 odd coherence T -- outside that class the bound is FALSE, see W69; audit v1.4 F1): with T>=M_* on a rank-two reference, |kappa_*| <= 2 sqrt(1-M_*^2)/(2-M_*^2) = ' + mp.nstr(bound_new, 6) + ' which does NOT exclude T_2 (rho^2 (2-M^2)^2 < 4(1-M^2) holds exactly for the locked decimals); the seed bound sqrt(1-M_*^2)=' + mp.nstr(bound_old, 6) + ' < T_2 (1-M^2 < rho^2, exact) relied on |kappa_*|<=|m_J| and is withdrawn',
    ok, f'exact: 1-M^2={lhs1} < T_2^2={rhs1}; T_2^2(2-M^2)^2={lhs2} < 4(1-M^2)={rhs2}; old={mp.nstr(bound_old,20)}, new={mp.nstr(bound_new,20)}', comparison=True)

# ---------------------------------------------------------------- chiral-bag antiunitary lemma
g0 = sp.diag(1, 1, -1, -1)
def gk(sk): return sp.Matrix(sp.BlockMatrix([[sp.zeros(2, 2), sk], [-sk, sp.zeros(2, 2)]]))
g1, g2, g3 = gk(sx), gk(sy), gk(sz)
g5 = sp.simplify(sp.I*g0*g1*g2*g3)
I4 = sp.eye(4)
Sig3 = sp.simplify(sp.I*g1*g2)
q, kk, m, thm, mu, th, p = sp.symbols('q k m theta_m mu theta p', real=True)
k1, k2 = kk*sp.cos(q), kk*sp.sin(q)
def Hk(p_):   # p_ stands for the real operator -i d/dx3 (imaginary-odd under K: p -> -p)
    return g0*(g1*k1 + g2*k2 + g3*p_) + m*g0*(sp.cos(thm)*I4 + sp.I*sp.sin(thm)*g5) + mu*I4
phik = 2*q - sp.pi
R = sp.cos(phik/2)*I4 - sp.I*sp.sin(phik/2)*Sig3
Sl = g0*R                                        # S = g0 R K  (K = complex conjugation)
def S_conj(X, p_odd=False):
    Xc = X.conjugate()
    if p_odd: Xc = Xc.subs(p, -p)
    return Sl * Xc * Sl.inv()
Bth = sp.cos(th)*(sp.I*g3) + sp.sin(th)*(g3*g5)
isreal = lambda X: sp.simplify(X - X.conjugate()) == sp.zeros(4, 4)
ok_rep = (isreal(g0) and isreal(g1) and isreal(g3) and isreal(g5) and sp.simplify(g2 + g2.conjugate()) == sp.zeros(4, 4)
          and sp.simplify(g5*g5 - I4) == sp.zeros(4, 4))
ok_H = Z(S_conj(Hk(p), p_odd=True) - Hk(p)) == sp.zeros(4, 4)
ok_B = Z(S_conj(Bth) - Bth) == sp.zeros(4, 4)
ok_g5 = Z(S_conj(g5) + g5) == sp.zeros(4, 4)
ok_S2 = Z(Sl*Sl.conjugate() - I4) == sp.zeros(4, 4)
add('C21', 'C', 'Lemma 8.1: in the representation (g0,g1,g3,g5 real; g2 imaginary), S_k = g0 exp(-i phi_k Sigma^3/2) K with phi_k=2q-pi satisfies S H_k S^-1 = H_k (real m(x3), mu(x3), any theta_m, any k), S B_theta S^-1 = B_theta (every theta), S g5 S^-1 = -g5, S^2 = +1',
    ok_rep and ok_H and ok_B and ok_g5 and ok_S2, f'rep={ok_rep} H={ok_H} B={ok_B} g5={ok_g5} S2={ok_S2}', universal=True)

# C22 pointwise density flips sign under S; k_perp = 0: every phi works
ph = sp.Matrix(sp.symbols('u1:5'))
dens = lambda v: sp.expand((v.H*g5*v)[0])
flip = Z(dens(Sl*ph.conjugate()) + dens(ph)) == 0
phg = sp.symbols('phi_g', real=True)
Rg = sp.cos(phg/2)*I4 - sp.I*sp.sin(phg/2)*Sig3
Sg = g0*Rg
Hk0 = Hk(p).subs(kk, 0)
ok_k0 = Z(Sg*Hk0.conjugate().subs(p, -p)*Sg.inv() - Hk0) == sp.zeros(4, 4)
add('C22', 'C', 'Lemma 8.1 (density): (S phi)^dag g5 (S phi) = -phi^dag g5 phi pointwise for every spinor; at k_perp=0 every rotation angle phi gives a symmetry',
    flip and ok_k0, 'symbolic', universal=True)

# C23 breakers: normal vector potential term is S-odd; tangential constant A_perp is absorbed by phi(k-A); e^{i a g5} rotates B_theta (Cor 38.7)
A3 = sp.symbols('A3', real=True)
odd = Z(S_conj(g0*g3*A3) + g0*g3*A3) == sp.zeros(4, 4)
aa = sp.symbols('a', real=True)
Ea = sp.cos(aa)*I4 + sp.I*sp.sin(aa)*g5
rot = Z(Ea*Bth*Ea.inv() - Bth.subs(th, th + 2*aa)) == sp.zeros(4, 4)
add('C23', 'C', 'Scope: the normal term A_3 g0 g3 is S-odd (breaker (b)); e^{i a g5} B_theta e^{-i a g5} = B_{theta+2a}, so a local axial rotation preserves the bag domain iff a|_{x3=0} in pi Z (Proposition 8.2)',
    odd and rot, 'symbolic', universal=True)

# W24 Wilson-lattice witness of level-wise vanishing (finite, specific parameters)
def lattice_witness(Nsite=40, a_lat=1.0, kperp=(0.3, 0.4), thm_v=0.4, th_v=0.9, seed=1):
    g0n = np.diag([1, 1, -1, -1]).astype(complex)
    def gkn(sk): return np.block([[np.zeros((2, 2)), sk], [-sk, np.zeros((2, 2))]]).astype(complex)
    g1n, g2n, g3n = gkn(sxn), gkn(syn), gkn(szn)
    g5n = 1j*g0n@g1n@g2n@g3n
    I4n = np.eye(4)
    rng_ = np.random.default_rng(seed)
    mprof = 1.0 + 0.3*rng_.random(Nsite)          # x-dependent real mass
    muprof = 0.2*rng_.random(Nsite)               # x-dependent real scalar potential
    H = np.zeros((4*Nsite, 4*Nsite), complex)
    for x_ in range(Nsite):
        blk = slice(4*x_, 4*x_+4)
        H[blk, blk] += (g0n@(g1n*kperp[0] + g2n*kperp[1]) + mprof[x_]*g0n@(np.cos(thm_v)*I4n + 1j*np.sin(thm_v)*g5n)
                        + muprof[x_]*I4n + g0n/a_lat)     # Wilson diagonal r=1
        if x_+1 < Nsite:
            nb = slice(4*x_+4, 4*x_+8)
            hop = (-1j*g0n@g3n)/(2*a_lat) - g0n/(2*a_lat)     # -i g0 g3 (psi_{x+1}-psi_{x-1})/2a + Wilson
            H[blk, nb] += hop; H[nb, blk] += hop.conj().T
    Bn = np.cos(th_v)*(1j*g3n) + np.sin(th_v)*(g3n@g5n)
    Pn = (I4n + Bn)/2
    Q = np.eye(4*Nsite, dtype=complex); Q[0:4, 0:4] = Pn        # bag projector at site 0
    Hb = Q@H@Q
    # antiunitary S on the lattice
    qv = np.arctan2(kperp[1], kperp[0]); phv = 2*qv - np.pi
    Sig3n = 1j*g1n@g2n
    Rn = np.cos(phv/2)*I4n - 1j*np.sin(phv/2)*Sig3n
    Sn = np.kron(np.eye(Nsite), g0n@Rn)
    sym = np.max(np.abs(Sn@Hb.conj()@np.linalg.inv(Sn) - Hb))
    E, Vv = np.linalg.eigh(Hb)
    # restrict to bag-admissible subspace: drop the null vectors created by Q at site 0 (they are exact zero modes of Q H Q)
    keep = [i for i in range(len(E)) if np.linalg.norm(Vv[:, i] - Q@Vv[:, i]) < 1e-9]
    E = E[keep]; Vv = Vv[:, keep]
    dens_max = 0.0; ndeg = 0
    for i in range(len(E)):
        # non-degenerate levels only
        if (i > 0 and abs(E[i]-E[i-1]) < 1e-8) or (i+1 < len(E) and abs(E[i+1]-E[i]) < 1e-8):
            ndeg += 1; continue
        v = Vv[:, i].reshape(Nsite, 4)
        d = np.einsum('xi,ij,xj->x', v.conj(), g5n, v).real
        dens_max = max(dens_max, np.max(np.abs(d)))
    # control: polarisation-mixing Hermitian perturbation (i g1 g3 type) breaks it
    Hc = Hb.copy(); Hc[4:8, 4:8] += 0.05*(1j*g1n@g3n)
    Ec, Vc = np.linalg.eigh(Hc)
    keepc = [i for i in range(len(Ec)) if np.linalg.norm(Vc[:, i] - Q@Vc[:, i]) < 1e-9]
    vc = Vc[:, keepc[len(keepc)//2]].reshape(Nsite, 4)
    dc = np.max(np.abs(np.einsum('xi,ij,xj->x', vc.conj(), g5n, vc).real))
    return sym, dens_max, ndeg, dc, len(E)
sym, dmax, ndeg, dctrl, nlev = lattice_witness()
add('W24', 'W', 'Wilson-lattice witness (40 sites, x-dependent real m and mu, bag angle 0.9, k_perp=(0.3,0.4)): S H S^-1 = H to machine precision and every non-degenerate level has pointwise |phi^dag g5 phi| < 1e-10; a polarisation-mixing control perturbation raises it above 1e-3',
    sym < 1e-12 and dmax < 1e-10 and dctrl > 1e-3, f'sym_resid={sym:.1e}, max_dens={dmax:.1e}, degenerate_levels_skipped={ndeg}, levels={nlev}, control_dens={dctrl:.2e}')

# ================================================================ v1.1 rows (audit response + deep exploration)
# C30 instrument completion of A3 (Theorem 4.6): E0 = e^{-eta} A, E1 = sqrt(I - E0^2) = sqrt(1-phi^-8) P_-, success probability,
#     failure branch = negative null state (no record), non-selective channel = K-dephasing with factor e^{-2eta} = phi^-4, m_K invariant
E0 = S(A/sp.exp(eta)); Pm = (I2 - K)/2; E1 = sp.sqrt(1 - phi**-8)*Pm
psucc = S(sp.trace(E0*sig*E0))
Lam = S(E0*sig*E0 + E1*sig*E1)
ok = (S(I2 - E0*E0 - E1*E1) == sp.zeros(2, 2)
      and S(psucc - sp.exp(-2*eta)*(sp.cosh(2*eta) + mK*sp.sinh(2*eta))) == 0
      and S(sp.trace(E1*sig*E1*J)) == 0 and S(sp.trace(E1*sig*E1*K) + sp.trace(E1*sig*E1)) == 0
      and S(sp.trace(Lam) - 1) == 0 and S(sp.trace(Lam*K) - mK) == 0
      and S(sp.trace(Lam*Kp) - phi**-4*mKp) == 0 and S(sp.trace(Lam*J) - phi**-4*mJ) == 0
      and S(sp.exp(-2*eta) - phi**-4) == 0)
add('C30', 'C', 'Theorem 4.6 (instrument completion): {E0=e^{-eta}A, E1=sqrt(1-phi^-8)P_-} is a two-outcome instrument (E0^2+E1^2=I); p_succ(sigma)=e^{-2eta}(cosh2eta + m_K sinh2eta); the failure branch is the negative null state (m_J=0, m_K=-1); the non-selective channel Lambda is K-dephasing: m_K invariant, (m_K\',m_J) -> phi^-4 (m_K\',m_J), phi^-4 = e^{-2eta}',
    ok, f'phi^-4={sp.N(phi**-4, 15)}', universal=True)

# C31 trade-off identity (Theorem 4.7): (prod_k p_succ,k) x (m_J(n)/m_J(0)) = e^{-2 n eta}; cumulative survival -> (1+m_K(0))/2
nn, z0 = sp.symbols('n zeta0', real=True)
prod = sp.exp(-2*nn*eta)*sp.cosh(z0 + 2*nn*eta)/sp.cosh(z0); ret = sp.cosh(z0)/sp.cosh(z0 + 2*nn*eta)
lim = sp.simplify(sp.limit(prod, nn, sp.oo).subs(sp.exp(2*z0), (1 + mK)/(1 - mK)))   # e^{2 zeta0} = (1+m_K)/(1-m_K)
ok = sp.simplify(prod*ret - sp.exp(-2*nn*eta)) == 0 and sp.simplify(lim - (1 + mK)/2) == 0
# unnormalised S_J is invariant (Theorem 4.3) -- the identity is its instrument reading
ok &= S(sp.trace(A*sig*A*J) - mJ) == 0
add('C31', 'C', 'Theorem 4.7 (success-probability x transverse-reference-retention identity): (prod p_k) x (m_J(n)/m_J(0)) = e^{-2 n eta} exactly for every reference with m_J(0) != 0 (the row checks the reference rapidity identity prod p = e^{-2n eta} cosh(zeta0+2n eta)/cosh zeta0 and retention cosh zeta0/cosh(zeta0+2n eta)); cumulative survival -> (1+m_K(0))/2; the un-normalised S_J is return-invariant (an algebraic identity of the filter, not an instrument-level conservation law)',
    ok, 'symbolic in zeta0, n, m_K', universal=True)

# C32 general-strength instrument (Remark 4.6.2(a)): E0 = A/lambda, lambda >= ||A|| = e^eta, dephasing factor
#     f(lambda) = lambda^-2 + sqrt((1-e^{2eta}/lambda^2)(1-e^{-2eta}/lambda^2)), f(e^eta) = phi^-4, f -> 1, f strictly increasing.
#     v1.3: FULLY EXACT (audit F4 of v1.2: the v1.2 row fell back to three numerical samples). Route: with t = lambda^-2, a = e^{2eta}, b = e^{-2eta}
#     one has ab = 1, a+b = 7 exactly, so the radicand (1 - a t)(1 - b t) IS the polynomial 1 - 7t + t^2 (exact identity), and both
#     parametrisations are the same principal square root; monotonicity: df/dt < 0 iff 2 sqrt(1-7t+t^2) < 7-2t (positive on (0, phi^-4])
#     iff 4(1-7t+t^2) < (7-2t)^2 iff 0 < 45.  No numerical comparison enters the PASS decision.
lam = sp.symbols('lambda', positive=True)
tt = sp.symbols('t', positive=True)
a_ = (7 + 3*sp.sqrt(5))/2; b_ = (7 - 3*sp.sqrt(5))/2                  # e^{2eta}, e^{-2eta} in exact radical form
ok = S(a_ - sp.exp(2*eta)) == 0 and S(b_ - sp.exp(-2*eta)) == 0        # the radical forms ARE e^{±2eta}
ok &= sp.simplify(a_*b_ - 1) == 0 and sp.simplify(a_ + b_ - 7) == 0      # ab = 1, a + b = 7
ok &= sp.simplify(sp.expand((1 - a_*tt)*(1 - b_*tt)) - (1 - 7*tt + tt**2)) == 0     # radicand identity (exact)
ft = tt + sp.sqrt(1 - 7*tt + tt**2)                                        # f in the t parametrisation (principal root; radicand >= 0 on (0, phi^-4])
f_lam = 1/lam**2 + sp.sqrt((1 - a_/lam**2)*(1 - b_/lam**2))               # f in the lambda parametrisation with exact a, b
ok &= sp.simplify(sp.expand((1 - a_/lam**2)*(1 - b_/lam**2)) - (1 - 7/lam**2 + 1/lam**4)) == 0   # same radicand, hence same principal root
f_lam_exp = 1/lam**2 + sp.sqrt(sp.expand((1 - a_/lam**2)*(1 - b_/lam**2)))            # f(lambda) with its radicand expanded exactly
ok &= sp.simplify(ft.subs(tt, 1/lam**2) - f_lam_exp) == 0                              # the t-form IS the lambda-form (exact, ties the code object ft to f)
ok &= sp.simplify(sp.diff(ft, tt) - (1 + (2*tt - 7)/(2*sp.sqrt(1 - 7*tt + tt**2)))) == 0   # derivative of the actual ft: sign decided by 2 sqrt(...) vs 7 - 2t
ok &= S(ft.subs(tt, phi**-4) - phi**-4) == 0                              # f at lambda = ||A|| (t = phi^-4) equals phi^-4
ok &= sp.limit(ft, tt, 0) == 1                                             # lambda -> oo
ok &= sp.simplify((7 - 2*tt)**2 - 4*(1 - 7*tt + tt**2) - 45) == 0        # discriminant identity
ok &= bool(7 - 2*phi**-4 > 0)                                              # 7 - 2t > 0 on the range (t <= phi^-4 < 1)
ok &= S(1 - 7*phi**-4 + phi**-8) == 0                                        # radicand is EXACTLY 0 at the endpoint t = phi^-4 = b (1 - (a+b)b + b^2 = 1 - ab = 0); v1.4: the v1.3 numerical `or` on this conjunct removed (audit F7)
add('C32', 'C', 'Remark 4.6.2(a) (instrument strength freedom, EXACT; every conjunct exact -- the v1.3 endpoint conjunct still carried a numerical `or` although its exact branch decided it, removed in v1.4, audit F7): with t=lambda^-2, a=e^{2eta}=(7+3sqrt5)/2, b=e^{-2eta}=(7-3sqrt5)/2: ab=1, a+b=7, so the radicand (1-a t)(1-b t) is exactly 1-7t+t^2 and f(lambda)=lambda^-2+sqrt((1-a/lambda^2)(1-b/lambda^2)) equals t+sqrt(1-7t+t^2) as principal roots; f(e^eta)=phi^-4 (minimal), f->1 as lambda->oo; f is STRICTLY INCREASING in lambda since (7-2t)^2-4(1-7t+t^2)=45>0 with 7-2t>0 on (0,phi^-4]',
    ok, 'symbolic; e^2eta+e^-2eta=7; discriminant gap 45', universal=True)

# C33 involutive holonomy cycle (Theorem 6.4): C = Ad_J o H, C^2 = id on all states (exact, un-normalised), fixed family m=(-tanh eta, 0, m_J), |m_J| <= sech eta = 2/3;
#     m_J has period 2 for every reference; p_succ on the fixed family = e^{-2eta}
sgen = sp.Matrix(2, 2, sp.symbols('s11 s12 s21 s22'))
Cyc = lambda X: J*A*X*A*J
ok = S(Cyc(Cyc(sgen)) - sgen) == sp.zeros(2, 2)
Cs = S(Cyc(sig)); trc = S(sp.trace(Cs))
sols = sp.solve([S(sp.trace(Cs*X)/trc - sp.trace(sig*X)) for X in (K, Kp, J)], [mK, mKp], dict=True)
ok &= len(sols) == 1 and S(sols[0][mK] + sp.tanh(eta)) == 0 and sols[0][mKp] == 0 and S(sp.tanh(eta) - sp.sqrt(5)/3) == 0
sig1 = S(Cs/trc); Cs2 = S(Cyc(sig1)); sig2 = S(Cs2/sp.trace(Cs2))
ok &= S(sp.trace(sig2*J) - mJ) == 0
ok &= S(psucc.subs(mK, -sp.tanh(eta)) - sp.exp(-2*eta)) == 0
# the pure endpoints |m_J| = sech(eta) = 2/3 of the fixed family are the N=2 extremal orbit of Theorem 4.5 (Bloch constraint)
ok &= S(sp.sqrt(1 - sp.tanh(eta)**2) - sp.Rational(2, 3)) == 0
add('C33', 'C', 'Theorem 6.4 (involutive cycle): C=Ad_J o H satisfies C^2=id exactly (JAJ=A^{-1}); fixed family m=(-tanh eta, 0, m_J)=(-sqrt5/3, 0, m_J), |m_J|<=2/3=sech eta (the rapidity -eta family; ONLY its pure endpoints |m_J|=2/3 are the N=2 extremal orbit of Thm 4.5); m_J returns after two cycles for EVERY reference; success probability on the fixed family = e^{-2eta} = phi^-4 per cycle',
    ok, 'symbolic', universal=True)

# C34 no-unital-refresh (Theorem 6.5), executable half: |Lambda r|^2 = m_K^2 + phi^-8 (m_K'^2+m_J^2) < |r|^2 unless m_K'=m_J=0 (the other half, HS-contractivity of unital maps, is Kadison-Schwarz: written proof)
f8_exact = (47 - 21*sp.sqrt(5))/2                                  # phi^-8 in exact radical form (v1.4.1, audit F2: replaces sp.N(phi**-8) < 1)
ok = S(sp.trace(Lam*K)**2 + sp.trace(Lam*Kp)**2 + sp.trace(Lam*J)**2 - (mK**2 + phi**-8*(mKp**2 + mJ**2))) == 0
ok &= S(phi**-8 - f8_exact) == 0
ok &= bool(sp.Integer(47)**2 > sp.Integer(21)**2*5) and bool(sp.Integer(21)**2*5 > sp.Integer(45)**2)   # 47 > 21 sqrt5 > 45, all positive => 0 < phi^-8 < 1 exactly
add('C34', 'C', 'Theorem 6.5, executable half: |Lambda(r)|^2 = m_K^2 + phi^-8 (m_K\'^2 + m_J^2) exactly, with 0 < phi^-8 < 1 certified exactly (phi^-8 = (47-21sqrt5)/2 and 47^2 > 21^2*5 > 45^2; v1.4.1 replaces the v1.4 numerical conjunct sp.N(phi^-8) < 1, audit F2), so strictly < |r|^2 unless m_K\'=m_J=0; combined with HS-contractivity of unital maps (written proof, Kadison-Schwarz) every fixed point of R o Lambda or Lambda o R with R unital has m_J = m_K\' = 0',
    ok, f'phi^-8={sp.N(phi**-8, 12)}', universal=True)
# W35 witness for Theorem 6.5 (RETYPED in v1.2; the v1.1 version found 0 fixed vectors among 3000 random rotations, a vacuous transverse test):
#     (a) lemma: for a rotation R, M = R.diag(1,q,q) with 0<q<1 has a fixed vector iff R e_K = e_K (then the fixed vector is e_K, transverse part 0):
#         |v| = |M v| = |diag(1,q,q) v| <= |v| with equality iff v || e_K.   (b) targeted family: 300 rotations ABOUT e_K -> fixed vector e_K found each time,
#     transverse part 0;  (c) 3000 random rotations: no eigenvalue 1 unless R e_K = e_K (consistent with (a));  (d) spec(Ad_J o Lambda) = {-1, -phi^-4, phi^-4}.
q = float(sp.N(phi**-4)); rngu = np.random.default_rng(20260905)
found_about_K = 0; worst_t = 0.0
for _ in range(300):
    th_ = rngu.uniform(0, 2*np.pi); Rk = np.array([[1, 0, 0], [0, np.cos(th_), -np.sin(th_)], [0, np.sin(th_), np.cos(th_)]])
    Mm = Rk @ np.diag([1., q, q]); w_, v_ = np.linalg.eig(Mm)
    for i in range(3):
        if abs(w_[i] - 1) < 1e-9:
            vec = np.real(v_[:, i]); vec /= np.linalg.norm(vec); worst_t = max(worst_t, abs(vec[1]), abs(vec[2])); found_about_K += 1
consistent = True; cnt_rand = 0
for _ in range(3000):
    Qm, _r = np.linalg.qr(rngu.normal(size=(3, 3)))
    if np.linalg.det(Qm) < 0: Qm[:, 0] *= -1
    Mm = Qm @ np.diag([1., q, q]); w_ = np.linalg.eigvals(Mm)
    has_fixed = bool(np.any(np.abs(w_ - 1) < 1e-9)); fixes_eK = bool(np.linalg.norm(Qm @ np.array([1., 0, 0]) - np.array([1., 0, 0])) < 1e-9)
    consistent &= (has_fixed == fixes_eK); cnt_rand += has_fixed
JR = np.diag([-1., -1., 1.]); MJ = JR @ np.diag([1., q, q]); wJ = np.linalg.eigvals(MJ)
add('W35', 'W', 'witness for Theorem 6.5 (retyped v1.2): 300 rotations about e_K each give R.diag(1,phi^-4,phi^-4) the fixed vector e_K with zero (m_K\',m_J) part; over 3000 random rotations an eigenvalue 1 occurs iff R e_K = e_K (lemma: |Mv|=|v| forces v || e_K) -- the v1.1 "no transverse fixed vector among random rotations" was vacuous (0 fixed vectors) and is now stated as consistency with this lemma; the audit cycle Ad_J o Lambda has spectrum {-1, -phi^-4, phi^-4}: no fixed point except r=0',
    found_about_K == 300 and worst_t < 1e-12 and consistent and np.allclose(sorted(wJ.real), sorted([-1, -q, q])),
    f'fixed vectors found (rotations about e_K)={found_about_K}, max transverse={worst_t:.1e}; random rotations with a fixed vector={cnt_rand} (all had R e_K=e_K: {consistent}); spec(Ad_J Lambda)={np.round(wJ.real,6)}')

# C36 coupling-class covariance (Theorem 5.8): H_R = X⊗(u.s) + chi Y⊗(v.s) with (u,v,w) = R(e_K,e_K',e_J) records m_w = m.w with the SAME law:
#     kappa_* = -chi m_w (1-c)/(1-(1-T_w^2)c), T_w^2 = |m|^2 - m_w^2; checked symbolically for a one-parameter tilt u = cos b e_K + sin b e_J, v = e_K'
bt = sp.symbols('beta', real=True)
u_op = sp.cos(bt)*K + sp.sin(bt)*J; v_op = Kp
def chan_fixed(u_op, v_op, chir):
    Ht = sp.kronecker_product(sx, u_op) + chir*sp.kronecker_product(sy, v_op)
    H2 = sp.simplify(Ht*Ht)
    assert sp.simplify(Ht*H2 - 4*Ht) == sp.zeros(4, 4)      # spec H in {0, +-2}: closed-form exponential
    Ut = sp.eye(4) + (sp.cos(2*al) - 1)*H2/4 - sp.I*sp.sin(2*al)*Ht/2
    rxv, ryv, rzv = sp.symbols('r_x r_y r_z', real=True)
    rho2 = (I2 + rxv*sx + ryv*sy + rzv*sz)/2
    o = Ut*sp.kronecker_product(rho2, sig)*Ut.H
    red = sp.zeros(2, 2)
    for i in range(2):
        for j in range(2):
            red[i, j] = sum(o[2*i+k, 2*j+k] for k in range(2))
    comps = [sp.expand(sp.trace(red*X)) for X in (sx, sy, sz)]
    Mt = sp.Matrix([[sp.diff(cc_, v) for v in (rxv, ryv, rzv)] for cc_ in comps])
    bt_ = sp.Matrix([cc_.subs({rxv: 0, ryv: 0, rzv: 0}) for cc_ in comps])
    return Mt, bt_
Mt, bt_ = chan_fixed(u_op, v_op, -1)
mw = -sp.sin(bt)*mK + sp.cos(bt)*mJ                       # w = u x v = (-sin b, 0, cos b) in (K,K',J) coordinates
Tw2 = mK**2 + mKp**2 + mJ**2 - mw**2
Dt = 1 - (1 - Tw2)*sp.cos(2*al)
# predicted fixed point = chiral fixed point of Thm 5.2 with the reference read in the rotated frame (m.u, m.v, m.w); carrier untouched
mu_ = sp.cos(bt)*mK + sp.sin(bt)*mJ; mv_ = mKp; chir_ = -1
pred_vec = sp.Matrix([-mw*mv_*sp.sin(2*al)/Dt, chir_*mw*mu_*sp.sin(2*al)/Dt, -chir_*mw*(1 - sp.cos(2*al))/Dt])
resid = (Mt*pred_vec + bt_ - pred_vec).applyfunc(lambda e: sp.simplify(sp.expand(sp.expand_trig(e*Dt))))
sa_, ca_, sb_, cb_ = sp.symbols('sa ca sb cb', real=True)
def trig_reduce(e):   # polynomial identity test modulo sin^2+cos^2=1: exact polynomial remainders in cos(alpha), cos(beta)
    e = sp.expand(sp.expand_trig(e)).subs({sp.sin(al): sa_, sp.cos(al): ca_, sp.sin(bt): sb_, sp.cos(bt): cb_})
    e = sp.rem(sp.expand(e), ca_**2 + sa_**2 - 1, ca_)
    e = sp.rem(sp.expand(e), cb_**2 + sb_**2 - 1, cb_)
    return sp.expand(e)
detIM = sp.det(sp.eye(3) - Mt)
det_pred = 2*sp.sin(2*al)**2*sp.sin(al)**2*Dt
ok = resid == sp.zeros(3, 1) and trig_reduce(detIM - det_pred) == 0
pred = mw*(1 - sp.cos(2*al))/Dt
add('C36', 'C', 'Theorem 5.8 (coupling-class covariance): for the tilted coupling X⊗(cos b K + sin b J) + chi Y⊗K\' det(I-M) = 2 sin^2 2alpha sin^2 alpha (1-(1-T_w^2)cos2alpha) (unique fixed point iff sin2alpha != 0) and the chiral fixed point read in the rotated frame (m.u, m.v, m.w) solves (I-M)r = b exactly: kappa_* = -chi m_w (1-cos2alpha)/(1-(1-T_w^2)cos2alpha), m_w = m.w, w = u x v = (-sin b, 0, cos b), T_w^2 = |m|^2 - m_w^2 (symbolic in b, m, alpha)',
    ok, 'symbolic; chi=-1 (chi=+1 follows by the same covariance)', universal=True)

# C37 light-cone attractor record (Theorem 5.9): under passive return m(n) -> e_K (Thm 4.1, m_K(0) > -1); the tilted record converges to
#     kappa_inf = -chi w_K (1-c)/(1-(1-w_K^2)c) with faithfulness margin (1-w_K^2)^2/D_inf^2; biased iff w_K != 0, faithful iff |w_K| < 1;
#     for the soldered chiral coupling w = e_J (w_K = 0) the limit record is 0 (Thm 4.4)
wK = sp.symbols('w_K', real=True)
kinf = pred.subs({mK: 1, mKp: 0, mJ: 0}).subs(sp.sin(bt), -wK).subs(sp.cos(bt)**2, 1 - wK**2)
kinf_pred = wK*(1 - sp.cos(2*al))/(1 - (1 - (1 - wK**2))*sp.cos(2*al))
ok = sp.simplify(kinf - kinf_pred) == 0
# faithfulness margin at the null state from the C28 identity with T^2 -> 1 - w_K^2, m_J -> w_K (|m|=1)
marg = ((1 - wK**2)**2 + (1 - (1 - wK**2) - wK**2)*0)/(1 - wK**2*sp.cos(2*al))**2
ok &= sp.simplify(marg - (1 - wK**2)**2/(1 - wK**2*sp.cos(2*al))**2) == 0
# exact limits of the orbit (Theorem 4.1): m_K -> 1, transverse -> 0 for zeta0 finite
ok &= sp.limit(sp.tanh(z0 + 2*nn*eta), nn, sp.oo) == 1 and sp.limit(sp.cosh(z0)/sp.cosh(z0 + 2*nn*eta), nn, sp.oo) == 0
# under the NON-selective instrument the K-population is conserved (C30): the tilted record converges to -chi w_K m_K(0) (1-c)/(1-(1-w_K^2 m_K(0)^2)c)
kns = pred.subs({mKp: 0, mJ: 0}).subs(sp.sin(bt), -wK).subs(sp.cos(bt)**2, 1 - wK**2)
kns_pred = wK*mK*(1 - sp.cos(2*al))/(1 - (1 - mK**2*(1 - wK**2))*sp.cos(2*al))   # T_w^2 = m_K(0)^2 (1 - w_K^2)
ok &= sp.simplify(kns - kns_pred) == 0
add('C37', 'C', 'Theorem 5.9 (light-cone attractor record): conditional reading m(n)->e_K gives kappa_inf = -chi w_K (1-cos2alpha)/(1-w_K^2 cos2alpha), faithfulness margin (1-w_K^2)^2/(1-w_K^2 cos2alpha)^2 (biased iff w_K!=0, faithful iff |w_K|<1); non-selective reading (m_K conserved, transverse -> 0) gives kappa -> -chi w_K m_K(0)(1-cos2alpha)/(1-(1-m_K(0)^2(1-w_K^2))cos2alpha); for the soldered chiral coupling w_K=0 and both limits vanish',
    ok, 'symbolic in w_K, alpha; orbit limits symbolic in zeta0', universal=True)
# V38 independent numeric confirmation of C36/C37: numpy/scipy iteration of the tilted channel at a random reference and at the null state
sxn_ = np.array([[0, 1], [1, 0]], complex); syn_ = np.array([[0, -1j], [1j, 0]]); szn_ = np.diag([1., -1]).astype(complex); I2n_ = np.eye(2)
Kn_ = sxn_; Kpn_ = 1j*szn_@Kn_; Jn_ = szn_
def fp_num(Hm, sgm_, a_):
    Um = expm(-1j*a_*Hm); rh = I2n_/2
    for _ in range(700):
        Rm = Um @ np.kron(rh, sgm_) @ Um.conj().T; rh = Rm.reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)
    return np.array([np.trace(rh@X).real for X in (sxn_, syn_, szn_)])
b_, a_, chir_ = 0.6, 1.2, -1
u_n = np.cos(b_)*Kn_ + np.sin(b_)*Jn_; Hn_ = np.kron(sxn_, u_n) + chir_*np.kron(syn_, Kpn_)
m_ = np.array([0.3, -0.2, 0.5]); sg_ = (I2n_ + m_[0]*Kn_ + m_[1]*Kpn_ + m_[2]*Jn_)/2
w_v = np.array([-np.sin(b_), 0, np.cos(b_)]); mw_ = m_@w_v; Tw_ = m_@m_ - mw_**2; c_ = np.cos(2*a_)
r_ran = fp_num(Hn_, sg_, a_); k_pred = -chir_*mw_*(1 - c_)/(1 - (1 - Tw_)*c_)
r_null = fp_num(Hn_, (I2n_ + Kn_)/2, a_); wK_ = -np.sin(b_)
k_inf = -chir_*wK_*(1 - c_)/(1 - wK_**2*c_); marg_ = (1 - wK_**2)**2/(1 - wK_**2*c_)**2
e1 = abs(r_ran[2] - k_pred); e2 = abs(r_null[2] - k_inf); e3 = abs(1 - r_null@r_null - marg_)
add('V38', 'V', 'numerical iteration (numpy/scipy, 700 collisions) of the tilted coupling (b=0.6, alpha=1.2, chi=-1): random mixed reference reproduces the C36 law; the positive null state reproduces kappa_inf and the faithfulness margin of C37 within 1e-9',
    e1 < 1e-9 and e2 < 1e-9 and e3 < 1e-9, f'errs={e1:.1e},{e2:.1e},{e3:.1e}; kappa_inf={k_inf:.6f}, 1-|r|^2={1-r_null@r_null:.6f}')

# W39 Proposition 8.2(ii) obligation: a smooth bounded alpha(x)=sin(x^2) does NOT preserve H^1 -- ||d/dx (e^{i alpha} psi)||_{L^2[0,L]} grows without bound
#     for psi(x)=(1+x)^{-0.6} in H^1(R+), while alpha in W^{1,inf} (alpha = sin x) keeps it bounded
xs = np.linspace(0, 400, 2_000_001); psi = (1 + xs)**-0.6
def dnorm(alpha_):
    g = np.exp(1j*alpha_)*psi; dg = np.gradient(g, xs)
    return [np.sqrt(np.trapezoid(np.abs(dg[:m_i])**2, xs[:m_i])) for m_i in (500_001, 1_000_001, 2_000_001)]
bad = dnorm(np.sin(xs**2)); good = dnorm(np.sin(xs))
add('W39', 'W', 'Proposition 8.2(ii) (v1.1 hypothesis): alpha(x)=sin(x^2) is smooth and bounded but ||(e^{i alpha}psi)\'||_{L^2[0,L]} grows with L for psi=(1+x)^{-0.6} in H^1 (alpha\' unbounded), whereas the Lipschitz alpha=sin x keeps it bounded: the domain-preservation statement needs alpha in W^{1,inf}',
    bad[2] > 1.3*bad[0] and bad[2] > 3*good[2] and good[2] < 1.2*good[0]*1.5, f'||.|| at L=100,200,400: unbounded-alpha\'={np.round(bad,3)}, Lipschitz={np.round(good,3)}')

# ================================================================ v1.2 rows (v1.1-audit counterexamples and repairs; every claim recomputed here)
Gjoint = sp.kronecker_product(sz, J)                     # joint grading J_E (x) J
def opv(vv): return vv[0]*K + vv[1]*Kp + vv[2]*J        # reference operator u.sigma_R in (K, K', J) coordinates
# C44 joint-grading transform sign and symmetry classification (Theorem 5.8(b)): Ad_{J_E⊗J}(X_E⊗(u.s)) = X_E⊗((u_K,u_K',-u_J).s);
#     [H_R, J_E⊗J] = 0 iff u_J = v_J = 0 (symbolic in u, v, chi)
uK_, uKp_, uJ_, vK_, vKp_, vJ_ = sp.symbols('u_K u_Kp u_J v_K v_Kp v_J', real=True)
XU = sp.kronecker_product(sx, opv((uK_, uKp_, uJ_)))
HRsym = XU + chi*sp.kronecker_product(sy, opv((vK_, vKp_, vJ_)))
sign_ok = sp.simplify(Gjoint*XU*Gjoint - sp.kronecker_product(sx, opv((uK_, uKp_, -uJ_)))) == sp.zeros(4, 4)
wrong_sign = sp.simplify(Gjoint*XU*Gjoint - sp.kronecker_product(sx, opv((-uK_, -uKp_, uJ_)))) == sp.zeros(4, 4)   # v1.1's printed sign: must NOT hold
comm = sp.simplify(HRsym*Gjoint - Gjoint*HRsym)
only_uJ_vJ = (sp.simplify(comm.subs({uJ_: 0, vJ_: 0})) == sp.zeros(4, 4)
              and sp.simplify(comm - comm.subs({uK_: 0, uKp_: 0, vK_: 0, vKp_: 0})) == sp.zeros(4, 4))
nonzero = (sp.simplify(comm.subs({vJ_: 0, uJ_: 1, chi: 1})) != sp.zeros(4, 4) and sp.simplify(comm.subs({uJ_: 0, vJ_: 1, chi: 1})) != sp.zeros(4, 4)
           and sp.simplify(comm.subs({vJ_: 0, uJ_: 1, chi: -1})) != sp.zeros(4, 4) and sp.simplify(comm.subs({uJ_: 0, vJ_: 1, chi: -1})) != sp.zeros(4, 4))
add('C44', 'C', 'Theorem 5.8(b): Ad_{J_E⊗J}(X_E⊗(u.sigma_R)) = X_E⊗((u_K, u_K\', -u_J).sigma_R) (the v1.1 proof printed (-u_K,-u_K\',u_J), which is checked NOT to hold); [H_R, J_E⊗J] depends only on (u_J, v_J) and vanishes iff u_J = v_J = 0, i.e. iff w = u x v = ±e_J (symbolic in u, v, both chiralities)',
    sign_ok and (not wrong_sign) and only_uJ_vJ and nonzero, 'symbolic', universal=True)

def chan_frame(u, v, chir):
    """exact affine data (M, b) of the collision channel for the frame (u, v) with symbolic reference m and angle alpha; spec H in {0,±2}."""
    Ht = sp.kronecker_product(sx, opv(u)) + chir*sp.kronecker_product(sy, opv(v))
    H2 = sp.simplify(Ht*Ht)
    assert sp.simplify(Ht*H2 - 4*Ht) == sp.zeros(4, 4)
    Ut = sp.eye(4) + (sp.cos(2*al) - 1)*H2/4 - sp.I*sp.sin(2*al)*Ht/2
    rxv, ryv, rzv = sp.symbols('r_x r_y r_z', real=True)
    rho2 = (I2 + rxv*sx + ryv*sy + rzv*sz)/2
    o = Ut*sp.kronecker_product(rho2, sig)*Ut.H
    red = sp.zeros(2, 2)
    for i in range(2):
        for j in range(2):
            red[i, j] = sum(o[2*i+k, 2*j+k] for k in range(2))
    comps = [sp.expand(sp.trace(red*X)) for X in (sx, sy, sz)]
    Mt = sp.Matrix([[sp.diff(cc_, v_) for v_ in (rxv, ryv, rzv)] for cc_ in comps])
    bt_ = sp.Matrix([cc_.subs({rxv: 0, ryv: 0, rzv: 0}) for cc_ in comps])
    return sp.simplify(Mt), sp.simplify(bt_), Ht
def frob(X): return sp.sqrt(sp.simplify(sp.trace(X.H*X)))

# W45 the audit's minimal counterexample to "w_K = 0 <=> joint-grading-even": proper frame (u,v,w) = (e_K, -e_J, e_K'): w_K = 0, grading-odd component, zero limiting record
u_c, v_c = (1, 0, 0), (0, 0, -1)
w_c = (u_c[1]*v_c[2]-u_c[2]*v_c[1], u_c[2]*v_c[0]-u_c[0]*v_c[2], u_c[0]*v_c[1]-u_c[1]*v_c[0])        # = (0, 1, 0)
Mc, bc, Hc = chan_frame(u_c, v_c, 1)
defect = frob(Gjoint*Hc*Gjoint - Hc)
Mn, bn = sp.simplify(Mc.subs({mK: 1, mKp: 0, mJ: 0})), sp.simplify(bc.subs({mK: 1, mKp: 0, mJ: 0}))     # conditional limit reference e_K
rlim = sp.simplify((sp.eye(3) - Mn).inv()*bn)
ok = (w_c == (0, 1, 0) and sp.simplify(defect - 4) == 0 and sp.simplify(rlim[2]) == 0 and sp.simplify(rlim) == sp.zeros(3, 1)
      and sp.simplify(sp.Matrix([u_c, v_c, w_c]).T.det() - 1) == 0)
add('W45', 'W', 'counterexample (audit F1): the proper frame (u,v,w) = (e_K, -e_J, e_K\') has w = e_K\' (w_K = 0), its Hamiltonian X_E⊗K - chi Y_E⊗J has joint-grading defect ||G H G - H||_F = 4 (grading-ODD component), and the conditional limiting record at the reference e_K is exactly 0: "w_K = 0" is a strictly larger class than "joint-grading-even", and a grading-odd component does not imply a surviving record',
    ok, f'w={w_c}, defect={defect}, limit r*={list(rlim)} (symbolic in alpha)')

# W46 same resource axis w = e_J, different Hamiltonian and channel: rotate (u,v) inside the odd plane by theta = 7/10 (Theorem 5.8(c))
th_ = sp.Rational(7, 10)
u_r, v_r = (sp.cos(th_), sp.sin(th_), 0), (-sp.sin(th_), sp.cos(th_), 0)
Mr, br, Hr = chan_frame(u_r, v_r, 1); M0, b0_, H0 = chan_frame((1, 0, 0), (0, 1, 0), 1)
grading_even = sp.simplify(Gjoint*Hr*Gjoint - Hr) == sp.zeros(4, 4)
subs_ = {mK: sp.Rational(3, 10), mKp: sp.Rational(1, 5), mJ: sp.Rational(2, 5), al: sp.Rational(7, 10)}
dH = float(sp.N(sp.re(frob(Hr - H0))))
dM = float(sp.N(sp.sqrt(sum(e**2 for e in sp.simplify((Mr - M0).subs(subs_))))))
# the record kappa_* is the same in both frames (class invariant): m_w = m_J, T_w = T for both
kap_r = sp.simplify(((sp.eye(3) - Mr).inv()*br)[2].subs(subs_)); kap_0 = sp.simplify(((sp.eye(3) - M0).inv()*b0_)[2].subs(subs_))
add('W46', 'W', 'Theorem 5.8(c): rotating (u,v) by theta=0.7 inside the odd plane keeps w = e_J and the joint-grading symmetry but changes the Hamiltonian (Frobenius distance 1.9397) and the affine matrix M for a fixed coherent reference (distance 0.2472), while the record kappa_* is unchanged: the soldered coupling is a unique resource-axis CLASS, not a unique Hamiltonian',
    grading_even and abs(dH - 1.93972291924599) < 1e-9 and abs(dM - 0.24716392368844592) < 1e-9 and sp.simplify(kap_r - kap_0) == 0,
    f'||H_theta - H_0||_F={dH:.10f}, ||M_theta - M_0||={dM:.10f}, kappa equal={sp.simplify(kap_r - kap_0) == 0}')

# W47 (audit F2) pure pole at |w_K| = 1 and zero unconditional bias at m_K(0) = 0
# (a) frame (u,v,w) = (e_K', e_J, e_K): w_K = 1; conditional limit reference e_K -> fixed point (0,0,-chi), |r*| = 1
Mp, bp, Hp = chan_frame((0, 1, 0), (0, 0, 1), 1)
Mp1, bp1 = sp.simplify(Mp.subs({mK: 1, mKp: 0, mJ: 0})), sp.simplify(bp.subs({mK: 1, mKp: 0, mJ: 0}))
rp = sp.simplify((sp.eye(3) - Mp1).inv()*bp1)
pure_ok = sp.simplify(rp - sp.Matrix([0, 0, -1])) == sp.zeros(3, 1)
# (b) tilt beta = 0.6 (w_K = -sin 0.6 != 0), unconditional reference limit (m_K(0),0,0) with m_K(0) = 0 -> fixed point 0
bt6 = sp.Rational(3, 5)
Mt6, bt6v, _ = chan_frame((sp.cos(bt6), 0, sp.sin(bt6)), (0, 1, 0), 1)
Mz, bz = sp.simplify(Mt6.subs({mK: 0, mKp: 0, mJ: 0})), sp.simplify(bt6v.subs({mK: 0, mKp: 0, mJ: 0}))
rz = sp.simplify((sp.eye(3) - Mz).inv()*bz)
zero_ok = sp.simplify(rz) == sp.zeros(3, 1) and sp.simplify(bz) == sp.zeros(3, 1)
add('W47', 'W', 'Theorem 5.9 exceptions (audit F2): (a) the frame (e_K\', e_J, e_K) has w_K = 1 and its conditional limiting carrier state is the PURE pole r* = (0,0,-chi), |r*| = 1 (biased but not faithful); (b) the tilted frame (w_K = -sin(3/5) != 0) with an initially K-unpolarised reference m_K(0) = 0 has zero unconditional bias (b = 0, r* = 0): "faithful biased iff w_K != 0" needed 0 < |w_K| < 1 (conditional) and 0 < |w_K m_K(0)| < 1 (unconditional)',
    pure_ok and zero_ok, f'(a) r*={list(rp)} (symbolic in alpha); (b) r*={list(rz)}')

# C48 threshold attainability (Theorem 5.9(iv)): k(a,c) = a(1-c)/(1-a^2 c); sup_c k = 2a/(1+a^2), NOT attained; exact gap; angle inverse; x(rho) inverts the sup
aa_, rr_ = sp.symbols('a rho', positive=True)
kac = aa_*(1 - cc)/(1 - aa_**2*cc); supk = 2*aa_/(1 + aa_**2)
gap_ok = sp.simplify(supk - kac - aa_*(1 - aa_**2)*(1 + cc)/((1 + aa_**2)*(1 - aa_**2*cc))) == 0
c_t = (aa_ - rr_)/(aa_*(1 - rr_*aa_))
inv_ok = sp.simplify(kac.subs(cc, c_t) - rr_) == 0
eq_ok = sp.simplify(c_t.subs(rr_, supk) + 1) == 0                      # equality with the supremum forces c = -1 (excluded)
xr_ = (1 - sp.sqrt(1 - rr_**2))/rr_
x_ok = sp.simplify(supk.subs(aa_, xr_) - rr_) == 0                      # sup = rho exactly at a = x(rho)
dk_ok = sp.simplify(sp.diff(kac, cc) + aa_*(1 - aa_**2)/(1 - aa_**2*cc)**2) == 0   # k decreasing in c for 0<a<1: sup approached as c -> -1
add('C48', 'C', 'Theorem 5.9(iv) (audit F3): with a=|w_K| in (0,1), c=cos2alpha in (-1,1): k(a,c)=a(1-c)/(1-a^2 c) is decreasing in c, sup_c k = 2a/(1+a^2) and 2a/(1+a^2) - k = a(1-a^2)(1+c)/((1+a^2)(1-a^2 c)) > 0 (supremum NOT attained); k(a,c_rho) = rho at c_rho = (a-rho)/(a(1-rho a)) and c_rho = -1 iff rho = 2a/(1+a^2); sup = rho at a = x(rho): a target rho is attained at an admissible angle iff a > x(rho) (strict), never at a = x(rho)',
    gap_ok and inv_ok and eq_ok and x_ok and dk_ok, 'symbolic in a, c, rho', universal=True)

# C49 the excluded angle alpha = pi/2: chiral channel M = diag(-1,-1,1), b = 0 for EVERY reference (both chiralities): every J_E-diagonal carrier state is fixed, no unique record
ok = True
for chir in (1, -1):
    Mq, bq, _ = chan_frame((1, 0, 0), (0, 1, 0), chir)
    ok &= sp.simplify(Mq.subs(al, sp.pi/2)) == sp.diag(-1, -1, 1) and sp.simplify(bq.subs(al, sp.pi/2)) == sp.zeros(3, 1)
add('C49', 'C', 'Theorem 5.9(iv) / Theorem 5.2: at the excluded angle alpha = pi/2 the chiral channel is M = diag(-1,-1,1), b = 0 for every reference and both chiralities (symbolic in m): every J_E-diagonal carrier state is fixed and no unique record exists, so the supremum 2a/(1+a^2) is not a value of any admissible channel',
    ok, 'symbolic in m, both chiralities', universal=True)

# C50 (audit F4) carrier record dynamics under the unconditional return (Prop 5.11): for the K-unpolarised reference m=(0,0,m0 f^n),
#     kappa_{n+1} = c^2 kappa_n - chi (1-c^2) m0 f^n; closed form; exact 4x4 instance alpha=pi/6, chi=+1, m0=1/2, rho0=I/2:
#     kappa1 = -3/8, kappa2 = (-45+18 sqrt5)/32, kappa2 - f kappa1 = -3/32 != 0; and Tr(J E1 sigma E1) = Tr(K' E1 sigma E1) = 0 for every sigma
cs_, fs_, m0s_, k0s_ = sp.symbols('c_s f_s m_0 kappa_0', real=True)
nn_ = sp.symbols('n', integer=True, nonnegative=True)
closed = (cs_**2)**nn_*k0s_ - (1 - cs_**2)*m0s_*((cs_**2)**nn_ - fs_**nn_)/(cs_**2 - fs_)
rec_ok = sp.simplify(closed.subs(nn_, nn_ + 1) - (cs_**2*closed - (1 - cs_**2)*m0s_*fs_**nn_)) == 0
# the affine data at m = (0,0,m_J): M = diag(c, c, c^2), b = -chi m_J (1-c^2) e_J  (from C13's M, b)
Mdiag, bdiag, _ = chan_frame((1, 0, 0), (0, 1, 0), 1)
Md, bd = sp.simplify(Mdiag.subs({mK: 0, mKp: 0})), sp.simplify(bdiag.subs({mK: 0, mKp: 0}))
diag_ok = (sp.simplify(Md - sp.diag(sp.cos(2*al), sp.cos(2*al), sp.cos(2*al)**2)) == sp.zeros(3, 3)
           and sp.simplify(bd - sp.Matrix([0, 0, -mJ*(1 - sp.cos(2*al)**2)])) == sp.zeros(3, 1))
# exact 4x4 instance
Hpp = sp.kronecker_product(sx, K) + sp.kronecker_product(sy, Kp)
Hpp2 = sp.simplify(Hpp*Hpp); assert sp.simplify(Hpp*Hpp2 - 4*Hpp) == sp.zeros(4, 4)
Upp = sp.eye(4) + (sp.cos(sp.pi/3) - 1)*Hpp2/4 - sp.I*sp.sin(sp.pi/3)*Hpp/2      # exact e^{-i(pi/6)H} via spec H in {0, ±2}
def carrier_after(rho_, ref_):
    o_ = sp.simplify(Upp*sp.kronecker_product(rho_, ref_)*Upp.H)
    return sp.simplify(sp.Matrix(2, 2, lambda i, j: sum(o_[2*i+k, 2*j+k] for k in range(2))))
ref0 = (I2 + sp.Rational(1, 2)*J)/2
Lam_ = lambda X: S(E0*X*E0 + E1*X*E1)
rho1 = carrier_after(I2/2, ref0); rho2 = carrier_after(rho1, Lam_(ref0))
k1 = S(sp.trace(rho1*J)); k2 = S(sp.trace(rho2*J))
inst_ok = (S(k1 + sp.Rational(3, 8)) == 0 and S(k2 - (-45 + 18*sp.sqrt(5))/32) == 0 and S(k2 - phi**-4*k1 + sp.Rational(3, 32)) == 0
           and S(closed.subs({nn_: 1, k0s_: 0, cs_: sp.Rational(1, 2), fs_: phi**-4, m0s_: sp.Rational(1, 2)}) - k1) == 0
           and S(closed.subs({nn_: 2, k0s_: 0, cs_: sp.Rational(1, 2), fs_: phi**-4, m0s_: sp.Rational(1, 2)}) - k2) == 0)
fail_ok = S(sp.trace(E1*sig*E1*J)) == 0 and S(sp.trace(E1*sig*E1*Kp)) == 0
add('C50', 'C', 'Proposition 5.11 (audit F4): at m=(0,0,m_J) the chiral channel is M=diag(c,c,c^2), b=-chi m_J(1-c^2)e_J, so with fresh copies m_J(n)=m0 f^n the carrier record obeys kappa_{n+1}=c^2 kappa_n - chi(1-c^2) m0 f^n with the closed form kappa_n=(c^2)^n kappa_0 - chi(1-c^2)m0((c^2)^n-f^n)/(c^2-f) (symbolic); exact 4x4 instance alpha=pi/6, chi=+1, m0=1/2, rho0=I/2: kappa1=-3/8, kappa2=(-45+18sqrt5)/32, kappa2 - f kappa1 = -3/32 != 0 (phi^-4n is the reference law, not the carrier lifetime); the canonical failure branch stores no transverse expectation: Tr(J E1 sigma E1) = Tr(K\' E1 sigma E1) = 0 for every sigma',
    rec_ok and diag_ok and inst_ok and fail_ok, f'kappa1={k1}, kappa2={k2}, kappa2-f*kappa1={S(k2 - phi**-4*k1)}', universal=True)

# C51 (audit F5) failure-branch unitary V: Q = I - A^2/lambda^2 = aI - bK; Lambda_V unital iff V Q V^dag = Q iff V K V^dag = K;
#     V = exp(i pi K/4) != I is unital and leaves the maximal-strength channel unchanged; V = exp(i pi J/4) rotates K and is nonunital; det Q(lambda=3) = 19/81
Qm_ = I2 - A*A/lam**2
Vk = (I2 + sp.I*K)/sp.sqrt(2); Vj = (I2 + sp.I*J)/sp.sqrt(2)
q_form = sp.simplify(Qm_ - ((1 - sp.cosh(2*eta)/lam**2)*I2 - sp.sinh(2*eta)/lam**2*K)) == sp.zeros(2, 2)
vk_ok = sp.simplify(Vk - I2) != sp.zeros(2, 2) and sp.simplify(Vk*K*Vk.H - K) == sp.zeros(2, 2) and sp.simplify(Vk*Qm_*Vk.H - Qm_) == sp.zeros(2, 2)
LamV = lambda X, V: S(E0*X*E0 + V*E1*X*E1*V.H)
unchanged = S(LamV(sig, Vk) - Lam_(sig)) == sp.zeros(2, 2)
vj_nonunital = S(LamV(I2, Vj) - I2) != sp.zeros(2, 2) and sp.simplify(Vj*K*Vj.H - K) != sp.zeros(2, 2)
# general lambda: the K-commuting V keeps the completion unital; a K-rotating V does not (lambda = 3)
Q3 = sp.simplify(Qm_.subs(lam, 3)); E0_3 = A/3
lam3_unital_k = sp.simplify(E0_3*E0_3 + Vk*Q3*Vk.H - I2) == sp.zeros(2, 2)     # E0^2 + V Q V^dag = I iff V Q V^dag = Q
lam3_nonunital_j = sp.simplify(E0_3*E0_3 + Vj*Q3*Vj.H - I2) != sp.zeros(2, 2)
detQ3 = S(sp.det(Q3))
add('C51', 'C', 'Remark 4.6.2(b) (audit F5): Q = I - A^2/lambda^2 = (1-cosh2eta/lambda^2) I - (sinh2eta/lambda^2) K, so the completion E0 sigma E0 + V Q^{1/2} sigma Q^{1/2} V^dag is unital iff V Q V^dag = Q iff V K V^dag = K; V = exp(i pi K/4) != I satisfies this and at maximal strength leaves the whole channel unchanged (symbolic in m); V = exp(i pi J/4) rotates K and gives a nonunital completion (at lambda=||A|| and at lambda=3); det Q = 19/81 > 0 at lambda = 3 (full rank: the failed state is input-dependent, not a re-preparation)',
    q_form and vk_ok and unchanged and vj_nonunital and lam3_unital_k and lam3_nonunital_j and detQ3 == sp.Rational(19, 81),
    f'det Q(3)={detQ3}', universal=True)

# C52 Lemma 5.10(a): characteristic polynomial of M (symbolic in m, c; chi = +1, sin2alpha = sqrt(1-c^2)) is (l-c)[l^2 - c(1+c) l + d], d = c[c^2 + q(1-c^2)], q = T^2;
#     Jury identities: 1 - c(1+c) + d = (1-c^2)[1-(1-q)c]; (1 + c(1+c) + d)|_{q=1} = (1+c)^2 and d/dq of it = c(1-c^2); d = c[1 - (1-q)(1-c^2)] so |d| <= |c|
lamb_ = sp.symbols('lambda_', real=True); q_ = sp.symbols('q', nonnegative=True)
sn_ = sp.sqrt(1 - cc**2)
Mg = sp.Matrix([[cc, 0, mKp*sn_], [0, cc, -mK*sn_], [-mKp*cc*sn_, mK*cc*sn_, cc**2]])     # Theorem 5.2 M at chi=+1 with sin4alpha/2 = sin2alpha cos2alpha
cp_ = sp.expand((lamb_*sp.eye(3) - Mg).det())
d_ = cc*(cc**2 + q_*(1 - cc**2))
target = sp.expand((lamb_ - cc)*(lamb_**2 - cc*(1 + cc)*lamb_ + d_))
cp_ok = sp.simplify(sp.expand(cp_.subs(mK**2, q_ - mKp**2)) - target) == 0
# chi = -1 gives the same polynomial (sign flips cancel in the products)
Mg2 = sp.Matrix([[cc, 0, -mKp*sn_], [0, cc, -mK*sn_], [mKp*cc*sn_, mK*cc*sn_, cc**2]])
cp2_ok = sp.simplify(sp.expand(sp.expand((lamb_*sp.eye(3) - Mg2).det()).subs(mK**2, q_ - mKp**2)) - target) == 0
j1 = sp.simplify(1 - cc*(1 + cc) + d_ - (1 - cc**2)*(1 - (1 - q_)*cc)) == 0
plus_ = 1 + cc*(1 + cc) + d_
j2 = sp.simplify(plus_.subs(q_, 1) - (1 + cc)**2) == 0 and sp.simplify(sp.diff(plus_, q_) - cc*(1 - cc**2)) == 0
j3 = sp.simplify(d_ - cc*(1 - (1 - q_)*(1 - cc**2))) == 0
add('C52', 'C', 'Lemma 5.10(a): for every reference the affine matrix M of Theorem 5.2 has characteristic polynomial (l-c)[l^2 - c(1+c)l + d], d = c[c^2 + q(1-c^2)], q = T^2 (symbolic in m, c, both chiralities); Jury identities for the quadratic: 1-c(1+c)+d = (1-c^2)[1-(1-q)c] > 0, (1+c(1+c)+d) is affine in q with slope c(1-c^2) and equals (1+c)^2 at q=1, and d = c[1-(1-q)(1-c^2)] gives |d| <= |c| < 1: all eigenvalues lie in the open unit disc for -1 < c < 1 (Schur stability)',
    cp_ok and cp2_ok and j1 and j2 and j3, 'symbolic', universal=True)

# V53 Lemma 5.10(b): actual sequential fresh-copy collisions (numpy/scipy, direct 4x4, tilted frame beta=0.6) converge to the limiting fixed point in both readings
eta_n = float(np.arccosh(1.5)); fn_ = float(np.exp(-2*eta_n))
def passive(m, n, conditional):
    if not conditional: return np.array([m[0], fn_**n*m[1], fn_**n*m[2]])
    t_ = np.tanh(2*n*eta_n); den = 1 + m[0]*t_
    return np.array([(m[0] + t_)/den, m[1]/np.cosh(2*n*eta_n)/den, m[2]/np.cosh(2*n*eta_n)/den])
def affine_num(u, v, m, a_, chir):
    Hn = np.kron(sxn_, u[0]*Kn_ + u[1]*Kpn_ + u[2]*Jn_) + chir*np.kron(syn_, v[0]*Kn_ + v[1]*Kpn_ + v[2]*Jn_)
    Un = expm(-1j*a_*Hn); sg = (I2n_ + m[0]*Kn_ + m[1]*Kpn_ + m[2]*Jn_)/2
    def ch(rh):
        out = Un @ np.kron(rh, sg) @ Un.conj().T
        return out.reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)
    bvec = np.array([np.trace(ch(I2n_/2) @ X).real for X in (sxn_, syn_, szn_)])
    Mm = np.column_stack([np.array([np.trace(ch(P/2) @ X).real for X in (sxn_, syn_, szn_)]) for P in (sxn_, syn_, szn_)])
    return Mm, bvec
b6 = 0.6; u6 = (np.cos(b6), 0, np.sin(b6)); v6 = (0, 1, 0)
m0v = np.array([0.4, 0.2, 0.3]); errs = []
for conditional in (False, True):
    rr = np.array([0.2, -0.1, 0.3]); limit = np.array([1.0 if conditional else m0v[0], 0, 0])
    Ml, bl = affine_num(u6, v6, limit, 0.7, 1); rlim = np.linalg.solve(np.eye(3) - Ml, bl)
    for n in range(140):
        Mn_, bn_ = affine_num(u6, v6, passive(m0v, n, conditional), 0.7, 1); rr = Mn_ @ rr + bn_
    errs.append(float(np.linalg.norm(rr - rlim)))
add('V53', 'V', 'Lemma 5.10(b): direct 4x4 sequential collisions with a fresh reference copy each step (tilted frame beta=0.6, alpha=0.7, chi=+1; reference m(0)=(0.4,0.2,0.3) evolving by the passive return) converge to the fixed point of the limit channel within 1e-11 after 140 collisions, in both the unconditional (m_K conserved) and the conditional (m -> e_K) readings',
    all(e < 1e-11 for e in errs), f'errors after 140 collisions: unconditional={errs[0]:.2e}, conditional={errs[1]:.2e}')

# C54 (audit F6) unconditional supremum over alpha: with b0 = m_K(0), sup_c |kappa_inf| = 2|w_K b0|/(2 - b0^2(1-w_K^2)) -- a function of (w_K, b0), not of w_K alone
b0s = sp.symbols('b_0', real=True)
kunc = -wK*b0s*(1 - cc)/(1 - (1 - b0s**2*(1 - wK**2))*cc)
sup_unc = sp.simplify(kunc.subs(cc, -1))                      # limit value at c -> -1 (not attained)
ok = sp.simplify(sup_unc + 2*wK*b0s/(2 - b0s**2*(1 - wK**2))) == 0
# it is the Theorem 5.3 supremum with m_w = w_K b0, T_w^2 = b0^2 (1-w_K^2): 2 m_w/(2-T_w^2) (checked against the C15 form of sup g)
mw_, Tw2_ = wK*b0s, b0s**2*(1 - wK**2)
ok &= sp.simplify(mw_*gfun.subs({TT2: Tw2_, cc: -1}) - 2*mw_/(2 - Tw2_)) == 0
add('C54', 'C', 'Theorem 5.9(v) (audit F6): in the unconditional reading the limiting record -chi w_K b0 (1-c)/(1-(1-b0^2(1-w_K^2))c), b0 = m_K(0), has sup over the collision angle equal to 2|w_K b0|/(2 - b0^2(1-w_K^2)) (the Theorem 5.3 supremum with m_w = w_K b0, T_w^2 = b0^2(1-w_K^2)); the optimum depends on (w_K, m_K(0)), not on w_K alone (symbolic)',
    ok, 'symbolic in w_K, b0', universal=True)

# C55 v1.0-audit leftovers repaired in v1.2 (L-1, L-2, L-4): H_chi^2 = 2(I + chi Z⊗Z) (both chiralities; the minus sign printed in v1.0/v1.1 is checked NOT to hold);
#     D endpoints D|_{T=0} = 1-c, D|_{T=1} = 1 (v1.1 had them interchanged) and D >= 1-|c|; g(c,0) = 1 identically (the sup is attained at T=0);
#     second-bound gap 2m/(1+m^2) - 2m/(2-T^2) = 2m(1-m^2-T^2)/((2-T^2)(1+m^2)) (equality iff m=0 or pure)
ok = True
for chir in (1, -1):
    Hc_ = sp.kronecker_product(sx, K) + chir*sp.kronecker_product(sy, Kp)
    ok &= sp.simplify(Hc_*Hc_ - 2*(sp.eye(4) + chir*Gjoint)) == sp.zeros(4, 4)
    ok &= sp.simplify(Hc_*Hc_ - 2*(sp.eye(4) - chir*Gjoint)) != sp.zeros(4, 4)
Dg = 1 - (1 - TT2)*cc
ok &= sp.simplify(Dg.subs(TT2, 0) - (1 - cc)) == 0 and sp.simplify(Dg.subs(TT2, 1) - 1) == 0
ok &= sp.simplify(gfun.subs(TT2, 0) - 1) == 0
mm2 = sp.symbols('m2', nonnegative=True)
ok &= sp.simplify(2*mm2/(1 + mm2**2) - 2*mm2/(2 - TT2) - 2*mm2*(1 - mm2**2 - TT2)/((2 - TT2)*(1 + mm2**2))) == 0
# D >= 1 - |c|: check the two sign cases symbolically: for c>=0, D - (1-c) = T^2 c >= 0; for c<0, D - (1+c) = -c(2 - T^2)... = (1-(1-T^2)c) - (1+c) = -c(2-T^2) >= 0
ok &= sp.simplify(Dg - (1 - cc) - TT2*cc) == 0 and sp.simplify(Dg - (1 + cc) + cc*(2 - TT2)) == 0
add('C55', 'C', 'v1.0/v1.1 leftovers (audit L-1, L-2, L-4): H_chi^2 = 2(I + chi Z⊗Z) for both chiralities (the printed minus sign does not hold); D = 1-(1-T^2)c has endpoints D=1-c at T=0 and D=1 at T=1 (interchanged in v1.1) and D-(1-c)=T^2 c, D-(1+c)=-c(2-T^2), hence D >= 1-|c| > 0; g(c,0) = 1 identically so the Theorem 5.3 supremum IS attained at T=0 ("not attained" needs T>0); second-bound gap 2m/(1+m^2)-2m/(2-T^2) = 2m(1-m^2-T^2)/((2-T^2)(1+m^2)): equality iff m=0 or the reference is pure',
    ok, 'symbolic', universal=True)

# W56 Theorem 6.6 (audit §8.2): time-dependent unital refreshes (a fresh random rotation each cycle): (1-f^2) sum |P_perp r_n|^2 <= |r_0|^2 and the transverse part -> 0
rng6 = np.random.default_rng(7); r6 = np.array([0.2, 0.5, 0.6]); r0n = float(r6 @ r6); tot = 0.0; steps = []
for n in range(2000):
    Qm6, _ = np.linalg.qr(rng6.normal(size=(3, 3)))
    if np.linalg.det(Qm6) < 0: Qm6[:, 0] *= -1
    lam_r = np.array([1, fn_, fn_])*r6
    steps.append(float(r6 @ r6 - (Qm6 @ lam_r) @ (Qm6 @ lam_r) - (1 - fn_**2)*(r6[1]**2 + r6[2]**2)))     # per-step inequality residual (>= 0)
    tot += r6[1]**2 + r6[2]**2
    r6 = Qm6 @ lam_r
add('W56', 'W', 'Theorem 6.6 witness: with a different random rotation (unital refresh) at every one of 2000 cycles after the phi^-4 dephaser, the per-step inequality |r_n|^2 - |r_{n+1}|^2 >= (1-f^2)|P_perp r_n|^2 holds at every step, the summed bound (1-f^2) sum |P_perp r_n|^2 <= |r_0|^2 holds, and the transverse component reaches machine zero (asymptotic depletion, not merely absence of a fixed point)',
    min(steps) > -1e-12 and (1 - fn_**2)*tot <= r0n + 1e-12 and float(np.hypot(r6[1], r6[2])) < 1e-12,
    f'min per-step residual={min(steps):.1e}, (1-f^2)*sum={(1-fn_**2)*tot:.6f} <= |r0|^2={r0n:.6f}, final transverse={float(np.hypot(r6[1], r6[2])):.1e}')

# V57 comparison (locked T_2): at |w_K| = x(T_2) exactly, every admissible angle gives |kappa_inf| < T_2 (alpha = 1.56: 0.83533 < 0.83538); the gap matches the C48 formula
xT = (1 - mp.sqrt(1 - T2_lock**2))/T2_lock
al156 = mp.mpf('1.56'); c156 = mp.cos(2*al156)
k156 = xT*(1 - c156)/(1 - xT**2*c156)
gap156 = xT*(1 - xT**2)*(1 + c156)/((1 + xT**2)*(1 - xT**2*c156))
ok = (k156 < T2_lock) and abs((T2_lock - k156) - gap156) < mp.mpf('1e-25') and abs(2*xT/(1 + xT**2) - T2_lock) < mp.mpf('1e-25')
add('V57', 'V', 'comparison (Theorem 5.9(iv) with locked T_2): at |w_K| = x(T_2) = ' + mp.nstr(xT, 12) + ' the supremum over alpha equals T_2 but the admissible angle alpha = 1.56 gives |kappa_inf| = ' + mp.nstr(k156, 8) + ' < T_2 = ' + mp.nstr(T2_lock, 8) + ' with the gap given exactly by the C48 formula: "reachable iff |w_K| >= 0.539" (v1.1) is replaced by the strict "|w_K| > x(T_2)"',
    ok, f'x(T_2)={mp.nstr(xT,20)}, kappa(1.56)={mp.nstr(k156,20)}, gap={mp.nstr(gap156,10)}', comparison=True)

# C58 Remark 6.6.1 (K15 refinement, audit optional): at maximal strength a failure state with Bloch vector v gives x' = x + (1-f^2)(1-x)(1+v_K)/2 for x = m_K;
#     fixed point x = 1 only, for v_K > -1
vK_, vKp2_, vJ2_ = sp.symbols('v_K v_Kp2 v_J2', real=True)
fail_state = (I2 + vK_*K + vKp2_*Kp + vJ2_*J)/2
LamF = S(E0*sig*E0 + (1 - phi**-8)*sp.trace(Pm*sig)*fail_state)          # E1 sigma E1 = (1-f^2) Tr(P_- sigma) P_- ; replaced by V|-><-|V^dag = fail_state
xprime = S(sp.trace(LamF*K))
law_ok = S(xprime - (mK + (1 - phi**-8)*(1 - mK)*(1 + vK_)/2)) == 0
fp = sp.solve(sp.Eq(S(xprime - mK).subs(vK_, sp.Rational(1, 3)), 0), mK)
add('C58', 'C', 'Remark 6.6.1 (K15 refinement): at lambda = ||A|| a non-canonical failure state with Bloch vector v gives the exact longitudinal law m_K\' = m_K + (1-f^2)(1-m_K)(1+v_K)/2 (symbolic in m, v); for v_K > -1 its only fixed point is m_K = 1 (transverse part necessarily zero): a pure re-preparation on the failure branch alone does not sustain a transverse reference state at maximal strength',
    law_ok and fp == [1], f'fixed points at v_K=1/3: {fp}', universal=True)

# ================================================================ v1.3 rows (v1.2-audit counterexamples, repairs and positive supplements; every claim recomputed here)
# W59 (audit F2): Schur stability is NOT one-step strict contractivity. At the reference m = e_K and alpha = pi/4 the chiral channel has
#     M = [[0,0,0],[0,0,-1],[0,0,0]] (nilpotent: M^2 = 0, rho(M) = 0) but ||M||_2 = 1, and the carrier states (I±Z)/2 map to (I∓Y)/2:
#     the trace distance 1 is preserved in one collision. Lemma 5.10(b) is unaffected (it uses an adapted norm).
Mq4, bq4, chq4 = None, None, None
Hq = sp.kronecker_product(sx, K) + sp.kronecker_product(sy, Kp); Hq2 = sp.simplify(Hq*Hq)
Uq4 = sp.eye(4) + (sp.cos(sp.pi/2) - 1)*Hq2/4 - sp.I*sp.sin(sp.pi/2)*Hq/2       # exact e^{-i(pi/4)H}
sig_eK = (I2 + K)/2
def ch_q4(rho_): 
    o_ = sp.simplify(Uq4*sp.kronecker_product(rho_, sig_eK)*Uq4.H)
    return sp.simplify(sp.Matrix(2, 2, lambda i, j: sum(o_[2*i+k, 2*j+k] for k in range(2))))
Mq4 = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.trace(ch_q4([sx, sy, sz][j]/2)*[sx, sy, sz][i])))
bq4 = sp.Matrix([sp.simplify(sp.trace(ch_q4(I2/2)*X)) for X in (sx, sy, sz)])
rp_, rm_ = ch_q4((I2 + sz)/2), ch_q4((I2 - sz)/2)
sv_max = max(sp.Abs(e_) for e_ in (Mq4.T*Mq4).eigenvals())
add('W59', 'W', 'audit F2 counterexample: at m = e_K, alpha = pi/4 the chiral channel is affine with M = [[0,0,0],[0,0,-1],[0,0,0]] and b = 0 (M^2 = 0, spectral radius 0, Schur-stable) but ||M||_2 = 1 and the carrier states (I±Z)/2 are mapped to (I∓Y)/2: the trace distance 1 is preserved in one collision. Schur stability of the affine part (Lemma 5.10(a)) does NOT give one-step strict contractivity of Phi_sigma in the Euclidean/trace distance; the v1.2 §10.3-7 sentence is withdrawn (Lemma 5.10(b) uses an adapted norm and stands)',
    Mq4 == sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 0, 0]]) and bq4 == sp.zeros(3, 1) and sp.simplify(Mq4*Mq4) == sp.zeros(3, 3)
    and sv_max == 1 and sp.simplify(rp_ - (I2 - sy)/2) == sp.zeros(2, 2) and sp.simplify(rm_ - (I2 + sy)/2) == sp.zeros(2, 2),
    f'M={Mq4.tolist()}, ||M||_2={sv_max}, (I+Z)/2 -> {rp_.tolist()}, (I-Z)/2 -> {rm_.tolist()}')

# C60 (audit F1): unconditional limiting record kappa = -chi w_K b0 (1-c)/D_w with D_w >= 1-|c| > 0: zero iff w_K b0 = 0 (NOT iff w_K = 0);
#     and |w_K| = 1 with 0 < |b0| < 1 gives a biased AND faithful unconditional record (kappa = -chi b0, margin 1 - b0^2); direct 4x4 witness at b0 = 1/2
kunc60 = -chi*wK*b0s*(1 - cc)/(1 - (1 - b0s**2*(1 - wK**2))*cc)
num60, den60 = sp.fraction(sp.together(kunc60))
Dw60 = 1 - (1 - b0s**2*(1 - wK**2))*cc
ok = (sp.factor(num60) == sp.factor(-chi*wK*b0s*(1 - cc)) or sp.simplify(num60 + chi*wK*b0s*(1 - cc)) == 0)
ok &= sp.simplify(Dw60 - (1 - cc) - b0s**2*(1 - wK**2)*cc) == 0 and sp.simplify(Dw60 - (1 + cc) + cc*(2 - b0s**2*(1 - wK**2))) == 0   # D_w - (1-c) = T_w^2 c, D_w - (1+c) = -c(2 - T_w^2): D_w >= 1-|c|
ok &= sp.simplify(kunc60.subs({wK: sp.Rational(3, 5), b0s: 0, cc: 0})) == 0                    # w_K != 0 but m_K(0) = 0: zero
Tw2_60 = b0s**2*(1 - wK**2); marg60 = (Tw2_60**2 + (1 - b0s**2)*(Tw2_60*(1 - cc**2) + (1 - cc)**2))/Dw60**2
ok &= sp.simplify(kunc60.subs({wK: 1, b0s: sp.Rational(1, 2)}) + chi/2) == 0 and sp.simplify(marg60.subs({wK: 1, b0s: sp.Rational(1, 2)}) - sp.Rational(3, 4)) == 0
ok &= sp.simplify(kunc60.subs(wK, 1) + chi*b0s) == 0 and sp.simplify(marg60.subs(wK, 1) - (1 - b0s**2)) == 0    # |w_K| = 1: kappa = -chi b0, margin 1 - b0^2 for every c
# direct 4x4: frame (e_K', e_J, e_K) (w = e_K), held reference (1/2, 0, 0), alpha = pi/4 -> fixed point (0,0,-1/2), margin 3/4; and Lambda fixes that reference
Mx60, bx60, _ = chan_frame((0, 1, 0), (0, 0, 1), 1)
Mx60h, bx60h = sp.simplify(Mx60.subs({mK: sp.Rational(1, 2), mKp: 0, mJ: 0, al: sp.pi/4})), sp.simplify(bx60.subs({mK: sp.Rational(1, 2), mKp: 0, mJ: 0, al: sp.pi/4}))
rx60 = sp.simplify((sp.eye(3) - Mx60h).inv()*bx60h)
sig_half = (I2 + K/2)/2
ok &= rx60[2] == -sp.Rational(1, 2) and sp.simplify(1 - (rx60.T*rx60)[0]) == sp.Rational(3, 4) and S(E0*sig_half*E0 + E1*sig_half*E1 - sig_half) == sp.zeros(2, 2)
# v1.4 (audit F3): the NEGATIVE axis w = -e_K, frame (e_K', -e_J): kappa_inf = -chi w_K m_K(0) = +chi m_K(0); direct 4x4 at m_K(0) = 1/2, chi = +1, alpha = pi/4 -> r* = (0,0,+1/2)
ok &= sp.simplify(kunc60.subs(wK, -1) - chi*b0s) == 0 and sp.simplify(marg60.subs(wK, -1) - (1 - b0s**2)) == 0
Mx60n, bx60n, _ = chan_frame((0, 1, 0), (0, 0, -1), 1)
Mx60nh, bx60nh = sp.simplify(Mx60n.subs({mK: sp.Rational(1, 2), mKp: 0, mJ: 0, al: sp.pi/4})), sp.simplify(bx60n.subs({mK: sp.Rational(1, 2), mKp: 0, mJ: 0, al: sp.pi/4}))
rx60n = sp.simplify((sp.eye(3) - Mx60nh).inv()*bx60nh)
ok &= rx60n[2] == sp.Rational(1, 2) and sp.simplify(1 - (rx60n.T*rx60n)[0]) == sp.Rational(3, 4)
add('C60', 'C', 'Theorem 5.9(ii) (audit F1): the unconditional limiting record -chi w_K b0 (1-c)/D_w, b0 = m_K(0), has numerator -chi w_K b0 (1-c) and denominator D_w >= 1-|c| > 0, so it is ZERO iff w_K m_K(0) = 0 (not iff w_K = 0: w_K = 3/5, m_K(0) = 0 gives 0); and |w_K| = 1 with 0 < |m_K(0)| < 1 gives a biased and FAITHFUL unconditional record (kappa = -chi w_K m_K(0) with w_K = ±1, margin 1 - m_K(0)^2; direct 4x4 witnesses at m_K(0) = 1/2, chi = +1: w = +e_K gives r* = (0,0,-1/2), w = -e_K gives r* = (0,0,+1/2), margin 3/4 both, reference return-invariant -- the v1.3 row and text dropped the sign w_K, audit F3): the pure pole at |w_K| = 1 is a CONDITIONAL-reading fact (symbolic in w_K, b0, c)',
    ok, f'direct r*(w=+e_K)={list(rx60)}, r*(w=-e_K)={list(rx60n)}', universal=True)

# C61 (audit F3, comparison row: uses locked M_*, T_2): K10 fixed-angle envelope. For fixed c the maximal capacity over references with T >= M_* is
#     B(c) = m_max (1-c)/(1 - m_max^2 c), m_max = sqrt(1-M_*^2) (the map m -> m(1-c)/(1-m^2 c) is increasing: derivative (1-c)(1+c m^2)/(1-c m^2)^2 > 0;
#     the pure reference at T = M_* maximises). B is decreasing in c; B(0) = sqrt(1-M_*^2) (the seed bound); B(c) < T_2 iff c > c_crit = (m_max - T_2)/(m_max(1 - T_2 m_max)).
#     cos2alpha >= 0 is therefore SUFFICIENT for the K10 kill but not necessary: at c = -1/10, B = 0.68210... < T_2 (exact rational comparison of squares).
env61 = mm2*(1 - cc)/(1 - mm2**2*cc)
ok = sp.simplify(sp.diff(env61, mm2) - (1 - cc)*(1 + cc*mm2**2)/(1 - cc*mm2**2)**2) == 0
ok &= sp.simplify(sp.diff(env61, cc) + mm2*(1 - mm2**2)/(1 - mm2**2*cc)**2) == 0            # decreasing in c for 0 < m < 1
mmax2_q = 1 - Mstar_q**2                                                                        # exact rational
B2_at = lambda cv: mmax2_q*(1 - cv)**2/(1 - mmax2_q*cv)**2                                     # B(c)^2 for rational c
ok &= bool(B2_at(sp.Rational(-1, 10)) < T2_lock_q**2) and bool(B2_at(0) < T2_lock_q**2) and sp.simplify(B2_at(0) - mmax2_q) == 0
mmax_m = mp.sqrt(1 - Mstar**2); ccrit = (mmax_m - T2_lock)/(mmax_m*(1 - T2_lock*mmax_m))     # display only (mp.nstr in the claim/detail)
# v1.4.1 (audit F2): the two facts used by the claim are certified EXACTLY, with no tolerance term.
mmv_, rho_ = sp.symbols('mm_env rho_env', positive=True)
env_sym = mmv_*(1 - cc)/(1 - mmv_**2*cc); crit_sym = (mmv_ - rho_)/(mmv_*(1 - rho_*mmv_))
ok &= sp.simplify(env_sym.subs(cc, crit_sym) - rho_) == 0                                      # B(c_crit) = rho identically
ok &= bool(mmax2_q < T2_lock_q**2) and bool(T2_lock_q**2*(1 + mmax2_q)**2 < 4*mmax2_q)         # m_max < T_2 < 2 m_max/(1+m_max^2)  =>  -1 < c_crit < 0 (exact rationals)
# at c slightly below c_crit the envelope exceeds T_2 (exact rational c = -0.64, squares compared)
ok &= bool(B2_at(sp.Rational(-64, 100)) > T2_lock_q**2) and bool(B2_at(sp.Rational(-63, 100)) < T2_lock_q**2)
add('C61', 'C', 'Corollary 7.1 (K10, audit v1.2 F3; comparison row; SOLDERED RESOURCE-AXIS CLASS w = +-e_J with the original J grading fixed, where T_w = T -- outside that class the exclusion is FALSE, see W66/W69; audit v1.4 F1): for fixed c = cos2alpha the maximal capacity over references with T >= M_* is the envelope B(c) = m_max(1-c)/(1-m_max^2 c), m_max = sqrt(1-M_*^2) (m -> m(1-c)/(1-m^2 c) increasing, exact derivative), B decreasing in c with B(0) = sqrt(1-M_*^2); the joint demand is excluded iff B(c) < T_2 iff c > c_crit = (m_max - T_2)/(m_max(1 - T_2 m_max)) = ' + mp.nstr(ccrit, 12) + '; hence cos2alpha >= 0 is SUFFICIENT for the K10 kill, not necessary: at c = -1/10, B = ' + mp.nstr(mmax_m*(1 + mp.mpf('0.1'))/(1 + mmax_m**2*mp.mpf('0.1')), 10) + ' < T_2 (exact rational comparison of squares); B(-0.64) > T_2 > B(-0.63); c_crit is certified exactly by B(c_crit) = rho and by m_max < T_2 < 2m_max/(1+m_max^2), the decimal being a display value (v1.4.1, audit F2)',
    ok, f'c_crit={mp.nstr(ccrit, 20)}; B(-1/10)^2={float(B2_at(sp.Rational(-1,10))):.10f} < T_2^2={float(T2_lock_q**2):.10f}', comparison=True)

# C62 (audit §7.1 positive witness; comparison row: uses locked T_2): two consecutive references of the pure passive orbit,
#     m^(0) = (-sqrt5/3, 0, 2/3) and m^(1) = (+sqrt5/3, 0, 2/3) = one passive return of m^(0), both have held-reference capacity
#     |kappa_*| = 16/19 > T_2 at the finite admissible angle cos2alpha = -3/5, with faithfulness margin 625/3249 > 0 (exact).
m0_62 = (-sp.sqrt(5)/3, 0, sp.Rational(2, 3)); m1_62 = (sp.sqrt(5)/3, 0, sp.Rational(2, 3)); c62 = -sp.Rational(3, 5)
kap62 = lambda m_: m_[2]*(1 - c62)/(1 - (1 - m_[0]**2 - m_[1]**2)*c62)
sig62 = (I2 + m0_62[0]*K + m0_62[1]*Kp + m0_62[2]*J)/2; o62 = S(A*sig62*A); tr62 = S(sp.trace(o62))
orbit_ok = all(S(sp.trace(o62*X)/tr62 - v_) == 0 for X, v_ in zip((K, Kp, J), m1_62))
ok = (sp.simplify(kap62(m0_62) - sp.Rational(16, 19)) == 0 and sp.simplify(kap62(m1_62) - sp.Rational(16, 19)) == 0 and orbit_ok
      and sp.simplify(sum(v_**2 for v_ in m0_62) - 1) == 0 and bool(sp.Rational(16, 19) > T2_lock_q)
      and sp.simplify(sp.Rational(5, 9)**2/(1 - (1 - sp.Rational(5, 9))*c62)**2 - sp.Rational(625, 3249)) == 0
      and S(sp.tanh(eta) - sp.sqrt(5)/3) == 0)
add('C62', 'C', 'Corollary 5.4(iv) (audit §7.1 witness; comparison row): the pure references m^(0) = (-sqrt5/3, 0, 2/3) (rapidity -eta) and m^(1) = (+sqrt5/3, 0, 2/3) = its passive return (exact) both have held-reference capacity |kappa_*| = 16/19 = 0.8421 > T_2 at the finite admissible angle cos2alpha = -3/5, with faithfulness margin 625/3249 > 0: a T_2-magnitude capacity at two consecutive passive returns is attained at a finite angle (not only as a supremum). Held-reference capacity witness; not a carrier-lifetime statement',
    ok, '16/19 exact; orbit step exact', comparison=True)

# C63 (audit F5): the excluded angles sin2alpha = 0 are not all the identity: alpha = pi gives U = ±I (identity channel); alpha = pi/2 gives U = -Z⊗Z,
#     i.e. the channel Ad_{J_E} on the carrier (M = diag(-1,-1,1), b = 0) for every reference and both chiralities
Hq_m = sp.kronecker_product(sx, K) - sp.kronecker_product(sy, Kp); Hq_m2 = sp.simplify(Hq_m*Hq_m)
Uexp = lambda Hx, Hx2, a_: sp.eye(4) + (sp.cos(2*a_) - 1)*Hx2/4 - sp.I*sp.sin(2*a_)*Hx/2
ok = True
for chir63, (Hx, Hx2) in ((1, (Hq, Hq2)), (-1, (Hq_m, Hq_m2))):
    Upi = sp.simplify(Uexp(Hx, Hx2, sp.pi)); Uh = sp.simplify(Uexp(Hx, Hx2, sp.pi/2))
    ok &= (Upi == sp.eye(4)) or (Upi == -sp.eye(4))
    ok &= sp.simplify(Uh + chir63*sp.kronecker_product(sz, sz)) == sp.zeros(4, 4)   # U = -chi Z⊗Z EXACTLY per chirality (v1.4, audit F5: the v1.3 row accepted either sign)
for chir in (1, -1):
    Mq, bq, _ = chan_frame((1, 0, 0), (0, 1, 0), chir)
    ok &= sp.simplify(Mq.subs(al, sp.pi/2)) == sp.diag(-1, -1, 1) and sp.simplify(bq.subs(al, sp.pi/2)) == sp.zeros(3, 1)
    ok &= sp.simplify(Mq.subs(al, sp.pi)) == sp.eye(3) and sp.simplify(bq.subs(al, sp.pi)) == sp.zeros(3, 1)
add('C63', 'C', 'Theorem 5.2(i) (audit F5): at the excluded angles sin2alpha = 0 the channel is the identity only for alpha = k pi (U = ±I, M = I, b = 0); for alpha = pi/2 + k pi, U = -chi Z⊗Z (the global phase is the chirality; checked per chirality in v1.4, audit F5 -- the manuscript text "U = -Z⊗Z" for both chiralities is withdrawn) and the channel is Ad_{J_E} on the carrier (M = diag(-1,-1,1), b = 0) for every reference and both chiralities (symbolic in m)',
    ok, 'symbolic in m; both chiralities; phase = chirality exact', universal=True)

# W64 (audit F6, comparison row): the rounded threshold "0.5391 < |w_K|" is not the exact boundary x(T_2): a = 0.53908 < 0.5391 with c = -0.99999 gives
#     kappa = 0.83538740... > T_2 (exact rational comparison); the exact condition is a > x(T_2) = 0.5390701239...
a64 = sp.Rational(13477, 25000); c64 = sp.Rational(-99999, 100000)
k64 = a64*(1 - c64)/(1 - a64**2*c64)
ok = bool(a64 < sp.Rational(5391, 10000)) and bool(k64 > T2_lock_q) and bool(mp.mpf('0.53908') > xT) and bool(mp.mpf(a64.p)/a64.q > xT)
add('W64', 'W', 'Theorem 5.9(iv) (audit F6; comparison row): a = 0.53908 < 0.5391 with cos2alpha = -0.99999 gives |kappa_inf| = ' + mp.nstr(mp.mpf(k64.p)/k64.q, 10) + ' > T_2 (exact rational comparison), so the rounded decimal 0.5391 is not an iff boundary; the exact statement is |w_K| > x(T_2) = ' + mp.nstr(xT, 12) + ' (and 0.53908 > x(T_2))',
    ok, f'a={a64}, c={c64}, kappa-T_2={float(k64 - T2_lock_q):.3e}', comparison=True)

# C65 (audit §6, Z-Spin specificity): for a general hyperbolic A_t = e^{eta_t K}, tr A_t = t > 2, cosh eta_t = t/2, the dephasing factor of the
#     canonical instrument is f_t = e^{-2 eta_t} = ((t - sqrt(t^2-4))/2)^2 and the whole §4 mechanism (K-dephasing, m_K conserved) holds verbatim;
#     t = 3 gives phi^-4. The trace-three value is the Z-Spin input; the mechanism is not specific to it.
t65 = sp.symbols('t', positive=True)
e65 = (t65 - sp.sqrt(t65**2 - 4))/2                       # candidate e^{-eta_t}
ok = sp.simplify(e65 + 1/e65 - t65) == 0                  # e + 1/e = t = 2 cosh eta_t, and e < 1 for t > 2: e = e^{-eta_t}
ok &= sp.simplify(e65**2 - ((t65 - sp.sqrt(t65**2 - 4))/2)**2) == 0
ok &= S(e65.subs(t65, 3)**2 - phi**-4) == 0 and S(e65.subs(t65, 3) - phi**-2) == 0
# general dephasing law: with A_t = (t/2) I + sqrt(t^2/4 - 1) K, E0 = A_t/||A_t||, E1 = sqrt(I - E0^2): m_K invariant, transverse multiplier e^{-2 eta_t} = e65^2
At = (t65/2)*I2 + sp.sqrt(t65**2/4 - 1)*K
lamA = t65/2 + sp.sqrt(t65**2/4 - 1)                      # ||A_t|| = e^{eta_t}
E0t = At/lamA; E1t = sp.sqrt(1 - e65**4)*(I2 - K)/2
ok &= sp.simplify(E0t*E0t + E1t*E1t - I2) == sp.zeros(2, 2)
Lt = sp.simplify(E0t*sig*E0t + E1t*sig*E1t)
ok &= sp.simplify(sp.trace(Lt*K) - mK) == 0 and sp.simplify(sp.trace(Lt*J) - e65**2*mJ) == 0 and sp.simplify(sp.trace(Lt*Kp) - e65**2*mKp) == 0
add('C65', 'C', 'Z-Spin specificity (v1.2 audit §6): for a general hyperbolic A_t = e^{eta_t K} with tr A_t = t > 2 the canonical instrument has E0 = A_t/e^{eta_t}, E1 = sqrt(1 - e^{-4eta_t}) P_-, and its unconditional channel is K-dephasing with m_K invariant and transverse factor f_t = e^{-2eta_t} = ((t - sqrt(t^2-4))/2)^2 (symbolic in t); t = 3 gives f_3 = phi^-4: the filtering/dephasing mechanism is general, the trace-three number is the Z-Spin input',
    ok, 'symbolic in t and m', universal=True)


# ================================================================ v1.4 rows (v1.3 audit response)
# W66 (audit F2; comparison row: uses locked T_2, M_*): the K10 envelope B(c) of Cor 7.1 / C61 is a statement about the SOLDERED resource-axis class
#     w = ±e_J, where the transducer coherence T_w equals the original odd coherence T = sqrt(m_K^2 + m_K'^2) (Thm 5.8(a): T_w = T iff w = ±e_J).
#     In the general Clifford-pair class the joint demand (T >= M_* and |kappa_*| = T_2 on one reference) is NOT excluded at c = 0 > c_crit:
#     (a) frame (e_K', e_J, e_K) (w = e_K), m = T_2 e_K, alpha = pi/4: T = T_2 > M_*, T_w = 0, direct 4x4 gives M = 0, kappa_* = -T_2 exactly, margin 1 - T_2^2 > 0,
#         and the reference is invariant under the unconditional return (A3'); B(0) = sqrt(1 - M_*^2) < T_2, so an UNQUALIFIED exclusion would deny this fixed point;
#     (b) the A-derived state sigma_2 = A^2/tr A^2 (C67) on the same frame has T = 3 sqrt5/7 > M_* and |kappa_*| = 3 sqrt5/7 > T_2.
Mx66, bx66, _ = chan_frame((0, 1, 0), (0, 0, 1), 1)
sub66 = {mK: T2_lock_q, mKp: 0, mJ: 0, al: sp.pi/4}
M66 = sp.simplify(Mx66.subs(sub66)); b66 = sp.simplify(bx66.subs(sub66))
r66 = sp.simplify((sp.eye(3) - M66).inv()*b66)
sigT66 = (I2 + T2_lock_q*K)/2
ok = (M66 == sp.zeros(3, 3) and r66[2] == -T2_lock_q and r66[0] == 0 and r66[1] == 0 and bool(T2_lock_q > Mstar_q)
      and sp.simplify(1 - (r66.T*r66)[0] - (1 - T2_lock_q**2)) == 0 and bool(1 - T2_lock_q**2 > 0)
      and S(E0*sigT66*E0 + E1*sigT66*E1 - sigT66) == sp.zeros(2, 2)
      and bool(mmax2_q < T2_lock_q**2) and ccrit < 0)                                             # B(0) < T_2 and c = 0 > c_crit
Tsq66 = mK**2 + mKp**2; Tw2_66 = (mK**2 + mKp**2 + mJ**2) - mK**2                                  # T^2 and T_w^2 for w = e_K
ok &= sp.simplify(Tsq66.subs({mK: T2_lock_q, mKp: 0}) - T2_lock_q**2) == 0 and sp.simplify(Tw2_66.subs({mK: T2_lock_q, mKp: 0, mJ: 0})) == 0
ok &= bool(sp.Rational(45, 49) > T2_lock_q**2) and bool(sp.Rational(45, 49) > Mstar_q**2)          # (b): tanh^2(2 eta) = 45/49
add('W66', 'W', 'Corollary 7.1 class scope (v1.3 audit F2; comparison row): the K10 envelope B(c) and the exclusion "iff c > c_crit" hold for the SOLDERED resource-axis class w = ±e_J (T_w = T); in the general Clifford-pair class the joint demand T >= M_* and |kappa_*| = T_2 on one reference is ATTAINED faithfully at c = 0 > c_crit: frame (e_K\', e_J, e_K), m = T_2 e_K, alpha = pi/4 gives T = T_2 > M_*, T_w = 0, M = 0, kappa_* = -T_2 exactly, margin 1 - T_2^2, reference return-invariant (A3\'), while B(0) = sqrt(1-M_*^2) < T_2; the A-derived sigma_2 (C67) on the same frame has T = 3sqrt5/7 > M_* and |kappa_*| = 3sqrt5/7 > T_2: the unqualified v1.3 statement is withdrawn',
    ok, f'r*={list(r66)}; T=T_2, T_w=0; B(0)^2={float(mmax2_q):.6f} < T_2^2={float(T2_lock_q**2):.6f}', comparison=True)

# C67 (audit F1): Lemma 3.3 (Tr f(A) J = 0) excludes a J-population of any function of A, NOT a longitudinal population or a longitudinal resource axis.
#     The A-derived family sigma_q = A^q/tr(A^q) = (I + tanh(q eta) K)/2 (q > 0; K = (2A - 3I)/sqrt5 is itself a function of A) has Tr(sigma_q J) = 0 and
#     m_K = tanh(q eta) != 0. On the frame (e_K', e_J, e_K) (w = e_K; the frame uses J) the held-reference fixed point is kappa_* = -chi tanh(q eta) for EVERY
#     admissible alpha (T_w = 0), faithful with margin sech^2(q eta); sigma_q is invariant under the unconditional return (A3') and NOT under the conditional one
#     (q -> q + 2). q = 2, chi = +1, alpha = pi/4: sigma_2 = (I + (3 sqrt5/7) K)/2, M = 0, b = (0,0,-3 sqrt5/7), margin 4/49 (one collision reaches the fixed point).
#     Formal witness only: no action selects the frame, the angle, the chirality, the instrument or the reference supply here.
qq = sp.symbols('q', positive=True); bq = sp.symbols('b_q', real=True)
Aq67 = sp.cosh(qq*eta)*I2 + sp.sinh(qq*eta)*K
sigq67 = sp.simplify(Aq67/sp.trace(Aq67))
ok = sp.simplify(sigq67 - (I2 + sp.tanh(qq*eta)*K)/2) == sp.zeros(2, 2)
ok &= S((2*A - 3*I2)/sp.sqrt(5) - K) == sp.zeros(2, 2)                                            # K = (2A - 3I)/sqrt5: a function of A
ok &= sp.simplify(sp.trace(sigq67*J)) == 0 and sp.simplify(sp.trace(sigq67*K) - sp.tanh(qq*eta)) == 0   # Lemma 3.3 holds; the K-population does not vanish
for chir67 in (1, -1):
    Mx67, bx67, _ = chan_frame((0, 1, 0), (0, 0, 1), chir67)
    Mx67 = Mx67.subs({mK: bq, mKp: 0, mJ: 0}); bx67 = bx67.subs({mK: bq, mKp: 0, mJ: 0})
    r67 = sp.simplify((sp.eye(3) - Mx67).inv()*bx67)
    ok &= sp.simplify(r67[2] + chir67*bq) == 0 and sp.simplify(r67[0]) == 0 and sp.simplify(r67[1]) == 0 and sp.simplify(1 - (r67.T*r67)[0] - (1 - bq**2)) == 0
    ok &= sp.simplify((sp.eye(3) - Mx67).det() - 2*sp.sin(2*al)**2*sp.sin(al)**2*(1 - sp.cos(2*al))) == 0   # unique iff sin2alpha != 0 (T_w = 0: D_w = 1 - c)
A2_67 = S(A*A); sig2_67 = S(A2_67/sp.trace(A2_67))
ok &= S(sig2_67 - (I2 + 3*sp.sqrt(5)/7*K)/2) == sp.zeros(2, 2) and S(sp.tanh(2*eta) - 3*sp.sqrt(5)/7) == 0 and S(sp.cosh(2*eta) - sp.Rational(7, 2)) == 0
Mx2, bx2, _ = chan_frame((0, 1, 0), (0, 0, 1), 1)
sub67 = {mK: 3*sp.sqrt(5)/7, mKp: 0, mJ: 0, al: sp.pi/4}
Mx2h, bx2h = sp.simplify(Mx2.subs(sub67)), sp.simplify(bx2.subs(sub67))
ok &= Mx2h == sp.zeros(3, 3) and sp.simplify(bx2h - sp.Matrix([0, 0, -3*sp.sqrt(5)/7])) == sp.zeros(3, 1) and sp.simplify(1 - (bx2h.T*bx2h)[0] - sp.Rational(4, 49)) == 0
sigb = (I2 + bq*K)/2
ok &= sp.simplify(S(E0*sigb*E0 + E1*sigb*E1) - sigb) == sp.zeros(2, 2)                              # unconditional return fixes every K-diagonal reference
o67 = S(A*sig2_67*A); ok &= S(o67/sp.trace(o67) - (I2 + sp.tanh(4*eta)*K)/2) == sp.zeros(2, 2) and S(sp.tanh(4*eta) - sp.tanh(2*eta)) != 0   # conditional return: q = 2 -> 4
add('C67', 'C', 'Corollary 5.12 (v1.3 audit F1): the A-derived longitudinal family sigma_q = A^q/tr(A^q) = (I + tanh(q eta) K)/2, q > 0, with K = (2A - 3I)/sqrt5 (both functions of A alone), satisfies Tr(sigma_q J) = 0 (Lemma 3.3) but has m_K = tanh(q eta) != 0; on the frame (e_K\', e_J, e_K) (w = e_K, T_w = 0) the held-reference fixed point is kappa_* = -chi tanh(q eta) for every admissible alpha with faithfulness margin sech^2(q eta) (symbolic in q, alpha, both chiralities); sigma_q is invariant under the unconditional return and moves to sigma_{q+2} under the conditional one; q = 2, chi = +1, alpha = pi/4: sigma_2 = (I + (3sqrt5/7)K)/2, M = 0, b = (0,0,-3sqrt5/7), margin 4/49 (one collision). Lemma 3.3 excludes a J-population of f(A) only; the v1.3 §6.7 line "must not be a function of A alone" is withdrawn. Formal witness, not an action selection',
    ok, 'symbolic in q (as b_q = tanh q eta), alpha; q = 2 instance exact', universal=True)

# C68 (audit F4): the conditional supremum sup_c |kappa_inf| = 2a/(1+a^2), a = |w_K|, is NOT attained only for 0 < a < 1; at a = 0 (k = 0) and a = 1 (k = 1)
#     it is attained at every admissible angle: the C48 gap a(1-a^2)(1+c)/((1+a^2)(1-a^2 c)) vanishes iff a in {0, 1} (for -1 < c < 1).
aa68 = sp.symbols('a', real=True)
k68 = aa68*(1 - cc)/(1 - aa68**2*cc); gap68 = 2*aa68/(1 + aa68**2) - k68
ok = sp.simplify(k68.subs(aa68, 0)) == 0 and sp.simplify(k68.subs(aa68, 1) - 1) == 0 and sp.simplify(gap68.subs(aa68, 0)) == 0 and sp.simplify(gap68.subs(aa68, 1)) == 0
ok &= sp.simplify(gap68 - aa68*(1 - aa68**2)*(1 + cc)/((1 + aa68**2)*(1 - aa68**2*cc))) == 0
ok &= sorted(sp.solve(sp.Eq(aa68*(1 - aa68**2), 0), aa68)) == [-1, 0, 1]
ok &= bool(gap68.subs({aa68: sp.Rational(1, 2), cc: sp.Rational(-1, 2)}) > 0)                       # interior: strictly positive
add('C68', 'C', 'Theorem 5.9(iv) endpoint attainment (v1.3 audit F4): sup_c |kappa_inf| = 2a/(1+a^2), a = |w_K|, is attained at a = 0 (value 0) and at a = 1 (value 1) at EVERY admissible angle -- the gap 2a/(1+a^2) - a(1-c)/(1-a^2 c) = a(1-a^2)(1+c)/((1+a^2)(1-a^2 c)) vanishes iff a in {0,1}; "the supremum is not attained" requires 0 < |w_K| < 1 (the v1.3 §2.3 firewall row and abstract omitted the qualifier; withdrawn) (symbolic in c)',
    ok, 'symbolic in c; gap zero iff a in {0,1}', universal=True)


# ================================================================ v1.4.1 rows (v1.4 audit response)
# W69 (audit F1; comparison row: uses locked M_*, T_2): the ANGLE-FREE K10 ceiling 2 sqrt(1-M_*^2)/(2-M_*^2) = 0.9115647535978405...
#     is a SOLDERED-class statement.  In the general Clifford-pair class take the proper frame (e_K', e_J, e_K) (w = e_K) and the
#     longitudinal reference m = p e_K with any p in [M_*, 1): then T^2 = p^2 >= M_*^2 (the M60 floor holds), T_w = 0, and the direct
#     4x4 partial trace gives M = diag(c, c, c^2), b = (0,0,-chi p (1-c^2)), hence the unique fixed point (0,0,-chi p) with
#     |kappa_*| = p and margin 1 - p^2 > 0 at EVERY admissible angle.  So the general-class supremum under the floor is 1 (unattained),
#     not 0.9116.  The A-derived state of Cor 5.12 at q = 2 supplies p = tanh(2 eta) = 3 sqrt5/7 with 45/49 > ceiling^2 exactly --
#     a target-independent instance (W66 is the p = T_2 instance, and T_2 itself lies BELOW the ceiling, so W66 alone does not break it).
pfree = sp.symbols('p_free', positive=True)
Mw69, bw69, _ = chan_frame((0, 1, 0), (0, 0, 1), 1)
Mw69 = sp.simplify(Mw69.subs({mK: pfree, mKp: 0, mJ: 0})); bw69 = sp.simplify(bw69.subs({mK: pfree, mKp: 0, mJ: 0}))
rw69 = sp.simplify((sp.eye(3) - Mw69).inv()*bw69)
ok = (sp.simplify(Mw69 - sp.diag(sp.cos(2*al), sp.cos(2*al), sp.cos(2*al)**2)) == sp.zeros(3, 3)
      and sp.simplify(bw69 - sp.Matrix([0, 0, -pfree*(1 - sp.cos(2*al)**2)])) == sp.zeros(3, 1)
      and sp.simplify(rw69[2] + pfree) == 0 and sp.simplify(rw69[0]) == 0 and sp.simplify(rw69[1]) == 0
      and sp.simplify(1 - (rw69.T*rw69)[0] - (1 - pfree**2)) == 0)
ceil2_q = 4*(1 - Mstar_q**2)/(2 - Mstar_q**2)**2                                    # the angle-free ceiling, squared, exact rational
b2_69 = 3*sp.sqrt(5)/7                                                              # tanh(2 eta) = the q = 2 population of Cor 5.12
ok &= S(sp.tanh(2*eta) - b2_69) == 0 and bool(sp.Rational(45, 49) > ceil2_q) and bool(sp.Rational(45, 49) > Mstar_q**2)
ok &= bool(T2_lock_q**2 < ceil2_q) and bool(T2_lock_q > Mstar_q)                    # T_2 is BELOW the ceiling: W66 is a different counterexample
ok &= bool(sp.Rational(999, 1000)**2 > ceil2_q) and bool(1 - sp.Rational(999, 1000)**2 > 0) and bool(sp.Rational(999, 1000) > Mstar_q)
sig69 = (I2 + b2_69*K)/2
ok &= S(E0*sig69*E0 + E1*sig69*E1 - sig69) == sp.zeros(2, 2)                        # the A-derived reference is return-invariant (A3')
add('W69', 'W', 'Corollary 7.1 angle-free ceiling, class scope (audit v1.4 F1; comparison row): for w = e_K and m = p e_K with any p in [M_*,1) the M60 floor T = p >= M_* holds, T_w = 0, and the unique held-reference fixed point is |kappa_*| = p with margin 1-p^2 > 0 at EVERY admissible angle (symbolic in p and alpha); hence over the general Clifford-pair class the supremum under the floor is 1 (unattained) and the angle-free ceiling 2sqrt(1-M_*^2)/(2-M_*^2) = 0.91156475... is valid only in the soldered class w = +-e_J. Target-independent instance: the A-derived p = tanh(2eta) = 3sqrt5/7 of Cor 5.12 has 45/49 > ceiling^2 exactly, and its reference is return-invariant. Note T_2 < ceiling, so W66 (p = T_2) breaks the fixed-angle exclusion, not this ceiling',
    ok, f'ceiling^2={float(ceil2_q):.12f} < 45/49={float(sp.Rational(45,49)):.12f}; T_2^2={float(T2_lock_q**2):.12f} < ceiling^2', comparison=True)

# C70 (audit F3): T_w = T is an identity of FUNCTIONALS on all reference states iff w = +-e_J.  T^2 - T_w^2 = m_J^2 - (m.w)^2 is a
#     quadratic form in m; it vanishes identically iff w w^T = e_J e_J^T, i.e. (with |w| = 1) iff w = +-e_J.  At a SINGLE state the
#     equality can hold off that axis: m = (1/2, 0, 1/2) (full rank) with w = e_K has T^2 = T_w^2 = 1/4.
m1_, m2_, m3_, w1_, w2_, w3_ = sp.symbols('m_1 m_2 m_3 w_1 w_2 w_3', real=True)
Qform = m3_**2 - (m1_*w1_ + m2_*w2_ + m3_*w3_)**2
Qpoly = sp.Poly(sp.expand(Qform), m1_, m2_, m3_)
coeff_sys = [sp.expand(cf) for cf in Qpoly.coeffs()]
sols = sp.solve(coeff_sys, [w1_, w2_, w3_], dict=True)
ok = len(sols) > 0 and all(sp.simplify(s.get(w1_, 0)) == 0 and sp.simplify(s.get(w2_, 0)) == 0 for s in sols)
ok &= sp.simplify(Qform.subs({w1_: 0, w2_: 0, w3_: 1})) == 0 and sp.simplify(Qform.subs({w1_: 0, w2_: 0, w3_: -1})) == 0
ok &= sp.simplify(Qform.subs({m1_: 0, m2_: 0, m3_: 1, w1_: 1, w2_: 0, w3_: 0})) == 1        # generic m: the functionals differ off the axis
ok &= sp.simplify(Qform.subs({m1_: sp.Rational(1, 2), m2_: 0, m3_: sp.Rational(1, 2), w1_: 1, w2_: 0, w3_: 0})) == 0   # pointwise coincidence off the axis
ok &= bool(sp.Rational(1, 4) + sp.Rational(1, 4) < 1)                                        # that state is full rank (|m| < 1), not a degenerate instance
add('C70', 'C', 'Type firewall T vs T_w (audit v1.4 F3): T^2 - T_w^2 = m_J^2 - (m.w)^2 vanishes for EVERY reference iff w w^T = e_J e_J^T, i.e. (|w| = 1) iff w = +-e_J -- the "T_w = T iff w = +-e_J" statement is an identity of FUNCTIONALS, solved here from the coefficients of the quadratic form (symbolic in m and w). At a single reference the equality can hold off that axis: the full-rank m = (1/2,0,1/2) with w = e_K has T^2 = T_w^2 = 1/4, while a generic m (e.g. e_J) separates them. The class condition of Cor 7.1 is unchanged',
    ok, 'symbolic in m, w; pointwise counterexample exact', universal=True)

# ---------------------------------------------------------------- guards / declarations
src = open(__file__, encoding='utf-8').read()
bad = [r_['id'] for r_ in rows if (not r_['comparison']) and any(tok in r_['claim'] + r_['detail'] for tok in ('T_2', 'M_*', '0.8353', '0.7633'))]
add('G40', 'G', 'target-blindness (row typing only; not a data-flow certificate): no non-comparison row mentions T_2, M_* or their digits; comparison rows are exactly C19, C20, C61, C62, V57, W64, W66, W69',
    bad == [] and sorted(r_['id'] for r_ in rows if r_['comparison']) == ['C19', 'C20', 'C61', 'C62', 'V57', 'W64', 'W66', 'W69'], f'offending={bad}')
# G69 (v1.4.1; audit v1.4 F2): numeric purity of the C rows, checked mechanically instead of asserted in prose.
#     The v1.3 audit removed a numerical OR from C32 and the manuscript then declared "no C row decides a PASS numerically";
#     the v1.4 audit found that C34 and C61 still did (AND conjuncts). Prose declarations failed twice, so the property is now a row.
#     Kill condition: a C-class row whose PASS decision (any line assigning to `ok` inside that row's block, or the ok-argument of its
#     add(...) call) contains sp.N / float( / mp.mpf( / np. / abs( / 1e- / evalf. Display-only uses (mp.nstr in claim or detail strings,
#     f-strings) are NOT part of the PASS decision and are not flagged.
import ast as _ast
def _numeric_pass_clauses(source):
    tree = _ast.parse(source); lines = source.split('\n')
    calls = sorted([n for n in _ast.walk(tree) if isinstance(n, _ast.Call) and getattr(n.func, 'id', '') == 'add'], key=lambda n: n.lineno)
    toks = ('sp.N(', 'float(', 'mp.mpf(', 'np.', 'abs(', '1e-', 'evalf')
    out, prev = {}, 0
    for n in calls:
        rid, cls, prev_end = n.args[0].value, n.args[1].value, prev
        prev = n.end_lineno
        if cls != 'C':
            continue
        okexpr = _ast.get_source_segment(source, n.args[3]) or ''
        bad = [L.strip() for L in lines[prev_end:n.end_lineno]
               if _re2.match(r'\s*ok\s*(&=|=)', L.split('#', 1)[0]) and any(tk in L.split('#', 1)[0] for tk in toks)]
        if any(tk in okexpr for tk in toks):
            bad.append('add-arg: ' + okexpr.strip()[:80])
        if bad:
            out[rid] = bad
    return out
import re as _re2
_impure = _numeric_pass_clauses(open(__file__, encoding='utf-8').read())
add('G69', 'G', 'numeric purity of the C rows (v1.4.1; audit v1.4 F2): no C-class row of THIS script decides its PASS with a floating-point or tolerance term -- the guard re-parses this file, isolates each C row block and the ok-argument of its add() call, and fails if any line feeding `ok` contains sp.N/float(/mp.mpf(/np./abs(/1e-/evalf. Display-only formatting (mp.nstr in claim and detail strings) is not part of the PASS decision and is not flagged. This replaces the prose declaration that was false in v1.3 (C32) and again in v1.4 (C34, C61)',
    _impure == {}, f'impure C rows: {sorted(_impure) if _impure else "none"}')

add('G41', 'G', 'script-internal consistency: SCRIPT == zs_m68_verify_v1_4_1.py and PAPER == ZS-M68 v1.4.1 (this row checks the script only; the manuscript cross-check is G42)',
    SCRIPT == 'zs_m68_verify_v1_4_1.py' and PAPER == 'ZS-M68 v1.4.1', SCRIPT)
# G42: real manuscript cross-check. Path = first non-flag argv or ZS-M68_v1_4_1.md next to the script. SKIP (not PASS) when absent.
#      v1.3/v1.4 scope (audit §5.2 of v1.2): checks (1) code/version tokens, (2) script name, (3) declared row count = ledger rows, (4) no live stale
#      version banner or stale run command (v1.0/v1.1/v1.2/v1.3 tokens on the banner/run lines), (5) the banner census line equals the class census
#      of THIS ledger. It does NOT check hashes (the banner hashes are injected after the run; make_manifest_v1_4_1.py --check verifies them).
_args = [a_ for a_ in sys.argv[1:] if not a_.startswith('--')]
STRICT = '--strict' in sys.argv[1:]
mpath = _args[0] if _args else os.path.join(HERE, 'ZS-M68_v1_4_1.md')
if os.path.exists(mpath):
    mtxt = open(mpath, encoding='utf-8').read()
    import re as _re
    n_rows_declared = None
    mm_ = _re.search(r'zs_m68_verify_v1_4_1\.py · rows=(\d+)', mtxt)
    if mm_: n_rows_declared = int(mm_.group(1))
    stale_tokens = ('VERSION: v1.0 ·', 'VERSION: v1.1 ·', 'VERSION: v1.2 ·', 'VERSION: v1.3 ·', 'VERSION: v1.4 ·', 'zs_m68_verify_v1_1.py · rows=', 'zs_m68_verify_v1_2.py · rows=',
                    'zs_m68_verify_v1_3.py · rows=', 'zs_m68_verify_v1_4.py · rows=', 'python3 zs_m68_verify_v1_1.py', 'python3 zs_m68_verify_v1_2.py',
                    'python3 zs_m68_verify_v1_3.py', 'python3 zs_m68_verify_v1_4.py ')
    stale = [tk for tk in stale_tokens if tk in mtxt]
    run_ok = 'python3 zs_m68_verify_v1_4_1.py [ZS-M68_v1_4_1.md] [--strict]' in mtxt
    # census line: the classes of the rows so far plus this row (G) and the declaration row (D)
    cens_ = {}
    for r_ in rows: cens_[r_['class']] = cens_.get(r_['class'], 0) + 1
    cens_['G'] = cens_.get('G', 0) + 1; cens_['D'] = cens_.get('D', 0) + 1
    univ_ = sum(r_['universal'] for r_ in rows)
    cm_ = _re.search(r'Evidence-bearing: P=(\d+), C=(\d+) \(symbolic-universal (\d+)\), V=(\d+), W=(\d+)', mtxt)
    gm_ = _re.search(r'Controls:\s+G=(\d+)', mtxt); dm_ = _re.search(r'Non-evidence:\s+D=(\d+)', mtxt)
    census_ok = bool(cm_ and gm_ and dm_) and (int(cm_.group(2)), int(cm_.group(3)), int(cm_.group(4)), int(cm_.group(5)), int(gm_.group(1)), int(dm_.group(1)), int(cm_.group(1))) == \
                (cens_.get('C', 0), univ_, cens_.get('V', 0), cens_.get('W', 0), cens_.get('G', 0), cens_.get('D', 0), 0)
    g42 = ('PAPER CODE: ZS-M68' in mtxt and 'VERSION: v1.4.1' in mtxt and 'zs_m68_verify_v1_4_1.py' in mtxt
           and n_rows_declared == len(rows) + 2 and stale == [] and run_ok and census_ok)      # +2: this row and the declaration row that follow
    add('G42', 'G', 'manuscript cross-check (scope: tokens, script name, row count, stale banner/run-command tokens, banner census = ledger census; NOT hashes): the manuscript file exists, carries PAPER CODE ZS-M68 / VERSION v1.4.1, names this script and its one-command run line, declares the same row count and the same class census as this ledger, and carries no live stale version/run token of v1.0-v1.4',
        g42, f'path={os.path.basename(mpath)}, declared_rows={n_rows_declared}, ledger_rows={len(rows)+2}, stale={stale}, run_line={run_ok}, census_match={census_ok}')
else:
    add('G42', 'G', 'manuscript cross-check: SKIPPED because no manuscript file was found (pass its path as argv[1]); a SKIP is not a PASS and is reported in the census',
        None, f'path={mpath} (absent)')
add('D43', 'D', 'declaration: P=0 (no executable row is a written proof); universal=True rows are symbolic over the free parameters named in the claim and nothing more (e.g. C09 checks N=2,3 and the pure orbit, C12 a three-level environment, C34 the norm identity); W/V rows are instances; the written halves of Theorems 6.5/6.6 (unital non-expansion), 5.8(a) (SU(2) covariance for a general rotation), Lemma 5.10(b) (perturbation argument in an adapted norm; W59 shows this is not one-step Euclidean contractivity) and Lemma 8.1(vii) (kernel-diagonal regulators) are in the manuscript; the seed verifier (41 rows) and the K12 suite (8 rows) are NOT INVOKED by this script (a separate 8/8 run in the v1.0 session is reported by the manuscript, not certified here) and are cited by hash',
    True, f"python {platform.python_version()}, sympy {sp.__version__}, numpy {np.__version__}, mpmath {mp.__version__}")

census = {}
for r_ in rows: census[r_['class']] = census.get(r_['class'], 0) + 1
summary = {'rows': len(rows), 'pass': sum(r_['result'] == 'PASS' for r_ in rows), 'fail': sum(r_['result'] == 'FAIL' for r_ in rows),
           'skip': sum(r_['result'] == 'SKIP' for r_ in rows),
           'census': census, 'universal_rows': sum(r_['universal'] for r_ in rows), 'P': 0}
out = {'artifact': SCRIPT, 'paper': PAPER, 'rows': rows, 'summary': summary,
       'script_sha256': hashlib.sha256(src.encode('utf-8')).hexdigest()}
with open(os.path.join(HERE, 'zs_m68_verify_v1_4_1.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
for r_ in rows: print(r_['id'], r_['class'], r_['result'], '|', r_['claim'][:110])
print('CENSUS rows=%d PASS=%d FAIL=%d SKIP=%d | evidence C=%d V=%d W=%d P=%d | controls G=%d | non-evidence D=%d | universal=%d | comparison=%s | strict=%s' % (
    summary['rows'], summary['pass'], summary['fail'], summary['skip'], census.get('C', 0), census.get('V', 0), census.get('W', 0), 0,
    census.get('G', 0), census.get('D', 0), summary['universal_rows'], sorted(r_['id'] for r_ in rows if r_['comparison']), STRICT))
print(summary)
sys.exit(0 if (summary['fail'] == 0 and (summary['skip'] == 0 or not STRICT)) else 1)
