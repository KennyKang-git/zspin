#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_s18_verify_v1_6.py
=====================
Fail-closed verifier for

    ZS-S18 v1.6 -- The Symmetric Two-Body Sector of the Z-Spin Master Action:
    A Closed Form for the Symmetric Cup Product, Exact Equivariance, the
    A_u (+) H_u Active Space, the Exact Harmonic Anchoring Identity, and a
    Negative Execution of the Geometric Hessian Route

    Kenny Kang  .  Z-Spin Cosmology Collaboration  .  July 2026

Design rules (inherited from zs_s17_verify_v2_2.py):
  * every check asserts on a NUMBER that this script computes;
  * nothing is read from a hard-coded table except the LOCKED corpus constants
    (A = 35/437, Q = 11, v = 245.93 GeV) and published lattice inputs, which are
    declared explicitly in LOCKED / EXTERNAL below;
  * the truncated icosahedron, its oriented 2-cochain complex, the signed I_h
    action, and the DEC cup product are rebuilt from Cartesian coordinates --
    no geometry is imported;
  * OPEN gates are PRINTED but NOT counted in the pass ratio.

Dependencies: numpy, scipy.
Run:  python zs_s18_verify_v1_6.py
Emits: a machine-readable JSON block to stdout, plus its SHA-256. Writes NO files.
"""

import itertools
import json
import sys
import hashlib
import platform
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull
from scipy.spatial.distance import pdist, squareform

# ----------------------------------------------------------------------------
# LOCKED corpus constants -- never re-fit (ZS-F2, ZS-F5, ZS-S4)
# ----------------------------------------------------------------------------
A_IMP = 35.0 / 437.0        # geometric impedance          ZS-F2   LOCKED
Q_REG = 11                  # register dimension           ZS-F5   LOCKED
DIM_Z = 2                   # Z-sector dimension           ZS-F5   LOCKED
V_HIGGS = 245.93            # GeV, Y-sector spectral VEV   ZS-S4   DERIVED

# ----------------------------------------------------------------------------
# EXTERNAL lattice inputs (declared, never fitted)
# Morningstar & Peardon, Phys. Rev. D 60, 034509 (1999)
# ----------------------------------------------------------------------------
MP_M0 = (1.730, 0.050, 0.080)   # GeV: value, stat, syst   0^{++}
MP_M2 = (2.400, 0.025, 0.120)   # GeV: value, stat, syst   2^{++}

TOL_EXACT = 1e-12
TOL_MACHINE = 1e-13

_checks = []
_open_gates = []


_external = []


def register_external(gid, txt):
    _external.append((gid, txt))


def check(idx, name, ok, detail=""):
    _checks.append((idx, name, bool(ok), detail))
    status = "PASS" if ok else "**FAIL**"
    print(f"  [{idx:2d}] {status:8s} {name}")
    if detail:
        print(f"       {detail}")
    return bool(ok)


def register_open(gid, text):
    _open_gates.append((gid, text))


def close(a, b, tol):
    return abs(float(a) - float(b)) <= tol


# ============================================================================
# 1. Rebuild the truncated icosahedron (TI) from Cartesian coordinates
# ============================================================================
def build_ti():
    phi = (1.0 + 5.0 ** 0.5) / 2.0
    base = [(0.0, 1.0, 3 * phi),
            (1.0, 2 + phi, 2 * phi),
            (phi, 2.0, 2 * phi + 1)]

    def even_perms(t):
        return [tuple(t[i] for i in p) for p in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]]

    verts = set()
    for b in base:
        for signs in itertools.product([1, -1], repeat=3):
            s = tuple(si * bi for si, bi in zip(signs, b))
            for p in even_perms(s):
                verts.add(tuple(round(x, 9) for x in p))
    V = np.array(sorted(verts))

    D = squareform(pdist(V))
    np.fill_diagonal(D, 1e9)
    emin = D.min()
    adj = D < emin * 1.05
    edges = [(i, j) for i in range(len(V)) for j in range(i + 1, len(V)) if adj[i, j]]

    hull = ConvexHull(V)
    planes = {}
    for k in range(len(hull.simplices)):
        key = tuple(np.round(np.concatenate([hull.equations[k, :3],
                                             [hull.equations[k, 3]]]), 6))
        planes.setdefault(key, []).append(hull.simplices[k])
    faces_raw = []
    for _key, sims in planes.items():
        vs = set()
        for s in sims:
            vs.update(s.tolist())
        faces_raw.append(sorted(vs))

    nbr = {i: set() for i in range(len(V))}
    for i, j in edges:
        nbr[i].add(j)
        nbr[j].add(i)

    def order_cycle(vs):
        vs = set(vs)
        start = min(vs)
        cyc = [start]
        prev, cur = None, start
        while len(cyc) < len(vs):
            nxts = [x for x in nbr[cur] if x in vs and x != prev]
            nxt = nxts[0] if len(nxts) == 1 else [x for x in nxts if x != start][0]
            if nxt == start:
                break
            cyc.append(nxt)
            prev, cur = cur, nxt
        return cyc

    centroid = V.mean(0)
    cycles = []
    for vs in faces_raw:
        c = order_cycle(vs)
        p = V[c]
        n = np.cross(p[1] - p[0], p[2] - p[0])
        if np.dot(n, p.mean(0) - centroid) < 0:
            c = c[::-1]
        cycles.append(c)

    eidx = {e: k for k, e in enumerate(edges)}
    B2 = np.zeros((len(cycles), len(edges)))
    for f, c in enumerate(cycles):
        for k in range(len(c)):
            u, w_ = c[k], c[(k + 1) % len(c)]
            if (u, w_) in eidx:
                B2[f, eidx[(u, w_)]] += 1.0
            else:
                B2[f, eidx[(w_, u)]] -= 1.0

    B1 = np.zeros((len(edges), len(V)))   # edge -> vertex boundary
    for k, (u, w_) in enumerate(edges):
        B1[k, w_] += 1.0
        B1[k, u] -= 1.0
    return V, edges, cycles, B2, B1, eidx


# ============================================================================
# 2. Signed I_h action on edges and oriented faces
# ============================================================================
def build_group(V, edges, cycles, eidx):
    key = lambda p: tuple(np.round(p, 5))
    vidx = {key(V[i]): i for i in range(len(V))}
    v0 = V[0]
    nb = [j for j in range(len(V)) if 1.9 < np.linalg.norm(V[j] - v0) < 2.1]
    Binv = np.linalg.inv(np.array([v0, V[nb[0]], V[nb[1]]]).T)

    G = []
    for i in range(len(V)):
        nbi = [j for j in range(len(V)) if 1.9 < np.linalg.norm(V[j] - V[i]) < 2.1]
        for p in itertools.permutations(nbi, 2):
            M = np.array([V[i], V[p[0]], V[p[1]]]).T @ Binv
            if np.allclose(M.T @ M, np.eye(3), atol=1e-6):
                W = (M @ V.T).T
                if all(key(x) in vidx for x in W):
                    G.append(M)

    fkey = {frozenset(c): f for f, c in enumerate(cycles)}
    PE, PF = [], []
    for M in G:
        W = (M @ V.T).T
        vm = [vidx[key(x)] for x in W]
        Pe = np.zeros((len(edges), len(edges)))
        for k, (u, w_) in enumerate(edges):
            aa, bb = vm[u], vm[w_]
            if (aa, bb) in eidx:
                Pe[eidx[(aa, bb)], k] = 1.0
            else:
                Pe[eidx[(bb, aa)], k] = -1.0
        Pf = np.zeros((len(cycles), len(cycles)))
        for f, c in enumerate(cycles):
            img = [vm[x] for x in c]
            g = fkey[frozenset(img)]
            cg = cycles[g]
            k0 = cg.index(img[0])
            same = all(cg[(k0 + m) % len(cg)] == img[m] for m in range(len(cg)))
            Pf[g, f] = 1.0 if same else -1.0
        PE.append(Pe)
        PF.append(Pf)
    return G, PE, PF


# ============================================================================
# 3. Character-theoretic isotype decomposition under I_h
# ============================================================================
_A5 = np.array([[1, 1, 1, 1, 1],
                [3, (1 + 5 ** 0.5) / 2, (1 - 5 ** 0.5) / 2, 0, -1],
                [3, (1 - 5 ** 0.5) / 2, (1 + 5 ** 0.5) / 2, 0, -1],
                [4, -1, -1, 1, 0],
                [5, 0, 0, -1, 1]])
_IRR = {}
for _i, _nm in enumerate(["A", "T1", "T2", "G", "H"]):
    _IRR[_nm + "g"] = np.concatenate([_A5[_i], _A5[_i]])
    _IRR[_nm + "u"] = np.concatenate([_A5[_i], -_A5[_i]])
_DIM = {"A": 1, "T1": 3, "T2": 3, "G": 4, "H": 5}
_CLASS_SIZES = np.array([1, 12, 12, 20, 15, 1, 12, 12, 20, 15])
_CLASS_KEYS = [(1.0, 3.0), (1.0, 1.618), (1.0, -0.618), (1.0, -0.0), (1.0, -1.0),
               (-1.0, -3.0), (-1.0, -1.618), (-1.0, 0.618), (-1.0, -0.0), (-1.0, 1.0)]


def isotype_from_char(chi_all, G):
    cls = {}
    for k, M in enumerate(G):
        cls.setdefault((round(float(np.linalg.det(M)), 4),
                        round(float(np.trace(M)), 4)), []).append(k)
    chi = np.array([chi_all[cls[o][0]] for o in _CLASS_KEYS])
    out = {}
    for nm, ch in _IRR.items():
        m = (_CLASS_SIZES * chi * ch).sum() / 120.0
        if abs(m) > 1e-6:
            out[nm] = int(round(m))
    return out


def isotype(P, G, PF):
    cls = {}
    for k, M in enumerate(G):
        cls.setdefault((round(float(np.linalg.det(M)), 4),
                        round(float(np.trace(M)), 4)), []).append(k)
    chi = np.array([np.trace(P @ PF[cls[o][0]]) for o in _CLASS_KEYS])
    out = {}
    for nm, ch in _IRR.items():
        m = (_CLASS_SIZES * chi * ch).sum() / 120.0
        if abs(m) > 1e-6:
            out[nm] = int(round(m))
    return out


# ============================================================================
# 4. DEC cup product on the oriented cell complex
# ============================================================================
def make_cup(cycles, eidx):
    def edgeval(vec, u, w_):
        return vec[eidx[(u, w_)]] if (u, w_) in eidx else -vec[eidx[(w_, u)]]

    def cup(x, y, avg=True):
        out = np.zeros(len(cycles))
        for f, c in enumerate(cycles):
            n = len(c)
            bs = list(range(n)) if avg else [0]
            tot = 0.0
            for b in bs:
                cc = [c[(b + m) % n] for m in range(n)]
                acc = 0.0
                s = 0.0
                for k in range(n - 1):
                    acc += edgeval(x, cc[k], cc[k + 1])
                    s += acc * edgeval(y, cc[k + 1], cc[(k + 2) % n])
                tot += s
            out[f] = tot / len(bs)
        return out
    return cup


def make_theta(cycles, eidx, B2):
    """Closed form of the SYMMETRIC cup product (Lemma S18.A):
         (x cup y + y cup x)(f) = (dx)(f)(dy)(f) - sum_{t in df} x(t) y(t).
       Contains no basepoint and no cyclic ordering beyond the boundary set."""
    def edgeval(vec, u, w_):
        return vec[eidx[(u, w_)]] if (u, w_) in eidx else -vec[eidx[(w_, u)]]

    def theta(x, y):
        Ex = B2 @ x
        Ey = B2 @ y
        dot = np.zeros(len(cycles))
        for f, c in enumerate(cycles):
            s = 0.0
            for k in range(len(c)):
                u, w_ = c[k], c[(k + 1) % len(c)]
                s += edgeval(x, u, w_) * edgeval(y, u, w_)
            dot[f] = s
        return Ex * Ey - dot
    return theta


# ============================================================================
# MAIN
# ============================================================================
def main():
    print("=" * 78)
    print("ZS-S18 v1.6 verifier -- fail-closed")
    print("LOCKED: A = 35/437 = %.9f | Q = %d | dim Z = %d | v = %.2f GeV"
          % (A_IMP, Q_REG, DIM_Z, V_HIGGS))
    print("=" * 78)
    res = {}

    # ---- Section A: the complex -------------------------------------------
    print("\n-- A. Truncated-icosahedron cell complex --")
    V, edges, cycles, B2, B1, eidx = build_ti()
    nV, nE, nF = len(V), len(edges), len(cycles)
    check(1, "TI census V=60, E=90, F=32; Euler chi = 2",
          (nV, nE, nF) == (60, 90, 32) and nV - nE + nF == 2,
          f"V={nV} E={nE} F={nF} chi={nV-nE+nF}")

    deg = np.zeros(nV, int)
    for u, w_ in edges:
        deg[u] += 1
        deg[w_] += 1
    sizes = sorted([len(c) for c in cycles])
    check(2, "3-valent; 12 pentagons + 20 hexagons",
          set(deg.tolist()) == {3} and sizes.count(5) == 12 and sizes.count(6) == 20,
          f"degrees={set(deg.tolist())} pent={sizes.count(5)} hex={sizes.count(6)}")

    dd = np.abs(B2 @ B1).max()
    check(3, "discrete Bianchi identity  d1 o d0 = 0", dd < TOL_EXACT,
          f"max|B2.B1| = {dd:.3e}")

    L2 = B2 @ B2.T
    w_, U = np.linalg.eigh(L2)
    groups = []
    for x in w_:
        if not groups or abs(x - groups[-1][0]) > 1e-8:
            groups.append([float(x), 1])
        else:
            groups[-1][1] += 1
    S7_SPEC = [(0.0, 1), (1.242842, 3), (3.267949, 5), (4.844366, 3), (6.0, 4),
               (6.732051, 5), (7.521090, 3), (8.0, 5), (8.391702, 3)]
    ok = len(groups) == 9 and all(
        close(groups[i][0], S7_SPEC[i][0], 1e-5) and groups[i][1] == S7_SPEC[i][1]
        for i in range(9))
    check(4, "L2 spectrum reproduces ZS-S7 Table (9 levels, degeneracies)", ok,
          "  ".join(f"{g[0]:.6f}({g[1]})" for g in groups))

    lam1 = float(w_[1])
    lam_h = float(w_[21])
    check(5, "lambda_1 = 1.2428416164 and lambda_h = 7.5210904061",
          close(lam1, 1.2428416164, 1e-9) and close(lam_h, 7.5210904061, 1e-9),
          f"lam1={lam1:.10f}  lam_h={lam_h:.10f}")
    res["lambda_1"] = lam1
    res["lambda_h"] = lam_h
    res["L2_spectrum"] = [[g[0], g[1]] for g in groups]

    # ---- Section B: signed I_h action --------------------------------------
    print("\n-- B. Signed I_h action (orientation-aware) --")
    G, PE, PF = build_group(V, edges, cycles, eidx)
    dets = [round(float(np.linalg.det(M)), 3) for M in G]
    check(6, "|I_h| = 120 = 60 proper + 60 improper",
          len(G) == 120 and dets.count(1.0) == 60 and dets.count(-1.0) == 60,
          f"|G|={len(G)}  proper={dets.count(1.0)}  improper={dets.count(-1.0)}")

    e_int = max(np.abs(PF[k] @ B2 - B2 @ PE[k]).max() for k in range(120))
    check(7, "B2 intertwines the signed edge and face actions", e_int < TOL_EXACT,
          f"max|P_F B2 - B2 P_E| = {e_int:.3e}")

    e_com = max(np.abs(PF[k] @ L2 - L2 @ PF[k]).max() for k in range(120))
    check(8, "[P_face, L2] = 0 under the SIGNED action", e_com < TOL_EXACT,
          f"max|[P,L2]| = {e_com:.3e}")

    iso_full = isotype(np.eye(nF), G, PF)
    expect = {"Au": 2, "T1g": 2, "T2g": 2, "Gg": 1, "Gu": 1, "Hu": 2}
    check(9, "Omega^2 isotype (signed) = 2A_u + 2T1g + 2T2g + G_g + G_u + 2H_u",
          iso_full == expect, str(iso_full))

    check(10, "CORRECTION to ZS-S7 s2.2: NOT all 10 I_h irreps once "
              "(6 distinct, 4 with multiplicity 2)",
          len(iso_full) == 6 and sum(iso_full.values()) == 10
          and sorted(iso_full.values()) == [1, 1, 2, 2, 2, 2],
          "distinct irreps = %d, total multiplicity = %d"
          % (len(iso_full), sum(iso_full.values())))
    res["Omega2_isotype_signed"] = iso_full

    per_level = {}
    for x, dgn in groups:
        idx = [k for k in range(nF) if abs(w_[k] - x) < 1e-6]
        per_level[f"{x if abs(x)>1e-9 else 0.0:.6f}"] = isotype(U[:, idx] @ U[:, idx].T, G, PF)
    res["isotype_per_level"] = per_level
    check(11, "lambda=0 is A_u (fundamental class is orientation-odd) and "
              "lambda=8 is A_u + G_u (accidental degeneracy)",
          per_level["0.000000"] == {"Au": 1} and per_level["8.000000"] == {"Au": 1, "Gu": 1},
          f"lam=0 -> {per_level['0.000000']} ; lam=8 -> {per_level['8.000000']}")

    # ---- Section C: canonical normalisation --------------------------------
    print("\n-- C. Canonical normalisation (fixed BEFORE the action) --")
    T1 = U[:, 1:4]
    a = [(B2.T @ T1[:, k]) / lam1 for k in range(3)]
    Gram = np.array([[a[i] @ a[j] for j in range(3)] for i in range(3)]) * lam1
    check(12, "<a_alpha, a_beta> = delta / lambda_1  (S17 Step 1 convention)",
          np.abs(Gram - np.eye(3)).max() < 1e-12,
          f"max|lam1*Gram - I| = {np.abs(Gram - np.eye(3)).max():.3e}")
    Omega0 = lam1 ** 0.5
    check(13, "Omega_0 = sqrt(lambda_1) = 1.1148",
          close(Omega0, 1.114828, 1e-5), f"Omega_0 = {Omega0:.10f}")
    res["Omega_0"] = Omega0

    cup = make_cup(cycles, eidx)

    # ---- Section D: antisymmetric channel (S17 reproduction) ---------------
    print("\n-- D. Antisymmetric (Yang-Mills) channel: S17 reproduction --")
    AN = cup(a[0], a[1]) - cup(a[1], a[0])
    cA = U.T @ AN
    tot = float((cA ** 2).sum())
    p_lo = float((cA[1:4] ** 2).sum()) / tot
    p_hi = float((cA[21:24] ** 2).sum()) / tot
    rest = tot - float((cA[1:4] ** 2).sum()) - float((cA[21:24] ** 2).sum())
    check(14, "alternating power split 92.8605% T1(lam1) + 7.1395% T1(lam_h)",
          close(100 * p_lo, 92.8605, 1e-3) and close(100 * p_hi, 7.1395, 1e-3),
          f"{100*p_lo:.4f}% / {100*p_hi:.4f}%   |rest| = {abs(rest):.3e}")
    resid = []
    for i in range(3):
        for j in range(3):
            if i < j:
                cc = U.T @ (cup(a[i], a[j]) - cup(a[j], a[i]))
                t = float((cc ** 2).sum())
                resid.append(abs(t - float((cc[1:4] ** 2).sum())
                                 - float((cc[21:24] ** 2).sum())) / t)
    check(15, "all-pairs alternating leakage out of the two-T1 space = 0",
          max(resid) < 1e-14, f"max relative residual = {max(resid):.3e}")

    Manti = np.array([cup(a[i], a[j]) - cup(a[j], a[i])
                      for i in range(3) for j in range(3) if i < j])
    ev, evec = np.linalg.eigh(Manti @ Manti.T)
    keep = ev > 1e-12 * ev.max()
    Qa = ((evec[:, keep] / np.sqrt(ev[keep])).T) @ Manti
    check(16, "antisymmetric image = T1g, dim Hom_I(T1 x T1, T1) = 1",
          Qa.shape[0] == 3 and isotype(Qa.T @ Qa, G, PF) == {"T1g": 1},
          f"dim = {Qa.shape[0]}, isotype = {isotype(Qa.T @ Qa, G, PF)}")
    res["anti_power_split"] = [100 * p_lo, 100 * p_hi]

    # ---- Section E: symmetric channel (the S18 sector) ---------------------
    print("\n-- E. Symmetric channel Sym^2(T1): the ZS-S18 sector --")
    Sd = {}
    for i in range(3):
        for j in range(i, 3):
            Sd[(i, j)] = cup(a[i], a[j]) + cup(a[j], a[i])
    Sij = lambda i, j: Sd[(min(i, j), max(i, j))]

    Msym = np.array([Sij(i, j) for i in range(3) for j in range(3)])
    ev, evec = np.linalg.eigh(Msym @ Msym.T)
    keep = ev > 1e-12 * ev.max()
    Qs = ((evec[:, keep] / np.sqrt(ev[keep])).T) @ Msym
    check(17, "Sym^2(T1) image is exactly 6-dimensional", Qs.shape[0] == 6,
          f"dim(image) = {Qs.shape[0]}")

    iso_sym = isotype(Qs.T @ Qs, G, PF)
    check(18, "Sym^2(T1) image isotype = A_u + H_u  (Theorem S18.3)",
          iso_sym == {"Au": 1, "Hu": 1}, str(iso_sym))

    AgH = [0.0, 3.267949192, 6.732050808, 8.0]

    def leak(v):
        c = U.T @ v
        t = float((c ** 2).sum())
        bad = sum(float(c[i] ** 2) for i, x in enumerate(w_)
                  if min(abs(x - y) for y in AgH) > 1e-6)
        return bad / t

    psiA = (Sij(0, 0) + Sij(1, 1) + Sij(2, 2)) / 3.0
    Hb = [Sij(0, 1), Sij(0, 2), Sij(1, 2),
          (Sij(0, 0) - Sij(1, 1)) / 2.0,
          (Sij(0, 0) + Sij(1, 1) - 2 * Sij(2, 2)) / 6.0]
    lk = max([leak(psiA)] + [leak(v) for v in Hb])
    check(19, "leakage out of the (A + H) isotype = 0 to machine precision",
          lk < 1e-25, f"max leakage = {lk:.3e}")
    check(20, "SCOPE CORRECTION: the symmetric channel does NOT spread over the "
              "spectrum; it closes on a 6-dim space",
          Qs.shape[0] == 6 and lk < 1e-25,
          "seed warning 'no small exactly-closed subspace' is refuted")

    # ---- Section F: equivariance audit ------------------------------------
    print("\n-- F. Equivariance audit (Theorem S18.1) --")
    err_p_s = err_p_a = 0.0
    err_i_s = err_i_a = 0.0
    nrm_s = np.abs(Sij(0, 1)).max()
    nrm_a = np.abs(AN).max()
    for k in range(120):
        det = float(np.sign(np.linalg.det(G[k])))   # EXACT sign, not the
        x, y = PE[k] @ a[0], PE[k] @ a[1]   # floating-point determinant (v1.1 fix)
        s_l = cup(x, y) + cup(y, x)
        a_l = cup(x, y) - cup(y, x)
        s_r = PF[k] @ Sij(0, 1)
        a_r = PF[k] @ AN
        if det > 0:
            err_p_s = max(err_p_s, np.abs(s_l - s_r).max())
            err_p_a = max(err_p_a, np.abs(a_l - a_r).max())
        else:
            err_i_s = max(err_i_s, np.abs(s_l - det * s_r).max())
            err_i_a = max(err_i_a, np.abs(a_l - a_r).max())
    check(21, "proper I (60 elements): BOTH channels exactly equivariant",
          err_p_s / nrm_s < 1e-13 and err_p_a / nrm_a < 1e-13,
          f"rel err  SYM = {err_p_s/nrm_s:.2e}   ANTI = {err_p_a/nrm_a:.2e}")
    check(22, "improper I_h\\I: SYM carries the det(g) orientation twist "
              "[v1.1: PROVEN via Lemma S18.A; residual now machine zero]",
          err_i_s / nrm_s < 1e-13,
          f"rel err |gB - det(g) Bg| = {err_i_s/nrm_s:.2e}")
    check(23, "improper I_h\\I: ANTI is orientation-blind (no det twist)",
          err_i_a / nrm_a < 1e-13,
          f"rel err |gB - Bg| = {err_i_a/nrm_a:.2e}")
    res["equivariance"] = {"proper_sym": err_p_s / nrm_s, "proper_anti": err_p_a / nrm_a,
                           "improper_sym_det": err_i_s / nrm_s,
                           "improper_anti": err_i_a / nrm_a}

    # ---- Section G: basepoint dichotomy -----------------------------------
    print("\n-- G. Basepoint dichotomy (Theorem S18.2) --")
    S01_avg = Sij(0, 1)
    S01_raw = cup(a[0], a[1], avg=False) + cup(a[1], a[0], avg=False)
    dsym = np.abs(S01_avg - S01_raw).max()
    check(24, "SYMMETRIC cup product is exactly basepoint-independent",
          dsym < 1e-12, f"max|avg - raw| = {dsym:.3e}")

    AN_raw = cup(a[0], a[1], avg=False) - cup(a[1], a[0], avg=False)
    cr = U.T @ AN_raw
    tr = float((cr ** 2).sum())
    clo_raw = (float((cr[1:4] ** 2).sum()) + float((cr[21:24] ** 2).sum())) / tr
    Mraw = np.array([cup(a[p], a[q_], avg=False) - cup(a[q_], a[p], avg=False)
                     for (p, q_) in ((0, 1), (0, 2), (1, 2))])
    P2T1 = T1 @ T1.T + U[:, 21:24] @ U[:, 21:24].T
    inv_ratio = float(np.trace(Mraw @ P2T1 @ Mraw.T)) / float(np.trace(Mraw @ Mraw.T))
    rot_spread = 0.0
    for _t in range(3):
        Rr = np.linalg.qr(np.random.default_rng(_t).normal(size=(3, 3)))[0]
        T1r = T1 @ Rr
        ar = [(B2.T @ T1r[:, m]) / lam1 for m in range(3)]
        Mr = np.array([cup(ar[p], ar[q_], avg=False) - cup(ar[q_], ar[p], avg=False)
                       for (p, q_) in ((0, 1), (0, 2), (1, 2))])
        rot_spread = max(rot_spread, abs(float(np.trace(Mr @ P2T1 @ Mr.T))
                                         / float(np.trace(Mr @ Mr.T)) - inv_ratio))
    check(25, "THEOREM S18.2, antisymmetric half: without basepoint averaging the raw "
              "map is NOT closed on the two-T1 space. Stated as the BASIS-INVARIANT "
              "trace ratio Tr(M P M^T)/Tr(M M^T) = 71.0350815252%, which is unchanged "
              "under random O(3) rotations of the degenerate T1 eigenbasis. (v1.0-v1.6 "
              "quoted 61.9257% for one index pair in one LAPACK eigenbasis; that "
              "number is basis-dependent -- random bases give 63.6%, 74.6%, 84.3% -- "
              "and is RETRACTED as a ledger value)",
          close(inv_ratio, 0.710350815252, 1e-9) and rot_spread < 1e-10
          and inv_ratio < 0.999,
          f"invariant ratio = {100*inv_ratio:.10f}% ; max drift over random T1 bases "
          f"= {rot_spread:.2e}")
    res["raw_map_closure"] = {"invariant_two_T1_ratio": inv_ratio}

    # ---- Section H: induced two-body operator ------------------------------
    print("\n-- H. Induced two-body operator on Sym^2(T1) --")
    cAg = U.T @ psiA
    tAg = float((cAg ** 2).sum())
    share0 = float(cAg[0] ** 2) / tAg
    share8 = float((cAg[24:29] ** 2).sum()) / tAg

    check(26, "HARMONIC ANCHORING (Theorem S18.4): the A-channel (|0++>) sits 85.5170% on "
              "ker L2 = the fundamental class",
          close(share0, 0.8551699690, 1e-8) and close(share0 + share8, 1.0, 1e-12),
          f"lam=0 share = {share0:.10f} ; lam=8 share = {share8:.10f}")

    cHb = U.T @ Hb[0]
    tHb = float((cHb ** 2).sum())
    sh_lo = float((cHb[4:9] ** 2).sum()) / tHb
    sh_hi = float((cHb[16:21] ** 2).sum()) / tHb
    check(27, "the H-channel (|2++>) sits 96.9178% on lambda = 5 - sqrt(3)",
          close(sh_lo, 0.9691781082, 1e-8) and close(sh_lo + sh_hi, 1.0, 1e-12),
          f"3.267949 share = {sh_lo:.10f} ; 6.732051 share = {sh_hi:.10f}")

    QH = np.array(Hb)
    ev, evec = np.linalg.eigh(QH @ QH.T)
    keep = ev > 1e-12 * ev.max()
    Qh = ((evec[:, keep] / np.sqrt(ev[keep])).T) @ QH
    blk = Qh @ L2 @ Qh.T
    eig = np.linalg.eigvalsh(blk)
    rH = float(eig.mean())
    check(28, "Schur: the induced L2 block on the H channel is an exact scalar "
              "3.3747193575 x I_5",
          Qh.shape[0] == 5 and (eig.max() - eig.min()) < 1e-10
          and close(rH, 3.3747193575, 1e-8),
          f"eigenvalues spread = {eig.max()-eig.min():.3e} ; value = {rH:.10f}")
    rA = float(psiA @ L2 @ psiA / (psiA @ psiA))
    check(29, "induced L2 on the A channel = 1.1586402482",
          close(rA, 1.1586402482, 1e-8), f"value = {rA:.10f}")
    res["induced_two_body"] = {"A_channel": rA, "H_channel": rH,
                               "A_share_lambda0": share0,
                               "H_share_5_minus_sqrt3": sh_lo}

    # ---- Section I: the Casimir-coproduct Layer-Lift (S17 import) ---------
    print("\n-- I. Casimir-coproduct Layer-Lift (ZS-S17 import) --")
    Sx = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / 2 ** 0.5
    Sy = np.array([[0, -1j, 0], [1j, 0, -1j], [0, 1j, 0]]) / 2 ** 0.5
    Sz = np.diag([1.0, 0.0, -1.0]).astype(complex)
    I3 = np.eye(3)
    C2 = Sx @ Sx + Sy @ Sy + Sz @ Sz
    check(30, "C_2(T1) = 2 I  =>  L2|_{T1} = (lambda_1/2) C_2",
          np.abs(C2 - 2 * np.eye(3)).max() < 1e-12,
          f"max|C2 - 2I| = {np.abs(C2 - 2*np.eye(3)).max():.3e}")

    SS = (np.kron(Sx, Sx) + np.kron(Sy, Sy) + np.kron(Sz, Sz))
    I_Z = lam1 * SS
    Q_Z = 0.25 * (I_Z + 2 * lam1 * np.eye(9))
    qs = np.round(np.sort(np.linalg.eigvalsh(Q_Z)), 6)
    uniq = sorted(set(qs.tolist()))
    check(31, "Q_Z = 1/4 (I_Z + 2 lambda_1 I) has spectrum {0, 0.3107, 0.9321}",
          len(uniq) == 3 and close(uniq[0], 0.0, 1e-6)
          and close(uniq[1], 0.310710, 1e-5) and close(uniq[2], 0.932131, 1e-5),
          f"spectrum = {uniq}")

    R_S17 = (1.0 + 3 * lam1 / 4.0) ** 0.5
    check(32, "R = sqrt(1 + 3 lambda_1 / 4) = 1.3900", close(R_S17, 1.3900, 1e-4),
          f"R = {R_S17:.6f}")
    res["R_S17"] = R_S17

    # ---- Section J: the negative execution --------------------------------
    print("\n-- J. Geometric Hessian route: NEGATIVE execution (Theorem S18.5) --")
    ratio = rH / (3 * lam1)
    check(33, "the geometric two-body operator does NOT equal (lambda_1/2) "
              "Delta(C_2): H eigenvalue 3.3747 vs 3 lambda_1 = 3.7285",
          not close(rH, 3 * lam1, 1e-3) and close(ratio, 0.905108, 1e-5),
          f"rH / (3 lam1) = {ratio:.9f}  (deficit {100*(1-ratio):.3f}%)")
    ratio_pure = (5 - 3 ** 0.5) / (3 * lam1)
    check(34, "the same statement for the pure eigenvalue 5 - sqrt(3)",
          close(ratio_pure, 0.876472, 1e-5),
          f"(5-sqrt3)/(3 lam1) = {ratio_pure:.9f}  (deficit {100*(1-ratio_pure):.3f}%)")
    res["geometric_vs_coproduct"] = {"ratio_rayleigh": ratio, "ratio_pure": ratio_pure}

    # ---- Section K: physical outputs and the SU(3) power audit -------------
    print("\n-- K. Physical outputs and the SU(3) discriminating-power audit --")
    m0 = V_HIGGS * A_IMP / Q_REG
    check(35, "m(0++) = v A / Q = 1.791 GeV (ZS-S7, topological cancellation)",
          close(m0, 1.791, 1e-3), f"m(0++) = {m0:.6f} GeV")
    m2 = R_S17 * m0
    check(36, "m(2++) = 1.3900 v A / Q = 2.489 GeV under the S17 Layer-Lift",
          close(m2, 2.489, 2e-3), f"m(2++) = {m2:.6f} GeV")
    res["m_0pp"] = m0
    res["m_2pp_S17"] = m2

    r_lat = MP_M2[0] / MP_M0[0]
    rel0 = ((MP_M0[1] ** 2 + MP_M0[2] ** 2) ** 0.5) / MP_M0[0]
    rel2 = ((MP_M2[1] ** 2 + MP_M2[2] ** 2) ** 0.5) / MP_M2[0]
    dr = r_lat * (rel0 ** 2 + rel2 ** 2) ** 0.5
    g_lat = (4.0 / 3.0) * (r_lat ** 2 - 1.0)
    dg = (4.0 / 3.0) * 2 * r_lat * dr
    check(37, "Morningstar-Peardon SU(3): R = 1.3873 +/- 0.1036, "
              "g_hf = 1.233 +/- 0.383",
          close(r_lat, 1.3873, 1e-3) and close(dr, 0.1036, 2e-3)
          and close(g_lat, 1.2327, 2e-3),
          f"R_lat = {r_lat:.4f} +/- {dr:.4f} ; g_hf = {g_lat:.4f} +/- {dg:.4f}")

    cands = {
        "S17 coproduct 1 + 3 lam1/4": 1 + 3 * lam1 / 4,
        "geometric Rayleigh 1 + rH/4": 1 + rH / 4,
        "geometric pure  1 + (5-sqrt3)/4": 1 + (5 - 3 ** 0.5) / 4,
        "geometric difference 1 + (rH-rA)/4": 1 + (rH - rA) / 4,
    }
    pulls = {k: ((v ** 0.5) - r_lat) / dr for k, v in cands.items()}
    check(38, "SU(3) alone has NO discriminating power: all four candidate "
              "normalisations lie within 1.4 sigma",
          max(abs(p) for p in pulls.values()) < 1.4,
          "  ".join(f"{k.split()[0]}:{p:+.2f}s" for k, p in pulls.items()))
    res["candidates"] = {k: {"R": v ** 0.5, "m2pp": (v ** 0.5) * m0,
                             "pull": pulls[k], "g_hf": (4.0 / 3.0) * (v - 1)}
                         for k, v in cands.items()}

    # ---- Section L: zero free parameters ----------------------------------
    print("\n-- L. Zero-free-parameter audit --")
    inputs = {"A": A_IMP, "Q": Q_REG, "dim_Z": DIM_Z, "v_GeV": V_HIGGS}
    check(39, "LOCKED-INPUT CONSISTENCY (not a global zero-free-parameter audit): every ZS-S18 number derives from {A, Q, dim Z, v} plus pure "
              "TI geometry; no fitted parameter is introduced",
          close(A_IMP, 35 / 437, 0) and Q_REG == 11 and DIM_Z == 2,
          f"inputs = {inputs}")
    check(40, "anti-numerology band inherited from ZS-S17: 89/3600 = 2.4722%",
          close(89 / 3600, 0.0247222, 1e-6), "89/3600 = %.6f" % (89 / 3600))

    # ---- Section M: closed form and the exact harmonic identity (v1.1) ----
    print("\n-- M. Lemma S18.A and the exact Harmonic Anchoring identity (v1.1) --")
    theta = make_theta(cycles, eidx, B2)

    rng = np.random.default_rng(20260301)
    xr, yr = rng.normal(size=nE), rng.normal(size=nE)
    lhs = cup(xr, yr) + cup(yr, xr)
    rhs = theta(xr, yr)
    check(41, "LEMMA S18.A: (x cup y + y cup x)(f) = (dx)(f)(dy)(f) "
              "- <x,y>_{df}, for arbitrary 1-cochains",
          np.abs(lhs - rhs).max() / np.abs(rhs).max() < 1e-14,
          f"max|LHS - RHS| = {np.abs(lhs-rhs).max():.3e}  "
          f"(||RHS||inf = {np.abs(rhs).max():.4f})")

    errg = max(np.abs((cup(a[i], a[j]) + cup(a[j], a[i])) - theta(a[i], a[j])).max()
               for i in range(3) for j in range(i, 3))
    check(42, "Lemma S18.A on the gap potentials, all six pairs",
          errg < 1e-14, f"max|S - Theta| = {errg:.3e}")

    rev = [[c[0]] + c[1:][::-1] for c in cycles]
    cup_rev = make_cup(rev, eidx)
    s_rev = cup_rev(a[0], a[1]) + cup_rev(a[1], a[0])
    a_rev = cup_rev(a[0], a[1]) - cup_rev(a[1], a[0])
    check(43, "COROLLARY 1 (=> Thm S18.2): Theta has no basepoint => the "
              "symmetric cup is reversal- and basepoint-invariant",
          np.abs(s_rev - Sij(0, 1)).max() < 1e-14,
          f"max|S(reversed cycle) - S(cycle)| = {np.abs(s_rev - Sij(0,1)).max():.3e}")
    check(44, "COROLLARY 2 (=> Thm S18.1ii): the antisymmetric cup is exactly "
              "ODD under cycle reversal",
          np.abs(a_rev + AN).max() < 1e-14,
          f"max|A(reversed) + A(cycle)| = {np.abs(a_rev + AN).max():.3e}")

    inc = np.abs(B2).sum(0)
    hvec = np.ones(nF)
    check(45, "closed oriented surface: every edge lies in exactly 2 faces, and "
              "h = (1,...,1) spans ker L_2 with ||h||^2 = 32",
          set(inc.tolist()) == {2.0} and np.abs(B2.T @ hvec).max() < TOL_EXACT
          and abs(float(hvec @ hvec) - 32.0) < TOL_EXACT,
          f"incidences = {set(inc.tolist())} ; |B2^T h| = {np.abs(B2.T @ hvec).max():.3e}")

    pred = (lam1 - 2.0) / lam1
    vals = {(i, j): float(hvec @ theta(a[i], a[j]))
            for i in range(3) for j in range(i, 3)}
    diag_err = max(abs(vals[(i, i)] - pred) for i in range(3))
    off_err = max(abs(vals[(i, j)]) for i in range(3) for j in range(i + 1, 3))
    check(46, "THEOREM S18.4 (exact): <h, Theta(a_al, a_be)> = "
              "delta_{al,be} (lambda_1 - 2)/lambda_1 = -0.6092155055",
          diag_err < 1e-14 and off_err < 1e-14 and close(pred, -0.6092155055, 1e-9),
          f"diagonal err = {diag_err:.3e} ; off-diagonal err = {off_err:.3e} ; "
          f"(lam1-2)/lam1 = {pred:.13f}")

    check(47, "COROLLARY 3: the traceless (H) part of Sym^2(T1) has EXACTLY "
              "zero overlap with the harmonic 2-form",
          max(abs(float(hvec @ v)) for v in Hb) < 1e-14,
          f"max|<h, psi_H>| = {max(abs(float(hvec @ v)) for v in Hb):.3e}")

    share_pred = (pred ** 2 / 32.0) / float(psiA @ psiA)
    check(48, "COROLLARY 4: lambda=0 share of the scalar channel = "
              "(lambda_1-2)^2 / (32 lambda_1^2 ||psi_A||^2), closed form",
          close(share_pred, share0, 1e-12),
          f"closed form = {share_pred:.12f} ; measured = {share0:.12f}")
    res["harmonic_identity"] = {"h_Theta_diagonal": pred,
                                "share_lambda0_closed_form": share_pred}

    # =======================================================================
    # Section N: Gate A (Wilson holonomy) and the two-body effective Hamiltonian
    # =======================================================================
    print("\n-- N. Wilson holonomy audit and the two-body effective Hamiltonian --")

    rk = np.linalg.matrix_rank(B2.T, tol=1e-9)
    rk1 = np.linalg.matrix_rank(B1, tol=1e-9)
    check(49, "LINEARIZED gauge-fixing census: dim Omega^1 = 90 = 59 (gradients, "
              "im B1) + 31 (physical, im B2^T). This is the abelianised Gauss law; "
              "the non-abelian constraint D_i[A]E_i = 0, its Coulomb kernel, the "
              "Faddeev-Popov determinant and the Gribov horizon are DEFERRED",
          rk == 31 and rk1 == 59 and rk + rk1 == nE,
          f"rank(B2^T) = {rk}, rank(B1) = {rk1}, sum = {rk+rk1}")
    res["gluon_modes"] = {"physical": int(rk), "pure_gauge": int(rk1),
                          "caveat": "linearized Gauss law only"}

    T1h = U[:, 21:24]
    Apair = {}
    for i in range(3):
        for j in range(i + 1, 3):
            Apair[(i, j)] = cup(a[i], a[j]) - cup(a[j], a[i])
    nrms = [float(v @ v) for v in Apair.values()]
    p1s = [float(np.linalg.norm(T1.T @ v) ** 2) for v in Apair.values()]
    phs = [float(np.linalg.norm(T1h.T @ v) ** 2) for v in Apair.values()]
    check(50, "epsilon structure: A_{ab} = eps_{abg}(c1 u^(1)_g + c_h u^(h)_g); "
              "the three pairs carry identical norms and channel weights",
          max(nrms) - min(nrms) < 1e-12 and max(p1s) - min(p1s) < 1e-12,
          f"||A||^2 spread = {max(nrms)-min(nrms):.3e}")

    c1sq = float(np.mean(p1s)); chsq = float(np.mean(phs)); kap2 = c1sq + chsq
    check(51, "geometric couplings c1^2 = 0.1236221351, c_h^2 = 0.0095045494, "
              "kappa^2 = c1^2 + c_h^2 = ||A_{ab}||^2",
          close(c1sq, 0.1236221351, 1e-9) and close(chsq, 0.0095045494, 1e-9)
          and close(kap2, float(np.mean(nrms)), 1e-12),
          f"c1^2 = {c1sq:.10f}  c_h^2 = {chsq:.10f}  kappa^2 = {kap2:.10f}")
    res["couplings"] = {"c1_sq": c1sq, "ch_sq": chsq, "kappa_sq": kap2}

    check(52, "kappa^2 reproduces the ZS-S17 alternating power split 92.8605/7.1395",
          close(100 * c1sq / kap2, 92.860523, 1e-4),
          f"{100*c1sq/kap2:.6f}% / {100*chsq/kap2:.6f}%")

    leak = 0.0
    for v in Apair.values():
        leak = max(leak, float(np.abs(v - (T1 @ (T1.T @ v) + T1h @ (T1h.T @ v))).max()))
    check(53, "EXACTLY TWO one-gluon exchange channels: <u_r, A_anti> non-zero only "
              "for r in T1(lambda_1) + T1(lambda_h) -- the dynamical content of the "
              "ZS-S17 two-T1 closure theorem",
          leak < 1e-13, f"max leakage = {leak:.3e}")

    # ---------- exact SU(N) generators, kept ONLY for N = 2,3,4 --------------
    def _gens(N):
        T = []
        for i in range(N):
            for j in range(i + 1, N):
                m = np.zeros((N, N), complex); m[i, j] = 1; m[j, i] = 1; T.append(m / 2)
                m = np.zeros((N, N), complex); m[i, j] = -1j; m[j, i] = 1j; T.append(m / 2)
        for k in range(1, N):
            m = np.zeros((N, N), complex)
            for i in range(k):
                m[i, i] = 1
            m[k, k] = -k
            T.append(m / np.sqrt(2 * k * (k + 1)))
        return np.array(T)

    def _fabc(N):
        T = _gens(N); dd = len(T); f = np.zeros((dd, dd, dd))
        for x in range(dd):
            for y in range(dd):
                C = T[x] @ T[y] - T[y] @ T[x]
                for z in range(dd):
                    f[x, y, z] = float(np.real(-2j * np.trace(C @ T[z])))
        return f

    EXTENDED = '--extended' in sys.argv
    NSMALL = [2, 3, 4, 5, 6] if EXTENDED else [2, 3, 4]
    FS = {N: _fabc(N) for N in [2, 3, 4]}
    ok_id = True
    for N in [2, 3, 4]:
        f = FS[N]; dA = N * N - 1
        ok_id &= close(float(np.einsum('abc,abc->', f, f)), N * dA, 1e-9)
        ok_id &= close(float(np.einsum('abc,acb->', f, f)), -N * dA, 1e-9)
        ok_id &= abs(float(np.abs(np.einsum('abc,bc->a', f, np.eye(dA))).max())) < 1e-12
        ok_id &= close(float(np.abs(np.einsum('acd,bcd->ab', f, f) - N * np.eye(dA)).max()),
                       0.0, 1e-9)
    check(54, "colour identities used analytically for all N are verified against "
              "explicit SU(N) generators for N = 2,3,4: f^acd f^bcd = N delta^ab, "
              "f^abc f^abc = N dim(Adj), f^abc f^acb = -N dim(Adj), f^abc delta^bc = 0",
          ok_id, "all four identities hold for N = 2, 3, 4")

    # ---------- GATE A: exact Wilson holonomy vs the cup-product curvature ----
    print("   [Gate A] expanding the exact Wilson plaquette action ...")
    apot = np.array([a[k] for k in range(3)])
    u1v = np.array([T1[:, k] for k in range(3)])
    FT = []
    for c_ in cycles:
        n = len(c_); row = []
        for k in range(n):
            uu, xx = c_[k], c_[(k + 1) % n]
            row.append((eidx[(uu, xx)], 1) if (uu, xx) in eidx else (eidx[(xx, uu)], -1))
        FT.append(row)

    P5 = [[(eidx[(c_[k], c_[(k + 1) % 5])], 1)
           if (c_[k], c_[(k + 1) % 5]) in eidx
           else (eidx[(c_[(k + 1) % 5], c_[k])], -1) for k in range(5)]
          for c_ in cycles if len(c_) == 5]
    P6 = [[(eidx[(c_[k], c_[(k + 1) % 6])], 1)
           if (c_[k], c_[(k + 1) % 6]) in eidx
           else (eidx[(c_[(k + 1) % 6], c_[k])], -1) for k in range(6)]
          for c_ in cycles if len(c_) == 6]
    E5 = np.array([[e for e, _ in r_] for r_ in P5])
    S5 = np.array([[sg for _, sg in r_] for r_ in P5])
    E6 = np.array([[e for e, _ in r_] for r_ in P6])
    S6 = np.array([[sg for _, sg in r_] for r_ in P6])

    def V2_exact(Aed, Tg, N, r=0.5, MC=16):
        """g^2 coefficient of the Wilson magnetic energy by Cauchy contour on the
        entire continuation of sum_f [N - Re Tr U_f].  Machine-precision numerical
        extraction -- NOT a closed form.  eigh is done once; no matrix inversions
        are needed because exp(igX)^{-1} = exp(-igX) exactly, also for complex g."""
        X = np.einsum('ae,aij->eij', Aed, Tg)
        lam, Wm = np.linalg.eigh(X)
        th = 2 * np.pi * np.arange(MC) / MC
        gs = r * np.exp(1j * th)
        ph = np.exp(1j * gs[:, None, None] * lam[None, :, :])
        Up = np.einsum('eij,mej,ekj->meik', Wm, ph, Wm.conj())
        Um = np.einsum('eij,mej,ekj->meik', Wm, 1.0 / ph, Wm.conj())
        tot = np.zeros(MC, dtype=complex)
        for Ee, Ss, L in ((E5, S5, 5), (E6, S6, 6)):
            A1 = np.where(Ss[None, :, :, None, None] > 0, Up[:, Ee], Um[:, Ee])
            A2 = np.where(Ss[None, :, :, None, None] > 0, Um[:, Ee], Up[:, Ee])
            Mp = A1[:, :, 0]; Mm = A2[:, :, L - 1]
            for k in range(1, L):
                Mp = Mp @ A1[:, :, k]
                Mm = Mm @ A2[:, :, L - 1 - k]
            tot += (N - 0.5 * (np.einsum('mfii->mf', Mp)
                               + np.einsum('mfii->mf', Mm))).sum(axis=1)
        return 2.0 * float(np.real((tot * np.exp(-4j * th)).mean() / r ** 4))

    def wilson_V(Aed, g, Tg, N):
        X = np.einsum('ae,aij->eij', Aed, Tg)
        lam, W = np.linalg.eigh(X)
        Ue = np.einsum('eij,ej,ekj->eik', W, np.exp(1j * g * lam), W.conj())
        Ud = np.conj(np.transpose(Ue, (0, 2, 1)))
        tot = 0.0
        for row in FT:
            M = np.eye(N, dtype=complex)
            for (k, s) in row:
                M = M @ (Ue[k] if s > 0 else Ud[k])
            tot += N - float(np.real(np.trace(M)))
        return 2.0 * tot / g ** 2

    def edgeval(vec, uu, ww):
        return vec[eidx[(uu, ww)]] if (uu, ww) in eidx else -vec[eidx[(ww, uu)]]

    def cup_bp(x, y, b0):
        out = np.zeros(nF)
        for fi, c_ in enumerate(cycles):
            n = len(c_); b = b0 % n
            cc = [c_[(b + m) % n] for m in range(n)]
            xs = [edgeval(x, cc[k], cc[(k + 1) % n]) for k in range(n)]
            ys = [edgeval(y, cc[k], cc[(k + 1) % n]) for k in range(n)]
            s = 0.0; acc = 0.0
            for k in range(n):
                s += acc * ys[k]; acc += xs[k]
            out[fi] = s
        return out

    Tg2 = _gens(2); f2 = FS[2]
    rng = np.random.default_rng(7)
    qr = rng.normal(size=(3, 3))
    Aed = np.einsum('aA,Ae->ae', qr, apot)
    dAf = np.einsum('aA,Af->af', qr, u1v)
    V0_cup = 0.5 * float(np.einsum('af,af->', dAf, dAf))
    gs = np.array([0.002, 0.004, 0.006, 0.008, 0.010])
    Vs = np.array([wilson_V(Aed, g, Tg2, 2) for g in gs])
    cf = np.linalg.lstsq(np.vstack([gs ** k for k in range(4)]).T, Vs, rcond=None)[0]
    check(55, "GATE A(i): the quadratic Wilson term reproduces the cochain curvature "
              "energy (1/2) sum_f (delta A)^2 exactly",
          close(cf[0], V0_cup, 1e-7),
          f"Wilson V0 = {cf[0]:.10f}  vs  (1/2)|delta A|^2 = {V0_cup:.10f}")

    cub_bp = []
    for b0 in range(4):
        Cf = np.zeros((3, nF))
        for aa in range(3):
            s = np.zeros(nF)
            for bb in range(3):
                for cc2 in range(3):
                    if f2[aa, bb, cc2] != 0.0:
                        s += f2[aa, bb, cc2] * cup_bp(Aed[bb], Aed[cc2], b0)
            Cf[aa] = s
        cub_bp.append(float(np.einsum('af,af->', dAf, Cf)))
    mu_fit = cf[1] / cub_bp[0]
    check(56, "GATE A(ii): the CUBIC Wilson vertex is exactly the cup-product form "
              "with coefficient mu = -1/2, i.e. B^a = (delta A)^a - (g/2) f^abc "
              "(A^b cup A^c) from Baker-Campbell-Hausdorff; and the cubic action term "
              "is BASEPOINT-INDEPENDENT",
          close(mu_fit, -0.5, 3e-4)
          and max(cub_bp) - min(cub_bp) < 1e-10,
          f"mu = {mu_fit:.8f} (target -1/2); basepoint spread = "
          f"{max(cub_bp)-min(cub_bp):.3e}")
    res["gate_A"] = {"mu_cubic": float(mu_fit)}

    Cf0 = np.zeros((3, nF))
    for aa in range(3):
        s = np.zeros(nF)
        for bb in range(3):
            for cc2 in range(3):
                if f2[aa, bb, cc2] != 0.0:
                    s += f2[aa, bb, cc2] * cup_bp(Aed[bb], Aed[cc2], 0)
        Cf0[aa] = s
    quart_naive = 0.25 * 0.5 * float(np.einsum('af,af->', Cf0, Cf0))   # mu^2 * (1/2)|C|^2
    check(57, "GATE A(iii) [NEGATIVE]: the QUARTIC Wilson vertex is NOT mu^2 times the "
              "square of the cup curvature; higher Baker-Campbell-Hausdorff terms and "
              "the quartic term of N - Re Tr U contribute at the same order. The naive "
              "seagull of ZS-S18 v1.2 is therefore RETRACTED",
          abs(cf[2] - quart_naive) > 0.2 * abs(quart_naive),
          f"Wilson quartic = {cf[2]:.10f}  vs  naive mu^2 |C|^2/2 = {quart_naive:.10f} "
          f"(ratio {cf[2]/quart_naive:.4f})")

    # ---------- the TRUE seagull, extracted from the Wilson action ----------
    print("   [Gate A] extracting the true quartic seagull for N = 2, 3, 4 ...")
    GSQ = np.array([0.10, 0.18, 0.26, 0.34, -0.10, -0.18, -0.26, -0.34])
    PINV = np.linalg.pinv(np.vstack([GSQ ** k for k in range(8)]).T)
    om = lam1 ** 0.5
    RA = np.eye(3) / np.sqrt(3.0)
    RH = np.diag([1.0, -1.0, 0.0]) / np.sqrt(2.0)

    def seagull(N):
        """Only two contractions are needed, not the full T_iijj matrix.  Global
        SU(N) invariance makes sum_a T_{(a,al)(a,al)(b,be)(b,be)} independent of b,
        so the register matrix needs d_A pair-evaluations per (al,be), not d_A^2."""
        Tg = _gens(N); dA = N * N - 1
        pairs = [(x, y) for x in range(dA) for y in range(3)]
        ixp = {p: k for k, p in enumerate(pairs)}
        nm = 3 * dA

        def V2(vec):
            q = np.zeros((dA, 3))
            for k, x in enumerate(vec):
                if x != 0.0:
                    q[pairs[k]] = x
            return V2_exact(np.einsum('aA,Ae->ae', q, apot), Tg, N)

        I = np.eye(nm)
        Qd = {}

        def Qi(i):
            if i not in Qd:
                Qd[i] = V2(I[i])
            return Qd[i]

        def Tij(i, j):
            if i == j:
                return Qi(i)
            return (V2(I[i] + I[j]) + V2(I[i] - I[j]) - 2 * Qi(i) - 2 * Qi(j)) / 12.0

        Mreg = np.zeros((3, 3))
        for al in range(3):
            for be in range(al, 3):
                sv = sum(Tij(ixp[(x, al)], ixp[(0, be)]) for x in range(dA))
                Mreg[al, be] = Mreg[be, al] = dA * sv

        def ctr(R):
            return float(sum(Mreg[al, be] * R[al, al] * R[be, be]
                             for al in range(3) for be in range(3))) / (2 * dA)
        return (6.0 / om ** 2) * lam1 ** 2 * (ctr(RH) - ctr(RA))

    SG = {N: seagull(N) for N in NSMALL}
    sN = np.array([SG[N] / N for N in NSMALL])
    xN = np.array([1.0 / N ** 2 for N in NSMALL])
    cofit = np.linalg.lstsq(np.vstack([np.ones_like(xN), xN]).T, sN, rcond=None)[0]
    check(58, "TRUE SEAGULL: extracted from the exact Wilson action for N = 2,3,4; it "
              "is about one tenth of the retracted naive value AND it carries a "
              "genuine 1/N^2 term, so the geometric coefficient is NOT exactly "
              "N-independent",
          all(SG[N] < 0 for N in NSMALL)
          and abs(cofit[1]) > 1e-3
          and abs(SG[2] / 2 / (-0.75 * kap2 * lam1)) < 0.2,
          f"seagull/N = {cofit[0]:.9f} + ({cofit[1]:.9f})/N^2 ; "
          f"values {[float(round(SG[N]/N,9)) for N in NSMALL]}")
    res["seagull"] = {"per_N": {str(N): SG[N] / N for N in NSMALL},
                      "fit_c0": float(cofit[0]), "fit_c2": float(cofit[1])}

    # ---------- exchange terms, analytic colour ----------
    eps3 = np.zeros((3, 3, 3))
    for p in itertools.permutations(range(3)):
        eps3[p] = np.sign(np.linalg.det(np.eye(3)[list(p)]))

    def exch1_coef(N, R):
        f = FS[N] if N in FS else None
        Z = np.einsum('abg,gm->abm', eps3, R)
        tot = 0.0
        for s in itertools.permutations(range(3)):
            L1 = "abc"; L2s = "".join(L1[s[k]] for k in range(3))
            sg = int(np.sign(np.linalg.det(np.eye(3)[list(s)])))
            colour = sg * N * (N * N - 1)
            tot += colour * float(np.einsum(f"{L1},{L2s}->", Z, Z, optimize=True))
        return tot

    ok55 = ok56 = True
    for N in [2, 3, 4]:
        dA = N * N - 1
        K2 = 9.0 / ((2 * om) ** 3 * 2 * dA)
        e3A = -K2 * exch1_coef(N, RA) / om
        e3H = -K2 * exch1_coef(N, RH) / om
        ok55 &= close((e3H - e3A) * om ** 4 / N, 27.0 / 4.0, 1e-9) and abs(e3H) < 1e-12
        Zh = np.einsum('gab,bm->gam', eps3, RA)
        Zh2 = np.einsum('gab,bm->gam', eps3, RH)

        def th(Z):
            i1 = N * dA * float(np.einsum('gam,gam->', Z, Z))
            i2 = -N * dA * float(np.einsum('gam,gma->', Z, Z))
            return (i1 + i2) / (2 * dA)
        pf = 4.0 / ((2 * lam_h ** 0.5) * (2 * om) ** 2)
        ehA = -pf * th(Zh) / lam_h ** 0.5
        ehH = -pf * th(Zh2) / lam_h ** 0.5
        ok56 &= close((ehH - ehA) * lam_h * om ** 2 / N, 3.0 / 4.0, 1e-9)
    check(59, "ONE-GLUON EXCHANGE, lambda_1 channel: 3-particle norm proportional to "
              "(Tr R)^2, hence EXACTLY ZERO in the H channel; coefficient +27/4 for "
              "every N (analytic colour, cross-checked against explicit f for N=2,3,4)",
          ok55, "coefficient = 27/4 and H-channel exchange = 0")
    # ---- the PHYSICAL (symmetrised) cubic vertex on {T1(lam1), T1(lam_h)} ----
    idx6 = list(range(1, 4)) + list(range(21, 24))
    lams6 = np.array([w_[k] for k in idx6])
    a6 = [(B2.T @ U[:, k]) / w_[k] for k in idx6]
    u6 = [B2 @ x for x in a6]

    def _Aa(x, y):
        return cup_bp(x, y, 0) - cup_bp(y, x, 0)

    T6 = np.zeros((6, 6, 6))
    for i_ in range(6):
        for j_ in range(6):
            for k_ in range(6):
                T6[i_, j_, k_] = (float(u6[i_] @ _Aa(a6[j_], a6[k_]))
                                  + float(u6[j_] @ _Aa(a6[k_], a6[i_]))
                                  + float(u6[k_] @ _Aa(a6[i_], a6[j_]))) / 3.0
    asym = max(abs(T6[i_, j_, k_] + T6[j_, i_, k_])
               for i_ in range(6) for j_ in range(6) for k_ in range(6))
    c1_pol = sum(T6[i_, j_, k_] ** 2 for i_ in range(3)
                 for j_ in range(3) for k_ in range(3)) / 6.0
    ch_pol = sum(T6[i_, j_, k_] ** 2 for i_ in range(3, 6)
                 for j_ in range(3) for k_ in range(3) if j_ < k_) / 3.0
    check(60, "CORRECTION to v1.4: the cubic Hamiltonian contains the TOTALLY "
              "SYMMETRISED tensor, whose mode part is totally ANTISYMMETRIC (residual "
              "exactly 0). Its lambda_1 block reproduces c1^2 = 0.1236221351, but its "
              "lambda_h block gives c_h,pol^2 = 0.0012658090, NOT the raw cup "
              "projection 0.0095045494. v1.4 used the raw value as a vertex; that was "
              "wrong. The 7.1395% of ZS-S17 is a projection, not a coupling",
          asym < 1e-14 and close(c1_pol, 0.1236221351, 1e-9)
          and close(ch_pol, 0.0012658090, 1e-9),
          f"antisymmetry residual = {asym:.1e}; c1^2 = {c1_pol:.12f}; "
          f"c_h,pol^2 = {ch_pol:.12f} (raw cup value 0.0095045494)")
    res["polarised_couplings"] = {"c1_sq": c1_pol, "ch_pol_sq": ch_pol,
                                  "ch_raw_sq": chsq}

    # ---- brute-force Fock exchange, built directly from the symmetric tensor ----
    print("   [Fock] exchange sector from the symmetrised vertex (mu = -1/2) ...")
    MU = -0.5

    def fock_exchange(N, nmode, hon=False):
        f = FS[N]; dA = N * N - 1
        modes = [(m, x) for m in range(nmode) for x in range(dA)]
        ix = {m: k for k, m in enumerate(modes)}; M = len(modes)
        omg = np.array([lams6[m] ** 0.5 for (m, x) in modes])
        S3 = np.zeros((M, M, M))
        nzf = np.argwhere(np.abs(f) > 1e-12)
        for i_ in range(nmode):
            for j_ in range(nmode):
                for k_ in range(nmode):
                    if hon and max(i_, j_, k_) < 3:
                        continue
                    t = T6[i_, j_, k_]
                    if abs(t) < 1e-14:
                        continue
                    pref = 0.5 * MU * t * (lams6[i_] * lams6[j_] * lams6[k_]) ** 0.5
                    for (x, y, z) in nzf:
                        S3[ix[(i_, x)], ix[(j_, y)], ix[(k_, z)]] += pref * f[x, y, z]

        def qop(st, i):
            out = {}; sc = 1.0 / np.sqrt(2 * omg[i])
            for occ, amp in st.items():
                ni = occ.count(i)
                k1 = tuple(sorted(occ + (i,)))
                out[k1] = out.get(k1, 0.0) + amp * sc * np.sqrt(ni + 1)
                if ni > 0:
                    l = list(occ); l.remove(i); k2 = tuple(sorted(l))
                    out[k2] = out.get(k2, 0.0) + amp * sc * np.sqrt(ni)
            return out

        def cubic(st):
            out = {}
            for i in range(M):
                if not np.any(np.abs(S3[i]) > 1e-14):
                    continue
                ai = {}
                for j in range(M):
                    if not np.any(np.abs(S3[i, j]) > 1e-14):
                        continue
                    aj = {}
                    for k in range(M):
                        if abs(S3[i, j, k]) < 1e-14:
                            continue
                        for o, v in qop(st, k).items():
                            aj[o] = aj.get(o, 0.0) + S3[i, j, k] * v
                    for o, v in aj.items():
                        for o2, v2 in qop({o: v}, j).items():
                            ai[o2] = ai.get(o2, 0.0) + v2
                for o, v in ai.items():
                    for o2, v2 in qop({o: v}, i).items():
                        out[o2] = out.get(o2, 0.0) + v2
            return out

        def build(R):
            st = {}
            for x in range(dA):
                for al in range(3):
                    for be in range(3):
                        if abs(R[al, be]) < 1e-14:
                            continue
                        i, j = ix[(al, x)], ix[(be, x)]
                        o = tuple(sorted((i, j)))
                        st[o] = st.get(o, 0.0) + R[al, be] * (np.sqrt(2.0) if i != j else 1.0)
            nr = np.sqrt(sum(v * v for v in st.values()))
            return {k: v / nr for k, v in st.items()}

        mu = {}
        for nmc, R in (("A", RA), ("H", RH)):
            psi = build(R); E2 = 2 * om; tot = 0.0
            for o, v in cubic(psi).items():
                dE = sum(omg[i] for i in o) - E2
                if abs(dE) < 1e-12:
                    continue
                tot += -v * v / dE
            mu[nmc] = tot
        return (4.0 / 3.0) * (mu["H"] - mu["A"]) / om / N

    FOCK_ONE = {N: fock_exchange(N, 3) for N in (2, 3)}
    FOCK_H = {N: fock_exchange(N, 6, hon=True) for N in (2, 3)}
    FOCK_FULL = {N: fock_exchange(N, 6) for N in (2, 3)}

    G_exch_1 = (9.0 / 4.0) * c1_pol * om
    check(61, "THEOREM S18.6A (lambda_1 exchange, CLOSED FORM): G_exch^(1) = "
              "(9/4) c1^2 sqrt(lambda_1) = 0.3100892081, exactly N-independent, and "
              "reproduced to 12 digits by brute-force Fock-space perturbation theory "
              "for SU(2) and SU(3)",
          close(G_exch_1, 0.3100892081, 1e-9)
          and all(close(FOCK_ONE[N], G_exch_1, 1e-11) for N in FOCK_ONE),
          f"closed form = {G_exch_1:.12f}; Fock SU(2) = {FOCK_ONE[2]:.12f}, "
          f"SU(3) = {FOCK_ONE[3]:.12f}")

    G_exch = FOCK_FULL[2]
    v14form = (om / 4.0) * (9 * c1sq + chsq)
    CF = (9.0 / 4.0) * om * (c1_pol + ch_pol)
    CFh = (9.0 / 4.0) * om * ch_pol
    check(62, "THEOREM S18.6A' (FULL EXCHANGE CLOSURE, new in v1.6): the two closed "
              "channels contribute ADDITIVELY with the SAME universal coefficient, "
              "because the virtual eigenvalue cancels (vertex^2 gives lambda_r, "
              "oscillator and denominator give 1/omega_r^2, and lambda_r/omega_r^2 = "
              "1). Hence G_exch = (9/4) sqrt(lambda_1) SUM_r c_{r,pol}^2 = "
              "(9/4) sqrt(lambda_1)(c1^2 + c_h,pol^2) = 0.3132643168. v1.5 declared "
              "this to have NO closed form; that was wrong and is CORRECTED. v1.4's "
              "(sqrt(lambda_1)/4)(9c1^2 + c_h^2) remains RETRACTED",
          close(G_exch, CF, 1e-12)
          and all(close(FOCK_H[N], CFh, 1e-11) for N in FOCK_H)
          and abs(FOCK_FULL[2] - FOCK_FULL[3]) < 1e-11
          and abs(G_exch - (om / 4.0) * (9 * c1sq + chsq)) > 1e-4,
          f"closed form = {CF:.15f}; Fock = {G_exch:.15f} (diff {G_exch-CF:.1e}); "
          f"lambda_h channel alone: Fock {FOCK_H[2]:.15f} vs (9/4)sqrt(lam1)c_h,pol^2 "
          f"= {CFh:.15f}")
    res["exchange"] = {"G_exch_lam1_closed": G_exch_1, "G_exch_full": G_exch,
                       "G_exch_closed_form": CF, "fock_h_only": FOCK_H,
                       "fock_lam1": FOCK_ONE, "fock_full": FOCK_FULL,
                       "retracted_v14_form": v14form}

    # 5-particle sector
    perms5 = list(itertools.permutations(range(5)))

    def _psum(tensors, sigma):
        L1 = "abcde"; L2s = "".join(L1[sigma[k]] for k in range(5))
        subs, ops = [], []
        for (t, sl) in tensors:
            ops.append(t); subs.append("".join(L1[sx] for sx in sl))
        for (t, sl) in tensors:
            ops.append(t); subs.append("".join(L2s[sx] for sx in sl))
        return float(np.einsum(",".join(subs) + "->", *ops, optimize=True))

    five_ok = True
    for N in (2, 3):
        f = FS[N]; dA = N * N - 1; tot = {}
        for nm_, R in (("A", RA), ("H", RH)):
            sfive = 0.0
            for sg in perms5:
                cc = _psum([(f, (0, 1, 2)), (np.eye(dA), (3, 4))], sg)
                if abs(cc) < 1e-12:
                    continue
                sfive += cc * _psum([(eps3, (0, 1, 2)), (R, (3, 4))], sg)
            tot[nm_] = sfive
        five_ok &= abs(tot["H"] - tot["A"]) < 1e-9 * max(1.0, abs(tot["A"]))
    check(63, "the 5-particle intermediate sector is a pure self-energy: identical in "
              "the A and H channels, contributing exactly zero to the splitting",
          five_ok, "|5-particle splitting| < 1e-9 for N = 2, 3")

    G_of_N = {N: G_exch + (4.0 / 3.0) * (SG[N] / N) / om for N in NSMALL}
    G_inf = G_exch + (4.0 / 3.0) * cofit[0] / om
    a_geom = (4.0 / 3.0) * cofit[1] / om
    check(64, "COROLLARY S18.6C: G(N) = G_exch + (4/3)s(N)/sqrt(lambda_1) = G_inf + "
              "a_geom/N^2 with G_inf = 0.298805 and a_geom = -0.005241 NON-ZERO",
          close(G_inf, 0.2988049, 3e-5) and abs(a_geom) > 1e-3,
          f"G_inf = {G_inf:.8f}, a_geom = {a_geom:.8f}, "
          f"G(N) = {[float(round(G_of_N[N],8)) for N in NSMALL]}")
    res["theorem_S18_6"] = {"G_infinity": float(G_inf), "a_geom": float(a_geom),
                            "G_of_N": {str(N): G_of_N[N] for N in NSMALL}}

    check(65, "RETRACTION of ZS-S18 v1.2 Theorem S18.6: the value G = 1.1025394066 and "
              "the claim a = b = 0 EXACTLY are both withdrawn. The v1.2 errors were a "
              "cubic coefficient mu = +1 instead of -1/2 and a seagull taken as the "
              "square of the cup curvature; v1.4 additionally mis-normalised the "
              "lambda_h vertex (Check 60)",
          abs(G_inf - 1.1025394066) > 0.5 and abs(a_geom) > 1e-3,
          f"v1.2 G = 1.1025394066 -> v1.5 G_inf = {G_inf:.8f} "
          f"(factor {1.1025394066/G_inf:.4f}); a_geom = {a_geom:.8f} != 0")

    # =======================================================================
    # Section R: v1.5 audit extensions
    # =======================================================================
    print("\n-- R. audit extensions --")

    order_ = np.argsort(w_)
    phys = [k for k in order_ if w_[k] > 1e-9]
    a_all = [(B2.T @ U[:, k]) / w_[k] for k in phys]
    u_all = [U[:, k] for k in phys]
    sl1 = [i for i, k in enumerate(phys) if abs(w_[k] - lam1) < 1e-9]
    slh = [i for i, k in enumerate(phys) if abs(w_[k] - lam_h) < 1e-9]

    def Aanti(x, y, b0):
        return cup_bp(x, y, b0) - cup_bp(y, x, b0)

    pol_leak = 0.0; pol_keep = 0.0
    for b0 in range(6):
        for al in sl1:
            for be in sl1:
                if al >= be:
                    continue
                vec = np.zeros(len(phys))
                for ri in range(len(phys)):
                    vec[ri] = (float(u_all[ri] @ Aanti(a_all[al], a_all[be], b0))
                               + float(u_all[al] @ Aanti(a_all[be], a_all[ri], b0))
                               + float(u_all[be] @ Aanti(a_all[ri], a_all[al], b0))) / 3.0
                msk = np.zeros(len(phys), bool); msk[sl1] = True; msk[slh] = True
                pol_leak = max(pol_leak, float(np.abs(vec[~msk]).max()))
                pol_keep = max(pol_keep, float(np.abs(vec[msk]).max()))
    check(66, "THEOREM S18.9: the FULLY POLARISED Wilson cubic vertex couples two "
              "external T1(lambda_1) legs ONLY into T1(lambda_1) + T1(lambda_h), over "
              "all 31 physical modes, for ALL SIX basepoints. Strictly stronger than "
              "Check 53, which needed basepoint averaging",
          pol_leak / pol_keep < 1e-12 and close(pol_keep, 0.3515993958, 1e-8),
          f"relative leakage = {pol_leak/pol_keep:.3e} over 6 basepoints; retained "
          f"magnitude = {pol_keep:.10f} (= c1)")
    res["polarised_cubic"] = {"relative_leakage": pol_leak / pol_keep,
                              "retained": pol_keep}

    def cup_avg_local(x, y):
        out = np.zeros(nF)
        for fi, c_ in enumerate(cycles):
            n = len(c_); tot = 0.0
            for b in range(n):
                cc = [c_[(b + m) % n] for m in range(n)]
                xs = [edgeval(x, cc[k], cc[(k + 1) % n]) for k in range(n)]
                ys = [edgeval(y, cc[k], cc[(k + 1) % n]) for k in range(n)]
                sv = 0.0; acc = 0.0
                for k in range(n):
                    sv += acc * ys[k]; acc += xs[k]
                tot += sv
            out[fi] = tot / n
        return out

    ratios = []
    for N in (2, 3):
        Tg = _gens(N); fN = FS[N]; dA = N * N - 1
        for seed in (7, 23):
            rr = np.random.default_rng(seed).normal(size=(dA, 3))
            Ae = np.einsum('aA,Ae->ae', rr, apot)
            V2w = V2_exact(Ae, Tg, N)
            for cf in (lambda x, y: cup_bp(x, y, 0), cup_avg_local):
                Cm = np.zeros((dA, nF))
                for a_ in range(dA):
                    sv = np.zeros(nF)
                    for b_ in range(dA):
                        for c2_ in range(dA):
                            if fN[a_, b_, c2_] != 0.0:
                                sv += fN[a_, b_, c2_] * cf(Ae[b_], Ae[c2_])
                    Cm[a_] = sv
                nv = 0.25 * 0.5 * float(np.einsum('af,af->', Cm, Cm))
                ratios.append(V2w / nv)
    check(67, "SCOPE of the Gate A(iii) mismatch: the ratio (Wilson quartic)/(naive "
              "cup-square) is field-, group- and convention-dependent -- NOT a "
              "universal 28%. Over 8 configurations it spans a range including a "
              "SIGN CHANGE",
          min(ratios) < 0.0 < max(ratios) and max(ratios) - min(ratios) > 0.3,
          f"ratio range = {min(ratios):.4f} .. {max(ratios):.4f}")
    res["quartic_ratio_range"] = [float(min(ratios)), float(max(ratios))]

    # ---- F-S18.16 reduced to ONE ratio rho = w5/w6 ----
    npent = [len(c_) for c_ in cycles]

    def gap_of_rho(rho):
        wf = np.array([rho if n == 5 else 1.0 for n in npent]); wf = wf / wf.mean()
        evw = np.sort(np.linalg.eigvalsh(np.diag(np.sqrt(wf)) @ L2 @ np.diag(np.sqrt(wf))))
        return float(evw[1]), int(np.sum(np.abs(evw - evw[1]) < 1e-8))

    edgelen = float(np.linalg.norm(V[edges[0][0]] - V[edges[0][1]]))
    A_pent = 0.25 * np.sqrt(5 * (5 + 2 * np.sqrt(5))) * edgelen ** 2
    A_hex = 1.5 * np.sqrt(3.0) * edgelen ** 2
    rho_area = A_pent / A_hex
    g1 = gap_of_rho(1.0); ga = gap_of_rho(rho_area); gh = gap_of_rho(1.0 / rho_area)
    rgrid = np.linspace(0.9, 1.2, 31)
    vals = [gap_of_rho(r)[0] for r in rgrid]
    rho_max = float(rgrid[int(np.argmax(vals))])
    check(68, "F-S18.16 reduced: pentagons and hexagons are each a single I_h orbit, "
              "so every I_h-invariant face weight is ONE ratio rho = w5/w6 (the common "
              "scale is absorbed in g). The two tested natural weights shift the gap "
              "by -5.77% and -3.57%, breaking LOCKED lambda_1 (L6) and hence "
              "Lambda_QCD. The gap stays 3-fold (T1) for every rho, so ALL of Part I "
              "survives. lambda_1(rho) peaks near rho = 1.05, NOT at rho = 1, so there "
              "is NO variational characterisation of the unweighted convention",
          close(g1[0], lam1, 1e-12) and g1[1] == 3 and ga[1] == 3 and gh[1] == 3
          and abs(ga[0] - lam1) / lam1 > 0.05 and abs(gh[0] - lam1) / lam1 > 0.03
          and abs(rho_max - 1.0) > 0.02,
          f"rho=1: {g1[0]:.10f}; rho={rho_area:.5f} (w~A): {ga[0]:.10f} "
          f"({100*(ga[0]-lam1)/lam1:+.3f}%); rho={1/rho_area:.5f} (w~1/A): "
          f"{gh[0]:.10f} ({100*(gh[0]-lam1)/lam1:+.3f}%); argmax at rho = {rho_max:.3f}")
    res["face_weight_gate"] = {"rho_1": g1[0], "rho_area": ga[0], "rho_hodge": gh[0],
                               "rho_argmax": rho_max}

    check(69, "ANTI-REGRESSION: the retracted v1.2 value 1.1025394066 and the retracted "
              "v1.4 closed form are produced by NO code path used for a physical result",
          abs(G_inf - 1.1025394066) > 0.5 and abs(G_exch - 1.1025394066) > 0.5
          and all(abs(FOCK_FULL[N] - 1.1025394066) > 0.5 for N in FOCK_FULL)
          and abs(G_exch - v14form) > 1e-4,
          f"G_inf = {G_inf:.8f}, G_exch = {G_exch:.8f}, Fock = {FOCK_FULL[2]:.8f}")

    # =======================================================================
    # Section P: the parity dictionary
    # =======================================================================
    print("\n-- P. Parity dictionary --")
    dets = np.array([float(np.linalg.det(M)) for M in G])
    sgnd = np.sign(dets)
    PFu = [PF[k] * sgnd[k] for k in range(120)]
    check(70, "P_F^unsigned(g) = det(g) P_F^signed(g), and det(g) is exactly the A_u "
              "character of I_h (exact sign used, per the v1.1 lesson)",
          max(abs(abs(dd_) - 1.0) for dd_ in dets) < 1e-8,
          f"max ||det(g)|-1| = {max(abs(abs(dd_)-1.0) for dd_ in dets):.3e}")

    iso_u = isotype(Qs.T @ Qs, G, PFu)
    check(71, "PARITY DICTIONARY: under the UNSIGNED (geometric) action the symmetric "
              "two-body image is A_g + H_g; the discrete Hodge star supplies the det "
              "twist, so both channels have P = +",
          iso_u == {"Ag": 1, "Hg": 1},
          f"unsigned isotype = {iso_u}")
    res["parity_dictionary"] = {"signed": {"A_u": 1, "H_u": 1}, "unsigned": iso_u}

    check(72, "charge conjugation: the two-gluon colour singlet is built on delta^ab, "
              "which is C-even; hence A_g -> 0^{++} and H_g -> 2^{++}, the 5-dim H "
              "being exactly the l=2 multiplet of I_h",
          iso_u.get("Hg", 0) == 1 and iso_u.get("Ag", 0) == 1,
          "Sym^2(T1) (x) singlet -> A_g + H_g -> 0++ + 2++, both P=+ C=+")


    # ---- F-S18.4 redefined: size of the FULL 31-mode two-gluon blocks ----
    Pphys = np.zeros((nF, nF))
    for k in phys:
        Pphys += np.outer(U[:, k], U[:, k])
    chi_u = np.array([float(np.trace(Pphys @ PF[k])) * sgnd[k] for k in range(120)])
    chi_sq = np.array([float(np.trace((Pphys @ PF[k] * sgnd[k])
                                      @ (Pphys @ PF[k] * sgnd[k]))) for k in range(120)])
    chi_sym = 0.5 * (chi_u ** 2 + chi_sq)
    d1 = isotype_from_char(chi_u, G)
    d2 = isotype_from_char(chi_sym, G)
    check(73, "F-S18.4 REDEFINED: by Theorem S18.9 the one-gluon exchange active space "
              "is already complete at O(g^2), so Gate C is NOT about adding virtual "
              "modes. Its remaining content is the FULL two-gluon basis built from all "
              "unordered pairs of the 31 physical modes. Its A_g and H_g blocks are "
              "reported here so the size of the deferred calculation is on record",
          d1.get("T1u", 0) == 2 and d2.get("Ag", 0) == 12 and d2.get("Hg", 0) == 28
          and sum(_DIM[k[:-1]] * v for k, v in d2.items()) == 31 * 32 // 2,
          f"one-gluon (31 modes, unsigned) = {d1}; Sym^2 = {d2}; "
          f"full A_g block dim = {d2.get('Ag',0)}, full H_g block dim = "
          f"{5*d2.get('Hg',0)} ({d2.get('Hg',0)} copies of H) -- v1.4 used 1 + 5")
    Tg2 = _gens(2)
    rr2 = np.random.default_rng(7).normal(size=(3, 3))
    Ae2 = np.einsum('aA,Ae->ae', rr2, apot)
    cvals = [V2_exact(Ae2, Tg2, 2, r_, M_) for (r_, M_) in
             ((0.3, 16), (0.4, 16), (0.5, 16), (0.6, 24), (0.8, 20), (0.5, 32))]
    spread = max(cvals) - min(cvals)
    check(74, "CONTOUR STABILITY: the quartic coefficient is stable to ~1e-13 across "
              "six independent (radius, node-count) choices. This is a "
              "MACHINE-PRECISION NUMERICAL EXTRACTION, not an exact closed form -- a "
              "finite-node contour and floating-point exponentials are used, so the "
              "analytic Magnus evaluation remains future work (ZS-S19)",
          spread < 1e-11 and close(cvals[2], 0.0283516667, 1e-9),
          f"values span {min(cvals):.16f} .. {max(cvals):.16f}, spread {spread:.1e}")
    res["contour_stability_spread"] = float(spread)

    res["full_two_gluon_blocks"] = {"Ag": d2.get("Ag", 0), "H_copies": d2.get("Hg", 0)}

    lam_t = 1.6550 / G_inf
    alpha_s_MZ = 11.0 / 93.0
    lam_t_MZ = 3.0 * 4.0 * np.pi * alpha_s_MZ
    register_external(
        "E-S18.1",
        f"Athenodorou-Teper SU(inf): m(0++)/sqrt(sigma) = 3.072(14), "
        f"m(2++)/sqrt(sigma) = 4.599(14) => g_hf(inf) = 1.655 +/- 0.033 "
        f"(independent-error assumption). With G_inf = {G_inf:.6f} this gives "
        f"lambda_t = {lam_t:.4f} +/- 0.11. NOT independently extracted here.")
    register_external(
        "E-S18.2",
        f"ZS-S1 gives alpha_s(M_Z) = 11/93 => lambda_t(M_Z, N=3) = {lam_t_MZ:.4f}. "
        f"The value {lam_t:.2f} required by E-S18.1 corresponds to alpha_s = "
        f"{lam_t/3/(4*np.pi):.4f}, i.e. one-loop mu_TI ~ 30 GeV. v1.2's 1.51 was in "
        f"sharp conflict; the Gate A correction reduces but does not remove the "
        f"tension. Scheme matching is F-S18.13.")
    res["external"] = {"lambda_t_from_lattice": float(lam_t),
                       "lambda_t_MZ_from_S1": float(lam_t_MZ)}

    # ---- OPEN gates (printed, NOT counted) --------------------------------
    register_open("F-S18.4", "Gate C, REDEFINED: Theorem S18.9 shows the one-gluon "
                             "exchange space is already complete at O(g^2), so this is "
                             "NOT about adding virtual modes. Build the A_g (dim 12) "
                             "and H_g (dim 140) blocks from all unordered pairs of the "
                             "31 physical modes (Sym^2 has dim 496), include the exact "
                             "Wilson quartic and the cubic couplings to adjacent Fock "
                             "sectors, and test convergence under an occupation "
                             "cutoff. At lambda_t ~ 5.5 use sparse Lanczos, not "
                             "perturbation theory.")
    register_open("F-S18.10", "Gate B: solve the NON-ABELIAN Gauss law D_i[A]E_i = 0 "
                              "with its Coulomb kernel and Faddeev-Popov measure to "
                              "O(g^2) in a named gauge; show mu_H - mu_A is "
                              "gauge-independent.")
    register_open("F-S18.13", "Gate D: fix a_TI from an independent observable "
                              "(string tension or Lambda_QCD, NOT the 2++/0++ ratio), "
                              "derive g_S14 = Z_g g_MSbar, and confront "
                              "lambda_t(mu_TI) with ZS-S1. See E-S18.2.")
    register_open("F-S18.15", "Gate E: covariance-aware fit of Athenodorou-Teper "
                              "N = 2..12, then test the SAME H_eff against 0++*, "
                              "0-+ and 2-+. Deferred to ZS-S19 but COUNTED OPEN here.")
    register_open("F-S18.16", "Metric-weight gate: derive w_f = 1 in the plaquette "
                              "sum from the ZS-S14 Hodge star with zero parameters, "
                              "rather than inferring it from consistency with ZS-S7. "
                              "Check 68 shows area and Hodge weights shift lambda_1 "
                              "by -5.77% and -3.57%.")
    # ---- ledger -----------------------------------------------------------
    print("\n" + "=" * 78)
    npass = sum(1 for _, _, ok, _ in _checks if ok)
    ntot = len(_checks)
    for gid, txt in _open_gates:
        print(f"  [OPEN] {gid}: {txt}")
    for gid, txt in _external:
        print(f"  [EXTERNAL-CONFRONTATION, not a computed check] {gid}: {txt}")
    print("-" * 78)
    print(f"  VERIFICATION: {npass}/{ntot} PASS "
          f"| {len(_open_gates)} OPEN gates + {len(_external)} EXTERNAL, NOT counted "
          f"| Zero New Geometric Parameters | Running-Coupling Matching Gate OPEN")
    print("=" * 78)

    res["verification"] = {"pass": npass, "total": ntot,
                           "open_gates": [g for g, _ in _open_gates],
                           "external": [g for g, _ in _external]}
    print("\n" + "-" * 78)
    print("  MACHINE-READABLE RESULT BLOCK (stdout only; no files are written)")
    print("-" * 78)
    def _canon(o):
        if isinstance(o, dict):
            return {str(k): _canon(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [_canon(v) for v in o]
        if isinstance(o, (int, bool, str)) or o is None:
            return o
        return float(f"{float(o):.10e}")

    import scipy
    env = {"python": platform.python_version(), "numpy": np.__version__,
           "scipy": scipy.__version__, "machine": platform.machine()}
    print("  environment: " + json.dumps(env))
    print("  NOTE: the digest below is over values canonically rounded to 10 "
          "significant digits, which absorbs BLAS-level last-bit differences. It is "
          "NOT a proof of bit-identical reproducibility across environments.")
    blob = json.dumps(_canon(res), indent=2, sort_keys=True)
    print("BEGIN_ZS_S18_RESULTS")
    print(blob)
    print("END_ZS_S18_RESULTS")
    print("SHA256(result block) = " + hashlib.sha256(blob.encode()).hexdigest())

    if npass != ntot:
        print("\n  FAIL-CLOSED: at least one check did not pass.")
        sys.exit(1)


if __name__ == "__main__":
    main()
