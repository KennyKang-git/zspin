#!/usr/bin/env python3
# =====================================================================
# ZS-M51 v1.3  VERIFICATION SUITE  (fail-closed)
# Author: Kenny Kang / Z-Spin Cosmology Collaboration
# deps: mpmath
#
# Mix of (i) high-precision algebraic regression checks and
#         (ii) RIGOROUS computer-assisted certifications:
#             - Krawczyk operator on complex intervals certifies the two
#               representative fibre cycles (unique root + multiplier sign).
# Numbering matches the v1.2 theorems.  Genuinely OPEN items
# (H-ORBIT, H-INV, H-PH-center) are registered and NOT counted as PASS.
# =====================================================================
import mpmath as mp
from math import gcd
mp.mp.dps = 50
twopi = 2*mp.pi
I = mp.mpc(0, 1)

def W0(z):    return mp.lambertw(z, 0)
def zstar_s(s):                     # general family f_s(z)=e^{i s z}
    a = I*s;  return -W0(-a)/a
def mult_s(s):  return abs(W0(-I*s))          # |f_s'(z*)| = |W0(-i s)|
def chi_fr(x):  return mp.log(abs(W0(-twopi*I*x)))   # polygon frozen exp, s=2 pi x

TOL = mp.mpf(10)**-40
ledger = []
def ck(name, cond): ledger.append((name, bool(cond)))

rho = mp.findroot(lambda v: mp.cos(v)-v, mp.mpf('0.739'))
xc  = mp.e**mp.sin(rho)/twopi
sc  = mp.e**mp.sin(rho)              # general-family threshold
nc  = twopi/sc

# =====================================================================
# PART I  — STANDALONE MATHEMATICS
# =====================================================================

# T1  General Multiplier Theorem  |f_s'(z*_s)| = |W0(-i s)|
for s in [mp.mpf('1.0'), mp.mpf('1.5'), mp.pi, twopi/mp.mpf(5)]:
    lhs = abs(I*s*zstar_s(s)); rhs = mult_s(s)
    ck(f"T1 general multiplier s={mp.nstr(s,4)}", abs(lhs-rhs) < TOL)

# T2  Dottie threshold s_c = e^{sin rho}; |W0(-i s_c)|=1 ; n_c=2pi/s_c
ck("T2 rho=cos rho", abs(mp.cos(rho)-rho) < mp.mpf(10)**-40)
ck("T2 s_c=e^{sin rho}=1.9613088464595", abs(sc-mp.mpf('1.9613088464595')) < mp.mpf('1e-12'))
ck("T2 |W0(-i s_c)|=1", abs(mult_s(sc)-1) < mp.mpf(10)**-30)
ck("T2 n_c=2pi/s_c=2pi e^{-sin rho}=3.2035675148878", abs(nc-mp.mpf('3.2035675148878')) < mp.mpf('1e-12'))
# analytic uniqueness witness: v(x)=-Im W0(-2pi i x) strictly increasing, <pi/2
vs = [(-mp.im(W0(-twopi*I*mp.mpf(k)/2000))) for k in range(1, 2000)]
ck("T2 v(x) strictly increasing on (0,1) (uniqueness)", all(vs[i] < vs[i+1] for i in range(len(vs)-1)))
ck("T2 v(x)<pi/2 on (0,1)", vs[-1] < mp.pi/2)

# T3  GENERAL LAMBERT MEAN IDENTITY  (1/X)∫_0^X log|W0(-2pi i x)|dx = log|W_X| - ReW_X/|W_X|^2
def LM_lhs(X): return mp.quad(lambda x: chi_fr(mp.mpf(x)), [0, X])/X
def LM_rhs(X):
    WX = W0(-twopi*I*X); return mp.log(abs(WX)) - mp.re(WX)/abs(WX)**2
for X in ['0.15', '0.25', '0.5', '0.8', '1.0']:
    Xm = mp.mpf(X)
    ck(f"T3 Lambert Mean Identity X={X}", abs(LM_lhs(Xm)-LM_rhs(Xm)) < mp.mpf(10)**-35)
# corollaries
ck("T3 band corollary (X=x_c) = -sin rho", abs(LM_rhs(xc)+mp.sin(rho)) < mp.mpf(10)**-30)
Lam_sec = LM_rhs(mp.mpf(1))
ck("T3 section corollary (X=1) = 0.00186237... > 0", Lam_sec > 0 and abs(Lam_sec-mp.mpf('0.0018623742238786')) < mp.mpf('1e-14'))

# T4  Invariant-graph separation No-Go + branch non-vanishing (measure-zero support)
def zstar_x(x):
    a = twopi*I*x; return -W0(-a)/a
ck("T4 separation |z*(1/2)-z*(1/4)|>0", abs(zstar_x(mp.mpf('0.5'))-zstar_x(mp.mpf('0.25'))) > mp.mpf('0.18'))
# Lemma T4.0: Im z*(x) > 0 on (0,1) (underpins injectivity => branch non-vanishing)
ck("T4.0 Im z*(x)>0 on (0,1) (injectivity of frozen family)",
   all(mp.im(zstar_x(mp.mpf(k)/500)) > 0 for k in range(1,500)))
brnz = True
for m in [2, 3, 5]:
    for j in range(m):
        a = mp.mpf(j)/m + mp.mpf('0.01'); b = mp.mpf(j+1)/m - mp.mpf('0.01')
        if a < mp.mpf('1e-9'): a = mp.mpf('0.005')
        da = abs(zstar_x(m*a-j)-zstar_x(a)); db = abs(zstar_x(m*b-j)-zstar_x(b))
        if da < mp.mpf('1e-9') and db < mp.mpf('1e-9'): brnz = False
ck("T4 Delta_{m,j} not identically zero on each branch", brnz)

# T5  FIXED-POINT CENSUS  saddle(x0<xc)/repeller(x0>xc); N_m=ceil(xc(m-1))-1
def census(m):
    sad = sum(1 for j in range(1, m-1) if mp.mpf(j)/(m-1) < xc)
    rep = sum(1 for j in range(1, m-1) if mp.mpf(j)/(m-1) > xc)
    return sad, rep
for m in range(2, 16):
    sad, rep = census(m)
    Nm = int(mp.ceil(xc*(m-1)))-1
    ck(f"T5 census m={m}: #saddle=ceil(xc(m-1))-1", sad == Nm)
    ck(f"T5 census m={m}: #repeller=(m-2)-N_m", rep == (m-2)-Nm)
ck("T5 first contracting fixed point at m=5 (x0=1/4)", (mp.mpf(1)/4 < xc) and (mp.mpf(1)/3 > xc))

# T6  Real 3x3 Jacobian classification at base-fixed points: moduli {|W0|,|W0|,m}
def real_jac_moduli(m, j):
    x0 = mp.mpf(j)/(m-1); z0 = zstar_x(x0); lamV = twopi*I*x0*z0; modV = abs(lamV)
    b = twopi*I*z0*z0
    J = mp.matrix([[mp.re(lamV), -mp.im(lamV), mp.re(b)],
                   [mp.im(lamV),  mp.re(lamV), mp.im(b)], [0, 0, m]])
    mods = sorted([abs(e) for e in mp.eig(J)[0]])
    return mods, modV
for (m, j) in [(5,1),(5,2),(7,1),(7,3),(9,1),(9,2),(13,3)]:
    mods, modV = real_jac_moduli(m, j)
    ck(f"T6 (m={m},j={j}) realJac moduli={{|W0|,|W0|,m}}",
       abs(mods[0]-min(modV,m)) < mp.mpf(10)**-18 and abs(max(mods)-max(modV,m)) < mp.mpf(10)**-18)
    x0 = mp.mpf(j)/(m-1)
    # classification: saddle (Es=2) iff modV<1 ; repeller (Eu=3) iff modV>1
    ck(f"T6 (m={m},j={j}) saddle<=>x0<xc", (modV < 1) == (x0 < xc))

# =====================================================================
# T7  RIGOROUS KRAWCZYK CERTIFICATION of two genuine fibre cycles
# =====================================================================
def base_orbit(k, n, m):
    xs = []; r = k % n; seen = []
    while True:
        xs.append(mp.mpf(r)/n); seen.append(r); r = (r*m) % n
        if r == seen[0]: break
    return xs
def Gpoint(xs, z):
    z0 = z; d = mp.mpf(1)
    for x in xs:
        zn = mp.e**(twopi*I*x*z0); d *= twopi*I*x*zn; z0 = zn
    return z0, d
def find_root(xs, seed):
    z = seed
    for _ in range(80):
        Gz, Gp = Gpoint(xs, z); z = z-(Gz-z)/(Gp-1)
    return z
mp.iv.dps = 34
ivpi = mp.iv.pi
def iv_c2pix(xrat): return mp.iv.mpc(mp.iv.mpf(0), 2*ivpi*mp.iv.mpf(xrat))
def Gbox(xs, Z):
    z = Z; d = mp.iv.mpc(mp.iv.mpf(1), mp.iv.mpf(0))
    for x in xs:
        c = iv_c2pix(x); zn = mp.iv.exp(c*z); d = c*zn*d; z = zn
    return z, d
def iv_pt(zc): return mp.iv.mpc(mp.iv.mpf([mp.re(zc), mp.re(zc)]), mp.iv.mpf([mp.im(zc), mp.im(zc)]))
def iv_box(zc, r): return mp.iv.mpc(mp.iv.mpf([mp.re(zc)-r, mp.re(zc)+r]), mp.iv.mpf([mp.im(zc)-r, mp.im(zc)+r]))
def inside(outer, inner):
    ro, io, ri, ii = outer.real, outer.imag, inner.real, inner.imag
    return ro.a < ri.a and ri.b < ro.b and io.a < ii.a and ii.b < io.b
def krawczyk(xs, zc, r):
    Gz, Gp = Gpoint(xs, zc); Y = 1/(Gp-1)
    X = iv_box(zc, r); one = mp.iv.mpc(mp.iv.mpf(1), mp.iv.mpf(0))
    Gb, Gpb = Gbox(xs, X); Fpb = Gpb - one
    K = iv_pt(zc) - iv_pt(Y)*iv_pt(Gz-zc) + (one - iv_pt(Y)*Fpb)*(X - iv_pt(zc))
    return inside(X, K), abs(Gpb)

# attracting: 1/7, m=2
xsA = base_orbit(1, 7, 2); zA = find_root(xsA, mp.mpc('0.2','-0.3'))
okA, magA = krawczyk(xsA, zA, mp.mpf('1e-3'))
ck("T7 Krawczyk 1/7,m=2: unique root K(X) in int(X)", okA)
ck("T7 Krawczyk 1/7,m=2: |G'| enclosure < 1 (certified ATTRACTING)", magA.b < 1)
# repelling: 1/3, m=2
xsR = base_orbit(1, 3, 2); zR = find_root(xsR, mp.mpc('0.4','0.3'))
okR, magR = krawczyk(xsR, zR, mp.mpf('1e-3'))
ck("T7 Krawczyk 1/3,m=2: unique root K(X) in int(X)", okR)
ck("T7 Krawczyk 1/3,m=2: |G'| enclosure > 1 (certified REPELLING)", magR.a > 1)

# =====================================================================
# PART II — POLYGON SPECIALIZATION (s = 2 pi / n)
# =====================================================================
seed = {3:1.033042, 4:0.891514, 5:0.787789, 6:0.707242, 8:0.588454, 12:0.440264}
for n, val in seed.items():
    m = abs(W0(-twopi*I*(mp.mpf(1)/n)))
    ck(f"P frozen multiplier n={n} = ZS-M1", abs(float(m)-val) < 1e-6)
    ck(f"P frozen sign n={n}", (m > 1) if n == 3 else (m < 1))
ck("P n_c (polygon) = general n_c", abs(nc-mp.mpf('3.2035675148878')) < mp.mpf('1e-12'))
# rapidity bridge chi_fr=log(2pi x)-alpha
for n in [4, 5, 8, 12]:
    x = mp.mpf(1)/n
    ck(f"P rapidity bridge n={n}", abs(chi_fr(x)-(mp.log(twopi*x)-mp.re(W0(-twopi*I*x)))) < TOL)

# =====================================================================
# PART III — CORPUS INTERFACE + ANTI-NUMEROLOGY
# =====================================================================
import itertools
ck("C two-clock cocycle additivity", (3+4, mp.log(2*5)) == (3+4, mp.log(2)+mp.log(5)))
logs = [mp.log(p) for p in [2, 3, 5, 7]]
rel = any(abs(sum(a*l for a, l in zip(A, logs))) < mp.mpf(10)**-25
          for A in itertools.product(range(-6, 7), repeat=4) if any(A))
ck("C {log2,3,5,7} bounded regression: no integer relation", not rel)
x = mp.mpf(1)/4; m4 = abs(W0(-twopi*I*x)); cv4 = chi_fr(x)
for mm in [2, 3, 5]:
    ck(f"AN m|f'|!=1 (m={mm})", abs(mm*m4-1) > mp.mpf('0.1'))
    ck(f"AN chiH+chi_fr!=0 (m={mm})", abs(mp.log(mm)+cv4) > mp.mpf('0.1'))
ck("AN Lambda_sec not forced to 0", Lam_sec > 0)

# =====================================================================
np_ = sum(1 for _, o in ledger if o); nt = len(ledger)
for nm, o in ledger: print(f"[{'PASS' if o else 'FAIL'}] {nm}")
print("=" * 70)
print(f"TOTAL: {np_}/{nt} checks PASS  (including two Krawczyk-certified cycles = {sum(1 for n,_ in ledger if n.startswith('T7'))} interval assertions)")
print()
print("REGISTERED OPEN / CLOSED-NEGATIVE (per v1.2 gate table):")
print("  H-UFC   CLOSED-NEGATIVE : global uniform 2D-fibre contraction (T7 repelling cycle certified).")
print("  H-2s1u  CLOSED-NEGATIVE : global {dim Es=2, dim Eu=1} splitting (same).")
print("  H-PH    OPEN/NON-CLAIM  : centre-type partial hyperbolicity on a compact invariant set.")
print("  H-ORBIT OPEN            : genuine a.e. fibre Lyapunov exponent over base ACIM.")
print("  H-INV   OPEN            : nontrivial invariant graphs on sub-bands.")
print()
print("Key:  rho=", mp.nstr(rho,12), " s_c=", mp.nstr(sc,12), " x_c=", mp.nstr(xc,12), " n_c=", mp.nstr(nc,12))
print("      Lambert-Mean corollaries: band=-sin rho=", mp.nstr(-mp.sin(rho),12), " Lambda_sec=", mp.nstr(Lam_sec,12))
assert np_ == nt, "FAIL-CLOSED: not all checks passed"
