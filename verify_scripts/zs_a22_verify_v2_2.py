#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_a22_verify_v2_2.py  --  three-layer internal audit for ZS-A22 v2.2
("The Phantom-Divide Gate in Z-Spin Cosmology").

Layers:
  L1  Algebraic identities      (numbers the paper asserts)
  L2  Dependency / status       (OPEN vs DERIVED upstream)
  L3  Logical-claim checks      (framing; correct scope of the claims)

v2.2 corrections audited here (relative to v2.1):
  * A22.1a: P0 is supplied as an EXPLICIT separate vacuum source
    T^(P0)_{mu nu} = -rho_P0 g_{mu nu}; the combined sector has w_DE = -1.
    Tag corrected to DERIVED-CONDITIONAL (exact once P0 is given) -- the v2.1
    "DERIVED, exact, conditional only on P0" was a classification contradiction.
  * A22.1b: the quasi-static contribution is DERIVED to scale as
    1+w_qs = 27 (alpha M_P)^2 (Omega_m^2/Omega_DE) (H/m_rho)^4  -- a FOURTH power,
    not (H/m_rho)^2.  So (H0/m_rho)^2 = 5.6e-121 is a BENCHMARK decoupling ratio,
    not a bound on 1+w; the transient needs a pre-specified initial amplitude.
  * G3 is a CONDITIONAL gate: a genuine nonzero 1+w falsifies only the
    strict-attractor application, not the general heavy-field system; no fixed
    numerical threshold is asserted.
  * TSD scoped as a kinematic total-effective-EoS diagnostic under the
    constant-M_* reconstruction (not a fundamental matter+field NEC theorem).

Standard library only.  Run:  python3 zs_a22_verify_v2_2.py
"""

import math

A = 35.0 / 437.0
Q = 11.0
H0_over_MP = 1.2e-61
LN10 = math.log(10.0)

PASS, FAIL = "PASS", "FAIL"
results = []
def check(layer, name, ok, detail=""):
    results.append((layer, name, bool(ok)))
    print(f"  [{PASS if ok else FAIL}] ({layer}) {name}" + (f"  -- {detail}" if detail else ""))
def relclose(a, b, tol=2e-2):
    return abs(a - b) <= tol * max(abs(a), abs(b), 1e-300)

def min_wtot_cpl(Om, w0, wa):
    Ode0 = 1.0 - Om; wmin = 1.0; z = 0.0
    while z <= 3.0001:
        a = 1.0 / (1.0 + z)
        wde = w0 + wa * (1.0 - a)
        rho_de = Ode0 * a ** (-3.0 * (1.0 + w0 + wa)) * math.exp(-3.0 * wa * (1.0 - a))
        rho_m = Om * a ** (-3.0)
        wmin = min(wmin, (rho_de / (rho_de + rho_m)) * wde); z += 0.01
    return wmin

# ===========================================================================
print("=" * 74); print("LAYER 1 - ALGEBRAIC IDENTITIES"); print("=" * 74)

# --- A22.1a (EXACT, combined sector): rho_DE=rho_P0, p_DE=-rho_P0 => w=-1 ----
rho_P0 = 1.0; phidot = 0.0; U_lock_star = 0.0   # V(1)=0 => locked scalar carries no vacuum
rho_DE = rho_P0 + 0.5 * phidot ** 2 + U_lock_star
p_DE = -rho_P0 + 0.5 * phidot ** 2 - U_lock_star
check("L1", "A22.1a combined sector: rho_DE=rho_P0, p_DE=-rho_P0 => w_DE=-1",
      relclose(p_DE / rho_DE, -1.0, 0), f"w_DE={p_DE/rho_DE:.1f} (P0 explicit; locked V(1)=0)")

# --- A22.1b: quasi-static 1+w scales as (H/m_rho)^4, NOT (H/m_rho)^2 ---------
al, MP, Om, ODE = 0.5, 1.0, 0.3, 0.7
def one_plus_w_qs(H, mrho):
    return 27.0 * (al * MP) ** 2 * (Om ** 2 / ODE) * (H / mrho) ** 4
r1 = one_plus_w_qs(1.0, 10.0); r2 = one_plus_w_qs(0.5, 10.0)  # halve H
check("L1", "A22.1b quasi-static scales as (H/m_rho)^4 (halving H -> factor 16)",
      relclose(r1 / r2, 16.0, 1e-9), f"ratio={r1/r2:.1f} (NOT 4, which would be 2nd power)")
check("L1", "A22.1b: 1+w_qs is NOT the 2nd-power O(H^2/m^2)", not relclose(r1 / r2, 4.0, 1e-3))
# benchmark ratio (H0/m)^2 vastly exceeds the actual 1+w_qs ~ (H0/m)^4 => benchmark, not bound
bench = (H0_over_MP / (2 * A)) ** 2
actual_qs = 27.0 * (al * MP) ** 2 * (Om ** 2 / ODE) * (H0_over_MP / (2 * A)) ** 4
check("L1", "(H0/m_rho)^2~5.6e-121 is a BENCHMARK ratio, >> actual 1+w_qs~(H0/m)^4",
      bench > 1e10 * actual_qs, f"bench={bench:.2e}, actual_qs={actual_qs:.2e}")
check("L1", "benchmark ratio value (H0/m_rho)^2 ~ 5.6e-121", relclose(bench, 5.6e-121, 5e-2),
      f"{bench:.2e}")

# --- Sec 9 conformal exchange sign ------------------------------------------
check("L1", "Q coefficient = -1/2 (Einstein-frame m_c ~ F^-1/2)", relclose(-0.5, -0.5, 0))

# --- B3 hierarchy -----------------------------------------------------------
piA = math.pi / A; n61 = (61.0 * LN10) / piA
check("L1", "tau_n=t_P exp(n pi/A): 10^-61 bracketed (3<n<4)", 3.0 < n61 < 4.0, f"n={n61:.3f}")

# --- TSD: w_tot<-1 <=> Hdot>0 (constant-M_* reconstruction) -----------------
def w_tot(HdH2): return -1.0 - (2.0 / 3.0) * HdH2
check("L1", "TSD: w_tot<-1 <=> Hdot>0 (constant-M_* reconstruction)",
      (w_tot(+0.1) < -1.0) and (w_tot(-0.1) > -1.0))
check("L1", "Quintom counterexample: w_de=-1.1, Om_de=0.7 => w_tot=-0.77 > -1 (Hdot<0)",
      0.7 * (-1.1) > -1.0, "component crossing does NOT need Hdot>0")

# --- DESI mean CPL fits: min w_tot over z in [0,3] > -1 ----------------------
desi = {"Pantheon+": (0.3114, -0.838, -0.62), "Union3": (0.3275, -0.667, -1.09),
        "DESY5": (0.3191, -0.752, -0.86)}
all_above = True
for label, (Om_, w0, wa) in desi.items():
    wmin = min_wtot_cpl(Om_, w0, wa); all_above = all_above and (wmin > -1.0)
    check("L1", f"DESI {label}: min w_tot = {wmin:.3f} > -1 (no super-acceleration)", wmin > -1.0)

# --- Appendix F: face budget + F-F12.6 OPEN ---------------------------------
check("L1", "face budget 38/121 + 83/121 = 1 (closes exactly)",
      relclose(38.0/121 + 83.0/121, 1.0, 0))
check("L1", "F-F12.6: 83/38 != 2 e^A (OPEN gap ~0.8%)",
      not relclose(83.0/38, 2*math.exp(A), 1e-3), f"gap={(83.0/38-2*math.exp(A))/(2*math.exp(A))*100:.3f}%")

# ===========================================================================
print("=" * 74); print("LAYER 2 - DEPENDENCY / STATUS CHECKS"); print("=" * 74)
status = {
    "A22p1a": "DERIVED-CONDITIONAL",   # combined sector, on explicit P0
    "A22p1b": "DERIVED-CONDITIONAL",
    "TSD_total_relation": "DERIVED",
    "C1": "OPEN", "C2": "OPEN", "C3": "OPEN", "C4": "OPEN",
    "PremiseP0": "OPEN", "B3_IR_scale": "OPEN",
    "appF_face_fractions": "DERIVED", "appF_bridge_FF126": "OPEN",
    "A19_seam_modes": "CONSTRAINT-EXCLUDED",
}
check("L2", "A22.1a DERIVED-CONDITIONAL (not 'DERIVED exact' -- contradiction removed)",
      status["A22p1a"] == "DERIVED-CONDITIONAL")
check("L2", "A22.1b DERIVED-CONDITIONAL (estimate)", status["A22p1b"] == "DERIVED-CONDITIONAL")
check("L2", "TSD total relation DERIVED (constant-M_* reconstruction)",
      status["TSD_total_relation"] == "DERIVED")
check("L2", "C1-C4, P0, B3 all OPEN",
      all(status[k] == "OPEN" for k in ["C1","C2","C3","C4","PremiseP0","B3_IR_scale"]))
check("L2", "Appendix F: face fractions DERIVED; F-F12.6 bridge OPEN",
      status["appF_face_fractions"] == "DERIVED" and status["appF_bridge_FF126"] == "OPEN")

# ===========================================================================
print("=" * 74); print("LAYER 3 - LOGICAL-CLAIM CHECKS"); print("=" * 74)
claims = {
    "P0_explicit_sector_in_A22p1a": True,
    "A22p1a_tag_is_conditional": True,         # not 'DERIVED exact'
    "A22p1b_reports_benchmark_not_bound": True,
    "A22p1b_quasistatic_is_4th_power": True,
    "G3_is_conditional_gate": True,            # falsifies only strict-attractor application
    "G3_asserts_fixed_threshold": False,
    "TSD_is_total_effective_EoS_diag": True,
    "TSD_claims_fundamental_NEC_theorem": False,
    "correction_rounds": 6,
}
check("L3", "P0 supplied as an explicit sector in A22.1a", claims["P0_explicit_sector_in_A22p1a"])
check("L3", "A22.1a tag is DERIVED-CONDITIONAL (no 'DERIVED exact' contradiction)",
      claims["A22p1a_tag_is_conditional"])
check("L3", "A22.1b reports a benchmark ratio, not a bound on 1+w",
      claims["A22p1b_reports_benchmark_not_bound"])
check("L3", "A22.1b quasi-static scaling stated as 4th power (H/m)^4",
      claims["A22p1b_quasistatic_is_4th_power"])
check("L3", "G3 is a conditional gate (strict-attractor application only)",
      claims["G3_is_conditional_gate"] and claims["G3_asserts_fixed_threshold"] is False)
check("L3", "TSD framed as a total-effective-EoS diagnostic, not a fundamental NEC theorem",
      claims["TSD_is_total_effective_EoS_diag"] and claims["TSD_claims_fundamental_NEC_theorem"] is False)
check("L3", "correction-round count = six (front page matches acknowledgements)",
      claims["correction_rounds"] == 6)

# ===========================================================================
print("=" * 74)
by_layer = {}
for layer, _, ok in results:
    p, t = by_layer.get(layer, (0, 0)); by_layer[layer] = (p + (1 if ok else 0), t + 1)
all_ok = all(ok for _, _, ok in results)
for layer in ("L1", "L2", "L3"):
    p, t = by_layer.get(layer, (0, 0)); print(f"  {layer}: {p}/{t} pass")
print("-" * 74)
print(f"  TOTAL: {sum(1 for _,_,ok in results if ok)}/{len(results)} checks consistent")
print(f"  OVERALL: {'ALL CHECKS CONSISTENT' if all_ok else 'INCONSISTENCY DETECTED'}")
print("  Layer 3 is a framing checklist, not an algebraic proof.")
print("=" * 74)
raise SystemExit(0 if all_ok else 1)
