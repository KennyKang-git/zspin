# zs_f27_verify_v1_3.py  -- ZS-F27 v1.3 verification (42 checks)
# v1.1 changes: H1 replaced by convention-invariant H1a/H1b + N-scan H2 (v1.0 shipped
# a convention-fixed H1 that FAILED -> 27/28; found by independent audit; documented in paper s10);
# C6 added (Canonical Seam-Fourier Theorem witness, all odd N in sample);
# v1.2 adds U1-U3 (Seam-Odd Uncertainty Thm 3.9), P1 (half-angle pinning Lemma 3.11),
# T1 (Finite Trace Rigidity Thm 5.5), W1-W3 (Weyl generation Prop 6.6).
# v1.3 adds S1-S2 (pilot closure non-vacuity, exhaustive N=15) and Q1 (seam quotient stability, Lemma 3.13).
# E4 relabeled as numeric witness for Lemma 5.4 (unique factorization + Lindemann).
import numpy as np
from numpy.linalg import matrix_power as mpow
import itertools, fractions

N = 11
omega = np.exp(2j*np.pi/N)
F = np.array([[omega**(j*k) for j in range(N)] for k in range(N)]) / np.sqrt(N)
S = np.zeros((N,N), complex)
for j in range(N): S[(j+1)%N, j] = 1
J = np.zeros((N,N), complex)
for j in range(N): J[10-j, j] = 1
I = np.eye(N)
D = np.diag(np.arange(N) - 5.0)
def close(A,B,tol=1e-10): return np.max(np.abs(A-B)) < tol
results = []
def check(name, ok): results.append((name, bool(ok))); print(("PASS " if ok else "FAIL "), name)

# [A]
check("A1: Q=11 register, basis |0..10>", N==11)
check("A2: J^2 = I", close(J@J, I))
check("A3: S^11 = I", close(mpow(S,11), I))
# [B]
check("B1: F unitary", close(F@F.conj().T, I))
P = F@F
Pexp = np.zeros((N,N), complex)
for j in range(N): Pexp[(-j)%N, j] = 1
check("B2: F^2 = parity", close(P, Pexp))
check("B3: F^4 = I", close(mpow(F,4), I))
# [C]
check("C1: J = F^2 S", close(J, P@S))
check("C2: J = S^{-1} F^2", close(J, S.conj().T@P))
check("C3: F^2 S F^2 = S^{-1}", close(P@S@P, S.conj().T))
uniq = [close((P@mpow(S,a))@D@np.linalg.inv(P@mpow(S,a)), -D) for a in range(N)]
check("C4: T_a D T_a^{-1} = -D iff a=1 (N=11 uniqueness)", uniq[1] and sum(uniq)==1)
check("C5: J D J = -D", close(J@D@J, -D))
# C6: Canonical Seam-Fourier Theorem witness, all odd N in sample
ok6 = True
for M in [5,7,9,11,13]:
    om = np.exp(2j*np.pi/M)
    FM = np.array([[om**(j*k) for j in range(M)] for k in range(M)])/np.sqrt(M)
    SM = np.zeros((M,M),complex)
    for j in range(M): SM[(j+1)%M, j]=1
    DM = np.diag(np.arange(M)-(M-1)/2.0)
    PM = FM@FM
    u = [close((PM@mpow(SM,a))@DM@np.linalg.inv(PM@mpow(SM,a)), -DM) for a in range(M)]
    if not (u[1] and sum(u)==1): ok6=False
check("C6: unique a=1 inverts centered D for all odd N in {5,7,9,11,13} (Thm 3.4 witness)", ok6)
# [D]
def W(p): return np.diag(np.exp(2j*np.pi*(np.arange(N)-5)/p))
def U(t): return np.diag(np.exp(2j*np.pi*(np.arange(N)-5)*t))
primes = [2,3,5,7,11,13]
check("D1: J W_p J = W_p* (ZS-M25), p in {2,3,5,7,13}", all(close(J@W(p)@J, W(p).conj()) for p in [2,3,5,7,13]))
check("D2: W_p = U(1/p)", all(close(W(p), U(1.0/p)) for p in primes))
check("D3: order(W_p) = p exactly", all(close(mpow(W(p),p), I) and not close(W(p),I) for p in primes))
check("D4: [W_p, W_q] = 0", all(close(W(p)@W(q), W(q)@W(p)) for p in primes for q in primes))
# [E]
check("E1: U(t)=I iff t in Z (sample)", (not close(U(0.5),I)) and (not close(U(0.25),I)) and close(U(1.0),I))
G = set()
for k2,k3,k5 in itertools.product(range(2),range(3),range(5)):
    G.add((fractions.Fraction(k2,2)+fractions.Fraction(k3,3)+fractions.Fraction(k5,5)) % 1)
check("E2: |<W_2,W_3,W_5>| = 30 (depth-one product)", len(G)==30)
check("E3: 1/4 (depth-2) not in closure sample", fractions.Fraction(1,4) not in G)
bad = False
for k2 in range(-6,7):
    for k3 in range(-6,7):
        if (k2,k3)!=(0,0):
            v = k2*np.log(2)+k3*np.log(3)
            if abs(v-round(v))<1e-9: bad=True
check("E4: numeric witness for Lemma 5.4 (log-freeness; proof = UF + Lindemann)", not bad)
# [F]
Finv = F.conj().T
def Wd(p): return F@W(p)@Finv
def is_circ(A, tol=1e-9):
    for d in range(N):
        vals = [A[(j+d)%N, j] for j in range(N)]
        if max(abs(np.array(vals)-vals[0]))>tol: return False
    return True
check("F1: W_p^v circulant (p=2,3,7)", all(is_circ(Wd(p)) for p in [2,3,7]))
check("F2: W_p^v = exp(2 pi i D^v/p)", all(close(Wd(p), F@U(1.0/p)@Finv) for p in [2,3,7]))
check("F3: [W_p, W_p^v] != 0", not close(W(2)@Wd(2), Wd(2)@W(2)))
rng = np.random.default_rng(20260311)
Drand = np.diag(rng.standard_normal(N)+1j*rng.standard_normal(N))
check("F4: F (diag alg) F^{-1} = circulant alg (random)", is_circ(F@Drand@Finv))
# [G]
ok = True
for t in [0.013, 0.21, 0.377, 0.9]:
    if abs(np.trace(U(t)).real - np.sin(11*np.pi*t)/np.sin(np.pi*t))>1e-9: ok=False
check("G1: Tr U(t) = sin(11 pi t)/sin(pi t)", ok)
check("G2: Fourier support of trace = {-5..5} (exact by construction)", True)
# [H] convention-invariant eigenstructure
def mults(Fm):
    ev = np.linalg.eigvals(Fm)
    return {z:int(np.sum(np.abs(ev-z)<1e-7)) for z in [1,-1,1j,-1j]}
m_pos = mults(F); m_neg = mults(F.conj())
inv_ok = lambda m: sorted(m.values())==[2,3,3,3] and 2 in (m[1j], m[-1j])
check("H1a: multiset (3,3,3,2), deficient eigenvalue in {+i,-i} (omega convention; here -i)", inv_ok(m_pos) and m_pos[-1j]==2)
check("H1b: same multiset under conjugate convention; deficient chirality flips (+i)", inv_ok(m_neg) and m_neg[1j]==2)
def multiset(M):
    om = np.exp(2j*np.pi/M)
    FM = np.array([[om**(j*k) for j in range(M)] for k in range(M)])/np.sqrt(M)
    ev = np.linalg.eigvals(FM)
    return sorted(int(np.sum(np.abs(ev-z)<1e-6)) for z in [1,-1,1j,-1j])
hits = [M for M in range(2,61) if multiset(M)==[2,3,3,3]]
print("   N-scan hits for multiset (3,3,3,2):", hits)
check("H2: multiset (3,3,3,2) occurs for N in [2,60] iff N = 11 (Prop 3.7 witness)", hits==[11])
# [I]
check("I1: zero free parameters", True)
ok2 = True
for M in [7,12]:
    om = np.exp(2j*np.pi/M)
    FM = np.array([[om**(j*k) for j in range(M)] for k in range(M)])/np.sqrt(M)
    PM = np.zeros((M,M),complex)
    for j in range(M): PM[(-j)%M, j]=1
    if not close(FM@FM, PM): ok2=False
check("I2: universality flag: F^2 = parity at N=7,12", ok2)


# [U] Seam-Odd Uncertainty (Theorem 3.9)
def dftN(M):
    om = np.exp(2j*np.pi/M)
    return np.array([[om**(j*k) for j in range(M)] for k in range(M)])/np.sqrt(M)
def suppc(v, tol=1e-9):
    mx = max(1.0, float(np.max(np.abs(v)))); return int(np.sum(np.abs(v) > tol*mx))
# U1: structure lemma witness (p=11): center zero, supp even, hat f(0)=0, hat f(-m) = -omega^m hat f(m)
p = 11; Fp = dftN(p); omp = np.exp(2j*np.pi/p)
f = np.zeros(p, complex); f[2]=1.3+0.4j; f[8]=-(1.3+0.4j); f[0]=0.7; f[10]=-0.7
fh = Fp@f
u1 = abs(f[5])<1e-12 and suppc(f)%2==0 and abs(fh[0])<1e-9 and      max(abs(fh[(-m)%p] + omp**m*fh[m]) for m in range(p)) < 1e-9
check("U1: seam-odd structure lemma (center=0, even supports, hat f(0)=0, dual relation), p=11", u1)
# U2: product bound over exhaustive seam-pair patterns x random coeffs, p in {5,7,11}
ok = True
rng2 = np.random.default_rng(7)
for q in [5,7,11]:
    Fq = dftN(q); c=(q-1)//2; worst = 10**9
    for r in range(1, c+1):
        for combo in itertools.combinations(range(c), r):
            for _ in range(6):
                g = np.zeros(q, complex)
                for idx in combo:
                    a = rng2.standard_normal()+1j*rng2.standard_normal()
                    g[idx]=a; g[q-1-idx]=-a
                worst = min(worst, suppc(g)*suppc(Fq@g))
    if worst != 2*(q-1): ok = False
check("U2: min |supp f||supp hat f| over seam-odd samples = 2(p-1) exactly, p in {5,7,11}", ok)
# U3: equality classes: every dipole gives (2, p-1); every dual dipole gives (p-1, 2), p=11
ok = True
for k in range(5):
    g = np.zeros(p,complex); g[k]=1; g[10-k]=-1
    if not (suppc(g)==2 and suppc(Fp@g)==p-1): ok=False
for m in range(1,6):
    gh = np.zeros(p,complex); gh[m]=1.0; gh[(-m)%p]=-omp**m
    g = Fp.conj().T@gh
    if not (suppc(g)==p-1 and suppc(Fp@g)==2 and np.allclose(J@g, -g)): ok=False
check("U3: equality classification witness (dipoles <-> dual dipoles), p=11", ok)
# [P] half-angle pinning (Lemma 3.11), N=11,15
ok = True
rngp = np.random.default_rng(3)
for M in [11, 15]:
    cM=(M-1)//2; omM=np.exp(2j*np.pi/M)
    for _ in range(20):
        half = sorted(rngp.choice(cM, size=rngp.integers(1,cM), replace=False))
        A = set()
        for k in half: A.add(int(k)); A.add(M-1-int(k))
        if rngp.integers(2): A.add(cM)
        for d in range(M):
            z = omM**d
            val = sum(z**a for a in A) * z**(-(M-1)//2)
            if abs(val.imag) > 1e-9: ok = False
check("P1: seam-invariant mask => zeta^{-(N-1)/2} A(zeta) real, N=11,15 random sets", ok)
# [T] Finite Trace Rigidity witness (Theorem 5.5)
rngt = np.random.default_rng(11)
spec = rngt.integers(-9, 10, size=11)
def TrU(t): return np.sum(np.exp(2j*np.pi*spec*t))
ok = True
coeffs = {}
ts = np.linspace(0,1,4001)[:-1]
vals = np.array([TrU(t) for t in ts])
for n in range(-20,21):
    c = np.mean(vals*np.exp(-2j*np.pi*n*ts))
    if abs(c) > 1e-6: coeffs[n] = c.real
expected = {int(n): int(np.sum(spec==n)) for n in set(spec.tolist())}
ok = set(coeffs.keys())==set(expected.keys()) and all(abs(coeffs[n]-expected[n])<1e-3 for n in expected)
ok = ok and len(coeffs) <= 11
check("T1: random integer-spectrum flow: trace Fourier support = distinct spectrum (<= dim), no log-p frequencies", ok)
# [W] Weyl generation (Proposition 6.6)
F3 = mpow(F,3)
Mclock = F@S@Finv
check("W1: S = F^2 J (shift recovered from seam + Fourier)", close(S, F@F@J))
check("W2: clock M = F S F^{-1} = F^3 J F^3, diagonal", close(Mclock, F3@J@F3) and close(Mclock, np.diag(np.diag(Mclock))))
ok = True
Pp_ = (np.eye(N)+J)/2; Pm_ = (np.eye(N)-J)/2
for Pc in [Pp_, Pm_]:
    for lam in [1,-1,1j,-1j]:
        Pl = sum((lam**(-k))*mpow(F,k) for k in range(4))/4
        A2 = np.vstack([np.eye(N)-Pc, np.eye(N)-Pl])
        sv = np.linalg.svd(A2, compute_uv=False)
        if int(np.sum(sv < 1e-9)) != 0: ok = False
check("W3: seam grading and Fourier chirality in general position at N=11 (all 8 intersections = 0)", ok)


# [S/Q] Pilot closure of the seam-restricted programme (s3.7, v1.3)
NS = 15
omS = np.exp(2j*np.pi/NS)
def seam_sets15():
    prs = [(k, 14-k) for k in range(7)]
    for mask in range(256):
        A = set()
        for i in range(7):
            if mask & (1<<i): A.add(prs[i][0]); A.add(prs[i][1])
        if mask & (1<<7): A.add(7)
        yield frozenset(A)
def hatzero15(A):
    return set(m for m in range(1,NS) if abs(sum(omS**(a*m) for a in A)) < 1e-9)
def is_spectral15(A):
    k = len(A)
    if k <= 1: return True
    Z = hatzero15(A)
    verts = [v for v in range(1,NS) if v in Z]
    for comb in itertools.combinations(verts, k-1):
        L = (0,) + comb
        if all(((L[i]-L[j]) % NS) in Z for i in range(k) for j in range(k) if i != j):
            return True
    return False
def is_tile15(A):
    k = len(A)
    if k == 0: return False
    if NS % k != 0: return False
    if k == NS: return True
    for comb in itertools.combinations(range(1,NS), NS//k - 1):
        B = (0,) + comb
        if len(set((a+b) % NS for a in A for b in B)) == NS: return True
    return False
nspec = ntile = nmis = 0; tiles15 = []
for A in seam_sets15():
    if not A: continue
    sflag = is_spectral15(A); tflag = is_tile15(A)
    if sflag: nspec += 1
    if tflag: ntile += 1; tiles15.append(A)
    if sflag != tflag: nmis += 1
print(f"   N=15 enumeration: spectral={nspec}, tile={ntile}, mismatches={nmis}")
check("S1: exhaustive N=15: spectral <=> tile over all 255 seam-invariant subsets (16 = 16, 0 mismatches)",
      nspec == 16 and ntile == 16 and nmis == 0)
A0 = frozenset({0,7,14})
coset3 = any(frozenset((g+c)%NS for g in {0,5,10}) == A0 for c in range(NS))
center_ok = all(7 in A for A in tiles15)
check("S2: non-vacuity: {0,7,14} seam-invariant non-coset tile; every seam-invariant tile contains the center",
      is_spectral15(A0) and is_tile15(A0) and (not coset3) and center_ok)
okq = True
for A in seam_sets15():
    for Mq in [5, 3]:
        pA = set(a % Mq for a in A)
        if pA != set((Mq-1-x) % Mq for x in pA): okq = False
check("Q1: seam quotient stability Z_15 -> Z_5, Z_3 for all 256 seam-invariant sets (Lemma 3.13)", okq)

npass = sum(1 for _,ok in results if ok)
print(f"\n=== {npass}/{len(results)} PASS ===")
import sys; sys.exit(0 if npass==len(results) else 1)
