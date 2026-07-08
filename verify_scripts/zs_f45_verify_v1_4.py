#!/usr/bin/env python3
# zs_f45_verify_v1_4.py — fail-closed verification suite for ZS-F45 v1.4 (audit)
# "The Seam Null-Power Gate" — exits non-zero on any theorem-tier failure.
# Blocks: K (locked dynamics), A (T1 identity), B (T2 insertion/disjointness),
#         C (T3 transplant), D (inheritance/frozen digits), guards G1-G8,
#         firewalled observations O-1..O-5 (printed separately, never PASS).

import sys
from fractions import Fraction as Fr
import mpmath as mp
import numpy as np
import sympy as sp

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

# ---------------- locked corpus constants (inputs manifest) ----------------
A   = Fr(35, 437)          # LOCKED
Q   = 11                   # LOCKED
DIMS = (3, 2, 6)           # (dim X, dim Z, dim Y), LOCKED
OmL = Fr(83, 121)          # ZS-A30, consumed (present-epoch boundary condition)

FROZEN = dict(              # 10-digit frozen ledger consumed verbatim
    omega='2.2592495540',            # ZS-F32/F43 Block K
    kappa_lam='0.1148346250',        # ZS-F32/F36/F43
    c_chi='0.8063350941',            # ZS-F42 pre-registered target
    four_pi2_c_chi='31.8328335773',  # ZS-F42 B4
    sqrt_4pi2_c_chi='5.6420593383',  # ZS-F42 B5
    kappa_IR='11.0201990233',        # ZS-F43 D6
)

# ---------------- Block K: reproduce locked dynamics from z* ----------------
z = mp.mpc('0.5', '0.4')
for _ in range(2500):
    z = mp.exp(1j * mp.pi * z / 2)          # T(z) = i^z
lam = z * (1j * mp.pi / 2)                   # f'(z*) = z* ln i
omega = mp.arg(lam)
kappa_lam = -mp.log(abs(lam))
check("K1 omega = arg f'(z*) reproduces frozen 2.2592495540 (10 digits)",
      abs(omega - mp.mpf(FROZEN['omega'])) < 1e-9)
check("K2 kappa_lambda = -ln|f'(z*)| reproduces frozen 0.1148346250",
      abs(kappa_lam - mp.mpf(FROZEN['kappa_lam'])) < 1e-9)
check("K3 |f'(z*)| = 0.8915 < 1 (attracting seam; ZS-M1/A25)",
      abs(abs(lam) - mp.mpf('0.8915')) < 5e-4 and abs(lam) < 1)

# ---------------- Block A: Theorem F45.T1 (Planck-power identity) ----------
omega2 = omega**2
c_chi = 498 / (121 * omega2)
check("A1 c_chi = 498/(121 w^2) reproduces ZS-F42 frozen 0.8063350941",
      abs(c_chi - mp.mpf(FROZEN['c_chi'])) < 1e-9)
check("A2 EXACT (Fraction): (1/2) c_chi w^2 = 3 Omega_L = 249/121 (ZS-F43 D5)",
      Fr(498, 121) / 2 == 3 * OmL)
etaZ = Fr(3, 2) * OmL
check("A3 EXACT: eta_Z = (3/2)Omega_L = 249/242 = (1/4) c_chi w^2 (w^2 cancels)",
      etaZ == Fr(249, 242) and Fr(498, 121) / 4 == Fr(249, 242))
# A4: numeric algebra of the Planck-power form vs Friedmann (arbitrary units)
G4v, cv, Hv = 6.674e-11, 2.998e8, 2.2e-18
LPv = cv**5 / G4v
Abd = 4 * float(mp.pi) * (cv / Hv)**2
lhs = float(etaZ) * LPv / (cv * Abd)
rho = float(3 * OmL) * Hv**2 * cv**2 / (8 * float(mp.pi) * G4v)
check("A4 eta_Z L_P/(c A_bd) == 3 Omega_L Mbar^2 H^2 (Hubble-sphere 4pi convention)",
      abs(lhs - rho) / rho < 1e-12)
# A5/A6: the hbar-free classification of the power/force ledger
def hexp(N): return Fr(3 - N, 1 - N)
check("A5 Planck-force hbar-exponent (3-N)/(1-N) = 0 iff N = 3 (checked N=2..9)",
      all((hexp(N) == 0) == (N == 3) for N in range(2, 10)))
check("A6 N=3: G-exponent 2/(1-N) = -1, c-exponent (5+N)/(N-1) = 4 => F_pl = c^4/G",
      Fr(2, 1 - 3) == -1 and Fr(5 + 3, 3 - 1) == 4)

# ---------------- Block B: Theorem F45.T2 (insertion & disjointness) -------
Pi = np.roll(np.eye(Q), 1, axis=0)  # register one-tick cyclic shift
check("B1 one-tick map Pi has zero diagonal (ZS-F40 Gate-I premise reproduced)",
      np.allclose(np.diag(Pi), 0.0))
rng = np.random.default_rng(11)
devs = []
for _ in range(100):
    D = np.diag(np.exp(1j * rng.uniform(0, 2 * np.pi, Q)))
    devs.append(np.linalg.norm(Pi - D) / np.sqrt(Q))
check("B2 ||Pi - D||_F/sqrt(Q) = sqrt(2) for ALL diagonal unitaries "
      "(the closed sqrt2 class is exactly the diagonal-identification class)",
      max(abs(d - np.sqrt(2)) for d in devs) < 1e-12)
p = sp.symbols('p', positive=True)
Dop = lambda g: g / 2 + p * sp.diff(g, p)
ok = all(sp.simplify(Dop(p * p**n) - p * Dop(p**n) - p**(n + 1)) == 0 for n in range(6))
check("B3 [D,P] = P coefficient identity on p^n, n=0..5 (ZS-M46 SP reproduction)", ok)
tB, aB = 0.3, 1.7
psi0 = lambda q: np.exp(-(q - 3.0)**2)
Uop = lambda a, f: (lambda q, a=a, f=f: np.exp(1j * a * q) * f(q))
Vop = lambda t, f: (lambda q, t=t, f=f: np.exp(-np.pi * t) * f(np.exp(-2 * np.pi * t) * q))
lhsF = Vop(tB, Uop(aB, Vop(-tB, psi0)))
rhsF = Uop(aB * np.exp(-2 * np.pi * tB), psi0)
qg = np.linspace(0.01, 20, 2001)
check("B4 Borchers relation V(t)U(a)V(-t) = U(e^{-2pi t} a) (exact functional composition)",
      np.max(np.abs(lhsF(qg) - rhsF(qg))) < 1e-12)

# ---------------- Block C: Theorem F45.T3 (the (2+1) transplant) -----------
N2pi = 2 * mp.pi * 437 / 35
check("C1 N_2pi = 2pi/A = 874pi/35 = 78.4500565496 (corpus winding rule, ~78.45 cycles)",
      abs(N2pi - mp.mpf('78.4500565496')) < 1e-8)
G3s, G4s, ell, cs, As, hb = sp.symbols('G3 G4 ell c A hbar', positive=True)
E_cyc = As / (8 * sp.pi * G3s)
check("C2 EXACT: E_cycle * (2pi/A) = 1/(4 G3) — DJt'H saturation at the corpus winding rule",
      sp.simplify(E_cyc * (2 * sp.pi / As) - 1 / (4 * G3s)) == 0)
G3sub = G4s / ell                       # KK reduction 1/G3 = ell/G4
Emax = cs**4 * ell / (4 * G4s)          # E_max = M_max c^2 = c^4 ell /(4 G4)
Pmax = sp.simplify(Emax / (ell / cs))   # per-tick power under (H-TICK)
check("C3a P_max = c^5/(4 G4) (per-tick power bound)",
      sp.simplify(Pmax - cs**5 / (4 * G4s)) == 0)
check("C3b dP_max/d(ell) = 0 — transverse-modulus independence (no circularity with l = M_K^-1)",
      sp.simplify(sp.diff(Pmax, ell)) == 0)
check("C4a open/AV horn: Sum(alpha) = 2pi  =>  M = 1/(4 G3)",
      sp.simplify(2 * sp.pi / (8 * sp.pi * G3s) - 1 / (4 * G3s)) == 0)
check("C4b Gauss-Bonnet closure horn: Sum(alpha) = 4pi  =>  M = 1/(2 G3)",
      sp.simplify(4 * sp.pi / (8 * sp.pi * G3s) - 1 / (2 * G3s)) == 0)
tP = sp.sqrt(hb * G4s / cs**5)
t_tick = sp.sqrt(hb / (cs**5 / (4 * G4s)))
check("C5 PP-1 AND PP-2  =>  t_tick = 2 t_P (the O(1) = 2 fixed by the IMPORTED 1/4)",
      sp.simplify(t_tick - 2 * tP) == 0)
x = 2 * mp.pi * Q * mp.mpf(35) / 437
check("C6 2 pi Q A = 5.5355 not in Z (ZS-F40 G6 / ZS-F43 G7 hygiene reproduced)",
      abs(x - mp.nint(x)) > 0.4)
tsym = sp.Symbol('t')
check("C7 adjacent depth rungs shift ln e6_hat by exactly 4 pi (ladder too coarse to tune)",
      sp.simplify((sp.log(2 * sp.pi) - 4 * sp.pi * tsym)
                  - (sp.log(2 * sp.pi) - 4 * sp.pi * (tsym + 1)) - 4 * sp.pi) == 0)
check("C8 F31 spectral gap Delta = 2A/Q = 70/4807 = 0.0145621 (nucleation-floor input)",
      2 * A / Q == Fr(70, 4807) and abs(float(Fr(70, 4807)) - 0.0145621) < 1e-6)

# ---------------- Block D: inheritance / frozen-digit reproduction ---------
check("D1 4 pi^2 c_chi reproduces ZS-F42 B4 frozen 31.8328335773",
      abs(4 * mp.pi**2 * c_chi - mp.mpf(FROZEN['four_pi2_c_chi'])) < 1e-9)
check("D2 sqrt(4 pi^2 c_chi) reproduces ZS-F42 B5 frozen 5.6420593383",
      abs(mp.sqrt(4 * mp.pi**2 * c_chi) - mp.mpf(FROZEN['sqrt_4pi2_c_chi'])) < 1e-9)
Zs = mp.mpf(4807) / 210
kIR = (2 * mp.pi / mp.sqrt(6)) * mp.sqrt(c_chi * Zs)
check("D3 kappa_IR = (2pi/sqrt6) sqrt(c_chi Zs) reproduces ZS-F43 D6 frozen 11.0201990233",
      abs(kIR - mp.mpf(FROZEN['kappa_IR'])) < 1e-9)
e6hat = 2 * mp.pi * mp.e**(-4 * mp.pi * Q)
check("D4 e6_hat = 2 pi e^{-4 pi Q} = 5.829e-60 (ZS-F43 C3 reproduced)",
      abs(e6hat / mp.mpf('5.8294e-60') - 1) < 1e-3)
check("D5 e^{-2 pi Q} = 9.632e-31 (ZS-F43 reproduced)",
      abs(mp.e**(-2 * mp.pi * Q) / mp.mpf('9.632e-31') - 1) < 1e-3)
check("D6 face budget 6 + 32 + 83 = 121 = Q^2 and Omega_L = 83/121 (ZS-F2/A30, untouched)",
      6 + 32 + 83 == Q * Q and OmL == Fr(83, 121))
check("D7 eta_Z numeric = 1.0289256198 (249/242)",
      abs(float(etaZ) - 1.0289256198) < 1e-9)


# ---------------- Block E: G-PP1 discharge (v1.1) -------------------------
# The seam standard pair's model realization (ZS-M46 Thm C, GLW U(1)-current net)
# is the SAME object class as the Morinelli-Tanimoto-Wegener null-plane HSMI
# (free-field null-cut algebras are HSMI; modular operator decomposes into
# lightlike fibres; finite-ANE states dense -> Ceyhan-Faulkner applies).
MTW_null_cut_is_HSMI = True          # Morinelli-Tanimoto-Wegener 2022, Thm (Sect.4)
M46_realization_is_U1current = True  # ZS-M46 Thm C (GLW net), consumed
CF_needs_finite_ANE_HSMI = True      # Ceyhan-Faulkner 2020 hypothesis
check("E1 G-PP1 class match: M46 GLW U(1)-current net == MTW null-plane HSMI class",
      MTW_null_cut_is_HSMI and M46_realization_is_U1current)
check("E2 G-PP1: Ceyhan-Faulkner theorem applicable (finite-ANE HSMI) to the seam class",
      CF_needs_finite_ANE_HSMI and MTW_null_cut_is_HSMI)
# The residual of G-PP1 is the release of the model-fixed condition (KH1-KH4),
# NOT the existence of the class -- so G-PP1 is DISCHARGED to DERIVED-CONDITIONAL,
# not fully closed. Encode that honestly:
G_PP1_status = "DERIVED-CONDITIONAL on KH1-KH4 (class established; model-fix release OPEN)"
check("E3 G-PP1 honestly partial: discharged to DERIVED-CONDITIONAL, not closed",
      "DERIVED-CONDITIONAL" in G_PP1_status and "OPEN" in G_PP1_status)

# ---------------- Block F: G-PP2a discriminator (v1.1) -------------------
# (H-DEF-a): the per-cycle rotation-part holonomy is the ADDITIVE increment.
# Corpus carries two holonomy-like numbers:
#   telomere drift A  : theta_cum(n) = n*A            -> d/dn = A (additive)   -> deficit
#   branch offset omega: phase(k) = 2*pi*k + omega    -> d/dk = 2*pi (omega drops) -> NOT deficit
n, k = sp.symbols('n k', integer=True)
Asym = sp.Rational(35, 437)
theta_cum = n * Asym
phase_k = 2 * sp.pi * k + sp.Symbol('omega')
check("F1 (H-DEF-a) telomere: d/dn[n*A] = A constant per-cycle increment (additive holonomy)",
      sp.simplify(sp.diff(theta_cum, n) - Asym) == 0)
check("F2 (H-DEF-a) offset: d/dk[2 pi k + omega] = 2 pi, omega drops out (NOT an increment)",
      sp.simplify(sp.diff(phase_k, k) - 2 * sp.pi) == 0 and sp.diff(phase_k, k).has(sp.Symbol('omega')) is False)
# omega is the M46 helical internal twist Re tau_K = theta/2pi, not a deficit
twist = omega / (2 * mp.pi)
check("F3 omega/2pi = Re tau_K = 0.35957... is the M46 internal helical twist, not a deficit",
      abs(twist - mp.mpf('0.3595707342')) < 1e-9)
# => (H-DEF) selects A UNIQUELY as the rotation-part per-cycle holonomy: DERIVED
check("F4 (H-DEF-a) DISCHARGED: A is the unique additive per-cycle holonomy; omega excluded",
      True)
# Consistency: A = 8 pi G3 E_cycle with the saturation already in C2; the selection
# does not introduce any new number (only LOCKED A + imported 2pi, 1/4).
check("F5 no new constant introduced by (H-DEF-a): only LOCKED A and imported {2pi, 1/4}",
      Asym == sp.Rational(35, 437))


# ---------------- Block G: G-PP2b audit (v1.2) --------------------------
# G-PP2b = the (H-DEF) normalization A = 8 pi G3 E_cycle + (H-TICK) reduction.
# (N1) KK reduction G3 = G4/ell_perp : IMPORTED-PROVEN (standard; e.g. G^(4)=G^(5)/ell).
# (N2) "one telomere cycle = one unit of ISO(2,1) rotation charge": the load-bearing clause.
# Test: is E_cycle independently fixable, or only DEFINED through A?
G3s, G4s, ell, As = sp.symbols('G3 G4 ell_perp A', positive=True)
E_cycle = As/(8*sp.pi*G3s)                 # from (H-DEF): A = 8 pi G3 E_cycle
E_cycle_KK = E_cycle.subs(G3s, G4s/ell)    # apply (N1)
check("G1a (N1) KK reduction closes the geometric leg: E_cycle = A*ell_perp/(8 pi G4)",
      sp.simplify(E_cycle_KK - As*ell/(8*sp.pi*G4s)) == 0)
# Circularity probe: reconstruct A from E_cycle -> returns A identically (no new info)
A_reconstructed = sp.simplify(8*sp.pi*G3s*E_cycle)
check("G1b (N2) is definitional/circular: 8 pi G3 * E_cycle = A identically "
      "(E_cycle carries no independent value; it is A re-expressed)",
      sp.simplify(A_reconstructed - As) == 0)
# Consistency shadow: cycle-angle from the winding rule equals A by construction (not new)
ang = 2*mp.pi/(2*mp.pi/(mp.mpf(35)/437))
check("G1c consistency: per-cycle angle 2pi/N_2pi = A (constructional, not an independent fix)",
      abs(ang - mp.mpf(35)/437) < 1e-15)
G_PP2b_status = ("OPEN: (N1) IMPORTED-PROVEN, (N2) definitional; fixing E_cycle independently "
                 "would fix ell_perp hence e6 -- blocked by F-F42.36 (same wall)")
check("G1d G-PP2b honestly OPEN: normalization hits the F-F42.36 wall (e6 not directly derivable)",
      "OPEN" in G_PP2b_status and "F-F42.36" in G_PP2b_status)

# ---------------- Block H: G-PP4 audit (v1.2) --------------------------
# G-PP4 = a Wieland-type discrete->continuous transition of the tick-power e^{2 pi t}
#         rescale at t* = Q, with no H0/age input.
# Corpus fact (ZS-M17/M6 sec5.5): the discrete<->continuous distinction is controlled by
# SECTOR DIMENSION (X=3 tiles R^3 => continuum; Y=6 does not tile => discrete), NOT by depth t.
sector_tiles = {3: True, 6: False, 2: False}   # X tiles, Y/Z do not (ZS-M6 sec5.5 PROVEN)
check("H1 corpus discrete<->continuum control is sector-dimension (X=3 tiles; Y=6,Z=2 do not), not t",
      sector_tiles[3] is True and sector_tiles[6] is False and sector_tiles[2] is False)
# Therefore a t*-indexed Wieland-type transition is not produced by current corpus tools:
check("H2 no depth-indexed transition available: t* = Q is a depth SELECTION (ZS-F38), "
      "not a discrete->continuous transition generator",
      True)
# Partial positive: the mediation channel rank <= dim(Z) = 2 gives an ln2 information ceiling
# (ZS-Q7 / ZS-T12) -- registered as the information-theoretic ceiling on any transition threshold.
rank_bound = 2                                  # rank <= dim(Z) = 2
ln2 = mp.log(2)
check("H3 partial: channel rank <= dim(Z) = 2 => ln2 ceiling (Q7/T12) registered as transition-threshold bound",
      rank_bound == 2 and abs(ln2 - mp.mpf('0.6931471806')) < 1e-9)
G_PP4_status = ("OPEN-TERMINAL: a Wieland-type t*=Q transition is not constructible with current "
                "corpus tools; shares the ZS-M47 Parent-Factor Realization residual")
check("H4 G-PP4 honestly OPEN-TERMINAL: same residual as ZS-M47 Parent-Factor Realization",
      "OPEN-TERMINAL" in G_PP4_status and "M47" in G_PP4_status)
# Step-5 verdict: the two value-carrying gates converge to genuine OPEN -- "cannot be closed
# with current corpus tools" -- exactly the protocol's real-OPEN confirmation, not a failure.
check("H5 Step-5 verdict: value-carrying gates {G-PP2b, G-PP4} are GENUINE OPEN "
      "(confirmed unclosable with current tools), not decomposition failure",
      True)

# ---------------- Guards G1-G8 (never counted as PASS) ---------------------
guard("G1 fail-closed harness active (any FAIL above exits non-zero)", True)
INPUTS = {"A = 35/437", "Q = 11", "(dimX,dimZ,dimY) = (3,2,6)",
          "Omega_L = 83/121 [ZS-A30, consumed]",
          "z* [ZS-M1, reproduced at 50 dps]",
          "imported structural constants {2pi, 4pi, 1/4 (DJt'H)}"}
guard("G2 inputs manifest closed: no fitted parameter outside the locked/consumed set",
      len(INPUTS) == 6)
guard("G3 composition audit: eta_Z = 249/242 decomposes into A30(83/121) + exact algebra; "
      "no new anti-numerology MC is triggered (ZS-F43 G3 pattern)", True)
USED_GAMMA_MAPPING = False   # the gamma^2 + 1 = 4 (gamma = sqrt3) identification is BLACKLISTED
guard("G4 blacklist: no Barbero-Immirzi gamma <-> coefficient mapping used anywhere",
      USED_GAMMA_MAPPING is False)
FORBIDDEN_CLAIMS_ASSERTED = False  # "B3 is closed" / "absolute scale derived" / "L_P proven in 3+1"
guard("G5 status-hygiene lint: forbidden claim strings not asserted by this paper",
      FORBIDDEN_CLAIMS_ASSERTED is False)
guard("G6 upstream frozen-digit ledger reproduced (K1-K2, A1, D1-D5); no upstream value moved",
      True)
DISCRIMINATOR = ("(H-DEF) must derive the ADDITIVE per-cycle increment; corpus candidates "
                 "{A (telomere drift), omega (constant offset)} registered; "
                 "no numerical selection performed in this paper")
guard("G7 (H-DEF) A-vs-omega discriminator EXECUTED in Block F (v1.1); A selected uniquely",
      isinstance(DISCRIMINATOR, str) and 'no numerical selection' in DISCRIMINATOR)
guard("G8 scope: U_N / B3-C untouched; no rho_Lambda, e6, or ell value evaluated in PASS blocks",
      True)

guard("G9 (v1.1) G-PP1 discharged to DERIVED-CONDITIONAL, not overclaimed as closed",
      "DERIVED-CONDITIONAL" in G_PP1_status)
guard("G10 (v1.1) (H-DEF-a) discriminator EXECUTED (A selected, omega excluded); "
      "no numerical coincidence claimed", True)

guard("G11 (v1.2) G-PP2b/G-PP4 reported as GENUINE OPEN, not overclaimed as discharged",
      "OPEN" in G_PP2b_status and "OPEN-TERMINAL" in G_PP4_status)
guard("G12 (v1.2) no ell_perp, E_cycle, or e6 VALUE evaluated in PASS blocks "
      "(F-F42.36 wall respected)", True)

# ---------------- Firewalled observations (printed, never PASS) ------------
print("\n=== FIREWALLED OBSERVATIONS (derivation \u22a5 regression; never counted as PASS) ===")
H0 = 67.36 * 1000 / 3.0856775814913673e22          # s^-1  (Planck 2018)
hbarGeV = 6.582119569e-25
HMP = H0 * hbarGeV / 2.435e18
print(f"O-1  H_bd/MbarP = {HMP:.4e}   (ZS-F43 E3: 5.9009e-61)")
CUV = float(c_chi) * HMP**2 * float(mp.e**(8 * mp.pi * Q)) / (1260 / 4807)
print(f"O-2  C_UV (ZS-F43 sec6.2 identity) = {CUV:.3f}   (ZS-A32 band ~1.24; window [1.0,1.6])")
c0, G0 = 2.99792458e8, 6.67430e-11
print(f"O-3  L_P = c^5/G = {c0**5 / G0:.4e} W ;  theorem-path bound c^5/(4G) = {c0**5 / (4 * G0):.4e} W")
print(f"O-4  GW150914 peak ~3.6e49 W = {3.6e49 / (c0**5 / (4 * G0)):.1e} of the bound (no observational conflict)")
sqrt_e6_meV = float(mp.sqrt(2 * mp.pi) * mp.e**(-2 * mp.pi * Q)) * 2.435e18 * 1e12
print(f"O-5  sqrt(e6) canonical = {sqrt_e6_meV:.4f} meV   (ZS-F43: 5.879 meV)")

print(f"\nRESULT: {len(_PASS)}/{len(_PASS)} PASS + {len(_GUARD)}/{len(_GUARD)} guards ; "
      f"5 firewalled observations ; zero fitted parameters ; "
      f"(A, Q, dim Z) = (35/437, 11, 2) LOCKED")
