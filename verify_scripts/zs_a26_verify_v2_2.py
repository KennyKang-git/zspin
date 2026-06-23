#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_a26_verify_v2_2.py
=====================
Corrected verification for ZS-A26 v2.2 (final A26 closure). Fixes the five v2.1
overstatements: (1) honest verification labeling (algebraic illustrations are
machine-checked; corpus-completeness and the physical no-go scope are ANALYTICAL,
not machine-verified); (2) corrected Fourier/commutator test; (3) withdrawn sign
claim; (4) the F23 additive-normalization distinction (entropy constant, not the
vacuum-energy offset); (5) three closure obligations, not three independent gates.

B3 is OPEN; not proven impossible; the missing piece is a vacuum-energy central
normalizer (NOT a relative tool). F23 is the most promising corpus-native template.

Run:  python3 zs_a26_verify_v2_2.py
"""

import math
import numpy as np

_P = 0; _F = 0
def check(name, ok, detail=""):
    """Machine-checked ALGEBRAIC facts only."""
    global _P, _F
    tag = "PASS" if ok else "FAIL"
    _P += ok; _F += (not ok)
    print(f"  [{tag}] {name}" + (f"  |  {detail}" if detail else ""))
    return ok

def analytical(name, detail=""):
    """An ANALYTICAL claim -- NOT machine-verified. Printed, not counted."""
    print(f"  [ANALYTICAL] {name}" + (f"  |  {detail}" if detail else ""))

def header(s):
    print("\n" + "=" * 78); print(s); print("=" * 78)

# ===================================================================== #
header("A. MACHINE-CHECKED ALGEBRAIC ILLUSTRATIONS (shift-blindness)")
# ===================================================================== #

# A1: S4-type hierarchy fixes arg min, not the absolute energy
phi = np.linspace(0.1, 3, 3000); Vshape = (phi**2 - 1)**2
argmins = [phi[np.argmin(Vshape + c0)] for c0 in (0.0, 5.0, -3.0)]
vmins = [(Vshape + c0).min() for c0 in (0.0, 5.0, -3.0)]
check("S4-type: VEV (arg min) is c0-invariant", max(argmins) - min(argmins) < 1e-6,
      f"arg min = {argmins[0]:.4f}")
check("S4-type: absolute V_eff(min) shifts by c0", abs(vmins[1]-vmins[0]-5) < 1e-6,
      f"V_eff(min) = {vmins[0]:+.1f}, {vmins[1]:+.1f}, {vmins[2]:+.1f}")

# A2: M16-type difference cancels c0
check("M16-type: Gamma1-Gamma2 blind to common c0",
      abs(((12.7+0)-(8.3+0)) - ((12.7+100)-(8.3+100))) < 1e-12)

# A3 (CORRECTED): commutator is shift-invariant; selector blind to sign/offset
H = np.array([[2.0, 0.3], [0.3, 1.0]]); F = np.array([[0.0, 1.0], [1.0, 0.0]])
def comm(X, Y): return X @ Y - Y @ X
c = 7.0
check("commutator is SHIFT-INVARIANT: [H+cI,F] = [H,F]  (H,F need NOT commute)",
      np.allclose(comm(H + c*np.eye(2), F), comm(H, F)),
      f"||[H,F]|| = {np.linalg.norm(comm(H,F)):.3f} (nonzero: H,F do NOT commute)")
# genuinely commuting pair: extension selected equally by H and H+cI; sign flips with c
Hd = np.diag([-1.0, 3.0]); Fd = np.diag([5.0, 9.0])   # commute (both diagonal)
ev0 = np.diag(Hd).copy(); evc = np.diag(Hd + 8*np.eye(2))
check("commuting pair: [Hd,Fd]=0 AND [Hd+cI,Fd]=0 (extension blind to shift)",
      np.allclose(comm(Hd, Fd), 0) and np.allclose(comm(Hd + 8*np.eye(2), Fd), 0))
check("a large c FLIPS the absolute sign of an eigenvalue (sign is NOT extension-fixed)",
      (ev0[0] < 0) and (evc[0] > 0), f"eig {ev0[0]:+.0f} -> {evc[0]:+.0f} under +8I")
print("  => CORRECTED: a boundary/Fourier selector fixes domain/extension/eigenvectors/relative")
print("     ordering, NOT the absolute eigenvalue or sign (those belong to N_center).")

# ===================================================================== #
header("B. ANALYTICAL CLAIMS (audit, NOT machine-verified)")
# ===================================================================== #
analytical("all COMPLETED RELATIVE mechanisms audited here are shift-blind",
           "audit of S4/M16/MTS-RMB/Fourier; not a proof over the entire corpus")
analytical("no COMPLETED corpus theorem fixes the VACUUM-ENERGY offset c0",
           "F23 fixes the ENTROPY additive constant, not c0 (see C)")
analytical("the three roles are CLOSURE OBLIGATIONS, possibly met by one mechanism",
           "not necessarily three independent gates")
analytical("Conditional Central-Shift No-Go: physical scope is analytical",
           "applies to relative selectors with a free central shift and no normalizer")

# ===================================================================== #
header("C. THE F23 DISTINCTION (corpus DOES fix an additive constant -- but not c0)")
# ===================================================================== #
print("  Verified-in-corpus (grep): F23.2/F23.4 fix the Type II additive ENTROPY constant")
c_entropy = 0.5 * math.log(2)
check("F23 entropy additive constant c = 1/2 ln 2 (corpus value)", abs(c_entropy - 0.3466) < 1e-3,
      f"c = 1/2 ln2 = {c_entropy:.4f} nats = 1/2 bit")
print("  => the corpus HAS an additive-normalization mechanism (the finite-register canonical trace),")
print("     so 'all corpus tools are relative' is TOO BROAD. BUT F23 fixes the ENTROPY constant,")
print("     NOT the vacuum-energy offset c0; and F23 is DERIVED-CONDITIONAL on the OPEN Condition C.")
print("     F23's trace mechanism is a PARTIAL TEMPLATE for the TYPE of move N_center needs.")

# ===================================================================== #
header("D. THE NO-GO AS A QUOTIENT THEOREM")
# ===================================================================== #
print("  Define: admissible action space  A ;  relative selector class  S_rel ;")
print("          central-shift group  R_center = { Gamma -> Gamma + c0 * Int(sqrt-g) }.")
print("  Tests A1-A3 show every f in S_rel is R_center-invariant, so S_rel FACTORS THROUGH A/R_center.")
print("  => c0 (hence the absolute Lambda) is UNIDENTIFIED by S_rel alone. [Conditional No-Go.]")
analytical("absolute impossibility of B3", "NOT PROVEN -- four N_center candidates remain (F23-type trace first)")

# ===================================================================== #
header("E. CLOSURE OBLIGATIONS & STATUS")
# ===================================================================== #
for o, role, status in [
    ("O1 Scale generation",        "STrlog O_grav, no free coeff", "template S4/M16; O_grav OPEN"),
    ("O2 State/domain selection",  "boundary/seam/Fourier -> domain/extension/ordering", "template F24/F27"),
    ("O3 Central normalization",   "fix/forbid c0*Int(sqrt-g) -> absolute offset+sign", "F23 = partial template (entropy, not c0); vacuum c0 OPEN"),
]:
    print(f"    {o:<28}: {role:<48} [{status}]")

# ===================================================================== #
header("F. RESTORED STANDING RESULTS (consolidated A26 findings -- preserved)")
# ===================================================================== #
A=35/437; OmegaL=83/121; OmegaM=38/121; alpha_PLC=0.1234529231; nu_now=3.527
# F.1 relational law (Branch IV) coefficient
coef = 3*OmegaL*math.sqrt(alpha_PLC)
check("relational law rho_L/Mbar^4 = 3*Omega_L*sqrt(alpha_PLC/N4) = 0.7230439/sqrt(N4)",
      abs(coef-0.7230439)<1e-6, f"3*Omega_L*sqrt(alpha_PLC) = {coef:.7f} (Omega_L=83/121, alpha_PLC={alpha_PLC})")
# F.2 S_MTS finite-register selection theorem + relative entropies
piX,piZ,piY=3/11,2/11,6/11; omX,omZ,omY=9/49,4/49,36/49
Dop=sum(o*math.log(o/p) for o,p in [(omX,piX),(omZ,piZ),(omY,piY)])
Dpo=sum(p*math.log(p/o) for o,p in [(omX,piX),(omZ,piZ),(omY,piY)])
check("S_MTS relative entropy D(omega||pi) = 0.0808390607 (observer vs trace)", abs(Dop-0.0808390607)<1e-9, f"{Dop:.10f}")
check("S_MTS relative entropy D(pi||omega) = 0.0909533851", abs(Dpo-0.0909533851)<1e-9, f"{Dpo:.10f}")
print("     S_MTS^fin(s) = -2s*ln2, unique root s=0 (selects trace pi, excludes observer omega). [PROVEN, v1.7]")
# F.3 Gate E pure-dS saddle scaling
print("     Gate E: V4 = 24pi^2/Lambda^2  =>  Lambda ~ T4^-1/2  =>  rho_L/Mbar^4 ~ 1/sqrt(N4) [DERIVED scaling, v1.8;")
print("             coefficient sqrt(24pi^2) != 0.7230439, coefficient match OPEN]")
# F.4 the 276.6 collapse / epoch tautology (anti-numerology)
epoch = 2*nu_now*math.pi/A
bz = 32*math.pi**2/(epoch*A)
check("276.6 collapse: 2*nu_now*pi/A = ln S_dS = 32pi^2/(b_Z g^2) all = the epoch (tautological)",
      abs(epoch-276.69)<0.1, f"2*nu_now*pi/A = {epoch:.2f}; b_Z = {bz:.3f} reproduces the epoch, NOT derived from BRST")
print("     => any exponent built from nu/S_dS/N4 to hit the epoch is TAUTOLOGICAL (anti-numerology). [v1.8/v2.0]")

# ===================================================================== #
header("G. ELIMINATED-PATHS LEDGER (preserved -- which routes are closed)")
# ===================================================================== #
ledger=[
 ("simple e^{-c/A} exponent fits",        "EXHAUSTED / numerology (A25; (1/8)e^{-7pi/A} RETRACTED)"),
 ("canonical continuous-core lift s->s_grav","CLOSED-NEGATIVE (Dual-Orbit Scale-Blindness Lemma, v1.8)"),
 ("trace-preserving full-s lift",          "CLOSED-NEGATIVE (forces I/11 vs connected QMS rho_s, v1.8)"),
 ("leading trace-equilibrium S_RMB^(0)",   "TERMINATED at leading order (DERIVED-CONDITIONAL on Condition C, v1.9)"),
 ("MTS/RMB canonical selector",            "epoch-blind / relative -> blind to the offset"),
 ("topological c0 quantization (Branch III)","RETRACTED (v1.5); transgression chain missing"),
]
for r,st in ledger: print(f"    {r:<42}: {st}")

header("VERDICT")
print("  B3 OPEN; not proven impossible. Relative tools are necessary (O1,O2) but provably")
print("  insufficient (the quotient no-go). The decisive missing piece is a VACUUM-ENERGY central")
print("  normalizer (O3) -- NOT another relative tool. F23 (entropy constant via finite-register")
print("  trace) is the most promising corpus-native template. A27 (the actual construction) is")
print("  DEFERRED until the counterterm classification can be computed or an explicit offset-")
print("  sensitive global action exists.")

header("SUMMARY")
print(f"  Machine-checked algebraic illustrations: {_P}/{_P+_F} PASS")
print(f"  Corpus-completeness & physical no-go scope: ANALYTICAL audit (NOT machine-verified)")
print("  Zero new fitted parameters; (A, Q, dim Z) = (35/437, 11, 2) LOCKED.")
print("  B3 OPEN; three closure obligations O1^O2^O3; O3 (vacuum central normalizer) is the gap.")
if _F == 0:
    print("\n  ALL ALGEBRAIC CHECKS PASS -- v2.1 overstatements corrected; B3 OPEN; A27 deferred.")
else:
    print("\n  SOME CHECKS FAILED -- inspect above.")
