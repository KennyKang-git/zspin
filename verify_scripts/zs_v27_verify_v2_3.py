#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZS-A27 v2.3 verification suite — channel-(ii) computation (§7.1), CONSERVATIVELY corrected: status downgrades, Z-sector range reconciled, even-dimension torsion concern, necessary-not-sufficient. NONE of 13-22 is a closure proof.
Consistency/diagnostic checks for the new section §5.3. These are structural and
parity checks, NOT physical proofs. They test the deep-search conclusion that the
determinant-line reformulation is parity-obstructed (NON-CLAIM) while the
cross-coupled quadratic-invariant reformulation is parity-consistent and recasts
B3-2 as a finite rank test (still OPEN: kernel transplant + uncomputed rank).

v2.1 corrections (external technical review):
  (5) the k-parity statement: even-degree objects are J_Z-EVEN (not "only linear is odd").
  (8) the quadratic invariant is basis-independent ONLY if K transforms covariantly;
      the Kraus/CPTP reading is OPEN (no explicit A27 vacuum channel), not DERIVED.
  (10) the conductor selector is barred by ZS-M28 as a CORPUS CITATION; [D_cond,Gamma]=0
      (both diagonal) so the old "breaks grading" reasoning was invalid.
  (11) the Gauss-Bonnet endpoints are an ARITHMETIC INPUT to ZS-M30 Thm 30.3; the 28.14
      promotion is a corpus result (M30), cited here, not re-derived.
Checks 10 and 11 are corpus citations, NOT proofs.
"""
import numpy as np

PASS = []
def check(name, cond, detail=""):
    PASS.append(bool(cond))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

print("="*78)
print("ZS-A27 v2.2 — §5.3 multiplicity-2 audit + §7.1 channel-(ii) transmutation computation")
print("="*78)

# H_D^- = span{psi_-3, psi_-11}; both Gamma=-1 (J_Z-odd) by ZS-M27.2.
# J_Z = gamma^5 = J (ZS-S15) acts as -1 on the whole odd plane.
JZ = np.diag([-1.0, -1.0])         # seam involution on the odd doublet
C  = np.array([[0.0, 1.0],[1.0, 0.0]])  # exchange involution C_{3<->11}

# (1) Odd multiplicity is exactly 2 (M27.2), not 0 and not 1.
mult = JZ.shape[0]
check("(1) odd cohomology multiplicity = 2 (ZS-M27.2)", mult == 2,
      f"dim H_D^- = {mult}")

# (2) character product chi_-3 * chi_-11 = chi_33 is V4-EVEN (a_chi additivity mod 2).
a3, a11 = 1, 1                      # odd characters carry a_chi = 1 (ZS-M22)
a33 = (a3 + a11) % 2               # = 0  -> even
check("(2) chi_-3 . chi_-11 = chi_33 is EVEN (ZS-M22 a_chi additivity)", a33 == 0,
      f"a_chi(chi_33) = ({a3}+{a11}) mod 2 = {a33}")

# (3) determinant line Psi_det = psi_-3 ^ psi_-11 is J_Z-EVEN (the parity obstruction).
detJZ = np.linalg.det(JZ)          # (-1)(-1) = +1 -> EVEN
check("(3) Psi_det = psi_-3 ^ psi_-11 is J_Z-EVEN  (=> determinant-line NON-CLAIM)",
      detJZ > 0, f"J_Z acts on Psi_det by det = {detJZ:+.0f} (M1 needs J_Z-ODD)")

# (4) exchange involution C is a DIFFERENT Z2 from the seam J_Z.
detC = np.linalg.det(C)            # -1 -> Psi_det is C-ODD
evJZ = sorted(np.linalg.eigvals(JZ).real.round().astype(int))
evC  = sorted(np.linalg.eigvals(C ).real.round().astype(int))
check("(4) C_{3<->11} != J_Z  (C-odd is not J_Z-odd)",
      (not np.array_equal(C, JZ)) and evJZ == [-1,-1] and evC == [-1,1],
      f"eig(J_Z)={evJZ}, eig(C)={evC}; C acts on Psi_det by det={detC:+.0f}")

# (5) J_Z-parity of a k-linear in odd fields = (-1)^k; only k=1 (the multiplet) is odd.
parities = {k: (-1)**k for k in (1,2,3,4)}
# CORRECTED: even-degree objects (det, bilinear) are J_Z-EVEN; odd-degree (k=1 AND k=3) are J_Z-odd
# -> "only linear is odd" is FALSE in general. What kills the determinant line is that the determinant
# (and every bilinear) is EVEN, so it cannot be the J_Z-ODD operator M1 needs. In the 2-dim odd algebra
# Lambda^3 H_D^- = 0, so the determinant-line *construction* leaves only the linear multiplet.
even_degree_even = (parities[2] > 0) and (parities[4] > 0)
odd_not_only_linear = (parities[1] < 0) and (parities[3] < 0)   # k=3 is ALSO odd
lambda3_vanishes = True   # dim H_D^- = 2  => Lambda^3 = 0
check("(5) even-degree objects are J_Z-EVEN (det/bilinear cannot be the odd operator); Lambda^3=0 in 2-dim",
      even_degree_even and odd_not_only_linear and lambda3_vanishes,
      f"parities {parities}: k=1,3 BOTH odd (not 'only linear'); det/bilinear (k=2,4) EVEN; Lambda^3(2-dim)=0")

# (6) cross-coupled residual rho = Omega^T K Omega is QUADRATIC (k=2) -> J_Z-EVEN (correct for a scalar).
k_residual = 2
check("(6) rho_Lambda = Omega^T K Omega is J_Z-EVEN (k=2) — correct for a parity-even scalar",
      (-1)**k_residual > 0, "vacuum-energy density must be parity-even")

# (7) K_- = P_- X^dag X P_- is PSD, and its 2x2 rank gives the A/B/C trichotomy.
rng = np.random.default_rng(0)
psd_ok = True
ranks_seen = set()
for _ in range(5000):
    X = rng.standard_normal((4,2)) + 1j*rng.standard_normal((4,2))
    K = X.conj().T @ X                       # P_- X^dag X P_- restricted to the 2-dim odd block
    w = np.linalg.eigvalsh(K)
    if w.min() < -1e-9: psd_ok = False
    ranks_seen.add(int(np.linalg.matrix_rank(K, tol=1e-9)))
# explicit rank-0/1/2 representatives
r0 = np.zeros((2,2)); r1 = np.outer([1,1],[1,1]).astype(float); r2 = np.array([[2.,1.],[1.,2.]])
trich = (np.linalg.matrix_rank(r0)==0 and np.linalg.matrix_rank(r1)==1 and np.linalg.matrix_rank(r2)==2)
check("(7) K_- = P X^dag X P is PSD; rank in {0,1,2} (Case C/A/B)", psd_ok and trich,
      f"min-eig>=0 over 5000 draws; ranks observed {sorted(ranks_seen)}")

# (8) CORRECTED: rank(X^dag X) = rank X is basis-independent LINEAR ALGEBRA. The SCALAR rho=Omega^dag K Omega
#     is basis-independent ONLY if K transforms covariantly (Omega->U Omega, K->U K U^dag); rotating Omega
#     with K FIXED is NOT invariant. The Kraus/CPTP reading needs an explicit A27 vacuum channel whose
#     Kraus operators are the columns of X -- M33's X(g) is an RH/Weil operator, not that channel -> OPEN.
X = rng.standard_normal((4,2)) + 1j*rng.standard_normal((4,2))
K = X.conj().T @ X
gram   = int(np.linalg.matrix_rank(K, tol=1e-9))
kraus  = int((np.linalg.svd(X, compute_uv=False) > 1e-9).sum())   # = rank X (linear algebra, no CPTP claim)
Om = rng.standard_normal(2) + 1j*rng.standard_normal(2)
U,_ = np.linalg.qr(rng.standard_normal((2,2)) + 1j*rng.standard_normal((2,2)))
rho0       = (Om.conj() @ K @ Om).real
rho_cov    = ((U@Om).conj() @ (U@K@U.conj().T) @ (U@Om)).real      # covariant -> invariant
rho_Kfixed = ((U@Om).conj() @ K @ (U@Om)).real                    # K fixed   -> NOT invariant
rank_basis_indep = (gram == kraus)
invariance_is_conditional = (abs(rho_cov-rho0) < 1e-9) and (abs(rho_Kfixed-rho0) > 1e-9)
check("(8) rank basis-independent linear algebra; scalar invariant IFF K covariant; Kraus/CPTP reading OPEN",
      rank_basis_indep and invariance_is_conditional,
      f"rank(X^dagX)={gram}=rank X={kraus}; rho_cov={rho_cov:.3f}=rho0={rho0:.3f}, rho_Kfixed={rho_Kfixed:.3f}!=rho0 (conditional)")

# (9) impedance primes are DISJOINT from the V4 ramified primes {3,11} (no CP/arithmetic conflation).
A_primes = {5,7,19,23}             # A = 35/437 = (5/19)(7/23)
V4_primes = {3,11}                 # conductors of K = Q(sqrt-3, sqrt-11)
check("(9) impedance primes {5,7,19,23} ∩ V4 primes {3,11} = ∅ (layers stay distinct)",
      A_primes.isdisjoint(V4_primes), f"intersection = {A_primes & V4_primes}")

# (10) CORRECTED -> CORPUS CITATION (not a re-derivation). The conductor selector is barred by ZS-M28.
#      The v2.0 reasoning ("not block-scalar -> breaks grading") was INVALID: D_cond=diag(0,log3,log11,log33)
#      and Gamma=diag(1,1,-1,-1) are BOTH diagonal, so [D_cond,Gamma]=0 -- a diagonal decoration commutes
#      with the chirality grading and does NOT break it. Real grading-breaking needs off-diagonal mixing
#      P+ D_cond P- != 0. Here we verify only the honest facts (commutation + the log tie) and CITE M28.
import math
Dcond = np.diag([0.0, math.log(3), math.log(11), math.log(33)])
Gamma4 = np.diag([1.0,1.0,-1.0,-1.0])
commutes = np.allclose(Dcond @ Gamma4 - Gamma4 @ Dcond, 0.0)          # TRUE: both diagonal
log_additive = abs((math.log(3)+math.log(11)) - math.log(33)) < 1e-12 # log3+log11=log33 (ZS-M33 D4b)
check("(10) conductor selector barred by ZS-M28 (CORPUS CITATION, not re-derived); [D_cond,Gamma]=0",
      commutes and log_additive,
      "diagonal D_cond COMMUTES with Gamma (old 'breaks grading' claim invalid); bar is ZS-M28, cited not proved")


# (11) ZS-M30 Thm 30.3 (Robin-Truncation Boundary Family, DERIVED) promotes ZS-M28 Thm 28.14
#      (chi_-3 Y-icosahedron carrier) from DERIVED-CANDIDATE -> DERIVED, by locating the chi_-3
#      Eisenstein face as the t=0 endpoint of an action-derived Robin family h(x;t)=A*K(x;t).
#      Structural fact verified against the supplied ZS-M30 v1.0 text (lines 24, 337, 366, 370).
A = 35/437
import math
# the Robin coefficient endpoints come from PROVEN Regge deficits (ZS-S6 G): icosahedron 12*(pi/3)=4pi,
# truncated icosahedron 60*(pi/15)=4pi (Gauss-Bonnet). Verify both close at 4pi (the family is well-posed).
gb_ico = abs(12*(math.pi/3)  - 4*math.pi) < 1e-12
gb_tic = abs(60*(math.pi/15) - 4*math.pi) < 1e-12
# CORRECTED -> ARITHMETIC INPUT + CORPUS CITATION. Equal Gauss-Bonnet endpoint deficits do NOT prove the
# continuous Robin family, the action interpolation, the chi_-3 carrier identification, or spectral
# continuity. They are an arithmetic INPUT to ZS-M30 Thm 30.3; the 28.14 promotion is a CORPUS result (M30),
# cited here, not re-derived. So "12/12 PASS" must NOT be read as "M30 promotion verified".
gb_inputs_ok = gb_ico and gb_tic          # arithmetic input only
check("(11) Gauss-Bonnet endpoints = arithmetic INPUT to ZS-M30 Thm 30.3 (promotion is a corpus result, cited)",
      gb_inputs_ok, "icosa 12*pi/3=4pi, t-icosa 60*pi/15=4pi (input); the Robin-family promotion is ZS-M30, not re-derived here")

# (12) ZS-M30 is ORTHOGONAL to the parity obstruction: it carries no wedge/J_Z/four-form content,
#      so the determinant-line NON-CLAIM (check 3) is unaffected and Breakthrough 1 stays NON-CLAIM.
#      (Recomputed: the parity of Psi_det is fixed by J_Z alone, independent of any geometric-carrier fact.)
JZ = np.diag([-1.0, -1.0])
parity_psidet = np.linalg.det(JZ)         # +1 (EVEN) -- depends only on J_Z, not on M30
m30_orthogonal = (parity_psidet > 0)      # still J_Z-even regardless of the carrier promotion
check("(12) ZS-M30 orthogonal to parity -> determinant-line stays NON-CLAIM",
      m30_orthogonal, "Psi_det parity = +1 is set by J_Z only; geometric-carrier status cannot flip it")

print("="*78)
# ============================================================================
# CHANNEL (ii) TRANSMUTATION COMPUTATION (section 7.1) -- consistency/diagnostic,
# NOT a physical proof: B3 closure via (ii) is OPEN (odd analytic torsion uncomputed).
# ============================================================================
import math as _m
Mp=2.435e18; rho_obs_q=2.24e-12; gamma=38/9
_ln2,_ln3,_ln11=_m.log(2),_m.log(3),_m.log(11)
C_M=11*_ln2+_ln3
v=Mp*_m.exp(-gamma*C_M)
check("(13) Higgs transmutation reproduces v=245.93 GeV (machinery, ZS-S1 Factorized Det)",
      abs(v-245.93)<0.5, f"v=Mp*exp(-(38/9)(11ln2+ln3))={v:.2f} GeV")
rho_blind=v**2/Mp
check("(14) BLIND B3 (E*=v, eighth power): rho^(1/4)=2.48e-5 eV",
      abs(rho_blind*1e9-2.48e-5)/2.48e-5<0.02, f"rho^(1/4)_blind={rho_blind*1e9:.3e} eV (obs 2.24e-3)")
miss=rho_obs_q/rho_blind
orders_X=_m.log10((Mp/rho_obs_q)**4); orders_Y=_m.log10(miss**4)
check("(15) FRAME: transmutation recovers ~112 of 120 orders (X->Y)",
      abs((orders_X-orders_Y)-112)<3, f"X={orders_X:.0f} orders, Y={orders_Y:.1f} orders -> recovered {orders_X-orders_Y:.0f}")
Estar_need=_m.sqrt(rho_obs_q*Mp); gap=8*gamma*C_M-8*_m.log(Mp/Estar_need)
check("(16) gap = documented S1 trap: E*/v~9.5, 8*ln(9.5)=18.0; 3pi off 0.07",
      abs(Estar_need/v-9.5)<0.1 and abs(gap-18.0)<0.1 and abs(3*_m.pi-9.5)<0.1,
      f"E*/v={Estar_need/v:.3f}, exponent gap={gap:.2f}=8ln(9.5), 3pi={3*_m.pi:.2f}")
C_odd_need=(gamma*C_M-_m.log(Estar_need/v))/gamma
def rho_q(C): return (Mp*_m.exp(-gamma*C))**2/Mp
over=rho_q(10*_ln2+_ln3)/rho_obs_q; under=rho_q(12*_ln2)/rho_obs_q
check("(17) ODD closure needs C_odd=8.190; natural integer invariants BRACKET but miss",
      abs(C_odd_need-8.190)<0.01 and over>2 and under<0.5,
      f"C_odd_need={C_odd_need:.3f}; 10ln2+ln3 -> x{over:.1f} over, 12ln2 -> x{under:.2f} under (no integer combo hits)")
b0g2=8*_m.pi**2/(gamma*C_odd_need)
L_Z=Mp*_m.exp(-8*_m.pi**2/((5/3)*0.4))
check("(18) gauge cross-check: same exponent (b0*g_-^2=2.283); Z-sector doesnt confine (range reconciled)",
      abs(b0g2-2.283)<0.01 and L_Z<1e-20 and abs(_m.log10(Mp/L_Z)-51)<2,
      f"b0*g_-^2={b0g2:.4f}=2.283; rep. point b0=5/3,g^2=0.4 -> Lambda={L_Z:.1e} GeV = {_m.log10(Mp/L_Z):.0f} orders below Planck (text v2.2 wrongly said 47); full Z range ~10^-64..10^-23 GeV")

# === v2.3 CONSERVATIVE CORRECTIONS (documentary checks; none is a closure proof) ===
# (19) blind output vs post-unsealing 112/120 must be separated
check("(19) blind output (2.48e-5 eV) is separate from the post-unsealing 112/120 comparison",
      abs(rho_blind*1e9-2.48e-5)/2.48e-5<0.02 and abs((orders_X-orders_Y)-112)<3,
      f"blind={rho_blind*1e9:.2e} eV (no observed input); '112 of 120' uses rho_obs={rho_obs_q:g} -> post-unsealing, NOT a blind result")
# (20) C_odd=8.190 is BACK-SOLVED from observed -> falsification target, not prediction
check("(20) C_odd=8.190 is back-solved from observed rho (falsification target, NOT a prediction)",
      abs(C_odd_need-8.190)<0.01,
      f"C_odd_need uses E*_need=sqrt(rho_obs*Mp)={Estar_need:.1f} GeV (observed) -> A28 must compute odd spectrum WITHOUT this value")
# (21) even-dimension torsion vanishing concern (Y-sector is 6-dim, EVEN) -> route is HYPOTHESIS
dimY=6
check("(21) even-dimension torsion concern: Y-sector dim is EVEN -> RS torsion trivial (unitary) unless conductor data evades",
      dimY%2==0,
      f"dimY={dimY} (even): Ray-Singer torsion =1 (log=0) for even-dim closed orientable unitary coeffs (Witten/Ray-Singer; CM is odd-dim) -> OPEN, needs external NCG check; torsion route = HYPOTHESIS not DERIVED-CONDITIONAL")
# (22) the odd invariant is NECESSARY, not SUFFICIENT: rho_Lambda not fixed without C_- and sequestering
C_minus_computed=False; sequester_compat_proven=False
check("(22) odd invariant is necessary-not-sufficient: even exponent=34.58 leaves C_-(A,Q) and sequestering compatibility OPEN",
      (not C_minus_computed) and (not sequester_compat_proven),
      "B3 closes only with ALL of B3-1..7 (R0 trunk + mu_-=0 + O_EW(-) + loop mixing + C_-(A,Q) + scaling + Selective Sequestering Compatibility, sec 8.2) -- 'wall=one number' withdrawn")

n_pass = sum(PASS); n = len(PASS)
print(f"RESULT: {n_pass}/{n} consistent  (1-9,12 structural; 10-11 corpus citations; 13-22 channel-(ii) computation + v2.3 corrections -- NONE is a closure proof: B3 OPEN; torsion route = HYPOTHESIS w/ even-dim vanishing concern; Selective Sequestering Compatibility = top OPEN; C_odd=8.190 is back-solved)")
print("NOTE: checks 10 (conductor bar, ZS-M28) and 11 (28.14 promotion, ZS-M30) are corpus citations,")
print("      NOT re-derivations. Checks 5 and 8 are corrected per the v2.1 external review.")
print("Interpretation: determinant-line path is parity-obstructed (NON-CLAIM);")
print("cross-coupled quadratic invariant is parity-consistent and recasts B3-2 as a")
print("finite rank test on the ZS-M33 kernel — still OPEN (transplant HYPOTHESIS + rank uncomputed).")
print("B3 remains OPEN. The odd invariant is one necessary-not-sufficient S1 subgate; the top open problem is the Selective Sequestering Compatibility Theorem (R0+M1, sec 8.2).")
print("Note: the channel-(ii) analysis originated in AI-assisted deep-search; internal consistency here is NOT independent validation -- external NCG review + DESI are what would settle it. No fitted parameters introduced.")
print("="*78)
assert n_pass == n, "some checks failed"
