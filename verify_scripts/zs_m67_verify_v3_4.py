#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZS-M67 v3.4 -- artifact L (Section 22, third audit-integration pass + the linear-order coherent-channel section 22.11).
Does NOT replace artifacts A-F; all remain in force.  SUPERSEDES artifact K (zs_m67_verify_v3_3.py, 48 rows) in full:
every K row is carried, retyped or replaced here.  The provenance baseline (artifact K's 48 row fingerprints, taken
from the SHIPPED v3.3 ledger) is EMBEDDED, so G18 measures provenance from the core files alone; if
zs_m67_verify_v3_3.json is also present it is cross-checked.

What v3.4 changes (the v3.3 audit, AUDIT-MAJOR-REVISION: central contribution SURVIVES, three S2, release-blocking;
accepted in full) and what this block certifies:

  S2-1 sect.25   the v2.6-vintage sentence "the remaining object is completely specified -- an action-derived ... CPTP map
                 with a unique faithful stationary state ... all now derived" read as a construction.  REPLACED: the
                 SIGNATURE of the missing object is specified; no such map or state-selection mechanism is constructed
                 (D40; guard G20 rule (iv); CLAIM-STATE MissingObject=SPECIFIED-NOT-CONSTRUCTED).
  S2-2 sect.22.9 the thermal ceiling |kappa| <= tanh(Delta/2T) is TARGET-INDEPENDENT; the number T/Delta <= 0.4147 is
                 TARGET-CONDITIONED (it uses |kappa| = T_2).  "first target-blind constraint" WITHDRAWN.  The same split
                 is written for Theorem 36: the functional form G_4 m^2 >= pi kappa/(2 c' sin thetabar (1 - kappa)) is
                 general; the x42 verdict is conditioned on (T_2, thetabar_*).  V32 retyped; CLAIM-STATE tokens added.
  S2-3 sect.27   the manuscript declared a four-file core INCLUDING the session file while the generated manifest
                 registered three objects and no session.  REPAIRED: authoritative core = manuscript, verifier, ledger,
                 release manifest (VERIFY sect.9.1); session, audit report and provenance supplement are registered as
                 provenance objects with measured hashes; G25 (new) reads the manuscript's package block and FAILS if the
                 declared core differs from the manifest's core.
  Elitzur        Thm 39.4 now carries the primary citation (Elitzur, Phys. Rev. D 12, 3978 (1975), read at abstract level
                 this session) and two explicit hypotheses: gauge-invariant POSITIVE measure; the boundary condition and
                 measure preserve the local colour/electromagnetic gauge symmetry (no boundary gauge reduction, no dressed
                 non-local order parameter).  C96 retyped.
  G21            exit_code([]) was 0; an empty ledger is now DEGRADED (exit 2).  Synthetic set extended: {} -> 2.
  W15/W16 (self) found beyond the audit: W15's claim text embedded a run-dependent 1e-16 residual, so its fingerprint
                 differed between the shipped run and a re-run on another machine (python 3.12 / numpy 2.4.4: 1.6e-16 vs
                 1.7e-16), silently moving G18's carried count.  Retyped: the claim states the threshold; the measured
                 value lives in the detail field (VERIFY N4, sect.9.2).  A lineage rescan for the same defect type found ONE
                 more instance, W16's 'min eig(G) = %.1e' (a numpy eigenvalue residual), retyped the same way.
  sect.22.11     NEW (research addition, kept separate from the correction pass; MANUSCRIPT sect.16 major revision):
                 C100 record composition (the flavour-blind J_E sees only the diagonal density blocks; the audit family's
                 record is kappa for every r), C101 the coherent channel's normal overlap is the HARMONIC MEAN
                 2 k1 k2/(k1 + k2) of the two edge localisation rates, ratio omega = 2 sqrt(m1 m2)/(m1 + m2) <= 1 to the
                 geometric mean (equality iff m1 = m2), C102 pair-channel decoupling: about ANY flavour-diagonal
                 reference state the linearised d-channel kernel is delta_jk delta_il-supported (flavour number), so the
                 coherent (tc) channel closes on itself and the flavour matrix D of Prop. 39.6 does not enter its onset.
                 Consequence: C99d (lambda_max(D) is the coherent critical coupling) is CLOSED-NEGATIVE at linear order
                 (D39); C99e stays OPEN, reformulated as ONE computation (Proof obligation 39.8', D39).  K9b stays OPEN.
  prior art      D41: Blasone-Jizba-Mavromatos-Smaldone, arXiv:1807.07616 (primary PDF read): flavour-off-diagonal
                 condensates are the signature of dynamically generated mixing in bulk two-flavour chiral models ->
                 the OBJECT of K9b is IMPORTED; the boundary-carrier question is NOT_FOUND in one query family:
                 OPEN-NOVELTY (narrowed).  Prop. 39.6 algebra: SPECIALIZED.

Evidence classes: C exact | V numeric | W witness | R control | G guard | D declaration | P proof.
This ledger: P = 0.  A PASS row is not a theorem.

run:  python3 zs_m67_verify_v3_4.py     (exit 0 iff FAIL == 0 and DEGRADED == 0; exit 1 if FAIL > 0; exit 2 if
                                          DEGRADED > 0 or the ledger is empty; expects ZS-M67_v3_4.md (or *M67_v3_4.md)
                                          beside it; the v3.3 ledger is OPTIONAL (cross-checked if present); paths
                                          overridable by ZS_M67_PAPER, ZS_M67_PREV_LEDGER)
"""
import hashlib, json, os, re, sys
import sympy as sp
import mpmath as mp
import numpy as np

mp.mp.dps = 60
SEED = 20260902
HERE = os.path.dirname(os.path.abspath(__file__))
SELF = os.path.abspath(__file__)
import glob
def _find_paper():
    p = os.environ.get("ZS_M67_PAPER")
    if p: return p
    cands = sorted(glob.glob(os.path.join(HERE, "ZS-M67_v3_4.md"))) or sorted(glob.glob(os.path.join(HERE, "*M67_v3_4.md")))
    return cands[0] if cands else os.path.join(HERE, "ZS-M67_v3_4.md")
PAPER = _find_paper()
PREV_LEDGER = os.environ.get("ZS_M67_PREV_LEDGER", os.path.join(HERE, "zs_m67_verify_v3_3.json"))

BASELINE_LEDGER = "zs_m67_verify_v3_3.json"   # artifact K; sha256 of the SHIPPED file: f5f577f0d43dc6e8fe8e067cc186d2d55fdea1daeaf29bb6e2515b0e5fb10020
BASELINE_FP = {   # id: (class, sha256(claim.strip())[:16]) of every artifact-K row -- EMBEDDED so that G18 measures provenance without the JSON
    "C85": ("C", "9b17e9a39e861b51"),
    "C86": ("C", "8b0c33f16c243574"),
    "C87": ("C", "1bdfb61bcebeff5b"),
    "C88": ("G", "6624ed883eb49151"),
    "C89": ("C", "e9926cb441deb361"),
    "C90": ("C", "8a4d230eda8be8db"),
    "C91": ("C", "ce85fa0673bfe731"),
    "C92": ("C", "ee1fbd93b384c80e"),
    "C93": ("C", "bd3ec9115fe8355f"),
    "C94": ("C", "1e35766b6f5589b9"),
    "C95": ("C", "caec453fd41f4194"),
    "C96": ("C", "f44fe6d1f74cac96"),
    "C97": ("C", "d114961564ba8d43"),
    "C98": ("C", "9f4d5b764a5d56f2"),
    "C99a": ("C", "3628c4ee824f8753"),
    "C99b": ("C", "25e5e1167bc49447"),
    "C99c": ("C", "9a7c0e1f6fe86e3d"),
    "D27": ("D", "44ef28ee77da1ff4"),
    "D28": ("D", "a683bbf7ddbe222e"),
    "D29": ("D", "eedf299812158e3e"),
    "D30": ("D", "43e6d60c22bd4c88"),
    "D31": ("D", "26f8bc4406864fa8"),
    "D32": ("D", "0ae12688b1c6ce58"),
    "D33": ("D", "a827e7e8117c03fd"),
    "D34": ("D", "33148e9d11a9f330"),
    "D35": ("D", "8f7d07a951d28c10"),
    "D36": ("D", "f76ba3367e49ee5f"),
    "D38": ("D", "f5d74a2b28b4ac76"),
    "G15": ("G", "b3c3f56f8f91dea0"),
    "G16": ("G", "68511aa7533866dd"),
    "G17": ("G", "bbf72994a3971178"),
    "G18": ("G", "187743554e7f875a"),
    "G19": ("G", "1a99ced0ed85ffa5"),
    "G20": ("G", "4519a85aa722c7a9"),
    "G21": ("G", "70e765567036d9ec"),
    "G22": ("G", "80708b482ee50f23"),
    "G23": ("G", "afb5516b45ffc0f6"),
    "G24": ("G", "8a7e4927b845a499"),
    "R16": ("R", "c335cdccf4b11f18"),
    "V27": ("V", "3a79db2ff3889b42"),
    "V28": ("V", "1682642b10631930"),
    "V30": ("V", "d63a080eb5513fb6"),
    "V31": ("V", "0ee8f8f751160015"),
    "V32": ("V", "779f8022bd2fa44f"),
    "V33": ("V", "0a0289fd73b7082b"),
    "W14": ("W", "16e53fce466bf484"),
    "W15": ("W", "447e9bbb315c4271"),
    "W16": ("W", "c1df16b4629f208a"),
}


ROWS = []
def row(rid, cls, claim, ok, detail="", universal=False, degraded=False):
    ROWS.append({"id": rid, "class": cls, "claim": claim,
                 "result": "DEGRADED" if degraded else ("PASS" if ok else "FAIL"),
                 "universal": bool(universal), "detail": str(detail)[:900]})
    return ok

# ----------------------------------------------------------------------------
I2, Z2 = sp.eye(2), sp.zeros(2)
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
blk = lambda A, B, Cc_, D: sp.Matrix(sp.BlockMatrix([[A, B], [Cc_, D]]))
g0 = blk(I2, Z2, Z2, -I2); g1 = blk(Z2, s1, -s1, Z2); g2 = blk(Z2, s2, -s2, Z2); g3 = blk(Z2, s3, -s3, Z2)
g5 = sp.I * g0 * g1 * g2 * g3
N = g0 * g3
gam = [g0, g1, g2, g3]
r2 = 1 / sp.sqrt(2)
Vp = sp.Matrix.hstack(r2 * sp.Matrix([0, 1, 0, -1]), r2 * sp.Matrix([1, 0, 1, 0]))
Vm = sp.Matrix.hstack(r2 * sp.Matrix([0, 1, 0, 1]), r2 * sp.Matrix([1, 0, -1, 0]))
JE = sp.simplify(Vp.H * g5 * Vp)                      # diag(-1, +1)
th = sp.Symbol('theta', real=True)
Wg = sp.I * sp.diag(sp.cos(th) + sp.I * sp.sin(th), sp.cos(th) - sp.I * sp.sin(th))
Psi = sp.simplify(Vp + Vm * Wg)                        # 4x2 basis of L_theta (Thm 14.1 / C41)
def z(M):     return sp.simplify(sp.expand_trig(sp.simplify(M))) == sp.zeros(*M.shape)
SX, SY = s1, s2
Xth = -sp.sin(th) * SX + sp.cos(th) * SY               # Theorem 21's boost generator X_theta
Yth = sp.cos(th) * SX + sp.sin(th) * SY

# ============================================================================
# C85  HORN A -- retyped/strengthened: stationary set AND the extremum type
# ============================================================================
mm_ = sp.Symbol('m', positive=True); tb = sp.Symbol('thetabar', real=True); Aa = sp.Symbol('A', real=True)
Gp, Gpp = sp.Symbol('Gp', positive=True), sp.Symbol('Gpp', real=True)     # Gamma'(A) > 0 is C54/C93's fact
Gam = sp.Function('Gamma')
Ath = mm_ * sp.cos(tb)
d1 = sp.diff(Gam(Aa), Aa).subs(Aa, Ath) * sp.diff(Ath, tb)
d2 = sp.diff(Gam(Aa), Aa, 2).subs(Aa, Ath) * sp.diff(Ath, tb)**2 + sp.diff(Gam(Aa), Aa).subs(Aa, Ath) * sp.diff(Ath, tb, 2)
d1s = d1.subs({sp.Derivative(Gam(Aa), Aa).subs(Aa, Ath): Gp})
d2s = d2.subs({sp.Derivative(Gam(Aa), (Aa, 2)).subs(Aa, Ath): Gpp}).subs({sp.Derivative(Gam(Aa), Aa).subs(Aa, Ath): Gp})
chain_ok = sp.simplify(d1s + mm_ * sp.sin(tb) * Gp) == 0
stat = set(sp.solve(sp.Eq(sp.sin(tb), 0), tb))
min_pi = sp.simplify(d2s.subs(tb, sp.pi)) == Gp * mm_          # > 0 : minimum
max_0 = sp.simplify(d2s.subs(tb, 0)) == -Gp * mm_              # < 0 : maximum
row("C85", "C", "HORN A (Phi_Z = Phi, ZS-S14 sect.10.3.5): with thetabar a DYNAMICAL FIELD whose potential is the "
    "boundary effective action Gamma(A), A = m cos(thetabar) (Thm 13), the chain rule gives dGamma/dthetabar = "
    "-m sin(thetabar) Gamma'(A); given Gamma'(A) > 0 (C54, and C93 below) the stationary set on [0, 2pi) is "
    "EXACTLY {0, pi}, and d^2Gamma/dthetabar^2 = -m cos(thetabar) Gamma' + m^2 sin^2(thetabar) Gamma'' equals "
    "+m Gamma' > 0 at pi and -m Gamma' < 0 at 0: thetabar = pi is the unique MINIMUM, 0 the maximum. Making the "
    "angle dynamical drives it to pi -- the point Shapiro-Lopatinski excludes (Thm 22), where the surface gap "
    "closes (Thm 15) and kappa = 0 (Thm 23). Scope: mean field, A5 (D29)",
    chain_ok and stat == {0, sp.pi} and min_pi and max_0,
    "stationary = {0, pi}; d2 at pi = +m Gamma'; d2 at 0 = -m Gamma'", universal=True)

# ============================================================================
# C93  the positivity of Gamma' everywhere: exact product identity
# ============================================================================
pp, Cc, Ss = sp.symbols('p C S', real=True)
kap_p = sp.sqrt(pp**2 + mm_**2)
prod_id = sp.expand((kap_p + mm_ * Cc) * (kap_p - mm_ * Cc) - (pp**2 + mm_**2 * Ss**2))
prod_ok = sp.simplify(prod_id.subs(Ss**2, 1 - Cc**2)) == 0
row("C93", "C", "GAMMA' > 0 EVERYWHERE (repair of the one-point check of v2.9's C85): modulo C^2 + S^2 = 1, "
    "(kappa(p) + A)(kappa(p) - A) = p^2 + m^2 sin^2(thetabar) EXACTLY, with kappa(p) - A >= kappa(p) - m >= 0; "
    "hence the integrand 1/(kappa(p)+A) of Gamma'(A) is strictly positive for every p except the single point "
    "p = 0, thetabar = pi, so Gamma'(A) > 0 on [-m, m] and Gamma is strictly increasing in A",
    prod_ok, "(kappa+A)(kappa-A) - (p^2 + m^2 S^2) == 0 mod (C^2+S^2-1)", universal=True)

# ============================================================================
# C89  the Noether currents of the Goldstone shift and their divergences ON SHELL
# ============================================================================
tmm = sp.Symbol('theta_m', real=True)
E5 = sp.cos(tmm) * sp.eye(4) + sp.I * sp.sin(tmm) * g5
pv = sp.Matrix(sp.symbols('p0:4')); pc = sp.Matrix(sp.symbols('q0:4'))
dv = [sp.Matrix(sp.symbols('d%d_0:4' % mu)) for mu in range(4)]
dc = [sp.Matrix(sp.symbols('e%d_0:4' % mu)) for mu in range(4)]
d0 = g0 * (-sp.I * mm_ * E5 * pv - sum((gam[k] * dv[k] for k in (1, 2, 3)), sp.zeros(4, 1)))
dc0 = (sp.I * mm_ * pc.T * E5.H + sum((dc[k].T * gam[k] for k in (1, 2, 3)), sp.zeros(1, 4))) * g0
Dv = [d0, dv[1], dv[2], dv[3]]; Dc = [dc0, dc[1].T, dc[2].T, dc[3].T]
def div(M):
    tot = sp.zeros(1, 1)
    for mu in range(4):
        tot += Dc[mu] * g0 * gam[mu] * M * pv + pc.T * g0 * gam[mu] * M * Dv[mu]
    return sp.expand(tot[0])
divV = sp.simplify(div(sp.eye(4)))
divA = sp.simplify(div(g5) - sp.expand((2 * sp.I * mm_ * pc.T * g0 * g5 * E5 * pv)[0]))
row("C89", "C", "GOLDSTONE NOETHER CURRENTS, DERIVED AND DIFFERENTIATED ON SHELL (the object C86 never built): "
    "with psi obeying i gamma^mu d_mu psi = m e^{i theta_m gamma5} psi and its adjoint, over free symbols for the "
    "components of psi, psi^dagger and their derivatives, d_mu(psibar gamma^mu psi) == 0 IDENTICALLY (vector shift: "
    "exactly conserved for every m, theta_m), while d_mu(psibar gamma^mu gamma5 psi) == 2 i m psibar gamma5 "
    "e^{i theta_m gamma5} psi (axial shift: NOT conserved for m != 0). A vector-charged Goldstone's linear coupling "
    "d_mu theta J_V^mu is therefore a total derivative; an axial-charged one's is not",
    divV == 0 and divA == 0, "div J_V = 0 ; div J_A - 2 i m psibar g5 e^{i tm g5} psi = 0", universal=True)

# ============================================================================
# C90  the complete bilinear ATLAS on the boundary subspace (16 Clifford elements)
# ============================================================================
def sig(mu, nu): return sp.I / 2 * (gam[mu] * gam[nu] - gam[nu] * gam[mu])
def bil(M): return sp.simplify(sp.expand_trig(sp.simplify(Psi.H * g0 * M * Psi)))      # psibar M psi on L_theta
def match(M2, target): return z(sp.simplify(sp.expand((M2 - target).rewrite(sp.exp))))
atlas = {
    "1":        (sp.eye(4),        2 * sp.sin(th) * JE),
    "i g5":     (sp.I * g5,        2 * sp.cos(th) * JE),
    "g3":       (g3,               sp.zeros(2)),
    "g3 g5":    (g3 * g5,          2 * JE),
    "g0":       (g0,               2 * sp.eye(2)),
    "g0 g5":    (g0 * g5,          sp.zeros(2)),
    "g1":       (g1,               2 * Xth),
    "g2":       (g2,               2 * Yth),
    "g1 g5":    (g1 * g5,          sp.zeros(2)),
    "g2 g5":    (g2 * g5,          sp.zeros(2)),
    "sig03":    (sig(0, 3),        2 * sp.cos(th) * sp.eye(2)),
    "sig12":    (sig(1, 2),        2 * sp.sin(th) * sp.eye(2)),
    "sig01":    (sig(0, 1),        -sp.sin(2 * th) * SX + (sp.cos(2 * th) - 1) * SY),
    "sig02":    (sig(0, 2),        (sp.cos(2 * th) - 1) * SX + sp.sin(2 * th) * SY),
    "sig13":    (sig(1, 3),        -sp.sin(2 * th) * SX + (sp.cos(2 * th) + 1) * SY),
    "sig23":    (sig(2, 3),        (sp.cos(2 * th) + 1) * SX + sp.sin(2 * th) * SY),
}
atlas_ok = {k: match(bil(M), T) for k, (M, T) in atlas.items()}
herm_ok = all(sp.simplify(M.H - g0 * M * g0) == sp.zeros(4, 4) for (M, _) in atlas.values())
flipX = z(sp.simplify(Xth * JE + JE * Xth)) and z(sp.simplify(Yth * JE + JE * Yth))
row("C90", "C", "BOUNDARY BILINEAR ATLAS (Theorem 27 extended from 4 scalars to all 16 Hermitian Dirac bilinears "
    "on L_theta, universal in theta): scalar/pseudoscalar/normal-axial -> multiples of J_E (2 sin theta, 2 cos theta, "
    "2); density gamma^0 and the tensors sigma^{03}, sigma^{12} -> multiples of the IDENTITY (2, 2 cos theta, "
    "2 sin theta); the tangential spatial vector currents gamma^1, gamma^2 -> 2 X_theta, 2 Y_theta -- the "
    "GRADING-ODD flip elements of Theorem 21 ({X,J_E}=0) -- and the remaining tensors sigma^{01,02,13,23} -> "
    "flip elements at doubled angle; the tangential AXIAL currents gamma^a gamma5 (a = 0,1,2), the normal vector "
    "current gamma^3 and gamma^0 gamma5 -> 0. Hence on the chiral-bag boundary the 16-dimensional bilinear space "
    "collapses onto span{1, J_E, X_theta, Y_theta}, and only the tangential VECTOR currents reach the flip family",
    all(atlas_ok.values()) and herm_ok and flipX,
    "16/16 matched; all Hermitian; X_theta, Y_theta anticommute with J_E", universal=True)

# ============================================================================
# C86  HORN B -- RETYPED: classification, exact part
# ============================================================================
al = sp.Symbol('alpha', real=True)
UV4 = sp.exp(sp.I * al) * sp.eye(4)                     # vector shift
UA4 = sp.cos(al) * sp.eye(4) + sp.I * sp.sin(al) * g5    # axial shift
UVc = sp.simplify(Vp.H * UV4 * Vp); UAc = sp.simplify(sp.expand_trig(sp.simplify(Vp.H * UA4 * Vp)))
vec_trivial = z(sp.simplify(UVc.H * JE * UVc - JE)) and z(sp.simplify(UVc.H * Xth * UVc - Xth))
ax_fixJ = z(sp.simplify(sp.expand_trig(sp.simplify(UAc.H * JE * UAc - JE))))
ax_movesX = not z(sp.simplify(sp.expand_trig(sp.simplify(UAc.H * Xth * UAc - Xth))))
flux_V = z(bil(g3)); flux_A = match(bil(g3 * g5), 2 * JE)
# axial rotation moves the boundary angle: B_{theta} -> B_{theta+2alpha} (Thm 9), mass phase oppositely (Cor 9.2)
Bth = lambda t: sp.cos(t) * (sp.I * g3) + sp.sin(t) * (g3 * g5)
thm9 = z(sp.simplify(sp.expand_trig(sp.simplify(UA4 * Bth(th) * UA4.H - Bth(th + 2 * al)))))
Mm = lambda t: g0 * (sp.cos(t) * sp.eye(4) + sp.I * sp.sin(t) * g5)       # psi^dag Mm psi = m psibar e^{i t g5} psi
mass_move = z(sp.simplify(sp.expand_trig(sp.simplify(UA4.H * Mm(tmm) * UA4 - Mm(tmm + 2 * al)))))
bdy_move = z(sp.simplify(sp.expand_trig(sp.simplify(UA4.H * Bth(th) * UA4 - Bth(th - 2 * al)))))
row("C86", "C", "HORN B (Phi_Z != Phi), EXACT PART -- retyped from v2.9's universal no-go to a classification by "
    "U(1)_Phi charge type: (V) a VECTOR-charged fermion: d_mu J_V^mu = 0 on shell (C89), the normal flux "
    "psibar gamma^3 psi = 0 on EVERY admissible L (isotropy, C70/C90), and the shift e^{i alpha} acts on the carrier "
    "as a scalar fixing J_E and X_theta -- so the bulk derivative coupling d_mu theta J_V^mu is a total derivative "
    "with vanishing boundary flux and is removed by psi -> e^{i q theta} psi: EXACT decoupling, coefficient-free. "
    "(A) an AXIAL-charged fermion: d_mu J_A^mu != 0 (C89), the normal flux is 2 J_E (C90) -- the Goldstone reaches "
    "the record through the axial boundary flux -- but the bulk-plus-boundary pair is the infinitesimal axial "
    "rotation: under psi = e^{i alpha gamma5} psi' the boundary angle of psi' is theta - 2alpha and its mass phase "
    "theta_m + 2alpha (Thm 9, Cor 9.2), so thetabar is invariant, and acts on the carrier as e^{i alpha J_E}, fixing J_E (C50): the record "
    "kappa and the invariant thetabar are untouched at zeroth order in tangential gradients. (A) also breaks the "
    "shift symmetry explicitly through the mass, so it is not an exact Goldstone of the fermion sector",
    vec_trivial and ax_fixJ and ax_movesX and flux_V and flux_A and thm9 and mass_move and bdy_move,
    "vector: trivial on carrier, flux 0 | axial: flux 2J_E, fixes J_E, moves X_theta, psi': theta-2a, theta_m+2a (thetabar invariant)",
    universal=True)

# ============================================================================
# C91  ONE Dirac field carries EXACTLY ONE edge band (the multiplicity lemma Thm 39 needed)
# ============================================================================
Es, Cs, Ssy, kap, k1 = sp.symbols('E C S kappa k_1')
gens = (kap, Es, Cs, Ssy, k1, mm_)
shell = [Cs**2 + Ssy**2 - 1, kap**2 - (k1**2 + mm_**2 - Es**2)]
Gsh = sp.groebner(shell, *gens, order='lex', domain='QQ<I>')
red = lambda ex: Gsh.reduce(sp.expand(ex))[1]
Dm = Es * g0 - k1 * g1 - sp.I * kap * g3 - mm_ * sp.eye(4)
sk = k1 * s1 + sp.I * kap * s3
Bcs = Cs * (sp.I * g3) + Ssy * (g3 * g5)
def chart(U):
    inker = all(red(x) == 0 for x in (Dm * U))
    Q = (sp.eye(4) - Bcs) / 2 * U
    mins = [red(4 * Q.extract([i, j], [0, 1]).det()) for i in range(4) for j in range(i + 1, 4)]
    mins = [x for x in mins if x != 0]
    Gm = sp.groebner(mins + shell, *gens, order='lex', domain='QQ<I>')
    return inker, Gm, Q
inker1, Gm1, Q1 = chart(sp.Matrix.vstack((Es + mm_) * sp.eye(2), sk))     # valid for E != -m
inker2, Gm2, Q2 = chart(sp.Matrix.vstack(sk, (Es - mm_) * sp.eye(2)))     # valid for E != +m
only1 = Gm1.reduce(sp.expand((Es + mm_) * (kap + mm_ * Cs)))[1] == 0
only2 = Gm2.reduce(sp.expand((Es - mm_) * (kap + mm_ * Cs)))[1] == 0
notin1 = Gm1.reduce(sp.expand(kap + mm_ * Cs))[1] != 0          # the E = -m factor is genuinely the chart's own zero
sh2 = sp.groebner([Cs**2 + Ssy**2 - 1, Es**2 - k1**2 - mm_**2 * Ssy**2], Es, Cs, Ssy, k1, mm_, order='lex', domain='QQ<I>')
def rank_at_root(Q):
    Qs = Q.subs(kap, -mm_ * Cs).applyfunc(lambda x: sh2.reduce(sp.expand(x))[1])
    minors0 = all(sh2.reduce(sp.expand(Qs.extract([i, j], [0, 1]).det()))[1] == 0 for i in range(4) for j in range(i + 1, 4))
    return minors0 and any(x != 0 for x in Qs)
rk1, rk2 = rank_at_root(Q1), rank_at_root(Q2)
row("C91", "C", "EDGE-BAND MULTIPLICITY OF ONE DIRAC FIELD IS EXACTLY ONE (universal, two charts, Groebner over "
    "Q(i)): for the decaying ansatz psi = u e^{-kappa x^3} e^{-iEt + i k_1 x^1} on the shell kappa^2 = k_1^2 + m^2 - "
    "E^2, the chiral-bag condition has a nonzero solution iff the 2x2 minors of P_-(theta) restricted to ker D vanish; "
    "their ideal together with the shell ideal contains (E + m)(kappa + m cos thetabar) in the chart valid for "
    "E != -m and (E - m)(kappa + m cos thetabar) in the chart valid for E != +m, so the ONLY bound-state "
    "localisation rate is kappa = -m cos thetabar (Thm 15), and there the solution space has rank EXACTLY one. "
    "Hence at fixed (k_perp, sign E) one Dirac field carries one edge state (Thm 26) and NO second band: extra "
    "bands can come only from extra fields. dim E+ = 2 (C38) is a fibre dimension and was never a band count",
    inker1 and inker2 and only1 and only2 and notin1 and rk1 and rk2,
    "ideal contains (E+-m)(kappa+mC); rank 1 at the root in both charts", universal=True)

# ============================================================================
# C92  Fock block structure: the d-channel of band i sees band i only (diagonal mean field)
# ============================================================================
G11 = sp.Matrix(4, 4, lambda i, j: sp.Symbol('a%d%d' % (i, j))); G22 = sp.Matrix(4, 4, lambda i, j: sp.Symbol('b%d%d' % (i, j)))
Gbig = blk(G11, sp.zeros(4, 4), sp.zeros(4, 4), G22)
Mbig = sp.eye(8)                                      # scalar contact (Sum_i psibar_i psi_i)^2
Fock = Mbig * Gbig * Mbig
F11, F12 = Fock[0:4, 0:4], Fock[0:4, 4:8]
dcoef = sp.simplify((N * g5 * F11).trace() / 4)
hartree = sp.simplify(Gbig.trace())
row("C92", "C", "MULTI-BAND CHANNEL STRUCTURE (replaces the 1/N_b scaling of v2.9's C87): for N fields coupled by "
    "the scalar contact term (Sum_i psibar_i psi_i)^2 (Lemma 36.1) with a colour/flavour-DIAGONAL two-point function "
    "G = diag(G_1, ..., G_N), the Fock (exchange) operator M G M is block-diagonal, its off-diagonal blocks vanish, "
    "and the d-channel coefficient (1/4)Tr(N gamma5 F_ii) of band i is a function of G_i ALONE; the Hartree term "
    "Tr(M G) = Sum_i Tr G_i sums over bands but feeds the scalar (a,b)-plane, which is the reflection (Thm 33a), "
    "not the record channel. Hence the Theorem-36 bound applies BAND BY BAND with that band's own (G_4, n, s); "
    "multiplicity neither eases nor tightens it. Consistent with v2.8 sect.25 item 19, which v2.9 contradicted",
    F12 == sp.zeros(4, 4) and F11.free_symbols <= G11.free_symbols and dcoef.free_symbols <= G11.free_symbols
    and hartree.free_symbols == (G11.free_symbols | G22.free_symbols) & hartree.free_symbols
    and len(hartree.free_symbols & G22.free_symbols) == 4,
    "Fock off-diagonal = 0; d-coef(1) = (a00-a11+a22-a33)/4 depends on G_1 only; Hartree sums both", universal=True)

# ============================================================================
# C87  -- RETYPED: the per-band bound (the 1/N_b easing is withdrawn)
# ============================================================================
Nb, cp, sth, kap_ = sp.symbols('N_b cprime sinthetabar kappa', positive=True)
bound1 = sp.pi * kap_ / (2 * cp * sth * (1 - kap_))
row("C87", "C", "Z2 MULTI-BAND, REPAIRED: by C91 bands are fields, by C92 each band's record self-coupling is its own "
    "(Thm 33b Fock term), so for N_b bands in a diagonal mean field the admission predicate is "
    "max_i G_4,i m_i^2 >= pi kappa/(2 c' sin(thetabar)(1-kappa)) -- the single-band bound of Theorem 36, "
    "INDEPENDENT of N_b. The v2.9 statement 'bound scales as 1/N_b' is WITHDRAWN (it was favourable to the "
    "multi-band route and wrong in that direction). The bound expression is re-certified as N_b-free",
    sp.simplify(sp.diff(bound1, Nb)) == 0 and Nb not in bound1.free_symbols,
    "d(bound)/dN_b == 0 ; N_b not a free symbol of the predicate", universal=True)


# ============================================================================
# C94  Theorem 38.3 -- the Lorentzian axial Jacobian density vanishes pointwise (charge conjugation)
# ============================================================================
Cm = sp.I * g2; Cinv = Cm.inv()
def conjC(A): return sp.simplify(Cm * A.conjugate() * Cinv)          # C A C^{-1} for antiunitary C = Cm K
ph = sp.Matrix(sp.symbols('f0:4')); phc = sp.Matrix(sp.symbols('h0:4'))   # phi, phi^* as independent symbols
Cphi = Cm * phc; Cphi_dag = (Cm.conjugate() * ph).T
dens_flip = sp.simplify(sp.expand((Cphi_dag * g5 * Cphi)[0]) - sp.expand((-phc.T * g5 * ph)[0])) == 0
Mm_ = lambda t: g0 * (sp.cos(t) * sp.eye(4) + sp.I * sp.sin(t) * g5)
c_g5 = conjC(g5) == -g5
c_L = sp.simplify(sp.expand_trig(conjC(Bth(th)) - Bth(th))) == sp.zeros(4, 4)
c_kin = all(sp.simplify(Cm * (sp.I * (g0 * gam[k]).conjugate()) * Cinv - sp.I * g0 * gam[k]) == sp.zeros(4, 4) for k in (1, 2, 3))
c_mass = sp.simplify(sp.expand_trig(Cm * Mm_(tmm).conjugate() * Cinv + Mm_(tmm))) == sp.zeros(4, 4)
row("C94", "C", "THEOREM 38.3, SCOPE NARROWED IN v3.2 (the H^2-regularised spectral supertrace cancellation; universal in "
    "(theta, theta_m, m)): the charge conjugation C = i gamma^2 K of Theorem 24 satisfies C gamma5 C^{-1} = -gamma5, "
    "flips the pointwise axial density (C phi)^dag gamma5 (C phi) = -phi^dag gamma5 phi for every spinor phi, preserves "
    "every L_theta, and anticommutes with H = -i gamma^0 gamma^k d_k + gamma^0 m e^{i theta_m gamma5} (kinetic and "
    "mass parts separately). Hence C pairs the spectrum E <-> -E of the self-adjoint chiral-bag Hamiltonian and the "
    "regularised supertrace Sum_n f(E_n^2) phi_n(x)^dag gamma5 phi_n(x) cancels POINTWISE, boundary included, for every "
    "regulator f(H^2). WHAT THIS ROW DOES NOT CERTIFY (v3.1 audit, scope correction): that the Fujikawa Jacobian of "
    "an ARBITRARY LOCAL axial rotation alpha(x) with the bag domain held fixed equals 1 -- a local alpha(x) need not "
    "map dom(H) to itself, and no domain-preservation proof is given; the constant-alpha case is C95 (co-rotation). "
    "The v3.1 sentence 'no eta or inflow term survives' is WITHDRAWN as a statement about local transformations",
    dens_flip and c_g5 and c_L and c_kin and c_mass,
    "C g5 C^-1 = -g5 ; density flips ; L_theta preserved ; {C, H} = 0 (kinetic, mass) ; local alpha(x): NOT certified", universal=True)

# ============================================================================
# C95  Theorem 38.4 -- unitary equivalence: spectral data depend on thetabar only
# ============================================================================
kin_inv = all(sp.simplify(UA4.H * g0 * gam[k] * UA4 - g0 * gam[k]) == sp.zeros(4, 4) for k in (1, 2, 3))
mass_co = sp.simplify(sp.expand_trig(UA4.H * Mm_(tmm) * UA4 - Mm_(tmm + 2 * al))) == sp.zeros(4, 4)
dom_co = z(sp.simplify(sp.expand_trig(sp.simplify(UA4.H * Bth(th) * UA4 - Bth(th - 2 * al)))))
row("C95", "C", "THEOREM 38.4 (spectral thetabar-invariance; universal): U = e^{i alpha gamma5} is unitary on "
    "L^2(R^3_+, C^4), fixes the kinetic matrices gamma^0 gamma^k, sends the mass matrix gamma^0 m e^{i theta_m gamma5} "
    "to that of theta_m + 2 alpha, and maps L_theta onto L_{theta - 2 alpha}; hence U^dag H(theta_m, theta_b) U = "
    "H(theta_m + 2 alpha, theta_b - 2 alpha) with U^dag dom(H) = dom(H'), a unitary equivalence of self-adjoint "
    "operators. Every spectral function (heat trace, zeta, eta, density of states, determinant, KMS pushforward) of "
    "the two operators coincides, so any spectrally regularised effective action depends on thetabar alone. With C50 "
    "this is the quantum half of Theorem 38(A): the co-rotating Jacobian of a constant axial rotation is exactly 1",
    kin_inv and mass_co and dom_co, "kinetic fixed ; mass phase +2alpha ; domain -2alpha", universal=True)

# ============================================================================
# C96  Theorem 39.4 -- K9 closed: off-diagonal colour/flavour condensates are gauge-variant
# ============================================================================
lam8 = [sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]), sp.Matrix([[0,-sp.I,0],[sp.I,0,0],[0,0,0]]), sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]]),
        sp.Matrix([[0,0,1],[0,0,0],[1,0,0]]), sp.Matrix([[0,0,-sp.I],[0,0,0],[sp.I,0,0]]), sp.Matrix([[0,0,0],[0,0,1],[0,1,0]]),
        sp.Matrix([[0,0,0],[0,0,-sp.I],[0,sp.I,0]]), sp.Matrix([[1,0,0],[0,1,0],[0,0,-2]]) / sp.sqrt(3)]
Xc = sp.Matrix(3, 3, lambda i, j: sp.Symbol('x%d%d' % (i, j)))
ceqs = []
for L_ in lam8: ceqs += list(Xc * L_ - L_ * Xc)
csol = sp.solve(ceqs, list(Xc), dict=True)
Xcs = Xc.subs(csol[0])
commutant_ok = len(Xcs.free_symbols) == 1 and sp.simplify(Xcs - Xcs[0, 0] * sp.eye(3)) == sp.zeros(3, 3)
phi_ = sp.symbols('phi1:4', real=True)
Tc = sp.diag(*[sp.exp(sp.I * p_) for p_ in phi_])
offdiag_phase = all(sp.simplify(sp.simplify(Tc * sp.Matrix(3, 3, lambda a, b: 1 if (a, b) == (i, j) else 0) * Tc.H)[i, j]
                                - sp.exp(sp.I * (phi_[i] - phi_[j]))) == 0 for i in range(3) for j in range(3) if i != j)
qem = {"t": sp.Rational(2, 3), "b": sp.Rational(-1, 3)}
em_charge = qem["t"] - qem["b"] != 0
row("C96", "C", "THEOREM 39.4, RE-QUANTIFIED IN v3.2 (K9a closed; exact + IMPORTED Elitzur): the commutant of su(3) (all "
    "eight Gell-Mann generators) in M_3(C) is C*1, so the only gauge-invariant COLOUR bilinear psibar_i M_ij psi_j has "
    "M proportional to the identity (Schur, as in Theorem 2); every colour-off-diagonal E_ij (i != j) transforms as "
    "e^{i(phi_i - phi_j)} E_ij under the Cartan torus and is gauge-VARIANT. By Elitzur's theorem (IMPORTED: S. Elitzur, "
    "Phys. Rev. D 12, 3978 (1975), primary listing read this session; SCOPE NARROWED IN v3.3; HYPOTHESES MADE EXPLICIT IN "
    "v3.4 -- (H1) gauge-invariant POSITIVE measure / gauge-invariant physical state, (H2) the boundary condition and the "
    "measure preserve the local colour and electromagnetic gauge symmetry: no boundary gauge reduction and no dressed "
    "non-local order parameter is used) the expectation of an UNDRESSED local gauge-variant operator vanishes, so a "
    "colour-off-diagonal boundary condensate of that type vanishes; fixed-gauge (unphysical) expectations, boundary "
    "gauge reductions, non-positive measures and dressed non-local operators are OUTSIDE this statement. For the weak doublet (t, b) the off-diagonal bilinear carries electric charge Q_t - Q_b = 1 != 0 and "
    "vanishes by the same theorem for unbroken U(1)_em. WHAT THIS ROW DOES NOT COVER (v3.1 "
    "audit, S3): a bilinear between two fields in the SAME gauge representation with the SAME unbroken charges "
    "(generation flavour: u-c, d-s, e-mu, colour contracted to a singlet) is gauge-INVARIANT and is NOT excluded by "
    "Elitzur; that class is K9b (C99, V33). The v3.1 sentence 'the diagonal mean field is a theorem' is WITHDRAWN "
    "and replaced by: colour- and charge-diagonality are theorems; generation-flavour diagonality is not",
    commutant_ok and offdiag_phase and em_charge, "commutant dim 1 ; E_ij phase e^{i(phi_i-phi_j)} ; Q_t - Q_b = 1 ; same-rep flavour: NOT covered ; Elitzur 1975: H1 positive gauge-invariant measure, H2 boundary preserves local gauge symmetry, undressed local operators only", universal=True)

# ============================================================================
# C97  Theorem 41 -- the thermal ceiling on the carrier record
# ============================================================================
Dl, eps, tau1, tau2, z0 = sp.symbols('Delta epsilon tau1 tau2 z0', positive=True)   # tau_1, tau_2: Bloch relaxation times (TYPE LOCK: not the target T_2)
xb, yb, zb = sp.symbols('x y z')
bloch = [-Dl * yb - xb / tau2, Dl * xb - 2 * eps * zb - yb / tau2, 2 * eps * yb - (zb - z0) / tau1]
solb = sp.solve(bloch, [xb, yb, zb], dict=True)[0]
zss = sp.simplify(solb[zb])
ceiling_form = sp.simplify(zss / z0 - (1 + Dl**2 * tau2**2) / (1 + Dl**2 * tau2**2 + 4 * eps**2 * tau1 * tau2)) == 0
ratio = (1 + Dl**2 * tau2**2) / (1 + Dl**2 * tau2**2 + 4 * eps**2 * tau1 * tau2)
ceiling_le1 = sp.simplify(1 / ratio - 1 - 4 * eps**2 * tau1 * tau2 / (1 + Dl**2 * tau2**2)) == 0     # 1/ratio = 1 + positive
nB_ = 1 / (sp.exp(3) - 1); g_ = sp.Rational(3, 10)
tau1n = 1 / (g_ * (2 * nB_ + 1)); z0n = -sp.tanh(sp.Rational(3, 2))
zW14 = zss.subs({z0: z0n, Dl: 1, eps: sp.Rational(3, 10), tau1: tau1n, tau2: 2 * tau1n}).evalf(15)
row("C97", "C", "THEOREM 41 (thermal ceiling; exact in the Bloch variables; TYPE LOCK v3.2: tau_1, tau_2 are the Bloch "
    "relaxation times, the Z-Spin target is T_2): for the carrier class {J_E-thermal damping with detailed balance "
    "(tau_1, equilibrium z0 = -tanh(Delta/2T)), J_E-dephasing (tau_2 <= 2 tau_1), static flip-odd term eps X_theta (C90)} "
    "the Bloch equations dx = -Delta y - x/tau_2, dy = Delta x - 2 eps z - y/tau_2, dz = 2 eps y - (z - z0)/tau_1 have "
    "the UNIQUE stationary record kappa = z0 (1 + Delta^2 tau_2^2)/(1 + Delta^2 tau_2^2 + 4 eps^2 tau_1 tau_2), whose "
    "ratio to z0 is 1/(1 + positive) <= 1. Hence |kappa| <= tanh(Delta/2T) for every eps, tau_1, tau_2 > 0: a flip-odd "
    "tangential datum can only LOWER the record below the rest-frame thermal value, never raise it. Reproduces W14 at eps = 0.3",
    ceiling_form and ceiling_le1 and abs(float(zW14) - (-0.770215152242570)) < 1e-9,
    "z_ss/z0 = (1+D^2 tau2^2)/(1+D^2 tau2^2+4e^2 tau1 tau2) ; W14 cross-check %.9f" % float(zW14), universal=True)

# ============================================================================
# C98  Corollary 37.2 -- derivative signs of the Jost integrand (A5 residue count)
# ============================================================================
Ai, pi_ = sp.symbols('A p', real=True)
kapi = sp.sqrt(pi_**2 + mm_**2)
alt = all(sp.simplify(sp.diff(1 / (kapi + Ai), Ai, k) - (-1)**k * sp.factorial(k) / (kapi + Ai)**(k + 1)) == 0 for k in range(1, 5))
row("C98", "C", "COROLLARY 37.2 (the A5 residue, counted): d^k/dA^k (kappa(p) + A)^{-1} = (-1)^k k! (kappa(p) + A)^{-k-1} "
    "for k = 1..4, so Gamma^(1) > 0, Gamma^(2) < 0, Gamma^(3) > 0, Gamma^(4) < 0 on (-m, m). With the counterterm freedom "
    "exactly a cubic in A (Thm 13c), the renormalised stationary equation f(A) = Gamma^(1)(A) + c1 + 2 c2 A + 3 c3 A^2 = 0 "
    "has f^(3) = Gamma^(4) < 0, so f^(2) has at most one zero, f^(1) at most two, and f AT MOST THREE roots in (-m, m): "
    "at most three off-pi-Z stationary values of cos(thetabar). Landing on A_* = m Re(lambda) and making it a minimum "
    "consumes one equation and one inequality, leaving exactly TWO real counterterm parameters as the A5 residue",
    alt, "sign alternation k = 1..4 exact", universal=True)

# ============================================================================
# C99a/b/c  Proposition 39.6, ALGEBRA ONLY (v3.3 split of v3.2's C99); C99d/C99e are OPEN and live in D36
# ============================================================================
Ad_ = N * g5                                   # the d-channel matrix (Hermitian involution)
A_herm = sp.simplify(Ad_.H - Ad_) == sp.zeros(4, 4) and sp.simplify(Ad_ * Ad_) == sp.eye(4)
yy1, yy2 = sp.symbols('y1 y2', positive=True)
Gc11 = sp.Matrix(4, 4, lambda i, j: sp.Symbol('a%d%d' % (i, j))); Gc22 = sp.Matrix(4, 4, lambda i, j: sp.Symbol('b%d%d' % (i, j)))
Gc12 = sp.Matrix(4, 4, lambda i, j: sp.Symbol('c%d%d' % (i, j)))
Gcoh = blk(Gc11, Gc12, Gc12.H, Gc22)            # flavour-COHERENT two-point function, Hermitian by construction (G_21 = G_12^dag)
Mflav = blk(yy1 * sp.eye(4), sp.zeros(4, 4), sp.zeros(4, 4), yy2 * sp.eye(4))   # Yukawa vertex diag(y1, y2) (x) 1_4
Fc = Mflav * Gcoh * Mflav
Fc11, Fc12, Fc21, Fc22 = Fc[0:4, 0:4], Fc[0:4, 4:8], Fc[4:8, 0:4], Fc[4:8, 4:8]
fock_offdiag = sp.simplify(Fc12 - yy1 * yy2 * Gc12) == sp.zeros(4, 4) and Fc12 != sp.zeros(4, 4) and sp.simplify(Fc21 - Fc12.H) == sp.zeros(4, 4)
row("C99a", "C", "PROPOSITION 39.6(a), ALGEBRA (v3.3 split; universal in G, y_i): for two fields with identical unbroken gauge "
    "charges coupled by the Yukawa-induced contact term with flavour vertex M = diag(y_1, y_2) (x) 1_4 and a "
    "flavour-coherent Hermitian two-point function G with off-diagonal block G_12 != 0 (G_21 = G_12^dag), the Fock "
    "operator M G M has the NONZERO off-diagonal block (MGM)_12 = y_1 y_2 G_12 and (MGM)_21 = (MGM)_12^dag: Theorem 39's "
    "block-diagonality is a property of the diagonal mean field, not of the interaction. THIS ROW SAYS NOTHING about the "
    "admission bound of a coherent carrier (D36)",
    A_herm and fock_offdiag, "F_12 = y1 y2 G_12 != 0 ; F_21 = F_12^dag ; N g5 Hermitian involution", universal=True)
Dc11 = sp.simplify((Ad_ * Fc11).trace() / 4); Dc22 = sp.simplify((Ad_ * Fc22).trace() / 4)
Dc12 = sp.simplify((Ad_ * Fc12).trace() / 4); Dc21 = sp.simplify((Ad_ * Fc21).trace() / 4)
diag_unchanged = (Dc11.free_symbols <= (Gc11.free_symbols | {yy1})) and (Dc22.free_symbols <= (Gc22.free_symbols | {yy2})) \
    and sp.simplify(Dc11 - yy1**2 * (Gc11[0, 0] - Gc11[1, 1] + Gc11[2, 2] - Gc11[3, 3]) / 4) == 0
offdiag_form = sp.simplify(Dc12 - yy1 * yy2 * (Gc12[0, 0] - Gc12[1, 1] + Gc12[2, 2] - Gc12[3, 3]) / 4) == 0
D_herm = sp.simplify(Dc21 - sp.conjugate(Dc12)) == 0
row("C99b", "C", "PROPOSITION 39.6(b), ALGEBRA (v3.3 split; universal): the flavour matrix of d-channel coefficients D_ij := "
    "(1/4) Tr(N gamma5 (MGM)_ij) has diagonal entries D_ii = (1/4) y_i^2 Tr(N gamma5 G_ii), UNCHANGED by G_12, off-diagonal "
    "entry D_12 = (1/4) y_1 y_2 Tr(N gamma5 G_12), and D_21 = conj(D_12): D is Hermitian whenever G is. THIS ROW DOES NOT "
    "assert that D_ii is the record self-coupling of band i inside a coherent carrier (D36)",
    diag_unchanged and offdiag_form and D_herm, "D_11 = y1^2 (a00-a11+a22-a33)/4 ; D_12 = y1 y2 (c00-c11+c22-c33)/4 ; D_21 = conj(D_12)", universal=True)
aa, cc, rr = sp.symbols('a c r', real=True)                 # D = [[a, b], [b*, c]], r = |b|
lam_max = (aa + cc) / 2 + sp.sqrt(((aa - cc) / 2)**2 + rr**2)
bracket_lo = sp.simplify(sp.expand((lam_max - aa) * (lam_max - cc) - rr**2)) == 0 \
    and sp.simplify(lam_max - (aa + cc) / 2 - sp.sqrt(4 * rr**2 + (aa - cc)**2) / 2) == 0   # (lam-a)(lam-c) = r^2 >= 0 and lam >= (a+c)/2  => lam >= max(a,c)
bracket_hi = sp.simplify((sp.Abs(aa - cc) / 2 + rr)**2 - (((aa - cc) / 2)**2 + rr**2) - rr * sp.Abs(aa - cc)) == 0   # => lam_max <= max(a,c) + r
row("C99c", "C", "PROPOSITION 39.6(c), ALGEBRA (v3.3 split; universal): for ANY Hermitian 2x2 matrix [[a, b], [conj b, c]] with "
    "r = |b|, the largest eigenvalue satisfies max(a, c) <= lambda_max <= max(a, c) + r, with equality on the left iff "
    "r = 0 ((lambda_max - a)(lambda_max - c) = r^2 and lambda_max >= (a + c)/2). A statement about matrices; whether "
    "lambda_max(D) is a critical coupling of anything physical is D36 (OPEN)",
    bracket_lo and bracket_hi, "(lam_max - a)(lam_max - c) = r^2 ; lam_max <= max(a,c) + r", universal=True)
row("D36", "D", "C99d / C99e -- OPEN (v3.2 audit, S3, accepted): (d) that lambda_max(D) is the critical coupling of a coherent "
    "two-flavour carrier, and (e) that Theorem 36's single-band admission bound pi kappa/(2 c' sin thetabar (1 - kappa)) "
    "is unchanged for such a carrier, are NOT proved. Theorem 36 was derived for one band, one mass, one gap, one "
    "density and one <1/E> with the filled-disk extremiser; Theorem 39 transferred it to several bands only because a "
    "diagonal mean field decouples the gap equations. A coherent carrier needs: the joint dispersion of two bands with "
    "different masses and gaps, the composition of the record kappa from the diagonal and off-diagonal density blocks, "
    "the Pauli occupation extremiser under coherence, a theorem placing lambda_max(D) (or another functional) in the "
    "critical gap equation, and the resulting admission criterion (Proof obligation 39.8). Until then the v3.2 "
    "sentences 'unchanged bound', 'n_c/n_t ~ 2e7 needed' and 'K9b REJECTED-BY-BOUND on n_partner <= n_top' are "
    "WITHDRAWN and K9b is OPEN", True, "")


# ============================================================================
# sect.22.11 (v3.4, research addition): C100 record composition, C101 normal overlap, C102 pair-channel decoupling
# ============================================================================
Jbl_ = blk(Ad_, sp.zeros(4, 4), sp.zeros(4, 4), Ad_)                    # the flavour-BLIND record operator J_E (x) 1_2 on the carrier
rec_lhs = sp.expand((Jbl_ * Gcoh).trace()); rec_rhs = sp.expand((Ad_ * Gc11).trace() + (Ad_ * Gc22).trace())
rec_exact = sp.simplify(rec_lhs - rec_rhs) == 0 and not (rec_lhs.free_symbols & Gc12.free_symbols)
uu_ = sp.Matrix(4, 1, lambda i, j: sp.Symbol('u%d' % i)); rr_ = sp.symbols('r_fam', positive=True)
ww_ = sp.Matrix.vstack(uu_, sp.sqrt(rr_) * Ad_ * uu_); Gw_ = ww_ * ww_.H
fam_rec = sp.simplify((Jbl_ * Gw_).trace() / Gw_.trace() - (uu_.H * Ad_ * uu_)[0] / (uu_.H * uu_)[0]) == 0
row("C100", "C", "LEMMA 39.9 (record composition; exact, universal in G): the record operator of the carrier is flavour-blind, "
    "J_E (x) 1_2, so for ANY Hermitian flavour-coherent two-point function G the record numerator Tr((J_E (x) 1) G) equals "
    "Tr(J_E G_11) + Tr(J_E G_22) and is INDEPENDENT of the off-diagonal block G_12: kappa = (n_1 kappa_1 + n_2 kappa_2)/(n_1 + n_2) "
    "is the density-weighted mean of the diagonal-block records, and coherence can enter the record only through the "
    "back-reaction of G_12 on the diagonal blocks via the gap equation. Checked on the v3.2 audit's family G = w w^dag, "
    "w = (u, sqrt(r) N gamma5 u): its record equals u^dag N gamma5 u / |u|^2 = kappa for EVERY r (the r = 7.4e5 of W16 "
    "moves the density, not the record). Answers item (ii) of Proof obligation 39.8 at the level of the carrier",
    rec_exact and fam_rec, "Tr((J (x) 1) G) = Tr(J G11) + Tr(J G22) exact ; family record = kappa for all r", universal=True)
xx_, k1_, k2_ = sp.symbols('x kappa1 kappa2', positive=True)
ov12_ = sp.integrate((2 * k1_ * sp.exp(-2 * k1_ * xx_)) * (2 * k2_ * sp.exp(-2 * k2_ * xx_)), (xx_, 0, sp.oo))
ov11_ = sp.integrate((2 * k1_ * sp.exp(-2 * k1_ * xx_)) ** 2, (xx_, 0, sp.oo))
harm_ = sp.simplify(ov12_ - 2 * k1_ * k2_ / (k1_ + k2_)) == 0 and sp.simplify(ov11_ - k1_) == 0
om_ = 2 * sp.sqrt(k1_ * k2_) / (k1_ + k2_)
om_le1 = sp.simplify(1 - om_ ** 2 - (k1_ - k2_) ** 2 / (k1_ + k2_) ** 2) == 0     # 1 - omega^2 = ((k1-k2)/(k1+k2))^2 >= 0, = 0 iff k1 = k2
row("C101", "C", "LEMMA 39.10 (the coherent channel's normal overlap; exact, universal in kappa_1, kappa_2 > 0): with the normalised "
    "edge profiles phi_i = sqrt(2 kappa_i) e^{-kappa_i x} of Lemma 36.2 (kappa_i = m_i |cos thetabar| at a common angle, Thm 15), "
    "the diagonal channel integrates the bulk quartic to G_4 kappa_i (Lemma 36.2) while the flavour-coherent channel "
    "(psibar_1 Gamma psi_2)(psibar_2 Gamma psi_1) integrates to G_4 * 2 kappa_1 kappa_2/(kappa_1 + kappa_2) -- the HARMONIC "
    "mean of the two localisation rates. Its ratio to the geometric mean sqrt(kappa_1 kappa_2) is "
    "omega = 2 sqrt(m_1 m_2)/(m_1 + m_2), and 1 - omega^2 = ((m_1 - m_2)/(m_1 + m_2))^2 >= 0: omega <= 1 with equality iff m_1 = m_2. "
    "The coherent channel's 2+1 contact strength is never larger than the geometric mean of the two diagonal strengths",
    harm_ and om_le1, "int phi1^2 phi2^2 = 2 k1 k2/(k1+k2) ; int phi1^4 = k1 ; 1 - omega^2 = ((k1-k2)/(k1+k2))^2", universal=True)
G0_ = blk(Gc11, sp.zeros(4, 4), sp.zeros(4, 4), Gc22)                    # a flavour-DIAGONAL reference two-point function (symbolic blocks)
E_ = {(i, j): sp.Matrix(2, 2, lambda a, b: 1 if (a == i and b == j) else 0) for i in range(2) for j in range(2)}
def _Bop(i, j): return sp.kronecker_product(E_[(i, j)], Ad_)             # the d-channel bilinear psibar_i Gamma psi_j as flavour E_ij (x) Gamma
kern_ = {(i, j, k, l): sp.expand((_Bop(i, j) * G0_ * _Bop(k, l) * G0_).trace()) for (i, j) in E_ for (k, l) in E_}
nz_ = [key for key, v in kern_.items() if v != 0]
decouple = len(nz_) == 4 and all(j == k and l == i for (i, j, k, l) in nz_) and all(kern_[(i, j, j, i)] != 0 for (i, j) in E_)
Mf_ = blk(yy1 * sp.eye(4), sp.zeros(4, 4), sp.zeros(4, 4), yy2 * sp.eye(4))
hart_diag = ((Mf_ * Gcoh).trace() * Mf_)[0:4, 4:8] == sp.zeros(4, 4)
row("C102", "C", "THEOREM 39.11 (pair-channel decoupling of the linearised coherent gap equation; exact, universal in the diagonal "
    "blocks): for ANY flavour-diagonal reference two-point function G_0 = diag(G_1, G_2) (the flavour-symmetric point or Theorem "
    "39's diagonal broken state) the Wick kernel of the d-channel bilinears B_ij = psibar_i Gamma psi_j, "
    "K[(ij),(kl)] = Tr(B_ij G_0 B_kl G_0), is nonzero ONLY for j = k and l = i (the 4 surviving entries of 16): the (12) "
    "channel couples only to (21) = (12)^dag, i.e. the linearised equation for the coherent condensate sigma_12 CLOSES ON ITSELF "
    "-- flavour number U(1)_1 x U(1)_2 is conserved by the reference state, the bulk (diagonal masses), the boundary condition "
    "(flavour-blind) and the interaction (sum_i y_i psibar_i psi_i)^2 -- and the Hartree term Tr(M G) M has no off-diagonal "
    "block. CONSEQUENCE: at linear order the coherent channel's onset is 1 = G_4 y_1 y_2 * (normal overlap, C101) * (interband "
    "d-channel response of the reference state); the flavour matrix D of Prop. 39.6, which is the Fock image of the ORDER "
    "PARAMETER, does not enter. C99d ('lambda_max(D) is the coherent carrier's critical coupling') is therefore "
    "CLOSED-NEGATIVE at linear order. What this row does NOT do: evaluate the interband response, or say anything about the "
    "deep coherent phase (rotated flavours with a non-diagonal bulk mass are not bands; Proof obligation 39.8')",
    decouple and hart_diag, "surviving kernel entries (i,j,k,l) = %s ; Hartree off-diagonal = 0" % nz_, universal=True)
row("D39", "D", "C99d / C99e AFTER v3.4 (sect.22.11): C99d -- 'lambda_max(D) is the critical coupling of a coherent two-flavour carrier' -- "
    "is CLOSED-NEGATIVE at linear order (Thm 39.11, C102): about any flavour-diagonal reference the coherent channel closes on "
    "itself and its onset functional is y_1 y_2 x (normal overlap, C101) x (interband d-channel response); D is the Fock image of "
    "the order parameter, not the kernel. In the deep coherent phase 'lambda_max(D)' is the larger eigenvalue of the condensate "
    "matrix, i.e. the boundary angle of a ROTATED flavour whose bulk mass matrix is not diagonal; Theorem 36 (one mass, one gap) "
    "does not apply to it, so the v3.2 reading is ill-typed there as well. C99e -- 'Theorem 36's single-band bound is unchanged "
    "for the coherent carrier' -- stays OPEN and is REFORMULATED as ONE computation, Proof obligation 39.8': (a) the interband "
    "d-channel response K_tc of Theorem 39's diagonal state, built from the edge dispersions E_i = sqrt(k^2 + Delta_i^2), the wall "
    "spinors of Thm 15 and the overlap of C101; (b) its maximum over Pauli-allowed occupations at fixed total record |kappa| = T_2 "
    "(composition C100); (c) the comparison of 1/(G_4 y_t y_c K_tc^max) with the corpus G_4. Items (i) [joint dispersion] and (ii) "
    "[record composition] of the v3.3 obligation are discharged at linear order (each band keeps its own dispersion about a "
    "diagonal reference; C100); items (iii)-(v) survive as (a)-(c). K9b: OPEN (unchanged); a first-order (discontinuous) "
    "appearance of the coherent phase is not excluded by the linear analysis and is part of (b)", True, "")
row("D40", "D", "AUDIT ACCEPTANCE RECORD (v3.3 audit, AUDIT-MAJOR-REVISION; central contribution SURVIVES; highest severity S2; "
    "release-blocking YES; research reopen NO; deterministic re-run 48/48 byte-identical, four fault injections reproduced): all "
    "findings accepted, 0 rejected -- S2-1 sect.25 physical-bridge overstatement ('completely specified ... all now derived') "
    "REPLACED by the signature statement: no CPTP map or state-selection mechanism is constructed in M67 (guard G20(iv); "
    "CLAIM-STATE MissingObject=SPECIFIED-NOT-CONSTRUCTED); S2-2 target-independent ceiling vs target-conditioned 0.4147 and "
    "Theorem 36's general functional form vs its (T_2, thetabar_*)-conditioned x42 verdict TYPED (V32; 'first target-blind "
    "constraint' WITHDRAWN); S2-3 release core / manifest object-graph mismatch REPAIRED (core = manuscript, verifier, ledger, "
    "release manifest; session, audit report and provenance supplement = provenance objects with measured hashes; G25); Elitzur "
    "citation and boundary hypotheses added (C96); exit_code([]) -> 2 (G21). One finding BEYOND the audit, reported here: W15's "
    "claim text embedded a machine-dependent 1e-16 residual (retyped); a lineage rescan found the same defect type once "
    "more (W16, a 1e-12 eigenvalue residual; retyped). Structural advice of the audit (do not force the coherent "
    "many-body theorem into a correction-only version) is honoured by SEPARATING sect.22.11 as a research addition under "
    "MANUSCRIPT sect.16 major-revision reclassification, with K9b kept OPEN. History rows H-0284/H-0285 are NOT edited; "
    "superseding rows are proposed for append", True, "")
row("D41", "D", "EXTERNAL BASELINE for K9b (EESF; deep-exploration sweep, one query family 'flavour off-diagonal condensate / "
    "generation-mixing bilinear / NJL / interband coherence'): M. Blasone, P. Jizba, N. E. Mavromatos, L. Smaldone, 'Chiral "
    "symmetry-breaking schemes and dynamical generation of masses and field mixing', arXiv:1807.07616 -- Existence: primary PDF "
    "read this session; Entailment: 'the generation of mixing implies the presence of off-diagonal condensates in flavor space', "
    "with the breaking pattern SU(2)_A x SU(2)_V x U(1)_V -> U(1)_V (only the total flavour charge survives) and a mean-field "
    "vacuum containing inter-flavour pair condensates (their eq. 40, U_k = cos(Theta_k1 - Theta_k2), V_k = sin(Theta_k1 - "
    "Theta_k2)); Scope: bulk 3+1, global chiral-flavour symmetry, no gauge field, no boundary; Freshness: n/a (theory). "
    "CLASSIFICATION: the OBJECT of K9b (a gauge-invariant generation-off-diagonal condensate with residual U(1)_V) is IMPORTED; "
    "Prop. 39.6's algebra is SPECIALIZED (the flavour-off-diagonal Fock block is the standard two-flavour structure); the "
    "boundary-carrier / chiral-bag-edge version of the question and Thm 39.11's onset functional were NOT_FOUND in the query "
    "family -- OPEN-NOVELTY (narrowed, not NEW). NOT_FOUND is not ABSENT. Secondary: arXiv:1606.00320 (same group, NJL effective "
    "action; abstract-level only)", True, "")

# ============================================================================
# V-block  (dps 60 ; the numbers of sect.21.3 recomputed, not copied)
# ============================================================================
zst = mp.findroot(lambda w: w - mp.e**(mp.log(1j) * w), mp.mpc('0.44', '0.36'))
lam_ = zst * mp.log(1j); Re_, Im_ = mp.re(lam_), abs(mp.im(lam_))
sin_star = mp.sqrt(1 - Re_**2); T2 = Im_ / sin_star
cprime = mp.mpf(1) / 2
req = mp.pi * T2 / (2 * cprime * sin_star * (1 - T2))
v_ = mp.mpf('245.93'); mh_ = mp.mpf('125.25'); mt_ = mp.mpf('171.872')
masses = {"top": mt_, "bottom": mp.mpf('4.18'), "charm": mp.mpf('1.27'), "tau": mp.mpf('1.77686')}
avail = {k: mf**4 / (2 * v_**2 * mh_**2) for k, mf in masses.items()}
short = {k: req / a for k, a in avail.items()}
row("V27", "V", "Z2 NUMBERS, RETYPED: with the bound per band (C87/C92) there is no 'required N_b'; the v2.9 figure "
    "N_b >= 42.07 is WITHDRAWN as moot. What remains is the per-band shortfall of sect.21.3: top %s x, bottom %s x, "
    "charm %s x, tau %s x -- unchanged by colour (3) or weak-doublet (6) multiplicity. CONDITIONAL on the "
    "identification and on the diagonal mean field" % tuple(mp.nstr(short[k], 4) for k in ("top", "bottom", "charm", "tau")),
    bool(short["top"] > 40) and bool(short["top"] < 44) and all(bool(short[k] > 1e7) for k in ("bottom", "charm", "tau")),
    "required G_4 m^2 = %s ; top available %s ; shortfall %s" % (mp.nstr(req, 8), mp.nstr(avail["top"], 8), mp.nstr(short["top"], 8)))

MP = mp.mpf('2.435e18')
f_short = (MP / mt_)**2 / req
row("V28", "V", "HORN B, CONDITIONAL PART (was 'for the record' in v2.9; now load-bearing for the residual class): "
    "any shift-symmetric coupling of the corpus Goldstone that is NOT removed by C86 -- bulk operators of dimension "
    ">= 6 or boundary-localised gradient terms -- carries a coefficient of order 1/f^2 with f = M_P from the ZS-S14 "
    "normalisation 1/2 M_P^2 |D H_5|^2, and misses Theorem 36's requirement by (M_P/m_t)^2/19.34 = %s. "
    "CONDITIONAL on f = M_P: a corpus-external normalisation is the named survivor" % mp.nstr(f_short, 6),
    bool(f_short > 1e25), "shortfall = %s" % mp.nstr(f_short, 8))

Delta_t = mt_ * sin_star
grad_req = MP * Delta_t
rho_ratio = grad_req**2 / 2 / mt_**4
row("V31", "V", "BOUNDARY-LOCALISED GOLDSTONE GRADIENT (the structural survivor of Theorem 38, made numerical): the "
    "operator (c/f) d_a theta_can psibar gamma^a psi restricted to L_theta acts on the carrier as the flip-odd "
    "element (c/f)(d_1 theta X_theta + d_2 theta Y_theta) (C90); to tilt the record at O(1) it must compete with the "
    "edge gap Delta = m_t sin(thetabar_*) = %s GeV, i.e. |d theta_can| ~ f Delta / c = %s GeV^2 for c = 1, whose "
    "gradient energy density (d theta)^2/2 exceeds m_t^4 by %s. No corpus background supplies this. CONDITIONAL on "
    "f = M_P and on the top wall" % (mp.nstr(Delta_t, 6), mp.nstr(grad_req, 6), mp.nstr(rho_ratio, 4)),
    bool(rho_ratio > 1e30), "ratio = %s" % mp.nstr(rho_ratio, 8))

T_over_D = 1 / (2 * mp.atanh(T2))
x_ens = mp.mpf('5.08249'); T_ens = 1 / x_ens
row("V32", "V", "COROLLARY 41.1 (the rest-frame datum bounded; TYPE LOCK v3.2: T_2 = %s is the Z-Spin TARGET, not a "
    "relaxation time; SIGN v3.3: with z_0 = -tanh(Delta/2T) the stationary record is negative in this convention, so the "
    "target condition is |kappa| = T_2, i.e. kappa = -T_2; TARGET-DEPENDENCE TYPED IN v3.4 (v3.3 audit S2): the ceiling "
    "|kappa| <= tanh(Delta/2T) of Theorem 41 is TARGET-INDEPENDENT, while the number below is TARGET-CONDITIONED because it "
    "inserts |kappa| = T_2 -- it is a necessary CAPACITY bound conditioned on the target, not a target-blind constraint; the "
    "v3.3 phrase 'first target-blind constraint' is WITHDRAWN): |kappa| = T_2 under Theorem 41 requires tanh(Delta/2T) >= T_2, "
    "i.e. T/Delta <= 1/(2 artanh T_2) = %s "
    "for the single-mode carrier (eps = 0 saturates it); the k_perp-integrated band ensemble of Cor. 26.3 sharpens this "
    "to T/Delta = %s at eps = 0. Any seam rest frame warmer than 0.4147 Delta cannot carry a record of magnitude T_2 on this "
    "route, whatever tangential datum it supplies. This is ONE NECESSARY CONDITION on the object D-S14-EVENT-001 asks for, not "
    "its discharge (Cor. 41.2 as re-scoped in v3.2). CONDITIONAL on the identification"
    % (mp.nstr(T2, 6), mp.nstr(T_over_D, 6), mp.nstr(T_ens, 6)),
    bool(T_over_D > mp.mpf('0.4146')) and bool(T_over_D < mp.mpf('0.4148')) and bool(T_ens < T_over_D),
    "T/Delta <= %s ; ensemble value %s ; target T_2 = %s" % (mp.nstr(T_over_D, 8), mp.nstr(T_ens, 6), mp.nstr(T2, 8)))

# V33  K9b: the equal-density eigenvalue arithmetic, RETYPED in v3.3 (CONDITIONAL on the OPEN items C99d/e of D36)
mc_, mu__ = mp.mpf('1.27'), mp.mpf('0.00216')
yc_over_yt, yu_over_yt = mc_ / mt_, mu__ / mt_          # y = sqrt2 m / v cancels v
enh_c = yc_over_yt / T2                                  # |D_12|/D_tt <= (y_c/y_t) sqrt(n_c/n_t) / kappa at n_c = n_t (Cauchy-Schwarz, record-band normalisation)
Dcc_eq = yc_over_yt**2 / T2                              # D_cc/D_tt <= (y_c/y_t)^2 (Tr G_cc / Tr G_tt) / kappa at equal density
lam_eq = (1 + Dcc_eq) / 2 + mp.sqrt(((1 - Dcc_eq) / 2)**2 + enh_c**2)   # lambda_max(D)/D_tt upper bound at equal density
row("V33", "V", "K9b, EQUAL-DENSITY ARITHMETIC ONLY (retyped v3.3; the v3.2 reading as a conditional rejection is WITHDRAWN): "
    "for the charge-2/3 partners of the top wall, IF the flavour matrix D were the admission quantity (C99d/e: OPEN, D36), "
    "then at equal band densities Cauchy-Schwarz on a positive G gives |D_12|/D_tt <= (y_c/y_t)/kappa = %s and "
    "D_cc/D_tt <= (y_c/y_t)^2/kappa = %s, so lambda_max(D)/D_tt <= %s -- an eigenvalue correction below 1 percent. "
    "THIS ROW DOES NOT establish a required partner density: W16 shows that with D_cc retained the audit's rank-one "
    "family reaches lambda_max/D_tt = 42.07 at n_c/n_t = 7.4e5, not at the 2.2e7 v3.2 printed (which dropped D_cc); and "
    "neither number is an admission criterion until D36 is closed. K9b: OPEN"
    % (mp.nstr(enh_c, 4), mp.nstr(Dcc_eq, 3), mp.nstr(lam_eq, 6)),
    bool(enh_c < mp.mpf('0.01')) and bool(lam_eq < mp.mpf('1.01')) and bool(lam_eq >= 1),
    "|D_12|/D_tt <= %s ; D_cc/D_tt <= %s ; lambda_max/D_tt <= %s at equal density" % (mp.nstr(enh_c, 6), mp.nstr(Dcc_eq, 4), mp.nstr(lam_eq, 8)))

om_tc = 2 * mp.sqrt(mt_ * mc_) / (mt_ + mc_); om_tu = 2 * mp.sqrt(mt_ * mu__) / (mt_ + mu__)
sup_tc = (mc_ / mt_) * om_tc; sup_tu = (mu__ / mt_) * om_tu
row("V34", "V", "LEMMA 39.10 EVALUATED (SM masses m_t = 171.872, m_c = 1.27, m_u = 0.00216 GeV; dps 60): omega_tc = %s, omega_tu = %s; "
    "the coherent channel's Yukawa-and-overlap weight relative to the top diagonal channel, (y_c/y_t) omega_tc = %s and "
    "(y_u/y_t) omega_tu = %s. These are the FIXED factors of the coherent onset condition of Thm 39.11; the interband "
    "response factor that multiplies them is NOT computed here (Proof obligation 39.8'), so this row states no admission verdict"
    % (mp.nstr(om_tc, 5), mp.nstr(om_tu, 5), mp.nstr(sup_tc, 5), mp.nstr(sup_tu, 4)),
    bool(om_tc < 1) and bool(om_tu < om_tc) and bool(sup_tc < mp.mpf('0.002')) and bool(sup_tc > mp.mpf('0.001')),
    "omega_tc = %s ; omega_tu = %s ; (y_c/y_t) omega_tc = %s ; (y_u/y_t) omega_tu = %s" % (mp.nstr(om_tc, 8), mp.nstr(om_tu, 8), mp.nstr(sup_tc, 8), mp.nstr(sup_tu, 8)))
# W16  the v3.2 audit's counterexample family, reproduced (numpy): positivity alone does not imply v3.2's density ratio
_g0 = np.diag([1, 1, -1, -1]).astype(complex)
def _gk(sig): return np.block([[np.zeros((2, 2)), sig], [-sig, np.zeros((2, 2))]]).astype(complex)
_g1, _g2, _g3 = _gk(np.array([[0, 1], [1, 0]], complex)), _gk(np.array([[0, -1j], [1j, 0]])), _gk(np.array([[1, 0], [0, -1]], complex))
_g5 = 1j * _g0 @ _g1 @ _g2 @ _g3; _A = _g0 @ _g3 @ _g5
_w, _v = np.linalg.eigh(_A); _k = float(T2)
_u = np.sqrt((1 + _k) / 2) * _v[:, 3] + np.sqrt((1 - _k) / 2) * _v[:, 0]          # u^dag A u = kappa = T_2
_q = float(yc_over_yt); _target = float(short["top"])
def _lam_family(r):
    W_ = np.concatenate([_u, np.sqrt(r) * _A @ _u]); G_ = np.outer(W_, W_.conj())
    M_ = np.diag([1, 1, 1, 1, _q, _q, _q, _q]).astype(complex); F_ = M_ @ G_ @ M_
    D_ = np.array([[np.trace(_A @ F_[:4, :4]), np.trace(_A @ F_[:4, 4:])], [np.trace(_A @ F_[4:, :4]), np.trace(_A @ F_[4:, 4:])]]) / 4
    Dn_ = D_ / D_[0, 0].real
    return float(np.max(np.linalg.eigvalsh(Dn_))), Dn_, float(np.min(np.linalg.eigvalsh(G_)))
r_audit = float(mp.findroot(lambda r: (1 + _q**2 * r) / 2 + mp.sqrt(((1 - _q**2 * r) / 2)**2 + (_q * mp.sqrt(r) / T2)**2) - _target, 7e5))
lam_r, Dn_r, gmin = _lam_family(r_audit)
r_v32 = float(((short["top"] - 1) * T2 / yc_over_yt)**2)
lam_v32, _, _ = _lam_family(r_v32)
row("W16", "W", "COUNTEREXAMPLE FAMILY OF THE v3.2 AUDIT, REPRODUCED (numpy; witness, not a theorem): with A = N gamma5, a unit "
    "spinor u with u^dag A u = kappa = T_2, and the rank-one positive block matrix G = w w^dag, w = (u, sqrt(r) A u), the "
    "flavour matrix is D/D_tt = [[1, q sqrt(r)/kappa], [q sqrt(r)/kappa, q^2 r]] with q = y_c/y_t. Solving lambda_max = %s "
    "(the top shortfall) gives r = n_c/n_t = %s -- explicit construction: lambda_max = %s, min eig(G) >= -1e-8 (positive to "
    "rounding; v3.4: the measured residual is in the detail field, not in this claim -- same retyping as W15). At v3.2's r = %s "
    "the same family gives lambda_max = %s, far above the target: v3.2's 'needed density ratio' "
    "dropped the charm diagonal D_cc = q^2 r D_tt. Neither r is an admission criterion (D36); the witness shows only that "
    "positivity of G alone does not fix a required density ratio"
    % (mp.nstr(short["top"], 6), mp.nstr(r_audit, 6), "%.5f" % lam_r, mp.nstr(r_v32, 4), "%.1f" % lam_v32),
    abs(lam_r - _target) < 1e-6 and gmin > -1e-8 and lam_v32 > 5 * _target and abs(Dn_r[1, 1].real - _q**2 * r_audit) < 1e-9,
    "r_audit = %.1f ; lambda_max(r_audit) = %.6f ; D_cc/D_tt = %.4f ; lambda_max(r_v32) = %.1f ; min eig(G) = %.1e" % (r_audit, lam_r, Dn_r[1, 1].real, lam_v32, gmin))

# ============================================================================
# W14  the carrier-level witness for the selector signature (kill tests K1-K3 run on the corpus chain)
# ============================================================================
sx_n = np.array([[0, 1], [1, 0]], complex); sy_n = np.array([[0, -1j], [1j, 0]]); sz_n = np.array([[1, 0], [0, -1]], complex)
JE_n = -sz_n
def liou(H, Ls):
    I = np.eye(2); L = -1j * (np.kron(H, I) - np.kron(I, H.T))
    for Lk in Ls:
        LdL = Lk.conj().T @ Lk
        L += np.kron(Lk, Lk.conj()) - 0.5 * np.kron(LdL, I) - 0.5 * np.kron(I, LdL.T)
    return L
def stationary(L):
    w, v = np.linalg.eig(L); idx = np.where(abs(w) < 1e-9)[0]
    return idx, v[:, idx]
Dl, x = 1.0, 3.0
H0 = 0.5 * Dl * JE_n
idx_a, _ = stationary(liou(H0, [np.sqrt(0.5) * JE_n]))                       # Thm-27 channel: QND dephasing
lower = np.array([[0, 1], [0, 0]], complex); raise_ = lower.conj().T
gd, nB = 0.3, 1 / (np.exp(x) - 1)
idx_b, vb = stationary(liou(H0, [np.sqrt(gd * (nB + 1)) * lower, np.sqrt(gd * nB) * raise_]))
rho_b = vb[:, 0].reshape(2, 2); rho_b = rho_b / np.trace(rho_b); kap_b = float(np.real(np.trace(rho_b @ JE_n)))
thn = 2.17294; Xn = -np.sin(thn) * sx_n + np.cos(thn) * sy_n
kaps = []
for eps in (0.3, 1.0):
    idx_c, vc = stationary(liou(H0 + eps * Xn, [np.sqrt(gd * (nB + 1)) * lower, np.sqrt(gd * nB) * raise_]))
    rc = vc[:, 0].reshape(2, 2); rc = rc / np.trace(rc); kaps.append((len(idx_c), float(np.real(np.trace(rc @ JE_n)))))
x_star = 2 * mp.atanh(T2)
row("W14", "W", "CARRIER-LEVEL WITNESS (one qubit, Lindblad, numpy): (a) the Theorem-27 channel alone -- a jump "
    "operator proportional to J_E -- is QND dephasing whose stationary manifold is the whole J_E-diagonal family "
    "(dimension 2): a formal QND event with NO selected record value (kill test K1/K2 on the contact channel: the "
    "pointer J_E is fixed, the value is not); (b) rest-frame thermal damping in the J_E basis (Thm 26.1's "
    "environment) has a UNIQUE faithful stationary state with kappa = -tanh(Delta/2T) exactly (here -0.905148 at "
    "Delta/T = 3); (c) adding a flip-odd Hamiltonian term eps X_theta -- the on-shell image of a tangential vector "
    "datum (C90) -- keeps uniqueness and moves kappa continuously (-0.7702 at eps/Delta = 0.3, -0.3072 at 1.0). "
    "(d) kill test K3: reaching |kappa| = T_2 in (b) (kappa = -T_2 in this sign convention) needs Delta/T = 2 artanh(T_2) = %s, a number read from lambda. "
    "The witness shows the signature of the missing object, not its construction" % mp.nstr(x_star, 6),
    len(idx_a) == 2 and len(idx_b) == 1 and abs(kap_b + np.tanh(x / 2)) < 1e-9 and all(n == 1 for n, _ in kaps)
    and abs(kaps[0][1] - kap_b) > 0.05 and min(np.linalg.eigvalsh(rho_b)) > 0,
    "dim stat: dephasing 2, thermal 1 ; kappa_b = %.6f ; kappa(eps=0.3) = %.6f ; kappa(eps=1) = %.6f" % (kap_b, kaps[0][1], kaps[1][1]))


# ============================================================================
# W15  lattice witness for Theorem 38.3, with the honest outcome of its controls (Observation 38.6)
# ============================================================================
def _lattice_axial(mode, Nl=40, a=0.1, k1=0.3, k2=0.4, m_=1.0, t_=0.4, th_=2.17, r_=1.0, seed=1):
    rng_ = np.random.default_rng(seed)
    g0n = np.diag([1, 1, -1, -1]).astype(complex)
    def gkn(sig): return np.block([[np.zeros((2, 2)), sig], [-sig, np.zeros((2, 2))]]).astype(complex)
    g1n, g2n, g3n = gkn(sx_n), gkn(sy_n), gkn(sz_n)
    g5n = 1j * g0n @ g1n @ g2n @ g3n; I4 = np.eye(4)
    hf = (-1j) * (g0n @ g3n) / (2 * a) - (r_ / (2 * a)) * g0n; hb = (1j) * (g0n @ g3n) / (2 * a) - (r_ / (2 * a)) * g0n
    Hf = np.zeros((4 * Nl, 4 * Nl), complex)
    for n_ in range(Nl):
        onsite = g0n @ (g1n * k1 + g2n * k2) + g0n @ (m_ * (np.cos(t_) * I4 + 1j * np.sin(t_) * g5n)) + (r_ / a) * g0n
        if mode == "mu(x)":   onsite = onsite + 0.2 * np.sin(0.5 * n_) * I4          # C-even: breaks {C,H} = 0
        if mode == "noise":   A_ = rng_.normal(size=(4, 4)) + 1j * rng_.normal(size=(4, 4)); onsite = onsite + 0.1 * (A_ + A_.conj().T)
        Hf[4*n_:4*n_+4, 4*n_:4*n_+4] = onsite
        if n_ + 1 < Nl:
            Hf[4*n_:4*n_+4, 4*(n_+1):4*(n_+1)+4] = hf; Hf[4*(n_+1):4*(n_+1)+4, 4*n_:4*n_+4] = hb
    Bn = np.cos(th_) * (1j * g3n) + np.sin(th_) * (g3n @ g5n)
    w, v = np.linalg.eigh(Bn); V0 = v[:, np.isclose(w, 1.0)]
    V = np.zeros((4 * Nl, 2 + 4 * (Nl - 1)), complex); V[0:4, 0:2] = V0; V[4:, 2:] = np.eye(4 * (Nl - 1))
    Hr = V.conj().T @ Hf @ V
    E, W = np.linalg.eigh(Hr); full = V @ W
    Es = np.sort(E); sym = float(np.max(np.abs(Es + Es[::-1])))
    dens = np.array([[float(np.real(full[4*x_:4*x_+4, n_].conj() @ g5n @ full[4*x_:4*x_+4, n_])) for x_ in range(Nl)] for n_ in range(len(E))])
    permode = float(np.max(np.abs(dens)))
    stt = max(float(np.max(np.abs(np.exp(-E**2 / L_**2) @ dens))) for L_ in (1.0, 3.0))
    ndeg = int(np.sum(np.diff(Es) < 1e-8))
    return sym, permode, stt, ndeg
symA, pmA, stA, ndA = _lattice_axial("bag")
symB, pmB, stB, ndB = _lattice_axial("mu(x)")
symC, pmC, stC, ndC = _lattice_axial("noise")
row("W15", "W", "LATTICE WITNESS FOR THEOREM 38.3 AND OBSERVATION 38.6 (numpy; half-space, 40 sites, a = 0.1, Wilson r = 1 to "
    "remove doublers, k_perp = (0.3, 0.4), m = 1, theta_m = 0.4, chiral-bag condition at site 0 by projection onto "
    "L_theta; v3.4 RETYPED to THRESHOLD form -- the measured residuals live in the detail field, because a claim text that "
    "embeds a 1e-16 residual is not byte-stable across machines and silently moved G18's carried count): (i) spectrum "
    "E <-> -E symmetric to <= 1e-9, non-degenerate (%d coincident levels), and the local supertrace "
    "Sum_n exp(-E_n^2/Lambda^2) phi_n(x)^dag gamma5 phi_n(x) <= 1e-9 at every site for Lambda = 1, 3 -- the CONCLUSION of "
    "Theorem 38.3 holds. (ii) HONEST CONTROL OUTCOME: on this lattice the axial density vanishes LEVEL BY LEVEL, "
    "max_n,x |phi_n(x)^dag gamma5 phi_n(x)| <= 1e-9, so a C-even perturbation mu(x) that breaks {C, H} = 0 (spectral "
    "asymmetry > 1e-3) does NOT raise the supertrace (<= 1e-9) -- the lattice vanishing is stronger than, and not a test of, "
    "the C-pairing mechanism; this level-wise vanishing is reported as Observation 38.6, unexplained, [열림]. (iii) A "
    "generic Hermitian onsite perturbation (C-breaking and polarisation-mixing) raises the per-mode density above 1e-4 and "
    "the supertrace above 1e-6: the check CAN fail. Theorem 38.3's proof is the algebraic pairing of C94, not this witness"
    % (ndA,),
    symA < 1e-9 and stA < 1e-9 and pmA < 1e-9 and symB > 1e-3 and stB < 1e-9 and pmC > 1e-4 and stC > 1e-6,
    "bag: sym %.1e per-mode %.1e supertrace %.1e | mu(x): sym %.1e supertrace %.1e | noise: per-mode %.1e supertrace %.1e"
    % (symA, pmA, stA, symB, stB, pmC, stC))

# ============================================================================
# REGISTRY  (replaces the four hard-coded strings of v2.9's C88)
# ============================================================================
def adm(G4m2):  # admission predicate of Theorem 36 (per band, C87)
    return bool(G4m2 >= req)
REGISTRY = [
    {"id": "K1", "source": "ZS-S14 v2.1 / M66 sect.6 Yukawa (Lemma 36.1)", "mediator": "Higgs h, scalar contact",
     "coupling": "contact (psibar psi)^2, d-channel via Fierz", "band": "top, N_b = 3 (colour)", "G4m2": avail["top"], "class": "corpus"},
    {"id": "K2", "source": "same, weak doublet", "mediator": "Higgs h, scalar contact", "coupling": "contact",
     "band": "top+bottom, N_b = 6 (diagonal mean field)", "G4m2": max(avail["top"], avail["bottom"]), "class": "corpus"},
    {"id": "K3", "source": "same", "mediator": "Higgs h, scalar contact", "coupling": "contact", "band": "bottom / charm / tau, one band each",
     "G4m2": max(avail["bottom"], avail["charm"], avail["tau"]), "class": "corpus"},
    {"id": "K4", "source": "ZS-S14 sect.2.11 Goldstone theta, Horn A", "mediator": "theta (massless), non-derivative via mass phase",
     "coupling": "effective potential Gamma(A)", "band": "any", "G4m2": None, "class": "corpus", "verdict_rule": "C85: stationary only at pi Z -> no admissible angle"},
    {"id": "K5", "source": "ZS-S14 sect.2.11 Goldstone theta, Horn B, vector charge", "mediator": "theta, derivative d theta J_V",
     "coupling": "linear bulk derivative", "band": "any", "G4m2": mp.mpf(0), "class": "corpus", "verdict_rule": "C86(V): exactly removable"},
    {"id": "K6", "source": "ZS-S14 sect.2.11 Goldstone theta, Horn B, axial charge", "mediator": "theta, derivative d theta J_A",
     "coupling": "linear bulk derivative + axial boundary flux 2 J_E", "band": "any", "G4m2": mp.mpf(0), "class": "corpus",
     "verdict_rule": "C86(A): record-blind at zeroth gradient order; explicit breaking by m"},
    {"id": "K7", "source": "ZS-S14 sect.2.11 Goldstone theta, shift-symmetric residual", "mediator": "theta, dim>=6 bulk or boundary-localised gradient",
     "coupling": "(c/f^2) or (c/f) d_a theta psibar gamma^a psi -> flip-odd on carrier (C90)", "band": "any",
     "G4m2": req / f_short, "class": "corpus-conditional", "verdict_rule": "V28/V31: 1/M_P^2 suppressed; CONDITIONAL on f = M_P"},
    {"id": "K8", "source": "sect.21.4 (ii): non-SM fermion heavier than its own mediator", "mediator": "unspecified, strongly coupled",
     "coupling": "non-contact", "band": "unspecified", "G4m2": None, "class": "corpus-external"},
    {"id": "K9a", "source": "sect.22.3 / 22.8: COLOUR-off-diagonal or CHARGE-changing boundary condensate <psibar_i Gamma psi_j>",
     "mediator": "Higgs contact, off-diagonal Fock block", "coupling": "contact, C92 hypothesis violated; gauge-VARIANT", "band": "N_b >= 2",
     "G4m2": None, "class": "corpus", "verdict_rule": "C96: gauge-variant, vanishes by Elitzur (Thm 39.4, K9a)"},
    {"id": "K9b", "source": "sect.22.8: SAME-gauge-representation generation-flavour coherence <psibar_t Gamma psi_c>, colour singlet",
     "mediator": "Higgs contact, off-diagonal Fock block y_t y_c G_tc (C99a)", "coupling": "contact; gauge-INVARIANT; admission quantity for a coherent carrier NOT derived (D36)",
     "band": "top + charm (or up), N_b = 2 coherent", "G4m2": None, "class": "corpus-open",
     "verdict_rule": "Theorem 36 does not apply to a coherent carrier; no admission criterion exists (D36, Proof obligation 39.8): OPEN"},
    {"id": "K10", "source": "sect.21.4 (iv): record value below T_2", "mediator": "n/a", "coupling": "n/a", "band": "n/a",
     "G4m2": None, "class": "excluded-by-identification"},
]
for e in REGISTRY:
    e["admitted"] = None if e["G4m2"] is None else adm(e["G4m2"])
    if e["admitted"] is True:
        e["status"] = "ADMITTED"
    elif e.get("verdict_rule") and e["class"] == "corpus":
        e["status"] = "REJECTED-STRUCTURAL"
    elif e["admitted"] is False:
        e["status"] = "REJECTED-BY-BOUND"
    elif e["class"] == "corpus-open":
        e["status"] = "OPEN"
    else:
        e["status"] = "EXTERNAL-UNEVALUABLE" if e["class"] == "corpus-external" else "NOT-A-CANDIDATE"
    e["G4m2_str"] = None if e["G4m2"] is None else mp.nstr(e["G4m2"], 6)
n_adm = sum(1 for e in REGISTRY if e["admitted"] is True)
n_corpus_eval = sum(1 for e in REGISTRY if e["admitted"] is not None)
n_struct = sum(1 for e in REGISTRY if e["status"] == "REJECTED-STRUCTURAL")
n_ext = sum(1 for e in REGISTRY if e["status"] == "EXTERNAL-UNEVALUABLE")
n_cond = sum(1 for e in REGISTRY if e["class"] == "corpus-conditional")
n_open = sum(1 for e in REGISTRY if e["status"] == "OPEN")
row("V30", "V", "CANDIDATE REGISTRY, EVALUATED (v3.3: K9b retyped OPEN): %d entries; the admission predicate "
    "G_4 m^2 >= %s is COMPUTED for every entry that carries a corpus number (%d entries) and none is admitted "
    "(%d admitted); %d entries are structurally rejected by a certified rule (C85, C86, C96; K5/K6 also carry the number 0); "
    "%d is corpus-external and UNEVALUABLE (K8 heavy-fermion sector); %d is a CONDITIONAL rejection (K7 on f = M_P) and is "
    "NOT counted as closed; %d is OPEN with no admission criterion (K9b: Theorem 36 does not apply to a coherent carrier, D36); "
    "K10 is not a candidate; K9a closed by Thm 39.4. Quantifier owned by the verifier: 'every registered candidate', not "
    "'every candidate'"
    % (len(REGISTRY), mp.nstr(req, 6), n_corpus_eval, n_adm, n_struct, n_ext, n_cond, n_open),
    n_adm == 0 and n_corpus_eval == 6 and n_struct == 4 and n_ext == 1 and n_cond == 1 and n_open == 1 and len(REGISTRY) == 11,
    " | ".join("%s:%s" % (e["id"], e["status"]) for e in REGISTRY))

FIELDS = ("id", "source", "mediator", "coupling", "band", "class", "status")
complement_map = {"(i) non-contact mediator": ("K4", "K5", "K6", "K7"), "(ii) heavier-than-mediator fermion": ("K8",),
                  "(iii) multi-band": ("K2", "K9a", "K9b"), "(iv) below T_2": ("K10",)}
ids = [e["id"] for e in REGISTRY]
row("C88", "G", "REGISTRY INTEGRITY (RETYPED C -> G; v2.9 counted four hard-coded strings): every entry carries the "
    "fields %s; every sect.21.4 complement item maps to >= 1 entry; ids are unique" % (FIELDS,),
    all(all(f in e and e[f] for f in FIELDS) for e in REGISTRY) and len(set(ids)) == len(ids)
    and all(all(k in ids for k in v) for v in complement_map.values()),
    "complement map: " + " ; ".join("%s -> %s" % (k, ",".join(v)) for k, v in complement_map.items()))

# ============================================================================
# R / G / D
# ============================================================================
row("R16", "R", "control: seed %d, mpmath dps 60; the C block uses no floating-point tolerance; W14 uses a 1e-9 "
    "null-space threshold on a 4x4 Liouvillian" % SEED, mp.mp.dps == 60, "dps=%d" % mp.mp.dps)
STRENGTH = ("no-go", "unital", "faithful", "selects", "torsor", "free", "unique",
            "exactly", "never", "strictly", "spurious")
BOUND = {"C85": ("exactly", "unique"), "C93": ("exactly", "strictly"), "C89": ("exactly", "free", "never"), "C90": (),
         "C86": ("exactly", "free", "no-go"), "C91": ("exactly", "never"), "C92": (), "C87": ("free",), "V27": (), "V28": (), "V31": (),
         "W14": ("unique", "faithful", "exactly", "selects"), "V30": (), "C94": ("exactly", "never"), "C95": ("exactly",),
         "C96": ("exactly",), "C97": ("unique", "exactly", "never"), "C98": ("exactly", "free"), "V32": (), "W15": (),
         "C99a": (), "C99b": ("never",), "C99c": (), "V33": (), "W16": (), "C100": (), "C101": ("never",), "C102": (), "V34": ()}
ev_rows = [r for r in ROWS if r["class"] in ("C", "V", "W", "P")]
unbound = sorted({(r["id"], w) for r in ev_rows for w in STRENGTH
                  if w in r["claim"].lower() and w not in BOUND.get(r["id"], ())})
probe_caught = any(w in "this row is freely torsor unital and never fails" for w in STRENGTH)
row("G15", "G", "STRONG-PREDICATE BINDING", len(unbound) == 0 and probe_caught,
    "unregistered = %s ; probe = %s" % (unbound, probe_caught))
UNIV = ("universal", "every", "for all", " all ", "identically", "free symbols")
bad_univ = sorted({r["id"] for r in ev_rows if any(w in r["claim"].lower() for w in UNIV) and not r["universal"]})
bad_univ = [b for b in bad_univ if b not in ("V30", "W15")]   # V30: bound to the registry; W15: 'every site' of ONE lattice, a witness
row("G19", "G", "UNIVERSAL-QUANTIFIER BINDING (V30's quantifier is bound to the registry; W15's 'every site' is one lattice)",
    len(bad_univ) == 0, "%s" % bad_univ)
row("G16", "G", "class discipline: P = 0", len([r for r in ROWS if r["class"] == "P"]) == 0, "")
row("G20", "G", "TYPING GUARD, sections 19-25 (v3.3: CLAIM-STATE sentence rule; v3.4: physical-bridge sentence rule (iv)): (i) each of 19-22 must carry "
    "'mean field' and 'DERIVED-CONDITIONAL'; section 20 'IMPORTED'; section 21 'CLOSED-NEGATIVE' and 'KILLED'; section 22 "
    "'CLOSED-NEGATIVE-CONDITIONAL', 'STRUCTURAL SURVIVOR', 'K9a', 'K9b', 'necessary condition' and 'OPEN'; section 23 "
    "'AUDIT-RESEARCH-REOPEN', 'WITHDRAWN', 'FREEZE-CANDIDATE' and 'WITHHELD'; (ii) every SENTENCE of sect.22.9 that contains "
    "'discharge' must contain a negation, a retraction marker or a conditional form (not / never / neither / no / withdrawn / retracted / require(s|d) / still / owed / must satisfy / would / necessary condition), so "
    "that flipping 'It is not its discharge' to 'It is its discharge' FAILS (the v3.2 audit's injection); (iii) sect.22.8 must "
    "not contain a live 'REJECTED-BY-BOUND' for K9b outside a retraction sentence; (iv) v3.4 (v3.3 audit S2): every SENTENCE "
    "of sect.25 that says the missing object is 'completely specified' must also say that it is NOT constructed (a negation "
    "or the marker 'signature'/'not constructed'), and the phrases 'all now derived' and 'first target-blind' may not occur "
    "live anywhere in the manuscript, so that the v2.6 sentence the v3.3 audit flagged FAILS when re-injected. LIMIT: (ii)-(iv) "
    "are sentence-level relation rules, not semantics; a paraphrase without the guarded words is not caught and is said so in sect.1",
    True, "evaluated at report time")
row("G23", "G", "TYPE LOCK + INTERNAL VERSION CONSISTENCY (CPN11; v3.3: symbol-table sentence rule added): (a) glyph rule -- in "
    "sect.22.9 the relaxation times are tau_1/tau_2 and the glyphs 'T\u2081' and '\u0394\u00b2T\u2082\u00b2' must not occur; (b) SYMBOL-TABLE rule -- "
    "every sentence of sect.22.9 that names a 'relaxation time' or 'dephasing time' must name tau_1 or tau_2 and must NOT name "
    "T_2, so that 'The transverse Bloch relaxation time is denoted T_2.' FAILS (the v3.2 audit's injection); (c) every row "
    "count the manuscript prints for artifact L must equal the measured row count; (d) no live run line may name a verifier "
    "other than this one for artifact L. LIMIT: (b) is a co-occurrence rule over sentences, not a type checker for prose",
    True, "evaluated at report time")
row("G24", "G", "CLAIM-STATE MANIFEST (new in v3.3; VERIFY sect.7.2 S4 -- relations are declared by explicit tokens and the guard "
    "reads only those): the manuscript carries a machine-readable CLAIM-STATE block; every registry id it declares must "
    "equal the status this ledger COMPUTED for that id, FREEZE-CANDIDATE must be WITHHELD and appear as such in sect.23, "
    "D-S14-EVENT-001 must be NECESSARY-CONDITION-SUPPLIED, Cor38.7 and C99e must be OPEN, C99d must be CLOSED-NEGATIVE-LINEAR "
    "(v3.4, Thm 39.11), MissingObject must be SPECIFIED-NOT-CONSTRUCTED, ThermalCeiling must be TARGET-INDEPENDENT and "
    "T-over-Delta must be TARGET-CONDITIONED (v3.4, v3.3 audit S2), the symbol table must declare T2=TARGET and "
    "tau1,tau2=RELAXATION, and artifactL.rows must equal the measured count. Live-fire: K9b=REJECTED-BY-BOUND in the block -> FAIL", True, "evaluated at report time")
row("G25", "G", "PACKAGE OBJECT GRAPH (new in v3.4; v3.3 audit S2-3; VERIFY sect.9.1, CPN1/CPN2): the manuscript's sect.27 package "
    "block declares an authoritative core and a provenance-object list; the core it declares must be EXACTLY the four objects "
    "this script registers in the manifest's core (manuscript, verifier, ledger, release manifest) -- neither the session file "
    "nor any other companion may be declared core -- and the session, audit report and provenance supplement must be "
    "declared as provenance objects, which the manifest registers with measured hashes. Live-fire: adding the session file "
    "to the core line -> FAIL", True, "evaluated at report time")
self_sha = hashlib.sha256(open(SELF, "rb").read()).hexdigest()
CORE_OBJECTS = ("manuscript", "verifier", "ledger", "manifest")
PROVENANCE_OBJECTS = ("session", "audit", "supplement")
def _sentences(block):
    # v3.4: whitespace inside a sentence is normalised, so a guarded phrase broken across a line ('completely\nspecified') is still seen
    return [re.sub(r"\s+", " ", t).strip() for t in re.split(r"(?<=[.!?])\s+(?=[A-Z\u2018\u201c\"*(`])|\n\s*\n", block) if t.strip()]
NEG_RE = re.compile(r"\b(not|never|neither|nor|no|withdrawn|retracted|requires?|required|still|owed|must satisfy|would)\b|necessary condition", re.I)
if os.path.exists(PAPER):
    txt = open(PAPER, encoding="utf-8").read()
    m_ = re.search(r"artifact L[^\n]*\n[^\n]*sha256\s*=\s*([0-9a-f]{64})", txt)
    printed = m_.group(1) if m_ else None
    row("G17", "G", "the artifact-L hash is MEASURED against the manuscript banner", printed == self_sha,
        "script = %s ; banner = %s" % (self_sha, printed))
    secs = {n: txt[txt.find("## %d." % n):txt.find("## %d." % (n + 1))] for n in (19, 20, 21, 22, 23, 25)}
    i229, i2210 = txt.find("### 22.9"), txt.find("### 22.10")
    blk41 = txt[i229:i2210] if (i229 >= 0 and i2210 > i229) else ""
    i228 = txt.find("### 22.8"); blk39 = txt[i228:i229] if (i228 >= 0 and i229 > i228) else ""
    tok20 = (all(("mean field" in secs[n].lower()) and ("DERIVED-CONDITIONAL" in secs[n]) for n in (19, 20, 21, 22))
             and ("IMPORTED" in secs[20]) and ("CLOSED-NEGATIVE" in secs[21]) and ("KILLED" in secs[21])
             and ("CLOSED-NEGATIVE-CONDITIONAL" in secs[22]) and ("STRUCTURAL SURVIVOR" in secs[22])
             and ("K9a" in secs[22]) and ("K9b" in secs[22]) and ("necessary condition" in secs[22]) and ("OPEN" in secs[22])
             and ("AUDIT-RESEARCH-REOPEN" in secs[23]) and ("WITHDRAWN" in secs[23]) and ("FREEZE-CANDIDATE" in secs[23])
             and ("WITHHELD" in secs[23]))
    bad_discharge = [t[:80] for t in _sentences(blk41) if "discharge" in t.lower() and not NEG_RE.search(t)]
    bad_k9b = [t[:80] for t in _sentences(blk39) if "REJECTED-BY-BOUND" in t and "K9b" in t and not any(w in t.lower() for w in ("withdrawn", "retract", "not ", "no longer"))]
    # (iv) v3.4: physical-bridge sentence rule over sect.25, plus two live-phrase bans over the whole manuscript
    BRIDGE_OK = re.compile(r"\b(not constructed|no such|signature|is not|are not|not a construction|specification)\b", re.I)
    bad_bridge = [t[:80] for t in _sentences(secs.get(25, "")) if "completely specified" in t.lower() and not BRIDGE_OK.search(t)
                  and "~~" not in t and not re.search(r"withdrawn|retract|replaced", t, re.I)]
    BAN_EXEMPT = re.compile(r"(withdrawn|retract|replace|~~|flagged|may not occur|banned|\bban\b|guard|inject|struck|\ucca0\ud68c|\uad50\uccb4)", re.I)
    live_ban = [w for w in ("all now derived", "first target-blind") if any(w in s and not BAN_EXEMPT.search(s) for s in _sentences(txt))]
    ok20 = tok20 and not bad_discharge and not bad_k9b and not bad_bridge and not live_ban
    for r in ROWS:
        if r["id"] == "G20":
            r["result"] = "PASS" if ok20 else "FAIL"
            r["detail"] = "tokens = %s ; unguarded 'discharge' sentences in 22.9 = %s ; live K9b REJECTED in 22.8 = %s ; unguarded 'completely specified' in 25 = %s ; live banned phrases = %s" % (tok20, bad_discharge, bad_k9b, bad_bridge, live_ban)
    glyph_ok = bool(blk41) and ("\u03c4\u2081" in blk41) and ("\u03c4\u2082" in blk41) and ("T\u2081" not in blk41) and ("\u0394\u00b2T\u2082\u00b2" not in blk41)
    bad_sym = [t[:80] for t in _sentences(blk41) if re.search(r"(relaxation|dephasing) time", t, re.I)
               and (("\u03c4\u2081" not in t and "\u03c4\u2082" not in t and "tau" not in t) or ("T\u2082" in t or "T_2" in t))]
    K_counts = [int(x) for x in re.findall(r"artifact L[^\n]*?\((\d+) rows", txt)] \
             + [int(x) for x in re.findall(r"zs_m67_verify_v3_4\.py[^\n]*?\((\d+) rows", txt)] \
             + [int(x) for x in re.findall(r"[Aa]rtifact L:\s*(\d+) rows", txt)] \
             + [int(x) for x in re.findall(r"artifact L[^\n]*\n\s*sha256[^\n]*\n\s*(\d+) rows", txt)]
    K_runs = re.findall(r"python3\s+(zs_m67_verify_v3_\d+\.py)[^\n]*artifact L", txt) + re.findall(r"run:\s+python3\s+(zs_m67_verify_v3_\d+\.py)", txt)
    # G25: the manuscript's package block (sect.27): core line and provenance-object line
    sec27 = txt[txt.find("## 27."):txt.find("## 28.")]
    pk_core = re.search(r"^package \(v3\.4 core[^\)]*\):\s*([^\n]+(?:\n\s{10,}[^\n]+)*)", sec27, re.M)
    pk_prov = re.search(r"^provenance objects[^\n]*?(?:\n[^\n]*?)?\):\s*([^\n]+(?:\n\s{10,}[^\n]+)*)", sec27, re.M)
    def _objs(s):
        s = s or ""
        found = set()
        if re.search(r"M67_v3_4\.md", s): found.add("manuscript")
        if "zs_m67_verify_v3_4.py" in s: found.add("verifier")
        if "zs_m67_verify_v3_4.json" in s: found.add("ledger")
        if "release_manifest_v3_4.json" in s: found.add("manifest")
        if "session_M67_v3_4" in s: found.add("session")
        if re.search(r"audit", s, re.I): found.add("audit")
        if "provenance_supplement" in s: found.add("supplement")
        return found
    G25_STATE = {"core_declared": sorted(_objs(pk_core.group(1) if pk_core else "")), "prov_declared": sorted(_objs(pk_prov.group(1) if pk_prov else "")),
                 "core_block_found": bool(pk_core), "prov_block_found": bool(pk_prov)}
    G23_STATE = {"glyph": glyph_ok, "bad_symbol_sentences": bad_sym, "K_counts": K_counts, "K_runs": K_runs}
    cs = re.search(r"<!--\s*CLAIM-STATE(.*?)-->", txt, re.S)
    CLAIM_STATE = dict(re.findall(r"^\s*([A-Za-z0-9_.\-,]+)\s*=\s*([A-Za-z0-9_\-]+)\s*$", cs.group(1), re.M)) if cs else None
else:
    row("G17", "G", "the artifact-K hash is MEASURED against the manuscript banner", False,
        "manuscript absent; sha256 = %s" % self_sha, degraded=True)
    for r in ROWS:
        if r["id"] in ("G20", "G23", "G24", "G25"):
            r["result"] = "DEGRADED"; r["detail"] = "manuscript absent"
    G23_STATE = None; CLAIM_STATE = None; secs = {}; G25_STATE = None
prov = {}
def finish_provenance():
    """G18: measured against the EMBEDDED artifact-J fingerprints; the artifact-J JSON, if present, is cross-checked."""
    global prov
    cur = {r["id"]: (r["class"], hashlib.sha256(r["claim"].strip().encode("utf-8")).hexdigest()[:16]) for r in ROWS}
    prev_ids, new_ids = set(BASELINE_FP), set(cur)
    carried = sorted(prev_ids & new_ids)
    retyped = sorted(i for i in carried if BASELINE_FP[i] != cur[i])
    reclassed = sorted(i for i in carried if BASELINE_FP[i][0] != cur[i][0])
    removed = sorted(prev_ids - new_ids)
    prov = {"baseline": "artifact K fingerprints embedded in this script (from the SHIPPED %s)" % BASELINE_LEDGER, "previous_rows": len(prev_ids),
            "final_rows_measured": len(new_ids), "carried_unchanged": len(carried) - len(retyped),
            "retyped_or_replaced": retyped, "class_changed": {i: "%s->%s" % (BASELINE_FP[i][0], cur[i][0]) for i in reclassed},
            "added": sorted(new_ids - prev_ids), "removed": removed,
            "removed_reason": "none removed; artifact K is superseded row-by-row" if not removed else "UNEXPECTED removal: see manuscript",
            "json_crosscheck": "absent (optional)", "degraded": False}
    ok = removed == []
    if os.path.exists(PREV_LEDGER):
        try:
            prevj = json.load(open(PREV_LEDGER, encoding="utf-8"))
            fpj = {r["id"]: (r["class"], hashlib.sha256(r["claim"].strip().encode("utf-8")).hexdigest()[:16]) for r in prevj.get("rows", [])}
            match = (fpj == BASELINE_FP)
            prov["json_crosscheck"] = "present: fingerprints %s the embedded baseline" % ("MATCH" if match else "DO NOT MATCH")
            ok = ok and match
        except Exception as ex:
            prov["json_crosscheck"] = "present but unreadable: %s" % ex; ok = False
    return ok
row("G18", "G", "ledger provenance MEASURED against the EMBEDDED artifact-K baseline (48 row fingerprints from the SHIPPED v3.3 ledger; "
    "the v3.3 JSON is optional and cross-checked when present) over the FINAL row set; no removal is expected and any "
    "removal FAILS. v3.4 note: the fingerprints of W15 and W16 are expected to change (claims retyped to threshold form) -- "
    "the shipped v3.3 claims embedded machine-dependent residuals (1e-16 supertrace; 1e-12 eigenvalue)", True, "computed at report time")
scan = {}
for fn in sorted(glob.glob(os.path.join(HERE, "zs_m67_verify_v*.py"))):
    t = open(fn, encoding="utf-8").read(); base = os.path.basename(fn)
    exit_ok = ("degs" in t and ("return 1 if fails else (2 if degs else 0)" in t or "def exit_code(" in t))
    run_lines = re.findall(r"run:\s+python3\s+(zs_m67_verify_v\d+_\d+\.py)", t)
    run_ok = all(r == base for r in run_lines) and len(run_lines) > 0
    scan[base] = {"exit_on_degraded": exit_ok, "docstring_run_line_current": run_ok}
lineage_all = ("v2_5", "v2_6", "v2_7", "v2_8", "v2_9", "v3_0", "v3_1", "v3_2", "v3_3")
not_shipped = [v for v in lineage_all if not any(v in k for k in scan)]
n_defect = sum(1 for v in scan.values() if not (v["exit_on_degraded"] and v["docstring_run_line_current"]))
self_base = os.path.basename(SELF)
row("G22", "G", "LINEAGE RESCAN (VERIFY sect.7.3) for the two v2.9 package defects -- exit 0 on DEGRADED and a stale "
    "docstring run line -- over every zs_m67_verify_v*.py present beside this script: %d script(s) scanned, %d with "
    "at least one defect, %d clean; siblings not shipped are reported as NOT SHIPPED = %s and are never counted as "
    "clean. Prior findings stand: artifact G (v2.9) fails both checks; H, I, J, K clean; C-F (v2_5-v2_8) NOT FOUND in "
    "project repo 2 -- UNAVAILABLE, not clean" % (len(scan), n_defect, len(scan) - n_defect, not_shipped),
    scan.get(self_base, {}).get("exit_on_degraded") is True and scan.get(self_base, {}).get("docstring_run_line_current") is True,
    json.dumps({"scan": scan, "not_shipped": not_shipped}, ensure_ascii=False))
def exit_code(rows):
    """the ONE exit-policy function; main() returns its value and G21 exercises it on synthetic row sets"""
    fails = [r for r in rows if r["result"] == "FAIL"]; degs = [r for r in rows if r["result"] == "DEGRADED"]
    if not rows: return 2                      # v3.4: an empty ledger is a degraded run, never a pass (v3.3 audit)
    return 1 if fails else (2 if degs else 0)
_syn = lambda *res: [{"result": x} for x in res]
g21_ok = (exit_code(_syn("PASS", "PASS")) == 0 and exit_code(_syn("PASS", "FAIL")) == 1 and exit_code(_syn("PASS", "DEGRADED")) == 2
          and exit_code(_syn("DEGRADED", "FAIL")) == 1 and exit_code([]) == 2)
row("G21", "G", "FAIL-CLOSED EXIT, FUNCTIONAL (v3.3; v3.4: the EMPTY ledger now exits 2 -- the v3.3 audit noted exit_code([]) == 0 "
    "was not fail-closed): the exit-policy function that main() returns is exercised on synthetic row sets -- {PASS,PASS} -> 0, "
    "{PASS,FAIL} -> 1, {PASS,DEGRADED} -> 2, {DEGRADED,FAIL} -> 1, {} -> 2. History: v2.9 exited 0 with G18 DEGRADED; the delivered v3.1 package gave exit 1 "
    "(G18 DEGRADED + G22 FAIL); the four-file v3.2 package as received by the auditor gave exit 2 (baseline ledger was a "
    "fifth file) -- repaired in v3.3 by embedding the baseline", g21_ok, "synthetic exit codes = %s ; empty -> %d" % ([exit_code(_syn("PASS")), exit_code(_syn("FAIL")), exit_code(_syn("DEGRADED")), exit_code(_syn("DEGRADED", "FAIL"))], exit_code([])))
row("D27", "D", "VERDICT (v3.4; unchanged from v3.3 except the K9b pointer): F-M66.17 is CLOSED-NEGATIVE, EXACTLY, for (a) every spectral route inside A1-A5, (b) the "
    "free-bulk route, (c) the Yukawa contact route on any number of COLOUR- and CHARGE-diagonal, generation-flavour-DIAGONAL "
    "bands -- colour/charge diagonality is a theorem (Thm 39.4, Elitzur, K9a closed), generation-flavour diagonality is a "
    "HYPOTHESIS (K9b OPEN: no admission criterion exists for a coherent carrier, D36), (d) the corpus Goldstone on Horn A "
    "inside A5, and (e) the corpus Goldstone's linear bulk couplings on Horn B, including the H^2-regularised spectral "
    "supertrace cancellation and the constant-alpha co-rotation inside A1-A4 (Thms 38.3, 38.4); the local-alpha(x) "
    "Jacobian with fixed bag domain is an OPEN proof obligation (Cor. 38.7). It is CLOSED-NEGATIVE-CONDITIONAL, on "
    "f = M_P, for the shift-symmetric residual (K7). The surviving set is {K7 on its condition, K8 corpus-external, K9b OPEN "
    "(corpus object)}. A5 remains a two-real-parameter upstream input (Cor. 37.2). The v3.2 sentences 'K9b REJECTED-BY-BOUND "
    "on n_partner <= n_top', 'unchanged bound' and 'n_c/n_t ~ 2e7 needed' are WITHDRAWN. v3.4: C99d CLOSED-NEGATIVE at linear order (Thm 39.11); C99e OPEN as Proof obligation 39.8' (D39)", True, "")
row("D28", "D", "RQ3 CONSEQUENCE (v3.4): OPEN -> OPEN. The route is closed inside the corpus up to the named conditions and "
    "one OPEN class (K9b), and REFORMULATED at the carrier: pointer J_E derived (Thm 20), event type QND (W14), record "
    "VALUE = rest-frame datum bounded by Theorem 41 (T/Delta <= 0.4147; |kappa| = T_2, kappa = -T_2 in the z_0 convention; the "
    "tangential datum can only lower |kappa|). ZS-S14 v2.1 supplies no rest-frame temperature, clock or tangential vector "
    "(read in v3.1) and registers the action-derived seam environment as debt D-S14-EVENT-001 (OPEN). WHAT M67 SUPPLIES TO "
    "THAT DEBT IS ONE NECESSARY CONDITION -- any thermal rest-frame route must satisfy T/Delta <= 0.4147 -- and NOT its "
    "discharge (Mission v1.4 RQ3, Definition 40: S4, S6, the action-derived environment and the instrument selection are "
    "still owed). 'The RQ3 residue and an RQ2 residue coincide' is [가설]: the RQ2 clock/rest-frame construction MAY supply "
    "one input of the RQ3 environment selection; identification requires a common action or a compatibility theorem "
    "(Mission v1.4 sect.4.2). The front-matter handoff is RQ2 -> RQ3 (v3.3 correction of 'RQ1 -> RQ3'). v3.4 typing (v3.3 audit S2): the ceiling is TARGET-INDEPENDENT, the number 0.4147 is TARGET-CONDITIONED (a capacity bound conditioned on |kappa| = T_2); the missing object is SPECIFIED by its signature and NOT CONSTRUCTED here", True, "")
row("D29", "D", "INDEPENDENCE: same-model re-execution only; no third-party clean-room; no proof assistant; "
    "qualified-human anchor NONE. Horn A inherits the A5 counterterm scope of Theorem 13. The quantum axial "
    "Jacobian with boundary (eta/inflow) is NOT computed here: C86(A) is a classical-plus-C50 statement and the "
    "anomaly question of Cor. 9.2 stays [열림] outside A4", True, "")
row("D30", "D", "MINIMAL SELECTOR SIGNATURE (Definition 40) and HANDOFF: an admissible boundary-record sector must be "
    "(S1) action-derived with no coefficient read from lambda or T_2, (S2) genuinely external with a boundary rest "
    "frame (A6) and a flip-odd component (Thm 21/25.1: unique stationary state with kappa != 0 requires flip "
    "breaking), (S3) admitted by the per-band bound (C87), (S4) faithful and biased (Cor 14.2/15.3), (S5) pointed: "
    "the record direction J_E derived (Thm 20), (S6) definite with Born weighting. Kill tests: K1 several "
    "instrument directions survive; K2 the reduced dynamics is flip-covariant; K3 a coefficient or state is tuned to "
    "lambda/T_2. ZS-M67 supplies S5 and the necessary parts of S2, S3 as theorems; S1 holds for the chain but the "
    "coefficient fails S3; S4, S6 are not supplied. BT-REFORMULATED, [가설] for the physical reading", True, "")
row("D31", "D", "AUDIT ACCEPTANCE RECORD: the v2.9 audit (AUDIT-RESEARCH-REOPEN, S3 on Thm 38, S2-S3 on Thm 39, C88 "
    "retype, docstring, G18 exit) is accepted in full, 0 findings rejected. History row H-0277 is NOT edited; a "
    "superseding correction row is proposed to the user for append", True, "")
row("D32", "D", "EXTERNAL BASELINE (EESF): Marachevsky-Vassilevich, 'Chiral anomaly for local boundary conditions', "
    "arXiv:hep-th/0309019 -- Existence: primary arXiv listing fetched this session; Entailment: computes boundary "
    "contributions to the chiral anomaly for local (bag) boundary conditions by heat-kernel methods (abstract-level); "
    "Scope: EUCLIDEAN, D-slash-squared regulator; Freshness: n/a (mathematics). NOT TRANSPORTED (Remark 4.1): Theorem "
    "38.3 is a Lorentzian H^2-regulator statement and neither confirms nor contradicts the Euclidean boundary term. "
    "Prior-art sweep for the bilinear atlas and the vanishing tangential axial current on chiral-bag boundaries: one "
    "query family, NOT_FOUND (not ABSENT): OPEN-NOVELTY", True, "")
row("D33", "D", "CORPUS READ: ZS-S14 v2.1 (repo 1, Google Doc, read this session, 125,638 chars): sect.2.11 TYPE LOCK "
    "(Phi = rho e^{i theta}, theta massless Goldstone, rho heavy m_rho = 2A M_P), sect.10.3.5 (Phi_Z = Phi OPEN, both "
    "horns), sect.14.1 item 4 (boundary phase law must be target-blind; no tuning of a clock duration or sector "
    "weight), debt D-S14-EVENT-001 (action-derived non-phase-covariant seam environment: OPEN). Grep for temperature, "
    "KMS, thermal, clock, rest frame: no rest-frame datum is supplied. Repo 2 grep for zs_m67_verify_v2_5..v2_8: NOT_FOUND",
    True, "")
row("D35", "D", "AUDIT ACCEPTANCE RECORD (v3.1 audit, AUDIT-RESEARCH-REOPEN, scope Thm 39.4 / sect.22.9 handoff / release "
    "package): all findings accepted, 0 rejected -- (1) Thm 39.4 over-quantified, S3: split into K9a CLOSED / K9b OPEN, "
    "and K9b computed once (C99, V33); (2) Cor. 41.2 too strong, S2: D-S14-EVENT-001 receives a necessary condition, not "
    "a discharge; RQ2<->RQ3 identity downgraded to [가설]; (3) Thm 38.3 local-Fujikawa wording, S2 scope: narrowed to "
    "the spectral supertrace cancellation, domain preservation for local alpha(x) left OPEN; (4) notation/front matter: "
    "tau_1/tau_2 vs T_2 type lock (G23), survivor list and scope verdict re-synchronised, artifact-I row count 37 -> 38 "
    "corrected; (5) package: v3.1 baseline ledger shipped, G22 no longer FAILS on missing siblings, manuscript path by "
    "glob, clean-room re-run. One finding BEYOND the audit, reported here: the delivered v3.1 four-file package gives "
    "exit 1 (G18 DEGRADED + G22 FAIL), stricter than the audit's exit 2. History rows H-0280/H-0281 are NOT edited; "
    "superseding rows are proposed to the user for append", True, "")


row("D34", "D", "LIFECYCLE (v3.4): MANUSCRIPT DRAFT; FREEZE-CANDIDATE WITHHELD (v3.1-v3.3 audits); re-proposal only after a "
    "targeted delta re-audit of the three S2 repairs, sect.22.11 and G25 finds no new S2+. Remaining inside scope: the coherent-channel "
    "admission computation for K9b (Proof obligation 39.8', ONE computation after Thm 39.11; a research item, not a correction), the local-alpha(x) domain-preservation obligation (Cor. 38.7), a "
    "prior-art sweep on K9b (OPEN-NOVELTY). Conditional / external: K7 (f = M_P), K8. Upstream: A5 (two reals), "
    "D-S14-EVENT-001 (one necessary condition supplied). Title changed to match scope ('selector exhaustion' withdrawn). "
    "Output role SUPPORT; no CORE promotion; no SSOT change", True, "")
row("D38", "D", "AUDIT ACCEPTANCE RECORD (v3.2 audit, AUDIT-RESEARCH-REOPEN targeted at the K9b quantitative conclusion; "
    "independence L3 other model family + L5 deterministic re-run and counterexample): all findings accepted, 0 rejected -- "
    "S3 K9b bound not derived: 'unchanged bound', '2.16e7', conditional rejection WITHDRAWN, K9b OPEN, C99 split into "
    "C99a-c + D36, W16 reproduces the audit's counterexample family (r = 7.4e5 with D_cc kept); S2 package: four-file "
    "clean room gave exit 2 -> baseline fingerprints embedded, release manifest generated at run time, four files "
    "reproduce 0/0; S2 guards: G20/G23 passed semantic injections -> sentence-level claim-state and symbol-table rules, "
    "G24 claim-state manifest, G21 functional, both injections now FAIL (live-fire), limits stated; S1 |kappa| = T_2 sign; "
    "S1/S2 Elitzur scope narrowed to gauge-invariant states and undressed operators; S2 A1-A6 restated in the manuscript "
    "(from v1.1's wording and this manuscript's own usage; A4/A5 wording reconstructed, marked); S1 RQ2 -> RQ3 handoff; "
    "S2 novelty of Prop. 39.6 -> OPEN-NOVELTY (no prior-art sweep); S2 title narrowed; structure: lineage moved to a "
    "provenance supplement. History rows H-0282/H-0283 are NOT edited; superseding rows are proposed for append", True, "")

def write_manifest(ledger_path, ledger):
    """release manifest, GENERATED from measured hashes (VERIFY sect.10: single machine source; no self-hash fixed point)"""
    def sha(pth): return hashlib.sha256(open(pth, "rb").read()).hexdigest() if os.path.exists(pth) else None
    man_name = "release_manifest_v3_4.json"
    def _first(pattern):
        c = sorted(glob.glob(os.path.join(HERE, pattern)))
        return c[0] if c else None
    prov_files = {"session": _first("session_M67_v3_4*.md"), "audit": _first("*audit*v3_3*.md") or _first("*audit*M67*.md"),
                  "supplement": _first("*M67_v3_4_provenance_supplement.md") or _first("*M67_v3_3_provenance_supplement.md")}
    man = {"paper": "ZS-M67 v3.4", "artifact": "L",
           "core": {   # VERIFY sect.9.1: the authoritative core is exactly these four objects (v3.3 audit S2-3)
               "manuscript": {"file": os.path.basename(PAPER), "sha256": sha(PAPER)},
               "verifier": {"file": os.path.basename(SELF), "sha256": self_sha},
               "ledger": {"file": os.path.basename(ledger_path), "sha256": sha(ledger_path)},
               "manifest": {"file": man_name, "sha256": None, "note": "this object; no self-hash fixed point (VERIFY sect.13)"}},
           "provenance_objects": {k: {"file": os.path.basename(v) if v else None, "present": bool(v), "sha256": sha(v) if v else None,
                                      "role": "review/provenance record; NOT read by the verifier's evidence rows"} for k, v in prov_files.items()},
           "baseline": {"artifact": "K", "embedded_fingerprints": len(BASELINE_FP), "json": os.path.basename(PREV_LEDGER),
                        "json_present": os.path.exists(PREV_LEDGER), "json_sha256": sha(PREV_LEDGER)},
           "rows": ledger["n_rows"], "census": ledger["census"], "n_fail": ledger["n_fail"], "n_degraded": ledger["n_degraded"],
           "exit_policy": ledger["exit_policy"], "claim_state_read": CLAIM_STATE,
           "object_graph_declared_by_manuscript": G25_STATE}
    with open(os.path.join(HERE, man_name), "w", encoding="utf-8") as f:
        json.dump(man, f, ensure_ascii=False, indent=1, sort_keys=True)

def main():
    ok18 = finish_provenance()
    for r in ROWS:
        if r["id"] == "G18":
            r["detail"] = json.dumps(prov, ensure_ascii=False)
            r["result"] = "PASS" if ok18 else "FAIL"
    n_final = len(ROWS)
    if G23_STATE is not None:
        counts_ok = len(G23_STATE["K_counts"]) >= 2 and all(c == n_final for c in G23_STATE["K_counts"])
        runs_ok = all(r == os.path.basename(SELF) for r in G23_STATE["K_runs"]) and len(G23_STATE["K_runs"]) >= 1
        ok23 = G23_STATE["glyph"] and not G23_STATE["bad_symbol_sentences"] and counts_ok and runs_ok
        for r in ROWS:
            if r["id"] == "G23":
                r["result"] = "PASS" if ok23 else "FAIL"
                r["detail"] = "glyph = %s ; symbol-table violations = %s ; printed K row counts = %s vs measured %d ; K run lines = %s" % (
                    G23_STATE["glyph"], G23_STATE["bad_symbol_sentences"], G23_STATE["K_counts"], n_final, G23_STATE["K_runs"])
    if CLAIM_STATE is not None or (G23_STATE is not None):
        reg_status = {e["id"]: e["status"] for e in REGISTRY}
        mism = []
        if not CLAIM_STATE:
            mism.append("CLAIM-STATE block missing")
        else:
            for k, v in CLAIM_STATE.items():
                if k in reg_status and reg_status[k] != v: mism.append("%s: declared %s, computed %s" % (k, v, reg_status[k]))
            for k, want in (("FREEZE-CANDIDATE", "WITHHELD"), ("D-S14-EVENT-001", "NECESSARY-CONDITION-SUPPLIED"), ("Cor38.7", "OPEN"),
                            ("C99d", "CLOSED-NEGATIVE-LINEAR"), ("C99e", "OPEN"), ("T2", "TARGET"), ("tau1,tau2", "RELAXATION"), ("RQ3", "OPEN"),
                            ("MissingObject", "SPECIFIED-NOT-CONSTRUCTED"), ("ThermalCeiling", "TARGET-INDEPENDENT"), ("T-over-Delta", "TARGET-CONDITIONED")):
                if CLAIM_STATE.get(k) != want: mism.append("%s: declared %s, required %s" % (k, CLAIM_STATE.get(k), want))
            if CLAIM_STATE.get("artifactL.rows") != str(n_final): mism.append("artifactL.rows: declared %s, measured %d" % (CLAIM_STATE.get("artifactL.rows"), n_final))
            if not all(k in CLAIM_STATE for k in reg_status): mism.append("registry ids missing from block: %s" % sorted(set(reg_status) - set(CLAIM_STATE)))
            if secs and "WITHHELD" not in secs.get(23, ""): mism.append("sect.23 lacks WITHHELD")
        for r in ROWS:
            if r["id"] == "G24":
                r["result"] = "PASS" if not mism else "FAIL"; r["detail"] = "mismatches = %s ; declared = %s" % (mism, CLAIM_STATE)
    if G25_STATE is not None:
        core_ok = G25_STATE["core_block_found"] and set(G25_STATE["core_declared"]) == set(CORE_OBJECTS)
        prov_ok = G25_STATE["prov_block_found"] and set(PROVENANCE_OBJECTS) <= set(G25_STATE["prov_declared"]) and not (set(G25_STATE["prov_declared"]) & set(CORE_OBJECTS))
        for r in ROWS:
            if r["id"] == "G25":
                r["result"] = "PASS" if (core_ok and prov_ok) else "FAIL"
                r["detail"] = "declared core = %s (required %s) ; declared provenance = %s (required >= %s)" % (
                    G25_STATE["core_declared"], list(CORE_OBJECTS), G25_STATE["prov_declared"], list(PROVENANCE_OBJECTS))
    census = {}
    for r in ROWS:
        census[r["class"]] = census.get(r["class"], 0) + 1
    fails = [r for r in ROWS if r["result"] == "FAIL"]
    degs = [r for r in ROWS if r["result"] == "DEGRADED"]
    ledger = {"artifact": os.path.basename(SELF), "sha256": self_sha, "paper": "ZS-M67 v3.4",
              "seed": SEED, "mpmath_dps": 60, "rows": ROWS, "n_rows": len(ROWS),
              "n_fail": len(fails), "n_degraded": len(degs), "census": census,
              "n_universal": len([r for r in ROWS if r["universal"]]),
              "proof_objects": 0, "provenance": prov,
              "registry": [{k: e[k] for k in ("id", "source", "mediator", "coupling", "band", "class", "status", "G4m2_str")} for e in REGISTRY],
              "exit_policy": "0 iff FAIL == 0 and DEGRADED == 0 ; 1 if FAIL > 0 ; 2 if DEGRADED > 0 or the ledger is empty"}
    ledger_path = os.path.join(HERE, "zs_m67_verify_v3_4.json")
    with open(ledger_path, "w", encoding="utf-8") as f:
        json.dump(ledger, f, ensure_ascii=False, indent=1, sort_keys=True)
    write_manifest(ledger_path, ledger)
    for r in ROWS:
        flag = "U" if r["universal"] else " "
        print("%-5s %-8s %s %s" % (r["id"], r["result"], flag, r["claim"][:92]))
        if r["detail"]:
            print("        -> %s" % r["detail"][:190])
    print("\nrows: %d  FAIL: %d  DEGRADED: %d  universal-flagged: %d"
          % (len(ROWS), len(fails), len(degs), ledger["n_universal"]))
    print("census: " + "  ".join("%s=%d" % kv for kv in sorted(census.items())))
    print("proof objects: 0.  A PASS row is not a theorem.")
    print("script sha256: %s" % self_sha)
    return exit_code(ROWS)

if __name__ == "__main__":
    sys.exit(main())
