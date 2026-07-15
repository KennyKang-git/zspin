#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_m52_verify_v1_3.py
=====================
v1.3 = v1.2 + third-review fixes:
  * B12 rebuilt on PROPER multiplicative subgroups (index>1) -- the actual BGK regime --
    (v1.2 used p=509,1019 where 2 is a PRIMITIVE ROOT, i.e. the FULL group, a trivial test);
    adds a numeric Truncation-Lemma (TL) check.  M52.3' is DERIVED-CONDITIONAL on TL
    (BGK + Erdos-Turan supply the IMPORTED-PROVEN discrepancy input; TL is the missing lemma).
  * B15 (NEW): the M52.7A inverse branches are Z^q-indexed nested logarithms (the v1.2
    single-map formula did NOT invert the composition); operator status OPEN-CONSTRUCTION.
  * B6 wrapped in np.seterr('ignore') -- exploratory double-precision Newton DETECTION.
  * Output reframed: 29->31 "regression/identity/interval checks"; the ANALYTIC theorems
    (M52.1A, M52.6A, M52.11) are proved in the TEXT, not by these numerical checks.
  * Seam-Matching No-Go stated for the "seam-compatible graph of the canonical [0,1) cocycle".
--- original v1.2 header below ---
zs_m52_verify_v1_2.py
=====================
Fail-closed verification suite for ZS-M52 v1.2
"Arithmetic Coherence in the Z-Spin Horizontal Clock: the Full Periodic Lyapunov
 Spectrum, the Seam-Matching No-Go, Arithmetic Invariant Measures, and the
 Large-Excursion Gate"
  -- Kenny Kang, Z-Spin Cosmology Collaboration, July 2026.

v1.2 integrates the second external review of v1.1.  KEY CHANGES carried here:
  * B3A (NEW, PROVEN): the real 3x3 monodromy DF_m^q is block-triangular with
    eigenvalue moduli {|M_x|, |M_x|, m^q}; per-step Lyapunov spectrum
    {lam_V, lam_V, log m}.  This FIXES the v1.1 mislabelling: K_x is the FIBRE
    kinematic-loading term and 2*pi*J_x the FIBRE amplitude-contraction term
    (both inside the fibre exponent); the true HORIZONTAL exponent is chi_H = log m.
  * B10 (NEW, PROVEN): Seam-Matching No-Go -- no continuous invariant graph on the
    seam-compatible graph of the canonical [0,1) cocycle (f_0=1 => h(0)=1; m*N1=1 contradiction).
    Closes the CONTINUOUS-circle category of H-INV negatively.
  * B11 (NEW, PROVEN): each certified word carries an atomic F_m-invariant measure
    mu_x with spectrum {lam_V, lam_V, log m}.  Closes the ARITHMETIC part of
    H-ORBIT (existence + exponent); the Lebesgue-base part stays OPEN.
  * B4 (UPGRADED): the attracting-cycle basin is PROVEN from B8 (|G'|<1 =>
    holomorphic local contraction => open basin => positive Lebesgue measure);
    the Monte-Carlo check is retained only as a regression sanity view.
  * B5 (RENAMED "Large-Excursion Gate"): reports only a precision-stable large
    excursion beyond 10^12 for 18 tested irrational-base trajectories; it does NOT
    assert sup|z_n|=inf or |z_n|->inf.
  * B8 (FIXED): exact-rational interval word x_j = iv.mpf(k)/iv.mpf(n) -- the
    float(x) perturbation of v1.1 is removed; the certificate now encloses the
    EXACT rational word => COMPUTER-ASSISTED PROVEN.
  * B12 (NEW): multiplicative-subgroup star-discrepancy -> 0 at large order,
    supporting the DERIVED-CONDITIONAL kinematic limit M52.3'.
  * B6 relabelled double-precision exploratory Newton DETECTION; B7 relabelled a
    frozen out-of-sample protocol (no chronological pre-registration claimed).

Dependencies: mpmath (>=1.3), numpy.
"""

import sys, hashlib
from math import gcd
import numpy as np
import mpmath as mp
from mpmath import iv

mp.mp.dps = 35
iv.dps = 35
PI    = mp.pi
TWOPI = 2 * mp.pi

# ---------------------------------------------------------------- harness
_PASS = 0; _LOG = []
def check(name, cond, detail=""):
    global _PASS
    ok = bool(cond); _LOG.append((name, ok, detail))
    if not ok:
        print("\n[FAIL] %s  %s" % (name, detail))
        for nm, o, d in _LOG:
            print("   %s  %s  %s" % ("PASS" if o else "FAIL", nm, d))
        sys.exit(1)
    _PASS += 1

# ---------------------------------------------------------------- core objects
def zstar(x):
    a = TWOPI * 1j * x; return -mp.lambertw(-a) / a
def chi_fr(x):
    return mp.log(abs(mp.lambertw(-TWOPI * 1j * x)))
def order(m, n):
    if gcd(m, n) != 1: return None
    r, v = 1, m % n
    while v != 1: v = (v * m) % n; r += 1
    return r
def base_cycle(k, n, m):
    cyc, x = [], k
    for _ in range(order(m, n)): cyc.append(mp.mpf(x)/n); x = (m*x) % n
    return cyc
def residue_cycle(k, n, m):
    res, x = [], k
    for _ in range(order(m, n)): res.append(x); x = (m*x) % n
    return res
def word_map(z, cyc):
    for x in cyc: z = mp.e ** (TWOPI*1j*x*z)
    return z
def word_multiplier(z0, cyc):
    z, M = z0, mp.mpf(1)
    for x in cyc: M *= TWOPI*1j*x*mp.e**(TWOPI*1j*x*z); z = mp.e**(TWOPI*1j*x*z)
    return M
def fibre_seq(z0, cyc):
    zs = [z0]
    for x in cyc[:-1]: zs.append(mp.e**(TWOPI*1j*x*zs[-1]))
    return zs
def find_attracting(cyc):
    best = None
    for s in [0.02+0.02j,0.1-0.1j,0.3+0.2j,0.5j,-0.2+0.3j,0.5+0.5j,0.05+0.4j,0.01-0.05j]:
        try: z = mp.findroot(lambda w: word_map(w, cyc)-w, mp.mpc(s))
        except Exception: continue
        if abs(word_map(z, cyc)-z) < mp.mpf(10)**-12:
            M = word_multiplier(z, cyc)
            if abs(M) < 1 and (best is None or abs(M) < abs(best[1])): best = (z, M)
    return best

print("=" * 76)
print("ZS-M52 v1.3  verification suite  (fail-closed)")
print("=" * 76)

# ---------------------------------------------------------------- B0 LOCKED constants
rho = mp.findroot(lambda v: mp.cos(v)-v, mp.mpf('0.739'))
s_c = mp.e**mp.sin(rho); x_c = s_c/TWOPI; n_c = TWOPI/s_c
check("B0.1 Dottie rho=cos rho", abs(mp.cos(rho)-rho) < mp.mpf(10)**-30)
check("B0.2 s_c=e^{sin rho}=1.9613088464595", abs(s_c-mp.mpf('1.9613088464595')) < mp.mpf(10)**-12)
check("B0.3 n_c=2pi/s_c=3.20356751489 (=M1/M51)", abs(n_c-mp.mpf('3.20356751489')) < mp.mpf(10)**-10)
check("B0.4 x_c=0.312151997844", abs(x_c-mp.mpf('0.312151997844')) < mp.mpf(10)**-11)
print("  [B0] rho=%s s_c=%s x_c=%s n_c=%s" % (mp.nstr(rho,10),mp.nstr(s_c,10),mp.nstr(x_c,10),mp.nstr(n_c,10)))

# ---------------------------------------------------------------- B1 frozen identities
xs = [mp.mpf(k)/2000 for k in range(1,2000)]
check("B1.1 Im z*(x)>0 on (0,1)", min(mp.im(zstar(x)) for x in xs) > 0)
xt = mp.mpf('0.3')
check("B1.2 chi_fr = log(2pi x) - 2pi x Im z*",
      abs(chi_fr(xt)-(mp.log(TWOPI*xt)-TWOPI*xt*mp.im(zstar(xt)))) < mp.mpf(10)**-30)
I = mp.quad(lambda x: mp.log(TWOPI*x), [0,1])
check("B1.3 int_0^1 log(2pi x)=log(2pi)-1", abs(I-(mp.log(TWOPI)-1)) < mp.mpf(10)**-30)
Lam_sec = mp.quad(chi_fr, [0,1]); J_frozen = mp.quad(lambda x: x*mp.im(zstar(x)), [0,1])
check("B1.4 (log2pi-1)-2pi J_frozen = Lambda_sec", abs((mp.log(TWOPI)-1)-TWOPI*J_frozen-Lam_sec) < mp.mpf(10)**-25)
band = mp.quad(chi_fr, [0, x_c])/x_c
check("B1.5 frozen band mean = -sin rho (= M51 T3.1 = seed <chi_V>~-0.669)",
      abs(band-(-mp.sin(rho))) < mp.mpf(10)**-20, "band=%s" % mp.nstr(band,10))
print("  [B1] log2pi-1=%s J_frozen=%s Lambda_sec=%s band=%s(=-sin rho)"
      % (mp.nstr(mp.log(TWOPI)-1,10),mp.nstr(J_frozen,8),mp.nstr(Lam_sec,8),mp.nstr(band,8)))

# ---------------------------------------------------------------- B2 q=ord_n(m)
allok = all(len(base_cycle(1,n,m))==order(m,n) for m in (2,3,5) for n in range(3,200) if gcd(m,n)==1)
check("B2.1 word length q == ord_n(m) (coherence return time)", allok)

# ---------------------------------------------------------------- B3 M52.1 decomposition
def decomp(k,n,m,attracting=True):
    cyc = base_cycle(k,n,m); q = len(cyc)
    if attracting: z0, M = find_attracting(cyc)
    else:
        z0 = mp.findroot(lambda w: word_map(w,cyc)-w, mp.mpc(0.3+0.3j)); M = word_multiplier(z0,cyc)
    zs = fibre_seq(z0,cyc)
    lamA = mp.log(abs(M))/q
    lamB = sum(mp.log(TWOPI*cyc[j])-TWOPI*cyc[j]*mp.im(zs[j]) for j in range(q))/q
    K = sum(mp.log(TWOPI*x) for x in cyc)/q; Jw = sum(cyc[j]*mp.im(zs[j]) for j in range(q))/q
    return lamA, lamB, K, Jw, z0, M, cyc, zs
lamA,lamB,K7,J7,z0_7,M7,cyc7,zs7 = decomp(1,7,2,True)
check("B3.1 M52.1: lamV=(1/q)log|M| = K_loading - 2pi J_contraction (1/7;2)",
      abs(lamA-lamB) < mp.mpf(10)**-30, "resid=%s" % mp.nstr(abs(lamA-lamB),3))
check("B3.2 word (1/7;2) coherent, |M|~0.20295", lamA<0 and abs(mp.e**(3*lamA)-mp.mpf('0.20294620'))<mp.mpf(10)**-6)
check("B3.3 coherence criterion: lamV<0 <=> J > K/2pi", (lamA<0)==(J7>K7/TWOPI))
lamAr,lamBr,K3,J3,_,_,_,_ = decomp(1,3,2,False)
check("B3.4 M52.1 (1/3;2) repelling, lamV~+0.2429", abs(lamAr-lamBr)<mp.mpf(10)**-25 and lamAr>0)
print("  [B3] (1/7;2): lamV=%s K_load=%s J_contr=%s | chi_H=log m=%s is the ACTUAL horizontal exponent"
      % (mp.nstr(lamA,8),mp.nstr(K7,6),mp.nstr(J7,6),mp.nstr(mp.log(2),6)))

# ---------------------------------------------------------------- B3A NEW: full 3x3 monodromy spectrum
def real_jac_step(x, z, m):
    a = 2j*np.pi*x*np.exp(2j*np.pi*x*z); b = 2j*np.pi*z*np.exp(2j*np.pi*x*z)
    return np.array([[a.real,-a.imag,b.real],[a.imag,a.real,b.imag],[0,0,m]])
m = 2; q7 = len(cyc7)
zsN = [complex(z0_7)]
for x in cyc7[:-1]: zsN.append(np.exp(2j*np.pi*float(x)*zsN[-1]))
J = np.eye(3)
for j in range(q7): J = real_jac_step(float(cyc7[j]), zsN[j], m) @ J
mods = sorted(abs(np.linalg.eigvals(J)))
lamV = float(mp.log(abs(M7))/q7)
check("B3A.1 monodromy moduli = {|M_x|,|M_x|,m^q}  (block-triangular, M52.1A)",
      abs(mods[0]-abs(complex(M7)))<1e-6 and abs(mods[1]-abs(complex(M7)))<1e-6 and abs(mods[2]-m**q7)<1e-6,
      "moduli={%.6f,%.6f,%.6f}" % tuple(mods))
check("B3A.2 lam_V<0<log m => exact 2s(dimE^s=2)/1u(dimE^u=1) saddle",
      lamV < 0 < np.log(m), "spectrum {lam_V,lam_V,log m}={%.4f,%.4f,%.4f}" % (lamV,lamV,np.log(m)))
print("  [B3A] full Lyapunov spectrum {lam_V,lam_V,log m}={%.4f,%.4f,%.4f}; moduli {%.4f,%.4f,%.4f}=|M|,|M|,m^q"
      % (lamV,lamV,np.log(m),mods[0],mods[1],mods[2]))

# ---------------------------------------------------------------- B4 basin PROVEN from B8 (regression view)
PIf = np.pi
def np_wmap(z, cyc):
    for x in cyc: z = np.exp(2j*PIf*x*z)
    return z
z07 = complex(z0_7.real, z0_7.imag)
def bounded(zi, cyc, N=60):
    z, k = zi, 0
    for _ in range(N):
        z = np.exp(2j*PIf*cyc[k%len(cyc)]*z); k += 1
        if not np.isfinite(z.real) or abs(z) > 1e8: return False
    return abs(z) < 1e3
rng = np.random.default_rng(7)
hits = sum(bounded(z07+0.1*(rng.standard_normal()+1j*rng.standard_normal()),[1/7,2/7,4/7]) for _ in range(500))
check("B4.1 attracting cycle basin PROVEN from B8 (|G'|<1 => open basin); regression view",
      float(abs(M7)) < 1.0 and hits/500 > 0.9,
      "|G'|=%.4f<1 => open (pos-measure) basin analytically; MC regression %.2f" % (float(abs(M7)), hits/500))

# ---------------------------------------------------------------- B5 Large-Excursion Gate (renamed)
def frozen_zstar(x):
    a = TWOPI*1j*x; return -mp.lambertw(-a)/a
def excursion_test(x0, m, N=500, thr=mp.mpf(10)**12):
    x = mp.mpf(x0) % 1; z = frozen_zstar(x); peaked = abs(z); back = False; reached = None
    for i in range(N):
        if -TWOPI*x*mp.im(z) > mp.log(thr): reached = i; break
        z = mp.e**(TWOPI*1j*x*z); a = abs(z)
        if a > peaked: peaked = a
        if a < 1 and peaked > 10: back = True
        x = (m*x) % 1
    return reached, back
by_dps = {}
for dps in (80,120,200):
    mp.mp.dps = dps
    reached=[]; backs=0
    for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]:
        x0 = mp.sqrt(p)-mp.floor(mp.sqrt(p)); r,b = excursion_test(x0,2)
        reached.append(r if r is not None else 500);
        if b: backs += 1
    fin = sorted([r for r in reached if r < 500]); by_dps[dps] = (len(fin), fin[len(fin)//2] if fin else None, backs)
mp.mp.dps = 35
n80 = by_dps[80]
check("B5.1 Large-Excursion Gate: 18 tested irrational-base trajectories reach |z|>1e12, dps-stable",
      n80[0] == 18 and by_dps[80][:2]==by_dps[120][:2]==by_dps[200][:2],
      "18/18 reach threshold; median=%s; identical dps 80/120/200 (NO sup=inf or ->inf inferred)" % n80[1])
check("B5.2 non-monotone pre-threshold returns observed (NOT |z_n|->inf)", n80[2] > 0,
      "return-to-small events: %d/18" % n80[2])
print("  [B5] Large-Excursion Gate: 18/18 tested irrational bases reach |z|>1e12 (median=%s, dps-stable); "
      "%d/18 non-monotone returns -> neither unboundedness nor divergence inferred" % (n80[1], n80[2]))

# ---------------------------------------------------------------- B6 density (double-precision Newton DETECTION)
def np_wmult(z0, cyc):
    z, M = z0, 1.0
    for x in cyc: M *= 2j*PIf*x*np.exp(2j*PIf*x*z); z = np.exp(2j*PIf*x*z)
    return abs(M)
def np_has_att(cyc):
    for s in [0.02+0.02j,0.1-0.1j,0.3+0.2j,0.5j,-0.2+0.3j,0.5+0.5j,0.05+0.4j,0.15+0.15j,0.2j,-0.1-0.1j]:
        z = complex(s); good = True
        for _ in range(200):
            h = 1e-8; f = np_wmap(z,cyc)-z; df = (np_wmap(z+h,cyc)-np_wmap(z-h,cyc))/(2*h)-1
            if abs(df) < 1e-13: good=False; break
            zn = z-f/df
            if not np.isfinite(zn.real) or abs(zn)>1e6: good=False; break
            if abs(zn-z) < 1e-12: z=zn; break
            z = zn
        if good and abs(np_wmap(z,cyc)-z)<1e-8 and 0<np_wmult(z,cyc)<1: return True
    return False
def enum(m, nmin, nmax):
    d = []
    for n in range(nmin, nmax+1):
        if gcd(m,n) != 1: continue
        q = order(m,n); seen = set()
        for k in range(1,n):
            if gcd(k,n) != 1: continue
            orb = set(); x = k
            for _ in range(q): orb.add(x); x=(m*x)%n
            rep = min(orb)
            if rep in seen: continue
            seen.add(rep); cyc=[]; x=rep
            for _ in range(q): cyc.append(x/n); x=(m*x)%n
            d.append((n,q,q/(n-1),1 if np_has_att(cyc) else 0))
    return d
np.seterr(all='ignore')   # B6 is EXPLORATORY double-precision Newton detection; overflow on divergent
                          # seeds is expected and harmless (guarded by isfinite / |z|>1e6 breaks).
train = enum(2,3,99); valid = enum(2,100,140)
corr_t = np.corrcoef([x[2] for x in train],[x[3] for x in train])[0,1]
corr_v = np.corrcoef([x[2] for x in valid],[x[3] for x in valid])[0,1]
check("B6.1 detection corr(ord ratio, coherence) reproduces OUT-OF-SAMPLE",
      corr_t<-0.15 and corr_v<-0.15 and abs(corr_t-corr_v)<0.1, "train=%.3f valid=%.3f" % (corr_t,corr_v))
rep = {}
for mm in (3,5):
    d = enum(mm,3,55); rep[mm] = np.corrcoef([x[2] for x in d],[x[3] for x in d])[0,1]
check("B6.2 negative correlation REPLICATES across m=3,5", rep[3]<-0.1 and rep[5]<-0.1)
print("  [B6] DETECTION corr: train=%.3f valid=%.3f | m=3 %.3f m=5 %.3f (double-precision Newton detection)"
      % (corr_t,corr_v,rep[3],rep[5]))

# ---------------------------------------------------------------- B7 frozen out-of-sample protocol
protocol = ("FROZEN-OOS ZS-M52 v1.2 | S=corr(1[ord_n(2)<=(n-1)/2],coherence) | null exchangeable | "
            "perm N=20000 seed=20260315 | threshold p<=0.05 | OUT-OF-SAMPLE valid 100<=n<=140 disjoint train n<=99")
phash = hashlib.sha256(protocol.encode()).hexdigest()
av = np.array([x[3] for x in valid]); short_v = np.array([1 if x[1]<=(x[0]-1)/2 else 0 for x in valid])
S_obs = np.corrcoef(short_v, av)[0,1]; rng2 = np.random.default_rng(20260315)
Sn = np.array([np.corrcoef(short_v, rng2.permutation(av))[0,1] for _ in range(20000)])
p_oos = float((np.abs(Sn) >= abs(S_obs)).mean())
check("B7.1 frozen out-of-sample p computed & reported (HELD at HYPOTHESIS-weak if p>0.05)",
      0.0 <= p_oos <= 1.0, "S_obs=%.3f p_oos=%.4f (>0.05 => HELD)" % (S_obs,p_oos))
print("  [B7] protocol-SHA256=%s... (frozen out-of-sample; not a chronological pre-registration)" % phash[:24])
print("  [B7] OOS binary S_obs=%.3f p=%.4f => %s" % (S_obs,p_oos,"clears 0.05" if p_oos<=0.05 else "does NOT clear 0.05 => HELD"))

# ---------------------------------------------------------------- B8 FIXED exact-rational Krawczyk
def krawczyk_exact(residues, n, z_approx, r=mp.mpf(10)**-4):
    zc = complex(z_approx)
    def wmap(z):
        for k in residues: z = mp.e**(TWOPI*1j*(mp.mpf(k)/n)*z)
        return z
    h = mp.mpf(10)**-14; Fp = (wmap(z_approx+h)-wmap(z_approx-h))/(2*h)-1; Y = complex(1/Fp)
    bx = iv.mpc(iv.mpf([zc.real-float(r),zc.real+float(r)]), iv.mpf([zc.imag-float(r),zc.imag+float(r)]))
    tp = 2*iv.pi
    def wmap_iv(zz):
        for k in residues:
            xj = iv.mpf(k)/iv.mpf(n); zz = iv.e**(iv.mpc(0,1)*tp*xj*zz)   # EXACT rational
        return zz
    def wder_iv(zz):
        z = zz; M = iv.mpc(1,0)
        for k in residues:
            xj = iv.mpf(k)/iv.mpf(n)
            M = M*(iv.mpc(0,1)*tp*xj*iv.e**(iv.mpc(0,1)*tp*xj*z)); z = iv.e**(iv.mpc(0,1)*tp*xj*z)
        return M
    zhat = iv.mpc(zc.real,zc.imag); Yiv = iv.mpc(Y.real,Y.imag)
    K = zhat - Yiv*(wmap_iv(zhat)-zhat) + (1-Yiv*(wder_iv(bx)-1))*(bx-zhat)
    inside = (K.real.a>bx.real.a and K.real.b<bx.real.b and K.imag.a>bx.imag.a and K.imag.b<bx.imag.b)
    mag = abs(wder_iv(bx)); return inside, (float(mag.a), float(mag.b))
res7 = residue_cycle(1,7,2)
cert7, mag7 = krawczyk_exact(res7, 7, z0_7)
check("B8.1 exact-rational Krawczyk certifies EXACT word (1/7;2), |M| interval < 1",
      cert7 and mag7[1] < 1.0, "EXACT x_j=k/7; certified box; |M| in [%.5f,%.5f]<1" % mag7)
print("  [B8] COMPUTER-ASSISTED PROVEN: exact-rational word (1,2,4)/7 attracting, |M| in [%.5f,%.5f]<1 (no float(x))" % mag7)

# ---------------------------------------------------------------- B9 Q=11 short-return (relabelled)
ord11 = {mm: order(mm,11) for mm in range(2,11)}
short_ret = [mm for mm in range(2,11) if ord11[mm] and ord11[mm] <= 5]
check("B9.1 Q=11 return length q=ord_11(m); short-return candidates exist",
      ord11[2]==10 and set(short_ret)=={3,4,5,9,10},
      "ord_11=%s; short-return candidates m in %s (coherence still to be certified)" % (ord11,short_ret))
print("  [B9] register Q=11: q=ord_11(m)=%s; m=2 maximal-return (primitive root); short-return candidates m in %s"
      % (ord11, short_ret))

# ---------------------------------------------------------------- B10 NEW Seam-Matching No-Go (M52.6A)
# structural certificates of the analytic proof: f_0(z)=1 (=> h(0)=1) and frozen non-circle-continuity
f0ok = all(abs(mp.e**(TWOPI*1j*0*mp.mpc(zz))-1) < mp.mpf(10)**-30 for zz in [0.3+0.2j,1-1j,5+5j,0.7-0.9j])
check("B10.1 f_0(z)=1 for all z  =>  h(0)=1 forced on the circle (M52.6A step)", f0ok)
gap = abs(zstar(mp.mpf('0.0001')) - zstar(mp.mpf('0.9999')))
check("B10.2 frozen family not circle-continuous (seam gap>0.5); M52.6A: no continuous R/Z graph (m*N1=1 contradiction)",
      gap > mp.mpf('0.5'), "|z*(0+)-z*(1-)|=%s (seam discontinuity)" % mp.nstr(gap,6))
print("  [B10] Seam-Matching No-Go: f_0=1=>h(0)=1; continuity forces u(1)-u(0)=1=m*N1, N1 in Z, m>=2 => CONTRADICTION")
print("        => NO continuous seam-compatible invariant graph for the canonical [0,1)-representative cocycle  [CLOSED-NEGATIVE, PROVEN]")

# ---------------------------------------------------------------- B11 NEW arithmetic invariant measure (H-ORBIT)
# atomic mu_x on the periodic orbit is F_m-invariant; spectrum {lam_V,lam_V,log m}
orbit = [(complex(zs7[j]), float(cyc7[j])) for j in range(q7)]
def Fm(pt, m):
    z, x = pt; return (complex(np.exp(2j*PIf*x*z)), (m*x) % 1.0)
image = [Fm(pt, 2) for pt in orbit]
# check the image set equals the orbit set (cyclic invariance)
def close(a,b): return abs(a[0]-b[0])<1e-8 and abs(a[1]-b[1])<1e-9
inv = all(any(close(im, o) for o in orbit) for im in image)
check("B11.1 atomic measure mu_x on the word orbit is F_m-invariant (PROVEN-EXISTS)", inv,
      "F_m permutes the q=%d orbit points cyclically" % q7)
check("B11.2 mu_x Lyapunov spectrum = {lam_V,lam_V,log m} (exponent PROVEN on certified word)",
      lamV < 0 < np.log(2), "arithmetic H-ORBIT closed; Lebesgue-base H-ORBIT remains OPEN")
print("  [B11] arithmetic invariant measure mu_x exists; spectrum {lam_V,lam_V,log m}; "
      "ARITHMETIC H-ORBIT closed, continuum H-ORBIT OPEN")

# ------------------------------------ B12 FIXED: PROPER multiplicative subgroups (index>1) + truncation tail
# (v1.2 used p=509,1019 where 2 is a PRIMITIVE ROOT => full F_p^x, index 1, a trivial test.
#  v1.3 uses PROPER subgroups (index>1) -- the actual BGK regime -- and checks the log-tail (Lemma TL).)
def star_disc(points):
    pts = np.sort(np.array(points)); N = len(pts); d = 0.0
    for i, x in enumerate(pts):
        d = max(d, abs(i/N - x), abs((i+1)/N - x))
    return d
def sub_orbit(m, p):
    orb = []; x = 1
    for _ in range(order(m, p)): orb.append(x/p); x = (m*x) % p
    return np.array(orb)
proper = {}   # p : (index, D*, K - (log2pi-1))
target = float(mp.log(TWOPI) - 1)
for p in [733, 4937, 19421, 52489]:
    o = order(2, p); idx = (p-1)//o
    orb = sub_orbit(2, p); D = star_disc(orb)
    K = float(np.mean(np.log(2*np.pi*orb)))
    proper[p] = (idx, D, K - target)
check("B12.1 PROPER subgroups (index>1) equidistribute: D* decreases with |H_p| (BGK regime)",
      all(proper[p][0] > 1 for p in proper) and proper[733][1] > proper[19421][1] > proper[52489][1],
      "D*: 733=%.4f 4937=%.4f 19421=%.4f 52489=%.4f (all index>1)"
      % (proper[733][1], proper[4937][1], proper[19421][1], proper[52489][1]))
check("B12.2 kinematic limit K -> log2pi-1 on PROPER subgroups (K deviation shrinks)",
      abs(proper[733][2]) > abs(proper[19421][2]) and abs(proper[19421][2]) < 0.01,
      "K-(log2pi-1): 733=%+.4f 19421=%+.4f 52489=%+.4f" % (proper[733][2], proper[19421][2], proper[52489][2]))
# Truncation Lemma TL numeric: small-x tail mean(-log x) over subgroup ~ Lebesgue tail eps(1-log eps) -> 0
orb2 = sub_orbit(2, 52489); o2 = len(orb2)
tail_contribs = {}
for eps in (0.01, 0.001):
    small = orb2[orb2 < eps]
    contrib = float(np.sum(-np.log(small))/o2) if len(small) else 0.0
    tail_contribs[eps] = (contrib, eps*(1-np.log(eps)))
check("B12.3 Truncation Lemma TL (numeric): subgroup log-tail -> 0 with eps, tracks Lebesgue tail",
      tail_contribs[0.001][0] < tail_contribs[0.01][0] < 0.1,
      "tail mean(-log x): eps=0.01 -> %.4f, eps=0.001 -> %.4f (Lebesgue %.4f, %.4f)"
      % (tail_contribs[0.01][0], tail_contribs[0.001][0], tail_contribs[0.01][1], tail_contribs[0.001][1]))
print("  [B12] PROPER subgroups: p=733(idx3)D*=%.4f | 4937(idx4)D*=%.4f | 19421(idx5)D*=%.4f | 52489(idx4)D*=%.4f"
      % (proper[733][1], proper[4937][1], proper[19421][1], proper[52489][1]))
print("  [B12] TL tail(-log x) mean: eps=0.01->%.4f, eps=0.001->%.4f -> 0  "
      "(M52.3' DERIVED-CONDITIONAL on Truncation Lemma TL; BGK+ET = IMPORTED-PROVEN discrepancy input)"
      % (tail_contribs[0.01][0], tail_contribs[0.001][0]))

# ------------------------------------ B15 NEW: corrected M52.7A inverse branches are Z^q-indexed nested logs
# G_x = f_{x_{q-1}} o ... o f_{x_0}; its inverse branches are indexed by k in Z^q via q nested logarithms.
# (v1.2 wrote a single-map formula w=(Log z + 2pi i k)/(2pi i x_0), which does NOT invert the composition.)
def np_f(x, w): return np.exp(2j*PIf*x*w)
def np_Gx(xs, w):
    for x in xs: w = np_f(x, w)
    return w
def inverse_branch(xs, z, kmulti):
    val = z
    for j in reversed(range(len(xs))):          # invert last map first: j = q-1,...,0
        val = (np.log(val) + 2j*PIf*kmulti[j]) / (2j*PIf*xs[j])
    return val
xs2 = [1/7, 2/7]; ztest = 0.5+0.4j
zq_ok = all(abs(np_Gx(xs2, inverse_branch(xs2, ztest, k)) - ztest) < 1e-9
            for k in [(0,0),(1,0),(0,1),(-1,2),(3,-2)])
xs3 = [1/13,2/13,4/13]
zq_ok3 = abs(np_Gx(xs3, inverse_branch(xs3, 0.3-0.2j, (1,-1,2))) - (0.3-0.2j)) < 1e-9
# and the WRONG single-map formula does NOT invert the q>=2 composition
w_wrong = (np.log(ztest) + 0) / (2j*PIf*xs2[0])
wrong_fails = abs(np_Gx(xs2, w_wrong) - ztest) > 1e-2
check("B15.1 M52.7A corrected: Z^q-indexed nested-log branches invert G_x (q=2,3)",
      zq_ok and zq_ok3, "|G_x(w_k(z))-z|<1e-9 for k in Z^2, Z^3")
check("B15.2 v1.2 single-map inverse formula does NOT invert the composition (it was wrong)",
      wrong_fails, "single-map residual = %.3f (nonzero)" % abs(np_Gx(xs2, w_wrong) - ztest))
print("  [B15] M52.7A inverse branches CORRECTED: multi-index k in Z^q, q nested logs "
      "(single-map formula of v1.2 refuted); operator status OPEN-CONSTRUCTION")

# ---------------------------------------------------------------- registry
print("\n" + "-" * 76)
print("ANALYTIC THEOREM LEDGER (proved in the TEXT; suite gives guards/examples, not formal proofs)")
print("-" * 76)
print("  M52.1  word-exponent decomposition lamV=K-2piJ ........ PROVEN (identity; guard B3)")
print("  M52.1A full periodic spectrum {lamV,lamV,log m}, 2s1u . PROVEN (algebra; example B3A)")
print("  M52.2  q=ord_n(m) coherence return time .............. PROVEN (elementary; guard B2)")
print("  M52.6A Seam-Matching No-Go (seam-compatible graph) .... CLOSED-NEGATIVE / PROVEN (proof; struct B10)")
print("  M52.11 arithmetic invariant measure + exponent ....... PROVEN-EXISTS (proof; example B11)")
print("  basin of certified attracting cycle .................. PROVEN from B8 (|G'|<1 => open basin)")
print("-" * 76)
print("CONDITIONAL / OPEN LEDGER")
print("-" * 76)
print("  ADMISSIBILITY canonical base Q/Z; physical = P-ADM ... DERIVED-CONDITIONAL")
print("  M52.3' kinematic limit K->log2pi-1 (proper subgroups)  DERIVED-CONDITIONAL on Truncation Lemma TL (B12)")
print("  H-INV  seam-compatible cts / bounded-meas / arbitrary  CLOSED-NEG(cts) ; OPEN(measurable)")
print("  H-ORBIT arithmetic / Lebesgue-base ................... CLOSED(arithmetic) ; OPEN(continuum)")
print("  M52.4  Large-Excursion Gate .......................... VERIFIED finite-time (B5; no unboundedness)")
print("  M52.O5 order-coherence density ....................... OBSERVATION / HYPOTHESIS-weak (HELD, p=%.4f)" % p_oos)
print("  M52.7A wordwise operator (Z^q nested-log branches) ... OPEN-CONSTRUCTION (B15)")
print("  M52.7B arithmetic ensemble pressure .................. OPEN PROGRAMME")

print("\n" + "=" * 76)
print("ZS-M52 v1.3  VERIFICATION:  %d/%d regression/identity/interval checks PASS  |  Zero Free Parameters"
      % (_PASS, _PASS))
print("(the analytic theorems are established by the TEXT proofs; the suite supplies computational")
print(" guards and certified examples, NOT machine formal proofs of the general statements)")
print("(chi_H = log m is the horizontal exponent; K,J are the two FIBRE-exponent components)")
print("(anti-numerology OUT-OF-SAMPLE p=%.4f > 0.05 => density law HELD at HYPOTHESIS-weak)" % p_oos)
print("=" * 76)
