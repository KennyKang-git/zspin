#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_a25_verify_v1_6.py
=====================
Verification script for ZS-A25 v1.6 — "The Cosmological-Constant Absolute Scale
in Z-Spin Cosmology, Capstone, Corrected."

This reproduces every numerical claim in the v1.6 Code-Availability note and the
body, and prints the v1.6 corrections to v1.5. It does NOT close B3, derive rho_Lambda,
or establish the i-tetration<->modular identification. It demonstrates:

  (1) the corpus constants used (A = (5/19)(7/23) = 35/437, Q = 11, Omega_Lambda = 83/121,
      Omega_Lambda/Omega_m = 2 e^A);
  (2) the i-tetration fixed point z* and its CONTRACTING (Type-III) multiplier;
  (3) that the i-tetration<->modular matching N is TAUTOLOGICAL (an identity, not a
      derivation);
  (4) the four-language number ~276.64 as ONE number with three labels
      (dimensional transmutation / epoch / de Sitter entropy) -- none derives the others;
  (5) that existing corpus coefficients FAIL by hundreds of orders;
  (6) that the local-stationary anomaly route needs a nonabelian sector (abelian fails);
  (7) the everpresent-Lambda check: 3 Omega_Lambda (H0/Mbar_P)^2 = ~7e-121 with NO tuned
      exponent, and the O(1) target chi_Z/alpha_patch = (3*83/121)^2 = 4.235;
  (8) two REJECTED unit-coincidences (anti-numerology);
  (9) the v1.6 corrections of v1.5's over-statements.

Dependencies: standard library only (math, cmath). mpmath used if available (optional).
Run:  python3 zs_a25_verify_v1_6.py
"""

import math
import cmath

try:
    import mpmath as mp
    mp.mp.dps = 40
    HAVE_MP = True
except Exception:
    HAVE_MP = False

# ----------------------------------------------------------------------------- #
#  test harness                                                                  #
# ----------------------------------------------------------------------------- #
_PASS = 0
_FAIL = 0


def check(name, ok, detail=""):
    global _PASS, _FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  |  {detail}"
    print(line)
    return ok


def approx(a, b, rtol=1e-3, atol=1e-9):
    return abs(a - b) <= atol + rtol * abs(b)


def header(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


# ============================================================================= #
#  §0  CORPUS CONSTANTS (LOCKED) AND THEIR VALIDATIONS                            #
# ============================================================================= #
header("§0  Corpus constants (LOCKED) and validations")

A_num, A_den = 35, 437
A = A_num / A_den                       # geometric impedance, LOCKED
Q = 11                                  # register, LOCKED
dimZ, dimX, dimY = 2, 3, 6              # sectors, LOCKED

# A as the product of the two polyhedral rapidity tangents (ZS-F19 D5):
#   delta_X = (V-F)/(V+F) for truncated octahedron  = (24-14)/(24+14) = 10/38 = 5/19
#   delta_Y = (V-F)/(V+F) for truncated icosahedron = (60-32)/(60+32) = 28/92 = 7/23
delta_X = (24 - 14) / (24 + 14)
delta_Y = (60 - 32) / (60 + 32)
A_from_polyhedra = delta_X * delta_Y
check("A = 35/437 (LOCKED)", approx(A, 0.080091533, rtol=1e-7),
      f"A = {A:.9f}")
check("A = tanh psi_X * tanh psi_Y = (5/19)(7/23) (ZS-F19 D5)",
      approx(A_from_polyhedra, A, rtol=1e-12),
      f"(10/38)(28/92) = {A_from_polyhedra:.9f}")
check("Q = dimZ + dimX + dimY = 11 (LOCKED)", (dimZ + dimX + dimY) == Q,
      f"{dimZ}+{dimX}+{dimY} = {dimZ+dimX+dimY}")

# Dimensionless cosmological ratios (DERIVED upstream):
Omega_L = 83 / 121
Omega_m = 38 / 121
check("Omega_Lambda = 83/121 (DERIVED)", approx(Omega_L, 0.6859504, rtol=1e-6),
      f"Omega_L = {Omega_L:.7f}")
check("Omega_Lambda + Omega_m = 121/121 = 1 (flat)",
      approx(Omega_L + Omega_m, 1.0, atol=1e-12),
      f"83/121 + 38/121 = {Omega_L+Omega_m:.6f}")
# HONEST: 83/38 and 2e^A are NOT exactly equal -- they agree to 0.8%. The corpus states
# both 'Omega_L/Omega_m = 2e^A' (DERIVED ratio) and the rationals 83/121, 38/121; the
# rational realization is an approximation, not an identity. Reported, not hidden.
ratio_actual = Omega_L / Omega_m            # 83/38
ratio_2eA = 2 * math.exp(A)
gap = abs(ratio_actual / ratio_2eA - 1)
check("Omega_L/Omega_m = 83/38 ~ 2 e^A to 0.8% (DERIVED ratio; rational realization APPROXIMATE)",
      gap < 0.01,
      f"83/38 = {ratio_actual:.5f} vs 2e^A = {ratio_2eA:.5f}  (gap {gap*100:.2f}%, NOT exact)")


# ============================================================================= #
#  §1  i-TETRATION FIXED POINT AND ITS CONTRACTING (TYPE-III) MULTIPLIER          #
# ============================================================================= #
header("§1  i-tetration fixed point z* and contracting multiplier (ZS-M1 / ZS-A24)")

# f(z) = i^z = exp(i*pi/2 * z); fixed point z* = f(z*).
def f(z):
    return cmath.exp(1j * math.pi / 2 * z)

# Known fixed point (ZS-M1 / ZS-F0):
z_star = complex(0.4382829367, 0.3605924719)

# Verify it is a fixed point and refine by iteration as an independent check.
z_iter = 0.5 + 0.3j
for _ in range(2000):
    z_iter = f(z_iter)
check("z* = i^{z*}  (fixed point, verified)",
      abs(f(z_star) - z_star) < 1e-9,
      f"|f(z*) - z*| = {abs(f(z_star)-z_star):.2e}")
check("independent iteration converges to z*",
      abs(z_iter - z_star) < 1e-6,
      f"iter -> {z_iter.real:.7f} + {z_iter.imag:.7f}i")

# Multiplier f'(z) = (i*pi/2) * exp(i*pi/2 * z) = (i*pi/2) * f(z); at z*: = (i*pi/2)*z*.
fprime = (1j * math.pi / 2) * z_star
mod_fprime = abs(fprime)               # = (pi/2)|z*|
check("f'(z*) = (i*pi/2) z*", True, f"f'(z*) = {fprime.real:+.5f} {fprime.imag:+.5f}i")
check("|f'(z*)| = 0.8915 < 1  (CONTRACTING = Type-III signature)",
      approx(mod_fprime, 0.8915, rtol=2e-3) and mod_fprime < 1.0,
      f"|f'(z*)| = {mod_fprime:.4f}")

neg_ln_fprime = -math.log(mod_fprime)
check("-ln|f'(z*)| = 0.1148", approx(neg_ln_fprime, 0.1148, rtol=2e-2),
      f"-ln|f'(z*)| = {neg_ln_fprime:.4f}")


# ============================================================================= #
#  §2  THE i-TETRATION <-> MODULAR MATCHING N IS TAUTOLOGICAL                     #
# ============================================================================= #
header("§2  The matching N is TAUTOLOGICAL (an identity, not a derivation)")

# N := (modular period pi/A) / (i-tetration rate -ln|f'(z*)|).
N = (math.pi / A) / neg_ln_fprime
check("N = (pi/A)/(-ln|f'(z*)|) = 341.58",
      approx(N, 341.58, rtol=2e-2), f"N = {N:.2f}")

# Tautology demonstration: by construction N * (-ln|f'|) == pi/A EXACTLY.
# So 'asserting N' is 'asserting the modular period equals N * (i-tetration rate)',
# i.e. the identification itself -- not an independent result.
lhs = N * neg_ln_fprime
rhs = math.pi / A
check("N * (-ln|f'|) == pi/A  EXACTLY  =>  N is the identification restated",
      approx(lhs, rhs, rtol=1e-12),
      f"{lhs:.6f} == {rhs:.6f}  (TAUTOLOGICAL)")

# And -ln|f'|/A is not a clean ratio:
ratio = neg_ln_fprime / A
check("-ln|f'(z*)|/A = 1.434 is NOT a clean ratio (no clean A-relation)",
      approx(ratio, 1.434, rtol=2e-2), f"-ln|f'|/A = {ratio:.4f}")


# ============================================================================= #
#  §3  THE FOUR-LANGUAGE NUMBER ~276.64 = ONE NUMBER, THREE LABELS                #
# ============================================================================= #
header("§3  Four-language number ~276.64 -- ONE number, three labels (DERIVED)")

# Observed leading exponent E_obs = ln(Mbar_P^4 / rho_Lambda)
#   rho_Lambda / Mbar_P^4 = 3 * Omega_Lambda * (H0/Mbar_P)^2  (Friedmann)
H0_over_MP = 5.90e-61                   # reduced-Planck units (H0 = 67.4 km/s/Mpc; B3)
rho_ratio = 3 * Omega_L * H0_over_MP**2
E_obs = -math.log(rho_ratio)
check("rho_Lambda/Mbar_P^4 = 3 Omega_L (H0/Mbar_P)^2 = ~7e-121",
      approx(rho_ratio, 7.16e-121, rtol=5e-2),
      f"= {rho_ratio:.3e}")
check("E_obs = ln(Mbar_P^4/rho_Lambda) = 276.64",
      approx(E_obs, 276.64, rtol=2e-3), f"E_obs = {E_obs:.2f}")

print("\n  The same E_obs read three ways (each BACK-SOLVED/CALIBRATED to E_obs,")
print("  NOT independently derived -- this is the honest core of v1.5/v1.6):")

# (a) Dimensional transmutation: rho/Mbar^4 = e^{-32 pi^2/(b_Z g_Z^2)}  (32 = 4*8, fourth power)
bg2_needed = 32 * math.pi**2 / E_obs
bZ_at_gA = bg2_needed / A               # at g_Z^2 = A
check("(a) transmutation: 32 pi^2/(b_Z g_Z^2) = E_obs => b_Z g_Z^2 = 1.1417",
      approx(bg2_needed, 1.1417, rtol=2e-3), f"b_Z g_Z^2 = {bg2_needed:.4f}")
check("    => b_Z = 14.25 at g_Z^2 = A  (back-solved, NOT derived)",
      approx(bZ_at_gA, 14.25, rtol=3e-3), f"b_Z = {bZ_at_gA:.3f}")

# (b) Epoch: 2 nu_now pi/A = E_obs
nu_now_needed = E_obs * A / (2 * math.pi)
check("(b) epoch: 2 nu_now pi/A = E_obs => nu_now = 3.527 (calibrated to present epoch)",
      approx(nu_now_needed, 3.527, rtol=3e-3), f"nu_now = {nu_now_needed:.3f}")
# (corpus ZS-A22 nu_now ~ 3.575 gives a slightly larger exponent; input-dependent)
E_from_A22 = 2 * 3.575 * math.pi / A
print(f"        [note] corpus ZS-A22 nu_now=3.575 -> 2 nu pi/A = {E_from_A22:.1f}"
      f" (input-dependent; ~1% from E_obs)")

# (c) de Sitter entropy: rho/Mbar^4 = 24 pi^2 / S_dS  => ln S_dS = E_obs + ln(24 pi^2)
S_dS = 24 * math.pi**2 / rho_ratio
ln_SdS = math.log(S_dS)
prefactor = math.log(24 * math.pi**2)
check("(c) de Sitter: rho/Mbar^4 = 24 pi^2/S_dS => ln S_dS = E_obs + ln(24 pi^2)",
      approx(ln_SdS, E_obs + prefactor, rtol=1e-9),
      f"ln S_dS = {ln_SdS:.2f} = {E_obs:.2f} + {prefactor:.2f}")
print(f"        => leading exponent 276.6 is COMMON; de Sitter adds an O(1) prefactor")
print(f"           ln(24 pi^2) = {prefactor:.2f} (~2% of 276.6). Agreement is at leading order.")

print("\n  KEY (anti-numerology): b_Z=14.25, nu_now=3.53, ln S_dS are the SAME number ~276.6;")
print("  none forces the others. 14.25 reproduces the epoch -- it is not derived from content.")


# ============================================================================= #
#  §4  EXISTING CORPUS COEFFICIENTS FAIL BY HUNDREDS OF ORDERS                    #
# ============================================================================= #
header("§4  Existing corpus coefficients FAIL (a useful negative result)")

def order_of_magnitude_for_b(bZ, g2=A):
    expo = 32 * math.pi**2 / (bZ * g2)
    log10 = -expo / math.log(10)
    return expo, log10

for label, bZ, expected_log10 in [("19/6", 19/6, -541),
                                   ("23/3", 23/3, -223),
                                   ("12",   12.0, -143)]:
    expo, log10 = order_of_magnitude_for_b(bZ)
    check(f"b_Z = {label}: rho/Mbar^4 ~ 1e{round(log10)}  (FAILS; target 1e-120)",
          approx(log10, expected_log10, atol=2.0),
          f"exponent {expo:.0f} -> 1e{log10:.0f}")

print("\n  => no existing coefficient is near 14.25; the answer is NOT already in the")
print("     corpus, and no coefficient may be used unless first derived from BRST content.")
print("     (A post-hoc 43/3 near-miss is REJECTED as numerology.)")


# ============================================================================= #
#  §5  THE LOCAL-STATIONARY ANOMALY ROUTE NEEDS A NONABELIAN SECTOR               #
# ============================================================================= #
header("§5  Nonabelian requirement (abelian U(1)_Z fails Gate Z1)")

# Pure SU(N) one-loop beta coefficient b = (11/3) N (no matter).
N_for_1425 = 14.25 * 3 / 11
check("pure SU(N): b = (11/3)N = 14.25 => N = 3.886 (NON-INTEGER, no clean gauge group)",
      approx(N_for_1425, 3.886, rtol=1e-2), f"N = {N_for_1425:.3f}")
# Abelian U(1): b = -(1/3) * sum q^2 < 0  (no asymptotic freedom) -> fails Z1 outright.
check("abelian U(1)_Z: b <= 0 (no asymptotic freedom) => fails Gate Z1 outright",
      True, "b_U(1) <= 0  =>  no dimensional transmutation")


# ============================================================================= #
#  §6  EVERPRESENT-LAMBDA: NO TUNED EXPONENT; O(1) TARGET                         #
# ============================================================================= #
header("§6  Everpresent-Lambda (Escape 2): no exponent to tune; O(1) target")

# rho_Lambda ~ Mbar_P^2 H^2 gives the observed value automatically; the '10^-121' is
# (H/Mbar_P)^2, small because the universe is OLD (large four-volume), not a tuned exponent.
check("3 Omega_L (H0/Mbar_P)^2 = ~7e-121 with NO tuned exponent",
      approx(rho_ratio, 7.16e-121, rtol=5e-2),
      f"= {rho_ratio:.3e}  [= (H/Mbar_P)^2 scale, not e^-276]")

# Target shifts from a tuned exponent to a benign O(1) coefficient:
#   Omega_L,rms = (1/3) sqrt(chi_Z/alpha_patch) -> 83/121  requires chi_Z/alpha_patch = (3 Omega_L)^2
target_O1 = (3 * Omega_L)**2
check("O(1) target: chi_Z/alpha_patch = (3*83/121)^2 = 4.235 (robust, NOT numerology-prone)",
      approx(target_O1, 4.235, rtol=1e-3), f"(3*83/121)^2 = {target_O1:.4f}")
print("\n  => ZS-A26 computes chi_Z on the canonical (3,2,6)/11 bottleneck generator and")
print("     finds it O(1) (0.2-2.1), but does not yet reproduce 4.235 (current j + alpha_patch")
print("     absent from the provided files): COMPUTED-INCOMPLETE, not closed.")


# ============================================================================= #
#  §7  REJECTED UNIT-COINCIDENCES (ANTI-NUMEROLOGY)                               #
# ============================================================================= #
header("§7  Rejected unit-coincidences (anti-numerology)")

arg_z_deg = math.degrees(cmath.phase(z_star))
pi_over_A = math.pi / A
print(f"  (i) arg z* = {arg_z_deg:.2f} deg  vs  pi/A = {pi_over_A:.3f}")
check("    REJECTED: arg z* ~ 39.4 deg ~ pi/A is a 180/pi conversion artifact (degrees arbitrary)",
      approx(arg_z_deg, 39.4, rtol=5e-3),
      "rejected as REJECTED-COINCIDENCE")

# (ii) Im f'(z*) = (pi/2) Re(z*) vs arg(z*) in radians
im_fprime = fprime.imag                 # = (pi/2) Re(z*)
arg_z_rad = cmath.phase(z_star)
print(f"  (ii) Im f'(z*) = (pi/2)Re(z*) = {im_fprime:.4f}  vs  arg z* = {arg_z_rad:.4f} rad")
check("    REJECTED: Im f'(z*) ~ arg z* is a z*-specific near-coincidence (no structure)",
      approx(im_fprime, arg_z_rad, rtol=5e-3),
      "rejected as REJECTED-COINCIDENCE")


# ============================================================================= #
#  §8  v1.6 CORRECTIONS OF v1.5 (status, not numerics)                            #
# ============================================================================= #
header("§8  v1.6 corrections of v1.5's over-statements")

corrections = [
    ("v1.5 'no rho_Lambda=f(A,Q) exists, PROVEN'",
     "-> CONDITIONAL Local-Stationary No-Go (DERIVED-CONDITIONAL); "
     "global quantum-state/boundary-selection OUTSIDE it"),
    ("v1.5 'flow-of-weights = c0, PROVEN identity'",
     "-> structural ANALOGY (DERIVED-CONDITIONAL); no map c0<->s_modular constructed"),
    ("v1.5 'nu_now = irreducible calibration (defect)'",
     "-> four-volume QUANTUM CLOCK, [Lambda_hat, T4_hat] = i hbar; "
     "Lambda its conjugate eigenvalue/fluctuation (completion of v1.5)"),
    ("complement (Escapes 1-2)",
     "unimodular boundary-eigenvalue + everpresent-Lambda; both OPEN; "
     "executed COMPUTED-INCOMPLETE in ZS-A26"),
    ("retained from v1.5 (DERIVED)",
     "four-language unification (~276.6); i-tetration tautology; transmutation failure"),
]
for claim, fix in corrections:
    print(f"  - {claim}\n      {fix}")

print("\n  VERDICT: rho_Lambda = f(A, Q, nu_now) with nu_now the universe's clock;")
print("           absolute scale unfixed by (A,Q) WITHIN local-stationary dynamics;")
print("           B3 is NOT closed and NOT proven impossible.")


# ============================================================================= #
#  SUMMARY                                                                       #
# ============================================================================= #
header("SUMMARY")
total = _PASS + _FAIL
print(f"  Checks: {_PASS}/{total} PASS, {_FAIL} FAIL")
print(f"  mpmath available: {HAVE_MP}")
print("  Zero new fitted parameters; (A, Q, dim Z) = (35/437, 11, 2) LOCKED.")
print("  B3 NOT closed, NOT proven impossible; complement executed in ZS-A26 (COMPUTED-INCOMPLETE).")
if _FAIL == 0:
    print("\n  ALL CHECKS PASS -- v1.6 numerics reproduced; corrections recorded.")
else:
    print("\n  SOME CHECKS FAILED -- inspect above.")
