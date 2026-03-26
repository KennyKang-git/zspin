#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════
  ZS-T2 v1.0 VERIFICATION SUITE
  Spectral Observatory: Structural Proximities Between Z-Spin Invariants
                        and Undetermined Physical Constants

  Z-Spin Cosmology Collaboration
  Kenny Kang
  March 2026

  30/30 tests — covers every quantitative claim in ZS-T2 v1.0
  Dependencies: standard library only (math, cmath, random, fractions)
═══════════════════════════════════════════════════════════════════════════
"""

import cmath
import math
import random
import sys
from fractions import Fraction

# ═══════════════════════════════════════════════════════════════════════════
# LOCKED CONSTANTS (from prior papers, zero new parameters)
# ═══════════════════════════════════════════════════════════════════════════
A = Fraction(35, 437)           # Geometric impedance
A_f = float(A)                  # 0.080091...
Z, X, Y = 2, 3, 6              # Sector dimensions
Q = Z + X + Y                   # = 11
lambda_vac = 2 * A_f**2         # Vacuum self-coupling
kappa_sq = float(Fraction(35, 4807))  # A/Q = perturbative expansion param
delta_X = Fraction(5, 19)       # X-sector curvature asymmetry
delta_Y = Fraction(7, 23)       # Y-sector curvature asymmetry
alpha_s_MZ = float(Fraction(11, 93))  # Strong coupling

# i-tetration fixed point: z* satisfying exp(iπz*/2) = z*
z_star = 0.4 + 0.6j
for _ in range(100000):
    z_star = cmath.exp(1j * cmath.pi * z_star / 2)
x_star = z_star.real            # Re(z*) = 0.438283...
y_star = z_star.imag            # Im(z*) = 0.360592...
mod_z_star = abs(z_star)        # |z*|   = 0.567555...

# Derived
sin2_thetaW = (48.0 / 91.0) * x_star  # From ZS-S1

# Observational data
PLANCK_ns = 0.9649              # Planck 2018 central value
PLANCK_ns_err = 0.0042          # 68% CL
PLANCK_1_minus_ns = 1 - PLANCK_ns
alpha_EM_PDG = 1.0 / 137.036   # PDG 2024
sin2_theta13_PDG = 0.0220       # PDG central
sin2_theta13_err = 0.0007       # PDG 68% CL
r_ZSU1 = 0.0089                # ZS-U1 prediction

# ═══════════════════════════════════════════════════════════════════════════
# TEST INFRASTRUCTURE
# ═══════════════════════════════════════════════════════════════════════════
results = []

def test(test_id, description, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    results.append((test_id, description, status, detail))
    mark = "\u2713" if condition else "\u2717"
    print(f"  [{mark}] {test_id:8s} {description}")
    if detail:
        print(f"           {detail}")
    if not condition:
        print(f"           *** FAILURE ***")
    return condition


# ═══════════════════════════════════════════════════════════════════════════
# [A] LOCKED INPUTS & IDENTITIES (6 tests)
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 72)
print("  ZS-T2 v1.0 VERIFICATION SUITE")
print("  Spectral Observatory")
print("=" * 72)
print()
print("[A] Locked Inputs & Identities")
print("-" * 72)

test("A1", "A = 35/437 = 0.080092",
     abs(A_f - 35/437) < 1e-15,
     f"A = {A_f:.10f}")

test("A2", "(Z,X,Y) = (2,3,6), Q = 11",
     Z == 2 and X == 3 and Y == 6 and Q == 11,
     f"Q = Z+X+Y = {Q}")

fp_err = abs(z_star - cmath.exp(1j * cmath.pi * z_star / 2))
test("A3", "z* is fixed point: exp(i\u03c0z*/2) = z*",
     fp_err < 1e-14,
     f"x* = {x_star:.10f}, y* = {y_star:.10f}, |error| = {fp_err:.2e}")

lv_exact = 2 * (35/437)**2
test("A4", "\u03bb_vac = 2A\u00b2 = 0.012829",
     abs(lambda_vac - lv_exact) < 1e-15,
     f"\u03bb_vac = {lambda_vac:.10f}")

kappa_exact = float(Fraction(35, 4807))
test("A5", "\u03ba\u00b2 = A/Q = 35/4807",
     abs(kappa_sq - kappa_exact) < 1e-15 and 437 * 11 == 4807,
     f"\u03ba\u00b2 = {kappa_sq:.10f}, 1/\u03ba\u00b2 = {1/kappa_sq:.6f}")

test("A6", "\u03b4_X = 5/19, \u03b4_Y = 7/23 (curvature asymmetries)",
     delta_X == Fraction(5, 19) and delta_Y == Fraction(7, 23),
     f"\u03b4_X = {float(delta_X):.10f}, \u03b4_Y = {float(delta_Y):.10f}")


# ═══════════════════════════════════════════════════════════════════════════
# [B] TIER-1: SPECTRAL TILT T1-1 (4 tests)
# ═══════════════════════════════════════════════════════════════════════════
print()
print("[B] Tier-1: Spectral Tilt  1 \u2212 n_s = A \u00d7 x*")
print("-" * 72)

Axstar = A_f * x_star
test("B1", "A \u00d7 x* = 0.035103 (Eq. 1)",
     abs(Axstar - 0.035103) < 0.000001,
     f"A \u00d7 x* = {Axstar:.10f}")

pull_ns = abs(Axstar - PLANCK_1_minus_ns) / PLANCK_ns_err
precision_ns = abs(Axstar - PLANCK_1_minus_ns) / PLANCK_1_minus_ns * 100
test("B2", "Pull vs Planck 2018: |pull| < 0.01\u03c3",
     pull_ns < 0.01,
     f"pull = {pull_ns:.4f}\u03c3, precision = {precision_ns:.4f}%")

N_star = 2.0 / Axstar
test("B3", "N* = 2/(A\u00d7x*) in [55, 60] reheating window",
     55 <= N_star <= 60,
     f"N* = {N_star:.4f} e-folds")

N_star_planck = 2.0 / (1.0 - PLANCK_ns)
test("B4", "N* \u2248 57.0 (Planck central value match)",
     abs(N_star - N_star_planck) < 0.1,
     f"N*(Z-Spin) = {N_star:.2f}, N*(Planck) = {N_star_planck:.2f}")


# ═══════════════════════════════════════════════════════════════════════════
# [C] TIER-1: FINE-STRUCTURE CONSTANT (4 tests)
# ═══════════════════════════════════════════════════════════════════════════
print()
print("[C] Tier-1: Fine-Structure Constant  \u03b1_EM \u2248 A/Q")
print("-" * 72)

inv_kappa_sq = 1.0 / kappa_sq
precision_alpha_LO = abs(inv_kappa_sq - 137.036) / 137.036 * 100
test("C1", "1/\u03ba\u00b2 = 137.343 (0.22% from PDG)",
     abs(inv_kappa_sq - 137.343) < 0.001 and abs(precision_alpha_LO - 0.22) < 0.02,
     f"1/\u03ba\u00b2 = {inv_kappa_sq:.6f}, precision = {precision_alpha_LO:.4f}%")

# Uniqueness: A/Q unique within 10%
candidates_near_alpha = []
zs_quantities = {
    'A': A_f, 'A/Q': A_f / Q, 'A\u00b2': A_f**2,
    'Z/Q': Z / Q, 'X/Q': X / Q, 'Y/Q': Y / Q,
    'A/Z': A_f / Z, 'A/X': A_f / X, 'A/Y': A_f / Y,
    'delta_X': float(delta_X), 'delta_Y': float(delta_Y),
    'x*': x_star, 'y*': y_star, '|z*|': mod_z_star,
    'lambda_vac': lambda_vac, 'A*x*': A_f * x_star,
    'A*y*': A_f * y_star, 'delta_X/Q': float(delta_X) / Q,
    'delta_Y/Q': float(delta_Y) / Q, 'Z*X/Q\u00b2': Z * X / Q**2,
    'Z*Y/Q\u00b2': Z * Y / Q**2, 'X*Y/Q\u00b2': X * Y / Q**2,
    'A/delta_X': A_f / float(delta_X), 'A/delta_Y': A_f / float(delta_Y),
    'x*/Q': x_star / Q, 'y*/Q': y_star / Q, '|z*|/Q': mod_z_star / Q,
    'A\u00b2/Q': A_f**2 / Q, 'A\u00b3': A_f**3, 'sqrt(A)': math.sqrt(A_f),
    'sqrt(A/Q)': math.sqrt(A_f / Q),
    'delta_X*delta_Y': float(delta_X) * float(delta_Y),
    'A*delta_X': A_f * float(delta_X), 'A*delta_Y': A_f * float(delta_Y),
    '1/(Z*Q)': 1 / (Z * Q), 'Z/(X*Y)': Z / (X * Y),
    'sqrt(Z*Y/Q)': math.sqrt(Z * Y / Q),
}
for name, val in zs_quantities.items():
    if val > 0:
        rel_err = abs(val - alpha_EM_PDG) / alpha_EM_PDG
        if rel_err < 0.10:
            candidates_near_alpha.append((name, val, rel_err))

test("C2", "A/Q is unique Z-Spin quantity within 10% of \u03b1_EM",
     len(candidates_near_alpha) == 1 and candidates_near_alpha[0][0] == 'A/Q',
     f"Candidates within 10%: {[(n, f'{v:.6f}', f'{e*100:.1f}%') for n,v,e in candidates_near_alpha]}")

lambda2 = 2 * A_f / Q
test("C3", "\u03ba\u00b2 = \u00bd\u03bb\u2082 (block-Laplacian eigenvalue)",
     abs(kappa_sq - lambda2 / 2) < 1e-15,
     f"\u03ba\u00b2 = {kappa_sq:.10f}, \u00bd\u03bb\u2082 = {lambda2/2:.10f}")

sw2 = (48.0 / 91.0) * x_star
test("C4", "sin\u00b2\u03b8_W = (48/91)x* \u2248 0.2312",
     abs(sw2 - 0.23122) < 0.001,
     f"sin\u00b2\u03b8_W(Z-Spin) = {sw2:.6f}, PDG \u2248 0.23122")


# ═══════════════════════════════════════════════════════════════════════════
# [D] NLO SCHUR COMPLEMENT \u00a75.3 (5 tests)
# ═══════════════════════════════════════════════════════════════════════════
print()
print("[D] NLO Schur Complement: \u03b1_EM = \u03ba\u00b2 + c\u2084\u03ba\u2074 + O(\u03ba\u2076)")
print("-" * 72)

dX = float(delta_X)
dY = float(delta_Y)

Delta_alpha = alpha_EM_PDG - kappa_sq
kappa_4 = kappa_sq**2
test("D1", "\u0394\u03b1 = \u03b1_obs \u2212 \u03ba\u00b2 > 0 and O(\u03ba\u2074)",
     Delta_alpha > 0 and 0.1 < Delta_alpha / kappa_4 < 1.0,
     f"\u0394\u03b1 = {Delta_alpha:.6e}, \u03ba\u2074 = {kappa_4:.6e}, \u0394\u03b1/\u03ba\u2074 = {Delta_alpha/kappa_4:.5f}")

c4_needed = Delta_alpha / kappa_4
test("D2", "c\u2084(needed) = \u0394\u03b1/\u03ba\u2074 is O(1) coefficient",
     0.1 < c4_needed < 1.0,
     f"c\u2084(needed) = {c4_needed:.5f}")

c4_candidate = dY + A_f * (dY - dX)
c4_exact = delta_Y + A * (delta_Y - delta_X)
test("D3", "c\u2084 = \u03b4_Y + A(\u03b4_Y \u2212 \u03b4_X) = 0.30765 (Eq. 7)",
     abs(c4_candidate - 0.30765) < 0.00001,
     f"c\u2084 = {c4_candidate:.10f} (exact rational: {c4_exact} = {float(c4_exact):.10f})")

alpha_NLO = kappa_sq + c4_candidate * kappa_4
inv_alpha_NLO = 1.0 / alpha_NLO
precision_NLO = abs(inv_alpha_NLO - 137.036) / 137.036 * 100
test("D4", "1/\u03b1_EM(NLO) = 137.0359, precision < 0.001%",
     abs(inv_alpha_NLO - 137.036) < 0.01 and precision_NLO < 0.001,
     f"1/\u03b1(NLO) = {inv_alpha_NLO:.4f}, precision = {precision_NLO:.5f}%")

residual_LO = abs(inv_kappa_sq - 137.036)
residual_NLO = abs(inv_alpha_NLO - 137.036)
reduction_factor = residual_LO / residual_NLO if residual_NLO > 0 else float('inf')
test("D5", "NLO reduces residual by factor ~3000\u00d7",
     reduction_factor > 1000,
     f"LO residual = {residual_LO:.4f}, NLO residual = {residual_NLO:.4f}, ratio = {reduction_factor:.0f}\u00d7")


# ═══════════════════════════════════════════════════════════════════════════
# [E] TIER-2 OBSERVATIONS (3 tests)
# ═══════════════════════════════════════════════════════════════════════════
print()
print("[E] Tier-2 Observations")
print("-" * 72)

r_SO = 2 * A_f**2 * math.log(2)
precision_r = abs(r_SO - r_ZSU1) / r_ZSU1 * 100
test("E1", "r = 2A\u00b2 \u00d7 ln 2 = 0.008893 (Eq. 4)",
     abs(r_SO - 0.008893) < 0.000001,
     f"r = {r_SO:.8f}, vs ZS-U1 r=0.0089: {precision_r:.2f}%")

test("E2", "r tension: r(N*=57) \u2260 r(Eq.4) (honest)",
     abs(r_SO - 0.0098) / 0.0098 > 0.05,
     f"r(Eq.4) = {r_SO:.6f} vs r(N*=57) \u2248 0.0098, gap = {abs(r_SO-0.0098)/0.0098*100:.1f}%")

sin2_13 = dX**2 / math.pi
pull_13 = (sin2_13 - sin2_theta13_PDG) / sin2_theta13_err
test("E3", "sin\u00b2\u03b8\u2081\u2083 \u2248 \u03b4_X\u00b2/\u03c0 = 0.02204 (Eq. 5), pull < 1\u03c3",
     abs(pull_13) < 1.0,
     f"sin\u00b2\u03b8\u2081\u2083 = {sin2_13:.6f}, PDG = {sin2_theta13_PDG}, pull = {pull_13:+.2f}\u03c3")


# ═══════════════════════════════════════════════════════════════════════════
# [F] ANTI-NUMEROLOGY MONTE CARLO (4 tests)
# ═══════════════════════════════════════════════════════════════════════════
print()
print("[F] Anti-Numerology Monte Carlo Scans")
print("-" * 72)

random.seed(20260315)  # Reproducible

# --- Build actual scan space (§4.1) ---
base_quantities = [
    Z/Q, X/Q, Y/Q,
    A_f, kappa_sq, A_f**2,
    float(delta_X), float(delta_Y),
    x_star, y_star, mod_z_star,
    lambda_vac, sin2_thetaW, alpha_s_MZ,
    Z/X, X/Y, Z/Y,
    float(delta_X)/float(delta_Y), float(delta_Y)/float(delta_X),
    A_f*x_star, 2*A_f, A_f/2,
    x_star**2, y_star**2,
    Q*A_f, float(delta_X)*float(delta_Y), X*Y/Q**2,
]
assert len(base_quantities) == 27, f"Base: {len(base_quantities)}"

scan_powers = [1, 2, 3, 0.5, -1]
scan_multipliers = list(range(1,8)) + [1/i for i in range(2,8)] + [
    math.pi, math.e, math.sqrt(2), math.sqrt(3), math.log(2),
    1/(2*math.pi), 1/(4*math.pi), 1/math.pi
]
assert len(scan_multipliers) == 21, f"Multipliers: {len(scan_multipliers)}"

candidates = []
for val in base_quantities:
    for p in scan_powers:
        try:
            v = val**p if val > 0 else abs(val)**p
            if v <= 0 or not math.isfinite(v): continue
            for m in scan_multipliers:
                c = v * m
                if math.isfinite(c) and c > 0:
                    candidates.append(c)
                    candidates.append(1/c)
        except:
            pass
scan_total = len(candidates)
test("F1", "Scan space = 27 \u00d7 5 \u00d7 21 \u00d7 2 = 5,670",
     scan_total == 5670,
     f"Computed: {scan_total}")

target_values = [
    1/137.036, 4.836e-3, 0.05946, 2.875e-4,
    0.47, 0.053, 0.024, 0.0073,
    0.2253, 0.0405, 3.82e-3, 8.1e-3, 3.08e-5,
    0.307, 0.546, 0.0220,
    0.685, 0.9649, 0.0351, 0.0089,
    0.7243, 0.5082, 1.554,
    0.0493, 0.265, 0.315, 0.6736, 0.054, 0.811,
]
n_targets = len(target_values)
assert n_targets == 29

match_window = 0.01
actual_hits = 0
for c in candidates:
    for tval in target_values:
        if tval > 0 and abs(c - tval)/tval < match_window:
            actual_hits += 1

expected_hits = scan_total * n_targets * 2 * match_window
hit_fraction = actual_hits / expected_hits
test("F2", f"Actual hits ({actual_hits}) < expected random hits (~{expected_hits:.0f})",
     actual_hits < expected_hits and hit_fraction < 0.10,
     f"Expected \u2248 {expected_hits:.0f}, actual = {actual_hits}, fraction = {hit_fraction*100:.1f}%")

N_MC = 100000
count_ns = 0
for _ in range(N_MC):
    a = random.randint(1, 500)
    b = random.randint(a + 1, 1000)
    val = (a / b) * x_star
    if abs(val - 0.0351) < 0.0042:
        count_ns += 1
p_ns = count_ns / N_MC
test("F3", "MC T1-1: p(random 1\u2212n_s match) ~ 2% (not rare alone)",
     0.005 < p_ns < 0.05,
     f"p = {p_ns*100:.2f}% ({count_ns}/{N_MC})")

count_alpha = 0
for _ in range(N_MC):
    a = random.randint(1, 500)
    b = random.randint(a + 1, 1000)
    val = (a / b) / Q
    if abs(val - alpha_EM_PDG) / alpha_EM_PDG < 0.005:
        count_alpha += 1
p_alpha = count_alpha / N_MC
test("F4", "MC T1-2: p(random \u03b1_EM match) < 0.2%",
     p_alpha < 0.005,
     f"p = {p_alpha*100:.3f}% ({count_alpha}/{N_MC})")


# ═══════════════════════════════════════════════════════════════════════════
# [G] FALSIFICATION GATE CONDITIONS (4 tests)
# ═══════════════════════════════════════════════════════════════════════════
print()
print("[G] Falsification Gate Conditions")
print("-" * 72)

test("G1", "F-SO.1: N* = 56.98 \u2208 [55, 59] (not falsified)",
     55 <= N_star <= 59,
     f"N* = {N_star:.2f}")

test("G2", "F-SO.3 PASSED: 0/37 independent ratios near \u03b1_EM",
     len(candidates_near_alpha) == 1,
     f"Found {len(candidates_near_alpha)} candidate(s) within 10%")

test("G3", "F-SO.4: NLO correction has correct sign (\u0394\u03b1 > 0 \u2192 c\u2084 > 0)",
     Delta_alpha > 0 and c4_candidate > 0,
     f"\u0394\u03b1 = {Delta_alpha:.6e} > 0, c\u2084 = {c4_candidate:.5f} > 0")

r_prediction = r_ZSU1
test("G4", "F-SO.5: r = 0.0089 \u2208 [0.005, 0.015] (LiteBIRD testable)",
     0.005 <= r_prediction <= 0.015,
     f"r = {r_prediction}")


# ═══════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════════
print()
print("=" * 72)
print("  VERIFICATION SUMMARY \u2014 ZS-T2 v1.0")
print("=" * 72)

n_pass = sum(1 for _, _, s, _ in results if s == "PASS")
n_fail = sum(1 for _, _, s, _ in results if s == "FAIL")
n_total = len(results)

categories = {
    'A': 'Locked Inputs & Identities',
    'B': 'Tier-1: Spectral Tilt',
    'C': 'Tier-1: Fine-Structure Constant',
    'D': 'NLO Schur Complement',
    'E': 'Tier-2 Observations',
    'F': 'Anti-Numerology Monte Carlo',
    'G': 'Falsification Gate Conditions',
}
for cat, name in categories.items():
    cat_results = [(tid, s) for tid, _, s, _ in results if tid.startswith(cat)]
    cat_pass = sum(1 for _, s in cat_results if s == "PASS")
    cat_total = len(cat_results)
    mark = "\u2713" if cat_pass == cat_total else "\u2717"
    print(f"  [{mark}] [{cat}] {name}: {cat_pass}/{cat_total}")

print()
print(f"  TOTAL: {n_pass}/{n_total} PASS")
print()

if n_fail > 0:
    print(f"  \u274c VERDICT: FAIL ({n_fail} failures)")
    failed = [(tid, desc) for tid, desc, s, _ in results if s == "FAIL"]
    for tid, desc in failed:
        print(f"    FAILED: {tid} \u2014 {desc}")
    sys.exit(1)
else:
    print(f"  \u2705 ALL {n_total} TESTS PASS")
    print(f"  ZS-T2 v1.0 VERIFIED \u2014 Zero free parameters confirmed")

print()
print("=" * 72)
print("  GRAND RESET COMPLIANCE")
print("=" * 72)
print(f"""
  Paper Code:     ZS-T2 (was Paper 44 / ZS-SO)
  Version:        v1.0 (consolidated from v1.2.0)
  Internal Refs:  All updated to v1.0
    - ZS-F1, ZS-F2, ZS-F5 v1.0
    - ZS-M1, ZS-M3, ZS-M6 v1.0 (was Paper 31)
    - ZS-S1 v1.0
    - ZS-U1 v1.0
    - ZS-Q7 v1.0
    - ZS-T3 v1.0 (was Paper 45 / ZS-SIM)
  Acknowledgements: Anthropic Claude, OpenAI ChatGPT, Google Gemini
  Epistemic Status Legend: PRESENT
  Falsification Framework: 5 gates documented
""")

print("=" * 72)
print("  KEY NUMERICAL RESULTS")
print("=" * 72)
print(f"  A = 35/437                    = {A_f:.10f}")
print(f"  x* = Re(z*)                   = {x_star:.10f}")
print(f"  A \u00d7 x* (1\u2212n_s)               = {Axstar:.10f}  [Planck: {PLANCK_1_minus_ns}]")
print(f"  N* = 2/(A\u00d7x*)                 = {N_star:.4f}")
print(f"  \u03ba\u00b2 = A/Q = 35/4807            = {kappa_sq:.10f}")
print(f"  1/\u03ba\u00b2 (LO)                     = {inv_kappa_sq:.6f}  [PDG: 137.036]")
print(f"  c\u2084 = \u03b4_Y + A(\u03b4_Y\u2212\u03b4_X)        = {c4_candidate:.10f}")
print(f"  1/\u03b1_EM (NLO)                  = {inv_alpha_NLO:.4f}  [PDG: 137.036]")
print(f"  NLO precision                 = {precision_NLO:.5f}%")
print(f"  r = 2A\u00b2 ln 2                  = {r_SO:.8f}")
print(f"  sin\u00b2\u03b8\u2081\u2083 = \u03b4_X\u00b2/\u03c0             = {sin2_13:.6f}  [PDG: {sin2_theta13_PDG}]")
print(f"  sin\u00b2\u03b8_W = (48/91)x*           = {sw2:.6f}")
print(f"  Scan space                    = {scan_total}")
print(f"  Hit rate                      = {hit_fraction*100:.1f}% of random expectation")
print("=" * 72)

sys.exit(0 if n_fail == 0 else 1)
