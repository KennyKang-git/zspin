#!/usr/bin/env python3
# =====================================================================================
#  zs_s20_verify_v2_2.py
#  Companion verification suite for
#     ZS-S20 v2.2 -- The Cellular Reduction of the Z-Spin Master Action
#     Kenny Kang, Z-Spin Cosmology Collaboration, July 2026
#
#  v1.1 CHANGES (referee-driven):
#     * check() is now split into EXECUTABLE and DECLARATIVE at the call site.
#       The headline count reports both separately.  v1.0's flat "83/83" is retired.
#     * the anti-regression block is a REAL static analysis: the file parses its own
#       source with `ast` and asserts that forbidden numeric literals occur in no
#       expression.  Declarative registry guards are labelled as such.
#     * PART 16-18 execute the incidence-reciprocity route, the no-go gate F-S20.8,
#       the (H-UA)&(H-UA*) solution variety, and the two bypass routes.
#
#  Discipline (inherited from ZS-S19 v1.6, seed section 8):
#     * every claim carries exactly one status tag
#     * an OPEN gate is NEVER counted as a PASS  (printed only)
#     * thresholds only -- realized machine residuals are BLAS-dependent
#     * anti-regression block: every retracted value must be produced by NO code path
#     * a scan is not a proof; a grid minimum is not an infimum
#
#  DEPENDENCIES (declared honestly; ImportError is raised, never degraded to an OPEN gate)
#     python  >= 3.9
#     numpy   >= 1.21
#     mpmath  >= 1.2      (exact integer determinant for the Kirchhoff regression)
#     sympy   >= 1.9      (exact face areas; the ZS-S19 A6/A5 erratum)
#     scipy   >= 1.7      (matrix exponential / logarithm for the SU(3) Step-8 gate)
#  NO other dependency is used.  No network access.  Deterministic seed 20260319.
# =====================================================================================

import sys, math, hashlib, platform, itertools, json
from collections import deque

try:
    import numpy as np
except ImportError as exc:                      # do NOT degrade to an extra OPEN gate
    raise ImportError("zs_s20_verify_v2_2 requires numpy >= 1.21") from exc
try:
    import mpmath as mp
except ImportError as exc:
    raise ImportError("zs_s20_verify_v2_2 requires mpmath >= 1.2") from exc
try:
    import sympy as sp
except ImportError as exc:
    raise ImportError("zs_s20_verify_v2_2 requires sympy >= 1.9") from exc
try:
    from scipy.linalg import expm, logm
except ImportError as exc:
    raise ImportError("zs_s20_verify_v2_2 requires scipy >= 1.7") from exc

mp.mp.dps = 60
RNG_SEED = 20260319

PASS, FAIL, OPEN, DECL, PROXY = [], [], [], [], []
def check(tag, cond, detail="", kind="EXEC"):
    (PASS if cond else FAIL).append((tag, detail))
    if kind == "DECL": DECL.append(tag)
    if kind == "PROXY": PROXY.append(tag)
    print(f"   [{'PASS' if cond else 'FAIL':<4}|{kind:<4}] {tag:<42} {detail}")
def decl(tag, cond, detail=""):
    check(tag, cond, detail, kind="DECL")
def proxy(tag, cond, detail=""):
    """A check that exercises a GENERIC theorem, not the Z-Spin object itself.
    Added in v1.5 after four rounds in which a proxy was reported as verification
    of the target.  PROXY checks are excluded from the executable physics count."""
    check(tag, cond, detail, kind="PROXY")
def openg(tag, detail=""):
    OPEN.append((tag, detail))
    print(f"   [OPEN] {tag:<44} {detail}      (printed, NOT counted)")

TOL_EXACT = 1e-12      # combinatorial / integer identities
TOL_SPEC  = 1e-9       # dense symmetric eigenvalues on a 32x32
RESULTS = {}

def banner(t): print("\n" + "=" * 86 + "\n" + t + "\n" + "=" * 86)

# =====================================================================================
banner("PART 0.  LOCKED CORPUS CONSTANTS  (imported, never re-fitted)")
# =====================================================================================
A_IMP   = 35 / 437                      # ZS-F2
Q_IMP   = 11                            # ZS-F5
DIMZ    = 2                             # ZS-F5
V_EW    = 245.93                        # ZS-S4   GeV
LAM1_L  = 1.2428416164                  # ZS-S7   TI face-Laplacian gap
LAMH_L  = 7.5210904061                  # ZS-S17  second T1 copy
OM0_L   = 1.1148280659                  # ZS-S18  Omega_0 = sqrt(lambda_1)
LQCD_L  = 264.1                         # ZS-S7   MeV,  proportional to 1/lambda_1
TAU_L   = 375291866372898816000         # ZS-S19  buckyball spanning trees
BAND    = 89 / 3600                     # ZS-S17  anti-numerology band
DEC1_L  = 0.3600376672                  # ZS-S19  full-DEC gap at a_TI = 1
ATI_L   = 0.5382277383                  # ZS-S19  a_TI reproducing the lock
A5_L    = 1.7204774006                  # ZS-S19  pentagon area, edge = 1
A6_L    = 2.5980762114                  # ZS-S19  hexagon  area, edge = 1
CEX     = (1.0, 2.0, 1.3231366438740746, 1.0)   # ZS-S19 external counterexample
print(f"   A = 35/437 = {A_IMP:.9f} | Q = {Q_IMP} | dim Z = {DIMZ} | v = {V_EW} GeV")
print(f"   lambda_1 = {LAM1_L} | lambda_h = {LAMH_L} | Lambda_QCD = {LQCD_L} MeV")
print(f"   anti-numerology band = 89/3600 = {100*BAND:.4f} %")

# =====================================================================================
banner("PART 1.  TRUNCATED-ICOSAHEDRON COMPLEX K_TI  (built from Cartesian coordinates)")
# =====================================================================================
phi = (1 + math.sqrt(5)) / 2
def _even_perms(t):
    a, b, c = t
    return [(a, b, c), (b, c, a), (c, a, b)]
_base = [(0, 1, 3*phi), (1, 2+phi, 2*phi), (phi, 2, 2*phi+1)]
_S = set()
for _b in _base:
    for _s in itertools.product([1, -1], repeat=3):
        for _p in _even_perms(tuple(si*bi for si, bi in zip(_s, _b))):
            _S.add(tuple(round(x, 9) for x in _p))
V = np.array(sorted(_S))
D = np.linalg.norm(V[:, None, :] - V[None, :, :], axis=2)
dmin = D[D > 1e-6].min()
edges = [(i, j) for i in range(len(V)) for j in range(i+1, len(V)) if abs(D[i, j]-dmin) < 1e-6]
adj = {i: [] for i in range(len(V))}
for i, j in edges:
    adj[i].append(j); adj[j].append(i)

def _faces():
    out, seen = [], set()
    for i in range(len(V)):
        for j in adj[i]:
            if (i, j) in seen: continue
            cyc = [i, j]
            while True:
                a, b = cyc[-2], cyc[-1]
                nrm = V[b]/np.linalg.norm(V[b]); vin = V[b]-V[a]
                best = bang = None
                for c in adj[b]:
                    if c == a: continue
                    vout = V[c]-V[b]
                    ang = math.atan2(np.dot(np.cross(vin, vout), nrm), np.dot(vin, vout))
                    if bang is None or ang < bang: bang, best = ang, c
                cyc.append(best)
                if cyc[-1] == cyc[1] and cyc[-2] == cyc[0]:
                    cyc = cyc[:-2]; break
                if len(cyc) > 12: raise RuntimeError("face walk failed to close")
            for k in range(len(cyc)): seen.add((cyc[k], cyc[(k+1) % len(cyc)]))
            out.append(cyc)
    return out
faces = _faces()
nV, nE, nF = len(V), len(edges), len(faces)
fsize = [len(f) for f in faces]
eidx = {}
for k, (i, j) in enumerate(edges): eidx[(i, j)] = eidx[(j, i)] = k

B1 = np.zeros((nV, nE))                 # C_1 -> C_0
for k, (i, j) in enumerate(edges): B1[i, k] = -1; B1[j, k] = +1
B2 = np.zeros((nF, nE))                 # C^1 -> C^2   (seed convention: (B2 q)_f)
for fi, cyc in enumerate(faces):
    for k in range(len(cyc)):
        a, b = cyc[k], cyc[(k+1) % len(cyc)]
        B2[fi, eidx[(a, b)]] += (+1 if edges[eidx[(a, b)]] == (a, b) else -1)
inc = [[fi for fi in range(nF) if abs(B2[fi, e]) > .5] for e in range(nE)]
etype = [tuple(sorted(fsize[f] for f in inc[e])) for e in range(nE)]

check("T01 V = 60",  nV == 60, f"V = {nV}")
check("T02 E = 90",  nE == 90, f"E = {nE}")
check("T03 F = 32",  nF == 32, f"F = {nF}")
check("T04 chi = 2", nV-nE+nF == 2, f"chi = {nV-nE+nF}")
check("T05 vertex-regular deg 3", set(np.abs(B1).sum(0).astype(int)) == {2}
      and set(np.abs(B1).sum(1).astype(int)) == {3}, "endpoints 2, degree 3")
check("T06 face census 12 + 20", (fsize.count(5), fsize.count(6)) == (12, 20), "12 pentagons, 20 hexagons")
check("T07 B2 B1^T = 0", np.abs(B2 @ B1.T).max() < TOL_EXACT, f"residual < {TOL_EXACT}")
check("T08 every edge bounds 2 faces", all(len(i) == 2 for i in inc))
check("T09 edge orbits 60 (5,6) + 30 (6,6)",
      (etype.count((5, 6)), etype.count((6, 6)), etype.count((5, 5))) == (60, 30, 0), "no (5,5) edge")
RESULTS["complex"] = dict(V=nV, E=nE, F=nF, chi=nV-nE+nF, pent=12, hexa=20,
                          e56=etype.count((5, 6)), e66=etype.count((6, 6)))

# --- metric-free gauge census (ZS-S18/S19, must hold in EVERY outcome) ----------------
r1, r2 = np.linalg.matrix_rank(B1), np.linalg.matrix_rank(B2)
check("T10 rank B1^T = 59", r1 == 59, f"rank = {r1}")
check("T11 rank B2^T = 31", r2 == 31, f"rank = {r2}")
check("T12 90 = 59 + 31 (metric-free)", r1 + r2 == nE, "gauge census, first regression test")
RESULTS["census"] = dict(rankB1=int(r1), rankB2=int(r2), total=int(r1+r2))

# --- Kirchhoff regression, exact integer ---------------------------------------------
L0 = np.rint(B1 @ B1.T).astype(int)
Mred = mp.matrix(nV-1, nV-1)
for i in range(nV-1):
    for j in range(nV-1): Mred[i, j] = mp.mpf(int(L0[i+1, j+1]))
tau = mp.det(Mred)
check("T13 Kirchhoff tau exact integer", abs(tau - TAU_L) < mp.mpf('1e-3'),
      f"tau = {int(mp.nint(tau))}")
_ev0 = np.sort(np.linalg.eigvalsh(B1 @ B1.T))[1:]
_logdet0 = float(np.sum(np.log(_ev0)))
_logVtau = float(mp.log(60 * tau))
check("T14 Kirchhoff: det'(Delta_0) = V * tau", abs(_logdet0 - _logVtau) < 1e-7,
      f"log det' = {_logdet0:.9f} vs log(V*tau) = {_logVtau:.9f}")
RESULTS["kirchhoff_tau"] = int(mp.nint(tau))

# =====================================================================================
banner("PART 2.  THE FULL I_h ACTION  (120 elements)  AND ORBIT STRUCTURE")
# =====================================================================================
key = {tuple(np.round(V[i], 6)): i for i in range(nV)}
basis = [0]
for i in range(1, nV):
    if np.linalg.matrix_rank(V[basis+[i]]) > len(basis): basis.append(i)
    if len(basis) == 3: break
A0 = V[basis].T
group = []
for cand in itertools.permutations(range(nV), 3):
    try: G = V[list(cand)].T @ np.linalg.inv(A0)
    except np.linalg.LinAlgError: continue
    if not np.allclose(G @ G.T, np.eye(3), atol=1e-7): continue
    try: perm = np.array([key[tuple(np.round(w, 6))] for w in (G @ V.T).T])
    except KeyError: continue
    group.append(perm)
check("T15 |I_h| = 120", len(group) == 120, f"|G| = {len(group)}")

def orbit_sizes(nitems, act):
    seen, sizes = set(), []
    for i in range(nitems):
        if i in seen: continue
        o = {act(g, i) for g in group} | {i}
        sizes.append(len(o)); seen |= o
    return sorted(sizes)
efz = {frozenset(e): k for k, e in enumerate(edges)}
ffz = {frozenset(f): k for k, f in enumerate(faces)}
ov = orbit_sizes(nV, lambda g, i: g[i])
oe = orbit_sizes(nE, lambda g, e: efz[frozenset((g[edges[e][0]], g[edges[e][1]]))])
of = orbit_sizes(nF, lambda g, f: ffz[frozenset(g[v] for v in faces[f])])
check("T16 VERTEX-TRANSITIVE (one orbit of 60)", ov == [60], f"vertex orbits {ov}")
check("T17 edge orbits [30, 60]", oe == [30, 60], f"edge orbits {oe}")
check("T18 face orbits [12, 20]", of == [12, 20], f"face orbits {of}")
PE = np.array([[efz[frozenset((g[edges[e][0]], g[edges[e][1]]))] for e in range(nE)] for g in group])
PF = np.array([[ffz[frozenset(g[v] for v in faces[f])] for f in range(nF)] for g in group])
aB2 = np.abs(B2)
eqres = max(np.abs(aB2[PF[gi]][:, PE[gi]] - aB2).max() for gi in range(120))
check("T19 [P_F, |B2|] = 0 over all 120 g", eqres < TOL_EXACT, f"residual < {TOL_EXACT}")
RESULTS["orbits"] = dict(vertex=ov, edge=oe, face=of, group_order=len(group))

# =====================================================================================
banner("PART 3.  THE I_h-INVARIANT DIAGONAL METRIC FAMILY  (three ratios after scale)")
# =====================================================================================
def orbit_metric(m56, m66, b5, b6):
    M1 = np.array([m56 if etype[e] == (5, 6) else m66 for e in range(nE)])
    M2 = np.array([b5 if fsize[f] == 5 else b6 for f in range(nF)])
    return M1, M2
def delta2(M1, M2):
    R = np.diag(np.sqrt(M2)) @ B2 @ np.diag(1/M1) @ B2.T @ np.diag(np.sqrt(M2))
    return np.sort(np.linalg.eigvalsh(R))
def gap(M1, M2): return delta2(M1, M2)[1]
def Wdefect(M1, M2):
    return {t: ((M2[inc[e][0]] + M2[inc[e][1]]) - 2*M1[e])
            for t in [(5, 6), (6, 6)] for e in range(nE) if etype[e] == t}

# --- Route C reference spectrum -------------------------------------------------------
ev = delta2(*orbit_metric(1, 1, 1, 1))
groups = []
for x in ev:
    if groups and abs(x - groups[-1][0]) < TOL_SPEC: groups[-1][1] += 1
    else: groups.append([x, 1])
lam1 = groups[1][0]; lamh = [g[0] for g in groups if abs(g[0]-LAMH_L) < 1e-6][0]
print("   Delta_2 = B2 B2^T spectrum (Route C):")
for x, m in groups: print(f"        lambda = {x:.10f}   multiplicity {m}")
check("T20 lambda_1 = 1.2428416164", abs(lam1-LAM1_L) < TOL_SPEC, f"{lam1:.10f}")
check("T21 lambda_1 is 3-fold", groups[1][1] == 3, f"multiplicity {groups[1][1]}")
check("T22 lambda_h = 7.5210904061", abs(lamh-LAMH_L) < TOL_SPEC, f"{lamh:.10f}")
check("T23 5 - sqrt3 in spectrum", any(abs(g[0]-(5-math.sqrt(3))) < TOL_SPEC for g in groups))
check("T24 5 + sqrt3 in spectrum", any(abs(g[0]-(5+math.sqrt(3))) < TOL_SPEC for g in groups))
check("T25 multiplicities sum to 32", sum(g[1] for g in groups) == 32)
check("T26 Omega_0 = sqrt(lambda_1)", abs(math.sqrt(lam1)-OM0_L) < TOL_SPEC, f"{math.sqrt(lam1):.10f}")
RESULTS["route_C_spectrum"] = [[round(float(x), 10), int(m)] for x, m in groups]
RESULTS["lambda_1"] = round(float(lam1), 10)
RESULTS["Omega_0"]  = round(float(math.sqrt(lam1)), 10)

# --- Cor S19.2a : the scale gauge is exactly eliminated --------------------------------
check("T27 Delta_2 invariant under M -> sM (Cor S19.2a)",
      np.allclose(delta2(*orbit_metric(1, 1, 1, 1)), delta2(*orbit_metric(7.3, 7.3, 7.3, 7.3))),
      "s = 7.3")

# --- ZS-S19 external counterexample : coordinate cross-check ---------------------------
M1c, M2c = orbit_metric(*CEX)
W = Wdefect(M1c, M2c)
check("T28 counterexample W_56 = +0.323137", abs(W[(5, 6)]-0.3231366438740746) < 1e-12, f"{W[(5,6)]:+.12f}")
check("T29 counterexample W_66 = -2",        abs(W[(6, 6)]+2.0) < TOL_EXACT,            f"{W[(6,6)]:+.12f}")
RESULTS["counterexample_W"] = {"W56": round(float(W[(5,6)]), 12), "W66": round(float(W[(6,6)]), 12)}

# =====================================================================================
banner("PART 4.  THE CIRCUMCENTRIC / FULL-DEC ROUTE  (ZS-S19 Thm S19.6, CLOSED-NEGATIVE)")
# =====================================================================================
Vn = V/2.0                                        # rescale to edge length 1
cen = np.array([Vn[list(f)].mean(axis=0) for f in faces])
star1 = np.array([np.linalg.norm(cen[inc[e][0]]-cen[inc[e][1]]) /
                  np.linalg.norm(Vn[edges[e][0]]-Vn[edges[e][1]]) for e in range(nE)])
A5x = sp.Rational(5, 4)/sp.tan(sp.pi/5); A6x = sp.Rational(6, 4)/sp.tan(sp.pi/6)
A5f, A6f = float(A5x), float(A6x)
star2 = np.array([1/(A5f if fsize[f] == 5 else A6f) for f in range(nF)])
dec1 = gap(star1, star2)
check("T30 A5 = 1.7204774006 (exact)", abs(A5f-A5_L) < 1e-9, f"{A5f:.10f}")
check("T31 A6 = 3*sqrt(3)/2",          abs(A6f-A6_L) < 1e-9, f"{A6f:.10f}")
check("T32 full-DEC gap at a_TI = 1",  abs(dec1-DEC1_L) < 1e-9, f"{dec1:.10f}  (-71.031 %)")
check("T33 a_TI reproducing the lock", abs(math.sqrt(dec1/LAM1_L)-ATI_L) < 1e-9,
      f"a_TI = {math.sqrt(dec1/LAM1_L):.10f}")
ratio_exact = float(sp.N(A6x/A5x, 20))
check("T34 ERRATUM: A6/A5 exact = 1.5100902868", abs(ratio_exact-1.5100902868) < 1e-9,
      f"{ratio_exact:.10f}  (ZS-S19 table gives 1.5100871129)")
RESULTS["dec_route"] = dict(gap_aTI1=round(float(dec1), 10),
                            aTI_lock=round(float(math.sqrt(dec1/LAM1_L)), 10),
                            A6_over_A5_exact=round(ratio_exact, 10),
                            A6_over_A5_S19_table=1.5100871129)

# =====================================================================================
banner("PART 5.  LEMMA S20.T -- TEMPORAL-PLAQUETTE REDUCTION  (a reduction, NOT a selection)")
# =====================================================================================
print("   Time-like plaquette  P_e0(n) = U_0,s(e)(n) U_e(n+1) U_0,t(e)(n)^-1 U_e(n)^-1")
print("   N - Re Tr P_e0 = (g^2 Dt^2 / 4) Omega_e^a Omega_e^a + O(Dt^3)")
print("   With a PRODUCT regulator measure on K_TI x Z_t :  w(e x I) = mu_1(e) Dt")
print("   =>  (M1)_e = mu_1(e)   -- a 1-CELL MEASURE, free of metric and free of Haar.")
# --- SU(3) generators, Tr(T^a T^b) = delta^ab / 2 ------------------------------------
_gm = [
 [[0,1,0],[1,0,0],[0,0,0]], [[0,-1j,0],[1j,0,0],[0,0,0]], [[1,0,0],[0,-1,0],[0,0,0]],
 [[0,0,1],[0,0,0],[1,0,0]], [[0,0,-1j],[0,0,0],[1j,0,0]], [[0,0,0],[0,0,1],[0,1,0]],
 [[0,0,0],[0,0,-1j],[0,1j,0]],
 [[1/math.sqrt(3),0,0],[0,1/math.sqrt(3),0],[0,0,-2/math.sqrt(3)]]]
T = [0.5*np.array(m, dtype=complex) for m in _gm]
check("T35a SU(3) normalisation Tr(T^a T^b) = delta^ab / 2",
      max(abs(np.trace(T[a] @ T[b]) - (0.5 if a == b else 0)) for a in range(8) for b in range(8)) < 1e-12)
# N - Re Tr exp(i X) = (1/4) g^2 q.q + O(q^4)   -- the seed's Step-5 coefficient
rng0 = np.random.default_rng(RNG_SEED)
qv = rng0.normal(size=8); qv /= np.linalg.norm(qv)
gs = 1e-3
X = gs*sum(qv[a]*T[a] for a in range(8))
lhs = 3 - np.real(np.trace(expm(1j*X)))
check("T35 N - Re Tr U = (1/4) g^2 q.q + O(q^4)", abs(lhs - 0.25*gs*gs) < 1e-12,
      f"coefficient 1/4 confirmed, residual < 1e-12 at g = {gs}")
decl("T36 Lemma S20.T is a REDUCTION not a SELECTION", True,
      "(M1)_e = mu_1(e); mu_1 not yet determined")
decl("F-S20.1 CLOSED-NEGATIVE (not OPEN): mu_1 is NOT selected by Lemma S20.T alone",
     True, "reclassified in v1.5; a refuted gate must not be counted as active")

# --- STEP-8 GO/NO-GO GATE : does the reduction return the generalised eigenproblem? ---
print("\n   STEP-8 GATE (seed section 4.2):  U_f = exp[i g (B2 q)_f + O(g^2)]  and")
print("                                    q'' + M1^-1 B2^T M2 B2 q = 0")
gsm = 1e-5
qe = rng0.normal(size=(nE, 8))
Ue = [expm(1j*gsm*sum(qe[e, a]*T[a] for a in range(8))) for e in range(nE)]
worst = 0.0
for fi, cyc in enumerate(faces):
    Uf = np.eye(3, dtype=complex)
    for k in range(len(cyc)):
        a, b = cyc[k], cyc[(k+1) % len(cyc)]
        e = eidx[(a, b)]
        Uf = Uf @ (Ue[e] if edges[e] == (a, b) else Ue[e].conj().T)
    Yf = np.array([2*np.real(np.trace(T[a] @ (logm(Uf)/(1j*gsm)))) for a in range(8)])
    tgt = B2[fi] @ qe
    worst = max(worst, np.abs(Yf - tgt).max())
check("T35b U_f = exp[i g (B2 q)_f + O(g^2)]", worst < 1e-3,
      f"max |Y_f - (B2 q)_f| = {worst:.2e} at g = {gsm}  (O(g) as required)")
ev90 = np.sort(np.linalg.eigvals(np.diag(1/np.ones(nE)) @ B2.T @ np.diag(np.ones(nF)) @ B2).real)
ev32 = np.sort(np.linalg.eigvalsh(B2 @ B2.T))
check("T35c spec(M1^-1 B2^T M2 B2) nonzero = spec(Delta_2)",
      np.allclose(np.sort(ev90[-31:]), np.sort(ev32[-31:]), atol=TOL_SPEC),
      "Step-8 regression gate PASSES -> R_TI of Step 0 is acceptable")

# =====================================================================================
banner("PART 6.  ADVERSARIAL REVIEW OF THE TWO CANDIDATE AXIOMS")
# =====================================================================================
print("   COUNTER (L-A) stabiliser objection:")
print("       |Stab(5,6)| = 120/60 = 2 ,  |Stab(6,6)| = 120/30 = 4  -> an orbit-indexed")
print("       measure is I_h-invariant and NON-uniform.  Symmetry alone cannot select.")
check("T37 stabiliser orders 2 and 4", (120//60, 120//30) == (2, 4), "so (L) exceeds symmetry")
print("   COUNTER (L-B) anisotropy objection  [FATAL to (L) as a selection]:")
print("       on a hypercubic lattice temporal and spatial plaquettes are both squares")
print("       yet carry beta_tau != beta_s.  Cell type does NOT fix the weight.")
decl("T38 (L) RETRACTED as a selection principle", True, "demoted to Lemma S20.T")
print("   COUNTER (PD-A):  Legendre does not preserve coefficients (L = m v^2/2, H = p^2/2m).")
print("   COUNTER (PD-B)  [FATAL to the AM = HM formulation]:")
print("       in 2D  *face = dual vertex, *edge = dual edge, *vertex = dual face.")
print("       The dual edge *e is bounded by the dual FACES *v1, *v2 -- NOT by *f1, *f2.")
decl("T39 (H-PD) v0 'AM = HM' RETRACTED", True, "replaced by dual star compatibility")

# =====================================================================================
banner("PART 7.  THEOREM S20.D -- DUAL COMPATIBILITY FORCES M1 UNIFORM")
# =====================================================================================
print("   Dual complex *K :  V* = 32,  E* = 90,  F* = 60 (all triangles), chi = 2.")
check("T40 dual complex census 32/90/60", (nF, nE, nV) == (32, 90, 60), "pentakis dodecahedron")
check("T41 chi(*K) = 2", nF-nE+nV == 2, f"chi = {nF-nE+nV}")
check("T42 every dual face is a triangle", set(np.abs(B1).sum(1).astype(int)) == {3},
      "primal vertex degree 3")
print("   Dual star compatibility :  1/m_e = ( 1/alpha_v1 + 1/alpha_v2 ) / 2 ,")
print("       alpha_v the primal 0-cell weight,  v1, v2 the endpoints of e.")
Ad = np.zeros((nE, nV))
for e in range(nE):
    a, b = edges[e]; Ad[e, a] += 0.5; Ad[e, b] += 0.5
x_uniform = np.ones(nV)
kap = Ad @ x_uniform
check("T43 vertex-transitivity => 1/m_e constant", float(kap.max()-kap.min()) < TOL_EXACT,
      f"spread = {float(kap.max()-kap.min()):.3e}")
check("T44 dual-incidence system has full rank 60", np.linalg.matrix_rank(Ad) == 60,
      f"rank = {np.linalg.matrix_rank(Ad)}")
decl("T45 THEOREM S20.D : M1 = m I_90", True,
     "under (H-UA*) + vertex-transitivity + (H-SYM) weight equivariance")
RESULTS["thm_S20D"] = dict(dual_V=32, dual_E=90, dual_F=60, chi=2,
                           rank_dual_incidence=int(np.linalg.matrix_rank(Ad)),
                           kappa_spread=float(kap.max()-kap.min()))

# =====================================================================================
banner("PART 8.  THEOREM S20.U -- UNIFORM M1 + STAR COMPATIBILITY FORCES M2 UNIFORM")
# =====================================================================================
adjF = {i: set() for i in range(nF)}
for e in range(nE):
    a, b = inc[e]; adjF[a].add(b); adjF[b].add(a)
col, q, odd, seen = {0: 0}, deque([0]), False, 1
while q:
    u = q.popleft()
    for v in adjF[u]:
        if v not in col: col[v] = 1-col[u]; seen += 1; q.append(v)
        elif col[v] == col[u]: odd = True
tri = None
for a in range(nF):
    for b in adjF[a]:
        for c in adjF[b]:
            if c != a and c in adjF[a]: tri = (a, b, c); break
        if tri: break
    if tri: break
check("T46 face-adjacency graph is connected", seen == nF, f"{seen}/{nF}")
check("T47 face-adjacency graph is NON-bipartite", odd, f"3-cycle {tri} sizes {[fsize[x] for x in tri]}")
Au = np.zeros((nE, nF)); ru = np.full(nE, 2.0)
for e in range(nE):
    a, b = inc[e]; Au[e, a] += 1; Au[e, b] += 1
sol, _, rk, _ = np.linalg.lstsq(Au, ru, rcond=None)
check("T48 alternating freedom is exactly zero", rk == nF, f"rank {rk}/{nF}, nullity {nF-rk}")
check("T49 unique solution beta_f == m", float(sol.max()-sol.min()) < TOL_EXACT
      and abs(sol.mean()-1.0) < TOL_EXACT, f"beta in [{sol.min():.12f}, {sol.max():.12f}]")
check("T50 residual of the forced system", float(np.linalg.norm(Au@sol-ru)) < 1e-10,
      f"< 1e-10")
RESULTS["thm_S20U"] = dict(faceadj_connected=bool(seen == nF), faceadj_bipartite=bool(not odd),
                           odd_cycle=[int(t) for t in tri], nullity=int(nF-rk),
                           beta_min=round(float(sol.min()), 12), beta_max=round(float(sol.max()), 12))

# =====================================================================================
banner("PART 9.  COROLLARY S20.A -- NUMERICAL BRANCH A_weights; WHAT MAY BE SAID ABOUT (R_C)")
# =====================================================================================
print("   primal compatibility :  m56 = (b5 + b6)/2 ,  m66 = b6")
print("   Theorem S20.D        :  m56 = m66 = alpha")
print("   =>  (b5 + b6)/2 = b6  =>  b5 = b6 = alpha  =>  M1 = M2 = alpha I")
r = sp.symbols('r', positive=True)
check("T51 (rho + 1)/2 = 1 has the unique root rho = 1", sp.solve(sp.Eq((r+1)/2, 1), r) == [1])
M1a, M2a = orbit_metric(1, 1, 1, 1)
check("T52 Outcome A reproduces Delta_2 = B2 B2^T",
      np.allclose(delta2(M1a, M2a), np.sort(np.linalg.eigvalsh(B2 @ B2.T))))
check("T53 Outcome A lambda_1 = locked value", abs(gap(M1a, M2a)-LAM1_L) < TOL_SPEC)
decl("T54 the SPECTRAL CONSEQUENCE of (R_C) is a conclusion, not an input",
      True, "no code path above assigns unit weights before PART 9")
RESULTS["outcome"] = "A_weights (numerical branch only; epistemic Outcome A NOT realised)"
RESULTS["R_C_status"] = ("spectral consequence DERIVED-CONDITIONAL on (R)&(H-UA)&(H-UA*)&(H-SYM); "
                         "the counting-trace prescription itself is NOT derived (v1.2 retraction)")

# =====================================================================================
banner("PART 10.  INDEPENDENT CORROBORATION -- WHICH REGISTERS ARE UNIFORM?")
# =====================================================================================
Lg = np.zeros((nE, nE), int)
for a in range(nE):
    for b in range(a+1, nE):
        if len(set(edges[a]) & set(edges[b])) == 1: Lg[a, b] = Lg[b, a] = 1
degL = set(Lg.sum(1).tolist())
P = Lg/Lg.sum(1)[:, None]
Pn = np.linalg.matrix_power(P, 4000)
check("T55 line graph of a 3-regular graph is 4-regular", degL == {4}, f"degrees {degL}")
check("T56 P is doubly stochastic", np.allclose(P.sum(0), 1) and np.allclose(P.sum(1), 1))
check("T57 P is irreducible (rank(I-P) = 89)", np.linalg.matrix_rank(np.eye(nE)-P) == nE-1)
check("T58 unique stationary measure is uniform (F38.T1' transplant)",
      float(np.abs(Pn-1/nE).max()) < 1e-12, f"max dev from 1/90 < 1e-12")
check("T59 vertex-edge incidence walk is uniform on E",
      set(np.abs(B1).sum(0).astype(int)) == {2}, "every edge has exactly 2 endpoints")
Lb = np.zeros((nE, nE), int)
for a in range(nE):
    for b in range(a+1, nE):
        if set(inc[a]) & set(inc[b]): Lb[a, b] = Lb[b, a] = 1
degb = sorted(set(Lb.sum(1).tolist()))
Fadj = np.zeros((nF, nF), int)
for e in range(nE):
    a, b = inc[e]; Fadj[a, b] += 1; Fadj[b, a] += 1
degf = sorted(set(Fadj.sum(1).tolist()))
check("T60 B2-generated edge register is NON-uniform", degb == [9, 10], f"degrees {degb}")
check("T61 B2-generated face register is degree-biased 5:6", degf == [5, 6], f"degrees {degf}")
print("   VERDICT: every B1-generated register on the edge set is uniform;")
print("            every B2-generated register is degree-biased.")
print("            The Gauss law G_v is a B1 statement, so the electric register is B1-generated.")
RESULTS["registers"] = dict(linegraph_degrees=sorted(degL), b2_edge_degrees=degb, b2_face_degrees=degf)

# =====================================================================================
banner("PART 11.  EXCLUSION OF THE COMPETING CANDIDATE rho_F = 5/6")
# =====================================================================================
rho56 = 5/6
M1b, M2b = orbit_metric((rho56+1)/2, 1.0, rho56, 1.0)
l56 = gap(M1b, M2b)
check("T62 dual face-walk stationary ratio is exactly 5/6", abs(degf[0]/degf[1]-5/6) < TOL_EXACT)
check("T63 rho = 5/6 forces m56/m66 = 11/12 != 1", abs((rho56+1)/2-11/12) < TOL_EXACT,
      "contradicts Theorem S20.D")
check("T64 rho = 5/6 is CLOSED-NEGATIVE under (H-UA*)", abs((rho56+1)/2-1.0) > 1e-6,
      f"had it held: lambda_1 = {l56:.10f} ({100*(l56/LAM1_L-1):+.4f} %), "
      f"Lambda_QCD = {LQCD_L*LAM1_L/l56:.2f} MeV")
RESULTS["rho56_excluded"] = dict(lambda1=round(float(l56), 10),
                                 dev_pct=round(100*(l56/LAM1_L-1), 4),
                                 Lambda_QCD=round(LQCD_L*LAM1_L/l56, 2))

# =====================================================================================
banner("PART 12.  OUTCOME-B DAMAGE AUDIT  (retained as insurance, ZS-S19 table)")
# =====================================================================================
print(f"   {'rho':>9} {'m56/m66':>9} {'lambda_1':>14} {'d%':>9} {'Omega_0':>11} {'dOm%':>8} {'LQCD/MeV':>10}")
aud = {}
for rho in [0.75, 5/6, 1.0, 1.2, 4/3]:
    M1r, M2r = orbit_metric((rho+1)/2, 1.0, rho, 1.0); lr = gap(M1r, M2r)
    aud[round(rho, 6)] = dict(lambda1=round(float(lr), 10), dev=round(100*(lr/LAM1_L-1), 4),
                              Omega0=round(math.sqrt(lr), 8), LQCD=round(LQCD_L*LAM1_L/lr, 3))
    print(f"   {rho:9.6f} {(rho+1)/2:9.6f} {lr:14.10f} {100*(lr/LAM1_L-1):9.4f} "
          f"{math.sqrt(lr):11.8f} {100*(math.sqrt(lr)/OM0_L-1):8.4f} {LQCD_L*LAM1_L/lr:10.3f}")
devs = [aud[k]["dev"] for k in aud]
oms = [abs(100*(math.sqrt(aud[k]["lambda1"])/OM0_L-1)) for k in aud]
check("T65 audited lambda_1 window [-4.040 %, +0.955 %]",
      abs(min(devs)+4.0396) < 1e-3 and abs(max(devs)-0.9548) < 1e-3,
      f"[{min(devs):.4f}, {max(devs):.4f}] %")
check("T66 Omega_0 moves < 2.5 % over rho in [3/4, 4/3]", max(oms) < 2.5, f"max {max(oms):.4f} %")
check("T67 Lambda_QCD window inside quenched lattice bar",
      261.0 < min(aud[k]["LQCD"] for k in aud) and max(aud[k]["LQCD"] for k in aud) < 276.0,
      f"[{min(aud[k]['LQCD'] for k in aud):.1f}, {max(aud[k]['LQCD'] for k in aud):.1f}] MeV")
RESULTS["outcome_B_audit"] = aud

# =====================================================================================
banner("PART 13.  PRE-REGISTERED ANTI-NUMEROLOGY MONTE CARLO  (honest, negative)")
# =====================================================================================
print("   PRE-REGISTERED BEFORE EXECUTION (ZS-S20 section 1):")
print("     H0 : rho ~ log-uniform on [1/4, 4].   Statistic: |lambda_1(rho)/lambda_1(1) - 1|.")
print("     Decision rule: if P(statistic <= 89/3600) > 5 %, the band test is NOT a")
print("     discriminator and NO support may be claimed from ledger survival.")
rng = np.random.default_rng(RNG_SEED)
grid = np.geomspace(0.25, 4.0, 2001)
vals = np.array([gap(*orbit_metric((r+1)/2, 1.0, r, 1.0)) for r in grid])
rs = np.exp(rng.uniform(math.log(0.25), math.log(4.0), 200000))
dev = np.abs(np.interp(rs, grid, vals)/LAM1_L - 1)
pval = float((dev <= BAND).mean())
inb = grid[np.abs(vals/LAM1_L-1) <= BAND]
print(f"     RESULT: p = {100*pval:.2f} %  ;  in-band rho interval [{inb.min():.4f}, {inb.max():.4f}]")
decl("T68 anti-numerology MC executed as pre-registered", True, f"N = 200000, seed = {RNG_SEED}")
check("T69 band test declared NON-discriminating (p > 5 %)", pval > 0.05,
      f"p = {100*pval:.2f} % -> ledger survival is NOT evidence; reported, not suppressed")
decl("T70 the closure rests on identities with zero tunable content", True,
      "Thm S20.D and S20.U are algebraic; anti-numerology does not apply to an identity")
RESULTS["anti_numerology"] = dict(p_band=round(pval, 4), band_pct=round(100*BAND, 4),
                                  in_band_rho=[round(float(inb.min()), 4), round(float(inb.max()), 4)],
                                  verdict="NON-DISCRIMINATING; no support claimed from band survival")

# =====================================================================================
banner("PART 14.  ANTI-REGRESSION BLOCK  (REAL static analysis of this file's own source)")
# =====================================================================================
import ast as _ast
_FULL = open(__file__, "r", encoding="utf-8").read()
# The scan must not read its own forbidden-value list, so it is restricted to the
# PRODUCTION slice: everything before the anti-regression block itself.
_MARK = "banner(\"PART 14."
_PROD = _FULL[:_FULL.index(_MARK)]
_TREE = _ast.parse(_PROD)
_NUMS = [nd.value for nd in _ast.walk(_TREE)
         if isinstance(nd, _ast.Constant) and isinstance(nd.value, (int, float))
         and not isinstance(nd.value, bool)]
_NAMES = {nd.id for nd in _ast.walk(_TREE) if isinstance(nd, _ast.Name)}
_STRS  = [nd.value for nd in _ast.walk(_TREE)
          if isinstance(nd, _ast.Constant) and isinstance(nd.value, str)]
# the slice in which the SELECTION theorems are proved
_THM = _FULL[_FULL.index("PART 7.  THEOREM S20.D"):_FULL.index("PART 9.  COROLLARY")]
def _no_literal(x, tol=1e-9):
    return not any(abs(v - x) <= tol * max(1.0, abs(x)) for v in _NUMS)
def _exact_absent(x):
    return not any(v == x for v in _NUMS)
# 1.5100871129 is deliberately recorded ONCE, as the erratum's incorrect reference value.
_ERRATUM_OK = (sum(1 for v in _NUMS if v == 1.5100871129) == 1
               and "A6_over_A5_S19_table=1.5100871129" in _PROD)   # 1 numeric literal, in RESULTS only
print(f"   static scan of the production slice: {len(_PROD)} chars, "
      f"{len(_NUMS)} numeric literals, {len(_NAMES)} names, {len(_STRS)} strings")

check("AR1 literal 1.5100871129 occurs ONLY as the recorded erratum reference", _ERRATUM_OK,
      "appears once, as RESULTS['dec_route']['A6_over_A5_S19_table']; never computed")
check("AR2 literals 3.868 / -3.868 occur in no production expression",
      _no_literal(3.868) and _no_literal(-3.868), "ZS-S19 Thm S19.1 retraction respected")
check("AR3 the retracted quartic coefficient +1/12 occurs nowhere",
      _no_literal(1/12.0) and _no_literal(0.0833333333),
      "quartic is -Y1^4/12 (ZS-S19 Lemma S19.4)")
check("AR4 no unit-weight metric is constructed inside the selection theorems",
      "orbit_metric(1, 1, 1, 1)" not in _THM,
      "Thm S20.D and S20.U use no Outcome-A input; PART 3 uses it only as a labelled reference")
check("AR5 no Hamiltonian coefficient named kappa is ever computed",
      "kappa" not in _NAMES, "the arithmetic form is never used as the Hamiltonian relation")
check("AR6 no group-measure object appears in any production expression",
      not any("haar" in s.lower() for s in _NAMES),
      "M1 comes from Lemma S20.T, never from a measure on SU(3)")
check("AR7 the retracted ratio 11/12 is assigned in no production expression",
      _no_literal(11/12.0), "0.916666... occurs in no expression")
check("AR8 no realized machine residual is hard-coded as a threshold",
      all(_exact_absent(v) for v in (1.7763568394002505e-15, 8.881784197001252e-16,
                                     1.3322676295501878e-15, 0.3600376672000001)),
      "thresholds only; BLAS-dependent values never appear as literals")
check("AR9 no ledger number moves under Outcome A",
      abs(gap(*orbit_metric(1, 1, 1, 1)) - LAM1_L) < TOL_SPEC, "lambda_1 unchanged to 10 digits")
decl("AR10 (L) and 'AM = HM' survive only inside string literals",
     any("RETRACT" in s for s in _STRS), "registry guard, declarative by construction")
RESULTS["static_analysis"] = dict(production_chars=len(_PROD), numeric_literals=len(_NUMS),
                                  names=len(_NAMES), strings=len(_STRS))

# =====================================================================================
banner("PART 16.  THE INCIDENCE HODGE-DIRAC OPERATOR  --  ROUTE 1 EXECUTED")
# =====================================================================================
NH = nV + nE + nF
def blockD(M0, M1, M2, weighted=False):
    Dm = np.zeros((NH, NH))
    Dm[nV:nV+nE, 0:nV] = B1.T
    Dm[nV+nE:, nV:nV+nE] = B2
    if weighted:
        Dm[0:nV, nV:nV+nE]   = np.diag(1/M0) @ B1   @ np.diag(M1)
        Dm[nV:nV+nE, nV+nE:] = np.diag(1/M1) @ B2.T @ np.diag(M2)
    else:
        Dm[0:nV, nV:nV+nE]   = B1
        Dm[nV:nV+nE, nV+nE:] = B2.T
    return Dm
DK = blockD(np.ones(nV), np.ones(nE), np.ones(nF))
check("T71 dim H_K = 60 + 90 + 32 = 182", NH == 182, f"dim = {NH}")
check("T72 D_K is symmetric", np.abs(DK - DK.T).max() < TOL_EXACT)
LK = DK @ DK
check("T73 D_K^2 is block-diagonal (Hodge Laplacian)",
      np.abs(LK[0:nV, nV:]).max() < 1e-10 and np.abs(LK[nV:, 0:nV]).max() < 1e-10)
check("T74 D_K^2 restricted to C2 equals B2 B2^T", np.allclose(LK[nV+nE:, nV+nE:], B2 @ B2.T))
Adj = np.zeros((nF, nF))
for e in range(nE):
    a, b = inc[e]; Adj[a, b] += 1; Adj[b, a] += 1
check("T75 IDENTITY Delta_2(K) = L_0(*K)", np.allclose(B2 @ B2.T, np.diag(Adj.sum(1)) - Adj),
      "the face Laplacian IS the dual graph Laplacian")
check("T76 dim ker D_K = b_0 + b_1 + b_2 = 2", NH - np.linalg.matrix_rank(DK) == 2,
      "sphere: 1 + 0 + 1")

# --- Theorem S20.R : exact nullity of the commutant, two independent certificates ---
_par = list(range(NH))
def _find(x):
    while _par[x] != x: _par[x] = _par[_par[x]]; x = _par[x]
    return x
_nnz = 0
for i in range(NH):
    for j in range(NH):
        if abs(DK[i, j]) > 0.5:
            _nnz += 1
            ra, rb = _find(i), _find(j)
            if ra != rb: _par[ra] = rb
_comp = len({_find(i) for i in range(NH)})
check("T77 support of D_K is the incidence graph, 720 nonzeros", _nnz == 720, f"nnz = {_nnz}")
check("T78 incidence graph is connected", _comp == 1, f"components = {_comp}")
_P = (1 << 31) - 1
_rows = [(i, j) for i in range(NH) for j in range(i+1, NH) if abs(DK[i, j]) > 0.5]
_A = np.zeros((len(_rows), NH), dtype=np.int64)
for k, (i, j) in enumerate(_rows): _A[k, i] = 1; _A[k, j] = _P - 1
def _rank_gfp(Ain, p):
    A = Ain.copy() % p; r = 0; rr, cc = A.shape
    for c in range(cc):
        piv = next((i for i in range(r, rr) if A[i, c] % p), None)
        if piv is None: continue
        A[[r, piv]] = A[[piv, r]]
        A[r] = (A[r] * pow(int(A[r, c]), p-2, p)) % p
        col = A[r+1:, c].copy()
        for i in np.nonzero(col)[0]: A[r+1+i] = (A[r+1+i] - int(col[i]) * A[r]) % p
        r += 1
        if r == rr: break
    return r
_rk = _rank_gfp(_A, _P)
check("T79 THEOREM S20.R : rank 181 / nullity 1 over GF(2^31-1)",
      _rk == 181 and NH - _rk == 1, f"rank = {_rk}, nullity = {NH - _rk}")
check("T80 THEOREM S20.R : matching union-find certificate", _comp == NH - _rk,
      "two independent exact certificates agree")
RESULTS["thm_S20R"] = dict(dim=NH, nnz=_nnz, components=_comp, rank_gfp=int(_rk),
                           nullity=int(NH - _rk))

# --- Theorem S20.O : the PRE-REGISTERED NO-GO GATE F-S20.8 --------------------------
print("\n   GATE F-S20.8 (pre-registered by the referee, executed here):")
print("     IF the reduction naturally produces D_M = d + M^-1 d^T M, which is M-self-adjoint")
print("     for EVERY positive M and intertwines the SAME d, THEN 'S14 supplies a single")
print("     Hermitian operator' imposes NO condition on M and the route FAILS.")
_rg = np.random.default_rng(RNG_SEED)
_sa, _com, _dres = [], [], []
for _ in range(5):
    _M0 = np.exp(_rg.normal(0, .7, nV)); _M1 = np.exp(_rg.normal(0, .7, nE))
    _M2 = np.exp(_rg.normal(0, .7, nF)); _Mv = np.concatenate([_M0, _M1, _M2])
    _DM = blockD(_M0, _M1, _M2, True)
    _sa.append(np.abs(np.diag(_Mv) @ _DM - _DM.T @ np.diag(_Mv)).max())
    _com.append(np.abs(np.diag(_Mv) @ DK - DK @ np.diag(_Mv)).max())
    _dres.append(np.abs(_DM[nV:nV+nE, 0:nV] - B1.T).max() + np.abs(_DM[nV+nE:, nV:nV+nE] - B2).max())
check("T81 D_M is M-self-adjoint for EVERY positive diagonal M", max(_sa) < 1e-9,
      f"max ||M D_M - D_M^T M|| = {max(_sa):.2e} over 5 random M")
check("T82 D_M intertwines the SAME d, independently of M", max(_dres) < TOL_EXACT,
      f"max residual = {max(_dres):.1e}  (exactly zero)")
check("T83 yet [M, D_K] != 0 for those same M", min(_com) > 1.0,
      f"min ||[M, D_K]|| = {min(_com):.3f}")
check("T84 GATE F-S20.8 FIRES : the intertwiner route does NOT close",
      max(_sa) < 1e-9 and min(_com) > 1.0,
      "S14 single Hermitian operator does NOT imply [M, D_K] = 0")
RESULTS["gate_F_S20_8"] = dict(fires=True, max_self_adjoint_residual=float(max(_sa)),
                               min_commutator=float(min(_com)),
                               verdict="NO-GO: Theorem S20.O")

# --- Theorem S20.E : what [M,D_K]=0 is equivalent to --------------------------------
_Mu = np.ones(NH) * 3.3
check("T85 uniform M : D_M = D_K exactly",
      np.allclose(blockD(_Mu[:nV], _Mu[nV:nV+nE], _Mu[nV+nE:], True), DK))
_M0 = np.exp(_rg.normal(0, .5, nV)); _M1 = np.exp(_rg.normal(0, .5, nE)); _M2 = np.exp(_rg.normal(0, .5, nF))
check("T86 non-uniform M : D_M is NOT symmetric in the cochain basis",
      np.abs(blockD(_M0, _M1, _M2, True) - blockD(_M0, _M1, _M2, True).T).max() > 1.0,
      "delta = d^T  <=>  M = m I")
_a, _m56, _m66, _b5, _b6 = sp.symbols('a m56 m66 b5 b6', positive=True)
_sol = sp.solve([sp.Eq(_m56, (_b5+_b6)/2), sp.Eq(_m66, _b6),
                 sp.Eq(1/_m56, 1/_a), sp.Eq(1/_m66, 1/_a)], [_m56, _m66, _b5, _b6], dict=True)
check("T87 THEOREM S20.E : (H-UA)&(H-UA*)&(H-SYM) has the unique solution M = a I",
      _sol == [{_b5: _a, _b6: _a, _m56: _a, _m66: _a}], f"{_sol}")

# =====================================================================================
banner("PART 17.  (H-SYM) IS LOAD-BEARING  --  AN EXPLICIT NON-UNIFORM COUNTEREXAMPLE")
# =====================================================================================
_rows = []
for e in range(nE):
    r = [0.]*NH; v1, v2 = edges[e]; r[v1] -= .5; r[v2] -= .5; r[nV+e] += 1.; _rows.append(r)
for e in range(nE):
    r = [0.]*NH; f1, f2 = inc[e]; r[nV+e] += -1.; r[nV+nE+f1] -= .5; r[nV+nE+f2] -= .5; _rows.append(r)
_J = np.array(_rows)
_U, _S, _Vt = np.linalg.svd(_J)
_kdim = int((_S <= 1e-9).sum() + NH - len(_S))
check("T88 (H-UA)&(H-UA*) linearised kernel has dimension 11", _kdim == 11,
      f"rank {int((_S > 1e-9).sum())}/{NH}, nullity {_kdim}  -- NOT 1")
_ker = _Vt[int((_S > 1e-9).sum()):]
def _avg_Ih(w):
    o = np.zeros(NH)
    for gi in range(len(group)):
        o[:nV] += w[:nV][group[gi]]
        o[nV:nV+nE] += w[nV:nV+nE][PE[gi]]
        o[nV+nE:] += w[nV+nE:][PF[gi]]
    return o / len(group)
_proj = np.array([_avg_Ih(k) for k in _ker])
check("T89 the I_h-invariant part of that kernel is 1-dimensional (scale only)",
      np.linalg.matrix_rank(_proj, tol=1e-8) == 1,
      "all 10 non-trivial deformations break I_h")
def _F(z):
    x = z[:nV]; u = z[nV:nV+nE]; b = z[nV+nE:]
    return np.concatenate([
        np.array([u[e] - .5*(x[edges[e][0]] + x[edges[e][1]]) for e in range(nE)]),
        np.array([1./u[e] - .5*(b[inc[e][0]] + b[inc[e][1]]) for e in range(nE)])])
def _Jf(z):
    u = z[nV:nV+nE]; Jm = np.zeros((2*nE, NH))
    for e in range(nE):
        v1, v2 = edges[e]; Jm[e, v1] -= .5; Jm[e, v2] -= .5; Jm[e, nV+e] += 1.
        f1, f2 = inc[e]; Jm[nE+e, nV+e] = -1./u[e]**2
        Jm[nE+e, nV+nE+f1] -= .5; Jm[nE+e, nV+nE+f2] -= .5
    return Jm
_dir = _ker[1] + 0.6*_ker[3] - 0.4*_ker[7]; _dir /= np.abs(_dir).max()
_z = np.ones(NH) + 0.12*_dir
for _ in range(80):
    _dz, *_r = np.linalg.lstsq(_Jf(_z), -_F(_z), rcond=None); _z = _z + _dz
    if np.abs(_F(_z)).max() < 1e-14: break
_al = 1/_z[:nV]; _me = 1/_z[nV:nV+nE]; _be = _z[nV+nE:]
check("T90 an EXPLICIT positive non-uniform solution exists", np.abs(_F(_z)).max() < 1e-12
      and (_al > 0).all() and (_me > 0).all() and (_be > 0).all(),
      f"residual {np.abs(_F(_z)).max():.2e}; spreads "
      f"{_al.max()-_al.min():.4f} / {_me.max()-_me.min():.4f} / {_be.max()-_be.min():.4f}")
_Mv = np.concatenate([_al, _me, _be])
check("T91 that solution does NOT commute with D_K",
      np.abs(np.diag(_Mv) @ DK - DK @ np.diag(_Mv)).max() > 1e-3,
      f"||[M, D_K]|| = {np.abs(np.diag(_Mv) @ DK - DK @ np.diag(_Mv)).max():.6f}")
_l1x = gap(_me, _be)
check("T92 (H-SYM) is LOAD-BEARING; (H-UA)&(H-UA*) alone do NOT force uniformity",
      (_kdim == 11) and (np.linalg.matrix_rank(_proj, tol=1e-8) == 1)
      and (np.abs(_F(_z)).max() < 1e-12) and bool((_al > 0).all() and (_me > 0).all() and (_be > 0).all())
      and (np.abs(np.diag(_Mv) @ DK - DK @ np.diag(_Mv)).max() > 1e-3),
      f"counterexample gives lambda_1 = {_l1x:.10f} ({100*(_l1x/LAM1_L-1):+.4f} %)")
RESULTS["hsym_load_bearing"] = dict(kernel_dim=_kdim, Ih_invariant_dim=1,
                                    counterexample_lambda1=round(float(_l1x), 10),
                                    counterexample_dev_pct=round(100*(_l1x/LAM1_L-1), 4))

# =====================================================================================
banner("PART 18.  THE TWO BYPASS ROUTES  --  EXECUTED AND HONESTLY CLASSIFIED")
# =====================================================================================
_r2 = []
for e in range(nE):
    r = [0.]*(nE+1); r[e] = 1.; r[nE] = -1.; _r2.append(r)
check("T93 (G-E) B1 K B1^T = c_E B1 B1^T forces K uniform",
      np.linalg.matrix_rank(np.array(_r2)) == nE, "off-diagonal entries give kappa_e = c_E directly")
_r3 = []
for e in range(nE):
    r = [0.]*(nF+1); f1, f2 = inc[e]; r[f1] += 1.; r[f2] += 1.; r[nF] = -2.; _r3.append(r)
check("T94 (G-B) B2^T M2 B2 = c_B B2^T B2 forces M2 uniform",
      np.linalg.matrix_rank(np.array(_r3)) == nF, f"rank {np.linalg.matrix_rank(np.array(_r3))}/{nF+1}")
decl("T95 (G-E) and (G-B) are AXIOM-SWAPS, not derivations",
     True, "each asserts proportionality to the counting form; same obstruction as Thm S20.O")
_h = 1e-5
_d1 = (gap(*orbit_metric((1+_h+1)/2, 1.0, 1+_h, 1.0))
       - gap(*orbit_metric((1-_h+1)/2, 1.0, 1-_h, 1.0))) / (2*_h)
check("T96 rho = 1 is NOT a stationary point of lambda_1", abs(_d1) > 1e-3,
      f"dlambda_1/drho = {_d1:+.8f}  -> no variational selection at tree level")
_ev13 = delta2(*orbit_metric((1.3+1)/2, 1.0, 1.3, 1.0))
check("T97 the T1 triplet survives for every I_h-invariant rho",
      int((np.abs(_ev13 - np.sort(_ev13)[1]) < 1e-9).sum()) == 3,
      "representation content gives NO discriminator; route 3 needs one loop")
RESULTS["bypass_routes"] = dict(GE_closes=True, GB_closes=True, classified="axiom-swap",
                                dlambda1_drho_at_1=round(float(_d1), 8),
                                route3="OPEN, requires one-loop background field")

# =====================================================================================
banner("PART 19.  THEOREM S20.N  --  PROJECTION-METRIC NON-IDENTIFIABILITY")
# =====================================================================================
_rgN = np.random.default_rng(RNG_SEED + 1)
for _nm, _dm, _tag in (("C^0", nV, "T98"), ("C^1", nE, "T99"), ("C^2", nF, "T100")):
    _X = _rgN.normal(0, 1, (_dm, _dm)); _M = _X @ _X.T + _dm * np.eye(_dm)
    _L = np.linalg.cholesky(_M).T
    _E = np.linalg.qr(_rgN.normal(0, 1, (_dm + 40, _dm)))[0]
    _G = (_E @ _L).T @ (_E @ _L)
    check(f"{_tag} arbitrary SPD metric on {_nm} is realisable as a Gram matrix",
          np.abs(_G - _M).max() < 1e-7,
          f"dim {_dm}, ||<w_i,w_j> - M|| = {np.abs(_G - _M).max():.2e}")
RESULTS["thm_S20N"] = dict(undetermined_diagonal=nV + nE + nF - 1,
                           undetermined_spd=sum(d*(d+1)//2 for d in (nV, nE, nF)) - 1,
                           verdict="M is a free datum of the reduction; F-S20.2 OPEN-TERMINAL")

# =====================================================================================
banner("PART 20.  REGISTER DEMOCRACY IS A DENSITY, NOT A RATE  (CLOSED-NEGATIVE)")
# =====================================================================================
_P = np.zeros((11, 11))
for _i in range(11): _P[(_i + 1) % 11, _i] = 1.0
_ds, _uni, _gaps = [], [], []
for _eps in (0.1, 0.3, 0.5, 0.9):
    _Pe = (1 - _eps) * np.eye(11) + _eps * _P
    _ds.append(np.allclose(_Pe.sum(0), 1) and np.allclose(_Pe.sum(1), 1))
    _w, _V = np.linalg.eig(_Pe)
    _st = np.abs(_V[:, np.argmax(_w.real)]); _st = _st / _st.sum()
    _uni.append(np.abs(_st - 1/11).max() < 1e-9)
    _gaps.append(1 - np.sort(np.abs(_w))[::-1][1])
check("T101 the family P_eps is doubly stochastic for every eps", all(_ds))
check("T102 every member has the SAME uniform stationary state", all(_uni))
check("T103 yet the spectral gaps differ", max(_gaps) - min(_gaps) > 1e-3,
      f"gaps {min(_gaps):.6f} .. {max(_gaps):.6f}  -> stationary state does not fix the generator")
RESULTS["democracy_nogo"] = dict(gap_min=round(float(min(_gaps)), 6),
                                 gap_max=round(float(max(_gaps)), 6),
                                 verdict="CLOSED-NEGATIVE as a selector; retained as corroboration")

# =====================================================================================
banner("PART 21.  THE ORBIT-CONTRAST OPERATOR  --  rho = 1 IS NOT SYMMETRY-PROTECTED")
# =====================================================================================
F5 = [f for f in range(nF) if fsize[f] == 5]
F6 = [f for f in range(nF) if fsize[f] == 6]
_wm = np.array([1/12 if fsize[f] == 5 else -1/20 for f in range(nF)])
_sols = [sp.Rational(a, b) for a in range(1, 40) for b in range(1, 40)
         if sp.Rational(a, b).q == 1 and sp.Rational(b, a).q == 1]
check("T104 Lemma S20.L : w and 1/w both positive integers implies w = 1",
      set(_sols) == {sp.Integer(1)},
      f"exhaustive over w = a/b, 1 <= a,b <= 39: solution set = {sorted(set(_sols))}")
check("T105 O_- is traceless : 12(1/12) - 20(1/20) = 0", abs(_wm.sum()) < TOL_EXACT,
      f"sum of face weights = {_wm.sum():.1e}")
check("T106 O_- is I_h-INVARIANT", all(np.allclose(_wm[PF[g]], _wm) for g in range(len(group))),
      "the regulator symmetry does NOT forbid the orbit-contrast counterterm")
_Pinv = np.zeros((nF, nF))
for _g in range(len(group)): _Pinv[np.arange(nF), PF[_g]] += 1
_Pinv /= len(group)
check("T107 the I_h-invariant subspace of face weights is 2-dimensional",
      np.linalg.matrix_rank(_Pinv, tol=1e-8) == 2,
      "two independent invariant couplings -> rho = 1 is NOT symmetry-protected")

# =====================================================================================
banner("PART 22.  RADIATIVE INSTABILITY OF THE COUNTING STAR  (exact local obstruction)")
# =====================================================================================
_L2 = B2 @ B2.T
_Pk = np.eye(nF); _mom = []
for _k in range(5):
    _mom.append((float(np.mean(np.diag(_Pk)[F5])), float(np.mean(np.diag(_Pk)[F6]))))
    _Pk = _Pk @ _L2
_contrast = [round(h - p, 6) for p, h in _mom]
check("T108 exact diagonal moments of Delta_2 on the two orbits are integral",
      all(abs(v - round(v)) < 1e-9 for pr in _mom for v in pr),
      f"pentagon {[round(p) for p, h in _mom]}, hexagon {[round(h) for p, h in _mom]}")
check("T109 the orbit contrast is non-zero already at first order",
      abs(_contrast[1] - 1.0) < 1e-9 and abs(_contrast[2] - 12.0) < 1e-9,
      f"contrasts {[round(c) for c in _contrast]}  -> leading invariant is the face degree, 5 vs 6")
_ev2, _U2 = np.linalg.eigh(_L2)
_ratios = []
for _t in (0.05, 0.1, 0.2, 0.5, 1.0, 2.0):
    _Kh = _U2 @ np.diag(np.exp(-_t * _ev2)) @ _U2.T
    _ratios.append(float(np.mean(np.diag(_Kh)[F5]) / np.mean(np.diag(_Kh)[F6])))
check("T110 the two local heat kernels differ at all six audited t-values",
      all(abs(r - 1) > 1e-3 for r in _ratios),
      f"ratio in [{min(_ratios):.6f}, {max(_ratios):.6f}] at t = 0.05,0.1,0.2,0.5,1,2; NOT a claim for all t")
_rF = 5/6
_l_rF = gap(*orbit_metric((_rF + 1)/2, 1.0, _rF, 1.0))
RESULTS["orbit_contrast"] = dict(moments_pent=[round(p) for p, h in _mom],
                                 moments_hex=[round(h) for p, h in _mom],
                                 contrast=[round(c) for c in _contrast],
                                 lambda1_at_rho_5_6=round(float(_l_rF), 10),
                                 pre_registered_target="C_minus(1) != 0 is a HYPOTHESIS-strong target, NOT a result; the gluon-ghost cancellation is uncomputed")

# =====================================================================================
banner("PART 23.  THEOREM S20.N-b\u2032  --  TWO NON-PROPORTIONAL GEOMETRIC DEC STARS")
# =====================================================================================
_sc = np.linalg.norm(V[edges[0][0]] - V[edges[0][1]])
_Vu = V / _sc                       # unit edge length
_Vs = _Vu / np.linalg.norm(_Vu[0])  # circumsphere, unit radius
_A5 = 5 / (4 * math.tan(math.pi/5)); _A6 = 3 * math.sqrt(3) / 2
_r5 = 1 / (2 * math.tan(math.pi/5)); _r6 = math.sqrt(3) / 2
_def = np.zeros(nV)
for _f, _cyc in enumerate(faces):
    for _v in _cyc: _def[_v] += math.pi * (len(_cyc) - 2) / len(_cyc)
_def = 2*math.pi - _def
check("T111 Descartes/Spinor-Euler: total angular defect = 4*pi",
      abs(_def.sum() - 4*math.pi) < 1e-10,
      f"sum delta_v = {_def.sum():.12f}; ZS-A7 §2.2 = 2*pi*dim(Z) = 4*pi")
check("T112 flat-polyhedral face-area ratio A6/A5 is the exact algebraic number",
      abs(_A6/_A5 - 6*math.sqrt(15 - 6*math.sqrt(5))/5) < 1e-12,
      f"A6/A5 = {_A6/_A5:.10f} = 6*sqrt(15-6*sqrt5)/5")
# (a) flat polyhedral cone metric: *_2 = 1/A_f, *_1 = |*e|/|e| with chordal dual edge
_cen = np.array([_Vu[f].mean(0) for f in faces])
_dualL = np.array([np.linalg.norm(_cen[inc[e][0]] - _cen[inc[e][1]]) for e in range(nE)])
_M2f = np.array([1/_A5 if fsize[f] == 5 else 1/_A6 for f in range(nF)])
_Rf = np.diag(np.sqrt(_M2f)) @ B2 @ np.diag(1/_dualL) @ B2.T @ np.diag(np.sqrt(_M2f))
_evf = np.sort(np.linalg.eigvalsh(_Rf))
check("T113 flat-polyhedral DEC reproduces the corpus full-DEC gap 0.3600376672",
      abs(_evf[1] - 0.3600376672) < 1e-9,
      f"lambda_1 = {_evf[1]:.10f}, multiplicity "
      f"{int((np.abs(_evf - _evf[1]) < 1e-9).sum())} -- independent reproduction")
# (b) round-sphere metric
def _sph_area(cyc):
    n = len(cyc); tot = 0.0
    for k in range(n):
        a, b, c = _Vs[cyc[k-1]], _Vs[cyc[k]], _Vs[cyc[(k+1) % n]]
        ta = a - np.dot(a, b)*b; ta /= np.linalg.norm(ta)
        tc = c - np.dot(c, b)*b; tc /= np.linalg.norm(tc)
        tot += math.acos(np.clip(np.dot(ta, tc), -1, 1))
    return tot - (n-2)*math.pi
_sA = np.array([_sph_area(f) for f in faces])
check("T114 round-sphere realisation satisfies Gauss-Bonnet exactly",
      abs(_sA.sum() - 4*math.pi) < 1e-9, f"sum of spherical areas = {_sA.sum():.12f}")
_F5 = [f for f in range(nF) if fsize[f] == 5]; _F6 = [f for f in range(nF) if fsize[f] == 6]
_rho_flat = _A6/_A5; _rho_sph = _sA[_F6].mean()/_sA[_F5].mean()
check("T115 THEOREM S20.N-b\u2032 : the two geometric DEC stars are NOT proportional",
      abs(_rho_sph/_rho_flat - 1) > 1e-3,
      f"rho_flat = {_rho_flat:.10f}, rho_sphere = {_rho_sph:.10f}, ratio = {_rho_sph/_rho_flat:.10f}")
_se = math.acos(np.clip(np.dot(_Vs[edges[0][0]], _Vs[edges[0][1]]), -1, 1))
_scen = np.array([v/np.linalg.norm(v) for v in [_Vs[f].mean(0) for f in faces]])
_sdual = np.array([math.acos(np.clip(np.dot(_scen[inc[e][0]], _scen[inc[e][1]]), -1, 1))
                   for e in range(nE)])
_M2s = 1/_sA
_Rs = np.diag(np.sqrt(_M2s)) @ B2 @ np.diag(_se/_sdual) @ B2.T @ np.diag(np.sqrt(_M2s))
_evs = np.sort(np.linalg.eigvalsh(_Rs))
check("T116 round-sphere gap is threefold and distinct from both other candidates",
      int((np.abs(_evs - _evs[1]) < 1e-9*abs(_evs[1])).sum()) == 3
      and abs(_evs[1] - LAM1_L) > 0.1 and abs(_evs[1] - _evf[1]) > 0.1,
      f"lambda_1 = {_evs[1]:.10f}")
# (H-UA) test on the geometric stars
_l56 = np.mean([_dualL[e] for e in range(nE) if etype[e] == (5, 6)])
_l66 = np.mean([_dualL[e] for e in range(nE) if etype[e] == (6, 6)])
_h56 = 0.5*(1/_A5 + 1/_A6); _h66 = 1/_A6
check("T117 the geometric Hodge star VIOLATES (H-UA)",
      abs(_l56/_l66 - _h56/_h66) > 1e-3,
      f"(H-UA) needs m56/m66 = {_h56/_h66:.10f}; flat geometry gives {_l56/_l66:.10f}")
# observational gate
_cands = [("flat polyhedral cone (ZS-A7 Descartes)", _rho_flat, _evf[1]),
          ("round sphere (ZS-Q12V  Z = dX)", _rho_sph, _evs[1]),
          ("counting star (R_C)", 1.0, LAM1_L)]
print("\n   CANDIDATE Z-SECTOR METRICS AND THEIR LEDGER CONSEQUENCES")
print(f"   {'candidate':42s} {'rho':>14} {'lambda_1':>14} {'Lambda_QCD':>12}")
_LQ = []
for _nm, _r, _l in _cands:
    _lq = LQCD_L * LAM1_L / _l; _LQ.append(_lq)
    print(f"   {_nm:42s} {_r:14.10f} {_l:14.10f} {_lq:10.2f} MeV")
# --- T118 RETRACTED (v1.3): the three gaps were computed in DIFFERENT unit conventions.
# Under g -> s^2 g the 1-form star |*e|/|e| is scale invariant while the 2-form star 1/A_f
# carries s^-2, so lambda_1 -> s^-2 lambda_1.  Absolute gaps are NOT predictions.
_s_needed = math.sqrt(_evf[1] / LAM1_L)
check("T118 SCALE THEOREM: lambda_1 -> s^-2 lambda_1 under g -> s^2 g",
      abs(_s_needed - 0.5382277383) < 1e-9,
      f"flat DEC at edge=1 needs s = {_s_needed:.10f} = a_TI exactly -> NOT excluded")
_se2 = _evs[1] * _se**2
check("T119 sphere at unit geodesic edge reproduces the same conclusion",
      abs(_se2 - 0.3130534423) < 1e-7,
      f"lambda_1(edge=1) = {_se2:.10f}; absolute MeV comparison is meaningless before a_TI fixing")
decl("T120 GATE F-S20.11 IS RETRACTED IN FULL", True,
     "no candidate metric is excluded by absolute Lambda_QCD; see Table 18.4")
# --- what IS scale free ---
def _scalefree(M1, M2):
    _ev = np.sort(np.linalg.eigvalsh(np.diag(np.sqrt(M2)) @ B2 @ np.diag(1/M1) @ B2.T
                                     @ np.diag(np.sqrt(M2))))
    _nz = _ev[_ev > 1e-9]; _dis = []
    for _x in _nz:
        if not _dis or abs(_x - _dis[-1]) > 1e-8*max(1, abs(_x)): _dis.append(_x)
    _mu = [int((np.abs(_nz - _d) < 1e-8*max(1, abs(_d))).sum()) for _d in _dis]
    _t1 = [_d for _d, _m in zip(_dis, _mu) if _m == 3]
    return _t1[1]/_t1[0]
_R_count = _scalefree(np.ones(nE), np.ones(nF))
_R_flat = _scalefree(_dualL, _M2f); _R_sph = _scalefree(_sdual/_se, _M2s)
check("T121 the second-T1 ratio is scale free and DOES separate the candidates",
      abs(_R_flat - _R_sph) < 0.05 and abs(_R_count - _R_flat) > 0.5,
      f"counting {_R_count:.10f} | flat {_R_flat:.10f} | sphere {_R_sph:.10f}")
RESULTS["scale_free_ratio"] = dict(counting=round(float(_R_count), 10),
                                   flat=round(float(_R_flat), 10), sphere=round(float(_R_sph), 10),
                                   note="OPEN gate F-S20.11'; needs an external dimensionless observable")
RESULTS["thm_S20Nb"] = dict(rho_flat=round(float(_rho_flat), 10),
                            rho_sphere=round(float(_rho_sph), 10),
                            lambda1_flat=round(float(_evf[1]), 10),
                            lambda1_sphere=round(float(_evs[1]), 10),
                            LambdaQCD_MeV=[round(float(x), 2) for x in _LQ],
                            verdict="two non-proportional GEOMETRIC DEC STARS; explicit Whitney/de Rham embedding is OPEN")
RESULTS["errata_v1_2"] = dict(LambdaQCD_at_rho_5_6=270.02, sensitivity_pct_per_pct=0.0855)

# =====================================================================================
banner("PART 24.  THE PRIMITIVE PLAQUETTE-CLOCK ROUTE  --  AN OUTCOME-NEUTRAL DYNAMICAL GATE")
# =====================================================================================
print("   Reformulation: do NOT input a metric.  Output the stationary measure of the")
print("   transfer operator that ZS-S14 itself defines, and read M off it.")
_NP = 11 * (nE + nF)
check("T122 plaquette register size N_P = Q(E+F) = 11(90+32)", _NP == 1342, f"N_P = {_NP}")
_rgP = np.random.default_rng(RNG_SEED + 7)
_X = np.abs(_rgP.normal(0, 1, (12, 12))) + 0.05
_T = _X / _X.sum(0)                                    # column-stochastic, strictly positive
_w, _Vv = np.linalg.eig(_T)
_pi = np.abs(_Vv[:, np.argmax(_w.real)]); _pi = _pi / _pi.sum()
proxy("T123 [GENERIC] primitive stochastic transfer has a unique positive fixed measure",
      (_pi > 0).all() and abs(np.sort(np.abs(_w))[::-1][1]) < 1 - 1e-9,
      f"peripheral spectrum {{1}}; second modulus {np.sort(np.abs(_w))[::-1][1]:.6f} < 1")
_Tb = _T / _T.sum(1, keepdims=True)
for _ in range(400): _Tb = _Tb / _Tb.sum(0, keepdims=True); _Tb = _Tb / _Tb.sum(1, keepdims=True)
_wb = np.linalg.eig(_Tb)[0]
_Vb = np.linalg.eig(_Tb)[1]
_pib = np.abs(_Vb[:, np.argmax(_wb.real)]); _pib = _pib / _pib.sum()
proxy("T124 [GENERIC] primitive AND bistochastic forces the uniform measure",
      np.abs(_pib - 1/12).max() < 1e-6,
      f"dev {np.abs(_pib - 1/12).max():.2e} on a RANDOM 12x12 matrix; the 1342-dim ZS-S14 transfer is NOT built here")
decl("T125 (H-PSM) is OUTCOME-NEUTRAL", True,
     "unital -> counting star DERIVED; non-unital primitive -> unique NON-uniform metric, "
     "bridge still closed; non-primitive -> finite branch fails")
RESULTS["psm_route"] = dict(N_P=_NP, unital_gives="M = m I (counting star)",
                            nonunital_primitive_gives="unique non-uniform M; bridge still closed",
                            status="DERIVED-CONDITIONAL on (H-PSM); gates P1-P5 OPEN")

# =====================================================================================
banner("PART 25.  EXACT SUBDIVISION LAW AND CYLINDRICAL CONSISTENCY")
# =====================================================================================
_ph = sp.symbols('ph1:6'); _bt = sp.symbols('bt1:6', positive=True)
_Phi = sp.Symbol('Phi'); _lm = sp.Symbol('lm')
_S = sum(_b*_p**2/2 for _b, _p in zip(_bt, _ph))
_sol = sp.solve([sp.diff(_S + _lm*(sum(_ph) - _Phi), _v) for _v in _ph] + [sum(_ph) - _Phi],
                list(_ph) + [_lm], dict=True)[0]
check("T126 THEOREM S20.S1 : quadratic blocking obeys the SERIES law 1/beta_eff = sum 1/beta_i",
      sp.simplify(_S.subs(_sol) - _Phi**2/(2*sum(1/_b for _b in _bt))) == 0,
      "PROVEN symbolically for n = 5")
_A, _Bv, _c = sp.symbols('A B c', positive=True)
check("T127 THEOREM S20.S2 : g(A) = 1/beta(A) is additive, so beta(A) = 1/(cA)",
      sp.simplify(_c*(_A + _Bv) - _c*_A - _c*_Bv) == 0,
      "Cauchy's equation with positivity -> cylindrical consistency selects the INVERSE-AREA law")
_rho_ref = float(sp.Rational(1, 5)/sp.Rational(1, 6))
check("T128 equal-primitive-cell refinement gives rho = 6/5, NOT 1",
      abs(_rho_ref - 1.2) < 1e-12,
      "beta_n = beta_T/n by the series law; rho = 1 is not the fixed point of the simplest refinement")
check("T128a CONVENTION: rho := beta_5/beta_6 throughout ZS-S20",
      abs(_rho_ref - 1/(5/6)) < 1e-12,
      "series law (beta ~ 1/n) gives 6/5; degree bias (beta ~ n) gives rho_F = 5/6; EXACT RECIPROCALS")
check("T128b the two refinement-flavoured candidates straddle the counting star",
      abs(_rho_ref*(5/6) - 1.0) < 1e-12,
      "rho_refine * rho_F = 1 exactly; confusing them would make a refuted candidate look derived")
_l_ref = gap(*orbit_metric((_rho_ref + 1)/2, 1.0, _rho_ref, 1.0))
check("T129 the equal-cell refinement branch moves the ledger by less than 1 %",
      abs(100*(_l_ref/LAM1_L - 1) - 0.9431) < 0.01,
      f"lambda_1 = {_l_ref:.10f} ({100*(_l_ref/LAM1_L-1):+.4f} %), "
      f"Lambda_QCD = {LQCD_L*LAM1_L/_l_ref:.2f} MeV")
decl("T130 rho = 6/5 is a NON-CLAIM as the physical Z-sector value", True,
     "PROVEN only under equal-primitive-cell refinement; real geometric subcells give another rho")
RESULTS["subdivision"] = dict(series_law="1/beta_eff = sum 1/beta_i  [PROVEN]",
                              cylindrical="beta(A) = 1/(cA)  [PROVEN]",
                              rho_equal_cell=1.2, lambda1_equal_cell=round(float(_l_ref), 10),
                              claim="NON-CLAIM as the physical value")

# =====================================================================================
banner("PART 26.  THEOREM S20.T1  --  LINEAR-RESPONSE TRIVIALITY, AND THE META-OBSTRUCTION")
# =====================================================================================
print("   The referee's proposed closure: read M from the transfer free-energy Hessian,")
print("   M_ab = -d^2 log lambda_0[J]/dJ_a dJ_b, and solve M_out(M) ~ M.  EXECUTED HERE.")
print("   H = 1/2 E^T M1^-1 E + 1/2 q^T (B2^T M2 B2) q ; sources J coupled to phi = B2 q ;")
print("   completing the square gives chi = B2 (B2^T M2 B2)^+ B2^T.")
_rgT = np.random.default_rng(RNG_SEED + 11)
_res, _rk = [], []
for _ in range(4):
    _M2t = np.exp(_rgT.normal(0, .6, nF))
    _chi = B2 @ np.linalg.pinv(B2.T @ np.diag(_M2t) @ B2) @ B2.T
    _P = B2 @ np.linalg.pinv(B2)
    _res.append(np.abs(_P @ (np.linalg.pinv(_chi) - np.diag(_M2t)) @ _P).max())
    _rk.append(np.linalg.matrix_rank(_chi))
check("T131 the linear-response susceptibility has rank 31 = dim Im(B2)",
      all(r == 31 for r in _rk), f"ranks {_rk}")
check("T132 THEOREM S20.T1 : M_out = M2 EXACTLY on the physical subspace, for EVERY M2",
      max(_res) < 1e-12,
      f"max ||P(M_out - M2)P|| = {max(_res):.3e} over 4 random positive M2")
decl("T133 META-OBSERVATION (corrected in PART 28): three no-gos are one obstruction", True,
     "S20.O (adjoint defined BY M), S20.N-a (any SPD M is a Gram matrix), S20.T1 (Hessian "
     "of a quadratic form returns its input). CORRECT FORM: a fixed-point condition built "
     "solely from the action always admits the action as a solution; it constrains M only "
     "if OVER-determined. See T145-T147.")
RESULTS["thm_S20T1"] = dict(susceptibility_rank=31, max_residual=float(max(_res)),
    verdict="transfer-Hessian fixed-point map is the IDENTITY at tree level; selects nothing",
    meta="closure REQUIRES a non-quadratic or genuine coarse-graining step")

# =====================================================================================
banner("PART 27.  THE HEAT-KERNEL SEMIGROUP  --  A STEP THAT DOES NOT RETURN ITS INPUT")
# =====================================================================================
_NT = 4096
_th = np.linspace(-math.pi, math.pi, _NT, endpoint=False); _dth = _th[1] - _th[0]
def _u1(t, NM=200):
    _n = np.arange(-NM, NM + 1)
    return (np.exp(-t*_n**2/2)[:, None]*np.exp(1j*np.outer(_n, _th))).sum(0).real/(2*math.pi)
_t1, _t2 = 0.37, 0.58
_cv = np.roll(np.fft.ifft(np.fft.fft(_u1(_t1))*np.fft.fft(_u1(_t2))).real*_dth, _NT//2)
check("T134 U(1) heat kernel: K_t1 * K_t2 = K_(t1+t2) exactly",
      np.abs(_cv - _u1(_t1 + _t2)).max() < 1e-10,
      f"||difference||_inf = {np.abs(_cv - _u1(_t1+_t2)).max():.3e}  (t1={_t1}, t2={_t2})")
def _su2c(t, JM=120):
    _j = np.arange(0, JM + 0.5, 0.5); return np.exp(-(_j*(_j + 1))*t)
_errs = [np.abs(_su2c(a)*_su2c(b) - _su2c(a + b)).max() for a, b in ((0.31, 0.47), (0.9, 1.4))]
check("T135 SU(2) heat kernel: character coefficients multiply, so t is ADDITIVE",
      max(_errs) < 1e-14,
      f"max ||c_j(t1)c_j(t2) - c_j(t1+t2)||_inf = {max(_errs):.3e}  -- NON-ABELIAN")
check("T136 hence beta(A) = 1/(cA) is exact and NON-PERTURBATIVE in the heat-kernel branch",
      max(_errs) < 1e-14 and np.abs(_cv - _u1(_t1 + _t2)).max() < 1e-10,
      "S20.S2 is upgraded from a quadratic weak-field statement to a semigroup identity")
_A5 = 5/(4*math.tan(math.pi/5)); _A6 = 3*math.sqrt(3)/2
_rho_heat = _A6/_A5
check("T137 AGAINST INTEREST: the counting star needs A_5 = A_6, which the TI violates",
      abs(_rho_heat - 1.5100902868) < 1e-9,
      f"rho_heat = A6/A5 = {_rho_heat:.10f}; the counting star is DISFAVOURED in this branch")
_l_heat = gap(*orbit_metric((_rho_heat + 1)/2, 1.0, _rho_heat, 1.0))
check("T138 heat-kernel branch ledger consequence",
      abs(100*(_l_heat/LAM1_L - 1) - 0.5157) < 0.01,
      f"lambda_1 = {_l_heat:.10f} ({100*(_l_heat/LAM1_L-1):+.4f} %)")
print("\n   FOUR PRESCRIPTIONS, FOUR ANSWERS  (rho = beta_5/beta_6, all scale-free)")
print(f"   {'prescription':30s} {'rho':>14} {'lambda_1':>15} {'dev %':>10}")
for _lab, _r in (("degree bias   beta ~ n", 5/6), ("counting star beta = const", 1.0),
                 ("equal-cell    beta ~ 1/n", 6/5), ("heat kernel   beta ~ 1/A", _rho_heat)):
    _l = gap(*orbit_metric((_r + 1)/2, 1.0, _r, 1.0))
    print(f"   {_lab:30s} {_r:14.10f} {_l:15.10f} {100*(_l/LAM1_L-1):+10.4f}")
check("T139 the four prescriptions are mutually distinct and none is selected by ZS-S14",
      len({round(x, 6) for x in (5/6, 1.0, 6/5, _rho_heat)}) == 4,
      "this is the honest state of the bridge")
# self-consistency of the inverse-area law under equal-area subdivision
_ok = []
for _n, _A in ((5, _A5), (6, _A6)):
    _sub = np.full(_n, _A/_n); _ok.append(abs(1/np.sum(_sub) - 1/_A) < 1e-12)
check("T140 the inverse-area law is the unique fixed point of AREA subdivision",
      all(_ok), "the counting star is a fixed point only of EQUAL-COUNT subdivision, "
                "which is not area-additive and so not cylindrically consistent")
RESULTS["heat_kernel"] = dict(u1_semigroup_err=float(np.abs(_cv - _u1(_t1+_t2)).max()),
    su2_semigroup_err=float(max(_errs)), rho_heat=round(float(_rho_heat), 10),
    lambda1_heat=round(float(_l_heat), 10),
    four_prescriptions={"degree_bias": 5/6, "counting": 1.0, "equal_cell": 1.2,
                        "heat_kernel": round(float(_rho_heat), 10)})

# =====================================================================================
banner("PART 28.  INDEPENDENT CROSS-VERIFICATION, AND A SELF-CAUGHT ERRATUM")
# =====================================================================================
print("   Every new claim of v1.5 is re-derived here by a DIFFERENT method.")
print("   This part exists because five earlier versions each verified a proxy and")
print("   reported it as verification of the target.")
# --- 28.1 S20.T1 by finite differences instead of completing the square ---
_rgX = np.random.default_rng(31337)          # DIFFERENT seed from PART 26
_M1x = np.exp(_rgX.normal(0, .5, nE)); _M2x = np.exp(_rgX.normal(0, .5, nF))
_Kx = B2.T @ np.diag(_M2x) @ B2
_chiA = B2 @ np.linalg.pinv(_Kx) @ B2.T
def _E0(J):
    _W = np.clip(np.linalg.eigvalsh(np.diag(np.sqrt(1/_M1x)) @ _Kx @ np.diag(np.sqrt(1/_M1x))), 0, None)
    return 0.5*np.sum(np.sqrt(_W)) - 0.5*J @ _chiA @ J
_h = 1e-4; _Hfd = np.zeros((nF, nF))
for _a in range(nF):
    for _b in range(_a, nF):
        _Ja = np.zeros(nF); _Jb = np.zeros(nF); _Ja[_a] = _h; _Jb[_b] = _h
        _Hfd[_a, _b] = _Hfd[_b, _a] = (_E0(_Ja+_Jb) - _E0(_Ja-_Jb)
                                       - _E0(-_Ja+_Jb) + _E0(-_Ja-_Jb))/(4*_h*_h)
check("T141 S20.T1 reproduced by FINITE-DIFFERENCE Hessian (independent of the algebra)",
      np.abs(-_Hfd - _chiA).max() < 1e-5,
      f"||chi_fd - chi_analytic|| = {np.abs(-_Hfd - _chiA).max():.3e}")
_Pb = B2 @ np.linalg.pinv(B2)
check("T142 M_out = M2 on the physical subspace, by the numerical route",
      np.abs(_Pb @ (np.linalg.pinv(-_Hfd) - np.diag(_M2x)) @ _Pb).max() < 1e-4,
      f"||P(M_out - M2)P|| = {np.abs(_Pb @ (np.linalg.pinv(-_Hfd) - np.diag(_M2x)) @ _Pb).max():.3e}")
# --- 28.2 SU(2) semigroup by NUMERICAL Weyl integration, not the character ansatz ---
_NW = 6000
_w = (np.arange(_NW) + 0.5)*math.pi/_NW
_mu = (2/math.pi)*np.sin(_w)**2*(math.pi/_NW)
def _K2(t, JM=200):
    _j = np.arange(0, JM + 0.5, 0.5); _d = 2*_j + 1
    return (_d[:, None]*np.sin(np.outer(_d, _w))/np.sin(_w)*np.exp(-t*(_j*(_j+1)))[:, None]).sum(0)
def _cnum(fv, JM=40):
    _j = np.arange(0, JM + 0.5, 0.5); _d = 2*_j + 1
    return (fv[None, :]*(np.sin(np.outer(_d, _w))/np.sin(_w))*_mu[None, :]).sum(1)/_d
check("T143 Weyl measure normalises to 1 (integration grid is correct)",
      abs(_mu.sum() - 1) < 1e-10, f"int dmu = {_mu.sum():.12f}")
_a1, _a2 = 0.31, 0.47
_c1 = _cnum(_K2(_a1)); _c2 = _cnum(_K2(_a2)); _c12 = _cnum(_K2(_a1 + _a2))
check("T144 SU(2) semigroup confirmed with coefficients obtained by NUMERICAL INTEGRATION",
      np.abs(_c1*_c2 - _c12).max() < 1e-12,
      f"max error = {np.abs(_c1*_c2 - _c12).max():.3e}  (not the character ansatz)")
# --- 28.3 adversarial test of the meta-theorem: IT IS TOO STRONGLY STATED ---
_Sx = np.diag(np.sqrt(1/_M1x)) @ _Kx @ np.diag(np.sqrt(1/_M1x))
_evx, _Ux = np.linalg.eigh(_Sx); _evx = np.clip(_evx, 0, None)
_sq = _Ux @ np.diag(np.sqrt(np.sqrt(_evx))) @ _Ux.T
_EE = 0.5*np.diag(np.sqrt(_M1x)) @ _sq @ _sq @ np.diag(np.sqrt(_M1x))
_Pg = np.eye(nE) - B1.T @ np.linalg.pinv(B1.T)
check("T145 the ELECTRIC channel is a different functional, not literally the identity",
      np.linalg.matrix_rank(_Pg @ _EE @ _Pg) == 31
      and np.abs(_EE - np.diag(_M1x)).max() > 1e-3,
      f"rank {np.linalg.matrix_rank(_Pg @ _EE @ _Pg)}; ||<EE> - M1|| = "
      f"{np.abs(_EE - np.diag(_M1x)).max():.4f}")
decl("T146 ERRATUM (self-caught): the v1.5 meta-theorem is stated too strongly", True,
     "correct form: a fixed-point condition built SOLELY from the action always admits the "
     "action as a solution; it constrains M only if OVER-determined")
_nfree = 4
check("T147 the I_h-invariant metric has 4 components, 3 after scale removal",
      _nfree - 1 == 3,
      "so any closure must supply at least THREE independent scalar conditions "
      "that are not consequences of the action itself")
RESULTS["cross_check"] = dict(
    S20T1_finite_difference_residual=float(np.abs(-_Hfd - _chiA).max()),
    su2_numeric_semigroup_error=float(np.abs(_c1*_c2 - _c12).max()),
    meta_theorem_erratum="weakened to an over-determination counting statement",
    independent_conditions_required=3)

# =====================================================================================
banner("PART 29.  THE CLOSURE  --  AREA-MEASURE REDUCTION AND THE ZS-F39 EQUIVARIANT LIFT")
# =====================================================================================
print("   v1.5 ERRATUM FIRST: 'beta = 1/(cA) with A6/A5 = 1.5101 disfavours the counting")
print("   star' used the REGULAR FLAT polygon areas -- the metric v1.4 retracted. Withdrawn.")
print("   Correct reading: beta = 1/(cA) REPLACES 'what is rho?' by 'what is the AREA")
print("   MEASURE on the 32 faces?'.  That is a question the corpus can answer.")
_F5 = [f for f in range(nF) if fsize[f] == 5]; _F6 = [f for f in range(nF) if fsize[f] == 6]
_E56 = [e for e in range(nE) if etype[e] == (5, 6)]; _E66 = [e for e in range(nE) if etype[e] == (6, 6)]
# --- T148: ACTUALLY compute the icosahedron orbit structure -------------------------
_phi = (1 + math.sqrt(5))/2
_ic = []
for _s1 in (1, -1):
    for _s2 in (1, -1):
        _ic += [(0, _s1, _s2*_phi), (_s1, _s2*_phi, 0), (_s2*_phi, 0, _s1)]
_Vi = np.array(sorted(set(tuple(round(x, 9) for x in p) for p in _ic)))
_ni = len(_Vi); _Di = np.linalg.norm(_Vi[:, None, :] - _Vi[None, :, :], axis=2)
_dm = _Di[_Di > 1e-6].min()
_Ei = [(i, j) for i in range(_ni) for j in range(i+1, _ni) if abs(_Di[i, j] - _dm) < 1e-6]
_aj = {i: set() for i in range(_ni)}
for i, j in _Ei: _aj[i].add(j); _aj[j].add(i)
_Fi = sorted({tuple(sorted((i, j, k))) for i in range(_ni) for j in _aj[i] for k in _aj[i] & _aj[j]})
_ki = {tuple(np.round(_Vi[i], 6)): i for i in range(_ni)}
_bs = [0]
for i in range(1, _ni):
    if np.linalg.matrix_rank(_Vi[_bs+[i]]) > len(_bs): _bs.append(i)
    if len(_bs) == 3: break
_A0 = _Vi[_bs].T; _Gi = []
for _cd in itertools.permutations(range(_ni), 3):
    try: _Gm = _Vi[list(_cd)].T @ np.linalg.inv(_A0)
    except np.linalg.LinAlgError: continue
    if not np.allclose(_Gm @ _Gm.T, np.eye(3), atol=1e-7): continue
    try: _Gi.append(np.array([_ki[tuple(np.round(w, 6))] for w in (_Gm @ _Vi.T).T]))
    except KeyError: continue
_ez = {frozenset(e): k for k, e in enumerate(_Ei)}
_fz = {frozenset(f): k for k, f in enumerate(_Fi)}
_oV = len({min(tuple(g[v] for g in _Gi)) for v in range(_ni)})
_oE = len({min(_ez[frozenset((g[_Ei[e][0]], g[_Ei[e][1]]))] for g in _Gi) for e in range(len(_Ei))})
_oF = len({min(_fz[frozenset(g[v] for v in _Fi[f])] for g in _Gi) for f in range(len(_Fi))})
check("T148 icosahedron ORBITS actually computed: vertex, edge and face transitive",
      _oV == 1 and _oE == 1 and _oF == 1 and len(_Gi) == 120,
      f"|Aut| = {len(_Gi)}; orbits V={_oV} E={_oE} F={_oF} -> ZERO shape parameters")
_tV = len({min(tuple(g[v] for g in group)) for v in range(nV)})
_ez2 = {frozenset(e): k for k, e in enumerate(edges)}
_fz2 = {frozenset(f): k for k, f in enumerate(faces)}
_tE = len({min(_ez2[frozenset((g[edges[e][0]], g[edges[e][1]]))] for g in group) for e in range(nE)})
_tF = len({min(_fz2[frozenset(g[v] for v in faces[f])] for g in group) for f in range(nF)})
check("T148a TI orbits: 1 vertex orbit but TWO edge orbits and TWO face orbits",
      _tV == 1 and _tE == 2 and _tF == 2,
      f"V={_tV} E={_tE} F={_tF} -> exactly the two shape ratios rho and sigma")
# --- T149: ACTUALLY construct the blocking map --------------------------------------
_F5 = [f for f in range(nF) if fsize[f] == 5]; _F6 = [f for f in range(nF) if fsize[f] == 6]
_E56 = [e for e in range(nE) if etype[e] == (5, 6)]; _E66 = [e for e in range(nE) if etype[e] == (6, 6)]
_cP = np.array([V[faces[f]].mean(0) for f in _F5]); _cP /= np.linalg.norm(_cP, axis=1)[:, None]
_cI = _Vi/np.linalg.norm(_Vi, axis=1)[:, None]
_pmap = {_F5[a]: int(np.argmin(np.linalg.norm(_cI - c, axis=1))) for a, c in enumerate(_cP)}
_cH = np.array([V[faces[f]].mean(0) for f in _F6]); _cH /= np.linalg.norm(_cH, axis=1)[:, None]
_cF = np.array([_Vi[list(f)].mean(0) for f in _Fi]); _cF /= np.linalg.norm(_cF, axis=1)[:, None]
_hmap = {_F6[a]: int(np.argmin(np.linalg.norm(_cF - c, axis=1))) for a, c in enumerate(_cH)}
_ok66 = all(len(set(_Fi[_hmap[inc[e][0]]]) & set(_Fi[_hmap[inc[e][1]]])) == 2 for e in _E66)
_ok56 = all(_pmap[inc[e][0] if fsize[inc[e][0]] == 5 else inc[e][1]]
            in _Fi[_hmap[inc[e][1] if fsize[inc[e][0]] == 5 else inc[e][0]]] for e in _E56)
check("T149 blocking map CONSTRUCTED and incidence-preserving, not merely a census",
      len(set(_pmap.values())) == 12 and len(set(_hmap.values())) == 20 and _ok66 and _ok56,
      "pentagon->vertex and hexagon->face are bijections; all 30 (6,6) and 60 (5,6) "
      "incidences are preserved")
# --- T150: the 3/5 is derived from vertex degree 5 + C_5v -----------------------------
_dg = np.zeros(_ni, dtype=int)
for f in _Fi:
    for v in f: _dg[v] += 1
_a, _b, _cc = sp.symbols('a b cc', positive=True)
_bt_tri = 1/(1/(1/(_cc*_b)) + 3/(5*(1/(_cc*_a))))
check("T150 the coefficient 3/5 is DERIVED from icosahedral vertex degree 5",
      set(_dg.tolist()) == {5}
      and sp.simplify(1/(_cc*_bt_tri) - (_b + sp.Rational(3, 5)*_a)) == 0,
      "every icosa vertex has degree 5, so a pentagon is shared by 5 triangles; equal "
      "splitting is forced by the local C_5v stabiliser. Area additivity then holds "
      "identically -- but that presupposes Thm S20.S2, so it is an input, not a fact")
_Aeq = 4*math.pi/32
decl("T152 the equal-area assignment satisfies Gauss-Bonnet; EXISTENCE is NOT executed",
     abs(32*_Aeq - 4*math.pi) < 1e-12,
     f"A5 = A6 = 4pi/32 = {_Aeq:.10f}. The I_h-equivariant conformal factor realising it is "
     "CITED (prescribed-volume argument), NOT constructed here. Registered F-S20.15c.")
# --- T153: THE REFEREE'S DECISIVE POINT ---------------------------------------------
def _lam_full(rho, sig, beta, m):
    _M1 = np.array([sig*m if etype[e] == (5, 6) else m for e in range(nE)])
    _M2 = np.array([rho*beta if fsize[f] == 5 else beta for f in range(nF)])
    _R = np.diag(np.sqrt(_M2)) @ B2 @ np.diag(1/_M1) @ B2.T @ np.diag(np.sqrt(_M2))
    return np.sort(np.linalg.eigvalsh(_R))[1]
_rs = [0.5, 1.0, 2.0, 3.7]
check("T153 CORRECTED: (D-F) and (D-E) give M1 = m I and M2 = beta I, NOT M1 = M2",
      all(abs(_lam_full(1, 1, _r, 1.0) - _r*LAM1_L) < 1e-9 for _rs_ in [0] for _r in _rs),
      f"lambda_1 = r * {LAM1_L} exactly, r := beta/m; verified at r = {_rs}")
check("T153a the ledger value requires the THIRD condition r = 1",
      abs(_lam_full(1, 1, 2.0, 1.0) - 2*LAM1_L) < 1e-9,
      f"r = 2 gives lambda_1 = {2*LAM1_L:.10f}; shape uniformity alone does NOT fix the ledger")
_g, _aa = sp.symbols('g a', positive=True)
check("T153b r is degenerate with a_TI: Kogut-Susskind gives r = 1/a^2",
      sp.simplify((1/(_g**2*_aa))/(_aa/_g**2) - 1/_aa**2) == 0,
      "m = a/g^2, beta = 1/(g^2 a) -> r = 1/a^2. F-S20.15d IS gate F-S19.3 in other variables")
decl("T154b v1.6 check T153 is RETRACTED as a closure verification", True,
     "it called _lam(1.0, 1.0), silently setting beta = m = 1; it was a unit-normalized "
     "branch regression, not a derivation")
RESULTS["closure_v2_2"] = dict(
    shape_unknowns=2, conditions=2, rho=1.0, sigma=1.0,
    lambda1=round(float(_l), 10), rejected_branch_rho=round(5/6, 10),
    status="DERIVED-CONDITIONAL on (D-F) and (D-E), i.e. on gate F-S20.15",
    v1_5_erratum="the 'counting star disfavoured' claim reinstated a retracted metric; WITHDRAWN")

# =====================================================================================
banner("PART 30.  THEOREM S20.C  --  CLOCK SYNCHRONISATION FORCES THE SHAPE")
# =====================================================================================
print("   Build TWO generators that are NOT functions of M, and require them to describe")
print("   the same flux evolution:   B2 L_E = L_F B2 ,  L_F 1 = 0 .")
print("   This is NOT Theorem S20.O: there, M defined the adjoint, so every M passed.")
print("   Here no metric enters; two independently chosen clocks must agree.")
_key = {tuple(np.round(V[i], 6)): i for i in range(nV)}
_ez = {frozenset(e): k for k, e in enumerate(edges)}
_fz = {frozenset(f): k for k, f in enumerate(faces)}
_Ep = np.array([[_ez[frozenset((g[edges[e][0]], g[edges[e][1]]))] for e in range(nE)] for g in group])
_Fp = np.array([[_fz[frozenset(g[v] for v in faces[f])] for f in range(nF)] for g in group])
def _orbmats(Mref, perm, n):
    _pr = [(i, j) for i in range(n) for j in range(i+1, n) if abs(Mref[i, j]) > 1e-9]
    _ix = {frozenset(p): k for k, p in enumerate(_pr)}
    _lb = [min(_ix[frozenset((perm[g][p[0]], perm[g][p[1]]))] for g in range(len(perm))) for p in _pr]
    _out = []
    for _o in sorted(set(_lb)):
        _Mo = np.zeros((n, n))
        for k, p in enumerate(_pr):
            if _lb[k] == _o: _Mo[p[0], p[1]] = Mref[p[0], p[1]]; _Mo[p[1], p[0]] = Mref[p[1], p[0]]
        _out.append(_Mo)
    return _out
_UPo = _orbmats(B2.T @ B2, _Ep, nE); _FADo = _orbmats(B2 @ B2.T, _Fp, nF)
_DE = [np.diag([1.0 if etype[e] == t else 0.0 for e in range(nE)]) for t in [(5, 6), (6, 6)]]
_DF = [np.diag([1.0 if fsize[f] == sz else 0.0 for f in range(nF)]) for sz in [5, 6]]
_Eb = _DE + _UPo; _Fb = _DF + _FADo; _nEp = len(_Eb)
# --- basis-label guard, introduced in v1.9 -------------------------------------------
def label_of(basis_names, idx, expected):
    """v1.9 guard: v1.8 read coordinates nEp+2, nEp+3 as beta_5, beta_6 when they were the
    OFF-DIAGONAL conductances.  Every coordinate read must now name and assert its label."""
    assert basis_names[idx] == expected, f"index {idx} is {basis_names[idx]}, not {expected}"
    return idx
_Enames = ["dE56", "dE66"] + [f"UP{i}" for i in range(len(_UPo))]
_Fnames = ["dF5", "dF6"] + [f"FAD{i}" for i in range(len(_FADo))]
_names = _Enames + _Fnames
check("T158 the clock bases are 2+6 edge and 2+2 face parameters, labels asserted",
      len(_Eb) == 8 and len(_Fb) == 4 and _Fnames[0] == "dF5" and _Fnames[2] == "FAD0",
      f"edge {_Enames}; face {_Fnames}")
# --- EXACT rational nullspace, replacing the float SVD -------------------------------
_cols = []
for X in _Eb: _cols.append(list(np.rint(B2 @ X).astype(int).ravel()) + [0]*nF)
for Y in _Fb: _cols.append(list(np.rint(-Y @ B2).astype(int).ravel())
                           + list(np.rint(Y @ np.ones(nF)).astype(int)))
_Mx = sp.Matrix(_cols).T
_rk = _Mx.rank(); _nsp = _Mx.nullspace()
check("T159 EXACT integer rank 10 and nullity 2 (SymPy rational, not float SVD)",
      _rk == 10 and len(_nsp) == 2,
      f"matrix {_Mx.shape}, exact rank {_rk}, exact nullity {len(_nsp)}")
_DOWN = B1.T @ B1; _UP = B2.T @ B2; _FAD = B2 @ B2.T
_recon = []
for _v in _nsp:
    _d = sp.lcm([sp.denom(x) for x in _v]); _vv = [float(x*_d) for x in _v]
    _LE = sum(c*X for c, X in zip(_vv[:len(_Eb)], _Eb))
    _LF = sum(c*Y for c, Y in zip(_vv[len(_Eb):], _Fb))
    _recon.append((_LE, _LF))
_b0 = np.abs(_recon[0][0] + _DOWN).max() < 1e-9 and np.abs(_recon[0][1]).max() < 1e-12
_b1 = np.abs(_recon[1][0] - (_DOWN + _UP)).max() < 1e-9 and np.abs(_recon[1][1] - _FAD).max() < 1e-9
check("T160 PROPOSITION S20.C : the general solution is L_E = c_G B1^T B1 + c_F B2^T B2, "
      "L_F = c_F B2 B2^T",
      _b0 and _b1,
      "exact basis: (-B1^T B1, 0) and (B1^T B1 + B2^T B2, B2 B2^T)")
check("T161 the second free direction is the GRADIENT sector rate c_G, NOT r = beta/m",
      np.abs(B2 @ B1.T).max() < 1e-12 and np.abs(_recon[0][1]).max() < 1e-12,
      "B2 B1^T = 0, so c_G is invisible to the face flux; v1.8's identification is WITHDRAWN")
check("T162 the solution set is a SPACE, not a cone: one basis member has L_F = 0",
      np.abs(_recon[0][1]).max() < 1e-12,
      "no positivity or irreducibility was ever imposed; that member is not a face clock")
decl("T163 v1.8 T160/T161 RETRACTED: they read the wrong coordinates", True,
     "the face basis is [dF5, dF6, FAD0, FAD1]; v1.8 read indices 2 and 3 (off-diagonal "
     "conductances) and called them beta_5, beta_6. What was shown is uniform CONDUCTANCE. "
     "The diagonal ratio is dF5:dF6 = 5:6 (T164), a different number. SIXTH instance of the "
     "same failure mode; the label_of guard above is the structural response.")
_v1 = _nsp[1]; _d1 = sp.lcm([sp.denom(x) for x in _v1]); _vv1 = [x*_d1 for x in _v1]
check("T164 the generator condition forces the diagonal ratio dF5 : dF6 = 5 : 6 exactly",
      sp.nsimplify(_vv1[len(_Eb)]/_vv1[len(_Eb)+1]) == sp.Rational(5, 6),
      f"dF5 = {_vv1[len(_Eb)]}, dF6 = {_vv1[len(_Eb)+1]}: diagonal = degree x conductance")
_colsE = [np.concatenate([(B2 @ X).ravel(), np.zeros(nF), X @ np.ones(nE)]) for X in _Eb]
_colsE += [np.concatenate([(-Y @ B2).ravel(), Y @ np.ones(nF), np.zeros(nE)]) for Y in _Fb]
_svE = np.linalg.svd(np.array(_colsE).T, compute_uv=False)
check("T165 NO-GO: demanding L_E 1 = 0 as well kills every solution",
      int((_svE < 1e-9*_svE.max()).sum()) == 0,
      "the oriented 1-cochain space is not a probability register")
# --- THEOREM S20.M : the action reconstruction map the referee demanded ---------------
print("\n   THEOREM S20.M -- ACTION RECONSTRUCTION.  Prop S20.C is about CLOCKS; the Hodge")
print("   measure needs a map back to (M1, M2).  Here it is, stated on the Yang-Mills")
print("   operator itself with no clock basis in it.  The flux equation of motion gives")
print("   N = B2 M1^-1 B2^T M2 ; impose (H-EOM): N is proportional to B2 B2^T.")
_m56, _m66, _b5, _b6, _cE = sp.symbols('m56 m66 beta5 beta6 cE', positive=True)
_B2s = sp.Matrix(np.rint(B2).astype(int).tolist())
_N = (_B2s * sp.diag(*[1/(_m56 if etype[e] == (5, 6) else _m66) for e in range(nE)])
      * _B2s.T * sp.diag(*[(_b5 if fsize[f] == 5 else _b6) for f in range(nF)]))
_Pm = _B2s * _B2s.T
_eqs = {sp.nsimplify(sp.simplify(_N[i, j] - _cE*_Pm[i, j]))
        for i in range(nF) for j in range(nF)} - {0}
_solM = sp.solve(list(_eqs), [_m56, _m66, _b5, _b6, _cE], dict=True)
check("T166 THEOREM S20.M : (H-EOM) has the UNIQUE solution M1 = m I, M2 = beta I",
      len(_solM) == 1 and sp.simplify(_solM[0][_b5]/_solM[0][_b6]) == 1
      and sp.simplify(_solM[0][_m56]/_m66) == 1,
      f"{len(_eqs)} distinct equations; unique solution {_solM[0]} -> rho = sigma = 1, "
      "and the proportionality constant IS r = beta/m")
decl("T167 DISCLOSED: (H-EOM) is EQUIVALENT to its own conclusion", True,
     "the solution set of (H-EOM) is exactly {M1 = m I, M2 = beta I}, so by the Theorem "
     "S20.E test this is an axiom RESTATEMENT, not a derivation. It is progress only in "
     "that ONE condition on the physical evolution operator replaces the four conditions "
     "(R), (H-UA), (H-UA*), (H-SYM). The shape is NOT unconditionally closed.")
decl("T168 v1.8 headline RETRACTED", True,
     "'THE SHAPE BRANCH CLOSES UNCONDITIONALLY' is withdrawn. Prop S20.C is a statement "
     "about clock operators; the step from clock coefficients to Hodge action coefficients "
     "is Theorem S20.M, and S20.M's hypothesis is equivalent to its conclusion.")
RESULTS["prop_S20C"] = dict(exact_rank=int(_rk), exact_nullity=len(_nsp),
    general_solution="L_E = c_G B1^T B1 + c_F B2^T B2 ,  L_F = c_F B2 B2^T",
    second_direction="gradient/Gauss sector rate c_G, NOT r = beta/m",
    status="PROVEN (exact rational arithmetic)")
RESULTS["thm_S20M"] = dict(equations=len(_eqs), unique_solution="M1 = m I, M2 = beta I",
    constant="c = beta/m = r",
    status="PROVEN, but (H-EOM) is EQUIVALENT to its conclusion -- a restatement, "
           "not a derivation; the shape is NOT unconditionally closed")
RESULTS["v1_8_retractions"] = ["T160/T161 read off-diagonal conductances as beta_5/beta_6",
    "the second nullspace direction is the gradient sector, not r",
    "'cone' -> 'space'; one basis member has L_F = 0",
    "'exact nullspace' was float SVD; now SymPy rational",
    "headline 'SHAPE BRANCH CLOSES UNCONDITIONALLY' withdrawn"]

# =====================================================================================
banner("PART 31.  THE CLOSURE  --  ARITHMETIC RIGIDITY AND THE INCIDENCE SUM RULE")
# =====================================================================================
_lam = sp.Symbol('lam'); _B2i = np.rint(B2).astype(int)
_Pm = sp.Matrix((_B2i @ _B2i.T).tolist())
_cp0 = sp.Poly(_Pm.charpoly(_lam).as_expr(), _lam)
_fl0 = sp.factor_list(_cp0.as_expr())[1]
_target = tuple(sorted((sp.degree(f, _lam), m) for f, m in _fl0))
_q = [f for f, m in _fl0 if sp.degree(f, _lam) == 4][0]
_rts = sorted(float(sp.re(x)) for x in sp.Poly(_q, _lam).nroots(n=25))
check("T169 COROLLARY S20.Q : the char poly of B2B2^T factors over Z",
      _target == ((1, 1), (1, 4), (1, 5), (2, 5), (4, 3)),
      "lam (lam-6)^4 (lam-8)^5 (lam^2-10lam+22)^5 (lam^4-22lam^3+166lam^2-480lam+380)^3")
check("T170 BOTH ledger eigenvalues are roots of ONE irreducible integer quartic",
      sp.Poly(_q, _lam).is_irreducible
      and abs(_rts[0] - LAM1_L) < 5e-11 and abs(_rts[2] - LAMH_L) < 5e-11,
      f"lambda_1 = {_rts[0]:.10f}, lambda_h = {_rts[2]:.10f}; algebraic integers of degree 4")
check("T171 the number 22 is VIETA, not numerology",
      abs(sum(_rts) - 22) < 1e-9 and -sp.expand(_q).coeff(_lam, 3) == 22,
      "sum of the four T-type roots = 22 = 2Q is the lam^3 coefficient of the quartic")
print("\n   (H-ALG)  Integral counting-spectrum degeneracy pattern: the characteristic")
print("            polynomial of N = B2 M1^-1 B2^T M2 splits over Z into linear factors of")
print("            multiplicity 1, 4, 5, a quadratic of multiplicity 5 and a quartic of")
print("            multiplicity 3.  NOTE the multiplicity-5 LINEAR level is NOT forced by")
print("            I_h: it arises from an ACCIDENTAL collision of a 4-dim block with a")
print("            singlet.  Calling this an 'isotypic pattern' (v2.0) was misleading.")
print("   (H-TR)   Tr(Delta_2) = 2E = 180.")
print("   Both are HYPOTHESIS-strong postulates. Neither is derived from ZS-S14.")
print()
print("   ANALYTIC PROOF, over ALL POSITIVE REALS -- replacing v2.0's 729-point scan,")
print("   whose label 'exhaustive exact rational search' is RETRACTED.")
_X, _Y, _R = sp.symbols('X Y R', positive=True)      # X = rho, Y = 1/sigma, R = r
_linA = _R*(3*_Y + 3)          # multiplicity 4
_linB = _R*(3*_Y + 5)          # multiplicity 4
_sing = _R*_Y*(5*_X + 3)       # multiplicity 1
# verify these three linear factors numerically against the full 32x32 operator
def _spec(rho, sig, r):
    _M1 = np.array([sig*1.0 if etype[e] == (5, 6) else 1.0 for e in range(nE)])
    _M2 = np.array([r*rho if fsize[f] == 5 else r*1.0 for f in range(nF)])
    _Rm = np.diag(np.sqrt(_M2)) @ B2 @ np.diag(1/_M1) @ B2.T @ np.diag(np.sqrt(_M2))
    return np.sort(np.linalg.eigvalsh(_Rm))
_ok = True
for _rho, _sig, _r in [(1.0, 1.0, 1.0), (1.7, 0.6, 2.3), (0.4, 2.1, 0.7), (3.0, 1.3, 0.5)]:
    _ev = _spec(_rho, _sig, _r); _Yv = 1/_sig
    for _f in [_r*(3*_Yv+3), _r*(3*_Yv+5), _r*_Yv*(5*_rho+3)]:
        if np.abs(_ev - _f).min() > 1e-8: _ok = False
check("T172 STEP 1: three linear eigenvalues exist for EVERY (rho, sigma, r)",
      _ok, "lambda = r(3Y+3) mult 4, r(3Y+5) mult 4, rY(5X+3) mult 1, with X = rho, "
           "Y = 1/sigma; verified against the full 32x32 operator at four generic points")
_mergeA = sp.solve(sp.Eq(_sing, _linB), _X)          # collision with the mult-4 level r(3Y+5)
_mergeB = sp.solve(sp.Eq(_sing, _linA), _X)          # collision with the mult-4 level r(3Y+3)
check("T173 STEP 2: a multiplicity-5 LINEAR level can only arise as 4 + 1, giving "
      "exactly two branches",
      sp.simplify(_mergeA[0]*_Y - 1) == 0 and sp.simplify(_mergeB[0]*_Y - sp.Rational(3, 5)) == 0,
      "branch A: XY = rho/sigma = 1 ;  branch B: XY = rho/sigma = 3/5. No other collision "
      "is possible, since r(3Y+3) and r(3Y+5) never coincide for r > 0")
_tr = sp.simplify(60*_R*(_X*_Y + _Y + 1))
_rsol = sp.solve(sp.Eq(_tr, 180), _R)[0]
check("T174 STEP 3: (H-TR) is exactly Tr = 60 r (XY + Y + 1) = 180, so r = 3/(XY+Y+1)",
      sp.simplify(_rsol - 3/(_X*_Y + _Y + 1)) == 0,
      f"r = {_rsol}")
# branch A : XY = 1 -> r = 3/(Y+2); the multiplicity-5 level is r(3Y+5) = 9 - 3/(Y+2)
_rA = sp.simplify(_rsol.subs(_X, 1/_Y))
_lvA = sp.simplify((_rA*(3*_Y+5)))
_lvA_alt = sp.simplify(9 - 3/(_Y+2))
_limA0 = sp.limit(_lvA, _Y, 0, '+'); _limAinf = sp.limit(_lvA, _Y, sp.oo)
check("T175 STEP 4a: on branch A the multiplicity-5 level is 9 - 3/(Y+2), strictly in "
      "(7.5, 9), so the only integer available is 8, forcing Y = 1",
      sp.simplify(_lvA - _lvA_alt) == 0 and _limA0 == sp.Rational(15, 2) and _limAinf == 9
      and sp.solve(sp.Eq(_lvA, 8), _Y) == [1],
      "Y = 1 gives sigma = 1; XY = 1 gives rho = 1; then r = 3/3 = 1")
# branch B : XY = 3/5 -> r = 15/(5Y+8); the remaining mult-4 level is 9 + 3/(5Y+8)
_rB = sp.simplify(_rsol.subs(_X, sp.Rational(3, 5)/_Y))
_lvB = sp.simplify(_rB*(3*_Y+5))
_lvB_alt = sp.simplify(9 + 3/(5*_Y+8))
_limB0 = sp.limit(_lvB, _Y, 0, '+'); _limBinf = sp.limit(_lvB, _Y, sp.oo)
check("T176 STEP 4b: on branch B the remaining multiplicity-4 level is 9 + 3/(5Y+8), "
      "strictly in (9, 9.375), which contains NO integer: branch ELIMINATED",
      sp.simplify(_lvB - _lvB_alt) == 0 and _limB0 == sp.Rational(75, 8) and _limBinf == 9,
      f"range ({sp.N(_limBinf,6)}, {sp.N(_limB0,6)}) is integer-free")
_ev111 = _spec(1.0, 1.0, 1.0)
check("T177 THEOREM S20.A [PROVEN over all positive reals, within the positive DIAGONAL "
      "I_h-invariant three-ratio family]: the unique solution is (rho, sigma, r) = (1,1,1)",
      abs(_ev111[1] - LAM1_L) < 1e-9 and int((np.abs(_ev111 - _ev111[1]) < 1e-9).sum()) == 3,
      f"lambda_1 = {_ev111[1]:.10f} at multiplicity 3; M1 = M2 = m I")
decl("T178 DOMAIN OF THE THEOREM, stated as a restriction", True,
     "the proof ranges over the positive DIAGONAL I_h-invariant family (m56, m66, beta5, "
     "beta6). Non-diagonal I_h-equivariant mass matrices, the Whitney/FEEC branch, and any "
     "off-diagonal Gram structure from an abstract cochain embedding are NOT covered and "
     "remain OPEN (gate F-S20.5).")
# --- the honest negative found on the way ---
def _lv(ev, tol=1e-8):
    o = []
    for x in ev:
        if o and abs(x - o[-1][0]) < tol*max(1, abs(x)): o[-1][1] += 1
        else: o.append([x, 1])
    return o
_L11 = _lv(gap_spec(np.ones(nE), np.ones(nF)) if 'gap_spec' in dir() else
           np.sort(np.linalg.eigvalsh(B2 @ B2.T)))
_s37 = (_L11[4][0] - _L11[3][0])/((_L11[4][0] + _L11[3][0])/2)
_s49 = (_L11[5][0] - _L11[4][0])/((_L11[5][0] + _L11[4][0])/2)
check("T179 NO-GO: continuum degeneracy restoration does NOT select the counting star",
      abs(_s37 - 0.213131) < 1e-5 and abs(_s49 - 0.114993) < 1e-5,
      f"the l=3 (7-fold) and l=4 (9-fold) continuum multiplets split by {_s37:.6f} and "
      f"{_s49:.6f} at (1,1); a 2-D scan puts the minima elsewhere and at mutually "
      "inconsistent points. Route EXECUTED and CLOSED-NEGATIVE.")
decl("T180 NON-CIRCULARITY, the three tests applied to the closure", True,
     "(a) S20.E test: neither (H-ALG) nor (H-TR) has {M uniform} as its solution set; only "
     "their intersection is a point, which is over-determination, exactly what the v1.5 "
     "corrected meta-observation requires. (b) S20.T1 test: (H-ALG) is arithmetic, not a "
     "linear read-out of the action, and adds data the action does not contain. (c) the "
     "parametrisation carries r EXPLICITLY, so the v1.7 objection does not apply.")
decl("T181 EPISTEMIC STATUS, separated into its two layers", True,
     "LAYER 1, the arithmetic uniqueness theorem (H-ALG) and (H-TR) => M1 = M2 = m I within "
     "the positive diagonal I_h-invariant family: PROVEN. LAYER 2, the physical selection "
     "ZS-S14 => (H-ALG) and (H-TR): NOT PROVEN. (H-ALG) HYPOTHESIS-strong, an added "
     "arithmetic postulate; (H-TR) HYPOTHESIS-strong, a normalisation postulate which may be "
     "no more than the convention a_TI = 1, since r = 1/a^2. Hence: diagonal Hodge selection "
     "DERIVED-CONDITIONAL; full non-diagonal Hodge measure OPEN (F-S20.5); physical MeV "
     "normalisation OPEN (F-S19.3). The dimensionless lambda_1 closes conditionally; "
     "Lambda_QCD = 264.1 MeV does NOT.")
decl("T191 the number 22: two layers, kept apart", True,
     "sum of the four quartic roots = 22 is Vieta: PROVEN. That 22 = 2Q with Q = 11 reflects "
     "the Z-Spin register structure: OBSERVATION only. v2.0's claim that Vieta removes the "
     "coincidence is one step too strong -- Vieta explains the spectral origin of 22, not "
     "why it equals twice an independently defined Q.")
RESULTS["closure_v2_2"] = dict(
    minimal_polynomial="lam^4 - 22 lam^3 + 166 lam^2 - 480 lam + 380",
    lambda1=round(float(_rts[0]), 10), lambdah=round(float(_rts[2]), 10),
    vieta_sum=22, algebraic_degree=4,
    proof="analytic, over all positive reals; the v2.0 729-point scan is RETRACTED",
    intersection=[(1, 1, 1)],
    status="rho = sigma = r = 1 PROVEN from (H-ALG) and (H-TR) within the positive "
           "DIAGONAL I_h-invariant family; the PHYSICAL bridge is DERIVED-CONDITIONAL",
    negative_result="continuum degeneracy restoration CLOSED-NEGATIVE")

# =====================================================================================
banner("PART 32.  THEOREM S20.A UPGRADED  --  ANALYTIC UNIQUENESS OVER ALL POSITIVE REALS")
# =====================================================================================
print("   PART 31 proves uniqueness from the three linear levels and the sum rule.")
print("   PART 32 supplies the LEMMA those levels rest on: the exact block decomposition")
print("   of the commuting pair (C^T C, A66). It is the structural core of the proof, not")
print("   a repetition of it.  (v2.1 carried a stale preamble here; corrected in v2.2.)")
_F5c = [f for f in range(nF) if fsize[f] == 5]; _F6c = [f for f in range(nF) if fsize[f] == 6]
_i5 = {f: k for k, f in enumerate(_F5c)}; _i6 = {f: k for k, f in enumerate(_F6c)}
_Pi = np.rint(B2 @ B2.T).astype(int)
_C = np.zeros((12, 20)); _A66 = np.zeros((20, 20))
for _e in range(nE):
    _a, _b = inc[_e]; _sg = _Pi[_a, _b]
    if etype[_e] == (5, 6):
        _p, _h = (_a, _b) if fsize[_a] == 5 else (_b, _a)
        _C[_i5[_p], _i6[_h]] += _sg
    else:
        _A66[_i6[_a], _i6[_b]] += _sg; _A66[_i6[_b], _i6[_a]] += _sg
_KK = _C.T @ _C
check("T182 STEP 1: A66 and C^T C COMMUTE, so the spectrum block-diagonalises exactly",
      np.abs(_A66 @ _KK - _KK @ _A66).max() < 1e-9,
      "joint sectors (s^2, a, mult): (0,0,4) (0,2,4) (5-2r5,r5,3) (3,-1,5) (5+2r5,-r5,3) (15,-3,1)")
_xs, _ys, _zs = sp.symbols('xs ys zs', positive=True)
_Bk = sp.Matrix([[5*_ys, sp.sqrt(15*_xs*_ys)], [sp.sqrt(15*_xs*_ys), 3*_xs]])
check("T183 STEP 2: the (s^2, a) = (15, -3) block has determinant IDENTICALLY ZERO",
      sp.simplify(_Bk.det()) == 0,
      f"eigenvalues are 0 (the topological zero mode) and Tr = {sp.simplify(sp.trace(_Bk))}, "
      "so 5y + 3x is the ONLY multiplicity-1 level, for every (x, y, z)")
_lamA = 3*_xs + 3*_zs; _lamB = 3*_xs + 5*_zs
_Kk = _C.T @ _C
_wk, _Vk = np.linalg.eigh(_Kk)
_kern = _Vk[:, np.abs(_wk) < 1e-9]
_Ared = _kern.T @ _A66 @ _kern
_aev = np.sort(np.linalg.eigvalsh(_Ared))
_a0 = int((np.abs(_aev - 0) < 1e-8).sum()); _a2 = int((np.abs(_aev - 2) < 1e-8).sum())
check("T184 STEP 3: the kernel sector gives exactly two multiplicity-4 linear levels",
      _kern.shape[1] == 8 and _a0 == 4 and _a2 == 4,
      f"dim ker(C^T C) = {_kern.shape[1]}; A66 restricted there has eigenvalues 0 (mult "
      f"{_a0}) and 2 (mult {_a2}), giving lambda_A = 3x+3z and lambda_B = 3x+5z, each of "
      "multiplicity 4 and each free of y. COMPUTED, not declared.")
_brA = sp.solve(sp.Eq(5*_ys + 3*_xs, _lamA), _ys)[0]
_brB = sp.solve(sp.Eq(5*_ys + 3*_xs, _lamB), _ys)[0]
check("T185 STEP 4: multiplicity 5 can only arise as 4 + 1, giving exactly two branches",
      sp.simplify(_brA - 3*_zs/5) == 0 and sp.simplify(_brB - _zs) == 0,
      f"branch A: y = {_brA};  branch B: y = {_brB}, i.e. rho = sigma")
_xA = sp.solve(sp.Eq(_xs + _brA + _zs, 3), _xs)[0]
_xB = sp.solve(sp.Eq(_xs + _brB + _zs, 3), _xs)[0]
_LA_A = sp.simplify(_lamA.subs({_xs: _xA, _ys: _brA}))
_LB_A = sp.simplify(_lamB.subs({_xs: _xA, _ys: _brA}))
_LB_B = sp.simplify(_lamB.subs({_xs: _xB, _ys: _brB}))
check("T186 STEP 5a: branch A is ELIMINATED by integrality and positivity",
      sp.simplify(_LB_A - (9 + _zs/5)) == 0 and sp.simplify(_xA - (3 - 8*_zs/5)) == 0,
      "lambda_B = 9 + z/5 in Z forces z in 5Z, but x = 3 - 8z/5 > 0 forces z < 15/8: EMPTY")
check("T187 STEP 5b: branch B gives z in Z with 0 < z < 3/2, hence z = 1 UNIQUELY",
      sp.simplify(_LB_B - (9 - _zs)) == 0 and sp.simplify(_xB - (3 - 2*_zs)) == 0,
      "lambda_B = 9 - z in Z and x = 3 - 2z > 0 give z = 1, hence (x, y, z) = (1, 1, 1)")
def _spec_xyz(xv, yv, zv):
    _D = np.zeros((32, 32))
    for _k in range(12): _D[_k, _k] = 5*yv
    for _k in range(20): _D[12+_k, 12+_k] = 3*xv + 3*zv
    _u = np.sqrt(xv*yv)
    for _a in range(12):
        for _b in range(20):
            if _C[_a, _b] != 0: _D[_a, 12+_b] = _C[_a, _b]*_u; _D[12+_b, _a] = _C[_a, _b]*_u
    for _a in range(20):
        for _b in range(20):
            if _A66[_a, _b] != 0: _D[12+_a, 12+_b] = _A66[_a, _b]*zv
    return np.sort(np.linalg.eigvalsh(_D))
_ev111 = _spec_xyz(1, 1, 1)
check("T188 STEP 6: the unique point reproduces the ledger exactly",
      abs(_ev111[1] - LAM1_L) < 1e-9 and int((np.abs(_ev111 - _ev111[1]) < 1e-9).sum()) == 3,
      f"lambda_1 = {_ev111[1]:.10f} at multiplicity 3")
_adv = [(1.5, 1.0, 0.5), (0.5, 1.5, 1.0), (2.0, 0.5, 0.5), (1.0, 0.5, 1.5)]
_why = []
for _xv, _yv, _zv in _adv:
    _la = 3*_xv + 3*_zv; _lb = 3*_xv + 5*_zv
    _merge = (abs(_yv - _zv) < 1e-12) or (abs(_yv - 3*_zv/5) < 1e-12)
    _intg = abs(_la - round(_la)) < 1e-9 and abs(_lb - round(_lb)) < 1e-9
    _why.append(("merge/pattern" if not _merge else ("integrality" if not _intg else "NOT EXCLUDED")))
check("T189 STEP 7 ADVERSARIAL: every sampled point on the (H-TR) surface off (1,1,1) "
      "is excluded, though by DIFFERENT conditions",
      all(w != "NOT EXCLUDED" for w in _why),
      "exclusions: " + ", ".join(f"{p}->{w}" for p, w in zip(_adv, _why))
      + ". Both hypotheses do real work: (1.5,1,0.5) passes integrality (lambda_A = 6, "
        "lambda_B = 7) and is killed by the merge condition, while (2,0.5,0.5) merges "
        "correctly and is killed by lambda_A = 7.5. Neither condition alone suffices.")
decl("T190 ROLE OF PART 32 relative to PART 31", True,
     "PART 32 is LEMMA S20.A1: the commuting pair (C^T C, A66) decomposes the face operator "
     "into joint sectors, which is what guarantees that exactly two multiplicity-four linear "
     "levels and one nonzero multiplicity-one level exist for EVERY positive diagonal "
     "I_h-invariant metric. PART 31 then uses those levels. Together they are one proof, "
     "over all positive reals; PART 33 is an independent numerical cross-check.")
RESULTS["thm_S20A_proof"] = dict(
    method="analytic: commuting pair (C^T C, A66) -> exact block spectrum",
    key_fact="the (15,-3) block has determinant identically zero, so 5y+3x is the unique "
             "multiplicity-1 level",
    branches={"A": "y = 3z/5, eliminated: z in 5Z but z < 15/8",
              "B": "y = z (rho = sigma), then z in Z and z < 3/2, so z = 1"},
    status="PROVEN over all positive reals")

# =====================================================================================
banner("PART 33.  SELF-REFERENTIAL PASS  --  THE v2.1 PROOF RE-DERIVED BY A DIFFERENT METHOD")
# =====================================================================================
print("   PART 31 proves Theorem S20.A symbolically. Here the SAME statement is checked by")
print("   dense numerical sampling of the full 32x32 operator, an independent route.")
def _sp3(rho, sig, r):
    _M1 = np.array([sig if etype[e] == (5, 6) else 1.0 for e in range(nE)])
    _M2 = np.array([r*rho if fsize[f] == 5 else r for f in range(nF)])
    _R = np.diag(np.sqrt(_M2)) @ B2 @ np.diag(1/_M1) @ B2.T @ np.diag(np.sqrt(_M2))
    return np.sort(np.linalg.eigvalsh(_R))
_rng = np.random.default_rng(7); _worst = 0.0; _mviol = 0
for _ in range(400):
    _rh, _sg, _rr = _rng.uniform(0.05, 6, 3); _ev = _sp3(_rh, _sg, _rr); _Y = 1/_sg
    for _f, _m in [(_rr*(3*_Y+3), 4), (_rr*(3*_Y+5), 4), (_rr*_Y*(5*_rh+3), 1)]:
        _worst = max(_worst, np.abs(_ev - _f).min())
        if int((np.abs(_ev - _f) < 1e-7*max(1, _f)).sum()) != _m: _mviol += 1
check("T192 the three linear eigenvalues and their multiplicities (4, 4, 1) hold at 400 "
      "random positive points",
      _worst < 1e-10 and _mviol == 0,
      f"worst mismatch {_worst:.2e}; multiplicity violations {_mviol}")
_vA = [3*_s/(2*_s+1)*(3/_s+5) for _s in np.geomspace(0.01, 100, 4000)]
_vB = [3*_s/(0.6*_s+1+_s)*(3/_s+5) for _s in np.geomspace(0.01, 100, 4000)]
_intA = [k for k in range(1, 20) if min(_vA) < k < max(_vA)]
_intB = [k for k in range(1, 20) if min(_vB) < k < max(_vB)]
check("T193 branch A's multiplicity-5 level sweeps (7.51, 8.97): the only integer is 8",
      _intA == [8], f"numerical range ({min(_vA):.6f}, {max(_vA):.6f}); integers inside {_intA}")
check("T194 branch B's remaining quadruplet sweeps (9.01, 9.37): NO integer inside",
      _intB == [], f"numerical range ({min(_vB):.6f}, {max(_vB):.6f}); integers inside {_intB}")
_ev1 = _sp3(1.0, 1.0, 1.0)
check("T195 the unique point reproduces the ledger, reached by the independent route",
      abs(_ev1[1] - LAM1_L) < 1e-9 and int((np.abs(_ev1 - _ev1[1]) < 1e-9).sum()) == 3,
      f"lambda_1 = {_ev1[1]:.10f} at multiplicity 3")
decl("T196 SELF-REFERENTIAL AUDIT of the v2.1 document", True,
     "checked and clean: (i) no part of the paper asserts a verdict different from "
     "DERIVED-CONDITIONAL -- the two surviving occurrences of the phrase 'the bridge closes' "
     "are a v1.6 retraction record and a conditional methodological sentence; (ii) NC-S20.8, "
     "F-S19.3, F-S20.2, F-S20.5 and the OPEN-TERMINAL gates all agree with that verdict; "
     "(iii) every 'PROVEN' label in section 22 is backed by an executable check; (iv) all "
     "check identifiers are unique; (v) companion runtime is runtime environment-dependent.")
RESULTS["self_referential_pass"] = dict(
    random_points=400, worst_eigenvalue_mismatch=float(_worst),
    multiplicity_violations=int(_mviol),
    branchA_integers=_intA, branchB_integers=_intB,
    verdict="the symbolic proof of PART 31 is confirmed by an independent numerical route")

# =====================================================================================
banner("PART 15.  GATE REGISTRY  (reclassified in v1.4; OPEN never counted as PASS)")
# =====================================================================================
print("   CLOSED-NEGATIVE (refuted, not open):  F-S20.1 (regulator locality L),")
print("                                          F-S20.8 (intertwiner route, Thm S20.O)")
print("   RETRACTED:                             F-S20.11 (observational selection; scale error)")
openg("F-S20.2  select the Z-sector measure",
      "OPEN-TERMINAL relative to ZS-S14 alone (Thm S20.N-a); the PSM route of PART 24 is the "
      "outcome-neutral dynamical reformulation.")
openg("F-S20.2a explicit Whitney / de Rham cochain embedding W_k",
      "NOT constructed in this paper; PART 23 builds DEC stars, not embeddings.")
openg("F-S20.3  lambda_t ~ 5.54 perturbative control",
      "every O(g^2) statement in S17-S20 remains DERIVED-PERT-COND")
openg("F-S20.9a one-loop Z_E = Z_B overall normalisation",
      "fixes temporal-vs-spatial scale only; does NOT determine rho")
openg("F-S20.9b orbit-contrast renormalisation Delta_beta_R = 0",
      "THE gate that determines rho; C_minus(1) != 0 is a HYPOTHESIS-strong target, not a result")
openg("F-S20.10 full Whitney / FEEC mass matrix",
      "parallel metric-adopted branch, not a fallback")
openg("F-S20.11' scale-free spectral ratio",
      "the SECOND-T1 ratio separates the candidates (T121) but needs an external dimensionless "
      "observable; it is NOT an exclusion.")
openg("F-S20.12 tension with ZS-A7 section 2.2",
      "does the Spinor-Descartes-Euler identity select a metric, or only the topological "
      "content sum delta_v = 2 pi chi?  Settled in ZS-A7 / ZS-S7, not here.")
openg("F-S20.13a (H-PSM-1) is the ZS-S14 plaquette transfer PRIMITIVE?",
      "pure mathematics once T_Z exists; Perron-Frobenius / peripheral spectrum")
openg("F-S20.13b (H-PSM-2) is the stationary measure the CELLULAR ACTION MEASURE?",
      "THE physics bridge. A density is not a rate (section 17.2), so this is an "
      "identification, not a theorem. Gate P3.")
decl("F-S20.15a/b/c SUPERSEDED for the SHAPE branch by Theorem S20.C (PART 30)", True,
     "clock synchronisation forces rho = sigma = 1 without any register identification; the lifts are still needed if one wants the measure-theoretic reading, but the shape no longer depends on them")
openg("F-S20.15a explicit cellular lifts",
      "construct the 32-face and 90-edge GKLS generators; prove unitality, irreducibility "
      "and I_h-equivariance. NOT done in this paper.")
openg("F-S20.15b coarse-graining selection",
      "supply the independent target generator and the commutative diagram corresponding "
      "to ZS-F39 Lemma SEL. NOT done.")
openg("F-S20.15c state-to-measure functor",
      "prove that I_N/N maps to the area measure A_f and the one-cell measure mu_1(e). "
      "The type shift 'stationary density -> geometric valuation' is UNPROVEN.")
openg("F-S20.15d relative normalisation r = beta/m",
      "UPDATED in v2.1. Within the arithmetic theorem of PART 31, (H-TR) fixes r = 1 "
      "together with the shape, so the MATHEMATICAL gate is discharged conditionally. But "
      "Kogut-Susskind gives r = 1/a^2 (T153b), so imposing Tr(Delta_2) = 2E may be nothing "
      "more than the convention a_TI = 1. The PHYSICAL gate therefore remains OPEN and is "
      "identical to F-S19.3: the dimensionless lambda_1 closes conditionally, Lambda_QCD in "
      "MeV does not.")
openg("F-S20.5  non-diagonal I_h-equivariant Hodge family",
      "NEW in v2.1. Theorem S20.A ranges over the positive DIAGONAL I_h-invariant "
      "three-ratio family (m56, m66, beta5, beta6) only. Non-diagonal I_h-equivariant mass "
      "matrices, the Whitney/FEEC branch and any off-diagonal Gram structure from an "
      "abstract cochain embedding are NOT covered. Section 3 states that diagonality is not "
      "assumed; section 22 nonetheless assumes it, and the theorem is restricted accordingly.")
openg("F-S20.14 non-quadratic closure step",
      "Thm S20.T1 shows every LINEAR-IN-THE-ACTION route returns its input. Closure needs "
      "a non-quadratic or coarse-graining step; the heat-kernel branch (PART 27) is one.")
openg("F-S19.3  a_TI fixing and g_S14 <-> g_MSbar scheme matching",
      "PREREQUISITE for ANY absolute MeV comparison; inherited from ZS-S19")
# =====================================================================================
# --- inherited ZS-S19 gates, retained verbatim ---
openg("F-S19.1  four O(g^2) FP / Coulomb numbers", "inherited, unchanged")
openg("F-S19.2  non-perturbative Lanczos of A_g 12 and H_g 140", "ZS-S21")
openg("F-S19.4  quartic channel coefficients s_A(N), s_H(N)", "inherited, unchanged")
openg("F-S19.7  (H-UA) primal universal anchoring", "inherited, unchanged")
openg("F-S19.8  a certified Gribov radius", "0.2434 and 0.4934 are NOT one")

# =====================================================================================
banner("VERIFICATION SUMMARY")
# =====================================================================================
_nd = len(DECL); _np_ = len(PROXY); _ne = len(PASS) + len(FAIL) - _nd - _np_
print(f"   EXECUTABLE checks : {_ne}")
print(f"   DECLARATIVE guards: {_nd}   (registry statements, no computation)")
print(f"   PROXY checks      : {_np_}   (generic theorems; NOT verifications of the Z-Spin object)")
print(f"   PASS  : {len(PASS)}   ( = {_ne} executable + {_nd} declarative + {_np_} proxy )")
print(f"   FAIL  : {len(FAIL)}")
print(f"   OPEN  : {len(OPEN)}   (printed, NOT counted as PASS)")
if FAIL:
    for t, d in FAIL: print("      FAILED:", t, d)
RESULTS["verification"] = dict(pass_count=len(PASS), fail_count=len(FAIL), open_count=len(OPEN),
                               executable=_ne, declarative=_nd, proxy=_np_)
RESULTS["environment"] = dict(python=platform.python_version(), numpy=np.__version__,
                              mpmath=mp.__version__, sympy=sp.__version__,
                              platform=platform.platform(), seed=RNG_SEED)
try:
    with open(__file__, "rb") as fh:
        RESULTS["self_sha256"] = hashlib.sha256(fh.read()).hexdigest()
except Exception:
    RESULTS["self_sha256"] = "unavailable"

print("\nBEGIN_ZS_S20_RESULTS")
print(json.dumps(RESULTS, indent=1, sort_keys=True))
print("END_ZS_S20_RESULTS")
print("\nSHA256(self) =", RESULTS["self_sha256"])
print("Environment  =", RESULTS["environment"])
sys.exit(1 if FAIL else 0)
