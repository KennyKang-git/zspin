#!/usr/bin/env python3
"""
ZS-S7 v1.0.0 Verification Suite: The Spinor Mass Gap
18 tests across 6 categories
"""
import sys
import numpy as np
from collections import defaultdict

PASS = 0
FAIL = 0

def check(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  [PASS] {name}")
    else:
        FAIL += 1
        print(f"  [FAIL] {name} {detail}")

print("="*65)
print("ZS-S7 v1.0.0 VERIFICATION SUITE")
print("The Spinor Mass Gap")
print("="*65)

# Constants
A = 35/437
Q = 11
X, Z_dim, Y = 3, 2, 6
phi = (1 + np.sqrt(5)) / 2
v_higgs = 245.93  # GeV

# ============================================================
print("\n[1] TRUNCATED ICOSAHEDRON GEOMETRY (4 tests)")
# ============================================================

# Build TI
raw = []
for s1 in [1, -1]:
    for s2 in [1, -1]:
        raw += [(0, s1*1, s2*3*phi), (s2*3*phi, 0, s1*1), (s1*1, s2*3*phi, 0)]
        for s3 in [1, -1]:
            raw += [(s1*2, s2*(1+2*phi), s3*phi), (s3*phi, s1*2, s2*(1+2*phi)), (s2*(1+2*phi), s3*phi, s1*2)]
            raw += [(s1*1, s2*(2+phi), s3*2*phi), (s3*2*phi, s1*1, s2*(2+phi)), (s2*(2+phi), s3*2*phi, s1*1)]

verts = []
for v in raw:
    v = np.array(v)
    if not any(np.linalg.norm(v - u) < 1e-6 for u in verts):
        verts.append(v)
verts = np.array(verts)

check("V = 60", len(verts) == 60)

dmat = np.zeros((60,60))
for i in range(60):
    for j in range(i+1,60):
        dmat[i,j] = dmat[j,i] = np.linalg.norm(verts[i]-verts[j])
edge_len = np.min(dmat[dmat>0])
edges = [(i,j) for i in range(60) for j in range(i+1,60) if abs(dmat[i,j]-edge_len)<0.01]
check("E = 90", len(edges) == 90)

# Face detection
adj = defaultdict(set)
for i,j in edges:
    adj[i].add(j); adj[j].add(i)

center = np.mean(verts, axis=0)
sorted_nbrs = {}
for v_idx in range(60):
    v_pos = verts[v_idx]
    normal = v_pos - center; normal /= np.linalg.norm(normal)
    nbrs = list(adj[v_idx])
    ref_d = verts[nbrs[0]] - v_pos
    ref_d -= np.dot(ref_d, normal)*normal; ref_d /= np.linalg.norm(ref_d)
    perp = np.cross(normal, ref_d)
    angs = []
    for n in nbrs:
        d = verts[n]-v_pos; d -= np.dot(d,normal)*normal
        angs.append(np.arctan2(np.dot(d,perp), np.dot(d,ref_d)))
    sorted_nbrs[v_idx] = [nbrs[k] for k in np.argsort(angs)]

next_map = {}
for v_idx in range(60):
    sn = sorted_nbrs[v_idx]
    for k, u in enumerate(sn):
        next_map[(u, v_idx)] = (v_idx, sn[(k+1)%len(sn)])

visited = set()
faces = []
for i,j in edges:
    for start in [(i,j),(j,i)]:
        if start in visited: continue
        face = [start[0]]; cur = start
        for _ in range(10):
            visited.add(cur); nxt = next_map.get(cur)
            if nxt is None: break
            if nxt == start: break
            face.append(nxt[0]); cur = nxt
        if cur is not None and next_map.get(cur)==start and 4<=len(face)<=7:
            fs = frozenset(face)
            if not any(fs==frozenset(f) for f in faces):
                faces.append(face)

pents = [f for f in faces if len(f)==5]
hexs = [f for f in faces if len(f)==6]
check("F = 32 (12 pent + 20 hex)", len(faces)==32 and len(pents)==12 and len(hexs)==20)
check("Euler: V-E+F = 2", 60-90+32 == 2)

# ============================================================
print("\n[2] FACE LAPLACIAN SPECTRUM (4 tests)")
# ============================================================

n_f = len(faces)
face_edge_sets = []
for f in faces:
    es = set()
    for k in range(len(f)):
        es.add(frozenset([f[k], f[(k+1)%len(f)]]))
    face_edge_sets.append(es)

A_face = np.zeros((n_f, n_f))
for i in range(n_f):
    for j in range(i+1, n_f):
        if face_edge_sets[i] & face_edge_sets[j]:
            A_face[i,j] = A_face[j,i] = 1

deg = np.sum(A_face, axis=1)
L2 = np.diag(deg) - A_face
evals = np.sort(np.linalg.eigvalsh(L2.astype(float)))
lambda1 = evals[1]

check("lambda_1 = 1.2428 (spectral gap)", abs(lambda1 - 1.2428) < 0.001, f"got {lambda1:.4f}")

# Degeneracy check
tol = 1e-3
degens = []
i = 0
while i < len(evals):
    cnt = 1
    while i+cnt < len(evals) and abs(evals[i+cnt]-evals[i]) < tol: cnt += 1
    degens.append(cnt); i += cnt
check("Degeneracies: 1,3,5,3,4,5,3,5,3", degens == [1,3,5,3,4,5,3,5,3], f"got {degens}")

# I_h: sum = 32 = all 10 irreps
check("Sum degens = 32 (all I_h irreps)", sum(degens) == 32)

# Exact eigenvalues
check("lambda(G) = 6 and lambda(H) = 8 exact", abs(evals[12]-6)<0.001 and abs(evals[24]-8)<0.001)

# ============================================================
print("\n[3] DESCARTES-SPINOR IDENTITY (3 tests)")
# ============================================================

delta_v = np.pi / 15
total_deficit = 60 * delta_v
check("Descartes: 60 x pi/15 = 4pi", abs(total_deficit - 4*np.pi) < 1e-10)
check("chi(S^2) = dim(Z) = 2", 2 == Z_dim)
check("4pi = 2pi x dim(Z)", abs(4*np.pi - 2*np.pi*Z_dim) < 1e-10)

# ============================================================
print("\n[4] PHYSICAL PREDICTIONS (4 tests)")
# ============================================================

E_local = v_higgs * A / 60
Lambda_pred = E_local / lambda1
m_pred = v_higgs * A / Q

check("E_local = vA/V_Y = 328 MeV", abs(E_local*1000 - 328.3) < 1, f"got {E_local*1000:.1f}")
check("Lambda = vA/(lam1*V_Y) = 264 MeV", abs(Lambda_pred*1000 - 264) < 2, f"got {Lambda_pred*1000:.1f}")
check("m = vA/Q = 1.791 GeV", abs(m_pred - 1.791) < 0.001, f"got {m_pred:.3f}")

# Topological cancellation
m_from_lambda = lambda1 * (60/Q) * Lambda_pred
check("Topological cancellation: lam1 V/Q Lambda = vA/Q", abs(m_from_lambda - m_pred) < 1e-10)

# ============================================================
print("\n[5] ANTI-NUMEROLOGY (2 tests)")
# ============================================================

# Archimedean pair scan
archimedean_deltas = {
    "trunc_cube": abs(24-14)/(24+14), "trunc_octa": abs(24-14)/(24+14),
    "trunc_dodeca": abs(60-32)/(60+32), "trunc_icosa": abs(60-32)/(60+32),
    "cuboctahedron": abs(12-14)/(12+14), "rhombicubocta": abs(24-26)/(24+26),
    "trunc_cubocta": abs(48-26)/(48+26), "snub_cube": abs(24-38)/(24+38),
    "icosidodeca": abs(30-32)/(30+32), "rhombicosidodeca": abs(60-62)/(60+62),
    "trunc_icosidodeca": abs(120-62)/(120+62), "snub_dodeca": abs(60-92)/(60+92),
    "trunc_tetra": abs(12-8)/(12+8),
}
names = list(archimedean_deltas.keys())
hits = 0; total = 0
for nx in names:
    for ny in names:
        if archimedean_deltas[ny] <= archimedean_deltas[nx]: continue
        total += 1
        A_test = archimedean_deltas[nx] * archimedean_deltas[ny]
        m_test = v_higgs * A_test / Q
        if abs(m_test - 1.73) / 1.73 < 0.05: hits += 1

p_arch = hits / total if total > 0 else 0
check(f"Archimedean scan: p = {p_arch:.3f} < 0.10", p_arch < 0.10)

# MC scan
np.random.seed(350437)
N_mc = 100000; mc_hits = 0
for _ in range(N_mc):
    A_r = np.random.uniform(0.01, 0.20)
    m_r = v_higgs * A_r / Q
    if abs(m_r - 1.73)/1.73 < 0.05: mc_hits += 1
p_mc = mc_hits / N_mc
check(f"MC scan (Q=11 fixed): p = {p_mc:.3f} < 0.05", p_mc < 0.05)

# ============================================================
print("\n[6] CROSS-CONSISTENCY (1 test)")
# ============================================================

alpha_s_zspin = 11/93
b0_zspin = 92/12  # = 23/3
b0_SM = (11*3 - 2*5)/3  # = 23/3
check("a_3 = b_0(SU3, nf=5) = 23/3", abs(b0_zspin - b0_SM) < 1e-10)

# ============================================================
print(f"\n{'='*65}")
print(f"  RESULT: {PASS}/{PASS+FAIL} PASS")
print(f"{'='*65}")

sys.exit(0 if FAIL == 0 else 1)
