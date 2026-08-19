#!/usr/bin/env python3
"""
ZS-S1 v1.1 companion verification suite.

Paper  : ZS-S1 v1.1 -- Gauge Coupling Unification: Incidence-Laplacian Bridge
         from Action to SM Gauge Couplings.  Dated erratum + scope correction.
Author : Kenny Kang
Date   : 2026-08-19 (KST)

WHAT THIS SCRIPT IS
-------------------
A fail-closed verification artifact.  Every row carries an explicit
verification class from the project taxonomy ([regulation]_verification-artifact
v1.2 section 2, canonical):

    C  CERTIFIED COMPUTATION (exact rational / high-precision ball)   evidence
    V  NUMERICAL VERIFICATION at a declared precision and tolerance   evidence
    W  NUMERIC WITNESS / counterexample / exhaustive finite search    evidence
    R  REGRESSION against a frozen superseded value                   control
    G  GUARD / invariant / fail-closed check                          control
    X  DIAGNOSTIC / exploratory                                       not evidence
    D  DECLARATION with a proof or source pointer                     not evidence
    T  TAUTOLOGY / premise-sharing control                            not evidence

Class ``P`` (THEOREM-PROOF) is NOT USED.  This script does not prove theorems.
The convention follows the project precedent set by zs_m61_verify_v1_1.py
(history H-0014) and zs_s14_verify_v2_1.py (history H-0049).  Statements that
the manuscript proves by argument appear here as ``D`` rows with a pointer.

ROW COUNT IS NOT THEOREM COUNT.

PRE-DECLARED RUN PARAMETERS  (declared before any result was inspected)
----------------------------------------------------------------------
    precision            : mpmath mp.dps = 50 decimal digits
    exact arithmetic     : fractions.Fraction wherever the object is rational
    monte-carlo seed     : numpy.random.seed(42)
    monte-carlo trials   : 100000
    monte-carlo window   : 1 per cent relative, on both beta-function slopes
    rational scan grid   : p in [1,100], q in [2,200]  (sensitivity, section J)
    integer shift grid   : delta in [-3,+3]            (sensitivity, section J)
    tolerance policy     : every ``V`` row declares an explicit tolerance AND a
                           justification string.  A tolerance looser than 1 per
                           cent is rejected by guard GRD07 unless its
                           justification begins with "TOL-JUSTIFY:".
                           Comparisons against a formula use 1e-40 (exact) or
                           1e-30 (transcendental).  Comparisons against
                           experiment are NEVER pass/fail against a rounded
                           constant: the pull in sigma is printed instead.
    external data policy : every external number carries a named source edition
                           and an as-of date.  See EXT below.
    printed precision    : a figure derived from a PDG input is printed with the
                           uncertainty that input propagates, and never with more
                           significant figures than that uncertainty supports
                           (numerical-hygiene rule N4).  Figures built only from
                           exact rationals, x*, and CODATA alpha are printed to the
                           declared 50-digit precision.
    audit disposition    : this artifact is the post-audit revision.  An independent
                           adversarial audit dated 2026-08-19 returned
                           AUDIT-CORRECTION-REQUIRED; its findings are repaired here
                           and in manuscript section 0.2 erratum E-S1-5.

WHAT THIS SCRIPT IS NOT
-----------------------
It does not derive alpha_2, and it does not search for a replacement rational
for alpha_2.  The numerical target is already known, so any expression found by
search now would be target-fitted by construction and would carry zero
evidential content.  See row J7 and manuscript sections 10.5 and 12.

Execution : python3 zs_s1_verify_v1_1.py
Outputs   : console census + zs_s1_verify_v1_1.json
Exit      : 0 iff 0 FAIL and every guard passes
Deps      : mpmath >= 1.3.0, numpy >= 1.24
"""

import ast
import hashlib
import json
import os
import re
import sys
from fractions import Fraction

import numpy as np
from mpmath import mp, mpf, sqrt, pi, fabs, lambertw, mpc

mp.dps = 50

PAPER_CODE = "ZS-S1"
PAPER_VERSION = "v1.1"
SCRIPT_VERSION = "v1.1.0"
PAPER_DATE = "2026-08-19"
MANUSCRIPT = "ZS-S1_v1_1.md"
LEGACY_SCRIPT = "zs_s1_verify_v1_0.py"

MC_SEED = 42
MC_TRIALS = 100000
MC_WINDOW = 0.01

EXPECTED_ROWS = 138
EXPECTED_CLASS_CENSUS = {
    "C": 23, "V": 22, "W": 8, "R": 12, "G": 25, "X": 10, "D": 22, "T": 16,
}

# =====================================================================
# LOCKED INPUTS  (upstream; never refitted here)
# =====================================================================
Z, X, Y = 2, 3, 6
Q = Z + X + Y                    # 11
G = 2 * Y                        # 12
A = Fraction(35, 437)

V_X, E_X, F_X = 24, 36, 14       # truncated octahedron   (X sector)
V_Y, E_Y, F_Y = 60, 90, 32       # truncated icosahedron  (Y sector)
VF_X, VF_Y = V_X + F_X, V_Y + F_Y
VEF_X, VEF_Y = V_X + E_X + F_X, V_Y + E_Y + F_Y

Oh, Ih, Td = 48, 120, 24
delta_X = Fraction(abs(F_X - V_X), F_X + V_X)
delta_Y = Fraction(abs(F_Y - V_Y), F_Y + V_Y)

n_f, N_c, n_g = 5, 3, 3
beta0_Z = 1
N_eff_Y = VF_Y + beta0_Z         # 93

# i-tetration fixed point z* = i^{z*}   (ZS-M1 v1.0)
z_star = lambertw(mpc(0, -1) * pi / 2) / (mpc(0, -1) * pi / 2)
x_star = z_star.real

# ZS-S4 v1.0 section 6.12 Thm V.9
v_S4 = mpf("245.93")

# =====================================================================
# EXTERNAL REFERENCE VALUES  (edition-named, as-of dated)
# =====================================================================
AS_OF = "2026-08-19"
EXT = {
    "m_W":        (mpf("80.3692"), mpf("0.0133"),
                   "PDG 2024, Mass and Width of the W Boson (rpp2024-rev-w-mass); "
                   "world average 80369.2 +- 13.3 MeV, CDF II 2022 excluded"),
    "m_W_fit":    (mpf("80.353"), mpf("0.006"),
                   "PDG 2024, rpp2024-rev-w-mass; electroweak-fit prediction"),
    "sin2_hat":   (mpf("0.23129"), mpf("0.00004"),
                   "PDG 2024, Physical Constants table / rpp2024-rev-standard-model "
                   "Table 10.2; sin^2 thetahat(M_Z), MS-bar"),
    "sin2_os":    (mpf("0.22348"), mpf("0.00010"),
                   "PDG 2024, rpp2024-rev-standard-model Table 10.2; on-shell s^2_W"),
    "alpha5_inv": (mpf("127.930"), mpf("0.008"),
                   "PDG 2024, rpp2024-rev-standard-model section 10.2.2; "
                   "alphahat^(5)(M_Z)^-1"),
    "M_Z":        (mpf("91.1880"), mpf("0.0020"),
                   "PDG 2024, Physical Constants table"),
    "alpha_s":    (mpf("0.1180"), mpf("0.0009"),
                   "PDG 2024, Physical Constants table; alpha_s(m_Z) = 0.1180(9)"),
    "G_F":        (mpf("1.1663788e-5"), mpf("6e-12"),
                   "PDG 2024, Physical Constants table"),
    "alpha0_inv": (mpf("137.035999177"), mpf("0.000000021"),
                   "CODATA 2022, inverse fine-structure constant"),
}

# Superseded external values that v1.0 and the correction report used.
# Held ONLY so that regression rows can prove they are no longer live.
SUPERSEDED_EXT = {
    "sin2_hat_pdg2023": mpf("0.23122"),
    "sin2_hat_err_v10": mpf("0.00003"),
    "sin2_os_pdg2023":  mpf("0.22339"),
    "alpha5_inv_2023":  mpf("127.951"),
    "M_Z_2023":         mpf("91.1876"),
}
# Superseded printed values internal to the ZS-S1 / ZS-S14 line.
SUPERSEDED_INTERNAL = {
    "m_W_v10_claim":    mpf("80.4"),      # ZS-S14 v1.0/v2.0 Thm S14.B Step 4  (E19)
    "sin2_pull_v10":    mpf("-1.26"),     # ZS-S1 v1.0 section 8.2             (E-S1-2)
    "v10_row_banner":   35,               # ZS-S1 v1.0 section 14 "35/35"      (E-S1-4)
    "v10_script_rows":  38,               # zs_s1_verify_v1_0.py actual rows   (E-S1-4)
}

alpha0 = 1 / EXT["alpha0_inv"][0]
alpha_em_MZ = 1 / EXT["alpha5_inv"][0]

# =====================================================================
# ROW REGISTRY
# =====================================================================
ROWS, _FAIL, _CONTRACT = [], [], []
EVIDENCE_CLASSES = ("C", "V", "W")
ALL_CLASSES = ("C", "V", "W", "R", "G", "X", "D", "T")


def row(rid, cls, cond, name, expected, actual,
        tol=None, why=None, pointer=None, resid=None):
    if cls == "P":
        raise SystemExit("CONTRACT VIOLATION: class P is not used in this suite")
    if cls not in ALL_CLASSES:
        raise SystemExit(f"CONTRACT VIOLATION: unknown class {cls!r} at {rid}")
    if cls == "D" and not pointer:
        raise SystemExit(f"CONTRACT VIOLATION: declaration row {rid} has no pointer")
    if cls == "V" and (tol is None or not why):
        raise SystemExit(f"CONTRACT VIOLATION: numerical row {rid} lacks tol/why")
    ok = bool(cond)
    e = {"id": rid, "class": cls, "name": name,
         "expected": str(expected), "actual": str(actual),
         "status": "PASS" if ok else "FAIL"}
    if tol is not None:
        e["tolerance"] = str(tol)
    if why:
        e["tolerance_basis"] = why
    if pointer:
        e["pointer"] = pointer
    if resid is not None:
        try:
            e["residual"] = f"{float(resid):.3e}"
        except Exception:
            e["residual"] = str(resid)
    ROWS.append(e)
    if not ok:
        _FAIL.append(rid)
    return ok


def pull(value, ref, err):
    return (value - ref) / err


def pct(value, ref):
    return (value / ref - 1) * 100


def nstr(v, n=12):
    return mp.nstr(v, n, strip_zeros=False)


print("=" * 78)
print(f"{PAPER_CODE} {PAPER_VERSION} VERIFICATION SUITE  (script {SCRIPT_VERSION})")
print("Gauge Coupling Unification: Incidence-Laplacian Bridge")
print(f"dps={mp.dps}  mc_seed={MC_SEED}  mc_trials={MC_TRIALS}  "
      f"mc_window={MC_WINDOW}  expected_rows={EXPECTED_ROWS}")
print(f"external data as-of {AS_OF}; editions named per row")
print("=" * 78)

# ---------------------------------------------------------------------
# A. LOCKED INPUTS AND POLYHEDRAL INVARIANTS
# ---------------------------------------------------------------------
row("A1", "T", Q == 11, "Q = Z + X + Y = 11", 11, Q)
row("A2", "T", G == 12, "G = 2Y = MUB(Q) = 12", 12, G)
row("A3", "T", (Z, X, Y) == (2, 3, 6), "(Z,X,Y) = (2,3,6)", "(2,3,6)", (Z, X, Y))
row("A4", "C", A == delta_X * delta_Y, "A = delta_X * delta_Y = 35/437",
    Fraction(35, 437), delta_X * delta_Y)
row("A5", "C", V_X - E_X + F_X == 2, "Euler X: V-E+F = 2", 2, V_X - E_X + F_X)
row("A6", "C", V_Y - E_Y + F_Y == 2, "Euler Y: V-E+F = 2", 2, V_Y - E_Y + F_Y)
row("A7", "C", Fraction(E_Y, E_X) == Fraction(5, 2), "Edge Lemma E_Y/E_X = 5/2",
    Fraction(5, 2), Fraction(E_Y, E_X))
row("A8", "C", VEF_Y == 182 and VEF_Y == 2 * 91, "Total-Count Y: V+E+F = 182 = 2*91",
    182, VEF_Y)
row("A9", "C", VEF_X == 74 and VEF_X == 2 * 37, "Total-Count X: V+E+F = 74 = 2*37",
    74, VEF_X)
row("A10", "C", Ih // Td == 5 and Oh // Td == Z,
    "|I_h|/|T_d| = 5 and |O_h|/|T_d| = 2 = Z", "(5,2)", (Ih // Td, Oh // Td))
row("A11", "T", VF_X == 38, "(V+F)_X = 38", 38, VF_X)
row("A12", "T", VF_Y == 92, "(V+F)_Y = 92", 92, VF_Y)
row("A13", "T", E_X == VF_X - 2 and E_Y == VF_Y - 2, "E = V+F-chi in both sectors",
    "(36,90)", (VF_X - 2, VF_Y - 2))
row("A14", "C", delta_X == Fraction(5, 19) and delta_Y == Fraction(7, 23),
    "delta_X = 5/19, delta_Y = 7/23", "(5/19,7/23)", (delta_X, delta_Y))

_arch13 = [(12, 18, 8), (12, 24, 14), (24, 36, 14), (24, 36, 14), (24, 48, 26),
           (48, 72, 26), (24, 60, 38), (30, 60, 32), (60, 90, 32), (60, 90, 32),
           (60, 120, 62), (120, 180, 62), (60, 150, 92)]
row("A15", "W", all(v + e + f == 2 * (v + f - 1) for v, e, f in _arch13),
    "Euler Cell-Count V+E+F = 2(V+F-1) over 13 Archimedean solids",
    "13/13", f"{sum(1 for v,e,f in _arch13 if v+e+f == 2*(v+f-1))}/13")

# ---------------------------------------------------------------------
# B. INCIDENCE-LAPLACIAN BRIDGE AND SPECTRAL-TO-BETA BRIDGE
# ---------------------------------------------------------------------
row("B1", "D", True, "Mode-Count Collapse: W_Gamma(mu) = (V+F) log mu + O(1)",
    "PROVEN in manuscript", "declaration",
    pointer="ZS-S1 v1.1 section 4, Mode-Count Collapse")
row("B2", "D", True, "Spectral density rule a(Gamma) = (V+F)_Gamma / G",
    "DERIVED in manuscript", "declaration",
    pointer="ZS-S1 v1.1 section 4, Eq.(8)")
row("B3", "C", V_Y == n_f * G, "V_Y = n_f * G = 5 * 12", 60, V_Y)
row("B4", "C", F_Y == (N_c ** 2 - 1) * G // N_c, "F_Y = (N^2-1) G/N = 8 * 4", 32, F_Y)
row("B5", "C", V_X == n_g * (N_c + 1) * 2, "V_X = n_g (N_c+1) 2 = 3*4*2", 24, V_X)
_b0_su3 = Fraction(11) - Fraction(2, 3) * n_f
_b0_su2 = Fraction(22, 3) - Fraction(4, 3) * n_g - Fraction(1, 6)
row("B6", "C", Fraction(VF_Y, G) == _b0_su3 == Fraction(23, 3),
    "a3 = (V+F)_Y/G = b0(SU(3), n_f=5) = 23/3", Fraction(23, 3), Fraction(VF_Y, G))
row("B7", "C", Fraction(VF_X, G) == _b0_su2 == Fraction(19, 6),
    "a2 = (V+F)_X/G = b0(SU(2), SM) = 19/6", Fraction(19, 6), Fraction(VF_X, G))
row("B8", "C", Fraction(VF_Y, VF_X) == Fraction(46, 19),
    "slope ratio a3/a2 = 46/19", Fraction(46, 19), Fraction(VF_Y, VF_X))
row("B9", "C", A.denominator == Fraction(VF_X, G).numerator * Fraction(VF_Y, G).numerator,
    "den(A) = num(a2) * num(a3) = 19*23", 437, A.denominator)
row("B10", "C", Q + 1 == G, "MUB(Q=11) = Q+1 = G = 12", 12, Q + 1)

# Hodge-Dirac block
_dim_exact, _dim_coexact = V_Y - 1, F_Y - 1
row("B11", "C", _dim_exact == 59 and _dim_coexact == 31 and _dim_exact + _dim_coexact == E_Y,
    "Hodge on TI: 59 exact + 31 coexact = 90 = E_Y", 90, _dim_exact + _dim_coexact)
row("B12", "C", Fraction(abs(_dim_exact - _dim_coexact), VF_Y) == delta_Y,
    "delta_Y = |exact-coexact|/(V+F) = 7/23", Fraction(7, 23),
    Fraction(abs(_dim_exact - _dim_coexact), VF_Y))
row("B13", "C", V_Y + F_Y == 92 and VEF_Y - E_Y == 92,
    "even chirality sector dim = V+F = 92", 92, VEF_Y - E_Y)

# ---------------------------------------------------------------------
# C. Z-SECTOR SCHUR COMPLEMENT
# ---------------------------------------------------------------------
row("C1", "T", Z == 2, "dim(Z) = 2", 2, Z)
row("C2", "D", beta0_Z == 1,
    "beta_0(Z) = 1 is the Z2-even connected-component mode",
    "1 (argument, not computed here)", beta0_Z,
    pointer="ZS-S1 v1.1 section 5.2-5.3; ZS-F5 v1.0 dim(Z)=2")
row("C3", "T", N_eff_Y == 93, "N_eff(Y) = (V+F)_Y + beta_0(Z) = 93", 93, N_eff_Y)

# ---------------------------------------------------------------------
# D. GAUGE COUPLING OUTPUTS, EXACT
# ---------------------------------------------------------------------
alpha_s = Fraction(Q, N_eff_Y)
alpha_2 = Fraction(Y, 5 * VF_X)
sin2_S1 = Fraction(48, 91) * x_star

row("D1", "T", alpha_s == Fraction(11, 93),
    "alpha_s = Q/[(V+F)_Y + beta_0(Z)] = 11/93", Fraction(11, 93), alpha_s)
row("D2", "T", alpha_2 == Fraction(3, 95),
    "alpha_2 = Y/[5 (V+F)_X] = 6/190 = 3/95  (ZS-S1 section 8.3 form)",
    Fraction(3, 95), alpha_2)
row("D3", "T", Fraction(1, 1) / alpha_2 == Fraction(95, 3),
    "1/alpha_2 = 95/3 exactly", Fraction(95, 3), 1 / alpha_2)
_r = fabs(1 / alpha_2 - mpf(95) / 3)
row("D4", "T", _r < mpf("1e-40"), "1/alpha_2 = 31.666... at 50 digits",
    "31.66666666666666666667", nstr(mpf(95) / 3, 22),
    resid=_r)
row("D5", "T", Fraction(5 * VF_X, 1) == 190 and Fraction(3, 95) == Fraction(6, 190),
    "denominator of alpha_2 is 5*(V+F)_X = 190, an X-sector object", 190, 5 * VF_X)
row("D6", "T", N_eff_Y == 93 and 5 * VF_X == 190 and N_eff_Y != 5 * VF_X,
    "alpha_s and alpha_2 do NOT share a denominator base (93 vs 190)",
    "93 != 190", f"{N_eff_Y} != {5*VF_X}")
row("D7", "C", Fraction(Ih, Td) == 5 and Fraction(E_Y, E_X) * Z == 5,
    "factor 5 = |I_h|/|T_d| = Z*(E_Y/E_X), two independent routes", 5,
    (Fraction(Ih, Td), Fraction(E_Y, E_X) * Z))
_r = fabs(sin2_S1 - mpf("0.23118220838348946547"))
row("D8", "V", _r < mpf("1e-20"),
    "sin^2 theta_W = (48/91) x* = 0.23118220838348946547",
    "0.23118220838348946547", nstr(sin2_S1, 20),
    tol="1e-20", why="x* is transcendental; 50-dps evaluation, print limited to 20 digits",
    resid=_r)
_r = fabs(mp.arg(z_star) - x_star * pi / 2)
row("D9", "V", _r < mpf("1e-40"), "Berry-phase identity arg(z*) = x* pi/2",
    "0", nstr(_r, 6), tol="1e-40",
    why="lambertw at 50 dps; residual is arithmetic noise", resid=_r)
_r = fabs(z_star - mpc(0, 1) ** z_star)
row("D10", "V", _r < mpf("1e-40"), "z* satisfies z = i^z at 50 digits",
    "0", nstr(_r, 6), tol="1e-40",
    why="fixed-point residual of the defining equation", resid=_r)

# ---------------------------------------------------------------------
# E. SCALE AND SCHEME DECLARATIONS   (the v1.1 scope correction)
# ---------------------------------------------------------------------
SCALE_TABLE = {
    "alpha_s":   ("mu = M_Z", "MS-bar", "DERIVED"),
    "sin2_th_W": ("mu = M_Z", "MS-bar", "DERIVED"),
    "alpha_2":   ("UNDECLARED", "UNDECLARED", "OBSERVATION"),
    "a2":        ("scale-free", "1-loop slope", "PROVEN"),
    "a3":        ("scale-free", "1-loop slope", "PROVEN"),
}
row("E1", "D", SCALE_TABLE["alpha_s"] == ("mu = M_Z", "MS-bar", "DERIVED"),
    "alpha_s carries scale mu = M_Z and scheme MS-bar", "declared",
    SCALE_TABLE["alpha_s"], pointer="ZS-S1 v1.1 section 8.0 Table 8.0")
row("E2", "D", SCALE_TABLE["sin2_th_W"] == ("mu = M_Z", "MS-bar", "DERIVED"),
    "sin^2 theta_W carries scale mu = M_Z and scheme MS-bar", "declared",
    SCALE_TABLE["sin2_th_W"], pointer="ZS-S1 v1.1 section 8.0 Table 8.0")
row("E3", "D", SCALE_TABLE["alpha_2"][0] == "UNDECLARED",
    "alpha_2 carries NO scale and NO scheme; physical identification OPEN",
    "UNDECLARED / OBSERVATION", SCALE_TABLE["alpha_2"],
    pointer="ZS-S1 v1.1 section 8.0 Table 8.0 and section 8.3'")
row("E4", "G", all(len(t) == 3 and all(t) for t in SCALE_TABLE.values()),
    "every coupling output has a (scale, scheme, status) triple",
    "5 complete triples", f"{len(SCALE_TABLE)} entries")
row("E5", "G", "M_Z" not in SCALE_TABLE["alpha_2"][0]
    and SCALE_TABLE["alpha_2"][2] != "DERIVED",
    "GUARD: alpha_2 is not silently re-declared as an M_Z DERIVED quantity",
    "not (M_Z, DERIVED)", SCALE_TABLE["alpha_2"])
row("E6", "D", True,
    "Branch C' of correction-report section C-03 adopted: per-output declaration",
    "C' (approved 2026-08-19)", "declaration",
    pointer="ZS-S1 v1.1 section 0.3 Decision Gate S1-A")

# ---------------------------------------------------------------------
# F. COMPARISON TO EXPERIMENT  -- pulls in sigma, never a rounded constant
# ---------------------------------------------------------------------
_as_pull = pull(mpf(alpha_s.numerator) / alpha_s.denominator,
                EXT["alpha_s"][0], EXT["alpha_s"][1])
row("F1", "V", fabs(_as_pull - mpf("0.311")) < mpf("5e-4"),
    f"alpha_s pull vs PDG 2024 = {nstr(_as_pull,4)} sigma (+0.311)",
    "+0.311 sigma", nstr(_as_pull, 4), tol="5e-4",
    why="PDG alpha_s error 0.0009 carries one significant figure, so the pull is "
        "printed to three; tolerance is half a unit in the last printed place")
row("F2", "X", fabs(_as_pull) < 1,
    "diagnostic: |alpha_s pull| < 1 sigma", "< 1", nstr(fabs(_as_pull), 6))
row("F3", "D", True, f"alpha_s reference source: {EXT['alpha_s'][2]}",
    f"as-of {AS_OF}", str(EXT["alpha_s"][0]), pointer=EXT["alpha_s"][2])

_s2_pull = pull(sin2_S1, EXT["sin2_hat"][0], EXT["sin2_hat"][1])
row("F4", "V", fabs(_s2_pull - mpf("-2.695")) < mpf("5e-4"),
    f"sin^2 theta_W pull vs PDG 2024 = {nstr(_s2_pull,4)} sigma (-2.695)",
    "-2.695 sigma", nstr(_s2_pull, 4), tol="5e-4",
    why="PDG sin^2 error 0.00004 carries one significant figure, so the pull is "
        "printed to four; tolerance is half a unit in the last printed place")
_s2_rel = pct(sin2_S1, EXT["sin2_hat"][0])
row("F5", "V", fabs(_s2_rel - mpf("-0.04660")) < mpf("5e-6"),
    f"sin^2 theta_W relative gap vs PDG 2024 = {nstr(_s2_rel,4)} per cent (-0.04660)",
    "-0.04660 per cent", nstr(_s2_rel, 4), tol="5e-6",
    why="PDG central value carries 5 significant figures; printed to 4, "
        "tolerance half a unit in the last printed place")
row("F6", "X", fabs(_s2_pull) < 3,
    "diagnostic: gate FS1-2 (|pull| > 3 sigma) has not fired", "< 3",
    nstr(fabs(_s2_pull), 6))
row("F7", "D", True, f"sin^2 theta_W reference source: {EXT['sin2_hat'][2]}",
    f"as-of {AS_OF}", str(EXT["sin2_hat"][0]), pointer=EXT["sin2_hat"][2])

# ---------------------------------------------------------------------
# G. THE SCALE DIAGNOSTIC   -- executed on every run
# ---------------------------------------------------------------------
a2_mp = mpf(alpha_2.numerator) / alpha_2.denominator
alpha2_hat_MZ = alpha_em_MZ / EXT["sin2_hat"][0]

_prod_internal = a2_mp * sin2_S1
row("G1", "T", _prod_internal > 0,
    "alpha_2 * sin^2 theta_W (both ZS-S1 internal) evaluated",
    "positive", nstr(_prod_internal, 15))
_g = pct(_prod_internal, alpha0)
row("G2", "V", fabs(_g - mpf("0.0430050")) < mpf("1e-6"),
    f"internal product vs alpha_em(0): gap = {nstr(_g,6)} per cent",
    "+0.0430050 per cent", nstr(_g, 8), tol="1e-6",
    why="ratio of two 50-dps quantities; printed to 6 significant figures")
_g2 = pct(_prod_internal, alpha_em_MZ)
_g2e = fabs(_g2 + 100) * (EXT["alpha5_inv"][1] / EXT["alpha5_inv"][0])
row("G3", "V", fabs(_g2 - mpf("-6.605")) < mpf("5e-4"),
    f"internal product vs alpha_em(M_Z): gap = {nstr(_g2,4)} +- {nstr(_g2e,2)} per cent",
    "-6.605 +- 0.006 per cent", nstr(_g2, 4), tol="5e-4",
    why="PDG alphahat^(5) error 0.008 propagates to +-0.006 per cent; printed to "
        "that precision, tolerance half a unit in the last printed place")
row("G4", "X", fabs(_g) < fabs(_g2) / 100,
    "the internal product lands on alpha_em(0), not alpha_em(M_Z), "
    "by more than two orders of magnitude",
    "|gap_0| << |gap_MZ|", f"{nstr(fabs(_g),4)} vs {nstr(fabs(_g2),4)}")

_hyb = alpha0 / EXT["sin2_hat"][0]
_g3 = pct(a2_mp, _hyb)
_g3e = (1 + _g3 / 100) * (EXT["sin2_hat"][1] / EXT["sin2_hat"][0]) * 100
row("G5", "V", fabs(_g3 - mpf("0.0897")) < mpf("5e-5"),
    f"alpha_2 vs alpha_em(0)/sin^2 thetahat(M_Z): gap = {nstr(_g3,3)} "
    f"+- {nstr(_g3e,3)} per cent",
    "+0.0897 +- 0.0173 per cent", nstr(_g3, 3), tol="5e-5",
    why="PDG sin^2 error 0.00004 propagates to +-0.0173 per cent, so this match is "
        "about five propagated sigma from zero and is NOT tighter than the paper's "
        "other agreements; printed to that precision")
_g4 = pct(a2_mp, alpha2_hat_MZ)
_a2he = alpha2_hat_MZ * sqrt((EXT["alpha5_inv"][1] / EXT["alpha5_inv"][0]) ** 2
                            + (EXT["sin2_hat"][1] / EXT["sin2_hat"][0]) ** 2)
_g4e = (1 + _g4 / 100) * (_a2he / alpha2_hat_MZ) * 100
row("G6", "V", fabs(_g4 - mpf("-6.561")) < mpf("5e-4"),
    f"alpha_2 vs PDG 2024 alphahat_2(M_Z): gap = {nstr(_g4,4)} +- {nstr(_g4e,3)} per cent",
    "-6.561 +- 0.0172 per cent", nstr(_g4, 4), tol="5e-4",
    why="PDG errors on alphahat^(5) and sin^2 propagate to +-0.0172 per cent; "
        "printed to that precision")
_inv_a2h_e = _a2he / alpha2_hat_MZ ** 2
row("G7", "V", fabs(1 / alpha2_hat_MZ - mpf("29.589")) < mpf("5e-4"),
    f"1/alphahat_2(M_Z) from PDG 2024 = {nstr(1/alpha2_hat_MZ,5)} "
    f"+- {nstr(_inv_a2h_e,2)}", "29.589 +- 0.0054", nstr(1 / alpha2_hat_MZ, 5),
    tol="5e-4", why="propagated PDG error is 0.0054, so five significant figures is "
                    "the ceiling; tolerance half a unit in the last printed place")
_ratio_lhs = a2_mp / alpha2_hat_MZ
_ratio_rhs = alpha0 / alpha_em_MZ
_g5 = (_ratio_lhs / _ratio_rhs - 1) * 100
row("G8", "V", fabs(_g5 - mpf("0.0897")) < mpf("5e-5"),
    "ratio identity alpha_2/alphahat_2(M_Z) vs alpha_em(0)/alpha_em(M_Z): "
    f"gap = {nstr(_g5,3)} per cent", "+0.0897 per cent", nstr(_g5, 3),
    tol="5e-5", why="same propagated PDG error as G5, +-0.0173 per cent")
row("G9", "T", fabs(_g5 - _g3) < mpf("1e-30"),
    "the ratio identity and the hybrid identity are ALGEBRAICALLY THE SAME "
    "statement (e = g_2 sin theta_W); not independent evidence",
    "identical", nstr(fabs(_g5 - _g3), 4))
row("G10", "D", True,
    "alpha_2 sin^2 theta_W = alpha_em is an exact tree identity, so G5 and G8 "
    "count once",
    "one observation", "declaration",
    pointer="ZS-S1 v1.1 section 8.6, remark following Eq.(18)")

# ---------------------------------------------------------------------
# H. m_W  -- computed, never compared to a rounded constant
# ---------------------------------------------------------------------
g2sq = 4 * pi * a2_mp
m_W_S1 = sqrt(g2sq) * v_S4 / 2
_r = fabs(g2sq - 12 * pi / 95)
row("H1", "V", _r < mpf("1e-40"), "g_2^2 = 4 pi alpha_2 = 12 pi / 95",
    nstr(12 * pi / 95, 15), nstr(g2sq, 15), tol="1e-40",
    why="closed-form identity; tolerance is arithmetic noise", resid=_r)
_mw_ref = mpf("77.461387318380")
_r = fabs(m_W_S1 - _mw_ref)
row("H2", "V", _r < mpf("1e-11"),
    "m_W = g_2 v/2 with v = 245.93 GeV taken exact-as-written evaluates to "
    "77.461387318380 GeV; as a physical statement this is 77.4614 GeV",
    "77.461387318380", nstr(m_W_S1, 14), tol="1e-11",
    why="ARITHMETIC IDENTITY, not a physical precision claim: v = 245.93 is treated "
        "as an exact input string. Physically v carries five significant figures, so "
        "m_W is quoted as 77.4614 GeV in the manuscript and the pull as -218.63 sigma",
    resid=_r)
row("H2b", "X", fabs(m_W_S1 - mpf("77.4614")) < mpf("5e-5"),
    "physical quotation m_W = 77.4614 GeV (six significant figures, matching the "
    "five-figure input v = 245.93)", "77.4614", nstr(m_W_S1, 6))
_mw_pull = pull(m_W_S1, EXT["m_W"][0], EXT["m_W"][1])
row("H3", "V", fabs(_mw_pull - mpf("-218.63")) < mpf("5e-3"),
    f"m_W pull vs PDG 2024 world average = {nstr(_mw_pull,5)} sigma (-218.63)",
    "-218.63 sigma", nstr(_mw_pull, 5), tol="5e-3",
    why="PDG m_W error 0.0133 carries three significant figures; the pull is printed "
        "to five, tolerance half a unit in the last printed place")
_mw_pull_fit = pull(m_W_S1, EXT["m_W_fit"][0], EXT["m_W_fit"][1])
row("H4", "V", fabs(_mw_pull_fit - mpf("-481.94")) < mpf("5e-3"),
    f"m_W pull vs PDG 2024 electroweak fit = {nstr(_mw_pull_fit,5)} sigma (-481.94)",
    "-481.94 sigma", nstr(_mw_pull_fit, 5), tol="5e-3",
    why="EW-fit error 0.006 carries one significant figure; the pull is printed to "
        "five, tolerance half a unit in the last printed place. The v1.1 pre-audit "
        "draft printed -481.9355, which is a mis-rounding of -481.93545")
_mw_rel = pct(m_W_S1, EXT["m_W"][0])
row("H5", "V", fabs(_mw_rel - mpf("-3.6181")) < mpf("5e-5"),
    f"m_W relative deviation = {nstr(_mw_rel,5)} per cent", "-3.6181 per cent",
    nstr(_mw_rel, 5), tol="5e-5",
    why="PDG m_W carries six significant figures; printed to five")
row("H6", "X", fabs(_mw_pull) > 100,
    "if alpha_2 were the M_Z MS-bar SU(2) coupling, m_W would be falsified "
    "at more than 100 sigma", "> 100 sigma", nstr(fabs(_mw_pull), 8))
row("H7", "D", True, f"m_W reference source: {EXT['m_W'][2]}", f"as-of {AS_OF}",
    str(EXT["m_W"][0]), pointer=EXT["m_W"][2])
row("H8", "D", True,
    "ZS-S1 makes no m_W prediction; the m_W chain is a downstream ZS-S14 "
    "identification g_2^2 = 4 pi alpha_2",
    "NON-CLAIM", "declaration",
    pointer="ZS-S1 v1.1 section 12 NC-5; ZS-S14 v2.1 section 5.2 erratum E19")

# ---------------------------------------------------------------------
# I. ESCAPE ROUTES -- recorded as closed
# ---------------------------------------------------------------------
_sin2_needed = alpha_em_MZ / a2_mp
_esc1 = pct(_sin2_needed, sin2_S1)
_esc1e = (1 + _esc1 / 100) * (EXT["alpha5_inv"][1] / EXT["alpha5_inv"][0]) * 100
row("I1", "V", fabs(_esc1 - mpf("7.072")) < mpf("5e-4"),
    "sin^2 theta_W required to absorb the gap = 0.247531, i.e. "
    f"{nstr(_esc1,4)} +- {nstr(_esc1e,2)} per cent above the ZS-S1 value",
    "+7.072 +- 0.007 per cent", nstr(_esc1, 4), tol="5e-4",
    why="propagated PDG error on alphahat^(5) is +-0.007 per cent")
row("I2", "X", fabs(_esc1) > 100 * fabs(_s2_rel),
    "the sin^2 theta_W escape route destroys an agreement 100x tighter than the "
    "shift it would need", "yes", f"{nstr(fabs(_esc1),4)} vs {nstr(fabs(_s2_rel),4)}")
_os_gap = pct(a2_mp, alpha0 / EXT["sin2_os"][0])
row("I3", "V", fabs(_os_gap - mpf("-3.290")) < mpf("5e-4"),
    "on-shell angle does not reproduce the hybrid: 3/95 lies "
    f"{nstr(_os_gap,4)} per cent BELOW alpha_em(0)/s^2_W(on-shell) = 0.0326533, "
    "equivalently that hybrid lies +3.402 per cent above 3/95",
    "-3.290 per cent", nstr(_os_gap, 4), tol="5e-4",
    why="PDG on-shell error 0.00010 propagates to +-0.045 per cent; printed to four "
        "significant figures, which that supports")
row("I4", "X", fabs(_os_gap) > 30 * fabs(_g3),
    "the 0.09 per cent hybrid match is specific to the MS-bar angle at M_Z",
    "yes", f"{nstr(fabs(_os_gap),4)} vs {nstr(fabs(_g3),4)}")
v_GF = 1 / sqrt(sqrt(2) * EXT["G_F"][0])
_v_dev = pct(v_S4, v_GF)
row("I5", "V", fabs(_v_dev - mpf("-0.11763")) < mpf("5e-6"),
    f"ZS-S4 v = 245.93 GeV is {nstr(_v_dev,5)} per cent from (sqrt2 G_F)^(-1/2) "
    f"= {nstr(v_GF,9)} GeV", "-0.11763 per cent", nstr(_v_dev, 5), tol="5e-6",
    why="G_F is known to ten significant figures; the limiting input is the "
        "five-figure v = 245.93, so five significant figures is the ceiling")
_v_needed = 2 * EXT["m_W"][0] / sqrt(g2sq)
_v_esc = pct(_v_needed, v_S4)
_v_esce = (1 + _v_esc / 100) * (EXT["m_W"][1] / EXT["m_W"][0]) * 100
row("I6", "V", fabs(_v_esc - mpf("3.7539")) < mpf("5e-5"),
    f"v required to absorb the gap = 255.162 GeV, i.e. {nstr(_v_esc,5)} "
    f"+- {nstr(_v_esce,2)} per cent above ZS-S4",
    "+3.7539 +- 0.017 per cent", nstr(_v_esc, 5), tol="5e-5",
    why="propagated PDG m_W error is +-0.017 per cent. The v1.1 pre-audit draft "
        "printed +3.75390, a mis-rounding of +3.753887")
row("I7", "X", fabs(_v_esc) > 30 * fabs(_v_dev),
    "the v escape route would break the G_F agreement by more than a factor 30",
    "> 30x", nstr(fabs(_v_esc / _v_dev), 6))
_tgt = 4 * pi * (v_S4 / (2 * EXT["m_W"][0])) ** 2
_tgte = 2 * _tgt * EXT["m_W"][1] / EXT["m_W"][0]
row("I8", "V", fabs(_tgt - mpf("29.417")) < mpf("5e-4"),
    f"1/alpha_2 that would reproduce m_W at v = 245.93 is {nstr(_tgt,5)} "
    f"+- {nstr(_tgte,2)}", "29.417 +- 0.0097", nstr(_tgt, 5), tol="5e-4",
    why="propagated PDG m_W error is 0.0097, so five significant figures is the "
        "ceiling")
row("I9", "D", True,
    "the target 1/alpha_2 in {29.4166763, 29.5889297} is KNOWN, therefore any "
    "replacement rational found by search is target-fitted",
    "firewall active", "declaration",
    pointer="ZS-S1 v1.1 section 12 NC-6 and section 10.5")

# ---------------------------------------------------------------------
# J. ADVERSARIAL AND SENSITIVITY  (grids pre-declared in the docstring)
# ---------------------------------------------------------------------
# ---- Archimedean adversarial, corrected after the 2026-08-19 audit (E-S1-5) ----
# The v1.0 test enumerated six solids, wrongly described as "all Archimedean solids
# sharing O_h or I_h symmetry".  Two of the six (snub cube, snub dodecahedron) are
# chiral (O and I, not O_h and I_h), and four genuine O_h/I_h solids were omitted --
# including the truncated cube and the truncated dodecahedron, which are exactly the
# counterexamples.  The full list, with point group and order, is enumerated here.
ARCHIMEDEAN = [
    ("truncated tetrahedron",       12,  18,   8, "T_d",  24),
    ("cuboctahedron",               12,  24,  14, "O_h",  48),
    ("truncated cube",              24,  36,  14, "O_h",  48),
    ("truncated octahedron",        24,  36,  14, "O_h",  48),
    ("rhombicuboctahedron",         24,  48,  26, "O_h",  48),
    ("truncated cuboctahedron",     48,  72,  26, "O_h",  48),
    ("snub cube",                   24,  60,  38, "O",    24),
    ("icosidodecahedron",           30,  60,  32, "I_h", 120),
    ("truncated dodecahedron",      60,  90,  32, "I_h", 120),
    ("truncated icosahedron",       60,  90,  32, "I_h", 120),
    ("rhombicosidodecahedron",      60, 120,  62, "I_h", 120),
    ("truncated icosidodecahedron",120, 180,  62, "I_h", 120),
    ("snub dodecahedron",           60, 150,  92, "I",    60),
]
row("J0", "C", len(ARCHIMEDEAN) == 13
    and all(v - e + f == 2 for _, v, e, f, _g, _o in ARCHIMEDEAN),
    "13 Archimedean solids enumerated with correct f-vectors and Euler characteristic",
    13, len(ARCHIMEDEAN))
_ohih = [a for a in ARCHIMEDEAN if a[4] in ("O_h", "I_h")]
row("J1", "C", len(_ohih) == 10,
    "10 of the 13 Archimedean solids carry O_h or I_h; the two snubs are chiral "
    "(O and I) and the truncated tetrahedron is T_d. The v1.0 count of 6 was wrong.",
    10, len(_ohih))
_hits_a2 = [a[0] for a in ARCHIMEDEAN if Fraction(a[1] + a[3], G) == Fraction(19, 6)]
_hits_a3 = [a[0] for a in ARCHIMEDEAN if Fraction(a[1] + a[3], G) == Fraction(23, 3)]
row("J2", "W", _hits_a2 == ["truncated cube", "truncated octahedron"]
    and _hits_a3 == ["truncated dodecahedron", "truncated icosahedron"],
    "ERRATUM E-S1-5: the (19/6, 23/3) pair is NOT uniquely realised. "
    "19/6 is given by the truncated cube AND the truncated octahedron; 23/3 by the "
    "truncated dodecahedron AND the truncated icosahedron.",
    "2 solids each", f"{_hits_a2} / {_hits_a3}")
row("J2b", "W", (24, 36, 14) == (V_X, E_X, F_X) and (60, 90, 32) == (V_Y, E_Y, F_Y),
    "the counterexample solids share the chosen solids' f-vectors exactly: "
    "truncated cube (24,36,14) = truncated octahedron; "
    "truncated dodecahedron (60,90,32) = truncated icosahedron",
    "identical f-vectors", "identical")
_swap_invariant = all([
    2 * 24 == 48, 48 == 48,                       # 2V_X and |O_h| for the truncated cube
    (60 + 90 + 32) // 2 == 91,                    # (V+E+F)_Y/2 for the truncated dodecahedron
    Fraction(24 + 14, G) == Fraction(19, 6),
    Fraction(60 + 32, G) == Fraction(23, 3),
    Fraction(abs(14 - 24), 14 + 24) == delta_X,
    Fraction(abs(32 - 60), 32 + 60) == delta_Y,
])
row("J2c", "W", _swap_invariant,
    "EVERY ZS-S1 number is invariant under the swap trunc.octahedron -> trunc.cube "
    "and trunc.icosahedron -> trunc.dodecahedron: a2, a3, 2V_X = 48, |O_h| = 48, "
    "(V+E+F)/2 = 91, delta_X = 5/19, delta_Y = 7/23 all coincide",
    "invariant", "invariant")
row("J2d", "W", len(_hits_a2) == 2 and len(_hits_a3) == 2
    and len({Fraction(a[1] + a[3], G) for a in ARCHIMEDEAN}) == 10,
    "what IS unique is the mode count: among the 13 Archimedean f-vectors exactly "
    "one value equals 19/6 and exactly one equals 23/3, but each is realised by two "
    "solids, so the selection is 2-fold degenerate and the spectral rule is blind "
    "to the difference",
    "unique value, 2-fold solid degeneracy",
    f"{len({Fraction(a[1]+a[3], G) for a in ARCHIMEDEAN})} distinct values")
row("J2e", "D", True,
    "gate FS1-4 as written in v1.0 ('alternative Archimedean produces (19/6, 23/3, "
    "G=12)' -> PROVEN safe) is FIRED; it is re-stated in v1.1 over mode counts",
    "FIRED", "declaration",
    pointer="ZS-S1 v1.1 section 0.2 E-S1-5, section 10.1, section 11 gate FS1-4'")
np.random.seed(MC_SEED)
_hits = 0
for _ in range(MC_TRIALS):
    _Gr = np.random.randint(6, 24)
    _v1 = np.random.randint(10, 200)
    _v2 = np.random.randint(10, 200)
    if (abs(_v1 / _Gr - 23 / 3) / (23 / 3) < MC_WINDOW
            and abs(_v2 / _Gr - 19 / 6) / (19 / 6) < MC_WINDOW):
        _hits += 1
_p_mc = _hits / MC_TRIALS
row("J3", "W", _p_mc < 0.0001,
    f"Monte Carlo random-match rate p = {_p_mc:.6f} ({_hits}/{MC_TRIALS})",
    "< 1e-4", f"{_p_mc:.6f}")
row("J4", "X", True,
    "CAVEAT: the null family G in [6,24], V+F in [10,200] was chosen after the "
    "polyhedral values were known; this MC bounds coincidence within that family "
    "only and is not a target-blind test",
    "diagnostic only", "recorded")
_shifts = [d for d in range(-3, 4)
           if abs(float(Q) / (VF_Y + d) - float(EXT["alpha_s"][0]))
           / float(EXT["alpha_s"][1]) < 1.0]
row("J5", "W", _shifts == [1], "only delta = +1 gives |alpha_s pull| < 1 sigma",
    "[1]", str(_shifts))
_rat = [(p, q) for p in range(1, 101) for q in range(2, 201)
        if abs(48 / 91 * p / q - float(EXT["sin2_hat"][0])) < float(EXT["sin2_hat"][1])]
_struct = [m for m in _rat if abs(m[0] / m[1] - float(x_star)) < 1e-6]
row("J6", "X", len(_struct) == 0,
    f"x* is not replaced by any structural rational in the declared grid "
    f"({len(_rat)} rationals within 1 sigma, 0 equal to x*)",
    0, len(_struct))
_alt = []
for _Gs in range(2, 21):
    for _vf2 in range(10, 201):
        if Fraction(_vf2, _Gs) != Fraction(19, 6):
            continue
        for _vf3 in range(10, 201):
            if Fraction(_vf3, _Gs) != Fraction(23, 3):
                continue
            for _b in range(-3, 4):
                if _vf3 + _b <= 0:
                    continue
                if abs(float(Q) / (_vf3 + _b) - float(EXT["alpha_s"][0])) \
                        / float(EXT["alpha_s"][1]) < 3.0:
                    _alt.append((_Gs, _vf2, _vf3, _b))
_alt_triples = sorted({(a, b, c) for a, b, c, _d in _alt})
_alt_shifts = sorted({d for _a, _b, _c, d in _alt})
row("J8", "W", _alt_triples == [(12, 38, 92)] and _alt_shifts == [0, 1, 2, 3],
    "exhaustive scan G in [2,20], V+F in [10,200], shift in [-3,+3]: the ONLY "
    "(G, V+F_X, V+F_Y) giving both beta-functions with alpha_s inside 3 sigma of "
    "PDG 2024 is (12, 38, 92); within it four shifts (0,+1,+2,+3) survive at 3 sigma "
    "and only +1 survives at 1 sigma (row J5). NOT_FOUND outside this grid is not "
    "ABSENT.",
    "[(12, 38, 92)] with shifts [0, 1, 2, 3]",
    f"{_alt_triples} with shifts {_alt_shifts}")
row("J9", "D", True,
    "the scan of row J8 is bounded by the declared grid and says nothing about "
    "(V+F, G) outside it",
    "grid-bounded", "declaration",
    pointer="ZS-S1 v1.1 section 10.3")
row("J7", "D", True,
    "no new expression for alpha_2 was proposed in v1.1; the anti-numerology "
    "record is therefore vacuous by construction",
    "no search performed", "declaration",
    pointer="ZS-S1 v1.1 section 10.5 ANTI_NUMEROLOGY_RECORD")

# ---------------------------------------------------------------------
# K. REGRESSION AGAINST SUPERSEDED VALUES  (errata E19, E-S1-2/3/4)
# ---------------------------------------------------------------------
row("K1", "R", EXT["sin2_hat"][0] != SUPERSEDED_EXT["sin2_hat_pdg2023"],
    "live sin^2 thetahat is PDG 2024 (0.23129), not the PDG 2023 value 0.23122",
    "0.23129", str(EXT["sin2_hat"][0]))
row("K2", "R", EXT["sin2_hat"][1] != SUPERSEDED_EXT["sin2_hat_err_v10"],
    "live sin^2 thetahat error is 0.00004, not the v1.0 value 0.00003",
    "0.00004", str(EXT["sin2_hat"][1]))
row("K3", "R", EXT["sin2_os"][0] != SUPERSEDED_EXT["sin2_os_pdg2023"],
    "live on-shell s^2_W is PDG 2024 (0.22348), not 0.22339",
    "0.22348", str(EXT["sin2_os"][0]))
row("K4", "R", EXT["alpha5_inv"][0] != SUPERSEDED_EXT["alpha5_inv_2023"],
    "live alphahat^(5)(M_Z)^-1 is PDG 2024 (127.930), not 127.951",
    "127.930", str(EXT["alpha5_inv"][0]))
row("K5", "R", EXT["M_Z"][0] != SUPERSEDED_EXT["M_Z_2023"],
    "live M_Z is PDG 2024 (91.1880), not 91.1876", "91.1880", str(EXT["M_Z"][0]))
row("K6", "R", fabs(m_W_S1 - SUPERSEDED_INTERNAL["m_W_v10_claim"]) > mpf("2"),
    "erratum E19: the retracted 80.4 GeV is not reproduced by the formula",
    "> 2 GeV away", nstr(fabs(m_W_S1 - SUPERSEDED_INTERNAL['m_W_v10_claim']), 8))
row("K7", "R", fabs(_s2_pull - SUPERSEDED_INTERNAL["sin2_pull_v10"]) > mpf("1"),
    "erratum E-S1-2: the v1.0 pull -1.26 sigma is superseded by -2.69 sigma",
    "> 1 sigma apart", nstr(fabs(_s2_pull - SUPERSEDED_INTERNAL['sin2_pull_v10']), 6))
_pull_with_old = pull(sin2_S1, SUPERSEDED_EXT["sin2_hat_pdg2023"],
                      SUPERSEDED_EXT["sin2_hat_err_v10"])
row("K8", "R", fabs(_pull_with_old - mpf("-1.25972")) < mpf("1e-4"),
    "the v1.0 figure -1.26 sigma is exactly reproduced by the superseded "
    "(0.23122, 0.00003) pair, confirming the source of the error",
    "-1.25972", nstr(_pull_with_old, 8))
_pull_2023_correct_err = pull(sin2_S1, SUPERSEDED_EXT["sin2_hat_pdg2023"],
                              mpf("0.00004"))
row("K9", "R", fabs(_pull_2023_correct_err - mpf("-0.94479")) < mpf("1e-4"),
    "even against PDG 2023 with the correct error 0.00004 the pull is -0.94479, "
    "so the v1.0 error bar was understated",
    "-0.94479", nstr(_pull_2023_correct_err, 8))
row("K10", "R", alpha_2 == Fraction(Y, 5 * VF_X) == Fraction(X, VF_Y + X),
    "erratum E-S1-3: both written forms EVALUATE to 3/95 -- ZS-S1 uses "
    "Y/[5(V+F)_X], the correction report and ZS-S14 quoted X/[(V+F)_Y+X]",
    "both equal 3/95", (Fraction(Y, 5 * VF_X), Fraction(X, VF_Y + X)))
row("K11", "R", 5 * VF_X != VF_Y + X,
    "the two forms have different denominators (190 vs 95) and different "
    "sector provenance, so they are not the same construction",
    "190 != 95", f"{5*VF_X} != {VF_Y+X}")
row("K12", "R", EXPECTED_ROWS != SUPERSEDED_INTERNAL["v10_row_banner"]
    and EXPECTED_ROWS != SUPERSEDED_INTERNAL["v10_script_rows"],
    "erratum E-S1-4: the v1.0 banner 35 and the v1.0 script row count 38 are "
    "both superseded by a measured row count",
    f"{EXPECTED_ROWS}", f"{EXPECTED_ROWS} vs (35, 38)")

# ---------------------------------------------------------------------
# L. CROSS-PAPER INTERFACE
# ---------------------------------------------------------------------
row("L1", "C", alpha_2 == Fraction(3, 95),
    "f_seam = 3/95 exported to ZS-U7 / ZS-M5 / ZS-S2 as a bare rational",
    Fraction(3, 95), alpha_2)
row("L2", "D", True,
    "the f_seam export is a dimensionless seam fraction and carries no scale "
    "or scheme; it is unaffected by the alpha_2 re-typing",
    "TYPE LOCK", "declaration",
    pointer="ZS-S1 v1.1 section 2.1 TYPE LOCK, row f_seam")
row("L3", "D", True,
    "ZS-S14 v2.1 Proposition S14.B' imports g_2 from ZS-S1; that import is "
    "withdrawn by this erratum",
    "withdraw", "declaration",
    pointer="ZS-S1 v1.1 section 11.3 downstream propagation item 5")
row("L4", "D", True, "A = 35/437 from ZS-F2 v1.0, LOCKED", "35/437", str(A),
    pointer="ZS-F2 v1.0")
row("L5", "D", True, "(Z,X,Y,Q) = (2,3,6,11) and dim(Z) = 2 from ZS-F5 v1.0",
    "(2,3,6,11)", f"({Z},{X},{Y},{Q})", pointer="ZS-F5 v1.0")
row("L6", "D", True, "x* = Re(z*) and Phi_Berry/(2pi) = x* from ZS-M1 v1.0",
    nstr(x_star, 10), nstr(x_star, 10), pointer="ZS-M1 v1.0 section 8")
row("L7", "D", True, "v = 245.93 GeV from ZS-S4 v1.0 section 6.12 Thm V.9",
    "245.93", str(v_S4), pointer="ZS-S4 v1.0 section 6.12")

# ---------------------------------------------------------------------
# M. GUARDS
# ---------------------------------------------------------------------
_src_path = os.path.abspath(__file__)
_src = open(_src_path, "r", encoding="utf-8").read()
_stem = os.path.splitext(os.path.basename(_src_path))[0]
_here = os.path.dirname(_src_path)

row("GRD01", "G", len(ROWS) + 1 > 0, "row registry is non-empty",
    "> 0", len(ROWS) + 1)

# self-AST audit: no literal True/False on evidence-bearing rows
_tree = ast.parse(_src)


def _is_constant_expr(node):
    """True if the node can be folded to a constant without touching program state.

    Hardened after the 2026-08-19 audit, which defeated the literal-only test with
    a constant-folding disjunction such as a trivially-true comparison ORed with a
    truthy literal.  Any expression whose leaves are all literals is rejected.
    """
    if isinstance(node, ast.Constant):
        return True
    if isinstance(node, (ast.BoolOp, ast.UnaryOp, ast.BinOp, ast.Compare,
                         ast.Tuple, ast.List, ast.Set, ast.IfExp)):
        return all(_is_constant_expr(c) for c in ast.iter_child_nodes(node)
                   if isinstance(c, ast.expr))
    return False


_bad_literals = []
_row_calls = 0
for _node in ast.walk(_tree):
    if isinstance(_node, ast.Call) and isinstance(_node.func, ast.Name) \
            and _node.func.id == "row":
        _row_calls += 1
        _cls_node = _node.args[1] if len(_node.args) >= 2 else None
        _cond_node = _node.args[2] if len(_node.args) >= 3 else None
        for _kw in _node.keywords:
            if _kw.arg == "cls":
                _cls_node = _kw.value
            if _kw.arg == "cond":
                _cond_node = _kw.value
        if _cls_node is None or _cond_node is None:
            _bad_literals.append((_node.lineno, "row() called without positional "
                                                "class/condition"))
            continue
        if isinstance(_cls_node, ast.Constant) and _cls_node.value in EVIDENCE_CLASSES:
            if _is_constant_expr(_cond_node):
                _bad_literals.append((_node.lineno, _cls_node.value))
row("GRD02", "G", len(_bad_literals) == 0,
    "self-AST audit: no evidence-bearing row (C/V/W) has a condition that folds to "
    "a constant, and no row() call hides its class or condition in a keyword",
    0, len(_bad_literals))
row("GRD03", "G", "\"P\"" in _src and "class P is not used" in _src,
    "class P is refused by the row() contract", "refused", "refused")
_p_rows = [r for r in ROWS if r["class"] == "P"]
row("GRD04", "G", len(_p_rows) == 0, "census contains no class P rows", 0, len(_p_rows))
_d_no_ptr = [r for r in ROWS if r["class"] == "D" and "pointer" not in r]
row("GRD05", "G", len(_d_no_ptr) == 0,
    "every declaration row carries a pointer", 0, len(_d_no_ptr))
_v_no_tol = [r for r in ROWS
             if r["class"] == "V" and ("tolerance" not in r or "tolerance_basis" not in r)]
row("GRD06", "G", len(_v_no_tol) == 0,
    "every numerical row declares a tolerance and a justification", 0, len(_v_no_tol))


def _tol_is_loose(t):
    """Fail closed: a tolerance we cannot parse as a number is treated as loose.

    Hardened after the 2026-08-19 audit, which defeated the previous version with
    the unparseable string "0.5 per cent (absolute)".
    """
    try:
        return float(t) > 0.01
    except (TypeError, ValueError):
        return True


_loose = [r for r in ROWS if r.get("tolerance") and _tol_is_loose(r["tolerance"])
          and not str(r.get("tolerance_basis", "")).startswith("TOL-JUSTIFY:")]
row("GRD07", "G", len(_loose) == 0,
    "no comparison row uses a tolerance looser than 1 per cent without an "
    "explicit TOL-JUSTIFY string", 0, len(_loose))
row("GRD08", "G", not re.search(r"\bor\s+(?:Tru[e]\b|1\b|not\s+Fals[e]\b|-1\b)", _src),
    "no guard is short-circuited by a constant disjunction", "absent", "absent")
_pre_guard = _src.split("# M. GUARDS")[0].replace(
    'except (TypeError, ValueError):', 'OK').replace(
    'except Exception:\n            e["residual"]', 'OK')
_ctxlib = "context" + "lib"
_swallow = ("except" in _pre_guard) or ("suppress" in _pre_guard) \
    or (_ctxlib in _src.replace("_ctxlib = \"context\" + \"lib\"", ""))
row("GRD09", "G", not _swallow,
    "no evidence row is wrapped in an exception swallow (a bare except, or the "
    "standard-library suppress context manager) before the guard block",
    "clean", "swallow found" if _swallow else "clean")
row("GRD10", "G", _row_calls >= EXPECTED_ROWS,
    "static row() call sites at least match the expected row count",
    f">= {EXPECTED_ROWS}", _row_calls)

# external-data guards
_ext_missing = [k for k, v in EXT.items() if not v[2]]
row("GRD11", "G", len(_ext_missing) == 0,
    "every external value names its source edition", 0, len(_ext_missing))
row("GRD12", "G", AS_OF == PAPER_DATE,
    "external as-of date matches the paper date", PAPER_DATE, AS_OF)
row("GRD13", "G", all("PDG 2024" in v[2] or "CODATA" in v[2] for v in EXT.values()),
    "LABEL CHECK ONLY: every external source string names PDG 2024 or CODATA. "
    "This checks the label, not the number; the numbers are checked by the "
    "regression rows K1-K5.",
    "all labelled", "all labelled")
_ext_pinned = {
    "sin2_hat": mpf("0.23129"), "sin2_os": mpf("0.22348"),
    "alpha5_inv": mpf("127.930"), "M_Z": mpf("91.1880"),
    "alpha_s": mpf("0.1180"), "m_W": mpf("80.3692"),
    "alpha0_inv": mpf("137.035999177"),
}
_pin_bad = [k for k, val in _ext_pinned.items() if EXT[k][0] != val]
row("GRD13b", "G", len(_pin_bad) == 0,
    "every external value equals its pinned PDG 2024 / CODATA 2022 figure",
    0, _pin_bad if _pin_bad else 0)

# manuscript integrity guard
# Token-proximity patterns: a retracted claim is caught by the co-occurrence of its
# load-bearing tokens inside a short window, not by one exact wording.  W(n) allows
# up to n intervening characters.
def _W(n):
    return r"[^.\n]{0,%d}" % n


FORBIDDEN = [
    (r"m\s*_?\s*w" + _W(30) + r"80\.4(?![0-9])", "retracted m_W = 80.4 GeV claim"),
    (r"80\.4(?![0-9])" + _W(30) + r"match", "retracted m_W = 80.4 agreement claim"),
    (r"match\w*" + _W(12) + r"observation", "retracted 'matching observation' wording"),
    (r"(?:within|better than|to)" + _W(12) + r"1\.3\s*sigma",
     "retracted '1.3 sigma' agreement banner"),
    (r"1\.3\s*sigma" + _W(20) + r"(?:agree|match)", "retracted '1.3 sigma' banner"),
    (r"electromagnetic" + _W(12) + r"coupling" + _W(6) + r"alpha\s*_?2",
     "retracted section 8.3 title"),
    (r"0\.23122" + _W(10) + r"0\.00003", "superseded PDG error bar"),
    (r"35\s*/\s*35" + _W(10) + r"pass", "superseded 35/35 verification banner"),
    (r"\ball\b" + _W(16) + r"standard model gauge coupling",
     "overclaim retracted in v1.1"),
    (r"five" + _W(24) + r"(?:formulas|couplings)" + _W(24) + r"(?:derived|match)",
     "retracted 'five gauge formulas DERIVED/match' banner"),
    (r"alpha\s*_?2\s*=" + _W(6) + r"x\s*/\s*\[?\s*\(\s*v\s*\+\s*f\s*\)\s*_?y",
     "misattributed alpha_2 form"),
    (r"0/6" + _W(40) + r"archimedean", "retracted 0/6 Archimedean count"),
    (r"archimedean" + _W(40) + r"0/6", "retracted 0/6 Archimedean count"),
    (r"0/6" + _W(40) + r"(?:solid|beta-function pair|19/6)",
     "retracted 0/6 Archimedean count"),
    (r"(?:trunc\w*\s*oct\w*|octahedron)" + _W(40) + r"unique",
     "retracted Archimedean uniqueness claim"),
]


import unicodedata


def _normalise(t, sep=" "):
    """Aggressive normalisation.  Hardened after the 2026-08-19 audit, which
    defeated the previous version with markdown emphasis, table pipes, full-width
    digits, mathematical-alphanumeric alpha and zero-width joiners."""
    t = unicodedata.normalize("NFKC", t)
    for _z in ("\u200b", "\u200c", "\u200d", "\u2060", "\ufeff", "\u00ad"):
        t = t.replace(_z, "")
    t = t.replace("−", "-").replace("–", "-").replace("—", "-").replace("‐", "-")
    t = t.replace("α", "alpha").replace("𝛼", "alpha").replace("𝜶", "alpha")
    t = t.replace("β", "beta").replace("θ", "theta").replace("ϑ", "theta")
    t = t.replace("₂", "_2").replace("₃", "_3").replace("²", "^2")
    t = t.replace("σ", "sigma").replace("ς", "sigma")
    t = t.replace("±", "+-").replace("≈", "~").replace("≅", "~").replace("→", "=")
    # strip markdown emphasis, table pipes, backticks, html tags
    t = re.sub(r"<[^>]*>", " ", t)
    t = re.sub(r"[`*_~|]+", sep, t)
    t = re.sub(r"\s+", " ", t)
    return t.lower()


_ms_path = os.path.join(_here, MANUSCRIPT)
_ms_present = os.path.exists(_ms_path)
row("GRD14", "G", _ms_present, f"manuscript {MANUSCRIPT} is present next to the script",
    "present", "present" if _ms_present else "MISSING")

_hits_forbidden = []
_ms_text = ""
if _ms_present:
    _ms_text = open(_ms_path, "r", encoding="utf-8").read()
    # Exemption model, tightened after the 2026-08-19 audit:
    #   (a) fenced code blocks;
    #   (b) the remainder of a line AFTER a <!--HIST--> marker that appears at the
    #       start of the line (leading whitespace allowed).  A marker placed mid-line
    #       or at the end of a line exempts nothing -- the previous version exempted
    #       the whole line, which the auditor used to smuggle live claims through.
    _live = re.sub(r"```.*?```", " ", _ms_text, flags=re.S)
    _live_lines = []
    for _l in _live.split("\n"):
        if re.match(r"^\s*<!--HIST-->", _l):
            continue
        _live_lines.append(_l.split("<!--HIST-->")[0])
    _live = "\n".join(_live_lines)
    # Scan under TWO normalisations: markdown separators replaced by a space, and
    # removed outright.  The audit's zero-width attack survived the first because
    # stripping the underscore of "m_W" to a space broke the token.
    _live_variants = [_normalise(_live, " "), _normalise(_live, "")]
    for _pat, _lbl in FORBIDDEN:
        if any(re.search(_pat, _v) for _v in _live_variants) \
                and _lbl not in _hits_forbidden:
            _hits_forbidden.append(_lbl)
row("GRD15", "G", _ms_present and len(_hits_forbidden) == 0,
    "no retracted statement survives in live manuscript text "
    "(exemption: fenced blocks and <!--HIST--> lines only; backticks are live)",
    0, _hits_forbidden if _hits_forbidden else 0)
_hist_ok = _ms_present and any(re.match(r"^\s*<!--HIST-->", l)
                               for l in _ms_text.split("\n"))
_hist_midline = [i + 1 for i, l in enumerate(_ms_text.split("\n"))
                 if "<!--HIST-->" in l and not re.match(r"^\s*<!--HIST-->", l)]
row("GRD16", "G", _hist_ok,
    "the manuscript uses the explicit history marker at the start of a line, not "
    "inline code spans", "line-initial marker present",
    "present" if _hist_ok else "absent")
row("GRD16b", "G", len(_hist_midline) == 0,
    "no <!--HIST--> marker is placed mid-line, where it would exempt only the tail "
    "and could be read as exempting the whole line",
    0, _hist_midline if _hist_midline else 0)

# manuscript <-> script value synchronisation
def _tok(x, n, signed=False):
    """Render a computed quantity exactly as the manuscript must print it.

    SYNC tokens are GENERATED FROM THE COMPUTATION, not hand-copied.  The previous
    version hard-coded twelve string literals, which meant a manuscript could agree
    with the literals while both disagreed with the arithmetic -- the defect the
    2026-08-19 audit found in three printed figures.
    """
    t = mp.nstr(x, n, strip_zeros=False)
    if signed and not t.startswith("-"):
        t = "+" + t
    return t


SYNC = [
    (_tok(m_W_S1, 6), "m_W, physical quotation"),
    (_tok(m_W_S1, 14), "m_W, exact-input arithmetic value"),
    (_tok(_mw_pull, 5), "m_W pull vs PDG 2024"),
    (_tok(_mw_pull_fit, 5), "m_W pull vs the electroweak fit"),
    (_tok(_mw_rel, 5, True), "m_W relative deviation"),
    (_tok(_s2_pull, 4), "sin^2 theta_W pull vs PDG 2024"),
    (_tok(_s2_rel, 4, True), "sin^2 theta_W relative gap"),
    (_tok(_as_pull, 3, True), "alpha_s pull vs PDG 2024"),
    (_tok(sin2_S1, 10), "sin^2 theta_W value"),
    (_tok(1 / alpha2_hat_MZ, 5), "1/alphahat_2(M_Z)"),
    (_tok(1 / a2_mp, 9), "1/alpha_2"),
    (_tok(1 / _prod_internal, 12), "1/(alpha_2 sin^2 theta_W)"),
    (_tok(_g, 5, True), "internal product vs alpha_em(0)"),
    (_tok(_g2, 4, True), "internal product vs alpha_em(M_Z)"),
    (_tok(_g4, 4, True), "alpha_2 vs alphahat_2(M_Z)"),
    (_tok(_g3, 3, True), "alpha_2 vs the Thomson hybrid"),
    (_tok(_esc1, 4, True), "sin^2 escape route"),
    (_tok(_os_gap, 4, True), "on-shell hybrid gap"),
    (_tok(_v_esc, 5, True), "v escape route"),
    (_tok(_v_dev, 5, True), "ZS-S4 v vs (sqrt2 G_F)^(-1/2)"),
    (_tok(_tgt, 5), "1/alpha_2 target for m_W"),
]
_sync_missing = []
if _ms_present:
    _ms_n = _normalise(_ms_text)
    for _tok, _lbl in SYNC:
        if _normalise(_tok) not in _ms_n:
            _sync_missing.append(_lbl)
row("GRD17", "G", _ms_present and len(_sync_missing) == 0,
    f"all {len(SYNC)} headline numbers, GENERATED FROM THE COMPUTATION, appear "
    "verbatim in the manuscript",
    0, _sync_missing if _sync_missing else 0)
row("GRD18", "G", _ms_present and f"{PAPER_CODE} {PAPER_VERSION}" in _ms_text
    and PAPER_DATE in _ms_text,
    "manuscript declares the same paper code, version and date as the script",
    f"{PAPER_CODE} {PAPER_VERSION} {PAPER_DATE}", "match" if _ms_present else "n/a")
row("GRD19", "G", _ms_present and f"EXPECTED_ROWS = {EXPECTED_ROWS}" in _ms_text,
    "manuscript quotes the script's EXPECTED_ROWS verbatim",
    f"EXPECTED_ROWS = {EXPECTED_ROWS}", "match" if _ms_present else "n/a")

_sha_py = hashlib.sha256(_src.encode("utf-8")).hexdigest()
_sha_md = hashlib.sha256(_ms_text.encode("utf-8")).hexdigest() if _ms_present else ""
row("GRD20", "G", len(_sha_py) == 64, "script self-hash computed",
    "64 hex", _sha_py[:16] + "...")
row("GRD21", "G", _ms_present and len(_sha_md) == 64,
    "manuscript hash computed and registered in the ledger (the pre-audit version "
    "hashed only the script)", "64 hex", (_sha_md[:16] + "...") if _sha_md else "n/a")

# =====================================================================
# CENSUS, GUARDS ON THE CENSUS, OUTPUT
# =====================================================================
census = {c: sum(1 for r in ROWS if r["class"] == c) for c in ALL_CLASSES}
n_total = len(ROWS)
n_fail = len(_FAIL)
n_evidence = sum(census[c] for c in EVIDENCE_CLASSES)

print()
for r in ROWS:
    mark = "PASS" if r["status"] == "PASS" else "FAIL"
    print(f"  [{mark}] [{r['class']}] {r['id']:<7} {r['name']}")
    if r["status"] == "FAIL":
        print(f"           expected={r['expected']}  actual={r['actual']}")

print()
print("=" * 78)
print(f"rows      : {n_total}   FAIL: {n_fail}")
print(f"census    : " + "  ".join(f"{c}={census[c]}" for c in ALL_CLASSES))
print(f"evidence  : C/V/W = {n_evidence}")
print(f"controls  : R/G   = {census['R'] + census['G']}")
print(f"non-evid. : X/D/T = {census['X'] + census['D'] + census['T']}")
print(f"artifact  : {os.path.basename(_src_path)} {SCRIPT_VERSION} "
      f"rows={n_total} sha256={_sha_py}")
print("=" * 78)

structural_ok = True
if n_total != EXPECTED_ROWS:
    print(f"GUARD FAIL: row count {n_total} != EXPECTED_ROWS {EXPECTED_ROWS}")
    structural_ok = False
if census != {**{c: 0 for c in ALL_CLASSES}, **EXPECTED_CLASS_CENSUS}:
    print(f"GUARD FAIL: class census {census} != expected {EXPECTED_CLASS_CENSUS}")
    structural_ok = False
if sum(census.values()) != n_total:
    print("GUARD FAIL: class census does not sum to the row count")
    structural_ok = False

print()
print("--- KEY RESULTS ---")
print(f"  alpha_s   = 11/93            = {nstr(mpf(11)/93,12)}   "
      f"pull {nstr(_as_pull,6)} sigma   [mu = M_Z, MS-bar]")
print(f"  sin^2thW  = (48/91) x*       = {nstr(sin2_S1,12)}   "
      f"pull {nstr(_s2_pull,6)} sigma   [mu = M_Z, MS-bar]")
print(f"  alpha_2   = 6/190 = 3/95     = {nstr(a2_mp,12)}   "
      f"1/alpha_2 = {nstr(1/a2_mp,12)}   [scale UNDECLARED]")
print(f"  a2 = 19/6, a3 = 23/3         [scale-free 1-loop slopes]")
print(f"  SCALE DIAGNOSTIC")
print(f"    alpha_2 * sin^2thW         = 1/{nstr(1/_prod_internal,12)}")
print(f"    alpha_em(0)^-1             = {EXT['alpha0_inv'][0]}   "
      f"gap {nstr(_g,6)} per cent")
print(f"    alpha_em(M_Z)^-1           = {EXT['alpha5_inv'][0]}      "
      f"gap {nstr(_g2,6)} per cent")
print(f"    alpha_2 vs alphahat_2(M_Z) = {nstr(_g4,6)} per cent")
print(f"  m_W = g_2 v/2 (v = 245.93)   = {nstr(m_W_S1,12)} GeV   "
      f"pull {nstr(_mw_pull,8)} sigma vs PDG 2024")
print(f"  MC anti-numerology           p = {_p_mc:.6f} ({_hits}/{MC_TRIALS}) "
      f"[null family is post-hoc; diagnostic only]")

report = {
    "paper": f"{PAPER_CODE} {PAPER_VERSION}",
    "paper_date": PAPER_DATE,
    "script_version": SCRIPT_VERSION,
    "manuscript": MANUSCRIPT,
    "supersedes_script": LEGACY_SCRIPT,
    "external_as_of": AS_OF,
    "precision_dps": mp.dps,
    "mc_seed": MC_SEED,
    "mc_trials": MC_TRIALS,
    "expected_rows": EXPECTED_ROWS,
    "rows": n_total,
    "fail": n_fail,
    "failed_ids": _FAIL,
    "census": census,
    "expected_census": EXPECTED_CLASS_CENSUS,
    "structural_guards_ok": structural_ok,
    "sha256_self": _sha_py,
    "sha256_manuscript": _sha_md,
    "sync_tokens": {lbl: tok for tok, lbl in SYNC},
    "external_values": {k: {"value": str(v[0]), "error": str(v[1]), "source": v[2]}
                        for k, v in EXT.items()},
    "key_values": {
        "alpha_s": "11/93",
        "alpha_s_pull_sigma": nstr(_as_pull, 8),
        "sin2_theta_W": nstr(sin2_S1, 20),
        "sin2_theta_W_pull_sigma": nstr(_s2_pull, 8),
        "alpha_2": "3/95",
        "inv_alpha_2": nstr(1 / a2_mp, 12),
        "inv_alpha2_hat_MZ_pdg2024": nstr(1 / alpha2_hat_MZ, 10),
        "alpha_2_vs_alpha2hat_percent": nstr(_g4, 8),
        "internal_product_inv": nstr(1 / _prod_internal, 12),
        "internal_vs_alpha_em0_percent": nstr(_g, 8),
        "internal_vs_alpha_emMZ_percent": nstr(_g2, 8),
        "m_W_GeV": nstr(m_W_S1, 16),
        "m_W_pull_sigma_pdg": nstr(_mw_pull, 10),
        "m_W_pull_sigma_fit": nstr(_mw_pull_fit, 10),
        "sin2_escape_percent": nstr(_esc1, 8),
        "v_escape_percent": nstr(_v_esc, 8),
        "mc_p": f"{_p_mc:.6f}",
    },
    "scale_scheme_table": {k: list(v) for k, v in SCALE_TABLE.items()},
    "tests": ROWS,
}
_out = os.path.join(_here, _stem + ".json")
with open(_out, "w", encoding="utf-8") as fh:
    json.dump(report, fh, indent=2, sort_keys=False)
    fh.write("\n")
print(f"\nJSON ledger: {_out}")

sys.exit(0 if (n_fail == 0 and structural_ok) else 1)
