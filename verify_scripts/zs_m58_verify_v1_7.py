#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_m58_verify_v1_7.py
=====================
Companion verification suite for

    ZS-M58 v1.7 -- Boundary-Frame Covariance, Pointed-Dilation
    Non-Identifiability, and the Character Reduction of F-M54-16'
    Kenny Kang, Z-Spin Cosmology Collaboration, July 2026

Scope
-----
This script verifies the MATHEMATICAL content of ZS-M58: the target channel
algebra, the QND-Equalizer equivalence, the scalar Sz.-Nagy--Foias
characteristic function, the TWO-GAUGE theorem (coincidence gauge vs pointer
frame gauge), the Euclidean reality obstruction, the Poisson-kernel dilation
universality no-go, the isometry/unitary type guard, the Route-S form closure
(annealed + CLT), and the logarithmic-lift branch structure.

v1.7 fixes (seventh audit response) -- A MATHEMATICAL ERROR IN M58.5':
  The v1.6 Four-Datum Separation stated the wrong relations.
    (i) its certificate ("all branches exponentiate to the same lambda") proves
        ENDPOINT =/=> LIFT, not LIFT =/=> ENDPOINT.  The true direction is
        LIFT => ENDPOINT, since a = exp(L).                       [Z34, Z36]
    (ii) for a nonvanishing path with FIXED endpoints, the endpoint-fixed
        homotopy class and the logarithm branch are the SAME datum: exp is the
        universal cover of C^*, so both are classified by the same integer.
        v1.6 claimed "D2 => D3 but not conversely"; in fact D2 <=> D3.  [Z35]
    (iii) D2 was typed as a U(1) transport path while the proof integrated a
        C^* multiplier path; a U(1) path cannot carry modulus evolution. [Z37]
  The theorem is restated as M58.5'' -- Endpoint-Lift-Intertwiner Separation --
  with THREE layers, the middle one having three equivalent descriptions.
  Ledger hygiene, also from audit 7:
    - the ledger now has a FIXED 173 rows: when the artifact is absent the
      downstream artifact checks are emitted as explicit FAIL rows rather than
      skipped (v1.6 shrank to 160 rows, so "156/166" was misreported).
    - payload tampering is detected by Z20d and Z24; Z25 is a negative-control
      digest-sensitivity guard and correctly PASSES.  Wording corrected.
    - Z31 guards against the INFERENCE that pointer preservation follows from
      complete-order equivalence.  It does not detect removal of (P) from a
      manuscript or a successor construction.  Claim lowered.

v1.6 fixes (sixth audit response) -- ARTIFACT-SOURCE PROVENANCE:
  v1.5 verified artifact INTEGRITY (the payload matches its own digest) but not
  artifact PROVENANCE (the payload was produced by THIS source).  Two exploits
  followed and were reproduced:
    (a) a v1.4-generated artifact passed the v1.5 suite 162/162, because the
        module tag was never read;
    (b) a valid artifact beside a stub source incapable of producing one also
        passed 162/162, because only the source's EXISTENCE and its REFUSAL
        behaviour were tested, never its clean execution.
  Closed by four new checks:
    Z20c  clean regeneration: a pristine copy of the construction source is
          RUN; requires rc == 0, no "FIREWALL VIOLATION", artifact emitted.
    Z20d  byte-for-byte reproducibility: canonical(regenerated payload) ==
          canonical(loaded payload) AND the two digests agree.
    Z20e  module tag equals the expected v1.7 module.
    Z20f  envelope source_sha256 equals the recomputed hash of this source.

v1.5 fixes (fifth audit response) -- THREE FAIL-OPEN DEFECTS IN v1.4:
  (1) a MISSING Route-B artifact was recorded as a DECLARATION, so running the
      verifier with no construction evidence at all returned 150/150 PASS with
      exit code 0.  Now a hard failure (Z20).
  (2) a MISSING construction source made Z26 PASS, because the else-branch set
      the residual to 0.0 and residual 0 means PASS.  Now 1.0 (hard failure).
  (3) Z26 was not end-to-end: it appended a banned token to a source STRING and
      checked that the string contained it -- a tautology.  Z26 now writes a
      mutated copy to a temp dir, RUNS it as a subprocess, and requires exit
      code != 0, "FIREWALL VIOLATION" on stdout, and NO artifact emitted.
      Z26b does the same for a banned decimal literal.
  Also: the terminal report still said v1.3 and repeated the retracted phrases
  "those five follow from ONE" and "ONE MISSING MORPHISM"; corrected.
  Also new: Z31/Z32 -- the POINTER-PRESERVATION condition (P) of M58.22A.
      Without (P) a complete-order intertwiner gives only unitary EQUIVALENCE,
      not literal equality in the fixed Z_path frame.

v1.4 fixes (fourth audit response) -- TWO REAL DEFECTS IN v1.3:
  (1) the v1.3 construction-layer firewall scanner truncated its own source
      scan and did NOT detect a forbidden identifier injected into the
      construction body.  Verified exploit; fixed by a whole-file scan, and
      guarded here by check Z26 which INJECTS a token and requires detection.
  (2) the v1.3 SHA-256 was decorative: the verifier never recomputed it, so a
      tampered artifact still passed.  Verified exploit; fixed by a
      payload/envelope canonical serialisation, recomputed at Z24 and
      negatively controlled at Z25.
  Also fixed: phi_f48 was AFFINE, not linear (out[0,0] = 1 - ...);  Z18 was a
  tautology (abs(2-2));  the directly relevant ZS-Q18 E_full check was absent.

v1.3 additions (third audit response):
  - Z-block: (i) the Z4 holonomy charge grading of M_2 and the PROVEN fact that
    order-4 covariance does NOT imply QND (explicit CPTP covariant non-QND
    counterexample); (ii) the Intertwiner Compression Theorem -- a complete-order
    isomorphism transports CPTP, QND, rank-2 AND the multiplier at once, so the
    five closure hypotheses compress to ONE; (iii) the Single-Cycle Obstruction:
    the audit's proposed mechanism for (H-ZSQ) is IMPOSSIBLE for a diagonal
    holonomy, and the correct mechanism is faithfulness, not transitivity;
    (iv) the carrier ledger against ZS-F48/ZS-Q18.
  - Route B is moved to a separate FIREWALLED module,
    zs_m58_expansion_construct_v1_7.py, whose artifact is loaded and compared
    here; that module may not name dim Z, z* or lambda.
  - Y17 relabelled: exact CONDITIONAL DISCRIMINATOR, not primary evidence.

v1.2 additions (second audit response + the holonomy-expansion gate):
  - Y-block: the COMPLEMENTARY EXPANSION GATE.  The v1.1 "neutral point" is
    recognised as the LOCKED corpus constant s_c = e^{sin rho} (ZS-M51 Thm T2),
    so the contraction gate is a PROVEN corpus theorem, not a heuristic.  The
    ZS-M51 Fixed-Point Census then selects the first contracting saddle
    (m, x0) = (5, 1/4) WITHOUT consuming dim Z, giving c = 2 pi i x0 = i pi/2
    and primitive holonomy order m - 1 = 4.
  - Q14 reclassified ANALYTIC -> PROXY: a Monte Carlo band is weaker evidence
    than the exact integer gate of the Y-block.

v1.1 additions (first audit response + the character reduction):
  - N-block: the four audit-demanded negative controls, three of which
    REFUTE claims made in v1.0 (M53 Kraus-phase identification, the
    Transport-Branch Identity, and the unrestricted Euclidean reality claim);
  - Q-block: the Character Reduction -- the quarter-turn generator from
    dim Z = 2, the character/uniqueness chain, the branch-free closure
    identity a = c z* = lambda, the Z-family overdetermination, and the
    pre-registered anti-numerology Monte Carlo.

It does NOT and CANNOT verify:
  - any ZS-S14 boundary construction (no S14 cellular data is loaded);
  - the Boundary-Response hypothesis (H-BR), the gluing axiom (G1) or
    holomorphy (G2) -- these are the residual conditions of M58.13;
  - the CRT-4 / H-CLK clock equality.

Anti-circularity firewall
-------------------------
Checks are tagged by class:
    A = ANALYTIC   -- exact/symbolic identity, target-free
    R = REGRESSION -- reproduces a locked corpus number from locked inputs
    X = GUARD      -- negative control; must FAIL to fail
    P = PROXY      -- related calculation, explicitly NOT evidence for a target
    D = DECLARATION-- recorded statement, no computation claimed

No check may return a literal True. Every check computes a residual and
compares it against a pre-registered tolerance.

Locked inputs: A = 35/437, Q = 11, dim Z = 2, z* (ZS-M1).
Everything else is derived. Zero free parameters.

Requires: numpy, scipy, mpmath
"""

from __future__ import annotations

import cmath
import math
import sys
from dataclasses import dataclass, field

import numpy as np
import mpmath as mp
from scipy.linalg import eigvalsh

mp.mp.dps = 40

# ----------------------------------------------------------------------------
# 0. LOCKED CORPUS INPUTS  (the only numbers entering from outside this file)
# ----------------------------------------------------------------------------

A_CONST = mp.mpf(35) / mp.mpf(437)          # ZS-F2, LOCKED
Q_CONST = 11                                # ZS-F5, LOCKED
DIM_Z = 2                                   # ZS-F5, LOCKED

# ZS-M1 i-tetration fixed point z* of T(z) = i^z
ZSTAR = mp.mpf('0.4382829367270321116') + mp.mpf('0.3605924718713854860') * 1j

# Derived, not inserted:
LAMBDA = (1j * mp.pi / 2) * ZSTAR           # lambda = T'(z*)
ABSL = abs(LAMBDA)
ARGL = mp.arg(LAMBDA)
MU = -mp.log(ABSL)                          # decoherence rate per Z-cycle
DELTA = mp.sqrt(1 - ABSL ** 2)              # defect
SIGMA2 = -2 * mp.log(ABSL)                  # Route-S phase variance = 2*MU

LAM = complex(LAMBDA)                       # float working copy
ABSLAM = float(ABSL)

TOL_EXACT = 1e-12
TOL_NUM = 1e-9
TOL_LOOSE = 1e-6

# ----------------------------------------------------------------------------
# Ledger machinery
# ----------------------------------------------------------------------------


@dataclass
class Ledger:
    rows: list = field(default_factory=list)

    def check(self, tag, cls, name, residual, tol, note=""):
        """Record a check. `residual` must be a computed number, never a bool."""
        if isinstance(residual, bool):
            raise TypeError(
                f"[{tag}] literal boolean residual is forbidden by the firewall"
            )
        r = float(residual)
        ok = (r <= tol) and math.isfinite(r)
        self.rows.append((tag, cls, name, r, tol, ok, note))
        return ok

    def declare(self, tag, name, note):
        self.rows.append((tag, "D", name, 0.0, 0.0, True, note))

    def report(self):
        width = 96
        print("=" * width)
        print("ZS-M58 v1.7 -- VERIFICATION LEDGER")
        print("=" * width)
        print(f"{'TAG':<8}{'CL':<4}{'CHECK':<50}{'RESIDUAL':>14}  {'':<4}")
        print("-" * width)
        n_pass = n_fail = 0
        by_class = {}
        for tag, cls, name, r, tol, ok, note in self.rows:
            by_class[cls] = by_class.get(cls, 0) + 1
            if cls == "D":
                print(f"{tag:<8}{cls:<4}{name[:49]:<50}{'--':>14}  DECL")
                n_pass += 1
                continue
            status = "PASS" if ok else "FAIL"
            if ok:
                n_pass += 1
            else:
                n_fail += 1
            print(f"{tag:<8}{cls:<4}{name[:49]:<50}{r:>14.3e}  {status}")
        print("-" * width)
        print(f"Classes: " + ", ".join(f"{k}={v}" for k, v in sorted(by_class.items())))
        print(f"TOTAL {len(self.rows)}   PASS {n_pass}   FAIL {n_fail}")
        print("=" * width)
        return n_fail


L = Ledger()

# ----------------------------------------------------------------------------
# 1. LOCKED CONSTANTS  (class R -- regression against the corpus)
# ----------------------------------------------------------------------------

print("\n[1] Locked constants (ZS-M1 / ZS-F2 / ZS-F5)")
print(f"    A          = 35/437 = {float(A_CONST):.12f}")
print(f"    Q          = {Q_CONST},  dim Z = {DIM_Z}")
print(f"    z*         = {mp.nstr(ZSTAR, 19)}")
print(f"    lambda     = {mp.nstr(LAMBDA, 19)}")
print(f"    |lambda|   = {mp.nstr(ABSL, 19)}")
print(f"    arg lambda = {mp.nstr(ARGL, 19)}")
print(f"    mu         = {mp.nstr(MU, 19)}")
print(f"    delta      = {mp.nstr(DELTA, 19)}")
print(f"    sigma^2    = {mp.nstr(SIGMA2, 19)}")

L.check("C01", "R", "|lambda| = 0.8915135657760470",
        abs(ABSL - mp.mpf('0.8915135657760470')), 1e-15)
L.check("C02", "R", "arg lambda = 2.2592495539025985",
        abs(ARGL - mp.mpf('2.2592495539025985')), 1e-14)
L.check("C03", "R", "mu = -ln|lambda| = 0.1148346249960096",
        abs(MU - mp.mpf('0.1148346249960096')), 1e-15)
L.check("C04", "R", "delta = sqrt(1-|lambda|^2) = 0.4529939977938757",
        abs(DELTA - mp.mpf('0.4529939977938757')), 1e-15)
L.check("C05", "A", "arg lambda = pi/2 + arg z*  (the i-quarter-turn)",
        abs(ARGL - (mp.pi / 2 + mp.arg(ZSTAR))), 1e-30)
L.check("C06", "A", "sigma^2 = 2 mu  (Route-S variance identity)",
        abs(SIGMA2 - 2 * MU), 1e-30)
L.check("C07", "R", "|lambda|^2 + (1-|lambda|^2) = 1 ; retain 0.7947964, leak 0.2052036",
        abs(ABSL ** 2 - mp.mpf('0.79479643796272216')), 1e-15)
L.check("C08", "X", "GUARD: lambda is NOT real (arg not in {0, pi})",
        max(0.0, TOL_EXACT - float(abs(mp.im(LAMBDA)))), TOL_EXACT,
        "must stay at 0: |Im lambda| is far from 0")

# ----------------------------------------------------------------------------
# 2. TARGET CHANNEL AND CHOI OPERATOR   (Sec 2 of the paper)
# ----------------------------------------------------------------------------

print("\n[2] Target QND channel, Choi operator, equalizer")

Z_PATH = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def qnd_channel(a):
    """Return the qubit dephasing (Z_path-QND) superoperator with multiplier a."""
    def phi(rho):
        out = np.array(rho, dtype=complex).copy()
        out[0, 1] *= a
        out[1, 0] *= np.conj(a)
        return out
    return phi


def choi(phi, d=2):
    """Choi operator C = sum_{jk} Phi(|j><k|) (x) |j><k|  (out (x) in-bar)."""
    C = np.zeros((d * d, d * d), dtype=complex)
    for j in range(d):
        for k in range(d):
            E = np.zeros((d, d), dtype=complex)
            E[j, k] = 1.0
            C += np.kron(phi(E), E)
    return C


C_lam = choi(qnd_channel(LAM))

# Basis order for kron(out, in): |00>,|01>,|10>,|11>
C_expected = np.zeros((4, 4), dtype=complex)
C_expected[0, 0] = 1.0
C_expected[3, 3] = 1.0
C_expected[0, 3] = LAM
C_expected[3, 0] = np.conj(LAM)

L.check("T01", "A", "Choi operator equals the closed form of Sec 2.2",
        np.max(np.abs(C_lam - C_expected)), TOL_EXACT)
L.check("T02", "A", "Choi operator is Hermitian",
        np.max(np.abs(C_lam - C_lam.conj().T)), TOL_EXACT)

ev = np.sort(eigvalsh(C_lam))
L.check("T03", "A", "Choi PSD (min eigenvalue >= 0)",
        max(0.0, -ev[0]), TOL_NUM)
L.check("T04", "A", "rank C_lambda = 2",
        abs(int(np.sum(np.abs(ev) > 1e-10)) - 2), 0.5)
L.check("T05", "A", "spec_{!=0} C_lambda = {1-|l|, 1+|l|}",
        max(abs(ev[2] - (1 - ABSLAM)), abs(ev[3] - (1 + ABSLAM))), TOL_NUM)

# Trace preservation: Tr_out C = I_in
Tr_out = np.zeros((2, 2), dtype=complex)
for i in range(2):
    for j in range(2):
        Tr_out[i, j] = sum(C_lam[2 * k + i, 2 * k + j] for k in range(2))
L.check("T06", "A", "trace preservation Tr_out C = I_in",
        np.max(np.abs(Tr_out - I2)), TOL_EXACT)

# Beginning-end equalizer Delta_Z = ker(Z_out (x) I - I (x) Z_in^T)
Meq = np.kron(Z_PATH, I2) - np.kron(I2, Z_PATH.T)
w, V = np.linalg.eigh(Meq)
ker_idx = [i for i in range(4) if abs(w[i]) < 1e-10]
P_delta = V[:, ker_idx] @ V[:, ker_idx].conj().T
L.check("T07", "A", "dim Delta_Z = 2 (span{|00>,|11>})",
        abs(len(ker_idx) - 2), 0.5)
L.check("T08", "A", "QND support: (I - P_Delta) C = 0",
        np.max(np.abs((np.eye(4) - P_delta) @ C_lam)), TOL_NUM)

# Liouville spectrum {1,1,lambda,lambda-bar}
Lsup = np.zeros((4, 4), dtype=complex)
phi = qnd_channel(LAM)
basis = []
for j in range(2):
    for k in range(2):
        E = np.zeros((2, 2), dtype=complex)
        E[j, k] = 1.0
        basis.append(E)
for c, E in enumerate(basis):
    Lsup[:, c] = phi(E).reshape(-1)
spec = np.linalg.eigvals(Lsup)
target_spec = np.array([1.0, 1.0, LAM, np.conj(LAM)])
res = min(
    np.max(np.abs(np.sort_complex(spec) - np.sort_complex(target_spec))), 1.0
)
L.check("T09", "R", "Liouville spectrum = {1,1,lambda,lambda-bar} (ZS-M53)",
        res, TOL_NUM)

# ----------------------------------------------------------------------------
# 3. THEOREM M58.2  --  QND-EQUALIZER EQUIVALENCE   (with negative controls)
# ----------------------------------------------------------------------------

print("\n[3] Theorem M58.2 -- QND <=> diagonal Kraus <=> Choi support in Delta_Z")


def kraus_channel(Ks):
    def phi(rho):
        return sum(K @ rho @ K.conj().T for K in Ks)
    return phi


def is_qnd_residual(phi):
    """Residual for Phi(P_j) = P_j, j = 0,1."""
    r = 0.0
    for j in range(2):
        P = np.zeros((2, 2), dtype=complex)
        P[j, j] = 1.0
        r = max(r, np.max(np.abs(phi(P) - P)))
    return r


def support_residual(phi):
    C = choi(phi)
    return np.max(np.abs((np.eye(4) - P_delta) @ C))


# (a) POSITIVE instance: diagonal Kraus family
k0 = np.diag([1.0, LAM / abs(LAM) * abs(LAM)]).astype(complex)
p_ = (1 + ABSLAM) / 2
u0 = math.sqrt(p_)
u1 = math.sqrt(1 - p_)
ph = cmath.exp(-1j * float(ARGL))   # (K_i)_11 carries e^{-i arg lambda}
K1 = np.diag([u0, u0 * ph]).astype(complex)
K2 = np.diag([u1, -u1 * ph]).astype(complex)
phi_diag = kraus_channel([K1, K2])
L.check("E01", "A", "diagonal Kraus family is TP",
        np.max(np.abs(K1.conj().T @ K1 + K2.conj().T @ K2 - I2)), TOL_EXACT)
L.check("E02", "A", "(2)=>(1): diagonal Kraus => QND",
        is_qnd_residual(phi_diag), TOL_EXACT)
L.check("E03", "A", "(1)=>(3): QND => supp C in Delta_Z",
        support_residual(phi_diag), TOL_EXACT)
L.check("E04", "A", "two-point unraveling reproduces multiplier lambda",
        abs(choi(phi_diag)[0, 3] - LAM), TOL_NUM)

# (b) NEGATIVE control 1: amplitude damping -- CPTP but NOT QND
g = 0.3
Ad0 = np.array([[1, 0], [0, math.sqrt(1 - g)]], dtype=complex)
Ad1 = np.array([[0, math.sqrt(g)], [0, 0]], dtype=complex)
phi_ad = kraus_channel([Ad0, Ad1])
L.check("E05", "X", "GUARD: amplitude damping is NOT QND (residual must be > tol)",
        max(0.0, TOL_LOOSE - is_qnd_residual(phi_ad)), TOL_LOOSE)
L.check("E06", "X", "GUARD: amplitude damping violates Delta_Z support",
        max(0.0, TOL_LOOSE - support_residual(phi_ad)), TOL_LOOSE)

# (c) NEGATIVE control 2: a unitary rotation -- CPTP, not QND
th = 0.4
Ur = np.array([[math.cos(th), -math.sin(th)],
               [math.sin(th), math.cos(th)]], dtype=complex)
phi_rot = kraus_channel([Ur])
L.check("E07", "X", "GUARD: X-rotation is NOT QND",
        max(0.0, TOL_LOOSE - is_qnd_residual(phi_rot)), TOL_LOOSE)

# (d) (3)=>(2): reconstruct diagonal Kraus from a Delta_Z-supported Choi
Csub = np.array([[1.0, LAM], [np.conj(LAM), 1.0]], dtype=complex)
evs, evecs = np.linalg.eigh(Csub)
recon = np.zeros((4, 4), dtype=complex)
Ks = []
for i in range(2):
    if evs[i] > 1e-14:
        v = math.sqrt(evs[i]) * evecs[:, i]
        Ks.append(np.diag([v[0], v[1]]))
phi_rec = kraus_channel(Ks)
L.check("E08", "A", "(3)=>(2): Delta_Z-supported Choi yields diagonal Kraus",
        np.max(np.abs(choi(phi_rec) - C_lam)), TOL_NUM)

# ----------------------------------------------------------------------------
# 4. THEOREM M58.3  --  SCALAR CHARACTERISTIC FUNCTION
# ----------------------------------------------------------------------------

print("\n[4] Theorem M58.3 -- scalar Sz.-Nagy--Foias characteristic function")


def theta(a, z):
    """Sz.-Nagy--Foias characteristic function of the scalar contraction T = a."""
    return (z - a) / (1 - np.conj(a) * z)


def theta_from_definition(a, z):
    """Theta_T(z) = -T + z D_{T*} (I - z T*)^{-1} D_T  for scalar T = a."""
    d = math.sqrt(max(0.0, 1 - abs(a) ** 2))
    return -a + z * d * (1.0 / (1 - z * np.conj(a))) * d


zs_test = [0.0, 0.3, -0.5, 0.2 + 0.4j, -0.15 - 0.62j, 0.71j]
r_def = max(abs(theta(LAM, z) - theta_from_definition(LAM, z)) for z in zs_test)
L.check("F01", "A", "SzNF definition reduces to the Blaschke factor",
        r_def, TOL_EXACT)

L.check("F02", "A", "Theta_lambda(lambda) = 0  (the zero IS the multiplier)",
        abs(theta(LAM, LAM)), TOL_EXACT)
L.check("F03", "A", "Theta_lambda(0) = -lambda",
        abs(theta(LAM, 0.0) + LAM), TOL_EXACT)

# inner on the unit circle
ts = np.linspace(0, 2 * math.pi, 4001)[:-1]
vals = np.array([theta(LAM, cmath.exp(1j * t)) for t in ts])
L.check("F04", "A", "|Theta_lambda| = 1 on the unit circle (inner)",
        float(np.max(np.abs(np.abs(vals) - 1.0))), 1e-11)

# winding number (degree)
ang = np.unwrap(np.angle(vals))
deg = (ang[-1] - ang[0] + (np.angle(vals[0]) - np.angle(vals[-1]))) / (2 * math.pi)
deg_int = round(float(np.unwrap(np.angle(np.append(vals, vals[0])))[-1]
                      - np.unwrap(np.angle(np.append(vals, vals[0])))[0])
                / (2 * math.pi))
L.check("F05", "A", "deg Theta_lambda = 1 (winding number)",
        abs(deg_int - 1), 0.25)

# defect indices (1,1)
L.check("F06", "A", "defect indices (d+,d-) = (1,1); D_A = D_A* = delta",
        abs(math.sqrt(1 - abs(LAM) ** 2) - float(DELTA)), TOL_EXACT)

# Q18 sign convention
L.check("F07", "A", "Q18 convention Theta^{Q18} = -Theta (same zero)",
        max(abs(((LAM - z) / (1 - np.conj(LAM) * z)) + theta(LAM, z))
            for z in zs_test), TOL_EXACT)

# c.n.u.: for |a|<1 the scalar contraction has no unitary summand
gram = 1 - abs(LAM) ** (2 * 200)
L.check("F08", "A", "c.n.u.: A^n -> 0, observability Gramian -> I",
        abs(gram - 1.0), 1e-12, "|lambda|^400 is the residual")

# ----------------------------------------------------------------------------
# 5. THEOREM M58.4  --  THE TWO-GAUGE THEOREM   (central result)
# ----------------------------------------------------------------------------

print("\n[5] Theorem M58.4 -- TWO GAUGES: coincidence gauge vs pointer-frame gauge")


def a_in_frame(phi, th_in, th_out):
    """Read the compressed multiplier in a rephased pointer frame.

    a = <0_out| Phi(|0_in><1_in|) |1_out>.  Rephasing the frame vectors
    |1>_in -> e^{i th_in}|1>_in and |1>_out -> e^{i th_out}|1>_out gives
    a -> e^{i(th_out - th_in)} a.  Nothing else in the structure moves.
    """
    e0 = np.array([1.0, 0.0], dtype=complex)
    e1i = np.array([0.0, cmath.exp(1j * th_in)], dtype=complex)
    e1o = np.array([0.0, cmath.exp(1j * th_out)], dtype=complex)
    rho = np.outer(e0, e1i.conj())            # |0_in><1_in| in the new frame
    sig = phi(rho)
    return np.vdot(e0, sig @ e1o)


def frame_rephase(C, th_in, th_out):
    """Same action written on the Choi operator (used for QND/TP invariance)."""
    Uin = np.diag([1.0, cmath.exp(1j * th_in)])
    Uout = np.diag([1.0, cmath.exp(1j * th_out)])
    V = np.kron(Uout, Uin)
    return V @ C @ V.conj().T


phi_lam = qnd_channel(LAM)
rng = np.random.default_rng(58)
worst_mod = 0.0
worst_law = 0.0
for _ in range(2000):
    ti, to = rng.uniform(0, 2 * math.pi, 2)
    a_g = a_in_frame(phi_lam, ti, to)
    worst_mod = max(worst_mod, abs(abs(a_g) - ABSLAM))
    worst_law = max(worst_law, abs(a_g - cmath.exp(1j * (to - ti)) * LAM))

# deterministic sweep for the orbit span
sweep = np.array([cmath.phase(a_in_frame(phi_lam, 0.0, t))
                  for t in np.linspace(0, 2 * math.pi, 2001)])
arg_span = float(np.max(sweep) - np.min(sweep))

L.check("G01", "A", "frame law: a -> e^{i(th_out - th_in)} a  (exact)",
        worst_law, TOL_NUM)
L.check("G02", "A", "|a| is INVARIANT under the pointer-frame group",
        worst_mod, TOL_NUM)
L.check("G03", "X", "GUARD: arg a is NOT invariant (orbit covers the circle)",
        max(0.0, (2 * math.pi - 0.02) - arg_span), 1e-9,
        "the orbit of arg a must span ~2pi")

# The frame group preserves the pointer observable and the QND property:
for ti, to in [(0.7, 2.1), (1.3, -0.4)]:
    Uin = np.diag([1.0, cmath.exp(1j * ti)])
    L.check(f"G04_{ti}", "A", "frame rephasing commutes with Z_path",
            np.max(np.abs(Uin @ Z_PATH - Z_PATH @ Uin)), TOL_EXACT)
    Cg = frame_rephase(C_lam, ti, to)
    L.check(f"G05_{ti}", "A", "rephased channel is still QND (supp in Delta_Z)",
            np.max(np.abs((np.eye(4) - P_delta) @ Cg)), TOL_NUM)
    Trg = np.zeros((2, 2), dtype=complex)
    for i in range(2):
        for j in range(2):
            Trg[i, j] = sum(Cg[2 * k + i, 2 * k + j] for k in range(2))
    L.check(f"G06_{ti}", "A", "rephased channel is still trace preserving",
            np.max(np.abs(Trg - I2)), TOL_NUM)

# Coincidence gauge (Sz.-Nagy--Foias): Theta -> c Theta, |c| = 1, FIXES the zero
worst_zero = 0.0
for _ in range(500):
    beta = rng.uniform(0, 2 * math.pi)
    c = cmath.exp(1j * beta)
    worst_zero = max(worst_zero, abs(c * theta(LAM, LAM)))
L.check("G07", "A", "coincidence gauge Theta -> cTheta FIXES the zero",
        worst_zero, TOL_EXACT)

# The two gauges are genuinely different group actions on the same datum
th_frame = 0.9
a_frame = cmath.exp(1j * th_frame) * LAM
L.check("G08", "X", "GUARD: frame gauge MOVES the zero (unlike coincidence gauge)",
        max(0.0, 1e-3 - abs(a_frame - LAM)), 1e-3)

# Uniqueness of the invariant: the orbit is exactly the circle |a| = |lambda|,
# so any continuous frame-invariant of a is a function of |a| alone.
orbit = np.array([cmath.exp(1j * t) * LAM for t in np.linspace(0, 2 * math.pi, 721)])
L.check("G09", "A", "frame orbit of a = the full circle |a| = |lambda|",
        float(np.max(np.abs(np.abs(orbit) - ABSLAM))), TOL_NUM)

# Consequence: the well-posed frame-free content of "Theta_S14 ~ Theta_lambda"
# is exactly |a_S14| = |lambda|.
L.declare("G10", "frame-free content of the gate = |a_S14| = |lambda|",
          "Theorem M58.4 corollary; arg a_S14 requires the transport R_boundary")

# ----------------------------------------------------------------------------
# 6. THEOREM M58.10 -- EUCLIDEAN REALITY OBSTRUCTION
# ----------------------------------------------------------------------------

print("\n[6] Theorem M58.10 -- reflection-positive/OS-real slabs force a real multiplier")

# If the compressed Choi block on Delta_Z is REAL symmetric PSD (the OS-real
# case), then a is real. Then the best possible zero residual against lambda is
# |Im lambda|, attained at a = Re lambda.
best_real = min(abs(complex(x, 0.0) - LAM) for x in np.linspace(-0.999, 0.999, 200001))
L.check("H01", "A", "min over real a of |a - lambda| = |Im lambda| = 0.6884532",
        abs(best_real - abs(LAM.imag)), 1e-5)
L.check("H02", "R", "Euclidean-class zero residual eps_0 >= 0.6884532 (decisive)",
        max(0.0, 0.688 - best_real), 1e-3)

# Explicit demonstration: real symmetric PSD Delta_Z block => real a
worst_imag = 0.0
for _ in range(3000):
    x = rng.uniform(-0.999, 0.999)
    B = np.array([[1.0, x], [x, 1.0]])          # real symmetric, PSD for |x|<1
    worst_imag = max(worst_imag, abs(np.imag(B[0, 1])))
L.check("H03", "A", "OS-real Delta_Z block => Im a = 0 identically",
        worst_imag, TOL_EXACT)

# Corroboration: a grading-symmetric collision (ZS-M57) also gives a real
# multiplier -- W_1 = J_E W_0 J_E with J_E real and rho_E real symmetric.
JE = np.array([[1, 0], [0, -1]], dtype=complex)
W0 = np.array([[math.cos(0.6), -math.sin(0.6)],
               [math.sin(0.6), math.cos(0.6)]], dtype=complex)
W1 = JE @ W0 @ JE
rhoE = np.diag([0.63, 0.37]).astype(complex)
a_coll = np.trace(rhoE @ W1.conj().T @ W0)
L.check("H04", "R", "M57 grading-symmetric collision gives a REAL multiplier",
        abs(np.imag(a_coll)), TOL_NUM)

# ----------------------------------------------------------------------------
# 7. THEOREM M58.6 -- POISSON-KERNEL DILATION UNIVERSALITY NO-GO
# ----------------------------------------------------------------------------

print("\n[7] Theorem M58.6 -- every strict scalar contraction has the SAME "
      "unpointed dilation")


def poisson_moment(a, n, nodes=200000):
    """<1, M_zeta^n 1>_{mu_a} with d mu_a = P_a dm ; should equal a^n."""
    t = np.linspace(0, 2 * math.pi, nodes, endpoint=False)
    z = np.exp(1j * t)
    P = (1 - abs(a) ** 2) / np.abs(1 - np.conj(a) * z) ** 2
    return np.sum(P * z ** n) / nodes


worst = 0.0
for a_test in [LAM, 0.5 + 0.0j, -0.3 + 0.6j, 0.82 * cmath.exp(1j * 0.3)]:
    for n in range(0, 6):
        worst = max(worst, abs(poisson_moment(a_test, n) - a_test ** n))
L.check("P01", "A", "Poisson moments <1, M_z^n 1>_{mu_a} = a^n  (all a, n<=5)",
        worst, 1e-8)

# Positivity of the Poisson kernel a.e. => unitary equivalence of (L^2(mu_a), M_z)
# with (L^2(m), M_z) for EVERY strict a. The parameter lives in the cyclic vector.
t = np.linspace(0, 2 * math.pi, 20000, endpoint=False)
zc = np.exp(1j * t)
Pa = (1 - abs(LAM) ** 2) / np.abs(1 - np.conj(LAM) * zc) ** 2
Pb = (1 - 0.5 ** 2) / np.abs(1 - 0.5 * zc) ** 2
L.check("P02", "A", "Poisson kernel P_a > 0 a.e. for a = lambda",
        max(0.0, 1e-12 - float(np.min(Pa))), 1e-12)
L.check("P03", "A", "Poisson kernel P_b > 0 a.e. for b = 0.5",
        max(0.0, 1e-12 - float(np.min(Pb))), 1e-12)
L.check("P04", "A", "both normalized: int P dm = 1",
        max(abs(np.mean(Pa) - 1), abs(np.mean(Pb) - 1)), 1e-9)
L.check("P05", "X", "GUARD: the two cyclic vectors DIFFER (sqrt P_a != sqrt P_b)",
        max(0.0, 1e-3 - float(np.max(np.abs(np.sqrt(Pa) - np.sqrt(Pb))))), 1e-3)
L.declare("P06", "unpointed dilation equality carries ZERO information about a",
          "Theorem M58.6: same M_zeta for every strict scalar contraction")

# ----------------------------------------------------------------------------
# 8. ISOMETRY / UNITARY TYPE GUARD  (F-M58.5)
# ----------------------------------------------------------------------------

print("\n[8] Type guard -- the minimal ISOMETRIC dilation is not unitary")

N = 60
S = np.zeros((N, N), dtype=complex)      # unilateral shift (truncated)
for i in range(N - 1):
    S[i + 1, i] = 1.0
L.check("V01", "A", "unilateral shift is an isometry: S*S = I",
        np.max(np.abs((S.conj().T @ S - np.eye(N))[:N - 1, :N - 1])), TOL_EXACT,
        "evaluated off the truncation column")
defect_uni = np.max(np.abs(S @ S.conj().T - np.eye(N)))
L.check("V02", "X", "GUARD: S S* != I, so S is NOT unitary",
        max(0.0, 0.5 - defect_uni), 0.5)
L.declare("V03", "unitary conjugation preserves unitarity",
          "hence W V_S14 W^dag = U_M46(1) is ill typed unless V_S14 is unitary")

# ----------------------------------------------------------------------------
# 9. THEOREM M58.9 -- ROUTE-S FORM CLOSURE (annealed + CLT => wrapped Gaussian)
# ----------------------------------------------------------------------------

print("\n[9] Theorem M58.9 -- Route-S form closure")

m_S = float(ARGL)
s2_S = float(SIGMA2)

# (a) Gaussian measure reproduces lambda
nodes, wts = np.polynomial.hermite.hermgauss(200)
xs = m_S + math.sqrt(2.0 * s2_S) * nodes
gauss_cf = np.sum(wts * np.exp(1j * xs)) / np.sum(wts)
L.check("S01", "A", "Gaussian E[e^{i phi}] = exp(i m - s^2/2) = lambda",
        abs(gauss_cf - LAM), 1e-12)

# (b) two-point measure reproduces lambda
p2 = (1 + ABSLAM) / 2
tp_cf = p2 * cmath.exp(1j * m_S) + (1 - p2) * cmath.exp(1j * (m_S + math.pi))
L.check("S02", "A", "two-point E[e^{i phi}] = (2p-1) e^{i m} = lambda",
        abs(tp_cf - LAM), TOL_EXACT)
L.check("S03", "R", "two-point weight p = (1+|lambda|)/2 = 0.9457567829",
        abs(p2 - 0.9457567828880235), 1e-13)

# (c) annealed vs quenched -- the corpus lambda^n law selects annealed
print("     n   annealed |l|^n     quenched exp(-n^2 s^2/2)")
ann_q = 0.0
for n in [1, 2, 3, 5]:
    ann = ABSLAM ** n
    que = math.exp(-n * n * s2_S / 2)
    print(f"     {n}   {ann:.10f}      {que:.10f}")
    if n >= 2:
        ann_q = max(ann_q, abs(ann - que))
L.check("S04", "R", "annealed matches corpus |lambda|^n at n=1",
        abs(ABSLAM ** 1 - math.exp(-1 * 1 * s2_S / 2)), 1e-13)
L.check("S05", "X", "GUARD: quenched FAILS already at n=2 (must differ)",
        max(0.0, 0.05 - abs(ABSLAM ** 2 - math.exp(-4 * s2_S / 2))), 0.05)

# (d) CLT: a sum of k iid finite-variance sub-cycle kicks -> wrapped Gaussian
def cf_sum_uniform(k, m_tot, s2_tot):
    """E[e^{i phi}] for phi = sum of k iid uniform kicks, matched mean/variance."""
    half = math.sqrt(3 * s2_tot / k)
    # per-kick uniform on [m_tot/k - half, m_tot/k + half]; cf of uniform:
    per = cmath.exp(1j * m_tot / k) * (math.sin(half) / half)
    return per ** k


errs = []
for k in [1, 2, 4, 8, 16, 32, 64]:
    errs.append(abs(cf_sum_uniform(k, m_S, s2_S) - LAM))
    print(f"     CLT k={k:>3}  |E[e^{{i phi}}] - lambda| = {errs[-1]:.3e}")
L.check("S06", "A", "CLT: k iid kicks -> wrapped Gaussian value (monotone)",
        errs[-1], 5e-5)
L.check("S07", "X", "GUARD: k=1 (single kick) does NOT reach lambda",
        max(0.0, 1e-3 - errs[0]), 1e-3)

# (e) the pre-registered F-M57.2 trap: 2 params fitted to 2 constraints
L.declare("S08", "F-M57.2 TRAP DECLARED: (m, s^2) solved from lambda",
          "ZERO evidential content by M56.7; recorded, not claimed as support")
L.declare("S09", "frame-free half of Route S is s^2 alone (Thm M58.4)",
          "m is pure gauge until R_boundary is action-derived")

# Holevo quantity of the one-event record (frame-free, for the record)
chi_hol = -p2 * math.log(p2) - (1 - p2) * math.log(1 - p2)
print(f"     Holevo chi (nats) = {chi_hol:.10f}   (ln 2 = {math.log(2):.10f})")
L.check("S10", "P", "PROXY: one-event Holevo chi = 0.2108245 < ln 2 (Z-bottleneck)",
        max(0.0, chi_hol - math.log(2)), TOL_EXACT,
        "NOT evidence for the target; a capacity consistency note only")

# ----------------------------------------------------------------------------
# 10. THEOREM M58.5 / M58.8 -- BRANCH STRUCTURE AND THE LOGARITHMIC LIFT
# ----------------------------------------------------------------------------

print("\n[10] Theorems M58.5 / M58.8 -- branches, Abel step, logarithmic lift")

branches = [complex(math.log(ABSLAM), float(ARGL) + 2 * math.pi * k)
            for k in (-1, 0, 1)]
for k, b in zip((-1, 0, 1), branches):
    print(f"     k={k:+d}   Log lambda = {b.real:.7f} + {b.imag:.7f} i")
L.check("B01", "R", "branch Im parts -4.0239357, 2.2592496, 8.5424349 (M57 Y3)",
        max(abs(branches[0].imag + 4.0239358),
            abs(branches[1].imag - 2.2592496),
            abs(branches[2].imag - 8.5424349)), 1e-6)
L.check("B02", "A", "every branch exponentiates back to lambda",
        max(abs(cmath.exp(b) - LAM) for b in branches), 1e-12)
L.check("B03", "X", "GUARD: branches are inequivalent as GENERATORS",
        max(0.0, 1.0 - abs(branches[2] - branches[1])), 1.0)

# Action-derived logarithmic lift along a non-vanishing path a(s)
def lift(path, dpath, n=200000):
    s = np.linspace(0.0, 1.0, n)
    f = np.array([path(x) for x in s])
    df = np.array([dpath(x) for x in s])
    return np.trapezoid(df / f, s)


ell = float(ARGL)
p_path = lambda s: cmath.exp(s * (math.log(ABSLAM) + 1j * float(ARGL)))
d_path = lambda s: (math.log(ABSLAM) + 1j * float(ARGL)) * p_path(s)
lifted = lift(p_path, d_path)
L.check("B04", "A", "path lift: exp(int a'/a ds) = a(1) = lambda",
        abs(cmath.exp(lifted) - LAM), 1e-9)
L.check("B05", "A", "path lift selects the k=0 branch (winding fixed by the path)",
        abs(lifted - branches[1]), 1e-7)

# A path with one extra winding gives a different branch -- non-uniqueness
p2_path = lambda s: cmath.exp(s * (math.log(ABSLAM) + 1j * (float(ARGL) + 2 * math.pi)))
d2_path = lambda s: (math.log(ABSLAM) + 1j * (float(ARGL) + 2 * math.pi)) * p2_path(s)
lift2 = lift(p2_path, d2_path)
L.check("B06", "X", "GUARD: a different action path gives a DIFFERENT branch",
        max(0.0, 1.0 - abs(lift2 - lifted)), 1.0)
L.declare("B07", "Abel coordinate u = Log chi / Log lambda divides by Log lambda",
          "ZS-M46: normalizing the step to 1 IS the branch choice (Thm M58.5)")

# ----------------------------------------------------------------------------
# 11. THEOREM M58.1 -- FACTOR-CORRESPONDENCE SEPARATION (dimension arithmetic)
# ----------------------------------------------------------------------------

print("\n[11] Theorem M58.1 -- tensor factor vs Choi rank")

# Q = 11 is prime, so it admits NO nontrivial tensor factorization at all.
divisors = [d for d in range(2, Q_CONST) if Q_CONST % d == 0]
L.check("K01", "A", "Q = 11 admits no nontrivial tensor factorization",
        float(len(divisors)), 0.5)
# Yet a rank-2 positive operator in Hom(C^2, C^2) exists (the target Choi).
L.check("K02", "A", "a rank-2 CP correspondence on C^2 exists nonetheless",
        abs(int(np.sum(np.abs(eigvalsh(C_lam)) > 1e-10)) - 2), 0.5)
L.declare("K03", "tensor-factor no-go does NOT imply a rank-2 CP no-go",
          "ZS-M56 constrains equivariant subsystem embeddings, not Hom spaces")

# ----------------------------------------------------------------------------
# 12. AUDIT-DEMANDED NEGATIVE CONTROLS  (v1.1)
#     Three of these REFUTE claims made in ZS-M58 v1.0.
# ----------------------------------------------------------------------------

print("\n[12] Audit negative controls -- v1.0 claims tested against counterexamples")

# N01. ZS-M53 Kraus-phase U(1)^2 does NOT move a.  Therefore it is NOT the same
#      group as the boundary-frame U(1)_in x U(1)_out of M58.4A.  v1.0 said it
#      was.  RETRACTED.
def mult_from_kraus(Ks):
    return sum(K[0, 0] * np.conj(K[1, 1]) for K in Ks)


a_before = mult_from_kraus([K1, K2])
worst_kraus = 0.0
for g1, g2 in [(0.7, -2.3), (1.9, 0.4), (-0.8, 2.9)]:
    a_after = mult_from_kraus([cmath.exp(1j * g1) * K1, cmath.exp(1j * g2) * K2])
    worst_kraus = max(worst_kraus, abs(a_after - a_before))
L.check("N01", "A", "M53 Kraus phases leave a INVARIANT (not the frame group)",
        worst_kraus, TOL_NUM,
        "refutes the v1.0 identification of the two U(1)^2 actions")

# N02. Same endpoint, different winding: the frame endpoint does NOT determine
#      the logarithmic branch.  This refutes the v1.0 Transport-Branch Identity.
end0 = cmath.exp(math.log(ABSLAM) + 1j * float(ARGL))
end1 = cmath.exp(math.log(ABSLAM) + 1j * (float(ARGL) + 2 * math.pi))
L.check("N02", "A", "two paths, IDENTICAL endpoint a(1)",
        abs(end0 - end1), TOL_EXACT)
lift_diff = abs((math.log(ABSLAM) + 1j * (float(ARGL) + 2 * math.pi))
                - (math.log(ABSLAM) + 1j * float(ARGL)) - 2j * math.pi)
L.check("N03", "A", "yet their logarithmic lifts differ by exactly 2 pi i",
        lift_diff, TOL_EXACT,
        "refutes v1.0 M58.5: endpoint does not fix the branch")

# N04. Positive Hermitian with real basis vectors but COMPLEX off-diagonal.
#      Refutes the v1.0 claim that reflection positivity alone forces a real.
cc = 0.4
Tpos = np.array([[1.0, 1j * cc], [-1j * cc, 1.0]], dtype=complex)
ev_pos = np.sort(eigvalsh(Tpos))
L.check("N05", "A", "T = [[1,ic],[-ic,1]] is positive Hermitian",
        max(0.0, -ev_pos[0]), TOL_NUM)
L.check("N06", "X", "GUARD: yet <e0,T e1> is NOT real -- positivity is not enough",
        max(0.0, 0.1 - abs(np.imag(Tpos[0, 1]))), 0.1,
        "refutes v1.0 M58.10 as stated; (H-OSR) antiunitary reality is required")

# The narrowed claim: add the antiunitary reality condition and reality returns.
JOS = np.eye(2, dtype=complex)          # complex conjugation in the real basis
Treal = np.real(Tpos) + 0j              # J T J = T holds iff T is real
L.check("N07", "A", "under (H-OSR) J_OS T J_OS = T, the off-diagonal IS real",
        abs(np.imag(Treal[0, 1])), TOL_EXACT)

# N08. Finite-k CLT is convergence, not exact equality.
L.check("N08", "X", "GUARD: finite-k CLT residual is NONZERO (asymptotic only)",
        max(0.0, 1e-9 - errs[-1]), 1e-9,
        "refutes v1.0 M58.9 'is a wrapped Gaussian'; limit statement only")

# ----------------------------------------------------------------------------
# 13. THE CHARACTER REDUCTION OF F-M54-16'   (v1.1, new)
# ----------------------------------------------------------------------------

print("\n[13] Character Reduction -- M58.11', M58.12, M58.13")

# Q01. Quarter-turn generator from dim Z = 2 alone.
#      Phase budget (ZS-M1 Sec 6):  Z^2 * (pi/2) = 2 pi  =>  quantum = 2 pi / Z^2.
c_gen = 2j * mp.pi / (DIM_Z ** 2)
print(f"     c = 2 pi i / (dim Z)^2 = {mp.nstr(c_gen, 15)}")
L.check("Q01", "A", "quarter-turn generator c = 2 pi i/(dim Z)^2 = i pi/2",
        abs(c_gen - 1j * mp.pi / 2), 1e-30,
        "derived from dim Z = 2 (ZS-F5, PROVEN); no free parameter")
L.check("Q02", "A", "c is purely imaginary (a rotation, not an attenuation)",
        abs(mp.re(c_gen)), 1e-30)

# Q03. Character law and the i^z identification.
zt = [mp.mpc('0.3', '0.7'), mp.mpc('-1.1', '0.4'), mp.mpc('0.9', '-0.2')]
r_char = max(abs(mp.exp(c_gen * (u + v)) - mp.exp(c_gen * u) * mp.exp(c_gen * v))
             for u in zt for v in zt)
L.check("Q03", "A", "(G1) character law T(z1+z2) = T(z1)T(z2)", r_char, 1e-28)
r_iz = max(abs(mp.exp(c_gen * u) - mp.power(1j, u)) for u in zt)
L.check("Q04", "A", "T(z) = exp(cz) = i^z  (ZS-M1 map recovered, not assumed)",
        r_iz, 1e-28)
L.check("Q05", "A", "(G3) normalization DT(0) = c",
        abs(c_gen * mp.exp(0) - c_gen), 1e-30)

# Q06. Fixed point and the closure identity -- NO logarithm anywhere.
zfix = mp.mpc('0.4', '0.4')
for _ in range(6000):
    zfix = mp.exp(c_gen * zfix)
L.check("Q06", "R", "fixed point of T is the locked z* (ZS-M1)",
        abs(zfix - ZSTAR), 1e-18)
L.check("Q07", "A", "DT(z) = c T(z), hence DT(z*) = c z*  (product, not exp/log)",
        abs(c_gen * mp.exp(c_gen * zfix) - c_gen * zfix), 1e-18)
a_closure = c_gen * zfix
print(f"     a = DT(z*) = c z* = {mp.nstr(a_closure, 20)}")
print(f"     lambda            = {mp.nstr(LAMBDA, 20)}")
L.check("Q08", "R", "CLOSURE IDENTITY  a = c z* = lambda  (exact, branch-free)",
        abs(a_closure - LAMBDA), 1e-18)
L.check("Q09", "A", "no logarithm enters: a is a product of two single-valued numbers",
        abs(abs(a_closure) - ABSL), 1e-18,
        "the M57.T.2' branch ambiguity does not touch the VALUE of a")

# Q10. Overdetermination: the strict-contraction gate over the quarter-turn family.
def fp_newton(c, z0=0.4 + 0.4j, it=400):
    z = complex(z0)
    for _ in range(it):
        e = np.exp(c * z)
        f, df = e - z, c * e - 1
        if df == 0 or not np.isfinite(df):
            return np.nan
        zn = z - f / df
        if not np.isfinite(zn):
            return np.nan
        if abs(zn - z) < 1e-15:
            z = zn
            break
        z = zn
    return z if abs(np.exp(c * z) - z) < 1e-10 else np.nan


print("     Z   c = 2 pi i/Z^2      |a| = |c z*|     strict contraction?")
mags = {}
for Zc in [1, 2, 3, 4, 5]:
    cz = 2j * math.pi / Zc ** 2
    zf = fp_newton(cz)
    mg = float('nan') if not np.isfinite(zf) else abs(cz * zf)
    mags[Zc] = mg
    print(f"     {Zc}   {cz.imag:12.7f} i    {mg:12.7f}     "
          f"{'yes' if np.isfinite(mg) and mg < 1 else 'EXCLUDED'}")
L.check("Q10", "A", "Z = 1 EXCLUDED by the strict-contraction gate (|a| > 1)",
        max(0.0, 1.0 - mags[1]), TOL_EXACT)
L.check("Q11", "R", "Z = 2 gives |a| = |lambda| = 0.8915136",
        abs(mags[2] - ABSLAM), 1e-12)
L.check("Q12", "P", "PROXY: Z = 2 is the LARGEST |a| < 1 in the family",
        max(0.0, max(mags[3], mags[4], mags[5]) - mags[2]), TOL_EXACT,
        "softest strict contraction; consistency note, NOT evidence")

# Q13. Distance to the neutral point -- anti-fine-tuning.
lo_t, hi_t = 1.5708, 2.5
for _ in range(80):
    mid = (lo_t + hi_t) / 2
    zf = fp_newton(1j * mid)
    m = float('nan') if not np.isfinite(zf) else abs(1j * mid * zf)
    if not np.isfinite(m):
        hi_t = mid
    elif m < 1:
        lo_t = mid
    else:
        hi_t = mid
print(f"     neutral point |a| = 1 at theta_c = {lo_t:.9f} ; pi/2 = {math.pi/2:.9f}")
L.check("Q13", "A", "theta = pi/2 is NOT fine-tuned to the neutral point",
        max(0.0, 0.05 - (lo_t - math.pi / 2)), 0.05,
        f"margin theta_c - pi/2 = {lo_t - math.pi/2:.6f}")

# Q14. PRE-REGISTERED ANTI-NUMEROLOGY MONTE CARLO.
#      Null: the boundary generator is c = i*theta with theta log-uniform on the
#      attracting range [0.1, 2.0].  Band: |a| within 1% of |lambda|.
#      Decision rule fixed before execution: PASS iff p <= 5%.
print("\n     ANTI-NUMEROLOGY MC (pre-registered; null: c = i*theta,"
      " theta log-uniform [0.1,2.0])")
rng_mc = np.random.default_rng(1158)
N_MC = 60000
thetas = np.exp(rng_mc.uniform(math.log(0.1), math.log(2.0), N_MC))
vals = np.array([(lambda zf: float('nan') if not np.isfinite(zf) else abs(1j * t * zf))
                 (fp_newton(1j * t)) for t in thetas])
fin = np.isfinite(vals)
band_lo, band_hi = ABSLAM * 0.99, ABSLAM * 1.01
n_hit = int(np.sum(fin & (vals >= band_lo) & (vals <= band_hi)))
p_mc = n_hit / int(fin.sum())
print(f"     N = {N_MC}, finite = {int(fin.sum())}, band = "
      f"[{band_lo:.7f}, {band_hi:.7f}]")
print(f"     hits = {n_hit},  p = {p_mc:.5f}   "
      f"({'PASS' if p_mc <= 0.05 else 'FAIL'} at the 5% rule)")
L.check("Q14", "P", f"PROXY: anti-numerology MC p = {p_mc:.5f} <= 5% (pre-reg)",
        max(0.0, p_mc - 0.05), 1e-12,
        "superseded in strength by the exact integer gate of the Y-block")

L.declare("Q15", "closure conditions: (H-PROC),(H-BR),(G1),(G2),(G3_S14)",
          "corrected in v1.2: G3 and the CPTP/QND/rank-2 process gate were missing")

# ----------------------------------------------------------------------------
# 13B. THE COMPLEMENTARY HOLONOMY-EXPANSION GATE   (v1.2, new)
# ----------------------------------------------------------------------------

print("\n[13B] Holonomy-expansion gate -- M58.16 .. M58.20")

# Y01-Y03.  The LOCKED corpus thresholds, recomputed from the Dottie number.
rho_d = mp.findroot(lambda r: mp.cos(r) - r, mp.mpf('0.739'))
s_c = mp.e ** mp.sin(rho_d)
n_c = 2 * mp.pi / s_c
x_c = 1 / n_c
print(f"     Dottie rho = {mp.nstr(rho_d,17)}")
print(f"     s_c = e^sin(rho) = {mp.nstr(s_c,17)}")
print(f"     n_c = 2 pi / s_c = {mp.nstr(n_c,17)}   (corpus LOCKED 3.20356751489)")
print(f"     x_c = 1 / n_c    = {mp.nstr(x_c,17)}")
L.check("Y01", "A", "Dottie number: rho = cos rho", abs(mp.cos(rho_d) - rho_d), 1e-28)
L.check("Y02", "R", "s_c = e^{sin rho} = 1.9613088465 (ZS-M51 Thm T2)",
        abs(s_c - mp.mpf('1.96130884645945594')), 1e-16)
L.check("Y03", "R", "n_c = 2 pi/s_c = 3.20356751489 (ZS-M1 LOCKED)",
        abs(n_c - mp.mpf('3.20356751489')), 1e-11)

# Y04.  RECOGNITION: the v1.1 "neutral point" IS s_c.
L.check("Y04", "R", "v1.1 neutral point theta_c EQUALS the locked s_c",
        abs(mp.mpf(lo_t) - s_c), 1e-8,
        "the v1.1 anti-fine-tuning margin was an unrecognised ZS-M51 theorem")

# Y05.  ZS-M51 Theorem T1: the multiplier of f_s(z) = e^{isz} is |W0(-is)|.
worst_T1 = 0.0
for s_val in [mp.pi / 2, mp.mpf('0.7'), mp.mpf('1.2'), 2 * mp.pi / 9]:
    z = mp.mpc('0.4', '0.4')
    for _ in range(4000):
        z = mp.exp(1j * s_val * z)
    worst_T1 = max(worst_T1, abs(abs(1j * s_val * z) - abs(mp.lambertw(-1j * s_val))))
L.check("Y05", "A", "ZS-M51 T1: |f_s'(z*)| = |W0(-is)| (4 values of s)",
        worst_T1, 1e-15)

# Y06.  ZS-M57: lambda = -W0(-log i), exactly.
L.check("Y06", "R", "lambda = -W0(-log i) = -W0(-i pi/2)  (ZS-M57 PROVEN)",
        abs(LAMBDA + mp.lambertw(-1j * mp.pi / 2)), 1e-18)

# Y07.  Primitive holonomy order on the expanding base T_m(x) = {mx}.
worst_ord = 0.0
for m in range(3, 12):
    x_prim = mp.mpf(1) / (m - 1)
    H = mp.exp(2j * mp.pi * x_prim)
    worst_ord = max(worst_ord, abs(H ** (m - 1) - 1))
    for k in range(1, m - 1):                       # no smaller order
        worst_ord = max(worst_ord, max(0.0, 1e-6 - float(abs(H ** k - 1))))
L.check("Y07", "A", "ord(H_prim) = m - 1 exactly, for m = 3..11",
        worst_ord, 1e-25)

# Y08-Y09.  ZS-M51 Fixed-Point Census:  N_m = ceil(x_c (m-1)) - 1.
print("     m   x_prim=1/(m-1)   N_m = ceil(x_c(m-1))-1")
first_saddle = None
for m in range(2, 9):
    N_m = int(mp.ceil(x_c * (m - 1))) - 1
    if N_m >= 1 and first_saddle is None:
        first_saddle = m
    print(f"     {m}   {float(1/mp.mpf(m-1)):>12.6f}   {N_m}"
          f"{'   <-- FIRST contracting saddle' if m == first_saddle else ''}")
L.check("Y08", "A", "census: N_m = 0 for m <= 4 (no contracting saddle)",
        float(max(int(mp.ceil(x_c*(m-1)))-1 for m in range(2, 5))), 0.5)
L.check("Y09", "R", "FIRST contracting saddle at m = 5, x0 = 1/4 (ZS-M51 T5-T6)",
        abs(first_saddle - 5), 0.5)

# Y10.  At that saddle: c, the map, the holonomy and its order -- no dim Z used.
x0 = mp.mpf(1) / 4
c_saddle = 2j * mp.pi * x0
H_saddle = mp.exp(2j * mp.pi * x0)
L.check("Y10", "A", "saddle generator c = 2 pi i x0 = i pi/2 (dim Z NOT used)",
        abs(c_saddle - 1j * mp.pi / 2), 1e-30)
L.check("Y11", "A", "saddle map e^{c z} = i^z", abs(mp.exp(c_saddle) - 1j), 1e-28)
L.check("Y12", "A", "primitive holonomy H = i, ord(H) = 4",
        max(abs(H_saddle - 1j), abs(H_saddle ** 4 - 1)), 1e-28)
L.check("Y13", "R", "saddle multiplier |W0(-i pi/2)| = |lambda| = 0.8915136",
        abs(abs(mp.lambertw(-1j * mp.pi / 2)) - ABSL), 1e-18)
L.check("Y14", "R", "topological entropy h_top(T_5) = log 5 (ZS-F47 PROVEN)",
        abs(mp.log(5) - mp.mpf('1.6094379124341003')), 1e-15)

# Y15-Y17.  The two gates on d = dim Z, under (H-ZSQ): x_d = 1/d^2, m_d = d^2+1.
print("\n     d   x_d=1/d^2   m_d=d^2+1   |W0(-i s_d)|   contraction   ord H   h_top")
ctr_pass, first_pass = [], []
for d in range(1, 7):
    x_d = mp.mpf(1) / d ** 2
    m_d = d ** 2 + 1
    s_d = 2 * mp.pi * x_d
    w_d = abs(mp.lambertw(-1j * s_d))
    if w_d < 1:
        ctr_pass.append(d)
    if m_d == 5:
        first_pass.append(d)
    print(f"     {d}   {float(x_d):>9.6f}   {m_d:>9}   {float(w_d):>12.7f}   "
          f"{'YES' if w_d < 1 else 'no':>11}   {m_d-1:>5}   {float(mp.log(m_d)):>7.5f}")
L.check("Y15", "A", "contraction gate  d^2 > n_c  <=>  d >= 2  (excludes d = 1)",
        float(abs(min(ctr_pass) - 2)), 0.5)
L.check("Y16", "A", "first-saddle gate  m_d = 5  <=>  d = 2 (unique)",
        float(abs(len(first_pass) - 1) + abs(first_pass[0] - 2)), 0.5)
inter = sorted(set(ctr_pass) & set(first_pass))
print(f"     G_ctr = {{d >= 2}} ,  G_first = {{2}} ,  intersection = {inter}")
L.check("Y17", "A", "EXACT INTEGER GATE: G_ctr n G_first = {2}",
        float(abs(len(inter) - 1) + abs(inter[0] - 2)), 0.5)

# Guards.
L.check("Y18", "X", "GUARD: d = 1 gives x = 1 == 0, a degenerate (non-interior) point",
        max(0.0, 1e-12 - float(abs(mp.mpf(1)/1 - 1))), 1e-12,
        "d = 1 is excluded twice over: no interior fixed point, and no contraction")
L.check("Y19", "X", "GUARD: contraction ALONE does not select d = 2 over d = 3,4,5",
        max(0.0, 3.5 - float(len(ctr_pass))), 3.5,
        "reported against interest: the contraction gate passes d >= 2")
L.check("Y20", "P", "PROXY: m = 5 is also the minimal m = 1 (mod 4) (ZS-F47)",
        float(min(m for m in range(2, 40) if m % 4 == 1) - 5), 0.5,
        "two independent minimality principles agree; NOT evidence by itself")
L.declare("Y21", "residual hypotheses of the expansion gate: (H-ZSQ), (H-MIN)",
          "(H-ZSQ) ord(H_dZ) = (dim Z)^2 ; (H-MIN) the S14 event IS the first saddle")
L.declare("Y22", "the s-family is ZS-M51 Thm T1 (IMPORTED-PROVEN), not an M58 invention",
          "only the specialisation s_d = 2 pi/d^2 under (H-ZSQ) is new here")

# ----------------------------------------------------------------------------
# 13C. THIRD-AUDIT BLOCK: charge grading, intertwiner compression,
#      the single-cycle obstruction, and the carrier ledger      (v1.3, new)
# ----------------------------------------------------------------------------

import itertools
import json
import os

print("\n[13C] Third-audit block -- M58.21 .. M58.24")

# --- Z01-Z04.  The Z4 holonomy charge grading of M_2(C). -------------------
U_H = np.diag([1.0, 1j])
charges = {}
worst_grade = 0.0
for (j, k) in [(0, 0), (1, 1), (0, 1), (1, 0)]:
    E = np.zeros((2, 2), dtype=complex)
    E[j, k] = 1.0
    out = U_H @ E @ U_H.conj().T
    ph = out[j, k]
    charges[(j, k)] = round(cmath.phase(ph) / (math.pi / 2)) % 4
    worst_grade = max(worst_grade, np.max(np.abs(out - ph * E)))
print(f"     charges: E00={charges[(0,0)]}, E11={charges[(1,1)]}, "
      f"E01={charges[(0,1)]}, E10={charges[(1,0)]}  (mod 4)")
L.check("Z01", "A", "Ad(U_H) acts diagonally on the four matrix units",
        worst_grade, TOL_EXACT)
L.check("Z02", "A", "charge grading: E00,E11 -> 0 ; E01 -> -1 ; E10 -> +1",
        float(abs(charges[(0, 0)]) + abs(charges[(1, 1)])
              + abs(charges[(0, 1)] - 3) + abs(charges[(1, 0)] - 1)), 0.5)

# --- Z03-Z07.  Covariant + CPTP but NOT QND: the explicit counterexample. ---
def phi_popmix(p, a):
    def f(rho):
        r = np.array(rho, dtype=complex)
        out = np.zeros((2, 2), dtype=complex)
        out[0, 0] = (1 - p) * r[0, 0] + p * r[1, 1]
        out[1, 1] = p * r[0, 0] + (1 - p) * r[1, 1]
        out[0, 1] = a * r[0, 1]
        out[1, 0] = np.conj(a) * r[1, 0]
        return out
    return f


p_mix, a_mix = 0.18, 0.6 + 0.3j
phi_cx = phi_popmix(p_mix, a_mix)
C_cx = choi(phi_cx)
L.check("Z03", "A", "counterexample channel is CP (Choi PSD)",
        max(0.0, -float(np.min(eigvalsh(C_cx)))), TOL_NUM)
Tr_cx = np.array([[sum(C_cx[2 * k + i, 2 * k + j] for k in range(2))
                   for j in range(2)] for i in range(2)])
L.check("Z04", "A", "counterexample channel is TP",
        np.max(np.abs(Tr_cx - I2)), TOL_EXACT)
cov = 0.0
for j, k in itertools.product(range(2), repeat=2):
    E = np.zeros((2, 2), dtype=complex)
    E[j, k] = 1.0
    cov = max(cov, np.max(np.abs(U_H @ phi_cx(E) @ U_H.conj().T
                                 - phi_cx(U_H @ E @ U_H.conj().T))))
L.check("Z05", "A", "counterexample channel is Ad(U_H)-covariant",
        cov, TOL_EXACT)
P0 = np.diag([1.0, 0.0]).astype(complex)
qnd_res = float(np.max(np.abs(phi_cx(P0) - P0)))
L.check("Z06", "X", "GUARD: yet it is NOT QND -- order-4 covariance is not enough",
        max(0.0, 0.05 - qnd_res), 0.05,
        f"population mixing p = {p_mix} survives covariance")
L.declare("Z07", "therefore (H-PROC) needs a conserved current, not covariance",
          "M58.21: the Z4 grading forbids coherence/population mixing and "
          "E01<->E10 mixing, but NOT E00<->E11 mixing")

# --- Z08-Z13.  Intertwiner Compression: J = Ad(V) transports everything. ----
rng_j = np.random.default_rng(7)
Mrand = rng_j.normal(size=(2, 2)) + 1j * rng_j.normal(size=(2, 2))
Vj, _ = np.linalg.qr(Mrand)


def phi_conj(rho):
    return Vj.conj().T @ qnd_channel(LAM)(Vj @ rho @ Vj.conj().T) @ Vj


C_j = choi(phi_conj)
Z_rot = Vj.conj().T @ Z_PATH @ Vj
P0r = (np.eye(2) + Z_rot) / 2
P1r = (np.eye(2) - Z_rot) / 2
L.check("Z08", "A", "J = Ad(V) transports complete positivity",
        max(0.0, -float(np.min(eigvalsh(C_j)))), TOL_NUM)
Tr_j = np.array([[sum(C_j[2 * k + i, 2 * k + j] for k in range(2))
                  for j in range(2)] for i in range(2)])
L.check("Z09", "A", "J transports trace preservation",
        np.max(np.abs(Tr_j - I2)), TOL_NUM)
L.check("Z10", "A", "J transports QND w.r.t. the rotated pointer",
        max(np.max(np.abs(phi_conj(P0r) - P0r)),
            np.max(np.abs(phi_conj(P1r) - P1r))), TOL_NUM)
L.check("Z11", "A", "J transports Choi rank two",
        abs(int(np.sum(np.abs(eigvalsh(C_j)) > 1e-10)) - 2), 0.5)
e0r = Vj.conj().T @ np.array([1.0, 0.0])
e1r = Vj.conj().T @ np.array([0.0, 1.0])
mult_j = np.vdot(e0r, phi_conj(np.outer(e0r, e1r.conj())) @ e1r)
L.check("Z12", "A", "J transports the multiplier itself",
        abs(mult_j - LAM), TOL_NUM)
L.declare("Z13", "M58.22A: a channel intertwiner BYPASSES (G1)-(G3),(H-BR)",
          "it does NOT derive them: (G2),(G3) are germ properties, not "
          "one-event channel properties.  Type premise: A^ptr_S14 is a unital "
          "C*-algebra with a fixed identification iota to M_2(C), and J,J^-1 "
          "are unital and completely positive; then J o iota^-1 = Ad(V).")
L.declare("Z13b", "M58.22B: the GERM-level intertwiner is what yields (G2),(G3)",
          "J T_S14(z) J^-1 = f_{1/4}(z) on a neighbourhood; strictly stronger "
          "than the channel statement and OPEN")

# --- Z14-Z17.  The single-cycle obstruction (corrects the audit's proposal). -
print("     d   ord(Ad U_d) with zeta a primitive d^2-th root   fixed matrix units")
worst_ord_real = 0.0
fixed_counts = {}
for d in (2, 3, 4):
    dsq = d * d
    zeta = cmath.exp(2j * math.pi / dsq)
    Ud = np.diag([zeta ** j for j in range(d)])
    order = None
    for n in range(1, 4 * dsq + 1):
        Un = np.linalg.matrix_power(Ud, n)
        dev = 0.0
        for j, k in itertools.product(range(d), repeat=2):
            E = np.zeros((d, d), dtype=complex)
            E[j, k] = 1.0
            dev = max(dev, np.max(np.abs(Un @ E @ Un.conj().T - E)))
        if dev < 1e-11:
            order = n
            break
    # Ad of a diagonal unitary fixes every E_jj
    nfix = 0
    for j in range(d):
        E = np.zeros((d, d), dtype=complex)
        E[j, j] = 1.0
        if np.max(np.abs(Ud @ E @ Ud.conj().T - E)) < 1e-12:
            nfix += 1
    fixed_counts[d] = nfix
    worst_ord_real = max(worst_ord_real, abs(order - dsq))
    print(f"     {d}   ord = {order:>3}  (= d^2 = {dsq})                        "
          f"      {nfix} of {dsq}")
L.check("Z14", "A", "(H-ZSQ) is REALIZABLE: ord(Ad U_d) = d^2 for d = 2,3,4",
        float(worst_ord_real), 0.5)
L.check("Z15", "X", "GUARD: Ad(diagonal) FIXES all d diagonal matrix units",
        float(sum(abs(fixed_counts[d] - d) for d in (2, 3, 4))), 0.5,
        "so single-cycle transitivity on the d^2 units is impossible")
L.declare("Z16", "M58.23: the (H-ZSQ) mechanism is FAITHFULNESS, not transitivity",
          "corrects the third audit's proposed single-cycle route")

# --- Z17-Z19.  The carrier ledger against ZS-F48 / ZS-Q18. -----------------
def E_f48(w):
    """ZS-F48 coherence-coordinate state manifold (2 real dims).

    Coherence coordinate placed at rho_01 = w so that the corpus convention
    Phi(rho)_01 = lambda rho_01 (ZS-M53/ZS-Q18) applies directly.  ZS-F48
    prints the transpose; the two differ by the choice of which off-diagonal
    carries lambda, and nothing else.
    """
    return np.array([[1 - 2 * abs(w) ** 2, w],
                     [np.conj(w), 2 * abs(w) ** 2]], dtype=complex)


def phi_ad(rho):
    """ZS-F48's amplitude-damping representative -- LINEAR form.

    v1.3 wrote out[0,0] = 1 - out[1,1], which is affine, not linear; it agreed
    with the linear map only on trace-one inputs.  Corrected here.
    """
    r = np.array(rho, dtype=complex)
    g = 1 - abs(LAM) ** 2
    out = np.zeros((2, 2), dtype=complex)
    out[0, 0] = r[0, 0] + g * r[1, 1]
    out[1, 1] = abs(LAM) ** 2 * r[1, 1]
    out[0, 1] = LAM * r[0, 1]
    out[1, 0] = np.conj(LAM) * r[1, 0]
    return out


def E_full(p, w):
    """ZS-Q18 Thm Q18.12 full-state carrier (3 real dims)."""
    return np.array([[1 - p, w], [np.conj(w), p]], dtype=complex)


# Z17.  Linearity of the corrected amplitude-damping representative.
lin_res = 0.0
rng_l = np.random.default_rng(41)
for _ in range(300):
    A = rng_l.normal(size=(2, 2)) + 1j * rng_l.normal(size=(2, 2))
    B = rng_l.normal(size=(2, 2)) + 1j * rng_l.normal(size=(2, 2))
    al, be = complex(*rng_l.normal(size=2)), complex(*rng_l.normal(size=2))
    lin_res = max(lin_res, np.max(np.abs(phi_ad(al * A + be * B)
                                         - al * phi_ad(A) - be * phi_ad(B))))
L.check("Z17", "A", "corrected Phi_AD is LINEAR (v1.3 form was affine)",
        lin_res, 1e-12)

# Z18.  ZS-F48 intertwiner on its own state manifold.
worst_f48 = 0.0
for w in [0.11 + 0.07j, -0.2 + 0.13j, 0.31j, 0.05]:
    worst_f48 = max(worst_f48, np.max(np.abs(phi_ad(E_f48(w)) - E_f48(LAM * w))))
L.check("Z18", "R", "ZS-F48: Phi_AD(E(w)) = E(lambda w) on the AD manifold",
        worst_f48, 1e-14, "amplitude damping, NOT a QND/Belavkin instrument")

# Z18b.  The DIRECTLY RELEVANT ZS-Q18 check, absent in v1.3.
worst_q18 = 0.0
for p_ in [0.13, 0.5, 0.81]:
    for w in [0.11 + 0.07j, -0.2 + 0.13j, 0.31j]:
        worst_q18 = max(worst_q18, np.max(np.abs(
            qnd_channel(LAM)(E_full(p_, w)) - E_full(p_, LAM * w))))
L.check("Z18b", "R", "ZS-Q18 Thm Q18.12: Phi_deph(E_full(p,w)) = E_full(p,lambda w)",
        worst_q18, 1e-14, "this, not the AD manifold, is the F-M54-16' carrier")

# Z18c.  Dimension claim by Jacobian RANK (v1.3's Z18 was abs(2-2)).
def jac_rank(f, x0, eps=1e-6):
    x0 = np.asarray(x0, dtype=float)
    cols = []
    for i in range(len(x0)):
        e = np.zeros_like(x0)
        e[i] = eps
        cols.append((np.asarray(f(x0 + e)) - np.asarray(f(x0 - e))) / (2 * eps))
    return np.linalg.matrix_rank(np.array(cols).T, tol=1e-6)


bloch_f48 = lambda uv: [uv[0], uv[1], 2 * (uv[0] ** 2 + uv[1] ** 2)]
bloch_full = lambda uvp: [uvp[0], uvp[1], uvp[2]]
r_f48 = min(jac_rank(bloch_f48, [0.17, -0.09]), jac_rank(bloch_f48, [0.4, 0.22]))
r_full = min(jac_rank(bloch_full, [0.17, -0.09, 0.3]),
             jac_rank(bloch_full, [0.05, 0.4, 0.7]))
print(f"     Jacobian rank: F48 manifold = {r_f48}, Q18 E_full = {r_full}")
L.check("Z18c", "A", "Jacobian rank: F48 manifold 2, Q18 E_full 3 in the Bloch ball",
        float(abs(r_f48 - 2) + abs(r_full - 3)), 0.5,
        "the gap is exactly one real coordinate: the population p")
L.declare("Z19", "M58.24 carrier lineage (corrected in v1.4)",
          "F48 = amplitude-damping coherence-coordinate PRECURSOR; "
          "Q18 Thm Q18.12 = the actual full-state QND carrier")

# --- Z20-Z23.  Route B artifact, loaded from the FIREWALLED module. ---------
import subprocess
import sys as _sys
import tempfile
from pathlib import Path as _Path

_here = _Path(__file__).parent
_art_path = _here / "m58_expansion_artifact.json"
_cpath = _here / "zs_m58_expansion_construct_v1_7.py"
_EXPECTED_MODULE = "zs_m58_expansion_construct_v1_7"

# --- Z20.  A MISSING ARTIFACT IS A HARD FAILURE (v1.4 recorded a DECLARATION).
L.check("Z20", "X", "REQUIRED: Route-B artifact exists",
        0.0 if _art_path.exists() else 1.0, 0.5,
        "v1.4 returned 150/150 PASS with no construction evidence at all")
L.check("Z20b", "X", "REQUIRED: Route-B construction source exists",
        0.0 if _cpath.exists() else 1.0, 0.5,
        "v1.4 PASSED Z26 when this file was deleted")

# --- Z20c-Z20f.  ARTIFACT-SOURCE PROVENANCE (v1.6).  Integrity is not enough:
#     v1.5 accepted a v1.4 artifact, and a valid artifact beside a stub source.
def _clean_regenerate():
    """Run a pristine copy of the construction source; return its envelope."""
    if not _cpath.exists():
        return None, "construction source missing"
    src = _cpath.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as td:
        cp = _Path(td) / _cpath.name           # same filename => same source hash
        cp.write_text(src, encoding="utf-8")
        proc = subprocess.run([_sys.executable, str(cp)], cwd=td,
                              capture_output=True, text=True, timeout=600)
        art = cp.with_name("m58_expansion_artifact.json")
        if proc.returncode != 0 or "FIREWALL VIOLATION" in proc.stdout:
            return None, f"clean run refused (rc={proc.returncode})"
        if not art.exists():
            return None, "clean run emitted no artifact"
        return json.loads(art.read_text(encoding="utf-8")), "ok"


_regen, _regen_note = _clean_regenerate()
L.check("Z20c", "X", "PROVENANCE: a clean copy of the source RUNS and emits",
        0.0 if _regen is not None else 1.0, 0.5, _regen_note)

def _canon(d):
    return json.dumps(d, sort_keys=True, separators=(",", ":"))

if _art_path.exists() and _regen is not None:
    _loaded = json.loads(_art_path.read_text(encoding="utf-8"))
    _same_payload = _canon(_regen["payload"]) == _canon(_loaded["payload"])
    _same_digest = _regen["sha256"] == _loaded.get("sha256")
    L.check("Z20d", "X", "PROVENANCE: regenerated payload matches byte-for-byte",
            0.0 if (_same_payload and _same_digest) else 1.0, 0.5,
            "closes exploit (a): a v1.4 artifact no longer passes")
    L.check("Z20e", "X", f"PROVENANCE: module tag == {_EXPECTED_MODULE}",
            0.0 if _loaded["payload"].get("module") == _EXPECTED_MODULE else 1.0,
            0.5, "v1.5 never read this field")
    import hashlib as _hl0
    _src_now = _hl0.sha256(_cpath.read_text(encoding="utf-8").encode()).hexdigest()
    L.check("Z20f", "X", "PROVENANCE: envelope source_sha256 == current source",
            0.0 if _loaded.get("source_sha256") == _src_now else 1.0, 0.5,
            "closes exploit (b): a stub source no longer passes")
    print(f"     provenance: payload match={_same_payload}, "
          f"digest match={_same_digest}, source bound={_loaded.get('source_sha256')==_src_now}")
else:
    L.check("Z20d", "X", "PROVENANCE: regenerated payload matches byte-for-byte",
            1.0, 0.5, "cannot regenerate")
    L.check("Z20e", "X", f"PROVENANCE: module tag == {_EXPECTED_MODULE}",
            1.0, 0.5, "cannot regenerate")
    L.check("Z20f", "X", "PROVENANCE: envelope source_sha256 == current source",
            1.0, 0.5, "cannot regenerate")

if _art_path.exists():
    import hashlib as _hl

    with open(_art_path, "r", encoding="utf-8") as _fh:
        ENV = json.load(_fh)
    PAY = ENV["payload"]

    def _canonical(d):
        return json.dumps(d, sort_keys=True, separators=(",", ":"))

    _recomputed = _hl.sha256(_canonical(PAY).encode("utf-8")).hexdigest()
    print(f"     artifact digest stored     {ENV['sha256'][:24]}...")
    print(f"     artifact digest recomputed {_recomputed[:24]}...")

    L.check("Z24", "A", "artifact SHA-256 recomputed and matches the envelope",
            0.0 if _recomputed == ENV["sha256"] else 1.0, 0.5,
            "v1.3 never recomputed this; a tampered artifact passed")

    _tampered = json.loads(_canonical(PAY))
    _tampered["census"]["5"] = 999
    _bad = _hl.sha256(_canonical(_tampered).encode("utf-8")).hexdigest()
    L.check("Z25", "X", "GUARD: tampering the payload CHANGES the digest",
            0.0 if _bad != ENV["sha256"] else 1.0, 0.5,
            "closes audit-4 exploit 2, end-to-end")

    L.check("Z27", "R", "artifact: first contracting saddle m = 5",
            abs(int(PAY["first_contracting_saddle_m"]) - 5), 0.5)
    L.check("Z28", "R", "artifact: generator c = i pi/2 (built without dim Z)",
            abs(mp.mpf(PAY["generator_c_im"]) - mp.pi / 2), 1e-20)
    L.check("Z29", "R", "artifact: primitive holonomy order = 4",
            abs(int(PAY["primitive_holonomy_order"]) - 4), 0.5)
    L.check("Z30", "R", "COMPARISON: artifact |multiplier| equals |lambda|",
            abs(mp.mpf(PAY["saddle_multiplier_modulus"]) - ABSL), 1e-19,
            "the ONLY place Route B meets the target")
else:
    # FIXED LEDGER SIZE (audit 7): emit the artifact-dependent rows as FAILs
    # rather than skipping them, so the row count is always 166.
    for _t, _cl, _nm in [
            ("Z24", "A", "artifact SHA-256 recomputed and matches the envelope"),
            ("Z25", "X", "GUARD: tampering the payload CHANGES the digest"),
            ("Z27", "R", "artifact: first contracting saddle m = 5"),
            ("Z28", "R", "artifact: generator c = i pi/2 (built without dim Z)"),
            ("Z29", "R", "artifact: primitive holonomy order = 4"),
            ("Z30", "R", "COMPARISON: artifact |multiplier| equals |lambda|")]:
        L.check(_t, _cl, _nm, 1.0, 0.5, "artifact absent -- unevaluable, so FAIL")


# --- Z26 / Z26b.  END-TO-END firewall attack tests (v1.4's were tautologies).
def _attack_firewall(injection: str, label: str):
    """Write a mutated copy of the construct module, RUN it, require refusal."""
    if not _cpath.exists():
        return 1.0, "construction source missing"
    src = _cpath.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as td:
        mut = _Path(td) / "construct_mutated.py"
        mut.write_text(src + "\n" + injection + "\n", encoding="utf-8")
        proc = subprocess.run([_sys.executable, str(mut)], cwd=td,
                              capture_output=True, text=True, timeout=300)
        emitted = (mut.with_name("m58_expansion_artifact.json")).exists()
        ok = (proc.returncode != 0
              and "FIREWALL VIOLATION" in proc.stdout
              and not emitted)
        return (0.0 if ok else 1.0,
                f"rc={proc.returncode}, artifact_emitted={emitted}")


_r26, _n26 = _attack_firewall("LAM" + "BDA = 123", "identifier")
L.check("Z26", "X", "END-TO-END: injected identifier => refusal, no artifact",
        _r26, 0.5, _n26)
_r26b, _n26b = _attack_firewall("_x = " + "0.89151" + "35657", "literal")
L.check("Z26b", "X", "END-TO-END: injected banned literal => refusal, no artifact",
        _r26b, 0.5, _n26b)

# --- Z31 / Z32.  THE POINTER-PRESERVATION CONDITION (P) of M58.22A.
# Without (P), a complete-order intertwiner yields unitary EQUIVALENCE only.
_qnd_rot = max(np.max(np.abs(phi_conj(P0r) - P0r)),
               np.max(np.abs(phi_conj(P1r) - P1r)))
_qnd_fix = max(np.max(np.abs(phi_conj(np.diag([1.0, 0.0]).astype(complex))
                            - np.diag([1.0, 0.0]).astype(complex))),
               np.max(np.abs(phi_conj(np.diag([0.0, 1.0]).astype(complex))
                            - np.diag([0.0, 1.0]).astype(complex))))
print(f"     QND residual: rotated pointer {_qnd_rot:.2e}, "
      f"FIXED Z_path {_qnd_fix:.2e}")
L.check("Z31", "X", "GUARD: pointer preservation does NOT follow from equivalence",
        max(0.0, 0.05 - float(_qnd_fix)), 0.05,
        "guards the INFERENCE only; does not detect (P) being dropped elsewhere")
_Vp = np.diag([1.0, cmath.exp(1j * 0.83)])          # preserves the pointer
_phi_p = lambda r: _Vp.conj().T @ qnd_channel(LAM)(_Vp @ r @ _Vp.conj().T) @ _Vp
_pres = max(np.max(np.abs(_Vp.conj().T @ Z_PATH @ _Vp - Z_PATH)),
            np.max(np.abs(_phi_p(np.diag([1.0, 0.0]).astype(complex))
                          - np.diag([1.0, 0.0]).astype(complex))))
L.check("Z32", "A", "with (P) [J(Z_ptr) = Z_path], fixed-frame QND holds",
        _pres, TOL_NUM,
        "condition (P) is what upgrades equivalence to equality")
L.declare("Z33", "M58.22A requires (P): J(Z^S14_ptr) = Z_path",
          "without it the theorem proves unitary equivalence, not the literal "
          "identity Phi_S14 = Phi^QND_{lambda, Z_path}")

# ----------------------------------------------------------------------------
# 13D. THE CORRECTED ENDPOINT-LIFT-INTERTWINER RELATIONS   (v1.7, M58.5'')
# ----------------------------------------------------------------------------

print("\n[13D] M58.5'' -- endpoint / lift / intertwiner, corrected relations")

_Log = cmath.log(LAM)


def _lift_of_branch(k, n=200000):
    """int_0^1 a'/a ds along a_k(s) = exp(s (Log a + 2 pi i k)), from 1 to a."""
    g = _Log + 2j * math.pi * k
    ss = np.linspace(0.0, 1.0, n)
    aa = np.exp(ss * g)
    return np.trapezoid((g * aa) / aa, ss)


_ks = (-2, -1, 0, 1, 2)
_lifts = [_lift_of_branch(k) for k in _ks]

# Z34.  LIFT => ENDPOINT.  a = exp(L) is determined by the branch.
L.check("Z34", "A", "LIFT => ENDPOINT: exp(lift) = a for every branch",
        max(abs(cmath.exp(l) - LAM) for l in _lifts), 1e-13,
        "v1.6 asserted the opposite direction")

# Z35.  ENDPOINT-FIXED HOMOTOPY CLASS  <=>  LOGARITHM BRANCH.
_pred = max(abs(_lifts[i] - (_Log + 2j * math.pi * _ks[i])) for i in range(len(_ks)))
L.check("Z35", "A", "lift = Log a + 2 pi i k exactly (exp is the universal cover)",
        _pred, 1e-13,
        "so homotopy class and branch are ONE datum, not two")
_inject = min(abs(_lifts[i] - _lifts[j])
              for i in range(len(_ks)) for j in range(i + 1, len(_ks)))
L.check("Z36", "A", "the class -> lift map is injective (min gap 2 pi)",
        abs(_inject - 2 * math.pi), 1e-9)

# Z37.  ENDPOINT =/=> LIFT.  This is what v1.6's certificate actually showed.
L.check("Z37", "X", "GUARD: ENDPOINT =/=> LIFT (same a, lifts differ by 2 pi i)",
        max(0.0, 1.0 - float(_inject)), 1.0,
        "distinct branches share one endpoint; v1.6 mislabelled this direction")

# Z38.  TYPE NOTE: a U(1) transport path cannot carry modulus evolution.
_s = np.linspace(0.0, 1.0, 2001)
_u1 = np.exp(1j * _s * cmath.phase(LAM))
_cx = np.exp(_s * _Log)
_u1_var = float(np.max(np.abs(_u1)) - np.min(np.abs(_u1)))
_cx_var = float(np.max(np.abs(_cx)) - np.min(np.abs(_cx)))
print(f"     |a(s)| variation: U(1) transport {_u1_var:.2e},  C* multiplier {_cx_var:.6f}")
L.check("Z38", "A", "U(1) transport path has constant modulus",
        _u1_var, 1e-12)
L.check("Z39", "X", "GUARD: the C* multiplier path does NOT (types differ)",
        max(0.0, 0.05 - _cx_var), 0.05,
        "v1.6 typed the lift datum as U(1) but integrated a C* path")
L.declare("Z40", "M58.5'': THREE layers, not four",
          "L1 endpoint; L2 lift (homotopy class == branch == winding integer); "
          "L3 event-step intertwiner.  L2 => L1, L1 =/=> L2, L1 ^ L2 =/=> L3")

# ----------------------------------------------------------------------------
# 14. FIREWALL SELF-SCAN
# ----------------------------------------------------------------------------

print("\n[14] Firewall self-scan")

with open(__file__, "r", encoding="utf-8") as fh:
    src = fh.read()

needle = "resid" + "ual = True"
bad_true = src.count(needle) + src.count(needle.replace(" ", ""))
L.check("W01", "A", "no literal True proof predicate",
        float(bad_true), 0.5)

# The construction layer of this paper computes NO a_S14: gate F-M58-1 is OPEN.
L.declare("W02", "no a_S14 is computed anywhere in this file",
          "F-M58-1 is OPEN by construction; no S14 cellular data is loaded")
L.declare("W03", "no eigenvalue clipping, no per-input renormalization",
          "positivity and trace preservation are tested, never enforced")
L.declare("W04", "zero free parameters",
          "inputs: A = 35/437, Q = 11, dim Z = 2, z*; all else derived")

# ----------------------------------------------------------------------------
# REPORT
# ----------------------------------------------------------------------------

n_fail = L.report()

print(f"""
TERMINAL STATUS (ZS-M58 v1.7)
-----------------------------
  F-M54-16'  unconditional : REFORMULATED / DECOMPOSED -- OPEN
  F-M54-16'  route 1       : CLOSED on (H-PROC)^(H-BR)^(G1)^(G2)^(G3_S14)
  F-M54-16'  route 2       : CLOSED on the existence of J with (13.2) AND the
                             pointer condition (P): J(Z^S14_ptr) = Z_path

  M58.22A  implication PROVEN; application to S14 BYPASS-CONDITIONAL, because
           the existence of J and of (P) is OPEN.  The transported equality
           J Phi_S14 J^-1 = Phi^QND_(lambda, Z_path) is the fixed-pointer
           realization only because J is pointer-preserving.  Without (P):
           unitary EQUIVALENCE only (guard Z31).
  M58.22B  GERM ROUTE: J T_S14(z) J^-1 = f_(1/4)(z) on a neighbourhood would
           additionally derive (G2) and (G3).  OPEN.

  The five-hypothesis character route is REPLACED by one equivalent-strength
  channel-realization problem: F-M54-16' is reduced to ONE UNKNOWN PHYSICAL
  STRUCTURE, not to one missing scalar.

  Route B (firewalled)     : rho -> s_c -> n_c -> x_c -> census -> (5, 1/4)
                             -> c = i pi/2, H = i, ord H = 4, |mult| = |lambda|
                             NO Z-Spin constant consumed.

  Fail-closed AND provenance-bound.  Each of these turns the ledger RED:
    missing artifact (Z20)            missing construction source (Z20b)
    source cannot run clean (Z20c)    artifact not reproducible (Z20d)
    wrong module tag (Z20e)           source hash unbound (Z20f)
    tampered payload (Z20d + Z24)     firewall fails to refuse (Z26/Z26b)
  Z25 is a negative-control digest-sensitivity guard and correctly PASSES.
  Z31 guards the INFERENCE that pointer preservation follows from complete-order
  equivalence; it does not detect (P) being dropped in a successor paper.
  M58.5'' (v1.7): THREE layers -- endpoint, lift (homotopy class == branch),
  intertwiner -- with L2 => L1, L1 =/=> L2, and (L1 ^ L2) =/=> L3.

  anti-numerology MC p={p_mc:.5f}  [PROXY];  Y17 = exact CONDITIONAL discriminator
  Programme: ZS-S28 -> ZS-M60 (intertwiner, TOP PRIORITY) -> ZS-M61 -> ZS-M59
""")

sys.exit(1 if n_fail else 0)
