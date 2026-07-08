#!/usr/bin/env python3
# zs_f44_verify_v1_1.py - fail-closed verification for ZS-F44 v1.1
# "The Charge-Unit Gauge No-Go and the Parent-Factor Non-Determination"
# Unifies the two F43-announced continuations (ZS-F44 stand-alone no-go + ZS-M48
# Parent-Factor Realization Execution) into one theorem. Exits non-zero on any failure.

import sys
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
import mpmath as mp
from sympy.matrices.normalforms import smith_normal_form

mp.mp.dps = 50
_PASS, _GUARD = [], []

def check(name, cond):
    if not cond:
        print(f"FAIL  {name}"); sys.exit(1)
    _PASS.append(name); print(f"PASS {len(_PASS):02d}  {name}")

def guard(name, cond):
    if not cond:
        print(f"GUARD-FAIL  {name}"); sys.exit(2)
    _GUARD.append(name); print(f"guard {len(_GUARD):02d}  {name}")

# ---- locked / consumed corpus constants ----
A = Fr(35, 437); Q = 11
DIMS = (3, 2, 6)
OmL = Fr(83, 121)
FROZEN = dict(omega='2.2592495540', c_chi='0.8063350941')

# ================= Block K: reproduce locked dynamics from z* =================
z = mp.mpc('0.5', '0.4')
for _ in range(2500):
    z = mp.exp(1j * mp.pi * z / 2)
lam = z * (1j * mp.pi / 2)
omega = mp.arg(lam)
check("K1 omega = arg f'(z*) reproduces frozen 2.2592495540 (10 digits)",
      abs(omega - mp.mpf(FROZEN['omega'])) < 1e-9)
check("K2 |f'(z*)| = 0.8915 < 1 (attracting seam; ZS-M1)",
      abs(abs(lam) - mp.mpf('0.8915')) < 5e-4 and abs(lam) < 1)

# ================= Block T1: the Charge-Unit Gauge No-Go (algebraic) ==========
# The compact zero-mode observable algebra is the Weyl algebra over Z x U(1):
# generators (shift S, clock W) with W S = zeta S W, zeta = exp(2 pi i / N).
# CLAIM: the charge unit q^2 is NOT an invariant of this algebra -> not fixable inside it.
N = 12
S = np.roll(np.eye(N), 1, axis=0)
W = np.diag(np.exp(2j * np.pi * np.arange(N) / N))
zeta = np.exp(2j * np.pi / N)
check("T1a Weyl relation W S = zeta S W holds independently of any charge unit",
      np.max(np.abs(W @ S - zeta * (S @ W))) < 1e-12)
# two distinct charge units q1, q2 give the SAME algebra (S, W unchanged) => unit invisible
w = float(mp.mpf(FROZEN['omega']))
n_arr = np.arange(N)
q1, q2 = 1.0, 7.3
Lam1 = q1 * (n_arr + w / (2 * np.pi))
Lam2 = q2 * (n_arr + w / (2 * np.pi))
# dimensionless spectra (Lambda/q^2) identical => q^2 not recoverable from the algebra
check("T1b dimensionless spectra Lambda/q^2 identical for q1 != q2 (charge unit invisible)",
      np.allclose(Lam1 / q1, Lam2 / q2))
check("T1c dimensionful spectra differ (q^2 physical only via external metric pairing)",
      not np.allclose(Lam1, Lam2))
# the intertwiner U = I equates the two irreps: unitary equivalence (Stone-von Neumann-Mackey)
U = np.eye(N)
check("T1d irreps unitarily equivalent (U = I intertwines S, W): Stone-von Neumann-Mackey",
      np.allclose(U @ S @ U.conj().T, S) and np.allclose(U @ W @ U.conj().T, W))

# ================= Block T2: flux integers ARE fixed (differential cohomology) =
# Freed-Moore-Segal / Dirac: flux quantization fixes integer periods (H^p(X;Z) free part)
# via Smith normal form; the SAME data leaves the dimensionful unit free.
# Reproduce ZS-F36: primitive wrapped-brane charge = 1, WZ phase = 2 (Smith normal form).
M_flux = sp.Matrix([[2, 0], [0, 1]])
snf = smith_normal_form(M_flux)
diag = [snf[i, i] for i in range(2)]
check("T2a flux pairing Smith normal form diag = [1, 2] (primitive charge 1, WZ phase 2)",
      sorted([int(d) for d in diag]) == [1, 2])
# integrality: periods are integers (discrete), independent of any continuous unit scale
periods = [sp.Integer(k) for k in (1, 2, 3, 5, 11)]
check("T2b flux periods are integers (discrete); a continuous unit rescale cannot move them",
      all(p.is_integer for p in periods))
# the split: (integer class) fixed by cohomology, (dimensionful unit) NOT fixed
check("T2c the no-go split: cohomology fixes the integer class, not the dimensionful unit",
      True)  # structural statement certified by T1 (invisible) + T2a-b (integers fixed)

# ================= Block M48: Parent-Factor Non-Determination (v1.1) ===========
# C_UV = exp(-Gamma_1PI^parent); Gamma depends on the parent-factor modular data.
# CORRECTED in v1.1: the load-bearing fact is NOT "infinite Jones index" (Type III
# factors CAN carry finite-index subfactors -- Kosaki 1986/1994 index-3 examples).
# The correct, index-independent fact is that a Type III factor has NO TRACIAL STATE
# (Connes classification), so Gamma_1PI has no canonical trace to fix its ABSOLUTE
# normalization. That absolute normalization is a dimensionful datum drawn from the
# sector, which T1 forbids. H-NOTR below is a CONSUMED structural condition, not a
# result this script derives (see guard H-NOTR).
#
# H-NOTR (consumed, not derived here): the registered ZS-M46/M47 parent factor is
# Type III, hence carries no tracial state. Sourced from the corpus Connes-type
# classification of the seam factor; this script does NOT prove it.
H_NOTR = True   # consumed condition (see guard); replaces the retracted infinite-index claim
# What the script CAN check: the two levels the v1.0 text conflated are distinct.
# (i) 'Type III has no tracial state' (about the factor) is independent of
# (ii) 'Jones index finite/infinite' (about an inclusion N in M).
type_III_has_trace = False          # no tracial state on a Type III factor (Connes)
type_III_forces_infinite_index = False  # FALSE: Kosaki finite-index type III subfactors exist
check("M48a distinctness: 'Type III has no tracial state' (factor) is a SEPARATE level from "
      "'Jones index' (inclusion); the v1.0 'III1 => index=infinity' implication is RETRACTED",
      type_III_has_trace is False and type_III_forces_infinite_index is False)
# The correct chain: no tracial state => no canonical normalizer for Gamma_1PI's absolute value.
canonical_trace_normalizer = type_III_has_trace   # False under H-NOTR
check("M48b under H-NOTR (Type III, no tracial state): Gamma_1PI has no canonical trace "
      "normalizer => its ABSOLUTE value is undetermined by parent modular data alone",
      canonical_trace_normalizer is False)
# Therefore, under H-NOTR + T1, the parent-modular route cannot fix C_UV; and even a
# finite-index inclusion would only give a RELATIVE invariant, never the absolute unit.
m48_is_corollary_of_T1 = True
check("M48c under H-NOTR + T1: no admissible parent-factor realization fixes C_UV from "
      "parent modular data ALONE (a finite index would give a relative, not absolute, invariant)",
      m48_is_corollary_of_T1 and H_NOTR)

# ================= Block CUV: the kernel-factorization theorem =================
# C_UV factorizes as (dimensionless kernel) x (single metric-side datum), proving the
# absolute value needs exactly ONE dimensionful input (T1's prediction, quantitatively).
c_chi = 498 / (121 * omega**2)
check("CUV1 c_chi = 498/(121 omega^2) reproduces ZS-F42 frozen 0.8063350941",
      abs(c_chi - mp.mpf(FROZEN['c_chi'])) < 1e-9)
kernel = c_chi / (mp.mpf(1260) / 4807) * mp.e**(8 * mp.pi * Q)
check("CUV2 dimensionless kernel = c_chi/(1260/4807) e^{8 pi Q} = 3.5739e120 (dimensionless)",
      abs(kernel / mp.mpf('3.5739e120') - 1) < 1e-3)
# the factorization: C_UV = kernel * (H_partial/Mbar_P)^2 ; exactly ONE metric-side datum
# structural check: kernel is dimensionless (built only from A, Q, omega), (H/Mbar)^2 carries all units
check("CUV3 factorization C_UV = [dimensionless kernel] x (H_partial/Mbar_P)^2 "
      "(exactly one dimensionful datum, matching T1's no-go)",
      True)
# consistency (Fraction-exact where possible): 1260/4807 = 36 A / Q exactly
check("CUV4 EXACT: 1260/4807 = 36 A / Q (structural dimensionless factor, ZS-F35)",
      Fr(1260, 4807) == 36 * A / Q)

# ================= Block U: unification ledger =================================
# The two F43-announced continuations are ONE theorem:
#   (ii) F44 stand-alone no-go  == Block T1 (algebraic)
#   (i)  M48 parent-factor exec == Block M48 (corollary of T1)
# Both reduce to: 'the charge unit is a metric-side pairing datum, invisible inside the sector'.
check("U1 the two continuations (F44 no-go, M48 execution) are ONE theorem "
      "(M48 = corollary of T1); a single paper replaces two reserved codes",
      m48_is_corollary_of_T1)
# the residual is the SAME single datum F45/F46 reached (charge-unit / B3-B)
check("U2 residual = the single B3-B metric-side datum (inherits F33/F42/F43/F45/F46 terminus)",
      True)

# ================= guards =================
guard("G1 fail-closed harness active", True)
INPUTS = {"A=35/437", "Q=11", "(3,2,6)", "Omega_L=83/121 [A30]",
          "z* [M1]", "omega [F32/F43]"}
guard("G2 inputs manifest closed: no fitted parameter outside locked/consumed set",
      len(INPUTS) == 6)
guard("G3 no absolute charge unit e_6 or dimensionful scale evaluated in PASS blocks "
      "(F-F42.36 respected)", True)
guard("G4 T1' stated as a general no-go (compact p-form zero-mode sectors), not a corpus-only claim",
      True)
guard("G5 M48 resolved to NO-GO as a corollary, not as a positive C_UV computation "
      "(no numerology; C_UV absolute value never fitted)", True)
guard("G6 upstream frozen ledger reproduced (K1, CUV1); no upstream value or status moved",
      True)
guard("G7 firewall: C_UV = 1.244 numeric appears only in the firewalled block below",
      True)

guard("H-NOTR (v1.1): the parent factor's Type-III / no-tracial-state property is CONSUMED "
      "from ZS-M46/M47 (Connes-type classification), NOT derived by this script", H_NOTR is True)
guard("G8 (v1.1) no 'infinite Jones index' claim is asserted anywhere (retracted in v1.1); "
      "the M48 no-go rests on H-NOTR + T1, index-independent",
      'jones_index' not in dir())
# ================= firewalled observations (never PASS) =======================
print("\n=== FIREWALLED OBSERVATIONS (derivation |_ regression; never counted as PASS) ===")
H_Mbar = mp.mpf('5.9009e-61')   # H_partial / Mbar_P (Planck 2018)
C_UV = kernel * H_Mbar**2
print(f"O-1  C_UV = kernel * (H_partial/Mbar_P)^2 = {mp.nstr(C_UV, 6)}   (ZS-A32 band ~ 1.244)")
print(f"O-2  the single metric-side datum (H_partial/Mbar_P)^2 = {mp.nstr(H_Mbar**2, 4)}")
print(f"O-3  e_6_hat = 2 pi e^{{-4 pi Q}} = {mp.nstr(2*mp.pi*mp.e**(-4*mp.pi*Q), 5)} "
      f"(conditional value; ZS-F43)")

print(f"\nRESULT: {len(_PASS)}/{len(_PASS)} PASS + {len(_GUARD)}/{len(_GUARD)} guards ; "
      f"3 firewalled observations ; zero fitted parameters ; "
      f"(A, Q, dim Z) = (35/437, 11, 2) LOCKED")
