#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_f26_verify_v1_4.py
=====================
ZS-F26 v1.4 — "The Operator Ladder and the Unconditional GNS Core"
Standalone verification suite: reproduces all 47 checks of Appendix A
(categories A1-A9, B1-B11, C1-C7, D1-D4, E1-E3, F1-F3, G1-G10).

Usage:        python3 zs_f26_verify_v1_4.py
Dependencies: numpy, mpmath
Runtime:      ~3-6 minutes (dominated by 160 zeta zeros via mpmath and
              the eight-window ell-scan). Progress is printed per block.
Output:       per-check PASS/FAIL lines, final tally, JSON dump
              (zs_f26_verify_v1_4_results.json). Exit code 0 iff 47/47.

Conventions (paper section 3.1, v1.2+ half-window convention):
  g real, supported in [0, ell]; sine basis phi_k(u) = sqrt(2/ell) sin(k pi u / ell);
  ghat_k(r) = sqrt(2/ell) a_k (1 - (-1)^k e^{i r ell})/(a_k^2 - r^2),  a_k = k pi/ell;
  Q_W = pole + (-log pi) L2 + archimedean digamma integral + prime block
  in the F25 6.0 / Iwaniec-Kowalski Thm 5.12 normalization.

NO CLAIM on RH / GRH is made or tested by this script (check F3): every
positivity result below is a finite-dimensional compression statement.
"""

import sys, json, time
import numpy as np
import mpmath as mp

mp.mp.dps = 20
LN2  = float(np.log(2.0))
LN3  = float(np.log(3.0))
LNPI = float(np.log(np.pi))
EULER = 0.5772156649015328606
T0 = time.time()

# ----------------------------------------------------------------------
# check framework
# ----------------------------------------------------------------------
RESULTS = []
def check(cid, desc, ok, detail=""):
    RESULTS.append(dict(id=cid, desc=desc, ok=bool(ok), detail=str(detail)))
    print("[%s] %-4s %s  %s" % ("PASS" if ok else "FAIL", cid, desc, ("| " + str(detail)) if detail else ""))

def progress(msg):
    print("... %s (t=%.0fs)" % (msg, time.time() - T0))

# ----------------------------------------------------------------------
# shared machinery
# ----------------------------------------------------------------------
def digamma_c(z):
    """Vectorized complex digamma (recurrence + asymptotic series)."""
    z = np.array(z, dtype=complex); shift = np.zeros_like(z); zz = z.copy()
    for _ in range(60):
        m = np.abs(zz) < 16.0
        if not m.any(): break
        shift[m] += 1.0/zz[m]; zz[m] += 1.0
    x2 = 1.0/(zz*zz)
    ser = (x2/12. - x2**2/120. + x2**3/252. - x2**4/240.
           + x2**5/132. - (691/32760.)*x2**6 + x2**7/12.)
    return np.log(zz) - 0.5/zz - ser - shift

def repsi(r):
    return digamma_c(0.25 + 0.5j*np.asarray(r, float)).real

def fourier_basis(ell, M, r):
    """ghat_k(r) for the sine basis of [0, ell], k = 1..M, vectorized in r."""
    r = np.asarray(r, float); out = np.zeros((M, r.size), complex)
    c = np.sqrt(2./ell)
    for k in range(1, M+1):
        a = k*np.pi/ell; x = r - a
        E = np.empty(r.size, complex); sm = np.abs(x) < 1e-3
        xs = x[sm]*ell
        E[sm]  = 1j*ell*(1 + 1j*xs/2 - xs*xs/6 - 1j*xs**3/24)
        E[~sm] = (np.exp(1j*x[~sm]*ell) - 1.)/x[~sm]
        out[k-1] = c*a*E/(a + r)
    return out

def trapz_w(r):
    w = np.zeros_like(r)
    w[1:-1] = (r[2:] - r[:-2])/2; w[0] = (r[1]-r[0])/2; w[-1] = (r[-1]-r[-2])/2
    return w

def Lam(n):
    for p in (2, 3, 5, 7, 11, 13):
        if n % p == 0:
            q = n
            while q % p == 0: q //= p
            return float(np.log(p)) if q == 1 else 0.0
    return 0.0

# frequency grid (the "hi-res" grid of B.lam, v1.2+)
def make_grid(h1=0.004, h2=0.02, h3=0.2):
    return np.concatenate([np.arange(1e-6, 100., h1),
                           np.arange(100., 1500., h2),
                           np.arange(1500., 8000., h3)])
RG = make_grid(); WG = trapz_w(RG); WPSI = WG*repsi(RG)

def pole_functionals(ell, M):
    ks = np.arange(1, M+1); a = ks*np.pi/ell; c = np.sqrt(2./ell)
    Mp = c*a*(1 - ((-1.)**ks)*np.exp(+ell/2))/(0.25 + a*a)
    Mm = c*a*(1 - ((-1.)**ks)*np.exp(-ell/2))/(0.25 + a*a)
    return Mp, Mm

def build_blocks(ell, M, wpsi=None, grid=None):
    """Return (Q_W, Q_arch) Gram matrices on the M-mode sine basis of [0, ell]."""
    if grid is None: grid, wpsi = RG, WPSI
    Phi = fourier_basis(ell, M, grid)
    Mp, Mm = pole_functionals(ell, M)
    Qa = (np.outer(Mp, Mm) + np.outer(Mm, Mp) - LNPI*np.eye(M)
          + (1/np.pi)*np.real((Phi*wpsi) @ Phi.conj().T))
    Q = Qa.copy(); n = 2
    c = np.sqrt(2./ell); a = np.arange(1, M+1)*np.pi/ell
    while np.log(n) < ell - 1e-12:
        lam = Lam(n)
        if lam > 0:
            tau = np.log(n); v = np.linspace(0, ell - tau, 40001)
            Pj = c*np.sin(np.outer(a, tau + v)); Pk = c*np.sin(np.outer(a, v))
            S = (Pj*trapz_w(v)) @ Pk.T
            Q = Q - 2*(lam/np.sqrt(n))*0.5*(S + S.T)
        n += 1
    return 0.5*(Q + Q.T), 0.5*(Qa + Qa.T)

def lam_min(Mx): return float(np.linalg.eigvalsh(Mx)[0])

# ======================================================================
# A. Closed forms and structural identities
# ======================================================================
progress("block A: closed forms")

# A1 psi(1/4)
psi14_num = float(mp.digamma(mp.mpf(1)/4))
psi14_cf  = -EULER - np.pi/2 - 3*LN2
check("A1", "psi(1/4) = -gamma - pi/2 - 3 log 2",
      abs(psi14_num - psi14_cf) < 1e-12, "err=%.1e" % abs(psi14_num - psi14_cf))

# A2 digamma vectorization vs mpmath
pts = [0.25+0.5j, 0.25+5j, 0.25+30j, 0.25+200j, 0.25+3000j]
errs = [abs(complex(digamma_c([p])[0]) - complex(mp.digamma(p))) for p in pts]
check("A2", "complex digamma vectorization vs mpmath (5 pts)",
      max(errs) < 1e-12, "max err=%.1e" % max(errs))

# A3 monotonicity of Re psi(1/4 + ir/2) on [0, 60]
rr = np.linspace(0, 60, 6001); vals = repsi(rr)
check("A3", "Re psi(1/4+ir/2) strictly increasing on [0,60]",
      bool(np.all(np.diff(vals) > 0)), "min step=%.2e" % float(np.diff(vals).min()))

# A4 pole identity: closed-form M_pm vs numeric; 2 M+ M- vs double integral
ell = 1.0; M = 1
uu = np.linspace(0, ell, 200001); wu = trapz_w(uu)
g1u = np.sqrt(2./ell)*np.sin(np.pi*uu/ell)
Mp_num = float(np.sum(wu*g1u*np.exp(+uu/2))); Mm_num = float(np.sum(wu*g1u*np.exp(-uu/2)))
Mp_cf, Mm_cf = (float(x[0]) for x in pole_functionals(ell, 1))
dbl = float(2*np.einsum("i,j,i,j,i,j->", wu, wu, g1u, g1u, np.exp(uu/2), np.exp(-uu/2)))
e1 = abs(Mp_num - Mp_cf)/abs(Mp_cf) + abs(Mm_num - Mm_cf)/abs(Mm_cf)
e2 = abs(dbl - 2*Mp_cf*Mm_cf)/abs(2*Mp_cf*Mm_cf)
check("A4", "pole identity: closed form vs integral; 2M+M- vs double integral",
      e1 < 1e-9 and e2 < 1e-9, "relerr=%.1e, %.1e" % (e1, e2))

# A5 scaling invariance (Lemma 3.1): M_pm(theta_s g) = e^{pm s/2} M_pm(g); |ghat| invariant
s_sh = 0.3
Mp_sh = float(np.sum(wu*g1u*np.exp(+(uu + s_sh)/2)))   # int g(u-s)e^{u/2}du = int g(v)e^{(v+s)/2}dv
Mm_sh = float(np.sum(wu*g1u*np.exp(-(uu + s_sh)/2)))
prod_inv = abs(Mp_sh*Mm_sh - Mp_cf*Mm_cf)/abs(Mp_cf*Mm_cf)
rtest = np.array([3.7, 14.1, 40.0])
gh0 = np.abs(fourier_basis(ell, 1, rtest)[0])
ghs = np.abs(fourier_basis(ell, 1, rtest)[0]*np.exp(1j*rtest*s_sh))
mod_inv = float(np.max(np.abs(gh0 - ghs)))
check("A5", "scaling invariance: pole product and |ghat| invariant under s=0.3",
      prod_inv < 1e-9 and mod_inv < 1e-14,  # prod tolerance = trapz quadrature error of the M_pm integrals (cf. A4)
      "prod relerr=%.1e, |ghat| diff=%.1e" % (prod_inv, mod_inv))

# A6 modal Plancherel
Phi1 = fourier_basis(ell, 1, RG)
plan = float((1/np.pi)*np.real(np.sum(WG*np.abs(Phi1[0])**2)))  # (1/2pi)*2*int_0^inf
check("A6", "modal Plancherel (1/2pi) int |ghat_1|^2 = 1",
      abs(plan - 1) < 5e-4, "ratio=%.6f" % plan)

# A7 sqrt2 log2
v = 2*Lam(2)/np.sqrt(2)
check("A7", "sqrt(2) log 2 = 2 Lam(2)/sqrt(2) = 0.980258",
      abs(v - np.sqrt(2)*LN2) < 1e-15 and abs(v - 0.980258) < 1e-6, "%.6f" % v)

# A8 rung order
ok8 = (Lam(6) == 0.0 and Lam(2) > 0 and Lam(3) > 0 and Lam(4) > 0 and Lam(5) > 0
       and LN2 < LN3 < np.log(4) < np.log(5) < np.log(6))
check("A8", "Lam(6)=0; rung order log2<log3<log4<log5; control log6", ok8)

# A9 forcing theorem (p-1)(q-1)=p unique prime solution
primes = [p for p in range(2, 98) if all(p % d for d in range(2, int(p**0.5)+1))]
sols = [(p, q) for p in primes for q in primes if (p-1)*(q-1) == p]
check("A9", "(p-1)(q-1)=p unique prime solution (2,3) over primes<=97",
      sols == [(2, 3)], str(sols))

# ======================================================================
# B. Two-sided explicit formula and window lambda_min table
# ======================================================================
progress("block B: zeta zeros (160) -- slowest step")
gammas160 = [float(mp.im(mp.zetazero(k))) for k in range(1, 161)]
gmax = gammas160[-1]

ellB = 1.0; MB = 8
QB, QaB = build_blocks(ellB, MB)
PhiB_g = fourier_basis(ellB, MB, np.array(gammas160))

def two_sided(cvec):
    rhs = float(cvec @ QB @ cvec)
    gh = cvec @ PhiB_g
    lhs = float(2*np.sum(np.abs(gh)**2))
    return lhs, rhs, abs(lhs - rhs)/abs(rhs)

c1 = np.zeros(MB); c1[0] = 1.0
lhs1, rhs1, re1 = two_sided(c1)
check("B1", "explicit formula two-sided, single mode, 160 zeros",
      re1 < 3e-3, "LHS=%.7f RHS=%.7f relerr=%.4f%%" % (lhs1, rhs1, 100*re1))

rng = np.random.default_rng(26); c8 = rng.standard_normal(MB); c8 /= np.linalg.norm(c8)
# use the fixed 8-mode test vector of B.1: alternating-decay profile
c8 = np.array([1.0, -0.6, 0.45, -0.3, 0.22, -0.15, 0.1, -0.07]); c8 /= np.linalg.norm(c8)
lhs8, rhs8, re8 = two_sided(c8)
check("B2", "explicit formula two-sided, 8-mode vector, 160 zeros",
      re8 < 5e-4, "relerr=%.5f%%" % (100*re8))

progress("block B: window lambda_min table")
LAMW, LAMA = {}, {}
for ellw in (0.60, 0.80, 1.00, 1.09, 1.30):
    Q, Qa = build_blocks(ellw, 80)
    LAMW[ellw] = lam_min(Q); LAMA[ellw] = lam_min(Qa)

refW = {0.60: 7.919e-3, 0.80: 1.944e-4, 1.00: 1.865e-6, 1.09: 9.501e-7, 1.30: 2.046e-8}
for cid, ellw in zip(("B3", "B4", "B5", "B6", "B7"), (0.60, 0.80, 1.00, 1.09, 1.30)):
    lw = LAMW[ellw]
    ok = lw > 0 and abs(lw - refW[ellw])/refW[ellw] < 0.25
    check(cid, "lambda_min(Q_W) > 0 at ell=%.2f" % ellw, ok, "%.3e (ref %.3e)" % (lw, refW[ellw]))

check("B8", "lambda_min(Q_arch) < 0 at ell=0.80/1.00/1.09/1.30 (indefinite)",
      all(LAMA[e] < 0 for e in (0.80, 1.00, 1.09, 1.30)),
      "vals=%s" % {e: round(LAMA[e], 4) for e in (0.80, 1.00, 1.09, 1.30)})

# B9 basis convergence at ell=1.00
lamM = [lam_min(build_blocks(1.00, m)[0]) for m in (40, 60, 80)]
ok9 = lamM[0] >= lamM[1] >= lamM[2] > 0 and (lamM[0] - lamM[2])/lamM[2] < 0.05
check("B9", "M=40/60/80 convergence of lambda_min(Q_W) at ell=1.00, monotone",
      ok9, "%.4e -> %.4e -> %.4e" % tuple(lamM))

# B10 quadrature doubling
progress("block B: quadrature doubling")
RG2 = make_grid(0.002, 0.01, 0.1); WPSI2 = trapz_w(RG2)*repsi(RG2)
q1 = lam_min(build_blocks(1.00, 40)[0])
q2 = lam_min(build_blocks(1.00, 40, wpsi=WPSI2, grid=RG2)[0])
check("B10", "quadrature doubling: lambda_min shift small at ell=1.00",
      abs(q1 - q2) < 1e-8, "shift=%.1e" % abs(q1 - q2))

# B11 ell=1.30 boundary case
check("B11", "ell=1.30 hi-res lambda_min(Q_W) positive near floor (~2e-8)",
      0 < LAMW[1.30] < 1e-7, "%.3e" % LAMW[1.30])

# ======================================================================
# C. Tail coercivity, witness constants, leakage (Lemma 4.5', Thm 4.4)
# ======================================================================
progress("block C: coercivity and witness")
ell0 = LN2
_, Qa06 = build_blocks(0.60, 80)
tails = {K: lam_min(Qa06[K:, K:]) for K in (5, 10, 20)}
for cid, K, ref in (("C1", 5, 1.469), ("C2", 10, 2.133), ("C3", 20, 2.808)):
    check(cid, "tail coercivity lambda_min(Q_arch, k>%d) at ell=0.60" % K,
          abs(tails[K] - ref) < 0.02, "%.3f (ref %.3f)" % (tails[K], ref))

R0 = float(mp.findroot(lambda t: float(mp.re(mp.digamma(mp.mpc(0.25, 0.5*t)))) - (LNPI+1.0), 17.0))
check("C4", "witness root R0 of Re psi(1/4+iR/2)=log pi + 1",
      abs(R0 - 17.0819) < 1e-3, "R0=%.4f" % R0)

def cpole_exact(K, ellx, N=2_000_000):
    ks = np.arange(K+1, N+1, dtype=float); a = ks*np.pi/ellx; sg = (-1.0)**ks
    mpv = np.sqrt(2./ellx)*a*(1 - sg*np.exp(+ellx/2))/(a*a + 0.25)
    mmv = np.sqrt(2./ellx)*a*(1 - sg*np.exp(-ellx/2))/(a*a + 0.25)
    ep, em = np.exp(ellx/2), np.exp(-ellx/2)
    avg = 0.5*(((1-ep)**2 + (1-em)**2) + ((1+ep)**2 + (1+em)**2))
    tail = (2./ellx)*avg*(ellx/np.pi)**2*(1.0/N)
    return float(K*(np.sum(mpv**2 + mmv**2) + tail))

def margin(K):
    aK1 = (K+1)*np.pi/ell0; dK = R0**2/aK1**2
    C = 8*R0*ell0/(np.pi**3*(1-dK)**2)
    cl = (LNPI + 1.0 - psi14_cf)*C
    cp = cpole_exact(K, ell0)
    return 1 - (cl + cp)/K, cl, cp

m24, cl24, cp24 = margin(24); m22, _, _ = margin(22); m21, _, _ = margin(21)
ok5 = (abs(m24 - 0.125) < 5e-3 and abs(cl24 - 20.38) < 0.05 and abs(cp24 - 0.631) < 5e-3
       and m22 > 0 and m21 < 0)
check("C5", "witness margin +0.125 at K0=24; min K0=22 (K=21 fails); c_leak=20.38 c_pole=0.631",
      ok5, "m24=%.4f m22=%.4f m21=%.4f cl=%.3f cp=%.4f" % (m24, m22, m21, cl24, cp24))

# C6/G2 measured low-frequency fraction vs truncation
rrlo = np.concatenate([np.linspace(-R0, -1e-6, 4000), np.linspace(1e-6, R0, 4000)])
wlo = trapz_w(rrlo)
frac = {}
for Mtr in (120, 200, 300):
    P = fourier_basis(ell0, Mtr, rrlo)
    L = (1/(2*np.pi))*np.real((P*wlo) @ P.conj().T); L = 0.5*(L + L.T)
    frac[Mtr] = {K: float(np.linalg.eigvalsh(L[K:, K:])[-1]) for K in (24, 36)}
ana = {24: 0.1333, 36: 0.0867}
ok6 = all(frac[m][K] <= ana[K] for m in frac for K in (24, 36)) \
      and abs(frac[120][36] - 0.0152) < 2e-3 and abs(frac[300][24] - 0.0297) < 3e-3
check("C6", "measured low-freq fraction <= analytic bound at truncations 84/164/264",
      ok6, "K36: %.4f/%.4f/%.4f  K24: %.4f/%.4f/%.4f" %
      (frac[120][36], frac[200][36], frac[300][36], frac[120][24], frac[200][24], frac[300][24]))

# C7 closed-form K-invariance + v1.1 truncation artifact reproduction
cp22, cp36 = cpole_exact(22, ell0), cpole_exact(36, ell0)
art24 = 0.632*(1 - 24/120); art36 = 0.632*(1 - 36/120)
ok7 = (abs(cp22 - 0.6308) < 2e-3 and abs(cp24 - 0.6310) < 2e-3 and abs(cp36 - 0.6314) < 2e-3
       and abs(art24 - 0.506) < 5e-3 and abs(art36 - 0.442) < 5e-3)
check("C7", "c_pole closed-form K-invariant (0.631); v1.1 artifact = (1-K/M) factor",
      ok7, "cp(22/24/36)=%.4f/%.4f/%.4f artifacts %.3f/%.3f" % (cp22, cp24, cp36, art24, art36))

# ======================================================================
# D. Section-Certification Gap and prime-channel norm
# ======================================================================
progress("block D: section gap")
Ns = [10**2, 10**3, 10**4, 10**5, 10**6]
HN = [float(np.sum(1.0/np.arange(1, n+1))) for n in Ns]
refH = [5.1874, 7.4855, 9.7876, 12.0901, 14.3927]
check("D1", "harmonic section bounds H_N diverge (N=1e2..1e6)",
      all(abs(a-b) < 1e-3 for a, b in zip(HN, refH)) and all(np.diff(HN) > 0),
      "H=%s" % [round(h, 4) for h in HN])

check("D2", "full-block non-completability: sum n b_n^2 = sum 1/n = H_N -> inf",
      HN[-1] > 14 and HN[-1] - HN[0] > 9, "H_1e6=%.4f" % HN[-1])

z12 = float(mp.zeta(1.2))
part = [float(np.sum(np.arange(1., n+1)**-1.2)) for n in (10**2, 10**3, 10**4)]
check("D3", "convergent control: zeta(1.2)=5.5916, section bounds converge",
      abs(z12 - 5.5916) < 1e-3 and part[0] < part[1] < part[2] < z12,
      "zeta=%.4f partials=%s" % (z12, [round(p, 3) for p in part]))

def prime_gram_norm(ellx, M=80):
    c = np.sqrt(2./ellx); a = np.arange(1, M+1)*np.pi/ellx; tau = LN2
    v = np.linspace(0, ellx - tau, 40001)
    S = ((c*np.sin(np.outer(a, tau + v)))*trapz_w(v)) @ (c*np.sin(np.outer(a, v))).T
    return float(np.linalg.norm(0.5*(S + S.T), 2))
norms = {e: prime_gram_norm(e) for e in (0.80, 1.00, 1.09, 1.30)}
check("D4", "prime-channel Gram spectral norm = 0.5000 (rung 1, all windows)",
      all(abs(n - 0.5) < 1e-3 for n in norms.values()),
      "%s" % {e: round(n, 5) for e, n in norms.items()})

# ======================================================================
# E. Exact-Half Lemma and the refuted sufficient route
# ======================================================================
progress("block E: Exact-Half")
def translation_matrix(ellx, M, tau):
    c = np.sqrt(2./ellx); a = np.arange(1, M+1)*np.pi/ellx
    u = np.linspace(tau, ellx, 40001); wu_ = trapz_w(u)
    return ((c*np.sin(np.outer(a, u)))*wu_) @ (c*np.sin(np.outer(a, u - tau))).T

T60 = translation_matrix(1.09, 60, LN2); T120 = translation_matrix(1.09, 120, LN2)
n2_60 = float(np.linalg.norm(T60 @ T60, 2)); n2_120 = float(np.linalg.norm(T120 @ T120, 2))
check("E1", "2-nilpotency: ||T_log2^2|| -> 0 with basis (ell=1.09 < 2 log 2)",
      n2_120 < n2_60 and n2_120 < 0.1, "M=60: %.4f -> M=120: %.4f" % (n2_60, n2_120))

sym120 = float(np.linalg.norm(0.5*(T120 + T120.T), 2))
check("E2", "Exact-Half: ||Re T_log2|| = 1/2; a priori bound 0.490129",
      abs(sym120 - 0.5) < 2e-3 and abs(np.sqrt(2)*LN2/2 - 0.490129) < 1e-6,
      "||Re T||=%.5f bound=%.6f" % (sym120, np.sqrt(2)*LN2/2))

check("E3", "sufficient route Q_arch >= 0.490 ||g||^2 fails (Q_arch indefinite)",
      all(LAMA[e] < 0 < 0.490129 for e in (0.80, 1.00, 1.09, 1.30)))

# ======================================================================
# F. Douglas criterion consistency, mediation profile, anti-overclaim
# ======================================================================
progress("block F: Douglas consistency")
rngF = np.random.default_rng(437)
def rand_psd(n):
    R = rngF.standard_normal((n, n)); return R @ R.T + 0.1*np.eye(n)

def douglas_norms(A, B, C, epses):
    wA, VA = np.linalg.eigh(A); wC, VC = np.linalg.eigh(C)
    out = []
    for eps in epses:
        Ai = VA @ np.diag((np.maximum(wA, 0)+eps)**-0.5) @ VA.T
        Ci = VC @ np.diag((np.maximum(wC, 0)+eps)**-0.5) @ VC.T
        out.append(float(np.linalg.norm(Ai @ B @ Ci, 2)))
    return out

def mat_sqrt(Mx):
    w, V = np.linalg.eigh(Mx); return V @ np.diag(np.sqrt(np.maximum(w, 0))) @ V.T

A_t, C_t = rand_psd(10), rand_psd(10)
EPSL = [1e-2, 1e-4, 1e-6, 1e-8]
# positive control: B = A^{1/2} K C^{1/2}, ||K|| = 0.9 -> block PSD, all ||K_eps|| <= 1
K_in = rngF.standard_normal((10, 10)); K_in *= 0.9/np.linalg.norm(K_in, 2)
B_ok = mat_sqrt(A_t) @ K_in @ mat_sqrt(C_t)
blk_ok = np.block([[A_t, B_ok], [B_ok.T, C_t]])
pos_ok = lam_min(0.5*(blk_ok + blk_ok.T)) > -1e-10
norms_ok = douglas_norms(A_t, B_ok, C_t, EPSL)
# negative control: ||K|| = 1.5 -> block not PSD, some ||K_eps|| > 1
K_bad = K_in*(1.5/0.9)
B_bad = mat_sqrt(A_t) @ K_bad @ mat_sqrt(C_t)
blk_bad = np.block([[A_t, B_bad], [B_bad.T, C_t]])
neg_bad = lam_min(0.5*(blk_bad + blk_bad.T)) < -1e-8
norms_bad = douglas_norms(A_t, B_bad, C_t, EPSL)
check("F1", "Douglas-Shmulyan consistency: PSD block <=> ||K_eps||<=1 (pos+neg controls)",
      pos_ok and max(norms_ok) <= 1 + 1e-9 and neg_bad and max(norms_bad) > 1,
      "pos max||K||=%.4f  neg max||K||=%.4f" % (max(norms_ok), max(norms_bad)))

# F2/G5/G7 need the rung-1 split blocks (paper section 7.5 / B.I)
progress("block F/G: rung-1 Douglas split")
def rung_split(ellp, MA=40, MB=80, ellb=0.60):
    """Blocks A (base V), B (cross), C (new W) of Q_W on [0,ellp], V from [0,ellb]."""
    cA = np.sqrt(2./ellb); aA = np.arange(1, MA+1)*np.pi/ellb
    cB = np.sqrt(2./ellp); aB = np.arange(1, MB+1)*np.pi/ellp
    v = np.linspace(0, ellb, 30001); wv = trapz_w(v)
    O = ((cA*np.sin(np.outer(aA, v)))*wv) @ (cB*np.sin(np.outer(aB, v))).T
    PhA = fourier_basis(ellb, MA, RG); PhB = fourier_basis(ellp, MB, RG)
    MpA, MmA = pole_functionals(ellb, MA); MpB, MmB = pole_functionals(ellp, MB)
    def arch(P1, Mp1, Mm1, P2, Mp2, Mm2, Ovl):
        ps = (1/np.pi)*np.real((P1*WPSI) @ P2.conj().T)
        return np.outer(Mp1, Mm2) + np.outer(Mm1, Mp2) - LNPI*Ovl + ps
    Quu = arch(PhA, MpA, MmA, PhA, MpA, MmA, np.eye(MA)); Quu = 0.5*(Quu + Quu.T)
    Qww = arch(PhB, MpB, MmB, PhB, MpB, MmB, np.eye(MB)); Qww = 0.5*(Qww + Qww.T)
    Quw = arch(PhA, MpA, MmA, PhB, MpB, MmB, O)
    n = 2
    while np.log(n) < ellp - 1e-12:
        lam = Lam(n)
        if lam > 0:
            tau = np.log(n)
            vv = np.linspace(0, ellp - tau, 40001)
            Pj = cB*np.sin(np.outer(aB, tau + vv)); Pk = cB*np.sin(np.outer(aB, vv))
            S = (Pj*trapz_w(vv)) @ Pk.T
            Qww = Qww - 2*(lam/np.sqrt(n))*0.5*(S + S.T)
            S1 = np.zeros((MA, MB))
            if tau < ellb - 1e-12:
                v1 = np.linspace(0, ellb - tau, 20001)
                S1 = ((cA*np.sin(np.outer(aA, tau + v1)))*trapz_w(v1)) @ (cB*np.sin(np.outer(aB, v1))).T
            ub = min(ellb, ellp - tau)
            v2 = np.linspace(0, ub, 20001)
            S2 = ((cA*np.sin(np.outer(aA, v2)))*trapz_w(v2)) @ (cB*np.sin(np.outer(aB, tau + v2))).T
            Quw = Quw - 2*(lam/np.sqrt(n))*0.5*(S1 + S2)
        n += 1
    Gt = np.eye(MB) - O.T @ O; Gt = 0.5*(Gt + Gt.T)
    lamG, SG = np.linalg.eigh(Gt); keep = lamG > 1e-8
    Tr = SG[:, keep]*(lamG[keep]**-0.5)
    A = Quu
    B = (Quw - Quu @ O) @ Tr
    C = Tr.T @ (Qww - O.T @ Quw - Quw.T @ O + O.T @ Quu @ O) @ Tr; C = 0.5*(C + C.T)
    return A, B, C, int(keep.sum())

ELLC = float(np.log(13.)/2.)
SPLITS = {}
for ellp in (1.09, ELLC):
    A_s, B_s, C_s, rk = rung_split(ellp)
    SPLITS[ellp] = dict(A=A_s, B=B_s, C=C_s, rank=rk,
                        norms=douglas_norms(A_s, B_s, C_s, [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]))

B109 = SPLITS[1.09]["B"]
sv = np.linalg.svd(B109, compute_uv=False)
check("F2", "mediation profile: cross block B nonzero, operator-valued (rank>1)",
      sv[0] > 1e-3 and float(np.sum(sv > 1e-6)) > 1, "top sv=%.4f, sv>1e-6: %d" % (sv[0], int(np.sum(sv > 1e-6))))

check("F3", "anti-overclaim: no RH/GRH/Weil-positivity asserted (all checks are finite compressions)",
      True, "declarative; see paper NC-F26.1/2")

# ======================================================================
# G. v1.2-v1.4 additions: closed forms, bridge, Douglas norms, scan
# ======================================================================
progress("block G: bridge + scan")
check("G1", "c_pole closed-form limit 9*ell0/pi^2 = 0.632 matches exact sums",
      abs(9*ell0/np.pi**2 - 0.632) < 1e-3 and abs(cp36 - 9*ell0/np.pi**2) < 2e-3,
      "limit=%.4f cp36=%.4f" % (9*ell0/np.pi**2, cp36))

mono = all(frac[120][K] < frac[200][K] < frac[300][K] for K in (24, 36))
check("G2", "measured fraction monotone increasing in truncation, bounded by Lemma 4.5'",
      mono and all(frac[m][K] <= ana[K] for m in frac for K in (24, 36)))

# G3 + bridge machinery
GAM6 = [float(mp.im(mp.zetazero(k))) for k in range(1, 7)]
def analyze(ellx, M):
    Q, Qa = build_blocks(ellx, M)
    w_, V_ = np.linalg.eigh(Q); lam = float(w_[0]); cmin = V_[:, 0]
    rs = np.arange(0., 40., 0.002); gh = np.abs(cmin @ fourier_basis(ellx, M, rs))
    mins = [(rs[i], gh[i]) for i in range(1, rs.size-1) if gh[i] < gh[i-1] and gh[i] < gh[i+1]]
    grid = []
    for g in GAM6: grid += [g - 1e-4, g, g + 1e-4]
    vg = cmin @ fourier_basis(ellx, M, np.array(grid))
    rows = []
    for i, g in enumerate(GAM6):
        vm, v0, vp = vg[3*i], vg[3*i+1], vg[3*i+2]
        val = abs(v0); der = abs((vp - vm)/2e-4)
        best = min(mins, key=lambda t: abs(t[0] - g)) if mins else (np.nan, np.nan)
        rows.append(dict(g=g, off=float(best[0] - g), val=float(val),
                         newton=float(val/der) if der > 0 else np.nan))
    return dict(lam=lam, lamA=lam_min(Qa), nmin=len(mins), mins=mins, rows=rows)

lamC3 = {M: analyze(ELLC, M) for M in (40, 60, 80)}
ok_g3 = all(0 < lamC3[M]["lam"] < 1e-7 for M in lamC3) and abs(lamC3[80]["lamA"] + 0.613) < 5e-3
check("G3", "ell=log13/2: lambda_min(Q_W)=+3.7e-8 stable M=40/60/80; Q_arch=-0.613",
      ok_g3, "lamW=%s lamA=%.4f" % (["%.2e" % lamC3[M]["lam"] for M in (40, 60, 80)], lamC3[80]["lamA"]))

AC = lamC3[80]
offs = [r["off"] for r in AC["rows"]]
tolerances = (0.01, 0.01, 0.02, 0.15, 0.35, 0.60)
controls_ok = all(not any(abs(m[0] - cpt) < 0.4 for m, _ in [(mm, 0) for mm in AC["mins"]])
                  for cpt in (17.58, 23.02, 27.72))
ok_g4 = (AC["nmin"] == 6 and all(abs(o) < t for o, t in zip(offs, tolerances)) and controls_ok)
check("G4", "bridge: all 6 local minima of |ghat_min| on [0,40] are gamma_1..6; controls empty",
      ok_g4, "nmin=%d offs=%s" % (AC["nmin"], [round(o, 3) for o in offs]))

okg5 = all(max(SPLITS[e]["norms"]) < 1.0 for e in SPLITS)
check("G5", "regularized Douglas norms ||K_{2,eps}|| < 1 at every eps, both rung windows",
      okg5, "1.09: %s | %.4f: %s" % ([round(n, 6) for n in SPLITS[1.09]["norms"]], ELLC,
                                     [round(n, 6) for n in SPLITS[ELLC]["norms"]]))

bound6 = np.sqrt(AC["lam"]/2)
ok_g6 = all(r["val"] <= bound6*1.001 for r in AC["rows"])
check("G6", "notch bound (Prop 7.10): all six |ghat_min(gamma_k)| <= sqrt(lambda_min/2)",
      ok_g6, "max val=%.2e bound=%.2e" % (max(r["val"] for r in AC["rows"]), bound6))

okg7 = all(all(np.diff(SPLITS[e]["norms"]) > 0) for e in SPLITS)
check("G7", "eps-monotone signature (Lemma 7.8): ||K_eps|| rises as eps->0, never crossing 1",
      okg7 and okg5)

# G8 basis convergence M=80/120/160 at ell_C
progress("block G: basis convergence M=120/160")
conv = {M: analyze(ELLC, M) for M in (80, 120, 160)}
off14_drift = max(abs(conv[80]["rows"][i]["off"] - conv[160]["rows"][i]["off"]) for i in range(4))
off56_drift = max(abs(conv[80]["rows"][i]["off"] - conv[160]["rows"][i]["off"]) for i in (4, 5))
lam_drift = abs(conv[80]["lam"] - conv[160]["lam"])/conv[80]["lam"]
check("G8", "basis convergence: gamma_1-4 offsets stable to 1e-3; gamma_5-6 drift small; quadrature-dominated",
      off14_drift < 5e-3 and off56_drift < 0.02 and lam_drift < 0.1,
      "drift g1-4=%.4f g5-6=%.4f lam=%.1f%%" % (off14_drift, off56_drift, 100*lam_drift))

# G9/G10 ell-scan
progress("block G: ell-scan (8 windows)")
SCAN = {e: analyze(e, 80) for e in (0.60, 0.80, 0.90, 1.00, 1.09, 1.20, ELLC, 1.30)}
pairs = []
for e, a in SCAN.items():
    for r in a["rows"]:
        off = abs(r["off"]); nw = r["newton"]
        if off < 2.0 and nw > 0 and abs(off - nw)/max(nw, 1e-9) < 0.5:
            pairs.append(off/nw)
med = float(np.median(pairs))
check("G9", "Newton law (Prop 7.11): resolved pairs ratio median ~1.04, range within [0.5,1.5]",
      25 <= len(pairs) <= 45 and 0.95 < med < 1.15 and min(pairs) > 0.5 and max(pairs) < 1.5,
      "pairs=%d median=%.3f range=[%.2f,%.2f]" % (len(pairs), med, min(pairs), max(pairs)))

nmins = [SCAN[e]["nmin"] for e in (0.60, 0.80, 0.90, 1.00, 1.09, 1.20, ELLC, 1.30)]
base = SCAN[0.60]
base_g1 = abs(base["rows"][0]["off"]) < 1.5
base_loose = all(abs(base["rows"][i]["off"]) > 0.3 for i in (1, 2))
check("G10", "resolution count monotone 3->6 with margin collapse; sub-rung control loose",
      all(np.diff(nmins) >= 0) and nmins[0] <= 4 and nmins[-1] == 6 and base_g1 and base_loose,
      "counts=%s base offs=%s" % (nmins, [round(base["rows"][i]["off"], 2) for i in range(3)]))

# ======================================================================
# tally
# ======================================================================
npass = sum(1 for r in RESULTS if r["ok"]); ntot = len(RESULTS)
print("\n" + "="*72)
print("ZS-F26 v1.4 verification: %d/%d PASS  (%.0f s)" % (npass, ntot, time.time() - T0))
print("NO CLAIM on RH / GRH; Gate D5 remains IMPORTED-OPEN == RH.")
print("="*72)
json.dump(dict(npass=npass, ntot=ntot, results=RESULTS),
          open("zs_f26_verify_v1_4_results.json", "w"), indent=1)
sys.exit(0 if npass == ntot else 1)
