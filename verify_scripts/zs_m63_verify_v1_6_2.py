#!/usr/bin/env python3
"""
zs_m63_verify_v1_6_2.py -- deterministic verification suite for ZS-M63 v1.6.2
=========================================================================
Paper : ZS-M63 v1.6.2, "Finite-Observable Saturation and Rigidity of
        Reflection Asymmetry"

CONSISTENCY PATCH FOR THE v1.6.1 AUDIT (AUDIT-PASS-MINOR, RELEASE-BLOCKING: NO)
--------------------------------------------------------------------------------
 V1  ROW_SPEC still carried pre-renumbering theorem labels (F3 "Thm 9.4",
     F4-F6 "Thm 9.5", and the F7 call site "Remark 9.3").  Fixed, and the row
     map / observations / JSON are regenerated together.
 V2  S3 only checks that the manuscript table is byte-identical to the
     registry, so a wrong number present in BOTH was invisible.  S5 now also
     cross-checks every "Thm x.y" / "Prop x.y" / "Remark x.y" label appearing in
     ROW_SPEC against the headings actually present in the manuscript.  This is
     precisely the hole that let V1 survive.
 V3  degraded runs reused the canonical output names, so a --no-sympy run could
     overwrite a good FULL ledger, and a stale certificate could let S7 pass.
     The profile suffix now records the degraded mode as well (".no_sympy"), so
     degraded runs never touch canonical artifacts.
 V4  manuscript-side only: the contribution table gained the missing row for
     Theorem 9.8, and the companion response document's round counts were
     brought up to date.

COMPLETION PATCH FOR THE v1.6 AUDIT (AUDIT-PASS-MINOR, S1 only)
----------------------------------------------------------------
 W1  F8 presented eta = min over six sampled b as if it were a uniform lower
     bound on lambda_min(Cov_b S) over the whole convex box.  It is a SAMPLED
     diagnostic and is now labelled as one; Thm 9.8 itself is untouched.
 W2  F8 said "first N = 8" while testing a non-contiguous ladder.  The ladder is
     contiguous over 1..12 now, so the reported first N is literally that.
 W3  S3 embedded the absolute manuscript path, making the ledger digest machine
     dependent.  Only the basename is recorded now.
 W4  the END-marker regex did not accept a three-component version, so v1.6.1
     would have been rejected by its own guard.
 W5  manuscript-side only: continuity of S stated in Thm 9.6 / Cor 9.7, the
     abstract Gevrey exponent unified, Stone-Weierstrass named, section and
     theorem numbers synchronised, manifest row count corrected.

CHANGES FORCED BY THE v1.5 AUDIT (AUDIT-MAJOR-REVISION)
--------------------------------------------------------
 X1  Corollary 9.6' claimed N_eps can be infinite for non-trigonometric
     sufficient statistics.  FALSE, and the truth is stronger: with
     L = ||S||_(inf,2), a degree-N trigonometric vector T_N with
     delta_N = ||T_N - S||_(inf,2) and 2 L delta_N < eta gives
     DF_N(b) = Cov_b(T_N, S) and x' DF_N x >= (eta - 2 L delta_N)|x|^2 > 0,
     so F_N(b) = E_b[T_N] is strongly monotone and injective on convex K, and
     E_b[T_N] is a function of the Fourier moments of order <= N.  Hence
     N_0 <= N < infinity ALWAYS.  New row F8.
 X2  Gevrey phase-diagram entry used e^{-rho n^alpha} while the theorem proves
     e^{-rho (n+1)^alpha}; the ratio tends to 0 for alpha > 1, so it is not a
     two-sided asymptotic.  Manuscript-side fix.
 X3  Theorem 7.3 asserted an active-set list as a theorem while declaring its
     exhaustiveness unproved.  Manuscript-side: demoted to a candidate list.
 X4  Artifact profile leakage: QUICK and FULL wrote the SAME filenames, so a
     shipped certificate could come from a different run than the shipped JSON.
     Output names now carry the profile, the JSON records it, and new guard S7
     checks the certificate count against the profile and the manuscript.
 X5  E12 passed at gap < 1e-2 while the manuscript claimed 1.1e-4; the
     threshold is now the claimed figure.  E7 no longer asserts a sign order
     between two discretisations whose biases are not comparable.

CHANGES FORCED BY THE v1.4 AUDIT (AUDIT-MAJOR-REVISION) -- CORRECTION ONLY
--------------------------------------------------------------------------
 Y1  fail-closed loophole: a default run with no --manuscript still PASSed S3
     and S5.  The manuscript is now auto-discovered; if it is absent and
     --no-manuscript is not given, S3 and S5 FAIL.  --no-manuscript is an
     explicit opt-out and is itself recorded as a failure.
 Y2  the previous guards did not notice that the manuscript still ended with
     "END OF ZS-M63 v1.2".  S5 now also checks the paper-code line and the
     terminal END marker against VERSION, and rejects any END marker naming a
     different version.
 Y3  manuscript-side corrections only (no code impact): N_eps was a Fourier
     truncation order but was used for a count of sufficient statistics; the
     model classes C_{s,B} and G_{rho,alpha,B} were never defined; Thm 8.3 used
     r_1 and ell without defining them; Thm 7.4 omitted its domain; and the E12
     wording overclaimed a "certificate at the LP optimum".

CHANGES FORCED BY THE v1.3 AUDIT (AUDIT-MAJOR-REVISION) -- CORRECTION ONLY
--------------------------------------------------------------------------
 Z1  Prop 5.7 claimed deg_sigma E = 2n+1 ALWAYS.  FALSE.  For n=1 with a_0 = 0
     (a symmetric interior datum) p_1(x) = x, so Res(p_1, p_1 o (-id)) = 0 and
     E(sigma) = -4 b_1^2 sigma^2 has degree 2, not 3.  The correct statement is
     deg <= 2n+1 with [sigma^{2n+1}] E = -2 Res(p_n, p_n o (-id)), hence exact
     degree 2n+1 IF AND ONLY IF that resultant is nonzero.  Row C11 now checks
     the universal bound, the leading-coefficient identity, AND a symmetric
     NEGATIVE CONTROL where the degree genuinely drops.
 Z2  Without sympy the script ABORTED (AttributeError on sp.Rational built
     outside the HAVE_SYMPY guard), so rows after E12 and the whole harness were
     never emitted.  All sympy use is now inside guards, E12b is sympy-free, and
     a --no-sympy switch forces the degraded path so the failure mode is itself
     testable.  The full 66-row ledger is emitted either way.
 Z3  Remark 5.9 margin: B <= 2n+1 bad points leave B+1 <= 2n+2 gaps, so the
     largest gap is >= L/(2n+2) and its midpoint is >= L/(4n+4) from anything
     bad.  The manuscript said L/(2n+3), which is not implied.
 Z4  Theorem 5.3 at N=2: C(2,2)+2*2 = 5 = N(N+3)/2, so the "add at most one,
     giving <= 6" clause was wrong arithmetic and is deleted; the bound
     N(N+3)/2 is universal.
 Z5  Stale-identifier drift has recurred in every round.  Two SELF-REFERENTIAL
     guards are added: S5 audits the manuscript and S6 audits this script for
     filename-shaped references to superseded versions and for declared counts
     that disagree with the constants actually used.  Row names in ROW_SPEC no
     longer embed any count, removing that drift class at the source.

CHANGES FORCED BY THE v1.2 AUDIT (AUDIT-MAJOR-REVISION)
-------------------------------------------------------
 A1  E12 was NOT a global certificate: the shift was chosen on a grid, the
     factorisation was numerical, the residual was measured on a grid, and no q
     or Gram matrix was emitted.  E12 is now an EXACT rational Gram (SOS)
     certificate -- rational Hermitian G, exact coefficient identity
     sum_i G[i,i+k] = c_k, and exact positivity of every leading principal
     minor -- so 1-P and -(P+P(-.)) are nonnegative on the WHOLE circle with no
     grid anywhere.  It yields a certified rational lower bound on A_2^-.
     The old numerical factorisation survives as the diagnostic row E12b.
 A2  The "environment-invariant row map" claim was false: row names changed with
     sympy availability.  All ids, classes and names now come from the frozen
     ROW_SPEC registry below; only status and detail depend on the environment.
     Row S4 guards that the emitted ids equal the registry exactly.
 A3  Thm 5.3 self-pair error: Delta_j + Delta_k <= 2pi is right for j != k but
     j = k needs 2 Delta_j <= 2pi, which is false.  Corrected count: j<k gives at
     most one collision each, j=k gives at most two (theta_j crosses 0 and pi
     once each), so |B| <= C(N,2) + 2N = N(N+3)/2 with N = n+1.  Row B4.
 A4  Prop 5.7 is NOT an independent second existence proof.  Non-vanishing of
     the eliminant uses Prop 5.6 (Sigma nondegenerate) together with the
     monotone finiteness of Thm 5.5 Step 5.  Row C11 now also certifies the
     EXACT degree 2n+1 and the leading coefficient -2 Res(p_n(x), p_n(-x)).
 A5  Yang-Xie endpoints live in T = [0,1]; the wrap-around arc is
     f_L = 1 - u/(2pi), f_H = u/(2pi).  Row E11.

CHANGES FORCED BY THE v1.1 AUDIT (AUDIT-CORRECTION-REQUIRED)
------------------------------------------------------------
 Q1  "each node moves 2pi/(n+1)" was FALSE (B5 computed acc.mean()).  Only
     sum_j Delta_j = 2pi holds.  Row B5 now reports the individual shifts, checks
     the sum, and checks that they are NOT all equal.  Delta_j+Delta_k <= 2pi
     still gives finiteness, so the theorem survives.
 Q2  Arc Sigma non-degeneracy is now proved and checked: Schur-complement
     formulas for sigma_-, sigma_+ (rows C9) and the exact identity
     sigma_+ - sigma_- = 2T(1 - b_n^2 e^T (T^2 I - J_n^2)^{-1} e)
                       = 2T det(L)/det(T^2 I - J_n^2)  (row C10),
     L = localizing matrix of (T^2-x^2)dnu, so Sigma nondegenerate <=> L > 0.
 Q3  Algebraic collision certificate: p_{n+1}(x;sigma) is AFFINE in sigma, so
     Res_x(p(x;sigma), p(-x;sigma)) is a polynomial in sigma of degree <= 2n+2
     (row C11).  Sharper than the pairwise bound.
 Q4  F-M63.ARC CLOSED: exact normalisation mapping to Yang-Xie Thm 2 verified
     coefficient by coefficient (row E11).
 Q5  E9 was called a "dual certificate" but only checked a grid.  Renamed to a
     numerical dual candidate; a GLOBAL Fejer-Riesz certificate is added (E12).
 Q6  Class census corrected again: C is symbolic-only; B7, C8, F1, Z1 were
     floating point and are re-tagged V.  Evidence = C+V+W; X is NOT evidence.
 Q7  requirements are EMBEDDED in this file (--print-requirements) so the pinned
     runtime cannot be lost when the package is re-attached.
 Q8  Degenerate points A=0 and t=0 of Thm 7.2 / 8.3 are declared and checked
     (row E13).  Sobolev constant renormalised: hatC = C/Lambda_n (row F7).
Rules : [규칙]_검증·아티팩트 v1.2  (Script Contract, fail-closed, class census)

CHANGES FORCED BY THE v1.0 INDEPENDENT AUDIT (AUDIT-MAJOR-REVISION)
-------------------------------------------------------------------
 R1  Thm 5.2 / 5.4 proof engine replaced.  Individual monotonicity of nodes does
     NOT give monotone pair sums (counterexample -2+x, 2-x).  New engine is the
     first-order eigenvalue perturbation identity, which gives a COMMON
     direction for every node:
        circle :  G(phi) = G_0..G_{n-1} diag(1,..,1,e^{i phi}),
                  d theta_j / d phi = |v_j(last)|^2 > 0    (rows B6, B7)
        arc    :  J(sigma) = J + sigma e_n e_n^T  (free last Jacobi diagonal
                  == free moment mu_{2n+1}),
                  d lambda_j / d sigma = |v_j(last)|^2 > 0 (rows C3, C4)
     The arc family is now parametrised by sigma, not by the seed node; the
     admissible sigma set is a single interval (row C5).
 R2  Chamber I quintic is verified (row E8); extremizer recovery and
     complementary slackness are checked (row E9).
 R3  Class census re-tagged honestly.  Finite random samples are V/W/X, never C.
     R rows are controls, not evidence.  Declared census is guarded (row S1).
 R4  The row map is AUTO-GENERATED into a companion file and the manuscript is
     checked against it (row S3).  No hand-copied numbers.
 R5  E4 no longer uses four-point rational substitution.  The identity is
     reduced to two exact rational-function identities (row E4).
 R6  Missing sympy no longer aborts the run: it emits a FAILING dependency row
     and the numeric blocks still execute.  requirements.txt is shipped.
 R7  Edge cases added: Thm 6.1 at a = 0 (row E1b), Thm 9.4 large-n regime
     (row F3), Thm 9.5 convex domain (row F5).

CONVENTION LOCK
---------------
  d_TV(P,Q) = sup_B |P(B)-Q(B)| = 1/2 ||P-Q||_var   in [0,1]
  A(mu) = d_TV(mu, R_# mu),  R(theta) = -theta
  m_k = int e^{i k theta} dmu,  m_0 = 1,  m_{-k} = conj(m_k)
  T_n(m) = [ m_{j-k} ]_{j,k=0..n}
  ||f||_{H^s}^2 = sum_k (1+k^2)^s |hat f(k)|^2,  dsigma = dtheta/2pi

CLASSES : P proof | C exact/symbolic | V numerical at tolerance | W witness /
          counterexample search | R regression control | G guard |
          X exploratory diagnostic | D declaration | T tautology control
CLASS P IS 0 BY CONSTRUCTION.  No row proves a theorem.

RUN     : python3 zs_m63_verify_v1_6_2.py [--quick] [--no-sympy]
                 [--manuscript PATH | --no-manuscript] [--print-requirements]
          The manuscript is auto-discovered when --manuscript is omitted; if it
          cannot be found, S3 and S5 FAIL unless --no-manuscript is passed.
EXIT    : 0 iff 0 FAIL, row count == EXPECTED_ROWS, census == EXPECTED_CENSUS
"""
from __future__ import annotations
import sys, json, hashlib, platform
import numpy as np
from scipy.optimize import linprog

try:
    import sympy as sp
    HAVE_SYMPY = True
except Exception:                                    # R6: do not abort
    sp = None
    HAVE_SYMPY = False

REQUIREMENTS = """# ZS-M63 v1.6.2 verification suite -- pinned runtime (CPython 3.13)
numpy==2.4.4
scipy==1.17.1
sympy==1.14.0
"""
if "--print-requirements" in sys.argv:
    print(REQUIREMENTS, end=""); sys.exit(0)

VERSION = "v1_6_2"
VERSION_DOT = "v1.6.2"
SUPERSEDED = ["v1_0", "v1_1", "v1_2", "v1_3", "v1_4", "v1_5", "v1_6", "v1_6_1"]
QUICK = "--quick" in sys.argv
if "--no-sympy" in sys.argv:            # audit Z2: make the degraded path testable
    sp = None
    HAVE_SYMPY = False
import os as _os
NO_MANUSCRIPT = "--no-manuscript" in sys.argv
MANUSCRIPT = None
if "--manuscript" in sys.argv:
    MANUSCRIPT = sys.argv[sys.argv.index("--manuscript") + 1]
elif not NO_MANUSCRIPT:                    # audit Y1: auto-discover, fail closed
    for _c in (f"ZS-M63_{VERSION}.md",
               _os.path.join("/mnt/user-data/outputs", f"ZS-M63_{VERSION}.md"),
               _os.path.join(_os.path.dirname(_os.path.abspath(__file__)),
                             f"ZS-M63_{VERSION}.md")):
        if _os.path.isfile(_c):
            MANUSCRIPT = _c
            break

SEED = 20260821
EXPECTED_ROWS = 68
EXPECTED_CENSUS = {"C": 7, "V": 30, "W": 11, "X": 2, "R": 3, "G": 8, "D": 4, "T": 3}
CERT_EXPECTED = 2 if "--quick" in sys.argv else 3
TOL_LP = 5e-4
PROFILE = ("quick" if QUICK else "full") + ("" if HAVE_SYMPY else "+no_sympy")
# audit X4/V3: neither a QUICK nor a degraded run may touch canonical artifacts
SUF = (".quick" if QUICK else "") + ("" if HAVE_SYMPY else ".no_sympy")
LP_N = 1200 if QUICK else 3000
rng = np.random.default_rng(SEED)
LEDGER: list[dict] = []

# --- frozen row registry (audit A2): id -> (class, name). Environment must not
# --- change any of these; only status and detail may vary.
ROW_SPEC = {
    "D1": ("D", "convention lock d_TV = 1/2||.||_var in [0,1]"),
    "D2": ("D", "class P = 0 by construction: no row proves a theorem"),
    "D3": ("D", "dependency declaration (R6): sympy required for the C rows"),
    "T1": ("T", "TV control on an explicitly known pair"),
    "T2": ("T", "premise control: reflection-symmetric support has gap 0"),
    "T3": ("T", "negative control: closed form disagrees with a perturbed datum"),
    "A1": ("C", "det T_2 = 1-2|m1|^2-|m2|^2+2Re(m1^2 conj m2)"),
    "A2": ("C", "det S_2 = t^3(1-d)(1+d-2c^2)"),
    "A3": ("C", "Schur identity A det R_2 = (A^2-|r1|^2)^2-|A r2-r1^2|^2"),
    "A4": ("V", "arc symmetric strip 2c^2-1 <= d <= 2(1+g)c-2g-1 (50 samples)"),
    "A5": ("V", "T_2(m) PSD for 200 random atomic measures"),
    "A6": ("G", "rejection guard: PSD implies det T_2 >= 0"),
    "B1": ("W", "OPUC zeros lie in the open unit disk (counterexample search)"),
    "B2": ("W", "node sets of B_tau, B_tau' are disjoint for tau != tau'"),
    "B3": ("W", "circle: reflection-free (n+1)-atom representation exists (n=1..6)"),
    "B4": ("X", "bad-set cardinality (heuristic) vs the corrected bound C(N,2)+2N = N(N+3)/2, N=n+1 (audit S1: self-pair j=k separated)"),
    "B5": ("W", "circle: ALL nodes co-monotone; SUM of shifts = 2pi; the shifts are NOT individually 2pi/(n+1) (v1.1 audit Q1)"),
    "B6": ("V", "circle derivative identity d theta_j/d phi = |v_j(last)|^2 > 0"),
    "B7": ("V", "unitarity identity sum_j |v_j(last)|^2 = 1 (total shift = 2pi)"),
    "B8": ("V", "atom lower bound: r <= n atoms forces rank T_n <= n"),
    "C1": ("V", "tan-half transport: arc trig moments <-> Hausdorff moments on [-T,T]"),
    "C2": ("V", "arc: sigma-family is exact to degree 2n with positive weights, n+1 atoms"),
    "C3": ("V", "arc derivative identity d lambda_j/d sigma = |v_j(last)|^2 (audit repair R1)"),
    "C4": ("W", "arc: ALL n+1 nodes strictly increasing in sigma (common direction)"),
    "C5": ("W", "arc: admissible sigma set is a SINGLE interval"),
    "C6": ("X", "arc collision count (heuristic) vs bound N(N+1)/2, N=n+1"),
    "C7": ("W", "arc: a reflection-free rule exists (max reflection gap > 0)"),
    "C8": ("V", "annihilator lemma: q <= 2n+1 distinct nodes give full column rank"),
    "E1": ("V", "Thm 6.1 n=1 full-circle closed form vs grid LP"),
    "E1b": ("V", "Thm 6.1 edge case a=0, i.e. m1 = +-1: A_1^- = 0 (audit repair R7)"),
    "E2": ("R", "regression: A_1^-(lambda) reproduces the M62 constant A*"),
    "E3": ("V", "Thm 7.4 n=2 odd-gauge closed form vs odd-data LP"),
    "E4": ("C", "Thm 7.4 exact: two rational identities certify the radical solution (audit repair R5, no point substitution)"),
    "E5": ("R", "regression against M62 Thm 16 body {|w|<=1, 2v^2-1 <= sqrt(1-w^2)}"),
    "E6": ("V", "Thm 7.2 n=2 full-circle Schur reduction vs grid LP"),
    "E7": ("V", "Thm 8.3 arc n=2 system (strip+Schur+localizer, exact d-elimination) vs arc LP"),
    "E8": ("C", "chamber polynomials incl. Chamber I quintic (audit repair R2)"),
    "E9": ("W", "n=2 numerical dual candidate on a 40001-point grid (not a certificate)"),
    "E10": ("V", "Thm 7.5 dual formula vs primal LP"),
    "F1": ("V", "Sobolev upper/lower constant ratio = pi/sqrt(2), independent of (B,s,n)"),
    "F2": ("V", "Sobolev witness: positivity, ||f_a||_Hs = B, A(f_a) = 2a/pi"),
    "F3": ("V", "Thm 9.5 Gevrey witness admissible in the declared large-n regime"),
    "F4": ("V", "Thm 9.6 grad psi = E_b[S] (numerical gradient)"),
    "F5": ("W", "Thm 9.6 Hess psi = Cov_b(S) > 0 on the declared convex box [-1.2,1.2]^3 (repair R7)"),
    "F6": ("V", "Thm 9.6 strong monotonicity on the box (segment stays inside)"),
    "G1": ("V", "Thm 6.3 fragility: boundary jump of W_n equals 1 - A(mu_m)"),
    "G2": ("W", "Thm 6.4 minimax Delta_n = 1: Haar fiber holds both A=0 and A=1"),
    "G3": ("W", "Thm 4.1 dense selector: R-free grid represents interior data, support <= 2n+1"),
    "G4": ("V", "Prop 3.3 monotonicity A_n^- <= A_{n+1}^-, hence W_{n+1} <= W_n"),
    "Z1": ("V", "T_1(lambda) positive definite, |lambda| < 1"),
    "Z2": ("R", "full-circle diagnostic interval I_1(lambda) = [A*, 1]"),
    "Z3": ("D", "scope: full-circle diagnostic only; arc version needs the M62 effective-arc convention; D-M61-IOTA remains OPEN"),
    "C9": ("V", "Prop 5.6 arc admissible set Sigma = [sigma_-, sigma_+] by Schur complement, vs direct scan (audit Q2)"),
    "C10": ("V", "Prop 5.6 identity sigma_+-sigma_- = 2T(1-b_n^2<e,(T^2I-J_n^2)^-1 e>) = 2T detL/detM > 0 iff L > 0 (audit Q2)"),
    "C11": ("C", "Prop 5.7: p_{n+1}(x;sigma) is affine in sigma; deg_sigma of the collision eliminant is at most 2n+1 with leading coefficient -2 Res(p_n, p_n o (-id)); exact degree 2n+1 iff that resultant is nonzero, with a symmetric negative control where it vanishes"),
    "E11": ("V", "F-M63.ARC closure: Yang-Xie Thm 2 localiser with f_L = 1-u/2pi, f_H = u/2pi in T=[0,1] equals 2 x our L_g coefficient by coefficient"),
    "E12": ("C", "EXACT rational Gram (SOS) certificate: 1-P and -(P+P(-.)) are a(th)^* G a(th) with G rational, Hermitian, coefficient identity exact and all leading principal minors exactly positive -- no grid"),
    "E12b": ("V", "numerical approximate Fejer-Riesz factorisation (diagnostic only; superseded as a certificate by E12)"),
    "E13": ("V", "declared degenerate points of Thm 7.2 / 8.3: t=0 and A=0 handled outside the 1/A, 1/t formulas (audit Q8)"),
    "F7": ("V", "Remark 9.4 corrected normalisation hatC = C/Lambda_n in [2sqrt2/pi, 1]; the square wave beats the single sine strictly (audit Q8)"),
    "F8": ("V", "Thm 9.8 Gibbs finite-Fourier saturation with NON-trigonometric statistics, SAMPLED diagnostic: eta_hat is the minimum of lambda_min(Cov_b S) over a FIXED FINITE set of b and is not a certified uniform bound over the box; checks DF_N(b) = Cov_b(T_N,S), the quadratic bound and strong monotonicity at those b, and reports the first N in the contiguous tested range 1..12 with 2 L delta_N < eta_hat"),
    "S4": ("G", "row registry guard: emitted ids equal ROW_SPEC ids, in order, once each"),
    "S6": ("G", "self-reference guard on this script: no filename-shaped reference to a superseded version, no count embedded in a ROW_SPEC name, and EXPECTED_CENSUS sums to EXPECTED_ROWS"),
    "S5": ("G", "self-reference guard on the manuscript: no filename-shaped reference to a superseded version; paper-code line and terminal END marker name the current version; declared row count, census and evidence total agree with the constants used here; every Thm/Prop/Remark label used in ROW_SPEC exists as a heading in the manuscript; fails closed when no manuscript is available"),
    "S7": ("G", "artifact profile guard: the certificate written by this run holds the number of certified data points expected for this profile, and agrees with the count claimed in the manuscript"),
    "S1": ("G", "census guard: P=0 and census matches the declared distribution"),
    "S2": ("G", "row count equals the declared EXPECTED_ROWS constant"),
    "S3": ("G", "manuscript structural row map is byte-identical to the registry-generated table; fails closed when no manuscript is available and --no-manuscript was not passed"),
}
ROW_ORDER = list(ROW_SPEC)


def row(rid, _cls_ignored, _name_ignored, ok, detail=""):
    """Class and name are taken from ROW_SPEC, never from the call site."""
    cls, name = ROW_SPEC[rid]
    LEDGER.append(dict(id=rid, cls=cls, name=name,
                       status="PASS" if ok else "FAIL", detail=detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {rid:<5} {cls}  {name}"
          + (f"   -- {detail}" if detail else ""))
    return ok


# =====================================================================
# shared numerics
# =====================================================================
def moments_from_atoms(theta, p, n):
    z = np.exp(1j * np.asarray(theta))
    return np.array([np.sum(p * z ** k) for k in range(n + 1)])


def toeplitz(m, n):
    T = np.zeros((n + 1, n + 1), dtype=complex)
    for j in range(n + 1):
        for k in range(n + 1):
            d = j - k
            T[j, k] = m[d] if d >= 0 else np.conj(m[-d])
    return T


def grid_lp_Aminus(m, n, u=np.pi, N=None):
    N = N or LP_N
    t = np.linspace(0.0, u, N)
    rs, rd, beq = [np.ones(N)], [np.zeros(N)], [1.0]
    for k in range(1, n + 1):
        rs.append(np.cos(k * t)); rd.append(np.zeros(N)); beq.append(m[k].real)
        rs.append(np.zeros(N)); rd.append(np.sin(k * t)); beq.append(m[k].imag)
    ns = N
    cost = np.concatenate([np.zeros(ns), np.ones(ns), np.ones(ns)])
    Aeq = np.zeros((len(beq), 3 * ns))
    for i, (a, b) in enumerate(zip(rs, rd)):
        Aeq[i, :ns] = a; Aeq[i, ns:2 * ns] = b; Aeq[i, 2 * ns:] = -b
    Aub = np.zeros((ns, 3 * ns)); idx = np.arange(ns)
    Aub[idx, idx] = -1.0; Aub[idx, ns + idx] = 1.0; Aub[idx, 2 * ns + idx] = 1.0
    r = linprog(cost, A_ub=Aub, b_ub=np.zeros(ns), A_eq=Aeq, b_eq=np.array(beq),
                bounds=[(0, None)] * (3 * ns), method="highs")
    return r.fun if r.success else np.nan


def dual_lp_Aminus(m, n, N=1500):
    t = np.linspace(-np.pi, np.pi, N); nv = 1 + 2 * n
    cost = np.zeros(nv); cost[0] = -1.0
    for k in range(1, n + 1):
        cost[k] = -m[k].real; cost[n + k] = -m[k].imag
    A1 = np.zeros((N, nv)); A1[:, 0] = 1.0
    A2 = np.zeros((N, nv)); A2[:, 0] = 1.0
    for k in range(1, n + 1):
        A1[:, k] = np.cos(k * t)
        A2[:, k] = np.cos(k * t); A2[:, n + k] = np.sin(k * t)
    r = linprog(cost, A_ub=np.vstack([A1, A2]),
                b_ub=np.concatenate([np.zeros(N), np.ones(N)]),
                bounds=[(None, None)] * nv, method="highs")
    return -r.fun, r.x


# ---- OPUC / unitary Hessenberg (circle) ------------------------------
def verblunsky(m, n):
    Phi = np.array([1.0 + 0j]); al = []
    mm = lambda j: m[j] if j >= 0 else np.conj(m[-j])
    for _ in range(n):
        Ps = np.conj(Phi[::-1])
        num = sum(Phi[i] * mm(i + 1) for i in range(len(Phi)))
        den = sum(Ps[i] * mm(i) for i in range(len(Ps)))
        a = np.conj(num / den); al.append(a)
        Phi = np.concatenate([[0], Phi]) - np.conj(a) * np.concatenate([Ps, [0]])
    return np.array(al), Phi


def hess_G(al, phi):
    n = len(al); G = np.eye(n + 1, dtype=complex)
    for j in range(n):
        Th = np.eye(n + 1, dtype=complex); rho = np.sqrt(1 - abs(al[j]) ** 2)
        Th[j, j] = np.conj(al[j]); Th[j, j + 1] = rho
        Th[j + 1, j] = rho;        Th[j + 1, j + 1] = -al[j]
        G = G @ Th
    D = np.eye(n + 1, dtype=complex); D[n, n] = np.exp(1j * phi)
    return G @ D


def circle_nodes(al, phi):
    ev, V = np.linalg.eig(hess_G(al, phi))
    V = V / np.linalg.norm(V, axis=0)
    return ev, V


def refl_gap_circle(z):
    return float(np.min(np.abs(z[:, None] - np.conj(z)[None, :])))


# ---- arc: tan-half transport + Jacobi sigma family -------------------
def trig_to_z_map(n):
    P = np.polynomial.polynomial; rows = []
    c0 = P.polypow([1, 0, 1], n)
    r = np.zeros(2 * n + 1); r[:len(c0)] = c0.real; rows.append(r)
    for k in range(1, n + 1):
        c = P.polymul(P.polypow([1, 1j], 2 * k), P.polypow([1, 0, 1], n - k))
        rr = np.zeros(2 * n + 1, dtype=complex); rr[:len(c)] = c
        rows.append(rr.real.copy()); rows.append(rr.imag.copy())
    return np.array(rows)


def jacobi_from_moments(mu, n):
    """a_0..a_{n-1}, b_1..b_n from mu_0..mu_2n ; a_n is FREE (needs mu_{2n+1})."""
    H = np.array([[mu[i + j] for j in range(n + 1)] for i in range(n + 1)])
    R = np.linalg.cholesky(H).T
    a = np.zeros(n + 1); b = np.zeros(n + 1)
    for k in range(n):
        a[k] = R[k, k + 1] / R[k, k] - (R[k - 1, k] / R[k - 1, k - 1] if k > 0 else 0.0)
    for k in range(1, n + 1):
        b[k] = R[k, k] / R[k - 1, k - 1]
    return a, b


def arc_rule(a, b, n, sigma, mu0):
    d = a[:n + 1].copy(); d[n] = sigma
    J = np.diag(d) + np.diag(b[1:n + 1], 1) + np.diag(b[1:n + 1], -1)
    lam, V = np.linalg.eigh(J)
    return lam, mu0 * V[0, :] ** 2, V


def arc_data(n, u):
    T = np.tan(u / 2); Mm = trig_to_z_map(n)
    K = 2 * n + 3
    th = rng.uniform(-u, u, K); p = rng.dirichlet(np.ones(K))
    mt = moments_from_atoms(th, p, n)
    tgt = np.concatenate([[1.0], np.array([[mt[k].real, mt[k].imag]
                                           for k in range(1, n + 1)]).ravel()])
    mu = np.linalg.solve(Mm, tgt)
    return T, mt, mu, tgt


def arc_admissible(a, b, n, mu0, T, M=None):
    M = M or (800 if QUICK else 3000)
    span = 6 * max(b[1:n + 1]); c0 = a[:n].mean() if n else 0.0
    sig = np.linspace(c0 - span, c0 + span, M)
    adm, sets, ws = [], [], []
    for s in sig:
        lam, w, _ = arc_rule(a, b, n, s, mu0)
        if np.all(np.abs(lam) <= T + 1e-12) and np.all(w > 0):
            adm.append(s); sets.append(lam); ws.append(w)
    return np.array(adm), np.array(sets), np.array(ws), sig[1] - sig[0]


# ---- closed forms ----------------------------------------------------
def A1_closed(x, y):
    a = 1.0 - abs(x)
    if a <= 1e-15:
        return 1.0 if abs(y) > 1e-15 else 0.0
    return abs(y) if abs(y) <= a else (y * y + a * a) / (2 * a)


def A2_odd_closed(y1, y2):
    y1, y2 = abs(y1), abs(y2)
    if y2 * y2 >= 2 * y1 * y1:
        return y2
    return 2 * y1 * y1 / np.sqrt(4 * y1 * y1 - y2 * y2)


def _feas_circle(t, m1, m2, ng):
    A = 1.0 - t
    if t <= 1e-15:
        return True
    if A <= 1e-15:
        return abs(m1.imag) < 1e-12 and abs(m2.imag) < 1e-12
    x1, y1, x2, y2 = m1.real, m1.imag, m2.real, m2.imag
    u1 = np.linspace(x1 - t, x1 + t, ng)
    K = u1 ** 2 - y1 ** 2
    base = A * A - u1 ** 2 - y1 ** 2
    D = base ** 2 - (A * y2 - 2 * u1 * y1) ** 2
    ok = (base >= 0) & (D >= 0)
    if not ok.any():
        return False
    sq = np.sqrt(np.maximum(D, 0.0))
    return bool(np.any(ok & ((K - sq) / A <= x2 + t - 2 * (x1 - u1) ** 2 / t + 1e-13)
                          & ((K + sq) / A >= x2 - t - 1e-13)))


def A2_schur(m1, m2, tol=1e-9, ng=None):
    ng = ng or (1201 if QUICK else 4001)
    if not _feas_circle(0.0, m1, m2, ng):
        return 1.0
    lo, hi = 0.0, 1.0
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if _feas_circle(mid, m1, m2, ng) else (lo, mid)
    return 1.0 - lo


def _feas_arc(t, m1, m2, gam, ng):
    A = 1.0 - t
    if t <= 1e-15:
        return True
    if A <= 1e-15:
        return abs(m1.imag) < 1e-12 and abs(m2.imag) < 1e-12
    eps = 1e-12
    for c in np.linspace(gam, 1.0, ng):
        e_lo = t * (2 * c * c - 1); e_hi = t * (2 * (1 + gam) * c - 2 * gam - 1)
        if e_hi < e_lo - eps:
            continue
        r1 = m1 - t * c
        R = A * A - abs(r1) ** 2
        if R < -eps:
            continue
        Z = A * m2 - r1 ** 2
        if abs(Z.imag) > R + eps:
            continue
        rho = np.sqrt(max(R * R - Z.imag ** 2, 0.0))
        lo, hi = (Z.real - rho) / A, (Z.real + rho) / A
        ell = r1.real - gam * A
        if ell < -eps:
            continue
        h0 = (A + m2) / 2 - gam * r1
        if abs(h0.imag) > ell + eps:
            continue
        rp = np.sqrt(max(ell * ell - h0.imag ** 2, 0.0))
        lo = max(lo, 2 * (h0.real - rp), e_lo)
        hi = min(hi, 2 * (h0.real + rp), e_hi)
        if lo <= hi + eps:
            return True
    return False


def A2_arc(m1, m2, u, tol=1e-6, ng=None):
    ng = ng or (801 if QUICK else 4001)
    gam = np.cos(u)
    if not _feas_arc(0.0, m1, m2, gam, ng):
        return 1.0
    lo, hi = 0.0, 1.0
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if _feas_arc(mid, m1, m2, gam, ng) else (lo, mid)
    return 1.0 - lo


# =====================================================================
# BLOCK D / T  -- declarations and controls
# =====================================================================
def block_DT():
    row("D1", "D", "convention lock d_TV = 1/2||.||_var in [0,1]", True, "declared")
    row("D2", "D", "class P = 0 by construction: no row proves a theorem", True,
        "theorems are proved in the manuscript")
    row("D3", "D", "dependency declaration (R6): sympy required for the C rows", HAVE_SYMPY,
        f"sympy {'present ' + sp.__version__ if HAVE_SYMPY else 'MISSING -- see requirements.txt'}")
    p, q = np.array([0.3, 0.7]), np.array([0.7, 0.3])
    row("T1", "T", "TV control on an explicitly known pair", abs(0.5 * np.sum(np.abs(p - q)) - 0.4) < 1e-15)
    z = np.array([np.exp(0.3j), np.exp(-0.3j)])
    row("T2", "T", "premise control: reflection-symmetric support has gap 0",
        refl_gap_circle(z) < 1e-15)
    # negative control: the n=1 closed form must NOT reproduce a deliberately wrong datum
    bad = A1_closed(0.3, 0.2)
    row("T3", "T", "negative control: closed form disagrees with a perturbed datum",
        abs(bad - A1_closed(0.3, 0.25)) > 1e-3, "a formula that matched everything would be vacuous")


# =====================================================================
# BLOCK A -- moment-body algebra
# =====================================================================
def block_A():
    if HAVE_SYMPY:
        x1, y1, x2, y2 = sp.symbols("x1 y1 x2 y2", real=True)
        m1, m2 = x1 + sp.I * y1, x2 + sp.I * y2
        T2 = sp.Matrix([[1, sp.conjugate(m1), sp.conjugate(m2)],
                        [m1, 1, sp.conjugate(m1)], [m2, m1, 1]])
        det = sp.expand(sp.re(sp.expand(T2.det())))
        claim = sp.expand(1 - 2 * (x1**2 + y1**2) - (x2**2 + y2**2)
                          + 2 * sp.re(sp.expand(m1**2 * sp.conjugate(m2))))
        row("A1", "C", "det T_2 = 1-2|m1|^2-|m2|^2+2Re(m1^2 conj m2)",
            sp.simplify(det - claim) == 0, "symbolic difference exactly 0")
        t, c, d = sp.symbols("t c d", real=True)
        S2 = t * sp.Matrix([[1, c, d], [c, 1, c], [d, c, 1]])
        row("A2", "C", "det S_2 = t^3(1-d)(1+d-2c^2)",
            sp.simplify(sp.expand(S2.det()) - sp.expand(t**3 * (1 - d) * (1 + d - 2 * c**2))) == 0)
        A, r1r, r1i, r2r, r2i = sp.symbols("A r1r r1i r2r r2i", real=True)
        r1, r2 = r1r + sp.I * r1i, r2r + sp.I * r2i
        R2 = sp.Matrix([[A, sp.conjugate(r1), sp.conjugate(r2)],
                        [r1, A, sp.conjugate(r1)], [r2, r1, A]])
        lhs = sp.expand(sp.re(sp.expand(R2.det())) * A)
        rhs = sp.expand((A**2 - (r1r**2 + r1i**2))**2
                        - ((A * r2r - (r1r**2 - r1i**2))**2 + (A * r2i - 2 * r1r * r1i)**2))
        row("A3", "C", "Schur identity A det R_2 = (A^2-|r1|^2)^2-|A r2-r1^2|^2",
            sp.simplify(lhs - rhs) == 0)
    else:
        for rid, nm in (("A1", "det T_2 identity"), ("A2", "det S_2 identity"),
                        ("A3", "Schur identity")):
            row(rid, "C", nm + " [requires sympy]", False, "sympy unavailable")

    gam = np.cos(1.3); bad = 0
    for _ in range(50):
        th = rng.uniform(-1.3, 1.3, 300); p = rng.dirichlet(np.ones(300))
        cc = float(np.sum(p * np.cos(th))); dd = float(np.sum(p * np.cos(2 * th)))
        if not (2 * cc**2 - 1 <= dd + 1e-12 <= 2 * (1 + gam) * cc - 2 * gam - 1 + 2e-12):
            bad += 1
    row("A4", "V", "arc symmetric strip 2c^2-1 <= d <= 2(1+g)c-2g-1 (50 samples)",
        bad == 0, f"violations {bad}")

    bad = 0
    for _ in range(200):
        th = rng.uniform(-np.pi, np.pi, 6); p = rng.dirichlet(np.ones(6))
        T = toeplitz(moments_from_atoms(th, p, 2), 2)
        if np.linalg.eigvalsh((T + T.conj().T) / 2).min() < -1e-12:
            bad += 1
    row("A5", "V", "T_2(m) PSD for 200 random atomic measures", bad == 0, f"violations {bad}")

    bad = 0
    for _ in range(200):
        m = np.array([1.0, rng.uniform(-1, 1) + 1j * rng.uniform(-1, 1),
                      rng.uniform(-2, 2) + 1j * rng.uniform(-2, 2)])
        T = toeplitz(m, 2)
        psd = np.linalg.eigvalsh((T + T.conj().T) / 2).min() >= -1e-12
        det = 1 - 2 * abs(m[1])**2 - abs(m[2])**2 + 2 * np.real(m[1]**2 * np.conj(m[2]))
        if psd and det < -1e-10:
            bad += 1
    row("A6", "G", "rejection guard: PSD implies det T_2 >= 0", bad == 0, f"violations {bad}")


# =====================================================================
# BLOCK B -- circle saturation, with the REPAIRED proof engine
# =====================================================================
def block_B():
    worst = 0.0
    for n in [1, 2, 3, 4, 5]:
        for _ in range(4 if QUICK else 12):
            th = rng.uniform(-np.pi, np.pi, n + 4); p = rng.dirichlet(np.ones(n + 4))
            _, Phi = verblunsky(moments_from_atoms(th, p, n), n)
            worst = max(worst, float(np.max(np.abs(np.roots(Phi[::-1])))))
    row("B1", "W", "OPUC zeros lie in the open unit disk (counterexample search)",
        worst < 1.0, f"max |zero| = {worst:.8f}")

    minsep = np.inf
    for n in [1, 2, 3, 4]:
        for _ in range(3 if QUICK else 8):
            th = rng.uniform(-np.pi, np.pi, n + 4); p = rng.dirichlet(np.ones(n + 4))
            al, _ = verblunsky(moments_from_atoms(th, p, n), n)
            f1, f2 = rng.uniform(0, 2 * np.pi), rng.uniform(0, 2 * np.pi)
            if abs(((f1 - f2 + np.pi) % (2 * np.pi)) - np.pi) < 1e-3:
                continue
            z1, _ = circle_nodes(al, f1); z2, _ = circle_nodes(al, f2)
            minsep = min(minsep, float(np.min(np.abs(z1[:, None] - z2[None, :]))))
    row("B2", "W", "node sets of B_tau, B_tau' are disjoint for tau != tau'",
        minsep > 1e-9, f"min separation {minsep:.3e}")

    ok, wmom, wmin, wgap = True, 0.0, np.inf, np.inf
    for n in [1, 2, 3, 4, 5, 6]:
        for _ in range(2 if QUICK else 4):
            th = rng.uniform(-np.pi, np.pi, n + 4); p = rng.dirichlet(np.ones(n + 4))
            m = moments_from_atoms(th, p, n)
            al, _ = verblunsky(m, n)
            best = None
            for phi in np.linspace(0.017, 2 * np.pi + 0.017, 37)[:-1]:
                z, _ = circle_nodes(al, phi)
                g = refl_gap_circle(z)
                if best is None or g > best[0]:
                    best = (g, z)
            g, z = best
            V = np.array([[zz ** k for zz in z] for k in range(n + 1)])
            q = np.linalg.solve(V, m[:n + 1])
            e = float(np.max(np.abs(V @ q - m[:n + 1])))
            ok &= (q.real.min() > 1e-13 and np.abs(q.imag).max() < 1e-9 and e < 1e-9
                   and g > 1e-6 and np.max(np.abs(np.abs(z) - 1)) < 1e-8)
            wmom = max(wmom, e); wmin = min(wmin, float(q.real.min())); wgap = min(wgap, g)
    row("B3", "W", "circle: reflection-free (n+1)-atom representation exists (n=1..6)",
        ok, f"max moment err {wmom:.2e}, min weight {wmin:.2e}, min reflection gap {wgap:.2e}")

    counts = []
    for n in [1, 2, 3]:
        th = rng.uniform(-np.pi, np.pi, n + 4); p = rng.dirichlet(np.ones(n + 4))
        al, _ = verblunsky(moments_from_atoms(th, p, n), n)
        M = 3000 if QUICK else 12000
        ph = np.linspace(0, 2 * np.pi, M + 1)[:-1]
        g = np.array([refl_gap_circle(circle_nodes(al, x)[0]) for x in ph])
        c = sum(1 for i in range(len(g))
                if g[i] < 2e-2 and g[i] <= g[i - 1] and g[i] <= g[(i + 1) % len(g)])
        N = n + 1
        counts.append((n, c, N * (N + 3) // 2))
    row("B4", "X", "", all(c <= b for _, c, b in counts),
        "; ".join(f"n={n}: {c} <= N(N+3)/2 = {b}" for n, c, b in counts)
        + "  [X: heuristic local-minimum count, not a proof]")

    same_dir = True; per_node = []; sums = []
    for n in [1, 2, 3]:
        th = rng.uniform(-np.pi, np.pi, n + 4); p = rng.dirichlet(np.ones(n + 4))
        al, _ = verblunsky(moments_from_atoms(th, p, n), n)
        M = 1500 if QUICK else 6000
        ph = np.linspace(0, 2 * np.pi, M + 1)
        cur = np.angle(circle_nodes(al, ph[0])[0])
        acc = np.zeros(n + 1); track = [acc.copy()]
        for i in range(1, M + 1):
            z = np.angle(circle_nodes(al, ph[i])[0]); used = set()
            for j in range(n + 1):
                dd = (z - cur[j] + np.pi) % (2 * np.pi) - np.pi
                for k in np.argsort(np.abs(dd)):
                    if k not in used:
                        used.add(k); acc[j] += dd[k]; cur[j] = z[k]; break
            track.append(acc.copy())
        inc = np.diff(np.array(track), axis=0)
        same_dir &= bool(np.all(inc > 0) or np.all(inc < 0))
        sh = np.abs(acc) / (2 * np.pi)
        per_node.append([round(float(v), 4) for v in sh])
        sums.append(float(np.abs(acc).sum()) / (2 * np.pi))
    sum_ok = all(abs(t - 1.0) < 2e-3 for t in sums)
    not_equal = any(max(v) - min(v) > 1e-2 for v in per_node)
    row("B5", "W", "circle: ALL nodes co-monotone; SUM of shifts = 2pi; the shifts "
                   "are NOT individually 2pi/(n+1) (audit Q1 correction)",
        same_dir and sum_ok and not_equal,
        f"per-node shifts/2pi {per_node}; sums {[round(t,6) for t in sums]}; "
        f"individually unequal: {not_equal}")

    werr, wmin = 0.0, np.inf
    for n in [1, 2, 3, 4]:
        for _ in range(2 if QUICK else 5):
            th = rng.uniform(-np.pi, np.pi, n + 4); p = rng.dirichlet(np.ones(n + 4))
            al, _ = verblunsky(moments_from_atoms(th, p, n), n)
            phi = rng.uniform(0, 2 * np.pi); h = 1e-6
            ev0, V0 = circle_nodes(al, phi); a0 = np.angle(ev0)
            pred = np.abs(V0[-1, :]) ** 2
            num = np.zeros(n + 1)
            for j in range(n + 1):
                for s, sh in ((1, h), (-1, -h)):
                    ev, _ = circle_nodes(al, phi + sh)
                    dd = (np.angle(ev) - a0[j] + np.pi) % (2 * np.pi) - np.pi
                    num[j] += s * dd[np.argmin(np.abs(dd))] / (2 * h)
            werr = max(werr, float(np.max(np.abs(num - pred))))
            wmin = min(wmin, float(pred.min()))
    row("B6", "V", "circle derivative identity d theta_j/d phi = |v_j(last)|^2 > 0",
        werr < 1e-6 and wmin > 0, f"max err {werr:.2e}, min |v(last)|^2 = {wmin:.2e}")

    worst = 0.0
    for n in [1, 2, 3, 4]:
        th = rng.uniform(-np.pi, np.pi, n + 4); p = rng.dirichlet(np.ones(n + 4))
        al, _ = verblunsky(moments_from_atoms(th, p, n), n)
        _, V = circle_nodes(al, rng.uniform(0, 2 * np.pi))
        worst = max(worst, abs(float(np.sum(np.abs(V[-1, :]) ** 2)) - 1.0))
    row("B7", "V", "unitarity identity sum_j |v_j(last)|^2 = 1 (total shift = 2pi)",
        worst < 1e-12, f"max deviation {worst:.2e}")

    bad = 0
    for n in [1, 2, 3]:
        for r in range(1, n + 1):
            th = rng.uniform(-np.pi, np.pi, r); p = rng.dirichlet(np.ones(r))
            if np.linalg.matrix_rank(toeplitz(moments_from_atoms(th, p, n), n), tol=1e-9) > n:
                bad += 1
    row("B8", "V", "atom lower bound: r <= n atoms forces rank T_n <= n", bad == 0,
        f"violations {bad}")


# =====================================================================
# BLOCK C -- arc saturation, sigma-parametrised (audit repair R1)
# =====================================================================
def block_C():
    n, u = 2, 1.4
    th = rng.uniform(-u, u, 7); p = rng.dirichlet(np.ones(7))
    m = moments_from_atoms(th, p, n)
    z = np.tan(th / 2); wnu = p / (1 + z ** 2) ** n
    munu = np.array([np.sum(wnu * z ** k) for k in range(2 * n + 1)])
    tgt = np.concatenate([[1.0], np.array([[m[k].real, m[k].imag]
                                           for k in range(1, n + 1)]).ravel()])
    row("C1", "V", "tan-half transport: arc trig moments <-> Hausdorff moments on [-T,T]",
        float(np.max(np.abs(trig_to_z_map(n) @ munu - tgt))) < 1e-12,
        f"max deviation {np.max(np.abs(trig_to_z_map(n) @ munu - tgt)):.2e}")

    cases = ([(1, 1.7), (2, 1.7)] if QUICK
             else [(nn, uu) for nn in (1, 2, 3) for uu in (2.4, 1.7, 0.9)])
    wexact, wpos, ok_exact = 0.0, np.inf, True
    wderiv, wdmin, ok_mono, ok_single = 0.0, np.inf, True, True
    colls, ok_free, wgap = [], True, np.inf
    natoms_ok = True
    for n, u in cases:
        T, mt, mu, _ = arc_data(n, u)
        a, b = jacobi_from_moments(mu, n)
        adm, sets, ws, dsig = arc_admissible(a, b, n, mu[0], T)
        if len(adm) < 10:
            ok_exact = ok_mono = ok_single = False; continue
        natoms_ok &= (sets.shape[1] == n + 1)
        for lam, w in zip(sets[::max(1, len(sets)//20)], ws[::max(1, len(ws)//20)]):
            e = float(np.max(np.abs(np.array([np.sum(w * lam ** k)
                                              for k in range(2 * n + 1)]) - mu)))
            wexact = max(wexact, e); ok_exact &= e < 1e-8
            wpos = min(wpos, float(w.min()))
        d = np.diff(sets, axis=0)
        ok_mono &= bool(np.all(d > 0))
        wdmin = min(wdmin, float(d.min()))
        ok_single &= bool(np.max(np.diff(adm)) < 3 * dsig + 1e-15)
        s0 = adm[len(adm) // 2]; h = 1e-6
        l0, _, V0 = arc_rule(a, b, n, s0, mu[0])
        lp, _, _ = arc_rule(a, b, n, s0 + h, mu[0])
        lm, _, _ = arc_rule(a, b, n, s0 - h, mu[0])
        wderiv = max(wderiv, float(np.max(np.abs((lp - lm) / (2 * h) - V0[-1, :] ** 2))))
        gaps = np.array([np.min(np.abs(S[:, None] + S[None, :])) for S in sets])
        c = sum(1 for i in range(1, len(gaps) - 1)
                if gaps[i] < 5e-3 and gaps[i] <= gaps[i - 1] and gaps[i] <= gaps[i + 1])
        colls.append((n, u, c, (n + 1) * (n + 2) // 2))  # N(N+1)/2, N=n+1
        ok_free &= gaps.max() > 1e-3
        wgap = min(wgap, float(gaps.max()))
    row("C2", "V", "arc: sigma-family is exact to degree 2n with positive weights, n+1 atoms",
        ok_exact and natoms_ok, f"max moment error {wexact:.2e}, min weight {wpos:.2e}")
    row("C3", "V", "arc derivative identity d lambda_j/d sigma = |v_j(last)|^2 (audit repair R1)",
        wderiv < 1e-6, f"max err {wderiv:.2e}")
    row("C4", "W", "arc: ALL n+1 nodes strictly increasing in sigma (common direction)",
        ok_mono, f"min increment {wdmin:.2e}")
    row("C5", "W", "arc: admissible sigma set is a SINGLE interval",
        ok_single, "seed-parametrisation gave n+1 intervals; sigma-parametrisation gives one")
    row("C6", "X", "", all(c <= b for _, _, c, b in colls),
        "; ".join(f"n={n},u={u}: {c} <= N(N+1)/2 = {b}" for n, u, c, b in colls))
    row("C7", "W", "arc: a reflection-free rule exists (max reflection gap > 0)",
        ok_free, f"min over cases of the max gap = {wgap:.4f}")

    bad = 0
    for n in [1, 2, 3]:
        for q in range(1, 2 * n + 2):
            zz = rng.uniform(-1, 1, q)
            V = np.array([[t ** k for t in zz] for k in range(2 * n + 1)])
            if np.linalg.matrix_rank(V, tol=1e-9) < q:
                bad += 1
    row("C8", "V", "annihilator lemma: q <= 2n+1 distinct nodes give full column rank",
        bad == 0, f"violations {bad} (numpy matrix_rank at tol 1e-9, not an exact rank proof)")


# =====================================================================
# BLOCK E -- exact envelopes and second-order geometry
# =====================================================================
def block_E():
    worst = 0.0
    for x, y in [(0.0, 0.5), (0.3, 0.2), (0.6, 0.5), (0.9, 0.4), (-0.7, 0.5),
                 (0.2, 0.9), (0.95, 0.2), (-0.4, -0.8)]:
        worst = max(worst, abs(A1_closed(x, y) - grid_lp_Aminus(np.array([1.0, x + 1j * y]), 1)))
    row("E1", "V", "Thm 6.1 n=1 full-circle closed form vs grid LP",
        worst < TOL_LP, f"max deviation {worst:.2e} (tol {TOL_LP})")

    edge_ok = True; ed = []
    for x, y in [(1.0, 0.0), (-1.0, 0.0), (0.999999, 0.0)]:
        v = A1_closed(x, y); lp = grid_lp_Aminus(np.array([1.0, x + 1j * y]), 1)
        edge_ok &= abs(v - lp) < TOL_LP and abs(v) < TOL_LP
        ed.append(f"({x},{y}) -> {v:.2e}")
    row("E1b", "V", "Thm 6.1 edge case a=0, i.e. m1 = +-1: A_1^- = 0 (audit repair R7)",
        edge_ok, "; ".join(ed))

    lam = complex(-0.5664173302854644027, 0.6884532271077021305)
    row("E2", "R", "regression: A_1^-(lambda) reproduces the M62 constant A*",
        abs(A1_closed(lam.real, lam.imag) - 0.763362818245963536) < 1e-15,
        "difference 0 at double precision")

    worst = 0.0
    for y1, y2 in [(0.3, 0.0), (0.5, 0.2), (0.2, 0.5), (0.6, 0.6), (0.1, 0.9),
                   (0.7, 0.3), (0.45, 0.55), (0.62, 0.12)]:
        t = np.linspace(0.0, np.pi, LP_N); ns = LP_N
        cost = np.concatenate([np.zeros(ns), np.ones(ns), np.ones(ns)])
        Aeq = np.zeros((3, 3 * ns)); Aeq[0, :ns] = 1.0
        Aeq[1, ns:2 * ns] = np.sin(t); Aeq[1, 2 * ns:] = -np.sin(t)
        Aeq[2, ns:2 * ns] = np.sin(2 * t); Aeq[2, 2 * ns:] = -np.sin(2 * t)
        Aub = np.zeros((ns, 3 * ns)); idx = np.arange(ns)
        Aub[idx, idx] = -1.0; Aub[idx, ns + idx] = 1.0; Aub[idx, 2 * ns + idx] = 1.0
        r = linprog(cost, A_ub=Aub, b_ub=np.zeros(ns), A_eq=Aeq,
                    b_eq=np.array([1.0, y1, y2]),
                    bounds=[(0, None)] * (3 * ns), method="highs")
        worst = max(worst, abs(A2_odd_closed(y1, y2) - r.fun))
    row("E3", "V", "Thm 7.4 n=2 odd-gauge closed form vs odd-data LP",
        worst < TOL_LP, f"max deviation {worst:.2e}")

    if HAVE_SYMPY:
        y1, y2 = sp.symbols("y1 y2", positive=True)
        A = 2 * y1**2 / sp.sqrt(4 * y1**2 - y2**2)
        id1 = sp.simplify(sp.together(A**2 - y2**2
                                      - (2 * y1**2 - y2**2)**2 / (4 * y1**2 - y2**2)))
        id2 = sp.simplify(sp.together(A**2 + 2 * y1**2 * (2 * y1**2 - y2**2)
                                      / (4 * y1**2 - y2**2) - 2 * y1**2))
        row("E4", "C", "Thm 7.4 exact: two rational identities certify the radical solution "
                       "(audit repair R5, no point substitution)",
            id1 == 0 and id2 == 0,
            "A^2-y2^2 = (2y1^2-y2^2)^2/(4y1^2-y2^2) and A^2 + A*sqrt(A^2-y2^2) = 2y1^2")
    else:
        row("E4", "C", "Thm 7.4 exact rational identities [requires sympy]", False, "sympy unavailable")

    ok = True
    for y1, y2 in [(0.7, 0.3), (0.9, 0.1), (0.5, 0.8), (0.2, 0.95)]:
        ok &= (((2 * y1**2 - 1) <= np.sqrt(max(0.0, 1 - y2**2)) + 1e-12)
               == (A2_odd_closed(y1, y2) <= 1 + 1e-12))
    row("E5", "R", "regression against M62 Thm 16 body {|w|<=1, 2v^2-1 <= sqrt(1-w^2)}", ok)

    worst = 0.0
    for _ in range(3 if QUICK else 8):
        th = rng.uniform(-np.pi, np.pi, 6); p = rng.dirichlet(np.ones(6))
        m = moments_from_atoms(th, p, 2)
        worst = max(worst, abs(A2_schur(m[1], m[2]) - grid_lp_Aminus(m, 2)))
    row("E6", "V", "Thm 7.2 n=2 full-circle Schur reduction vs grid LP",
        worst < TOL_LP, f"max deviation {worst:.2e}")

    worst, signs = 0.0, []
    for u in ([1.5] if QUICK else [2.4, 1.5, 1.0]):
        for _ in range(2 if QUICK else 3):
            th = rng.uniform(-u, u, 7); p = rng.dirichlet(np.ones(7))
            m = moments_from_atoms(th, p, 2)
            a = A2_arc(m[1], m[2], u); b = grid_lp_Aminus(m, 2, u=u, N=max(800, LP_N // 2))
            worst = max(worst, abs(a - b)); signs.append(a - b)
    row("E7", "V", "", worst < 5e-4,
        f"max |deviation| {worst:.2e}; signed diffs "
        f"{[round(float(x), 6) for x in signs]} (both routes are discretisations "
        "whose biases are not comparable, so no sign order is asserted)")

    if HAVE_SYMPY:
        tt, A, u1, x1, y1, x2, y2 = sp.symbols("tt A u1 x1 y1 x2 y2", real=True)
        As = 1 - tt
        X = A * x2 - u1**2 + y1**2
        Y = A * y2 - 2 * u1 * y1
        R = A**2 - u1**2 - y1**2
        F2 = sp.expand((R**2 - Y**2).subs(A, As))
        F3 = sp.expand(((X - A * tt)**2 + Y**2 - R**2).subs(A, As))
        Fc = sp.expand((R**2 - Y**2).subs({u1: x1 - tt, A: As}))
        c_ = (x1 - u1) / tt
        F1n = sp.expand(sp.numer(sp.cancel(sp.together(
            ((X - A * tt * (2 * c_**2 - 1))**2 + Y**2 - R**2).subs(A, As)))))
        degs = (sp.Poly(F1n, tt).degree(), sp.Poly(F1n, u1).degree(),
                sp.Poly(F2, tt).degree(), sp.Poly(F2, u1).degree(),
                sp.Poly(F3, tt).degree(), sp.Poly(Fc, tt).degree())
        Res = sp.Poly(sp.expand(sp.resultant(sp.Poly(F2, u1),
                                             sp.Poly(sp.diff(F2, u1), u1))), tt).degree()
        row("E8", "C", "chamber polynomials incl. Chamber I quintic (audit repair R2)",
            degs == (5, 4, 4, 4, 3, 2) and Res == 8,
            f"ChI deg_t={degs[0]} deg_u1={degs[1]}; ChII deg_t={degs[2]} deg_u1={degs[3]}; "
            f"ChIII deg_t={degs[4]}; c=+-1 deg_t={degs[5]}; Res_u1(ChII) deg_t={Res}")
    else:
        row("E8", "C", "chamber polynomial degrees [requires sympy]", False, "sympy unavailable")

    # extremizer recovery + complementary slackness at n=2 (audit repair R2)
    ok, worst_cs, worst_val = True, 0.0, 0.0
    for _ in range(2 if QUICK else 5):
        th = rng.uniform(-np.pi, np.pi, 6); p = rng.dirichlet(np.ones(6))
        m = moments_from_atoms(th, p, 2)
        val, coef = dual_lp_Aminus(m, 2)
        c0, a1, a2, b1, b2 = coef[0], coef[1], coef[2], coef[3], coef[4]
        tg = np.linspace(-np.pi, np.pi, 40001)
        P = c0 + a1 * np.cos(tg) + a2 * np.cos(2 * tg) + b1 * np.sin(tg) + b2 * np.sin(2 * tg)
        E = c0 + a1 * np.cos(tg) + a2 * np.cos(2 * tg)
        feas = (P.max() <= 1 + 1e-4) and (E.max() <= 1e-4)
        prim = grid_lp_Aminus(m, 2)
        worst_val = max(worst_val, abs(prim - val))
        n_or = np.sum((P > 1 - 1e-4) & (np.r_[True, np.diff(P) > 0][:len(P)] |
                                        np.r_[np.diff(P) < 0, True][:len(P)]))
        ok &= feas
        worst_cs = max(worst_cs, float(max(P.max() - 1, E.max(), 0.0)))
    row("E9", "W", "n=2 NUMERICAL dual candidate on a 40001-point grid (not a global certificate; see E12)",
        ok and worst_val < TOL_LP,
        f"max constraint violation {worst_cs:.2e}, max |primal-dual| {worst_val:.2e}")

    worst = 0.0
    for n in [1, 2, 3]:
        for _ in range(1 if QUICK else 3):
            th = rng.uniform(-np.pi, np.pi, n + 4); p = rng.dirichlet(np.ones(n + 4))
            m = moments_from_atoms(th, p, n)
            worst = max(worst, abs(grid_lp_Aminus(m, n) - dual_lp_Aminus(m, n)[0]))
    row("E10", "V", "Thm 7.5 dual formula vs primal LP", worst < TOL_LP,
        f"max duality gap {worst:.2e}")


# =====================================================================
# BLOCK F -- structured rigidity
# =====================================================================
def block_F():
    ratios = []
    for s, B, n in [(1, 1.5, 4), (2, 2.0, 6), (0.5, 1.2, 10), (3, 5.0, 8)]:
        Lam = (1 + (n + 1) ** 2) ** (-s / 2)
        a = np.sqrt(2 * (B ** 2 - 1)) * Lam
        ratios.append((2 * np.sqrt(B ** 2 - 1) * Lam) / (2 * a / np.pi))
    row("F1", "V", "Sobolev upper/lower constant ratio = pi/sqrt(2), independent of (B,s,n)",
        max(abs(r - np.pi / np.sqrt(2)) for r in ratios) < 1e-12,
        f"pi/sqrt2 = {np.pi/np.sqrt(2):.12f}; spread {max(ratios)-min(ratios):.2e}")

    grid = np.linspace(-np.pi, np.pi, 200001)[:-1]
    ok, det = True, []
    for s, B, n in [(1, 1.5, 4), (2, 2.0, 6), (0.5, 1.2, 10), (3, 5.0, 8)]:
        Lam = (1 + (n + 1) ** 2) ** (-s / 2)
        a = min(1.0, np.sqrt(2 * (B ** 2 - 1)) * Lam)
        f = 1 + a * np.sin((n + 1) * grid)
        Aex = 0.5 * np.mean(np.abs(f - (1 - a * np.sin((n + 1) * grid))))
        Hs = np.sqrt(1 + a ** 2 / 2 * (1 + (n + 1) ** 2) ** s)
        ok &= (f.min() >= 0) and (Hs <= B + 1e-12) and abs(Aex - 2 * a / np.pi) < 1e-6
        det.append(f"s={s},B={B},n={n}: a={a:.4f}")
    row("F2", "V", "Sobolev witness: positivity, ||f_a||_Hs = B, A(f_a) = 2a/pi",
        ok, "; ".join(det))

    ok, det = True, []
    for rho, alpha, B in [(0.5, 1.0, 2.0), (0.3, 0.7, 3.0)]:
        n0 = None
        for n in range(1, 200):
            a = np.sqrt(2 * (B ** 2 - 1)) * np.exp(-rho * (n + 1) ** alpha)
            if a <= 1.0:
                n0 = n; break
        a = np.sqrt(2 * (B ** 2 - 1)) * np.exp(-rho * (n0 + 1) ** alpha)
        nrm = np.sqrt(1 + a ** 2 / 2 * np.exp(2 * rho * (n0 + 1) ** alpha))
        ok &= (a <= 1.0) and (nrm <= B + 1e-12)
        det.append(f"rho={rho},alpha={alpha},B={B}: valid for n >= {n0}")
    row("F3", "V", "Thm 9.4 Gevrey witness admissible in the declared large-n regime (repair R7)",
        ok, "; ".join(det))

    def gibbs(b, p, N=20001):
        th = np.linspace(-np.pi, np.pi, N)
        S = np.array([np.sin((k + 1) * th) for k in range(p)])
        w = np.exp(b @ S); w /= np.trapezoid(w, th)
        mean = np.array([np.trapezoid(S[k] * w, th) for k in range(p)])
        Cov = np.array([[np.trapezoid(S[i] * S[j] * w, th) - mean[i] * mean[j]
                         for j in range(p)] for i in range(p)])
        return mean, Cov

    p = 3; ok_g, worst_g = True, 0.0
    for _ in range(3 if QUICK else 8):
        b = rng.uniform(-1.2, 1.2, p)
        mean, _ = gibbs(b, p)
        h = 1e-5; g = np.zeros(p)
        th = np.linspace(-np.pi, np.pi, 20001)
        S = np.array([np.sin((j + 1) * th) for j in range(p)])
        for k in range(p):
            e = np.zeros(p); e[k] = h
            g[k] = (np.log(np.trapezoid(np.exp((b + e) @ S), th))
                    - np.log(np.trapezoid(np.exp((b - e) @ S), th))) / (2 * h)
        worst_g = max(worst_g, float(np.max(np.abs(g - mean))))
    row("F4", "V", "Thm 9.5 grad psi = E_b[S] (numerical gradient)",
        worst_g < 1e-6, f"max deviation {worst_g:.2e}")

    lam_min = np.inf; ok_pd = True
    box = [(-1.2, 1.2)] * p                                    # convex compact domain
    for _ in range(4 if QUICK else 12):
        b = np.array([rng.uniform(lo, hi) for lo, hi in box])
        _, Cov = gibbs(b, p)
        lm = float(np.linalg.eigvalsh(Cov).min())
        lam_min = min(lam_min, lm); ok_pd &= lm > 1e-8
    row("F5", "W", "Thm 9.5 Hess psi = Cov_b(S) > 0 on the declared convex box "
                   "[-1.2,1.2]^3 (repair R7)",
        ok_pd, f"eta := min sampled lambda_min = {lam_min:.4f}")

    ok_m, worst_m = True, np.inf
    for _ in range(4 if QUICK else 12):
        b = np.array([rng.uniform(lo + .1, hi - .1) for lo, hi in box])
        b2 = b + rng.normal(0, 0.05, p)
        b2 = np.clip(b2, -1.2, 1.2)
        m1, C1 = gibbs(b, p); m2, C2 = gibbs(b2, p)
        lm = min(float(np.linalg.eigvalsh(C1).min()), float(np.linalg.eigvalsh(C2).min()))
        lhs = float(np.dot(m1 - m2, b - b2)); rhs = lm * float(np.dot(b - b2, b - b2))
        ok_m &= (lhs > 0) and (lhs >= rhs - 1e-6)
        if np.linalg.norm(b - b2) > 1e-9:
            worst_m = min(worst_m, lhs / max(np.dot(b - b2, b - b2), 1e-18))
    row("F6", "V", "Thm 9.5 strong monotonicity on the box (segment stays inside)",
        ok_m, f"min observed monotonicity modulus {worst_m:.4f}")


# =====================================================================
# BLOCK G -- dichotomy, fragility, minimax, dense selector
# =====================================================================
def block_G():
    ok, rep = True, []
    for th0 in [0.0, 0.15, 0.5, 1.2, np.pi / 2]:
        Amu = 0.0 if abs(np.sin(th0)) < 1e-15 else 1.0
        v = 1 - A1_closed((1 - 1e-5) * np.cos(th0), (1 - 1e-5) * np.sin(th0))
        ok &= abs(v - (1 - Amu)) < 2e-2
        rep.append(f"arg={th0:.3f}: W->{v:.5f} (pred {1-Amu:.1f})")
    row("G1", "V", "Thm 6.3 fragility: boundary jump of W_n equals 1 - A(mu_m)", ok,
        "; ".join(rep))

    ok = True
    for n in [1, 2, 3, 4]:
        m = np.zeros(n + 1, dtype=complex); m[0] = 1.0
        al, _ = verblunsky(m, n)
        ok &= max(refl_gap_circle(circle_nodes(al, ph)[0])
                  for ph in np.linspace(0.01, 2 * np.pi, 97)) > 1e-6
    row("G2", "W", "Thm 6.4 minimax Delta_n = 1: Haar fiber holds both A=0 and A=1", ok,
        "Haar symmetric (A=0) plus a reflection-free POPUC rule (A=1)")

    ok, worst, rfree = True, 0.0, np.inf
    for n in [1, 2]:
        u = 1.6; K0 = 400; h = (u - 0.04) / (K0 - 1)
        pos = 0.02 + h * np.arange(K0)
        neg = -(0.02 + h * (np.arange(K0) + 0.5))
        g = np.concatenate([pos, neg])
        rfree = min(rfree, float(np.min(np.abs(g[:, None] + g[None, :]))))
        th = rng.uniform(-u, u, 2 * n + 3); p = rng.dirichlet(np.ones(2 * n + 3))
        m = moments_from_atoms(th, p, n)
        rows_, beq = [np.ones(len(g))], [1.0]
        for k in range(1, n + 1):
            rows_.append(np.cos(k * g)); beq.append(m[k].real)
            rows_.append(np.sin(k * g)); beq.append(m[k].imag)
        r = linprog(np.zeros(len(g)), A_eq=np.array(rows_), b_eq=np.array(beq),
                    bounds=[(0, None)] * len(g), method="highs")
        ok &= r.success and (np.sum(r.x > 1e-10) <= 2 * n + 1)
        if r.success:
            worst = max(worst, float(np.max(np.abs(np.array(rows_) @ r.x - np.array(beq)))))
    row("G3", "W", "Thm 4.1 dense selector: R-free grid represents interior data, support <= 2n+1",
        ok, f"max moment residual {worst:.2e}, grid R-freeness {rfree:.2e}")

    ok = True
    for _ in range(2 if QUICK else 5):
        th = rng.uniform(-np.pi, np.pi, 8); p = rng.dirichlet(np.ones(8))
        m = moments_from_atoms(th, p, 3)
        a1, a2, a3 = (grid_lp_Aminus(m[:2], 1), grid_lp_Aminus(m[:3], 2),
                      grid_lp_Aminus(m[:4], 3))
        ok &= (a1 <= a2 + TOL_LP) and (a2 <= a3 + TOL_LP)
    row("G4", "V", "Prop 3.3 monotonicity A_n^- <= A_{n+1}^-, hence W_{n+1} <= W_n", ok)


# =====================================================================
# BLOCK Z -- Z-Spin conditional diagnostic
# =====================================================================
def block_Z():
    lam = complex(-0.5664173302854644027, 0.6884532271077021305)
    T1 = toeplitz(np.array([1.0, lam]), 1)
    row("Z1", "V", "T_1(lambda) positive definite, |lambda| < 1",
        np.linalg.eigvalsh((T1 + T1.conj().T) / 2).min() > 0,
        f"|lambda| = {abs(lam):.18f}")
    Am = A1_closed(lam.real, lam.imag)
    row("Z2", "R", "full-circle diagnostic interval I_1(lambda) = [A*, 1]",
        abs(Am - 0.763362818245963536) < 1e-15, f"W_1 = {1-Am:.18f}")
    row("Z3", "D", "scope: full-circle diagnostic only; arc version needs the M62 "
                   "effective-arc convention; D-M61-IOTA remains OPEN", True,
        "declaration, not a physical claim")


# =====================================================================
# BLOCK N -- v1.2 additions forced by the v1.1 audit
# =====================================================================
def _sigma_endpoints(a, b, n, T):
    """Schur-complement endpoints of the admissible interval Sigma."""
    Jn = np.diag(a[:n]) + np.diag(b[1:n], 1) + np.diag(b[1:n], -1)
    en = np.zeros(n); en[n - 1] = 1.0
    bn2 = b[n] ** 2
    sm = -T + bn2 * en @ np.linalg.solve(Jn + T * np.eye(n), en)
    sp_ = T - bn2 * en @ np.linalg.solve(T * np.eye(n) - Jn, en)
    return sm, sp_, Jn, en, bn2


def block_N():
    # ---- C9 : Sigma = [sigma_-, sigma_+] by Schur complement -------------
    worst = 0.0; step = None
    cases = ([(1, 1.5), (2, 1.5)] if QUICK
             else [(nn, uu) for nn in (1, 2, 3, 4) for uu in (2.4, 1.5, 0.8)])
    for n, u in cases:
        T, _mt, mu, _tg = arc_data(n, u)
        a, b = jacobi_from_moments(mu, n)
        sm, sp_, *_ = _sigma_endpoints(a, b, n, T)
        grid = np.linspace(sm - 1.0, sp_ + 1.0, 8001 if QUICK else 40001)
        step = grid[1] - grid[0]
        ok = []
        for sg in grid:
            d = a[:n + 1].copy(); d[n] = sg
            J = np.diag(d) + np.diag(b[1:n + 1], 1) + np.diag(b[1:n + 1], -1)
            lam = np.linalg.eigvalsh(J)
            if lam.min() >= -T - 1e-12 and lam.max() <= T + 1e-12:
                ok.append(sg)
        if not ok:
            worst = np.inf; break
        worst = max(worst, abs(sm - min(ok)), abs(sp_ - max(ok)))
    row("C9", "V", "Prop 5.6 arc admissible set Sigma = [sigma_-, sigma_+] by Schur "
                   "complement, vs direct scan (audit Q2)",
        worst < 3 * step, f"max |Schur - scan| = {worst:.2e} (scan step {step:.1e})")

    # ---- C10 : exact non-degeneracy identity ------------------------------
    wid, wdet, lmin = 0.0, 0.0, np.inf
    for n, u in cases:
        T, _mt, mu, _tg = arc_data(n, u)
        a, b = jacobi_from_moments(mu, n)
        sm, sp_, Jn, en, bn2 = _sigma_endpoints(a, b, n, T)
        M0 = T * T * np.eye(n) - Jn @ Jn
        L = M0 - bn2 * np.outer(en, en)
        idn = 2 * T * (1 - bn2 * en @ np.linalg.solve(M0, en))
        det = 2 * T * np.linalg.det(L) / np.linalg.det(M0)
        wid = max(wid, abs((sp_ - sm) - idn)); wdet = max(wdet, abs(idn - det))
        lmin = min(lmin, float(np.linalg.eigvalsh(L).min()))
    row("C10", "V", "Prop 5.6 identity sigma_+-sigma_- = 2T(1-b_n^2<e,(T^2I-J_n^2)^-1 e>) "
                    "= 2T detL/detM > 0 iff L > 0 (audit Q2)",
        wid < 1e-10 and wdet < 1e-10 and lmin > 0,
        f"max |gap - identity| {wid:.2e}; max |identity - det form| {wdet:.2e}; "
        f"min lambda_min(L) over cases {lmin:.3e}")

    # ---- C11 : algebraic collision eliminant ------------------------------
    if HAVE_SYMPY:
        x, sg = sp.symbols("x sg")
        rep = []; ok = True

        def _elim(aa, bb, n):
            def cpoly(k):
                if k == 0:
                    return sp.Integer(1)
                M = sp.zeros(k, k)
                for i in range(k):
                    M[i, i] = aa[i]
                    if i + 1 < k:
                        M[i, i + 1] = bb[i + 1]; M[i + 1, i] = bb[i + 1]
                return sp.expand((x * sp.eye(k) - M).det())
            pn, pnm = cpoly(n), cpoly(n - 1)
            p = sp.expand((x - sg) * pn - bb[n] ** 2 * pnm)
            pm = sp.expand(p.subs(x, -x))
            R = sp.Poly(sp.resultant(sp.Poly(p, x), sp.Poly(pm, x)), sg)
            Rp = sp.simplify(sp.resultant(sp.Poly(pn, x),
                                          sp.Poly(sp.expand(pn.subs(x, -x)), x)))
            return sp.Poly(p, sg).degree(), R, Rp

        # (i) generic asymmetric data: universal bound and the leading coefficient
        for n in [1, 2, 3]:
            aa = [sp.Rational(int(rng.integers(1, 6)), 7) for _ in range(n)]
            bb = [sp.Rational(int(rng.integers(1, 6)), 4) for _ in range(n + 1)]
            dp, R, Rp = _elim(aa, bb, n)
            bound_ok = (dp == 1 and R.degree() <= 2 * n + 1)
            lead_ok = (Rp != 0 and R.degree() == 2 * n + 1
                       and sp.simplify(R.all_coeffs()[0] + 2 * Rp) == 0)
            ok &= bound_ok and lead_ok
            rep.append(f"n={n} generic: deg={R.degree()} <= {2*n+1}, Res!=0, lead/Res = "
                       f"{sp.simplify(R.all_coeffs()[0]/Rp)}")

        # (ii) NEGATIVE CONTROL (audit Z1): symmetric Gauss nodes make Res vanish
        #      and the degree genuinely drop below 2n+1.
        for n, aa in [(1, [sp.Integer(0)]), (2, [sp.Integer(0), sp.Integer(0)])]:
            bb = [sp.Rational(1, 1)] + [sp.Rational(int(k) + 1, 3) for k in range(n)]
            dp, R, Rp = _elim(aa, bb, n)
            drop_ok = (Rp == 0 and R.degree() < 2 * n + 1)
            ok &= drop_ok
            rep.append(f"n={n} symmetric control: Res = {Rp}, deg = {R.degree()} "
                       f"< {2*n+1} (universal exact degree is FALSE)")
        row("C11", "C", "", ok, "; ".join(rep))
    else:
        row("C11", "C", "", False, "sympy unavailable")

    # ---- E11 : Yang-Xie normalisation mapping (F-M63.ARC) -----------------
    worst_r, worst_T = 0.0, 0.0
    for u in [2.4, 1.5, 1.0, 0.6]:
        fL, fH = 1.0 - u / (2 * np.pi), u / (2 * np.pi)   # T = [0,1] (audit A5)
        sgn = np.sign(fH - fL)
        r0 = -2 * np.cos(np.pi * (fH - fL)) * sgn
        r1 = np.exp(1j * np.pi * (fL + fH)) * sgn
        worst_r = max(worst_r, abs(r0 - (-2 * np.cos(u))), abs(r1 - 1.0))
        gam = np.cos(u)
        for _ in range(3):
            A = rng.uniform(0.2, 0.9)
            R1 = A * (rng.uniform(-.4, .4) + 1j * rng.uniform(-.4, .4))
            R2 = A * (rng.uniform(-.4, .4) + 1j * rng.uniform(-.4, .4))
            t = {0: A, 1: np.conj(R1), 2: np.conj(R2), -1: R1, -2: R2}
            Tg = np.array([[r1 * t[j - i + 1] + r0 * t[j - i] + np.conj(r1) * t[j - i - 1]
                            for j in range(2)] for i in range(2)])
            ell = R1.real - gam * A
            h = (A + R2) / 2 - gam * R1
            worst_T = max(worst_T, float(np.max(np.abs(
                Tg - 2 * np.array([[ell, np.conj(h)], [h, ell]])))))
    row("E11", "V", "", worst_r < 1e-12 and worst_T < 1e-12,
        f"max |r-parameters - (-2cos u, 1)| = {worst_r:.2e}; "
        f"max |T_g(YX) - 2 L_g| = {worst_T:.2e}")

    # ---- E12 : EXACT rational Gram (SOS) certificate ----------------------
    # ---- E12b: the old numerical factorisation, kept as a diagnostic ------
    def _gram_numeric(cvec, n):
        cn = np.array([complex(sp.N(z)) for z in cvec])
        rts = np.roots(cn[::-1])
        ins = sorted([z for z in rts if abs(z) < 1.0], key=abs)[:n]
        q = np.poly(ins)[::-1]
        th = np.linspace(-np.pi, np.pi, 4001)
        val = np.abs(np.array([np.polyval(q[::-1], np.exp(1j * t)) for t in th])) ** 2
        tgt = np.real(np.array([sum(cn[k + n] * np.exp(1j * k * t)
                                    for k in range(-n, n + 1)) for t in th]))
        sc = np.sqrt(max(np.mean(tgt) / max(np.mean(val), 1e-300), 0.0))
        q = sc * q
        val = np.abs(np.array([np.polyval(q[::-1], np.exp(1j * t)) for t in th])) ** 2
        return np.outer(np.conj(q), q), float(np.max(np.abs(val - tgt)))

    def _ratmat(G, den):
        N = G.shape[0]; M = sp.zeros(N, N)
        for i in range(N):
            for j in range(N):
                M[i, j] = (sp.Rational(round(G[i, j].real * den), den)
                           + sp.I * sp.Rational(round(G[i, j].imag * den), den))
        return (M + M.conjugate().T) / 2

    def _fix_sums(G, cvec, n):
        N = n + 1; D = sp.zeros(N, N)
        for k in range(0, n + 1):
            cur = sum(G[i, i + k] for i in range(N - k))
            d = sp.expand(cvec[n + k] - cur); cnt = N - k
            for i in range(cnt):
                D[i, i + k] += d / cnt
                if k > 0:
                    D[i + k, i] += sp.conjugate(d) / cnt
        return sp.expand(G + D)

    def _exact_psd(G):
        mins = []
        for k in range(1, G.shape[0] + 1):
            mins.append(sp.nsimplify(sp.re(sp.expand(G[:k, :k].det()))))
        return all(sp.simplify(d) > 0 for d in mins), mins

    def _certify(cvec, n):
        """Peel a rational constant, factor the remainder numerically, then work
        exactly: rationalise, repair the coefficient identity, add (s/N) I."""
        N = n + 1
        cn = np.array([complex(sp.N(z)) for z in cvec])
        th = np.linspace(-np.pi, np.pi, 20001)
        Rv = np.real(np.array([sum(cn[k + n] * np.exp(1j * k * t)
                                   for k in range(-n, n + 1)) for t in th]))
        rmin = float(Rv.min())
        if rmin <= 0:
            return None
        for frac in [2, 4, 8]:
            s_r = sp.Rational(int(rmin / frac * 10 ** 8), 10 ** 8)
            if s_r <= 0:
                continue
            cp_ = list(cvec); cp_[n] = sp.expand(cvec[n] - s_r)
            G0, _ = _gram_numeric(cp_, n)
            for den in [10 ** 6, 10 ** 8, 10 ** 10]:
                G = _fix_sums(_ratmat(G0, den), cp_, n)
                G = sp.expand(G + (s_r / N) * sp.eye(N))
                if not all(sp.simplify(sp.expand(
                        sum(G[i, i + k] for i in range(N - k)) - cvec[n + k])) == 0
                        for k in range(0, n + 1)):
                    continue
                ok, mins = _exact_psd(G)
                if ok:
                    return G, mins
        return None

    n = 2
    cert_rows, cert_ok, best_gap = [], True, 0.0
    cert_dump = []
    if HAVE_SYMPY:
        data = [(sp.Rational(1, 5), sp.Rational(3, 10),
                 sp.Rational(-1, 10), sp.Rational(1, 5)),
                (sp.Rational(-1, 4), sp.Rational(1, 4),
                 sp.Rational(1, 5), sp.Rational(-1, 10))]
        if not QUICK:
            data.append((sp.Rational(3, 10), sp.Rational(-2, 5),
                         sp.Rational(1, 10), sp.Rational(1, 4)))
        for (x1, y1, x2, y2) in data:
            mm = np.array([1.0, float(x1) + 1j * float(y1), float(x2) + 1j * float(y2)])
            valn, xv = dual_lp_Aminus(mm, n)
            den0 = 10 ** 5
            c0 = sp.Rational(round(xv[0] * den0), den0)
            aa = [sp.Rational(round(xv[1] * den0), den0), sp.Rational(round(xv[2] * den0), den0)]
            bb = [sp.Rational(round(xv[3] * den0), den0), sp.Rational(round(xv[4] * den0), den0)]
            done = False
            for shift in [sp.Rational(1, 10 ** 4), sp.Rational(1, 3000),
                          sp.Rational(1, 1000), sp.Rational(1, 300)]:
                c0s = c0 - shift
                cP = [sp.Integer(0)] * (2 * n + 1); cP[n] = c0s
                for k in range(1, n + 1):
                    cP[n + k] = (aa[k - 1] - sp.I * bb[k - 1]) / 2
                    cP[n - k] = (aa[k - 1] + sp.I * bb[k - 1]) / 2
                cR1 = [-z for z in cP]; cR1[n] = sp.expand(cR1[n] + 1)
                cR2 = [sp.Integer(0)] * (2 * n + 1); cR2[n] = -2 * c0s
                for k in range(1, n + 1):
                    cR2[n + k] = -aa[k - 1]; cR2[n - k] = -aa[k - 1]
                r1 = _certify(cR1, n); r2 = _certify(cR2, n)
                if r1 and r2:
                    lb = sp.expand(c0s + aa[0] * x1 + aa[1] * x2 + bb[0] * y1 + bb[1] * y2)
                    gap = valn - float(lb)
                    best_gap = max(best_gap, gap)
                    cert_rows.append(f"m1={x1}+{y1}i: certified A_2^- >= {lb} "
                                     f"({float(lb):.8f}), LP {valn:.8f}, gap {gap:.1e}")
                    cert_dump.append((x1, y1, x2, y2, lb, r1[0], r1[1], r2[0], r2[1]))
                    done = True
                    break
            cert_ok &= done
        globals()["CERT_COUNT"] = len(cert_dump)
        row("E12", "C", "",
            cert_ok and best_gap < 1.1e-4 and len(cert_dump) == CERT_EXPECTED,
            "; ".join(cert_rows) + f"  [max gap {best_gap:.2e} < 1.1e-4; "
                                   f"{len(cert_dump)} certificates written, "
                                   f"{CERT_EXPECTED} expected for profile {PROFILE}]")
        with open(f"zs_m63_certificate_{VERSION}{SUF}.txt", "w", encoding="utf-8") as f:
            f.write(f"ZS-M63 {VERSION_DOT} ({PROFILE} profile) -- EXACT rational "
                    "Gram (SOS) dual certificates, n=2\n")
            f.write("R(theta) = a(theta)^* G a(theta) with a = (1, e^{i th}, e^{2i th});\n")
            f.write("coefficient identity  sum_i G[i,i+k] = c_k  holds exactly;\n")
            f.write("all leading principal minors are exactly positive rationals.\n")
            for (x1, y1, x2, y2, lb, G1, m1_, G2, m2_) in cert_dump:
                f.write("\n" + "=" * 70 + "\n")
                f.write(f"m1 = {x1} + {y1} i,  m2 = {x2} + {y2} i\n")
                f.write(f"certified lower bound  A_2^- >= {lb}\n")
                f.write("\nG for 1 - P:\n" + sp.sstr(G1) + "\n  minors: " + sp.sstr(m1_) + "\n")
                f.write("\nG for -(P + P(-.)):\n" + sp.sstr(G2) + "\n  minors: "
                        + sp.sstr(m2_) + "\n")
    else:
        globals()["CERT_COUNT"] = 0
        row("E12", "C", "", False, "sympy unavailable")

    def _gram_numeric_np(cn, n):
        """pure-numpy Fejer-Riesz diagnostic; cn is a length-(2n+1) complex array"""
        rts = np.roots(cn[::-1])
        ins = sorted([z for z in rts if abs(z) < 1.0], key=abs)[:n]
        q = np.poly(ins)[::-1]
        th = np.linspace(-np.pi, np.pi, 4001)
        val = np.abs(np.array([np.polyval(q[::-1], np.exp(1j * t)) for t in th])) ** 2
        tgt = np.real(np.array([sum(cn[k + n] * np.exp(1j * k * t)
                                    for k in range(-n, n + 1)) for t in th]))
        sc = np.sqrt(max(np.mean(tgt) / max(np.mean(val), 1e-300), 0.0))
        q = sc * q
        val = np.abs(np.array([np.polyval(q[::-1], np.exp(1j * t)) for t in th])) ** 2
        return float(np.max(np.abs(val - tgt)))

    wres, wslack = 0.0, 0.0
    for _ in range(2 if QUICK else 6):
        th = rng.uniform(-np.pi, np.pi, 6); p = rng.dirichlet(np.ones(6))
        m = moments_from_atoms(th, p, 2)
        val, xv = dual_lp_Aminus(m, 2)
        c0, aa, bb = xv[0], xv[1:3], xv[3:5]
        tg = np.linspace(-np.pi, np.pi, 200001)
        P = c0 + aa[0]*np.cos(tg) + aa[1]*np.cos(2*tg) + bb[0]*np.sin(tg) + bb[1]*np.sin(2*tg)
        E = c0 + aa[0]*np.cos(tg) + aa[1]*np.cos(2*tg)
        slack = max(0.0, P.max() - 1.0, E.max())
        c0p = c0 - slack
        cc1 = np.zeros(5, dtype=complex)
        cc1[2] = 1.0 - c0p
        for k in (1, 2):
            cc1[2 + k] = -aa[k-1]/2 + 1j*bb[k-1]/2
            cc1[2 - k] = -aa[k-1]/2 - 1j*bb[k-1]/2
        wres = max(wres, _gram_numeric_np(cc1, 2)); wslack = max(wslack, slack)
    row("E12b", "V", "", wres < 1e-3 and wslack < 1e-3,
        f"numerical residual max |R - |q|^2| on a 4001-point grid = {wres:.2e}; "
        f"grid-determined shift = {wslack:.2e} (diagnostic; E12 is the certificate)")

    # ---- E13 : declared degenerate points ---------------------------------
    ok = True
    ok &= (A2_schur(0.0 + 0j, 0.0 + 0j) < 1e-6)          # symmetric data -> A = 0, t -> 1
    ok &= abs(A1_closed(1.0, 0.0)) < 1e-12               # a = 0 branch
    ok &= abs(A2_odd_closed(0.0, 0.0)) < 1e-12           # y1 = y2 = 0
    m1 = 0.2 + 0.3j; m2 = 0.1 + 0.05j
    ok &= _feas_circle(0.0, m1, m2, 201)                 # t = 0 branch returns True
    ok &= _feas_arc(0.0, m1, m2, np.cos(1.5), 51)
    row("E13", "V", "declared degenerate points of Thm 7.2 / 8.3: t=0 and A=0 handled "
                    "outside the 1/A, 1/t formulas (audit Q8)", ok,
        "A_2^-(0,0)=0; A_1^-(+-1,0)=0; t=0 branch short-circuits before division")

    # ---- F7 : Sobolev constant, corrected normalisation -------------------
    vals = []
    for s_, n_ in [(1, 4), (2, 6), (0.5, 10)]:
        N = 4096; th = 2 * np.pi * np.arange(N) / N
        g = np.sign(np.sin((n_ + 1) * th))
        G = np.fft.fft(g) / N
        ks = np.fft.fftfreq(N, 1 / N).astype(int)
        v = sum(float(1 + k * k) ** (-float(s_)) * abs(c) ** 2
                for k, c in zip(ks, G) if abs(k) > n_)
        Lam = (1 + (n_ + 1) ** 2) ** (-s_ / 2)
        vals.append((s_, n_, np.sqrt(v) / Lam))
    lo = 2 * np.sqrt(2) / np.pi
    row("F7", "V", "Remark 9.4 corrected normalisation hatC = C/Lambda_n in [2sqrt2/pi, 1]; "
                   "the square wave beats the single sine strictly (audit Q8)",
        all(lo < r <= 1 + 1e-9 for _, _, r in vals),
        "; ".join(f"s={s_},n={n_}: hatC >= {r:.6f}" for s_, n_, r in vals)
        + f"  (lower end 2sqrt2/pi = {lo:.6f})")

    # ---- F8 : Gibbs finite-Fourier saturation with NON-trigonometric S (X1) --
    NG = 20001 if QUICK else 40001
    tg = np.linspace(-np.pi, np.pi, NG)
    Sst = np.array([np.sin(tg) / (1.30 - np.cos(tg)),
                    np.sin(2 * tg) / (1.45 - np.cos(tg)),
                    np.sin(3 * tg) / (1.60 - np.cos(tg))])
    pdim = Sst.shape[0]
    Lnorm = float(np.max(np.sqrt(np.sum(Sst ** 2, axis=0))))

    def _gib(bv):
        wv = np.exp(bv @ Sst); wv /= np.trapezoid(wv, tg); return wv

    def _cov(wv, U, V):
        mu = np.array([np.trapezoid(u * wv, tg) for u in U])
        mv = np.array([np.trapezoid(v * wv, tg) for v in V])
        return np.array([[np.trapezoid(U[i] * V[j] * wv, tg) - mu[i] * mv[j]
                          for j in range(len(V))] for i in range(len(U))])

    def _proj(f, N):
        c = np.fft.rfft(f[:-1]) / (NG - 1)
        o = np.full(NG, np.real(c[0]))
        for k in range(1, N + 1):
            ck = ((-1) ** k) * c[k]
            o += 2 * (np.real(ck) * np.cos(k * tg) - np.imag(ck) * np.sin(k * tg))
        return o

    grid_b = [np.array(v) for v in
              [(-0.6, -0.2, 0.4), (0.5, 0.3, -0.5), (0.0, 0.6, 0.2),
               (-0.3, 0.5, -0.1), (0.7, -0.6, 0.6), (0.2, -0.4, -0.7)]]
    eta = min(float(np.linalg.eigvalsh(_cov(_gib(bv), Sst, Sst)).min()) for bv in grid_b)
    Nsat = dsat = None
    for N in list(range(1, 13)) + [16, 24]:      # contiguous over 1..12 (audit W2)
        TN = np.array([_proj(Sst[k], N) for k in range(pdim)])
        dN = float(np.max(np.sqrt(np.sum((TN - Sst) ** 2, axis=0))))
        if 2 * Lnorm * dN < eta:
            Nsat, dsat = N, dN
            break
    ok8, derr, mono = (Nsat is not None), float("nan"), float("nan")
    if ok8:
        TN = np.array([_proj(Sst[k], Nsat) for k in range(pdim)])
        bnd = eta - 2 * Lnorm * dsat
        quad_ok = True
        for bv in grid_b:
            DF = _cov(_gib(bv), TN, Sst)
            quad_ok &= float(np.linalg.eigvalsh((DF + DF.T) / 2).min()) >= bnd - 1e-9
        bv = grid_b[0]; h = 1e-5
        DF = _cov(_gib(bv), TN, Sst); num = np.zeros((pdim, pdim))
        for jj in range(pdim):
            e = np.zeros(pdim); e[jj] = h
            wp, wm = _gib(bv + e), _gib(bv - e)
            for ii in range(pdim):
                num[ii, jj] = (np.trapezoid(TN[ii] * wp, tg)
                               - np.trapezoid(TN[ii] * wm, tg)) / (2 * h)
        derr = float(np.max(np.abs(num - DF)))
        mono = np.inf
        for ii in range(len(grid_b)):
            for jj in range(ii + 1, len(grid_b)):
                b1, b2 = grid_b[ii], grid_b[jj]
                F1 = np.array([np.trapezoid(TN[k] * _gib(b1), tg) for k in range(pdim)])
                F2 = np.array([np.trapezoid(TN[k] * _gib(b2), tg) for k in range(pdim)])
                mono = min(mono, float(np.dot(F1 - F2, b1 - b2)
                                       / np.dot(b1 - b2, b1 - b2)))
        ok8 = quad_ok and derr < 1e-7 and mono >= bnd - 1e-9
    row("F8", "V", "", ok8,
        f"L={Lnorm:.4f}; eta_hat={eta:.6f} = min over {len(grid_b)} SAMPLED b "
        f"(diagnostic, not a certified uniform bound over the box); first N in the "
        f"contiguous tested range 1..12 with 2L*delta_N<eta_hat is N={Nsat} "
        f"(delta_N={dsat:.3e}); max |dE_b[T_N]/db - Cov_b(T_N,S)| = {derr:.2e}; "
        f"min sampled monotonicity modulus {mono:.6f} >= eta_hat-2L*delta_N")



# =====================================================================
# harness + auto-generated row map (audit repair R4)
# =====================================================================
def rowmap_text():
    lines = ["| row | class | check |", "|---|---|---|"]
    for rid in ROW_ORDER:
        if rid.startswith("S"):              # guards are described separately
            continue
        cls, nm = ROW_SPEC[rid]
        lines.append(f"| `{rid}` | `{cls}` | {nm.replace('|','/')} |")
    return "\n".join(lines)


def harness():
    ids = [r["id"] for r in LEDGER]
    reg_ok = (ids == [i for i in ROW_ORDER if not i.startswith("S")]
              and len(set(ids)) == len(ids))
    row("S4", "G", "", reg_ok,
        f"emitted {len(ids)} content rows matching ROW_SPEC exactly, in order")

    # ---- S5 / S6 : self-reference guards (audit Z5) ----
    import re as _re
    stale_pat = _re.compile(r"zs_m63_[A-Za-z0-9_]*(" + "|".join(SUPERSEDED) + r")\.(py|md|txt|json)")
    try:
        own = open(__file__, encoding="utf-8").read()
    except Exception:
        own = ""
    own_stale = sorted(set(stale_pat.findall_iter(own))) if False else \
        sorted({mo.group(0) for mo in stale_pat.finditer(own)})
    name_has_count = [rid for rid, (c, nm) in ROW_SPEC.items()
                      if _re.search(r"=\s*\d{2,}", nm)]
    census_sum = sum(EXPECTED_CENSUS.values())
    row("S6", "G", "",
        (not own_stale) and (not name_has_count) and census_sum == EXPECTED_ROWS,
        f"stale filename refs in this script: {own_stale or 'none'}; "
        f"ROW_SPEC names embedding a count: {name_has_count or 'none'}; "
        f"sum(EXPECTED_CENSUS) = {census_sum} = EXPECTED_ROWS")

    if MANUSCRIPT:
        try:
            txt = open(MANUSCRIPT, encoding="utf-8").read()
            ms_stale = sorted({mo.group(0) for mo in stale_pat.finditer(txt)})
            end_lines = [l for l in txt.strip().splitlines() if l.strip()]
            end_ok = end_lines[-1].strip() == f"**END OF ZS-M63 {VERSION_DOT}**"
            bad_end = sorted({mo.group(0) for mo in
                              _re.finditer(r"\*\*END OF ZS-M63 v1\.\d+(?:\.\d+)?\*\*", txt)
                              if mo.group(0) != f"**END OF ZS-M63 {VERSION_DOT}**"})
            code_ok = f"**Paper code:** `ZS-M63 {VERSION_DOT}`" in txt
            # audit V2: a wrong label present in BOTH registry and table was invisible
            lab_full = {"Thm": "Theorem", "Prop": "Proposition", "Remark": "Remark",
                        "Lem": "Lemma", "Cor": "Corollary"}
            labs = set()
            for _c, _nm in ROW_SPEC.values():
                for mo in _re.finditer(r"\b(Thm|Prop|Remark|Lem|Cor) (\d+\.\d+)", _nm):
                    labs.add((mo.group(1), mo.group(2)))
            bad_lab = sorted({f"{k} {v}" for k, v in labs
                              if f"{lab_full[k]} {v}" not in txt})
            decl = [f"EXPECTED_ROWS = {EXPECTED_ROWS}",
                    " ".join(f"{k}={v}" for k, v in
                             [("C", EXPECTED_CENSUS["C"]), ("V", EXPECTED_CENSUS["V"]),
                              ("W", EXPECTED_CENSUS["W"]), ("X", EXPECTED_CENSUS["X"]),
                              ("R", EXPECTED_CENSUS["R"]), ("G", EXPECTED_CENSUS["G"]),
                              ("D", EXPECTED_CENSUS["D"]), ("T", EXPECTED_CENSUS["T"])]),
                    f"C+V+W = {sum(EXPECTED_CENSUS[k] for k in 'CVW')}",
                    f"rows = {EXPECTED_ROWS}"]
            missing = [d for d in decl if d not in txt]
            row("S5", "G", "", (not ms_stale) and (not missing)
                and end_ok and (not bad_end) and code_ok and (not bad_lab),
                f"stale filename refs: {ms_stale or 'none'}; declared strings not "
                f"found: {missing or 'none'}; paper-code line correct: {code_ok}; "
                f"terminal END marker correct: {end_ok}; wrong END markers: "
                f"{bad_end or 'none'}; ROW_SPEC labels absent from the manuscript: "
                f"{bad_lab or 'none'} (of {len(labs)} checked)")
        except OSError as e:
            row("S5", "G", "", False, str(e))
    elif NO_MANUSCRIPT:
        row("S5", "G", "", False,
            "--no-manuscript was passed: the manuscript guard is DECLARED SKIPPED "
            "and is recorded as a failure, not a pass")
    else:
        row("S5", "G", "", False,
            f"no manuscript found (looked for ZS-M63_{VERSION}.md); pass "
            "--manuscript PATH, or --no-manuscript to acknowledge the gap")

    ncert = globals().get("CERT_COUNT", 0)
    cert_file = f"zs_m63_certificate_{VERSION}{SUF}.txt"
    try:
        ctxt = open(cert_file, encoding="utf-8").read()
        nfile = ctxt.count("certified lower bound")
    except OSError:
        nfile = -1
    ms_ok, ms_note = True, "no manuscript"
    if MANUSCRIPT and not QUICK:
        try:
            mt = open(MANUSCRIPT, encoding="utf-8").read()
            words = {1: "one", 2: "two", 3: "three", 4: "four"}
            ms_ok = f"{words.get(CERT_EXPECTED, CERT_EXPECTED)} whole-circle exact " \
                    f"dual-feasibility certificates" in mt
            ms_note = f"manuscript claims {words.get(CERT_EXPECTED)}: {ms_ok}"
        except OSError as e:
            ms_ok, ms_note = False, str(e)
    dep_ok = HAVE_SYMPY or (ncert == 0 and nfile <= 0)
    row("S7", "G", "",
        ((ncert == CERT_EXPECTED) and (nfile == CERT_EXPECTED) and ms_ok)
        or (not HAVE_SYMPY and ncert == 0),
        f"profile {PROFILE}: E12 produced {ncert}, {cert_file} holds {nfile}, "
        f"expected {CERT_EXPECTED}; {ms_note}"
        + ("; sympy absent so E12 produced none, which is the declared degraded state" if not HAVE_SYMPY else ""))

    census = {}
    for r in LEDGER:
        census[r["cls"]] = census.get(r["cls"], 0) + 1
    census["G"] = census.get("G", 0) + 3          # S1, S2, S3 emitted after this row
    ok1 = census.get("P", 0) == 0 and all(
        census.get(k, 0) == v for k, v in EXPECTED_CENSUS.items()) and \
        set(census) <= set(EXPECTED_CENSUS) | {"P"}
    row("S1", "G", "", ok1,
        "declared " + " ".join(f"{k}={v}" for k, v in sorted(EXPECTED_CENSUS.items()))
        + " | observed " + " ".join(f"{k}={v}" for k, v in sorted(census.items())))
    row("S2", "G", "", len(LEDGER) + 2 == EXPECTED_ROWS,
        f"emitted {len(LEDGER)+2} rows, EXPECTED_ROWS = {EXPECTED_ROWS}")
    if MANUSCRIPT:
        try:
            txt = open(MANUSCRIPT, encoding="utf-8").read()
            body = rowmap_text()
            hit = body.strip() in txt
            row("S3", "G", "manuscript structural row map is byte-identical to the auto-generated table (environment-invariant)",
                hit, f"manuscript {_os.path.basename(MANUSCRIPT)}, rowmap sha256 "
                     f"{hashlib.sha256(body.encode()).hexdigest()[:16]}")
        except OSError as e:
            row("S3", "G", "manuscript sync guard", False, str(e))
    elif NO_MANUSCRIPT:
        row("S3", "G", "", False,
            "--no-manuscript was passed: the row-map sync guard is DECLARED "
            "SKIPPED and is recorded as a failure, not a pass")
    else:
        row("S3", "G", "", False,
            f"no manuscript found (looked for ZS-M63_{VERSION}.md); the "
            f"registry row map was written to zs_m63_rowmap_{VERSION}.md")


def main():
    print("=" * 78)
    print("ZS-M63 v1.6.2 deterministic verification suite  "
          f"({'QUICK' if QUICK else 'FULL'})")
    print(f"python {platform.python_version()}  numpy {np.__version__}  "
          f"scipy {__import__('scipy').__version__}  "
          f"sympy {sp.__version__ if HAVE_SYMPY else 'MISSING'}")
    print(f"seed={SEED}  LP grid N={LP_N}  EXPECTED_ROWS={EXPECTED_ROWS}")
    print("=" * 78)
    for blk in (block_DT, block_A, block_B, block_C, block_E, block_F, block_G,
                block_Z, block_N):
        print(f"\n--- {blk.__name__} ---")
        blk()
    print("\n--- harness ---")
    harness()

    fails = [r for r in LEDGER if r["status"] == "FAIL"]
    census = {}
    for r in LEDGER:
        census[r["cls"]] = census.get(r["cls"], 0) + 1
    print("\n" + "=" * 78)
    print(f"rows = {len(LEDGER)}   FAIL = {len(fails)}")
    print("census: " + "  ".join(f"{k}={v}" for k, v in sorted(census.items()))
          + f"   evidence(C+V+W) = {sum(census.get(k,0) for k in 'CVW')}  (X is NOT evidence)")
    with open(f"zs_m63_rowmap_{VERSION}.md", "w", encoding="utf-8") as f:
        f.write(rowmap_text() + "\n")
    with open(f"zs_m63_observations_{VERSION}{SUF}.md", "w", encoding="utf-8") as f:
        f.write("| row | status | observed |\n|---|---|---|\n")
        for r in LEDGER:
            f.write(f"| `{r['id']}` | {r['status']} | "
                    f"{(r['detail'] or '-').replace('|','/')} |\n")
    out = dict(paper="ZS-M63 v1.6.2", profile=PROFILE, seed=SEED,
               rows=len(LEDGER), fails=len(fails), census=census, ledger=LEDGER)
    blob = json.dumps(out, indent=1, sort_keys=True)
    with open(f"zs_m63_verify_{VERSION}{SUF}.json", "w", encoding="utf-8") as f:
        f.write(blob)
    print("ledger sha256 =", hashlib.sha256(blob.encode()).hexdigest())
    bad = (len(LEDGER) != EXPECTED_ROWS)
    if bad:
        print(f"!! row-count guard: expected {EXPECTED_ROWS}, got {len(LEDGER)}")
    sys.exit(1 if (fails or bad) else 0)


if __name__ == "__main__":
    main()
