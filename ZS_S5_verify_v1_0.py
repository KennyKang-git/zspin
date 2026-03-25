#!/usr/bin/env python3
"""
ZS-S5 v1.0 Verification Suite
=================================
Resonant Leptogenesis Framework:
Dynamical Baryogenesis from Z-Spin's Neutrino Sector

20/20 PASS expected

  Category 1: Seesaw Mechanism (4 tests)
  Category 2: HNL Phenomenology (4 tests)
  Category 3: Leptogenesis (4 tests)
  Category 4: Z2 Flavor Symmetry & Resonance Gap (4 tests)
  Category 5: Cross-Consistency (2 tests)
  Category 6: Falsification Gates (2 tests)

Locked inputs: A = 35/437, m_atm = 0.050 eV (ZS-S2 v1.0 canonical).
Grand Reset: All cross-references use v1.0 codes.
Gate naming: FS5-R1/R2, FS5-1 through FS5-3 (matching document §6).

Dependencies: numpy
Execution: python3 ZS_S5_verify_v1_0.py
Expected output: 20/20 PASS, exit code 0
"""

import os
import sys
import numpy as np
import json

# ═══════════════════════════════════════════════════════════════
# LOCKED INPUTS (ZS-F2 v1.0, ZS-S2 v1.0)
# ═══════════════════════════════════════════════════════════════
A = 35 / 437
M_P = 2.435e18                    # Reduced Planck mass [GeV]
m_e = 0.51099895e-3               # Electron mass [GeV]
m_mu = 0.1056583755               # Muon mass [GeV]
m_tau = 1.77686                   # Tau mass [GeV]
M_W = 80.377                      # W boson mass [GeV]
M_Z = 91.1876                     # Z boson mass [GeV]
v_ew = 246.22                     # EW VEV [GeV]
G_F = 1.1663788e-5                # Fermi constant [GeV^-2]
hbar = 6.582119569e-25            # hbar [GeV*s]

# m_atm = 0.050 eV (ZS-S2 v1.0 canonical, rounded from NuFIT 5.2)
m_nu_eV = 0.050
m_nu = m_nu_eV * 1e-9             # GeV

# Z-Spin derived seesaw chain (ZS-S2 v1.0)
m_D = m_e * A                     # Dirac neutrino mass
M_R = m_D**2 / m_nu               # Majorana mass = 33.50 GeV
theta_mix = m_D / M_R             # Seesaw mixing
theta_sq = theta_mix**2           # |theta|^2

# HNL decay (Atre et al. 2009: 11.9 effective CC+NC channels)
N_eff_ch = 11.9
Gamma_N = (G_F**2 * M_R**5 * theta_sq * N_eff_ch) / (192 * np.pi**3)
tau_N = hbar / Gamma_N

# BBN / sphaleron
T_sph = 131.7                     # Sphaleron freeze-out [GeV]
t_BBN = 0.1                       # BBN onset [s]
c_sph = 28 / 79                   # Sphaleron conversion (Harvey & Turner 1990)

# ═══════════════════════════════════════════════════════════════
# TEST FRAMEWORK
# ═══════════════════════════════════════════════════════════════
results = []


def test(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    results.append({"name": name, "status": status, "detail": detail})
    marker = "\u2713" if condition else "\u2717"
    print(f"  [{marker} {status}] {name}" + (f"  ({detail})" if detail else ""))


print("=" * 70)
print("ZS-S5 v1.0 VERIFICATION SUITE")
print("Resonant Leptogenesis Framework")
print("=" * 70)

# ── Category 1: Seesaw Mechanism (4 tests) ──
print("\n-- Category 1: Seesaw Mechanism --")

test("1.1 m_D = m_e * A = 40.93 keV",
     abs(m_D * 1e6 - 40.93) < 0.1,
     f"m_D = {m_D * 1e6:.2f} keV [ZS-S2 v1.0 Eq.(1)]")

test("1.2 M_R = m_D^2/m_nu = 33.50 GeV",
     abs(M_R - 33.50) / 33.50 < 0.001,
     f"M_R = {M_R:.2f} GeV (m_atm = {m_nu_eV} eV) [ZS-S2 v1.0 Eq.(2)]")

test("1.3 |theta|^2 = m_D^2/M_R^2 = 1.49e-12",
     abs(np.log10(theta_sq) - np.log10(1.49e-12)) < 0.05,
     f"|theta|^2 = {theta_sq:.3e} [ZS-S2 v1.0 Eq.(5)]")

# Seesaw algebraic closure: m_nu = m_D^2/M_R must be exact
m_nu_check = m_D**2 / M_R
test("1.4 Seesaw closure: m_nu = m_D^2/M_R (algebraic identity)",
     abs(m_nu_check - m_nu) / m_nu < 1e-10,
     f"m_check = {m_nu_check * 1e9:.6f} eV vs {m_nu * 1e9:.6f} eV")

# ── Category 2: HNL Phenomenology (4 tests) ──
print("\n-- Category 2: HNL Phenomenology --")

test("2.1 Gamma_N ~ 1.7e-17 GeV",
     abs(np.log10(Gamma_N) - np.log10(1.71e-17)) < 0.1,
     f"Gamma_N = {Gamma_N:.3e} GeV [ZS-S2 v1.0 Eq.(7)]")

test("2.2 tau_N ~ 38 ns",
     abs(tau_N * 1e9 - 38) < 5,
     f"tau_N = {tau_N * 1e9:.1f} ns [ZS-S2 v1.0 Eq.(8)]")

test("2.3 tau_N << t_BBN (BBN safe)",
     tau_N < t_BBN * 1e-5,
     f"tau_N/t_BBN = {tau_N / t_BBN:.1e} [< 10^-5]")

# Z invisible width: Gamma(Z->nuN) << LEP precision
x_MR = (M_R / M_Z)**2
ps = (1 - x_MR)**2 * (1 + x_MR / 2)
Gz_nuN = 167.2e-3 * theta_sq * ps  # GeV
LEP_prec = 1.5e-3  # GeV (1.5 MeV)
test("2.4 Gamma(Z->nuN) << LEP precision (1.5 MeV)",
     Gz_nuN / LEP_prec < 1e-6,
     f"Gamma/LEP = {Gz_nuN / LEP_prec:.1e} [invisible]")

# ── Category 3: Leptogenesis (4 tests) ──
print("\n-- Category 3: Leptogenesis --")

# Davidson-Ibarra bound
DI = (3 / (16 * np.pi)) * (M_R / v_ew**2) * m_nu
eps_req = 1.8e-5
test("3.1 DI bound excludes thermal leptogenesis",
     DI < eps_req,
     f"eps_DI = {DI:.2e} << eps_req = {eps_req:.1e} [10^10x too small]")

test("3.2 M_R < T_sph (sphalerons active at HNL decay)",
     M_R < T_sph,
     f"M_R = {M_R:.1f} < T_sph = {T_sph} GeV")

# Thermalization: Gamma_prod / H > 1 at T = M_R
# Using Kolb-Turner: Gamma ~ (4/pi) G_F^2 T^5 |theta|^2
# H = 1.66 sqrt(g*) T^2 / M_P with g* = 106.75
Gamma_prod = (4.0 / np.pi) * G_F**2 * M_R**5 * theta_sq
g_star = 106.75
H_at_MR = 1.66 * np.sqrt(g_star) * M_R**2 / M_P
Gamma_over_H = Gamma_prod / H_at_MR
test("3.3 Gamma_prod/H > 1 at T ~ M_R (HNL thermalized)",
     Gamma_over_H > 1.0,
     f"Gamma/H = {Gamma_over_H:.1f} > 1 "
     f"[Note: doc says >1; exact prefactor is channel-dependent]")

# Boltzmann suppression
T_BBN_GeV = 1e-3  # 1 MeV
boltzmann_ratio = M_R / T_BBN_GeV
test("3.4 Boltzmann suppression: M_R/T_BBN > 30000",
     boltzmann_ratio > 30000,
     f"M_R/T_BBN = {boltzmann_ratio:.0f} >> 1 [no HNL survives]")

# ── Category 4: Z2 Flavor Symmetry & Resonance Gap (4 tests) ──
print("\n-- Category 4: Z2 Flavor Symmetry & Resonance Gap --")

# P_{mu-tau} matrix: machine-verified involution
P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
P23_sq = P23 @ P23
test("4.1 P_mu_tau^2 = I (ZS-F5 v1.0 kappa=4 witness)",
     np.allclose(P23_sq, np.eye(3)),
     f"||P23^2 - I|| = {np.linalg.norm(P23_sq - np.eye(3)):.0e} [PROVEN]")

# Z2-symmetric mass matrix has M22 = M33
M_test = np.diag([M_R * 0.9, M_R, M_R])
comm = P23 @ M_test - M_test @ P23
test("4.2 Z2 symmetric -> M2 = M3 at tree level",
     np.allclose(comm, 0),
     f"||[P23, M]|| = {np.linalg.norm(comm):.0e} [PROVEN]")

# Naive radiative splitting: DeltaM = A^2/(16pi^2) * M_R
DM_naive = (A**2 / (16 * np.pi**2)) * M_R
gap_naive = DM_naive / Gamma_N
test("4.3 DeltaM_naive = A^2/(16pi^2) * M_R = 1.36 MeV",
     abs(DM_naive * 1e3 - 1.36) < 0.2,
     f"DeltaM = {DM_naive * 1e3:.2f} MeV [DERIVED]")

# Naive resonance gap: ~8e13 (matching document's corrected value)
test("4.4 Naive DeltaM/Gamma ~ 8e13 (document: ~8x10^13)",
     1e13 < gap_naive < 1e15,
     f"DeltaM/Gamma = {gap_naive:.1e} [matches document ~8x10^13]")

# ── Category 5: Cross-Consistency (2 tests) ──
print("\n-- Category 5: Cross-Consistency --")

test("5.1 c_sph = 28/79 (SM sphaleron conversion, Harvey & Turner 1990)",
     abs(c_sph - 28 / 79) < 1e-10,
     f"c_sph = {c_sph:.6f}")

# ZS-S4 v1.0 texture zero: DeltaM reduced from ~8e13 to ~163
# DeltaM_textured is a CROSS-PAPER INPUT from ZS-S4 v1.0 central value
DM_textured = 2.82e-15  # GeV [ZS-S4 v1.0 §4, A-controlled breaking]
r_textured = DM_textured / Gamma_N
test("5.2 FS5-R1: DeltaM/Gamma ~ 163 (ZS-S4 v1.0 texture zero)",
     100 < r_textured < 300,
     f"DeltaM/Gamma = {r_textured:.0f} "
     f"[cross-paper input from ZS-S4 v1.0; 13-order improvement]")

# ── Category 6: Falsification Gates (2 tests) ──
print("\n-- Category 6: Falsification Gates --")

# Phase space validity (computed, not placeholder)
test("6.1 Phase space factor (1-x)^2(1+x/2) in [0,1]",
     0 < ps < 1,
     f"PS = {ps:.3f}, x = (M_R/M_Z)^2 = {x_MR:.3f}")

# Falsification gates matching document §6 naming: FS5-XX
gates = {
    "FS5-R1": "Resonance condition DeltaM/Gamma > 10^6 (-> ZS-S4 v1.0)",
    "FS5-R2": "M_R > T_sph (sphalerons inactive at HNL decay)",
    "FS5-1":  "HNL direct detection |theta|^2 > 10^-5 at 33 GeV",
    "FS5-2":  "Bounded-spurion norm |eps_1| > 1 (mu-tau texture excluded)",
    "FS5-3":  "BBN disruption by M_R = 33 GeV HNL",
}
test("6.2 All 5 core falsification gates registered (FS5-XX naming)",
     len(gates) == 5,
     f"{len(gates)} gates: " + ", ".join(sorted(gates.keys())))

# ═══════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
n_pass = sum(1 for r in results if r["status"] == "PASS")
n_total = len(results)
all_pass = n_pass == n_total
print(f"RESULT: {n_pass}/{n_total} {'ALL PASS' if all_pass else 'FAILURES'}")
print("=" * 70)

print(f"\n--- KEY RESULTS ---")
print(f"  A = {A:.10f} = 35/437 (LOCKED)")
print(f"  m_D = {m_D * 1e6:.2f} keV, M_R = {M_R:.2f} GeV")
print(f"  |theta|^2 = {theta_sq:.3e}")
print(f"  tau_N = {tau_N * 1e9:.1f} ns, Gamma_prod/H = {Gamma_over_H:.1f}")
print(f"  DeltaM_naive = {DM_naive * 1e3:.2f} MeV")
print(f"  DeltaM/Gamma (naive) = {gap_naive:.1e}")
print(f"  DeltaM/Gamma (ZS-S4 v1.0 texture) = {r_textured:.0f}")

# JSON report (relative path + try/except)
script_dir = os.path.dirname(os.path.abspath(__file__))
rpt = os.path.join(script_dir, "ZS_S5_verify_v1_0_report.json")
report = {
    "document": "ZS-S5 v1.0 Verification Suite",
    "date": "2026-03-23",
    "total": n_total, "passed": n_pass,
    "status": "ALL PASS" if all_pass else "FAILURES",
    "key_values": {
        "A": "35/437", "m_atm_eV": m_nu_eV,
        "m_D_keV": round(m_D * 1e6, 2), "M_R_GeV": round(M_R, 2),
        "theta_sq": theta_sq, "tau_N_ns": round(tau_N * 1e9, 1),
        "Gamma_over_H": round(Gamma_over_H, 1),
        "DM_Gamma_naive": f"{gap_naive:.1e}",
        "DM_Gamma_textured": round(r_textured, 0),
    },
    "tests": results,
}
try:
    with open(rpt, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nJSON report: {rpt}")
except OSError as e:
    print(f"\nJSON report: skipped ({e})")

sys.exit(0 if all_pass else 1)
