#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_s23_verify_v1_3.py
=====================
Companion verification suite for

    ZS-S23 v1.3 -- The Action-to-Hessian Bridge on the Physical Z-Spin Carrier:
    the Metric Route, the Clock Route, and the Central-Hessian Theorem

    Kenny Kang, Z-Spin Cosmology Collaboration, July 2026

One self-contained file. No data assets, no imported mesh files, no auxiliary
scripts. Every carrier K_n = GP(n,n) is generated from the 12 icosahedron
vertices and the Eisenstein (Goldberg-Coxeter) lattice patch.

Check kinds, inherited from the ZS-S20 / ZS-S21 discipline:
    C  check     -- executable assertion on a number computed from the actual
                    Z-Spin object K_n
    P  proxy     -- auxiliary family or generic model; never counted as a
                    verification of K_n
    X  computed  -- numerical convergence / extrapolation result, NOT a theorem
    D  decl      -- registry statement with no numerical content

v1.1 REVIEW RESPONSE.  The v1.0 declaration ledger was internally inconsistent:
D174/D178/D183/D184/D193/D197 carried pre-split theorem numbers (S24.x, S22.x)
and three statements that the v1.0 BODY had already retracted -- "geometric
route selects Class M", "identity-Hessian EXACTLY Delta_S21", "STEP B closed
unconditionally".  All are corrected here; no declaration in this file now
contradicts the body.  New in v1.1:
    S18a  closed-form round-metric identities -> Theorem S23.1 becomes PROVEN
          (analytic monotonicity + IVT + a certified separating rational point)
    S18c  symmetry-forced geodesy: 3 of the 4 arcs and BOTH dual vertices are
          metric-INDEPENDENT for every I_h-invariant metric (mirror planes)
    S18d  quadrature-convergence audit -- the v1.0 residual 1.6e-14 was a SOLVER
          residual; the true geometric residual is RESOLUTION-DEPENDENT and is
          printed by the run rather than hard-coded here
    S18e  IVT existence certificate + Jacobian/IFT branch + a third, structurally
          independent conformal profile

Fail-closed: exits non-zero on any FAIL. Emits its own SHA256.
Deterministic seed 20260320.

LOCKED, never re-fitted:  A = 35/437, Q = 11, dim Z = 2,
                          lambda_1 = 1.2428416164, lambda_h = 7.5210904061.
ZS-S23 uses NONE of these numerically outside the regression block. It uses
only the incidence data of the carrier family.

ZERO NEW FITTED PHYSICAL PARAMETERS.  The conformal probe coordinates t, a, w
are NOT physical parameters and are NOT fitted to any observation: they are
search coordinates on the space of I_h-invariant metrics, used solely to
establish NON-IDENTIFIABILITY.  n is a regulator index, not a fitted parameter.

v1.2 REVIEW RESPONSE (second cycle).  Six closure conditions:
  (1) F-S23.9 CLOSED-PASS -- the t = 7/20 separator now carries a genuine
      mpmath INTERVAL certificate, not a high-precision float evaluation, so
      Theorem S23.1 keeps status PROVEN without contradicting its own gate.
  (2) Theorem S23.2 SPLIT -- the abstract IVT lemma (PROVEN-CONDITIONAL on
      D1-D3) is separated from its application to the audited discretisation
      (VERIFIED for D1/D3, COMPUTED for D2 global monotonicity).  v1.1's
      "D1-D3 each VERIFIED, therefore existence at proof strength" was one
      grade too strong and is retracted (S23-R12).
  (3) Lemma S23.2a narrowed: symmetry forces STATIONARY geodesy, not GLOBAL
      minimality.  A multistart test is added and a new gate F-S23.12 opened.
  (4) F-S23.1 rewritten -- the v1.1 wording was logically void.
  (5) banner, residual figures, quadrature grid and FAST labelling reconciled
      with the manuscript.
  (6) "Zero Free Parameters" -> "Zero New Fitted Physical Parameters".

v1.3 REVIEW RESPONSE (third cycle) -- TERMINAL editorial / epistemic closure.
No new physics and no new claims.  Six corrections:
  (1) Corollary S23.2e demoted DERIVED -> COMPUTED.  A COMPUTED application
      cannot carry a DERIVED corollary; v1.2 asserted both.  Retraction S23-R14.
  (2) Lemma S23.2b gains hypothesis (D2b), UNIFORM ROOT BRACKETING.  Strict
      monotonicity gives uniqueness, NOT existence, of t_w(a); v1.2's proof
      said "By (D2), t_w(a) exists and is unique", which is false as stated.
      New check T176a2 tests the bracket on the whole grid.  Retraction S23-R15.
  (3) The w = 0.45 monotonicity/curvature audit is now actually executed
      (v1.2 tabulated it but computed only w = 0.60), and the geodesic-corrected
      root is now computed here instead of being quoted from an off-line run.
      New checks T176a.45, T170m.
  (4) COMPUTED-status entries are reclassified from kind C to kind X, so the
      ledger no longer contradicts the manuscript's epistemic demotions.
  (5) Theorem S23.4 regularity corrected: C^2 gives o(a^2), not O(a^3).
  (6) The claim that the conformal potential is non-smooth IN THE AMPLITUDE is
      withdrawn: dependence on a is smooth; the max over twelve axes is
      non-smooth in the SPATIAL argument, hence in t, at Voronoi boundaries.
"""

import os
import sys
import time
import hashlib
import numpy as np
import mpmath as mp
import scipy.sparse as sp
import scipy.sparse.linalg as sla
from scipy.spatial import ConvexHull

np.random.seed(20260320)

PHI = (1.0 + 5.0 ** 0.5) / 2.0

A_LOCK = 35.0 / 437.0
Q_LOCK = 11
DIMZ_LOCK = 2
LAM1_LOCK = 1.2428416164
LAMH_LOCK = 7.5210904061

S21_TABLE = {
    "counting": [1.2428416164, 3.2679491924, 4.8443660283, 6.0000000000,
                 6.7320508076, 7.5210904061, 8.0000000000, 8.3917019492],
    "cfl": [1.2202641716, 3.2426532809, 5.1280732201, 5.9288147079,
            6.8374309601, 7.4839523690, 7.5635898643, 8.4499002960,
            9.0172479099],
    "fullmetric": [1.2069213135, 3.2021584823, 5.0114038007, 5.9240580690,
                   6.5914753301, 7.5015797384, 7.6668698858, 8.6855691448,
                   9.2889568387],
}
S21_SIGMA = 0.8973272361
S21_RHO = 1.5100902868

PHI_G = (1.0 + 5.0 ** 0.5) / 2.0
_CLI = ["E", "C5", "C5sq", "C3", "C2"]
_I_CH = {"A": [1, 1, 1, 1, 1],
         "T1": [3, PHI_G, 1 - PHI_G, 0, -1],
         "T2": [3, 1 - PHI_G, PHI_G, 0, -1],
         "G": [4, -1, -1, 1, 0],
         "H": [5, 0, 0, -1, 1]}
_DIM = {"A": 1, "T1": 3, "T2": 3, "G": 4, "H": 5}
IRREPS = [x + p for x in ["A", "T1", "T2", "G", "H"] for p in ("g", "u")]
IRDIM = {x + p: _DIM[x] for x in _DIM for p in ("g", "u")}


def build_Ih():
    """I_h as 120 orthogonal 3x3 matrices preserving the icosahedron vertex set."""
    import itertools
    IV, _ = icosahedron()
    base = IV[:3]
    S = set(map(tuple, np.round(IV, 5)))
    out = []
    for perm in itertools.permutations(range(12), 3):
        M = np.linalg.lstsq(base, IV[list(perm)], rcond=None)[0]
        if not np.allclose(M.T @ M, np.eye(3), atol=1e-7):
            continue
        if set(map(tuple, np.round(IV @ M, 5))) != S:
            continue
        if not any(np.allclose(M, X, atol=1e-7) for X in out):
            out.append(M)
    return out


def _rot_class(R):
    t = np.trace(R)
    for nm, val in [("E", 3.0), ("C5", 1 + 2 * np.cos(2 * np.pi / 5)),
                    ("C5sq", 1 + 2 * np.cos(4 * np.pi / 5)),
                    ("C3", 0.0), ("C2", -1.0)]:
        if abs(t - val) < 1e-6:
            return nm
    raise ValueError(t)


def Ih_data(G):
    """I_h = I x Z2 : g = eps * r with eps = det g and r in I."""
    return [(int(round(np.linalg.det(M))), _rot_class(int(round(np.linalg.det(M))) * M))
            for M in G]


def chi(al, g):
    x, p = al[:-1], al[-1]
    eps, c = g
    val = _I_CH[x][_CLI.index(c)]
    return val if p == "g" else eps * val


def face_perms(c, G):
    key = {tuple(np.round(p, 5)): i for i, p in enumerate(c["P"])}
    return [np.array([key[tuple(np.round(q, 5))] for q in c["P"] @ M]) for M in G]


def projectors(c, G, GD, prm):
    F = c["F_K"]
    out = {}
    idx = np.arange(F)
    for al in IRREPS:
        Pm = np.zeros((F, F))
        for g, p in zip(GD, prm):
            Pm[p, idx] += chi(al, g)
        out[al] = IRDIM[al] / 120.0 * Pm
    return out


def dist_to_pent(c):
    N = c["F_K"]
    adj = [[] for _ in range(N)]
    for a, b in c["edges"]:
        adj[a].append(b)
        adj[b].append(a)
    d = np.full(N, -1)
    q = list(np.where(c["is5"])[0])
    for x in q:
        d[x] = 0
    while q:
        nq = []
        for x in q:
            for y in adj[x]:
                if d[y] < 0:
                    d[y] = d[x] + 1
                    nq.append(y)
        q = nq
    return d


def n_orbits(pts, G):
    key = {tuple(np.round(p, 5)): i for i, p in enumerate(pts)}
    n = len(pts)
    par = list(range(n))

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for M in G:
        for i, q in enumerate(pts @ M):
            a, b = f(i), f(key[tuple(np.round(q, 5))])
            if a != b:
                par[a] = b
    return len(set(f(i) for i in range(n)))



# ---------------------------------------------------------------- v1.2 helpers
def _arc(a, b):
    return np.arccos(np.clip(float(np.dot(a, b)), -1.0, 1.0))


def _sph_area_ordered(pts):
    c = pts.mean(0)
    c = c / np.linalg.norm(c)
    tot = 0.0
    for i in range(len(pts)):
        p, q = pts[i], pts[(i + 1) % len(pts)]
        A = _arc(p, q); B = _arc(c, q); C = _arc(c, p)
        s_ = 0.5 * (A + B + C)
        T_ = (np.tan(s_ / 2) * np.tan((s_ - A) / 2) *
              np.tan((s_ - B) / 2) * np.tan((s_ - C) / 2))
        tot += 4 * np.arctan(np.sqrt(max(T_, 0.0)))
    return tot


def truncation_geometry(t):
    """STEP A: the one-parameter I_h spherical carrier family K_TI(t).
    Truncation depth t in (0,1/2); t = 1/3 is the Archimedean carrier.
    Face centres (= dual vertices) are I_h high-symmetry points, hence
    t-INDEPENDENT, so the dual arcs are fixed and only the primal varies."""
    IV, IF = icosahedron()
    IE = []
    d = np.linalg.norm(IV[0] - IV[1:], axis=1).min()
    for i in range(12):
        for j in range(i + 1, 12):
            if abs(np.linalg.norm(IV[i] - IV[j]) - d) < 1e-9:
                IE.append((i, j))
    FC = np.array([IV[a] + IV[b] + IV[c] for a, b, c in IF])
    FC = FC / np.linalg.norm(FC, axis=1)[:, None]
    P = {}
    for (i, j) in IE:
        p = (1 - t) * IV[i] + t * IV[j]
        q = t * IV[i] + (1 - t) * IV[j]
        P[(i, j)] = p / np.linalg.norm(p)
        P[(j, i)] = q / np.linalg.norm(q)
    adj = {i: [] for i in range(12)}
    for (i, j) in IE:
        adj[i].append(j); adj[j].append(i)

    def order(pts, ctr):
        e1 = pts[0] - ctr
        e1 = e1 - np.dot(e1, ctr) * ctr
        e1 = e1 / np.linalg.norm(e1)
        e2 = np.cross(ctr, e1)
        ang = np.arctan2([np.dot(p - ctr, e2) for p in pts],
                         [np.dot(p - ctr, e1) for p in pts])
        return [pts[k] for k in np.argsort(ang)]

    pent0 = order([P[(0, j)] for j in adj[0]], IV[0])
    a, b, c = IF[0]
    hex0 = order([P[(a, b)], P[(b, a)], P[(b, c)],
                  P[(c, b)], P[(c, a)], P[(a, c)]], FC[0])
    A5 = _sph_area_ordered(np.array(pent0))
    A6 = _sph_area_ordered(np.array(hex0))
    (i, j) = IE[0]
    l66 = _arc(P[(i, j)], P[(j, i)])
    l56 = _arc(pent0[0], pent0[1])
    fi = [k for k, (x, y, z) in enumerate(IF) if 0 in (x, y, z)][0]
    d56 = _arc(IV[0], FC[fi])
    sh = [k for k, (x, y, z) in enumerate(IF) if i in (x, y, z) and j in (x, y, z)]
    d66 = _arc(FC[sh[0]], FC[sh[1]])
    return dict(t=t, A5=A5, A6=A6, l56=l56, l66=l66, d56=d56, d66=d66,
                rho=A6 / A5, sigma=(d56 / l56) / (d66 / l66),
                total=12 * A5 + 20 * A6)


def su3_generators():
    L = [np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex),
         np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex),
         np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], complex),
         np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex),
         np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex),
         np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex),
         np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex),
         np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], complex) / np.sqrt(3)]
    return [x / 2 for x in L]


def identity_hessian(Phi, Tb, h=1e-4):
    """Hessian of a function on SU(3) at the identity, in the T^a basis."""
    from scipy.linalg import expm
    H = np.zeros((8, 8))
    for a in range(8):
        for b in range(8):
            def f(x, y):
                return Phi(expm(1j * (x * Tb[a] + y * Tb[b])))
            H[a, b] = (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h)) / (4 * h * h)
    return H


def su3_heat_kernel_action(t):
    reps = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

    def C2(p, q):
        return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0

    def dim(p, q):
        return (p + 1) * (q + 1) * (p + q + 2) // 2

    def chi(pq, U):
        p, q = pq
        tr = np.trace(U)
        if (p, q) == (0, 0): return 1.0 + 0j
        if (p, q) == (1, 0): return tr
        if (p, q) == (0, 1): return np.conj(tr)
        if (p, q) == (1, 1): return abs(tr) ** 2 - 1
        if (p, q) == (2, 0): return 0.5 * (tr ** 2 + np.trace(U @ U))
        if (p, q) == (0, 2): return np.conj(0.5 * (tr ** 2 + np.trace(U @ U)))

    def K(U):
        return sum(dim(*r) * np.exp(-t * C2(*r)) * chi(r, U).real for r in reps)
    K0 = K(np.eye(3))
    return lambda U: -np.log(max(K(U), 1e-300)) + np.log(K0)


def min_edge_boundary(c):
    """global minimum edge boundary (Stoer-Wagner) of the dual graph of K_n."""
    N = c["F_K"]
    W = np.zeros((N, N))
    for a, b in c["edges"]:
        W[a, b] += 1.0
        W[b, a] += 1.0
    active = list(range(N))
    groups = {i: [i] for i in range(N)}
    best = np.inf
    bestsize = None
    Wc = W.copy()
    while len(active) > 1:
        A = [active[0]]
        rest = active[1:]
        w = {v: Wc[active[0], v] for v in rest}
        while rest:
            z = max(rest, key=lambda v: w[v])
            rest.remove(z)
            A.append(z)
            for v in rest:
                w[v] += Wc[z, v]
        t_, s_ = A[-1], A[-2]
        cut = sum(Wc[t_, v] for v in active if v != t_)
        if cut < best:
            best = cut
            bestsize = len(groups[t_])
        for v in active:
            if v not in (s_, t_):
                Wc[s_, v] += Wc[t_, v]
                Wc[v, s_] = Wc[s_, v]
        groups[s_] = groups[s_] + groups[t_]
        active.remove(t_)
    return best, bestsize

# ------------------------------------------------- v1.0 (S24) conformal freedom
def _phi_conf(p, IV, amp, w=0.6):
    """I_h-invariant conformal potential: bump on the 12 pentagon-centre axes.
    |p . IV| is antipodal-symmetric, hence invariant under the full I_h."""
    d = np.arccos(np.clip(np.abs(p @ IV.T).max(), -1.0, 1.0))
    return amp * np.exp(-(d / w) ** 2)


def _arclen_conf(a, b, IV, amp, w, n=48, pf=None):
    PF = _phi_conf if pf is None else pf
    ang = _arc(a, b)
    if ang < 1e-12:
        return 0.0
    ts = (np.arange(n) + 0.5) / n
    pts = np.array([(np.sin((1 - t) * ang) * a + np.sin(t * ang) * b) / np.sin(ang)
                    for t in ts])
    return float(np.mean(np.exp([PF(p, IV, amp, w) for p in pts])) * ang)


def _polyarea_conf(pts, IV, amp, w, n=18, pf=None):
    PF = _phi_conf if pf is None else pf
    c = pts.mean(0)
    c = c / np.linalg.norm(c)
    tot = 0.0
    for i in range(len(pts)):
        p, q = pts[i], pts[(i + 1) % len(pts)]
        A0 = _sph_area_ordered(np.array([c, p, q]))
        s_, m_ = 0.0, 0
        for a_ in range(n):
            for b_ in range(n - a_):
                u = (a_ + 1 / 3) / n
                ww = (b_ + 1 / 3) / n
                z = 1 - u - ww
                if z < 0:
                    continue
                x = u * c + ww * p + z * q
                x = x / np.linalg.norm(x)
                s_ += np.exp(2 * PF(x, IV, amp, w))
                m_ += 1
        tot += A0 * s_ / max(m_, 1)
    return tot


def conformal_sigma_rho(t, amp, w=0.6, nL=48, nA=18, pf=None):
    """(sigma, rho) of the carrier K_TI(t) in the I_h-invariant conformal metric
    e^{2 phi} g_round.  amp = 0 reproduces truncation_geometry(t).

    v1.1: the quadrature orders nL (arc panels) and nA (area subdivisions) are
    EXPOSED, because the v1.0 defaults (48, 18) are not converged and the v1.0
    'residual 1.6e-14' was a SOLVER residual on the approximate functional, not
    a geometric one.  See check T175b.  `pf` optionally overrides the conformal
    potential, allowing a structurally independent profile family."""
    PF = _phi_conf if pf is None else pf
    IV, IF = icosahedron()
    FC = np.array([IV[a] + IV[b] + IV[c] for a, b, c in IF])
    FC = FC / np.linalg.norm(FC, axis=1)[:, None]
    d0 = np.linalg.norm(IV[0] - IV[1:], axis=1).min()
    IE = [(i, j) for i in range(12) for j in range(i + 1, 12)
          if abs(np.linalg.norm(IV[i] - IV[j]) - d0) < 1e-9]
    adj = {i: [] for i in range(12)}
    for (i, j) in IE:
        adj[i].append(j); adj[j].append(i)
    P = {}
    for (i, j) in IE:
        p = (1 - t) * IV[i] + t * IV[j]
        q = t * IV[i] + (1 - t) * IV[j]
        P[(i, j)] = p / np.linalg.norm(p)
        P[(j, i)] = q / np.linalg.norm(q)

    def order(pts, ctr):
        e1 = pts[0] - ctr
        e1 = e1 - np.dot(e1, ctr) * ctr
        e1 = e1 / np.linalg.norm(e1)
        e2 = np.cross(ctr, e1)
        ang = np.arctan2([np.dot(p - ctr, e2) for p in pts],
                         [np.dot(p - ctr, e1) for p in pts])
        return [pts[k] for k in np.argsort(ang)]

    pent0 = order([P[(0, j)] for j in adj[0]], IV[0])
    a, b, c = IF[0]
    hex0 = order([P[(a, b)], P[(b, a)], P[(b, c)],
                  P[(c, b)], P[(c, a)], P[(a, c)]], FC[0])
    A5 = _polyarea_conf(np.array(pent0), IV, amp, w, n=nA, pf=PF)
    A6 = _polyarea_conf(np.array(hex0), IV, amp, w, n=nA, pf=PF)
    (i, j) = IE[0]
    l66 = _arclen_conf(P[(i, j)], P[(j, i)], IV, amp, w, n=nL, pf=PF)
    l56 = _arclen_conf(pent0[0], pent0[1], IV, amp, w, n=nL, pf=PF)
    fi = [k for k, (x, y, z) in enumerate(IF) if 0 in (x, y, z)][0]
    d56 = _arclen_conf(IV[0], FC[fi], IV, amp, w, n=nL, pf=PF)
    sh = [k for k, (x, y, z) in enumerate(IF)
          if i in (x, y, z) and j in (x, y, z)]
    d66 = _arclen_conf(FC[sh[0]], FC[sh[1]], IV, amp, w, n=nL, pf=PF)
    return (d56 / l56) / (d66 / l66), A6 / A5


LEDGER = []
FAILED = []


def rec(tag, kind, ok, msg):
    LEDGER.append((tag, kind, "PASS" if ok else "FAIL", msg))
    if not ok:
        FAILED.append(tag)
    return ok


def check(tag, ok, msg):
    return rec(tag, "C", bool(ok), msg)


def proxy(tag, ok, msg):
    return rec(tag, "P", bool(ok), msg)


def computed(tag, ok, msg):
    return rec(tag, "X", bool(ok), msg)


def decl(tag, msg):
    LEDGER.append((tag, "D", "DECL", msg))


# =====================================================================
# 1.  CARRIER CONSTRUCTION
# =====================================================================

def icosahedron():
    v = []
    for s1 in (+1, -1):
        for s2 in (+1, -1):
            v.append((0.0, s1 * 1.0, s2 * PHI))
            v.append((s1 * 1.0, s2 * PHI, 0.0))
            v.append((s1 * PHI, 0.0, s2 * 1.0))
    V = np.array(v) / np.sqrt(1.0 + PHI * PHI)
    d = np.linalg.norm(V[0] - V[1:], axis=1).min()
    faces = []
    for i in range(12):
        for j in range(i + 1, 12):
            for k in range(j + 1, 12):
                if (abs(np.linalg.norm(V[i] - V[j]) - d) < 1e-9 and
                        abs(np.linalg.norm(V[j] - V[k]) - d) < 1e-9 and
                        abs(np.linalg.norm(V[i] - V[k]) - d) < 1e-9):
                    faces.append((i, j, k))
    return V, faces


def gc_patch(h, k):
    e1 = np.array([1.0, 0.0])
    e2 = np.array([0.5, np.sqrt(3.0) / 2.0])
    p1 = h * e1 + k * e2
    c60, s60 = 0.5, np.sqrt(3.0) / 2.0
    p2 = np.array([c60 * p1[0] - s60 * p1[1], s60 * p1[0] + c60 * p1[1]])
    M = np.column_stack([e1, e2])
    corners = np.linalg.solve(M, np.column_stack([np.zeros(2), p1, p2]))
    lo = np.floor(corners.min(axis=1)).astype(int) - 2
    hi = np.ceil(corners.max(axis=1)).astype(int) + 2
    Tinv = np.linalg.inv(np.column_stack([p1, p2]))
    out = []
    for i in range(lo[0], hi[0] + 1):
        for j in range(lo[1], hi[1] + 1):
            u, v = Tinv @ (i * e1 + j * e2)
            w = 1.0 - u - v
            if u > -1e-9 and v > -1e-9 and w > -1e-9:
                out.append((max(w, 0.0), max(u, 0.0), max(v, 0.0)))
    return np.array(out)


def geodesic(h, k):
    IV, IF = icosahedron()
    bary = gc_patch(h, k)
    pts, key = [], {}
    for (fa, fb, fc) in IF:
        Aa, Bb, Cc = IV[fa], IV[fb], IV[fc]
        for (w0, w1, w2) in bary:
            p = w0 * Aa + w1 * Bb + w2 * Cc
            p = p / np.linalg.norm(p)
            kk = tuple(np.round(p, 6))
            if kk not in key:
                key[kk] = len(pts)
                pts.append(p)
    P = np.array(pts)
    hull = ConvexHull(P, qhull_options="Qt")
    tri, seen = [], set()
    for t in hull.simplices:
        key3 = tuple(sorted(int(x) for x in t))
        if key3 not in seen:
            seen.add(key3)
            tri.append(key3)
    ed = set()
    for (a, b, c) in tri:
        ed.add((min(a, b), max(a, b)))
        ed.add((min(b, c), max(b, c)))
        ed.add((min(a, c), max(a, c)))
    edges = np.array(sorted(ed))
    deg = np.zeros(len(P), dtype=int)
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    return P, edges, tri, deg


def carrier(n, h=None, k=None):
    h = n if h is None else h
    k = n if k is None else k
    P, edges, tri, deg = geodesic(h, k)
    is5 = (deg == 5)
    d0 = is5[edges[:, 0]]
    d1 = is5[edges[:, 1]]
    return dict(n=n, P=P, edges=edges, tris=tri, deg=deg, is5=is5,
                V_K=len(tri), E_K=len(edges), F_K=len(P),
                defect_edge=(d0 | d1), adj_pent=int((d0 & d1).sum()),
                n_pent=int(is5.sum()))


# =====================================================================
# 2.  THE OPERATOR (Lemma S22.0, imported from ZS-S22 v1.3)
# =====================================================================

def delta(c, sigma=1.0, rho=1.0, edge_w=None, vert_w=None):
    edges = c["edges"]
    N = c["F_K"]
    if edge_w is None:
        edge_w = np.where(c["defect_edge"], 1.0 / sigma, 1.0)
    if vert_w is None:
        vert_w = np.where(c["is5"], rho, 1.0)
    a, b = edges[:, 0], edges[:, 1]
    rows = np.concatenate([a, b, a, b])
    cols = np.concatenate([a, b, b, a])
    vals = np.concatenate([edge_w, edge_w, -edge_w, -edge_w])
    L = sp.coo_matrix((vals, (rows, cols)), shape=(N, N)).tocsr()
    S = sp.diags(np.sqrt(vert_w))
    return (S @ L @ S).tocsr()


def incidence_B2(c):
    N, E = c["F_K"], c["E_K"]
    B = np.zeros((N, E))
    for i, (u, v) in enumerate(c["edges"]):
        B[u, i] = +1.0
        B[v, i] = -1.0
    return B


def spectrum(c, edge_w=None, vert_w=None, K=12, sigma=1.0, rho=1.0):
    L = delta(c, sigma, rho, edge_w, vert_w)
    N = L.shape[0]
    if N < 700:
        ev = np.sort(np.linalg.eigvalsh(L.toarray()))
    else:
        ev = np.sort(sla.eigsh(L, k=min(N - 2, 4 * K + 12), sigma=-1e-8,
                               which="LM", return_eigenvectors=False))
    ev = ev[ev > 1e-9 * max(1.0, ev.max())]
    lev = []
    for x in ev:
        if lev and abs(x - lev[-1][0]) < 1e-6 * max(1.0, abs(x)):
            lev[-1][1] += 1
        else:
            lev.append([x, 1])
    return lev[:K]


# =====================================================================
# 3.  BRANCHES
# =====================================================================

def circumcenters(P, tris):
    Aa = P[[t[0] for t in tris]]
    Bb = P[[t[1] for t in tris]]
    Cc = P[[t[2] for t in tris]]
    a = Bb - Aa
    b = Cc - Aa
    nrm = np.cross(a, b)
    n2 = (nrm * nrm).sum(1)[:, None]
    return Aa + np.cross((a * a).sum(1)[:, None] * b -
                         (b * b).sum(1)[:, None] * a, nrm) / (2 * n2)


def sph_poly_area(pts):
    c = pts.mean(0)
    c = c / np.linalg.norm(c)
    tot = 0.0
    for i in range(len(pts)):
        p, q = pts[i], pts[(i + 1) % len(pts)]
        a = np.arccos(np.clip(np.dot(p, q), -1, 1))
        b = np.arccos(np.clip(np.dot(c, q), -1, 1))
        d = np.arccos(np.clip(np.dot(c, p), -1, 1))
        s = 0.5 * (a + b + d)
        t = (np.tan(s / 2) * np.tan((s - a) / 2) *
             np.tan((s - b) / 2) * np.tan((s - d) / 2))
        tot += 4 * np.arctan(np.sqrt(max(t, 0.0)))
    return tot


def dec_weights(c, spherical=True):
    P, edges, tris = c["P"], c["edges"], c["tris"]
    cc = circumcenters(P, tris)
    if spherical:
        cc = cc / np.linalg.norm(cc, axis=1)[:, None]
    eidx = {(int(u), int(v)): i for i, (u, v) in enumerate(map(tuple, edges))}
    inc = [[] for _ in range(len(edges))]
    for ti, t in enumerate(tris):
        for a, b in ((t[0], t[1]), (t[1], t[2]), (t[0], t[2])):
            inc[eidx[(min(a, b), max(a, b))]].append(ti)
    ew = np.zeros(len(edges))
    for ei, (u, v) in enumerate(edges):
        c1, c2 = cc[inc[ei][0]], cc[inc[ei][1]]
        if spherical:
            dual = np.arccos(np.clip(np.dot(c1, c2), -1, 1))
            prim = np.arccos(np.clip(np.dot(P[u], P[v]), -1, 1))
        else:
            dual = np.linalg.norm(c1 - c2)
            prim = np.linalg.norm(P[u] - P[v])
        ew[ei] = dual / prim
    vt = [[] for _ in range(len(P))]
    for ti, t in enumerate(tris):
        for v in t:
            vt[v].append(ti)
    Ar = np.zeros(len(P))
    for v in range(len(P)):
        pts = cc[vt[v]]
        ctr = P[v]
        e1 = pts[0] - ctr
        e1 = e1 - np.dot(e1, ctr) * ctr
        e1 = e1 / np.linalg.norm(e1)
        e2 = np.cross(ctr, e1)
        ang = np.arctan2([np.dot(p - ctr, e2) for p in pts],
                         [np.dot(p - ctr, e1) for p in pts])
        pts = pts[np.argsort(ang)]
        if spherical:
            Ar[v] = sph_poly_area(pts)
        else:
            g = pts.mean(0)
            Ar[v] = sum(0.5 * np.linalg.norm(
                np.cross(pts[i] - g, pts[(i + 1) % len(pts)] - g))
                for i in range(len(pts)))
    beta = 1.0 / Ar
    ew = ew / np.median(ew[~c["defect_edge"]])
    beta = beta / np.median(beta[~c["is5"]])
    return ew, beta


def branch(c, name):
    if name == "C":
        return np.ones(c["E_K"]), np.ones(c["F_K"])
    if name == "S21f":
        return (np.where(c["defect_edge"], 1.0 / S21_SIGMA, 1.0),
                np.where(c["is5"], S21_RHO, 1.0))
    if name == "FLAT":
        return np.ones(c["E_K"]), 6.0 / c["deg"].astype(float)
    if name == "psi+":
        pe = c["deg"][c["edges"][:, 0]] + c["deg"][c["edges"][:, 1]]
        return 12.0 / pe.astype(float), c["deg"].astype(float) / 6.0
    if name == "psi-":
        pe = c["deg"][c["edges"][:, 0]] + c["deg"][c["edges"][:, 1]]
        return pe.astype(float) / 12.0, 6.0 / c["deg"].astype(float)
    if name == "S-DEC":
        return dec_weights(c, spherical=True)
    if name == "P-DEC":
        return dec_weights(c, spherical=False)
    raise ValueError(name)


MF_BRANCHES = ["C", "S21f", "FLAT", "psi+", "psi-"]
M_BRANCHES = ["S-DEC", "P-DEC"]


def fit_1_over_n2(ns, ys):
    ns = np.array(ns, float)
    X = np.column_stack([np.ones(len(ns)), ns ** -2, ns ** -4])
    co = np.linalg.lstsq(X, np.array(ys), rcond=None)[0]
    return co[0], (lambda m: co[0] + co[1] / m ** 2 + co[2] / m ** 4)


# =====================================================================
# 4.  VERIFICATION PROGRAMME
# =====================================================================

def main():
    FAST = os.environ.get("ZS_S23_FAST", "") == "1"
    _T0 = time.time()
    print("BEGIN_ZS_S23_RESULTS")
    print("ZS-S23 v1.3 verification companion -- fail-closed")
    if FAST:
        print("MODE = FAST / NON-PUBLICATION VERIFICATION")
        print("  Structural checks run under REDUCED quadrature. The "
              "full-resolution publication")
        print("  ledger is NOT executed in this mode, and residual figures below "
              "will differ")
        print("  from the manuscript. Unset ZS_S23_FAST to reproduce the paper.")
    else:
        print("MODE = FULL / PUBLICATION VERIFICATION")
    print("LOCKED: A = 35/437 = %.12f | Q = %d | dim Z = %d | "
          "lambda_1 = %.10f | lambda_h = %.10f"
          % (A_LOCK, Q_LOCK, DIMZ_LOCK, LAM1_LOCK, LAMH_LOCK))
    decl("D000", "ZS-S23 introduces zero new constants and ZERO NEW FITTED "
                 "PHYSICAL PARAMETERS. The conformal probe coordinates t, a, w are "
                 "search coordinates on the space of I_h-invariant metrics, used "
                 "only to establish non-identifiability; they are not physical "
                 "predictions and are not fitted to observation. n is a regulator "
                 "index sent to infinity, not a fitted parameter.")
    decl("D001", "(H-W), (Z-A0), (Z-A1) are imported from ZS-S21 v1.3 and "
                 "are not re-derived here.")

    NS = [1, 2, 3, 4, 5, 6, 8, 10, 12]
    CAR = {}

    print("\n[S1] Theorem S22.1 (IMPORTED from ZS-S22 v1.3) -- Goldberg-Coxeter census")
    print("  %3s %7s %7s %7s %6s %8s %9s"
          % ("n", "V_n", "E_n", "F_n", "pent", "E_(5,6)", "isolated"))
    for n in NS:
        c = carrier(n)
        CAR[n] = c
        check("T010.%d" % n,
              c["V_K"] == 60 * n * n and c["E_K"] == 90 * n * n
              and c["F_K"] == 30 * n * n + 2,
              "census (60n^2, 90n^2, 30n^2+2) at n=%d" % n)
        check("T011.%d" % n, c["n_pent"] == 12, "12 pentagons at n=%d" % n)
        check("T012.%d" % n, int(c["defect_edge"].sum()) == 60,
              "60 (5,6) edges at n=%d" % n)
        check("T013.%d" % n, c["adj_pent"] == 0,
              "isolated pentagons at n=%d" % n)
        check("T014.%d" % n, c["V_K"] - c["E_K"] + c["F_K"] == 2,
              "chi = 2 at n=%d" % n)
        print("  %3d %7d %7d %7d %6d %8d %9s"
              % (n, c["V_K"], c["E_K"], c["F_K"], c["n_pent"],
                 int(c["defect_edge"].sum()), c["adj_pent"] == 0))
    check("T015", all(3 * CAR[n]["V_K"] == 2 * CAR[n]["E_K"] for n in NS),
          "cubic carrier: 3V = 2E for every generated n")

    print("\n[S2] Lemma S22.0 (IMPORTED from ZS-S22 v1.3) -- B_2 B_2^T = dual Laplacian")
    for n in [1, 2, 3]:
        c = CAR[n]
        B = incidence_B2(c)
        d = np.abs(B @ B.T - delta(c, 1.0, 1.0).toarray()).max()
        check("T020.%d" % n, d < 1e-10,
              "B2 B2^T = Delta_n(1,1) at n=%d, dev %.2e" % (n, d))
        print("    n=%d  max |B2 B2^T - Delta_n(1,1)| = %.3e" % (n, d))

    print("\n[S3] Gate F-S22.1 (IMPORTED) -- K_1 regression vs ZS-S21 v1.3 Table 6.2")
    c1 = CAR[1]
    for nm, key, sg, rh in [("counting", "counting", 1.0, 1.0),
                            ("spatial CFL", "cfl", 1.0, S21_RHO),
                            ("full metric", "fullmetric", S21_SIGMA, S21_RHO)]:
        L = delta(c1, sg, rh).toarray()
        r = 180.0 / np.trace(L)
        ev = np.sort(np.linalg.eigvalsh(L))[1:] * r
        lv = []
        for x in ev:
            if not lv or abs(x - lv[-1]) > 1e-7:
                lv.append(x)
        d = max(abs(a - b) for a, b in zip(lv, S21_TABLE[key]))
        check("T030.%s" % key, d < 1e-8,
              "K_1 %s branch matches ZS-S21, dev %.2e" % (nm, d))
        print("    %-12s levels=%d  max |computed - ZS-S21| = %.3e"
              % (nm, len(lv), d))
    ev1 = np.sort(np.linalg.eigvalsh(delta(c1, 1, 1).toarray()))
    check("T031", abs(ev1[1] - LAM1_LOCK) < 1e-9,
          "LOCKED lambda_1 reproduced, dev %.2e" % abs(ev1[1] - LAM1_LOCK))
    check("T032", abs(ev1[21] - LAMH_LOCK) < 1e-8,
          "LOCKED lambda_h reproduced, dev %.2e" % abs(ev1[21] - LAMH_LOCK))
    print("    LOCKED lambda_1 = %.10f (dev %.2e) | lambda_h = %.10f (dev %.2e)"
          % (ev1[1], abs(ev1[1] - LAM1_LOCK), ev1[21],
             abs(ev1[21] - LAMH_LOCK)))
    print("\n[S18] Theorem S23.1 -- STEP A, the round-metric no-go")
    print("    In 2 spatial dimensions the Hodge star on 2-forms maps Omega^2 -> Omega^0.")
    print("    UNDER A CELLWISE-CONSTANT (mass-lumped, lowest-order Whitney) REDUCTION,")
    print("    and NOT exactly, Int_f Tr(F ^ *F) = Tr(Phi_f^2)/A_f, i.e. beta_f = 1/A_f.")
    print("    Cauchy-Schwarz gives only an inequality in general, and in the non-abelian")
    print("    case Phi_f = Int_f F is NOT the holonomy (non-abelian Stokes). [S23-R2]")
    print("    The residual freedom IN THE ROUND METRIC is the I_h carrier geometry, a")
    print("    ONE-parameter family (a 60-point I_h orbit has a Z_2 stabiliser).")
    from scipy.optimize import brentq
    g13 = truncation_geometry(1.0 / 3.0)
    check("T170", abs(g13["total"] - 4 * np.pi) < 1e-6,
          "spherical areas close: 12A5 + 20A6 = 4pi (residual %.2e)"
          % abs(g13["total"] - 4 * np.pi))
    d56, d66 = g13["d56"], g13["d66"]
    g25 = truncation_geometry(0.25)
    check("T171", abs(g25["d56"] - d56) < 1e-12 and abs(g25["d66"] - d66) < 1e-12,
          "dual arcs are t-independent (face centres are I_h fixed points)")
    print("    %8s %11s %11s %12s %11s %11s" %
          ("t", "A5", "A6", "rho=A6/A5", "sigma", "12A5+20A6"))
    for t_ in [0.10, 0.20, 0.25, 1.0 / 3.0, 0.40, 0.45]:
        gg = truncation_geometry(t_)
        print("    %8.4f %11.6f %11.6f %12.6f %11.6f %11.7f"
              % (t_, gg["A5"], gg["A6"], gg["rho"], gg["sigma"], gg["total"]))
    t_rho = brentq(lambda t: truncation_geometry(t)["rho"] - 1, 0.05, 0.49, xtol=1e-13)
    t_sig = brentq(lambda t: truncation_geometry(t)["sigma"] - 1, 0.05, 0.49, xtol=1e-13)
    s_at_rho = truncation_geometry(t_rho)["sigma"]
    r_at_sig = truncation_geometry(t_sig)["rho"]
    print("    equal-area  rho = 1 at t = %.10f  ->  sigma = %.10f" % (t_rho, s_at_rho))
    print("    sigma = 1          at t = %.10f  ->  rho   = %.10f" % (t_sig, r_at_sig))
    print("    Archimedean t = 1/3            ->  (sigma, rho) = (%.10f, %.10f)"
          % (g13["sigma"], g13["rho"]))
    check("T172", abs(t_rho - t_sig) > 1e-3,
          "IN THE ROUND METRIC no t gives sigma = rho = 1 : "
          "|t_rho - t_sigma| = %.4e" % abs(t_rho - t_sig))
    check("T173", abs(s_at_rho - 1) > 0.3 and abs(r_at_sig - 1) > 0.3,
          "the (sigma,rho) trajectory misses (1,1) by a wide margin")
    decl("D174", "Theorem S23.1 is scoped to the ROUND metric. It does NOT say that "
                 "no metric realises orbit-blindness; see Theorem S23.2. Its status "
                 "in v1.1 is PROVEN, not 'PROVEN by exhibition': section S18a supplies "
                 "closed forms for r5(t), A5(t), l56(t), l66(t) and exact t-independent "
                 "dual arcs, from which strict monotonicity of sigma and rho follows "
                 "analytically, root uniqueness follows from monotonicity, and the "
                 "strict separation t_sigma < 7/20 < t_rho is certified at a single "
                 "rational point.")

    # =================================================================
    # S18a  CLOSED-FORM ROUND-METRIC IDENTITIES  (v1.1: S23.1 -> PROVEN)
    # =================================================================
    print("\n[S18a] Theorem S23.1 upgraded to PROVEN -- closed forms + monotonicity")
    print("    c := V_i . V_j = 1/sqrt5 for adjacent icosahedron vertices.  Then")
    print("      tan r5(t)     = t sqrt(1-c^2) / (1 - t(1-c))          [strictly incr]")
    print("      A5(t)         = 10 arctan(cot(pi/5)/cos r5) - 3 pi    [strictly incr]")
    print("      A6            = (pi - 3 A5)/5     (area closure)      [strictly decr]")
    print("      rho(t)        = pi/(5 A5) - 3/5                       [strictly decr]")
    print("      l56(t)        = 2 arcsin(sin r5 sin(pi/5))            [strictly incr]")
    print("      l66(t)        = 2 arctan((1-2t) sqrt((1-c)/(1+c)))    [strictly decr]")
    print("      cos d56       = sqrt(1/3 + 2 sqrt5/15),  cos d66 = sqrt5/3   [exact]")
    print("      sigma(t)      = (d56/d66)(l66/l56)                    [strictly decr]")
    mp.mp.dps = 40
    cc = mp.mpf(1) / mp.sqrt(5)

    def _r5(t):
        t = mp.mpf(t); return mp.atan(t * mp.sqrt(1 - cc ** 2) / (1 - t * (1 - cc)))

    def _A5(t):
        return 10 * mp.atan(mp.cot(mp.pi / 5) / mp.cos(_r5(t))) - 3 * mp.pi

    def _rho(t):
        return mp.pi / (5 * _A5(t)) - mp.mpf(3) / 5

    def _l56(t):
        return 2 * mp.asin(mp.sin(_r5(t)) * mp.sin(mp.pi / 5))

    def _l66(t):
        t = mp.mpf(t); return 2 * mp.atan((1 - 2 * t) * mp.sqrt((1 - cc) / (1 + cc)))

    _D56 = mp.acos(mp.sqrt(mp.mpf(1) / 3 + 2 * mp.sqrt(5) / 15))
    _D66 = mp.acos(mp.sqrt(5) / 3)

    def _sig(t):
        return (_D56 / _l56(t)) * (_l66(t) / _D66)

    dev = max(float(abs(_A5(t_) - truncation_geometry(t_)["A5"]))
              for t_ in (0.15, 0.25, 1.0 / 3.0, 0.42))
    check("T170a", dev < 1e-12,
          "closed-form A5(t) reproduces the constructed spherical area, dev %.2e" % dev)
    devd = max(float(abs(_D56 - mp.mpf(g13["d56"]))), float(abs(_D66 - mp.mpf(g13["d66"]))))
    check("T170b", devd < 1e-12,
          "exact dual arcs cos d56 = sqrt(1/3+2sqrt5/15), cos d66 = sqrt5/3, dev %.2e" % devd)
    devs = max(float(abs(_sig(t_) - truncation_geometry(t_)["sigma"]))
               for t_ in (0.15, 0.25, 1.0 / 3.0, 0.42))
    check("T170c", devs < 1e-11,
          "closed-form sigma(t) reproduces the constructed sigma, dev %.2e" % devs)
    grid = [mp.mpf('0.05') + mp.mpf(k) / 400 for k in range(0, 177)]
    dmax_r = max(mp.diff(_rho, t_) for t_ in grid)
    dmax_s = max(mp.diff(_sig, t_) for t_ in grid)
    check("T170d", dmax_r < 0 and dmax_s < 0,
          "d rho/dt <= %.4f < 0 and d sigma/dt <= %.4f < 0 on [0.05, 0.49]: BOTH "
          "STRICTLY DECREASING, hence each has AT MOST ONE root"
          % (float(dmax_r), float(dmax_s)))
    _cf = mp.cot(mp.pi / 5) * mp.cot(5 * mp.pi / 16)
    _trho = mp.findroot(lambda t_: _rho(t_) - 1, mp.mpf(t_rho))
    check("T170e", abs(_A5(_trho) - mp.pi / 8) < mp.mpf('1e-25')
          and abs(mp.cos(_r5(_trho)) - _cf) < mp.mpf('1e-25')
          and abs(_trho - mp.mpf(t_rho)) < mp.mpf('1e-11'),
          "CLOSED FORM for the equal-area point: rho = 1 <=> A5 = pi/8 <=> "
          "cos r5 = cot(pi/5) cot(5pi/16) = %.13f" % float(_cf))
    _ts = mp.mpf(7) / 20
    sg7, rh7 = _sig(_ts), _rho(_ts)
    check("T170f", sg7 < 1 and rh7 > 1,
          "SEPARATOR t = 7/20 (floating point, 40 dps): sigma = %.16f < 1 < %.16f "
          "= rho" % (float(sg7), float(rh7)))
    print("    sigma(7/20) = %.16f  <  1  <  %.16f = rho(7/20)"
          % (float(sg7), float(rh7)))

    # ---- v1.3: GENUINE INTERVAL CERTIFICATE, gate F-S23.9 ------------------
    iv = mp.iv
    iv.dps = 50

    def _I(x):
        return iv.mpf(x)

    def _iatan(x):
        return iv.atan2(x, _I(1))

    def _iacos_pos(x):
        return _iatan(iv.sqrt(_I(1) - x * x) / x)

    def _iasin(x):
        return _iatan(x / iv.sqrt(_I(1) - x * x))

    def _iv_sig_rho(tq):
        PIv = iv.pi
        cq = _I(1) / iv.sqrt(_I(5))
        tanr = tq * iv.sqrt(_I(1) - cq * cq) / (_I(1) - tq * (_I(1) - cq))
        rq = _iatan(tanr)
        cot5 = iv.cos(PIv / 5) / iv.sin(PIv / 5)
        Aq = 10 * _iatan(cot5 / iv.cos(rq)) - 3 * PIv
        rhq = PIv / (5 * Aq) - _I(3) / _I(5)
        L56 = 2 * _iasin(iv.sin(rq) * iv.sin(PIv / 5))
        L66 = 2 * _iatan((_I(1) - 2 * tq) * iv.sqrt((_I(1) - cq) / (_I(1) + cq)))
        D56 = _iacos_pos(iv.sqrt(_I(1) / _I(3) + 2 * iv.sqrt(_I(5)) / _I(15)))
        D66 = _iacos_pos(iv.sqrt(_I(5)) / _I(3))
        return (D56 / D66) * (L66 / L56), rhq

    _S, _R = _iv_sig_rho(_I(7) / _I(20))
    check("T170f-iv", _S.b < 1 and _R.a > 1,
          "INTERVAL CERTIFICATE (mpmath.iv, 50 dps), gate F-S23.9: rigorous outer "
          "enclosures at t = 7/20 give sup sigma <= %.18f < 1 and inf rho >= %.18f > "
          "1, with enclosure widths %.2e and %.2e. This is an ENCLOSURE, not a "
          "high-precision float evaluation, so Theorem S23.1's separator is CERTIFIED "
          "and F-S23.9 is CLOSED-PASS."
          % (float(_S.b), float(_R.a), float(_S.b - _S.a), float(_R.b - _R.a)))
    check("T170f-r", _S.b < mp.mpf(765) / 1000 and _R.a > mp.mpf(1304) / 1000,
          "quotable RATIONAL bounds certified: sigma(7/20) < 765/1000 and "
          "rho(7/20) > 1304/1000")
    _Sa, _Ra = _iv_sig_rho(_I(1) / _I(4))
    _Sb, _Rb = _iv_sig_rho(_I(2) / _I(5))
    check("T170f-b", _Sa.a > 1 and _Sb.b < 1 and _Ra.a > 1 and _Rb.b < 1,
          "the IVT bracket endpoints are certified as well: at t = 1/4 both sigma and "
          "rho are rigorously > 1, at t = 2/5 both are rigorously < 1, so EXISTENCE of "
          "each root is enclosed as well as uniqueness")
    print("    INTERVAL CERT: sigma(7/20) in [%.15f, %.15f], rho(7/20) in "
          "[%.15f, %.15f]" % (float(_S.a), float(_S.b), float(_R.a), float(_R.b)))
    decl("D174a", "Theorem S23.1 (Round-Metric No-Go) is PROVEN in v1.1, superseding "
                  "v1.0's 'PROVEN by exhibition'. Proof: (i) tan r5(t) is a ratio of a "
                  "positive strictly increasing numerator and a positive strictly "
                  "decreasing denominator on (0,1/2), so r5 is strictly increasing; "
                  "(ii) A5 is strictly increasing in r5 and A6 = (pi-3A5)/5 by area "
                  "closure, so rho = pi/(5 A5) - 3/5 is strictly decreasing; (iii) l56 "
                  "is strictly increasing and l66 strictly decreasing in t while d56, "
                  "d66 are t-independent I_h-fixed-point data, so sigma is strictly "
                  "decreasing; (iv) strict monotonicity gives at most one root each and "
                  "the intermediate value theorem gives at least one; (v) the single "
                  "rational point t = 7/20 satisfies sigma < 1 < rho, certified in v1.2 by a "
                  "genuine mpmath INTERVAL enclosure (T170f-iv), which by monotonicity "
                  "forces t_sigma < 7/20 < t_rho. The IVT bracket endpoints t = 1/4 "
                  "and t = 2/5 are enclosed too (T170f-b). No numerical root find "
                  "enters the proof, and gate F-S23.9 is CLOSED-PASS. Scope: the ROUND "
                  "metric only.")

    # =================================================================
    # S18c  SYMMETRY-FORCED GEODESY  (v1.1, new)
    # =================================================================
    print("\n[S18c] Lemma S23.2a -- which carrier data are metric-INDEPENDENT")
    print("    Fixed-point sets of isometries are totally geodesic, and the unique fixed")
    print("    point of a face stabiliser is the circumcentre for EVERY invariant metric.")
    IVv, IFf = icosahedron()
    FCc = np.array([IVv[a] + IVv[b] + IVv[c] for a, b, c in IFf])
    FCc = FCc / np.linalg.norm(FCc, axis=1)[:, None]

    def _rotm(ax, an):
        a_ = ax / np.linalg.norm(ax)
        K = np.array([[0, -a_[2], a_[1]], [a_[2], 0, -a_[0]], [-a_[1], a_[0], 0]])
        return np.eye(3) + np.sin(an) * K + (1 - np.cos(an)) * K @ K

    Ggr = [np.eye(3)]
    gens = [_rotm(IVv[0], 2 * np.pi / 5), _rotm(FCc[0], 2 * np.pi / 3), -np.eye(3)]
    ch = True
    while ch:
        ch = False
        for g_ in list(Ggr):
            for h_ in gens:
                m_ = h_ @ g_
                if not any(np.abs(m_ - x_).max() < 1e-9 for x_ in Ggr):
                    Ggr.append(m_); ch = True
    check("T170g", len(Ggr) == 120, "full icosahedral group I_h reconstructed, |I_h| = %d"
          % len(Ggr))
    mirrors = []
    for g_ in Ggr:
        if (abs(np.linalg.det(g_) + 1) < 1e-9 and abs(np.trace(g_) - 1) < 1e-9
                and np.abs(g_ @ g_ - np.eye(3)).max() < 1e-9):
            w_, v_ = np.linalg.eigh(g_)
            nv = v_[:, int(np.argmin(w_))]
            if not any(min(np.linalg.norm(nv - m_), np.linalg.norm(nv + m_)) < 1e-8
                       for m_ in mirrors):
                mirrors.append(nv)
    check("T170h", len(mirrors) == 15, "I_h has %d distinct mirror planes" % len(mirrors))

    def _inmir(p_, q_):
        return any(abs(p_ @ m_) < 1e-9 and abs(q_ @ m_) < 1e-9 for m_ in mirrors)

    def _stab(p_):
        return sum(1 for g_ in Ggr if np.linalg.norm(g_ @ p_ - p_) < 1e-9)

    t_a = 1.0 / 3.0
    adjc = {i_: [] for i_ in range(12)}
    d0_ = np.linalg.norm(IVv[0] - IVv[1:], axis=1).min()
    IEe = [(i_, j_) for i_ in range(12) for j_ in range(i_ + 1, 12)
           if abs(np.linalg.norm(IVv[i_] - IVv[j_]) - d0_) < 1e-9]
    for i_, j_ in IEe:
        adjc[i_].append(j_); adjc[j_].append(i_)
    Pp = {}
    for (i_, j_) in IEe:
        p_ = (1 - t_a) * IVv[i_] + t_a * IVv[j_]
        q_ = t_a * IVv[i_] + (1 - t_a) * IVv[j_]
        Pp[(i_, j_)] = p_ / np.linalg.norm(p_)
        Pp[(j_, i_)] = q_ / np.linalg.norm(q_)

    def _ord(pts, ctr):
        e1 = pts[0] - ctr; e1 = e1 - np.dot(e1, ctr) * ctr; e1 = e1 / np.linalg.norm(e1)
        e2 = np.cross(ctr, e1)
        an = np.arctan2([np.dot(p_ - ctr, e2) for p_ in pts],
                        [np.dot(p_ - ctr, e1) for p_ in pts])
        return [pts[k_] for k_ in np.argsort(an)]

    pent0 = _ord([Pp[(0, j_)] for j_ in adjc[0]], IVv[0])
    check("T170i", _stab(IVv[0]) == 10 and _stab(FCc[0]) == 6,
          "dual vertices are ISOLATED fixed points of C_5v (|Stab| = 10) and C_3v "
          "(|Stab| = 6), hence the circumcentre of EVERY I_h-invariant metric: the "
          "'fixed dual vertices' step is FORCED, not an approximation")
    i_, j_ = IEe[0]
    fi_ = [k_ for k_, (x_, y_, z_) in enumerate(IFf) if 0 in (x_, y_, z_)][0]
    sh_ = [k_ for k_, (x_, y_, z_) in enumerate(IFf)
           if i_ in (x_, y_, z_) and j_ in (x_, y_, z_)]
    m56 = _inmir(IVv[0], FCc[fi_]); m66 = _inmir(FCc[sh_[0]], FCc[sh_[1]])
    p66 = _inmir(Pp[(i_, j_)], Pp[(j_, i_)]); p56 = _inmir(pent0[0], pent0[1])
    print("    dual d56 in a mirror: %s | dual d66: %s | primal (6,6): %s | "
          "primal (5,6): %s" % (m56, m66, p66, p56))
    check("T170j", m56 and m66 and p66 and (not p56),
          "EXACTLY THREE of the four arcs lie in mirror planes and are therefore "
          "totally geodesic for EVERY I_h-invariant metric; only the primal (5,6) "
          "edge is not, and its midpoint still lies on a mirror")
    decl("D174b", "Lemma S23.2a (Symmetry-Forced STATIONARY Geodesy, PROVEN). For any "
                  "I_h-invariant metric on S^2: (i) the pentagon and hexagon "
                  "circumcentres are the unique fixed points of C_5v and C_3v and are "
                  "therefore metric-independent; (ii) the two dual arcs and the primal "
                  "(6,6) edge lie in mirror planes, and the fixed-point set of an "
                  "isometry is totally geodesic, so they are STATIONARY geodesics of "
                  "every I_h-invariant metric and their conformal lengths are exact AS "
                  "SYMMETRY-SELECTED GEODESICS, which is how this paper DEFINES the "
                  "DEC edge lengths. v1.2 correction: totally geodesic gives "
                  "STATIONARITY, NOT global minimality, so reading these lengths as "
                  "global metric DISTANCES requires the extra step registered at gate "
                  "F-S23.12; (iii) "
                  "only the primal (5,6) edge is not mirror-contained, so it is the "
                  "ONLY residual approximation of the audited discretisation. This "
                  "converts three quarters of the external review's 'fixed path "
                  "network' objection into a theorem and isolates the remaining "
                  "quarter, measured in S18d.")

    # =================================================================
    # S18d  QUADRATURE-CONVERGENCE AUDIT  (v1.1, the honest residual)
    # =================================================================
    print("\n[S18d] Theorem S23.2 -- quadrature audit. The v1.0 residual 1.6e-14 was a")
    print("       SOLVER residual on an approximate functional, NOT a geometric one.")
    from scipy.optimize import fsolve, brentq
    QGRID = ([(24, 12), (48, 18), (96, 32)] if FAST
             else [(24, 12), (48, 18), (96, 36), (192, 64), (384, 96)])
    NLR, NAR = QGRID[-1]
    print("    %6s %6s | %14s %14s" % ("n_arc", "n_area", "t*", "amp*"))
    qroots = {}
    for (nL_, nA_) in QGRID:
        x_ = fsolve(lambda z: np.array(conformal_sigma_rho(z[0], z[1], w=0.60,
                                                           nL=nL_, nA=nA_)) - 1.0,
                    [0.332, 0.688], xtol=1e-13)
        qroots[(nL_, nA_)] = x_
        print("    %6d %6d | %14.10f %14.10f" % (nL_, nA_, x_[0], x_[1]))
    xref = qroots[(NLR, NAR)]
    x48 = qroots[(48, 18)]
    computed("T175a", abs(x48[0] - xref[0]) < 1e-3 and abs(x48[1] - xref[1]) < 1e-1,
          "the root CONVERGES under quadrature refinement: |dt*| = %.2e, |da*| = %.2e"
          % (abs(x48[0] - xref[0]), abs(x48[1] - xref[1])))
    sg_, rh_ = conformal_sigma_rho(x48[0], x48[1], w=0.60, nL=NLR, nA=NAR)
    truer = max(abs(sg_ - 1), abs(rh_ - 1))
    computed("T175b", truer > 1e-6,
          "HONEST RESIDUAL at the %s reference grid (%d, %d): the v1.0 published root "
          "re-evaluated there gives (sigma, rho) = (%.10f, %.10f), a TRUE geometric "
          "residual of %.2e, not 1.6e-14. The figure is RESOLUTION-DEPENDENT by "
          "construction; the manuscript quotes the FULL-mode value and a FAST run "
          "legitimately prints a different one. Retraction S23-R8."
          % ("FAST" if FAST else "FULL", NLR, NAR, sg_, rh_, truer))
    print("    v1.0 root at reference quadrature: (sigma, rho) = (%.10f, %.10f)"
          % (sg_, rh_))
    print("    TRUE geometric residual = %.2e   (v1.0 quoted 1.6e-14, a SOLVER "
          "residual)" % truer)

    # =================================================================
    # S18e  IVT EXISTENCE + JACOBIAN/IFT + THIRD PROFILE
    # =================================================================
    print("\n[S18e] Theorem S23.2 -- IVT existence certificate, IFT branch, 3rd profile")
    # v1.3: the IVT / Jacobian / third-profile block runs on its own STATED working
    # grid (NLI, NAI), NOT on the finest quadrature-table grid (NLR, NAR). The
    # existence argument needs a fixed stated discretisation, not the finest one,
    # and running it at (384, 96) cost ~390 s for no epistemic gain.
    NLI, NAI = (48, 18) if FAST else (96, 32)
    print("    IVT / Jacobian / third-profile working grid = (%d, %d); the (%d, %d) "
          "grid of Table 3.3 is used only for the quadrature audit and T175b."
          % (NLI, NAI, NLR, NAR))
    s0, r0 = conformal_sigma_rho(t_sig, 0.0, nL=NLI, nA=NAI)
    check("T175", abs(s0 - 1) < 5e-5 and abs(r0 - r_at_sig) < 5e-3,
          "conformal machinery reproduces the round metric at amp = 0 "
          "(sigma %.6f, rho %.6f)" % (s0, r0))
    NLm, NAm = (48, 18) if FAST else (48, 18)
    tgrid = np.linspace(0.28, 0.40, 9 if FAST else 17)
    agrid = np.linspace(0.0, 0.90, 5 if FAST else 13)
    d2res = {}
    for wD in (0.60, 0.45):
        wr = -1e9
        brk_lo, brk_hi = 1e9, -1e9
        for a_ in agrid:
            vs = np.array([conformal_sigma_rho(t_, a_, w=wD, nL=NLm, nA=NAm)[0]
                           for t_ in tgrid])
            wr = max(wr, float((np.diff(vs) / np.diff(tgrid)).max()))
            brk_lo = min(brk_lo, float(vs[0]))     # sigma at t = 0.28, want > 1
            brk_hi = max(brk_hi, float(vs[-1]))    # sigma at t = 0.40, want < 1
        hcur, cv = 1e-3, 0.0
        for a_ in agrid[::4]:
            for t_ in tgrid[::4]:
                f0 = conformal_sigma_rho(t_, a_, w=wD, nL=NLm, nA=NAm)[0]
                fp = conformal_sigma_rho(t_ + hcur, a_, w=wD, nL=NLm, nA=NAm)[0]
                fm = conformal_sigma_rho(t_ - hcur, a_, w=wD, nL=NLm, nA=NAm)[0]
                cv = max(cv, abs(fp - 2 * f0 + fm) / hcur ** 2)
        dtw = float(np.diff(tgrid)[0])
        d2res[wD] = (wr, cv, dtw, brk_lo, brk_hi, 0.5 * cv * dtw < abs(wr))
        print("    (D2) w = %.2f, %d x %d grid: worst secant slope %+.6f | "
              "max|d2sigma/dt2| %.3f | 0.5*curv*dt = %.5f -> t-direction %s"
              % (wD, len(tgrid), len(agrid), wr, cv, 0.5 * cv * dtw,
                 "COVERED" if d2res[wD][5] else "NOT COVERED"))
        print("    (D2b) w = %.2f: min_a sigma(0.28,a) = %.6f > 1 > %.6f = "
              "max_a sigma(0.40,a)" % (wD, brk_lo, brk_hi))
    worst = max(d2res[0.60][0], d2res[0.45][0])
    curv = max(d2res[0.60][1], d2res[0.45][1])
    dt_ = d2res[0.60][2]
    covered = d2res[0.60][5] and d2res[0.45][5]
    computed("T176a", worst < 0 and covered,
          "(D2) COMPUTED EVIDENCE, NOT AN ENCLOSURE: on a %d x %d grid over "
          "[0.28,0.40] x [0,0.90] every secant slope of sigma in t is <= %+.6f < 0, "
          "and the sampled curvature bound 0.5*max|d2sigma/dt2|*dt = %.5f is smaller "
          "than that margin, so the t-direction IS covered between grid points. The "
          "a-direction is SAMPLED at %d points and is NOT covered: no bound on "
          "d2sigma/dtda is computed. (v1.3 correction, S23-R17: the dependence on the "
          "amplitude a IS smooth; the max over twelve axes is non-smooth in the "
          "SPATIAL argument, hence in t at Voronoi boundaries, not in a. v1.2 "
          "misattributed the non-smoothness.) (D2) therefore stays COMPUTED, and "
          "the existence claim resting on it is an APPLICATION at COMPUTED strength, "
          "not a proof. Retraction S23-R12."
          % (len(tgrid), len(agrid), worst, 0.5 * curv * dt_, len(agrid)))
    computed("T176a.45", d2res[0.45][0] < 0 and d2res[0.45][5],
             "the SAME grid and curvature audit executed for w = 0.45: worst secant "
             "slope %+.6f, max|d2sigma/dt2| %.3f, interpolation bound %.5f. v1.2 "
             "tabulated this row but computed only w = 0.60; it is now computed."
             % (d2res[0.45][0], d2res[0.45][1], 0.5 * d2res[0.45][1] * d2res[0.45][2]))
    brk_ok = all(d2res[wD][3] > 1 > d2res[wD][4] for wD in (0.60, 0.45))
    computed("T176a2", brk_ok,
             "(D2b) UNIFORM ROOT BRACKETING, new in v1.3. Strict monotonicity gives "
             "UNIQUENESS of t_w(a) but NOT existence: a function can decrease and "
             "stay above 1. Over the whole %d-point amplitude grid and both widths, "
             "min_a sigma(0.28,a) = %.6f > 1 > %.6f = max_a sigma(0.40,a), so the "
             "root is bracketed for every audited a. Lemma S23.2b now carries (D2b) "
             "explicitly. Retraction S23-R15."
             % (len(agrid), min(d2res[wD][3] for wD in (0.60, 0.45)),
                max(d2res[wD][4] for wD in (0.60, 0.45))))

    def _g(a_, w_):
        ta = brentq(lambda t_: conformal_sigma_rho(t_, a_, w=w_, nL=NLI, nA=NAI)[0] - 1,
                    0.28, 0.40, xtol=1e-12)
        return conformal_sigma_rho(ta, a_, w=w_, nL=NLI, nA=NAI)[1] - 1.0, ta

    roots = []
    for w_ in (0.60, 0.45):
        g0, _ = _g(0.0, w_); g1, _ = _g(0.90, w_)
        check("T176b.%d" % int(100 * w_), g0 > 0 > g1,
              "(D3) w = %.2f : g(0) = %+.8f > 0 > %+.8f = g(0.90). SIGN CHANGE. With "
              "(D1) and (D2) this gives existence of a* in (0, 0.90) with sigma = rho "
              "= 1 by the intermediate value theorem -- far stronger than a solver "
              "residual, but the APPLICATION inherits the COMPUTED status of (D2). "
              "Graded claim: LEMMA S23.2b PROVEN-CONDITIONAL; APPLICATION VERIFIED on "
              "(D1) and (D3), COMPUTED on (D2)" % (w_, g0, g1))
        a_s = brentq(lambda a_: _g(a_, w_)[0], 0.0, 0.90, xtol=1e-12)
        t_s = _g(a_s, w_)[1]
        ss, rr = conformal_sigma_rho(t_s, a_s, w=w_, nL=NLI, nA=NAI)
        roots.append((w_, t_s, a_s, ss, rr))
        print("    w = %.2f : IVT-bracketed a* = %.10f, t* = %.10f -> "
              "(sigma, rho) = (%.10f, %.10f)" % (w_, a_s, t_s, ss, rr))
    computed("T176", all(abs(ss - 1) < 1e-8 and abs(rr - 1) < 1e-8
                      for _, _, _, ss, rr in roots),
          "the orbit-blind point (1,1) is attained for both audited profiles")
    Jd = []
    for (w_, t_s, a_s, _, _) in roots:
        h_ = 1e-5; J = np.zeros((2, 2))
        for k_ in range(2):
            zp = [t_s, a_s]; zm = [t_s, a_s]
            zp[k_] += h_; zm[k_] -= h_
            fp = np.array(conformal_sigma_rho(zp[0], zp[1], w=w_, nL=NLI, nA=NAI))
            fm = np.array(conformal_sigma_rho(zm[0], zm[1], w=w_, nL=NLI, nA=NAI))
            J[:, k_] = (fp - fm) / (2 * h_)
        Jd.append((w_, float(np.linalg.det(J)), float(np.linalg.cond(J))))
        print("    w = %.2f : det J = %+.4e, cond J = %.2f" % (w_, Jd[-1][1], Jd[-1][2]))
    computed("T177", all(abs(dj) > 1e-2 and cj < 1e3 for _, dj, cj in Jd),
          "the Jacobian d(sigma,rho)/d(t,a) is NONSINGULAR and well conditioned at both "
          "roots (det = %.3e, %.3e), so the implicit function theorem gives a locally "
          "unique C^1 branch w -> (t*(w), a*(w)): the solution set contains a "
          "one-parameter ARC. NOTE: this does NOT prove a global continuum over the "
          "full infinite-dimensional profile space, which stays a CONJECTURE."
          % (Jd[0][1], Jd[1][1]))
    computed("T177a", abs(roots[0][1] - roots[1][1]) > 1e-4
          or abs(roots[0][2] - roots[1][2]) > 1e-4,
          "the two roots are DISTINCT, establishing NON-UNIQUENESS within the audited "
          "discretisation (two points alone would NOT establish a continuum; T177 "
          "supplies the branch)")

    def _phi3(p_, IVx, amp_, w_):
        """structurally INDEPENDENT profile: bump on the 3-fold (hexagon) axes
        rather than the 5-fold (pentagon) axes. Also I_h-invariant."""
        d_ = np.arccos(np.clip(np.abs(p_ @ FCc.T).max(), -1.0, 1.0))
        return amp_ * np.exp(-(d_ / w_) ** 2)

    r3 = []
    for w_, z0 in ((0.50, [0.336, -0.60]), (0.70, [0.336, -0.88])):
        x_ = fsolve(lambda z: np.array(conformal_sigma_rho(z[0], z[1], w=w_, nL=NLI,
                                                           nA=NAI, pf=_phi3)) - 1.0,
                    z0, xtol=1e-12)
        ss, rr = conformal_sigma_rho(x_[0], x_[1], w=w_, nL=NLI, nA=NAI, pf=_phi3)
        r3.append((w_, x_[0], x_[1], ss, rr))
        print("    3-fold profile w = %.2f : t* = %.9f  a* = %+.9f -> "
              "(sigma, rho) = (%.10f, %.10f)" % (w_, x_[0], x_[1], ss, rr))
    computed("T177b", all(abs(ss - 1) < 1e-8 and abs(rr - 1) < 1e-8
                       for _, _, _, ss, rr in r3) and all(a_ < 0 for _, _, a_, _, _ in r3),
          "a THIRD, structurally independent I_h-invariant profile family -- a bump on "
          "the 3-fold hexagon axes instead of the 5-fold pentagon axes, and reaching "
          "(1,1) at NEGATIVE amplitude -- also attains the orbit-blind point. Four "
          "profiles in two structurally distinct families now reach it, so reachability "
          "is not an artefact of the pentagon-axis ansatz")

    decl("D178", "Theorem S23.2 (Conformal Reachability), v1.2 SPLIT. Within the "
                 "audited discretisation D -- I_h combinatorics of K_TI(t), "
                 "symmetry-forced dual vertices, mirror-geodesic arcs, round-arc "
                 "(5,6) edge, midpoint arc quadrature and centroid area quadrature at "
                 "the stated orders -- the orbit-blind point sigma = rho = 1 IS "
                 "attained, and the attainment is certified by the intermediate value "
                 "theorem (T176a, T176b) rather than by a solver residual. THE STATUS "
                 "IS NOW SPLIT IN TWO, because v1.1 conflated them. (a) LEMMA S23.2b, "
                 "the abstract IVT statement -- if (D1) continuity, (D2) strict "
                 "monotonicity of sigma in t on the rectangle and (D3) the sign change "
                 "of g all hold, then a root exists -- is PROVEN-CONDITIONAL. (b) THE "
                 "APPLICATION of that lemma to the audited discretisation is VERIFIED "
                 "for (D1) and (D3) and only COMPUTED for (D2), because a finite grid "
                 "plus a sampled curvature bound covers the t-direction but not the "
                 "a-direction. v1.1's 'each VERIFIED, therefore existence at proof "
                 "strength' was one grade too strong: retraction S23-R12. v1.3 adds "
                 "hypothesis (D2b), uniform root bracketing, without which the lemma's "
                 "proof step 'by (D2) t_w(a) exists' is invalid, since monotonicity "
                 "gives uniqueness and not existence (T176a2, retraction S23-R15). v1.3 "
                 "also demotes Corollary S23.2e from DERIVED to COMPUTED: a COMPUTED "
                 "application cannot carry a DERIVED corollary (retraction S23-R14). "
                 "The metric route's non-identifiability is therefore STRONG COMPUTED "
                 "COUNTEREVIDENCE against the Class-M verdict, not a proof of "
                 "under-determination. The "
                 "numerical values of (t*, a*) are COMPUTED, with quadrature drift "
                 "measured in T175a and the honest geometric residual of the v1.0 root "
                 "in T175b. Non-uniqueness is established (T177a); a LOCAL C^1 branch "
                 "follows from the implicit function theorem (T177); a GLOBAL continuum "
                 "over the infinite-dimensional profile space remains a CONJECTURE. "
                 "STEP A VERDICT: the metric route does NOT select a class. It "
                 "UNDER-determines -- the ZS-S20 non-identifiability shape recurring "
                 "one level up, at the metric rather than at the measure. This does NOT "
                 "promote the clock route of Theorem S23.3, which section 4.3 shows "
                 "does not close either.")

    # =================================================================
    # S18f  GLOBAL MINIMALITY MULTISTART  (v1.2, gate F-S23.12)
    # =================================================================
    print("\n[S18f] Lemma S23.2a(ii) -- stationary geodesic vs GLOBAL minimiser")
    print("    Totally geodesic gives STATIONARITY. Global minimality is a separate")
    print("    question; a multistart search over normal displacements tests it.")
    from scipy.optimize import minimize as _minim
    _rngm = np.random.default_rng(20260320)
    _t0, _a0, _W0 = roots[0][1], roots[0][2], 0.60
    _P2 = {}
    for (i2, j2) in IEe:
        p2 = (1 - _t0) * IVv[i2] + _t0 * IVv[j2]
        q2 = _t0 * IVv[i2] + (1 - _t0) * IVv[j2]
        _P2[(i2, j2)] = p2 / np.linalg.norm(p2)
        _P2[(j2, i2)] = q2 / np.linalg.norm(q2)
    _pent2 = _ord([_P2[(0, j2)] for j2 in adjc[0]], IVv[0])

    def _plen(a2, b2, cf, amp2, w2, nq=100):
        ang2 = float(np.arccos(np.clip(np.dot(a2, b2), -1, 1)))
        e1 = a2.copy()
        e2 = b2 - np.dot(b2, a2) * a2
        e2 = e2 / np.linalg.norm(e2)
        nv = np.cross(a2, b2)
        nv = nv / np.linalg.norm(nv)
        s2 = (np.arange(nq) + 0.5) / nq
        th2 = s2 * ang2
        base = np.cos(th2)[:, None] * e1 + np.sin(th2)[:, None] * e2
        off = np.zeros(nq)
        for k2, ck in enumerate(cf):
            off = off + ck * np.sin((k2 + 1) * np.pi * s2)
        X2 = base + off[:, None] * nv
        X2 = X2 / np.linalg.norm(X2, axis=1)[:, None]
        Xf = np.vstack([a2, X2, b2])
        seg = np.arccos(np.clip(np.einsum('ij,ij->i', Xf[:-1], Xf[1:]), -1, 1))
        mid = (Xf[:-1] + Xf[1:]) / 2
        mid = mid / np.linalg.norm(mid, axis=1)[:, None]
        vals = np.array([_phi_conf(x2, IVv, amp2, w2) for x2 in mid])
        return float(np.sum(np.exp(vals) * seg))

    Kb = 8
    NST = 4 if FAST else 6
    print("    %-28s %14s %16s %11s" % ("arc", "round-path L",
                                        "best of %d starts" % NST, "rel. gain"))
    gains = {}
    for nm2, pa2, pb2 in [("dual d56   [mirror]", IVv[0], FCc[fi_]),
                          ("dual d66   [mirror]", FCc[sh_[0]], FCc[sh_[1]]),
                          ("primal (6,6) [mirror]", _P2[(i_, j_)], _P2[(j_, i_)]),
                          ("primal (5,6) [NOT mir]", _pent2[0], _pent2[1])]:
        pa2 = np.array(pa2)
        pb2 = np.array(pb2)
        L0b = _plen(pa2, pb2, np.zeros(Kb), _a0, _W0)
        bst = L0b
        for tr in range(NST):
            x0b = np.zeros(Kb) if tr == 0 else _rngm.normal(scale=0.25, size=Kb)
            rr2 = _minim(lambda cf: _plen(pa2, pb2, cf, _a0, _W0), x0b,
                         method='Nelder-Mead',
                         options=dict(maxiter=2500, fatol=1e-13, xatol=1e-10))
            bst = min(bst, float(rr2.fun))
        gains[nm2] = (L0b - bst) / L0b
        print("    %-28s %14.10f %16.10f %11.2e" % (nm2, L0b, bst, gains[nm2]))
    mir = [v for k2, v in gains.items() if "mirror" in k2]
    nonmir = [v for k2, v in gains.items() if "NOT mir" in k2][0]
    computed("T170k", max(mir) < 1e-8 < nonmir,
          "MULTISTART: no path shorter than the mirror great circle is found for any "
          "of the three mirror-contained arcs (max relative gain %.2e over %d random "
          "starts in an %d-mode displacement basis), while the non-mirror (5,6) arc "
          "yields %.2e. This is EVIDENCE for, not a PROOF of, global minimality: the "
          "basis is finite and the optimiser is local. Gate F-S23.12 stays OPEN."
          % (max(mir), NST, Kb, nonmir))
    # ---- v1.3: the GEODESIC-CORRECTED ROOT, computed here, not quoted ------
    print("\n    Geodesic-corrected root: the (5,6) edge is the only non-mirror arc,")
    print("    so re-solve sigma = rho = 1 with its round arc replaced by the true")
    print("    conformal geodesic. v1.2 quoted this from an off-line run; v1.3 computes it.")
    NLg, NAg = (48, 18) if FAST else (64, 24)
    Kg, nqg = 2, 70

    def _geo56(pa3, pb3, amp3, w3):
        best = _plen(pa3, pb3, np.zeros(Kg), amp3, w3, nq=nqg)
        r3 = _minim(lambda cf: _plen(pa3, pb3, cf, amp3, w3, nq=nqg), np.zeros(Kg),
                    method='Powell',
                    options=dict(maxiter=600, ftol=1e-11, xtol=1e-8))
        return min(best, float(r3.fun))

    def _sr_geo(t3, a3, w3=0.60):
        P3 = {}
        for (i3, j3) in IEe:
            p3 = (1 - t3) * IVv[i3] + t3 * IVv[j3]
            q3 = t3 * IVv[i3] + (1 - t3) * IVv[j3]
            P3[(i3, j3)] = p3 / np.linalg.norm(p3)
            P3[(j3, i3)] = q3 / np.linalg.norm(q3)
        pent3 = _ord([P3[(0, j3)] for j3 in adjc[0]], IVv[0])
        hexf = IFf[0]
        a4, b4, c4 = hexf
        hex3 = _ord([P3[(a4, b4)], P3[(b4, a4)], P3[(b4, c4)],
                     P3[(c4, b4)], P3[(c4, a4)], P3[(a4, c4)]], FCc[0])
        A5g = _polyarea_conf(np.array(pent3), IVv, a3, w3, n=NAg)
        A6g = _polyarea_conf(np.array(hex3), IVv, a3, w3, n=NAg)
        l66g = _arclen_conf(P3[(i_, j_)], P3[(j_, i_)], IVv, a3, w3, n=NLg)
        l56g = _geo56(np.array(pent3[0]), np.array(pent3[1]), a3, w3)
        d56g = _arclen_conf(IVv[0], FCc[fi_], IVv, a3, w3, n=NLg)
        d66g = _arclen_conf(FCc[sh_[0]], FCc[sh_[1]], IVv, a3, w3, n=NLg)
        return (d56g / l56g) / (d66g / l66g), A6g / A5g

    xg = fsolve(lambda z: np.array(_sr_geo(z[0], z[1])) - 1.0,
                [roots[0][1], roots[0][2]], xtol=1e-7)
    sgg, rgg = _sr_geo(xg[0], xg[1])
    print("    round-arc root    : t* = %.9f  a* = %.9f" % (roots[0][1], roots[0][2]))
    print("    geodesic-corrected: t* = %.9f  a* = %.9f  -> (sigma, rho) = "
          "(%.9f, %.9f)" % (xg[0], xg[1], sgg, rgg))
    computed("T170m", abs(sgg - 1) < 1e-6 and abs(rgg - 1) < 1e-6
             and abs(xg[0] - roots[0][1]) < 5e-3,
             "GEODESIC-CORRECTED ROOT, computed in-suite in v1.3 (v1.2 quoted it from "
             "an off-line run). Replacing the round (5,6) arc by its true conformal "
             "geodesic moves the root to t* = %.9f, a* = %.9f, a systematic shift of "
             "dt* = %.2e and da* = %.2e. EXISTENCE SURVIVES the correction; only "
             "digits move. This is the quantitative content of gate F-S23.11."
             % (xg[0], xg[1], abs(xg[0] - roots[0][1]), abs(xg[1] - roots[0][2])))

    decl("D174c", "Gate F-S23.12 (new in v1.2). Lemma S23.2a(ii) proves that the "
                  "three mirror-contained arcs are STATIONARY geodesics of every "
                  "I_h-invariant metric. It does NOT prove that they are GLOBALLY "
                  "MINIMISING, and a DEC edge length read as a metric distance would "
                  "require that. This paper DEFINES the DEC primal and dual lengths as "
                  "the symmetry-selected geodesics, under which definition Lemma "
                  "S23.2a(ii) is exact and no further step is needed. Any downstream "
                  "paper that reinterprets these lengths as global metric distances "
                  "must discharge F-S23.12 first. T170k supplies multistart evidence "
                  "consistent with global minimality but does not close the gate.")

    print("\n[S19] Theorem S23.3 -- the CLOCK route: measure transfer from ZS-F38")
    print("    ZS-F38 Theorem F38.T1' (Perron-Frobenius + Birkhoff-von Neumann):")
    print("    an irreducible doubly stochastic register clock has UNIQUE stationary")
    print("    measure rho_Q = I_Q/Q, the democratic (mode-count) measure, and ZS-M44's")
    print("    exact arrowhead solve excluded the METRIC benchmark to 0.45%.")
    Pm = np.ones((Q_LOCK, Q_LOCK)) / Q_LOCK
    ev = np.sort(np.abs(np.linalg.eigvals(Pm)))[::-1]
    check("T180", abs(ev[0] - 1) < 1e-12 and ev[1] < 1e-12,
          "doubly stochastic irreducible clock: unique unit eigenvalue")
    Pcyc = np.roll(np.eye(Q_LOCK), 1, axis=0)
    stat = np.ones(Q_LOCK) / Q_LOCK
    check("T181", np.abs(Pcyc @ stat - stat).max() < 1e-14,
          "the Q = 11 cyclic clock fixes the democratic measure exactly")
    check("T182", abs(float(np.trace(np.eye(Q_LOCK) / Q_LOCK)) - 1.0) < 1e-14,
          "Tr(rho_Q) = 1 for rho_Q = I_Q/Q")
    decl("D183", "Theorem S23.3 (Measure Transfer). If the Z-sector carrier cells "
                 "carry the register clock's stationary measure -- named hypothesis "
                 "(Z-A3), carrier-clock identification -- then by ZS-F38 T1' that "
                 "measure is uniform, hence beta_f = const and m_e = const, hence "
                 "sigma = rho = 1. (Z-A1) is therefore no longer an isolated postulate: "
                 "it is an INSTANCE of a proved unique-ergodicity selection theorem. "
                 "Status DERIVED-CONDITIONAL on (H-CLK) ^ (H-mix) ^ (Z-A3). THIS IS AN "
                 "UPPER BOUND on what the transfer delivers: rho_Q is a stationary "
                 "PROBABILITY and M_1^-1 is a kinetic STIFFNESS, distinct doubly "
                 "stochastic generators share the uniform stationary measure with "
                 "different rates, and ZS-S20 already named that step the unresolved "
                 "bridge (H-PSM-2). (Z-A1) is therefore RELOCATED to (Z-A3), NOT "
                 "eliminated: the corpus axiom COUNT IS UNCHANGED. Retraction S23-R4.")
    decl("D184", "Where the two routes leave the class question, v1.1. The METRIC "
                 "route does NOT select: it under-determines (D178). The CLOCK route "
                 "would select Class MF, but only across the density-to-rate "
                 "identification (Z-A3)/(H-PSM-2), which is OPEN, and ZS-F40's physical "
                 "clock discharge returned CLOSED-NEGATIVE with a Frobenius deviation "
                 "of exactly sqrt(2), unreconciled here (gate F-S23.5). NEITHER ROUTE "
                 "CLOSES THE CLASS QUESTION. It is OPEN, and it is now OPEN in ONE "
                 "NAMED PLACE. ZS-M44's 0.45% arrowhead solve favours mode-count over "
                 "metric, but it is evidence rather than derivation, and it is evidence "
                 "about the REGISTER, not about the CARRIER. v1.0's declaration that "
                 "'the GEOMETRIC route selects Class M' contradicted its own body and "
                 "is withdrawn here. Retractions S23-R3, S23-R5.")

    print("\n[S20] Theorem S23.4 -- STEP B: the central-action Hessian is FORCED")
    Tb = su3_generators()
    orthoT = max(abs(np.trace(Tb[a] @ Tb[b]) - (0.5 if a == b else 0.0))
                 for a in range(8) for b in range(8))
    check("T190", orthoT < 1e-12,
          "su(3) basis normalised, Tr(T^a T^b) = delta/2, residual %.2e" % orthoT)
    print("    %-26s %22s %16s" % ("central action Phi", "Hess/Killing residual", "kappa"))
    for nm, Phi in [("Wilson beta = 1", lambda U: 1.0 * (1 - np.trace(U).real / 3)),
                    ("Wilson beta = 2.7", lambda U: 2.7 * (1 - np.trace(U).real / 3)),
                    ("heat kernel t = 0.4", su3_heat_kernel_action(0.4)),
                    ("heat kernel t = 1.1", su3_heat_kernel_action(1.1))]:
        Hh = identity_hessian(Phi, Tb)
        kap = float(np.trace(Hh)) / 8.0
        res = float(np.abs(Hh - kap * np.eye(8)).max()) / max(abs(kap), 1e-30)
        check("T191.%s" % nm.split()[0] + nm.split()[-1], res < 1e-6,
              "Hessian of %s is proportional to the Killing form, residual %.2e"
              % (nm, res))
        print("    %-26s %22.3e %16.8f" % (nm, res, kap))
    Hn = identity_hessian(lambda U: (U[0, 0].real) ** 2, Tb)
    kn = float(np.trace(Hn)) / 8.0
    resn = float(np.abs(Hn - kn * np.eye(8)).max()) / max(abs(kn), 1e-30)
    check("T192", resn > 0.1,
          "CONTROL: a NON-central action is not proportional, residual %.2e" % resn)
    print("    %-26s %22.3e  <- control, non-central"
          % ("Re(U_00)^2", resn))
    decl("D193", "Theorem S23.4 (Central-Hessian Theorem, PROVEN). For a compact "
                 "SIMPLE G, any C^2 central Phi has Ad-invariant Hessian at the "
                 "identity, and by Schur the space of Ad-invariant symmetric bilinear "
                 "forms on a simple g is one-dimensional. Hence Hess Phi|_1 = kappa_Phi "
                 "<.,.>_K. Consequently ANY positive central plaquette action expands "
                 "as S = const + (a^2/2) <A, B^T diag(kappa_p) B A> + o(a^2) for Phi in "
                 "C^2, or + O(a^3) if Phi is C^3 (v1.3 regularity correction, "
                 "S23-R16): the "
                 "identity-neighbourhood Hessian is the EDGE-space operator H_edge = "
                 "B_2^T diag(kappa_p) B_2, with beta_p = kappa_p. It is NOT equal to "
                 "Delta_S21, which is a FACE-space operator; the correct relation is "
                 "NONZERO-ISOSPECTRAL and is verified in S20c. Retraction S23-R1. STEP "
                 "B is PROVEN-CONDITIONAL on single-plaquette locality (H-W), NOT "
                 "unconditional -- gauge invariance forbids non-central terms but does "
                 "NOT forbid gauge-invariant MULTI-plaquette terms. Retraction S23-R6. "
                 "The Hessian's FORM is gauge-group independent for simple G and does "
                 "NOT require knowing which central action STEP A produces; only the "
                 "VALUES kappa_p do.")

    print("\n[S20b] Lemma S23.5 -- centrality is FORCED, not assumed")
    print("    A single-plaquette term Phi(U_f) transforms as U_f -> g U_f g^-1 under a")
    print("    gauge transformation at its base vertex, so gauge invariance REQUIRES")
    print("    Phi(gUg^-1) = Phi(U): centrality is the definition of gauge invariance here.")
    rng = np.random.default_rng(20260320)

    def _rand_su3():
        X = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        Qm, Rm = np.linalg.qr(X)
        Qm = Qm @ np.diag(np.diag(Rm) / np.abs(np.diag(Rm)))
        return Qm / np.linalg.det(Qm) ** (1.0 / 3.0)

    print("    %-28s %38s %11s" % ("plaquette functional",
                                   "max |Phi(gUg^-1)-Phi(U)|, 2000 draws", "gauge inv"))
    conj_dev = {}
    for nm, Phi in [("Wilson", lambda U: 1 - np.trace(U).real / 3),
                    ("heat kernel t = 0.7", su3_heat_kernel_action(0.7)),
                    ("Re(U_00)^2 non-central", lambda U: (U[0, 0].real) ** 2)]:
        dv = 0.0
        for _ in range(2000):
            U = _rand_su3(); gg2 = _rand_su3()
            dv = max(dv, abs(Phi(gg2 @ U @ np.conj(gg2).T) - Phi(U)))
        conj_dev[nm] = dv
        print("    %-28s %38.3e %11s" % (nm, dv, dv < 1e-10))
    check("T195", conj_dev["Wilson"] < 1e-10 and conj_dev["heat kernel t = 0.7"] < 1e-10,
          "Wilson and heat-kernel plaquette terms are conjugation invariant")
    check("T196", conj_dev["Re(U_00)^2 non-central"] > 1e-3,
          "a NON-central single-plaquette functional is NOT gauge invariant "
          "(deviation %.3e), so it cannot occur in the reduction"
          % conj_dev["Re(U_00)^2 non-central"])
    decl("D197", "Lemma S23.5 (Centrality is Forced). For a single-plaquette term the "
                 "base-vertex gauge transformation acts by conjugation, so gauge "
                 "invariance is EQUIVALENT to centrality. Combined with Theorem S23.4 "
                 "this gives Corollary S23.5a: ANY gauge-invariant single-plaquette "
                 "cellular action -- whatever the explicit face-and-prism integration "
                 "of ZS-S14 produces -- has identity-Hessian H_edge = B_2^T "
                 "diag(kappa_p) B_2, which is NONZERO-ISOSPECTRAL to Delta_S21 and NOT "
                 "equal to it. Gate F-S23.8 remains OPEN: a gauge-invariant "
                 "MULTI-plaquette term would add terms outside B_2^T diag(kappa_p) B_2, "
                 "and it is excluded only by (H-W), which this paper does NOT close. "
                 "The constructive half of STEP A is therefore not required for the "
                 "FORM of the Hessian, only for the VALUES kappa_p.")

    print("\n[S20c] Theorem S23.6 -- edge Hessian vs face operator: NONZERO-ISOSPECTRAL")
    print("    The quadratic expansion lives on EDGE space: H_edge = M1^{-1/2} B^T M2 B M1^{-1/2},")
    print("    dimension E x E = 90 x 90 on K_TI.  The ZS-S21 operator is the FACE operator")
    print("    Delta_2 = M2^{1/2} B M1^{-1} B^T M2^{1/2}, dimension F x F = 32 x 32.")
    print("    These are NOT the same operator.  They share their NONZERO spectrum.")
    cI = CAR[1]
    Fn, En = cI["F_K"], len(cI["edges"])
    Bm = np.zeros((Fn, En))
    for kk, (aa, bb) in enumerate(cI["edges"]):
        Bm[aa, kk] = 1.0
        Bm[bb, kk] = -1.0
    print("    %-22s %10s %10s %8s %8s %14s"
          % ("(sigma, rho)", "edge dim", "face dim", "rank_e", "rank_f", "max deviation"))
    isores = []
    for (sg, rh) in [(1.0, 1.0), (0.8939748058, 1.5293717121), (1.3, 0.7)]:
        m1 = np.where(cI["defect_edge"], 1.0 / sg, 1.0)
        m2 = np.where(cI["is5"], rh, 1.0)
        M1ih = np.diag(np.sqrt(1.0 / m1))
        He = M1ih @ Bm.T @ np.diag(m2) @ Bm @ M1ih
        Df = np.diag(np.sqrt(m2)) @ Bm @ np.diag(1.0 / m1) @ Bm.T @ np.diag(np.sqrt(m2))
        we = np.sort(np.linalg.eigvalsh(He))
        wf = np.sort(np.linalg.eigvalsh(Df))
        ne, nf = we[we > 1e-9], wf[wf > 1e-9]
        dev = float(np.abs(ne - nf).max()) if len(ne) == len(nf) else np.inf
        isores.append(dev)
        print("    (%8.4f,%8.4f) %10s %10s %8d %8d %14.2e"
              % (sg, rh, str(He.shape), str(Df.shape), len(ne), len(nf), dev))
    check("T198", max(isores) < 1e-8,
          "edge and face operators are nonzero-isospectral, max deviation %.2e"
          % max(isores))
    check("T199", Fn != En,
          "the two operators live on different spaces (%d vs %d), so they are NOT equal"
          % (En, Fn))
    decl("D199a", "Review correction (ZS-S22 v1.2 review, item 4). ZS-S22 v1.2 wrote "
                  "that the identity-neighbourhood Hessian is EXACTLY Delta_S21. That "
                  "is a TYPE ERROR: the Hessian is a 90 x 90 operator on edge space and "
                  "Delta_S21 is a 32 x 32 operator on face space. The correct relation "
                  "is NONZERO-ISOSPECTRAL, verified here to 1e-14 at three weight "
                  "points. Retraction S23-R1.")

    nc = sum(1 for x in LEDGER if x[1] == "C")
    npx = sum(1 for x in LEDGER if x[1] == "P")
    nx = sum(1 for x in LEDGER if x[1] == "X")
    nd = sum(1 for x in LEDGER if x[1] == "D")
    npass = sum(1 for x in LEDGER if x[2] == "PASS")
    print("\n" + "=" * 72)
    print("LEDGER: %d executable entries PASS = %d theorem-bearing checks (C) "
          "+ %d COMPUTED diagnostics (X) + %d proxy (P) | %d declarative (D) "
          "| %d FAIL"
          % (npass, nc, nx, npx, nd, len(FAILED)))
    print("  C = assertion on the actual Z-Spin object that carries proof weight.")
    print("  X = COMPUTED diagnostic: numerical evidence with measured but "
          "unbounded")
    print("      discretisation error. Carries NO proof weight, per the "
          "manuscript legend.")
    if FAILED:
        print("FAILED:", FAILED)
    print("MODE = %s | wall-clock runtime = %.1f s | environment-dependent"
          % ("FAST (non-publication)" if FAST else "FULL (publication)",
             time.time() - _T0))
    if FAST:
        print("WARNING: FAST mode. The full-resolution publication ledger was NOT "
              "executed.")
    print("SHA256(self) = %s"
          % hashlib.sha256(open(__file__, "rb").read()).hexdigest())
    print("END_ZS_S23_RESULTS")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
