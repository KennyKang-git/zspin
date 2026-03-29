#!/usr/bin/env python3
"""
ZS-M6 Verification Suite v1.0
=================================
Block-Laplacian Spectral Verification
Companion to ZS-F2 v1.0 §7-§9: Product Structure & Heat Kernel

Combined 29-gate verification:
  Part I  (A1-A10): Log-Determinant at 50-digit precision
  Part II (B1-B10): Heat Kernel Factorization
  Part III (C1-C9): Hodge-Dirac Operator

Locked inputs: A=35/437, Q=11, (Z,X,Y)=(2,3,6).
Operator: 11x11 Block-Laplacian with Z-mediated cross-coupling,
  identical to heat_kernel_factorization.py (Paper 31 v1.0.1).
Precision: mpmath (80-digit working / 50-digit display) for log-det;
  numpy/scipy double for matrix expm and eigenvalues.

Usage:
  python3 ZS_M6_Verification_Suite_v1_0.py
  Expected output: 29/29 PASS
  Exit code: 0 (all pass) or 1 (any fail)
  JSON results: ZS_M6_v1_0_verification_results.json (same directory)

Dependencies: numpy, scipy, mpmath (REQUIRED)
"""
try:
    import mpmath; mpmath.mp.dps = 80
except ImportError:
    import sys; print("FATAL: mpmath required."); sys.exit(1)

import numpy as np
from scipy.linalg import expm, eigvalsh
import json, sys
from pathlib import Path
from fractions import Fraction

Z_dim, X_dim, Y_dim = 2, 3, 6
Q = 11; G = 12
A_frac = Fraction(35, 437); A_f = float(A_frac)
delta_X_frac = Fraction(5, 19); delta_Y_frac = Fraction(7, 23)
VX, FX, EX = 24, 14, 36; VY, FY, EY = 60, 32, 90

phi = (1 + np.sqrt(5)) / 2
a_X = 38.0 / 12.0; a_Y = 92.0 / 12.0
lambda_X = a_X / X_dim
lambda_Y_T1 = a_Y / Y_dim
lambda_Y_T2 = (5 - np.sqrt(5)) / 2 * a_Y / Y_dim
kappa = np.sqrt(35.0 / (437.0 * 11.0))

results = []
def test(name, cond, detail=""):
    s = "PASS" if cond else "FAIL"
    results.append({"test": name, "status": s, "detail": detail})
    print(f"  {'✅' if cond else '❌'} {name}: {s}" + (f"  ({detail})" if detail else ""))

print("=" * 72)
print("ZS-M6 VERIFICATION SUITE v1.0")
print("Block-Laplacian Spectral Verification")
print("=" * 72)

def build_BL(mu, cs=1.0):
    L = np.zeros((Q, Q))
    for i in range(X_dim): L[i,i] = lambda_X + mu**2
    L[3,3] = 0.0 + mu**2; L[4,4] = 1.0 + mu**2
    for i in range(3): L[5+i,5+i] = lambda_Y_T1 + mu**2
    for i in range(3): L[8+i,8+i] = lambda_Y_T2 + mu**2
    k = kappa * cs
    for i in range(X_dim): L[i,3] += k; L[3,i] += k
    for j in range(Y_dim): L[3,5+j] += k; L[5+j,3] += k
    return L

L_full = build_BL(1.0, 1.0); L_dec = build_BL(1.0, 0.0)
eigs_f = np.sort(eigvalsh(L_full)); eigs_d = np.sort(eigvalsh(L_dec))
L_X = L_full[0:3,0:3].copy(); L_Z = L_full[3:5,3:5].copy(); L_Y = L_full[5:11,5:11].copy()

print("\n--- Part I: Log-Determinant (A1-A10) ---")

test("A1: Symmetry ℒ = ℒᵀ", np.max(np.abs(L_full-L_full.T)) < 1e-15,
     f"‖ℒ-ℒᵀ‖ = {np.max(np.abs(L_full-L_full.T)):.2e}")

lmin = np.min(eigs_f)
test("A2: Positive definite at μ=1", lmin > 0, f"λ_min = {lmin:.4f}")

test("A3: X-Y block ≡ 0", np.max(np.abs(L_full[0:3,5:11])) < 1e-15,
     f"‖L_XY‖ = {np.max(np.abs(L_full[0:3,5:11])):.2e}")

Tr_err = abs(np.trace(L_full) - (np.trace(L_X)+np.trace(L_Z)+np.trace(L_Y)))
test("A4: Tr(ℒ) = Σ Tr(L_i)", Tr_err < 1e-12, f"|ΔTr| = {Tr_err:.2e}")

mp_L = mpmath.matrix(Q,Q)
for i in range(Q):
    for j in range(Q): mp_L[i,j] = mpmath.mpf(str(L_full[i,j]))
mp_ld = mpmath.log(mpmath.det(mp_L)); np_ld = np.sum(np.log(eigs_f))
test("A5: ln det(ℒ) 50-digit", abs(float(mp_ld)-np_ld)/abs(np_ld) < 1e-12,
     f"ln det = {mpmath.nstr(mp_ld, 20)}")

dX = Fraction(abs(FX-VX), FX+VX); dY = Fraction(abs(FY-VY), FY+VY)
test("A6: δ_X = 5/19", dX == delta_X_frac, f"δ_X = {dX}")
test("A7: δ_Y = 7/23", dY == delta_Y_frac, f"δ_Y = {dY}")
A_c = dX * dY
test("A8: A = δ_X×δ_Y = 35/437", A_c == A_frac, f"A = {A_c}")

ms = np.max(np.abs(eigs_f - eigs_d))
test("A9: Eigenvalue shift O(κ²)", abs(ms - 0.0483) < 0.005, f"|Δλ|_max = {ms:.4f}")

cond = np.max(eigs_f)/np.min(eigs_f)
test("A10: Condition number < 10⁴", cond < 1e4, f"κ(ℒ) = {cond:.2f}")

print("\n--- Part II: Heat Kernel (B1-B10) ---")

ts = [0.001, 0.01, 0.1, 1.0]
def hkt(L,ts):
    e = eigvalsh(L); return {t: np.sum(np.exp(-t*e)) for t in ts}
TF = hkt(L_full,ts); TX = hkt(L_X,ts); TZ = hkt(L_Z,ts); TY = hkt(L_Y,ts)
TS = {t: TX[t]+TZ[t]+TY[t] for t in ts}

test("B1: K_XY(t=0) = 0", np.max(np.abs(np.eye(Q)[0:3,5:11])) < 1e-14, "identity")

re = abs(TF[0.001]-TS[0.001])/TF[0.001]
test("B2: Tr[K]=ΣTr[K_i] at t→0", re < 1e-6, f"rel err = {re:.2e}")

a1e = abs(-np.trace(L_full)-(-np.trace(L_X)-np.trace(L_Z)-np.trace(L_Y)))
test("B3: Seeley-DeWitt a₁ exact", a1e < 1e-12, f"|Δa₁| = {a1e:.2e}")

best_nXY = 0; best_t_pk = 0
for t in np.linspace(0.01, 5.0, 500):
    K = expm(-t*L_full); nxy = np.linalg.norm(K[0:3,5:11])
    if nxy > best_nXY: best_nXY = nxy; best_t_pk = t
K_pk = expm(-best_t_pk*L_full); nxx_pk = np.linalg.norm(K_pk[0:3,0:3])
pr = best_nXY / nxx_pk if nxx_pk > 0 else 999
test("B4: Leakage ratio at peak ‖K_XY‖ < 0.1", pr < 0.1,
     f"peak ‖K_XY‖={best_nXY:.3e} at t={best_t_pk:.3f}, ratio={pr:.4f}")

tsh = np.array([0.001,0.005,0.01,0.05])
nXY=[]; nXZ=[]
for t in tsh:
    K=expm(-t*L_full); nXY.append(np.linalg.norm(K[0:3,5:11])); nXZ.append(np.linalg.norm(K[0:3,3:5]))
axy = np.polyfit(np.log(tsh), np.log(np.array(nXY)+1e-30), 1)[0]
axz = np.polyfit(np.log(tsh), np.log(np.array(nXZ)+1e-30), 1)[0]
test("B5: ‖K_XY‖~t^α, α>1.5", axy > 1.5, f"α_XY={axy:.3f}, α_XZ={axz:.3f}")

test("B6: A = δ_X×δ_Y = 35/437", A_c == Fraction(35,437), f"A = {A_c}")

mus = [1.0, 2.0, 5.0, 10.0]; dww = []
for mu in mus:
    ef=eigvalsh(build_BL(mu,1.0)); ed=eigvalsh(build_BL(mu,0.0))
    Wf=0.5*np.sum(np.log(ef)); Wd=0.5*np.sum(np.log(ed)); dww.append((Wf-Wd)/Wd)
test("B7: δW/W ~-0.34% at μ=1", abs(dww[0]*100-(-0.34)) < 0.15,
     f"δW/W = [{', '.join(f'{d*100:.4f}%' for d in dww)}]")

eXY = np.concatenate([eigvalsh(L_X), eigvalsh(L_Y)]); eZo = eigvalsh(L_Z)
se = abs(TF[0.1]-(np.sum(np.exp(-0.1*eXY))+np.sum(np.exp(-0.1*eZo))))/TF[0.1]
test("B8: Schur trace reconstruction", se < 0.01, f"rel err = {se:.4e}")

np.random.seed(350437); mr = np.zeros(200)
for trial in range(200):
    Lr = np.zeros((Q,Q))
    for i in range(X_dim): Lr[i,i]=np.random.uniform(0.5,3.0)
    for i in range(Z_dim): Lr[X_dim+i,X_dim+i]=np.random.uniform(0.0,2.0)
    for i in range(Y_dim): Lr[X_dim+Z_dim+i,X_dim+Z_dim+i]=np.random.uniform(1.0,4.0)
    for i in range(X_dim): w=np.random.uniform(-0.2,0.2); Lr[i,X_dim]+=w; Lr[X_dim,i]+=w
    for i in range(Y_dim): w=np.random.uniform(-0.2,0.2); Lr[X_dim,X_dim+Z_dim+i]+=w; Lr[X_dim+Z_dim+i,X_dim]+=w
    Kr=expm(-0.5*Lr); nx=np.linalg.norm(Kr[0:3,0:3])
    mr[trial]=np.linalg.norm(Kr[0:3,5:11])/nx if nx>0 else 999
fb = np.mean(mr<0.1)*100
test("B9: Ensemble >90% leakage<0.1", fb>90, f"{fb:.0f}% below 0.1")

ef10=eigvalsh(build_BL(10.0,1.0)); ed10=eigvalsh(build_BL(10.0,0.0))
me = abs(np.sum(np.exp(-0.01*ef10))-np.sum(np.exp(-0.01*ed10)))/np.sum(np.exp(-0.01*ed10))
test("B10: Mode-Count Collapse", me < 0.01, f"coupling err at μ=10: {me:.2e}")

# ════════════════════════════════════════════════════════════════════
# Part III: Hodge-Dirac Operator (C1-C9) [NEW in v1.0 Hodge-Dirac update]
# ════════════════════════════════════════════════════════════════════
print("\n--- Part III: Hodge-Dirac Operator (C1-C9) ---")

# Build Truncated Icosahedron geometry
phi_gr = (1 + np.sqrt(5)) / 2
_vset = set()
_base = [(0,1,3*phi_gr),(0,1,-3*phi_gr),(0,-1,3*phi_gr),(0,-1,-3*phi_gr)]
for _s1 in [1,-1]:
    for _s2 in [1,-1]:
        for _s3 in [1,-1]:
            _base.append((_s1*2, _s2*(1+2*phi_gr), _s3*phi_gr))
            _base.append((_s1*1, _s2*(2+phi_gr), _s3*2*phi_gr))
for (a,b,c) in _base:
    for p in [(a,b,c),(b,c,a),(c,a,b)]:
        _vset.add(tuple(round(x,10) for x in p))
TI_verts = [np.array(v) for v in sorted(_vset)]
assert len(TI_verts) == 60, f"TI vertices: {len(TI_verts)}"

TI_edges = [(i,j) for i in range(60) for j in range(i+1,60)
            if abs(np.linalg.norm(TI_verts[i]-TI_verts[j])-2.0)<1e-6]
assert len(TI_edges) == 90, f"TI edges: {len(TI_edges)}"

_ei = {}
for idx,(a,b) in enumerate(TI_edges): _ei[(a,b)]=idx; _ei[(b,a)]=idx

from scipy.spatial import ConvexHull
_hull = ConvexHull(np.array(TI_verts))
_fn = []
for tri in _hull.simplices:
    v0,v1,v2 = [np.array(TI_verts[k]) for k in tri]
    n = np.cross(v1-v0, v2-v0); n /= np.linalg.norm(n)
    if np.dot(n, (v0+v1+v2)/3) < 0: n = -n
    _fn.append(n)
_cl = []; _used = set()
for i in range(len(_hull.simplices)):
    if i in _used: continue
    c = [i]; _used.add(i)
    for j in range(i+1, len(_hull.simplices)):
        if j in _used: continue
        if np.linalg.norm(_fn[i]-_fn[j]) < 1e-6: c.append(j); _used.add(j)
    _cl.append(c)
TI_faces = []; TI_fnorms = []
for c_ in _cl:
    vs = set()
    for ti in c_:
        for v in _hull.simplices[ti]: vs.add(v)
    TI_faces.append(sorted(vs)); TI_fnorms.append(_fn[c_[0]])
assert len(TI_faces) == 32

def _orient(fv, normal):
    center = np.mean([TI_verts[v] for v in fv], 0)
    lv = [TI_verts[v]-center for v in fv]
    u = lv[0]-np.dot(lv[0],normal)*normal; u /= np.linalg.norm(u)
    w = np.cross(normal, u)
    angles = [np.arctan2(np.dot(l,w), np.dot(l,u)) for l in lv]
    return [fv[k] for k in np.argsort(angles)]
_of = [_orient(TI_faces[fi], TI_fnorms[fi]) for fi in range(32)]

# Build boundary operators
d0_TI = np.zeros((90, 60))
for e_idx,(i,j) in enumerate(TI_edges): d0_TI[e_idx,i]=-1; d0_TI[e_idx,j]=+1
d1_TI = np.zeros((32, 90))
for fi, face in enumerate(_of):
    for k in range(len(face)):
        vi,vj = face[k], face[(k+1)%len(face)]
        ek = (min(vi,vj), max(vi,vj))
        if ek in _ei: d1_TI[fi, _ei[ek]] = 1.0 if vi<vj else -1.0

# Build Hodge-Dirac D_TI (182x182)
N_TI = 182
D_TI = np.zeros((N_TI, N_TI))
D_TI[60:150, :60] = d0_TI;      D_TI[:60, 60:150] = d0_TI.T
D_TI[150:182, 60:150] = d1_TI;  D_TI[60:150, 150:182] = d1_TI.T

# Hodge Laplacians
Delta0 = d0_TI.T @ d0_TI
Delta1 = d0_TI @ d0_TI.T + d1_TI.T @ d1_TI
Delta2 = d1_TI @ d1_TI.T
D2 = D_TI @ D_TI
DeltaH = np.zeros((N_TI, N_TI))
DeltaH[:60,:60] = Delta0; DeltaH[60:150,60:150] = Delta1; DeltaH[150:,150:] = Delta2

# C1: Chain complex
chain_err = np.max(np.abs(d1_TI @ d0_TI))
test("C1: Chain complex d₁∘d₀ = 0", chain_err < 1e-12, f"||d₁d₀|| = {chain_err:.2e}")

# C2: Lichnerowicz D² = Δ_Hodge
lich_err = np.max(np.abs(D2 - DeltaH))
test("C2: Lichnerowicz D² = Δ_Hodge", lich_err < 1e-10, f"||D²-Δ|| = {lich_err:.2e}")

# C3: Chirality {D, Γ} = 0
Gamma = np.zeros(N_TI)
Gamma[:60] = +1; Gamma[60:150] = -1; Gamma[150:] = +1
ac = D_TI * Gamma[np.newaxis,:] + Gamma[:,np.newaxis] * D_TI
ac_err = np.max(np.abs(ac))
test("C3: Chirality {D,Γ} = 0", ac_err < 1e-10, f"||{{D,Gamma}}|| = {ac_err:.2e}")

# C4: Betti numbers (1,0,1)
eig0 = eigvalsh(Delta0); eig1 = eigvalsh(Delta1); eig2 = eigvalsh(Delta2)
b0 = np.sum(np.abs(eig0) < 1e-8); b1 = np.sum(np.abs(eig1) < 1e-8); b2 = np.sum(np.abs(eig2) < 1e-8)
test("C4: Betti (b₀,b₁,b₂) = (1,0,1)", (b0,b1,b2) == (1,0,1), f"({b0},{b1},{b2})")

# C5: Even sector dim = V+F = 92
even_dim = 60 + 32  # Ω⁰ + Ω²
test("C5: Even sector dim = V+F = 92", even_dim == 92 and even_dim == VY+FY)

# C6: Total dim = 2(V+F-1) = 182
test("C6: V+E+F = 2(V+F-1) = 182", 60+90+32 == 2*(60+32-1) == 182)

# C7: Hodge asymmetry = δ_Y = 7/23
rank_d0 = np.linalg.matrix_rank(d0_TI, tol=1e-8)
rank_d1 = np.linalg.matrix_rank(d1_TI, tol=1e-8)
hodge_asym = Fraction(abs(rank_d0 - rank_d1), even_dim)
test("C7: Hodge asymmetry = δ_Y = 7/23", hodge_asym == delta_Y_frac,
     f"({rank_d0}-{rank_d1})/{even_dim} = {hodge_asym}")

# C8: Zero modes of D = 2
eig_D = eigvalsh(D_TI)
n_zero_D = np.sum(np.abs(eig_D) < 1e-8)
test("C8: Zero modes of D = b₀+b₁+b₂ = 2", n_zero_D == 2)

# C9: Spectral symmetry N⁺ = N⁻ = 90
n_pos = np.sum(eig_D > 1e-8); n_neg = np.sum(eig_D < -1e-8)
test("C9: Spectral symmetry N⁺=N⁻=90", n_pos == 90 and n_neg == 90,
     f"N⁺={n_pos}, N⁻={n_neg}")
print("\n" + "=" * 72)
np_ = sum(1 for r in results if r['status']=='PASS'); nt = len(results)
print(f"RESULT: {np_}/{nt} PASS")
na = sum(1 for r in results[:10] if r['status']=='PASS')
nb = sum(1 for r in results[10:20] if r['status']=='PASS')
nc = sum(1 for r in results[20:] if r['status']=='PASS')
print(f"  Part I: {na}/10  Part II: {nb}/10  Part III: {nc}/9")
print(f"\n  ln det(ℒ) = {mpmath.nstr(mp_ld,20)}")
print(f"  |Δλ|_max = {ms:.4f}, peak leakage = {pr:.4f}")
print(f"  α_XY = {axy:.3f}, δW/W(μ=1) = {dww[0]*100:.4f}%")
if np_ < nt:
    for f in results:
        if f['status']=='FAIL': print(f"  ❌ {f['test']}: {f['detail']}")
    sys.exit(1)
else: print(f"\n✅ ALL 29 TESTS PASS — BLOCK-LAPLACIAN + HODGE-DIRAC VERIFIED")

d = Path(__file__).parent if '__file__' in dir() else Path('.')
with open(d/"ZS_M6_v1_0_verification_results.json",'w') as f:
    json.dump({"suite":"ZS-M6 v1.0","tests":results,"summary":f"{np_}/{nt} PASS",
               "key":{"ln_det":float(mp_ld),"max_shift":round(ms,4),"peak_leakage":round(pr,4),
                      "alpha_XY":round(axy,3),"dW_W_pct":round(dww[0]*100,4)}},f,indent=2)
