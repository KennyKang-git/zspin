#!/usr/bin/env python3
"""M72 v1.8: finite checks for T31--P34, not a proof or novelty certificate.

Python 3.10+, numpy, scipy. Run --output FILE, or --self-test --output FILE.
Every self-test runs ALL rows in a fresh python -O process and checks that the
six wrong predictions fail only their designated comparator. P=0 throughout.
The untouched v1.7 verifier and its inherited evidence are separate.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time

import numpy as np
import scipy
from scipy.special import iv, logsumexp, roots_legendre

VERSION = "ZS-M72 v1.8"
MUTATION = None
MUTATIONS = {
    "wrong_majorizing_phase": "V72",
    "wrong_frozen_phase": "V73",
    "zero_distortion": "V74",
    "independent_sixth_cumulant": "C75",
    "missing_first_resonance": "C76",
    "transfer_unshifted_cap": "W77",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valid_parameters(q, a, r):
    return all(type(z) is int for z in (q, a, r)) and q >= 2 and a != 0 and r != 0


@lru_cache(maxsize=512)
def log_integral(freqs, theta, phi=0.0, refinement=1):
    """Periodic trapezoidal quadrature. Floating diagnostic, not enclosure."""
    maxfreq = max(1, *map(abs, freqs))
    size = 1 << math.ceil(math.log2(max(2048, 32 * maxfreq)))
    size *= refinement
    x = np.arange(size, dtype=float) / size
    values = np.zeros(size)
    for f in freqs:
        values += np.cos(2 * np.pi * (np.remainder(f * x, 1.0) + phi))
    return float(logsumexp(theta * values) - math.log(size))


def checked_integral(freqs, theta, phi=0.0):
    v = log_integral(tuple(freqs), theta, phi)
    w = log_integral(tuple(freqs), theta, phi, 2)
    require(abs(v - w) < 2e-9, "quadrature refinement failed")
    return w


def logM(q, n, theta, phi=0.0):
    return checked_integral(tuple(q ** k for k in range(n)), theta, phi)


def nonperiodic_log_integral(freqs, theta, phi, order):
    """Composite Gauss--Legendre route for the unfrozen cylinder tail."""
    segments = max(8, math.ceil(2 * max(map(abs, freqs))))
    nodes, weights = roots_legendre(order)
    x = (np.arange(segments)[:, None] + (nodes[None, :] + 1) / 2) / segments
    values = sum(np.cos(2 * np.pi * (f * x + phi)) for f in freqs)
    total = np.sum(np.exp(theta * values) * weights[None, :]) / (2 * segments)
    return float(math.log(total))


def cumulants(freqs, order):
    """Exact constant coefficients of (sum(z^f+z^-f))^m / 2^m."""
    poly = {0: 1}
    moments = [F(1)]
    for degree in range(1, order + 1):
        nxt = defaultdict(int)
        for exponent, count in poly.items():
            for f in freqs:
                nxt[exponent + f] += count
                nxt[exponent - f] += count
        poly = nxt
        moments.append(F(poly.get(0, 0), 2 ** degree))
    return moment_cumulants(moments)


def moment_cumulants(moments):
    kap = [F(0)]
    for m in range(1, len(moments)):
        kap.append(moments[m] - sum(F(math.comb(m - 1, j - 1)) * kap[j]
                                   * moments[m - j] for j in range(1, m)))
    return kap


def C71():
    cases = 0
    for q in (2, 3, 4, 7):
        for a in (-5, -1, 1, 3):
            for r in (-9, -2, 1, 4):
                for m in (1, 2, 4):
                    d = q ** m
                    xstar = F(1, 2 * abs(r))
                    jstar = int(d * xstar)
                    require(abs(F(r * jstar, d) - r * xstar) <= F(abs(r), d),
                            "negative-tilt phase is not covered")
                    require((r * xstar - F(1, 2)).denominator == 1,
                            "half-turn congruence failed")
                    for j in sorted({0, d - 1, jstar}):
                        for y in (F(0), F(1, 7), F(1)):
                            for ell in (0, 1, 3):
                                left = (a * q ** (m + ell) + r) * F(j + y, d)
                                right = a * q ** ell * y + F(r * j, d) + F(r * y, d)
                                require(left - right == a * q ** ell * j,
                                        "exact cylinder identity failed")
                                require(abs(F(r * y, d)) <= F(abs(r), d),
                                        "exact freezing error failed")
                                cases += 1
                    require((a * q + r) - q * (a + r) == (1 - q) * r,
                            "local recurrence defect failed")
    return {"exact_rational_cases": cases, "q": [2, 3, 4, 7],
            "a": [-5, -1, 1, 3], "r": [-9, -2, 1, 4], "m": [1, 2, 4],
            "scope": "finite modular, phase-coverage and defect identities; not the universal lemma"}


def bessel_integral(q, n, theta, phi, cutoff=14):
    coeff = {0: 1.0 + 0j}
    for k in range(n):
        step = q ** k
        factors = [(h * step, iv(abs(h), theta) * np.exp(2j * np.pi * h * phi))
                   for h in range(-cutoff, cutoff + 1)]
        nxt = defaultdict(complex)
        for x, c in coeff.items():
            for y, d in factors:
                nxt[x + y] += c * d
        coeff = nxt
    return coeff.get(0, 0j)


def V72():
    worst_cross_error = 0.0
    min_slack = math.inf
    checks = 0
    for q, n in ((2, 4), (3, 4), (4, 3)):
        for t in (0.7, 1.3):
            majorant = logM(q, n, t, 0.5 if MUTATION == "wrong_majorizing_phase" else 0.0)
            for phi in (0.0, 0.125, 0.3, 0.5):
                value = logM(q, n, t, phi)
                require(value <= majorant + 2e-9, "wrong phase majorant")
                min_slack = min(min_slack, majorant - value)
                shifted = logM(q, n, t, phi + 0.5)
                negative = logM(q, n, -t, phi)
                require(abs(negative - shifted) < 2e-9, "half-turn identity failed")
                fourier = bessel_integral(q, n, t, phi)
                direct = math.exp(value)
                error = abs(fourier - direct) / direct
                require(error < 2e-9, "Bessel/phase quadrature disagreement")
                worst_cross_error = max(worst_cross_error, float(error))
                checks += 1
    return {"cases": checks, "Bessel_cutoff": 14, "relative_cross_error": worst_cross_error,
            "minimum_log_majorant_slack": min_slack,
            "scope": "finite Fourier truncations versus doubled quadrature; floating, not interval"}


def V73():
    rows = []
    for q, a, r in ((2, 1, 1), (2, -2, -3), (3, 3, 1), (4, -1, 4)):
        m, N, theta = 6, 4, 2.0
        d = q ** m
        for j in (0, int(d / (2 * abs(r))), d - 1):
            phi = r * j / d
            freqs = tuple(a * q ** k + r / d for k in range(N))
            direct16 = nonperiodic_log_integral(freqs, theta, phi, 16)
            direct32 = nonperiodic_log_integral(freqs, theta, phi, 32)
            require(abs(direct16 - direct32) < 2e-8, "cylinder integration refinement failed")
            frozen_phi = phi + (0.25 if MUTATION == "wrong_frozen_phase" else 0.0)
            frozen = logM(q, N, theta, frozen_phi)
            error = N * 2 * math.pi * abs(theta) * abs(r) / d
            require(abs(direct32 - frozen) <= error + 2e-8,
                    "cylinder tail violates its declared freezing bound")
            rows.append({"q": q, "a": a, "r": r, "j": j,
                         "log_error": abs(direct32 - frozen), "bound": error,
                         "quadrature_16_vs_32": abs(direct16 - direct32)})
    sandwich = []
    for q, a, r, n, m in ((2, 2, 1, 9, 5), (2, -2, -1, 9, 5),
                           (3, 1, -2, 7, 4), (4, 1, 3, 6, 3)):
        for theta in (-2.0, 0.7, 2.0):
            N, t = n - m, abs(theta)
            z = checked_integral(tuple(a * q ** k + r for k in range(n)), theta)
            base = logM(q, N, t)
            e = N * 2 * math.pi * t * abs(r) * q ** (-m)
            lo, hi = base - m * t - m * math.log(q) - 2 * e, base + m * t + e
            require(lo - 2e-8 <= z <= hi + 2e-8, "finite sandwich (9.46) failed")
            sandwich.append({"q": q, "a": a, "r": r, "n": n, "m": m,
                             "theta": theta, "logZ": z, "lo": lo, "hi": hi})
    return {"cylinders": rows, "finite_sandwich": sandwich,
            "scope": "unfrozen Gauss integration vs frozen periodic quadrature; both signs and negative multipliers"}


def V74():
    worst = 0.0
    cases = 0
    for q in (2, 3, 4):
        for theta in (-2.0, -0.6, 0.6, 2.0):
            D = 0.0 if MUTATION == "zero_distortion" else 2 * math.pi * abs(theta) / (q - 1)
            for phi in (0.0, 0.17, 0.5):
                discrepancy = abs(logM(q, 6, theta, phi) - 2 * logM(q, 3, theta, phi))
                require(discrepancy <= D + 2e-8, "almost multiplicativity bound failed")
                worst = max(worst, discrepancy / D if D else 0.0)
                cases += 1
    return {"cases": cases, "N": 3, "K": 3, "largest_fraction_of_D": worst,
            "scope": "finite almost-multiplicativity checks; does not prove the limiting bound"}


def C75():
    rows = []
    for n in (7, 8, 9):
        kap = cumulants([2 ** k + 1 for k in range(1, n + 1)], 6)
        prediction = F(5 * n, 4) if MUTATION == "independent_sixth_cumulant" else F(45 * n * n + 380 * n - 1875, 16)
        require(kap[1] == kap[3] == kap[5] == 0, "odd cumulant not zero")
        require(kap[2] == F(n, 2) and kap[4] == F(-3 * n + 28, 8), "lower cumulants mismatch")
        require(kap[6] == prediction, "sixth cumulant prediction rejected")
        rows.append({"n": n, "cumulants_1_to_6": [str(x) for x in kap[1:]]})
    return {"exact_rows": rows, "source": "AKP 2512.15501v1 Theorem B (IMPORTED)",
            "scope": "exact finite Laurent polynomial counts, not a new proof of the all-n source formula"}


def C76():
    rows = []
    for q, n in ((2, 5), (4, 4), (6, 4)):
        kap = cumulants([q ** k for k in range(n)], q + 1)
        one_moments = [F(math.comb(m, m // 2), 2 ** m) if m % 2 == 0 else F(0)
                       for m in range(q + 2)]
        iid = moment_cumulants(one_moments)
        for m in range(1, q + 1):
            require(kap[m] == n * iid[m], "unexpected lower-order geometric resonance")
        excess = kap[q + 1] - n * iid[q + 1]
        prediction = F(0) if MUTATION == "missing_first_resonance" else F((q + 1) * (n - 1), 2 ** q)
        require(excess == prediction, "first resonance coefficient rejected")
        rows.append({"q": q, "n": n, "exact_excess_cumulant": str(excess),
                     "limiting_Taylor_coefficient": str(F(1, 2 ** q * math.factorial(q))),
                     "one_sided_derivative_jump": str(F(q + 1, 2 ** (q - 1)))})
    return {"exact_rows": rows, "scope": "finite checks of imported first resonance; cusp conclusion uses T31 analytically"}


def W77():
    rows = []
    # pi < 22/7 and sqrt(3) < 7/4 give osc(u) < 11/12.
    oscillation_upper = F(22, 7) * F(7, 4) / 6
    require(oscillation_upper == F(11, 12) < 1, "oscillation rational bound failed")
    # sqrt(3)/2 > 3/4, certified after squaring the positive quantities.
    require(F(3, 4) > F(9, 16), "cos(pi/6) threshold failed")
    for n in (4, 7, 16, 64):
        old_lower = -F(1, 2) - oscillation_upper / n
        require(old_lower > -F(3, 4), "unshifted exclusion failed")
        delta = F(1, 12 * (2 ** n + 1))
        freqs = [2 ** k + 1 for k in range(1, n + 1)]
        require(all(f % 2 == 1 for f in freqs), "odd half-turn witness failed")
        require(max(freqs) * delta <= F(1, 12), "witness interval too large")
        # The center U=1/2 gives exactly -1, without evaluating a floating cosine.
        claimed_lower = old_lower if MUTATION == "transfer_unshifted_cap" else -F(1)
        require(-F(1) >= claimed_lower, "old geometric cap contradicted by the shifted center")
        rows.append({"n": n, "unshifted_average_lower_bound": str(old_lower),
                     "shifted_event_probability_lower_bound": str(2 * delta)})
    return {"exact_witnesses": rows, "scope": "finite rational phase intervals plus the inherited T13 inequality"}


def pressure(q, theta, grid):
    x = np.arange(grid) / grid
    ys = np.array([(x + j) / q for j in range(q)])
    positions = ys * grid
    lo = np.floor(positions).astype(int) % grid
    fraction = positions - np.floor(positions)
    weights = np.exp(theta * np.cos(2 * np.pi * ys)) / q
    vector = np.ones(grid)
    for iteration in range(2000):
        nxt = np.sum(weights * ((1 - fraction) * vector[lo]
                                + fraction * vector[(lo + 1) % grid]), axis=0)
        scale = nxt.max()
        nxt /= scale
        if np.max(abs(nxt - vector)) < 1e-13:
            return float(math.log(scale))
        vector = nxt
    raise ValueError("Ruelle iteration did not converge")


def V78():
    pressures = []
    for q in (2, 3, 4):
        pp = pressure(q, 2.0, 8192)
        pm = pressure(q, -2.0, 8192)
        refinement = max(abs(pp - pressure(q, 2.0, 4096)),
                         abs(pm - pressure(q, -2.0, 4096)))
        require(refinement < 2e-6, "pressure grid discrepancy too large")
        require(abs(pp - pm) < 2e-7 if q % 2 else pp - pm > 0.04,
                "pressure parity/branch comparison failed")
        pressures.append({"q": q, "positive_tilt": pp, "negative_tilt": pm,
                          "grid_refinement": refinement})
    values = []
    for n in (8, 12):
        for r in (0, 1, 2, -1):
            freqs = tuple(2 ** (k + 1) + r for k in range(n))
            pos = checked_integral(freqs, 2.0) / n
            neg = checked_integral(freqs, -2.0) / n
            if r % 2:
                require(abs(pos - neg) < 2e-9, "odd-frequency finite-n symmetry failed")
            if r == 0:
                require(pos - neg > 0.4, "r=0 must not be silently symmetrized")
            values.append({"n": n, "r": r, "logMGF_per_term_plus2": pos,
                           "logMGF_per_term_minus2": neg})
    return {"pressure_diagnostics": pressures, "finite_MGF_diagnostics": values,
            "scope": "finite grid and quadrature diagnostics; no convergence rate or universal theorem inferred from them"}


def G79():
    require(valid_parameters(2, -3, 1), "valid integer parameters rejected")
    for args in ((1, 1, 1), (2, 0, 1), (2, 1, 0), (2, 1.5, 1), (True, 1, 1)):
        require(not valid_parameters(*args), "theorem domain enlarged silently")
    require(list(ROWS) == ["C71", "V72", "V73", "V74", "C75", "C76", "W77", "V78", "G79"],
            "row registry changed without a ledger revision")
    require(all(row in ROWS for row in MUTATIONS.values()), "mutation target missing")
    return {"version": VERSION, "P": 0, "rows": list(ROWS),
            "scope": "parameter and registry guard; no theorem, physical promotion or grade certification"}


ROWS = {f.__name__: f for f in (C71, V72, V73, V74, C75, C76, W77, V78, G79)}


def run():
    start = time.time()
    results = []
    for name, function in ROWS.items():
        try:
            evidence = function()
            row = {"id": name, "class": name[0], "status": "PASS", "evidence": evidence}
        except Exception as error:
            row = {"id": name, "class": name[0], "status": "FAIL", "error": str(error)}
        print(name, row["status"], file=sys.stderr, flush=True)
        results.append(row)
    failed = [r["id"] for r in results if r["status"] != "PASS"]
    return {"version": VERSION, "profile": "V1.8-NEW-ALL", "P": 0,
            "status": "FAIL" if failed else "PASS", "mutation": MUTATION,
            "census": {"total": len(results), "by_class": dict(Counter(r["class"] for r in results)),
                       "failed": failed}, "rows": results,
            "runtime": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__, "optimized": not __debug__,
                        "seconds": time.time() - start},
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "limits": "Finite exact identities, numerical diagnostics and witnesses; analytic proofs and novelty/grade are outside the executable verdict."}


def self_test():
    start = time.time()
    with tempfile.TemporaryDirectory(prefix="m72_v18_") as temp:
        def child(mutation):
            path = Path(temp) / ((mutation or "baseline") + ".json")
            command = [sys.executable, "-O", str(Path(__file__).resolve()), "--output", str(path)]
            if mutation:
                command += ["--mutate", mutation]
            result = subprocess.run(command, capture_output=True, text=True, timeout=240)
            require(path.exists(), "child failed to emit JSON: " + result.stderr[-500:])
            data = json.loads(path.read_text())
            require(result.returncode == (0 if data["status"] == "PASS" else 1),
                    "child exit status disagrees with its evidence")
            return data
        baseline = child(None)
        require(baseline["status"] == "PASS", "self-test baseline failed")
        base_rows = {r["id"]: r for r in baseline["rows"]}
        tests = []
        for mutation, target in MUTATIONS.items():
            data = child(mutation)
            failed = data["census"]["failed"]
            unaffected = all(row == base_rows[row["id"]] for row in data["rows"] if row["id"] != target)
            ok = failed == [target] and unaffected and data["runtime"]["optimized"]
            tests.append({"mutation": mutation, "target": target, "status": "PASS" if ok else "FAIL",
                          "failed_rows": failed, "other_rows_evidence_unchanged": unaffected})
            print("SELF-TEST", mutation, tests[-1]["status"], file=sys.stderr, flush=True)
        return {"version": VERSION, "profile": "SELF-TEST-ALL-ROWS", "P": 0,
                "status": "PASS" if all(t["status"] == "PASS" for t in tests) else "FAIL",
                "baseline": baseline, "tests": tests, "seconds": time.time() - start,
                "scope": "six genuine wrong predictions, each in a fresh python -O process with all nine rows and exact comparison of unaffected row evidence"}


def main():
    global MUTATION
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--mutate", choices=list(MUTATIONS))
    args = parser.parse_args()
    require(not (args.self_test and args.mutate), "choose a run or the self-test suite")
    MUTATION = args.mutate
    data = self_test() if args.self_test else run()
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"version": VERSION, "profile": data["profile"], "status": data["status"],
                      "output": str(destination)}))
    return 0 if data["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
