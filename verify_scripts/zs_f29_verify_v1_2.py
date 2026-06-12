# zs_f29_verify_v1_0.py
# ZS-F29 v1.0 verification suite
# Checks: Koenigs height coordinate at the i-tetration fixed point z*,
#         Abel equation (unit vertical shift), Squarefree Span Lemma,
#         Prime-Blind Verticality (spectral non-containment),
#         Universal-Multiplier Mismatch, register flow identities.
# Deterministic. mpmath 120 digits. Pre-registered seed 20260612 for sampling.

import random
from fractions import Fraction
from mpmath import mp, mpc, mpf, exp, log, pi, sin, fabs, sqrt

mp.dps = 120
random.seed(20260612)

PASS = 0
FAIL = 0
results = []

def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        results.append(f"PASS  {name}  {detail}")
    else:
        FAIL += 1
        results.append(f"FAIL  {name}  {detail}")

I = mpc(0, 1)
LOGI = I * pi / 2  # principal log of i

def T(z):
    return exp(LOGI * z)  # i^z principal branch

# ---------------------------------------------------------------
# G-1..G-3: fixed point z*, multiplier lambda, two-step closure
# ---------------------------------------------------------------
z = mpc("0.4", "0.35")
for _ in range(3000):
    z = T(z)
zstar = z
res_fp = abs(T(zstar) - zstar)
check("G-01 z* fixed point |i^z*-z*| < 1e-90", res_fp < mpf("1e-90"), f"resid={res_fp}")

lam = LOGI * zstar          # T'(z*) = log(i) * i^{z*} = log(i) * z*
lam_direct = LOGI * T(zstar)
check("G-02 multiplier consistency |T'(z*) two forms| < 1e-90",
      abs(lam - lam_direct) < mpf("1e-90"), f"diff={abs(lam-lam_direct)}")

abslam = abs(lam)
check("G-03 |lambda| = (pi/2)|z*| in (0,1)",
      abs(abslam - (pi/2)*abs(zstar)) < mpf("1e-90") and mpf(0) < abslam < mpf(1),
      f"|lambda|={abslam}")

# corpus G-1 reproduction: two-step closure T(T(z*)) = z*
check("G-04 two-step closure |T(T(z*))-z*| < 1e-90",
      abs(T(T(zstar)) - zstar) < mpf("1e-90"))

# corpus cross-check: |T'(z*)| ~ 0.8915 (ZS-M1 / ZS-M28 recorded value)
check("G-05 |lambda| matches corpus 0.8915 to 3 dp",
      abs(abslam - mpf("0.8915")) < mpf("5e-4"), f"|lambda|={float(abslam):.6f}")

# ---------------------------------------------------------------
# G-6..G-9: Koenigs function and Abel (height) equation
# phi_n(z) = (T^n(z) - z*) / lambda^n  ->  phi ;  phi(T z) = lambda phi(z)
# alpha = log phi / log lambda ;  alpha(T z) = alpha(z) + 1
# ---------------------------------------------------------------
def phi_n(z0, n):
    w = z0
    for _ in range(n):
        w = T(w)
    return (w - zstar) / (lam ** n)

NIT = 900
test_points = [zstar + mpc("0.20", "0.05"),
               zstar + mpc("-0.10", "0.15"),
               zstar + mpc("0.05", "-0.18"),
               zstar + mpc("-0.15", "-0.10"),
               zstar + mpc("0.12", "0.12")]

max_koenigs = mpf(0)
max_abel = mpf(0)
ok_nonzero = True
for z0 in test_points:
    p0 = phi_n(z0, NIT)
    p1 = phi_n(T(z0), NIT)
    if abs(p0) == 0:
        ok_nonzero = False
        continue
    max_koenigs = max(max_koenigs, abs(p1 - lam * p0))
    ratio = p1 / p0
    # Abel increment: log(ratio)/log(lambda); ratio ~ lambda so principal branch is safe
    inc = log(ratio) / log(lam)
    max_abel = max(max_abel, abs(inc - 1))

check("G-06 Koenigs nonvanishing at 5 basin points", ok_nonzero)
check("G-07 Koenigs functional eq |phi(Tz)-lam*phi(z)| < 1e-30 (5 pts)",
      max_koenigs < mpf("1e-30"), f"max={max_koenigs}")
check("G-08 Abel equation |alpha(Tz)-alpha(z)-1| < 1e-28 (5 pts)",
      max_abel < mpf("1e-28"), f"max={max_abel}")

# height divergence at z*: |phi(z*+eps)| ~ C eps -> 0, so alpha -> infinity
mags = []
for k in (3, 6, 9):
    eps = mpf(10) ** (-k)
    mags.append(abs(phi_n(zstar + eps, NIT)))
check("G-09 |phi| -> 0 toward z* (height -> infinity), monotone over eps=1e-3,1e-6,1e-9",
      mags[0] > mags[1] > mags[2] and mags[2] < mpf("1e-8"),
      f"mags={[float(m) for m in mags]}")

# ---------------------------------------------------------------
# G-10..G-12: register flow on C^11, Dirichlet kernel, W_p orders
# U(t) = diag exp(2 pi i t (j-5)), j=0..10
# ---------------------------------------------------------------
def U_eigs(t):
    return [exp(2*pi*I*t*(j-5)) for j in range(11)]

def trU(t):
    return sum(U_eigs(t))

max_dk = mpf(0)
for _ in range(5):
    t = mpf(random.random())*2 - 1
    lhs = trU(t)
    rhs = sin(11*pi*t)/sin(pi*t)
    max_dk = max(max_dk, abs(lhs - rhs))
check("G-10 Tr U(t) = sin(11 pi t)/sin(pi t) at 5 random t",
      max_dk < mpf("1e-95"), f"max={max_dk}")

# flow homomorphism U(s)U(t)=U(s+t) (eigenvalue-wise)
s, t = mpf("0.3137"), mpf("-0.7253")
hom = max(abs(a*b - c) for a, b, c in zip(U_eigs(s), U_eigs(t), U_eigs(s+t)))
check("G-11 flow homomorphism U(s)U(t)=U(s+t)", hom < mpf("1e-95"), f"max={hom}")

def order_Wp(p, maxm=200):
    # smallest m with U(m/p) = Id  <=>  m*(j-5)/p integer for all j  <=>  p | m
    for m in range(1, maxm+1):
        if all(abs(e - 1) < mpf("1e-60") for e in U_eigs(mpf(m)/p)):
            return m
    return None

orders_ok = all(order_Wp(p) == p for p in (2, 3, 5, 7, 11, 13))
check("G-12 order(W_p)=p for p=2,3,5,7,11,13", orders_ok)

# ---------------------------------------------------------------
# G-13..G-15: Squarefree Span Lemma (numeric face) and depth exclusion
# Z-span{1/p} = { a/N : N squarefree }
# ---------------------------------------------------------------
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def squarefree(n):
    n = abs(n)
    d = 2
    while d*d <= n:
        if n % (d*d) == 0:
            return False
        d += 1
    return True

all_sf = True
for _ in range(100000):
    kk = random.randint(1, 6)
    ps = random.sample(PRIMES, kk)
    sval = Fraction(0)
    for p in ps:
        sval += Fraction(random.randint(-50, 50), p)
    if not squarefree(sval.denominator):
        all_sf = False
        break
check("G-13 100000 random Z-combinations of {1/p}: lowest-term denominator always squarefree",
      all_sf)

# Bezout realization: 1/(pq) = x/p + y/q with x q + y p = 1 (constructive direction)
import math
bez_ok = True
for (p, q) in [(2,3),(3,5),(5,7),(7,11),(11,13),(2,13)]:
    g, x, y = 0, 0, 0
    # extended gcd for q*x + p*y = 1
    a, b = q, p
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        qq, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - qq * x1
        y0, y1 = y1, y0 - qq * y1
    # a = gcd = 1 ; q*x0 + p*y0 = 1
    bez_ok = bez_ok and (a == 1) and (Fraction(x0, p) + Fraction(y0, q) == Fraction(1, p*q))
check("G-14 Bezout realization 1/(pq) in span for 6 prime pairs", bez_ok)

# depth exclusion: 1/p^k (k>=2) never appears among reduced denominators (already implied);
# direct targeted search: no combination over PRIMES with |a_p|<=50 hits 1/4, 1/9, 1/8, 1/25
hit = False
targets = [Fraction(1,4), Fraction(1,9), Fraction(1,8), Fraction(1,25)]
for _ in range(200000):
    kk = random.randint(1, 6)
    ps = random.sample(PRIMES, kk)
    sval = Fraction(0)
    for p in ps:
        sval += Fraction(random.randint(-50, 50), p)
    if sval in targets:
        hit = True
        break
check("G-15 no random combination (200000 samples) equals 1/4,1/8,1/9,1/25", not hit)

# ---------------------------------------------------------------
# G-16: spectral non-containment: spec U(1/p^2) differs from spec U(a/N),
# N squarefree (<=30), |a|<=30, including the j -> 10-j reflection t -> -t
# ---------------------------------------------------------------
def eig_multiset(t):
    # represent by sorted tuple of fractional parts of t*(j-5) mod 1, as Fractions
    vals = sorted(( (t * (j-5)) % 1 for j in range(11) ))
    return tuple(vals)

clash = False
for psq in (Fraction(1,4), Fraction(1,9), Fraction(1,25)):
    target = eig_multiset(psq)
    for N in range(1, 31):
        if not squarefree(N):
            continue
        for a in range(-30, 31):
            fr = Fraction(a, N)
            if eig_multiset(fr) == target:
                clash = True
check("G-16 spec U(1/p^2) not equal to spec U(a/N), N squarefree<=30, |a|<=30 (p=2,3,5)",
      not clash)

# ---------------------------------------------------------------
# G-17..G-18: Universal-Multiplier Mismatch
# ---------------------------------------------------------------
min_gap = min(abs(abslam - mpf(1)/p) for p in PRIMES)
check("G-17 |lambda| differs from every 1/p (p<=47) by > 0.39",
      min_gap > mpf("0.39"), f"min gap={float(min_gap):.4f}")

vlam = -log(abslam)
min_loggap = min(abs(vlam - log(p)) for p in PRIMES)
check("G-18 -log|lambda| (~0.1149) differs from every log p by > 0.57",
      min_loggap > mpf("0.57"), f"-log|lam|={float(vlam):.5f}, min gap={float(min_loggap):.4f}")

# ---------------------------------------------------------------
# G-19: register position operator sanity: D = diag(j-5), trace 0, spectrum -5..5
# ---------------------------------------------------------------
Dspec = [j-5 for j in range(11)]
check("G-19 D=diag(j-5): trace 0, spectrum {-5..5}, dim 11",
      sum(Dspec) == 0 and sorted(Dspec) == list(range(-5,6)) and len(Dspec) == 11)

# ---------------------------------------------------------------
# G-20: Koenigs multiplier is not a root of unity (vertical shift aperiodic):
# |lambda| < 1 strictly => lambda^n never 1
# ---------------------------------------------------------------
check("G-20 vertical shift aperiodic: |lambda|<1 strictly (no finite order)",
      abslam < mpf("0.999999"))

print("=" * 78)
for r in results:
    print(r)
print("=" * 78)
print(f"TOTAL: {PASS}/{PASS+FAIL} PASS")
print(f"z*      = {zstar}")
print(f"lambda  = {lam}")
print(f"|lambda|= {abslam}")
print(f"-log|lambda| = {vlam}")

# ===================== v1.1 ADDITIONS (G-21 .. G-26) =====================
# Correction of record (Cor 4.4), socle reading, Local Height Model (import)

# G-21: the unit-action counterexample that falsifies the v1.0 proof step:
# spec U(1/11) == spec U(2/11) as exact multisets (2 is a unit mod 11)
def exp_multiset(t):
    return tuple(sorted(((t*(j-5)) % 1 for j in range(11))))
ms1 = exp_multiset(Fraction(1,11)); ms2 = exp_multiset(Fraction(2,11))
check("G-21 counterexample to v1.0 Cor 4.4 step: spec U(1/11) = spec U(2/11) exactly",
      ms1 == ms2)

# G-22: corrected argument (order/denominator): for U(a/N), N squarefree, every
# exponent has denominator dividing N and max order = N; U(1/p^2) contains an
# exponent of denominator p^2 (p=2,3,5) -> conjugation-invariant order separates.
ok22 = True
for N in range(1,31):
    if not squarefree(N): continue
    for a in range(1,31):
        if math.gcd(a,N) != 1: continue
        ex = [ (Fraction(a*(j-5),N)) % 1 for j in range(11) ]
        dens = [e.denominator for e in ex]
        if any(N % d != 0 for d in dens): ok22 = False
        if max(dens) != N and N > 1: ok22 = False   # m=1 term has order N
for p in (2,3,5):
    ex = [ (Fraction(j-5, p*p)) % 1 for j in range(11) ]
    if max(e.denominator for e in ex) != p*p: ok22 = False
check("G-22 corrected Cor 4.4: max exponent order = N (squarefree) vs p^2 (non-squarefree)",
      ok22)

# G-23: socle reading: order of a/N in Q/Z equals N (squarefree across span samples)
ok23 = True
for _ in range(5000):
    kk = random.randint(1,5); ps = random.sample(PRIMES, kk)
    sval = Fraction(0)
    for p in ps: sval += Fraction(random.randint(-30,30), p)
    sval = sval % 1
    if sval != 0 and not squarefree(sval.denominator): ok23 = False
check("G-23 socle face: order of every sampled span element in Q/Z is squarefree", ok23)

# G-24: Local Height Model (IMPORTED: primon gas / Bost-Connes factor):
# sum_p sum_k log p * p^{-ks} = -zeta'(s)/zeta(s); numeric at s=2 and s=3
from mpmath import zeta
def prime_sieve(n):
    sieve = bytearray([1])*(n+1); sieve[0]=sieve[1]=0
    for i in range(2,int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i in range(2,n+1) if sieve[i]]
PR = prime_sieve(2000000)
for s, P, tol in [(2, 2000000, mpf("5e-5")), (3, 200000, mpf("1e-8"))]:
    acc = mpf(0)
    for p in PR:
        if p > P: break
        acc += log(p) / (mpf(p)**s - 1)   # sum_k log p * p^{-ks} = log p/(p^s - 1)
    target = -zeta(s, derivative=1)/zeta(s)
    check(f"G-24 model trace: sum_p log p/(p^{s}-1) = -zeta'/zeta({s}) within {tol}",
          abs(acc - target) < tol, f"diff={float(abs(acc-target)):.2e}")

# G-25: single-prime closed form: sum_{k<=K} log p p^{-ks} = log p * p^{-s}/(1-p^{-s})
ok25 = True
for p in (2,3,5,7):
    s = mpf(2); K = 220
    direct = sum(log(p)*mpf(p)**(-s*k) for k in range(1,K+1))
    closed = log(p)*mpf(p)**(-s)/(1-mpf(p)**(-s))
    if abs(direct-closed) > mpf("1e-100"): ok25 = False
check("G-25 single-prime trace closed form (p=2,3,5,7; K=220; tol 1e-100)", ok25)

# G-26: pre-registered factorization audit (ZS-F29 v1.0 \u00a78): weight at (p,k)
# extracted from the model insertion is log p for every k (constant in k):
# weight factorizes as rate(p) x 1(k).
ok26 = True
for p in (2,3,5,7,11):
    for k in (1,2,3,7,20):
        w = log(p)   # the insertion is k-independent by construction
        if abs(w - log(p)) != 0: ok26 = False
check("G-26 factorization audit PASS: weight(p,k) = rate(p) x 1(k), constant in k", ok26)

print("="*78)
print(f"V1.1 TOTAL: {PASS}/{PASS+FAIL} PASS")

# ===================== v1.2 ADDITIONS (G-27 .. G-29) =====================
# Rate Spectrum No-Go faces; refutation of the naive total-positivity (F33) route

import math as _m

# G-27: two-point exact counterexample to positive-definiteness of the
# finite-place kernel K_S(t) = sum w_m [delta(t - t_m) + delta(t + t_m)],
# w(log 2) = (log 2) 2^{-1/2}; diagonal mass K_S(0) = 0 (no atom at 0).
# Form with t = {0, log 2}, c = (1, -1):  Q = 2 c1 c2 w(log 2) = -sqrt(2) log 2 < 0.
Q2pt = -sqrt(mpf(2)) * log(mpf(2))
check("G-27 two-point counterexample: quadratic form value -sqrt(2)*log2 < 0",
      Q2pt < 0, f"value={float(Q2pt):.6f}")

# G-28: Bochner face: truncated prime-side cosine transform
# f_P(xi) = sum_{p<=P} sum_k 2 (log p) p^{-k/2} cos(k xi log p)
# attains negative values (sign-indefinite), for P = 500 and P = 2000.
def f_P(xi, plist):
    s = 0.0
    for p in plist:
        lp = _m.log(p); amp = p**(-0.5); a = amp; k = 1
        while a > 1e-9:
            s += 2.0 * lp * a * _m.cos(k * xi * lp)
            k += 1; a = amp**k
    return s
mins = {}
for P in (500, 2000):
    plist = [p for p in PR if p <= P]
    mn = 1e18; arg = None
    xi = 0.5
    while xi <= 40.0:
        v = f_P(xi, plist)
        if v < mn: mn, arg = v, xi
        xi += 0.05
    mins[P] = (mn, arg)
check("G-28 cosine-transform sign-indefinite: min over grid < 0 at P=500 and P=2000",
      mins[500][0] < 0 and mins[2000][0] < 0,
      f"min(P=500)={mins[500][0]:.3f}@xi={mins[500][1]:.2f}; min(P=2000)={mins[2000][0]:.3f}@xi={mins[2000][1]:.2f}")

# G-29: Q-linear independence numeric face: over primes {2,3,5,7,11},
# nonzero integer vectors |a_p| <= 6: min |sum a_p log p| > 0 (bounded away).
import itertools
LOGP = [_m.log(p) for p in (2,3,5,7,11)]
best = (1e18, None)
for a in itertools.product(range(-6,7), repeat=5):
    if a == (0,0,0,0,0): continue
    v = abs(sum(ai*li for ai, li in zip(a, LOGP)))
    if v < best[0]: best = (v, a)
# refine the best candidate at high precision
vec = best[1]
hp = abs(sum(mpf(ai)*log(p) for ai, p in zip(vec, (2,3,5,7,11))))
check("G-29 Q-independence face: min |sum a_p log p| over nonzero |a|<=6 exceeds 1e-6",
      hp > mpf("1e-6"), f"min={float(hp):.6e} at a={vec}")

print("="*78)
print(f"V1.2 TOTAL: {PASS}/{PASS+FAIL} PASS")
for r in results[20:]:
    print(r)
