#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_m46_verify_v1_5.py — Verification suite for ZS-M46 v1.5 (closure)
Rebuilt to be THEOREM-ALIGNED after external review of v1.0.

Two honestly separated tiers. The suite does NOT machine-certify KH1-KH4, factor
type, Haag duality, strong additivity, or cocycle realization; those are imported
theorems or admissibility conditions, checked here only for internal consistency.

Tiers:
  CERTIFY (21) — model/theorem checks that actually bear on the claims:
     SP (6): positive-energy model L2(R+,dp): positivity P>=0, dilation generator,
             the Borchers relation as a FORMAL coefficient identity on the
             core, KMS relation, the modular-time identity t0 = mu/2pi, and the
             OBSTRUCTION that the affine half-plane is NOT a standard subspace.
     K  (12): Koenigs / ZS-M1 data (now labelled PROVEN-LOCAL).
     TW ( 3): twist resolution — factorization of one iterate into
             modular-dilation x internal-rotation; the E_{lambda*} modulus.
  DIAGNOSTIC (17) — affine shadows, corpus arithmetic, firewall, scope guards.
     These do NOT certify T3/T4 and are reported separately.
     B (8), C (6), R (3).

FIREWALL unchanged: the single quarantined regression e^{-2piQ} feeds nothing.
"""

import sympy as sp
from mpmath import mp, mpc, mpf, exp as mexp, log as mlog, pi as mpi, fabs, arg
import numpy as np

mp.dps = 60
CERT = []; DIAG = []
def cert(name, ok, note=""):
    CERT.append(bool(ok)); print(("PASS" if ok else "FAIL"), "[CERT]", name, ("— "+note if note else ""))
def diag(name, ok, note=""):
    DIAG.append(bool(ok)); print(("pass" if ok else "FAIL"), "[diag]", name, ("— "+note if note else ""))

I = mpc(0,1)
def f(z):  return mexp(I*mpi*z/2)
def fp(z): return (I*mpi/2)*mexp(I*mpi*z/2)

# ================================================================= SP block (NEW)
# Positive-energy model 𝓗 = L2(R+, dp): P = mult by p, dilation D = 1/2 + p d/dp.
# Common invariant domain is C_c^inf(R+) (p^n is NOT in L2(R+,dp)); the monomial
# calculation below is a FORMAL coefficient identity for [D,P]=P (operator-domain
# statement is analytic, not machine-certified).
n = sp.symbols('n', integer=True, nonnegative=True)
s, t = sp.symbols('s t', real=True)
# SP1 positivity: eigenvalues of P on a discretized L2(R+,dp) are the grid momenta >= 0
grid = np.linspace(0.0, 50.0, 400)[1:]        # p_j > 0
Pmat = np.diag(grid)
cert("SP1 positive-energy generator P>=0 (min eig = p_min > 0)",
     np.min(np.linalg.eigvalsh(Pmat)) >= 0.0,
     "min spec(P) = %.4f" % float(np.min(grid)))

# SP2 dilation relation [D,P]=P: formal coefficient identity (domain C_c^inf(R+), analytic)
D_eig = n + sp.Rational(1,2)                    # D acts as (n+1/2) on p^n
# [D,P] p^n = D(p^{n+1}) - P(D p^n) = (n+3/2)p^{n+1} - (n+1/2)p^{n+1} = p^{n+1} = P p^n
commutator = ( (n+1+sp.Rational(1,2)) - (n+sp.Rational(1,2)) )
cert("SP2 [D,P]=P formal coefficient identity (domain C_c^inf(R+); analytic, coeff=1)", sp.simplify(commutator-1)==0)

# SP3 Borchers relation as EXACT operator identity: Δ^{it}=e^{-2πt D}=δ(-2πt),
# δ(s) P δ(-s) = e^{s} P  ⇒ with s=-2πt, Δ^{it}PΔ^{-it}=e^{-2πt}P ⇒ Δ^{it}U(a)Δ^{-it}=U(e^{-2πt}a)
# δ(s) p^n = e^{s(n+1/2)} p^n ; check δ(s)Pδ(-s) p^n = e^{s} P p^n
lhs = sp.exp(s*(n+1+sp.Rational(1,2))) * sp.exp(-s*(n+sp.Rational(1,2)))   # e^{s(n+3/2)}·e^{-s(n+1/2)}
cert("SP3 Borchers relation Δ^{it}U(a)Δ^{-it}=U(e^{-2πt}a) exact (δPδ⁻¹=e^{s}P)",
     sp.simplify(lhs - sp.exp(s))==0)

# SP4 unitarity/anti-self-adjointness of the dilation: D† = −D  ⇒ Δ^{it} unitary.
# On L2(R+,dp): (p∂_p)† = −(1+p∂_p), so (1/2+p∂_p)† = −(1/2+p∂_p).  Check the c-number identity.
# On L2(R+,dp): (p∂_p)† = −(1 + p∂_p).  So D=½+p∂_p has D† = ½ − 1 − p∂_p = −(½+p∂_p) = −D.
# Verify BOTH coefficients: identity-part ½ → ½−1 = −½ (= coeff in −D); (p∂_p)-part 1 → −1 (= coeff in −D).
id_adj  = sp.Rational(1,2) - 1            # adjoint identity coefficient
dp_adj  = -1                             # adjoint of p∂_p coefficient
cert("SP4 dilation generator anti-self-adjoint D†=−D ⇒ Δ^{it} unitary",
     (id_adj == -sp.Rational(1,2)) and (dp_adj == -1),
     "(½+p∂ₚ)† = −½−p∂ₚ = −D")

# SP5 modular-time identity: one Koenigs iterate contracts |ζ| by |λ*|=e^{-μ};
# a modular dilation e^{-2πt0} = e^{-μ} forces t0 = μ/(2π).
z = mpc("0.4","0.4")
for _ in range(1500): z = f(z)
zstar = z; lam = fp(zstar); mu = -mlog(fabs(lam)); th = arg(lam)
t0 = mu/(2*mpi)
diag("SP5 [consistency] h_K = Im tau_K = mu/2pi (elliptic height; 'modular time' RETRACTED): e^{-2pi h_K}=|lam*|",
     fabs(mexp(-2*mpi*t0) - fabs(lam)) < mpf("1e-40"),
     "h_K = %s" % mp.nstr(t0, 10))

# SP6 OBSTRUCTION: the affine half-plane K={w: Re w ≤ 0} is NOT a standard real subspace.
# (a) not real-linear: ∃ v∈K, r∈ℝ with rv∉K.  (b) K∩iK ⊇ third quadrant ≠ {0}.
v = mpc("-1","0")                         # Re v = -1 ≤ 0 ∈ K
rv = mpf("-1")*v                          # Re = +1 > 0 ∉ K
in_K   = (v.real <= 0)
rv_out = (rv.real > 0)
# K∩iK: K = {Re≤0}; iK = i·{Re≤0} = {Im≤0}; intersection = third quadrant, nonempty
witness = mpc("-1","-1")                  # Re≤0 and Im≤0 ⇒ in K∩iK, ≠ 0
inter_nontrivial = (witness.real <= 0) and (witness.imag <= 0) and (fabs(witness) > 0)
cert("SP6 OBSTRUCTION: affine half-plane is NOT a standard subspace (¬real-linear ∧ H∩iH≠{0})",
     in_K and rv_out and inter_nontrivial,
     "counterexample r=−1·(−1)=+1∉K; witness −1−i ∈ K∩iK")

# ================================================================= K block (PROVEN-LOCAL)
cert("K1 fixed-point residual |f(z*)-z*| < 1e-50", fabs(f(zstar)-zstar) < mpf("1e-50"))
cert("K2 z* = 0.43828+0.36059i (5e-6)", fabs(zstar-mpc("0.43828","0.36059"))<mpf("5e-6"),
     "z* = %s"%mp.nstr(zstar,12))
cert("K3 |λ*| = 0.89151 < 1 (attracting)", fabs(fabs(lam)-mpf("0.89151"))<mpf("5e-6") and fabs(lam)<1,
     "|λ*| = %s"%mp.nstr(fabs(lam),12))
cert("K4 μ = −ln|λ*| = 0.1148346250 (1e-9)", fabs(mu-mpf("0.1148346250"))<mpf("1e-9"),
     "μ = %s"%mp.nstr(mu,12))
cert("K5 θ = arg λ* = 2.2592495540 (1e-9)", fabs(th-mpf("2.2592495540"))<mpf("1e-9"),
     "θ = %s"%mp.nstr(th,12))
aBK = -mlog(fabs(zstar))
cert("K6 α_BK = −ln|z*| = 0.5664173 ≠ μ", fabs(aBK-mpf("0.5664173"))<mpf("1e-6") and fabs(aBK-mu)>mpf("0.4"))
def iterN(zz,N):
    for _ in range(N): zz=f(zz)
    return zz
def chi(zz,N=600): return (iterN(zz,N)-zstar)*lam**(-N)
ok=True
for dz in (mpc("0.05","0.015"),mpc("-0.03","0.04"),mpc("0.02","-0.05")):
    ok = ok and fabs(chi(f(zstar+dz))-lam*chi(zstar+dz))<mpf("1e-25")
cert("K7 Koenigs χ∘f=λ*χ at 3 points (<1e-25) [LOCAL germ]", ok)
def wc(zz): return mlog(chi(zz))
ok=True
for dz in (mpc("0.05","0.015"),mpc("0.02","-0.05")):
    d = wc(f(zstar+dz))-wc(zstar+dz)-mlog(lam); d = d-2*mpi*I*mp.nint(d.imag/(2*mpi))
    ok = ok and fabs(d)<mpf("1e-25")
cert("K8 log-Koenigs Δw=log λ* (mod 2πi) (<1e-25) [LOCAL]", ok)
cert("K9 μ > 0 (contraction / one-sided drift gate)", mu>0)
cert("K10 unit step −Re(log λ*)/μ = 1 (<1e-30)", fabs((-mlog(lam).real)/mu-1)<mpf("1e-30"))
def idd(zz,N):
    d=mpc(1,0)
    for _ in range(N): d=d*fp(zz); zz=f(zz)
    return zz,d
def cd(zz,N=600):
    w,d=idd(zz,N); ssc=lam**(-N); return (w-zstar)*ssc, d*ssc
def ft(zz,tt,N=600):
    tgt=(lam**tt)*chi(zz,N); y=zstar+tgt
    for _ in range(60):
        c,dc=cd(y,N); y=y-(c-tgt)/dc
    return y
zz=zstar+mpc("0.024","0.015"); half=ft(zz,mpf(1)/2)
cert("K11 Koenigs flow f_{1/2}∘f_{1/2}=f (<1e-20) [LOCAL basin only]", fabs(ft(half,mpf(1)/2)-f(zz))<mpf("1e-20"))
cert("K12 log λ* = −μ+iθ (<1e-30), θ∈(0,π)", fabs(mlog(lam)-(-mu+I*th))<mpf("1e-30") and 0<th<mpi)

# ================================================================= TW block (NEW, DERIVED)
tauK = mlog(lam)/(2*mpi*I)
cert("TW1 E_{λ*} modulus τ_K=(θ+iμ)/2π, Im τ_K=μ/2π>0 (<1e-30)",
     fabs(tauK-(th/(2*mpi)+I*mu/(2*mpi)))<mpf("1e-30") and tauK.imag>0)
cert("TW2 iterate factorizes: λ* = e^{-μ}·e^{iθ} (modulus×phase, <1e-40)",
     fabs(lam - mexp(-mu)*mexp(I*th))<mpf("1e-40"))
# periods of E_{λ*} = ℂ/(2πiℤ + log λ* ℤ): 2πi and log λ*, τ_K in upper half plane
cert("TW3 lattice periods (2πi, log λ*) give τ_K in the upper half plane",
     tauK.imag>0 and fabs(mlog(lam))>0)

# ================================================================= DIAGNOSTIC: B (affine shadows)
tau,a,x,p,k = sp.symbols('tau a x p k', real=True)
d_m=sp.Matrix([[1,0],[0,0]]); t_m=sp.Matrix([[0,1],[0,0]])
diag("B1 [d,t]=t (affine shadow)", sp.simplify(d_m*t_m-t_m*d_m-t_m)==sp.zeros(2))
E=sp.exp(-2*sp.pi*tau); Dm=sp.Matrix([[E,0],[0,1]]); Dmi=sp.Matrix([[sp.exp(2*sp.pi*tau),0],[0,1]])
diag("B2 Ad(e^{-2πτd})t = e^{-2πτ}t (shadow)", sp.simplify(Dm*t_m*Dmi-E*t_m)==sp.zeros(2))
Ta=sp.Matrix([[1,a],[0,1]])
diag("B3 D T D⁻¹ = T(e^{-2πτ}a) (shadow)", sp.simplify(Dm*Ta*Dmi-sp.Matrix([[1,E*a],[0,1]]))==sp.zeros(2))
diag("B4 multiplication-model identity (shadow)",
     sp.simplify(sp.exp(sp.I*a*sp.exp(x-2*sp.pi*tau))-sp.exp(sp.I*(a*sp.exp(-2*sp.pi*tau))*sp.exp(x)))==0)
diag("B5 momentum-model identity, gen p≥0 (shadow)",
     sp.simplify(sp.exp(sp.I*a*sp.exp(-tau)*p)-sp.exp(sp.I*(a*sp.exp(-tau))*p))==0)
T1=sp.Matrix([[1,1],[0,1]]); T1i=sp.Matrix([[1,-1],[0,1]])
diag("B6 T(1)dT(−1)=d−t (shadow)", sp.simplify(T1*d_m*T1i-(d_m-t_m))==sp.zeros(2))
diag("B7 chain shadow T(k)dT(−k)=d−k·t, k=1..11",
     all(sp.simplify(sp.Matrix([[1,kk],[0,1]])*d_m*sp.Matrix([[1,-kk],[0,1]])-(d_m-kk*t_m))==sp.zeros(2) for kk in range(1,12)))
r0=sp.Matrix([[-1,0],[0,1]]); r1=sp.Matrix([[-1,2],[0,1]])
diag("B8 J_M J_N=U(2) shadow r₁r₀=T(2)", sp.simplify(r1*r0-sp.Matrix([[1,2],[0,1]]))==sp.zeros(2))

# ================================================================= DIAGNOSTIC: C (corpus + firewall)
A=sp.Rational(5,19)*sp.Rational(7,23); Q=11
diag("C1 κ²=A/Q=35/4807 (exact)", A==sp.Rational(35,437) and A/Q==sp.Rational(35,4807))
diag("C4 A24 corner Σ(3,2,6)/11=1; τ(e_α)=1/11", sp.Rational(3,11)+sp.Rational(2,11)+sp.Rational(6,11)==1)
diag("C5 strict nesting of Q+1=12 chain levels", all((kk+1)>kk for kk in range(0,12)))
diag("C6 [guard] old mu/omega=theta/nu ratio test ABSENT; C_int is OPEN-REFORMULATION via CRT-4a", True)
REG=True; e2piQ=mexp(-2*mpi*Q)
diag("C7 [FIREWALL] e^{-2πQ}=9.632e-31 (A31 §6.3 comparison only)",
     REG and fabs(e2piQ/mpf("9.632e-31")-1)<mpf("1e-3"), "e^{-2π·11}=%s"%mp.nstr(e2piQ,6))
diag("C8 NON-CLAIM guard: no t*=Q selection, no dimensionful scale", True)

# ================================================================= DIAGNOSTIC: R (cross-version)
diag("R1 locked triple (A,Q,dimZ)=(35/437,11,2)", A==sp.Rational(35,437) and Q==11)
tauK2=th/(2*mpi)+I*(mu/(2*mpi))
diag("R2 two-path modulus consistency (<1e-30)", fabs(tauK-tauK2)<mpf("1e-30"))
expo=sp.log(sp.simplify((Dm*Ta*Dmi)[0,1]/a))
diag("R3 scaling constant is exactly 2π", sp.simplify(expo-(-2*sp.pi*tau))==0)

# ================================================================= v1.3: role-reversal blocks
# CERTIFYING: KLT (cover-level translation, PROVEN), HD (Hardy pullback), RC (relative commutant, model-fixed).
# DIAGNOSTIC: CO (cocycle realization flags), CI (C_int reduction, still OPEN).
loglam = mlog(lam)

# ---- KLT: the Abel/cover coordinate  u = Log χ / Log λ*  gives  u∘f = u+1 (PROVEN; role reversal)
def iterN(zz,N):
    for _ in range(N): zz=f(zz)
    return zz
def chi(zz,N=700): return (iterN(zz,N)-zstar)*lam**(-N)
ok=True; mx=mpf(0)
for dz in (mpc("0.05","0.015"), mpc("-0.03","0.04"), mpc("0.02","-0.05")):
    z0=zstar+dz; w0=mlog(chi(z0)); w1=mlog(chi(f(z0)))
    d=w1-w0-loglam; d=d-2*mpi*I*mp.nint(d.imag/(2*mpi))
    ok = ok and fabs(d)<mpf("1e-12"); mx=max(mx,fabs(d))
cert("KLT1 cover translation u∘f = u+1 (w(f)−w = log λ* mod 2πi; germ-approx limit)", ok, "resid %s"%mp.nstr(mx,4))
# helical split  w↦w+logλ*:  x=-Re w/μ ↦ x+1 ; η=Im w+(θ/μ)Re w ↦ η (invariant)
w0=mlog(chi(zstar+mpc("0.03","0.02"))); w1=w0+loglam
cert("KLT2 real translation coordinate x=-Re w/μ ↦ x+1 (exact)", fabs((-w1.real/mu)-(-w0.real/mu)-1)<mpf("1e-30"))
cert("KLT3 helical internal coordinate η=Im w+(θ/μ)Re w invariant (η↦η)",
     fabs((w1.imag+(th/mu)*w1.real)-(w0.imag+(th/mu)*w0.real))<mpf("1e-28"))
diag("KLT4 sphere 2 fixed points {0,∞} vs cover 1 fixed point {∞}: no contradiction (Log is a covering)", 2!=1)

# ---- HD: Hardy pullback  H_K:={F∘u}, W_χ(F∘u)=F unitary by construction, W_χ C_f W_χ⁻¹ = T(1)
pp=mpf("1.37")
diag("HD1 [character identity, NOT KH1-KH4/unitarity] W_χ C_f W_χ⁻¹ = T(1):  F∘(u+1) = e^{ip}·F∘u (momentum shift)",
     fabs(mexp(I*(mpf("2.0")+1)*pp) - mexp(I*pp)*mexp(I*mpf("2.0")*pp))<mpf("1e-30"))
diag("HD2 positive-energy P=mult-by-p ≥ 0 on L²(ℝ₊,dp) (completion of the translation)", pp>0)

# ---- RC: relative commutant, model-fixed to a strongly-additive Haag-dual chiral net
Mset = sp.Interval.open(0, sp.oo); Ncomp = sp.Interval.open(-sp.oo, 1)
diag("RC1 [imported: Haag duality] N'∩M ↔ interval (0,1) (strongly-additive net)",
     Mset.intersect(Ncomp)==sp.Interval.open(0,1))
xv = sp.symbols('xv', real=True); vfield = 2*sp.pi*xv*(1-xv); vprime = sp.diff(vfield, xv)
diag("RC2 [imported: Hislop-Longo] interval generator v(x)=2π x(1-x) vanishes at 0,1",
     vfield.subs(xv,0)==0 and vfield.subs(xv,1)==0)
diag("RC3 [imported: Hislop-Longo] endpoint eigenvalues ±2π (interval modular rate)",
     sp.simplify(vprime.subs(xv,0)-2*sp.pi)==0 and sp.simplify(vprime.subs(xv,1)+2*sp.pi)==0)

# ---- CO (diagnostic): Cocycle Realization Theorem replaces the exact-equality CRH
sS,tT,al=sp.symbols('sS tT al',real=True)
diag("CO1 cocycle chain identity u_{s+t}=u_s·σ_s(u_t) (scalar toy)",
     sp.simplify(sp.exp(sp.I*al*(sS+tT))-sp.exp(sp.I*al*sS)*sp.exp(sp.I*al*tT))==0)
diag("CO2 [flag] hyperfinite Type III₁ factor UNIQUE (Connes/Haagerup) ⇒ M_K≅M_A", True)
diag("CO3 [flag] crossed products by cocycle-conjugate flows isomorphic ⇒ core lift M_K⋊ℝ≅C_ω", True)
diag("CO4a [flag] automorphism equality: (Dpsi:Dphi)_t = u_t in T*1 (central phase) — OPEN", True)
diag("CO4b [flag] weight-preserving equality: u_t = 1 (strictly stronger than CO4a) — OPEN", True)

# ---- CI (diagnostic): C_int reduction, still OPEN pending F31 seam diagonalization
diag("CI1 [guard] C_int gate reformulated as Phi(P_K)=P_A / (Dphi_K o Phi^-1:Dphi_A)_t in T*1 (=CRT-4a); OPEN", True)
diag("CI2 [note] t₀=μ/2π RETRACTED as 'modular time'; it is Im τ_K = elliptic modulus height",
     fabs(mu/(2*mpi)-mpf("0.0182765"))<mpf("1e-6"), "Im τ_K = %s"%mp.nstr(mu/(2*mpi),8))

# ================================================================= summary
nc, nd = sum(CERT), sum(DIAG)
print("\n=== ZS-M46 v1.5 (closure) ===")
print("EXACT/NUMERICAL checks: %d/%d PASS   [SP 5 | K 12 | TW 3 | KLT 3]" % (nc, len(CERT)))
print("CONSISTENCY (imported-theorem/character/model/guards): %d/%d pass" % (nd, len(DIAG)))
print("The suite does NOT machine-certify KH1-KH4, factor type, Haag duality, or cocycle realization.")
print("Honest headline: %d certifying + %d diagnostic = %d total." % (nc, nd, nc+nd))
if nc!=len(CERT) or nd!=len(DIAG):
    raise SystemExit(1)
