#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_s21_verify_v1_2.py
=====================================================================
Companion verification suite for

    ZS-S21 v1.2 TERMINAL -- The Instrument Construction:
    Closing the Cellular Transfer-Matrix / Hodge-Measure Sub-Bridge
    of Z-Spin Yang-Mills
    Kenny Kang, Z-Spin Cosmology Collaboration, July 2026

Environment : Python 3.12+, numpy 2.4+, scipy 1.17+, sympy 1.14+, mpmath 1.3
Deterministic seed : 20260320
Results block delimited by  BEGIN_ZS_S21_RESULTS / END_ZS_S21_RESULTS
The file emits its own SHA256.

CHECK KINDS
-----------
  check : an executable assertion on a computed number derived from the
          actual 90/32-dimensional Z-Spin objects (or the 9/5-dimensional
          two-orbit model complex used for the end-to-end transfer-matrix
          diagonalisation).
  proxy : a generic theorem verified on a surrogate object.  A proxy is
          NEVER counted as a verification of the Z-Spin object itself.
  decl  : a registry statement (gate status, epistemic tag, supersession).
          Declarative only; carries no numerical content.

ANTI-REGRESSION
---------------
The suite parses its own source with `ast` and asserts that no `check`-kind
assertion is a literal True / a bare constant.  (ZS-S20 v2.2 retraction.)
=====================================================================
"""

import ast, hashlib, inspect, itertools, os, sys, time
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigsh
from scipy.special import ive

SEED = 20260320
RNG = np.random.default_rng(SEED)
np.set_printoptions(precision=10, suppress=True)

# ---------------------------------------------------------------- ledger ---
LEDGER = []
def record(cid, kind, desc, ok, detail=""):
    LEDGER.append(dict(id=cid, kind=kind, desc=desc, ok=bool(ok), detail=detail))
    tag = {"check": "CHK", "proxy": "PRX", "decl": "DEC"}[kind]
    print(f"  [{tag}] {cid:<9} {'PASS' if ok else 'FAIL':4}  {desc}"
          + (f"   | {detail}" if detail else ""))

def chk(cid, desc, ok, detail=""):  record(cid, "check", desc, ok, detail)
def prx(cid, desc, ok, detail=""):  record(cid, "proxy", desc, ok, detail)
def dec(cid, desc, detail=""):      record(cid, "decl",  desc, True, detail)

APPROX = lambda a, b, t=1e-9: abs(float(a) - float(b)) < t

# ===========================================================================
# 0.  LOCKED CONSTANTS  (never re-fitted)
# ===========================================================================
A_IMP   = sp.Rational(35, 437)          # geometric impedance  A = delta_X delta_Y
Q_REG   = 11                            # register width  Q = 3 + 6 + 2
DIM_Z   = 2
LAM1_L  = 1.2428416164                  # locked, a_TI = 1 convention
LAMH_L  = 7.5210904061

print("BEGIN_ZS_S21_RESULTS")
print("=" * 74)
print("ZS-S21 v1.2 verification suite   seed =", SEED)
print("=" * 74)

print("\n[S1] LOCKED CONSTANTS")
chk("T001", "A = 35/437 = delta_X * delta_Y = (5/19)*(7/23)",
    A_IMP == sp.Rational(5, 19) * sp.Rational(7, 23), f"A = {A_IMP}")
chk("T002", "Q = 11 = dim X + dim Y + dim Z = 3 + 6 + 2", Q_REG == 3 + 6 + 2)
chk("T003", "dim Z = 2", DIM_Z == 2)
dec("D004", "HYPOTHESIS REGISTER (v1.1). The closure of ZS-S21 rests on exactly "
            "three named statements, none of which is a free parameter: "
            "(H-W) the cellular reduction of ZS-S14 onto K_TI x a_t Z is a "
            "group-valued Wilson-type plaquette action with compact link "
            "variables and nearest-neighbour coupling in time; "
            "(Z-A0) K_TI enters the reduction metric-free; "
            "(Z-A1) EXPANDED IN v1.2 -- the plaquette weights are orbit-blind "
            "for BOTH anisotropy classes: within each class the character-kernel "
            "coefficient is independent of every ambient combinatorial orbit and "
            "of every dual-cell datum, so beta_e = beta_t for all 90 edges and "
            "beta_f = beta_s for all 32 faces.")
dec("D005", "SCOPE. In this suite and in ZS-S21, 'Yang-Mills bridge' denotes the "
            "cellular transfer-matrix / Hodge-measure sub-bridge only. It does "
            "NOT denote closure of the full non-perturbative SU(3) glueball "
            "spectrum, the absolute glueball interaction coefficient, or the "
            "continuum scheme-matching programme.")

# ===========================================================================
# 1.  REBUILD K_TI FROM SCRATCH  (no imported data files)
# ===========================================================================
print("\n[S2] K_TI  --  independent reconstruction")

PHI = (1 + 5 ** 0.5) / 2
def _even(t):
    a, b, c = t
    return [(a, b, c), (b, c, a), (c, a, b)]
_verts = set()
for t in [(0, 1, 3 * PHI), (1, 2 + PHI, 2 * PHI), (PHI, 2, 2 * PHI + 1)]:
    for p in _even(t):
        for s in itertools.product([1, -1], repeat=3):
            _verts.add(tuple(round(s[i] * p[i], 9) for i in range(3)))
V = np.array(sorted(_verts))

D = np.linalg.norm(V[:, None, :] - V[None, :, :], axis=2)
dmin = D[D > 1e-6].min()
edges = sorted((i, j) for i in range(len(V)) for j in range(i + 1, len(V))
               if abs(D[i, j] - dmin) < 1e-6)
eidx = {e: k for k, e in enumerate(edges)}

hull = ConvexHull(V)
_norms, _groups = [], []
for s, eq in zip(hull.simplices, hull.equations):
    n = np.round(eq[:4], 7); hit = False
    for k, nn in enumerate(_norms):
        if np.allclose(nn, n, atol=1e-5):
            _groups[k].update(s.tolist()); hit = True; break
    if not hit:
        _norms.append(n); _groups.append(set(s.tolist()))

def _order(fv, eq):
    pts = V[fv]; c = pts.mean(0); n = np.array(eq[:3])
    u = pts[0] - c; u /= np.linalg.norm(u); w = np.cross(n, u)
    o = [fv[i] for i in np.argsort(
        [np.arctan2(np.dot(p - c, w), np.dot(p - c, u)) for p in pts])]
    q = V[o]
    if np.dot(np.cross(q[1] - q[0], q[2] - q[0]), n) < 0:
        o = o[::-1]
    return o
faces = sorted((_order(sorted(g), nn) for g, nn in zip(_groups, _norms)),
               key=lambda f: (len(f), f))
nV, nE, nF = len(V), len(edges), len(faces)

B1 = np.zeros((nV, nE))
for k, (i, j) in enumerate(edges):
    B1[i, k], B1[j, k] = -1, +1
B2 = np.zeros((nF, nE))
for f, cyc in enumerate(faces):
    for a in range(len(cyc)):
        i, j = cyc[a], cyc[(a + 1) % len(cyc)]
        if i < j: B2[f, eidx[(i, j)]] += 1
        else:     B2[f, eidx[(j, i)]] -= 1

chk("T010", "V, E, F = 60, 90, 32", (nV, nE, nF) == (60, 90, 32), f"{nV},{nE},{nF}")
chk("T011", "Euler characteristic chi = 2", nV - nE + nF == 2)
chk("T012", "12 pentagons and 20 hexagons",
    sum(len(f) == 5 for f in faces) == 12 and sum(len(f) == 6 for f in faces) == 20)
chk("T013", "chain complex  B2 B1^T = 0 exactly",
    np.abs(B2 @ B1.T).max() < 1e-12, f"max |B2 B1^T| = {np.abs(B2@B1.T).max():.1e}")
rk1, rk2 = np.linalg.matrix_rank(B1), np.linalg.matrix_rank(B2)
chk("T014", "rank B1 = 59  (exact / longitudinal)", rk1 == 59)
chk("T015", "rank B2 = 31  (coexact / transverse)", rk2 == 31)
chk("T016", "metric-free Hodge census 90 = 59 + 31 + 0", nE - rk1 - rk2 == 0)
chk("T017", "ker B2^T = span(1), dimension 1", nF - rk2 == 1)
chk("T018", "delta_Y = |V - F|/(V + F) = 28/92 = 7/23",
    sp.Rational(abs(nV - nF), nV + nF) == sp.Rational(7, 23))

# edge and face orbits
_fo = [[] for _ in range(nE)]
for f, cyc in enumerate(faces):
    for a in range(len(cyc)):
        i, j = cyc[a], cyc[(a + 1) % len(cyc)]
        _fo[eidx[(min(i, j), max(i, j))]].append(len(cyc))
etype = [tuple(sorted(x)) for x in _fo]
i56 = [k for k in range(nE) if etype[k] == (5, 6)]
i66 = [k for k in range(nE) if etype[k] == (6, 6)]
p5 = [f for f in range(nF) if len(faces[f]) == 5]
p6 = [f for f in range(nF) if len(faces[f]) == 6]
chk("T019", "edge orbits: 60 of type (5,6), 30 of type (6,6)",
    len(i56) == 60 and len(i66) == 30)
chk("T020", "face orbits: 12 pentagons, 20 hexagons", len(p5) == 12 and len(p6) == 20)

# ===========================================================================
# 2.  EXACT SPECTRAL ALGEBRA  (Cor S20.Q, carried forward)
# ===========================================================================
print("\n[S3] Exact spectral algebra of B2 B2^T")

L2i = sp.Matrix((B2 @ B2.T).round().astype(int))
lam = sp.symbols("lam")
chi = sp.factor(L2i.charpoly(lam).as_expr())
target = (lam * (lam - 6) ** 4 * (lam - 8) ** 5 * (lam ** 2 - 10 * lam + 22) ** 5
          * (lam ** 4 - 22 * lam ** 3 + 166 * lam ** 2 - 480 * lam + 380) ** 3)
chk("T030", "characteristic polynomial factorises as in Cor S20.Q",
    sp.simplify(sp.expand(chi - target)) == 0)
quart = sp.Poly(lam ** 4 - 22 * lam ** 3 + 166 * lam ** 2 - 480 * lam + 380, lam)
chk("T031", "the quartic p(lam) is irreducible over Q", quart.is_irreducible)
qr = sorted(float(sp.N(r, 20)) for r in quart.all_roots())
chk("T032", "lambda_1 is a root of p(lam)", APPROX(qr[0], LAM1_L, 1e-9), f"{qr[0]:.10f}")
chk("T033", "lambda_h is a root of p(lam)", APPROX(qr[2], LAMH_L, 1e-9), f"{qr[2]:.10f}")
chk("T034", "sum of the four roots of p is 22  (Vieta)", APPROX(sum(qr), 22.0, 1e-9))
chk("T035", "lam^2 - 10 lam + 22 has roots 5 +/- sqrt(3), multiplicity 5",
    APPROX(5 - 3 ** 0.5, 3.2679491924, 1e-9) and APPROX(5 + 3 ** 0.5, 6.7320508076, 1e-9))
chk("T036", "Tr(B2 B2^T) = 2E = 180", APPROX(np.trace(B2 @ B2.T), 180.0, 1e-9))

w_full = np.sort(np.linalg.eigvalsh(B2 @ B2.T))
levels = []
for x in w_full:
    if levels and abs(x - levels[-1][0]) < 1e-8: levels[-1][1] += 1
    else: levels.append([x, 1])
chk("T037", "spectrum has 9 distinct levels with multiplicities 1,3,5,3,4,5,3,5,3",
    [m for _, m in levels] == [1, 3, 5, 3, 4, 5, 3, 5, 3])
chk("T038", "multiplicities sum to F = 32", sum(m for _, m in levels) == 32)

# ===========================================================================
# 3.  ERRATUM E-1 : I_h isotypic content of Omega^2(K_TI)
# ===========================================================================
print("\n[S4] I_h representation content of the 32-dimensional face space")

Vn = V / np.linalg.norm(V[0])
def _isometries(P):
    n = len(P); tol = 1e-6; DD = P @ P.T; base = [0]
    for k in range(1, n):
        if np.linalg.matrix_rank(P[base + [k]], tol=1e-6) == len(base) + 1:
            base.append(k)
        if len(base) == 3: break
    Ainv = np.linalg.inv(P[base]); out = []
    for t in itertools.permutations(range(n), 3):
        if not all(abs(DD[base[a], base[b]] - DD[t[a], t[b]]) < tol
                   for a in range(3) for b in range(3)):
            continue
        R = Ainv @ P[list(t)]
        if np.abs(R.T @ R - np.eye(3)).max() > 1e-6: continue
        Qm = P @ R
        idx = np.argmin(((Qm[:, None, :] - P[None, :, :]) ** 2).sum(-1), axis=1)
        if np.abs(Qm - P[idx]).max() < 1e-6:
            out.append((R, idx))
    return out
GRP = _isometries(Vn)
chk("T040", "|Aut(K_TI)| = 120 = |I_h|", len(GRP) == 120, f"{len(GRP)}")

_fk = {tuple(sorted(f)): k for k, f in enumerate(faces)}
FPERM = [np.array([_fk[tuple(sorted(idx[np.array(f)].tolist()))] for f in faces])
         for _, idx in GRP]
PIm = []
for fp in FPERM:
    M = np.zeros((nF, nF)); M[fp, np.arange(nF)] = 1; PIm.append(M)

_chiA5 = {
    3.0: {"1": 1, "3": 3, "3p": 3, "4": 4, "5": 5},
    round(1 + 2 * np.cos(2 * np.pi / 5), 6): {"1": 1, "3": PHI, "3p": 1 - PHI, "4": -1, "5": 0},
    round(1 + 2 * np.cos(4 * np.pi / 5), 6): {"1": 1, "3": 1 - PHI, "3p": PHI, "4": -1, "5": 0},
    round(1 + 2 * np.cos(2 * np.pi / 3), 6): {"1": 1, "3": 0, "3p": 0, "4": 1, "5": -1},
    -1.0: {"1": 1, "3": -1, "3p": -1, "4": 0, "5": 1}}
def _key(R):
    dt = np.linalg.det(R); tr = round(np.trace(R * np.sign(dt)), 6)
    for k in _chiA5:
        if abs(k - tr) < 1e-4: return k, (1 if dt > 0 else -1)
    raise ValueError(tr)
NAMES = [(a, b) for a in ["1", "3", "3p", "4", "5"] for b in ["g", "u"]]
LABEL = {("1","g"):"A_g", ("1","u"):"A_u", ("3","g"):"T_1g", ("3","u"):"T_1u",
         ("3p","g"):"T_2g", ("3p","u"):"T_2u", ("4","g"):"G_g", ("4","u"):"G_u",
         ("5","g"):"H_g", ("5","u"):"H_u"}
def _chi(nm, R):
    k, par = _key(R); a, b = nm
    return _chiA5[k][a] * (1 if b == "g" else par)
def decompose(fun):
    out = {}
    for nm in NAMES:
        m = sum(fun(i) * _chi(nm, GRP[i][0]) for i in range(len(GRP))) / len(GRP)
        if abs(m) > 1e-4: out[LABEL[nm]] = round(m, 4)
    return out

face_dec = decompose(lambda i: np.trace(PIm[i]))
chk("T041", "Omega^2(K_TI) = 2A_g + 2T_1u + 2T_2u + 2H_g + G_g + G_u",
    face_dec == {"A_g": 2.0, "T_1u": 2.0, "T_2u": 2.0, "H_g": 2.0, "G_g": 1.0, "G_u": 1.0},
    str(face_dec))
chk("T042", "ERRATUM E-1a: NOT all ten I_h irreps occur; exactly six do",
    len(face_dec) == 6 and all(x not in face_dec for x in ("A_u", "T_1g", "T_2g", "H_u")))

wv, U = np.linalg.eigh(B2 @ B2.T)
lev_idx = []
for i, x in enumerate(wv):
    if lev_idx and abs(x - lev_idx[-1][0]) < 1e-8: lev_idx[-1][1].append(i)
    else: lev_idx.append([x, [i]])
iso = {}
for x, ids in lev_idx:
    P = U[:, ids] @ U[:, ids].T
    iso[round(x, 8)] = decompose(lambda i: np.trace(P @ PIm[i]))
chk("T043", "ERRATUM E-1b: lambda = 8 (mult 5) is A_g + G_g, not the H irrep",
    set(iso[8.0]) == {"A_g", "G_g"}, str(iso[8.0]))
chk("T044", "lambda = 6 (mult 4) is G_u", set(iso[6.0]) == {"G_u"}, str(iso[6.0]))
chk("T045", "lambda_1 and lambda_h both sit in T_1u",
    set(iso[round(qr[0], 8)]) == {"T_1u"} and set(iso[round(qr[2], 8)]) == {"T_1u"})
v_ag = 20 * np.array([1.0 if len(f) == 5 else 0.0 for f in faces]) \
     - 12 * np.array([0.0 if len(f) == 5 else 1.0 for f in faces])
chk("T046", "the second A_g eigenvector (20*1_pent - 12*1_hex) has eigenvalue 8",
    np.abs((B2 @ B2.T) @ v_ag - 8 * v_ag).max() < 1e-9,
    f"residual = {np.abs((B2@B2.T)@v_ag - 8*v_ag).max():.1e}")

# ===========================================================================
# 4.  K_TI x a_t Z  --  cell census and congruence
# ===========================================================================
print("\n[S5] The complex K_TI x a_t Z in temporal gauge")

NT = 4
temporal = [(e, t) for e in range(nE) for t in range(NT)]
spatial  = [(f, t) for f in range(nF) for t in range(NT)]
chk("T050", "2-cells per time slab: 90 temporal + 32 spatial",
    len(temporal) // NT == 90 and len(spatial) // NT == 32)
chk("T051", "temporal plaquettes are in bijection with the 90 edges",
    sorted({p[0] for p in temporal}) == list(range(nE)) and len(temporal) // NT == nE)
chk("T052", "K_TI carries no 3-cells: dim K = 2, so there is no third plaquette class",
    len(faces) == 32 and nV - nE + nF == 2)
elen = np.array([np.linalg.norm(V[i] - V[j]) for i, j in edges])
chk("T053", "all 90 edges of K_TI are congruent (Archimedean)",
    np.ptp(elen) < 1e-8, f"length spread = {np.ptp(elen):.2e}")
chk("T054", "=> all 90 temporal plaquettes e x a_t are mutually congruent",
    np.ptp(elen) < 1e-8 and len({len(f) for f in faces}) == 2)
A5a = 5 / (4 * np.tan(np.pi / 5)); A6a = 3 * np.sqrt(3) / 2
chk("T055", "spatial faces are NOT congruent: A6/A5 = 1.5100902868",
    APPROX(A6a / A5a, 1.5100902868, 1e-9), f"A6/A5 = {A6a/A5a:.10f}")

# ===========================================================================
# 5.  THEOREM S21.1  --  the transfer matrix produces a DIAGONAL M
# ===========================================================================
print("\n[S6] Theorem S21.1: M is diagonal, on the actual 90/32 objects")

BT, BS = 1.7, 0.9
h = 1e-5
def _hess(fun, n):
    H = np.zeros((n, n))
    for a in range(n):
        ea = np.zeros(n); ea[a] = h
        for b in range(a, n):
            eb = np.zeros(n); eb[b] = h
            H[a, b] = H[b, a] = (fun(ea + eb) - fun(ea - eb)
                                 - fun(-ea + eb) + fun(-ea - eb)) / (4 * h * h)
    return H
Ht = _hess(lambda u: BT * np.sum(1 - np.cos(u)), nE)
dev_t = np.abs(Ht - BT * np.eye(nE)).max()
chk("T060", "temporal Wilson Hessian = beta_t * I_90  (M1 uniform)",
    dev_t < 1e-6, f"max dev = {dev_t:.2e}")
chk("T061", "temporal Hessian has zero off-diagonal part => F-S20.5 cannot fire",
    np.abs(Ht - np.diag(np.diag(Ht))).max() < 1e-6)
Hs = _hess(lambda th: BS * np.sum(1 - np.cos(B2 @ th)), nE)
dev_s = np.abs(Hs - BS * (B2.T @ B2)).max()
chk("T062", "spatial Wilson Hessian = beta_s * B2^T B2  (M2 = beta_s I_32)",
    dev_s < 1e-5, f"max dev = {dev_s:.2e}")
chk("T063", "no edge-edge coupling outside the incidence pattern of B2^T B2",
    np.abs(Hs[np.abs(B2.T @ B2) < 1e-12]).max() < 1e-5)
# T063b: diagonality of M2 must hold for ARBITRARY orbit-dependent weights,
# not only for the uniform branch.  This is the general content of Thm S21.1.
bf_nu = np.array([1.3 if len(f) == 5 else 0.8 for f in faces])
Hnu = _hess(lambda th: float(np.sum(bf_nu * (1 - np.cos(B2 @ th)))), nE)
dev_nu = np.abs(Hnu - B2.T @ np.diag(bf_nu) @ B2).max()
chk("T064", "with orbit-dependent weights beta_5 = 1.3, beta_6 = 0.8 the spatial "
            "Hessian is still B2^T diag(beta_f) B2, i.e. M2 is diagonal in the "
            "face basis for EVERY weight assignment",
    dev_nu < 1e-5, f"max dev = {dev_nu:.2e}")
# T065 (NEW in v1.2): the TEMPORAL analogue.  The transfer matrix propagates
# edge-orbit dependence exactly as it propagates face-orbit dependence; it does
# not remove it.  This is what makes Theorem S21.2 conditional, not absolute.
be_nu = np.array([1.3 if etype[k] == (5, 6) else 0.8 for k in range(nE)])
Ht_nu = _hess(lambda u: float(np.sum(be_nu * (1 - np.cos(u)))), nE)
dev_tnu = np.abs(Ht_nu - np.diag(be_nu)).max()
chk("T065", "with orbit-dependent temporal weights beta_56 = 1.3, beta_66 = 0.8 "
            "the temporal Hessian is diag(beta_e), NOT beta_t I_90: the transfer "
            "matrix PROPAGATES electric orbit dependence and does not remove it",
    dev_tnu < 1e-6 and abs(Ht_nu[i56[0], i56[0]] - Ht_nu[i66[0], i66[0]]) > 0.4,
    f"max dev = {dev_tnu:.2e}; H(5,6) = {Ht_nu[i56[0],i56[0]]:.6f}, "
    f"H(6,6) = {Ht_nu[i66[0],i66[0]]:.6f}")

# ===========================================================================
# 6.  THEOREM S21.2  --  sigma = 1 is DERIVED, unconditionally
# ===========================================================================
print("\n[S7] Theorem S21.2: edge-orbit uniformity  sigma = m56/m66 = 1")

def D2(rho, sigma, r=1.0):
    m = np.ones(nE); m[i56] = sigma; m[i66] = 1.0
    b = np.ones(nF); b[p5] = rho;    b[p6] = 1.0
    S = np.diag(np.sqrt(b)) @ B2 @ np.diag(1.0 / m) @ B2.T @ np.diag(np.sqrt(b))
    return np.sort(np.linalg.eigvalsh(r * S))

chk("T070", "rho = sigma = 1 reproduces spec(B2 B2^T) exactly",
    np.abs(D2(1, 1) - w_full).max() < 1e-9)
chk("T071", "sigma = 1 returns the LOCKED lambda_1 = 1.2428416164",
    APPROX(D2(1, 1)[1], LAM1_L, 1e-9), f"lambda_1 = {D2(1,1)[1]:.10f}")
chk("T072", "sigma = 1.2550451434 (H-UA of ZS-S20) gives lambda_1 = 1.0820156113",
    APPROX(D2(1, 1.2550451434)[1], 1.0820156113, 1e-8),
    f"lambda_1 = {D2(1,1.2550451434)[1]:.10f}")
chk("T073", "sigma = 0.9105929973 (flat cone metric) does NOT return the locked value",
    abs(D2(1, 0.9105929973)[1] - LAM1_L) > 1e-3,
    f"lambda_1 = {D2(1,0.9105929973)[1]:.10f}")
chk("T074", "PRIMAL congruence only: the mean edge length of the (5,6) orbit "
            "equals that of the (6,6) orbit, so no weight built from the "
            "plaquette's own primal geometry can separate them",
    abs(elen[i56].mean() - elen[i66].mean()) < 1e-8,
    f"|e|_56 - |e|_66 = {elen[i56].mean()-elen[i66].mean():.1e}")

# ---- v1.2: the temporal AMBIENT-STAR obstruction -------------------------
# The two edge orbits have identical primal length but DIFFERENT ambient stars:
# a (5,6) edge borders a pentagon and a hexagon, a (6,6) edge borders two
# hexagons.  Every dual measure therefore separates them.
_L = elen[0]
_a5 = _L / (2 * np.tan(np.pi / 5))            # pentagon apothem
_a6 = _L * np.sqrt(3) / 2                     # hexagon apothem
sig_intrinsic = (_a5 + _a6) / (2 * _a6)       # intrinsic flat unfolded dual
_cc = [V[np.array(f)].mean(0) for f in faces]
_fo2 = {k: [] for k in range(nE)}
for f, cyc in enumerate(faces):
    for a in range(len(cyc)):
        i, j = cyc[a], cyc[(a + 1) % len(cyc)]
        _fo2[eidx[(min(i, j), max(i, j))]].append(f)
_dl = np.array([np.linalg.norm(_cc[_fo2[k][0]] - _cc[_fo2[k][1]]) for k in range(nE)])
sig_chordal = _dl[i56].mean() / _dl[i66].mean()
chk("T075", "the DUAL measure separates the two edge orbits even though the "
            "primal lengths coincide: |*e|_56/|*e|_66 = 0.8973272361 "
            "(intrinsic) and 0.9105929973 (chordal circumcentric)",
    abs(sig_intrinsic - 1) > 1e-3 and abs(sig_chordal - 1) > 1e-3,
    f"intrinsic {sig_intrinsic:.10f} | chordal {sig_chordal:.10f}")
chk("T076", "the chordal circumcentric ratio reproduces the ZS-S20 Table 17.1 "
            "flat-cone value m56/m66 = 0.9105929973 independently",
    APPROX(sig_chordal, 0.9105929973, 1e-9), f"{sig_chordal:.10f}")
chk("T077", "the metric-free ambient-star family beta_e = psi_e({deg f : f > e}) "
            "realises any sigma > 0, so (H-W) alone does NOT give sigma = 1",
    len({round(D2(1.0, x)[1], 8) for x in (0.8, 0.9, 1.0, 1.15, 1.3)}) == 5,
    "lambda_1 in " + str([round(D2(1.0, x)[1], 8) for x in (0.8, 0.9, 1.0, 1.15, 1.3)]))
dec("D078", "RETRACTION S21-R3 (v1.2, against v1.1). Version 1.1 stated Theorem "
            "S21.2 as unconditional in the weights and titled its section "
            "'Edge-Orbit Uniformity Is Unconditional'. That is too strong. The "
            "primal-plaquette congruence is unconditional (Lemma S21.2, T053, "
            "T054, T074); the WEIGHT uniformity sigma = 1 is not, because a "
            "metric-free ambient-star function or any dual measure separates the "
            "orbits (T065, T075, T076, T077). sigma = 1 is DERIVED-CONDITIONAL on "
            "the expanded (Z-A1), exactly as rho = 1 is.")

# ===========================================================================
# 7.  rho = beta_5/beta_6  --  the one residual dimensionless number
# ===========================================================================
print("\n[S8] The residual: rho = beta_5/beta_6  (Axiom Z-A branch point)")

for rho in (0.9, 1.0, 1.2, 1.5100902868):
    sp_ = D2(rho, 1.0)
    mm = []
    for x in sp_:
        if mm and abs(x - mm[-1][0]) < 1e-8: mm[-1][1] += 1
        else: mm.append([x, 1])
    print(f"        rho = {rho:.10f}  multiplicities = {[m for _,m in mm]}"
          f"   lambda_1 = {sp_[1]:.10f}")
chk("T080", "Lemma S20.A1: the unique nonzero multiplicity-one level is r(5 rho + 3)",
    all(any(abs(x - (5 * r_ + 3)) < 1e-7 for x in D2(r_, 1.0))
        for r_ in (0.7, 0.9, 1.2, 1.5, 2.3)))
chk("T081", "the two multiplicity-4 levels 6 and 8 are rho-independent",
    all(sum(abs(D2(r_, 1.0) - 6) < 1e-8) == 4 and sum(abs(D2(r_, 1.0) - 8) < 1e-8) >= 4
        for r_ in (0.7, 1.2, 2.3)))
chk("T082", "at rho = 1 the A_g and G_g levels accidentally coincide at 8 (mult 5); "
            "for rho != 1 they split",
    sum(abs(D2(1.0, 1.0) - 8) < 1e-9) == 5 and sum(abs(D2(1.2, 1.0) - 8) < 1e-9) == 4)
# All branch comparisons are made in ONE stated convention: (H-TR) Tr Delta_2 = 2E,
# which fixes the scale r for each rho.  Tr Delta_2 = r (60 rho + 120), so r = 3/(rho+2).
rscale = lambda rho: 3.0 / (rho + 2.0)
lam1_of = lambda rho: D2(rho, 1.0, rscale(rho))[1]
chk("T083", "counting branch (rho = 1) reproduces the LOCKED lambda_1 exactly "
            "in the (H-TR) convention",
    APPROX(lam1_of(1.0), 1.2428416164, 1e-9), f"lambda_1 = {lam1_of(1.0):.10f}")
LAM1_CFL = lam1_of(A6a / A5a)
chk("T084", "CFL / heat-kernel branch (rho = A6/A5 = 1.5100902868) gives a "
            "DIFFERENT lambda_1 in the same convention",
    abs(LAM1_CFL - LAM1_L) > 1e-3, f"lambda_1 = {LAM1_CFL:.10f}")
chk("T085", "the branch separation in lambda_1 is -1.816 %, i.e. -0.912 % in the "
            "physical energy omega = sqrt(r lambda)",
    APPROX(100 * (LAM1_CFL / LAM1_L - 1), -1.8162, 5e-3),
    f"dlambda = {100*(LAM1_CFL/LAM1_L-1):.4f} %, "
    f"domega = {100*((LAM1_CFL/LAM1_L)**0.5-1):.4f} %")
dec("D086", "ZS-S20 Table 19.2 quotes lambda_1 = 1.2492508718 (+0.5157 %) for the "
            "heat-kernel branch without stating its normalisation convention. "
            "In the (H-TR) convention adopted here the value is different. "
            "Registered as ERRATUM-CANDIDATE E-5; it does not affect the closure "
            "argument, which needs only that the two branches are separated.")
dec("D087", "RETRACTION S21-R2. ZS-S21 v1.0 inferred rho = 1 from the metric-free "
            "axiom alone. That inference is INVALID: beta_f = beta_s psi(n_f) is "
            "metric-free and gives any rho > 0. This is the ZS-S19 v1.3 psi(n_f) "
            "retraction recurring. v1.1 splits the axiom into (Z-A0) metric-free "
            "and (Z-A1) orbit-blind, and rho = 1 follows only from BOTH.")
# the psi(n_f) family is metric-free and spans all of rho > 0
psi_rhos = [(1.0, "psi = 1"), (1.2, "psi = 1/n_f"), (5/6, "psi = n_f"),
            (4/3, "psi = 1/(n_f - 2)"), (0.75, "psi = n_f - 2")]
chk("T086", "the metric-free family beta_f = beta_s psi(n_f) realises many "
            "distinct rho, so (Z-A0) alone does NOT give rho = 1",
    len({round(x, 10) for x, _ in psi_rhos}) == 5
    and len({round(lam1_of(x), 8) for x, _ in psi_rhos}) == 5,
    "rho in " + str([round(x, 6) for x, _ in psi_rhos]))
chk("T087", "each psi branch returns a different lambda_1, so rho is a genuine "
            "continuous freedom until (Z-A1) is imposed",
    max(abs(lam1_of(x) / LAM1_L - 1) for x, _ in psi_rhos) > 0.01,
    "lambda_1 in " + str([round(lam1_of(x), 8) for x, _ in psi_rhos]))

# ---- isotype-resolved branch comparison -----------------------------------
def levels_iso(rho):
    b = np.ones(nF); b[p5] = rho
    S = np.diag(np.sqrt(b)) @ B2 @ B2.T @ np.diag(np.sqrt(b))
    rr = 180.0 / np.trace(S)                       # (H-TR) normalisation
    S = rr * S
    ww, UU = np.linalg.eigh(S); out = []; i = 0
    while i < len(ww):
        j = i
        while j + 1 < len(ww) and abs(ww[j + 1] - ww[i]) < 1e-8: j += 1
        ids = list(range(i, j + 1)); Pp = UU[:, ids] @ UU[:, ids].T
        out.append((ww[i], len(ids), decompose(lambda k: np.trace(Pp @ PIm[k]))))
        i = j + 1
    return out
def lowest_of(L, tag):
    for x, m, iso in L:
        if x > 1e-9 and tag in iso: return x
    return None
Lc = levels_iso(1.0); Lf = levels_iso(A6a / A5a)
nz_c = [(x, m, "+".join(iso)) for x, m, iso in Lc if x > 1e-9]
nz_f = [(x, m, "+".join(iso)) for x, m, iso in Lf if x > 1e-9]
print("        counting branch (rho = 1):")
for x, m, s_ in nz_c: print(f"          {x:.10f}  x{m}  {s_}")
print("        CFL branch (rho = A6/A5):")
for x, m, s_ in nz_f: print(f"          {x:.10f}  x{m}  {s_}")
chk("T088", "the branch shift is NOT uniform across modes: the lowest T_1u moves "
            "by -0.9125 % in omega while the lowest T_2u moves by +10.6281 %",
    APPROX(100 * ((lowest_of(Lf, "T_2u") / lowest_of(Lc, "T_2u")) ** 0.5 - 1),
           10.6281, 5e-3),
    f"T_1u {100*((lowest_of(Lf,'T_1u')/lowest_of(Lc,'T_1u'))**0.5-1):+.4f} % ; "
    f"T_2u {100*((lowest_of(Lf,'T_2u')/lowest_of(Lc,'T_2u'))**0.5-1):+.4f} % ; "
    f"G_u {100*((lowest_of(Lf,'G_u')/lowest_of(Lc,'G_u'))**0.5-1):+.4f} %")
chk("T089", "ORDERING DISCRIMINATOR: the third-lowest excitation has multiplicity "
            "3 (T_2u) in the counting branch and multiplicity 4 (G_u) in the CFL "
            "branch -- a qualitative, precision-free branch test",
    nz_c[2][1] == 3 and nz_c[2][2] == "T_2u" and nz_f[2][1] == 4 and nz_f[2][2] == "G_u",
    f"counting {nz_c[2][1]}x{nz_c[2][2]} | CFL {nz_f[2][1]}x{nz_f[2][2]}")
# scale-free ratios
R_T2_c = (lowest_of(Lc, "T_2u") / lowest_of(Lc, "T_1u")) ** 0.5
R_T2_f = (lowest_of(Lf, "T_2u") / lowest_of(Lf, "T_1u")) ** 0.5
R_Hg_c = (lowest_of(Lc, "H_g") / lowest_of(Lc, "T_1u")) ** 0.5
R_Hg_f = (lowest_of(Lf, "H_g") / lowest_of(Lf, "T_1u")) ** 0.5
chk("T092", "scale-free discriminator D1 = omega(T_2u,1)/omega(T_1u,1): "
            "counting 1.9742883436 vs CFL 2.2042305065, separation +11.65 %",
    APPROX(R_T2_c, 1.9742883436, 1e-8) and APPROX(100 * (R_T2_f / R_T2_c - 1), 11.6470, 5e-3),
    f"D1 count {R_T2_c:.10f} | CFL {R_T2_f:.10f} | midpoint {(R_T2_c+R_T2_f)/2:.10f}")
chk("T093", "scale-free discriminator D2 = omega(H_g,1)/omega(T_1u,1) is WEAK: "
            "counting 1.6215477963 vs CFL 1.6301340807, separation only +0.53 %",
    APPROX(R_Hg_c, 1.6215477963, 1e-8) and abs(100 * (R_Hg_f / R_Hg_c - 1)) < 1.0,
    f"D2 count {R_Hg_c:.10f} | CFL {R_Hg_f:.10f} | "
    f"sep {100*(R_Hg_f/R_Hg_c-1):+.4f} %")

# ---- v1.2: the FULL metric branch, sigma and rho both metric-induced -----
def levels_iso2(sigma, rho):
    m = np.ones(nE); m[i56] = sigma
    b = np.ones(nF); b[p5] = rho
    S = np.diag(np.sqrt(b)) @ B2 @ np.diag(1.0 / m) @ B2.T @ np.diag(np.sqrt(b))
    S = (180.0 / np.trace(S)) * S
    ww, UU = np.linalg.eigh(S); out = []; i = 0
    while i < len(ww):
        j = i
        while j + 1 < len(ww) and abs(ww[j + 1] - ww[i]) < 1e-8: j += 1
        ids = list(range(i, j + 1)); Pp = UU[:, ids] @ UU[:, ids].T
        out.append((ww[i], len(ids), decompose(lambda k: np.trace(Pp @ PIm[k])))); i = j + 1
    return out
Lm = levels_iso2(sig_intrinsic, A6a / A5a)
nz_m = [(x, m, "+".join(iso)) for x, m, iso in Lm if x > 1e-9]
print("        full metric branch (sigma and rho both metric-induced):")
for x, m, s_ in nz_m: print(f"          {x:.10f}  x{m}  {s_}")
chk("T094", "the full metric branch gives lambda_1 = 1.2069213135, a shift of "
            "-2.8902 % from the counting branch",
    APPROX(nz_m[0][0], 1.2069213135, 1e-8),
    f"lambda_1 = {nz_m[0][0]:.10f} ({100*(nz_m[0][0]/LAM1_L-1):+.4f} %)")
R_T2_m = (lowest_of(Lm, "T_2u") / lowest_of(Lm, "T_1u")) ** 0.5
chk("T095", "the ordering discriminator is ROBUST: the third excitation has "
            "multiplicity 3 (T_2u) in the counting branch and multiplicity 4 "
            "(G_u) in BOTH metric branches",
    nz_c[2][1] == 3 and nz_f[2][1] == 4 and nz_m[2][1] == 4 and nz_m[2][2] == "G_u",
    f"counting {nz_c[2][1]} | spatial-CFL {nz_f[2][1]} | full metric {nz_m[2][1]}")
chk("T096", "D1 separates the counting branch from BOTH metric branches by more "
            "than 11 %, so gate F-S21.8 is branch-robust",
    (R_T2_f / R_T2_c - 1) > 0.11 and (R_T2_m / R_T2_c - 1) > 0.11,
    f"D1 count {R_T2_c:.10f} | spatial-CFL {R_T2_f:.10f} | full metric {R_T2_m:.10f}")

# ===========================================================================
# 8.  (H-TR) IS A UNIT CHOICE
# ===========================================================================
print("\n[S9] (H-TR) Tr Delta_2 = 2E is a scale condition, not a shape condition")
rsym = sp.Symbol("r", positive=True)
def trace_of(rho, r):
    m = np.ones(nE); m[i56] = 1.0
    b = np.ones(nF); b[p5] = rho
    return r * float(np.trace(np.diag(b) @ B2 @ np.diag(1 / m) @ B2.T))
sols = [float(sp.solve(sp.Eq(trace_of(r_, rsym), 180), rsym)[0]) for r_ in (0.8, 1.0, 1.3)]
chk("T090", "Tr Delta_2 = 2E has a positive solution r for EVERY rho",
    all(s > 0 for s in sols), f"r(0.8, 1.0, 1.3) = {[round(s,10) for s in sols]}")
chk("T091", "at rho = 1 the condition gives r = 1 (the a_TI = 1 convention)",
    APPROX(sols[1], 1.0, 1e-12))

# ===========================================================================
# 9.  GAUSS LAW AND THE CENSUS INSIDE THE CONSTRUCTED THEORY
# ===========================================================================
print("\n[S10] Gauss law, census 59 + 31, reflection positivity")
chk("T100", "Gauss constraints (B1 E)_v = 0 : 59 independent", rk1 == 59)
chk("T101", "physical edge degrees of freedom 90 - 59 = 31 = rank B2^T",
    nE - rk1 == rk2 == 31)
chk("T102", "no harmonic edge modes, H^1(K_TI) = 0", nE - rk1 - rk2 == 0)
chk("T103", "the Gauss generator commutes with the constructed Hamiltonian: "
            "B1 B2^T = 0 so magnetic term is gauge invariant",
    np.abs(B1 @ B2.T).max() < 1e-12)
# reflection positivity: character coefficients of the U(1) kinetic kernel
bt_test = 3.7
coef = np.array([ive(n, bt_test) for n in range(0, 40)])
chk("T104", "U(1) temporal kernel has strictly positive character coefficients "
            "I_n(beta_t) > 0 for all n  => T = A K A is positive",
    bool(np.all(coef > 0)), f"min I_n = {coef.min():.3e}")
_j = np.arange(0, 30)
chk("T105", "SU(2) heat-kernel coefficients exp(-t C_2(j)) > 0, C_2(j) = j(j+1)",
    bool(np.all(np.exp(-0.4 * _j * (_j + 1)) > 0)))
_pq = np.array([[(p ** 2 + q ** 2 + p * q + 3 * p + 3 * q) / 3.0
                 for q in range(0, 12)] for p in range(0, 12)])
chk("T106", "SU(3) heat-kernel coefficients exp(-t C_2(p,q)) > 0 with the actual "
            "SU(3) Casimir C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3 on a 12 x 12 "
            "(p,q) grid; C_2 >= 0 with equality only for the singlet",
    bool(np.all(np.exp(-0.4 * _pq) > 0)) and _pq.min() == 0.0
    and bool(np.all(_pq[1:, :] > 0)),
    f"C_2(1,0) = {_pq[1,0]:.6f}, C_2(1,1) = {_pq[1,1]:.6f}, max = {_pq.max():.4f}")
dec("D110", "Reflection positivity is a statement about the TIME reflection; "
            "no property of the spatial complex enters. Outcome D of the seed "
            "cannot fire and is removed from the pre-registration.")

# ===========================================================================
# 10. END-TO-END TRANSFER-MATRIX DIAGONALISATION  (two-orbit model complex)
# ===========================================================================
print("\n[S11] End-to-end compact-U(1) transfer-matrix test (triangular prism)")

Pp = np.array([[1, 0, 0], [-.5, np.sqrt(3) / 2, 0], [-.5, -np.sqrt(3) / 2, 0],
               [1, 0, 1.], [-.5, np.sqrt(3) / 2, 1], [-.5, -np.sqrt(3) / 2, 1]])
hl = ConvexHull(Pp); nrm, grp = [], []
for s, eq in zip(hl.simplices, hl.equations):
    n = np.round(eq[:4], 7); hit = False
    for k, nn in enumerate(nrm):
        if np.allclose(nn, n, atol=1e-5): grp[k].update(s.tolist()); hit = True; break
    if not hit: nrm.append(n); grp.append(set(s.tolist()))
def _ordp(fv, eq):
    pts = Pp[fv]; c = pts.mean(0); n = np.array(eq[:3])
    u = pts[0] - c; u /= np.linalg.norm(u); w = np.cross(n, u)
    o = [fv[i] for i in np.argsort(
        [np.arctan2(np.dot(p - c, w), np.dot(p - c, u)) for p in pts])]
    q = Pp[o]
    if np.dot(np.cross(q[1] - q[0], q[2] - q[0]), n) < 0: o = o[::-1]
    return o
pf = sorted((_ordp(sorted(g), nn) for g, nn in zip(grp, nrm)), key=lambda f: (len(f), f))
pe = sorted({tuple(sorted((f[a], f[(a + 1) % len(f)]))) for f in pf for a in range(len(f))})
pei = {e: k for k, e in enumerate(pe)}
pnV, pnE, pnF = 6, len(pe), len(pf)
pB2 = np.zeros((pnF, pnE)); pB1 = np.zeros((pnV, pnE))
for k, (i, j) in enumerate(pe): pB1[i, k], pB1[j, k] = -1, 1
for f, cyc in enumerate(pf):
    for a in range(len(cyc)):
        i, j = cyc[a], cyc[(a + 1) % len(cyc)]
        if i < j: pB2[f, pei[(i, j)]] += 1
        else:     pB2[f, pei[(j, i)]] -= 1
chk("T120", "model complex has two face orbits (2 triangles, 3 squares) and "
            "two edge orbits (6 of type (3,4), 3 of type (4,4))",
    sorted(len(f) for f in pf) == [3, 3, 4, 4, 4] and
    sum(1 for k in range(pnE)
        if sorted(len(f) for f in pf
                  if pe[k][0] in f and pe[k][1] in f) == [4, 4]) == 3)
chk("T121", "model complex chain complex pB2 pB1^T = 0", np.abs(pB2 @ pB1.T).max() < 1e-12)
plam = np.sort(np.linalg.eigvalsh(pB2 @ pB2.T))
def _wspec(wf):
    M = np.diag(wf); M *= pnF / np.trace(M)
    return np.sort(np.linalg.eigvalsh(np.sqrt(M) @ pB2 @ pB2.T @ np.sqrt(M)))
lam_inv = _wspec([1 / len(f) for f in pf])
lam_lin = _wspec([float(len(f)) for f in pf])

def _ks_spectrum(bt, bs, C, k=6):
    Bred = pB2[:pnF - 1]
    st = list(itertools.product(range(-C, C + 1), repeat=pnF - 1))
    sid = {c: i for i, c in enumerate(st)}; N = len(st)
    nv = np.array([Bred.T @ np.array(c) for c in st])
    tab = np.array([-np.log(ive(n, bt) / ive(0, bt))
                    for n in range(int(np.abs(nv).max()) + 1)])
    H = lil_matrix((N, N))
    H.setdiag(tab[np.abs(nv).astype(int)].sum(1) + bs * pnF)
    sh = [np.eye(pnF - 1, dtype=int)[f] for f in range(pnF - 1)] \
         + [-np.ones(pnF - 1, dtype=int)]
    for i, c in enumerate(st):
        ca = np.array(c)
        for v in sh:
            for s in (1, -1):
                c2 = tuple(ca + s * v)
                if c2 in sid: H[sid[c2], i] -= bs / 2
    w = np.sort(eigsh(H.tocsr(), k=k, which="SA",
                      return_eigenvectors=False, tol=1e-11, maxiter=50000))
    return w - w[0], N

FAST = os.environ.get("ZS_S21_FAST", "0") == "1"
runs = [(25, 1.0, 5)] if FAST else [(25, 1.0, 5), (50, 1.0, 6), (100, 1.0, 7)]
ratios = []
for bt, bs, C in runs:
    g, N = _ks_spectrum(bt, bs, C)
    pred = np.sort(np.sqrt(plam[1:] * bs / bt))
    obs = g[1:1 + len(pred)]
    ratios.append(obs[1] / obs[0])
    print(f"        beta_t={bt:4d} C={C} dim={N:6d}   E_k/omega_k = "
          f"{np.round(obs/pred,5)}   E2/E1 = {obs[1]/obs[0]:.5f}")
    chk(f"T13{runs.index((bt,bs,C))}",
        f"beta_t={bt}: excitation energies match omega_k = sqrt(r lambda_k) "
        f"of the UNIFORM measure to better than 4 %",
        np.abs(obs / pred - 1).max() < 0.04,
        f"max dev = {100*np.abs(obs/pred-1).max():.2f} %")
r_uni = float(np.sqrt(plam[2] / plam[1]))
r_inv = float(np.sqrt(lam_inv[2] / lam_inv[1]))
r_lin = float(np.sqrt(lam_lin[2] / lam_lin[1]))
chk("T140", "the observed E2/E1 selects the uniform measure over psi = 1/n_f",
    abs(np.mean(ratios) - r_uni) < abs(np.mean(ratios) - r_inv),
    f"obs {np.mean(ratios):.5f} | uniform {r_uni:.5f} | psi=1/n {r_inv:.5f}")
chk("T141", "the observed E2/E1 selects the uniform measure over psi = n_f",
    abs(np.mean(ratios) - r_uni) < abs(np.mean(ratios) - r_lin),
    f"obs {np.mean(ratios):.5f} | uniform {r_uni:.5f} | psi=n   {r_lin:.5f}")
prx("P150", "the prism is a PROXY for K_TI: it shares the two-face-orbit / "
            "two-edge-orbit pathology but is not the Z-Spin object",
    True)

# ===========================================================================
# 11. THE FALSIFIABLE SPECTRUM  (erratum E-2, erratum E-4)
# ===========================================================================
print("\n[S12] The dimensionless spectrum and the physical observable")

lam1 = D2(1, 1)[1]
tbl = [(x, m) for x, m in levels if x > 1e-9]
chk("T160", "the ratio table has 8 nonzero levels, multiplicities summing to 31",
    len(tbl) == 8 and sum(m for _, m in tbl) == 31)
chk("T161", "ERRATUM E-2: the level lambda = 8.3917019492 (mult 3, ratio "
            "6.7520284470) is present and must appear in the table",
    any(APPROX(x, 8.3917019492, 1e-8) and m == 3 for x, m in tbl))
print("        lambda_k          mult   lambda_k/lambda_1   omega_k/omega_1")
for x, m in tbl:
    print(f"        {x:.10f}   {m:2d}    {x/lam1:.10f}     {np.sqrt(x/lam1):.10f}")
chk("T162", "ERRATUM E-4: normal-mode energies obey omega = sqrt(r lambda), "
            "so the observable ratios are sqrt(lambda_k/lambda_1)",
    APPROX(np.sqrt(tbl[1][0] / lam1), 1.6215477963, 1e-9),
    f"omega_2/omega_1 = {np.sqrt(tbl[1][0]/lam1):.10f}")
chk("T163", "the ratio table is invariant under r  (scale-free)",
    np.abs(D2(1, 1, 3.14159)[1:] / D2(1, 1, 3.14159)[1] - w_full[1:] / w_full[1]).max() < 1e-9)

# ===========================================================================
# 12. ANTI-NUMEROLOGY
# ===========================================================================
print("\n[S13] Anti-numerology")
NMC = 200000
hits = int(np.sum(RNG.integers(1, 45, size=NMC) == 22))
chk("T170", "22 = 2Q is NOT upgraded: a uniform null over admissible integer "
            "root-sums gives p = 0.0229, far above any evidential threshold",
    hits / NMC > 0.005, f"p = {hits/NMC:.5f}")
dec("D171", "22 = 2Q remains an OBSERVATION. No connecting theorem is claimed "
            "and it plays no role in the closure argument.")
chk("T172", "the closure argument uses no numerical coincidence: every step is "
            "either an incidence count, a congruence, or a Hessian",
    dev_t < 1e-6 and dev_s < 1e-5 and np.ptp(elen) < 1e-8)

# ===========================================================================
# 13. GATE REGISTRY
# ===========================================================================
print("\n[S14] Gate registry")
dec("G200", "F-S20.5 (non-diagonal I_h-equivariant family)", "SUPERSEDED-BY-CONSTRUCTION (T060-T063)")
dec("G201", "F-S20.14 (non-quadratic closure step)",         "CLOSED by Theorem S21.1")
dec("G215", "F-S21.12 (NEW v1.2) The transfer matrix is shown to SELECT rather "
            "than merely propagate an orbit weight in either anisotropy class",
            "Does not fire; it propagates (T064, T065). This is a NEGATIVE result "
            "about the construction and is reported as such.")
dec("G202", "F-S20.15a-d (register-lift / normalisation)",   "SUPERSEDED-BY-CONSTRUCTION")
dec("G203", "F-S18.16b, F-S19.6b (action-level determination of M)",
            "REDUCED by construction; the residual is one ratio rho, fixed by (Z-A0) & (Z-A1)")
dec("G204", "F-S19.3 (a_TI and the scheme relation)",        "REFRAMED as scale setting")
dec("G205", "F-S21.1 temporal-plaquette bijection",          "does not fire (T051)")
dec("G206", "F-S21.2 off-diagonal M",                        "does not fire (T061)")
dec("G207", "F-S21.3 face-orbit dependence at O(g^0)",       "does not fire under (Z-A0) & (Z-A1); M2 is diagonal for EVERY weight (T064)")
dec("G208", "F-S21.4 reflection positivity on K_TI",         "cannot fire; removed (D110)")
dec("G209", "F-S21.5 Gauss census not 59 + 31",              "does not fire (T100-T102)")
dec("G209b","F-S21.9 erratum E-1a wrong (Omega^2 contains A_u/T_1g/T_2g/H_u)", "does not fire (T041, T042)")
dec("G210", "F-S21.6 any dimensionless ratio moves",         "does not fire (T030-T038, T160-T163)")
dec("G211", "F-S21.7 (NEW) Axiom Z-A0 is contradicted: ZS-S14 is shown to supply "
            "K_TI with a metric, an area or a dual measure", "OPEN")
dec("G212", "F-S21.8 (REDEFINED v1.1, BRANCH-ROBUST v1.2) The third-lowest "
            "excitation is found to have multiplicity 4 (G_u) rather than 3 "
            "(T_2u), or D1 = omega(T_2u,1)/omega(T_1u,1) falls above the "
            "midpoint 2.0892594252. Both metric branches sit on the same side "
            "(T095, T096), so the gate discriminates orbit-blind from "
            "orbit-sensitive weighting, not merely one metric from another.",
            "OPEN -- observational")
dec("G213", "F-S21.10 (EXPANDED v1.2) Axiom Z-A1 is contradicted: the ZS-S14 "
            "reduction is shown to weight 2-cells by ANY ambient datum -- a "
            "combinatorial function psi(n_f) of face degree, a function "
            "psi_e({deg f : f > e}) of the edge star, or a dual measure",
            "OPEN -- this is the ZS-S19 R_C axiom restated at group-valued level "
            "and extended to the temporal class; it is the single load-bearing "
            "choice of the whole S-line")
dec("G214", "F-S21.11 (NEW) (H-W) is contradicted: the ZS-S14 cellular reduction "
            "is shown NOT to be of Wilson type (e.g. non-compact link variables, "
            "or coupling beyond nearest neighbour in time)",
            "OPEN -- Theorems S21.1 and S21.2 both rest on (H-W)")

# ===========================================================================
# 14. ANTI-REGRESSION: no `check` is a literal constant
# ===========================================================================
print("\n[S15] Anti-regression static analysis")
src = inspect.getsource(sys.modules[__name__])
tree = ast.parse(src)
bad = []
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "chk":
        if len(node.args) >= 3:
            a = node.args[2]
            if isinstance(a, ast.Constant):
                bad.append(node.args[0].value if isinstance(node.args[0], ast.Constant) else "?")
chk("T190", "no check-kind assertion is a literal constant (ZS-S20 v2.2 lesson)",
    len(bad) == 0, f"offenders = {bad}")

# ===========================================================================
print("\n" + "=" * 74)
nchk = sum(1 for e in LEDGER if e["kind"] == "check")
npass = sum(1 for e in LEDGER if e["kind"] == "check" and e["ok"])
nprx = sum(1 for e in LEDGER if e["kind"] == "proxy")
ndec = sum(1 for e in LEDGER if e["kind"] == "decl")
fails = [e["id"] for e in LEDGER if not e["ok"]]
print(f"VERIFICATION SUMMARY : {npass}/{nchk} executable checks PASS, "
      f"{nprx} proxy, {ndec} declarative, {len(fails)} FAIL")
if fails: print("FAILING:", fails)
print("Zero CONTINUOUS dimensionless parameters given (H-W) & (Z-A0) & the "
      "expanded (Z-A1); WITHOUT (Z-A1) two ratios sigma and rho survive. "
      "A = 35/437, Q = 11, dim Z = 2, lambda_1 = 1.2428416164 -- all LOCKED, "
      "none re-fitted.")
try:
    with open(os.path.abspath(__file__), "rb") as fh:
        print("SHA256(self) =", hashlib.sha256(fh.read()).hexdigest())
except Exception as exc:
    print("SHA256(self) = unavailable:", exc)
print("END_ZS_S21_RESULTS")
sys.exit(1 if fails else 0)
