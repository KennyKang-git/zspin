#!/usr/bin/env python3
"""ZS-M71 v1.4.1 companion verifier.

One-command run (paper and script in the same folder):

    python3 zs_m71_verify_v1_4_1.py --paper ZS-M71_v1_4_1.md --output zs_m71_verify_v1_4_1.json

Self-test (baseline + functional/structural mutations + controls):

    python3 zs_m71_verify_v1_4_1.py --paper ZS-M71_v1_4_1.md --self-test --output zs_m71_verify_v1_4_1.json

Standalone and offline; NumPy and SciPy required. Every evidence row (C/V/W)
certifies a finite computation, exact identity, or witness stated in the
manuscript; no row is a proof object (P=0), and no row certifies novelty,
research grade, physical selection, or mission status (D rows are SKIP).
G rows check the package (paper <-> script <-> ledger consistency); they are
controls, not scientific evidence. The manuscript proofs are the authority for
the universal statements; this script attacks them on finite instances only.

Claim IDs used in the registry (manuscript section in parentheses):
  T-CAP  invariant single-shot capacity identity (section 2)
  T-EC   low-energy bound, witness, imported circular-uncertainty bound (section 3)
  T-ASY  imported Sips asymptotics of the unweighted deficit (section 3)
  L-CAL  calibrated finite-bin record law and static weights (section 4)
  T-WR   weighted frontier duality (section 5)
  T-SAT  finite-energy saturation and the Gaussian counterexample (section 5)
  T-CERT exact rational tail certificates (section 5)
  T-BL   small-resolution boundary-layer theorem and lemmas (section 6)
  C-2    second-order constants, conjecture only (section 6)
  A-CUR  conditional boundary-current witness (appendix A)
  T-JCE / T-JB / T-SB / T-SBC / T-AR / T-DT (section 7)
  PACKAGE / NOVELTY / PROOF / MISSION  controls and non-claims

Version history:
  1.4.1  integrates the v1.4 full audit. Scientific rows, tolerances, tables and
         fault injections are unchanged; only the paired file names and versions
         move, because the audit's four findings are manuscript-side.
  1.4    integrates the supplied v1.3 audit. No scientific row, tolerance,
         registry entry or table changes. The qualification guards move: the
         manuscript now declares PASS, so the ledger mutation is re-pointed to
         a PASS/HOLD mismatch and a new structural mutation checks that a PASS
         cannot be declared without the recorded substantive-novelty basis.
  1.3    integrates the supplied v1.2 audit; adds the small-bin roundoff
         regression V28, an exact finite product witness C13, and preserves the audited T-SBC proof by a byte hash.
         Equation (R1) and regression row R01 are distinct namespaces.
  1.2    adds joint charge-energy and separability checks C10-C12, V20-V27, W04-W05;
         retains all v1.1 science checks and its historical corrections.
  1.1    audit-integrated revision; V11 replaced by a constant exterior envelope;
         live paper-fed phase/reflection/tail/Taylor/window probes added;
         C04 retains exact rational samples, its transcendental check moves to V12;
         four static certificates and other surviving numerical routes retained.
  1.0.0  companion of the Korean-language draft of M71 v1.0 (33 rows, 18 mutations).
  1.0.1  editorial only, for the English manuscript: the two generated table
         cells that were Korean ("no budget", readout description) are now
         English, the doc-table mutation anchor follows, and the table-block
         reader drops header rows language-independently. No scientific row,
         tolerance, registry entry or mutation was changed.
"""
import argparse
import collections
import hashlib
import json
import math
import os
import platform
import re
import subprocess
import sys
import tempfile
from fractions import Fraction as Q
from pathlib import Path

VERSION = "1.4.1"
PAPER_VERSION = "1.4.1"
SCRIPT_NAME = "zs_m71_verify_v1_4_1.py"
PAPER_NAME = "ZS-M71_v1_4_1.md"
# A provenance anchor, not a proof checker: the supplied audit accepted this text.
AUDITED_T_SBC_SHA256 = "4cb50d6cec89506e47148136271d589df44436dfb6028b676af73af242aa3179"
RUN_COMMAND = "python3 zs_m71_verify_v1_4_1.py --paper ZS-M71_v1_4_1.md --output zs_m71_verify_v1_4_1.json"

# registry: (row id, class, claim id)
REGISTRY = [
    ("V01", "V", "T-CAP"), ("C01", "C", "T-EC"), ("V02", "V", "T-EC"), ("V03", "V", "T-EC"),
    ("C02", "C", "T-EC"), ("R01", "R", "T-EC"), ("V04", "V", "T-EC"), ("V05", "V", "T-ASY"),
    ("V06", "V", "L-CAL"), ("V07", "V", "L-CAL"),
    ("C03", "C", "T-CERT"), ("V08", "V", "T-SAT"), ("W01", "W", "T-SAT"),
    ("C04", "C", "T-BL"), ("C05", "C", "T-BL"), ("C06", "C", "T-BL"), ("V09", "V", "T-BL"),
    ("V10", "V", "T-BL"), ("V11", "V", "T-BL"), ("V12", "V", "T-BL"), ("V13", "V", "T-BL"),
    ("X01", "X", "C-2"),
    ("C07", "C", "A-CUR"), ("V14", "V", "A-CUR"),
    ("V15", "V", "L-CAL"), ("V16", "V", "T-BL"), ("V17", "V", "T-BL"),
    ("C08", "C", "LOCAL-TAYLOR"), ("C09", "C", "T-BL"), ("W02", "W", "T-CERT"),
    ("V18", "V", "RECORD-SCOPE"), ("W03", "W", "RECORD-SCOPE"), ("V19", "V", "T-BL"),
    ("C10", "C", "T-JCE"), ("V20", "V", "T-JCE"),
    ("V21", "V", "T-JB"), ("C11", "C", "T-AR"), ("W04", "W", "T-JB"),
    ("V22", "V", "T-SB"), ("V23", "V", "T-SB"), ("W05", "W", "T-SB"),
    ("C12", "C", "T-SB"), ("V24", "V", "T-SBC"), ("V25", "V", "T-SB"),
    ("V26", "V", "T-DT"), ("V27", "V", "T-SBC"),
    ("V28", "V", "RECORD-SCOPE"),
    ("C13", "C", "T-SB"),
    ("G07", "G", "PACKAGE"),
    ("G01", "G", "PACKAGE"), ("G02", "G", "PACKAGE"), ("G03", "G", "PACKAGE"),
    ("G04", "G", "PACKAGE"), ("G05", "G", "PACKAGE"), ("G06", "G", "PACKAGE"),
    ("D01", "D", "NOVELTY"), ("D02", "D", "PROOF"), ("D03", "D", "MISSION"),
]
V12_ROW_IDS = ["C10","V20","V21","C11","W04","V22","V23","W05","C12","V24","V25","V26","V27"]
ROW_IDS = [r[0] for r in REGISTRY]
CLASS_OF = {r[0]: r[1] for r in REGISTRY}
CLAIM_OF = {r[0]: r[2] for r in REGISTRY}

# equation tags and theorem labels that must exist in the manuscript
REQUIRED_TAGS = [str(i) for i in range(1, 37)] + ["11a", "30a", "30b", "30c", "33a", "33b", "33c", "34a", "A1", "A2", "A3", "A4", "A5"]
REQUIRED_TAGS += ["R"+str(i) for i in range(1,20)]
REQUIRED_LABELS = ["T-CAP", "T-EC", "T-ASY", "L-CAL", "T-WR", "T-SAT", "T-CERT", "T-BL", "C-2", "A-CUR"]

REQUIRED_LABELS += ["T-JCE","T-JB","T-SB","T-SBC","T-AR","T-DT"]

FUNCTIONAL_FAULTS = {
    "unstable-small-bin-weights":"V28", "swap-finite-witness-ratio":"C13",
    "ignore-energy-twirl":"V20", "linear-rotor-gap":"V20",
    "wrong-joint-length":"V21", "product-marginals-have-record":"W04",
    "treat-mode-envelope-as-exact":"W05", "omit-sine-boundary-term":"V23",
    "wrong-bandwidth-constant":"V24", "drop-detuning-half":"V26",
    "duplicate-registry": "G06", "drop-twirl-block": "V01", "overtight-energy-complement": "R01",
    "erase-frequency-weights": "V06", "zero-blockwise-phase": "V07",
    "false-spectral-certificate": "C03", "break-exact-w-identity": "C04",
    "fake-oscillator-constant": "V09", "inflate-tbl-lower-bound": "V10",
    "break-supersolution": "V11", "fake-second-order-constant": "X01",
    "lose-current-sign": "C07", "force-eraser-blind": "V14",
}
STRUCTURAL_FAULTS = {
    "doc-audited-proof-drift":"G02",
    "doc-rotor-gap":"V20", "doc-joint-root":"V21",
    "doc-separable-constant":"V24", "doc-independent-modes":"W05",
    "doc-sinc-half":"V26",
    "doc-hash": "G01", "doc-equation": "G02", "doc-table": "G03",
    "doc-ledger": "G04", "doc-version": "G05", "doc-census": "G04",
    "doc-qualification-basis": "G04",
    "doc-phase-sign": "V15", "doc-beta-sign": "V15", "doc-reflection": "V16",
    "doc-tail-rate": "V17", "doc-mixed-coefficient": "C08", "doc-no-click": "V18",
    "doc-universal-lower": "G07",
}
FAULTS = dict(FUNCTIONAL_FAULTS, **STRUCTURAL_FAULTS)

QUAL_VOCAB = {"PASS", "HOLD", "FAIL"}
GRADE_VOCAB = {"1", "2", "3", "4", "5", "UNASSESSED"}
CAND_VOCAB = {"3", "4", "5", "NONE"}


def sha256_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def fmt(x, nd=9):
    return f"{x:.{nd}f}"


# ---------------------------------------------------------------------------
# scientific rows
# ---------------------------------------------------------------------------
def run_science(fault, math_only_paper_missing=False):
    import numpy as np
    import scipy
    from scipy.integrate import quad, solve_ivp
    from scipy.linalg import eigh_tridiagonal, expm
    from scipy.optimize import brentq
    from scipy.special import mathieu_a

    rows = {}
    tables = {}

    def row(rid, ok, **ev):
        rows[rid] = {"id": rid, "class": CLASS_OF[rid], "claim": CLAIM_OF[rid],
                     "status": "PASS" if bool(ok) else "FAIL", "evidence": ev}

    def near(rid, error, tol, **ev):
        row(rid, math.isfinite(float(error)) and abs(error) <= tol, error=float(error), tolerance=tol, **ev)

    def td(a, b):
        return float(np.linalg.svd(a - b, compute_uv=False).sum() / 2)

    # ---- V01 : T-CAP twirl identity on random mixed states --------------------
    rng = np.random.default_rng(71303)
    twirl_error = 0.
    energy_gap = 0.
    for _ in range(100):
        mm = np.arange(-4, 5)
        v = rng.normal(size=9) + 1j * rng.normal(size=9)
        v[4] += 10 ** rng.uniform(0, 5)
        v /= np.linalg.norm(v)
        rho = .8 * np.outer(v, v.conj()) + .2 * np.diag(abs(v) ** 2)
        coh = np.abs(np.diag(rho, 1)).sum()
        z = float(np.dot(mm * mm, rho.diagonal().real))
        energy_gap = max(energy_gap, float(coh - min(1., math.sqrt(2 * z))))
        q = (np.arange(2)[:, None] + mm).ravel()
        mask = (q[:, None] == q[None, :])
        if fault == "drop-twirl-block":
            mask = np.ones_like(mask)
        dx = np.kron(np.array([[0, 1], [1, 0]]), rho) * mask
        twirl_error = max(twirl_error, abs(np.linalg.svd(dx, compute_uv=False).sum() / 2 - coh))
    near("V01", twirl_error, 1e-10, samples=100,
         scope="charge-twirl of X (x) sigma vs sum of adjacent moduli; finite samples, proof in section 2")

    # ---- C01 : exact finite-support identities behind the low-energy bound ----
    identities = [collections.defaultdict(int), collections.defaultdict(int)]

    def monomial(poly, c, i, j):
        if -3 <= i <= 3 and -3 <= j <= 3:
            poly[tuple(sorted((i, j)))] += c
    for mm in range(-4, 5):
        monomial(identities[0], mm, mm, mm - 1)
        monomial(identities[0], -mm, mm, mm + 1)
        monomial(identities[0], -1, mm, mm + 1)
        monomial(identities[1], 1, mm - 1, mm - 1)
        monomial(identities[1], 1, mm + 1, mm + 1)
        monomial(identities[1], -2, mm - 1, mm + 1)
        monomial(identities[1], -2, mm, mm)
        monomial(identities[1], 2, mm, mm + 2)
    residuals = [{str(k): v for k, v in p.items() if v} for p in identities]
    row("C01", not any(residuals), residuals=residuals,
        scope="shift identity (3a) and difference-norm identity (3b) on finite support; extension in section 3")

    # ---- V02 / V03 : energy bound samples and the low-energy witness --------
    near("V02", energy_gap, 1e-10, samples=100, scope="no violation of C <= min(1, sqrt(2 zeta)) on 100 mixed states")
    werr = 0.
    for zz in [1e-9, 1e-4, .01, .1, .3, .5, .9, 1.]:
        amp = np.array([math.sqrt(zz / 2), math.sqrt(1 - zz), math.sqrt(zz / 2)])
        sig = np.outer(amp, amp)
        werr = max(werr, abs(float(np.abs(np.diag(sig, 1)).sum()) - math.sqrt(2 * zz * (1 - zz))),
                   abs(float(np.dot(np.array([1., 0., 1.]), np.diag(sig))) - zz))
    ratio = math.sqrt(2 * 1e-9 * (1 - 1e-9)) / math.sqrt(2 * 1e-9)
    near("V03", max(werr, abs(ratio - 1)), 1e-8, witness_max_error=werr, low_energy_ratio=ratio,
         scope="three-point witness (4): C = sqrt(2 zeta (1-zeta)) and energy zeta at eight energies")

    # ---- C02 : imported circular-uncertainty bound strictly dominates (6) ----
    mul = lambda a, b: [sum(a[j] * b[i - j] for j in range(len(a)) if 0 <= i - j < len(b))
                        for i in range(len(a) + len(b) - 1)]
    lhs = mul(mul([7, 16, 8], [7, 16, 8]), [1, 0, 4])
    rhs = [0, 0] + [256 * x for x in [1, 4, 6, 4, 1]]
    poly = [a - b for a, b in zip(lhs, rhs)]
    row("C02", poly == [49, 224, 308, 128, 0, 0, 0], coefficients_ascending=poly,
        scope="exact polynomial (7): U_old^2 - U_B^2 has positive coefficients; domination proof in section 3")

    # ---- R01 : retained bound (6) has no violation (regression, subsumed) ----
    Mgrid = 600
    mg = np.arange(-Mgrid, Mgrid + 1).astype(float)

    def frontier(mu):
        _, vec = eigh_tridiagonal(-mu * mg * mg, .5 * np.ones(len(mg) - 1),
                                  select="i", select_range=(len(mg) - 1, len(mg) - 1))
        a = np.abs(vec[:, 0]); a /= np.linalg.norm(a)
        return float(np.dot(mg * mg, a * a)), float(np.sum(a[:-1] * a[1:]))

    def newbound(z):
        denom = 4. if fault == "overtight-energy-complement" else 8.
        return 1 - 1 / (denom * (1 + math.sqrt(z)) ** 2)
    front = [frontier(mu) for mu in np.logspace(-5, 1.2, 60)]
    worst_new = max(s - newbound(z) for z, s in front)
    rng2 = np.random.default_rng(20260911)
    for _ in range(2000):
        wd = rng2.uniform(.4, 60.); c0 = rng2.uniform(-25, 25)
        a = np.abs(np.exp(-(mg - c0) ** 2 / (4 * wd * wd)) * (1 + .6 * rng2.normal(size=len(mg))) ** 2) + 1e-300
        a /= np.linalg.norm(a)
        z = float(np.dot(mg * mg, a * a)); s = float(np.sum(a[:-1] * a[1:]))
        worst_new = max(worst_new, s - newbound(z))
    row("R01", worst_new <= 0, max_violation=worst_new,
        scope="regression of the retained, subsumed bound (6) on the finite-cutoff frontier and 2000 states; not evidence of novelty")

    # ---- V04 : dual eigenproblem vs imported Mathieu characteristic value ----
    mm = np.arange(-90, 91, dtype=float)
    ee = []
    for lam in [.03, .1, 1., 5.]:
        lv = eigh_tridiagonal(-lam * mm * mm, np.full(len(mm) - 1, .5),
                              select='i', select_range=(len(mm) - 1, len(mm) - 1), eigvals_only=True)[0]
        theory = -lam * mathieu_a(0, -2 / lam) / 4
        ee.append(abs(float(lv) - float(theory)))
    near("V04", max(ee), 3e-11, max_dimension=len(mm), nu_grid=[.03, .1, 1., 5.],
         scope="(8): sup spec(A_0 - nu M^2) = -(nu/4) a_0(-2/nu) at four dual variables")

    # ---- V05 : imported Sips asymptotics (9) ---------------------------------
    mg9 = np.arange(-900, 901).astype(float)

    def frontier9(mu):
        _, vec = eigh_tridiagonal(-mu * mg9 * mg9, .5 * np.ones(len(mg9) - 1), select="i",
                                  select_range=(len(mg9) - 1, len(mg9) - 1))
        aa = np.abs(vec[:, 0]); aa /= np.linalg.norm(aa)
        return float(np.dot(mg9 * mg9, aa * aa)), float(np.sum(aa[:-1] * aa[1:]))
    errs = []
    for mu in (1 / (8 * 10 ** 2), 1 / (8 * 30 ** 2), 1 / (8 * 100 ** 2), 1 / (8 * 300 ** 2)):
        z, s = frontier9(mu)
        pred = 1 / (8 * z + .5) - 1 / (512 * (2 * z + 1 / 8) ** 3)
        errs.append(dict(zeta=z, one_minus_F0=1 - s, sips_prediction=pred,
                         relative_error=abs((1 - s) - pred) / (1 - s), eight_zeta_deficit=8 * z * (1 - s)))
    near("V05", max(x['relative_error'] for x in errs), 2e-5, cases=errs,
         scope="imported DLMF 28.8.1 expansion mapped through (8); novelty NONE")

    # ---- V06 : calibrated finite-bin law (11)-(12) vs full output probabilities ----
    def weights(m, ratio, h=None):
        omega = ratio * (2 * m + 1)
        if h is None:
            return 1 / np.sqrt(1 + omega * omega)
        return np.abs(np.expm1((-1 + 1j * omega) * h)) / (np.sqrt(1 + omega * omega) * (-np.expm1(-h)))
    rng3 = np.random.default_rng(71525)
    m5 = np.arange(-2, 3); n5 = len(m5)
    Rm = rng3.normal(size=(n5, n5)) + 1j * rng3.normal(size=(n5, n5))
    sigma = Rm @ Rm.conj().T; sigma /= np.trace(sigma)
    hb, Bb, delta = .37, 4, 1.7
    Tb = Bb * hb
    outcomes = [[], []]
    for qq in range(-2, 4):
        ia = qq + 2 if -2 <= qq <= 2 else None
        ib = n5 + (qq - 1) + 2 if -2 <= qq - 1 <= 2 else None
        for j in range(Bb):
            beta = 0.
            if ia is not None and ib is not None:
                omega = delta * (2 * qq - 1)
                km = (np.exp((-1 - 1j * omega) * (j + 1) * hb) - np.exp((-1 - 1j * omega) * j * hb)) / (-1 - 1j * omega)
                beta = -np.angle(sigma[qq + 2, qq + 1] * km)
            for r in [1, -1]:
                v = np.zeros(2 * n5, dtype=complex)
                if ia is not None: v[ia] = 1 / np.sqrt(2)
                if ib is not None: v[ib] = r * np.exp(1j * beta) / np.sqrt(2)
                for kk, sign in enumerate([1, -1]):
                    qubit = np.array([[1., sign], [sign, 1.]]) / 2
                    rho = np.kron(qubit, sigma)

                    def density(t):
                        phase = np.exp(-1j * np.tile(delta * m5 * m5, 2) * t)
                        rt = phase[:, None] * rho * phase.conj()[None, :]
                        return math.exp(-t) * float((v.conj() @ rt @ v).real)
                    outcomes[kk].append(quad(density, j * hb, (j + 1) * hb, epsabs=1e-12)[0])
    for p in outcomes: p.append(math.exp(-Tb))
    actual = np.abs(np.array(outcomes[0]) - outcomes[1]).sum() / 2
    w = weights(m5[:-1], delta, hb)
    if fault == "erase-frequency-weights": w = np.ones_like(w)
    expected = (1 - math.exp(-Tb)) * np.dot(w, np.abs(np.diag(sigma, 1)))
    near("V06", max(abs(actual - expected), *(abs(sum(p) - 1) for p in outcomes)), 1e-10,
         actual_TV=float(actual), weighted_formula=float(expected), bins=Bb, reference_dimension=n5,
         minimum_probability=float(np.min(outcomes)), no_click=math.exp(-Tb),
         scope="one 5-dimensional mixed reference, 4 bins, all charge labels, no-click included")

    # ---- V07 : static sector-phase optimum via a rotated-jump GKSL model ----
    vp = np.array([1., 1.]) / math.sqrt(2); vm = np.array([1., -1.]) / math.sqrt(2)

    def blockwise_tv(kk, dd, TT, zeta, betas):
        mvv = np.arange(-1, 2)
        qq = (np.arange(2)[:, None] + mvv).ravel()
        vecs = []
        for qval in sorted(set(qq)):
            ind = np.flatnonzero(qq == qval)
            for r in (1, -1):
                v = np.zeros(6, complex)
                if len(ind) == 2:
                    v[ind] = np.array([1, r * np.exp(1j * betas.get(qval, 0.))]) / math.sqrt(2)
                else:
                    v[ind] = 1 / math.sqrt(2)
                vecs.append(v)
        HH = np.diag(np.r_[np.tile(dd * mvv * mvv, 2), np.zeros(8)]).astype(complex)
        Ls = []
        for j, v in enumerate(vecs):
            L = np.zeros((14, 14), complex)
            L[6 + j, :6] = math.sqrt(kk) * v.conj()
            Ls.append(L)
        RR = sum(L.conj().T @ L for L in Ls)
        assert np.allclose(RR[:6, :6], kk * np.eye(6))
        ps = np.array([math.sqrt(zeta / 2), math.sqrt(1 - zeta), math.sqrt(zeta / 2)])

        def rhs2(t, y):
            rr = y.reshape(14, 14)
            return (-1j * (HH @ rr - rr @ HH) + sum(L @ rr @ L.conj().T for L in Ls) - (RR @ rr + rr @ RR) / 2).ravel()
        pp = []
        for vv in (vp, vm):
            r0 = np.zeros((14, 14), complex)
            uu = np.kron(vv, ps)
            r0[:6, :6] = np.outer(uu, uu.conj())
            s = solve_ivp(rhs2, (0, TT), r0.ravel(), rtol=1e-10, atol=1e-12)
            rh = s.y[:, -1].reshape(14, 14)
            pp.append(np.array([rh[6 + j, 6 + j].real for j in range(8)] + [np.trace(rh[:6, :6]).real]))
        return float(.5 * np.abs(pp[0] - pp[1]).sum())
    kb, db, TTb, zb = 1., 4., 20., .1
    Cb = math.sqrt(2 * zb * (1 - zb))
    KT = kb / complex(kb, -db) * (1 - math.exp(-kb * TTb) * np.exp(1j * db * TTb))
    beta_star = 0. if fault == "zero-blockwise-phase" else -float(np.angle(KT))
    tv_zero = blockwise_tv(kb, db, TTb, zb, {})
    tv_opt = blockwise_tv(kb, db, TTb, zb, {0: beta_star, 1: -beta_star})
    e_zero = abs(tv_zero - Cb * abs(KT.real)); e_opt = abs(tv_opt - Cb * abs(KT))
    row("V07", e_zero < 1e-9 and e_opt < 1e-9, tv_zero_phase=tv_zero, predicted_D_sign=Cb * abs(KT.real),
        tv_optimal_phase=tv_opt, predicted_C_absK=Cb * abs(KT), error_zero=e_zero, error_optimal=e_opt,
        scope="three-point reference, 14-dimensional GKSL with rotated jumps; static weights (13) at a single edge pair")

    # ---- C03 : exact rational tail certificates (18)-(19) ---------------------
    def eigpair(ratio, lam=0., h=None, L=100):
        m = np.arange(-L, L + 1, dtype=float)
        w_ = weights(m[:-1], ratio, h)
        val, vec = eigh_tridiagonal(-lam * m * m, w_ / 2, select='i', select_range=(len(m) - 1, len(m) - 1))
        v = np.abs(vec[:, 0]); v /= np.linalg.norm(v)
        z = float(np.dot(m * m, v * v))
        score = float(np.dot(w_, v[:-1] * v[1:]))
        return float(val[0]), v, z, score

    def finite_enclosure(ratio, lam, L):
        rf, lf = float(ratio), float(lam)
        val = eigpair(rf, lf, L=L)[0]
        scale = 10 ** 11
        low = Q(math.floor(val * scale) - 4, scale)
        high = Q(math.ceil(val * scale) + 4, scale)

        def above_top(x):
            pivot = x + lam * L * L
            if pivot <= 0: return False
            for k in range(-L + 1, L + 1):
                edge = k - 1
                b2 = Q(1, 4) / (1 + ratio * ratio * (2 * edge + 1) ** 2)
                pivot = x + lam * k * k - b2 / pivot
                if pivot <= 0: return False
            return True
        step = Q(1, 10 ** 9)
        while above_top(low): low -= step
        while not above_top(high): high += step
        return low, high, (not above_top(low) and above_top(high))

    def score_lower(v, ratio, L):
        c = [int(round(float(x) * 10 ** 10)) for x in v]
        den = sum(x * x for x in c)
        energy = Q(sum(k * k * x * x for k, x in zip(range(-L, L + 1), c)), den)
        score = Q(0); bits = 45
        for k, x, y in zip(range(-L, L), c[:-1], c[1:]):
            sq = Q(1) / (1 + ratio * ratio * (2 * k + 1) ** 2)
            wlo = Q(math.isqrt((sq.numerator * (1 << (2 * bits))) // sq.denominator), 1 << bits)
            score += Q(x * y, den) * wlo
        return energy, score
    certificates = []
    for ratio, target in [(Q(1), None), (Q(4), None), (Q(1), Q(1, 10)), (Q(4), Q(1, 10))]:
        L = 36
        if target is None:
            lam = Q(0)
        else:
            ztarget = float(target) * (1 - 1e-7)
            root = brentq(lambda l: eigpair(float(ratio), l, L=L)[2] - ztarget, 1e-9, 100.)
            lam = Q(math.ceil(root * 10 ** 9), 10 ** 9)
        _, v, z, score = eigpair(float(ratio), float(lam), L=L)
        lo, hi, cert = finite_enclosure(ratio, lam, L)
        tail = Q(1) / (ratio * (2 * L + 1)) - lam * (L + 1) ** 2
        b = Q(1) / (2 * ratio * (2 * L + 1))
        upper = hi + b * b / (hi - tail)
        en, lower = score_lower(v, ratio, L)
        feasible = (target is None or en <= target)
        if target is not None: upper += lam * target
        if fault == "false-spectral-certificate": upper = lower - Q(1, 100000)
        ok = cert and hi > tail and feasible and lower <= upper
        certificates.append(dict(ratio=str(ratio), energy_budget=str(target), lambda_dual=str(lam), cutoff=L,
                                 lower_rational=str(lower), upper_rational=str(upper), lower=float(lower),
                                 upper=float(upper), width=float(upper - lower), feasible_energy_rational=str(en),
                                 finite_eigen_bracket=[str(lo), str(hi)], tail_upper=str(tail),
                                 boundary_norm_upper=str(b), certificate_ok=bool(ok)))
    row("C03", all(x['certificate_ok'] for x in certificates), certificates=certificates,
        scope="four declared static cases: exact LDL positivity, rational square-root lower witness, Schur tail bound")
    # outward-rounded printed interval (12 decimals): floor/ceil of the rationals
    def round_down(q, nd=12): return math.floor(q * 10 ** nd) / 10 ** nd
    def round_up(q, nd=12): return math.ceil(q * 10 ** nd) / 10 ** nd
    tables["CERT"] = ["| " + " | ".join([c['ratio'], ("none" if c['energy_budget'] == "None" else "ζ≤" + c['energy_budget']),
                                         f"{round_down(Q(c['lower_rational'])):.12f}", f"{round_up(Q(c['upper_rational'])):.12f}"]) + " |"
                      for c in certificates]

    # ---- V08 : finite-resolution ceiling and critical energy (two cutoffs) ----
    table = []
    for ratio, h in [(1, None), (4, None), (20, None), (1, .5), (1, .1), (1, .03), (1, .01)]:
        val, v, z, score = eigpair(ratio, h=h, L=160)
        val2, _, z2, _ = eigpair(ratio, h=h, L=240)
        table.append(dict(delta_over_kappa=ratio, kappa_h=h, ceiling=val, critical_energy=z,
                          eigen_refinement=abs(val - val2), energy_refinement=abs(z - z2),
                          eigen_identity_error=abs(score - val), ordinary_coherence=float(np.sum(v[:-1] * v[1:]))))
    row("V08", all(0 < x['ceiling'] < 1 and x['critical_energy'] > 0 and x['eigen_refinement'] < 1e-11
                   and x['energy_refinement'] < 1e-8 and x['eigen_identity_error'] < 1e-11 for x in table),
        table=table, scope="numerical ceilings Lambda_w and critical energies at L=160 vs L=240; not interval-certified")
    tables["CEILING"] = ["| " + " | ".join([("static phase per sector, infinite window" if x['kappa_h'] is None else "calibrated phase per sector and bin"),
                                            str(x['delta_over_kappa']), ("—" if x['kappa_h'] is None else str(x['kappa_h'])),
                                            fmt(x['ceiling']), fmt(x['critical_energy'])]) + " |" for x in table]

    # ---- W01 : broad Gaussian: high coherence, poor static record --------------
    m3 = np.arange(-300, 301, dtype=float)
    v = np.exp(-m3 * m3 / (4 * 30 ** 2)); v /= np.linalg.norm(v)
    ordinary = float(np.dot(v[:-1], v[1:]))
    record = float(np.dot(weights(m3[:-1], 1), v[:-1] * v[1:]))
    optimal = eigpair(1)[0]
    row("W01", ordinary > .999 and record < .1 and optimal > .5, ordinary_coherence=ordinary,
        static_record=record, record_ceiling=optimal,
        scope="witness against optimising coherence alone: same static readout, s=30 Gaussian")

    # ---- T-BL lemma rows ----------------------------------------------------
    rngb = np.random.default_rng(71707)
    res = []
    for _ in range(50):
        A = Q(int(rngb.integers(1, 500)), int(rngb.integers(1, 500)))
        T = Q(int(rngb.integers(0, 500)), int(rngb.integers(1, 500)))
        r = Q(int(rngb.integers(1, 99)), 100)
        c = Q(int(rngb.integers(-99, 100)), 100)
        w2 = A * ((1 - r) ** 2 + 2 * r * (1 - c)) / ((A + T) * (1 - r) ** 2)
        rho2 = A * r / (1 - r) ** 2
        rhs = (T - 2 * rho2 * (1 - c)) / (A + T)
        if fault == "break-exact-w-identity":
            rhs = (T - rho2 * (1 - c)) / (A + T)
        res.append(1 - w2 - rhs)
    tr = max(abs(abs(1 - np.exp(-a + 1j * t)) ** 2 - ((1 - math.exp(-a)) ** 2 + 4 * math.exp(-a) * math.sin(t / 2) ** 2))
             for a in (1e-3, .05, .3, 1.) for t in (1e-3, .1, 1., 3., 7., 30.))
    row("C04", all(x == 0 for x in res), rational_residual_max=str(max(res, key=abs)),
        scope="(24): exact rational core at 50 declared rational samples; transcendental check belongs to V12")

    Lc = 7
    ws = [Q(int(rngb.integers(1, 100)), 100) for _ in range(2 * Lc + 2)]
    av = [Q(int(rngb.integers(-9, 10)), 7) for _ in range(2 * Lc + 1)]

    def w_at(m): return ws[m + Lc + 1]
    def a_at(vec, m): return vec[m + Lc] if -Lc <= m <= Lc else Q(0)
    def Qform(vec):
        return (sum(w_at(m) * (a_at(vec, m + 1) - a_at(vec, m)) ** 2 for m in range(-Lc - 1, Lc + 1)) / 2
                + sum(((1 - w_at(m - 1)) + (1 - w_at(m))) / 2 * a_at(vec, m) ** 2 for m in range(-Lc, Lc + 1)))
    direct = sum(x * x for x in av) - sum(w_at(m) * a_at(av, m) * a_at(av, m + 1) for m in range(-Lc - 1, Lc + 1))
    r1 = direct - Qform(av)
    ts = [Q(int(rngb.integers(0, 5)), 5) for _ in range(2 * Lc + 1)]
    chi1 = [(1 - t * t) / (1 + t * t) for t in ts]; chi2 = [2 * t / (1 + t * t) for t in ts]
    b1 = [x * y for x, y in zip(chi1, av)]; b2 = [x * y for x, y in zip(chi2, av)]
    loc = sum(w_at(m) * a_at(av, m) * a_at(av, m + 1)
              * ((a_at(chi1, m + 1) - a_at(chi1, m)) ** 2 + (a_at(chi2, m + 1) - a_at(chi2, m)) ** 2)
              for m in range(-Lc - 1, Lc + 1)) / 2
    r2 = Qform(av) - (Qform(b1) + Qform(b2) - loc)
    row("C05", r1 == 0 and r2 == 0 and all(x * x + y * y == 1 for x, y in zip(chi1, chi2)),
        residual_form=str(r1), residual_ims=str(r2), scope="(28) quadratic-form identity and (30) discrete IMS, exact rationals")

    poly = collections.defaultdict(lambda: Q(0))
    for mm in range(-6, 7):
        if -4 <= mm + 1 <= 4: poly[mm + 1] += Q(2 * mm + 1, 2)
        if -4 <= mm <= 4: poly[mm] += -Q(2 * mm + 1, 2) + 1
    c06 = {str(k): str(v) for k, v in poly.items() if v != 0}
    row("C06", not c06, residuals=c06, scope="telescoping input of (29) on finite support")

    worst = -1e9
    for it in range(2000):
        n = int(rngb.integers(3, 60)); mm = np.arange(-n, n + 1)
        om = 10 ** rngb.uniform(-3, 1)
        if it % 2:
            n = int(min(4000, max(n, 6 / math.sqrt(om)))); mm = np.arange(-n, n + 1)
            v = np.exp(-om * mm * mm / 2) * (1 + .05 * rngb.normal(size=len(mm)))
        else:
            v = rngb.normal(size=len(mm)) * np.exp(-mm * mm / (2 * rngb.uniform(1, 30) ** 2))
        d = np.diff(np.r_[0., v, 0.])
        lhs_ = .5 * np.sum(d * d) + .5 * om * om * np.sum((mm * mm + .25) * v * v)
        target = (om if fault == "fake-oscillator-constant" else om / 2) * np.sum(v * v)
        worst = max(worst, float(target - lhs_))
    ratios = []
    for om in (1., .1, .01, .001):
        mm = np.arange(-4000, 4001); v = np.exp(-om * mm * mm / 2); v /= np.linalg.norm(v)
        d = np.diff(np.r_[0., v, 0.])
        ratios.append(float((.5 * np.sum(d * d) + .5 * om * om * np.sum((mm * mm + .25) * v * v)) / (om / 2)))
    row("V09", worst <= 1e-12 and all(r >= 1 for r in ratios) and ratios[-1] - 1 < 3e-4,
        max_violation=worst, gaussian_ratios=ratios,
        scope="(29): no violation on 2000 random and near-tight vectors; Gaussian ratio -> 1")

    def weights_bl(m, eps, a):
        th = 2 * eps * (m + .5)
        return a * np.abs(1 - np.exp(-a + 1j * th)) / (np.sqrt(a * a + th * th) * (1 - math.exp(-a)))

    def top(eps, a, L):
        m = np.arange(-L, L + 1, dtype=float)
        w_ = weights_bl(m[:-1], eps, a)
        val, vec = eigh_tridiagonal(np.zeros(len(m)), w_ / 2, select='i', select_range=(len(m) - 1, len(m) - 1))
        v = np.abs(vec[:, 0]); v /= np.linalg.norm(v)
        return float(val[0]), v, m, w_

    def lower_bound(eps, a):
        K = math.ceil(eps ** -.75)
        Theta = 2 * eps * (2 * K + 1.5)
        if Theta * Theta > 12:
            return None, dict(K=K)
        y = (Theta * Theta + a * a) / 12
        eta = y / 2 + y * y / 2
        om = eps / math.sqrt(3)
        omt = om * math.sqrt(max(0., 1 - Theta * Theta / 30))
        core = math.sqrt(max(0., 1 - eta)) * omt / 2 - a * a / 24
        thK = 2 * eps * (K - .5)
        Vtail = min(thK ** 4 / (36 * (a * a + thK * thK)), .27)
        Lloc = 4 * math.sin(math.pi / (4 * K)) ** 2
        lb = min(core, Vtail) - Lloc / 2
        if fault == "inflate-tbl-lower-bound":
            lb *= 1.5
        return lb, dict(K=K, eta=eta, core=core, V_tail=Vtail, L_loc=Lloc)

    def gaussian_upper(eps, a, L):
        s2 = math.sqrt(3) / (2 * eps)
        m = np.arange(-L, L + 1, dtype=float)
        v = np.exp(-m * m / (4 * s2)); v /= np.linalg.norm(v)
        w_ = weights_bl(m[:-1], eps, a)
        return 1 - float(np.dot(w_, v[:-1] * v[1:]))
    table10 = []
    ok10 = True
    for ratio in (1., 4., 20.):
        for eps in (.03, .01, .003, .001):
            a = eps / ratio
            L = int(max(300, 12 * math.sqrt(math.sqrt(3) / (2 * eps))))
            lam, v, m, w_ = top(eps, a, L)
            lam2 = top(eps, a, L + 120)[0]
            lb, info = lower_bound(eps, a)
            ub = gaussian_upper(eps, a, L)
            om2 = eps / (2 * math.sqrt(3))
            z = float(np.dot(m * m, v * v))
            ok10 &= (lb is not None) and (lb <= 1 - lam <= ub + 1e-15) and abs(lam - lam2) < 1e-11
            table10.append(dict(delta_over_kappa=ratio, eps=eps, kappa_h=a, one_minus_Lambda=1 - lam, lower=lb,
                                upper_gaussian=ub, lower_over_leading=lb / om2, upper_over_leading=ub / om2,
                                zeta_crit_times_eps=z * eps, product_deficit_energy=(1 - lam) * z,
                                cutoff_refinement=abs(lam - lam2), **info))
    ok10 &= all((x['upper_gaussian'] - x['eps'] / (2 * math.sqrt(3))) / x['eps'] ** 2 <= 1 / 3 + (1 / x['delta_over_kappa']) ** 2 / 24
                for x in table10)
    row("V10", ok10 and all(abs(x['product_deficit_energy'] - .25) < .0015 for x in table10 if x['eps'] <= .003),
        table=table10, scope="(31)-(32) lower bound <= 1-Lambda <= Gaussian upper bound on a 12-point grid; product -> 1/4")
    tables["BL"] = ["| " + " | ".join([str(x['eps']), fmt(x['one_minus_Lambda'] / x['eps'], 6), fmt(x['zeta_crit_times_eps'], 6),
                                       fmt(x['product_deficit_energy'], 7), fmt(x['lower_over_leading'], 4), fmt(x['upper_over_leading'], 6)]) + " |"
                    for x in table10 if x['delta_over_kappa'] == 1.]

    # V11 replacement: a constant envelope on the entire exterior, matching L6.
    out11=[]
    for eps in (.03,.01,.003):
        a=eps; L=1200
        lam,v,m,w_=top(eps,a,L)
        K=math.ceil(eps**-.75); m1=2*K
        theta1=2*eps*(m1+.5)
        qenv=float(weights_bl(np.array([float(m1)]),eps,a)[0])
        rate=math.acosh(lam/qenv)
        if fault=='break-supersolution': rate*=1.5
        geometric=math.exp(-2*rate)
        closed=geometric*(m1*m1/(1-geometric)+2*m1/(1-geometric)**2+(1+geometric)/(1-geometric)**3)
        tail_bound=2*float(v[m1+L]**2)*closed
        edge_m=np.arange(m1,L-1)
        wm=weights_bl(edge_m.astype(float),eps,a);wp=weights_bl(edge_m.astype(float)+1,eps,a)
        # node j=m+1 has edges m,m+1
        residual=float(np.max((wm*math.exp(rate)+wp*math.exp(-rate))/2-lam))
        global_tail_upper=math.sqrt(a*a+4)/(2*math.pi)
        usable=[j for j in range(m1+1,L) if v[j+L]>1e-13 and v[m1+L]>1e-13]
        dominance=max([math.log(v[j+L]/v[m1+L])+rate*(j-m1) for j in usable],default=None)
        c2=np.sin(np.minimum(np.maximum((np.abs(m)-K)/K,0),1)*math.pi/2)**2
        cmass=float(np.dot(c2,v*v))
        out11.append(dict(eps=eps,K=K,m1=m1,theta1=theta1,Lambda=lam,q=qenv,p=rate,
                          envelope_gap=lam-qenv,exterior_upper=global_tail_upper,
                          supersolution_residual=residual,domination_log_excess=dominance,
                          components_above_noise=len(usable),noise_floor=1e-13,
                          c_mass=cmass,boundary_mass=float(v[m1+L]**2),geometric_second_moment=closed,
                          analytic_tail_formula_value=tail_bound,
                          scope='finite diagnostic; the infinite bound is established analytically in L6'))
    row('V11',all(x['theta1']<2*math.pi and .5<x['q']<x['Lambda'] and x['exterior_upper']<.5
                 and x['supersolution_residual']<=1e-14
                 and (x['domination_log_excess'] is None or x['domination_log_excess']<=1e-9)
                 and x['boundary_mass']<=x['c_mass']+1e-14 for x in out11),
        cases=out11,scope='L5-L6 replacement: constant exterior envelope, positive supersolution, finite above-noise comparisons')

    def w_of(a, th):
        return a * abs(np.exp(0) - np.exp(-a + 1j * th)) / (math.sqrt(a * a + th * th) * (1 - math.exp(-a)))
    viol_lo = viol_up = viol_tail = viol_mono = viol_star = -1.
    for a in (1e-3, .01, .1, .3, .5):
        for th in np.linspace(1e-4, 5.4, 3000):
            g = 1 - w_of(a, th); y = (th * th + a * a) / 12
            viol_lo = max(viol_lo, th * th / 24 * (1 - th * th / 30) - a * a / 24 - g)
            viol_up = max(viol_up, g - (y / 2 + y * y / 2))
        for th in np.linspace(.05, 60., 30000):
            g = 1 - w_of(a, th)
            viol_tail = max(viol_tail, min(th ** 4 / (36 * (a * a + th * th)), .27) - g)
        th = np.linspace(1e-6, 2 * math.pi, 20000)
        ww = np.array([w_of(a, t) for t in th])
        viol_mono = max(viol_mono, float(np.max(np.diff(ww))))
        ws_ = w_of(a, 3.8)
        viol_star = max(viol_star, max(w_of(a, t) for t in np.linspace(3.8, 200., 50000)) - ws_)
    row("V12", viol_lo <= 0 and viol_up <= 0 and viol_tail <= 0 and viol_mono <= 0 and viol_star <= 0 and tr < 1e-12,
        violations=dict(lower=viol_lo, upper=viol_up, tail=viol_tail, monotone=viol_mono, star=viol_star),
        transcendental_identity_error=float(tr), scope="(24)-(27) on grids; finite floating-point checks, not universal proofs")

    c1 = 1 / (2 * math.sqrt(3)); c2 = math.sqrt(3) / 2
    rowsbl = []
    for h in [.1, .03, .01, .003, .001]:
        L = 900; m = np.arange(-L, L + 1, dtype=float); om_ = (2 * m[:-1] + 1)
        w_ = np.abs(np.expm1((-1 + 1j * om_) * h)) / (np.sqrt(1 + om_ * om_) * (-np.expm1(-h)))
        val, vec = eigh_tridiagonal(np.zeros(len(m)), w_ / 2, select='i', select_range=(len(m) - 1, len(m) - 1))
        v = np.abs(vec[:, 0]); v /= np.linalg.norm(v)
        z = float(np.dot(m * m, v * v))
        rowsbl.append(dict(kappa_h=h, deficit_over_delta_h=float((1 - val[0]) / h), energy_times_delta_h=float(z * h),
                           edge_mass=float(v[0] ** 2 + v[-1] ** 2)))
    dev = [max(abs(x['deficit_over_delta_h'] - c1), abs(x['energy_times_delta_h'] - c2)) for x in rowsbl]
    row("V13", all(dev[i + 1] < dev[i] for i in range(len(dev) - 1)) and dev[-1] < 1e-4 and all(x['edge_mass'] < 1e-30 for x in rowsbl),
        table=rowsbl, target_constants=dict(deficit=c1, energy=c2), deviations=dev,
        scope="monotone convergence to the T-BL constants at delta/kappa=1, L=900; consistent with the theorem, not its proof")

    vals = []
    for eps in (.002, .001, .0005):
        a = eps; L = int(30 * math.sqrt(1 / eps))
        lam, v, m, w_ = top(eps, a, L)
        z = float(np.dot(m * m, v * v))
        vals.append((eps, ((1 - lam) - eps / (2 * math.sqrt(3))) / eps ** 2, z - math.sqrt(3) / (2 * eps), ((1 - lam) * z - .25) / eps))
    (e1, c1_, z1, p1), (e2, c2_, z2, p2) = vals[-2], vals[-1]
    rr = e1 / e2
    rich = dict(c2=(rr * c2_ - c1_) / (rr - 1), dzeta=(rr * z2 - z1) / (rr - 1), dprod=(rr * p2 - p1) / (rr - 1))
    targets = dict(c2=-1 / 20, dzeta=1 / 20, dprod=-1 / (20 * math.sqrt(3)))
    if fault == "fake-second-order-constant":
        targets['c2'] = -1 / 25
    dev2 = max(abs(rich[k] - targets[k]) for k in targets)
    near("X01", dev2, 2e-4, richardson=rich, targets=targets,
         samples=[dict(eps=e, c2=c, dzeta=z, dprod=p) for e, c, z, p in vals],
         scope="diagnostic for the CONJECTURE (34); not evidence for a theorem")

    # ---- appendix A : conditional boundary-current witness --------------------
    up = [3, 1]; um = [3, -1]
    Hp = [[4, 3], [3, -4]]; Hm = [[4, -3], [-3, -4]]
    mv = lambda H, u: [sum(H[i][j] * u[j] for j in range(2)) for i in range(2)]
    jp_im = -up[1]; jm_im = -um[1]
    if fault == "lose-current-sign": jm_im = jp_im
    current_cross = Q(jp_im * jm_im, 10)
    Fabs2 = Q(4, 5); gamma2 = Q(1, 4)
    cross = gamma2 * Fabs2 * current_cross
    row("C07", mv(Hp, up) == [5 * x for x in up] and mv(Hm, um) == [5 * x for x in um]
        and sum(x * x for x in up) == 10 and sum(x * x for x in um) == 10
        and current_cross == Q(-1, 10) and cross == Q(-1, 50),
        spinor_numerators=[up, um], norm_squared=10, current_cross=str(current_cross), coupling_cross=str(cross),
        coupling_intensity=str(gamma2 * Fabs2 / 10), scope="(A1)-(A2): exact spinor eigenrelations and mixed amplitude of the declared vertex")

    Fz = (4 + 2j) / 5; gam = .5
    g0 = -1j * gam * Fz / math.sqrt(10); g1 = -g0
    omega_ = math.sqrt(10); Omega = omega_ - 1
    H4 = np.diag([0., 0., Omega, Omega]).astype(complex)
    H4[2, 0] = g0; H4[0, 2] = g0.conjugate(); H4[3, 1] = g1; H4[1, 3] = g1.conjugate()
    out14 = []
    for T in (.3, 1., 2.):
        U = expm(-1j * T * H4)
        Rabi = math.sqrt(Omega * Omega + 4 * abs(g0) ** 2)
        eta = 4 * abs(g0) ** 2 / Rabi ** 2 * math.sin(Rabi * T / 2) ** 2
        for beta in (0., math.pi / 2, .4):
            ep = np.array([0, 0, 1, np.exp(1j * beta)]) / math.sqrt(2)
            em = np.array([0, 0, 1, -np.exp(1j * beta)]) / math.sqrt(2)
            prob = []; momentum = []
            for s in (1, -1):
                init = np.array([1, s, 0, 0], complex) / math.sqrt(2)
                psi = U @ init
                prob.append([abs(np.vdot(ep, psi)) ** 2, abs(np.vdot(em, psi)) ** 2, float(np.sum(abs(psi[:2]) ** 2))])
                momentum.append([abs(psi[2]) ** 2, abs(psi[3]) ** 2, float(np.sum(abs(psi[:2]) ** 2))])
            tv = float(np.abs(np.array(prob[0]) - prob[1]).sum() / 2)
            blind = float(np.abs(np.array(momentum[0]) - momentum[1]).sum() / 2)
            target = eta * abs(math.cos(beta))
            if fault == "force-eraser-blind": target = 0.
            out14.append(dict(T=T, beta=beta, eta=eta, TV=tv, predicted=target, momentum_record=blind,
                              normalization_error=max(abs(sum(p) - 1) for p in prob),
                              unitary_error=float(np.linalg.norm(U.conj().T @ U - np.eye(4)))))
    near("V14", max(max(abs(x['TV'] - x['predicted']), x['momentum_record'], x['normalization_error'], x['unitary_error']) for x in out14),
         1e-12, cases=out14, scope="(A3)-(A5): exact four-state unitary; coherent detector gives eta|cos beta|, momentum detector 0")

    runtime = {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__}
    return rows, tables, runtime


# ---------------------------------------------------------------------------
# v1.1 audit regressions. No import of either predecessor verifier is required.
# The paired checks read the LIVE displayed formulae, not the correction table.
# ---------------------------------------------------------------------------
def live_parameters(text):
    """Parse only deliberately narrow, displayed formulae; reject missing forms.

    This is not a LaTeX theorem prover. These fields feed actual computations.
    Changing prose outside these formulae still requires mathematical review.
    """
    if text is None:
        return dict(phase=-1, beta=-1, reflection=0, tail_mode='maximum',
                    mixed=Q(-1, 480), include_no_click=True)
    def section(start, end):
        return text.split(start, 1)[1].split(end, 1)[0]
    cal = section('## 4.', '## 5.')
    refl = section('**Vertex reflection.**', '*Step 1')
    taylor = section('**Local coefficient correction.**', 'The table below')
    far = section('**Legacy-bound regression.', '### 6.4')
    scope = section('### 8.1', '### 8.2')
    phase = re.search(r'\\kappa e\^{\s*-\\kappa t\s*([+-])\s*i\\omega_\{q-1\}t\s*}', cal)
    beta = re.search(r'\\beta_\{q,j\}\s*=\s*([+-])\\arg', cal)
    reflection = re.search(r'v_\{(-m|-1-m)\}=v_m', refl)
    mixed = re.search(r'([+-])\\frac\{a\^2\\theta\^2\}\{(\d+)\}', taylor)
    if not all((phase, beta, reflection, mixed)):
        raise ValueError('Live equation parsing failed: phase, beta, reflection, or mixed coefficient')
    tail_mode = ('maximum' if 'q^{\\rm old}_\\varepsilon=\\max\\{w_{M_0},w_*\\}' in far
                 else 'floor_only' if 'q^{\\rm old}_\\varepsilon=w_*' in far else None)
    if tail_mode is None:
        raise ValueError('Live legacy-bound definition is missing')
    include = 'D^{\\max}_{h,T}=(1-e^{-\\kappa T})\\Lambda_w(h)' in scope
    return dict(phase=1 if phase.group(1)=='+' else -1,
                beta=1 if beta.group(1)=='+' else -1,
                reflection=0 if reflection.group(1)=='-m' else -1,
                mixed=Q(1 if mixed.group(1)=='+' else -1, int(mixed.group(2))),
                tail_mode=tail_mode, include_no_click=include)


def run_revision_checks(paper_text, fault, science_rows):
    import cmath
    import numpy as np
    from scipy.integrate import quad
    from scipy.linalg import eigh_tridiagonal
    from scipy.sparse import diags
    from scipy.sparse.linalg import eigsh
    out = {}
    def emit(rid, ok, **data):
        out[rid] = dict(id=rid, **{'class':CLASS_OF[rid]}, claim=CLAIM_OF[rid],
                        status='PASS' if bool(ok) else 'FAIL', evidence=data)
    p = live_parameters(paper_text)

    # V15: Schrödinger evolution with a complex off-diagonal; phase comes from paper.
    phase_cases = []
    for alpha in (0., .37, -1.2):
        psi = np.array([1., np.exp(1j*alpha)])/math.sqrt(2)
        sigma = np.outer(psi, psi.conj())
        energies = np.array([0., 1., 0., 1.])
        integral = -np.expm1(-1 + p['phase']*1j)/(1-p['phase']*1j)
        beta = p['beta']*np.angle(sigma[1,0]*integral)
        def distribution(sign, b):
            rho = np.kron(np.array([[1.,sign],[sign,1.]])/2, sigma)
            probs = []
            for indices in ([0], [1,2], [3]):
                for r in (1,-1):
                    ket = np.zeros(4, complex); ket[indices[0]]=1/math.sqrt(2)
                    if len(indices)==2: ket[indices[1]]=r*np.exp(1j*b)/math.sqrt(2)
                    def density(t):
                        u = np.exp(-1j*energies*t)
                        rt = u[:,None]*rho*u.conj()[None,:]
                        return math.exp(-t)*float(np.vdot(ket,rt@ket).real)
                    probs.append(quad(density,0.,1.,epsabs=1e-13,epsrel=1e-13)[0])
            return np.array(probs+[math.exp(-1)])
        pp,pm = distribution(1,beta),distribution(-1,beta)
        tv = float(np.abs(pp-pm).sum()/2)
        expected = abs(-np.expm1(-1-1j)/(1+1j))/2
        old_beta = -np.angle(sigma[1,0]*(-np.expm1(-1+1j)/(1-1j)))
        old_tv = float(np.abs(distribution(1,old_beta)-distribution(-1,old_beta)).sum()/2)
        phase_cases.append(dict(alpha=alpha,beta=float(beta),actual_tv=tv,expected=expected,
                                wrong_sign_tv=old_tv,normalization_error=max(abs(pp.sum()-1),abs(pm.sum()-1)),
                                minimum_probability=float(min(pp.min(),pm.min()))))
    emit('V15',all(abs(x['actual_tv']-x['expected'])<1e-12 and x['normalization_error']<1e-12
                   and x['minimum_probability']>=-1e-14 for x in phase_cases),
         parameters={k:p[k] for k in ('phase','beta')},cases=phase_cases,
         scope='F01/A01: paper-fed phase, full Born output, three finite complex references')

    def weight(theta,a):
        return a*np.abs(np.expm1(-a+1j*np.asarray(theta)))/(np.hypot(a,theta)*-np.expm1(-a))
    def top(eps,cut=500):
        mm=np.arange(-cut,cut+1,dtype=float); ww=weight(2*eps*(mm[:-1]+.5),eps)
        vals,vec=eigh_tridiagonal(np.zeros(len(mm)),ww/2,select='i',select_range=(len(mm)-1,len(mm)-1))
        vv=np.abs(vec[:,0]); vv/=np.linalg.norm(vv)
        return mm,vv,float(vals[0]),ww
    mm,vv,lam,ww=top(.001)
    by_index={int(k):float(v) for k,v in zip(mm,vv)}
    refl_err=max(abs(v-by_index[-int(k)+p['reflection']]) for k,v in zip(mm,vv)
                 if -int(k)+p['reflection'] in by_index)
    wrong_err=max(abs(v-by_index[-int(k)-1]) for k,v in zip(mm,vv) if -int(k)-1 in by_index)
    matrix=diags([ww/2,ww/2],[-1,1],shape=(len(mm),len(mm)),format='csr')
    commute=float(np.max(np.abs((matrix@vv)[::-1]-matrix@vv[::-1])))
    emit('V16',refl_err<1e-10 and commute<1e-12 and wrong_err>1e-4,
         reflection_offset=p['reflection'],symmetry_residual=refl_err,commutator_residual=commute,
         old_symmetry_residual=wrong_err,scope='F02/A02: finite eigenvector; universal edge/vertex proof in section 6.3')

    eps=.001; M0=math.floor(math.pi/(2*eps)-.5)
    wM=float(weight(2*eps*(M0+.5),eps)); ws=float(weight(3.8,eps))
    qold=max(wM,ws) if p['tail_mode']=='maximum' else ws
    actual=math.acosh(lam/max(wM,ws)); bound=math.acosh(lam/qold)
    emit('V17',actual+1e-13>=bound and bound>1 and math.acosh(lam/ws)>actual+.2,
         M0=M0,w_M0=wM,w_star=ws,actual_p_M0=actual,declared_lower_bound=bound,
         false_v1_0_lower_bound=math.acosh(lam/ws),scope='F03/A03: corrected legacy M0 comparison; v1.1 proof uses L6 instead')

    # C08: exact bivariate coefficient identity, without symbolic-library dependencies.
    # With A=a^2, B=theta^2, 1-w^2=[B-4 rho^2 sin^2(theta/2)]/(A+B).
    # To total degree 3 in (A,B), the numerator must be (A+B)*(B/12-A*B/240-B^2/360).
    def mul(f,g):
        h=collections.defaultdict(Q)
        for (i,j),x in f.items():
            for (k,l),y in g.items(): h[i+k,j+l]+=x*y
        return {k:v for k,v in h.items() if v}
    rho2={(0,0):Q(1),(1,0):Q(-1,12),(2,0):Q(1,240)}
    four_sin2={(0,1):Q(1),(0,2):Q(-1,12),(0,3):Q(1,360)}
    numerator={k:-v for k,v in mul(rho2,four_sin2).items() if sum(k)<=3}
    numerator[0,1]+=1; numerator={k:v for k,v in numerator.items() if v}
    y={(0,1):Q(1,12),(1,1):Q(-1,240),(0,2):Q(-1,360)}
    identity=mul({(1,0):Q(1),(0,1):Q(1)},y)==numerator
    theta4=y[0,2]/2+y[0,1]**2/8
    mixed=y[1,1]/2
    # rho^2 is inverse of (sinh(a/2)/(a/2))^2 through a^4.
    sinh_ratio_square=[Q(1),Q(1,12),Q(1,360)]
    inverse=[Q(1),rho2[1,0],rho2[2,0]]
    inverse_res=[sum(sinh_ratio_square[j]*inverse[k-j] for j in range(k+1)) for k in (1,2)]
    emit('C08',identity and all(x==0 for x in inverse_res) and mixed==p['mixed'] and theta4==Q(-1,1920),
         mixed=str(mixed),paper_mixed=str(p['mixed']),theta4=str(theta4),rho_inverse_residuals=list(map(str,inverse_res)),
         scope='F04/A04: exact polynomial coefficients through total degree four; no spectral perturbation theorem')

    # C09: infinite geometric second moment by an exact recurrence, not truncation.
    moments=[]
    for r in (Q(1,4),Q(1,2),Q(9,10)):
        for M in (1,17,356):
            S=lambda n: Q(n*n)/(1-r)+2*n*r/(1-r)**2+r*(1+r)/(1-r)**3
            residual=S(M)-M*M-r*S(M+1)
            shifted=r*(M*M/(1-r)+2*M/(1-r)**2+(1+r)/(1-r)**3)
            closed_diff=shifted-r*S(M+1)
            moments.append(dict(r=str(r),M=M,residual=str(residual),shifted_residual=str(closed_diff)))
    emit('C09',all(x['residual']=='0' and x['shifted_residual']=='0' for x in moments),cases=moments,
         scope='Exact geometric-series recurrence; infinite-tail convergence follows from 0<r<1 in L6')

    certs=science_rows['C03']['evidence']['certificates']
    zstate=np.array([0.,1.,0.]); arbitrary_score=float(np.dot(zstate[:-1],zstate[1:]))
    emit('W02',arbitrary_score==0 and all(Q(c['lower_rational'])>0 for c in certs)
         and all(c['certificate_ok'] for c in certs),
         energy=float(zstate@np.diag([1.,0.,1.])@zstate),record=arbitrary_score,
         optimum_lower_bounds=[c['lower_rational'] for c in certs],
         scope='F05/A05: admissible zero-record state refutes a universal positive lower endpoint; C03 provides feasible lower witnesses')

    finite=[]
    for ep in (.02,.005,.001):
        m,v,L,w=top(ep); z=float(np.dot(m*m,v*v)); normalized=(1-L)*z
        for regime,noclick in (('fixed_T',math.exp(-1)),('o(eps)',ep**2),('c_eps',2*ep)):
            Ttarget=-math.log(noclick); bins=math.ceil(Ttarget/ep); T=bins*ep
            n=math.exp(-T)
            D=(1-n)*L if p['include_no_click'] else L
            lhs=(1-D)*z; rhs=n*z+(1-n)*normalized
            finite.append(dict(eps=ep,regime=regime,bins=bins,T=T,no_click_over_eps=n/ep,
                               product=lhs,normalized_product=normalized,identity_error=abs(lhs-rhs)))
    err=max(x['identity_error'] for x in finite)
    last={x['regime']:x for x in finite if x['eps']==.001}
    finite_static_tv=abs(-np.expm1(-1-1j)/(1+1j))/2
    naive_static_rescaling=(1-math.exp(-1))/(2*math.sqrt(2))
    emit('V18',abs(finite_static_tv-naive_static_rescaling)>.05 and err<2e-10 and last['fixed_T']['product']>100 and abs(last['o(eps)']['product']-.25)<.002
         and abs(last['c_eps']['product']-(.25+math.sqrt(3)))<.005,
         identity_error=err,cases=finite,finite_window_static_tv=float(finite_static_tv),
         invalid_rescaled_infinite_static_tv=naive_static_rescaling,scope='F06/A07: exact finite-window identity and three finite sequences with T=B*h')

    paths=[]
    for variance in (10.,30.,100.):
        ep=variance**-2; cut=math.ceil(12*math.sqrt(variance)); m=np.arange(-cut,cut+1,dtype=float)
        v=np.exp(-m*m/(4*variance));v/=np.linalg.norm(v)
        w=weight(2*ep*(m[:-1]+.5),ep)
        score=float(np.dot(w,v[:-1]*v[1:])); z=float(np.dot(m*m,v*v))
        paths.append(dict(eps=ep,energy=z,eps_energy=ep*z,score=score,product=(1-score)*z))
    emit('W03',abs(paths[-1]['product']-.125)<1e-4 and paths[-1]['product']<.13,
         cases=paths,scope='A08: positive-resolution Gaussian path; supports analytic path argument in section 8.1')

    cross=[]
    for ep in (.02,.005,.001):
        m,v,L,w=top(ep)
        op=diags([w/2,w/2],[-1,1],shape=(len(m),len(m)),format='csr')
        trial=np.exp(-m*m*ep/4);trial/=np.linalg.norm(trial)
        values,vectors=eigsh(op,k=1,which='LA',v0=trial,tol=2e-14,maxiter=20000)
        zvec=np.abs(vectors[:,0]);zvec/=np.linalg.norm(zvec)
        other=float(zvec@(op@zvec));z=float(np.dot(m*m,zvec*zvec))
        cross.append(dict(eps=ep,Lambda=other,energy=z,product=(1-other)*z,
                          eigen_route_error=abs(other-L),energy_route_error=abs(z-float(np.dot(m*m,v*v))),
                          residual=float(np.linalg.norm(op@zvec-other*zvec))))
    emit('V19',all(x['eigen_route_error']<2e-12 and x['energy_route_error']<1e-7 and x['residual']<1e-10 for x in cross),
         cases=cross,scope='A06: ARPACK vs tridiagonal eigenpairs; neither certifies the infinite moment. A09 is covered by C03/V08.')
    return out


# ---------------------------------------------------------------------------
# package rows (read the manuscript)
# ---------------------------------------------------------------------------
def v12_parameters(text):
    """Read a small, declared subset of live equations; not semantic validation."""
    out = dict(gap_offset=1, joint_sqrt=True, sep_constant=math.pi,
               envelope_relation='upper', sinc_denominator=2)
    if text is None:
        return out
    sec = text.split('## 7. Joint charge',1)[1].split('## 8.',1)[0]
    out['gap_offset'] = int(re.search(r'For \$d_m=2m\+(\d+)\$',sec).group(1))
    if r'With $n=\lfloor\sqrt N\rfloor$' in sec:
        out['joint_sqrt'] = True
    elif r'With $n=\lfloor N\rfloor$' in sec:
        out['joint_sqrt'] = False
    else:
        raise ValueError('R5 floor/square-root declaration not parsed')
    val = re.search(r'\\lim N\(1-\\mathcal D_N\^\{\\rm sep\}\)=(\\pi(?:/2)?)\s*,',sec).group(1)
    out['sep_constant'] = math.pi/2 if val.endswith('/2') else math.pi
    rel = re.search(r'\\mathcal D_N\^\{\\rm sep\}\s*(\\le|=)\\lambda_\{\\max\}\(A_\{u,N\}\)',sec).group(1)
    out['envelope_relation'] = 'upper' if rel == r'\le' else 'equality'
    den = re.search(r'\\frac\{\(1-r\)\\tau\(2m\+1\)\}(?:\{(\d+)\}|(\d+))',sec).groups()
    out['sinc_denominator'] = int(next(x for x in den if x))
    return out


def run_v12_checks(text, fault):
    """Finite attacks on the new joint/separable reference theorems."""
    import numpy as np
    from scipy.linalg import eigh_tridiagonal
    from scipy.sparse import diags
    from scipy.sparse.linalg import eigsh
    from scipy.integrate import quad
    out = {}; tables = {}; p = v12_parameters(text)
    if fault == 'linear-rotor-gap': p['gap_offset'] = 2
    if fault == 'wrong-joint-length': p['joint_sqrt'] = False
    if fault == 'treat-mode-envelope-as-exact': p['envelope_relation'] = 'equality'
    if fault == 'wrong-bandwidth-constant': p['sep_constant'] = math.pi/2
    if fault == 'drop-detuning-half': p['sinc_denominator'] = 1

    def emit(rid,ok,**ev):
        out[rid] = dict(id=rid, **{'class':CLASS_OF[rid]}, claim=CLAIM_OF[rid],
                        status='PASS' if bool(ok) else 'FAIL', evidence=ev)

    def graph(N,rad,r=Q(1)):
        """Energy equality independently enumerated, without the gap formula."""
        labels=[(m,k) for m in range(-rad,rad+1) for k in range(N+1)]
        energies={(m,Q(m*m)+r*k):i for i,(m,k) in enumerate(labels)}; edges=[]
        for i,(m,k) in enumerate(labels):
            j=energies.get((m+1,Q(m*m)+r*k))
            if j is not None: edges.append((i,j))
        return labels,edges

    def gamma(rho,labels,offset=1):
        lookup={x:i for i,x in enumerate(labels)}; val=0.
        for i,(m,k) in enumerate(labels):
            j=lookup.get((m+1,k-(2*m+offset)))
            if j is not None: val+=abs(rho[i,j])
        return float(val)

    def largest_component(labels,edges):
        adj=[[] for _ in labels]
        for i,j in edges: adj[i].append(j);adj[j].append(i)
        seen=set(); sizes=[]
        for i in range(len(labels)):
            if i in seen:continue
            stack=[i];seen.add(i);size=0
            while stack:
                u=stack.pop();size+=1
                for v in adj[u]:
                    if v not in seen:seen.add(v);stack.append(v)
            sizes.append(size)
        return max(sizes,default=1)

    # C10: exact charge/energy matching, including negative gaps and end levels.
    tested=0;ok=True
    for N in range(13):
        labels,edges=graph(N,8);actual=set(edges);lookup={x:i for i,x in enumerate(labels)}
        expected=set()
        for i,(m,k) in enumerate(labels):
            j=lookup.get((m+1,k-(2*m+1)))
            if j is not None:expected.add((i,j))
        ok &= actual==expected
        for i,j in edges:
            m,k=labels[i];mp,kp=labels[j]
            ok &= 1+m==mp and m*m+k==mp*mp+kp;tested+=1
    emit('C10',ok,exact_edges=tested,bandwidths=list(range(13)),rotor_radius=8,
         arithmetic='integer/Fraction',scope='finite complete enumeration of both conserved eigenvalues versus R2')

    # V20: full twirled matrices and Born probabilities versus edge formula.
    rng=np.random.default_rng(712020);err=0.;bornerr=0.;commerr=0.;cases=0
    X=np.array([[0.,1.],[1.,0.]])
    plus=np.array([[.5,.5],[.5,.5]]);minus=np.array([[.5,-.5],[-.5,.5]])
    for N in (1,2,3):
        labels,_=graph(N,3);dim=len(labels)
        qs=np.array([s+m for s in (0,1) for m,k in labels])
        es=np.array([m*m+k for s in (0,1) for m,k in labels])
        mask=(qs[:,None]==qs[None,:])
        if fault!='ignore-energy-twirl':mask=mask & (es[:,None]==es[None,:])
        for _ in range(6):
            z=rng.normal(size=(dim,5))+1j*rng.normal(size=(dim,5));rho=z@z.conj().T;rho/=np.trace(rho)
            diff=np.kron(X,rho);tw=diff*mask
            ev,vec=np.linalg.eigh(tw)
            true_tv=float(np.abs(ev).sum()/2);form=gamma(rho,labels,p['gap_offset'])
            signs=np.where(abs(ev)>1e-12,np.sign(ev),0.)
            effect=(vec*((1+signs)/2))@vec.conj().T
            pd=float(np.trace(effect@np.kron(plus-minus,rho)).real)
            err=max(err,abs(true_tv-form));bornerr=max(bornerr,abs(pd-true_tv))
            commerr=max(commerr,float(np.max(np.abs(effect*(qs[:,None]-qs[None,:])))),
                        float(np.max(np.abs(effect*(es[:,None]-es[None,:])))))
            cases+=1
    emit('V20',err<2e-12 and bornerr<2e-12 and commerr<2e-10,
         cases=cases,trace_norm_error=err,born_error=bornerr,commutator_error=commerr,
         parsed_gap_offset=p['gap_offset'],scope='raw complex mixed matrices; full charge/energy pinching and Helstrom Born probabilities')

    # V21: independently enumerated shell graphs, plus direct dense eigenvalues.
    gerr=0.;eigerr=0.;samples=[]
    for N in range(65):
        rad=max(2,(N+1)//2+1);labels,edges=graph(N,rad)
        L=largest_component(labels,edges)
        ni=math.isqrt(N) if p['joint_sqrt'] else N
        pred=math.cos(math.pi/(2*ni+2));actual=math.cos(math.pi/(L+1)) if L>1 else 0.
        gerr=max(gerr,abs(pred-actual))
        if N<=8:
            A=np.zeros((len(labels),len(labels)))
            for i,j in edges:A[i,j]=A[j,i]=.5
            eigerr=max(eigerr,abs(float(np.linalg.eigvalsh(A)[-1])-actual))
        if N in (0,1,2,3,4,8,9,16,25,64):samples.append(dict(N=N,longest_vertices=L,joint=actual))
    emit('V21',gerr<2e-14 and eigerr<2e-12,graph_error=gerr,dense_eigenvalue_error=eigerr,
         enumerated_bandwidths='0..64',samples=samples,
         scope='finite graph enumeration; the manuscript proves exclusion of every unenumerated high-energy shell')

    # C11: rational spectral resonance, using exact energy equalities on a complete edge range.
    ar_cases=[];ok=True
    for N in (0,1,2,3,4,5,8):
        for numerator in range(1,10):
            for denominator in range(1,7):
                if math.gcd(numerator,denominator)!=1:continue
                r=Q(numerator,denominator)
                rad=(numerator*N)//denominator+2
                labels,edges=graph(N,rad,r)
                L=largest_component(labels,edges)
                if numerator==1:expected=2*math.isqrt(N//denominator)+1
                elif numerator%2==1 and N>=denominator:expected=2
                else:expected=1
                ok &= L==expected
                ar_cases.append((N,numerator,denominator,L))
    emit('C11',ok,cases=len(ar_cases),arithmetic='Fraction, no floating resonance tolerance',
         representative=[x for x in ar_cases if x[0]==4 and (x[1],x[2]) in ((1,1),(1,2),(3,2),(2,1),(7,5))],
         irrational_scope='proved from integer/nonzero gap in text, not approximated by floating samples',
         scope='R17 numerator parity, minimal denominator bandwidth, and reciprocal-integer ladders')

    # W04: entangled N=1 state, its marginals, and matched product optimum.
    N=1;labels,_=graph(N,1);v=np.zeros(6)
    v[labels.index((-1,0))]=.5;v[labels.index((0,1))]=1/math.sqrt(2);v[labels.index((1,0))]=.5
    rho=np.outer(v,v);tensor=rho.reshape(3,2,3,2)
    rhoR=np.trace(tensor,axis1=1,axis2=3);rhoC=np.trace(tensor,axis1=0,axis2=2)
    joint=gamma(rho,labels);marg=gamma(np.kron(rhoR,rhoC),labels)
    ppt=float(np.linalg.eigvalsh(tensor.transpose(0,3,2,1).reshape(6,6))[0])
    a=np.array([.5,1/math.sqrt(2),.5]);b=np.ones(2)/math.sqrt(2)
    prod=gamma(np.outer(np.kron(a,b),np.kron(a,b)),labels)
    expected_marg=joint if fault=='product-marginals-have-record' else 0.
    energies=np.array([m*m+k for m,k in labels]);stat=float(np.max(abs(rho*(energies[:,None]-energies[None,:]))))
    emit('W04',abs(joint**2-.5)<2e-14 and abs(prod**2-.125)<2e-14 and abs(marg-expected_marg)<2e-14
         and abs(ppt+.5)<2e-14 and stat==0.,joint=joint,product_optimum=prod,
         product_of_marginals=marg,partial_transpose_minimum=ppt,stationarity_error=stat,
         rotor_energy=float(np.dot(v*v,[m*m for m,k in labels])),compensator_marginal=rhoC.tolist(),
         scope='one unconditional matched-bandwidth witness; marginal substitution cannot preserve its record')

    def env(N,d):
        d=np.asarray(d,dtype=int)
        return np.where(d<=N,np.cos(np.pi/(N//d+2)),0.)

    def corr_sine(N,d):
        d=np.asarray(d,dtype=float);B=N+2.;theta=np.pi/B
        first=(1-d/B)*np.cos(d*theta)
        second=np.sin(d*theta)/(B*np.tan(theta))
        if fault=='omit-sine-boundary-term':second=np.zeros_like(second)
        return np.where(d<=N,first+second,0.)

    def top_weight(w):
        return float(eigh_tridiagonal(np.zeros(len(w)+1),np.asarray(w)/2,
                                     select='i',select_range=(len(w),len(w)))[0][0])

    # V22: common-state multimode product expression, not independent mode optimisation.
    err=0.;violation=0.;cases=0
    for N in (1,2,3,4,8):
        labels,_=graph(N,5);mm=np.arange(-5,6)
        for _ in range(12):
            a=rng.normal(size=11)+1j*rng.normal(size=11);a/=np.linalg.norm(a)
            b=rng.normal(size=N+1)+1j*rng.normal(size=N+1);b/=np.linalg.norm(b)
            v=np.kron(a,b);rho=np.outer(v,v.conj());direct=gamma(rho,labels)
            c={d:float(np.dot(abs(b[:-d]),abs(b[d:]))) for d in range(1,N+1)}
            factor=sum(abs(a[i]*a[i+1])*c.get(abs(2*int(m)+1),0.) for i,m in enumerate(mm[:-1]))
            err=max(err,abs(direct-factor))
            violation=max(violation,max((c[d]-float(env(N,d)) for d in c),default=0.));cases+=1
    emit('V22',err<2e-13 and violation<2e-13,cases=cases,factorisation_error=err,
         max_bound_violation=violation,scope='pure complex products and simultaneous mode bounds for one compensator state')

    # V23: explicit autocorrelation checked against its finite defining sum.
    err=0.;cases=0
    for N in (1,2,3,4,8,16,31,64,257):
        b=np.sqrt(2/(N+2))*np.sin(np.pi*(np.arange(N+1)+1)/(N+2))
        for d in range(1,N+2):
            direct=float(b[:-d]@b[d:]) if d<=N else 0.
            err=max(err,abs(direct-float(corr_sine(N,d))));cases+=1
    emit('V23',err<3e-13,cases=cases,max_error=err,scope='R10 includes the finite-interval boundary term')

    # W05: N=3 shows the independent-mode upper relaxation cannot be an equality.
    N=3;ev,vec=eigh_tridiagonal(np.zeros(4),np.ones(3)/2)
    b=abs(vec[:,-1]);c1=float(b[:-1]@b[1:]);c3=float(b[0]*b[-1])
    need1=float(env(N,1));need3=float(env(N,3))
    simultaneous=abs(c1-need1)<1e-12 and abs(c3-need3)<1e-12
    contract_ok=(p['envelope_relation']=='upper' or simultaneous)
    emit('W05',contract_ok and not simultaneous and need3-c3>.3,
         max_c1=need1,c3_at_unique_positive_c1_optimizer=c3,max_c3=need3,
         leading_eigenvalue_simple_gap=float(ev[-1]-ev[-2]),relation_declared=p['envelope_relation'],
         scope='Perron uniqueness for d=1 plus incompatible d=3 maximisation; strictness of upper relaxation at N=3')

    # C12: exact N=4 upper-envelope characteristic polynomial and separation.
    def xpoly(a):return [Q(0)]+a
    def subpoly(a,b):
        n=max(len(a),len(b));return [(a[i] if i<len(a) else Q(0))-(b[i] if i<len(b) else Q(0)) for i in range(n)]
    p0=[Q(1)];p1=[Q(0),Q(1)]
    for offdiag_squared in (Q(1,16),Q(3,16),Q(3,16),Q(1,16)):
        p0,p1=p1,subpoly(xpoly(p1),[offdiag_squared*x for x in p0])
    expected=[Q(0),Q(7,256),Q(0),Q(-1,2),Q(0),Q(1)]
    emit('C12',p1==expected and Q(7,16)<Q(3,4),
         characteristic_coefficients=[str(x) for x in p1],
         factorisation='x*(x^2-1/16)*(x^2-7/16)',
         separable_upper_squared='7/16',joint_optimum_squared='3/4',
         scope='exact finite N=4 spectral upper certificate; the exact separable optimum is not asserted')

    # V24: spectral squeeze for the sharp asymptotic coefficient.
    band=[]
    for N in (1,2,3,4,8,16,64,256,1024,4096,16384):
        rad=(N+1)//2;m=np.arange(-rad,rad);d=abs(2*m+1)
        lo=top_weight(corr_sine(N,d));up=top_weight(env(N,d));joint=math.cos(math.pi/(2*math.isqrt(N)+2))
        band.append(dict(N=N,separable_lower=lo,separable_upper=up,joint=joint,
                         sep_error_lower=N*(1-up),sep_error_upper=N*(1-lo),joint_error=N*(1-joint)))
    last=band[-1];target=p['sep_constant']
    emit('V24',all(x['separable_lower']<=x['separable_upper']+2e-12 and x['separable_upper']<x['joint'] for x in band)
         and abs(last['sep_error_lower']-target)<.05 and abs(last['sep_error_upper']-target)<.02
         and abs(last['joint_error']-math.pi**2/8)<.025,
         samples=band,parsed_separable_constant=target,
         scope='finite asymptotic diagnostics for both bounding matrices; analytic liminf/limsup proof is in T-SBC')
    tables['BAND']=[f"| {x['N']} | {x['separable_lower']:.9f} | {x['separable_upper']:.9f} | {x['joint']:.9f} | {x['sep_error_lower']:.6f}–{x['sep_error_upper']:.6f} |" for x in band]

    # V25: a different eigensolver and a fixed starting vector.
    cross=[]
    for N in (8,32,128,512):
        rad=(N+1)//2;m=np.arange(-rad,rad);d=abs(2*m+1)
        for name,w in (('upper',env(N,d)),('lower',corr_sine(N,d))):
            A=diags([w/2,w/2],[-1,1],shape=(len(w)+1,len(w)+1),format='csr')
            sites=np.arange(-rad,rad+1);v0=np.exp(-sites*sites/max(N,1))
            val,vec=eigsh(A,k=1,which='LA',v0=v0,tol=3e-14,maxiter=30000)
            residual=float(np.linalg.norm(A@vec[:,0]-val[0]*vec[:,0]))
            cross.append(dict(N=N,kind=name,error=abs(float(val[0])-top_weight(w)),residual=residual))
    emit('V25',all(x['error']<3e-12 and x['residual']<2e-11 for x in cross),cases=cross,
         scope='ARPACK sparse eigenpair versus tridiagonal solver; neither proves a limit')

    # V26: the phase frequency is computed from the two actual basis energies.
    dt=[];err=0.;violation=0.
    for N in (1,4,9):
        n=math.isqrt(N);m=np.arange(-n,n+1);s=np.cos(np.pi*m/(2*n+2))/math.sqrt(n+1)
        base=float(s[:-1]@s[1:])
        for r in (1.,1.017,.9):
            for tau in (.5,2.,9.):
                direct=0.;form=0.;moment=0.
                for i,mi in enumerate(m[:-1]):
                    k=N-int(mi)**2;kp=N-(int(mi)+1)**2
                    energy0=int(mi)**2+r*k;energy1=(int(mi)+1)**2+r*kp
                    hz=energy1-energy0
                    integ=quad(lambda t: math.cos(hz*t),-tau/2,tau/2,epsabs=1e-13)[0]/tau
                    coeff=float(s[i]*s[i+1]);direct+=coeff*abs(integ)
                    x=(1-r)*tau*(2*int(mi)+1)/p['sinc_denominator']
                    form+=coeff*abs(float(np.sinc(x/np.pi)));moment+=coeff*(2*int(mi)+1)**2
                loss=base-direct;bound=(1-r)**2*tau*tau*moment/24
                err=max(err,abs(direct-form));violation=max(violation,-loss,loss-bound)
                dt.append(dict(N=N,r=r,tau=tau,contrast=direct,loss=loss,bound=bound))
    emit('V26',err<2e-12 and violation<2e-12,cases=dt,quadrature_error=err,max_bound_violation=violation,
         parsed_sinc_denominator=p['sinc_denominator'],
         scope='finite-time charge-preserving POVM; exact energy invariance is not claimed at detuning')

    # V27: one common product state also obeys the matched mean rotor budget.
    gp=[]
    for N in (256,1024,4096,16384):
        var=N/(4*math.pi);cut=math.ceil(12*math.sqrt(var));m=np.arange(-cut,cut+1)
        a=np.exp(-m*m/(4*var));a/=np.linalg.norm(a);d=abs(2*m[:-1]+1)
        score=float(np.dot(a[:-1]*a[1:],corr_sine(N,d)))
        z=float(np.dot(a*a,m*m))
        gp.append(dict(N=N,score=score,mean_rotor_energy=z,energy_over_N=z/N,
                       scaled_error=N*(1-score),compensator_mean_energy=N/2))
    emit('V27',all(x['mean_rotor_energy']<x['N'] for x in gp) and abs(gp[-1]['scaled_error']-math.pi)<.025,
         cases=gp,scope='R14–R16 Gaussian/sine product witness; same additional mean rotor budget in both preparation classes')
    return out,tables




def run_v13_finite_certificate(fault):
    """Exact N=3 counterexample to finite-band optimality of the sine state.

    Rational correlations and a characteristic-polynomial recurrence suffice.
    The radical comparison is reduced to an integer inequality of known sign;
    no decimal solver or assertion of the global separable optimum is used.
    """
    raw = (3,2,2,3) if fault == 'swap-finite-witness-ratio' else (2,3,3,2)
    norm2 = sum(v*v for v in raw)
    c1 = Q(sum(raw[i]*raw[i+1] for i in range(3)), norm2)
    c3 = Q(raw[0]*raw[3], norm2)
    lam2 = (c3*c3+2*c1*c1)/4
    # Ascending powers of x for det(xI-A), from the actual four hoppings.
    p0, p1 = [Q(1)], [Q(0),Q(1)]
    for w in (c3,c1,c1,c3):
        xprev = [Q(0)]+p1
        for i,v in enumerate(p0): xprev[i] -= (w*w/4)*v
        p0,p1 = p1,xprev
    expected = [Q(0),c3*c3*lam2/4,Q(0),-(c3*c3/4+lam2),Q(0),Q(1)]
    # The sine-baseline square is (33+9 sqrt(5))/160.
    lhs = 160*lam2-33
    radical_margin = lhs*lhs-Q(405)
    ok = (c1==Q(21,26) and c3==Q(2,13) and lam2==Q(449,1352)
          and p1==expected and lhs>0 and radical_margin>0)
    return dict(id='C13', **{'class':'C'}, claim='T-SB',
                status='PASS' if ok else 'FAIL', evidence=dict(
                N=3, compensator_amplitude_numerators=list(raw), norm_squared=norm2,
                c1=str(c1), c3=str(c3), attained_contrast_squared=str(lam2),
                monic_characteristic_coefficients=list(map(str,p1)),
                sine_baseline_squared='(33+9*sqrt(5))/160',
                rational_lhs=str(lhs), positive_squared_comparison_margin=str(radical_margin),
                equivalent_integer_margin=3403**2-5*1521**2,
                scope='exact finite product certificate strictly improves the common-sine lower bound at N=3; not a global separable optimum'))


def run_v13_roundoff_check(fault):
    """A21 audit diagnostic: stable weights versus normalized phase quadrature.

    The nonnegative physical loss is checked on both sides. Merely accepting
    a negative value because it is below an upper tolerance would miss the
    cancellation in 1-exp(-a). No clipping is used to hide weight violations.
    This finite computation is not a proof of the Gaussian limit.
    """
    import numpy as np
    qx, qw = np.polynomial.legendre.leggauss(48)
    t = (qx + 1) / 2
    cases = []
    for z in (1000., 10000.):
        eps = z**-2; a = eps
        cut = int(8 * math.sqrt(z)) + 5
        m = np.arange(-cut, cut+1, dtype=float)
        f = np.exp(-m*m/(4*z)); f /= np.linalg.norm(f)
        adjacent = f[:-1] * f[1:]
        theta = 2*eps*(m[:-1]+.5)
        stable = a*np.abs(np.expm1(-a-1j*theta))/(np.hypot(a,theta)*-np.expm1(-a))
        naive = a*np.abs(1-np.exp(-a-1j*theta))/(np.hypot(a,theta)*(1-np.exp(-a)))
        weights = naive if fault == 'unstable-small-bin-weights' else stable
        # Independent route: a finite quadrature of the normalized density.
        # Normalize its positive weights directly; do not reuse expm1 or w.
        density = qw*np.exp(-a*t); density /= density.sum()
        phases = np.outer(theta, t)
        integral = np.cos(phases)@density + 1j*(np.sin(phases)@density)
        quadrature = np.abs(integral)
        s1 = float(adjacent.sum()); sw = float(weights@adjacent)
        energy = float(np.dot(m*m, f*f))
        # Sum the small losses before scaling to avoid subtracting two sums.
        loss_scaled = float(np.dot(1-weights, adjacent))*z
        naive_loss = float(np.dot(1-naive, adjacent))*z
        cases.append(dict(z=z, eps=eps, cutoff=cut, mean_energy=energy,
                          scaled_product=(1-sw)*energy, scaled_extra_loss=loss_scaled,
                          subtraction_route_extra_loss=(s1-sw)*z,
                          naive_scaled_extra_loss=naive_loss,
                          max_weight_excess=float(max(0., weights.max()-1)),
                          naive_max_weight_excess=float(max(0., naive.max()-1)),
                          max_quadrature_error=float(np.max(np.abs(weights-quadrature)))))
    ok = all(x['max_weight_excess']<3e-15 and x['max_quadrature_error']<3e-14
             and -3e-12 <= x['scaled_extra_loss'] <= 1e-6 for x in cases)
    ok &= abs(cases[-1]['scaled_product']-.125)<2e-6
    return dict(id='V28', **{'class':'V'}, claim='RECORD-SCOPE',
                status='PASS' if ok else 'FAIL', evidence=dict(cases=cases,
                weight_tolerance=3e-15, quadrature_tolerance=3e-14,
                scaled_loss_interval=[-3e-12,1e-6],
                scope='v1.2 audit A21: two small-bin finite witnesses, expm1 versus independent 48-node phase quadrature; two-sided nonnegative-loss regression, no limit certificate'))


def load_paper(path, fault):
    text = Path(path).read_text(encoding="utf-8")
    if fault == "doc-hash":
        text = re.sub(r'"script_sha256":\s*"[0-9a-f]+"', '"script_sha256": "' + "0" * 64 + '"', text)
    if fault == "doc-equation":
        text = text.replace("\\tag{11}", "\\tag{999}", 1)
    if fault == "doc-table":
        text = re.sub(r"(<!-- CERT-TABLE -->\n(?:.*\n)*?\| 1 \| none \| )0\.5", r"\g<1>0.6", text, count=1)
    if fault == "doc-ledger":
        # The manuscript declares PASS; desynchronise the ledger from the front matter.
        text = re.sub(r'"qualification":\s*"PASS"', '"qualification": "HOLD"', text)
    if fault == "doc-qualification-basis":
        # A PASS must carry the recorded substantive-novelty basis, not a bare assertion.
        text = re.sub(r'"qualification_basis":\s*"substantive_novelty_resolved"',
                      '"qualification_basis": "author_declared"', text)
    if fault == "doc-version":
        text = text.replace("<!-- M71-META", "python3 m71_seed_verify_v1_7.py --self-test --output m71_seed_verify_v1_7.json\n<!-- M71-META", 1)
    if fault == "doc-census":
        text = re.sub(r'"rows":\s*\d+', '"rows": 999', text, count=1)
    if fault == 'doc-phase-sign':
        text = text.replace(r'\kappa e^{-\kappa t-i\omega_{q-1}t}', r'\kappa e^{-\kappa t+i\omega_{q-1}t}', 1)
    if fault == 'doc-beta-sign':
        text = text.replace(r'\beta_{q,j}=-\arg', r'\beta_{q,j}=+\arg', 1)
    if fault == 'doc-reflection':
        text = text.replace(r'v_{-m}=v_m.', r'v_{-1-m}=v_m.', 1)
    if fault == 'doc-tail-rate':
        text = text.replace(r'q^{\rm old}_\varepsilon=\max\{w_{M_0},w_*\}',r'q^{\rm old}_\varepsilon=w_*',1)
    if fault == 'doc-mixed-coefficient':
        text = text.replace(r'-\frac{a^2\theta^2}{480}',r'-\frac{a^2\theta^2}{288}',1)
    if fault == 'doc-no-click':
        text = text.replace(r'D^{\max}_{h,T}=(1-e^{-\kappa T})\Lambda_w(h)',r'D^{\max}_{h,T}=\Lambda_w(h)',1)
    if fault == 'doc-universal-lower':
        text = text.replace('"lower_endpoint": "optimum_only"','"lower_endpoint": "all_states"',1)
    if fault == 'doc-rotor-gap':
        text = text.replace('For $d_m=2m+1$', 'For $d_m=2m+2$', 1)
    if fault == 'doc-joint-root':
        text = text.replace(r'With $n=\lfloor\sqrt N\rfloor$',r'With $n=\lfloor N\rfloor$',1)
    if fault == 'doc-separable-constant':
        text = text.replace(r'\lim N(1-\mathcal D_N^{\rm sep})=\pi,',r'\lim N(1-\mathcal D_N^{\rm sep})=\pi/2,',1)
    if fault == 'doc-independent-modes':
        text = text.replace(r'\le\lambda_{\max}(A_{u,N})',r'=\lambda_{\max}(A_{u,N})',1)
    if fault == 'doc-sinc-half':
        text = text.replace(r'\frac{(1-r)\tau(2m+1)}2',r'\frac{(1-r)\tau(2m+1)}1',1)
    if fault == 'doc-audited-proof-drift':
        text = text.replace('The floor function produces a bounded', 'The floor function produces an unbounded', 1)
    return text


def run_package(paper_path, fault, rows, tables, script_path):
    out = {}

    def row(rid, ok, **ev):
        out[rid] = {"id": rid, "class": CLASS_OF[rid], "claim": CLAIM_OF[rid],
                    "status": "PASS" if bool(ok) else "FAIL", "evidence": ev}
    if paper_path is None or not Path(paper_path).exists():
        for rid in ("G01", "G02", "G03", "G04", "G05", "G07"):
            row(rid, False, reason="manuscript not supplied or not found")
        return out, None
    text = load_paper(paper_path, fault)
    meta_match = re.search(r"<!-- M71-META\n(.*?)\n-->", text, re.S)
    meta = None
    try:
        meta = json.loads(meta_match.group(1)) if meta_match else None
    except ValueError:
        meta = None
    actual_sha = sha256_file(script_path)
    ok1 = (meta is not None and meta.get("script_sha256") == actual_sha and meta.get("paper_version") == PAPER_VERSION
           and meta.get("script") == SCRIPT_NAME and meta.get("script_version") == VERSION and RUN_COMMAND in text)
    row("G01", ok1, meta_present=meta is not None, script_sha256_actual=actual_sha,
        script_sha256_declared=(meta or {}).get("script_sha256"), run_command_present=RUN_COMMAND in text)

    missing_tags = [t for t in REQUIRED_TAGS if ("\\tag{%s}" % t) not in text]
    missing_labels = [l for l in REQUIRED_LABELS if l not in text]
    proof_fragment = text.split('### 7.5 Sharp asymptotic',1)[-1].split('### 7.6 ',1)[0]
    proof_sha = hashlib.sha256(proof_fragment.encode('utf-8')).hexdigest()
    proof_unchanged = proof_sha == AUDITED_T_SBC_SHA256
    row("G02", not missing_tags and not missing_labels and proof_unchanged,
        missing_tags=missing_tags, missing_labels=missing_labels, required_tags=len(REQUIRED_TAGS),
        audited_T_SBC_sha256=AUDITED_T_SBC_SHA256, actual_T_SBC_sha256=proof_sha,
        audited_proof_text_unchanged=proof_unchanged,
        scope="tag/label coverage plus exact preservation of v1.2 section 7.5 accepted by the supplied audit; provenance, not mathematical validity")

    def block(name):
        mm = re.search(r"<!-- %s-TABLE -->\n(.*?)<!-- /%s-TABLE -->" % (name, name), text, re.S)
        if not mm: return None
        lines = mm.group(1).splitlines()
        # data rows only: drop the header row (the line followed by a |--- rule) and the rule itself
        return [l for i, l in enumerate(lines) if l.startswith("| ") and not l.startswith("|---")
                and not (i + 1 < len(lines) and lines[i + 1].startswith("|---"))]
    table_ok = True; detail = {}
    for name in ("CERT", "CEILING", "BL", "BAND"):
        printed = block(name)
        expected = tables.get(name)
        same = printed is not None and expected is not None and printed == expected
        table_ok &= same
        detail[name] = dict(present=printed is not None, rows_printed=None if printed is None else len(printed),
                            rows_expected=None if expected is None else len(expected), identical=same,
                            first_mismatch=next(((p, e) for p, e in zip(printed or [], expected or []) if p != e), None))
    row("G03", table_ok, tables=detail)

    census = dict(collections.Counter(CLASS_OF[r] for r in ROW_IDS))
    front_qual = re.search(r"\*\*PAPER QUALIFICATION:\*\*\s*([A-Z]+)", text)
    ok4 = meta is not None
    if ok4:
        ok4 &= meta.get("qualification") in QUAL_VOCAB and str(meta.get("research_grade")) in GRADE_VOCAB \
            and str(meta.get("candidate_grade")) in CAND_VOCAB and str(meta.get("target_grade")) in GRADE_VOCAB
        ok4 &= meta.get("rows") == len(ROW_IDS) and meta.get("census") == census
        ok4 &= sorted(meta.get("ledger", {}).keys()) == sorted(ROW_IDS) and all(meta["ledger"][r] == [CLASS_OF[r], CLAIM_OF[r]] for r in ROW_IDS)
        ok4 &= front_qual is not None and front_qual.group(1) == meta.get("qualification")
        ok4 &= meta.get("qualification") == "HOLD" or meta.get("qualification_basis") == "substantive_novelty_resolved"
    row("G04", ok4, meta_rows=(meta or {}).get("rows"), computed_rows=len(ROW_IDS), computed_census=census,
        front_matter_qualification=front_qual.group(1) if front_qual else None,
        meta_qualification=(meta or {}).get("qualification"),
        scope="vocabulary and internal consistency of status fields, row registry and ledger; a HOLD may not be self-promoted")

    live_cmds = [l.strip() for l in text.splitlines() if re.match(r"^\s*python3?\s+\S+\.py", l)]
    bad = [l for l in live_cmds if SCRIPT_NAME not in l]
    stale = [l for l in text.splitlines() if "m71_seed_verify" in l and re.match(r"^\s*python", l)]
    row("G05", not bad and not stale, live_commands=live_cmds, foreign_commands=bad, stale_seed_commands=stale,
        scope="every live run command in the manuscript refers to this script (VERIFY CPN11); lineage mentions in prose are allowed")
    try:
        parameters = live_parameters(text)
        parameter_ok = (parameters == live_parameters(None))
    except (ValueError, IndexError) as exc:
        parameters = {'error': str(exc)}; parameter_ok = False
    contract = (meta or {}).get('operational_contract', {})
    zero_record = rows.get('W02', {}).get('evidence', {}).get('record')
    lows = rows.get('W02', {}).get('evidence', {}).get('optimum_lower_bounds', [])
    # The universal-lower mutation has a real counterexample, not just a banned token.
    lower_valid = (contract.get('lower_endpoint') == 'optimum_only' or
                   (contract.get('lower_endpoint') == 'all_states' and zero_record is not None
                    and all(zero_record >= float(Q(lo)) for lo in lows)))
    row('G07', parameter_ok and lower_valid and contract.get('upper_endpoint') == 'all_feasible_states'
        and contract.get('no_click') == 'included' and contract.get('one_quarter_path') == 'saturation',
        parameters={k:str(v) if isinstance(v,Q) else v for k,v in parameters.items()},
        contract=contract,zero_record_witness=zero_record,
        scope='narrow live-equation parser plus mathematical counterexample to universal certificate lower endpoint; not a natural-language proof checker')
    return out, meta


def main():
    ap = argparse.ArgumentParser(description="ZS-M71 v1.4.1 companion verifier")
    ap.add_argument("--paper", type=Path, default=None)
    ap.add_argument("--output", type=Path, default=None)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--math-only", action="store_true")
    ap.add_argument("--fault", choices=sorted(FAULTS))
    args = ap.parse_args()
    fault = args.fault
    if fault == "duplicate-registry": ROW_IDS.append(ROW_IDS[0])
    try:
        import numpy  # noqa
        import scipy  # noqa
    except ImportError as exc:
        print(json.dumps({"status": "FAIL", "dependency_error": str(exc), "not_run_count": len(ROW_IDS)}))
        return 2

    rows, tables, runtime = run_science(fault)
    ptext = (load_paper(args.paper, fault) if not args.math_only and args.paper and args.paper.exists() else None)
    try:
        rows.update(run_revision_checks(ptext, fault, rows))
    except Exception as exc:
        # Fail closed for the entire revision suite if a malformed paper/formula
        # prevents its checks; the legacy suite and package checks still finish.
        for rid in ('V15','V16','V17','C08','C09','W02','V18','W03','V19'):
            rows[rid] = dict(id=rid, **{'class':CLASS_OF[rid]}, claim=CLAIM_OF[rid],
                             status='FAIL', evidence={'error':type(exc).__name__+': '+str(exc)})
    try:
        new_rows,new_tables=run_v12_checks(ptext,fault)
        rows.update(new_rows);tables.update(new_tables)
    except Exception as exc:
        for rid in V12_ROW_IDS:
            rows[rid]=dict(id=rid, **{'class':CLASS_OF[rid]}, claim=CLAIM_OF[rid],
                           status='FAIL', evidence={'error':type(exc).__name__+': '+str(exc)})
    try:
        rows['V28'] = run_v13_roundoff_check(fault)
    except Exception as exc:
        rows['V28'] = dict(id='V28', **{'class':'V'}, claim='RECORD-SCOPE', status='FAIL',
                           evidence={'error':type(exc).__name__+': '+str(exc)})
    try:
        rows['C13'] = run_v13_finite_certificate(fault)
    except Exception as exc:
        rows['C13'] = dict(id='C13', **{'class':'C'}, claim='T-SB', status='FAIL',
                           evidence={'error':type(exc).__name__+': '+str(exc)})
    script_path = Path(__file__).resolve()
    if args.math_only:
        pkg = {rid: {"id": rid, "class": "G", "claim": "PACKAGE", "status": "SKIP", "evidence": {"reason": "--math-only"}}
               for rid in ("G01", "G02", "G03", "G04", "G05", "G07")}
        meta = None
    else:
        pkg, meta = run_package(args.paper, fault, rows, tables, script_path)
    rows.update(pkg)
    # G06 : registry uniqueness and census self-count
    census = dict(collections.Counter(CLASS_OF[r] for r in ROW_IDS))
    rows["G06"] = {"id": "G06", "class": "G", "claim": "PACKAGE",
                   "status": "PASS" if len(set(ROW_IDS)) == len(ROW_IDS) and sum(census.values()) == len(ROW_IDS) else "FAIL",
                   "evidence": {"census": census, "scope": "structural control"}}
    for rid, reason in (("D01", "external novelty is not machine-checkable; see manuscript section 9"),
                        ("D02", "no formal proof object; hand proofs in sections 2-7"),
                        ("D03", "physical selection / mission status not certified; see section 8")):
        rows[rid] = {"id": rid, "class": "D", "claim": CLAIM_OF[rid], "status": "SKIP", "evidence": {"reason": reason}}
    ordered = [rows[r] for r in ROW_IDS]
    fails = [r["id"] for r in ordered if r["status"] == "FAIL"]
    statuses = dict(collections.Counter(r["status"] for r in ordered))
    result = {
        "script": SCRIPT_NAME, "script_version": VERSION, "paper_version": PAPER_VERSION,
        "status": "FAIL" if fails else "PASS", "statuses": statuses, "failed_ids": fails,
        "rows": ordered, "census": census, "total": len(ordered),
        "evidence_rows": sum(census.get(k, 0) for k in "PCVW"), "control_rows": sum(census.get(k, 0) for k in "RG"),
        "non_evidence_rows": sum(census.get(k, 0) for k in "XDT"),
        "fault": fault, "math_only": bool(args.math_only),
        "paper": str(args.paper.name) if args.paper else None,
        "paper_sha256": sha256_file(args.paper) if args.paper and args.paper.exists() else None,
        "script_sha256": sha256_file(script_path),
        "reproduce_command": RUN_COMMAND, "runtime": runtime,
        "tables_generated": tables,
        "scientific_limits": [
            "finite samples and grids are not universal proofs; the universal statements are proved by hand in the manuscript",
            "C03 certifies four rational static cases; T-BL rows attack lemmas on finite instances; X01 diagnoses a conjecture",
            "no novelty, research grade, physical selection or mission status is certified (D01-D03 SKIP)",
            "T-SBC asymptotic and T-AR irrational cases have analytic proofs, not exhaustive numerical certification",
            "V28 repairs audit A21 roundoff; G02 preserves audited proof bytes without certifying the proof",
            "P = 0: no proof object is executed",
            "qualification and research grade are recorded in the manuscript, not established by this script",
        ],
    }
    if args.self_test:
        if args.math_only:
            result['status']='FAIL'
            result['self_test_error']='--self-test requires the paired manuscript profile'
        live = []
        me = [sys.executable, str(script_path)]
        base_args = ["--paper", str(args.paper)] if args.paper else []
        for fname, required in FAULTS.items():
            print('Self-test mutation: '+fname, file=sys.stderr, flush=True)
            proc = subprocess.run(me + base_args + ["--fault", fname], capture_output=True, text=True)
            try:
                payload = json.loads(proc.stdout)
            except ValueError:
                payload = {"failed_ids": []}
            live.append({"fault": fname, "kind": "functional" if fname in FUNCTIONAL_FAULTS else "structural",
                         "expected_failed_id": required, "exit_code": proc.returncode,
                         "detected": proc.returncode == 1 and required in payload.get("failed_ids", []),
                         "failed_ids": payload.get("failed_ids", []), "stderr_tail": proc.stderr[-200:]})
        controls = {}
        proc = subprocess.run(me, capture_output=True, text=True)
        try:
            p = json.loads(proc.stdout)
        except ValueError:
            p = {}
        controls["missing-paper"] = {"exit": proc.returncode, "FAIL": p.get("failed_ids"),
                                     "status": "PASS" if proc.returncode == 1 and set(p.get("failed_ids", [])) == {"G01", "G02", "G03", "G04", "G05", "G07"} else "FAIL"}
        proc = subprocess.run(me + base_args + ["--math-only"], capture_output=True, text=True)
        try:
            p = json.loads(proc.stdout)
        except ValueError:
            p = {}
        controls["math-only"] = {"exit": proc.returncode, "statuses": p.get("statuses"),
                                 "status": "PASS" if proc.returncode == 0 and p.get("statuses", {}).get("SKIP") == 9 else "FAIL"}
        proc = subprocess.run([sys.executable, "-S", str(script_path)] + base_args, capture_output=True, text=True)
        try:
            p = json.loads(proc.stdout)
        except ValueError:
            p = {}
        controls["dependencies-hidden-with-python-S"] = {"exit": proc.returncode, "error": p.get("dependency_error"),
                                                          "not_run_count": p.get("not_run_count"),
                                                          "status": "PASS" if proc.returncode == 2 and p.get("not_run_count") == len(ROW_IDS) else "FAIL"}
        outs = []
        for _ in range(2):
            with tempfile.TemporaryDirectory() as d:
                sp = Path(d) / SCRIPT_NAME; sp.write_bytes(script_path.read_bytes())
                pa = []
                if args.paper:
                    pp = Path(d) / PAPER_NAME; pp.write_bytes(args.paper.read_bytes()); pa = ["--paper", str(pp)]
                oj = Path(d) / "out.json"
                proc = subprocess.run([sys.executable, str(sp)] + pa + ["--output", str(oj)], capture_output=True, text=True)
                outs.append((proc.returncode, oj.read_bytes() if oj.exists() else b""))
        controls["isolated-two-process"] = {"exit_codes": [o[0] for o in outs], "byte_identical": outs[0][1] == outs[1][1] and len(outs[0][1]) > 0,
                                            "status": "PASS" if outs[0][0] == 0 and outs[1][0] == 0 and outs[0][1] == outs[1][1] else "FAIL"}
        result["live_fire"] = live
        result["controls"] = controls
        result["self_test_status"] = "PASS" if all(x["detected"] for x in live) and all(c["status"] == "PASS" for c in controls.values()) else "FAIL"
        if result["self_test_status"] == "FAIL":
            result["status"] = "FAIL"
    txt = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=False)
    if args.output:
        args.output.write_text(txt + "\n", encoding="utf-8")
    print(txt)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
