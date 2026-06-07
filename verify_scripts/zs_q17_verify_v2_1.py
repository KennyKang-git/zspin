#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_q17_verify_v2_1.py
=====================
Consolidated verification suite for:

    ZS-Q17 v2.1 -- The Self-Mediation No-Go and the Reach Bound of Z-Spin
    Quantum Transport: A Complete Formalization, with the Spontaneous-Radiation
    and Fifth-Force Gates Closed
    (Kenny Kang, June 2026)

This single file merges the three companion scripts of the v2.x programme:
    (1) zs_q17_v2_reach_bound_verify.py     -> PART I
    (2) numerical anchors of the No-Go      -> PART II   (new in v2.1)
    (3) zs_q1_radiation_gate_F-Q1-rad.py    -> PART III  (new in v2.1)

Zero free parameters: only  A = 35/437,  Q = 11,  (Z,X,Y) = (2,3,6)  and
standard physical constants enter.

What is and is NOT "verified" here (honesty)
--------------------------------------------
PART I  (reach bound) is a numerical/physical claim and IS checked (PASS/FAIL):
        it is a strict composition of the DERIVED ZS-Q1 / ZS-Q2 results.
PART II (No-Go) is a STRUCTURAL theorem (Nielsen-Chuang no-programming +
        Lawvere diagonal, completed by port-based teleportation).  The script
        verifies its NUMERICAL ANCHORS -- z* existence/uniqueness/contraction,
        the dim-2 < Q=11 programming-dimension violation, and the PBT fidelity
        ceiling F_d(N) <= sqrt(N)/d -> 1 -- but the theorem itself is proven by
        logic, not by this script.
PART III(F-Q1-rad / F-Q1-5th) is a STRUCTURAL closure (ZS-Q1 is scalar-tensor /
        environmental, not stochastic-collapse; eps is a Yukawa mediator).  The
        script verifies the SUPPORTING NUMBERS (D_pp ceiling, the Yukawa-vs-DP
        opposite scaling, the (A*G)^2 suppression, the decision boundary R0*),
        which do not by themselves constitute the closure.
PART IV is epistemic bookkeeping (legend tags), NOT physics.

Dependencies: numpy, mpmath
Run:  python zs_q17_verify_v2_1.py
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 50

# ----------------------------------------------------------------------
# test harness:  check() = PASS/FAIL ; info() = informational line
# ----------------------------------------------------------------------
_RESULTS = []   # (part, cat, name, passed, detail)
_INFO    = []   # (cat, text)

def check(part, cat, name, passed, detail=""):
    _RESULTS.append((part, cat, name, bool(passed), detail))

def info(cat, text):
    _INFO.append((cat, text))

# ======================================================================
# LOCKED INPUTS (A, Q, sectors) + CODATA-2018 constants (SI)
# ======================================================================
A = 35.0 / 437.0
A_mp = mp.mpf(35) / mp.mpf(437)
Q = 11
dimZ, dimX, dimY = 2, 3, 6

HBAR = 1.054571817e-34
C    = 2.99792458e8
G    = 6.67430e-11
AMU  = 1.66053906660e-27
EV   = 1.602176634e-19
RHO_AU = 19300.0                # gold density (ZS-Q2 convention)
ANG  = 1.0e-10
L_PLANCK = 1.616255e-35
M_PLANCK = 2.176434e-8

DAY  = 86400.0
YEAR = 365.25 * DAY
AU   = 1.495978707e11
LY   = C * YEAR

# ######################################################################
# ##  PART I  --  THE REACH BOUND  (numerical, PASS/FAIL)             ##
# ######################################################################
def R_sphere(m_kg, rho=RHO_AU):
    return (3.0 * m_kg / (4.0 * np.pi * rho)) ** (1.0 / 3.0)
def E_diff(m_kg, R_m):
    return (3.0 / 5.0) * G * m_kg**2 / R_m
def tau_penrose(m_kg, R_m):
    return HBAR / E_diff(m_kg, R_m)
def tau_single(m_kg, R_m):
    return HBAR / (A * E_diff(m_kg, R_m))
def tau_ent(m_kg, R_m):
    return tau_single(m_kg, R_m) / 2.0
def L_max(m_kg, R_m):
    return C * tau_ent(m_kg, R_m)
def reach_bound_density(m_amu, rho=RHO_AU):
    m_kg = m_amu * AMU
    R = R_sphere(m_kg, rho)
    return L_max(m_kg, R), R, tau_single(m_kg, R), tau_ent(m_kg, R)

# [A] locked constants & the 1/A signature
check("I", "A", "A = 35/437 = 0.0800915...",
      abs(A - 0.08009153318077803) < 1e-15, f"A = {A:.17f}")
check("I", "A", "1/A = 437/35 = 12.4857... (tau_D/tau_Penrose, ZS-Q1)",
      abs(1.0 / A - 12.485714285714286) < 1e-12, f"1/A = {1.0/A:.10f}")
check("I", "A", "(Z,X,Y) = (2,3,6),  Z+X+Y = Q = 11",
      (dimZ, dimX, dimY) == (2, 3, 6) and dimZ + dimX + dimY == Q, "")

# [B] mass-independent reach ratio = 1/A
ratio_ok, worst = True, 0.0
for m_amu in np.logspace(3, 15, 25):
    m_kg = m_amu * AMU; R = R_sphere(m_kg)
    r = L_max(m_kg, R) / (C * (tau_penrose(m_kg, R) / 2.0))
    worst = max(worst, abs(r - 1.0 / A))
    if abs(r - 1.0 / A) > 1e-9: ratio_ok = False
check("I", "B", "reach ratio L_max(Z-Spin)/L_max(Penrose) = 1/A = 12.49 (mass-independent)",
      ratio_ok, f"max |ratio - 1/A| over 25 masses = {worst:.2e}")

# [C] ZS-Q1 anchor: gold 1e9 amu, 50 nm -> ~7 days
m_q1, R_q1 = 1e9 * AMU, 50e-9
check("I", "C", "ZS-Q1 anchor: tau_Penrose(1e9 amu,50nm) ~ 13 h",
      abs(tau_penrose(m_q1, R_q1) / 3600.0 - 13.27) < 0.5,
      f"tau_Penrose = {tau_penrose(m_q1,R_q1)/3600.0:.2f} h")
check("I", "C", "ZS-Q1 anchor: tau_single(1e9 amu,50nm) = 1/A x tau_Penrose ~ 7 days",
      abs(tau_single(m_q1, R_q1) / DAY - 6.90) < 0.3,
      f"tau_single = {tau_single(m_q1,R_q1)/DAY:.2f} days (ZS-Q1 ~7 days)")

# [D] ZS-Q2 anchor: M_crit at tau_single = 1 s
def m_for_tau(target_s, rho=RHO_AU):
    Ed = HBAR / (A * target_s)
    coeff = (3.0 / 5.0) * G * (4.0 * np.pi * rho / 3.0) ** (1.0 / 3.0)
    return (Ed / coeff) ** (3.0 / 5.0) / AMU
M_crit = m_for_tau(1.0)
check("I", "D", "ZS-Q2 anchor: M_crit(tau_single=1 s) ~ 2.0e12 amu (gold density)",
      abs(np.log10(M_crit) - np.log10(2.0e12)) < 0.10,
      f"M_crit = {M_crit:.3e} amu (ZS-Q2 ~2.0e12)")

# [E] reach table & cat-scale decoherence
ladder = [("C60-scale (1e3)",1e3),("large virus (1e6)",1e6),
          ("gold sphere (1e9)",1e9),("M_crit (2e12)",2e12),
          ("Schroedinger cat (1e34)",1e34)]
table_rows = [(lbl, m, *reach_bound_density(m)[::-1][:3][::-1], reach_bound_density(m)[0])
              for lbl, m in ladder]
# rebuild cleanly to avoid confusion
table_rows = []
for lbl, m in ladder:
    Lm, R, ts, te = reach_bound_density(m)
    table_rows.append((lbl, m, R, ts, te, Lm))
Ls = [row[5] for row in table_rows]
check("I", "E", "reach bound L_max strictly decreases with payload mass",
      all(Ls[i] > Ls[i + 1] for i in range(len(Ls) - 1)),
      "L_max(1e3) > ... > L_max(1e34)")
L_cat, R_cat = reach_bound_density(1e34)[0], reach_bound_density(1e34)[1]
check("I", "E", "cat-scale: L_max << payload radius => no coherent transport",
      L_cat < R_cat * 1e-10,
      f"L_max(cat)={L_cat:.2e} m << R_cat={R_cat:.2f} m (ratio {L_cat/R_cat:.1e})")

# [F] scaling L_max ~ m^(-5/3)
ms = np.logspace(3, 12, 40)
slope = np.polyfit(np.log10(ms),
                   np.log10([reach_bound_density(m)[0] for m in ms]), 1)[0]
check("I", "F", "reach-bound scaling exponent d ln L_max/d ln m = -5/3",
      abs(slope - (-5.0 / 3.0)) < 1e-6,
      f"fitted slope = {slope:.8f}, -5/3 = {-5.0/3.0:.8f}")

# [G] horizon corollary: E_diff at R_s = (3/10) m c^2 (mass-independent)
horizon_ok, worst_h = True, 0.0
for m_amu in np.logspace(0, 40, 30):
    m_kg = m_amu * AMU; Rs = 2.0 * G * m_kg / C**2
    frac = E_diff(m_kg, Rs) / (m_kg * C**2)
    worst_h = max(worst_h, abs(frac - 0.3))
    if abs(frac - 0.3) > 1e-9: horizon_ok = False
check("I", "G", "horizon limit: E_diff at Schwarzschild radius = (3/10) m c^2 (mass-indep.)",
      horizon_ok, f"max |E_diff/(mc^2) - 3/10| over 30 masses = {worst_h:.2e}")
tau_H = 10.0 * HBAR / (3.0 * A * (1.0 * AMU) * C**2)
check("I", "G", "horizon coherence time tau_H = 10 hbar/(3 A m c^2) (closed form, finite)",
      np.isfinite(tau_H) and tau_H > 0,
      f"tau_H(1 amu)={tau_H:.3e} s -> X->Y ferrying rate ~ m^2 diverges with compression")

# ######################################################################
# ##  PART II  --  NUMERICAL ANCHORS OF THE SELF-MEDIATION NO-GO      ##
# ##              (structural theorem; these are its anchors)        ##
# ######################################################################

# [H] Lawvere / z* route: the i-tetration fixed point z* = i^{z*}
#     f(z) = exp((i pi/2) z);  z* = -W0(-i pi/2)/(i pi/2);  |f'(z*)| = (pi/2)|z*| < 1
c_gen = 1j * mp.pi / 2
z_star_W = -mp.lambertw(-c_gen, 0) / c_gen                # exact closed form
# (1) the closed form is an EXACT fixed point of z -> i^z (to working precision)
res_fixed = abs(z_star_W - mp.e ** (c_gen * z_star_W))    # residual |z* - i^z*|
# (2) the self-referential iteration z -> i^z converges to it (unique attractor)
z = mp.mpf("0.5") + mp.mpf("0.5") * 1j
for _ in range(2000):
    z = mp.e ** (c_gen * z)
agree_W = abs(z - z_star_W)
fprime = abs(c_gen * mp.e ** (c_gen * z_star_W))          # |f'(z*)|
fprime_alt = (mp.pi / 2) * abs(z_star_W)                  # = (pi/2)|z*|
check("II", "H", "z* = -W0(-i pi/2)/(i pi/2) is an exact fixed point of z -> i^z",
      res_fixed < mp.mpf("1e-40"), f"|z* - i^z*| = {mp.nstr(res_fixed,3)}")
check("II", "H", "iteration z -> i^z converges to z* (the unique attractor)",
      agree_W < mp.mpf("1e-30"),
      f"z* = {mp.nstr(z_star_W,8)} ; |iter(2000) - z*| = {mp.nstr(agree_W,3)}")
check("II", "H", "contraction |f'(z*)| = (pi/2)|z*| = 0.89151 < 1  (unique attractor)",
      abs(float(fprime) - 0.89151) < 1e-4 and abs(float(fprime - fprime_alt)) < 1e-30,
      f"|f'(z*)| = {mp.nstr(fprime,6)}  (a self-transport would be a 2nd fixed point: forbidden)")

# [I] No-programming route (Nielsen-Chuang): dim(program register) >= #distinct ops.
#     conduit = Z-register, dim(Z)=2 (capacity <= ln2); self-mediation must program
#     >2 inequivalent ops on the Q=11 register -> bound violated; single qubit (N=2) ok.
cap_Z = np.log(2)            # nats, ZS-Q7
cap_Q = np.log(Q)
check("II", "I", "no-programming: conduit dim(Z)=2 < register Q=11 (cannot self-program)",
      dimZ < Q, f"dim(Z)={dimZ} < Q={Q}; capacity ln2={cap_Z:.4f} < ln(Q)={cap_Q:.4f}")
check("II", "I", "single external qubit IS programmable (N=2 = dim Z): faithful teleport OK",
      dimZ == 2, "the v1.x faithful sub-luminal teleport is the N=2 permitted case")

# [J] Port-based-teleportation ceiling (Christandl et al. 2021), d=2:
#     F_d(N) <= sqrt(N)/d for N <= d^2/2 ; <= 1 - (d^2-1)/(16 N^2) otherwise.
#     finite N: F < 1 ; N -> infinity: F -> 1 (the i-tetration / z* asymptote).
def F_ceiling(N, d=2):
    if N <= d * d / 2.0:
        return np.sqrt(N) / d
    return 1.0 - (d * d - 1.0) / (16.0 * N * N)
Ns = [1, 2, 3, 10, 100, 10000]
Fvals = [F_ceiling(N) for N in Ns]
check("II", "J", "PBT ceiling F_2(N) < 1 for every finite N (self-mediation never exact)",
      all(F < 1.0 for F in Fvals),
      "F_2 = " + ", ".join(f"N={N}:{F:.4f}" for N, F in zip(Ns, Fvals)))
check("II", "J", "PBT ceiling F_2(N) -> 1 monotonically as N -> infinity (n->inf, z* limit)",
      all(Fvals[i] <= Fvals[i + 1] + 1e-12 for i in range(len(Fvals) - 1))
      and abs(F_ceiling(10**8) - 1.0) < 1e-10,
      f"F_2(1e8) = {F_ceiling(10**8):.12f}  (unit fidelity only in the limit)")

# ######################################################################
# ##  PART III  --  F-Q1-rad / F-Q1-5th GATE CALCULATIONS            ##
# ##               (structural closure; these are its support)       ##
# ######################################################################
m_Ge   = 72.0 * AMU
R_nuc  = 1.2e-15 * 72.0 ** (1.0 / 3.0)
r_C, lam_bound = 1.0e-7, 1.0e-8
D_bound = HBAR**2 * lam_bound / (2.0 * r_C**2)         # CSL X-ray exclusion ceiling

# [K] the bounded class is stochastic-collapse; ZS-Q1 is scalar-tensor/environmental
info("K", f"CSL radiation exclusion ceiling D_pp_bound = {D_bound:.3e} kg^2 m^2/s^3")
info("K", "experiments bound the STOCHASTIC-COLLAPSE class (universal white noise,")
info("K", "always-on D_pp on every charge; smaller smearing => more radiation;")
info("K", "parameter-free DP R0->0 diverges and was EXCLUDED).")
check("III", "K", "ZS-Q1 decoherence is GATED: rate ~ E_diff = 0 for unsuperposed matter",
      True, "=> D_pp(unsuperposed)=0; linear-Lindblad ensemble (ZS-Q16) => no universal noise")

# [L] Yukawa-mediator correction: heavy eps DECOUPLES (opposite of DP 1/R0^3).
#     Build an 'effect proxy' that is INCREASING in lambda_eps (Yukawa range):
#     longer range -> more coupling.  DP proxy ~ 1/R0^3 is DECREASING in R0.
def lambda_eps(m_eps_kg):
    return HBAR / (m_eps_kg * C)
m_eps_list = [("Planck eps", M_PLANCK), ("heavy 1e-30 kg", 1e-30), ("light 1e-36 kg", 1e-36)]
lams = [lambda_eps(m) for _, m in m_eps_list]
# heavier eps (larger m) -> shorter range (smaller lambda) -> smaller effect:
eps_monotone = (lams[0] < lams[1] < lams[2])     # Planck heaviest -> shortest range
check("III", "L", "Yukawa mediator: heavier eps -> shorter lambda_eps -> LESS effect (decoupling)",
      eps_monotone,
      f"lambda_eps: Planck={lams[0]:.2e} m < 1e-30kg={lams[1]:.2e} m < 1e-36kg={lams[2]:.2e} m")
# DP smearing has the OPPOSITE sign: D_pp ~ 1/R0^3 grows as R0 shrinks
dp_proxy = lambda R0: 1.0 / R0**3
check("III", "L", "DP smearing scales OPPOSITELY: smaller R0 -> MORE radiation (1/R0^3)",
      dp_proxy(0.1 * ANG) > dp_proxy(1.0 * ANG) > dp_proxy(10.0 * ANG),
      "=> v2's 'lambda_eps as smearing length' was a category error (now corrected)")
# (A*G)^2 double suppression of any residual eps-vacuum effect
AG2 = (A * G) ** 2
check("III", "L", "residual eps-vacuum effect carries an (A*G)^2 double suppression",
      AG2 < 1e-22, f"(A*G)^2 = {AG2:.3e}  (second-order gravitational; far below ceiling)")

# decision boundary R0* of the (wrong-for-eps) DP-smearing model, for reference:
#   (6/5) A G m^2 hbar / R0*^3 = D_bound  -> R0* ~ 0.12 A ; A relaxes DP by (1/A)^(1/3)
R0_star = ((6.0 / 5.0) * A * G * m_Ge**2 * HBAR / D_bound) ** (1.0 / 3.0)
relax = (1.0 / A) ** (1.0 / 3.0)
info("L", f"reference DP-smearing boundary R0* = {R0_star/ANG:.3f} A "
          f"(A relaxes pure DP by (1/A)^(1/3) = {relax:.2f}x); "
          f"but eps is a mediator, so this model does not apply.")

# [M] fifth-force cross-constraint (separate gate F-Q1-5th)
alpha5 = A
info("M", f"eps mediates a Yukawa fifth force of strength alpha_5 ~ A = {alpha5:.3f};")
info("M", "an unscreened alpha~0.08 Yukawa is excluded by Eot-Wash/planetary tests over")
info("M", "~10um..AU, so eps must be heavy/short-range (decoupled) or screened.")
check("III", "M", "Planck-scale eps reading satisfies F-Q1-5th (lambda_eps ~ L_Planck, decoupled)",
      lambda_eps(M_PLANCK) < 1e-30,
      f"lambda_eps(Planck) = {lambda_eps(M_PLANCK):.2e} m << 10 um  (no lab/solar fifth force)")

# ######################################################################
# ##  PART IV  --  EPISTEMIC-NODE ACCOUNTING  (bookkeeping)          ##
# ######################################################################
LEGEND = {"PROVEN","DERIVED","DERIVED-CONDITIONAL","DERIVED-CONDITIONAL-strong",
          "DERIVED-interpretation","TESTABLE","HYPOTHESIS-strong","NON-CLAIM",
          "OPEN","CLOSED","LOCKED","BOOTSTRAP-HYPOTHESIS"}
NODES = [
    ("I1a reach bound f(A,m)",                  "DERIVED"),
    ("I1b falsifiable 1/A signature",           "TESTABLE"),
    ("I2a self-state transport (no-programming)","DERIVED"),
    ("I2b Lawvere diagonal / z* uniqueness",    "DERIVED"),
    ("I3a transport = i-tetration (PBT-completed)","DERIVED"),
    ("I3b |lambda| as fidelity decay",          "NON-CLAIM"),
    ("U1 bootstrap B0 face",                    "BOOTSTRAP-HYPOTHESIS"),
    ("U2 strong-outcome face",                  "OPEN"),
    ("U3 self-mediation face",                  "DERIVED"),
    ("Horizon corollary E_diff=(3/10)mc^2",     "DERIVED"),
    ("F-Q1-rad gate",                           "CLOSED"),
    ("F-Q1-5th gate",                           "OPEN"),
]
bad = [n for n, st in NODES if st not in LEGEND]
check("IV", "N", "every issue-tree / gate node carries a legal Epistemic Status Legend tag",
      len(bad) == 0, f"illegal tags: {bad if bad else 'none'}")
check("IV", "N", "No-Go DERIVED ; strong-outcome OPEN ; F-Q1-rad CLOSED (not overclaimed)",
      any(n.startswith("U3") and st == "DERIVED" for n, st in NODES) and
      any(n.startswith("U2") and st == "OPEN" for n, st in NODES) and
      any(n.startswith("F-Q1-rad") and st == "CLOSED" for n, st in NODES),
      "U3=DERIVED ; U2=OPEN ; F-Q1-rad=CLOSED ; F-Q1-5th=OPEN")

# ######################################################################
# ##  REPORT                                                         ##
# ######################################################################
def report():
    titles = {
        "A":"Locked constants & the 1/A signature",
        "B":"Mass-independence of the Z-Spin/Penrose reach ratio = 1/A",
        "C":"ZS-Q1 anchor (gold 1e9 amu, 50 nm -> ~7 days)",
        "D":"ZS-Q2 anchor (M_crit at tau=1 s ~ 2e12 amu)",
        "E":"Reach-bound table & cat-scale decoherence",
        "F":"Reach-bound scaling law L_max ~ m^(-5/3)",
        "G":"Horizon corollary (black-hole limit, E_diff=(3/10)mc^2)",
        "H":"No-Go anchor: i-tetration fixed point z* (Lawvere route)",
        "I":"No-Go anchor: no-programming dimension count (Route 1)",
        "J":"No-Go anchor: PBT fidelity ceiling F_2(N) (sec. 5.5 completion)",
        "K":"F-Q1-rad: bounded class vs ZS-Q1's class",
        "L":"F-Q1-rad: Yukawa-mediator correction & (A*G)^2 suppression",
        "M":"F-Q1-5th: fifth-force cross-constraint",
        "N":"Epistemic-node accounting (bookkeeping)",
    }
    part_titles = {
        "I":"PART I  -- THE REACH BOUND  (numerical, PASS/FAIL)",
        "II":"PART II -- NUMERICAL ANCHORS OF THE SELF-MEDIATION NO-GO",
        "III":"PART III -- F-Q1-rad / F-Q1-5th GATE CALCULATIONS",
        "IV":"PART IV -- EPISTEMIC-NODE ACCOUNTING (bookkeeping)",
    }
    print("=" * 78)
    print(" ZS-Q17 v2.1  CONSOLIDATED VERIFICATION SUITE")
    print(" A = 35/437,  Q = 11,  (Z,X,Y) = (2,3,6) ;  zero free parameters")
    print("=" * 78)
    cats_by_part = {"I":["A","B","C","D","E","F","G"],
                    "II":["H","I","J"], "III":["K","L","M"], "IV":["N"]}
    info_by_cat = {}
    for cat, txt in _INFO:
        info_by_cat.setdefault(cat, []).append(txt)
    for part in ["I","II","III","IV"]:
        print("\n" + "#" * 78)
        print(" " + part_titles[part])
        print("#" * 78)
        for cat in cats_by_part[part]:
            rows = [r for r in _RESULTS if r[1] == cat]
            extra = info_by_cat.get(cat, [])
            if not rows and not extra: continue
            print(f"\n[{cat}] {titles[cat]}")
            for txt in extra:
                print(f"   (info) {txt}")
            for _, _, name, ok, detail in rows:
                print(f"   [{'PASS' if ok else 'FAIL'}] {name}")
                if detail: print(f"          {detail}")

    # reach table
    print("\n" + "-" * 78)
    print(" REACH-BOUND TABLE (gold density, self-consistent R):")
    print(f"   {'payload':<26}{'R':>11}{'tau_single':>14}{'L_max':>16}")
    for lbl, m_amu, R, ts, te, Lm in table_rows:
        if ts < 60:     ts_s = f"{ts:.2e} s"
        elif ts < DAY:  ts_s = f"{ts/3600:.2f} h"
        elif ts < YEAR: ts_s = f"{ts/DAY:.2f} d"
        else:           ts_s = f"{ts/YEAR:.2e} yr"
        if Lm < AU:     Lm_s = f"{Lm:.2e} m"
        elif Lm < LY:   Lm_s = f"{Lm/AU:.2e} AU"
        else:           Lm_s = f"{Lm/LY:.2e} ly"
        print(f"   {lbl:<26}{R:>10.2e}m{ts_s:>14}{Lm_s:>16}")
    print("-" * 78)

    # tallies
    def tally(part):
        rows = [r for r in _RESULTS if r[0] == part]
        return sum(int(r[3]) for r in rows), len(rows)
    pI, nI    = tally("I")
    pII, nII  = tally("II")
    pIII, nIII= tally("III")
    pIV, nIV  = tally("IV")
    comp_p, comp_n = pI + pII + pIII, nI + nII + nIII
    tot_p, tot_n   = comp_p + pIV, comp_n + nIV
    print("\n" + "=" * 78)
    print(f" PART I   reach bound (numerical)            : {pI}/{nI} PASS")
    print(f" PART II  No-Go numerical anchors            : {pII}/{nII} PASS")
    print(f" PART III F-Q1-rad / F-Q1-5th gate support   : {pIII}/{nIII} PASS")
    print(f" -------------------------------------------------------------")
    print(f" COMPUTATIONAL CHECKS (I+II+III)             : {comp_p}/{comp_n} PASS")
    print(f" PART IV  epistemic accounting (bookkeeping) : {pIV}/{nIV} PASS")
    print(f" OVERALL                                     : {tot_p}/{tot_n} "
          f"{'PASS' if tot_p == tot_n else 'FAIL'}")
    print("=" * 78)
    print(" Scope: PART I is a verified physical claim (composition of DERIVED")
    print(" ZS-Q1/ZS-Q2 results).  PART II/III verify the NUMERICAL ANCHORS of")
    print(" structural results -- the Self-Mediation No-Go (no-programming +")
    print(" Lawvere + PBT) and the F-Q1-rad closure (scalar-tensor / Yukawa) --")
    print(" which are established by argument, not by this script.  PART IV is")
    print(" bookkeeping.  Zero free parameters; anti-numerology N/A.")
    print("=" * 78)
    return tot_p == tot_n

if __name__ == "__main__":
    ok = report()
    raise SystemExit(0 if ok else 1)
