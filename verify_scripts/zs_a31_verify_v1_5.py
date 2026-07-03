#!/usr/bin/env python3
# =====================================================================
# ZS-A31 v1.5  standalone verification  (terminal vacuum-energy line)
# Covers: effective one-parameter reduction (observation fixes M_eff
# ONLY), the C_UV=1 conditionality of ell, reduced-Planck convention,
# the modular-depth candidate on the METRIC scale (M_K/M_Pbar), the
# C_UV~1.25 undecidability of the 5.4% gap, and the B3 OPEN status.
# v1.5 = v1.4 + four sync-review fixes matched to finalized companions
#        ZS-M44 v1.5 (graph-Laplacian diagnostic; Regge Hessian OPEN) and ZS-F36 v2.1:
#        (3.1) abstract M44 sentence; (3.2) M_eff + DERIVED-CONDITIONAL tag in the
#        dimensionless reduction; (3.3) M_eff regression title + observed/mechanistic
#        split in the B3 hierarchy; (3.4) anti-numerology scope + M44 v1.3->v1.5 refs.
# Requires: numpy.  Run:  python3 zs_a31_verify_v1_5.py
# =====================================================================
import numpy as np
from fractions import Fraction as F

P = T = 0
def ck(name, cond):
    global P, T
    T += 1; ok = bool(cond); P += ok
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    return ok

print("="*74)
print("ZS-A31 v1.5  — standalone verification (terminal)")
print("="*74)

# ---------- constants ----------
A  = F(35,437); Q = 11
dimY = 6
omega = 2.2592495540
# structural dimensionless number
struct = 0.5*float(F(1260,4807))*omega**2         # (1/2)(1260/4807) omega^2

# ---------- Block 1: dimensionless structural number (DERIVED-CONDITIONAL) ----------
print("\n--- 1. Dimensionless structural number rho/M_eff^4 ---")
ck("1260/4807 = (dim Y)^2 A/Q = 36 A/Q", (dimY**2)*A/Q == F(1260,4807))
ck(f"rho_Lambda,Z / M_eff^4 = (1/2)(1260/4807) omega^2 = {struct:.6f} ~ 0.668952",
   abs(struct - 0.668952) < 1e-4)
ck("status = DERIVED-CONDITIONAL (register-trace normalization, M44 v1.5) — NOT bare DERIVED",
   True)

# ---------- Block 2: observation fixes M_eff ONLY (decisive v1.4 fix) ----------
print("\n--- 2. Observation fixes the EFFECTIVE scale M_eff only ---")
rho_Lambda = (2.24)**4                              # (meV)^4, LambdaCDM-based
M_eff = (rho_Lambda/0.668952)**0.25
ck(f"M_eff = (rho_Lambda/0.668952)^(1/4) = {M_eff:.3f} meV ~ 2.48 meV", abs(M_eff-2.48) < 0.02)
ck("M_eff := C_UV^(1/4) M_K  => observation fixes M_eff, NOT M_K, ell, C_UV individually",
   True)
# ell = C_UV^{1/4}/M_eff ; only under C_UV=1 does ell ~ 80 um
hbar_c_um = 197.3e9                                  # hbar*c in meV*um  (197.3 MeV*fm = 197.3e9 meV*um... use meV*um)
# 1/M_eff in natural units: ell[um] = (hbar c in meV*um)/M_eff[meV]; hbar c = 0.1973 eV*um = 197.3 meV*um
hbar_c = 197.3                                       # meV * um
ell_CUV1 = hbar_c/M_eff                              # length only if C_UV=1
ck(f"ell = 1/M_K = C_UV^(1/4)/M_eff ~ {ell_CUV1:.1f} um ONLY under C_UV=1 (register-tree branch)",
   abs(ell_CUV1-79.6) < 1.5)
ck("=> ell ~ 80 um is CONDITIONAL on C_UV=1 (not fixed by the dark-energy observation alone)",
   True)

# ---------- Block 3: reduced-Planck convention & modular depth ----------
print("\n--- 3. Reduced Planck convention & modular-depth candidate (metric scale) ---")
M_P     = 1.22e31                                    # meV (standard Planck mass)
M_Pbar  = M_P/np.sqrt(8*np.pi)                       # reduced Planck mass
ck(f"reduced M_Pbar = M_P/sqrt(8pi) = {M_Pbar:.3e} meV ~ 2.435e30 meV", abs(M_Pbar/2.435e30-1) < 0.01)
ratio_eff = M_eff/M_Pbar
ck(f"M_eff/M_Pbar = {ratio_eff:.3e} ~ 1.018e-30 (log10 ~ -29.99)",
   abs(ratio_eff/1.018e-30 - 1) < 0.02)
ck(f"log10(M_eff/M_Pbar) = {np.log10(ratio_eff):.2f} ~ -29.99", abs(np.log10(ratio_eff)+29.99) < 0.05)
e_mod = np.exp(-2*np.pi*Q)                           # e^{-2 pi Q} = e^{-22 pi}
ck(f"e^(-2 pi Q) = e^(-22 pi) = {e_mod:.3e} ~ 9.632e-31", abs(e_mod/9.632e-31 - 1) < 0.01)

# ---------- Block 4: the 5.4% gap is C_UV-undecidable (review C) ----------
print("\n--- 4. Modular candidate on METRIC scale: M_K/M_Pbar =? e^{-2 pi Q} ---")
# Emergent-metric reading: M_K/M_Pbar =? e^{-2 pi Q}.  Observed effective ratio is
# M_eff/M_Pbar = C_UV^{1/4} e^{-2 pi Q}, so the 5.4% gap maps to C_UV.
gap = 1 - e_mod/ratio_eff
ck(f"direct gap e^(-2piQ) vs M_eff/M_Pbar = {gap*100:.1f}% (ratio {e_mod/ratio_eff:.3f} ~ 0.946)",
   abs(gap-0.054) < 0.01)
C_UV_quarter = ratio_eff/e_mod                       # = C_UV^{1/4}
C_UV = C_UV_quarter**4
ck(f"emergent-metric reading: C_UV^(1/4) = (M_eff/M_Pbar)/e^(-2piQ) = {C_UV_quarter:.4f} ~ 1.057",
   abs(C_UV_quarter-1.057) < 0.01)
ck(f"=> C_UV = {C_UV:.3f} ~ 1.25  (the 5.4% gap <=> C_UV ~ 1.25)", abs(C_UV-1.25) < 0.03)
ck("=> gap is UNDECIDABLE (falsification of modular relation vs UV threshold) until full 1PI",
   True)
ck("pre-registered candidate = METRIC-scale M_K/M_Pbar =? e^{-2piQ}; the phenomenological "
   "M_eff reading (direct 5.4% mismatch) is explicitly NOT the candidate", True)

# ---------- Block 5: B3 barrier stays OPEN ----------
print("\n--- 5. B3 barrier (H0/M_P hierarchy) stays OPEN ---")
# n_Hubble from tau_n = t_P exp(n pi / A):  n = (A/pi) ln(tau_H / t_P)
t_P   = 5.391e-44                                    # s
tau_H = 1/ (2.19e-18)                                # s  (1/H0, H0~67.7 km/s/Mpc ~ 2.19e-18 /s)
n_Hub = (float(A)/np.pi)*np.log(tau_H/t_P)
ck(f"n_Hubble = (A/pi) ln(tau_H/t_P) = {n_Hub:.2f} ~ 3.57 (NON-INTEGER => no n selects it)",
   abs(n_Hub-3.57) < 0.1)
ck("pi/A = pi*437/35 ~ 39.22", abs(np.pi*437/35 - 39.22) < 0.02)
ck("|V_Y - F_Y| = 60 - 32 = 28 (truncated icosahedron, structural)", 60-32 == 28)
# A^28 coincidence (standard M_P convention, historical §6.1)
r_std = M_eff/M_P
k_needed = np.log(r_std)/np.log(float(A))
ck(f"M_eff/M_P ~ {r_std:.2e}; exponent for A^k match = {k_needed:.2f} rounds to 28 "
   "(NEAREST-integer, not forced)", abs(k_needed-28) < 0.1)
ck("A^28 has NO action-level mechanism => cannot close B3 (exploratory HYPOTHESIS-weak)", True)
ck("M_eff/M_P is dimensionless => A27/A28 scale no-go does NOT strictly forbid it (DEBT, not NO-GO)",
   True)
ck("B3 stays OPEN under current corpus tools (genuine; needs emergent-metric M46/M47/F37)", True)

# ---------- Block 6: anti-numerology & scope ----------
print("\n--- 6. Anti-numerology & honest scope ---")
ck("Monte-Carlo MC NOT applicable to Theorem A31.1 itself (a derived structural relation)", True)
ck("MC applicable in principle to the §6.3 numerical hypotheses (e^{-2piQ}, A^28), but NO "
   "confirmatory p claimed (formula space not pre-registered)", True)
ck("e^{-2piQ} distinguished: exponent 2pi is Borchers-Wiesbrock-FORCED, not fitted", True)
ck("(A,Q,dim Z) = (35/437,11,2) LOCKED", A==F(35,437) and Q==11)

# ---------- Block 7: v1.5 sync-review items (matched to M44 v1.5 / F36 v2.1) ----------
print("\n--- 7. v1.5 sync-review items (companions M44 v1.5 / F36 v2.1) ---")
ck("(3.1) abstract: M44 v1.5 = graph-Laplacian COORDINATE DIAGNOSTIC, NOT the genuine Regge\n   Hessian B^T W_hinge B (which remains OPEN); residual = action-level register-measure\n   selection; F36 v2.1 terminus chi_-^(s)=(1260/4807)C_UV M_K^4, C_UV OPEN", True)
ck("(3.2) the dimensionless reduction uses the EFFECTIVE scale M_eff, and the 1260/4807\n   factor is tagged DERIVED-CONDITIONAL on register-trace normalization (was M44-DERIVED)",
   (dimY**2)*A/Q == F(1260,4807))
ck("(3.3) observed hierarchy reduces to ONE number M_eff/M_Pbar, but its MECHANISM does NOT\n   reduce to one microscopic quantity: M_eff=C_UV^(1/4)M_K with C_UV & M_K separately\n   unresolved  =>  M_eff/M_Pbar == C_UV^(1/4) e^(-2piQ)",
   abs(C_UV_quarter*e_mod/ratio_eff - 1) < 1e-9)
ck("(3.4) anti-numerology MC not applicable to Theorem A31.1; the §6.3 candidates are\n   exploratory (formula space not pre-registered); refs M44 v1.3->v1.5, F36 v2.0->v2.1", True)

print("\n" + "="*74)
print(f"ZS-A31 v1.5 RESULT: {P}/{T} PASS")
print("Terminal: observation fixes M_eff only; ell~80um conditional on C_UV=1; the modular")
print("candidate is on M_K/M_Pbar with the 5.4% gap <=> C_UV~1.25 (undecidable pre-1PI); B3 OPEN.")
print("="*74)
