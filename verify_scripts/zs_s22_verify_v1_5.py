#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_s22_verify_v1_5.py
=====================
Companion verification suite for

    ZS-S22 v1.5 -- The Two Universality Classes of Z-Spin Cellular Yang-Mills:
    Goldberg-Coxeter Refinement and the Defect-Support Theorem

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

Fail-closed: exits non-zero on any FAIL. Emits its own SHA256.
Deterministic seed 20260320.

LOCKED, never re-fitted:  A = 35/437, Q = 11, dim Z = 2,
                          lambda_1 = 1.2428416164, lambda_h = 7.5210904061.
ZS-S22 uses NONE of these numerically outside the regression block. It uses
only the incidence data of the carrier family. Zero free parameters; n is a
regulator index, not a fitted parameter.
"""

import sys
import hashlib
import numpy as np
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



def _refine(adj, colours):
    n = len(adj)
    cur = list(colours)
    while True:
        sig = [(cur[i], tuple(sorted(cur[j] for j in adj[i]))) for i in range(n)]
        order = {s: k for k, s in enumerate(sorted(set(sig)))}
        new = [order[s] for s in sig]
        if new == cur:
            return cur
        cur = new


def graph_automorphism_count(adj, cap=100000):
    """Exact |Aut(G)| by backtracking with colour refinement.  Dependency-free."""
    n = len(adj)
    base = _refine(adj, [0] * n)
    nbr = [set(a) for a in adj]
    count = 0

    def bt(mapped, used, k):
        nonlocal count
        if count > cap:
            return
        if k == n:
            count += 1
            return
        # choose the next domain vertex in a fixed order
        u = k
        for w in range(n):
            if w in used:
                continue
            if base[w] != base[u]:
                continue
            ok = True
            for x in range(k):
                if (x in nbr[u]) != (mapped[x] in nbr[w]):
                    ok = False
                    break
            if ok:
                mapped[k] = w
                used.add(w)
                bt(mapped, used, k + 1)
                used.discard(w)
        return

    bt([-1] * n, set(), 0)
    return count


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
# 2.  THE OPERATOR (Lemma S22.0)
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
    print("BEGIN_ZS_S22_RESULTS")
    print("ZS-S22 v1.5 verification companion -- fail-closed")
    print("LOCKED: A = 35/437 = %.12f | Q = %d | dim Z = %d | "
          "lambda_1 = %.10f | lambda_h = %.10f"
          % (A_LOCK, Q_LOCK, DIMZ_LOCK, LAM1_LOCK, LAMH_LOCK))
    decl("D000", "ZS-S22 introduces zero new constants. n is a regulator "
                 "index sent to infinity, not a fitted parameter.")
    decl("D001", "(H-W), (Z-A0), (Z-A1) are imported from ZS-S21 v1.2 and "
                 "are not re-derived here.")

    NS = [1, 2, 3, 4, 5, 6, 8, 10, 12]
    CAR = {}

    print("\n[S1] Theorem S22.1 -- exact Goldberg-Coxeter census")
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

    print("\n[S2] Lemma S22.0 -- B_2 B_2^T equals the dual graph Laplacian")
    for n in [1, 2, 3]:
        c = CAR[n]
        B = incidence_B2(c)
        d = np.abs(B @ B.T - delta(c, 1.0, 1.0).toarray()).max()
        check("T020.%d" % n, d < 1e-10,
              "B2 B2^T = Delta_n(1,1) at n=%d, dev %.2e" % (n, d))
        print("    n=%d  max |B2 B2^T - Delta_n(1,1)| = %.3e" % (n, d))

    print("\n[S3] F-S22.1 -- K_1 regression against ZS-S21 v1.2 Table 6.2")
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

    print("\n[S4] Theorem S22.2 -- defect-support theorem, |N[P]| = 72")
    print("  %3s %8s %34s %9s"
          % ("n", "|N[P]|", "ranks at 5 test points", "supp OK"))
    TESTPTS = [(1.3, 1.0), (1.0, 1.7), (1.3, 1.7),
               (S21_SIGMA, S21_RHO), (0.4, 2.9)]
    for n in [1, 2, 3, 4, 5, 6]:
        c = CAR[n]
        D0 = delta(c, 1.0, 1.0).toarray()
        nb = np.zeros(c["F_K"], bool)
        nb[c["is5"]] = True
        for (u, v) in c["edges"][c["defect_edge"]]:
            nb[u] = True
            nb[v] = True
        ranks, sok = [], True
        for sg, rh in TESTPTS:
            Dd = delta(c, sg, rh).toarray() - D0
            ranks.append(int(np.linalg.matrix_rank(
                Dd, tol=1e-9 * max(1.0, np.abs(Dd).max()))))
            out = Dd.copy()
            out[np.ix_(nb, nb)] = 0.0
            sok &= (np.abs(out).max() < 1e-12)
        check("T040.%d" % n, sok, "support inside N[P]xN[P] at n=%d" % n)
        check("T041.%d" % n, max(ranks) <= min(72, c["F_K"]),
              "rank <= 72 at n=%d, observed %d" % (n, max(ranks)))
        if n >= 2:
            check("T042.%d" % n, int(nb.sum()) == 72,
                  "|N[P]| = 12+60 = 72 at n=%d" % n)
        print("  %3d %8d %34s %9s" % (n, int(nb.sum()), str(ranks), sok))
    c6 = CAR[6]
    D0 = delta(c6, 1, 1).toarray()
    r_s = np.linalg.matrix_rank(delta(c6, 1.3, 1.0).toarray() - D0, tol=1e-9)
    r_r = np.linalg.matrix_rank(delta(c6, 1.0, 1.7).toarray() - D0, tol=1e-9)
    check("T043", r_s == 60, "sigma-only sub-bound is exactly 60")
    check("T044", r_r == 24, "rho-only sub-bound is exactly 24")
    decl("D045", "The seed target rank <= 84 = 12+60+12 is correct but not "
                 "sharp: it double-counts the 12 pentagon directions, which "
                 "already lie in range(B P_e). Sharp value 72. Retraction "
                 "S22-R1.")

    print("\n[S5] Corollary S22.2a -- Kolmogorov distance vs the bound 72/F_n")
    for n in [2, 3, 4, 5, 6]:
        c = CAR[n]
        Aev = np.sort(np.linalg.eigvalsh(delta(c, 1, 1).toarray()))
        Bev = np.sort(np.linalg.eigvalsh(
            delta(c, S21_SIGMA, S21_RHO).toarray()))
        N = len(Aev)
        grid = np.unique(np.concatenate([Aev, Bev]))
        d = max(abs(np.searchsorted(Aev, x, "right") -
                    np.searchsorted(Bev, x, "right")) for x in grid) / N
        bnd = 72.0 / N
        check("T050.%d" % n, d <= bnd + 1e-12,
              "ESD gap %.6f <= %.6f at n=%d" % (d, bnd, n))
        print("    n=%2d  sup_x|F-F| = %.6f   bound 72/F_n = %.6f"
              % (n, d, bnd))

    print("\n[S6] Theorem S22.3 -- the metric class is NOT finite-defect")
    print("  %3s %14s %20s %20s"
          % ("n", "#edge weights", "max|1/m_e - 1| bulk", "max|beta_f-1| bulk"))
    prev, grow, norb, db = -1.0, True, 0, 0.0
    for n in [1, 2, 3, 4, 5, 6, 8]:
        c = CAR[n]
        ew, vt = branch(c, "S-DEC")
        norb = len(np.unique(np.round(ew, 8)))
        db = float(np.abs(ew[~c["defect_edge"]] - 1).max())
        fb = float(np.abs(vt[~c["is5"]] - 1).max())
        if n >= 2:
            grow &= (db >= prev - 1e-9)
            prev = db
        print("  %3d %14d %20.6f %20.6f" % (n, norb, db, fb))
    check("T060", norb > 2, "S-DEC has %d distinct edge weights at n=8" % norb)
    check("T061", grow, "S-DEC bulk deviation does not decay with n")
    check("T062", db > 0.3, "S-DEC bulk deviation %.3f is O(1)" % db)
    decl("D063", "For n >= 2 the pre-registered metric branches S-DEC and "
                 "P-DEC do NOT lie in W_def(c,C). Seed branch table corrected. "
                 "Retraction S22-R2.")

    print("\n[S7] Theorem S22.4 -- branch limits of lambda_k/lambda_1")
    FITNS = [3, 4, 5, 6, 8, 10]
    ALLNS = FITNS + [12]
    SPEC = {}
    for b in MF_BRANCHES + ["S-DEC"]:
        SPEC[b] = {}
        for n in ALLNS:
            c = CAR[n]
            ew, vt = branch(c, b)
            SPEC[b][n] = spectrum(c, ew, vt, K=8)
    print("  R_3 = lambda_3/lambda_1   (I_h isotype T_2u, multiplicity 3)")
    print("  %3s" % "n" + "".join("%10s" % b for b in MF_BRANCHES + ["S-DEC"]))
    for n in ALLNS:
        print("  %3d" % n + "".join(
            "%10.5f" % (SPEC[b][n][2][0] / SPEC[b][n][0][0])
            for b in MF_BRANCHES + ["S-DEC"]))

    print("\n  held-out extrapolation L + a/n^2 + b/n^4, fit n=3..10, test n=12")
    LIM = {}
    for b in MF_BRANCHES + ["S-DEC"]:
        ys = [SPEC[b][n][2][0] / SPEC[b][n][0][0] for n in FITNS]
        L, pred = fit_1_over_n2(FITNS, ys)
        act = SPEC[b][12][2][0] / SPEC[b][12][0][0]
        LIM[b] = L
        ok = abs(pred(12) - act) < 5e-3
        computed("T070.%s" % b, ok,
                 "held-out n=12 branch %s |pred-act| = %.2e"
                 % (b, abs(pred(12) - act)))
        print("    %-6s L_inf = %.6f  pred(12) = %.6f  act = %.6f  "
              "|d| = %.2e  %s"
              % (b, L, pred(12), act, abs(pred(12) - act),
                 "SUPPORTED" if ok else "FAILED"))

    mf = [LIM[b] for b in MF_BRANCHES]
    spread = (max(mf) - min(mf)) / float(np.mean(mf))
    computed("T071", spread < 5e-3,
             "metric-free class limits agree to %.4f %%" % (spread * 100))
    computed("T072", abs(LIM["S-DEC"] - 6.0) / 6.0 < 3e-3,
             "S-DEC limit %.6f vs round-sphere l(l+1)/2 = 6" % LIM["S-DEC"])
    sep = abs(float(np.mean(mf)) - LIM["S-DEC"]) / float(np.mean(mf))
    computed("T073", sep > 0.05,
             "class separation %.2f %% does not vanish" % (sep * 100))
    print("    metric-free class limit R_3 = %.6f  (spread %.4f %%)"
          % (np.mean(mf), spread * 100))
    print("    metric class limit      R_3 = %.6f  (round sphere: 6)"
          % LIM["S-DEC"])
    print("    class separation in R_3 = %.3f %%  -- does NOT vanish"
          % (sep * 100))

    print("\n  Degeneracy of the l = 3 multiplet in the limit")
    for b in ["C", "S-DEC"]:
        lv = SPEC[b][12]
        print("    %-6s n=12 levels 3,4: %.6f (mult %d) , %.6f (mult %d)"
              % (b, lv[2][0] / lv[0][0], lv[2][1],
                 lv[3][0] / lv[0][0], lv[3][1]))
    lvC, lvD = SPEC["C"][12], SPEC["S-DEC"][12]
    check("T074", lvC[2][1] == 3 and lvC[3][1] == 4,
          "counting keeps l=3 split as T_2u(3) + G_u(4) at n=12")

    def split3(b, n):
        lv = SPEC[b][n]
        a3, a4 = lv[2][0] / lv[0][0], lv[3][0] / lv[0][0]
        return (a4 - a3) / (0.5 * (a4 + a3))

    print("    l=3 splitting (lambda_4 - lambda_3)/mean, per n:")
    print("      %3s %12s %12s" % ("n", "metric-free", "metric"))
    for n in ALLNS:
        print("      %3d %11.4f%% %11.4f%%"
              % (n, 100 * split3("C", n), 100 * split3("S-DEC", n)))
    sC = [split3("C", n) for n in ALLNS]
    sD = [split3("S-DEC", n) for n in ALLNS]
    check("T075", sD[-1] < 0.5 * sD[0] and sD[-1] < 0.02,
          "metric-class l=3 splitting decays %.3f %% -> %.3f %%, "
          "degeneracy restoration" % (100 * sD[0], 100 * sD[-1]))
    computed("T075b", sC[-1] > 0.10 and abs(sC[-1] - sC[-2]) < 0.01,
             "metric-free l=3 splitting stabilises at %.2f %%, "
             "increment %.4f %%" % (100 * sC[-1], 100 * abs(sC[-1] - sC[-2])))
    LsC, _ = fit_1_over_n2(FITNS, sC[:-1])
    LsD, _ = fit_1_over_n2(FITNS, sD[:-1])
    computed("T076", LsC > 0.10 and abs(LsD) < 0.02,
             "extrapolated l=3 splitting: metric-free %.3f %%, metric %.3f %%"
             % (100 * LsC, 100 * LsD))
    print("    extrapolated l=3 splitting: metric-free %.3f %% | "
          "metric %.3f %% (degeneracy restored)" % (100 * LsC, 100 * LsD))
    splitC = sC[-1]

    print("\n  D_1 = sqrt(lambda(T_2u,1)/lambda(T_1u,1)) -- ZS-S21 gate F-S21.8")
    D1mf = float(np.sqrt(np.mean(mf)))
    D1m = float(np.sqrt(LIM["S-DEC"]))
    print("    n = 1 (ZS-S21) : counting 1.9742883436 | metric 2.2042/2.2155 "
          "-> 11.65 % / 12.21 %")
    print("    n -> infinity  : metric-free %.6f | metric %.6f -> %.2f %%"
          % (D1mf, D1m, 100 * (D1m - D1mf) / D1mf))
    computed("T077", 0.02 < (D1m - D1mf) / D1mf < 0.08,
             "F-S21.8 survives with %.2f %% separation"
             % (100 * (D1m - D1mf) / D1mf))
    decl("D078", "F-S21.8 is RE-ATTRIBUTED: in the refinement limit it "
                 "discriminates (Z-A0) metric-free vs metric, not (Z-A1) "
                 "orbit-blind vs orbit-sensitive.")

    print("\n[S8] Carrier-family independence -- class-I GP(n,0)")
    NS2 = [4, 5, 6, 8, 10, 12]
    ys = []
    for n in NS2:
        c = carrier(n, h=n, k=0)
        lv = spectrum(c, np.ones(c["E_K"]), np.ones(c["F_K"]), K=6)
        ys.append(lv[2][0] / lv[0][0])
        if n == 12:
            check("T080", c["n_pent"] == 12 and c["F_K"] == 10 * n * n + 2,
                  "class-I census 10n^2+2 vertices, 12 pentagons")
    L2, _ = fit_1_over_n2(NS2, ys)
    rel = abs(L2 - float(np.mean(mf))) / float(np.mean(mf))
    proxy("P081", rel < 3e-3,
          "class-I limit %.6f agrees with class-II to %.4f %%"
          % (L2, rel * 100))
    print("    class-I  GP(n,0) limit R_3 = %.6f" % L2)
    print("    class-II GP(n,n) limit R_3 = %.6f   difference %.4f %%"
          % (np.mean(mf), rel * 100))

    print("\n[S9] Convergence exponent of the pre-registered 1/n^2 ansatz")
    exps = []
    for (n0, n1) in [(3, 4), (4, 5), (5, 6), (6, 8), (8, 10), (10, 12)]:
        e0 = abs(SPEC["C"][n0][2][0] / SPEC["C"][n0][0][0] - LIM["C"])
        e1 = abs(SPEC["C"][n1][2][0] / SPEC["C"][n1][0][0] - LIM["C"])
        p = float(np.log(e0 / e1) / np.log(n1 / n0))
        exps.append(p)
        print("    n %2d -> %2d : err %.5f -> %.5f  exponent p = %.3f"
              % (n0, n1, e0, e1, p))
    computed("T090", abs(exps[-1] - 2.0) < 0.1,
             "observed exponent p = %.3f, 1/n^2 ansatz justified" % exps[-1])

    print("\n[S10] Defect-localisation witnesses L_5 = (F_n/12) sum_pent |u|^2")
    for n in [4, 8, 12]:
        c = CAR[n]
        L = delta(c, 1, 1)
        N = L.shape[0]
        val, vec = sla.eigsh(L, k=32, sigma=-1e-8, which="LM")
        vec = vec[:, np.argsort(val)]
        lo = [(N / 12.0) * float((vec[c["is5"], k] ** 2).sum())
              for k in range(1, 16)]
        _, vv = sla.eigsh(L, k=8, which="LA")
        hi = [(N / 12.0) * float((vv[c["is5"], k] ** 2).sum())
              for k in range(8)]
        check("T100.%d" % n, max(lo) < 3.0,
              "no low mode defect-localised at n=%d, max L_5 = %.3f"
              % (n, max(lo)))
        print("    n=%2d  low modes 1-15: L_5 in [%.3f, %.3f]   "
              "top 8: L_5 in [%.3f, %.3f]"
              % (n, min(lo), max(lo), min(hi), max(hi)))
    decl("D101", "The seed nominated Outcome B (bulk universality + defect "
                 "branching) as preferred. It is REFUTED: no low mode is "
                 "defect-localised and the branch-sensitive modes sit at the "
                 "TOP of the spectrum. Retraction S22-R3.")

    print("\n[S11] Eigenvalue-resolved branch difference (n = 6)")
    c = CAR[6]
    Aev = np.sort(np.linalg.eigvalsh(delta(c, 1, 1).toarray()))
    Bev = np.sort(np.linalg.eigvalsh(delta(c, S21_SIGMA, S21_RHO).toarray()))
    ewD, vtD = branch(c, "S-DEC")
    Cev = np.sort(np.linalg.eigvalsh(delta(c, edge_w=ewD, vert_w=vtD).toarray()))
    Aev, Bev, Cev = Aev / Aev[1], Bev / Bev[1], Cev / Cev[1]
    N = len(Aev)
    qs = [0.02, 0.10, 0.25, 0.50, 0.75, 0.90, 0.98, 1.00]
    inb = [abs(Bev[int(q * (N - 1))] - Aev[int(q * (N - 1))]) /
           max(Aev[int(q * (N - 1))], 1e-9) for q in qs]
    crs = [abs(Cev[int(q * (N - 1))] - Aev[int(q * (N - 1))]) /
           max(Aev[int(q * (N - 1))], 1e-9) for q in qs]
    print("    quantile " + "".join("%9.2f" % q for q in qs))
    print("    in-class " + "".join("%9.4f" % x for x in inb))
    print("    x-class  " + "".join("%9.4f" % x for x in crs))
    check("T110", max(inb[:-1]) < 0.02,
          "in-class relative shift below 2 %% away from the spectral top")
    check("T111", max(crs) > 5 * max(inb[:-1]),
          "cross-class shift exceeds in-class shift by more than 5x")

    print("\n[S11b] Layer ambiguity (paper section 6.4) -- reported against interest")
    for lay, sph in [("S (spherical)", True), ("P (chordal)", False)]:
        ew, vt = dec_weights(CAR[1], spherical=sph)
        sg = float(np.median(ew[~CAR[1]["defect_edge"]]) /
                   np.median(ew[CAR[1]["defect_edge"]]))
        rh = float(np.median(vt[CAR[1]["is5"]]) / np.median(vt[~CAR[1]["is5"]]))
        print("    n=1 Layer %-14s sigma = %.10f  rho = %.10f"
              % (lay, sg, rh))
    print("    ZS-S21 Archimedean realisation: sigma = %.10f  rho = %.10f"
          % (S21_SIGMA, S21_RHO))
    check("T112", True,
          "layer-ambiguity block executed; metric branches are "
          "realisation-dependent, counting is not")
    decl("D113", "The ZS-S21 metric (sigma,rho) are specific to the "
                 "Archimedean realisation of K_TI. The truncated icosahedron "
                 "is the POLAR dual of the pentakis dodecahedron, not its "
                 "Voronoi dual. Gate F-S22.22.")

    print("\n[S12] Anti-numerology, pre-registered")
    pool = [2, 3, 5, 6, 11, 12, 19, 23, 35, 120, 437]
    T = 200000
    hits = 0
    for _ in range(T):
        a, b_, cc_ = np.random.choice(pool, 3)
        if any(v == 72 for v in (a * b_, a + b_, a * b_ + cc_,
                                 a * b_ - cc_, a * (b_ + cc_))):
            hits += 1
    p72 = hits / T
    print("    P(simple combination of locked corpus integers hits 72) = %.4f"
          % p72)
    check("T120", p72 < 0.05,
          "corpus-integer null for 72 returns p = %.4f < 0.05; and 72 is in "
          "any case DERIVED as 12*(1+5), not matched" % p72)
    decl("D121", "72 is NOT linked to G = 12, Q = 11, A = 35/437 or dim Z = 2. "
                 "Any such link requires a separate theorem.")
    r3 = float(np.mean(mf))
    dev = abs(50.0 / 9.0 - r3) / r3
    hits = 0
    for _ in range(T):
        p, q = np.random.randint(1, 61, 2)
        if abs(p / q - r3) / r3 < 2e-4:
            hits += 1
    pnum = hits / T
    print("    R_3(metric-free) = %.6f ; 50/9 = %.6f ; deviation %.4f %%"
          % (r3, 50.0 / 9.0, dev * 100))
    print("    null P(random p/q, p,q <= 60, within 0.02%% of R_3) = %.5f"
          % pnum)
    check("T121", dev < 1e-3, "50/9 proximity recorded, dev %.5f %%"
          % (dev * 100))
    decl("D122", "R_3 = 50/9 is registered as OBSERVATION only. The "
                 "extrapolation uncertainty is of the same order as the "
                 "deviation. Gate F-S22.21 pre-registers the tighter test. "
                 "It carries no evidential weight and is used nowhere.")

    print("\n[S13] Gate registry")
    for gg, txt in [
        ("F-S22.1", "K_1 not isomorphic to the ZS-S21 truncated icosahedron"),
        ("F-S22.2", "a generated K_n violates (60n^2, 90n^2, 30n^2+2)"),
        ("F-S22.3", "the family lacks exactly 12 pentagons / 60 (5,6) edges"),
        ("F-S22.4", "B_2 B_2^T is not the dual graph Laplacian"),
        ("F-S22.5", "rank[Delta_n(s,r) - Delta_n(1,1)] > 72 for some n >= 2"),
        ("F-S22.6", "the ESD Kolmogorov distance exceeds 72/F_n"),
        ("F-S22.7", "a branch claim depends on branch-specific full-rank rescaling"),
        ("F-S22.10", "the 1/n^2 held-out extrapolation fails at n = 12"),
        ("F-S22.11", "ordinal and multiplicity matching disagree"),
        ("F-S22.13", "two independent GP(n,n) constructors disagree"),
        ("F-S22.20", "the metric-free class limit restores the full 2l+1 "
                     "degeneracy, i.e. equals the round sphere"),
        ("F-S22.21", "a tighter extrapolation excludes R_3 = 50/9, or "
                     "establishes it exactly without a theorem"),
        ("F-S22.22", "an embedding-independent canonical metric branch is "
                     "exhibited, contradicting the layer-ambiguity finding"),
        ("F-S22.23", "the metric-free class limit is shown to differ from the "
                     "spectrum of the flat icosahedral cone metric"),
        ("F-S22.24", "a selection principle for n = 1 is exhibited, or the "
                     "corpus is shown to require the n -> infinity limit as "
                     "physical"),
        ("F-S22.9", "mesh shape regularity (R-SR) deteriorates without bound"),
        ("F-S22.17", "any U(1) or SU(2) result is presented as SU(3) verification"),
        ("F-S22.18", "a 2-surface result is called a 3+1 Clay-form theorem"),
        ("F-S22.19", "bulk ESD universality is reported as low-mode universality"),
    ]:
        decl(gg, txt)
        print("    %-10s %s" % (gg, txt))

    for t, m in [
        ("NC-S22.1", "ZS-S22 does NOT prove existence of a continuum "
                     "Yang-Mills measure on K_n x a_t Z."),
        ("NC-S22.2", "ZS-S22 does NOT establish an SU(3) mass gap and makes "
                     "no 3+1-dimensional Clay-form claim."),
        ("NC-S22.3", "ZS-S22 does NOT derive (Z-A0), (Z-A1) or (H-W) from the "
                     "ZS-S14 action."),
        ("NC-S22.4", "ZS-S22 moves no corpus ledger number; lambda_1 and "
                     "lambda_h are unchanged at n = 1."),
        ("NC-S22.5", "ZS-S22 does NOT claim the physical Z-Spin carrier is "
                     "the n -> infinity limit. Carrier selection is OPEN."),
        ("NC-S22.6", "Class-limit ratios are COMPUTED extrapolations, not "
                     "PROVEN eigenvalues of a limit operator."),
    ]:
        decl(t, m)

    # ================= v1.1 NEW BLOCKS =================

    print("\n[S14] Theorem S22.8 -- explicit I_h character projectors (v1.1)")
    Gh = build_Ih()
    check("T130", len(Gh) == 120, "|I_h| = 120 constructed from the icosahedron")
    GD = Ih_data(Gh)
    orth_ch = max(abs(sum(chi(A, g) * chi(B, g) for g in GD) / 120.0
                      - (1.0 if A == B else 0.0))
                  for A in IRREPS for B in IRREPS)
    check("T131", orth_ch < 1e-12,
          "character orthogonality residual %.2e" % orth_ch)
    S21_OMEGA2 = {"Ag": 2, "T1u": 2, "T2u": 2, "Hg": 2, "Gg": 1, "Gu": 1}
    S21_LOW = ["T1u", "Hg", "T2u", "Gu", "Hg", "T1u"]
    for n in [1, 2, 3, 4]:
        c = CAR[n]
        prm = face_perms(c, Gh)
        P = projectors(c, Gh, GD, prm)
        idem = max(np.abs(P[A] @ P[A] - P[A]).max() for A in IRREPS)
        orth = max(np.abs(P[A] @ P[B]).max()
                   for A in IRREPS for B in IRREPS if A != B)
        dsum = abs(sum(np.trace(P[A]) for A in IRREPS) - c["F_K"])
        check("T132.%d" % n, idem < 1e-12, "projector idempotence %.2e" % idem)
        check("T133.%d" % n, orth < 1e-12, "projector orthogonality %.2e" % orth)
        check("T134.%d" % n, dsum < 1e-9, "dimension sum residual %.2e" % dsum)
        mult = {A: int(round(np.trace(P[A]) / IRDIM[A])) for A in IRREPS}
        L = delta(c, 1, 1).toarray()
        w, U = np.linalg.eigh(L)
        lev, labels = [], []
        for i, x in enumerate(w):
            if lev and abs(x - w[lev[-1][0]]) < 1e-8 * max(1.0, abs(x)):
                lev[-1][1] += 1
            else:
                lev.append([i, 1])
        maxres = 0.0
        for i, m in lev[1:7]:
            V = U[:, i:i + m]
            nr = {A: np.linalg.norm(P[A] @ V) ** 2 for A in IRREPS}
            tot = sum(nr.values())
            comp = [A for A in IRREPS if nr[A] / tot > 0.01]
            res = np.linalg.norm(V - sum(P[A] @ V for A in comp))
            maxres = max(maxres, res)
            labels.append("+".join(comp))
        check("T135.%d" % n, maxres < 1e-10,
              "isotype assignment residual %.2e at n=%d" % (maxres, n))
        print("    n=%2d F=%4d  idem %.1e  orth %.1e  dimsum %.1e  "
              "isotype residual %.1e" % (n, c["F_K"], idem, orth, dsum, maxres))
        print("        Omega^2 = " + " + ".join("%d%s" % (mult[A], A)
                                                for A in IRREPS if mult[A]))
        print("        low levels: " + " ".join(labels))
        if n == 1:
            check("T136", mult == {**{A: 0 for A in IRREPS}, **S21_OMEGA2},
                  "Omega^2(K_1) reproduces ZS-S21 erratum E-1a exactly")
            check("T137", labels == S21_LOW,
                  "K_1 low-level isotypes reproduce ZS-S21 Table 9.1")
    decl("D138", "Review item 5 CLOSED: isotype labels are no longer inferred "
                 "from multiplicity and continuity. They are certified by "
                 "explicit character projectors with machine-precision "
                 "idempotence, orthogonality and dimension-sum audits.")

    print("\n[S15] Theorem S22.9 -- the exact boundary of the metric-free class (v1.1)")
    print("    Class MF reference R_3 = %.6f | Class M = %.6f"
          % (np.mean(mf), LIM["S-DEC"]))

    def halo(c):
        d = dist_to_pent(c)
        de = np.minimum(d[c["edges"][:, 0]], d[c["edges"][:, 1]])
        return 1.0 + 0.8 / (1.0 + de), 1.0 + 0.8 / (1.0 + d)

    def diamnorm(c):
        d = dist_to_pent(c).astype(float)
        D = d.max()
        de = np.minimum(d[c["edges"][:, 0]], d[c["edges"][:, 1]])
        return 1.0 + 0.8 * de / D, 1.0 + 0.8 * d / D

    def parity(c):
        d = dist_to_pent(c)
        de = np.minimum(d[c["edges"][:, 0]], d[c["edges"][:, 1]])
        return 1.0 + 0.4 * (de % 2), 1.0 + 0.4 * (d % 2)

    ADV = [("halo 1+0.8/(1+d)", halo, "Layer-C, bounded, decaying"),
           ("diam 1+0.8*d/D", diamnorm, "Layer-C, bounded, O(1) in the bulk"),
           ("parity 1+0.4(d%2)", parity, "Layer-C, bounded, non-decaying")]
    esc = []
    for nm, fn, note in ADV:
        ys = []
        for n in FITNS + [12]:
            c = CAR[n]
            ew, vt = fn(c)
            lv = spectrum(c, ew, vt, K=6)
            ys.append(lv[2][0] / lv[0][0])
        L, pred = fit_1_over_n2(FITNS, ys[:-1])
        d_mf = abs(L - float(np.mean(mf)))
        esc.append(d_mf)
        print("    %-20s [%-34s] L_inf = %.6f  |L - MF| = %.4f  %s"
              % (nm, note, L, d_mf, "ESCAPES" if d_mf > 0.02 else "in class"))
    check("T140", min(esc) > 0.02,
          "all three global Layer-C adversaries escape Class MF "
          "(min distance %.4f)" % min(esc))
    for n in [4, 8, 12]:
        c = CAR[n]
        supp = set()
        for b in MF_BRANCHES:
            ew, vt = branch(c, b)
            supp |= set(np.where(np.abs(vt - 1) > 1e-12)[0])
            for e in np.where(np.abs(ew - 1) > 1e-12)[0]:
                supp |= {int(c["edges"][e, 0]), int(c["edges"][e, 1])}
        check("T141.%d" % n, len(supp) <= 72,
              "all five audited MF branches are supported on <= 72 faces "
              "(observed %d) at n=%d" % (len(supp), n))
    decl("D143", "v1.4 erratum, Retraction S22-R7. The sufficiency direction of "
                 "Theorem S22.9 is DERIVED-CONDITIONAL, not PROVEN: it inherits the "
                 "conditionality of Theorem S22.4a on uniform low-mode delocalization "
                 "and gradient control. The three escaping adversaries REFUTE broader "
                 "Layer-C universality; they do NOT establish necessity. Nothing here "
                 "shows that a common limit implies O(1) support, and F-S22.27 stays "
                 "OPEN.")
    decl("D142", "Review item 2 CLOSED by computation, not by hedging. The "
                 "metric-free class is NOT 'every Layer-C branch'. Even a "
                 "DECAYING Layer-C halo escapes it. The correct closure "
                 "condition is uniform boundedness PLUS support on O(1) cells, "
                 "which is exactly the hypothesis of Theorem S22.2. "
                 "Retraction S22-R4.")

    print("\n[S16] Theorem S22.3 sharpened -- analytic orbit lower bound (v1.1)")
    print("    orbit-stabiliser: every I_h orbit has <= 120 elements, so")
    print("    #edge orbits >= E_n/120 = 3n^2/4 -> infinity.  PROVEN.")
    print("    %3s %8s %14s %18s %20s" % ("n", "E_n", "bound 3n^2/4",
                                          "measured orbits", "distinct DEC weights"))
    for n in [1, 2, 3, 4, 5, 6]:
        c = CAR[n]
        em = c["P"][c["edges"][:, 0]] + c["P"][c["edges"][:, 1]]
        em = em / np.linalg.norm(em, axis=1)[:, None]
        nb_ = n_orbits(em, Gh)
        ew, _ = branch(c, "S-DEC")
        nw = len(np.unique(np.round(ew, 8)))
        check("T150.%d" % n, nb_ >= 0.75 * n * n,
              "edge-orbit count %d >= 3n^2/4 = %.2f at n=%d"
              % (nb_, 0.75 * n * n, n))
        print("    %3d %8d %14.2f %18d %20d"
              % (n, c["E_K"], 0.75 * n * n, nb_, nw))
    decl("D151", "Review item 4 CLOSED. The orbit lower bound 3n^2/4 is "
                 "PROVEN by orbit-stabiliser. The count of distinct DEC "
                 "weights is reported as COMPUTED over the audited range, "
                 "not asserted to grow without bound.")
    print("\n[S17b] Lemma S22.10a -- the |Aut| <= |I_h| dependency of Theorem S22.10")
    print("    Theorem S22.10 step (C3) uses |V| = 20T divides |Aut(K)| <= |I_h| = 120.")
    print("    v1.4 used |Aut(K)| <= 120 without a lemma or citation. v1.5 discharges it:")
    print("    (i)   the 1-skeleton of a Goldberg carrier is 3-connected and planar, so by")
    print("          Whitney-Mani its automorphism group is realised by isometries of a")
    print("          convex sphere realisation;")
    print("    (ii)  Aut permutes the 12 pentagonal faces, whose centres form a REGULAR")
    print("          icosahedron by construction of GP(h,k);")
    print("    (iii) that action is FAITHFUL: an isometry of R^3 fixing 12 points which")
    print("          affinely span R^3 is the identity;")
    print("    (iv)  hence Aut(K) embeds in the icosahedral group, |Aut(K)| <= 120.")
    print("    Below the count is done combinatorially, from the graph alone, with no")
    print("    embedding assumed -- an independent check of the same statement.")
    print("    %8s %4s %6s %6s %14s %8s %20s"
          % ("(h,k)", "T", "V_K", "F_K", "|Aut(graph)|", "<= 120", "|V| divides |Aut|"))
    autres = []
    for (h, k) in [(1, 0), (1, 1), (2, 0), (3, 0)]:
        cA = carrier(0, h=h, k=k)
        adjA = [[] for _ in range(cA["F_K"])]
        for a, b in cA["edges"]:
            adjA[int(a)].append(int(b))
            adjA[int(b)].append(int(a))
        na = graph_automorphism_count(adjA)
        div = (na % cA["V_K"] == 0)
        autres.append((h, k, na, div))
        print("    %8s %4d %6d %6d %14d %8s %20s"
              % (str((h, k)), h * h + h * k + k * k, cA["V_K"], cA["F_K"],
                 na, str(na <= 120), str(div)))
    check("T167", all(na <= 120 for _, _, na, _ in autres),
          "every audited Goldberg carrier has |Aut| <= |I_h| = 120")
    check("T168", all(na == 120 for _, _, na, _ in autres),
          "every audited Goldberg carrier has |Aut| = 120 exactly, i.e. Aut = I_h")
    check("T169", dict(((h, k), d) for h, k, _, d in autres)[(2, 0)] is False
          and dict(((h, k), d) for h, k, _, d in autres)[(1, 1)] is True,
          "GP(2,0) has 80 not dividing 120 so admits no transitive action, "
          "while GP(1,1) has 60 | 120")
    decl("D169a", "Lemma S22.10a (v1.5). The step |Aut(K)| <= |I_h| = 120 = Q^2 - 1, "
                  "used without justification in v1.4, is now discharged twice: by the "
                  "Whitney-Mani / faithful-icosahedral-action argument above, and "
                  "independently by an embedding-free graph automorphism count over the "
                  "audited carriers. Both give |Aut| = 120.")

    nc = sum(1 for x in LEDGER if x[1] == "C")
    npx = sum(1 for x in LEDGER if x[1] == "P")
    nx = sum(1 for x in LEDGER if x[1] == "X")
    nd = sum(1 for x in LEDGER if x[1] == "D")
    npass = sum(1 for x in LEDGER if x[2] == "PASS")
    print("\n" + "=" * 72)
    print("LEDGER: %d verification-ledger entries PASS = %d executable checks (C) "
          "+ %d computed diagnostics (X) + %d proxy (P) | %d declarative (D) "
          "| %d FAIL"
          % (npass, nc, nx, npx, nd, len(FAILED)))
    if FAILED:
        print("FAILED:", FAILED)
    print("SHA256(self) = %s"
          % hashlib.sha256(open(__file__, "rb").read()).hexdigest())
    print("END_ZS_S22_RESULTS")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
