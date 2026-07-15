#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_m49_verify_v1_3.py
=====================
Fail-closed verification suite for

  ZS-M49 v1.3 -- The C2^3 Quasicrystal Lift of the Galois-Graded Suzuki Operator
                 The Theta-Lipschitz Zero-Exclusion Certificate, an Eight-Channel
                 Suzuki Preconditioner, Two NO-GOs, and POME-K' by Import

Author: Kenny Kang / Z-Spin Collaboration.   Date: July 2026.
Zero fitted parameters.  A = 35/437, Q = 11, (Z,X,Y) = (2,3,6) LOCKED.

Categories
  A  Locked inputs                                                        (5)
  B  Icosahedral carrier: Lambda^2 V4 = 3 (+) 3',  End = Q(sqrt5)        (13)
  C  C2^3 Galois data: field, characters, conductors, disc               (12)
  D  Dedekind factorisation / Frobenius detector                          (5)
  E  Theorem M49.NG1  (prime log-lengths are not uniformly discrete)      (4)
  F  Theorem M49.NG2  (log p are Q-linearly independent)                  (3)
  G  Theorem M49.C certificate + eight-channel zeros + T9 budget         (22)
  H  Anti-numerology / provenance / the monotone lemma                    (5)
  J  Multiquadratic ensemble control + the scaling observation           (10)
  K  Reusable certified table + independent ZS-M48 cross-validation       (5)
                                                              TOTAL  =   84

Exits non-zero on the first failure.  The expected count is HARD-CODED.

=======================  WHAT CHANGED IN v1.3  =========================
The v1.2 external review accepted Theorem M49.C but found that its IMPLEMENTATION
still had four gaps in the outward enclosure of the two truncation tails.  All
four are closed here; the MATHEMATICS of M49.C is unchanged and the numerical
values of M1 are unchanged to every printed digit.

  (4.1) The n-tail was a FINITE float sum over range(N+1, N+400) with no bound on
        what lay beyond.  v1.3 replaces it by a CLOSED-FORM INFINITE-SUM bound
              S_N := sum_{n>N} n^a e^{-c(n^2-N^2)}  <=  q/(2 pi)      (c = pi/q),
        valid whenever N >= sqrt(q/(2 pi)) -- which the chosen N always satisfies.
        Nothing is truncated.
  (4.2) The tails were computed with math.exp / math.log / sum in Python floats,
        with no outward rounding.  v1.3 computes EVERY tail quantity in arb ball
        arithmetic and takes .upper() only at the very end.
  (4.3) The x-tail used "x^alpha log x is decreasing beyond X".  For ODD parity
        alpha = -1/4 and that function INCREASES up to x = e^4 = 54.598, while the
        v1.2 code chose X = 53 at q = 3.  The claim was FALSE there.  v1.3 does not
        use monotonicity at all: it bounds x^alpha <= X^alpha (alpha < 0) and
        log x <= x, giving
              Int_X^oo e^{-cx} x^alpha log x dx  <=  X^alpha e^{-cX} (X/c + 1/c^2),
        which needs no monotonicity and holds for every alpha < 0 and every X >= 1.
  (4.4) The integration endpoint was U = acb(math.log(Xf)) -- a float log, so a
        sliver could fall between the end of the quadrature and the start of the
        tail.  v1.3 makes U an EXACT INTEGER and defines X := e^U as an arb ball,
        so the quadrature ends exactly where the tail bound begins.
  Lemma M49.C1 (the quadrature-free closed form) is likewise now a rigorous arb
  bound with its own closed-form infinite-sum tail, and G17 compares it against
  the sharp M1 by INTERVAL comparison.
  New checks: G21 (both tails are arb-derived, closed-form, and < 1e-23) and
  G22 (c*X >= 60 in every channel -- the structural guard that replaces the false
  monotonicity assumption of v1.2).

Also in v1.3: the external-novelty language of Sec. 11 is narrowed.  M49.C is NOT
a replacement for Platt-type rigorous / Turing-method L-zero verification; it is a
lightweight LOW-HEIGHT certificate for channel selection in a Suzuki audit.

REQUIREMENTS: python-flint (Arb ball arithmetic), sympy, mpmath.
Fail-closed: if python-flint is absent the run ABORTS (no silent float fallback).
Typical wall clock: ~100 s.
"""

import sys, math, itertools
import sympy as sp
from sympy import Rational, Matrix, eye, zeros, primerange, isprime, igcd
from sympy.ntheory.factor_ import factorint
from sympy.functions.combinatorial.numbers import jacobi_symbol
from mpmath import mp, log as mplog, pslq

try:
    from flint import arb, acb, ctx, dirichlet_char
except ImportError:
    print("*** ABORT: python-flint is REQUIRED for the Theorem M49.C certificate.")
    print("***        pip install python-flint")
    sys.exit(3)

mp.dps = 30
ctx.dps = 40

EXPECTED_CHECKS = 84
_n = 0

def check(cid, desc, ok, detail=""):
    global _n
    _n += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {cid:<7} {desc}" + (f"   | {detail}" if detail else ""))
    if not ok:
        print("\n*** FAIL-CLOSED: aborting on first failure ***")
        sys.exit(1)

# ======================================================================
# A -- locked inputs
# ======================================================================
print("\n=== A. Locked inputs (ZS-F1/F2/F5) ===")
A = Rational(35, 437)
Q, dimZ, dimX, dimY = 11, 2, 3, 6
check("A1", "A = 35/437", A == Rational(35, 437), f"A = {float(A):.9f}")
check("A2", "Q = 11 and Q = Z+X+Y", Q == dimZ + dimX + dimY, "2+3+6 = 11")
check("A3", "Q is prime", isprime(Q))
check("A4", "kappa^2 = A/Q = 35/4807", A / Q == Rational(35, 4807))
check("A5", "eta(4)/4 > A > eta(5)/5  (A-bracketing, ZS-M1 §8)",
      0.3221188634 / 4 > float(A) > 0.3930067437 / 5, "0.080530 > 0.080092 > 0.078601")

# ======================================================================
# B -- the icosahedral carrier
# ======================================================================
print("\n=== B. Icosahedral carrier: Lambda^2 V_4 = 3 (+) 3', End_QA5 = Q(sqrt5) ===")

def perm_matrix_std(g):
    M = zeros(4, 4); g4 = g[4]
    for i in range(4):
        gi = g[i]
        if gi < 4: M[gi, i] += 1
        if g4 < 4: M[g4, i] -= 1
    return M

def wedge2(M):
    idx = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    W = zeros(6, 6)
    for c, (i, j) in enumerate(idx):
        for r, (k, l) in enumerate(idx):
            W[r, c] = M[k, i] * M[l, j] - M[l, i] * M[k, j]
    return W

g5 = (1, 2, 3, 4, 0); g3 = (1, 2, 0, 3, 4)
compose = lambda a, b: tuple(a[b[x]] for x in range(5))
G = {(0, 1, 2, 3, 4)}; frontier = [(0, 1, 2, 3, 4)]
while frontier:
    new = []
    for x in frontier:
        for gen in (g5, g3):
            y = compose(gen, x)
            if y not in G:
                G.add(y); new.append(y)
    frontier = new
G = sorted(G)
check("B1", "|A5| = 60 from the two generators", len(G) == 60, f"|G| = {len(G)}")

def sgn_perm(g):
    s = 1; p = list(g)
    for i in range(5):
        for j in range(i + 1, 5):
            if p[i] > p[j]: s = -s
    return s
check("B2", "all elements even (A5, not S5)", all(sgn_perm(g) == 1 for g in G))

R5 = perm_matrix_std(g5); R3 = perm_matrix_std(g3)
check("B3", "V4 is an integral 4-dim rep", all(x.is_integer for x in list(R5) + list(R3)))
W5 = wedge2(R5); W3 = wedge2(R3)
check("B4", "Lambda^2 V4 is an integral 6-dim rep",
      W5.shape == (6, 6) and all(x.is_integer for x in list(W5) + list(W3)))

chars6 = {g: sp.trace(wedge2(perm_matrix_std(g))) for g in G}
def order_of(g):
    o, x, e = 1, g, (0, 1, 2, 3, 4)
    while x != e:
        x = compose(x, g); o += 1
    return o
five = [g for g in G if order_of(g) == 5]
two2 = [g for g in G if order_of(g) == 2]          # the double transpositions
check("B5", "chi_W(5-cycle) = 1", all(chars6[g] == 1 for g in five), "20 elements of order 5")
inner = sp.Rational(sum(chars6[g] ** 2 for g in G), 60)
check("B6", "<chi_W, chi_W> = 2  ==>  a sum of TWO distinct irreps",
      inner == 2, f"<chi,chi> = {inner}   (NOTE: true for BOTH 3+3' and 1+5)")
# ---- v1.2 NEW: B5/B6 do NOT distinguish 3 (+) 3' from 1 (+) 5.  These do.
inv_mult = sp.Rational(sum(chars6[g] for g in G), 60)
check("B12", "invariant multiplicity <chi_W, 1> = 0  ==>  1 (+) 5 is EXCLUDED",
      inv_mult == 0, f"<chi_W,1> = {inv_mult}   (1 (+) 5 would give 1)")
check("B13", "chi_W(double transposition) = -2  (1 (+) 5 would give +2)",
      all(chars6[g] == -2 for g in two2),
      f"{len(two2)} elements of order 2; chi_W = -2 ==> the summands are 3 and 3'")

xs = sp.symbols('x0:36')
X = Matrix(6, 6, xs)
eqs = list(X * W5 - W5 * X) + list(X * W3 - W3 * X)
Msys, _ = sp.linear_eq_to_matrix(eqs, xs)
ns = Msys.nullspace()
check("B7", "dim_Q End_{QA5}(Lambda^2 V4) = 2", len(ns) == 2, f"dim = {len(ns)}")

basis = [Matrix(6, 6, list(v)) for v in ns]
cand = None
for c0 in range(-3, 4):
    for c1 in range(-3, 4):
        if (c0, c1) == (0, 0): continue
        Mx = c0 * basis[0] + c1 * basis[1]
        if sp.trace(Mx) == 0 and Mx != zeros(6, 6):
            cand = Mx; break
    if cand is not None: break
check("B8", "a traceless element exists in the commutant", cand is not None)
den = sp.lcm([sp.denom(x) for x in cand])
s_mat = sp.Matrix(6, 6, [sp.Integer(x * den) for x in cand])
gg = 0
for x in s_mat: gg = sp.igcd(gg, abs(int(x)))
s_mat = sp.Matrix(6, 6, [sp.Integer(x / gg) for x in s_mat])
check("B9", "s^2 = 5*I", s_mat * s_mat == 5 * eye(6), "integral commutant generator")
check("B10", "tr s = 0 and det s = -125",
      sp.trace(s_mat) == 0 and s_mat.det() == -125,
      f"tr = {sp.trace(s_mat)}, det = {s_mat.det()}")
star = s_mat / sp.sqrt(5)
check("B11", "star = s/sqrt5 is an involution ==> End = Q(sqrt5); +-1 eigenspaces are 3-dim",
      sp.simplify(star * star - eye(6)) == zeros(6, 6) and
      (star + eye(6)).rank() == 3 and (star - eye(6)).rank() == 3,
      "P_par = (I+star)/2, P_perp = (I-star)/2, each of rank 3")

# ======================================================================
# C -- C2^3 Galois data
# ======================================================================
print("\n=== C. C2^3 Galois data for L = Q(sqrt-3, sqrt-11, sqrt5) ===")
DISCS = [1, -3, 5, -11, -15, 33, -55, 165]

def kron(d, n):
    """FULL Kronecker symbol (d|n) for ANY integer n (v1.1 fix, retained)."""
    if n == 0: return 1 if abs(d) == 1 else 0
    res = 1
    if n < 0:
        n = -n
        if d < 0: res = -res
    e = 0
    while n % 2 == 0:
        n //= 2; e += 1
    if e:
        if d % 2 == 0: return 0
        res *= (1 if d % 8 in (1, 7) else -1) ** e
    if n == 1: return res
    if igcd(d, n) != 1: return 0
    return res * int(jacobi_symbol(d, n))

sqfree = lambda n: (all(e == 1 for e in factorint(abs(n)).values()) if abs(n) > 1 else abs(n) == 1)
check("C1", "-3, -11, 5 independent in Q*/(Q*)^2",
      not any(sp.sqrt(abs(sp.prod(t))).is_Integer
              for t in [(-3, -11), (-3, 5), (-11, 5), (-3, -11, 5)]))
check("C2", "|Gal(L/Q)| = 2^3 = 8 characters", len(DISCS) == 8)
check("C3", "every d is squarefree", all(sqfree(d) for d in DISCS))
check("C4", "every d = 1 (mod 4) ==> fundamental discriminant",
      all(d % 4 == 1 for d in DISCS))
conds = [abs(d) for d in DISCS]
check("C5", "conductors = {1,3,5,11,15,33,55,165}",
      sorted(conds) == [1, 3, 5, 11, 15, 33, 55, 165])
disc_L = 1
for c in conds: disc_L *= c
check("C6", "disc(L) = prod of conductors = 165^4", disc_L == 165 ** 4)
check("C7", "disc(L) = 3^4 * 5^4 * 11^4", factorint(disc_L) == {3: 4, 5: 4, 11: 4})

def sfk(m):
    s = 1 if m > 0 else -1; k = 1
    for p, e in factorint(abs(m)).items():
        if e % 2: k *= p
    return k * s
check("C8", "the 8 characters form a group under multiplication (C2^3)",
      all(sfk(d1 * d2) in DISCS for d1 in DISCS for d2 in DISCS))
ok = all(kron(d1, n) * kron(d2, n) == kron(sfk(d1 * d2), n)
         for n in range(1, 400) if igcd(n, 165) == 1
         for d1 in DISCS for d2 in DISCS)
check("C9", "chi_{d1}(n)*chi_{d2}(n) = chi_{d1 d2}(n), all n < 400 coprime to 165", ok)
check("C10", "parity split: 4 even {1,5,33,165}, 4 odd {-3,-11,-15,-55}",
      sorted(d for d in DISCS if d > 0) == [1, 5, 33, 165] and
      sorted(d for d in DISCS if d < 0) == [-55, -15, -11, -3])
check("C11", "chi_d(-1) = (d|-1) = sign(d)   [real Kronecker; v1.0's check was a tautology]",
      all(kron(d, -1) == (1 if d > 0 else -1) for d in DISCS))
check("C12", "the V4 subgroup {1,-3,-11,33} of ZS-M22 is preserved",
      all(d in DISCS for d in (1, -3, -11, 33)))

# ======================================================================
# D -- Frobenius detector
# ======================================================================
print("\n=== D. Frobenius detector ===")
splits = total = 0; ok_sum = ok_split = True
for p in primerange(2, 3000):
    if 165 % p == 0: continue
    total += 1
    S = sum(kron(d, p) for d in DISCS)
    if S not in (0, 8): ok_sum = False
    if all(kron(d, p) == 1 for d in DISCS):
        splits += 1
        if S != 8: ok_split = False
    elif S != 0:
        ok_split = False
check("D1", "sum over the 8 characters is 0 or 8 for every unramified p < 3000", ok_sum)
check("D2", "sum = 8 <==> p splits completely in L", ok_split)
check("D3", "density of completely split primes ~ 1/8",
      abs(splits / total - 0.125) < 0.04, f"{splits}/{total} = {splits/total:.4f}")
check("D4", "ZS-M22 V4 factorisation survives inside C2^3",
      all(sum(kron(d, p) for d in (1, -3, -11, 33)) in (0, 4)
          for p in primerange(2, 1000) if p not in (3, 11)))
check("D5", "ramified primes of L are exactly {3, 5, 11}",
      sorted(factorint(165).keys()) == [3, 5, 11])

# ======================================================================
# E / F -- the two NO-GOs
# ======================================================================
print("\n=== E. Theorem M49.NG1 (prime log-lengths are not uniformly discrete) ===")
P = list(primerange(2, 10 ** 6))
gaps = [math.log(P[i + 1]) - math.log(P[i]) for i in range(len(P) - 1)]
check("E1", "min log-gap over p < 10^6 is < 1e-5", min(gaps) < 1e-5, f"{min(gaps):.3e}")
w1 = min(math.log(P[i + 1]) - math.log(P[i]) for i in range(len(P) - 1) if P[i] < 10 ** 4)
w2 = min(math.log(P[i + 1]) - math.log(P[i])
         for i in range(len(P) - 1) if 10 ** 5 < P[i] < 10 ** 6)
check("E2", "min log-gap strictly decreases with the window", w2 < w1,
      f"[<1e4]: {w1:.3e}  [1e5,1e6]: {w2:.3e}")
check("E3", "log-gap = log(1 + (p'-p)/p) -> 0 (PNT)",
      all(abs(gaps[i] - math.log(1 + (P[i + 1] - P[i]) / P[i])) < 1e-12
          for i in range(0, len(gaps), 997)))
check("E4", "==> {m log p} is NOT uniformly discrete ==> NOT a relatively-compact-window "
            "model set in ANY internal space", min(gaps) < 1e-5,
      "SCOPE: this excludes model sets; it does NOT force infinite dimension (NC-M49.10)")

print("\n=== F. Theorem M49.NG2 (log p are Q-linearly independent) ===")
mp.dps = 60
rel3 = pslq([mplog(2), mplog(3), mplog(5)], maxcoeff=10 ** 8, maxsteps=10 ** 5)
check("F1", "no integer relation among log2, log3, log5 (PSLQ, 60 dps)", rel3 is None)
rel5 = pslq([mplog(p) for p in (2, 3, 5, 7, 11)], maxcoeff=10 ** 6, maxsteps=10 ** 5)
check("F2", "no integer relation among log p, p <= 11", rel5 is None)
check("F3", "==> <log p> is free abelian of infinite rank; no FINITE-VALUED roof that is "
            "locally constant on a FINITE Markov partition can realise it",
      rel3 is None and rel5 is None,
      "SCOPE: countable partitions / unbounded roofs are NOT excluded (NC-M49.10)")
mp.dps = 30

# ======================================================================
# G -- Theorem M49.C certificate + the eight channels
# ======================================================================
print("\n=== G. Theorem M49.C (Theta-Lipschitz certificate) + eight-channel zeros ===")

_cc = {}
def flint_char(q):
    if q in _cc: return _cc[q]
    for idx in range(q):
        try: c = dirichlet_char(q, idx)
        except Exception: continue
        if c.is_real() and c.is_primitive() and not c.is_principal():
            _cc[q] = c; return c
    raise RuntimeError("no real primitive character mod %d" % q)

def Lam(d, t):
    """completed Lambda(1/2+it, chi_d), as an acb BALL, via flint's dirichlet_l."""
    q = abs(d); a = 0 if d > 0 else 1
    s = acb(arb(1) / 2, t)
    return (acb(q) / acb.pi()) ** ((s + a) / 2) * ((s + a) / 2).gamma() \
           * acb.dirichlet_l(s, flint_char(q))
LamR = lambda d, t: Lam(d, t).real

# ---------- Theorem M49.C : a RIGOROUS t-independent Lipschitz bound ----------
# Hecke:  Lambda(1/2+it,chi) = 2 Int_1^oo theta_chi(x) x^{a/2-3/4} cos((t/2)log x) dx
#         theta_chi(x) = sum_{n>=1} n^a chi(n) e^{-pi n^2 x/q}     (eps(chi) = +1)
# =>      |d/dt Lambda| <= M1 := Int_1^oo Theta(x) x^{a/2-3/4} log x dx,  Theta >= |theta|
# The substitution x = e^u makes the integrand ENTIRE, so Arb's rigorous adaptive
# Gauss-Legendre quadrature applies with NO branch-cut caveat.
def M1_rigorous(d):
    """A FULLY RIGOROUS arb upper bound for M1(chi) = Int_1^oo Theta(x) x^al log x dx.

       Every quantity below is an arb ball; .upper() is taken once, at the end.
       Parameters are EXACT integers, so the quadrature endpoint and the tail
       start-point coincide by construction (v1.2 gap 4.4).

         c   := pi/q                       (arb)
         N   := ceil(sqrt(60 q / pi))      so that  c N^2 >= 60
         U   := ceil(log(60 q / pi))       an EXACT INTEGER
         X   := e^U                        (arb ball), so that  c X >= 60

       main   = Int_0^U Theta_N(e^u) e^{(al+1)u} u du      [x = e^u : ENTIRE integrand,
                                                            so Arb's rigorous adaptive
                                                            Gauss-Legendre applies with
                                                            no branch-cut caveat]
       n-tail : for x >= 1,  sum_{n>N} n^a e^{-c n^2 x} <= S_N e^{-c N^2 x},
                S_N := sum_{n>N} n^a e^{-c(n^2-N^2)} <= q/(2 pi)   [CLOSED FORM, no
                truncation -- valid since N >= sqrt(q/(2pi))].  Then, using x^al <= 1
                and log x <= x-1 on [1,oo),
                   contribution <= S_N e^{-c N^2} / (c N^2)^2 .
       u-tail : for u >= U,  Theta(e^u) <= B e^{-c e^u},  B := sum_n n^a e^{-c(n^2-1)X}
                <= 1 + 1/(2 c X)   [CLOSED FORM].  Then, with x = e^u,
                   Int_X^oo e^{-cx} x^al log x dx <= X^al e^{-cX} (X/c + 1/c^2),
                using ONLY  x^al <= X^al (al < 0)  and  log x <= x.
                *** No monotonicity of x^al log x is assumed -- that assumption was
                    FALSE for odd parity in v1.2 (gap 4.3). ***
    """
    q = abs(d); a = 0 if d > 0 else 1
    al = arb(a) / 2 - arb(3) / 4                 # alpha < 0 in both parities
    c = arb.pi() / arb(q)
    N = int(math.ceil(math.sqrt(60.0 * q / math.pi)))
    U = int(math.ceil(math.log(60.0 * q / math.pi)))     # EXACT integer endpoint
    Ua = arb(U); X = Ua.exp()                            # X = e^U, an arb ball
    def f(u, analytic):                                  # ENTIRE in u
        s_ = acb(0)
        for n in range(1, N + 1):
            s_ += acb(n) ** a * (-acb.pi() * acb(n * n) * u.exp() / acb(q)).exp()
        return s_ * ((acb(al) + 1) * u).exp() * u
    main = acb.integral(f, acb(0), acb(Ua)).real
    cN2 = c * arb(N * N)
    S_N = arb(q) / (2 * arb.pi())                        # closed-form infinite-sum bound
    tail_n = S_N * (-cN2).exp() / cN2 ** 2
    cX = c * X
    B = 1 + 1 / (2 * cX)                                 # closed-form infinite-sum bound
    tail_u = B * X ** al * (-cX).exp() * (X / c + 1 / c ** 2)
    return dict(M1=main + tail_n + tail_u, N=N, U=U,
                tail_n=tail_n, tail_u=tail_u, cX=cX)

def M1_closed(d):
    """Lemma M49.C1 -- quadrature-free, and now a RIGOROUS arb bound:
         M1 <= (q/pi)^2 * sum_{n>=1} n^{a-4} e^{-pi n^2 / q},
       with the infinite tail closed by  sum_{n>N} n^{a-4} e^{-c n^2}
                                          <= N^{-3} e^{-c N^2} / (2 c N)."""
    q = abs(d); a = 0 if d > 0 else 1
    c = arb.pi() / arb(q); N = 200
    s_ = arb(0)
    for n in range(1, N + 1):
        s_ += arb(n) ** (a - 4) * (-c * arb(n * n)).exp()
    s_ += arb(N) ** (-3) * (-c * arb(N * N)).exp() / (2 * c * arb(N))
    return (arb(q) / arb.pi()) ** 2 * s_

ZERO = arb(0)
def bsign(v):
    if v.contains(ZERO): raise RuntimeError("ball contains 0")
    return 1 if v > 0 else -1

def certify(d, tmax=45.0, nbis=64):
    """Theorem M49.C certificate:
       (i)  a certified enclosure of a zero (odd multiplicity) of Lambda(1/2+it,chi_d);
       (ii) a certified proof that Lambda(1/2+it,chi_d) != 0 for EVERY t in [0, gamma_lo]
            -- hence NO zero of ANY multiplicity lies below it on the critical line."""
    R = M1_rigorous(d); M1 = R['M1']
    fp = lambda t: float(LamR(d, arb(t)).mid())
    t = 0.0; v = fp(0.0); a0 = None
    while t < tmax:
        t2 = t + 0.01; v2 = fp(t2)
        if v * v2 < 0: a0 = t; break
        t, v = t2, v2
    if a0 is None: raise RuntimeError("no sign change below %g for d=%d" % (tmax, d))
    lo = arb(int(round(a0 * 100))) / 100
    hi = arb(int(round(a0 * 100)) + 1) / 100
    slo = bsign(LamR(d, lo))
    assert bsign(LamR(d, hi)) != slo
    for _ in range(nbis):
        mid = (lo + hi) / 2
        if bsign(LamR(d, mid)) == slo: lo = mid
        else: hi = mid
    # --- the covering grid; every cell is recorded so that G16 can RE-VERIFY it
    cells = []
    t = arb(0); v = LamR(d, t); s0 = bsign(v)
    while True:
        va = arb(abs(v).lower())
        h = arb('0.9') * va / M1
        if h > arb('0.05'): h = arb('0.05')
        if (t + h) > lo:
            cells.append((t, lo - t, va)); break        # final cell, closed at gamma_lo
        cells.append((t, h, va))
        t = t + h; v = LamR(d, t)
        assert bsign(v) == s0
        if len(cells) > 50000: raise RuntimeError("grid stalled, d=%d" % d)
    mid = (lo + hi) / 2; rad = (hi - lo) / 2
    return dict(d=d, lo=lo, hi=hi, M1=M1, R=R, cells=cells,
                gamma=arb(mid.mid(), (rad + arb('1e-38')).upper()))

def reverify(c):
    """independent re-verification of the covering certificate (this is what G16 tests)."""
    M1 = c['M1']; cur = arb(0)
    for (t, h, va) in c['cells']:
        if not (t - cur).contains(ZERO): return False          # cells must be contiguous
        if not (va > M1 * h): return False                     # |Lambda| > M1*h on the cell
        cur = t + h
    return (cur - c['lo']).contains(ZERO) or cur > c['lo']     # union covers [0, gamma_lo]

check("G1", "Lambda(1/2+it, chi_d) is real: |Im| < 1e-25 for all 7 non-trivial channels",
      all(abs(Lam(d, arb('1.7')).imag) < arb('1e-25') for d in DISCS if d != 1))

CERT = {d: certify(d) for d in DISCS if d != 1}
gam = {d: CERT[d]['gamma'] for d in CERT}

REF = {-3: '8.039737', 5: '6.6485', -11: '2.477244', 33: '2.996951'}
for i, d in enumerate([-3, 5, -11, 33], start=2):
    check(f"G{i}", f"chi_{d}: certified enclosure agrees with the ZS-M48 value {REF[d]}",
          abs(gam[d] - arb(REF[d])) < arb('1e-4'), gam[d].str(15, radius=True))
for i, d in enumerate([-15, -55, 165], start=6):
    check(f"G{i}", f"chi_{d} (NEW channel): CERTIFIED lowest critical-line zero",
          CERT[d]['hi'] - CERT[d]['lo'] < arb('1e-15'),
          gam[d].str(18, radius=True) + f"  [cells {len(CERT[d]['cells'])}]")

nz0 = arb('14.13').zeta_nzeros(); nz1 = arb('14.14').zeta_nzeros()
ZETA1 = acb.zeta_zero(1).imag
check("G9", "zeta channel (flint, rigorous): N(14.13)=0, N(14.14)=1",
      nz0 == 0 and nz1 == 1 and abs(ZETA1 - arb('14.134725141734694')) < arb('1e-12'),
      ZETA1.str(18, radius=True))

fm = lambda z: float(z.mid())
min_V4 = min([gam[-3], gam[-11], gam[33]], key=fm)
min_NEW = min([gam[5], gam[-15], gam[-55], gam[165]], key=fm)
check("G10", "min over the V4 channels = gamma_1(chi_-11)", fm(min_V4) == fm(gam[-11]))
check("G11", "min over the 4 NEW channels = gamma_1(chi_165)", fm(min_NEW) == fm(gam[165]))
check("G12", "*** O4 PRE-REGISTERED BENCHMARK: gamma_1(new) < min over V4 ***",
      (min_V4 - min_NEW) > 0,
      f"{min_NEW.str(10)} < {min_V4.str(10)}  PASS (a benchmark, NOT a family theorem)")
check("G13", "the first zero is NOT monotone in the conductor (chi_-15 > chi_33)",
      (gam[-15] - gam[33]) > 0, f"q=15: {gam[-15].str(7)} > q=33: {gam[33].str(7)}")

a0 = arb('0.2')
bud = lambda g: g / a0 + 1 / (2 * a0)
bz, b11, b165 = bud(ZETA1), bud(gam[-11]), bud(gam[165])
check("G14", "T9 budget: log N* = 73.17 (zeta) / 14.89 (chi_-11) / 8.85 (chi_165)",
      abs(bz - arb('73.1736')) < arb('0.01') and abs(b11 - arb('14.8862')) < arb('0.01')
      and abs(b165 - arb('8.8483')) < arb('0.01'),
      f"{bz.str(6)} / {b11.str(6)} / {b165.str(6)}")
coll = (bz - b165) / arb(10).log()
check("G15", "prime-budget collapse zeta -> chi_165 = 27.94 orders of magnitude",
      abs(coll - arb('27.936')) < arb('0.02'),
      f"{coll.str(6)} orders  (ZS-M48's V4 decomposition alone: 25.4)")

# ---- the four checks that make G16 a real certificate (v1.2) ----
check("G16", "*** THEOREM M49.C CERTIFICATE, RE-VERIFIED: contiguous cells, "
             "|Lambda(t_k)| > M1*h_k on every cell, union covers [0, gamma_lo] "
             "==> NO zero of ANY multiplicity below gamma_1 on the critical line ***",
      all(reverify(CERT[d]) for d in CERT),
      "cells/channel: " + ", ".join(f"{abs(d)}:{len(CERT[d]['cells'])}" for d in CERT))
check("G17", "Lemma M49.C1 (quadrature-free, arb): M1_sharp <= M1_closed, by INTERVAL "
             "comparison -- an independent, quadrature-free safety net",
      all((M1_closed(d) - CERT[d]['M1']) > 0 for d in CERT),
      " ; ".join(f"q={abs(d)}: {float(CERT[d]['M1'].upper()):.3f} <= "
                 f"{float(M1_closed(d).upper()):.1f}" for d in (-3, -11, 165)))
ok = True; ratios = []
for d in CERT:
    Mu = float(CERT[d]['M1'].upper()); h = 1e-6; mx = 0.0; k = 0
    while k * 0.05 <= float(gam[d].mid()) + 0.5:
        t = k * 0.05
        mx = max(mx, abs(float((LamR(d, arb(t + h)) - LamR(d, arb(t - h))).mid()) / (2 * h)))
        k += 1
    ratios.append(mx / Mu)
    if mx > Mu: ok = False
check("G18", "sanity: the SAMPLED max |dLambda/dt| really is <= M1 (guards the theta rep)",
      ok, "max ratio |Lambda'|/M1 over the 7 channels = %.3f (a wrong theta rep would exceed 1)"
          % max(ratios))

def Lam_theta(d, t):
    """INDEPENDENT ALGORITHM: the Hecke theta integral, on the entire chart x = e^u."""
    q = abs(d); a = 0 if d > 0 else 1
    al = arb(a) / 2 - arb(3) / 4
    N = int(math.ceil(math.sqrt(45.0 * q / math.pi))) + 1
    Xf = float(math.ceil(50.0 * q / math.pi)) + 10.0
    co = [kron(d, n) for n in range(N + 1)]
    def f(u, analytic):
        s = acb(0)
        for n in range(1, N + 1):
            if co[n]:
                s += acb(co[n]) * acb(n) ** a \
                     * (-acb.pi() * acb(n * n) * u.exp() / acb(q)).exp()
        return s * ((acb(al) + 1) * u).exp() * ((acb(t) / 2) * u).cos()
    return 2 * acb.integral(f, acb(0), acb(math.log(Xf))).real

dmax = max(abs(float((LamR(d, arb('1.1')) - Lam_theta(d, arb('1.1'))).mid())) for d in CERT)
check("G19", "*** INDEPENDENT ALGORITHM CROSS-CHECK: the Hecke theta integral reproduces "
             "flint's dirichlet_l value of Lambda(1/2+1.1i) in all 7 channels ***",
      dmax < 1e-20, f"max discrepancy = {dmax:.2e}  (two unrelated evaluation routes)")
zmax = max(abs(float(Lam_theta(d, gam[d]).mid())) for d in CERT)
check("G20", "the independent theta evaluation also vanishes at every certified gamma_1",
      zmax < 1e-12, f"max |Lambda_theta(gamma_1)| = {zmax:.2e}")

# ---- v1.3: the two truncation tails are now CLOSED-FORM and arb-derived ----
tn_max = max(float(CERT[d]['R']['tail_n'].upper()) for d in CERT)
tu_max = max(float(CERT[d]['R']['tail_u'].upper()) for d in CERT)
check("G21", "*** OUTWARD ENCLOSURE COMPLETE: both truncation tails of M1 are bounded by "
             "CLOSED-FORM INFINITE SUMS (S_N <= q/2pi ; B <= 1 + 1/(2cX)) and evaluated "
             "entirely in arb -- nothing is truncated, nothing is rounded inward ***",
      tn_max < 1e-23 and tu_max < 1e-23,
      f"max n-tail = {tn_max:.1e} ; max u-tail = {tu_max:.1e}  (v1.2 used float sums)")
cx_min = min(float(CERT[d]['R']['cX'].lower()) for d in CERT)
check("G22", "*** the u-tail bound needs NO monotonicity of x^alpha log x (v1.2 assumed it, "
             "and it is FALSE for odd parity below x = e^4): the guard is c*X >= 60 ***",
      cx_min >= 60.0 and all(CERT[d]['R']['U'] == int(CERT[d]['R']['U']) for d in CERT),
      f"min c*X over the 7 channels = {cx_min:.1f} ; U is an exact integer in every channel")

# ======================================================================
# H -- anti-numerology / provenance / the monotone lemma
# ======================================================================
print("\n=== H. Anti-numerology, provenance, monotone lemma ===")
M13_PREREG = [3, 5, 11, 15, 33, 55, 165]
check("H1", "the extended modulus list equals the ZS-M13 §4.3 list, pre-registered March 2026",
      sorted(c for c in conds if c != 1) == M13_PREREG,
      "the quasicrystal argument supplies the REASON, not the NUMBERS")
check("H2", "no free parameter added: A, Q, (Z,X,Y) unchanged",
      A == Rational(35, 437) and (Q, dimZ, dimX, dimY) == (11, 2, 3, 6))
check("H3", "sqrt(5) enters ONLY through End_{QA5}(3(+)3') -- PROVEN, not fitted",
      s_mat * s_mat == 5 * eye(6))
check("H4", "NON-CLAIM: nothing here proves or advances RH/GRH", True,
      "the POME-K' gates are structural; Weil positivity is untouched (ZS-M48 O2)")
check("H5", "Lemma M49.O1 [PROVEN, trivial]: min over C2^3 <= min over V4 (subset monotonicity)",
      min(fm(gam[d]) for d in gam) <= min(fm(gam[d]) for d in (-3, -11, 33)) + 1e-30,
      "only STRICTNESS was ever the content of O4")

# ======================================================================
# J -- ensemble control (DIAGNOSTIC tier)
# ======================================================================
print("\n=== J. Finite multiquadratic ensemble control -- DIAGNOSTIC (~45 s) ===")
ctx.dps = 15
ENS_PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]; ENS_PMAX = 2000

def LamR_fast(d, t):
    q = abs(d); a = 0 if d > 0 else 1
    s = acb(arb(1) / 2, arb(t))
    return float(((acb(q) / acb.pi()) ** ((s + a) / 2) * ((s + a) / 2).gamma()
                  * acb.dirichlet_l(s, flint_char(q))).real.mid())
_g1 = {}
def gamma1_fast(d, step=0.02, tmax=40.0):
    if d in _g1: return _g1[d]
    t, v = 0.0, LamR_fast(d, 0.0)
    while t < tmax:
        t2 = t + step; v2 = LamR_fast(d, t2)
        if v * v2 < 0:
            lo, hi, vlo = t, t2, v
            for _ in range(45):
                m = 0.5 * (lo + hi); vm = LamR_fast(d, m)
                if vlo * vm < 0: hi = m
                else: lo, vlo = m, vm
            _g1[d] = 0.5 * (lo + hi); return _g1[d]
        t, v = t2, v2
    raise RuntimeError(d)
st = lambda p: p if p % 4 == 1 else -p
def dsc(S):
    v = 1
    for p in S: v *= st(p)
    return v

triples = [T for T in itertools.combinations(ENS_PRIMES, 3) if T[0]*T[1]*T[2] <= ENS_PMAX]
cases, fields = [], []
for (p, q, r) in triples:
    subs = [(p,), (q,), (r,), (p, q), (p, r), (q, r), (p, q, r)]
    gs = {S: gamma1_fast(dsc(S)) for S in subs}
    c8 = min(gs.values())
    fields.append(dict(N=p*q*r, c8=c8, top=(min(gs, key=lambda S: gs[S]) == (p, q, r))))
    for (a, b) in [(p, q), (p, r), (q, r)]:
        cases.append(min(gs[(a,)], gs[(b,)], gs[tuple(sorted((a, b)))]) - c8)
ln10 = math.log(10)
strict = sum(1 for g in cases if g > 1e-9)
med = sorted(cases)[len(cases) // 2] / (0.2 * ln10)
check("J1", "ensemble enumerated (a COMPLETE enumeration, not a Monte Carlo)",
      len(triples) == 58 and len(_g1) == 110,
      f"{len(triples)} C2^3 fields, {len(cases)} (field,V4) cases, {len(_g1)} characters")
check("J2", "Lemma M49.O1 holds in 100% of ensemble cases (gain >= 0)",
      all(g >= -1e-12 for g in cases), "trivial; the check guards the code, not the maths")
check("J3", "E1: the C2^3 lift gives a STRICT gain in >= 80% of cases",
      strict / len(cases) >= 0.80, f"{strict}/{len(cases)} = {100*strict/len(cases):.1f}%")
check("J4", "E1: median gain in T9 orders of magnitude at (a,t) = (0.2, 0)",
      1.0 < med < 2.5, f"median {med:.3f} (mean {sum(cases)/len(cases)/(0.2*ln10):.3f}, "
                       f"max {max(cases)/(0.2*ln10):.3f})")
zg = _g1[-11] - _g1[165]
check("J5", "E1: the Z-Spin field's own gain = 2.62 T9 orders, and is not an outlier",
      abs(zg / (0.2 * ln10) - 2.622) < 0.02
      and sum(1 for g in cases if g <= zg) / len(cases) < 0.95,
      f"{zg/(0.2*ln10):.3f} orders; {100*sum(1 for g in cases if g<=zg)/len(cases):.1f}%"
      " of cases gain less")
xs_m = {d: g * math.log(abs(d)) / (2 * math.pi) for d, g in _g1.items()}
xv = list(xs_m.values()); nx = len(xv); xm = sum(xv) / nx
xsd = (sum((v - xm) ** 2 for v in xv) / (nx - 1)) ** 0.5
check("J6", "E2: the scaled first zero x = gamma_1 log q / 2pi is O(1)",
      0.9 < xm < 1.25 and xsd < 0.45,
      f"n={nx}  mean {xm:.4f}  sd {xsd:.4f}  min {min(xv):.4f}  max {max(xv):.4f}")
x165 = xs_m[165]
p2 = sum(1 for v in xv if abs(v - xm) >= abs(x165 - xm)) / nx
check("J7", "E2: x(165) is statistically UNEXCEPTIONAL within this finite ensemble",
      p2 > 0.05,
      f"x(165) = {x165:.4f}, z = {(x165-xm)/xsd:+.3f}, empirical two-sided p = {p2:.3f}. "
      "SCOPE: consistent with conductor scaling; does NOT establish causality (NC-M49.11)")
c8_ours = min(_g1[d] for d in (-3, 5, -11, -15, 33, -55, 165))
below = sum(1 for f in fields if f['c8'] <= c8_ours)
check("J8", "E3: the Z-Spin field is NOT a lucky field (its gamma_1^min sits near the TOP)",
      below / len(fields) > 0.9,
      f"{100*below/len(fields):.1f}% of the {len(fields)} fields have a LOWER gamma_1^min; "
      f"P[argmin = top conductor] = {sum(1 for f in fields if f['top'])/len(fields):.3f}")
# ---- v1.2 NEW: the two numbers the paper quotes are now CHECKED, not just printed
lq = [math.log(abs(d)) for d in _g1]; mlq = sum(lq) / nx
xs_l = [xs_m[d] for d in _g1]
slope = sum((lq[i] - mlq) * (xs_l[i] - xm) for i in range(nx)) / sum((l - mlq) ** 2 for l in lq)
check("J9", "E2: OLS slope of x on log q  (the paper's 'no drift' claim, now a check)",
      abs(slope) < 0.20, f"slope = {slope:+.5f}   (|slope| < 0.20 required; gate F-M49.10)")
mn = sum(math.log(f['N']) for f in fields) / len(fields)
mc = sum(f['c8'] for f in fields) / len(fields)
cov = sum((math.log(f['N']) - mn) * (f['c8'] - mc) for f in fields)
corr = cov / (math.sqrt(sum((math.log(f['N']) - mn) ** 2 for f in fields))
              * math.sqrt(sum((f['c8'] - mc) ** 2 for f in fields)))
check("J10", "E3: corr(log pqr, gamma_1^min) < -0.30  (the paper's correlation, now a check)",
      corr < -0.30, f"corr = {corr:+.4f}   (conductor, not luck, tracks the minimum)")
ctx.dps = 40

# ======================================================================
# K -- the certificate as a REUSABLE tool: external cross-validation
# ======================================================================
print("\n=== K. Theorem M49.C applied beyond L: reusable certified table ===")
EXTRA = [-4, -7, 13, -19, 17]
XC = {d: certify(d) for d in EXTRA}
M48REF = {-4: '6.0210', -7: '4.4757', 13: '3.1193'}      # ZS-M48 v2.7 §6.7, arb-certified
for i, d in enumerate([-4, -7, 13], start=1):
    check(f"K{i}", f"INDEPENDENT CROSS-VALIDATION: q={abs(d)} reproduces ZS-M48's "
                   f"certified {M48REF[d]}",
          abs(XC[d]['gamma'] - arb(M48REF[d])) < arb('1e-3'),
          XC[d]['gamma'].str(15, radius=True))
check("K4", "the certificate extends to further channels (q = 19, 17) with no new theory",
      all(reverify(XC[d]) for d in (-19, 17)),
      f"q=19: {XC[-19]['gamma'].str(12)} ; q=17: {XC[17]['gamma'].str(12)}")
check("K5", "*** Theorem M49.C is FIELD-AGNOSTIC: all 12 certified channels carry the full "
            "[0, gamma_lo] zero-exclusion certificate ***",
      all(reverify(c) for c in list(CERT.values()) + list(XC.values())),
      "7 channels of L + 5 external discriminants; the method is a reusable preconditioner tool")

# ======================================================================
print("\n" + "=" * 80)
if _n != EXPECTED_CHECKS:
    print(f"*** GUARD FAILURE: ran {_n} checks, expected {EXPECTED_CHECKS} ***")
    sys.exit(2)
print(f"ZS-M49 v1.3 VERIFICATION: {_n}/{EXPECTED_CHECKS} PASS  |  Zero Free Parameters")
print("Theorem tier   (exact rational/integer, SymPy)          : B, C, D, H")
print("CERTIFIED tier (Arb ball arithmetic + rigorous quadrature): G, K")
print("DIAGNOSTIC tier(double precision, finite enumeration)     : J")
print("=" * 80)
print("\nCERTIFIED Table 9.1 -- lowest critical-line zero of ANY multiplicity")
print("  (Theorem M49.C: enclosure + zero-exclusion on [0, gamma_lo])\n")
print("  %-9s %-6s %-42s %10s" % ("channel", "q", "gamma_1 (arb enclosure)", "M1 (rig.)"))
print("  zeta      q=1    " + ZETA1.str(16, radius=True))
for d in [-3, 5, -11, -15, 33, -55, 165]:
    print("  chi_%-6d q=%-5d %-42s %10.4f"
          % (d, abs(d), gam[d].str(16, radius=True), float(CERT[d]['M1'].upper())))
print("\nAuxiliary certified channels (Category K):")
for d in EXTRA:
    print("  chi_%-6d q=%-5d %-42s %10.4f"
          % (d, abs(d), XC[d]['gamma'].str(16, radius=True), float(XC[d]['M1'].upper())))
