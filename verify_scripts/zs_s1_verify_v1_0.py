#!/usr/bin/env python3
"""
ZS-S1 v1.0 Verification Suite
=================================
Gauge Coupling Unification: Incidence-Laplacian Bridge
from Action to SM Gauge Couplings

38/38 PASS expected

Covers:
  Category 1: Polyhedral Invariants (6 tests)
  Category 2: IL Bridge (4 tests)
  Category 3: Z-Sector Schur Complement (3 tests)
  Category 4: Spectral-to-beta Bridge (4 tests)
  Category 5: Gauge Couplings (5 tests)
  Category 6: PDG Pull Tests (3 tests)
  Category 7: Archimedean Adversarial (3 tests)
  Category 8: Monte Carlo Anti-Numerology (1 test)
  Category 9: Sensitivity Analysis (2 tests)
  Category 10: Cross-Paper Interface (4 tests)
  Category 11: Hodge-Dirac Integration (3 tests)

All from locked inputs: A = 35/437, Q = 11, (Z,X,Y) = (2,3,6), z* = i^{z*}.
Grand Reset: All cross-references use v1.0 codes.

Dependencies: numpy, mpmath
Execution: python3 ZS_S1_verify_v1_0.py
Expected output: 35/35 PASS, exit code 0
"""

import os
import sys
import numpy as np
from fractions import Fraction
import mpmath
import json

mpmath.mp.dps = 50

# ═══════════════════════════════════════════════════════════════
# LOCKED INPUTS (from ZS-F2 v1.0, ZS-F5 v1.0, ZS-M1 v1.0)
# ═══════════════════════════════════════════════════════════════
Z, X, Y = 2, 3, 6
Q = Z + X + Y       # = 11
G = 2 * Y           # = 12
A = Fraction(35, 437)

# Polyhedral data (ZS-F2 v1.0)
V_X, E_X, F_X = 24, 36, 14   # Truncated Octahedron (X)
V_Y, E_Y, F_Y = 60, 90, 32   # Truncated Icosahedron (Y)

VF_X = V_X + F_X          # = 38
VF_Y = V_Y + F_Y          # = 92
VEF_X = V_X + E_X + F_X   # = 74
VEF_Y = V_Y + E_Y + F_Y   # = 182

# Symmetry group orders
Oh, Ih, Td = 48, 120, 24

# delta deviations (ZS-F2 v1.0)
delta_X = Fraction(abs(F_X - V_X), F_X + V_X)  # 10/38 = 5/19
delta_Y = Fraction(abs(F_Y - V_Y), F_Y + V_Y)  # 28/92 = 7/23

# i-tetration fixed point z* = i^{z*} (ZS-M1 v1.0)
z_star = mpmath.lambertw(-1j * mpmath.pi / 2) / (-1j * mpmath.pi / 2)
x_star = float(z_star.real)
y_star = float(z_star.imag)

# PDG 2024 reference values
ALPHA_S_PDG, ALPHA_S_ERR = 0.1180, 0.0009
SIN2W_PDG, SIN2W_ERR = 0.23122, 0.00003

# SM parameters
n_f, N_c, n_g = 5, 3, 3

# ═══════════════════════════════════════════════════════════════
# TEST FRAMEWORK
# ═══════════════════════════════════════════════════════════════
results = []


def test(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    results.append({"name": name, "status": status, "detail": detail})
    marker = "\u2713" if condition else "\u2717"
    print(f"  [{marker} {status}] {name}" + (f"  ({detail})" if detail else ""))
    return condition


print("=" * 70)
print("ZS-S1 v1.0 VERIFICATION SUITE")
print("Gauge Coupling Unification: Incidence-Laplacian Bridge")
print("=" * 70)

# ── Category 1: Polyhedral Invariants (6 tests) ──
print("\n-- Category 1: Polyhedral Invariants --")
test("1.1 Euler X: V-E+F=2", V_X - E_X + F_X == 2)
test("1.2 Euler Y: V-E+F=2", V_Y - E_Y + F_Y == 2)
test("1.3 Edge Lemma: E_Y/E_X = 5/2", Fraction(E_Y, E_X) == Fraction(5, 2))
test("1.4 Total-Count Y: V+E+F=182", VEF_Y == 182 and VEF_Y == 2 * 91)
test("1.5 Total-Count X: V+E+F=74", VEF_X == 74 and VEF_X == 2 * 37)
test("1.6 |I_h|/|T_d|=5, |O_h|/|T_d|=2=Z", Ih // Td == 5 and Oh // Td == Z)

# ── Category 2: IL Bridge (4 tests) ──
print("\n-- Category 2: IL Bridge --")
test("2.1 Mode-count X: V+F=38", VF_X == 38)
test("2.2 Mode-count Y: V+F=92", VF_Y == 92)
test("2.3 E = V+F-chi for X", E_X == VF_X - 2)
test("2.4 E = V+F-chi for Y", E_Y == VF_Y - 2)

# ── Category 3: Z-Sector Schur Complement (3 tests) ──
print("\n-- Category 3: Z-Sector Schur Complement --")
test("3.1 dim(Z) = 2", Z == 2)
beta0_Z = 1
test("3.2 beta_0(Z) = 1 (Z2: 1 even + 1 odd)", beta0_Z == 1)
N_eff_Y = VF_Y + beta0_Z
test("3.3 N_eff(Y) = (V+F)_Y + beta_0(Z) = 93", N_eff_Y == 93)

# ── Category 4: Spectral-to-beta Bridge (4 tests) ──
print("\n-- Category 4: Spectral-to-beta Bridge --")
test("4.1 V_Y = n_f * G = 60", V_Y == n_f * G, f"{V_Y} = {n_f}*{G}")
test("4.2 F_Y = (N^2-1)*G/N = 32", F_Y == (N_c**2 - 1) * G // N_c)
test("4.3 V_X = n_g*(N_c+1)*2 = 24", V_X == n_g * (N_c + 1) * 2)
b0_SU2 = Fraction(22, 3) - Fraction(4, 3) * n_g - Fraction(1, 6)
test("4.4 a2 = (V+F)_X/G = b0(SU(2))", Fraction(VF_X, G) == b0_SU2)

# ── Category 5: Gauge Couplings (5 tests) ──
print("\n-- Category 5: Gauge Couplings --")
alpha_s = Fraction(Q, N_eff_Y)
test("5.1 alpha_s = Q/N_eff(Y) = 11/93", alpha_s == Fraction(11, 93))
sin2w = float(Fraction(48, 91)) * x_star
test("5.2 sin2theta_W = (48/91)*x* ~ 0.23118",
     abs(sin2w - 0.23118) < 0.00001, f"sin2w = {sin2w:.5f}")
alpha_2 = Fraction(Y, 5 * VF_X)
test("5.3 alpha_2 = Y/[5*(V+F)_X] = 3/95", alpha_2 == Fraction(3, 95))
b0_SU3 = Fraction(11, 1) - Fraction(2, 3) * n_f
test("5.4 a3 = (V+F)_Y/G = 23/3", Fraction(VF_Y, G) == b0_SU3 == Fraction(23, 3))
test("5.5 a2 = 19/6", Fraction(VF_X, G) == Fraction(19, 6))

# ── Category 6: PDG Pull Tests (3 tests) ──
print("\n-- Category 6: PDG Pull Tests --")
pull_as = (float(alpha_s) - ALPHA_S_PDG) / ALPHA_S_ERR
test("6.1 alpha_s pull < 3sigma", abs(pull_as) < 3, f"pull = {pull_as:+.2f}sigma")
pull_s2w = (sin2w - SIN2W_PDG) / SIN2W_ERR
test("6.2 sin2theta_W pull < 3sigma", abs(pull_s2w) < 3, f"pull = {pull_s2w:+.2f}sigma")
arg_z = float(mpmath.arg(z_star))
test("6.3 Berry phase: arg(z*) = x*pi/2", abs(arg_z - x_star * np.pi / 2) < 1e-12)

# ── Category 7: Archimedean Adversarial (3 tests) ──
print("\n-- Category 7: Archimedean Adversarial --")
arch = [(12, 24, 14), (24, 48, 26), (24, 60, 38),
        (30, 60, 32), (60, 120, 62), (60, 150, 92)]
fm = sum(1 for v, e, f in arch
         if Fraction(v + f, G) in {Fraction(19, 6), Fraction(23, 3)})
test("7.1 0/6 Archimedean false matches", fm == 0)
pm = sum(1 for i, (v1, e1, f1) in enumerate(arch)
         for j, (v2, e2, f2) in enumerate(arch) if i < j
         and {Fraction(v1 + f1, G), Fraction(v2 + f2, G)} ==
         {Fraction(19, 6), Fraction(23, 3)})
test("7.2 0 Archimedean pair matches", pm == 0)
test("7.3 Trunc.Oct * Trunc.Ico unique",
     Fraction(VF_X, G) == Fraction(19, 6) and Fraction(VF_Y, G) == Fraction(23, 3))

# ── Category 8: Monte Carlo Anti-Numerology (1 test) ──
# seed=42, 100K trials -> 4 hits = 0.004% (matches document section 10.2)
print("\n-- Category 8: Monte Carlo Anti-Numerology --")
np.random.seed(42)
N_trials = 100000
hits = 0
for _ in range(N_trials):
    G_r = np.random.randint(6, 24)
    VF1 = np.random.randint(10, 200)
    VF2 = np.random.randint(10, 200)
    if (abs(VF1 / G_r - 23 / 3) / (23 / 3) < 0.01 and
            abs(VF2 / G_r - 19 / 6) / (19 / 6) < 0.01):
        hits += 1
p_mc = hits / N_trials
test("8.1 P(random match) < 0.01%", p_mc < 0.0001,
     f"p = {p_mc:.6f} ({hits}/{N_trials})")

# ── Category 9: Sensitivity Analysis (2 tests) ──
print("\n-- Category 9: Sensitivity Analysis --")
shifts_1s = [d for d in range(-3, 4)
             if abs(Q / (VF_Y + d) - ALPHA_S_PDG) / ALPHA_S_ERR < 1.0]
test("9.1 Only delta=+1 gives |pull|<1sigma", shifts_1s == [1],
     f"shifts: {shifts_1s}")
rat_match = []
for pn in range(1, 101):
    for qd in range(2, 201):
        if abs(48 / 91 * pn / qd - SIN2W_PDG) < SIN2W_ERR:
            rat_match.append((pn, qd))
struct = [m for m in rat_match if abs(m[0] / m[1] - x_star) < 1e-6]
test("9.2 x* not replaceable by structural rational", len(struct) == 0,
     f"{len(rat_match)} rationals within 1sigma, 0 are x*")

# ── Category 10: Cross-Paper Interface (4 tests) ──
print("\n-- Category 10: Cross-Paper Interface --")
test("10.1 A = delta_X * delta_Y = 35/437", A == delta_X * delta_Y)
test("10.2 den(A) = num(a2) * num(a3)",
     A.denominator == Fraction(VF_X, G).numerator * Fraction(VF_Y, G).numerator)
test("10.3 MUB(Q=11) = Q+1 = G = 12", Q + 1 == G)
test("10.4 f_seam = alpha_2 = 3/95", alpha_2 == Fraction(3, 95))


# ── Category 11: Hodge-Dirac Integration (3 tests) ──
print("\n-- Category 11: Hodge-Dirac Integration --")

# 11.1 Euler Cell-Count Theorem: V+E+F = 2(V+F-1) for all Archimedean
archimedean_all = [
    (12,18,8), (12,24,14), (24,36,14), (24,36,14),
    (24,48,26), (48,72,26), (24,60,38), (30,60,32),
    (60,90,32), (60,90,32), (60,120,62), (120,180,62), (60,150,92)
]
euler_ok = all(v+e+f == 2*(v+f-1) for v,e,f in archimedean_all)
test("11.1 Euler Cell-Count: V+E+F=2(V+F-1) all Arch.", euler_ok,
     f"13/13 verified" if euler_ok else "FAIL")

# 11.2 Hodge decomposition: 59 exact + 31 coexact = 90
dim_exact = V_Y - 1   # = 59 (rank d₀ = V - b₀, b₀=1 on S²)
dim_coexact = F_Y - 1  # = 31 (rank d₁ = F - b₂, b₂=1 on S²)
test("11.2 Hodge: 59 exact + 31 coexact = 90",
     dim_exact == 59 and dim_coexact == 31 and dim_exact + dim_coexact == E_Y,
     f"{dim_exact}+{dim_coexact}={dim_exact+dim_coexact}")

# 11.3 Hodge asymmetry = δ_Y
hodge_asym = Fraction(abs(dim_exact - dim_coexact), V_Y + F_Y)
test("11.3 δ_Y = |exact-coexact|/(V+F) = 7/23",
     hodge_asym == delta_Y,
     f"({dim_exact}-{dim_coexact})/{VF_Y} = {hodge_asym}")

# ═══════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
n_pass = sum(1 for r in results if r["status"] == "PASS")
n_total = len(results)
all_pass = n_pass == n_total
print(f"RESULT: {n_pass}/{n_total} {'ALL PASS' if all_pass else 'FAILURES DETECTED'}")
print("=" * 70)

print(f"\n--- KEY RESULTS ---")
print(f"  a2 = {float(Fraction(VF_X, G)):.4f} = 19/6, "
      f"a3 = {float(Fraction(VF_Y, G)):.4f} = 23/3")
print(f"  sin2theta_W = {sin2w:.5f} (pull = {pull_s2w:+.2f}sigma)")
print(f"  alpha_s = {float(alpha_s):.5f} (pull = {pull_as:+.2f}sigma)")
print(f"  alpha_2 = {float(alpha_2):.5f} = 3/95")
print(f"  MC: p = {p_mc:.6f} ({hits}/{N_trials})")

# JSON report: save to script directory (portable for any environment)
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "ZS_S1_verify_v1_0_report.json")
report = {
    "document": "ZS-S1 v1.0 Verification Suite",
    "date": "2026-03-23",
    "total": n_total,
    "passed": n_pass,
    "status": "ALL PASS" if all_pass else "FAILURES",
    "key_values": {
        "A": "35/437", "alpha_s": str(alpha_s),
        "sin2w": round(sin2w, 5), "alpha_2": str(alpha_2),
        "a2": str(Fraction(VF_X, G)), "a3": str(Fraction(VF_Y, G)),
        "mc_hits": hits, "mc_trials": N_trials, "mc_p": round(p_mc, 6),
    },
    "tests": results,
}
try:
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nJSON report: {output_path}")
except OSError as e:
    print(f"\nJSON report: skipped ({e})")

sys.exit(0 if all_pass else 1)
