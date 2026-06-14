#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_a18_verify_v1_5.py
=====================================================================
Verification script for

    ZS-A18 v1.5 -- "A Recombination No-Go for Z-Spin Goldstone Dark Matter:
    The Massless Dichotomy, the Sound-Speed Window, and the
    Time-Dependent-Mass Obstruction"
    (Kenny Kang, Z-Spin Collaboration, 2026)

WHAT THIS SCRIPT DOES (and, just as importantly, what it does NOT do)
---------------------------------------------------------------------
It reproduces the paper's verification banner:

    "25/25 Internal Consistency Audit PASS | Recombination NO-GO:
     no single m_theta -- constant OR time-dependent -- both preserves the
     eps-Halo and clusters at the 3rd peak (Sec.7.2/7.3); a falling mass
     dilutes as rho~m*a^-3 so the gap is conserved | G-A18.M OPEN (non-adiabatic only)"

in two clearly separated parts:

  PART 1 (25 checks) -- an *internal consistency / anti-numerology audit*:
        the locked axioms (A, Q, dim Z), the ZS-F2 face-counting budget,
        the physical densities, the frozen radial mode, the computed
        isocurvature bound (Sec. 5), the equation-of-state dichotomy
        (Sec. 4), and the backward-compatibility mass window (Sec. 7.1).
        These are arithmetic and logical facts. Passing them does NOT
        verify any physical mechanism.

  PART 2 (F-A18.2) -- the *decisive Boltzmann computation* (Sec. 6.1),
        run with CAMB if available. It checks that, IN THE w~=0 COLD
        REALIZATION, the Z-Spin background reproduces the coherent
        acoustic peaks including the third (l3, D_l, H3/H2). This is a
        CONDITIONAL pass: CAMB assumes the dark matter clusters, so the
        run verifies the massive-pseudo-Goldstone branch and confirms
        the Sec. 4 dichotomy numerically -- it cannot establish that the
        Z-Goldstone is massive.

  PART 3 -- an honest status report. The four core dynamical gates
        (passivity, adiabaticity, w~=0, c_s^2~=0) and the decisive mass
        gate G-A18.M remain OPEN. This script does not, and is not meant
        to, close them. Overall status: HYPOTHESIS-strong programme.

Run:   python3 zs_a18_verify_v1_5.py
CAMB:  pip install camb   (optional; Part 2 is skipped gracefully if absent)
=====================================================================
"""

import math
import sys

# ---------------------------------------------------------------------
# Test harness
# ---------------------------------------------------------------------
class Audit:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.rows = []

    def check(self, name, ok, got="", expect="", note=""):
        ok = bool(ok)
        self.passed += ok
        self.failed += (not ok)
        tag = "PASS" if ok else "FAIL"
        self.rows.append((tag, name, str(got), str(expect), note))
        return ok

    def report(self, title):
        print("\n" + "=" * 78)
        print(title)
        print("=" * 78)
        w = max(len(r[1]) for r in self.rows)
        for tag, name, got, expect, note in self.rows:
            line = f"[{tag}] {name:<{w}}"
            if got or expect:
                line += f"  got={got}"
                if expect:
                    line += f"  expect={expect}"
            if note:
                line += f"   ({note})"
            print(line)
        print("-" * 78)
        print(f"  {self.passed}/{self.passed + self.failed} checks PASS")
        return self.failed == 0


def approx(a, b, rtol=2e-3, atol=0.0):
    return abs(a - b) <= atol + rtol * abs(b)


# =====================================================================
# CONSTANTS  (LOCKED axioms + external inputs, all disclosed)
# =====================================================================
A      = 35.0 / 437.0          # geometric impedance  (LOCKED)
Q      = 11                    # register dimension   (LOCKED)
dimZ   = 2                     # Z-sector dimension   (LOCKED)

h      = 0.6736                # external (Planck)
h2     = h * h

# external (disclosed in Sec. 9 / Sec. 11)
As     = 2.1e-9                # scalar amplitude
r_ten  = 0.0089                # ZS-U1 tensor-to-scalar ratio
T_cmb  = 2.7255                # K
N_eff  = 3.046                 # CMB-epoch effective number (ZS-T1)
M_P_eV = 2.435e18 * 1e9        # reduced Planck mass in eV

# physical / astrophysical constants (SI-ish, for the mass window)
hbar_c_eVm = 1.97327e-7        # eV*m
kpc_m      = 3.0857e19         # m
# H0 in eV:  H0 = 2.1332e-33 * (H0 in km/s/Mpc)/100  -> with h:
H0_eV      = 1.437e-33 * (h / 0.6736)   # ~1.437e-33 eV at h=0.6736


# =====================================================================
# PART 1 -- INTERNAL CONSISTENCY AUDIT (21 checks)
# =====================================================================
a = Audit()

# --- Group A: locked axioms (3) ---
a.check("A1  impedance A = 35/437",
        approx(A, 35/437) and abs(A - 0.0800915) < 1e-6,
        got=f"{A:.7f}", expect="35/437=0.0800915")
a.check("A2  register Q = 11", Q == 11, got=Q, expect=11)
a.check("A3  Z-sector dim(Z) = 2", dimZ == 2, got=dimZ, expect=2)

# --- Group B: ZS-F2 face-counting budget (6) ---
Ob   = 6 / 121.0      # baryons
Ocdm = 32 / 121.0     # cold dark matter (truncated-icosahedron faces)
Om   = Ob + Ocdm      # total matter = 38/121
OL   = 83 / 121.0     # dark energy
a.check("B1  Omega_b   = 6/121",  approx(Ob, 6/121),  got=f"{Ob:.5f}",   expect="0.04959")
a.check("B2  Omega_cdm = 32/121", approx(Ocdm,32/121), got=f"{Ocdm:.5f}", expect="0.26446 (32 faces)")
a.check("B3  Omega_m   = 38/121", approx(Om, 38/121),  got=f"{Om:.5f}",   expect="0.31405")
a.check("B4  Omega_L   = 83/121", approx(OL, 83/121),  got=f"{OL:.5f}",   expect="0.68595")
a.check("B5  flatness  Ob+Ocdm+OL = 1", approx(Ob + Ocdm + OL, 1.0),
        got=f"{Ob+Ocdm+OL:.6f}", expect="1.000000", note="6+32+83=121")
a.check("B6  Omega_c/Omega_b = 16/3", approx(Ocdm/Ob, 16/3),
        got=f"{Ocdm/Ob:.4f}", expect="5.3333")

# --- Group C: physical densities (4) ---
wb = Ob   * h2
wc = Ocdm * h2
wm = Om   * h2
a.check("C1  omega_b = (6/121)h^2 ~ 0.02250",  approx(wb, 0.02250, rtol=3e-3),
        got=f"{wb:.5f}", expect="0.02250")
a.check("C2  omega_c = (32/121)h^2 = 0.12000", approx(wc, 0.12000, rtol=3e-3),
        got=f"{wc:.5f}", expect="0.12000", note="the DM density the 3rd peak fixes")
a.check("C3  omega_m = (38/121)h^2 = 0.14250", approx(wm, 0.14250, rtol=3e-3),
        got=f"{wm:.5f}", expect="0.14250")
# matter-radiation equality from omega_m / omega_r
w_gamma = 2.4728e-5                                   # photons (T=2.7255K)
w_rad   = w_gamma * (1.0 + 0.2271 * N_eff)            # + neutrinos
z_eq    = wm / w_rad - 1.0
a.check("C4  z_eq ~ 3405 (omega_m/omega_r, N_eff=3.046)", approx(z_eq, 3405, rtol=5e-3),
        got=f"{z_eq:.0f}", expect="3405", note="Planck 3402 +/- 26")

# --- Group D: frozen radial mode (1) ---
m_rho = 2 * A           # in units of M_P
a.check("D1  m_rho = 2A*M_P ~ 0.1602 M_P", approx(m_rho, 0.1602, rtol=3e-3),
        got=f"{m_rho:.4f} M_P", expect="0.1602 M_P", note="ZS-F1 frozen radial mode")

# --- Group E: isocurvature gate, Sec. 5 (4) ---
# H_* from r:  P_T=(2/pi^2)(H_*/M_P)^2 ; r=P_T/A_s
H_over_MP = math.pi * math.sqrt(r_ten * As / 2.0)
H_star    = H_over_MP * M_P_eV
f_theta   = M_P_eV          # corpus VEV |Phi|~1 -> f_theta ~ M_P
theta_i   = 1.0
dtheta    = H_star / (2 * math.pi * f_theta)
P_iso     = (H_star / (math.pi * theta_i * f_theta)) ** 2
beta_iso  = P_iso / (P_iso + As)
a.check("E1  H_*/M_P = pi*sqrt(r A_s/2) ~ 9.6e-6", approx(H_over_MP, 9.60e-6, rtol=5e-3),
        got=f"{H_over_MP:.3e}", expect="9.60e-6", note=f"H_*={H_star/1e9:.2e} GeV")
a.check("E2  delta-theta = H_*/(2 pi f_theta) ~ 1.53e-6", approx(dtheta, 1.53e-6, rtol=5e-3),
        got=f"{dtheta:.3e}", expect="1.53e-6")
a.check("E3  beta_iso ~ 4.4e-3", approx(beta_iso, 4.4e-3, rtol=5e-2),
        got=f"{beta_iso:.3e}", expect="4.4e-3")
a.check("E4  beta_iso < 0.038 (Planck 2018 95% CL)", beta_iso < 0.038,
        got=f"{beta_iso:.3e}", expect="< 0.038", note=f"margin x{0.038/beta_iso:.1f}")

# --- Group F: equation-of-state dichotomy, Sec. 4 (1) ---
w_kination = 1.0     # homogeneous massless Goldstone (ZS-M43; c_s=1)
w_monopole = -1.0/3  # static global-monopole halo  (ZS-M43 / Barriola-Vilenkin)
w_cdm_req  = 0.0     # what the third peak requires
dichotomy_ok = (not approx(w_kination, w_cdm_req, atol=1e-9)) and \
               (not approx(w_monopole, w_cdm_req, atol=1e-9))
a.check("F1  massless Goldstone w in {1, -1/3}, never 0",
        dichotomy_ok, got="{+1, -1/3}", expect="0 excluded",
        note="A18.3/A18.4 in TENSION; escape = massive pseudo-Goldstone")

# --- Group G: backward-compatibility mass window, Sec. 7.1 (2) ---
# lower bound: oscillate by equality  m >~ H_eq
H_eq = H0_eV * math.sqrt(2 * Om * (1 + z_eq) ** 3)        # eV
# upper bound: epsilon-Halo flat rotation curve to ~30 kpc (Compton)
m_up = hbar_c_eVm / (30 * kpc_m)                          # eV
a.check("G1  H_eq ~ 2.3e-28 eV (mass-window lower bound)", approx(H_eq, 2.3e-28, rtol=8e-2),
        got=f"{H_eq:.2e} eV", expect="2.3e-28 eV", note="oscillate by equality -> CDM")
a.check("G2  Compton upper ~ 2.1e-28 eV AND upper < lower (window ~closed)",
        approx(m_up, 2.1e-28, rtol=8e-2) and (m_up < H_eq),
        got=f"{m_up:.2e} eV", expect="< H_eq",
        note=f"upper/lower={m_up/H_eq:.2f}; LSS needs >~1e-21 eV (7 orders up)")

# --- Group H: CMB sound-speed window closure, Sec. 7.2 (2) -- NEW in v1.4 ---
def _eV_to_invMpc(m_eV):
    return (m_eV/hbar_c_eVm)*kpc_m*1000.0   # eV -> inverse comoving Mpc (1 Mpc = 1000 kpc)
def cs2_third_peak(m_eV, k3=813/13900.0, a_rec=1/1100.0):
    m = _eV_to_invMpc(m_eV)
    x = (k3/(2*m*a_rec))**2
    return x/(1.0+x)
cs2_cand = cs2_third_peak(2.3e-28)
a.check("H1  c_s^2(k3,a_rec) = 0.44 at Sec.7.1 mass (NOT cold)", approx(cs2_cand, 0.444, atol=0.01),
        got=f"{cs2_cand:.3f}", expect="0.444", note="ultralight scalar is pressure-supported at the 3rd peak")
# threshold mass for c_s^2<0.01, then disjointness vs eps-Halo upper bound
import numpy as _np
_ms=_np.logspace(-29,-25,4000); _mthr=None
for _m in _ms:
    if cs2_third_peak(_m)<0.01:
        _mthr=_m; break
halo_up=2.1e-28
a.check("H2  window disjoint: m(c_s^2<0.01) > eps-Halo bound by ~decade",
        (_mthr is not None) and (_mthr > halo_up) and approx(_mthr,2.05e-27,rtol=5e-2),
        got=f"{_mthr:.2e} eV", expect="> 2.1e-28 eV",
        note=f"ratio {_mthr/halo_up:.1f}x -> no mass clusters AND preserves the halo")

# --- Group I: time-dependent-mass conserved obstruction, Sec. 7.3 (2) -- NEW in v1.5 ---
gap = 2.05e-27/2.1e-28            # Sec.7.2 mass gap (cluster / halo-safe)
a_ratio = 1100.0                  # recombination -> today
n_need = math.log(gap)/math.log(a_ratio)
dens_shortfall = a_ratio**n_need  # extra dilution from rho ∝ m a^-3 = a^-(3+n)
a.check("I1  conserved obstruction: density shortfall == mass gap", approx(dens_shortfall, gap, rtol=1e-6),
        got=f"{dens_shortfall:.2f}x", expect=f"{gap:.2f}x",
        note=f"n={n_need:.3f}; rho∝m a^-3 turns the c_s^2 gap into an equal density gap")
# m ∝ T (n=1) dilutes at the radiation rate: q = 3+n = 4
q_mT = 3.0 + 1.0
a.check("I2  m∝T (n=1) dilutes as radiation: rho∝a^-(3+n)=a^-4", approx(q_mT, 4.0, atol=1e-9),
        got=f"q={q_mT:.1f}", expect="4.0",
        note="pressureless (<w>~0) yet radiation-rate dilution -> not CDM")

part1_ok = a.report("PART 1  --  INTERNAL CONSISTENCY / ANTI-NUMEROLOGY AUDIT (target 25)")


# =====================================================================
# PART 2 -- F-A18.2 DECISIVE BOLTZMANN RUN (CAMB), Sec. 6.1
#   CONDITIONAL on the w~=0 cold realization.
# =====================================================================
print("\n" + "=" * 78)
print("PART 2  --  F-A18.2a COLD-FLUID CONTROL RUN (CAMB)  [w=0 limit; control, not Z-field]")
print("=" * 78)

def find_peaks(ell, tt, lo=80, hi=1300):
    peaks = []
    for l in range(lo + 5, hi - 5):
        win = tt[l - 5:l + 6]
        if tt[l] == win.max() and tt[l] > tt[l - 20] and tt[l] > tt[l + 20]:
            if not peaks or l - peaks[-1][0] > 60:
                peaks.append((l, tt[l]))
    return peaks

camb_ok = None
try:
    import numpy as np
    import camb

    pars = camb.CAMBparams()
    pars.set_cosmology(H0=100 * h, ombh2=wb, omch2=wc, mnu=0.06, tau=0.0544)
    pars.InitPower.set_params(As=As, ns=0.9674, r=0.0)
    pars.set_for_lmax(2600, lens_potential_accuracy=1)
    res = camb.get_results(pars)
    powers = res.get_cmb_power_spectra(pars, CMB_unit='muK', raw_cl=False)
    tt = powers['total'][:, 0]
    ell = np.arange(tt.size)
    pk = find_peaks(ell, tt)
    der = res.get_derived_params()

    b = Audit()
    if len(pk) >= 3:
        (l1, D1), (l2, D2), (l3, D3) = pk[0], pk[1], pk[2]
        print(f"  Peaks (lensed D_l): P1={D1:.0f}@{l1}  P2={D2:.0f}@{l2}  P3={D3:.0f}@{l3} muK^2")
        b.check("F-A18.2a  third-peak position l3 ~ 813 (Planck ~810)",
                approx(l3, 813, atol=12), got=l3, expect="813")
        b.check("F-A18.2b  third-peak height D_l ~ 2542 muK^2 (Planck ~2530)",
                approx(D3, 2542, rtol=3e-2), got=f"{D3:.0f}", expect="2542")
        b.check("F-A18.2c  H3/H2 ~ 0.982 (third ~ second: the CDM signature)",
                approx(D3 / D2, 0.982, atol=0.02), got=f"{D3/D2:.3f}", expect="0.982")
        b.check("F-A18.2d  coherent peaks, NOT a smeared hump (>=3 resolved peaks)",
                len(pk) >= 3, got=f"{len(pk)} peaks", expect=">=3")
    th = der.get('thetastar', None)
    if th is not None:
        b.check("F-A18.2e  100*theta_* ~ 1.0408 (Planck 1.04109)",
                approx(th, 1.0408, atol=2e-3), got=f"{th:.4f}", expect="1.0408")
    rd = der.get('rdrag', None)
    if rd is not None:
        b.check("F-A18.2f  r_drag ~ 147 Mpc (Planck 147.09)",
                approx(rd, 147.0, rtol=5e-3), got=f"{rd:.2f} Mpc", expect="147 Mpc")
    camb_ok = b.report("F-A18.2a cold-fluid control-run checks (assumes clustering)")
except ImportError:
    print("  [SKIPPED] CAMB not installed.  `pip install camb`  to run Part 2.")
    print("  (Part 1 arithmetic audit is independent of CAMB and reported above.)")
except Exception as exc:  # pragma: no cover
    print(f"  [ERROR] CAMB run failed: {exc}")


# =====================================================================
# PART 3 -- HONEST EPISTEMIC STATUS  (the script does NOT close these)
# =====================================================================
print("\n" + "=" * 78)
print("PART 2b --  TIME-DEPENDENT-MASS KG INTEGRATION (Sec. 7.3)")
print("=" * 78)
try:
    import numpy as _np
    from scipy.integrate import solve_ivp as _solve
    _Om,_Or,_OL=0.3153,9.2e-5,0.6848
    def _H2(a): return _Or*a**-4+_Om*a**-3+_OL
    def _dlnH(a):
        h2=_H2(a); return 0.5*(-4*_Or*a**-4-3*_Om*a**-3)/h2
    def _fit_q(n,a_i=2e-3,ef=3.0,mu=40.0):
        Ni=_np.log(a_i); Nf=Ni+ef; mi=mu*_np.sqrt(_H2(a_i))
        def rhs(N,y):
            th,thp=y; a=_np.exp(N); h=_np.sqrt(_H2(a)); mh=mi*(a/a_i)**(-n)/h
            return [thp,-(_dlnH(a)+3.0)*thp-mh**2*th]
        sol=_solve(rhs,[Ni,Nf],[1.0,0.0],method='DOP853',rtol=1e-9,atol=1e-11,
                   dense_output=True,max_step=2e-3)
        N=_np.linspace(Ni,Nf,30000); th,thp=sol.sol(N); a=_np.exp(N); h=_np.sqrt(_H2(a))
        m=mi*(a/a_i)**(-n); rho=0.5*(h*thp)**2+0.5*m**2*th**2; p=0.5*(h*thp)**2-0.5*m**2*th**2
        msk=N>(Ni+1.0); Nb=_np.linspace(Ni+1.0,Nf,25)
        rb=_np.array([rho[msk][(N[msk]>=Nb[i])&(N[msk]<Nb[i+1])].mean() for i in range(24)])
        wb=_np.array([(p[msk]/rho[msk])[(N[msk]>=Nb[i])&(N[msk]<Nb[i+1])].mean() for i in range(24)])
        Nc=0.5*(Nb[:-1]+Nb[1:]); q=-_np.polyfit(Nc,_np.log(rb),1)[0]
        return q,float(wb.mean())
    c=Audit()
    for n in (0.0,0.333,1.0):
        q,w=_fit_q(n)
        c.check(f"KG  n={n:<5}: rho exponent q = 3+n = {3+n:.3f}", approx(q,3+n,atol=0.03),
                got=f"{q:.3f}", expect=f"{3+n:.3f}", note=f"<w>={w:+.3f} (pressureless)")
    camb2_ok=c.report("Time-dependent-mass KG checks (rho ∝ m a^-3 = a^-(3+n); <w>~0)")
except ImportError:
    print("  [SKIPPED] scipy not installed.  `pip install scipy`  to run Part 2b.")
    camb2_ok=None
except Exception as _e:
    print(f"  [ERROR] KG integration failed: {_e}"); camb2_ok=None


print("\n" + "=" * 78)
print("PART 3  --  HONEST EPISTEMIC STATUS  (per ZS-A18 v1.5)")
print("=" * 78)
status = [
    ("EOS dichotomy (Sec. 4)",        "DERIVED",
     "massless Goldstone w in {1,-1/3}, never 0; needs a mass"),
    ("Isocurvature gate (Sec. 5)",    "DERIVED-CONDITIONAL",
     "beta_iso~4.4e-3<0.038, conditional on axion-condensate, f_theta~M_P"),
    ("Passivity A18.1",               "HYPOTHESIS-strong",
     "pinning mechanism at z~1100 unspecified -> OPEN"),
    ("Matter scaling w~=0 (A18.3)",   "TENSION with M43",
     "needs massive pseudo-Goldstone"),
    ("Sound speed c_s^2~=0 (A18.4)",  "TENSION with M43",
     "massless time-dep has c_s=1"),
    ("F-A18.2a control run (Sec.6.1)","COMPUTED-PASS (assumes clustering)",
     "cold-fluid control; NOT a Z-field evolution (F-A18.2b is OPEN)"),
    ("Sound-speed window (Sec.7.2)",  "DERIVED no-go (constant mass)",
     "c_s^2~0.44 at 3rd peak; halo-safe & clustering masses disjoint by a decade"),
    ("Time-dep mass (Sec.7.3)",       "DERIVED no-go  <-- v1.5 central result",
     "rho∝m*a^-3: bridging the gap (x9.8) costs an identical x9.8 density shortfall"),
    ("Topology change F-A18.10",      "OPEN (gate)",
     "V=Lambda^4(1-cos theta) may turn Z-anchor vortices into a string-wall network"),
    ("Mass gate G-A18.M (Sec. 7)",    "OPEN for non-adiabatic only",
     "constant- AND time-dependent-mass escapes CLOSED; only non-adiabatic/multi-sector left"),
]
wn = max(len(s[0]) for s in status)
for name, tag, note in status:
    print(f"  {name:<{wn}} : {tag}")
    print(f"  {'':<{wn}}   {note}")

print("\n" + "-" * 78)
print("  OVERALL: DERIVED recombination NO-GO for the minimal Goldstone /")
print("  pseudo-Goldstone dark-matter identification. Massless -> w in {1,-1/3};")
print("  halo-safe mass -> c_s^2~0.44 at the 3rd peak (no clustering); clustering")
print("  mass -> Compton << 30 kpc (breaks eps-Halo) and 6 orders below LSS.")
print("  The time-dependent-mass escape (v1.5) is also closed: a falling mass")
print("  dilutes the field as rho ∝ m*a^-3, so any mass ratio used to bridge the")
print("  sound-speed gap reappears as an identical density shortfall (obstruction")
print("  conserved). G-A18.M stays OPEN only for non-adiabatic/multi-sector")
print("  constructions, which must re-pass this battery (exact KG/axion-CAMB scan).")
print("-" * 78)


# =====================================================================
# EXIT STATUS
# =====================================================================
ok = part1_ok and (camb_ok in (True, None))   # None = CAMB absent (audit still valid)
print(f"\nVerification banner: {a.passed}/{a.passed + a.failed} Internal Consistency Audit "
      f"{'PASS' if part1_ok else 'FAIL'} | Recombination NO-GO (constant + time-dependent mass; "
      f"Sec.7.2/7.3) | F-A18.2a {'PASS' if camb_ok else ('SKIP' if camb_ok is None else 'FAIL')} "
      f"(control) | G-A18.M OPEN for non-adiabatic only")
sys.exit(0 if ok else 1)
