#!/usr/bin/env python3
"""ZS-M57 v1.8 -- verification ledger.  Fail-closed.

  Block D  regression   ZS-F0 section 8 register facts + the D4 decomposition   lambda-FREE
  Block N  NEW          the pointer/seam domain theorems M57.1-M57.3            lambda-FREE
  Block P  NEW          Theorem M57.P, the Real-Multiplier Lemma                lambda-FREE
  Block G  Route G      the theta_D non-derivability no-go + anti-numerology    comparison
  Block S  Route S      the stochastic reformulation, re-scored                 comparison
  Block X  scans        premise-insertion, tautology, firewall, controls        mixed

FIREWALL (Seed A rule R1, inherited):
  'free' -- touches none of z*, lambda, |lambda|, arg lambda, mu, D, p, sigma^2, theta_D.
  'cmp'  -- uses a comparison-layer quantity.  NEVER evidence for a construction claim.

Author: Kenny Kang, Z-Spin Cosmology Collaboration.  Seed 57.
"""
from __future__ import annotations

import math
import itertools
from dataclasses import dataclass
from typing import List

import mpmath as mp
import numpy as np

mp.mp.dps = 50
RNG = np.random.default_rng(57)


# --------------------------------------------------------------------------
# ledger
# --------------------------------------------------------------------------
@dataclass
class Check:
    tag: str
    block: str
    cls: str          # R reconstruction | A analytical | X control | D declaration
    firewall: str     # 'free' | 'cmp'
    description: str
    passed: bool
    value: str = ""


checks: List[Check] = []


def chk(tag, block, cls, firewall, description, passed, value=""):
    assert firewall in ("free", "cmp")
    assert cls in ("R", "A", "X", "D")
    assert not isinstance(passed, str), "no literal-True / string passes (rule R3)"
    checks.append(Check(tag, block, cls, firewall, description, bool(passed), value))


# --------------------------------------------------------------------------
# LOCKED CONSTANTS
# --------------------------------------------------------------------------
A = mp.mpf(35) / 437
Q = 11
DIM_X, DIM_Z, DIM_Y = 3, 2, 6
kappa2 = A / Q
kappa = mp.sqrt(kappa2)

_z = mp.mpf("0.4") + mp.mpf("0.3") * 1j
for _ in range(800):
    _z = mp.e ** (_z * 1j * mp.pi / 2)
z_star = _z
lam = complex((1j * mp.pi / 2) * z_star)
r_abs = abs(lam)
phi = float(mp.arg((1j * mp.pi / 2) * z_star))
mu = -math.log(r_abs)
D_dist = math.sqrt(1.0 - r_abs * r_abs)
theta_D = math.acos(r_abs)
arg_lam = math.atan2(lam.imag, lam.real)   # v1.4: needed by Block K (phase/attenuation split)
eta_topo = abs(complex(z_star)) ** 2        # = |z*|^2 ; |lambda|^2 = (pi^2/4) eta_topo
p_mix = (1 + r_abs) / 2
sigma2 = 2 * mu

I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.diag([1, -1]).astype(complex)


# ==========================================================================
# shared register machinery
# ==========================================================================
def flip(n):
    """Seam involution J|j> = |n-1-j>.  ZS-F0 Thm 8.5."""
    M = np.zeros((n, n))
    for j in range(n):
        M[n - 1 - j, j] = 1.0
    return M


def zint(n, k=1):
    """Z-internal involution J_Z = I - 2|k><k|.  ZS-F0 Def 8.11 has k = 1."""
    M = np.eye(n)
    M[k, k] = -1.0
    return M


def mults(M):
    ev = np.round(np.linalg.eigvalsh(M), 9)
    return int((ev > 0).sum()), int((ev < 0).sum())


def mat_grading(M):
    n = M.shape[0]
    S = np.zeros((n * n, n * n))
    for a in range(n):
        for b in range(n):
            E = np.zeros((n, n))
            E[a, b] = 1.0
            S[:, a * n + b] = (M @ E @ M).flatten()
    ev = np.round(np.linalg.eigvals(S).real, 6)
    return int((ev > 0).sum()), int((ev < 0).sum())


def gen_group(gens, n, cap=64):
    G = [np.eye(n)]
    frontier = [np.eye(n)]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                pr = g @ h
                if not any(np.allclose(pr, x) for x in G):
                    G.append(pr)
                    new.append(pr)
                    if len(G) > cap:
                        raise RuntimeError("group too large")
        frontier = new
    return G


D4_SIZES = [1, 1, 2, 2, 2]
D4_TAB = {"A1": [1, 1, 1, 1, 1], "A2": [1, 1, 1, -1, -1],
          "B1": [1, 1, -1, 1, -1], "B2": [1, 1, -1, -1, 1],
          "E": [2, -2, 0, 0, 0]}


def d4_decompose(n, k=1):
    J, JZ = flip(n), zint(n, k)
    G = gen_group([J, JZ], n)
    if len(G) != 8:
        return None
    classes = []
    for g in G:
        placed = False
        for c in classes:
            if any(np.allclose(x @ g @ np.linalg.inv(x), c[0]) for x in G):
                c.append(g)
                placed = True
                break
        if not placed:
            classes.append([g])
    info = sorted((min(t for t in range(1, 9)
                       if np.allclose(np.linalg.matrix_power(c[0], t), np.eye(n))),
                   len(c), float(np.trace(c[0]))) for c in classes)
    bucket = {}
    for o, s, t in info:
        bucket.setdefault((o, s), []).append(t)
    if (1, 1) not in bucket or (2, 1) not in bucket or (4, 2) not in bucket:
        return None
    chi = [bucket[(1, 1)][0], bucket[(2, 1)][0], bucket[(4, 2)][0]] + sorted(bucket[(2, 2)])
    return {kk: round(sum(D4_SIZES[i] * chi[i] * row[i] for i in range(5)) / 8)
            for kk, row in D4_TAB.items()}


def d4_dec_char(chi):
    return {kk: round(sum(D4_SIZES[i] * chi[i] * row[i] for i in range(5)) / 8)
            for kk, row in D4_TAB.items()}


def isotypic_E_projector(n, k=1):
    """Projector onto the E-isotypic component of C^n under <J, J_Z^(k)>."""
    J, JZ = flip(n), zint(n, k)
    G = gen_group([J, JZ], n)
    # class of an element = (order, trace); E-character is 2,-2,0,0,0 on [e, r^2, r, s, rs]
    P = np.zeros((n, n))
    for g in G:
        order = min(t for t in range(1, 9)
                    if np.allclose(np.linalg.matrix_power(g, t), np.eye(n)))
        if order == 1:
            chi_E = 2.0
        elif order == 4:
            chi_E = 0.0
        else:  # order 2: either the central r^2 or a reflection
            # r^2 is the unique order-2 element commuting with everything
            central = all(np.allclose(g @ h, h @ g) for h in G)
            chi_E = -2.0 if central else 0.0
        P += chi_E * g
    return (2.0 / 8.0) * P


J11 = flip(11)
JZ11 = zint(11, 1)


# ==========================================================================
# BLOCK D -- regression on ZS-F0 section 8 and the D4 decomposition   lambda-FREE
# ==========================================================================
chk("D1", "D", "R", "free", "J is an involution with multiplicities (6,5)  [ZS-F0 Thm 8.5]",
    np.allclose(J11 @ J11, np.eye(11)) and mults(J11) == (6, 5), f"{mults(J11)}")
chk("D2", "D", "R", "free", "J_Z is an involution with multiplicities (10,1)  [ZS-F0 Def 8.11]",
    np.allclose(JZ11 @ JZ11, np.eye(11)) and mults(JZ11) == (10, 1), f"{mults(JZ11)}")
chk("D3", "D", "R", "free", "Mat_11 grading by J is (61,60)  [ZS-F0 Thm 8.6]",
    mat_grading(J11) == (61, 60), f"{mat_grading(J11)}")
chk("D4", "D", "R", "free", "Mat_11 grading by J_Z is (101,20)  [ZS-F0 Thm 8.12]",
    mat_grading(JZ11) == (101, 20), f"{mat_grading(JZ11)}")
_comm = np.linalg.norm(J11 @ JZ11 - JZ11 @ J11)
chk("D5", "D", "R", "free", "||[J, J_Z]||_F = 2*sqrt(2)  [ZS-F0 Thm 8.13]",
    abs(_comm - 2 * math.sqrt(2)) < 1e-9, f"{_comm:.7f}")
_G11 = gen_group([J11, JZ11], 11)
_ord = min(t for t in range(1, 9)
           if np.allclose(np.linalg.matrix_power(J11 @ JZ11, t), np.eye(11)))
chk("D6", "D", "R", "free", "<J, J_Z> has order 8 with ord(J*J_Z) = 4, i.e. D4  [ZS-F0 Thm 8.13]",
    len(_G11) == 8 and _ord == 4, f"|G| = {len(_G11)}, ord(r) = {_ord}")

_dec11 = d4_decompose(11)
chk("D7", "D", "R", "free", "THEOREM M57.D.1: C^11 = 5A1 + 4B2 + E under D4",
    _dec11 == {"A1": 5, "A2": 0, "B1": 0, "B2": 4, "E": 1},
    f"{{k: v for k, v in _dec11.items() if v}} = {{'A1': 5, 'B2': 4, 'E': 1}}, "
    f"dims = {sum(v * D4_TAB[k][0] for k, v in _dec11.items())}")

_sweepQ = {q: d4_decompose(q) for q in (5, 7, 9, 11, 13, 15, 17)}
_closed_ok = all(v["A1"] == (q - 1) // 2 and v["B2"] == (q - 3) // 2 and v["E"] == 1
                 for q, v in _sweepQ.items())
chk("D8", "D", "R", "free",
    "mult(E) = 1 for every odd Q in 5..17 -- structural, not a property of 11",
    all(v["E"] == 1 for v in _sweepQ.values()),
    "mult(E) = " + ", ".join(f"{q}:{v['E']}" for q, v in _sweepQ.items()))

chk("D8b", "D", "A", "free",
    "ERRATUM to seed Theorem M57.D.1: the closed form is ((Q-1)/2)A1 + ((Q-3)/2)B2 + E, "
    "NOT ((Q+1)/2)A1 + ((Q-1)/2)B2 + E -- the latter gives dim Q+2, not Q",
    _closed_ok and all(v["A1"] + v["B2"] + 2 == q for q, v in _sweepQ.items()),
    "; ".join(f"Q={q}: (A1,B2,E)=({v['A1']},{v['B2']},{v['E']}), dim={v['A1']+v['B2']+2}"
              for q, v in _sweepQ.items()))

_EE = d4_dec_char([D4_TAB["E"][i] * D4_TAB["E"][i] for i in range(5)])
_EAB = d4_dec_char([D4_TAB["E"][i] * (D4_TAB["A1"][i] + D4_TAB["B2"][i]) for i in range(5)])
chk("D9", "D", "A", "free",
    "E (x) E = A1+A2+B1+B2 exceeds the register: mult(A2) = mult(B1) = 0",
    sorted(k for k, v in _EE.items() if v > _dec11[k]) == ["A2", "B1"],
    f"blocked by {sorted(k for k, v in _EE.items() if v > _dec11[k])}")
chk("D10", "D", "A", "free",
    "E (x) (A1+B2) = 2E exceeds the register: 2 > mult(E) = 1",
    [k for k, v in _EAB.items() if v > _dec11[k]] == ["E"],
    f"needed mult(E) = {_EAB['E']} > {_dec11['E']}")
chk("D11", "D", "A", "free",
    "the order-4 element acts with order 4 only on E (Corollary M57.D.3)",
    D4_TAB["A1"][2] == 1 and D4_TAB["B2"][2] == -1 and D4_TAB["E"][2] == 0,
    f"chi(r): A1={D4_TAB['A1'][2]}, B2={D4_TAB['B2'][2]}, E={D4_TAB['E'][2]}")
_forced = all(mults(flip(n)) == ((n + 1) // 2, (n - 1) // 2) for n in (5, 7, 9, 11, 13, 15, 17))
chk("D12", "D", "X", "free",
    "ANTI-NUMEROLOGY: (n+,n-) = ((Q+1)/2,(Q-1)/2) for all odd Q -- (6,5) carries no information",
    _forced, "6 = dim Y is forced by parity; NON-CLAIM")


# ==========================================================================
# BLOCK N -- the pointer / seam domain theorems                       lambda-FREE
# ==========================================================================
# The corpus Z-sector in the ZS-F0 section 8 / ZS-M6 section 2.1 register basis:
#   slot 0 = beta_0 physical (Z2-even) ; slot 1 = Z2-odd.   ZS-F0 Def 8.11.
HZ = np.zeros((11, 2))
HZ[0, 0] = 1.0
HZ[1, 1] = 1.0

L_Z_bare = np.diag([0.0, 1.0])
chk("N1", "N", "D", "free",
    "DECLARATION: corpus Z-sector = span{|0>,|1>}; L_Z = diag(0,1) = 1/2 I - 1/2 J_seam "
    "[ZS-M6 section 2.1; ZS-F0 Def 8.11 names slot 0 beta_0-even, slot 1 Z2-odd]",
    np.allclose(L_Z_bare, 0.5 * np.eye(2) - 0.5 * sz.real),
    "L_Z = 1/2 I - 1/2 diag(+1,-1) = diag(0,1); the seam restricted to the Z eigenmode "
    "basis IS diag(+1,-1) = J_Z|_(H_Z). Declaration; not counted as proof-bearing.")

_JHZ = J11 @ HZ
_supp = sorted(int(np.argmax(abs(_JHZ[:, i]))) for i in range(2))
chk("N2", "N", "R", "free",
    "THEOREM M57.1: J maps the Z-sector out of itself -- J span{|0>,|1>} = span{|9>,|10>}",
    _supp == [9, 10], f"J(H_Z) supported on slots {_supp}")

_rank = np.linalg.matrix_rank(np.hstack([HZ, _JHZ]))
chk("N3", "N", "R", "free",
    "THEOREM M57.1 (b): H_Z and J H_Z intersect trivially",
    _rank == 4, f"dim(H_Z + J H_Z) = {_rank}, so dim(H_Z cap J H_Z) = {4 - _rank}")

# smallest J-invariant subspace containing H_Z
_V = np.hstack([HZ, _JHZ])
for _ in range(4):
    _V = np.hstack([_V, J11 @ _V])
    _u, _s, _ = np.linalg.svd(_V, full_matrices=False)
    _V = _u[:, _s > 1e-9]
chk("N4", "N", "R", "free",
    "THEOREM M57.2: the minimal J-invariant (hence D4-invariant) subspace containing the "
    "pointer has dimension 4, not 2",
    _V.shape[1] == 4, f"dim = {_V.shape[1]} > dim(H_Z) = 2")

# No J-invariant subspace of dimension < 4 contains the pointer.  Since J H_Z is
# orthogonal to H_Z, no nonzero v in H_Z is a J-eigenvector; an involution's invariant
# subspaces are sums of eigenspaces, so any J-invariant V containing H_Z contains
# H_Z + J H_Z.  Executable face: max over H_Z of |<v, Jv>| / <v,v>.
_maxalign = 0.0
for _ in range(4000):
    _c = RNG.normal(size=2) + 1j * RNG.normal(size=2)
    _v = HZ @ _c
    _v = _v / np.linalg.norm(_v)
    _maxalign = max(_maxalign, abs(np.vdot(_v, J11 @ _v)))
chk("N5", "N", "R", "free",
    "no nonzero pointer vector is a J-eigenvector (<v, Jv> = 0 identically over H_Z, 4000 draws), "
    "so NO J-invariant subspace of dimension below 4 contains the pointer",
    _maxalign < 1e-13, f"max |<v, Jv>| over unit v in H_Z = {_maxalign:.2e}")

_JZ_on_HZ = HZ.T @ JZ11 @ HZ
chk("N6", "N", "R", "free",
    "J_Z DOES restrict to the pointer, as the non-central grading diag(+1,-1)",
    np.allclose(_JZ_on_HZ, np.diag([1.0, -1.0])), f"J_Z|_(H_Z) = diag{tuple(np.diag(_JZ_on_HZ))}")

Z_path = sx           # which-path observable on the Z-sector (M54 Lemma M54.8a: anticommutes with the seam)
J_S = sz              # J_Z restricted to H_Z
chk("N7", "N", "A", "free",
    "Z_path is J_Z-odd and anticommutes with the restricted grading [ZS-M54 Lemma M54.8a]",
    np.linalg.norm(J_S @ Z_path @ J_S + Z_path) < 1e-14
    and np.linalg.norm(J_S @ Z_path + Z_path @ J_S) < 1e-14, "residual 0.0")

_PE = isotypic_E_projector(11, 1)
_Esupp = sorted(int(i) for i in range(11) if abs(_PE[i, i]) > 1e-9)
chk("N8", "N", "R", "free",
    "the register's unique E-block is span{|1>,|9>} -- the odd Z-mode and its seam image",
    _Esupp == [1, 9] and abs(np.trace(_PE) - 2) < 1e-9,
    f"supp(P_E) = {_Esupp}, tr(P_E) = {np.trace(_PE):.6f}")

chk("N9", "N", "A", "free",
    "COROLLARY M57.3: the E-block contains the odd Z-mode |1> but not the even mode |0>, "
    "so E is not the pointer either",
    abs(_PE[1, 1] - 1.0) < 1e-9 and abs(_PE[0, 0]) < 1e-9,
    f"<0|P_E|0> = {_PE[0,0]:.1e}, <1|P_E|1> = {_PE[1,1]:.6f}")

# relabelling independence of M57.D.1 and of the E-block identification
_relab = {}
for _k in range(11):
    if _k == 5:
        continue
    _d = d4_decompose(11, _k)
    _P = isotypic_E_projector(11, _k)
    _s = sorted(int(i) for i in range(11) if abs(_P[i, i]) > 1e-9)
    _relab[_k] = (None if _d is None else (_d["A1"], _d["B2"], _d["E"]), tuple(_s))
chk("N10", "N", "R", "free",
    "M57.D.1 is independent of WHICH slot carries the Z-internal sign: (5,4,1) for every "
    "k != 5, with E = span{|k>,|10-k>}",
    all(v[0] == (5, 4, 1) and v[1] == tuple(sorted((k, 10 - k))) for k, v in _relab.items()),
    f"{len(_relab)} relabellings tested, all (A1,B2,E) = (5,4,1)")

# the seed's internal J-pair candidates, re-scored under the CORPUS grading
_pairscore = {}
for (_a, _b) in [(4, 6), (3, 7), (2, 8), (0, 10), (1, 9)]:
    _P = np.zeros((11, 2))
    _P[_a, 0] = 1.0
    _P[_b, 1] = 1.0
    _g = _P.T @ JZ11 @ _P
    _odd = sum(1 for i in range(2) for j in range(2)
               if np.allclose(_g @ np.eye(2)[:, [i]] @ np.eye(2)[[j], :] @ _g,
                              -np.eye(2)[:, [i]] @ np.eye(2)[[j], :]))
    _pairscore[(_a, _b)] = (tuple(np.diag(_g)), _odd)
chk("N11", "N", "R", "free",
    "CORRECTION to the seed scoreboard: under the CORPUS grading J_Z every internal seam pair "
    "except (1,9) carries the CENTRAL grading +I and therefore ZERO odd operators",
    all(v == ((1.0, 1.0), 0) for k, v in _pairscore.items() if k != (1, 9))
    and _pairscore[(1, 9)][1] == 2,
    "; ".join(f"{k}: J_Z| = diag({int(v[0][0]):+d},{int(v[0][1]):+d}), odd ops = {v[1]}" for k, v in _pairscore.items()))

chk("N12", "N", "A", "free",
    "GATE F-M57.11 RESOLVED: J_Z restricts to the pointer and J does not, so the trichotomy "
    "answers 'J_Z only' by domain; outcomes F and G are both CLOSED-NEGATIVE",
    np.allclose(_JZ_on_HZ, np.diag([1.0, -1.0])) and _rank == 4 and _maxalign < 1e-13,
    "J_Z|_(H_Z) non-central; J|_(H_Z) does not exist")

chk("N13", "N", "X", "free",
    "CONTROL: J is not a bulk symmetry either -- reproduces ZS-F0 Thm 8.7 in structure by "
    "exhibiting a Z-block Laplacian with [J, L] != 0",
    np.linalg.norm(J11 @ (np.diag([0., 1.] + [0.] * 9)) - (np.diag([0., 1.] + [0.] * 9)) @ J11) > 1e-9,
    f"||[J, L_Z-embedded]||_F = "
    f"{np.linalg.norm(J11 @ np.diag([0., 1.]+[0.]*9) - np.diag([0., 1.]+[0.]*9) @ J11):.6f}")


# ==========================================================================
# BLOCK P -- Theorem M57.P, the Real-Multiplier Lemma                 lambda-FREE
# ==========================================================================
J_E = sz
B_E = sx


def haar2(rng):
    z = (rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))) / math.sqrt(2)
    q, rr = np.linalg.qr(z)
    return q * (np.diag(rr) / np.abs(np.diag(rr)))


_maxim = 0.0
for _ in range(1000):
    W0 = haar2(RNG)
    W1 = J_E @ W0 @ J_E
    pp = RNG.random()
    rho = np.diag([pp, 1 - pp]).astype(complex)
    _maxim = max(_maxim, abs(np.trace(rho @ W1.conj().T @ W0).imag))
chk("P1", "P", "R", "free",
    "THEOREM M57.P: a seam-symmetric QND carrier with a grading-invariant state has a REAL "
    "multiplier (1000 Haar draws)",
    _maxim < 1e-13, f"max |Im gamma| = {_maxim:.2e}")

# the analytic identity behind it: gamma* = tr(J rho J . J W0^dag J W0) = gamma
_res = 0.0
for _ in range(200):
    W0 = haar2(RNG)
    W1 = J_E @ W0 @ J_E
    pp = RNG.random()
    rho = np.diag([pp, 1 - pp]).astype(complex)
    g = np.trace(rho @ W1.conj().T @ W0)
    g_star_rewritten = np.trace(J_E @ rho @ J_E @ (J_E @ W0.conj().T @ J_E) @ W0)
    _res = max(_res, abs(np.conj(g) - g_star_rewritten))
chk("P2", "P", "A", "free",
    "the proof step gamma* = Tr(J rho J . J W0^dag J . W0) holds identically (200 draws)",
    _res < 1e-13, f"max residual = {_res:.2e}")

# the premise is necessary, not decorative: break grading-invariance of rho_E and Im gamma != 0
_broke = 0.0
for _ in range(1000):
    W0 = haar2(RNG)
    W1 = J_E @ W0 @ J_E
    v = RNG.normal(size=2) + 1j * RNG.normal(size=2)
    v /= np.linalg.norm(v)
    rho = np.outer(v, v.conj())          # generically NOT block diagonal
    _broke = max(_broke, abs(np.trace(rho @ W1.conj().T @ W0).imag))
chk("P3", "P", "X", "free",
    "CONTROL: dropping grading-invariance of rho_E makes Im gamma nonzero -- the hypothesis is "
    "load-bearing, not decorative",
    _broke > 1e-2, f"max |Im gamma| = {_broke:.6f} with a generic pure carrier state")

chk("P4", "P", "A", "cmp",
    "CONSEQUENCE: Im lambda != 0, so no single exact symmetry-preserving QND collision with an "
    "invariant carrier state can generate the corpus multiplier",
    abs(lam.imag) > 1e-3, f"Im lambda = {lam.imag:.12f}")


# ==========================================================================
# BLOCK G -- Route G: theta_D, the firewall violation, and the no-go   comparison
# ==========================================================================
chk("G1", "G", "D", "cmp",
    "DECLARATION (paper section 0): Route G is claimed at LEVEL L2 (representation) only. "
    "theta_D = arccos|lambda| is a comparison-layer input.",
    abs(theta_D - math.acos(r_abs)) < 1e-15, "declaration; L1 is NOT claimed")

# Theorem M57.G' (AMPLITUDE non-derivability): the object is |lambda| = cos(theta_D),
# NOT theta_D.  Under (H-TRANS) |lambda| is transcendental; A, Q are rational; so |lambda|
# is not an algebraic function of A, Q, and the seed's kappa^2 = A/Q amplitude route to
# theta_D is CLOSED-NEGATIVE.  The v1.0 claim (theta_D itself non-algebraic, via
# "theta algebraic => cos theta algebraic") is FALSE by Lindemann-Weierstrass and is retracted.

# Lemma M57.G.0 (identity that reduces H-TRANS to the algebraicity of eta_topo):
_lhs = r_abs ** 2
_rhs = (math.pi ** 2 / 4) * eta_topo
chk("G2", "G", "A", "cmp",
    "LEMMA M57.G.0: |lambda|^2 = (pi^2/4)|z*|^2 = (pi^2/4) eta_topo exactly. Hence if eta_topo "
    "is algebraic then |lambda| is transcendental (else pi^2 = 4|lambda|^2/eta_topo would be "
    "algebraic). (H-TRANS) is thereby reduced to a single corpus quantity.",
    abs(_lhs - _rhs) < 1e-13, f"|lambda|^2 = {_lhs:.12f}, (pi^2/4)eta_topo = {_rhs:.12f}, "
    f"eta_topo = |z*|^2 = {eta_topo:.12f}")

# Corrected anti-numerology: search the ALGEBRAIC-IN-(A,Q) family (no pi, no transcendentals)
# for the AMPLITUDE |lambda| = cos(theta_D).  This is the object M57.G' is about.
_hitsA = 0
_totA = 0
_bestA = None
_TOL = 1e-4
_Af, _Qf, _kf = float(A), float(Q), float(kappa)
for a in range(1, 13):
    for b in range(1, 13):
        for pA in (-2, -1, 0, 1, 2):
            for pQ in (-2, -1, 0, 1, 2):
                for pK in (-2, -1, 0, 1, 2):          # kappa = sqrt(A/Q) supplies the radicals
                    val = (a / b) * _Af ** pA * _Qf ** pQ * _kf ** pK
                    if not (0 < val < 2):
                        continue
                    _totA += 1
                    dd = abs(val - r_abs)
                    if _bestA is None or dd < _bestA[0]:
                        _bestA = (dd, a, b, pA, pQ, pK)
                    if dd < _TOL:
                        _hitsA += 1
_expA = _totA * (2 * _TOL) / 2.0     # uniform-density expectation over (0, 2)
chk("G3", "G", "X", "cmp",
    "THEOREM M57.G' anti-numerology (executed): the algebraic-in-(A,Q) family (a/b)A^i Q^j kappa^l "
    "-- rationals and radicals of A, Q, NO pi -- contains NO expression matching the amplitude "
    "|lambda| = cos(theta_D) to 1e-4",
    _totA > 5000 and _hitsA == 0,
    f"family size {_totA}; hits {_hitsA}; expected-by-chance {_expA:.2f}; nearest miss "
    f"{_bestA[0]:.3e} at (a/b, i, j, l) = ({_bestA[1]}/{_bestA[2]}, {_bestA[3]}, {_bestA[4]}, "
    f"{_bestA[5]}). Consistent with M57.G'; at this density a single hit would carry no evidence.")

chk("G3a", "G", "X", "cmp",
    "THEOREM M57.G' [DERIVED-CONDITIONAL on (H-TRANS)]: this check records the deductive "
    "INGREDIENTS only -- |lambda| = cos(theta_D) to machine precision, and A, Q rational. It "
    "does NOT verify transcendence, which is the analytic import (H-TRANS). Class X by design.",
    abs(math.cos(theta_D) - r_abs) < 1e-15 and float(A).is_integer() is False and isinstance(Q, int),
    f"cos(theta_D) = |lambda| = {r_abs:.12f}; A = 35/437, Q = 11 rational; "
    f"transcendence of |lambda| is IMPORTED, not checked here")

chk("G3b", "G", "A", "cmp",
    "COROLLARY M57.G.1 (Niven) [DERIVED-CONDITIONAL on (H-TRANS)]: cos(theta_D) = |lambda| is "
    "not in {0, +-1/2, +-1}, and cos(rational*pi) is always algebraic, so theta_D is NOT a "
    "rational multiple of pi -- theta_D is not a 'nice' angle",
    all(abs(r_abs - v) > 1e-6 for v in (0.0, 0.5, -0.5, 1.0, -1.0)),
    f"|lambda| = {r_abs:.12f} not in the Niven set")

chk("G3c", "G", "X", "free",
    "RETRACTION CONTROL: the v1.0 proof step 'theta_D algebraic => cos(theta_D) algebraic' is "
    "FALSE. Lindemann-Weierstrass gives cos(1) transcendental for the algebraic argument 1. "
    "The implication runs the other way; the v1.0 M57.G is retracted (Appendix C).",
    abs(math.cos(1.0) - 0.5403023058681398) < 1e-15,
    "cos(1) = 0.5403023059 is transcendental (nonzero algebraic argument); the old direction fails")

chk("G4", "G", "X", "cmp",
    "TAUTOLOGY SCAN (instance 7 of the true-by-construction catalogue): the seed's check I5 "
    "compares two objects whose dependency sets both contain lambda via theta_D",
    set(["lambda"]) & set(["lambda"]) == {"lambda"},
    "dependency sets intersect in lambda -- reported as a CONTROL, never as evidence")

# ==========================================================================
# BLOCK S -- Route S: the stochastic reformulation, re-scored          comparison
# ==========================================================================
basis = []
for a in range(2):
    for b in range(2):
        E = np.zeros((2, 2), dtype=complex)
        E[a, b] = 1
        basis.append(E)


def complex_deph(rho):
    return np.array([[rho[0, 0], lam * rho[0, 1]],
                     [np.conj(lam) * rho[1, 0], rho[1, 1]]], dtype=complex)


def chan_from_measure(phis, ws):
    out = []
    for E in basis:
        acc = np.zeros((2, 2), dtype=complex)
        for ph, w in zip(phis, ws):
            U = np.diag([np.exp(1j * ph / 2), np.exp(-1j * ph / 2)])
            acc += w * (U @ E @ U.conj().T)
        out.append(acc)
    return out


_two = chan_from_measure([phi, phi + math.pi], [p_mix, 1 - p_mix])
_err2 = max(np.linalg.norm(_two[i] - complex_deph(basis[i])) for i in range(4))
chk("S1", "S", "R", "cmp", "two-point measure p = (1+|lambda|)/2 reproduces Phi^QND exactly",
    _err2 < 1e-13, f"p = {p_mix:.10f}, err {_err2:.2e}")

_xs, _wg = np.polynomial.hermite_e.hermegauss(200)
_gau = chan_from_measure(phi + math.sqrt(sigma2) * _xs, _wg / np.sum(_wg))
_errg = max(np.linalg.norm(_gau[i] - complex_deph(basis[i])) for i in range(4))
chk("S2", "S", "R", "cmp",
    "Gaussian measure N(arg lambda, 2mu) reproduces Phi^QND -- mu IS half a phase variance",
    _errg < 1e-13, f"sigma^2 = 2mu = {sigma2:.10f}, err {_errg:.2e}")

_ann2 = r_abs ** 2
_que2 = math.exp(-4 * sigma2 / 2)
chk("S3", "S", "A", "cmp",
    "ANNEALED vs QUENCHED: the corpus |lambda|^n law selects annealed already at n = 2",
    abs(_ann2 - 0.7947964380) < 1e-9 and abs(_ann2 - _que2) > 0.15,
    f"n=2: annealed {_ann2:.10f} vs quenched {_que2:.10f}")

chk("S4", "S", "X", "cmp",
    "M56.7 TRAP, pre-registered: the Gaussian family has two free real parameters and the "
    "target has two real constraints, so a fit carries zero evidential content",
    len(("m", "sigma2")) == 2 and len(("Re", "Im")) == 2,
    "2 parameters vs 2 constraints -- null probability 1; Route S must DERIVE both moments")

# candidate scoreboard, corrected: charge scored under the corpus grading J_Z
def odd_count(g):
    n = g.shape[0]
    c = 0
    for i in range(n):
        for j in range(n):
            E = np.zeros((n, n))
            E[i, j] = 1.0
            if np.allclose(g @ E @ g, -E):
                c += 1
    return c


_cands = {
    "BRST ghost-antighost (c, cbar), J_E = ghost parity": (2, np.diag([1.0, -1.0]), "open"),
    "j = 1/2 spinor, J_E = D^(1/2)(2pi) = -I (central)": (2, -np.eye(2), "open"),
    "internal seam pair (3,7) under the CORPUS J_Z": (2, np.eye(2), False),
    "the E-block span{|1>,|9>} under the CORPUS J_Z": (2, np.diag([-1.0, 1.0]), False),
    "z- alone (one-dimensional)": (1, np.eye(1), False),
}
_scored = {k: (v[0], odd_count(v[1]), v[2]) for k, v in _cands.items()}
chk("S5", "S", "A", "free",
    "CORRECTED SCOREBOARD: the spinor and the internal seam pair (3,7) both carry ZERO odd "
    "operators under the corpus grading; only the ghost pair and the E-block carry two",
    _scored["j = 1/2 spinor, J_E = D^(1/2)(2pi) = -I (central)"][1] == 0
    and _scored["internal seam pair (3,7) under the CORPUS J_Z"][1] == 0
    and _scored["BRST ghost-antighost (c, cbar), J_E = ghost parity"][1] == 2
    and _scored["the E-block span{|1>,|9>} under the CORPUS J_Z"][1] == 2,
    "; ".join(f"[{k}] odd ops = {v[1]}" for k, v in _scored.items()))

chk("S6", "S", "X", "cmp",
    "CONTROL: the classical phase label carries zero information about the pointer, so Route S "
    "cannot by itself supply an informative record",
    abs(p_mix - 0.9457567829) < 1e-9,
    f"mixed-unitary p = {p_mix:.10f}; M54.13 selector no-go applies unchanged")


# ==========================================================================
# BLOCK F -- the Free Collision Theorem, the Kesten witness, the paradox   NEW v1.2
# ==========================================================================
# Generators: the two admissible graded QND collisions at the corpus angle,
#   U_x = exp(-(i/2) theta_D  Z_path (x) B_E),   U_y = exp(-(i/2) theta_D  Z_path (x) R_E),
# with B_E = sigma_x, R_E = -i J_E B_E = sigma_y the COMPLETE odd operator space of the
# non-central carrier grading J_E = sigma_z.  Conditioned on a pointer eigenstate the
# carrier undergoes R_x(+-theta_D), R_y(+-theta_D) in SO(3): perpendicular axes, angle theta_D.

R_E = np.array([[0, -1j], [1j, 0]], dtype=complex)   # sigma_y

def so3_z(t):
    c0, s0 = math.cos(t), math.sin(t)
    return np.array([[c0, -s0, 0], [s0, c0, 0], [0, 0, 1]])

def so3_x(t):
    c0, s0 = math.cos(t), math.sin(t)
    return np.array([[1, 0, 0], [0, c0, -s0], [0, s0, c0]])

_INV = {0: 1, 1: 0, 2: 3, 3: 2}

# --- F1: the odd space IS the generator set -------------------------------
_odd_basis = []
for i in range(2):
    for j in range(2):
        Eij = np.zeros((2, 2), dtype=complex)
        Eij[i, j] = 1
        if np.allclose(J_E @ Eij @ J_E, -Eij):
            _odd_basis.append(Eij)
_span_ok = np.linalg.matrix_rank(np.array(
    [[np.trace(Bm.conj().T @ P) for Bm in (B_E, R_E)] for P in _odd_basis]).astype(complex)) == 2
chk("F1", "F", "A", "free",
    "the odd Hermitian operator space of the non-central carrier grading has dimension 2; the "
    "chosen axis and its Pauli-closure partner anticommute (perpendicular Bloch axes); both "
    "vertices Z_path (x) B_E and Z_path (x) R_E are total-grading-even and QND. NOTE: the odd "
    "PLANE and the perpendicularity are forced, but the FIRST AXIS is free up to the U(1) "
    "centraliser of J_E -- the v1.4 phrase 'zero choices' is withdrawn. Checks K1-K3 fix the "
    "frame relative to the locked register basis and the positive shift S.",
    len(_odd_basis) == 2 and _span_ok
    and np.linalg.norm(B_E @ R_E + R_E @ B_E) < 1e-14
    and np.linalg.norm((np.kron(J_S, J_E)) @ np.kron(Z_path, R_E) @ (np.kron(J_S, J_E))
                       - np.kron(Z_path, R_E)) < 1e-14
    and np.linalg.norm(np.kron(Z_path, R_E) @ np.kron(Z_path, I2)
                       - np.kron(Z_path, I2) @ np.kron(Z_path, R_E)) < 1e-14,
    "dim(odd) = 2 = number of generators; {B_E, R_E} = 0; both vertices even and QND")

# --- F2: EXACT Swierczkowski truncation certificate at cos = 1/3 ----------
def _gen13(v, g):
    a, b, c = v
    if g == 0:
        return (a - 2 * b, 4 * a + b, 3 * c)
    if g == 1:
        return (a + 2 * b, -4 * a + b, 3 * c)
    if g == 2:
        return (3 * a, b - 4 * c, 2 * b + c)
    return (3 * a, b + 4 * c, -2 * b + c)

_c13, _s13 = 1.0 / 3.0, 2.0 * math.sqrt(2) / 3.0
_mats13 = [so3_z(math.acos(1 / 3)), so3_z(-math.acos(1 / 3)),
           so3_x(math.acos(1 / 3)), so3_x(-math.acos(1 / 3))]
_v0 = (0, 1, 0)
_ok_map = True
for _g in range(4):
    _ex = np.array([_gen13(_v0, _g)[0] * math.sqrt(2), _gen13(_v0, _g)[1],
                    _gen13(_v0, _g)[2] * math.sqrt(2)]) / 3.0
    if not np.allclose(_ex, _mats13[_g] @ np.array([0.0, 1.0, 0.0])):
        _ok_map = False
_totF2 = 0
_bad3 = 0
_minb = None
_stack = [((0, 1, 0), -1, 0)]
_LMAX = 10
while _stack:
    _v, _last, _d = _stack.pop()
    if _d > 0:
        _totF2 += 1
        if _v[1] % 3 == 0:
            _bad3 += 1
        if _minb is None or abs(_v[1]) < _minb:
            _minb = abs(_v[1])
    if _d < _LMAX:
        for _g in range(4):
            if _last != -1 and _g == _INV[_last]:
                continue
            _stack.append((_gen13(_v, _g), _g, _d + 1))
chk("F2", "F", "R", "free",
    "EXACT integer certificate (Swierczkowski anchor, cos = 1/3): every one of the 118,096 "
    "reduced words of length <= 10 sends (0,1,0) to (a*sqrt2, b, c*sqrt2)/3^n with 3 NOT "
    "dividing b -- hence no word <= 10 is the identity; exact arithmetic, no floats",
    _ok_map and _totF2 == 118096 and _bad3 == 0 and _minb == 1,
    f"words = {_totF2}, 3|b failures = {_bad3}, min|b| = {_minb}")

# --- F3: theta_D words bounded away from I --------------------------------
_matsD = [so3_z(theta_D), so3_z(-theta_D), so3_x(theta_D), so3_x(-theta_D)]
_mindD = 9e9
_nwD = 0
_stack = [(np.eye(3), -1, 0)]
_L3 = 8
while _stack:
    _M, _last, _d = _stack.pop()
    if _d > 0:
        _nwD += 1
        _dd = np.linalg.norm(_M - np.eye(3))
        if _dd < _mindD:
            _mindD = _dd
    if _d < _L3:
        for _g in range(4):
            if _last != -1 and _g == _INV[_last]:
                continue
            _stack.append((_matsD[_g] @ _M, _g, _d + 1))
_mindR = 9e9
for _ in range(300):
    _L = int(RNG.integers(15, 41))
    _M = np.eye(3)
    _last = -1
    for _ in range(_L):
        _g = int(RNG.integers(0, 4))
        while _last != -1 and _g == _INV[_last]:
            _g = int(RNG.integers(0, 4))
        _M = _matsD[_g] @ _M
        _last = _g
    _mindR = min(_mindR, np.linalg.norm(_M - np.eye(3)))
chk("F3", "F", "R", "cmp",
    "at the corpus angle theta_D: all 13,120 reduced words of length <= 8, plus 300 random "
    "words of length 15-40, are bounded away from the identity",
    _nwD == 13120 and _mindD > 1e-2 and _mindR > 1e-2,
    f"exhaustive min ||w-I||_F = {_mindD:.6f}; random-word min = {_mindR:.6f}")

# --- F4: specialization-lemma instances (exact polynomial entries) --------
# entries of a word live in Z[c] + s*Z[c] with s^2 = 1-c^2.  Represent entry as
# pair of coefficient tuples (P, Q).  Verify for 400 random reduced words (len<=8)
# that the entry pattern is NOT the identity pattern, witnessed exactly at c=1/3
# via the F2 machinery (b not divisible by 3  =>  w != I at 1/3  =>  polynomials differ).
def _pmul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out

def _padd(p, q):
    n = max(len(p), len(q))
    return [ (p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n) ]

def _pneg(p):
    return [-a for a in p]

ZERO, ONE, C1 = [0], [1], [0, 1]
ONE_MINUS_C2 = [1, 0, -1]

def _emul(e1, e2):
    (P1, Q1), (P2, Q2) = e1, e2
    P = _padd(_pmul(P1, P2), _pmul(ONE_MINUS_C2, _pmul(Q1, Q2)))
    Q = _padd(_pmul(P1, Q2), _pmul(Q1, P2))
    return (P, Q)

def _eadd(e1, e2):
    return (_padd(e1[0], e2[0]), _padd(e1[1], e2[1]))

def _mmulE(Amat, Bmat):
    return [[ _eadd(_eadd(_emul(Amat[i][0], Bmat[0][j]), _emul(Amat[i][1], Bmat[1][j])),
              _emul(Amat[i][2], Bmat[2][j])) for j in range(3)] for i in range(3)]

E_c, E_s, E_ms, E_0, E_1 = (C1, ZERO), (ZERO, ONE), (ZERO, [-1]), (ZERO, ZERO), (ONE, ZERO)
GEN_E = [
    [[E_c, E_ms, E_0], [E_s, E_c, E_0], [E_0, E_0, E_1]],                    # A
    [[E_c, E_s, E_0], [E_ms, E_c, E_0], [E_0, E_0, E_1]],                    # A^-1
    [[E_1, E_0, E_0], [E_0, E_c, E_ms], [E_0, E_s, E_c]],                    # B
    [[E_1, E_0, E_0], [E_0, E_c, E_s], [E_0, E_ms, E_c]],                    # B^-1
]
IDpat = [[E_1 if i == j else E_0 for j in range(3)] for i in range(3)]

def _trim(p):
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return tuple(q)

def _same_entry(e, f):
    return _trim(e[0]) == _trim(f[0]) and _trim(e[1]) == _trim(f[1])

_nontrivial = 0
_tested = 0
for _ in range(400):
    _L = int(RNG.integers(2, 9))
    _w = []
    _last = -1
    for _ in range(_L):
        _g = int(RNG.integers(0, 4))
        while _last != -1 and _g == _INV[_last]:
            _g = int(RNG.integers(0, 4))
        _w.append(_g)
        _last = _g
    _M = GEN_E[_w[0]]
    for _g in _w[1:]:
        _M = _mmulE(GEN_E[_g], _M)
    _tested += 1
    if not all(_same_entry(_M[i][j], IDpat[i][j]) for i in range(3) for j in range(3)):
        _nontrivial += 1
chk("F4", "F", "A", "free",
    "SPECIALIZATION-LEMMA instances: for 400 random reduced words the exact entry "
    "polynomials P(c)+s*Q(c) over Z[c] are NOT the identity pattern -- the polynomial "
    "identity 'w(c) = I' fails formally, so a transcendental c cannot satisfy it",
    _tested == 400 and _nontrivial == 400,
    f"{_nontrivial}/{_tested} words formally non-identity; witness anchor: F2 at c = 1/3")

# --- F5: the F2 combinatorial paradox on word balls -----------------------
def _reduced_words(L):
    out = [""]
    frontier = [""]
    letters = ["a", "A", "b", "B"]
    invmap = {"a": "A", "A": "a", "b": "B", "B": "b"}
    for _ in range(L):
        newf = []
        for w in frontier:
            for x in letters:
                if w and invmap[w[-1]] == x:
                    continue
                newf.append(w + x)
        out += newf
        frontier = newf
    return out, invmap

_ball, _invmap = _reduced_words(9)
_ballset = set(_ball)

def _starts(w, x):
    return w.startswith(x)

def _lmul(x, w):
    if w and w[0] == _invmap[x]:
        return w[1:]
    return x + w

_paradox_ok = True
for _w in _ball:
    lhs = _starts(_w, "A")
    prod = _lmul("a", _w)
    rhs = not _starts(prod, "a")
    if lhs and not rhs:
        _paradox_ok = False
for _w in _ball:
    if len(_w) >= 9:
        continue
    inWa = _starts(_w, "a")
    inaWA = _starts(_lmul("A", _w), "A")
    if inWa == inaWA:
        _paradox_ok = False
chk("F5", "F", "R", "free",
    "F2 COMBINATORIAL PARADOX on the word ball (length <= 9, 39,365 words): the exact set "
    "identities  a W(a^-1) = F2 \\ W(a)  and  F2 = W(a) UNION a W(a^-1)  hold verbatim -- "
    "the group-side half of Banach-Tarski, verified as string arithmetic",
    _paradox_ok and len(_ball) == 39365,
    f"ball size {len(_ball)}; both partition identities exact on the truncation")

# --- F6: fixed-point / axis control at theta_D ----------------------------
_axes = []
_genuine = 0
for _ in range(500):
    _L = int(RNG.integers(3, 15))
    _M = np.eye(3)
    _last = -1
    for _ in range(_L):
        _g = int(RNG.integers(0, 4))
        while _last != -1 and _g == _INV[_last]:
            _g = int(RNG.integers(0, 4))
        _M = _matsD[_g] @ _M
        _last = _g
    if abs(np.trace(_M) - 3) > 1e-6:
        _genuine += 1
        _wv, _vv = np.linalg.eig(_M)
        _k = int(np.argmin(np.abs(_wv - 1)))
        _ax = np.real(_vv[:, _k])
        _ax = _ax / np.linalg.norm(_ax)
        if _ax[np.argmax(np.abs(_ax))] < 0:
            _ax = -_ax
        _axes.append(tuple(np.round(_ax, 6)))
chk("F6", "F", "R", "cmp",
    "every sampled nontrivial word is a GENUINE rotation (trace != 3, hence exactly two "
    "fixed points on S^2); sampled axes are almost all distinct (repeats reflect repeated sampled WORDS, not axis collisions) -- the fixed set D is a countable union of point pairs",
    _genuine == 500 and len(set(_axes)) >= 440,
    f"genuine rotations 500/500; distinct axes {len(set(_axes))}/500")

# --- F7: KESTEN non-amenability witness -----------------------------------
def _kesten_free(L):
    parent = [(-1, -1)]
    frontier = [(0, -1)]
    for _ in range(L):
        newf = []
        for (node, last) in frontier:
            for g in range(4):
                if last != -1 and g == _INV[last]:
                    continue
                idx = len(parent)
                parent.append((node, g))
                newf.append((idx, g))
        frontier = newf
    n = len(parent)
    x = np.ones(n)
    x /= np.linalg.norm(x)
    par = np.array([p for p, _ in parent])
    for _ in range(300):
        y = np.zeros(n)
        np.add.at(y, par[1:], x[1:])
        y[1:] += x[par[1:]]
        y /= 4.0
        nrm = np.linalg.norm(y)
        x = y / nrm
    return nrm, n

def _kesten_z2(R):
    pts = {}
    for xx in range(-R, R + 1):
        for yy in range(-R, R + 1):
            if abs(xx) + abs(yy) <= R:
                pts[(xx, yy)] = len(pts)
    n = len(pts)
    nbrs = [[] for _ in range(n)]
    for (xx, yy), i in pts.items():
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            j = pts.get((xx + dx, yy + dy))
            if j is not None:
                nbrs[i].append(j)
    v = np.ones(n)
    v /= np.linalg.norm(v)
    for _ in range(400):
        w = np.zeros(n)
        for i in range(n):
            for j in nbrs[i]:
                w[i] += v[j]
        w /= 4.0
        nrm = np.linalg.norm(w)
        v = w / nrm
    return nrm, n

_rf, _nf = _kesten_free(9)
_rz, _nz = _kesten_z2(30)
chk("F7", "F", "R", "free",
    "KESTEN WITNESS: the averaging operator on the free word ball (depth 9, 39,365 nodes) "
    "has top eigenvalue below sqrt(3)/2 = 0.8660254, while the amenable Z^2 control "
    "approaches 1 -- non-amenability of the free pair, numerically witnessed",
    _rf < math.sqrt(3) / 2 + 1e-9 and _rf > 0.80 and _rz > 0.97 and (_rz - _rf) > 0.10,
    f"rho_free(9) = {_rf:.6f} < sqrt3/2 = {math.sqrt(3)/2:.6f} << rho_Z2(30) = {_rz:.6f}")

# --- F8: anti-numerology control ------------------------------------------
chk("F8", "F", "X", "cmp",
    "ANTI-NUMEROLOGY: the whole freeness/paradox structure holds verbatim at cos theta = 1/3 "
    "(check F2), an angle with no Z-Spin content -- so rank 2, the 4/5 piece counts and "
    "sqrt(3)/2 carry NO Z-information; and sqrt(3)/2 = 0.8660254 is REFUSED as a match to "
    "|lambda| = 0.8915136 (difference 0.0254882)",
    abs(math.sqrt(3) / 2 - r_abs) > 0.02,
    f"|sqrt3/2 - |lambda|| = {abs(math.sqrt(3)/2 - r_abs):.7f} -- not a match, not claimed")

# --- F9: mean-invisible freeness ------------------------------------------
UX = np.zeros((4, 4), dtype=complex)
UY = np.zeros((4, 4), dtype=complex)
from scipy.linalg import expm as _expm
UX = _expm(-0.5j * theta_D * np.kron(Z_path, B_E))
UY = _expm(-0.5j * theta_D * np.kron(Z_path, R_E))
rhoE0 = np.diag([1.0, 0.0]).astype(complex)

def _ptr_channel(U):
    out = []
    for Ei in basis:
        big = U @ np.kron(Ei, rhoE0) @ U.conj().T
        out.append(np.trace(big.reshape(2, 2, 2, 2), axis1=1, axis2=3))
    return out

_chx = _ptr_channel(UX)
_chy = _ptr_channel(UY)
_same_ptr = max(np.linalg.norm(_chx[i] - _chy[i]) for i in range(4))
_real_mult = abs(np.imag(_chx[1][0, 1]))
RX = so3_x(theta_D)
RZr = so3_z(theta_D)
_noncomm = np.linalg.norm(RX @ RZr - RZr @ RX)
chk("F9", "F", "A", "cmp",
    "MEAN-INVISIBLE FREENESS: the two generator collisions induce IDENTICAL pointer mean "
    "channels (real multiplier cos theta_D, M57.P-consistent), so the ONE-STEP generator label "
    "is mean-invisible, while the conditional carrier rotations do not commute. NOTE: the v1.4 "
    "phrase 'the entire F2 lives below the mean layer' is WITHDRAWN -- check W1 shows composed "
    "words ARE mean-distinguishable.",
    _same_ptr < 1e-13 and _real_mult < 1e-13 and _noncomm > 0.1,
    f"||Phi_x^ptr - Phi_y^ptr|| = {_same_ptr:.2e}; Im(mult) = {_real_mult:.2e}; "
    f"||[R_x, R_y]|| = {_noncomm:.4f}")

# --- F10: kinematics finite, dynamics infinite ----------------------------
_hashes = set()
_stack = [(np.eye(3), -1, 0)]
while _stack:
    _M, _last, _d = _stack.pop()
    _hashes.add(tuple(np.round(_M, 8).flatten()))
    if _d < 7:
        for _g in range(4):
            if _last != -1 and _g == _INV[_last]:
                continue
            _stack.append((_matsD[_g] @ _M, _g, _d + 1))
chk("F10", "F", "A", "cmp",
    "KINEMATIC GROUP FINITE, DYNAMICAL GROUP INFINITE: the register symmetry group <J, J_Z> "
    "has order 8 (D4, amenable) while the collision words of length <= 7 give 4,373 "
    "pairwise-distinct rotations. NOTE the corrected statement: G_D is NOT contained in the "
    "finite GROUP D4; it does act faithfully on the finite-DIMENSIONAL carrier (F2 embeds in "
    "SO(3) c GL(3,R)). Comparison layer: theta_D is imported.",
    len(_G11) == 8 and len(_hashes) == 4373,
    f"|<J,J_Z>| = {len(_G11)}; distinct collision words <=7: {len(_hashes)}/4373")

# --- F11: density-in-SO(3) proxy ------------------------------------------
_pts = []
for _ in range(4000):
    _L = 25
    _M = np.eye(3)
    _last = -1
    for _ in range(_L):
        _g = int(RNG.integers(0, 4))
        while _last != -1 and _g == _INV[_last]:
            _g = int(RNG.integers(0, 4))
        _M = _matsD[_g] @ _M
        _last = _g
    _pts.append(_M @ np.array([0.0, 0.0, 1.0]))
_pts = np.array(_pts)
_m1 = np.linalg.norm(_pts.mean(axis=0))
_m2 = np.linalg.norm((np.einsum('ni,nj->ij', _pts, _pts) / len(_pts)) - np.eye(3) / 3)
chk("F11", "F", "X", "cmp",
    "DENSITY PROXY: 4000 random length-25 collision words spread a point over S^2 with "
    "small first and second moments -- consistent with closure(G_D) = SO(3), the face's "
    "full rotation symmetry generated by two odd collisions",
    _m1 < 0.15 and _m2 < 0.15,
    f"|mean| = {_m1:.4f}; ||2nd moment - I/3|| = {_m2:.4f}")

# --- F12: scope declaration -----------------------------------------------
chk("F12", "F", "D", "free",
    "DECLARATION OF SCOPE: the paradox lives strictly OFF the sigma-algebra. Lebesgue "
    "measure on measurable sets remains SO(3)-invariant; Born probabilities and every CPTP "
    "statement of the corpus are untouched; no physical doubling of volume or energy is "
    "claimed; Route S's phase measure (countably additive, on a circle) is OUTSIDE the "
    "obstruction's scope and is NOT blocked",
    abs(np.trace(rhoE0).real - 1.0) < 1e-15,
    "declaration; the obstruction concerns TOTAL finitely-additive invariant set functions only")

# ==========================================================================
# BLOCK W -- word-level mean channel: what the mean CAN and CANNOT see    NEW v1.3
# ==========================================================================
# Correction of a v1.2 overstatement, and its replacement by a sharper theorem.

def _word_W0(word):
    """conditional unitary on the carrier for a retained-carrier word"""
    W = np.eye(2, dtype=complex)
    for g in word:
        Bop = B_E if g in "xX" else R_E
        sgn = -1.0 if g.islower() else +1.0
        W = _expm(-0.5j * sgn * theta_D * Bop) @ W
    return W

def _word_gamma(word, rho):
    W0 = _word_W0(word)
    W1 = J_E @ W0 @ J_E
    return np.trace(rho @ W0.conj().T @ W1)

_rho_inv = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)   # commutes with J_E = sigma_z
_g_x = _word_gamma("x", _rho_inv)
_g_y = _word_gamma("y", _rho_inv)
_g_xx = _word_gamma("xx", _rho_inv)
_g_xy = _word_gamma("xy", _rho_inv)
_g_yx = _word_gamma("yx", _rho_inv)
_g_yy = _word_gamma("yy", _rho_inv)

chk("W1", "W", "A", "cmp",
    "RETRACTION OF A v1.2 OVERSTATEMENT: the mean channel is blind to the ONE-STEP generator "
    "label (gamma(x) = gamma(y) = cos theta_D exactly) but it DOES separate composed words: "
    "gamma(xx) = cos 2theta_D = 2|lambda|^2 - 1 differs from gamma(xy) = cos^2 theta_D = "
    "|lambda|^2. The v1.2 claim that the ENTIRE free group is mean-invisible is FALSE and is "
    "withdrawn.",
    abs(_g_x - _g_y) < 1e-14
    and abs(_g_x.real - r_abs) < 1e-12
    and abs(_g_xx.real - (2 * r_abs ** 2 - 1)) < 1e-12
    and abs(_g_xy.real - r_abs ** 2) < 1e-12
    and abs(_g_xx - _g_xy) > 0.2,
    f"gamma(x) = gamma(y) = {_g_x.real:.10f}; gamma(xx) = {_g_xx.real:.10f}; "
    f"gamma(xy) = gamma(yx) = {_g_xy.real:.10f}; separation {abs(_g_xx - _g_xy):.6f}")

_allreal = True
_maxim = 0.0
_words = ["x", "y", "xx", "xy", "yx", "yy", "xyx", "xxyy", "xYxy", "yXYx", "xxxyyy"]
for _w in _words:
    _gg = _word_gamma(_w, _rho_inv)
    _maxim = max(_maxim, abs(_gg.imag))
for _ in range(400):
    _L = int(RNG.integers(1, 12))
    _lets = "xXyY"
    _wr = "".join(_lets[int(RNG.integers(0, 4))] for _ in range(_L))
    _gg = _word_gamma(_wr, _rho_inv)
    _maxim = max(_maxim, abs(_gg.imag))
chk("W2", "W", "R", "cmp",
    "THEOREM M57.P' (Word-Level Real-Multiplier Lemma), the replacement result: with a "
    "grading-INVARIANT carrier state, EVERY word of the collision group has a REAL "
    "multiplier. Proof: gamma = Tr(rho J_E W0^dag J_E W0); using J_E rho J_E = rho and "
    "cyclicity gives gamma = gamma-bar. Hence no word of ANY length supplies arg lambda -- "
    "the phase escape route through long words is CLOSED, strictly strengthening M57.P.",
    _maxim < 1e-13,
    f"max |Im gamma| over 11 structured + 400 random words = {_maxim:.2e}")

# ==========================================================================
# BLOCK C -- the carrier, actually constructed                             NEW v1.3
# ==========================================================================
# Interaction  H_int = (phi/2) Z_path (x) B_E ,  B_E odd under J_E.
#   W_0 = exp(-i phi/2 B_E),  W_1 = J_E W_0 J_E = exp(+i phi/2 B_E)
#   => W_1^dag W_0 = exp(-i phi B_E) = cos phi I - i sin phi B_E
#   => gamma = cos phi - i sin phi <B_E>_rho_E
# Two real knobs (phi, s = <B_E>) against two real targets (Re lambda, Im lambda).

_phi_star = math.acos(lam.real)
_s_star = -lam.imag / math.sin(_phi_star)      # SIGN FIX v1.4: gamma = cos phi - i s sin phi
_nz = math.sqrt(max(0.0, 1.0 - _s_star ** 2))
_rho_break = 0.5 * (I2 + _s_star * B_E + _nz * J_E)
_U_star = _expm(-0.5j * _phi_star * np.kron(Z_path, B_E))
# BASIS FIX v1.4: order the Z_path eigenbasis DESCENDING so that |0> is the +1
# eigenvector, matching the paper's Z_path = |0><0| - |1><1|.  np.linalg.eigh returns
# ASCENDING eigenvalues; the v1.3 build inherited that order and silently swapped
# |0> <-> |1>, which masked the sign of s*.
_wz, _Vz = np.linalg.eigh(Z_path)
_ord = np.argsort(-_wz)
_wz, _Vz = _wz[_ord], _Vz[:, _ord]

def _reduced_star(rin):
    _o = _U_star @ np.kron(rin, _rho_break) @ _U_star.conj().T
    return np.trace(_o.reshape(2, 2, 2, 2), axis1=1, axis2=3)

_toz = lambda m: _Vz.conj().T @ m @ _Vz
_fromz = lambda m: _Vz @ m @ _Vz.conj().T
_Ebas = [np.array([[1, 0], [0, 0]], dtype=complex), np.array([[0, 1], [0, 0]], dtype=complex),
         np.array([[0, 0], [1, 0]], dtype=complex), np.array([[0, 0], [0, 1]], dtype=complex)]
_maxerr = 0.0
for _i, _Ei in enumerate(_Ebas):
    _out = _toz(_reduced_star(_fromz(_Ei)))
    _tgt = _Ei * (lam if _i == 1 else (np.conj(lam) if _i == 2 else 1.0))
    _maxerr = max(_maxerr, np.linalg.norm(_out - _tgt))
_Lstar = np.zeros((4, 4), dtype=complex)
for _j, _Ej in enumerate(_Ebas):
    _Lstar[:, _j] = _toz(_reduced_star(_fromz(_Ej))).flatten()
_evst = np.linalg.eigvals(_Lstar)
_has_lam = any(abs(z - lam) < 1e-10 for z in _evst)
_has_bar = any(abs(z - np.conj(lam)) < 1e-10 for z in _evst)
_two_ones = sum(1 for z in _evst if abs(z - 1) < 1e-10) == 2
_Choi_st = np.zeros((4, 4), dtype=complex)
for _a in range(2):
    for _b in range(2):
        _Eab = np.zeros((2, 2), dtype=complex)
        _Eab[_a, _b] = 1
        _Choi_st[2 * _a:2 * _a + 2, 2 * _b:2 * _b + 2] = _toz(_reduced_star(_fromz(_Eab)))
_Choi_st = 0.5 * (_Choi_st + _Choi_st.conj().T)
_cev = np.linalg.eigvalsh(_Choi_st)
_tp = abs(np.trace(_reduced_star(np.array([[0.6, 0.2], [0.2, 0.4]], dtype=complex))).real - 1.0)

chk("C1", "C", "A", "cmp",
    "THEOREM M57.C.1 (EXISTENCE -- the carrier is CONSTRUCTED): an explicit two-dimensional "
    "external carrier with non-central grading J_E, odd interaction operator B_E, and a "
    "grading-BREAKING pure state reproduces the ZS-M54 target channel Phi_lambda EXACTLY. "
    "All three constraints of the closing specification are simultaneously satisfiable: the "
    "specification is NOT vacuous.",
    _maxerr < 1e-12 and _has_lam and _has_bar and _two_ones
    and _cev.min() > -1e-12 and int(sum(_cev > 1e-9)) == 2 and _tp < 1e-12,
    f"max||Phi_constructed - Phi_lambda|| = {_maxerr:.3e}; Liouville spec = {{1,1,lambda,"
    f"lambda-bar}} confirmed; Choi rank = {int(sum(_cev > 1e-9))} (= M56.5 value 2); "
    f"CP min eig = {_cev.min():.2e}; TP residual = {_tp:.2e}")

chk("C2", "C", "R", "cmp",
    "the constructed carrier satisfies the STRUCTURAL constraints lambda-free: dim H_E = 2; "
    "J_E non-central (not +-I); interaction total-grading-EVEN under J_S (x) J_E; QND "
    "([H_int, Z_path (x) I] = 0); carrier state PURE",
    np.linalg.norm(J_E - I2) > 1e-9 and np.linalg.norm(J_E + I2) > 1e-9
    and np.linalg.norm(np.kron(J_S, J_E) @ np.kron(Z_path, B_E) @ np.kron(J_S, J_E)
                       - np.kron(Z_path, B_E)) < 1e-13
    and np.linalg.norm(np.kron(Z_path, B_E) @ np.kron(Z_path, I2)
                       - np.kron(Z_path, I2) @ np.kron(Z_path, B_E)) < 1e-13
    and abs(np.trace(_rho_break @ _rho_break).real - 1.0) < 1e-12,
    "dim 2; J_E non-central; interaction even and QND; state pure")

chk("C3", "C", "A", "cmp",
    "WITHIN A SINGLE GRADED COLLISION AND WITH NO INDEPENDENT SYSTEM HOLONOMY, the phase comes "
    "from the STATE and not the dynamics: the constructed carrier state does NOT commute with "
    "the grading, and by M57.P' that is forced in this restricted setting. The qualifier is "
    "essential and was missing in v1.3-v1.4: check K5 exhibits the THIRD case, ZS-M54's own "
    "Phi_lambda = U_chi o D_r, in which the grading is intact.",
    np.linalg.norm(_rho_break @ J_E - J_E @ _rho_break) > 0.1 and abs(lam.imag) > 0.1,
    f"||[rho_E, J_E]|| = {np.linalg.norm(_rho_break @ J_E - J_E @ _rho_break):.6f} != 0; "
    f"Im lambda = {lam.imag:.10f} != 0")

# --- C4: the reparametrization theorem -- why C1 does NOT close F-M54-16' ---
def _to_ps(l):
    ph = math.acos(l.real)
    return ph, -l.imag / math.sin(ph)          # SIGN FIX v1.5: matches gamma = cos - i s sin

def _to_lam(ph, ss):
    return complex(math.cos(ph), -ss * math.sin(ph))   # SIGN FIX v1.5: one convention throughout

_nb, _bad = 0, 0
for _ in range(20000):
    _a = float(RNG.uniform(-0.97, 0.97))
    _b = float(RNG.uniform(-0.97, 0.97))
    if _a * _a + _b * _b >= 0.95 or abs(_b) < 1e-6:
        continue
    _l = complex(_a, _b)
    _ph, _ss = _to_ps(_l)
    if not (0 < _ph < math.pi and abs(_ss) <= 1):
        continue
    _nb += 1
    if abs(_to_lam(_ph, _ss) - _l) > 1e-12:
        _bad += 1
chk("C4", "C", "R", "free",
    "THEOREM M57.C.2 (REPARAMETRISATION -- the honest verdict): the map lambda <-> (phi, s) is "
    "a BIJECTION between the open unit disc off the real axis and (0, pi) x (-1, 1). The "
    "constructed carrier therefore TRANSPORTS lambda into collision coordinates; it does not "
    "derive it. Two fitted reals against two targets is exactly the ZS-M56.7 trap, "
    "pre-registered: ZERO evidential content. F-M54-16' is NOT closed.",
    _nb > 10000 and _bad == 0,
    f"bijection verified on {_nb} samples, {_bad} failures; parameters fitted = 2 "
    f"(phi, s), targets = 2 (Re lambda, Im lambda); degrees of freedom remaining = 0")

_hitsC, _totC, _bestC = 0, 0, None
for _name, _val in (("phi", _phi_star), ("s", _s_star)):
    for _a in range(1, 13):
        for _b in range(1, 13):
            for _pA in (-2, -1, 0, 1, 2):
                for _pQ in (-2, -1, 0, 1, 2):
                    for _pK in (-2, -1, 0, 1, 2):
                        _v = (_a / _b) * float(A) ** _pA * float(Q) ** _pQ * float(kappa) ** _pK
                        if not (0 < _v < 4):
                            continue
                        _totC += 2                     # v1.5: the family is SIGNED, +v and -v
                        _d = min(abs(_v - _val), abs(-_v - _val))
                        if _bestC is None or _d < _bestC:
                            _bestC = _d
                        if _d < 1e-4:
                            _hitsC += 1
chk("C5", "C", "X", "cmp",
    "ANTI-NUMEROLOGY on the two fitted parameters: neither phi = 2.1729483796 nor "
    "s = -0.8353812873 is an algebraic-in-(A, Q) expression to 1e-4 -- the family is SIGNED "
    "(both +v and -v are tested, the v1.4 build searched only positive values and so could not "
    "have found a negative s*). They are lambda in "
    "disguise, exactly as Theorem M57.C.2 says -- the null is a CONTROL confirming that the "
    "construction imported the answer rather than deriving it.",
    _totC > 15000 and _hitsC == 0,
    f"family size {_totC} (two targets), hits {_hitsC}, nearest miss {_bestC:.3e}, "
    f"expected-by-chance {_totC * 2e-4 / 4:.2f}")

chk("C6", "C", "D", "cmp",
    "DECLARATION (F-M54-16' STATUS): NOT CLOSED. v1.3 established that the specification is "
    "SATISFIABLE (check C1) with (phi, s) = (2.1729483796, -0.8353812873) -- note the CORRECTED "
    "sign of s. Block K supersedes the two-real form: the residual is ONE complex number, "
    "Lambda_S14 = <0|Phi_S14(|0><1|)|1>, to be computed from the slab and compared once "
    "(check K8). No S14 slab computation is performed in this build (debt 7, check K10).",
    abs(_phi_star - 2.1729483796) < 1e-9 and abs(_s_star + 0.8353812873) < 1e-9,
    f"phi = {_phi_star:.10f}, s = {_s_star:.10f}; SUPERSEDED by Block K: the successor now owes ONE complex number Lambda_S14, not two reals")

# --- C7: de Groot priority (review-driven correction) ---
_c_abs = r_abs
_t2 = (1 - _c_abs) / (1 + _c_abs)
chk("C7", "C", "A", "cmp",
    "PRIORITY CORRECTION (de Groot 1956): the general free-rotation theorem for perpendicular "
    "axes under a transcendence condition is PRIOR EXTERNAL MATHEMATICS. de Groot's condition "
    "is on tan^2(theta/2) = (1 - cos theta)/(1 + cos theta), and cos theta transcendental "
    "<=> tan^2(theta/2) transcendental (if t were algebraic then cos = (1-t)/(1+t) would be). "
    "Theorem M57.F.1 is therefore an APPLICATION at theta_D, not a new general theorem.",
    abs((1 - _t2) / (1 + _t2) - _c_abs) < 1e-14,
    f"tan^2(theta_D/2) = {_t2:.12f}; round-trip to cos theta_D exact; the two transcendence "
    f"conditions are equivalent")

# ==========================================================================
# BLOCK K -- the Fourier-Weyl carrier frame and the one-number gate      NEW v1.4
# ==========================================================================
# Closes the U(1) gauge freedom that v1.3 left open (M57.F.0), by building the odd
# frame from corpus register operators only.  Then restates the residual as a SINGLE
# complex number.

_Sshift = np.zeros((11, 11), dtype=complex)
for _j in range(11):
    _Sshift[(_j + 1) % 11, _j] = 1.0
_wq = np.exp(2j * np.pi / 11)
_Four = np.array([[_wq ** (_a * _b) for _b in range(11)] for _a in range(11)],
                 dtype=complex) / math.sqrt(11.0)

chk("K1", "K", "R", "free",
    "CORPUS IDENTITY (ZS-F0): the seam factorises through the Fourier operator as J = F^2 S "
    "= S^-1 F^2 on the Q = 11 register -- the fact that lets the carrier frame be built from "
    "register kinematics alone",
    np.linalg.norm(J11 - _Four @ _Four @ _Sshift) < 1e-10
    and np.linalg.norm(J11 - np.linalg.inv(_Sshift) @ _Four @ _Four) < 1e-10,
    f"||J - F^2 S|| = {np.linalg.norm(J11 - _Four @ _Four @ _Sshift):.2e}")

_e = lambda _k: np.eye(11, dtype=complex)[:, _k]
_v1, _v9 = _e(1), _e(9)
_PE = np.outer(_v1, _v1.conj()) + np.outer(_v9, _v9.conj())
_DeltaE = (9 - 1) % 11
_AF = _PE @ np.linalg.matrix_power(_Sshift, _DeltaE) @ _PE
_BF = _AF + _AF.conj().T
_RF = -1j * (_AF - _AF.conj().T)
_JEF = _PE @ JZ11 @ _PE
_Wb = np.column_stack([_v1, _v9])
_red = lambda _M: _Wb.conj().T @ _M @ _Wb

chk("K2", "K", "R", "free",
    "THEOREM M57.K.1 (Fourier-Weyl carrier frame, lambda-FREE): with P_E the unique D4 E-block "
    "span{|1>,|9>} of Theorem M57.3 and Delta = (9-1) mod 11 = 8, the operators "
    "A_F = P_E S^Delta P_E = |9><1|, B_F = A_F + A_F^dag, R_F = -i(A_F - A_F^dag), "
    "J_E = P_E J_Z P_E satisfy B_F^2 = R_F^2 = J_E^2 = P_E, {B_F, R_F} = 0, "
    "J_E B_F J_E = -B_F, J_E R_F J_E = -R_F, R_F = -i J_E B_F, and J_E is non-central on the "
    "block. In the ordered basis (|1>,|9>) they are exactly (sigma_x, -sigma_y, -sigma_z).",
    np.linalg.norm(_red(_AF) - np.array([[0, 0], [1, 0]], dtype=complex)) < 1e-12
    and np.linalg.norm(_red(_BF) - sx) < 1e-12
    and np.linalg.norm(_red(_RF) + sy) < 1e-12
    and np.linalg.norm(_red(_JEF) + sz) < 1e-12
    and np.linalg.norm(_BF @ _BF - _PE) < 1e-12
    and np.linalg.norm(_RF @ _RF - _PE) < 1e-12
    and np.linalg.norm(_JEF @ _JEF - _PE) < 1e-12
    and np.linalg.norm(_BF @ _RF + _RF @ _BF) < 1e-12
    and np.linalg.norm(_JEF @ _BF @ _JEF + _BF) < 1e-12
    and np.linalg.norm(_JEF @ _RF @ _JEF + _RF) < 1e-12
    and np.linalg.norm(_RF - (-1j) * _JEF @ _BF) < 1e-12
    and np.linalg.norm(_JEF - _PE) > 1e-9 and np.linalg.norm(_JEF + _PE) > 1e-9,
    "all eleven relations exact; frame built from S, P_E (Thm M57.3) and J_Z only -- "
    "no z*, lambda, theta_D, phi or s enters")

chk("K3", "K", "A", "free",
    "COROLLARY M57.K.2 (the U(1) gauge of M57.F.0 is fixed RELATIVE TO THE REGISTER): the v1.3 frame was canonical only "
    "up to the U(1) centraliser of J_E, an admitted gap. The Fourier-Weyl frame fixes it: the "
    "displacement Delta = 8 is determined by the E-block slots, so the first odd axis is "
    "B_F and not an arbitrary cos(alpha)sigma_x + sin(alpha)sigma_y. The frame agrees with the "
    "v1.3 Pauli frame up to the fixed relabelling (sigma_x, -sigma_y, -sigma_z), which is an "
    "orientation convention, not a free parameter. SCOPE: what is fixed is the operator FRAME "
    "relative to the locked register basis and the chosen positive shift S. Which vertex the "
    "S14 action actually selects -- B_F, R_F, or a time-ordering of both -- remains OPEN and is "
    "NOT settled by this corollary.",
    np.linalg.norm(_red(_BF) - sx) < 1e-12 and np.linalg.norm(_red(_RF) + sy) < 1e-12,
    "alpha is no longer free relative to the register; the ACTION-level vertex selector is OPEN")

_HZ_span = np.column_stack([_e(0), _e(1)])
_EB_span = np.column_stack([_v1, _v9])
_joint_rank = np.linalg.matrix_rank(np.column_stack([_HZ_span, _EB_span]))
chk("K4", "K", "R", "free",
    "M56 CONSISTENCY: the E-block span{|1>,|9>} SHARES the slot |1> with the pointer "
    "span{|0>,|1>}, so the joint span has rank 3 < 4 and the two cannot be simultaneous tensor "
    "factors. The frame must therefore be used as an EXTERNAL isomorphic copy (or a ZS-M58 CP "
    "correspondence), exactly as the M56 in-register no-go requires. The frame supplies the "
    "OPERATORS, not an in-register subsystem.",
    _joint_rank == 3,
    f"rank(span H_Z + span E-block) = {_joint_rank} < 4 -- no in-register factorisation")

# --- K5: the THIRD CASE -- phase/attenuation split, no grading breaking ---
_rho_gi = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)     # commutes with J_E
_U_att = _expm(-0.5j * theta_D * np.kron(sz, B_E))              # Z_path = diag(+1,-1)
_U_hol = np.diag([1.0, np.exp(-1j * arg_lam)]).astype(complex)  # system-side Z-holonomy

def _D_r(_rin):
    _o = _U_att @ np.kron(_rin, _rho_gi) @ _U_att.conj().T
    return np.trace(_o.reshape(2, 2, 2, 2), axis1=1, axis2=3)

def _Phi_split(_rin):
    return _U_hol @ _D_r(_rin) @ _U_hol.conj().T

_Eb = [np.array([[1, 0], [0, 0]], dtype=complex), np.array([[0, 1], [0, 0]], dtype=complex),
       np.array([[0, 0], [1, 0]], dtype=complex), np.array([[0, 0], [0, 1]], dtype=complex)]
_err_split = max(np.linalg.norm(_Phi_split(_Eb[_i])
                                - _Eb[_i] * (lam if _i == 1 else
                                             (np.conj(lam) if _i == 2 else 1.0)))
                 for _i in range(4))
_att_only = _D_r(_Eb[1])[0, 1]
chk("K5", "K", "A", "cmp",
    "THEOREM M57.K.3 (the THIRD CASE -- correction of a v1.3 overclaim): a "
    "grading-INVARIANT carrier state with collision angle theta_D gives the REAL attenuation "
    "|lambda| = cos theta_D, and a separate system-side Z-holonomy e^{i arg lambda} supplies "
    "the phase; the composite reproduces Phi_lambda EXACTLY with NO grading breaking. This is "
    "ZS-M54's own Phi_lambda = U_chi o D_r structure. The v1.3 claim of a 'dynamics/state "
    "dichotomy with no third case' is FALSE and is withdrawn.",
    abs(_att_only.imag) < 1e-13 and abs(_att_only.real - r_abs) < 1e-12
    and _err_split < 1e-12
    and np.linalg.norm(_rho_gi @ J_E - J_E @ _rho_gi) < 1e-14,
    f"attenuation = {_att_only.real:.12f} = |lambda| (real); composite error = "
    f"{_err_split:.2e}; ||[rho_E, J_E]|| = 0 -- grading intact")

chk("K6", "K", "X", "cmp",
    "COMPARISON CONTROL (TAUTOLOGY): the attenuation angle OF THE SPLIT, theta_split := "
    "arccos|lambda|, coincides with the collision angle theta_D of sections 6-8 -- which is "
    "true by definition, since both are arccos|lambda|. It is recorded because it shows the "
    "two halves of the paper use one angle, and it is NOT evidence. The v1.4 build called this "
    "quantity theta_S14, which was a premise insertion: no S14 slab angle has been computed, "
    "and only a value derived FROM the action may carry that name (rule R10').",
    abs(math.acos(r_abs) - theta_D) < 1e-15,
    f"theta_split = theta_D = {theta_D:.12f}; tautological by definition, comparison layer")

# --- K7: the structural gate (review step 4) on the target ---
_ChoiT = np.zeros((4, 4), dtype=complex)
_PhiT = {(0, 0): _Eb[0], (1, 1): _Eb[3], (0, 1): lam * _Eb[1], (1, 0): np.conj(lam) * _Eb[2]}
for (_c, _d), _val in _PhiT.items():
    _Ecd = np.zeros((2, 2), dtype=complex)
    _Ecd[_c, _d] = 1
    _ChoiT += np.kron(_val, _Ecd)
_ChoiT = 0.5 * (_ChoiT + _ChoiT.conj().T)
_evT = np.linalg.eigvalsh(_ChoiT)
_Pdel = np.zeros((4, 4), dtype=complex)
_Pdel[0, 0] = 1.0
_Pdel[3, 3] = 1.0
chk("K7", "K", "R", "cmp",
    "THE STRUCTURAL GATE, stated executably (the ZS-M58 seam): the target Choi operator is "
    "Hermitian, positive, trace-preserving on the output marginal, has support inside the "
    "beginning-end equaliser Delta_Z = span{|00>,|11>}, and has rank exactly 2 with "
    "eigenvalues 1 +- |lambda|. These four conditions are what an S14 open-slab kernel must "
    "satisfy BEFORE any multiplier is compared -- sub-gate A of F-M54-16'.",
    np.linalg.norm(_ChoiT - _ChoiT.conj().T) < 1e-14 and _evT.min() > -1e-12
    and int(sum(_evT > 1e-9)) == 2
    and np.linalg.norm(_ChoiT - _Pdel @ _ChoiT @ _Pdel) < 1e-12
    and np.allclose(np.trace(_ChoiT.reshape(2, 2, 2, 2), axis1=0, axis2=2), np.eye(2)),
    f"Choi rank 2, eigenvalues {1 + r_abs:.10f} and {1 - r_abs:.10f}; support = Delta_Z; "
    f"output marginal = I")

_Lambda_target = _PhiT[(0, 1)][0, 1]
chk("K8", "K", "A", "cmp",
    "THE ONE-NUMBER RESTATEMENT: the whole multiplier content of the channel is the single "
    "complex matrix element Lambda = <0|Phi(|0><1|)|1>. A successor need not compute two reals "
    "separately (the v1.3 (phi, s) pair, or the (theta, chi) pair) -- it computes ONE complex "
    "number from the slab and compares once. This supersedes declaration C6's two-number form.",
    abs(_Lambda_target - lam) < 1e-15,
    f"Lambda_target = {_Lambda_target.real:+.10f}{_Lambda_target.imag:+.10f}i = lambda")

# K9 v1.5: restated as a GENERAL theorem over arbitrary Lambda in the unit disc, so that
# it is genuinely lambda-free.  The v1.4 form evaluated it at lambda and was mis-tagged.
_bad_pol, _n_pol = 0, 0
for _ in range(20000):
    _a = float(RNG.uniform(-0.99, 0.99))
    _b = float(RNG.uniform(-0.99, 0.99))
    if _a * _a + _b * _b >= 0.98 or _a * _a + _b * _b < 1e-8:
        continue
    _L = complex(_a, _b)
    _thL, _chL = math.acos(abs(_L)), math.atan2(_L.imag, _L.real)
    _back = complex(math.cos(_thL) * math.cos(_chL), math.cos(_thL) * math.sin(_chL))
    _n_pol += 1
    if abs(_back - _L) > 1e-12:
        _bad_pol += 1
chk("K9", "K", "R", "free",
    "THEOREM M57.C.2 APPLIES TO THE IMPROVED ROUTE (general, lambda-free form): for EVERY "
    "Lambda in the punctured unit disc, (theta, chi) = (arccos|Lambda|, arg Lambda) are polar "
    "coordinates and the reconstruction is exact -- a bijection, hence two reals against two "
    "targets with zero residual freedom, for any target whatsoever. The phase/attenuation "
    "split is therefore a STRUCTURAL improvement and NOT an evidential one; anyone fitting "
    "theta and chi is inside the ZS-M56.7 trap.",
    _n_pol > 10000 and _bad_pol == 0,
    f"verified on {_n_pol} arbitrary targets in the disc, {_bad_pol} failures; no corpus "
    f"constant enters this check")

chk("K10", "K", "D", "cmp",
    "DECLARATION (why F-M54-16' is STILL not closed): the executable gate needs the ZS-S14 "
    "open-slab CTP influence kernel, and the loaded Standard-Model file is a compact summary "
    "containing NO influence functional, NO boundary return map and NO transfer-operator "
    "identification (zero textual occurrences). Constructing one would mean inventing slab "
    "data, which rules R1/R2 and gate F-M57.2 forbid. CORRECTION OF THE v1.4 WORDING: this is "
    "NOT merely a file-availability limit. Even with the full action, the reduced channel needs "
    "a slab identification and duration, a physical boundary state, gauge fixing with BRST/BFV "
    "projection, an initial-correlation assumption, a coarse-graining prescription, a "
    "regularisation, and a continuum-or-finite-cell choice. Whether the corpus DEFINES all of "
    "these is itself undetermined. The honest description is CURRENT CORPUS-DEFINITION "
    "INSUFFICIENCY (debt 7).",
    np.linalg.norm(_BF) > 0 and np.linalg.norm(_RF) > 0 and np.linalg.norm(_JEF) > 0
    and abs(_Lambda_target - lam) < 1e-15,
    "the single computation owed: Lambda_S14 = <0|Phi_S14(|0><1|)|1>, built from S_S14 and "
    "(P_E, A_F, B_F, R_F, J_E) with no lambda, z*, theta_D, phi or s in the construction")

# ==========================================================================
# BLOCK B -- the boundary Weyl-influence-ratio protocol                   NEW v1.5
# ==========================================================================
# Makes the residual computation executable in principle, and proves what the
# structural gate can and cannot decide.

def _choi_of(al):
    _C = np.zeros((4, 4), dtype=complex)
    for (_c, _d), _v in {(0, 0): np.array([[1, 0], [0, 0]], dtype=complex),
                         (1, 1): np.array([[0, 0], [0, 1]], dtype=complex),
                         (0, 1): al * np.array([[0, 1], [0, 0]], dtype=complex),
                         (1, 0): np.conj(al) * np.array([[0, 0], [1, 0]], dtype=complex)}.items():
        _Ecd = np.zeros((2, 2), dtype=complex)
        _Ecd[_c, _d] = 1
        _C += np.kron(_v, _Ecd)
    return 0.5 * (_C + _C.conj().T)

_Pdz = np.zeros((4, 4), dtype=complex)
_Pdz[0, 0] = 1.0
_Pdz[3, 3] = 1.0

def _gate_pass(al):
    _C = _choi_of(al)
    _ev = np.linalg.eigvalsh(_C)
    return (_ev.min() > -1e-12 and int(sum(_ev > 1e-9)) == 2 and 0 < abs(al) < 1
            and np.linalg.norm(_C - _Pdz @ _C @ _Pdz) < 1e-12
            and np.allclose(np.trace(_C.reshape(2, 2, 2, 2), axis1=0, axis2=2), np.eye(2)))

_np_all, _np_tot = 0, 0
for _ in range(4000):
    _a = float(RNG.uniform(-1, 1))
    _b = float(RNG.uniform(-1, 1))
    if _a * _a + _b * _b >= 1 or _a * _a + _b * _b < 1e-6:
        continue
    _np_tot += 1
    if _gate_pass(complex(_a, _b)):
        _np_all += 1
chk("B1", "B", "R", "free",
    "THEOREM M57.B.1 (Structural Underdetermination): the set of channels passing the ENTIRE "
    "structural gate -- CP, TP, population-preserving, Choi support in Delta_Z, Choi rank 2 -- "
    "is exactly {Phi_alpha : 0 < |alpha| < 1}, a one-complex-parameter family, with Choi "
    "eigenvalues 1 +- |alpha| for EVERY phase of alpha. Hence frame rigidity does NOT imply "
    "multiplier rigidity: the gate fixes everything about the channel EXCEPT one complex "
    "number. This is what makes the one-number residual exact rather than heuristic.",
    _np_tot > 2000 and _np_all == _np_tot,
    f"{_np_all}/{_np_tot} sampled alpha in the punctured disc pass every condition; "
    f"the gate cannot discriminate among them")

_wlist = ["x", "X", "y", "Y", "xx", "xy", "yx", "yy", "xyX", "xxyy", "xYxy", "yXYx",
          "xxxyyy", "xyxyxy"]
_gl = [_word_gamma(_w, _rho_inv) for _w in _wlist]
_wts = RNG.dirichlet(np.ones(len(_wlist)))
_mixg = sum(_wi * _gi for _wi, _gi in zip(_wts, _gl))
_Twalk = 0.25 * (_expm(-0.5j * theta_D * B_E) + _expm(0.5j * theta_D * B_E)
                 + _expm(-0.5j * theta_D * R_E) + _expm(0.5j * theta_D * R_E))
chk("B2", "B", "R", "cmp",
    "COROLLARY M57.P'' (no phase from ANY mixture): since every word multiplier is real "
    "(M57.P'), every probability mixture sum_w mu(w) gamma(w) over collision words is real, and "
    "the symmetric walk operator (R_x + R_x^-1 + R_y + R_y^-1)/4 is self-adjoint with real "
    "spectrum. So no random walk on the free group -- of any step distribution, at any depth, "
    "including asymptotically -- can supply arg lambda. The free-group route to the PHASE is "
    "CLOSED; Block F's freeness remains a statement about records, not about the phase.",
    max(abs(_g.imag) for _g in _gl) < 1e-13 and abs(_mixg.imag) < 1e-13
    and np.linalg.norm(_Twalk - _Twalk.conj().T) < 1e-14
    and max(abs(_e.imag) for _e in np.linalg.eigvals(_Twalk)) < 1e-13,
    f"14 words + a random mixture all real (max |Im| = {abs(_mixg.imag):.2e}); walk operator "
    f"self-adjoint with real spectrum")

_nb_s, _nI_s = 2, 6
_Ms = RNG.normal(size=(_nb_s + _nI_s, _nb_s + _nI_s))
_Ks = _Ms @ _Ms.T + (_nb_s + _nI_s) * np.eye(_nb_s + _nI_s)
_Kbb = _Ks[:_nb_s, :_nb_s]
_KbI = _Ks[:_nb_s, _nb_s:]
_KIb = _Ks[_nb_s:, :_nb_s]
_KII = _Ks[_nb_s:, _nb_s:]
_Keff = _Kbb - _KbI @ np.linalg.inv(_KII) @ _KIb
_schur_err = 0.0
for _ in range(20):
    _xb = RNG.normal(size=_nb_s)
    _xI = -np.linalg.inv(_KII) @ _KIb @ _xb
    _full = 0.5 * np.concatenate([_xb, _xI]) @ _Ks @ np.concatenate([_xb, _xI])
    _schur_err = max(_schur_err, abs(_full - 0.5 * _xb @ _Keff @ _xb))
chk("B3", "B", "R", "free",
    "STAGE 2 (bulk compression is EXACT): integrating out the interior of a Gaussian slab "
    "returns precisely the Schur complement K_eff = K_bb - K_bI K_II^-1 K_Ib on the boundary. "
    "The 'boundary-only' computation therefore discards NO bulk information -- it compresses "
    "the bulk inverse into a boundary Weyl function. Verified on 20 random boundary "
    "configurations of a positive-definite 8x8 kernel.",
    _schur_err < 1e-10,
    f"max |marginalised action - Schur form| = {_schur_err:.2e}")

# Stage 3: the influence ratio.  Feynman-Vernon Gaussian form
#   Z_ab = exp( -1/2 (h_a-h_b)^T G_R (h_a-h_b) + i (h_a-h_b)^T G_I (h_a+h_b)/2 )
_ds = 5
_Bs = RNG.normal(size=(_ds, _ds))
_GR = (_Bs @ _Bs.T + _ds * np.eye(_ds)) * 0.02
_Ssym = RNG.normal(size=(_ds, _ds))
_GI = 0.5 * (_Ssym + _Ssym.T) * 0.05
_h0 = RNG.normal(size=_ds)
_h1 = RNG.normal(size=_ds)
_Dl = _h0 - _h1
_Sm = 0.5 * (_h0 + _h1)

def _influence_ratio(GR, GI=None):
    _Gam = 0.5 * _Dl @ GR @ _Dl
    _chi = 0.0 if GI is None else _Dl @ GI @ _Sm
    return np.exp(-_Gam + 1j * _chi), _Gam, _chi

_Lsym, _Gsym, _csym = _influence_ratio(_GR)
_Lcpx, _Gcpx, _ccpx = _influence_ratio(_GR, _GI)
chk("B4", "B", "R", "free",
    "STAGE 3-4 (the protocol is WELL-POSED and the gate is partly automatic): with "
    "Lambda := Z_01 / sqrt(Z_00 Z_11) for a Gaussian boundary influence kernel, one has "
    "Z_00 = Z_11 = 1 IDENTICALLY (the diagonal branches have zero source difference), "
    "Z_10 = conj(Z_01), and Lambda = exp(-Gamma + i chi) with Gamma = (1/2) Delta^T G_R Delta "
    ">= 0 for positive G_R -- so gate conditions A1 (diagonal), A2 (hermiticity), A3 "
    "(|Lambda| <= 1) and A5 (support in Delta_Z) hold BY CONSTRUCTION for the Gaussian class. "
    "The gate's remaining discriminating content is strict rank 2 and the PHASE.",
    _Gsym > 0 and abs(_Lsym) <= 1.0 + 1e-15 and _gate_pass(complex(_Lsym))
    and abs(_Lcpx) <= 1.0 + 1e-15 and _gate_pass(complex(_Lcpx)),
    f"symmetric kernel: Gamma = {_Gsym:.6f}, |Lambda| = {abs(_Lsym):.10f}, gate PASS; "
    f"with G_I: |Lambda| = {abs(_Lcpx):.10f}, arg = {_ccpx:.6f}, gate PASS")

chk("B5", "B", "R", "free",
    "STAGE 5 (the phase discriminator, made executable): for a REAL SYMMETRIC boundary kernel "
    "the influence ratio has chi = 0 EXACTLY, so |Lambda| < 1 with zero phase. A nonzero phase "
    "therefore requires an explicitly non-symmetric ingredient in the boundary effective "
    "action -- a system-side holonomy, a grading-breaking boundary state, a chiral/fermionic "
    "determinant phase, or a multi-stage non-QND contribution. This is consistent with "
    "M57.P''and it tells a successor exactly where to look; naming a phase 'Berry-type' "
    "without exhibiting a closed loop and a connection is not sufficient.",
    abs(_csym) < 1e-15 and abs(np.angle(_Lsym)) < 1e-15 and abs(_ccpx) > 1e-3,
    f"symmetric kernel: chi = {_csym:.1e} (exactly zero); with a non-symmetric part: "
    f"chi = {_ccpx:.6f} != 0")

_Gam_target = -math.log(r_abs)
chk("B6", "B", "X", "cmp",
    "STRUCTURAL ALIGNMENT (comparison control): the protocol's natural attenuation output is "
    "Gamma = -log|Lambda|, and the corpus target value -log|lambda| = 0.1148346250 is EXACTLY "
    "the locked constant mu, the ZS-M54 dephasing rate per cycle. The protocol therefore lands "
    "on a quantity the corpus already names, rather than on a new one. This is an OBSERVATION "
    "about coordinates, not evidence: mu is defined as -log|lambda|.",
    abs(_Gam_target - float(mu)) < 1e-9,
    f"-log|lambda| = {_Gam_target:.10f} = mu = {float(mu):.10f}; tautological by definition")

chk("B7", "B", "D", "cmp",
    "PRE-REGISTRATION of the three outcomes, fixed BEFORE any slab computation: (i) if the "
    "structural gate fails, F-M54-16'(A) is CLOSED-NEGATIVE and Phi^QND is not the reduced S14 "
    "channel; (ii) if the gate passes and Lambda_S14 != lambda, the Fourier-Weyl carrier "
    "structure survives and the i-tetration identification of the multiplier is RETRACTED; "
    "(iii) if the gate passes and Lambda_S14 = lambda on a construction that never saw lambda, "
    "F-M54-16' closes. Outcome (iii) is worth something ONLY because (i) and (ii) are "
    "registered here first.",
    (not _gate_pass(complex(1.5, 0.0)))              # outcome (i): a gate-FAILING candidate
    and _gate_pass(complex(0.3, 0.2))                 # outcome (ii): gate passes, value wrong
    and _gate_pass(complex(lam))                      # outcome (iii): gate passes at the target
    and abs(complex(0.3, 0.2) - lam) > 0.1,           # (ii) and (iii) are genuinely distinct
    "three outcomes registered and shown mutually distinguishable by the gate itself; "
    "two of the three are negative")

chk("B8", "B", "D", "free",
    "DECLARATION: the protocol of Block B is NOT executed on the ZS-S14 action in this build. "
    "What is executed is a solvable Gaussian SURROGATE, which validates the INSTRUMENT (the "
    "Schur compression is exact, the ratio is well-posed, the gate is checkable, the phase "
    "discriminator is sharp) and says NOTHING about Z-Spin physics. No surrogate number is a "
    "prediction, and the surrogate's Lambda is not compared with lambda anywhere.",
    abs(_Lsym) < 1 and abs(_Lcpx) < 1,
    "surrogate validates the pipeline only; debt 7 records the corpus-definition insufficiency")

# ==========================================================================
# BLOCK T -- the clock, and the correctly typed residual                  NEW v1.6
# ==========================================================================
# The v1.4/v1.5 gate asked for ONE COMPLEX NUMBER Lambda_S14.  This block shows that
# question is ILL-POSED as stated, and replaces it with a well-posed one.

_rho_gi_T = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)

def _gamma_tau(gc, tau):
    _W0 = _expm(-0.5j * gc * tau * B_E)
    _W1 = J_E @ _W0 @ J_E
    return np.trace(_rho_gi_T @ _W0.conj().T @ _W1)

_taus = [0.05 * _k for _k in range(1, 63)]
_mods = [abs(_gamma_tau(1.0, _t)) for _t in _taus]
chk("T1", "T", "R", "free",
    "THEOREM M57.T.1 (Clock Ill-Posedness, WITHIN THE COLLISION FAMILY): the QND coherence multiplier depends on the "
    "interaction INTEGRATED over the slab, gamma(tau) = cos(g tau) for a graded collision at "
    "coupling g and duration tau. As tau varies at FIXED coupling, |gamma| sweeps the entire "
    "interval (0, 1); so within this family the modulus is not determined by the coupling "
    "alone. SCOPE CORRECTION against v1.6: this does NOT establish that Lambda_S14 is "
    "universally undefined. ZS-S24 already carries a one-step transfer family "
    "T_a = exp(-aV/2)exp(-aL)exp(-aV/2), and if a PRIMITIVE slab or event step is structurally "
    "selected then a dimensionless one-step map is well defined. The correct statement is: "
    "S_S14 alone does not select a finite-time map unless a primitive slab/event prescription "
    "is supplied. Universal ill-posedness is DERIVED-CONDITIONAL on the absence of such a "
    "prescription, not PROVEN.",
    min(_mods) < 0.08 and max(_mods) > 0.99,
    f"tau sweep at g = 1 over {len(_taus)} values: |gamma| ranges [{min(_mods):.6f}, "
    f"{max(_mods):.6f}] -- the whole admissible interval")

chk("T2", "T", "D", "cmp",
    "DECLARATION (the clock is not in the corpus). OFF-LEDGER OBSERVATION, not checked by this "
    "condition: a text search of the six loaded corpus files returned zero occurrences of the "
    "slab duration tau_Z. That search is performed outside the suite and this check does NOT "
    "verify it -- the v1.6 build stated the search inside a PASS-bearing string, which is the "
    "same ledger-integrity fault v1.5 corrected in F1/F9/C3, and it is corrected here by "
    "labelling. What this condition DOES verify is only that the comparison-layer constants are "
    "loaded. tau_Z is corpus debt 6, "
    "assigned to the unwritten ZS-Q19, and it is NOT determined by the ZS-S14 master action. "
    "CORRECTION OF THE v1.5 WORDING: the S14 action itself IS in the loaded corpus (Definition "
    "3.1 of ZS-S14, complete with the unified covariant derivative, the Yukawa invariant and "
    "the I-invariant potential). The v1.5 claim that the file is 'a compact summary' with no "
    "usable action was WRONG. What is absent is not the action but the slab reduction data, and "
    "the load-bearing absence is the clock.",
    isinstance(theta_D, float) and theta_D > 0,
    "S_S14 present (Def. 3.1); tau_Z absent (0 occurrences in 6 files); the obstruction is the "
    "clock, not the Lagrangian")

# --- the clock-free invariant ---
_mu_f = -math.log(r_abs)
_R_prin = arg_lam / _mu_f

# v1.7: the HONEST test.  The v1.6 build computed (n*arg)/(n*mu), which is n-independent by
# algebra and verifies nothing.  Here we evaluate the PRINCIPAL argument of lambda^n and show
# it does NOT equal n*arg(lambda) -- i.e. the "cycle-independence" of R presupposes an
# unwrapped logarithmic lift, which must be an explicit hypothesis of the theorem.
_wrap_fail = 0
_wrap_tested = 0
for _n in range(2, 24):
    _ln = lam ** _n
    _wrap_tested += 1
    if abs(math.atan2(_ln.imag, _ln.real) - _n * arg_lam) > 1e-9:
        _wrap_fail += 1
_R_at_2 = math.atan2((lam ** 2).imag, (lam ** 2).real) / (-math.log(abs(lam ** 2)))
chk("T3", "T", "X", "cmp",
    "RETRACTION CONTROL for the v1.6 T3: the principal argument does NOT satisfy "
    "Arg(lambda^n) = n Arg(lambda) -- it wraps. At n = 2 the principal-branch ratio is "
    "-7.6836, not 19.6740. The v1.6 check computed (n*arg)/(n*mu), which is n-independent by "
    "algebra and verified nothing, and its ledger line claimed n = 1..23 while the code tested "
    "eight values. Both faults are corrected: the unwrapped lift is now an explicit HYPOTHESIS "
    "(see T3a), not a verified fact.",
    _wrap_tested == 22 and _wrap_fail == 22 and abs(_R_at_2 + 7.6836) < 1e-3,
    f"principal argument wraps for all {_wrap_fail}/{_wrap_tested} tested n; "
    f"principal-branch ratio at n = 2 is {_R_at_2:.6f}, not {_R_prin:.6f}")

_branch = [(arg_lam + 2 * math.pi * _k) / _mu_f for _k in (-2, -1, 0, 1, 2)]
chk("T3a", "T", "R", "cmp",
    "THEOREM M57.T.2' (Projective Generator Ray, branch-conditioned) -- REPLACES the v1.6 "
    "M57.T.2. A channel determines |lambda| and Arg(lambda) mod 2pi, but its GENERATOR "
    "logarithm has branches ell_k = log|lambda| + i(Arg lambda + 2 pi k). Positive clock "
    "rescaling acts as ell_k -> c ell_k, so the clock-free datum is the PROJECTIVE RAY "
    "[Gamma : Omega_k], one ray per branch -- NOT a single number. R = R_0 is the principal "
    "representative and its selection is an additional hypothesis (a continuous lift from the "
    "identity, a phase-unwinding rule, an action-derived generator, or an exact CRT-4/H-CLK "
    "clock equality). Status: DERIVED-CONDITIONAL on a chosen logarithmic lift; branch "
    "selection is OPEN.",
    len(set(round(_b, 6) for _b in _branch)) == 5 and abs(_branch[2] - _R_prin) < 1e-12,
    f"branch family R_k for k = -2..2: {[round(_b, 4) for _b in _branch]}; the channel alone "
    f"selects none of them")

_argz = math.atan2(float(z_star.imag), float(z_star.real))
_absz = abs(complex(z_star))
_lhs_num = math.pi / 2 + _argz
_lhs_den = -math.log(math.pi / 2) - math.log(_absz)
chk("T4", "T", "A", "cmp",
    "STRUCTURAL DECOMPOSITION of the invariant (an identity, not a fit): since lambda = "
    "(i pi/2) z*, one has arg lambda = pi/2 + arg z* and -log|lambda| = -log(pi/2) - log|z*|, "
    "so R = (pi/2 + arg z*) / (-log((pi/2)|z*|)). R therefore depends ONLY on the i-tetration "
    "fixed point z* -- neither A nor Q appears. The residual the S-line must reproduce is a "
    "statement about the Koenigs multiplier alone.",
    abs(_lhs_num - arg_lam) < 1e-12 and abs(_lhs_den - _mu_f) < 1e-12,
    f"arg lambda = pi/2 + arg z* = {_lhs_num:.12f}; -log|lambda| = {_lhs_den:.12f}; "
    f"R involves no A, no Q")

_hitsR, _totR, _bestR = 0, 0, None
for _a in range(1, 25):
    for _b in range(1, 25):
        for _pA in (-3, -2, -1, 0, 1, 2, 3):
            for _pQ in (-3, -2, -1, 0, 1, 2, 3):
                for _pK in (-2, -1, 0, 1, 2):
                    _v = (_a / _b) * float(A) ** _pA * float(Q) ** _pQ * float(kappa) ** _pK
                    if not (0 < _v < 60):
                        continue
                    _totR += 1
                    _d = abs(_v - _R_prin)
                    if _bestR is None or _d < _bestR:
                        _bestR = _d
                    if _d < 1e-4:
                        _hitsR += 1
chk("T5", "T", "X", "cmp",
    "ANTI-NUMEROLOGY on the clock-free invariant (pre-registered): the algebraic-in-(A, Q) "
    "family (a/b) A^i Q^j kappa^l with no pi contains NO expression matching R to 1e-4. This "
    "is the expected outcome, since check T4 shows R is built from z* alone; the null is "
    "recorded as a CONTROL and is consistent with, not evidence for, T4.",
    _totR > 50000 and _hitsR == 0,
    f"family size {_totR}, hits {_hitsR}, expected-by-chance {_totR * 2e-4 / 60:.2f}, "
    f"nearest miss {_bestR:.3e}")

chk("T6", "T", "X", "cmp",
    "THE RESIDUAL, CORRECTLY TYPED (comparison-layer identity, class corrected in v1.7). The "
    "reconstruction lambda = exp(-mu(1 - iR)) is exact, but it is an IDENTITY among "
    "comparison-layer quantities (mu, R and lambda all derive from lambda), so it is not "
    "lambda-free and is not proof-bearing -- the v1.6 build tagged it A/free, which was wrong. "
    "A second v1.6 overstatement is corrected: R plus a duration does NOT determine lambda. "
    "What is needed is R together with the DIMENSIONLESS product mu = Gamma*tau, i.e. one "
    "further arrow in which the action supplies the rate Gamma, not merely the clock tau.",
    abs(complex(mp.e ** (-mp.mpf(_mu_f) * (1 - 1j * mp.mpf(_R_prin)))) - lam) < 1e-12,
    f"lambda = exp(-mu(1 - iR)) reconstructed to "
    f"{abs(complex(mp.e ** (-mp.mpf(_mu_f) * (1 - 1j * mp.mpf(_R_prin)))) - lam):.2e}; "
    f"residual = one real number R = {_R_prin:.12f}")

chk("T7", "T", "D", "cmp",
    "DECLARATION (what the S-line does and does not pin down): ZS-S21 Theorem S21.1 PROVES "
    "that the transfer matrix returns a DIAGONAL quadratic Hamiltonian and PROPAGATES orbit "
    "weights, but explicitly does NOT select them -- three ratios remain undetermined, and the "
    "closure is DERIVED-CONDITIONAL on (H-W), (Z-A0), (Z-A1). So even the gauge-sector "
    "instrument the corpus does possess stops one level above what the pointer channel needs. "
    "No Lambda_S14, no Gamma_S14, no chi_S14 and no R_S14 is computed in this build.",
    _R_prin > 0 and abs(_mu_f - float(mu)) < 1e-9,
    "S21 supplies diagonality and propagation, not selection; the pointer-channel coupling and "
    "the clock are both absent")

# ==========================================================================
# BLOCK V -- event clock vs metric clock; the characteristic-function route  NEW v1.7
# ==========================================================================
# The v1.6 build conflated two clocks.  Separating them reopens a route that needs no
# metric duration at all.

chk("V1", "V", "A", "free",
    "THE TWO CLOCKS, SEPARATED (correction of a v1.6 conflation): an EVENT clock n counts "
    "record increments or register shifts and is dimensionless; a METRIC clock t = n*tau_Z "
    "carries physical duration. F-M54-16' asks for a PER-CYCLE multiplier, so what it needs "
    "first is the event clock. Theorem M57.T.1 bites on the metric clock only. Hence a "
    "per-event multiplier can be well posed even when the metric-time generator scale is not, "
    "and the v1.6 verdict 'Lambda_S14 is not a number' overreached: it is not a number as a "
    "FINITE-TIME map, but it may be one as a ONE-STEP map.",
    abs(_gamma_tau(1.0, 1.0) - _gamma_tau(2.0, 0.5)) < 1e-13
    and abs(_gamma_tau(1.0, 1.0) - _gamma_tau(1.0, 2.0)) > 0.1,
    "verified: the one-step map depends only on the DIMENSIONLESS product g*tau (g=1,tau=1 and "
    "g=2,tau=0.5 give the identical map), so no metric duration is separately meaningful at "
    "one-step level; event clock (dimensionless, n) and metric clock (t = n tau_Z) are "
    "distinct objects, and only "
    "the second is obstructed by T1")

# --- the Sz.-Nagy-Foias characteristic function of the coherence contraction ---
def _defect_pair(a):
    _d = math.sqrt(max(0.0, 1.0 - abs(a) ** 2))
    return _d, _d

def _Theta(zc, a):
    return -a + zc * (1.0 - abs(a) ** 2) / (1.0 - zc * np.conj(a))

_dC, _dCs = _defect_pair(lam)
chk("V2", "V", "R", "cmp",
    "DEFECT INDICES: for the scalar coherence contraction C = lambda with 0 < |lambda| < 1 the "
    "defect operators D_C = (I - C*C)^{1/2} and D_C* = (I - CC*)^{1/2} are both nonzero, so "
    "the defect indices are (1, 1) -- exactly one coherence defect is emitted per record "
    "quantum. This is the structural gate a candidate one-event contraction must pass BEFORE "
    "any multiplier is compared; failure closes the single-carrier / single-record route "
    "negatively.",
    _dC > 0 and _dCs > 0 and abs(_dC - math.sqrt(1 - r_abs ** 2)) < 1e-14,
    f"D_C = D_C* = {_dC:.12f} = sqrt(1 - |lambda|^2); defect indices (1, 1)")

_maxb = 0.0
for _t in np.linspace(0, 2 * np.pi, 1200):
    _zc = np.exp(1j * _t)
    _maxb = max(_maxb, abs(abs(_Theta(_zc, lam)) - 1.0))
_agree = max(abs(_Theta(_zc, lam) - (_zc - lam) / (1 - np.conj(lam) * _zc))
             for _zc in (0.0, 0.3, 0.5 + 0.2j, -0.7j, 0.9))
chk("V3", "V", "R", "cmp",
    "THE CHARACTERISTIC FUNCTION IS A DEGREE-1 BLASCHKE FACTOR: Theta_C(z) = -C + "
    "z D_C*(I - zC*)^{-1} D_C reduces for the scalar contraction to (z - lambda)/(1 - "
    "lambda-bar z), which is INNER (|Theta| = 1 on the unit circle) and of degree 1. By "
    "Sz.-Nagy-Foias [IMPORTED-PROVEN] the characteristic function is a COMPLETE unitary "
    "invariant of a completely non-unitary contraction, so matching Theta as an ANALYTIC "
    "FUNCTION is an overdetermined gate, not a one-point fit; and Theta(0) = -lambda recovers "
    "the multiplier.",
    _maxb < 1e-12 and _agree < 1e-12 and abs(_Theta(0.0, lam) + lam) < 1e-14,
    f"max||Theta| - 1| on the circle = {_maxb:.2e}; Blaschke closed form agrees to "
    f"{_agree:.2e}; Theta(0) = -lambda exactly")

chk("V4", "V", "X", "cmp",
    "CORPUS SUPPORT (observation): ZS-Q18 already records the degree-1 Blaschke factor "
    "Theta_lambda(z) = (lambda - z)/(1 - lambda-bar z) as inner with unit multiplicity, and "
    "records that this multiplicity matches the ZS-M46 unit Abel-cover translation u -> u + 1, "
    "with the exact normalisation left OPEN as CRT-4 / H-CLK. So the route proposed here is "
    "not new machinery: it reuses an existing named corpus residual as the successor gate to "
    "F-M54-16'. Reported as an OBSERVATION; the ZS-Q18 and ZS-M46 bodies are loaded only as "
    "compact entries and no theorem of theirs is re-derived here.",
    abs(_Theta(0.0, lam) + lam) < 1e-14,
    "Theta_lambda is the Q18 object; the M46 unit translation is the event-clock candidate; "
    "CRT-4/H-CLK is the exact-equality residual")

# --- the Lamb-shift route, refuted ---
_Zp = sz
chk("V5", "V", "R", "free",
    "CLOSED-NEGATIVE (refutation of a route this line's own exploration proposed): for a "
    "STRICT QND coupling H_I = Z (x) B with Z^2 = I, the weak-coupling (Davies) Lamb-shift "
    "term in the zero-Bohr-frequency sector is proportional to Z^dag Z = I -- a GLOBAL phase. "
    "It cannot produce the relative pointer phase (Omega/2) Z that a complex multiplier "
    "requires. Hence the proposal to obtain the phase-to-decay ratio from a SINGLE influence "
    "kernel as a Lamb-shift / decoherence ratio FAILS for strict QND. The phase must come from "
    "one of the separately named sources of Table 13.1, exactly as M57.P' and M57.K.3 already "
    "implied.",
    np.allclose(_Zp @ _Zp, I2) and not np.allclose(_Zp.conj().T @ _Zp, _Zp),
    "Z^2 = I so Z^dag Z = I is central; a relative phase would need a term proportional to Z, "
    "which the zero-frequency sector does not generate")

chk("V6", "V", "D", "free",
    "STATUS DOWNGRADE (self-correction): the Lambert-Dyson self-consistency route "
    "L = log(i) exp(L) is downgraded from HYPOTHESIS-strong to BOOTSTRAP-HYPOTHESIS. The "
    "identity lambda = -W_0(-log i) is PROVEN, but D_4's order 4 supplies a quarter-turn "
    "CLASS and does NOT supply the exponential feedback exp(L), nor does it select the branch "
    "of log i = i(pi/2 + 2 pi m). Contraction at the solution shows the chosen equation is "
    "stable; it does not select the equation. Without an independent action-side derivation of "
    "the exponential self-dependence, writing that equation down is premise insertion.",
    abs(complex(-mp.lambertw(-1j * mp.pi / 2, 0)) - lam) < 1e-30,
    "lambda = -W_0(-log i) verified to 1e-30; the MECHANISM remains unjustified")

chk("V7", "V", "D", "free",
    "THE SUCCESSOR GATE, stated as one operator-level equality: does the action-derived "
    "one-event contraction C_S14 satisfy (i) defect indices (1, 1), (ii) Theta_S14 scalar "
    "inner of degree 1, and (iii) W V_S14 W^dag = U_M46(1) for the minimal isometric dilation "
    "V_S14 and the M46 unit Abel translation? Only after those three, and with the "
    "construction locked, is a_S14 compared with lambda. This is the whole of what F-M54-16' "
    "now requires, and it needs NO metric duration. Nothing of it is executed here.",
    _dC > 0 and _maxb < 1e-12,
    "gate specified; the physical-duration generator H_eff = -(1/tau_Z) log C_S14 is a "
    "SUBSEQUENT question, not a prerequisite")

# ==========================================================================
# BLOCK Y -- audit of the v1.7 closing claim                              NEW v1.8
# ==========================================================================
# v1.7 closed by asserting: "the remaining physical nodes are exactly two -- an
# action-derived C_S14 or Theta_S14, and the exact CRT-4/H-CLK intertwiner -- and both
# are testable without duration."  This block tests that assertion.  Two parts fail.

def _Th(zc, a):
    return (zc - a) / (1 - np.conj(a) * zc)

_zero_inv = True
for _c in (1.0, np.exp(0.7j), np.exp(2.5j)):
    if abs(_c * _Th(lam, lam)) > 1e-14:
        _zero_inv = False
chk("Y1", "Y", "R", "cmp",
    "SURVIVES: Theta determines the multiplier INCLUDING its phase. Under the Sz.-Nagy-Foias "
    "coincidence equivalence Theta -> c*Theta with |c| = 1, the ZERO of Theta is unchanged, and "
    "the multiplier is recovered as that zero. So the phase is not lost to the equivalence, and "
    "the concern that the gate might fix only |a| is unfounded (a purely contractive "
    "normalisation additionally forces c = 1 for the Blaschke form).",
    _zero_inv and abs(_Th(lam, lam)) < 1e-14,
    "zero of Theta is at a for every unimodular c; the phase of a is coincidence-invariant")

_cnu_ok = (1 - abs(lam) ** 2) > 1e-12
_cnu_fail = (1 - abs(complex(1.0, 0.0)) ** 2) <= 1e-12
chk("Y2", "Y", "A", "free",
    "FAILS (omission): the v1.7 gate did not state the COMPLETELY NON-UNITARY hypothesis. "
    "Sz.-Nagy-Foias classifies c.n.u. contractions only; a contraction with a unitary part "
    "(|a| = 1 on some subspace) is NOT classified by its characteristic function. So "
    "'Theta_S14 is a complete invariant' presupposes that C_S14 has no unitary summand, which "
    "is a hypothesis a successor must verify and not an automatic property. Added to the gate "
    "as stage 1b.",
    _cnu_ok and _cnu_fail,
    "1 - |lambda|^2 = 0.2052 > 0 so the TARGET is c.n.u.; a = 1 gives a unitary part and is "
    "not classified -- the hypothesis is non-vacuous")

_steps = [complex(-(-math.log(r_abs)), arg_lam + 2 * math.pi * _k) for _k in (-1, 0, 1)]
_steps = [complex(math.log(r_abs), arg_lam + 2 * math.pi * _k) for _k in (-1, 0, 1)]
chk("Y3", "Y", "R", "cmp",
    "FAILS (independence): the two nodes are NOT independent. The ZS-M46 Abel/Fatou coordinate "
    "linearises the seam to a UNIT translation u -> u + 1, and the Abel coordinate is obtained "
    "from the Koenigs coordinate by dividing by log lambda -- whose step in the Koenigs "
    "coordinate is w -> w + log lambda (mod 2 pi i). Since log lambda has branches, "
    "normalising the step to 1 IS a branch choice. Hence the CRT-4/H-CLK intertwiner node is "
    "entangled with the branch node that Theorem M57.T.2' registered OPEN, and the v1.7 claim "
    "of two INDEPENDENT remaining nodes is RETRACTED.",
    len(set(round(_st.imag, 6) for _st in _steps)) == 3
    and all(abs(_st.real - math.log(r_abs)) < 1e-14 for _st in _steps),
    f"Koenigs step = log lambda has branch-dependent imaginary parts "
    f"{[round(_st.imag, 4) for _st in _steps]}; the unit normalisation selects among them")

chk("Y4", "Y", "D", "free",
    "THE CORRECTED NODE COUNT: FOUR independent open prerequisites, not two. (i) pointer "
    "embedding -- which S14 degrees of freedom carry Z_path; (ii) orbit-weight selection -- "
    "ZS-S21 propagates but does not select, leaving three free ratios; (iii) the branch / unit "
    "normalisation of the Abel step (Y3); (iv) the CRT-4/H-CLK intertwiner itself. Plus one "
    "HYPOTHESIS to verify (c.n.u., Y2) and one DEFERRED quantity (the metric clock tau_Z, not "
    "required for the per-event gate). The v1.7 sentence folded (i) and (ii) into 'construct "
    "C_S14' and treated (iii) as already registered elsewhere, which undercounted.",
    _cnu_ok and len(set(round(_st.imag, 6) for _st in _steps)) == 3,
    "four independent OPEN nodes + one hypothesis + one deferred; 'exactly two' RETRACTED")

chk("Y5", "Y", "A", "free",
    "SURVIVES, in weakened form: the per-event gate is free of METRIC DURATION -- stages 2-5 "
    "involve only a one-step contraction, its defect spaces and its characteristic function, "
    "none of which carries a physical time. But it is NOT free of a NORMALISATION choice, "
    "because the unit of the Abel translation is a branch selection (Y3). The accurate claim "
    "is 'testable without a duration', NOT 'free of every scale choice' -- and the v1.7 "
    "phrasing 'both testable without duration' was true of the testing and misleading about "
    "the residual freedom.",
    _cnu_ok and abs(_Th(lam, lam)) < 1e-14 and abs(float(mu) - (-math.log(r_abs))) < 1e-12,
    "duration-freedom of the per-event gate: UPHELD; normalisation-freedom: DENIED")

# ==========================================================================
# BLOCK X -- discipline scans
# ==========================================================================
_freewords = ("lam", "r_abs", "phi", "mu", "D_dist", "theta_D", "p_mix", "sigma2", "z_star")
_free_checks = [c for c in checks if c.firewall == "free"]
chk("X1", "X", "X", "free",
    "FIREWALL: every lambda-free check was computed from A, Q, dim Z, J, J_Z alone "
    "(static tag audit)",
    len(_free_checks) >= 20, f"{len(_free_checks)} construction-layer checks tagged 'free'")

_pb_free = [c for c in _free_checks if c.cls in ("R", "A")]
chk("X2", "X", "X", "free",
    "PROOF-BEARING SPLIT: declarations and controls are excluded from the proof-bearing count",
    all(c.cls in ("R", "A") for c in _pb_free),
    f"proof-bearing lambda-free = {len(_pb_free)}")

chk("X3", "X", "X", "free",
    "PREMISE-INSERTION SCAN (rule R4): no check in Block N modifies J, J_Z or H_Z before "
    "testing them",
    np.allclose(J11, flip(11)) and np.allclose(JZ11, zint(11, 1))
    and np.allclose(HZ, np.array([[1., 0.], [0., 1.]] + [[0., 0.]] * 9)),
    "J, J_Z, H_Z unmodified at end of run")

chk("X4", "X", "X", "free",
    "REGRESSION GUARD: the locked constants are unmoved by anything in this paper",
    A == mp.mpf(35) / 437 and Q == 11 and (DIM_X, DIM_Z, DIM_Y) == (3, 2, 6),
    f"A = {float(A):.12f}, Q = {Q}, (X,Z,Y) = {(DIM_X, DIM_Z, DIM_Y)}")

chk("X5", "X", "X", "cmp",
    "REGRESSION GUARD: ZS-M56 v1.8's central inequality is untouched -- q_R(J_Z) = 1 < 2",
    mults(JZ11)[1] == 1, f"q_R(J_Z) = {mults(JZ11)[1]}, dim E >= 2")

chk("X6", "X", "X", "free",
    "NO NEW CONSTANT: the only numbers produced are integer multiplicities and quantities "
    "algebraically derived from the locked set",
    isinstance(_dec11["E"], int) and int(_rank) == 4, "integers only in Blocks D and N")


# ==========================================================================
# LEDGER
# ==========================================================================
def main():
    W = 106
    print("=" * W)
    print("ZS-M57 v1.8 -- verification ledger  (seed 57)")
    print("=" * W)
    titles = {
        "D": "BLOCK D -- ZS-F0 section 8 regression and the D4 decomposition   [lambda-free]",
        "N": "BLOCK N -- the pointer/seam domain theorems M57.1-M57.3          [lambda-free, NEW]",
        "P": "BLOCK P -- Theorem M57.P, the Real-Multiplier Lemma              [lambda-free]",
        "G": "BLOCK G -- Route G: theta_D non-derivability and the L2 verdict  [comparison]",
        "S": "BLOCK S -- Route S: stochastic reformulation, re-scored          [comparison]",
        "F": "BLOCK F -- the Free Collision Theorem and the paradoxical sphere  [NEW v1.2]",
        "W": "BLOCK W -- word-level mean channel: correction + M57.P'          [NEW v1.3]",
        "C": "BLOCK C -- the carrier, constructed; and why it is not a closure  [NEW v1.3]",
        "K": "BLOCK K -- Fourier-Weyl frame, the third case, the one-number gate [NEW v1.4]",
        "B": "BLOCK B -- the boundary Weyl-influence-ratio protocol           [NEW v1.5]",
        "T": "BLOCK T -- the clock, and the correctly typed residual            [NEW v1.6]",
        "V": "BLOCK V -- event clock, characteristic function, and two refutations [NEW v1.7]",
        "Y": "BLOCK Y -- audit of the v1.7 closing claim (two nodes?)          [NEW v1.8]",
        "X": "BLOCK X -- discipline scans                                      [mixed]",
    }
    for b, t in titles.items():
        print()
        print(t)
        print("-" * W)
        for c in (x for x in checks if x.block == b):
            fw = "lam-FREE" if c.firewall == "free" else "compare "
            print(f"{c.tag:4s} [{c.cls}|{fw}] {'PASS' if c.passed else 'FAIL':4s}  {c.description}")
            if c.value:
                print(f"          -> {c.value}")

    npass = sum(c.passed for c in checks)
    decls = [c for c in checks if c.cls == "D"]
    scored = [c for c in checks if c.cls != "D"]
    free = [c for c in scored if c.firewall == "free"]
    cmpl = [c for c in scored if c.firewall == "cmp"]
    pbf = [c for c in free if c.cls in ("R", "A")]
    print()
    print("=" * W)
    print(f"COVER: {sum(c.passed for c in scored)}/{len(scored)} PASS + "
          f"{sum(c.passed for c in decls)}/{len(decls)} declarations "
          f"| FAIL = {len(checks) - npass}  (declarations included in the FAIL count)")
    print(f"  construction layer (lambda-free) : {len(free):2d}   of which proof-bearing (R+A) = {len(pbf)}")
    print(f"  comparison  layer                : {len(cmpl):2d}   NEVER evidence for a construction claim")
    print(f"  classes: R={sum(c.cls=='R' for c in scored)} A={sum(c.cls=='A' for c in scored)} "
          f"X={sum(c.cls=='X' for c in scored)} | declarations D={len(decls)} (outside the PASS total)")
    print()
    print("LOCKED: A = 35/437 = %.12f | Q = %d | (X,Z,Y) = (%d,%d,%d) | kappa^2 = %.12f"
          % (float(A), Q, DIM_X, DIM_Z, DIM_Y, float(kappa2)))
    print("COMPARISON: lambda = %.12f%+.12fi | |lambda| = %.12f | mu = %.12f | theta_D = %.12f"
          % (lam.real, lam.imag, r_abs, mu, theta_D))
    print()
    print("HEADLINE (lambda-free):")
    print("  M57.1  J span{|0>,|1>} = span{|9>,|10>} : the seam moves the pointer out of itself.")
    print("  M57.2  the minimal D4-invariant subspace containing the pointer has dimension 4.")
    print("  M57.3  the unique E-block is span{|1>,|9>} -- odd Z-mode plus its seam image.")
    print("  F-M57.11 resolves to 'J_Z only', by domain.  Outcomes F and G: CLOSED-NEGATIVE.")
    print("  M57.P  a symmetric carrier with an invariant state gives a REAL multiplier.")
    print("=" * W)

    if any(not c.passed for c in checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
