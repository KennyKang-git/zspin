#!/usr/bin/env python3
"""ZS-M76 paper v2.5 — integrated finite verifier, code v2.5.

사용법 / Usage (Python >=3.11 for the pinned dependency stack):
  python -m pip install numpy==2.3.5 scipy==1.17.0 sympy==1.14.0 mpmath==1.3.0
  python zs_m76_verify_v2_5.py --quick
  python zs_m76_verify_v2_5.py --full --out full.json
  python zs_m76_verify_v2_5.py --new-only --out new.json
  python zs_m76_verify_v2_5.py --self-test --out self_test.json
  python zs_m76_verify_v2_5.py --list
  python zs_m76_verify_v2_5.py --suite physical_bridge_check --out bridge.json

Standalone: all ten release computations are readable functions in this file.
No sibling scripts, input data, network, extraction, exec/eval, or auto-install.
Each suite runs in an isolated (-I) child of THIS file. Assertions from the
release are explicit require() calls and remain active under python -O.
The standard library orchestrator still writes UNKNOWN rows if dependencies
are missing. Exit 0 = all requested finite checks pass; 1 = FAIL; 2 = UNKNOWN
or usage/I/O error. A subset PASS is never a complete ten-suite PASS.

QUICK: all ten suites, 42 inherited paths (d=2..4), 3000 Lemma 7.4 samples,
700 new entropy configurations, 12 entropy paths, 45 interior perturbations.
FULL: additionally 28 inherited paths (d=5,6) and two local optimizations.
NEW-ONLY: four v2.5 suites. The localized d=17 optimization runs even in QUICK.
FULL optimization can be slow; --timeout is the per-suite limit in seconds
(default 1800). Timeout is UNKNOWN, never PASS; later suites still run.

Evidence: C = finite exact arithmetic/symbolic identities; V = numerical;
W = explicit counterexample; X = diagnostic; G = self-test guard only; P=0.
Mixed C22 rows certify their exact subidentities only; accompanying floating
spectra are finite auxiliary checks. Overlapping rows are NOT independent
proofs. Failed local searches never certify a global exclusion theorem.
Legacy v2.4 constants/paths are explicitly marked historical regression;
their delta^(1/4) bound and old gap do not replace v2.5's sqrt(delta) and
nu_d = 1/(4*10^16*d^7). Paper and code versions are both v2.5.

Reproducibility: inherited fixed seeds/tolerances and finite scopes retained;
float64 (no interval enclosure), SymPy rationals, mpmath 40/60/80 digits.
Tested with Python3.12.14; Python syntax requires3.10 or newer, while the
documented NumPy/SciPy versions require3.11 or newer.
Workers use one BLAS thread. Canonical JSON excludes elapsed time and dates;
same-environment runs are expected byte-identical. Other BLAS/library versions
may change roundoff/optimization results; actual versions are recorded.
Optional --paper PATH verifies the v2.5 manuscript byte hash. Without it the
target hash is declared, not claimed to have been checked on disk.

Limit: this verifies encoded finite cases, not universal proofs, novelty,
NP-hardness, physical realization, human review, or research grade.
Physical bridge remains an instrument-fibre mathematical specialization.
The45 interior perturbations use random dephasing Schur centers, not the
NP-hard gadget outputs; their size is bounded via the Choi trace norm.

Repo2 reference conventions (retrieved 2026-10-21):
  zs_m75_verify_v1_3_1.py: self-contained finite scopes and mutation failures.
  zs_m72_verify_v1_8.py: fixed registry, require(), live-fire under python -O.
  zs_m71_verify_v1_4_1.py: claim/class registry and dependency reporting.
Only conventions are adopted; no M71/M72/M75 scientific results are imported.
Source hashes and reference URLs are in SOURCE_PROVENANCE / REPO2_REFERENCES.
"""
from __future__ import annotations

import argparse
from collections import Counter
import contextlib
import copy
import hashlib
import importlib
import importlib.metadata
import io
import json
import math
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
from types import SimpleNamespace

CODE_VERSION = '2.5'
PAPER_VERSION = '2.5'
PAPER_SHA256 = '794f94f8eb4f42cca767fae1c23d6d86cd3860369a0ee461fd4e5facb5abaa82'
CLASSES = 'PCVWRGXDT'
LIMITATIONS = (
    'Finite checks only; P=0. No universal proof, novelty, physical realization, '
    'NP-hardness or research-grade certification. Row scopes overlap and their '
    'counts are not counts of independent proofs. Historical v2.4 formulas '
    'are regression checks, not current v2.5 constants.'
)
REPO2_REFERENCES = {
    'folder': 'https://drive.google.com/drive/folders/1YHGbPaxv7DaT2-s6YeddszNP5NuBFoOU',
    'zs_m75_verify_v1_3_1.py': 'https://drive.google.com/file/d/1-trVbDUbUzZ5Rp2jcnp9QeVZ9LZuhDKn/view',
    'zs_m72_verify_v1_8.py': 'https://drive.google.com/file/d/1LGStM8x-Hmzg4gnB49sTkPKgSIO484SN/view',
    'zs_m71_verify_v1_4_1.py': 'https://drive.google.com/file/d/1aV9SIqh-cLPP1-0iPgDN_YmDt9V11i9T/view',
}
MUTATIONS = {'cpsd': 'C22-01', 'normalization': 'C22-03', 'readout': 'C22-04'}
DEPENDENCIES = {
    'channel_controls': ('numpy', 'scipy', 'sympy', 'mpmath'),
    'bounded_degree': ('numpy',),
    'derivations': ('sympy',),
    'v24_constants': ('mpmath',),
    'v24_localized_certificate': ('numpy', 'scipy', 'sympy'),
    'v24_stability_paths': ('numpy', 'scipy'),
    'entropy_rounding_checks': ('numpy', 'scipy', 'mpmath'),
    'v25_interior_verify': ('numpy', 'scipy', 'sympy'),
    'physical_bridge_check': ('sympy',),
    'adversarial_new_checks': (),
}
NEW_SUITES = tuple(DEPENDENCIES)[6:]
SEEDS = {
    'channel_controls': [20261019], 'bounded_degree': [], 'derivations': [],
    'v24_constants': [], 'v24_localized_certificate': [0, 8, 20, 40, 60],
    'v24_stability_paths': [20261020, 3, 5],
    'entropy_rounding_checks': [20261021], 'v25_interior_verify': [7625],
    'physical_bridge_check': [], 'adversarial_new_checks': [],
}


class CheckFailure(ValueError):
    """A computed check failed (also active in optimized Python)."""


def require(condition, message):
    if not bool(condition):
        raise CheckFailure(message)


def json_default(value):
    if hasattr(value, 'item'):
        return value.item()
    raise TypeError(f'Not JSON serializable: {type(value).__name__}')


def canonical_json(value):
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False,
                      allow_nan=False, default=json_default) + '\n'


def atomic_write(path, text):
    """Replace a report only after its complete JSON has been serialized."""
    path = Path(path).expanduser().resolve()
    require(path != Path(__file__).resolve(), 'Output must not overwrite this verifier')
    path.parent.mkdir(parents=True, exist_ok=True)
    name = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8',
                                         dir=path.parent, delete=False) as handle:
            name = handle.name
            handle.write(text)
        os.replace(name, path)
    finally:
        if name and os.path.exists(name):
            os.unlink(name)


def finite_tree(value):
    if isinstance(value, float):
        require(math.isfinite(value), 'Non-finite number in result')
    elif isinstance(value, dict):
        for item in value.values():
            finite_tree(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            finite_tree(item)


def class_counts(rows):
    counts = Counter(row['class'] for row in rows)
    return {cls: counts[cls] for cls in CLASSES}


def combine_status(statuses):
    statuses = list(statuses)
    if not statuses or 'FAIL' in statuses:
        return 'FAIL'
    if any(s != 'PASS' for s in statuses):
        return 'UNKNOWN'
    return 'PASS'


def exit_code(status):
    return {'PASS': 0, 'FAIL': 1, 'UNKNOWN': 2}[status]


def environment():
    versions = {}
    for name in ('numpy', 'scipy', 'sympy', 'mpmath'):
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = None
    return {'python': platform.python_version(), 'implementation': platform.python_implementation(),
            'system': platform.system(), 'machine': platform.machine(), 'libraries': versions,
            'worker_blas_threads': 1, 'floating_precision': 'float64 (not interval)',
            'mpmath_dps': {'channel_controls': 80, 'v24_constants': 40, 'entropy_rounding_checks': 60},
            'tolerances': 'Suite-local comparisons retained verbatim; no global tolerance widening.'}


# Fixed registry; never inferred from this run's result.
REGISTRY = {'channel_controls': {'container': 'rows',
                      'key': 'id',
                      'rows': [{'id': 'C22-01',
                                'source_key': 'C22-01',
                                'class': 'C',
                                'claim': 'exact negative witness plus actual repaired CPSD rejection',
                                'scope': 'Sections 2–7 and 9; exact subidentities plus auxiliary finite '
                                         'numerics'},
                               {'id': 'C22-02',
                                'source_key': 'C22-02',
                                'class': 'C',
                                'claim': 'YES need not have a positive branch margin',
                                'scope': 'Sections 2–7 and 9; exact subidentities plus auxiliary finite '
                                         'numerics'},
                               {'id': 'C22-03',
                                'source_key': 'C22-03',
                                'class': 'C',
                                'claim': 'rational safe constants and physical/dimensionless normalization',
                                'scope': 'Sections 2–7 and 9; exact subidentities plus auxiliary finite '
                                         'numerics'},
                               {'id': 'V22-01',
                                'source_key': 'V22-01',
                                'class': 'X',
                                'claim': 'corrected Gershgorin numbers; monotonicity proof remains in '
                                         'manuscript',
                                'scope': 'Sections 2–7 and 9; exact subidentities plus auxiliary finite '
                                         'numerics'},
                               {'id': 'V22-02',
                                'source_key': 'V22-02',
                                'class': 'V',
                                'claim': 'rational entry conversion on all K4 branches; exact PSD repair '
                                         'control',
                                'scope': 'Sections 2–7 and 9; exact subidentities plus auxiliary finite '
                                         'numerics'},
                               {'id': 'C22-04',
                                'source_key': 'C22-04',
                                'class': 'C',
                                'claim': 'one finite-rate channel and same dilation admit informative and '
                                         'uninformative readouts',
                                'scope': 'Sections 2–7 and 9; exact subidentities plus auxiliary finite '
                                         'numerics'},
                               {'id': 'V22-03',
                                'source_key': 'V22-03',
                                'class': 'V',
                                'claim': 'determinant/noise-cost identity and norm bound on nonnormal-noise '
                                         'controls',
                                'scope': 'Sections 2–7 and 9; exact subidentities plus auxiliary finite '
                                         'numerics'},
                               {'id': 'V22-04',
                                'source_key': 'V22-04',
                                'class': 'V',
                                'claim': 'approximate intermediate pointer-state estimate on weak noisy '
                                         'moving path',
                                'scope': 'Sections 2–7 and 9; exact subidentities plus auxiliary finite '
                                         'numerics'},
                               {'id': 'V22-05',
                                'source_key': 'V22-05',
                                'class': 'V',
                                'claim': 'singular dephasing closure counterexample',
                                'scope': 'Sections 2–7 and 9; exact subidentities plus auxiliary finite '
                                         'numerics'}]},
 'bounded_degree': {'container': 'cases',
                    'key': 'name',
                    'rows': [{'id': 'bounded_degree-01',
                              'source_key': 'unit_yes',
                              'class': 'V',
                              'claim': 'unit_yes',
                              'scope': 'Section 5 private-triangle bounded-degree reduction: five finite '
                                       'instances'},
                             {'id': 'bounded_degree-02',
                              'source_key': 'contradiction_no',
                              'class': 'V',
                              'claim': 'contradiction_no',
                              'scope': 'Section 5 private-triangle bounded-degree reduction: five finite '
                                       'instances'},
                             {'id': 'bounded_degree-03',
                              'source_key': 'binary_yes',
                              'class': 'V',
                              'claim': 'binary_yes',
                              'scope': 'Section 5 private-triangle bounded-degree reduction: five finite '
                                       'instances'},
                             {'id': 'bounded_degree-04',
                              'source_key': 'chain_no',
                              'class': 'V',
                              'claim': 'chain_no',
                              'scope': 'Section 5 private-triangle bounded-degree reduction: five finite '
                                       'instances'},
                             {'id': 'bounded_degree-05',
                              'source_key': 'three_yes',
                              'class': 'V',
                              'claim': 'three_yes',
                              'scope': 'Section 5 private-triangle bounded-degree reduction: five finite '
                                       'instances'}]},
 'derivations': {'container': 'rows',
                 'key': 'name',
                 'rows': [{'id': 'derivations-01',
                           'source_key': 'Anchored identity 2.5',
                           'class': 'C',
                           'claim': 'Anchored identity 2.5',
                           'scope': 'Sections 2,5 and Appendix B: seven finite symbolic identities'},
                          {'id': 'derivations-02',
                           'source_key': 'Private-block identity 5.9',
                           'class': 'C',
                           'claim': 'Private-block identity 5.9',
                           'scope': 'Sections 2,5 and Appendix B: seven finite symbolic identities'},
                          {'id': 'derivations-03',
                           'source_key': 'Equations 5.14 and 5.16',
                           'class': 'C',
                           'claim': 'Equations 5.14 and 5.16',
                           'scope': 'Sections 2,5 and Appendix B: seven finite symbolic identities'},
                          {'id': 'derivations-04',
                           'source_key': 'Equations 5.21 to 5.25',
                           'class': 'C',
                           'claim': 'Equations 5.21 to 5.25',
                           'scope': 'Sections 2,5 and Appendix B: seven finite symbolic identities'},
                          {'id': 'derivations-05',
                           'source_key': 'Calibration identity B.7',
                           'class': 'C',
                           'claim': 'Calibration identity B.7',
                           'scope': 'Sections 2,5 and Appendix B: seven finite symbolic identities'},
                          {'id': 'derivations-06',
                           'source_key': 'Riccati factorization B.11',
                           'class': 'C',
                           'claim': 'Riccati factorization B.11',
                           'scope': 'Sections 2,5 and Appendix B: seven finite symbolic identities'},
                          {'id': 'derivations-07',
                           'source_key': 'Half-bound state B.12 and overlap B.13',
                           'class': 'C',
                           'claim': 'Half-bound state B.12 and overlap B.13',
                           'scope': 'Sections 2,5 and Appendix B: seven finite symbolic identities'}]},
 'v24_constants': {'container': 'rows',
                   'key': 'name',
                   'rows': [{'id': 'v24_constants-01',
                             'source_key': 'Corollary 6.3 constant',
                             'class': 'V',
                             'claim': 'Corollary 6.3 constant',
                             'scope': 'Historical v2.4 Sections 6–8 constants and delta^(1/4) grid; not '
                                      'current v2.5 gap'},
                            {'id': 'v24_constants-02',
                             'source_key': 'Theorem 6.4 NO margin',
                             'class': 'V',
                             'claim': 'Theorem 6.4 NO margin',
                             'scope': 'Historical v2.4 Sections 6–8 constants and delta^(1/4) grid; not '
                                      'current v2.5 gap'},
                            {'id': 'v24_constants-03',
                             'source_key': 'Theorem 8.1 constants',
                             'class': 'V',
                             'claim': 'Theorem 8.1 constants',
                             'scope': 'Historical v2.4 Sections 6–8 constants and delta^(1/4) grid; not '
                                      'current v2.5 gap'},
                            {'id': 'v24_constants-04',
                             'source_key': 'Theorem 7.6 Step 0 and Step 6 numerical inequalities',
                             'class': 'V',
                             'claim': 'Theorem 7.6 Step 0 and Step 6 numerical inequalities',
                             'scope': 'Historical v2.4 Sections 6–8 constants and delta^(1/4) grid; not '
                                      'current v2.5 gap'},
                            {'id': 'v24_constants-05',
                             'source_key': 'Theorem 7.6 chain (7.22) / (d^4 log(2/c) delta^(1/4)) on a grid',
                             'class': 'V',
                             'claim': 'Theorem 7.6 chain (7.22) / (d^4 log(2/c) delta^(1/4)) on a grid',
                             'scope': 'Historical v2.4 Sections 6–8 constants and delta^(1/4) grid; not '
                                      'current v2.5 gap'}]},
 'v24_localized_certificate': {'container': 'rows',
                               'key': 'name',
                               'rows': [{'id': 'v24_localized_certificate-01',
                                         'source_key': 'Corollary 6.3 vertex certificates (exact)',
                                         'class': 'C',
                                         'claim': 'Corollary 6.3 vertex certificates (exact)',
                                         'scope': 'Lemma 6.2/Corollary 6.3 finite certificates and '
                                                  'diagnostic local search'},
                                        {'id': 'v24_localized_certificate-02',
                                         'source_key': 'Lemma 5.3 / Corollary 6.3 2x2 certificates for '
                                                       'unintended shifts (exact)',
                                         'class': 'C',
                                         'claim': 'Lemma 5.3 / Corollary 6.3 2x2 certificates for unintended '
                                                  'shifts (exact)',
                                         'scope': 'Lemma 6.2/Corollary 6.3 finite certificates and '
                                                  'diagnostic local search'},
                                        {'id': 'v24_localized_certificate-03',
                                         'source_key': 'Numerical search for a nearby embeddable channel '
                                                       '(K4, d=17)',
                                         'class': 'X',
                                         'claim': 'Numerical search for a nearby embeddable channel (K4, '
                                                  'd=17)',
                                         'scope': 'Lemma 6.2/Corollary 6.3 finite certificates and '
                                                  'diagnostic local search'},
                                        {'id': 'v24_localized_certificate-04',
                                         'source_key': 'lambda_min(C) for growing d (Lemma 5.6 remark)',
                                         'class': 'V',
                                         'claim': 'lambda_min(C) for growing d (Lemma 5.6 remark)',
                                         'scope': 'Lemma 6.2/Corollary 6.3 finite certificates and '
                                                  'diagnostic local search'}]},
 'v24_stability_paths': {'container': 'rows',
                         'key': 'name',
                         'rows': [{'id': 'v24_stability_paths-01',
                                   'source_key': 'kappa equals -(1/d) log det T (7.4a)',
                                   'class': 'V',
                                   'claim': 'kappa equals -(1/d) log det T (7.4a)',
                                   'scope': 'Historical v2.4 Lemmas 7.3–7.5 and old stability chain: '
                                            'discretized finite paths'},
                                  {'id': 'v24_stability_paths-02',
                                   'source_key': 'Lemma 7.3 identity at t=0 and integrated bound (7.24)',
                                   'class': 'V',
                                   'claim': 'Lemma 7.3 identity at t=0 and integrated bound (7.24)',
                                   'scope': 'Historical v2.4 Lemmas 7.3–7.5 and old stability chain: '
                                            'discretized finite paths'},
                                  {'id': 'v24_stability_paths-03',
                                   'source_key': 'Frame length (7.26)',
                                   'class': 'V',
                                   'claim': 'Frame length (7.26)',
                                   'scope': 'Historical v2.4 Lemmas 7.3–7.5 and old stability chain: '
                                            'discretized finite paths'},
                                  {'id': 'v24_stability_paths-04',
                                   'source_key': "Constructed C'' within chain (7.22) and CPSD",
                                   'class': 'V',
                                   'claim': "Constructed C'' within chain (7.22) and CPSD",
                                   'scope': 'Historical v2.4 Lemmas 7.3–7.5 and old stability chain: '
                                            'discretized finite paths'},
                                  {'id': 'v24_stability_paths-05',
                                   'source_key': 'Lemma 7.4: (7.17) and identity (7.18) on random instances',
                                   'class': 'V',
                                   'claim': 'Lemma 7.4: (7.17) and identity (7.18) on random instances',
                                   'scope': 'Historical v2.4 Lemmas 7.3–7.5 and old stability chain: '
                                            'discretized finite paths'}],
                         'full_row': {'id': 'v24_stability_paths-06',
                                      'source_key': 'Adversarial optimisation towards non-embeddable d=3 '
                                                    'targets',
                                      'class': 'X',
                                      'claim': 'Two six-segment local optimization attempts; no global lower '
                                               'bound',
                                      'scope': 'Historical v2.4 full-only diagnostic'}},
 'entropy_rounding_checks': {'container': 'checks',
                             'key': 'id',
                             'rows': [{'id': 'ER-V01',
                                       'source_key': 'ER-V01',
                                       'class': 'V',
                                       'claim': '700 instantaneous random configurations, d=2..8',
                                       'scope': 'Current v2.5 Lemma 7.3a/Theorem 7.6 entropy and sqrt(delta) '
                                                'constant checks'},
                                      {'id': 'ER-V02',
                                       'source_key': 'ER-V02',
                                       'class': 'V',
                                       'claim': '12 nonunital time-dependent paths, d=2..5, 16-point '
                                                'quadrature per segment',
                                       'scope': 'Current v2.5 Lemma 7.3a/Theorem 7.6 entropy and sqrt(delta) '
                                                'constant checks'},
                                      {'id': 'ER-C01',
                                       'source_key': 'ER-C01',
                                       'class': 'C',
                                       'claim': 'exact integer comparisons in constant chain',
                                       'scope': 'Current v2.5 Lemma 7.3a/Theorem 7.6 entropy and sqrt(delta) '
                                                'constant checks'},
                                      {'id': 'ER-V03',
                                       'source_key': 'ER-V03',
                                       'class': 'V',
                                       'claim': '60-digit numerical hardness constant (analytic ln100<5 also '
                                                'suffices)',
                                       'scope': 'Current v2.5 Lemma 7.3a/Theorem 7.6 entropy and sqrt(delta) '
                                                'constant checks'}]},
 'adversarial_new_checks': {'container': 'rows',
                            'key': 'id',
                            'rows': [{'id': 'N_coefficient',
                                      'source_key': 'N_coefficient',
                                      'class': 'C',
                                      'claim': 'd delta + 32 d^2 kbar delta + 18 d^3 kbar delta <= 35 d^3 '
                                               'kbar delta',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'frame_factor',
                                      'source_key': 'frame_factor',
                                      'class': 'C',
                                      'claim': 'C_alpha/g <= 54/17 < 16/5',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'frame_length',
                                      'source_key': 'frame_length',
                                      'class': 'C',
                                      'claim': 'frame length coefficient',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'sqrt_term',
                                      'source_key': 'sqrt_term',
                                      'class': 'C',
                                      'claim': '24/sqrt(2) < 17',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'N_term',
                                      'source_key': 'N_term',
                                      'class': 'C',
                                      'claim': 'sqrt(72) < 17/2',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'tau',
                                      'source_key': 'tau',
                                      'class': 'C',
                                      'claim': 'tau + delta coefficient',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'final',
                                      'source_key': 'final',
                                      'class': 'C',
                                      'claim': '495/sqrt(2) < 400',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'alpha_bound',
                                      'source_key': 'alpha_bound',
                                      'class': 'C',
                                      'claim': '1/(4 sqrt(2)) < 1/5',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'C_alpha',
                                      'source_key': 'C_alpha',
                                      'class': 'C',
                                      'claim': '2/(1-alpha)^(3/2)<=3 when alpha<=1/5',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'two_E',
                                      'source_key': 'two_E',
                                      'class': 'C',
                                      'claim': '8(d-1)sqrt(delta)<=8/sqrt(72)<1',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'near_identity',
                                      'source_key': 'near_identity',
                                      'class': 'C',
                                      'claim': 'r<=2p+p/(4d²)<1/2 for d>=1,p<=1/8',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'choi_margin',
                                      'source_key': 'choi_margin',
                                      'class': 'C',
                                      'claim': 'p/d-2d*[p/(4d²)]=p/(2d)',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'interior_radius',
                                      'source_key': 'interior_radius',
                                      'class': 'C',
                                      'claim': 'nu/(8*4*50*d³)',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'exterior_gap',
                                      'source_key': 'exterior_gap',
                                      'class': 'C',
                                      'claim': 'nu-2*(nu/8)=3nu/4',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'nonunital_counterexample',
                                      'source_key': 'nonunital_counterexample',
                                      'class': 'W',
                                      'claim': 'K=|0><1|, rho=diag(9/10,1/10): Fprime=-4/25, V=0',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'},
                                     {'id': 'nonunital_correct_bound',
                                      'source_key': 'nonunital_correct_bound',
                                      'class': 'C',
                                      'claim': 'the R1 remainder handles this exact counterexample to '
                                               'Fprime>=2V',
                                      'scope': 'Current v2.5 Sections 7–8: scalar identities and nonunital '
                                               'counterexample'}]},
 'v25_interior_verify': {'container': None,
                         'key': None,
                         'rows': [{'id': 'INT-C01',
                                   'source_key': 'exact_constants',
                                   'class': 'C',
                                   'claim': 'Rational radius/gap relations at six encoded dimensions',
                                   'scope': 'Current v2.5 Section 8; finite exact ratios'},
                                  {'id': 'INT-C02',
                                   'source_key': 'exact_choi',
                                   'class': 'C',
                                   'claim': 'Q J(Omega-id) Q = Q/d at d=2,3,4; wrong normalization rejected',
                                   'scope': 'Current v2.5 Lemma 8.2; finite symbolic examples'},
                                  {'id': 'INT-V01',
                                   'source_key': 'perturbations',
                                   'class': 'V',
                                   'claim': '45 HP/TP perturbations: CCP log, CPTP channel and '
                                            'reconstruction',
                                   'scope': 'Current v2.5 Lemmas 8.2–8.3; numerical p=1/16 controls, not '
                                            'resolution of tiny hardness radius'},
                                  {'id': 'INT-W01',
                                   'source_key': 'negative_control',
                                   'class': 'W',
                                   'claim': 'Anti-depolarization gives negative conditional Choi eigenvalue',
                                   'scope': 'Finite numerical negative control near identity; no universal '
                                            'theorem certificate'}]},
 'physical_bridge_check': {'container': None,
                           'key': None,
                           'rows': [{'id': 'PB-C01',
                                     'source_key': 'qubit',
                                     'class': 'C',
                                     'claim': 'Binary instrument at c=3/5: Bhattacharyya overlap3/5 and '
                                              'error1/10',
                                     'scope': 'Current v2.5 Section 9; exact finite instrument example'},
                                    {'id': 'PB-C02',
                                     'source_key': 'trine',
                                     'class': 'C',
                                     'claim': 'd=3 trine channel and impossible common-outcome PSD '
                                              'decomposition',
                                     'scope': 'Current v2.5 Section 9; exact finite compatibility '
                                              'counterexample'}]}}

SOURCE_PROVENANCE = {'channel_controls': {'filename': 'zs_m76_v2_2_verify.py',
                      'sha256': 'dfeb5f4183b1bbf6c9239e9feed010c69453ab5a4cdd8cec996a8c85ebd9cff5'},
 'bounded_degree': {'filename': 'bounded_degree_probe.py',
                    'sha256': '0114942f576cd548a87c85786a198c71b9d9af940e77ea7a09eae00ba80ccaa1'},
 'derivations': {'filename': 'verify_v23_derivations.py',
                 'sha256': '7866a565eae360653a27fa7e01d6df7dd89632428635cafc14aef463a1da63f3'},
 'v24_constants': {'filename': 'v24_constants.py',
                   'sha256': 'd4a3133f444f311a071ebf16591acfe89074773afc190b40e5dbf25c7e850621'},
 'v24_localized_certificate': {'filename': 'v24_localized_certificate.py',
                               'sha256': 'a69dcf6374095549123eef929c00c52100492c2c1838fced54c5ac6b6bf28fde'},
 'v24_stability_paths': {'filename': 'v24_stability_paths.py',
                         'sha256': 'a15bca591c6a065bb1477b6d0e9d6a830c73e2e0cb8bae8df7d30e2a6b4c4eca'},
 'entropy_rounding_checks': {'filename': 'verify_entropy_rounding.py',
                             'sha256': 'c78009ae9ef4d497dba38260437eb7fd0c38c61b2347172a47d96ca98c17a820'},
 'v25_interior_verify': {'filename': 'v25_interior_verify.py',
                         'sha256': '8aeae82d2759e5300296dd2021ec103d6e1ecd02b05c5dc9e91949e67b71340f'},
 'physical_bridge_check': {'filename': 'physical_bridge_check.py',
                           'sha256': '7a47c116aa213134bde4a78c124812a234527ea4925762606b2cd8b31a270c19'},
 'adversarial_new_checks': {'filename': 'adversarial_new_checks.py',
                            'sha256': '6c6a564d0c57f63aa220480c90d5f2fd77420304f40038a74ec94e73cf9ff5ea'}}


# Source: zs_m76_v2_2_verify.py; arithmetic and finite sample scope retained.
def suite_channel_controls(profile="quick", mutation="none"):
    """Targeted checks for M76 v2.2. Finite checks are not universal proof or grade certification.
    Run: python scripts/zs_m76_v2_2_verify.py --out results/v22_results.json
    Dependencies: numpy, scipy, sympy, mpmath. Seed: 20261019.
    Mutations: cpsd (discard negative eigenvalue), normalization (omit pi), readout (wrong Kraus).
    """
    import itertools, platform
    args = SimpleNamespace(mutation=mutation)
    import numpy as np
    import scipy
    from scipy.linalg import null_space, expm, polar
    import sympy as s
    import mpmath as mp
    mp.mp.dps=80;rng=np.random.default_rng(20261019);rows=[]
    def check(i,cls,claim,fn):
     try:
      ok,data=fn();status='PASS' if bool(ok) else 'FAIL'
     except Exception as e: status='UNKNOWN';data={'error':repr(e)}
     rows.append(dict(id=i,cls=cls,claim=claim,status=status,data=data));print(i,status,flush=True)
    def minimum(M):
     d=len(M)
     if args.mutation=='cpsd':
      P=np.eye(d)-np.ones((d,d))/d
      return float(np.linalg.eigvalsh(P@M@P)[1])
     Q=null_space(np.ones((1,d)));return float(np.linalg.eigvalsh(Q.conj().T@M@Q)[0])
    def negative():
     L=s.Matrix([[0,-4,-s.Rational(9,5),-s.Rational(9,5)],[-4,0,-s.Rational(9,5),-s.Rational(9,5)],[-s.Rational(9,5),-s.Rational(9,5),0,-4],[-s.Rational(9,5),-s.Rational(9,5),-4,0]])
     h=s.Matrix([1,1,-1,-1]);q=(h.T*L*h)[0];M=np.array(L,float);C=np.exp(M)
     ev=float(np.linalg.eigvalsh(C)[0]);mn=minimum(M)
     return q==-s.Rational(8,5) and ev>0 and mn<-.39,dict(exact_witness=str(q),channel_min=ev,restricted_min=mn)
    check('C22-01','C','exact negative witness plus actual repaired CPSD rejection',negative)
    def zero_margin():
     k=s.symbols('k',real=True);G=s.Matrix([[1,-1+2*s.I*k],[-1-2*s.I*k,1]])
     det=s.expand(G.det());C=np.exp(np.array([[0,-.5,-.5],[-.5,0,-2],[-.5,-2,0]])*np.pi)
     return det==-4*k*k and min(np.linalg.eigvalsh(C))>0,dict(determinant=str(det),channel_min=float(np.linalg.eigvalsh(C)[0]),branch_zero_eigenvalues=[0,2])
    check('C22-02','C','YES need not have a positive branch margin',zero_margin)
    def constants():
     pi_lo=s.Rational(314159,100000);pi_hi=s.Rational(22,7)
     x=8*pi_hi/7;N=40;terms=[x**k/s.factorial(k) for k in range(N+1)]
     upper=sum(terms)+x**(N+1)/s.factorial(N+1)/(1-x/(N+2))
     gamma_lo=11*pi_lo/1690
     gdim=s.Rational(11,1690);gphys=s.pi*gdim if args.mutation!='normalization' else gdim
     identity=s.simplify(gphys-s.pi*gdim)
     return upper<40 and gamma_lo>s.Rational(1,50) and identity==0,dict(exp_upper_float=float(upper),gamma_lower=float(gamma_lo),pi_identity_residual=str(identity),cstar=str(mp.exp(-8*mp.pi/7)),epsilon_coefficient=str(11*mp.pi*mp.exp(-8*mp.pi/7)/10140))
    check('C22-03','C','rational safe constants and physical/dimensionless normalization',constants)
    def gersh():
     a=mp.e**(-mp.pi)+8*mp.e**(-2*mp.pi);b=9*mp.e**(-mp.pi)
     # derivative sign of (2k+1)*exp(-pi*sqrt(k)/2): 8sqrt(k)<pi(2k+1), k>=4.
     ks=[4,5,10,100];vals=[(2*k+1)*mp.exp(-mp.pi*mp.sqrt(k)/2) for k in ks]
     return a>mp.mpf('.05') and a<mp.mpf('.059') and b<mp.mpf('.389') and all(vals[i]>vals[i+1] for i in range(3)),dict(nonanchor=str(a),anchor_at_k4=str(b))
    check('V22-01','V','corrected Gershgorin numbers; monotonicity proof remains in manuscript',gersh)
    def gram(n,edges,owners):
     t=1/13;W=[0]*n
     for a,b,w in edges: W[a]+=w;W[b]+=w
     G=np.zeros((n+2*len(edges),)*2,complex)
     for v in range(n):G[v,v]=14/15*t*t*(W[v]+35)
     for j,(a,b,w) in enumerate(edges):
      p=n+2*j;q=p+1;sgn=1 if owners[j]==b else -1
      G[p,p]=G[q,q]=8/7;G[p,q]=1j*sgn;G[q,p]=-1j*sgn
      x=t if w==1 else t*(1+1j)
      for v,vals in [(a,[x,-1j*x]),(b,[x,1j*x])]:
       for idx,z in zip([p,q],vals):G[idx,v]=z;G[v,idx]=z.conjugate()
     return G
    def channel(G):
     d=len(G)+1;ell=np.zeros((d,d),complex);diag=G.diagonal().real
     ell[1:,0]=-np.pi*diag/2;ell[0,1:]=ell[1:,0]
     ell[1:,1:]=np.pi*(G-(diag[:,None]+diag[None,:])/2)
     return np.exp(ell),ell
    def rational_round():
     cases=[];allok=True
     for w in [1,2]:
      edges=[(a,b,w) for a in range(4) for b in range(a+1,4)];Gs=[]
      for bits in itertools.product([0,1],repeat=6):
       own=[edges[j][bit] for j,bit in enumerate(bits)];G=gram(4,edges,own);Gs.append((float(np.linalg.eigvalsh(G)[0]),G))
      val,G=max(Gs,key=lambda z:z[0]);C,ell=channel(G);d=len(C)
      ed=s.Rational(1,12000*(d-1));eta=ed/(32*d);N=int(s.ceiling(2/eta))
      # Rational integers/N, Hermitian by construction, diagonal exactly 1.
      R=np.eye(d,dtype=complex)
      for i in range(d):
       for j in range(i):
        z=complex(round(C[i,j].real*N)/N,round(C[i,j].imag*N)/N);R[i,j]=z;R[j,i]=z.conjugate()
      q=float(d*eta);Ct=(R+q*np.eye(d))/(1+q);err=float(np.max(abs(Ct-C)))
      lnew=ell+np.log(Ct/C);A=lnew[1:,1:]-lnew[1:,0,None]-lnew[None,0,1:]
      mineig=float(np.linalg.eigvalsh(A)[0]);cmin=float(np.linalg.eigvalsh(Ct)[0]);low=float(np.min(abs(Ct)))
      ok=(err<float(ed)/16 and cmin>0 and low>.02 and (val>11/1690 if w==1 else max(x[0] for x in Gs)<-11/1690))
      if w==1:ok &= mineig>0
      allok &= ok;cases.append(dict(weight=w,d=d,signs=64,best_dimless_eigenvalue=val,rounding_error=err,allowed_error=float(ed)/16,channel_min=cmin,coherence_min=low,same_branch_physical_min=mineig,denominator=N,denominator_bits=N.bit_length()))
     # Negative PSD roundoff control: a rank-one C rounded outward is invalid until diagonal repair.
     h=s.Rational(1,1000);R=s.Matrix([[1,1+h],[1+h,1]]);fixed=(R+2*h*s.eye(2))/(1+2*h)
     exact=R.det()<0 and fixed.det()>0
     return allok and exact,dict(cases=cases,raw_indefinite_det=str(R.det()),repaired_det=str(fixed.det()))
    check('V22-02','V','rational entry conversion on all K4 branches; exact PSD repair control',rational_round)
    def instrument():
     I=s.eye(2);Z=s.diag(1,-1)
     # A0=2/sqrt(5) I, A1=1/sqrt(5) Z; M+=(2I+Z)/sqrt(10), M-=(2I-Z)/sqrt(10).
     M=[2*I+Z,2*I-Z]
     if args.mutation=='readout':M[1]=M[0]
     equal=True
     for i in range(2):
      for j in range(2):
       E=s.zeros(2);E[i,j]=1
       out=4*E/5+Z*E*Z/5;new=sum((A*E*A.T/10 for A in M),s.zeros(2))
       equal &= out==new
     probs=[[s.expand((A*s.diag(int(j==0),int(j==1))*A.T).trace()/10) for A in M] for j in range(2)]
     tv=sum(abs(probs[0][k]-probs[1][k]) for k in range(2))/2
     return equal and tv==s.Rational(4,5),dict(same_channel=bool(equal),probabilities=[[str(p) for p in row] for row in probs],pointer_tv=str(tv),uninformative_probabilities=['4/5','1/5'])
    check('C22-04','C','one finite-rate channel and same dilation admit informative and uninformative readouts',instrument)
    def dissipator(F):
     d=len(F);I=np.eye(d);A=F.conj().T@F
     return np.kron(F.conjugate(),F)-.5*(np.kron(I,A)+np.kron(A.T,I))
    def determinant():
     cases=[];ok=True
     for d in [2,3,5]:
      Fs=[]
      for j in range(3):
       F=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));F-=np.trace(F)*np.eye(d)/d;Fs.append(F/np.linalg.norm(F))
      weights=[.03,.08,.13];D=sum(w*dissipator(F) for w,F in zip(weights,Fs));T=expm(D)
      residual=abs(np.trace(D)+d*sum(weights));norm=np.linalg.norm(D,2);det=float(np.linalg.det(T).real);rate=-2/d*np.log(det)
      ok &= residual<1e-12 and norm<=rate+1e-12
      cases.append(dict(d=d,trace_residual=float(residual),dissipator_norm=float(norm),determinant=det,rate_bound=float(rate)))
     return ok,dict(cases=cases)
    check('V22-03','V','determinant/noise-cost identity and norm bound on nonnormal-noise controls',determinant)
    def pointer():
     d=3;I=np.eye(d);F=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));F-=np.trace(F)*I/d;F/=np.linalg.norm(F)
     H=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));H=(H+H.conj().T)/5
     L=-1j*(np.kron(I,H)-np.kron(H.T,I))+1e-7*dissipator(F)
     U=expm(1j*H);end=np.kron(U.conjugate(),U)@expm(L)
     P=[np.diag([int(j==i) for j in range(d)]).astype(complex) for i in range(d)]
     apply=lambda T,A:(T@A.reshape(-1,order='F')).reshape((d,d),order='F')
     trnorm=lambda A:float(np.sum(np.linalg.svd(A,compute_uv=False)))
     delta=max(trnorm(apply(end,p)-p) for p in P);E=2*d*(d-1)*delta;alpha=(d-1)*np.sqrt(2*delta)/(1-E);bound=2*E+2*alpha
     vals=[];ok=E<.5 and alpha<1
     for t in [0,.2,.5,.9,1]:
      states=[apply(expm(t*L),p) for p in P];V=np.column_stack([np.linalg.eigh((x+x.conj().T)/2)[1][:,-1] for x in states]);W,_=polar(V)
      dist=max(trnorm(x-np.outer(W[:,j],W[:,j].conjugate())) for j,x in enumerate(states))
      impur=sum(1-np.trace(x@x).real for x in states)
      ov=max(np.trace(states[j]@states[k]).real for j in range(d) for k in range(j))
      ok &= dist<=bound+1e-12 and impur<=E+1e-12 and ov<=2*delta+1e-12
      vals.append(dict(t=t,frame_trace_error=dist,sum_impurity=float(impur),max_overlap=float(ov)))
     return ok,dict(endpoint_pointer_error=delta,E=E,alpha=alpha,proved_bound=bound,samples=vals,scope='finite controls; no derivative or generator-rounding claim')
    check('V22-04','V','approximate intermediate pointer-state estimate on weak noisy moving path',pointer)
    def singular():
     d=3;D=np.diag([1 if i==j else 0 for j in range(d) for i in range(d)])
     cases=[];ok=np.linalg.matrix_rank(D)==d
     for n in [1,4,10]:
      T=expm(n*(D-np.eye(d*d)));formula=D+np.exp(-n)*(np.eye(d*d)-D)
      err=np.max(abs(T-formula));ok &= err<1e-14;cases.append(dict(n=n,residual=float(err),distance=float(np.linalg.norm(T-D,2))))
     return ok,dict(dephasing_rank=int(np.linalg.matrix_rank(D)),cases=cases)
    check('V22-05','V','singular dephasing closure counterexample',singular)
    result={'paper_version':'2.2','status':'PASS' if all(r['status']=='PASS' for r in rows) else 'FAIL','mutation':args.mutation,'scope':'exact identities and finite numerical controls, not universal proof/novelty/grade','seed':20261019,'precision':'SymPy exact rationals; mpmath 80 digits; float64 numerical checks','environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':s.__version__,'mpmath':mp.__version__},'census':{c:sum(r['cls']==c for r in rows) for c in ['C','V']},'rows':rows}
    return result


# Source: bounded_degree_probe.py; arithmetic and finite sample scope retained.
def suite_bounded_degree(profile="quick", mutation="none"):
    """Independent small controls for the private-triangle bounded-degree reduction.
    Not a proof or new accepted manuscript theorem. No original verifier import.
    """
    import itertools, math
    from collections import Counter
    import numpy as np

    CASES = {
     'unit_yes': ((1,),),
     'contradiction_no': ((1,),(-1,)),
     'binary_yes': ((1,2),),
     'chain_no': ((1,),(-1,2),(-2,)),
     'three_yes': ((1,2,3),),
    }

    def build(clauses):
        ids={}
        def vertex(name):
            if name not in ids:ids[name]=len(ids)
            return ids[name]
        edges=[]
        variables=sorted({abs(x) for c in clauses for x in c})
        for x in variables:
            a=vertex(('lit',x)); b=vertex(('lit',-x));edges.append((a,b,2))
        for ci,c in enumerate(clauses):
            cv=vertex(('clause',ci))
            for lit in c:edges.append((cv,vertex(('lit',lit)),1))
            if len(c)<3:
                tri=[vertex(('triangle',ci,j)) for j in range(3)]
                edges.extend((tri[j],tri[(j+1)%3],2) for j in range(3))
                for j in range(3-len(c)):edges.append((cv,tri[j],1))
        return ids,edges

    def solve_capacity(n,edges):
        # Owner is outgoing endpoint, matching MMO weight load. Heavier edges first.
        order=sorted(range(len(edges)),key=lambda j:-edges[j][2])
        load=[0]*n; owner=[None]*len(edges);visited=0
        def rec(q):
            nonlocal visited
            visited+=1
            if q==len(order):return owner.copy()
            j=order[q];a,b,w=edges[j]
            for v in (a,b):
                if load[v]+w<=2:
                    owner[j]=v;load[v]+=w
                    out=rec(q+1)
                    if out is not None:return out
                    load[v]-=w
            return None
        return rec(0),visited

    def sat(clauses):
        variables=sorted({abs(x) for c in clauses for x in c})
        for bits in itertools.product([False,True],repeat=len(variables)):
            val=dict(zip(variables,bits))
            if all(any(val[abs(x)]==(x>0) for x in c) for c in clauses):return val
        return None

    def matrix(n,edges,owner,t=1/13):
        # No π: this is dimensionless anchored matrix, as originally in (21.2).
        g=np.zeros((n+2*len(edges),)*2,complex);weight=[0]*n
        for a,b,w in edges:weight[a]+=w;weight[b]+=w
        for v in range(n):g[v,v]=14/15*t*t*(weight[v]+35)
        for j,(a,b,w) in enumerate(edges):
            p=n+2*j;q=p+1;g[p,p]=g[q,q]=8/7
            # s=+1 loads b heavily, s=-1 loads a heavily.
            s=1 if owner[j]==b else -1
            g[p,q]=1j*s;g[q,p]=-1j*s
            x=t if w==1 else t*(1+1j)
            for v,vector in ((a,(x,-1j*x)),(b,(x,1j*x))):
                for z,y in zip((p,q),vector):g[z,v]=y;g[v,z]=np.conjugate(y)
        return g

    rows=[]
    for name,clauses in CASES.items():
        require(max(Counter(x for c in clauses for x in c).values())<=2, 'bounded_degree: max(Counter(x for c in clauses for x in c).values())<=2')
        ids,edges=build(clauses);n=len(ids);deg=Counter(v for a,b,w in edges for v in (a,b))
        truth=sat(clauses);owner,nodes=solve_capacity(n,edges)
        row={'name':name,'clauses':clauses,'vertices':n,'edges':len(edges),'max_degree':max(deg.values()),'sat':truth is not None,'capacity2_feasible':owner is not None,'dfs_nodes':nodes,'dimensionless_gap':1.1/169}
        require((truth is not None)==(owner is not None), 'bounded_degree: (truth is not None)==(owner is not None)')
        require(row['max_degree']<=3, "bounded_degree: row['max_degree']<=3")
        if owner is not None:
            g=matrix(n,edges,owner)
            eig=float(np.linalg.eigvalsh(g)[0]);row.update(sat_assignment=truth,owner=owner,lambda_min=eig,above_yes_gap=eig>=1.1/169)
            require(row['above_yes_gap'], "bounded_degree: row['above_yes_gap']")
            # Direct Schur complement against independent owner loads checks sign mapping.
            s=g[:n,:n]-g[:n,n:]@np.linalg.solve(g[n:,n:],g[n:,:n])
            load=[0]*n
            for j,v in enumerate(owner):load[v]+=edges[j][2]
            target=np.array([14/15/169*(35-14*u) for u in load])
            row['schur_diagonal_residual']=float(np.max(np.abs(np.diag(s)-target)))
            row['schur_offdiagonal_residual']=float(np.max(np.abs(s-np.diag(np.diag(s)))))
            require(row['schur_diagonal_residual']<1e-12 and row['schur_offdiagonal_residual']<1e-12, "bounded_degree: row['schur_diagonal_residual']<1e-12 and row['schur_offdiagonal_residual']<1e-12")
        else:
            # Enumerate every owner, evaluate the explicit negative Rayleigh certificate;
            # full eigenspectrum only on selected extrema, avoiding many expensive eigensolves.
            worst_load=0;max_rayleigh=-math.inf;maxowner=None;max_norm=0;count=0
            for bits in itertools.product((0,1),repeat=len(edges)):
                choice=[edges[j][bit] for j,bit in enumerate(bits)];load=[0]*n
                for j,v in enumerate(choice):load[v]+=edges[j][2]
                v=max(range(n),key=load.__getitem__);require(load[v]>=3, 'bounded_degree: load[v]>=3')
                numerator=14/15/169*(35-14*load[v])
                # Norm squared of e_v - P^{-1}B e_v. Independent exact eigenvalue sizes.
                norm2=1.0
                for j,(a,b,w) in enumerate(edges):
                    if v not in (a,b):continue
                    lam=1/7 if choice[j]==v else 15/7
                    norm2+=2*w/169/(lam*lam)
                ray=numerator/norm2
                require(ray<=-1.1/169, 'bounded_degree: ray<=-1.1/169')
                count+=1;max_norm=max(max_norm,norm2)
                if ray>max_rayleigh:max_rayleigh=ray;maxowner=choice
            eig=float(np.linalg.eigvalsh(matrix(n,edges,maxowner))[0])
            row.update(all_signs_tested=count,max_negative_certificate=max_rayleigh,max_witness_norm_squared=max_norm,selected_lambda_min=eig,below_no_gap=eig<=-1.1/169)
            require(row['below_no_gap'], "bounded_degree: row['below_no_gap']")
        row['pass']=True;rows.append(row)
    result={'status':'PASS','scope':'small deterministic controls, not universal proof or novelty assessment','normalization':'dimensionless G; physical anchor is pi*G','original_verifier_imported':False,'cases':rows}
    return result


# Source: verify_v23_derivations.py; arithmetic and finite sample scope retained.
def suite_derivations(profile="quick", mutation="none"):
    """Exact checks of equations newly consolidated in the English manuscript.
    These checks are finite identities and inequalities, not universal proof certificates.
    """
    import sympy as s
    rows=[]
    def record(name,ok,data):rows.append({'name':name,'status':'PASS' if bool(ok) else 'FAIL','data':data})
    # Arbitrary Hermitian 3-by-3 logarithm and complex zero-sum vector.
    a,b,c,p,r,h=s.symbols('a b c p r h',real=True)
    L=s.Matrix([[0,a+s.I*p,b+s.I*r],[a-s.I*p,0,c+s.I*h],[b-s.I*r,c-s.I*h,0]])
    x1,y1,x2,y2=s.symbols('x1 y1 x2 y2',real=True)
    w=s.Matrix([x1+s.I*y1,x2+s.I*y2]);z=s.Matrix([-sum(w),*w])
    G=s.Matrix(2,2,lambda i,j:L[i+1,j+1]-L[i+1,0]-L[0,j+1])
    res=s.expand((s.conjugate(z).T*L*z)[0]-(s.conjugate(w).T*G*w)[0])
    record('Anchored identity 2.5',res==0,{'residual':str(res),'dimension':3})
    xr,xi=s.symbols('xr xi',real=True);x=xr+s.I*xi
    B=s.Matrix([[x,x],[-s.I*x,s.I*x]])
    residuals=[]
    for sg in [-1,1]:
     P=s.Matrix([[s.Rational(8,7),s.I*sg],[-s.I*sg,s.Rational(8,7)]])
     expected=s.diag(2*(xr*xr+xi*xi)/(s.Rational(8,7)+sg),2*(xr*xr+xi*xi)/(s.Rational(8,7)-sg))
     residuals.append((s.conjugate(B).T*P.inv()*B-expected).applyfunc(s.simplify))
    record('Private-block identity 5.9',all(M==s.zeros(2) for M in residuals),{'signs':[-1,1],'residuals':[str(M) for M in residuals]})
    t=s.Rational(1,13);q=s.Rational(11,10)*t*t;h=s.Rational(14,15)*t*t*41;m=s.Rational(98,15)*t*t
    shift=s.factor(m-q*(1+14*h));ray=s.factor(m/(1+588*t*t))
    record('Equations 5.14 and 5.16',shift==s.Rational(49339,4284150) and shift>0 and ray==s.Rational(98,11355) and ray>q,{'shift_margin':str(shift),'negative_Rayleigh_magnitude':str(ray),'target_gap':str(q)})
    x=s.Rational(628,175);lo=sum(x**j/s.factorial(j) for j in range(15))
    y=s.Rational(198,245);up=sum(y**j/s.factorial(j) for j in range(15))+y**15/s.factorial(15)/(1-y/16)
    k=s.Rational(4)*s.Rational(22,7)**2*s.Rational(9,4)/33
    record('Equations 5.21 to 5.25',lo>36 and up<s.Rational(9,4) and k==s.Rational(1452,539) and k<s.Rational(27,10) and s.Rational(14,15)*s.Rational(157,50)>k,{'exp_lower_rational':str(lo),'exp_upper_rational':str(up),'kappa_upper':str(k)})
    rho,x,y,qv,lu,lw,eps=s.symbols('rho x y q lu lw eps',positive=True)
    f=(3-x-y)*qv/2+qv**3/6
    fx,fy,fq=[s.diff(f,v) for v in [x,y,qv]]
    grad=4*x/rho*fx**2+4*y*fy**2+(y/rho+x)*fq**2+4*qv*(fx*fq/rho+fy*fq)
    twov=lu*rho**2*(x-1)**2+lw*(y-1)**2+2*eps*rho*(x*y-qv*qv)
    epsw=lw*(rho+1)/(2*rho*rho)
    rhs=lw*(4*rho+4-rho*x-y)/(4*rho)*(x+y-1-qv*qv)**2+(lu*rho*rho-lw/rho)*(1-x)**2+2*(eps-epsw)*rho*(x*y-qv*qv)
    res=s.factor(twov-lw*grad-rhs)
    record('Calibration identity B.7',res==0,{'residual':str(res),'normalization':'divided by b^4'})
    T=s.symbols('T',real=True);W=s.Matrix([[T/rho,-1/s.sqrt(rho)],[-1/s.sqrt(rho),T]])
    Wp=W.diff(T)*(1-T*T);ew=(1+rho)/(2*rho*rho)
    v=s.Matrix([T,-s.sqrt(rho)]);V=2*ew*(v*v.T)-2*(1-T*T)*s.diag(0,1)
    resid=(W*W-Wp-V).applyfunc(s.simplify)
    record('Riccati factorization B.11',resid==s.zeros(2),{'residual':str(resid)})
    phi,S=s.symbols('phi S',real=True);kappa=1+1/rho
    psi=s.Matrix([s.sqrt(rho)*phi,T*phi+S]);psip=psi.diff(T)*(1-T*T)+psi.diff(phi)*S/rho+psi.diff(S)*(-kappa*T*S)
    zero=(psip+W*psi).applyfunc(s.simplify);over=s.simplify((v.T*psi)[0]+s.sqrt(rho)*S)
    record('Half-bound state B.12 and overlap B.13',zero==s.zeros(2,1) and over==0,{'first_order_residual':str(zero),'overlap_residual':str(over)})
    result={'status':'PASS' if all(r['status']=='PASS' for r in rows) else 'FAIL','scope':'seven exact finite identity/constant checks; no novelty or independent review claim','sympy':s.__version__,'rows':rows}
    return result


# Source: v24_constants.py; arithmetic and finite sample scope retained.
def suite_v24_constants(profile="quick", mutation="none"):
    """ZS-M76 v2.4: exact and high-precision checks of the new numerical constants.

    Rows
      V  Corollary 6.3: eps_* = 7 pi e^{-8pi/7}/34065 and the identity 98/476910 = 7/34065
      V  Theorem 6.4: eps_* - 1/192000 > 1/80000, |C~| > 1/50 margin
      V  Theorem 8.1: 120 log(100)/(5e7) < 1/80000, nu_d < 1/(72 d^2) <= 1/(100 sqrt d) for d >= 2
      V  Theorem 7.6, Step 0 and Step 6: every displayed numerical inequality, as a function of d >= 2,
         checked in 40-digit arithmetic at d = 2 and by monotonicity in d (stated in each row)
      V  Theorem 7.6: the full chain (7.22) divided by d^4 log(2/c) delta^{1/4}, maximised on a grid
    These are finite checks of constants; they do not replace the proofs.
    """
    import math
    from fractions import Fraction as Fr

    import mpmath as mp
    mp.mp.dps = 40
    rows = []


    def record(name, cls, ok, data):
        rows.append({'name': name, 'class': cls, 'status': 'PASS' if bool(ok) else 'FAIL', 'data': data})


    pi = mp.pi
    cstar = mp.e ** (-8 * pi / 7)
    mu = mp.mpf(98) / 11355
    eps_star = 7 * pi * cstar / 34065
    record('Corollary 6.3 constant', 'V',
           Fr(98, 476910) == Fr(7, 34065) and abs(pi * mu * cstar / 42 - eps_star) < mp.mpf(10) ** -35 and eps_star < cstar / 2,
           {'eps_star': mp.nstr(eps_star, 12), 'c_star_over_2': mp.nstr(cstar / 2, 12),
            'eps_d_coefficient': mp.nstr(11 * pi * cstar / 10140, 12),
            'eps_star_exceeds_eps_d_from_d': int(mp.ceil(1 + (11 * pi * cstar / 10140) / eps_star))})
    margin = eps_star - mp.mpf(1) / 192000
    record('Theorem 6.4 NO margin', 'V', margin > mp.mpf('1.2601e-5') > mp.mpf(1) / 80000,
           {'eps_star_minus_1_over_192000': mp.nstr(margin, 12), 'one_over_80000': mp.nstr(mp.mpf(1) / 80000, 12)})
    lhs = 120 * mp.log(100) / mp.mpf('5e7')
    ok81 = lhs < mp.mpf('1.11e-5') < mp.mpf(1) / 80000
    okreg = all((mp.mpf(5e7) * d ** 4) ** -4 < mp.mpf(1) / (72 * d * d) <= 1 / (100 * mp.sqrt(d)) for d in range(2, 2000))
    record('Theorem 8.1 constants', 'V', ok81 and okreg,
           {'120_log100_over_5e7': mp.nstr(lhs, 12), 'nu_2': mp.nstr((mp.mpf(5e7) * 16) ** -4, 6),
            'regime_checked_for_d_in': [2, 1999], 'regime_is_monotone_beyond': '1/(72d^2) decreases faster than 1/(100 sqrt d)'})

    # Theorem 7.6 Step 0 / Step 6 inequalities.  s = sqrt(delta) <= 1/(sqrt(72) d).
    # Each bound is worst at d = 2 or is d-free; monotonicity noted per row.
    s_d = lambda d: 1 / (mp.sqrt(72) * d)
    E_max = lambda d: 2 * d * (d - 1) * s_d(d) ** 2               # increasing to 1/36
    alpha_coef = mp.mpf(36) / 35 * mp.sqrt(2)                     # alpha <= alpha_coef (d-1) s
    checks = {}
    checks['E<=1/36'] = all(E_max(d) <= mp.mpf(1) / 36 for d in [2, 3, 10, 10 ** 6])
    checks['alpha<=0.1715'] = all(alpha_coef * (d - 1) * s_d(d) <= mp.mpf('0.1715') for d in [2, 3, 10, 10 ** 6])
    a = mp.mpf('0.1715')
    Ca = (1 - a) ** mp.mpf(-0.5) + (1 + a) * (1 - a) ** mp.mpf(-1.5)
    checks['C_alpha<=2.66'] = Ca <= mp.mpf('2.66')
    checks['2E<=0.472(d-1)s'] = all(4 * d * (d - 1) * s_d(d) ** 2 <= mp.mpf('0.472') * (d - 1) * s_d(d) for d in [2, 10, 10 ** 6])
    checks['eps0<=3.39(d-1)s'] = mp.mpf('0.472') + 2 * alpha_coef <= mp.mpf('3.39')
    # N <= d(d-1) s^2 + 4*3.39 d(d-1)^2 kbar s and d(d-1) s^2 <= 0.05 d (d-1)^2 kbar s  (kbar >= d log 2)
    checks['N<=13.61 d^3 kbar s'] = all(s_d(d) <= mp.mpf('0.05') * (d - 1) * d * mp.log(2) for d in [2, 3, 10]) and 4 * mp.mpf('3.39') + mp.mpf('0.05') <= mp.mpf('13.61')
    checks['sqrt(13.61)<=3.69'] = mp.sqrt(mp.mpf('13.61')) <= mp.mpf('3.69')
    checks['72^(-1/4)<=0.344 (and *13.61<=4.68)'] = mp.mpf(72) ** mp.mpf(-0.25) <= mp.mpf('0.3438') and mp.mpf('13.61') * mp.mpf(72) ** mp.mpf(-0.25) <= mp.mpf('4.68')
    checks['(6alpha+2E)<=9.21(d-1)s and *0.344<=3.17'] = 6 * alpha_coef + mp.mpf('0.472') <= mp.mpf('9.21') and mp.mpf('9.21') * mp.mpf(72) ** mp.mpf(-0.25) <= mp.mpf('3.17')
    frame_coef = Ca / (mp.mpf(17) / 18) * (2 * mp.mpf('3.69') + mp.mpf('3.17') / mp.sqrt(2))
    checks['frame<=27.1 d^2'] = frame_coef <= mp.mpf('27.1')
    tau_coef = 4 * mp.mpf('3.69') / 2 + 2 * mp.mpf('4.68') + 2 * mp.mpf('27.1') / mp.sqrt(2)
    checks['tau<=55.1 d^(5/2)'] = tau_coef + mp.mpf('0.01') <= mp.mpf('55.1')
    checks['1+sqrt(2d)<=2.122 sqrt(d)'] = 1 / mp.sqrt(2) + mp.sqrt(2) <= mp.mpf('2.122')
    checks['2.122*55.1<=120'] = mp.mpf('2.122') * mp.mpf('55.1') <= 120
    record('Theorem 7.6 Step 0 and Step 6 numerical inequalities', 'V', all(checks.values()),
           {k: bool(v) for k, v in checks.items()} | {'C_alpha_at_0.1715': mp.nstr(Ca, 8), 'frame_coef': mp.nstr(frame_coef, 8), 'tau_coef': mp.nstr(tau_coef, 8)})


    def chain(d, delta, c):
        kappa = d * mp.log(2 / c)
        E = 2 * d * (d - 1) * delta
        alpha = (d - 1) * mp.sqrt(2 * delta) / (1 - E)
        eps0 = 2 * E + 2 * alpha
        N = d * (d - 1) * (delta + 4 * eps0 * kappa)
        g = 1 - 2 * E
        Cal = (1 - alpha) ** mp.mpf(-0.5) + (1 + alpha) * (1 - alpha) ** mp.mpf(-1.5)
        frame = Cal / g * (2 * mp.sqrt(d) * mp.sqrt(kappa * N) + (6 * alpha + 2 * E) * d * kappa)
        tau = 4 * mp.sqrt(kappa * N) + 2 * N + 2 * frame
        return (1 + mp.sqrt(2 * d)) * (tau + delta)


    worst, arg = mp.mpf(0), None
    for d in list(range(2, 41)) + [60, 100, 200, 500, 1000, 10 ** 4, 10 ** 6]:
        for c in [1, 0.9, 0.5, 0.1, 1 / 50, float(cstar), 1e-3, 1e-10, 1e-100]:
            dmax = min(c / (2 * math.sqrt(d)), 1 / (72 * d * d))
            for f in [1, 0.9, 0.5, 0.1, 1e-2, 1e-4, 1e-8, 1e-16, 1e-40]:
                delta = mp.mpf(dmax) * f
                r = chain(d, delta, mp.mpf(c)) / (d ** 4 * mp.log(2 / mp.mpf(c)) * delta ** mp.mpf(0.25))
                if r > worst:
                    worst, arg = r, (d, c, f)
    record('Theorem 7.6 chain (7.22) / (d^4 log(2/c) delta^(1/4)) on a grid', 'V', worst < 120,
           {'max_ratio': mp.nstr(worst, 8), 'argmax_d_c_fraction': [arg[0], arg[1], arg[2]],
            'grid': 'd in 2..40 and up to 1e6; c in [1e-100,1]; delta = fraction * delta_d(c)'})

    status = 'PASS' if all(r['status'] == 'PASS' for r in rows) else 'FAIL'
    return {'status': status, 'rows': rows}


# Source: v24_localized_certificate.py; arithmetic and finite sample scope retained.
def suite_v24_localized_certificate(profile="quick", mutation="none"):
    """ZS-M76 v2.4: checks for the localized certificates of Lemma 6.2 and Corollary 6.3.

    Rows
      C  exact (sympy over Q(i)) vertex certificates for every sign branch of three NO gadgets:
         support <= 7 and Rayleigh quotient <= -98/11355
      C  exact 2x2 certificates for every single-entry unintended integer shift (K4 gadget)
      X  numerical search for an embeddable pointer-preserving channel near the K4 NO output
      V  lambda_min(C) of gadget correlation matrices for growing d (remark after Lemma 5.6)
    Finite checks only; Corollary 6.3 is proved in the manuscript.
    """
    import itertools, math
    import numpy as np
    import sympy as sp
    from scipy.optimize import minimize




    t = sp.Rational(1, 13)
    I = sp.I


    def gadget(nv, edges, s):
        """edges: list of (a,b,w) with a<b. Returns sympy Ghat (branch s) and index maps."""
        m = len(edges)
        n = nv + 2 * m
        G = sp.zeros(n, n)
        W = [0] * nv
        for a, b, w in edges:
            W[a] += w; W[b] += w
        for v in range(nv):
            G[v, v] = sp.Rational(14, 15) * t ** 2 * (W[v] + 35)
        for k, (a, b, w) in enumerate(edges):
            p, q = nv + 2 * k, nv + 2 * k + 1
            G[p, p] = G[q, q] = sp.Rational(8, 7)
            G[p, q] = I * s[k]; G[q, p] = -I * s[k]
            x = t if w == 1 else t * (1 + I)
            G[p, a] = x; G[q, a] = -I * x; G[p, b] = x; G[q, b] = I * x
            for r in (p, q):
                G[a, r] = sp.conjugate(G[r, a]); G[b, r] = sp.conjugate(G[r, b])
        return G


    def loads(nv, edges, s):
        o = [0] * nv
        for (a, b, w), sg in zip(edges, s):
            o[b if sg == 1 else a] += w
        return o


    def vertex_certificate(nv, edges, s, G, v):
        n = G.shape[0]
        z = sp.zeros(n, 1); z[v] = 1
        for k, (a, b, w) in enumerate(edges):
            if v not in (a, b):
                continue
            p, q = nv + 2 * k, nv + 2 * k + 1
            P = G.extract([p, q], [p, q])
            Bv = sp.Matrix([G[p, v], G[q, v]])
            y = -P.inv() * Bv
            z[p] = y[0]; z[q] = y[1]
        num = sp.simplify((z.H * G * z)[0, 0])
        den = sp.simplify((z.H * z)[0, 0])
        supp = sum(1 for i in range(n) if z[i] != 0)
        return sp.nsimplify(num), sp.nsimplify(den), supp


    def check_exact(nv, edges, max_signs=None):
        worst = None; maxsupp = 0; count = 0
        for s in itertools.product([1, -1], repeat=len(edges)):
            o = loads(nv, edges, s)
            vs = [v for v in range(nv) if o[v] >= 3]
            require(vs, "v24_localized_certificate: vs :: 'feasible orientation found: not a NO instance'")
            G = gadget(nv, edges, s)
            num, den, supp = vertex_certificate(nv, edges, s, G, vs[0])
            r = sp.nsimplify(num / den)
            worst = r if worst is None or r > worst else worst
            maxsupp = max(maxsupp, supp); count += 1
            if max_signs and count >= max_signs:
                break
        return worst, maxsupp, count


    def check_unintended_2x2(nv, edges):
        """For every off-diagonal entry and every nonzero integer shift k in {+-1,+-2},
        the 2x2 principal minor certificate has Rayleigh quotient < -0.72 (exact)."""
        s0 = [1] * len(edges)
        G = gadget(nv, edges, s0)
        n = G.shape[0]
        worst = -sp.oo
        private = {(nv + 2 * k, nv + 2 * k + 1) for k in range(len(edges))}
        for i in range(n):
            for j in range(i + 1, n):
                for k in (-2, -1, 1, 2):
                    if (i, j) in private:
                        # intended values are +i and -i (k=0 and k=-1 from +i); others are unintended
                        val = G[i, j] + 2 * I * k
                        if sp.simplify(val - (-I)) == 0:
                            continue
                    else:
                        val = G[i, j] + 2 * I * k
                    a, c = G[i, i], G[j, j]
                    lam_min = (a + c) / 2 - sp.sqrt(((a - c) / 2) ** 2 + sp.Abs(val) ** 2)
                    worst = sp.Max(worst, sp.nsimplify(lam_min))
        return worst


    def corr_from_G(Gnum):
        n = Gnum.shape[0]; d = n + 1
        C = np.ones((d, d), complex)
        dg = np.real(np.diag(Gnum))
        for i in range(n):
            C[i + 1, 0] = C[0, i + 1] = np.exp(-np.pi * dg[i] / 2)
            for j in range(n):
                if i != j:
                    beta = (dg[i] + dg[j]) / 2 - Gnum[i, j].real
                    C[i + 1, j + 1] = np.exp(np.pi * (-beta + 1j * Gnum[i, j].imag))
        return C


    def nearest_embeddable_attempt(C, Gbranch, trials=3, seed=0):
        """Minimise a smooth surrogate of max|C - exp(ell)| over CPSD ell built from an
        anchored PSD matrix M M^dag plus diagonal phases, started near the given branch."""
        rng = np.random.default_rng(seed)
        d = C.shape[0]; n = d - 1
        w, U = np.linalg.eigh(Gbranch)
        M0 = U @ np.diag(np.sqrt(np.clip(w, 0, None)))
        best = np.inf
        for tr in range(trials):
            x0 = np.concatenate([(M0 + 0.01 * rng.normal(size=M0.shape)).real.ravel(),
                                 (M0.imag + 0.01 * rng.normal(size=M0.shape)).ravel(),
                                 0.01 * rng.normal(size=n)])

            def build(x):
                Mr = x[:n * n].reshape(n, n); Mi = x[n * n:2 * n * n].reshape(n, n); a = x[2 * n * n:]
                M = Mr + 1j * Mi
                Gp = M @ M.conj().T  # PSD anchored matrix (units of pi)
                ell = np.zeros((d, d), complex)
                # recover ell from anchored G with zero anchor-row phases: ell_i0 = -G_ii/2, ell_ij = G_ij - (G_ii+G_jj)/2
                dg = np.real(np.diag(Gp))
                ell[1:, 0] = -dg / 2; ell[0, 1:] = -dg / 2
                ell[1:, 1:] = Gp - (dg[:, None] + dg[None, :]) / 2
                np.fill_diagonal(ell, 0)
                ph = np.concatenate([[0.0], a])
                ell = np.pi * ell + 1j * (ph[:, None] - ph[None, :])
                return np.exp(ell)

            def f(x, p=40):
                Dm = build(x)
                e = np.abs(Dm - C)
                return (np.sum(e ** p)) ** (1 / p)

            res = minimize(f, x0, method='L-BFGS-B', options=dict(maxiter=3000))
            Dm = build(res.x)
            best = min(best, float(np.max(np.abs(Dm - C))))
        return best



    def random_cubic_graph(nv, seed):
        rng = np.random.default_rng(seed)
        while True:
            stubs = [v for v in range(nv) for _ in range(3)]
            rng.shuffle(stubs)
            E = set(); ok = True
            for i in range(0, len(stubs), 2):
                a, b = sorted((stubs[i], stubs[i + 1]))
                if a == b or (a, b) in E:
                    ok = False; break
                E.add((a, b))
            if ok:
                return [(a, b, int(rng.integers(1, 3))) for (a, b) in sorted(E)]


    def gadget_numeric(nv, edges):
        t = 1 / 13
        m = len(edges); n = nv + 2 * m
        G = np.zeros((n, n), complex); W = np.zeros(nv)
        for a, b, w in edges:
            W[a] += w; W[b] += w
        for v in range(nv):
            G[v, v] = 14 / 15 * t * t * (W[v] + 35)
        for k, (a, b, w) in enumerate(edges):
            p, q = nv + 2 * k, nv + 2 * k + 1
            G[p, p] = G[q, q] = 8 / 7; G[p, q] = 1j; G[q, p] = -1j
            x = t if w == 1 else t * (1 + 1j)
            G[p, a] = x; G[q, a] = -1j * x; G[p, b] = x; G[q, b] = 1j * x
            for r in (p, q):
                G[a, r] = np.conj(G[r, a]); G[b, r] = np.conj(G[r, b])
        return G

    rows = []
    def record(name, cls, ok, data):
        rows.append({'name': name, 'class': cls, 'status': 'PASS' if bool(ok) else 'FAIL', 'data': data})

    mu = sp.Rational(98, 11355)
    K4 = [(0, 1, 2), (0, 2, 2), (0, 3, 2), (1, 2, 2), (1, 3, 2), (2, 3, 2)]
    K4m = [(0, 1, 2), (0, 2, 2), (0, 3, 1), (1, 2, 2), (1, 3, 2), (2, 3, 2)]
    prism = [(0, 1, 2), (1, 2, 2), (0, 2, 2), (3, 4, 2), (4, 5, 2), (3, 5, 2), (0, 3, 2), (1, 4, 2), (2, 5, 2)]
    res = {}
    for name, nv, E in [('K4_w2', 4, K4), ('K4_mixed', 4, K4m), ('prism_w2', 6, prism)]:
        worst, maxsupp, cnt = check_exact(nv, E)
        res[name] = dict(branches=cnt, worst_rayleigh=str(worst), worst_float=float(worst), max_support=maxsupp)
    record('Corollary 6.3 vertex certificates (exact)', 'C',
           all(r['max_support'] <= 7 and sp.Rational(r['worst_rayleigh']) <= -mu for r in res.values()), res)
    w2 = check_unintended_2x2(4, K4)
    record('Lemma 5.3 / Corollary 6.3 2x2 certificates for unintended shifts (exact)', 'C', w2 < -sp.Rational(72, 100),
           {'worst_lambda_min': str(w2), 'float': float(w2)})
    eps_star = 7 * math.pi * math.exp(-8 * math.pi / 7) / 34065
    Gs = gadget(4, K4, [1] * 6)
    Gnum = np.array(Gs.evalf(), dtype=complex)
    C = corr_from_G(Gnum)
    best = nearest_embeddable_attempt(C, Gnum + 0.05 * np.eye(Gnum.shape[0]), trials=2)
    record('Numerical search for a nearby embeddable channel (K4, d=17)', 'X', best >= eps_star,
           {'best_max_distance_found': best, 'eps_star': eps_star})
    lam = {}
    for nv in (8, 20, 40, 60):
        E = random_cubic_graph(nv, seed=nv)
        Cn = corr_from_G(gadget_numeric(nv, E))
        lam[str(1 + nv + 2 * len(E))] = float(np.min(np.linalg.eigvalsh(Cn)))
    record('lambda_min(C) for growing d (Lemma 5.6 remark)', 'V', all(v > 0 for v in lam.values()), {'d_to_lambda_min': lam})
    status = 'PASS' if all(r['status'] == 'PASS' for r in rows) else 'FAIL'
    return {'status': status, 'rows': rows}


# Source: v24_stability_paths.py; arithmetic and finite sample scope retained.
def suite_v24_stability_paths(profile="quick", mutation="none"):
    """ZS-M76 v2.4: finite controls for the stability theorem (Lemmas 7.3-7.5, Theorem 7.6).

    Piecewise-constant time-dependent GKLS paths are integrated in the lab frame and in the
    Hamiltonian interaction picture.  Along each path the script computes the Lowdin frame of the
    top eigenvectors, the off-frame noise N(t), the exact derivative of the overlap sum S(t), the
    frame length, the dissipation budget kappa, and the embeddable Schur matrix C'' built in Step 5
    of the proof.  Every inequality of the proof is compared with its numerical value.  A second
    part runs an adversarial optimisation of six-segment paths towards a non-embeddable d=3 target.
    These are finite controls (class V); they do not prove the theorem.
    """
    import numpy as np
    from scipy.linalg import expm
    from scipy.optimize import minimize

    args = SimpleNamespace(quick=(profile != 'full'))
    rng = np.random.default_rng(20261020)


    def traceless_basis(d):
        """HS-orthonormal traceless basis of M_d (generalized Gell-Mann, normalized)."""
        B = []
        for j in range(d):
            for k in range(j + 1, d):
                X = np.zeros((d, d), complex); X[j, k] = X[k, j] = 1 / np.sqrt(2); B.append(X)
                Y = np.zeros((d, d), complex); Y[j, k] = -1j / np.sqrt(2); Y[k, j] = 1j / np.sqrt(2); B.append(Y)
        for l in range(1, d):
            Z = np.zeros((d, d), complex)
            for m in range(l):
                Z[m, m] = 1
            Z[l, l] = -l
            Z /= np.sqrt(l * (l + 1))
            B.append(Z)
        return B


    def sup_ham(H):
        d = H.shape[0]; I = np.eye(d)
        return -1j * (np.kron(I, H) - np.kron(H.T, I))


    def sup_diss(K):
        d = K.shape[0]; I = np.eye(d); KK = K.conj().T @ K
        return np.kron(K.conj(), K) - 0.5 * np.kron(I, KK) - 0.5 * np.kron(KK.T, I)


    def apply(S, X):
        d = X.shape[0]
        return (S @ X.reshape(-1, order='F')).reshape(d, d, order='F')


    def choi(S, d):
        J = np.zeros((d * d, d * d), complex)
        for i in range(d):
            for j in range(d):
                E = np.zeros((d, d), complex); E[i, j] = 1
                J += np.kron(E, apply(S, E))
        return J


    def tn(X):
        return np.sum(np.linalg.svd(X, compute_uv=False))


    def diamond_ub(S, d):
        return tn(choi(S, d))  # ||Phi||_diamond <= ||J(Phi)||_1 (unnormalized Choi)


    def lowdin_frame(rhos, prev_vecs=None):
        d = len(rhos)
        V = np.zeros((d, d), complex)
        lam1 = []
        for j, r in enumerate(rhos):
            w, U = np.linalg.eigh(r)
            v = U[:, -1]; lam1.append(w[-1])
            if prev_vecs is not None:  # discrete parallel transport of the phase
                ph = np.vdot(prev_vecs[:, j], v)
                v = v * (np.conj(ph) / abs(ph)) if abs(ph) > 1e-14 else v
            else:
                ph = v[j]; v = v * (np.conj(ph) / abs(ph))
            V[:, j] = v
        S = V.conj().T @ V
        w, U = np.linalg.eigh(S)
        Sinvh = U @ np.diag(w ** -0.5) @ U.conj().T
        Y = V @ Sinvh
        alpha = np.linalg.norm(S - np.eye(d), 2)
        return V, Y, np.array(lam1), alpha


    def schur_gen_from_diag(Ks):
        """Schur coefficients g_ij of sum_alpha D[diag(k_alpha)] (eq. (3.4))."""
        d = Ks[0].shape[0]
        g = np.zeros((d, d), complex)
        for K in Ks:
            k = np.diag(K)
            g += np.outer(k, k.conj()) - 0.5 * (np.abs(k)[:, None] ** 2 + np.abs(k)[None, :] ** 2)
        return g


    def random_path(d, nseg, mode, eps_off, rate, hscale, seed_rng):
        """Return list of (H, [K_alpha]) piecewise-constant segments (lab frame).

        mode 'rotate-return': H_t rotates the frame and returns; dissipators are
        diagonal in the instantaneous pointer frame W_t P_j W_t^dag plus a random
        off-frame part of relative size eps_off.
        """
        Fs = traceless_basis(d)
        segs = []
        H0 = seed_rng.normal(size=(d, d)) + 1j * seed_rng.normal(size=(d, d)); H0 = hscale * (H0 + H0.conj().T) / 2
        H1 = seed_rng.normal(size=(d, d)) + 1j * seed_rng.normal(size=(d, d)); H1 = hscale * (H1 + H1.conj().T) / 2
        half = nseg // 2
        Hs = [H0 if s < half // 2 else H1 for s in range(half)]
        Hs = Hs + [-h for h in reversed(Hs)]  # exact return of the unitary part
        W = np.eye(d, dtype=complex)
        dt = 1.0 / nseg
        for s in range(nseg):
            H = Hs[s]
            Wmid = expm(-1j * H * dt / 2) @ W
            Ks = []
            for a in range(2):
                Dg = np.diag(np.sqrt(rate) * (seed_rng.normal(size=d) + 1j * seed_rng.normal(size=d)))
                R = seed_rng.normal(size=(d, d)) + 1j * seed_rng.normal(size=(d, d))
                np.fill_diagonal(R, 0)
                if mode == 'generic':
                    K = np.sqrt(rate) * (seed_rng.normal(size=(d, d)) + 1j * seed_rng.normal(size=(d, d)))
                else:
                    K = Wmid @ (Dg + eps_off * np.sqrt(rate) * R) @ Wmid.conj().T
                K = K - np.trace(K) / d * np.eye(d)  # canonical traceless form
                Ks.append(K)
            # moving trace parts into H is exact for traceless K; we dropped scalar parts
            segs.append((H, Ks))
            W = expm(-1j * H * dt) @ W
        return segs, dt


    def analyse(d, segs, dt, substeps=4):
        I = np.eye(d)
        P = [np.outer(I[j], I[j]).astype(complex) for j in range(d)]
        Lam = np.eye(d * d, dtype=complex)
        LamI = np.eye(d * d, dtype=complex)  # interaction picture propagator
        W = np.eye(d, dtype=complex)
        kappa = 0.0
        intN = 0.0
        intKO = 0.0  # int sum ||K|| ||O||
        max_eps0 = 0.0
        min_slack_A = np.inf
        Sprev = 0.0
        sumB_minus_2N = []
        frame_len = 0.0
        prevV = None
        prevY = np.eye(d, dtype=complex)
        g_int = np.zeros((d, d), complex)
        duhamel_err_bound = 0.0
        E_max = 0.0
        alpha_max = 0.0
        h = dt / substeps
        for (H, Ks) in segs:
            for sub in range(substeps):
                # interaction-picture jump operators at the midpoint
                Wm = expm(-1j * H * h / 2) @ W
                Kt = [Wm.conj().T @ K @ Wm for K in Ks]
                rhos = [apply(LamI, Pj) for Pj in P]
                V, Y, lam1, alpha = lowdin_frame(rhos, prevV)
                Q = [np.outer(Y[:, j], Y[:, j].conj()) for j in range(d)]
                eps0 = max(tn(rhos[j] - Q[j]) for j in range(d))
                max_eps0 = max(max_eps0, eps0)
                alpha_max = max(alpha_max, alpha)
                E_now = sum(np.real(np.trace(rhos[j] @ rhos[k])) for j in range(d) for k in range(d) if j != k)
                E_max = max(E_max, E_now)
                Khat = [Y.conj().T @ K @ Y for K in Kt]
                Nt = sum(np.linalg.norm(Kh - np.diag(np.diag(Kh)), 'fro') ** 2 for Kh in Khat)
                K2 = sum(np.linalg.norm(K, 2) ** 2 for K in Kt)
                KO = sum(np.linalg.norm(Kh, 2) * np.linalg.norm(Kh - np.diag(np.diag(Kh)), 2) for Kh in Khat)
                # exact derivative of S(t) at this time
                Dsup = sum(sup_diss(K) for K in Kt)
                dS = 0.0
                for j in range(d):
                    for k in range(d):
                        if j != k:
                            dS += np.real(np.trace(apply(Dsup, rhos[j]) @ rhos[k]) + np.trace(rhos[j] @ apply(Dsup, rhos[k])))
                lowerA = 2 * Nt - 8 * d * (d - 1) * eps0 * K2
                min_slack_A = min(min_slack_A, dS - lowerA)
                sumB_minus_2N.append(dS - 2 * Nt)
                intN += Nt * h
                intKO += KO * h
                kappa += sum(np.linalg.norm(K, 'fro') ** 2 for K in Kt) * h
                g_int += schur_gen_from_diag(Khat) * h
                # frame speed (finite difference of Y), measured at the end of the substep below
                # advance
                S_step = expm(Dsup * h)
                LamI = S_step @ LamI
                Lam = expm((sup_ham(H) + sum(sup_diss(K) for K in Ks)) * h) @ Lam
                W = expm(-1j * H * h) @ W
                prevV = V
                rhos_new = [apply(LamI, Pj) for Pj in P]
                V2, Y2, _, _ = lowdin_frame(rhos_new, V)
                frame_len += np.linalg.norm(Y2 - Y, 2)
        return dict(Lam=Lam, W1=W, LamI=LamI, kappa=kappa, intN=intN, intKO=intKO,
                    max_eps0=max_eps0, min_slack_A=min_slack_A, frame_len=frame_len,
                    g_int=g_int, E_max=E_max, alpha_max=alpha_max,
                    maxabs_B_minus_2N=float(np.max(np.abs(sumB_minus_2N))))


    def run_case(d, mode, eps_off, rate, hscale, nseg=24, substeps=4):
        segs, dt = random_path(d, nseg, mode, eps_off, rate, hscale, rng)
        R = analyse(d, segs, dt, substeps)
        Lam = R['Lam']
        # Schur projection C of T
        C = np.zeros((d, d), complex)
        for i in range(d):
            for j in range(d):
                E = np.zeros((d, d), complex); E[i, j] = 1
                C[i, j] = apply(Lam, E)[i, j]
        np.fill_diagonal(C, 1.0)
        PhiC = np.diag(C.reshape(-1, order='F'))
        delta = diamond_ub(Lam - PhiC, d)
        c = np.min(np.abs(C))
        # constructed embeddable Schur matrix C'' (proof): C' = exp(int g), then phase twist
        Cp = np.exp(R['g_int'])
        # endpoint unitary U = W1 Y1 (Y1 from final frame); compare via pointer phases
        I = np.eye(d)
        rhos1 = [apply(R['LamI'], np.outer(I[j], I[j]).astype(complex)) for j in range(d)]
        V1, Y1, _, _ = lowdin_frame(rhos1)
        U = R['W1'] @ Y1
        ph = np.angle(np.diag(U))
        Cpp = Cp * np.exp(1j * (ph[:, None] - ph[None, :]))
        err_max = np.max(np.abs(C - Cpp))
        # CPSD check of log of C''
        ell = np.log(Cpp + 0j)
        # anchored PSD with the actual branch used (g_int + phase term)
        ellb = R['g_int'] + 1j * (ph[:, None] - ph[None, :])
        G = ellb[1:, 1:] - ellb[1:, :1] - ellb[:1, 1:]
        G = (G + G.conj().T) / 2
        cpsd_min = np.min(np.linalg.eigvalsh(G))
        # theorem quantities
        tau_bound = 4 * np.sqrt(R['kappa'] * R['intN']) + 2 * R['intN'] + 2 * R['frame_len']
        detT = np.linalg.det(Lam)
        kappa_det = float(-np.log(abs(detT)) / d)
        g = 1 - 2 * R['E_max']
        a = R['alpha_max']
        Ca = (1 - a) ** -0.5 + (1 + a) * (1 - a) ** -1.5
        frame_bound = Ca / g * (2 * np.sqrt(d) * np.sqrt(R['kappa'] * R['intN']) + (6 * a + 2 * R['E_max']) * d * R['kappa'])
        Cfinal = (1 + np.sqrt(2 * d))
        final_bound_chain = Cfinal * (4 * np.sqrt(R['kappa'] * R['intN']) + 2 * R['intN'] + 2 * frame_bound + delta)
        return dict(kappa_det=kappa_det, frame_bound=float(frame_bound), final_bound_chain=float(final_bound_chain),
                    d=d, eps_off=eps_off, rate=rate, hscale=hscale, delta_ub=float(delta), c=float(c),
                    kappa=float(R['kappa']), intN=float(R['intN']), max_eps0=float(R['max_eps0']),
                    E_max=float(R['E_max']), alpha_max=float(R['alpha_max']),
                    min_slack_stepA=float(R['min_slack_A']), maxabs_B_minus_2N=R['maxabs_B_minus_2N'],
                    stepA_bound_intN=float(d * (d - 1) * (delta + 4 * R['max_eps0'] * R['kappa'])),
                    frame_len=float(R['frame_len']), tau_bound=float(tau_bound),
                    err_max_C_minus_Cpp=float(err_max), cpsd_min_eig=float(cpsd_min))



    def adversary(Omega, nseg=6, trials=2, maxiter=400, seed=3):
        d = 3
        loc = np.random.default_rng(seed)
        ell = np.zeros((d, d), complex)
        ell[1, 0] = -0.5; ell[2, 0] = -0.5; ell[1, 2] = -0.5 + 1j * Omega
        ell = ell + ell.conj().T
        C = np.exp(ell)
        PhiC = np.diag(C.reshape(-1, order='F'))
        npar = d * d + 4 * d * d

        def unpack(x):
            segs = []
            for s in range(nseg):
                y = x[s * npar:(s + 1) * npar]
                Hr = y[:d * d].reshape(d, d)
                H = (Hr + Hr.T) / 2 + 1j * (Hr - Hr.T) / 2
                Ks = []
                for k in range(2):
                    z = y[d * d + k * 2 * d * d: d * d + (k + 1) * 2 * d * d]
                    K = z[:d * d].reshape(d, d) + 1j * z[d * d:].reshape(d, d)
                    Ks.append(K - np.trace(K) / d * np.eye(d))
                segs.append((H, Ks))
            return segs

        def endpoint(x):
            T = np.eye(d * d, dtype=complex)
            for (H, Ks) in unpack(x):
                T = expm((sup_ham(H) + sum(sup_diss(K) for K in Ks)) / nseg) @ T
            return T

        obj = lambda x: np.linalg.norm(endpoint(x) - PhiC, 'fro') ** 2
        best = None
        for _ in range(trials):
            res = minimize(obj, 0.6 * loc.normal(size=nseg * npar), method='L-BFGS-B', options=dict(maxiter=maxiter))
            if best is None or res.fun < best.fun:
                best = res
        T = endpoint(best.x)
        R = analyse(d, unpack(best.x), 1.0 / nseg, substeps=8)
        I = np.eye(d)
        rhos1 = [apply(R['LamI'], np.outer(I[j], I[j]).astype(complex)) for j in range(d)]
        _, Y1, _, _ = lowdin_frame(rhos1)
        U = R['W1'] @ Y1
        ph = np.angle(np.diag(U))
        Cpp = np.exp(R['g_int']) * np.exp(1j * (ph[:, None] - ph[None, :]))
        return dict(Omega=Omega, triangle_bound=float(np.sqrt(0.75)), frob_min=float(np.sqrt(best.fun)),
                    delta_ub=float(diamond_ub(T - PhiC, d)), E_max=float(R['E_max']),
                    err_C_minus_Cpp=float(np.max(np.abs(C - Cpp))))


    rows = []
    def record(name, cls, ok, data):
        rows.append({'name': name, 'class': cls, 'status': 'PASS' if bool(ok) else 'FAIL', 'data': data})

    dims = (2, 3, 4) if args.quick else (2, 3, 4, 5, 6)
    cases = []
    for d in dims:
        for eps_off in (0.0, 1e-2, 5e-2, 2e-1):
            for hscale in (0.5, 5.0, 20.0):
                cases.append(run_case(d, 'rotate-return', eps_off, rate=0.3, hscale=hscale, nseg=24 if hscale < 10 else 60))
        for rate in (1e-4, 1e-3):
            cases.append(run_case(d, 'generic', 0.0, rate=rate, hscale=5.0))
    inreg = [r for r in cases if r['E_max'] < 0.5]
    record('kappa equals -(1/d) log det T (7.4a)', 'V', max(abs(r['kappa'] - r['kappa_det']) for r in cases) < 1e-10,
           {'max_abs_diff': max(abs(r['kappa'] - r['kappa_det']) for r in cases), 'paths': len(cases)})
    record('Lemma 7.3 identity at t=0 and integrated bound (7.24)', 'V',
           all(r['min_slack_stepA'] > -1e-9 for r in cases) and all(r['intN'] <= r['stepA_bound_intN'] for r in inreg),
           {'paths_in_regime_E<1/2': len(inreg), 'max_intN_over_bound': max(r['intN'] / r['stepA_bound_intN'] for r in inreg)})
    record('Frame length (7.26)', 'V', all(r['frame_len'] <= r['frame_bound'] for r in inreg),
           {'max_ratio': max(r['frame_len'] / r['frame_bound'] for r in inreg)})
    record('Constructed C\'\' within chain (7.22) and CPSD', 'V',
           all(r['err_max_C_minus_Cpp'] <= r['final_bound_chain'] for r in inreg) and all(r['cpsd_min_eig'] > -1e-9 for r in cases),
           {'max_err_over_chain': max(r['err_max_C_minus_Cpp'] / r['final_bound_chain'] for r in inreg),
            'max_err_over_delta_ub': max(r['err_max_C_minus_Cpp'] / r['delta_ub'] for r in cases if r['delta_ub'] > 0)})
    adv = [] if args.quick else [adversary(1.2), adversary(0.95)]
    if adv:
        record('Adversarial optimisation towards non-embeddable d=3 targets', 'X',
               all(a['frob_min'] > 0.01 for a in adv), {'runs': adv})

    def lemma74_random(trials=3000, seed=5):
        """Pointwise check of (7.17) and of identity (7.18) on random states and jump operators."""
        loc = np.random.default_rng(seed)
        def Dm(K, X):
            KK = K.conj().T @ K
            return K @ X @ K.conj().T - 0.5 * (KK @ X + X @ KK)
        worst_ratio = 0.0; worst_id = 0.0
        for _ in range(trials):
            d = int(loc.integers(2, 7)); E = loc.uniform(0, 0.45)
            U, _r = np.linalg.qr(loc.normal(size=(d, d)) + 1j * loc.normal(size=(d, d)))
            rest = loc.dirichlet(np.ones(d - 1)) * loc.uniform(0, E)
            lam = np.concatenate([[1 - rest.sum()], rest])
            rho = U @ np.diag(lam) @ U.conj().T
            Ks = [loc.uniform(0.01, 3) * (loc.normal(size=(d, d)) + 1j * loc.normal(size=(d, d))) for _ in range(int(loc.integers(1, 4)))]
            rdot = sum(Dm(K, rho) for K in Ks)
            v = U[:, 0]; P = np.outer(v, v.conj()); Q = np.eye(d) - P
            w, V = np.linalg.eigh(rho); idx = int(np.argmax(w)); l1 = w[idx]
            Pdot = np.zeros((d, d), complex)
            for k in range(d):
                if k != idx:
                    Pk = np.outer(V[:, k], V[:, k].conj())
                    Pdot += (Pk @ rdot @ P + P @ rdot @ Pk) / (l1 - w[k])
            rhs = 0.0
            for K in Ks:
                nK = np.linalg.norm(K, 2); r = Q @ K @ v; u = Q @ K.conj().T @ v; k = np.vdot(v, K @ v)
                rhs += nK * (1.5 * np.linalg.norm(r) + 0.5 * np.linalg.norm(u)) + 2 * E * nK ** 2
                worst_id = max(worst_id, float(np.linalg.norm(Q @ Dm(K, P) @ v - (np.conj(k) * r - 0.5 * k * u - 0.5 * Q @ K.conj().T @ r))))
            worst_ratio = max(worst_ratio, float(np.linalg.norm(Pdot, 2) / (rhs / (1 - 2 * E))))
        return dict(trials=trials, max_lhs_over_rhs=worst_ratio, max_residual_7_18=worst_id)

    l74 = lemma74_random()
    record('Lemma 7.4: (7.17) and identity (7.18) on random instances', 'V', l74['max_lhs_over_rhs'] <= 1 and l74['max_residual_7_18'] < 1e-10, l74)

    status = 'PASS' if all(r['status'] == 'PASS' for r in rows) else 'FAIL'
    return {'status': status, 'rows': rows, 'paths': cases}


# Source: verify_entropy_rounding.py; arithmetic and finite sample scope retained.
def suite_entropy_rounding_checks(profile="quick", mutation="none"):
    """Finite controls of the v2.5 linear-entropy estimate (not a universal proof).

    Random-state instantaneous residual tests; nonnormal nonunital time-dependent
    paths with exact segment propagators and Gauss-Legendre quadrature; elementary
    constant comparisons. Only these arithmetic/sample scopes are certified.
    """
    from fractions import Fraction
    from math import factorial
    import numpy as np
    from scipy.linalg import expm
    from numpy.polynomial.legendre import leggauss


    def diss(k, x):
        kk = k.conj().T @ k
        return k @ x @ k.conj().T - (kk @ x + x @ kk) / 2


    def super_diss(k):
        d = len(k); eye = np.eye(d); kk = k.conj().T @ k
        return np.kron(k.conj(), k) - (np.kron(eye, kk) + np.kron(kk.T, eye)) / 2


    def apply(s, x):
        return (s @ x.reshape(-1, order='F')).reshape(x.shape, order='F')


    def frame(rhos):
        cols, es = [], []
        for rho in rhos:
            w, u = np.linalg.eigh((rho + rho.conj().T) / 2)
            cols.append(u[:, -1]); es.append(max(0.0, 1-w[-1]))
        v = np.column_stack(cols)
        gram = v.conj().T @ v
        w, u = np.linalg.eigh(gram)
        q = v @ u @ np.diag(w**(-0.5)) @ u.conj().T
        alpha = np.linalg.norm(gram - np.eye(len(rhos)), 2)
        return v, q, sum(es), alpha


    def instantaneous(rhos, ks):
        v, q, e, alpha = frame(rhos)
        variance, off, derivative = 0., 0., 0.
        k2 = sum(np.linalg.norm(k, 2)**2 for k in ks)
        d = len(rhos)
        for j, rho in enumerate(rhos):
            for k in ks:
                kv = k @ v[:, j]
                kq = k @ q[:, j]
                variance += np.linalg.norm(kv - v[:, j]*np.vdot(v[:, j], kv))**2
                off += np.linalg.norm(kq - q[:, j]*np.vdot(q[:, j], kq))**2
                derivative -= 2*np.trace(rho @ diss(k, rho)).real
        return dict(V=variance, N=off, Fprime=derivative, e=e, alpha=alpha, k2=k2,
                    entropy_error=abs(derivative - 2*variance),
                    entropy_bound=16*e*k2,
                    transfer_bound=2*variance+8*d*alpha**2*k2)


    def main():
        rng = np.random.default_rng(20261021)
        checks=[]
        max_entropy_ratio=0.; max_transfer_ratio=0.
        # Slightly rotated, slightly mixed pointer states; operators are nonnormal.
        for d in range(2, 9):
            for _ in range(100):
                rhos=[]
                for j in range(d):
                    v=np.eye(d, dtype=complex)[:, j] + 0.03*(rng.normal(size=d)+1j*rng.normal(size=d))
                    v /= np.linalg.norm(v)
                    x=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
                    rem=x@x.conj().T; rem/=np.trace(rem)
                    eps=rng.uniform(1e-6, 0.02)
                    rhos.append((1-eps)*np.outer(v,v.conj())+eps*rem)
                ks=[rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)) for a in range(2)]
                z=instantaneous(rhos, ks)
                max_entropy_ratio=max(max_entropy_ratio,z['entropy_error']/z['entropy_bound'])
                max_transfer_ratio=max(max_transfer_ratio,z['N']/z['transfer_bound'])
                require(z['entropy_error'] <= z['entropy_bound'] + 1e-10, "entropy_rounding_checks: z['entropy_error'] <= z['entropy_bound'] + 1e-10")
                require(z['N'] <= z['transfer_bound'] + 1e-10, "entropy_rounding_checks: z['N'] <= z['transfer_bound'] + 1e-10")
        checks.append(dict(id='ER-V01',classification='V',scope='700 instantaneous random configurations, d=2..8',
                           max_entropy_ratio=max_entropy_ratio,max_transfer_ratio=max_transfer_ratio,status='PASS'))

        # Piecewise time-dependent dissipative paths. No assumption of unitality.
        nodes, weights=leggauss(16)
        path_rows=[]
        for d in range(2,6):
            eye=np.eye(d,dtype=complex)
            pointers=[np.outer(eye[:,j],eye[:,j].conj()) for j in range(d)]
            for eps in (1e-5,1e-4,1e-3):
                rhos=[p.copy() for p in pointers]
                integral_v=integral_n=kappa=0.
                max_entropy_ratio_path=0.
                for seg in range(5):
                    ks=[]
                    for a in range(2):
                        k=np.diag(.25*(rng.normal(size=d)+1j*rng.normal(size=d)))
                        k+=eps*(rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)))
                        k-=np.trace(k)/d*eye
                        ks.append(k)
                    gen=sum(super_diss(k) for k in ks)
                    dt=.2
                    for node,weight in zip(nodes,weights):
                        sm=expm(gen*dt*(node+1)/2)
                        rs=[apply(sm,r) for r in rhos]
                        z=instantaneous(rs,ks)
                        integral_v+=weight*dt/2*z['V']
                        integral_n+=weight*dt/2*z['N']
                        if z['entropy_bound']>1e-15:
                            max_entropy_ratio_path=max(max_entropy_ratio_path,z['entropy_error']/z['entropy_bound'])
                    send=expm(gen*dt)
                    rhos=[apply(send,r) for r in rhos]
                    kappa+=dt*sum(np.linalg.norm(k,'fro')**2 for k in ks)
                delta=max(np.sum(np.abs(np.linalg.eigvalsh((r-p+r.conj().T-p.conj().T)/2))) for r,p in zip(rhos,pointers))
                E=2*d*(d-1)*delta
                require(E<1/3, 'entropy_rounding_checks: E<1/3')
                alpha=(d-1)*np.sqrt(2*delta)/(1-E)
                final_F=sum(1-np.trace(r@r).real for r in rhos)
                bound_v=d*delta/2+8*E*kappa
                bound_n=d*delta+16*E*kappa+8*d*alpha**2*kappa
                require(final_F<=d*delta+1e-12, 'entropy_rounding_checks: final_F<=d*delta+1e-12')
                require(integral_v<=bound_v+1e-12, 'entropy_rounding_checks: integral_v<=bound_v+1e-12')
                require(integral_n<=bound_n+1e-12, 'entropy_rounding_checks: integral_n<=bound_n+1e-12')
                path_rows.append(dict(d=d,eps=eps,delta=delta,E=E,kappa=kappa,
                                      integral_V=integral_v,V_bound=bound_v,V_ratio=integral_v/bound_v,
                                      integral_N=integral_n,N_bound=bound_n,N_ratio=integral_n/bound_n,
                                      instantaneous_entropy_ratio_max=max_entropy_ratio_path))
        checks.append(dict(id='ER-V02',classification='V',scope='12 nonunital time-dependent paths, d=2..5, 16-point quadrature per segment',
                           max_integrated_V_ratio=max(x['V_ratio'] for x in path_rows),
                           max_integrated_N_ratio=max(x['N_ratio'] for x in path_rows),status='PASS'))
        # Rational/squared comparisons can all be checked without floating point.
        require(36**2*2*4 < 9*35**2, 'entropy_rounding_checks: 36**2*2*4 < 9*35**2')  # (36/35)*sqrt2 <3/2
        require(25 < 32, 'entropy_rounding_checks: 25 < 32')               # 1/(4sqrt2)<1/5
        # C_(1/5) = (5/2)*sqrt(5/4)<3.
        require(125 < 144, 'entropy_rounding_checks: 125 < 144')
        require(54*5 < 16*17, 'entropy_rounding_checks: 54*5 < 16*17')
        require(64 < 72, 'entropy_rounding_checks: 64 < 72')               # 4/sqrt72<1/2
        require(24**2 < 17**2*2, 'entropy_rounding_checks: 24**2 < 17**2*2')
        require(72*4 < 17**2, 'entropy_rounding_checks: 72*4 < 17**2')
        require(17*10+85+1376+10 < 1650, 'entropy_rounding_checks: 17*10+85+1376+10 < 1650')
        require(495**2 < 400**2*2, 'entropy_rounding_checks: 495**2 < 400**2*2')
        require(sum(Fraction(5**j, factorial(j)) for j in range(7)) > 100, 'entropy_rounding_checks: sum(Fraction(5**j, factorial(j)) for j in range(7)) > 100')
        require(Fraction(400*5, 200000000) < Fraction(1, 80000), 'entropy_rounding_checks: Fraction(400*5, 200000000) < Fraction(1, 80000)')
        checks.append(dict(id='ER-C01',classification='C',scope='exact integer comparisons in constant chain',status='PASS'))
        import mpmath as mp
        mp.mp.dps=60
        gap_ratio=mp.mpf(400)*mp.log(100)/mp.mpf(200000000)*80000
        require(gap_ratio<1, 'entropy_rounding_checks: gap_ratio<1')
        checks.append(dict(id='ER-V03',classification='V',scope='60-digit numerical hardness constant (analytic ln100<5 also suffices)',
                           ratio_to_gap=str(gap_ratio),status='PASS'))
        result=dict(checks=checks,paths=path_rows,census=dict(P=0,C=1,V=3,FAIL=0),
                    limitations='Finite arithmetic and path controls do not certify the universal theorem, novelty, physical realization, or research grade.')
        return result

    return main()


# Source: v25_interior_verify.py; arithmetic and finite sample scope retained.
def suite_v25_interior_verify(profile="quick", mutation="none"):
    """Finite controls for the explicit interior lemma; not a universal proof.

    Positive controls perturb a regularized coherent Schur channel in arbitrary
    HP/TP directions, then reconstruct the short GKLS correction via logm.
    The negative control removes depolarizing slack, detecting non-CCP logs.
    """
    from fractions import Fraction
    import numpy as np
    import scipy.linalg as la
    import sympy as sp


    def choi_to_super(j, d):
        s = np.zeros((d*d, d*d), complex)
        for a in range(d):
            for c in range(d):
                s[:, a+c*d] = j[a*d:(a+1)*d, c*d:(c+1)*d].reshape(-1, order='F')
        return s


    def super_to_choi(s, d):
        j = np.zeros_like(s)
        for a in range(d):
            for c in range(d):
                j[a*d:(a+1)*d, c*d:(c+1)*d] = s[:, a+c*d].reshape((d, d), order='F')
        return j


    def tnorm(a):
        return float(la.svdvals(a).sum())


    def main():
        rng = np.random.default_rng(7625)
        out = {'scope': 'exact rational constants plus finite HP/TP perturbation controls',
               'not_proved_by_script': ['universal interior theorem', 'novelty', 'NP-hardness', 'research grade'],
               'positive_controls': [], 'negative_control': {}}
        # r<=2p+p/(4d^2)<1/2 and 2d*eta<=p/(2d) in exact rational arithmetic.
        exact = []
        for d in [2,3,4,7,100,1000000]:
            p = Fraction(1,8)
            eta = p / (4*d*d)
            require(2*p+eta < Fraction(1,2), 'v25_interior_verify: 2*p+eta < Fraction(1,2)')
            require(2*d*eta == p/(2*d), 'v25_interior_verify: 2*d*eta == p/(2*d)')
            nu = Fraction(1, 4*10**16*d**7)  # v2.5 gap; ratio identities are scale-independent
            rho = nu/(1600*d**3)
            require(50*d*rho == (nu/8)/(4*d*d), 'v25_interior_verify: 50*d*rho == (nu/8)/(4*d*d)')
            require(nu-2*(nu/8) == 3*nu/4, 'v25_interior_verify: nu-2*(nu/8) == 3*nu/4')
            exact.append(d)
        out['exact_constant_dimensions'] = exact
        exact_slack = []
        for d in [2,3,4]:
            v_exact = sp.Matrix([1 if i == j else 0 for i in range(d) for j in range(d)])
            q_exact = sp.eye(d*d)-v_exact*v_exact.T/d
            j_generator = sp.eye(d*d)/d-v_exact*v_exact.T
            require(q_exact*j_generator*q_exact == q_exact/d, 'v25_interior_verify: q_exact*j_generator*q_exact == q_exact/d')
            require(q_exact*q_exact == q_exact, 'v25_interior_verify: q_exact*q_exact == q_exact')
            # Deliberate normalization omission must not satisfy the identity.
            require(q_exact*j_generator*q_exact != q_exact, 'v25_interior_verify: q_exact*j_generator*q_exact != q_exact')
            exact_slack.append({'d':d,'QJ_Omega_minus_id_Q':'Q/d',
                                'normalization_omission_detected':True})
        out['exact_conditional_choi_slack'] = exact_slack
        for d in [2,3,4]:
            ident = np.eye(d*d)
            v = np.eye(d).reshape(-1, order='F')
            omega = np.outer(v,v)/d
            p = 1/16
            dep = (1-p)*ident+p*omega
            # Real dephasing generator from actual diagonal Lindblad coordinates.
            coords = rng.normal(size=(d,3))/3
            ell = -0.5*np.sum((coords[:,None,:]-coords[None,:,:])**2,axis=-1)
            phases = rng.normal(size=d)
            ell = ell+1j*(phases[:,None]-phases[None,:])
            c = np.exp(ell)
            t = np.diag(c.reshape(-1,order='F'))
            m_bound = d/np.min(np.abs(c))
            radius = p/(4*d*d*m_bound)
            center = dep@t
            qbasis = la.null_space(v[None,:])
            for n in range(15):
                raw = rng.normal(size=(d*d,d*d))+1j*rng.normal(size=(d*d,d*d))
                j = (raw+raw.conj().T)/2
                partial = np.einsum('abcb->ac',j.reshape(d,d,d,d))
                j = j-np.kron(partial,np.eye(d)/d)
                j *= radius/(2*tnorm(j))
                perturb = choi_to_super(j,d)
                require(la.norm(super_to_choi(perturb,d)-j) < 1e-12, 'v25_interior_verify: la.norm(super_to_choi(perturb,d)-j) < 1e-12')
                s = center+perturb
                a = s@la.inv(t)
                l = la.logm(a)
                jl = super_to_choi(l,d)
                compression = qbasis.conj().T@jl@qbasis
                min_ccp = float(la.eigvalsh((compression+compression.conj().T)/2)[0])
                theoretical = p/(2*d)
                require(min_ccp > theoretical-1e-12, 'v25_interior_verify: min_ccp > theoretical-1e-12')
                require(la.norm(v.conj()@l) < 1e-11, 'v25_interior_verify: la.norm(v.conj()@l) < 1e-11')
                require(la.norm(jl-jl.conj().T) < 1e-11, 'v25_interior_verify: la.norm(jl-jl.conj().T) < 1e-11')
                reconstructed = la.expm(l)@t
                residual = float(la.norm(reconstructed-s))
                require(residual < 1e-10, 'v25_interior_verify: residual < 1e-10')
                min_choi = float(la.eigvalsh(super_to_choi(s,d))[0])
                require(min_choi > 0, 'v25_interior_verify: min_choi > 0')
                out['positive_controls'].append({'d':d,'sample':n,
                      'radius':float(radius),'conditional_choi_min':min_ccp,
                      'proved_lower_bound':theoretical,'channel_choi_min':min_choi,
                      'reconstruction_residual':residual})
        d=2
        v=np.eye(d).reshape(-1,order='F')
        omega=np.outer(v,v)/d
        anti=np.eye(d*d)+1e-4*(np.eye(d*d)-omega)
        l=la.logm(anti)
        qbasis=la.null_space(v[None,:])
        eigs=la.eigvalsh(qbasis.conj().T@super_to_choi(l,d)@qbasis)
        require(eigs[0] < 0, 'v25_interior_verify: eigs[0] < 0')
        out['negative_control']={'removed_slack':'anti-depolarization near identity',
                                 'conditional_choi_min':float(eigs[0]),
                                 'expected':'negative, so no affine ball at identity',
                                 'detected':True}
        out['result']='PASS_WITH_FINITE_SCOPE'
        return out

    return main()


# Source: physical_bridge_check.py; arithmetic and finite sample scope retained.
def suite_physical_bridge_check(profile="quick", mutation="none"):
    """Exact finite controls for the M76 instrument-fibre specialization.
    These are not universal proofs; the accompanying text supplies those.
    """
    import sympy as s
    C=s.Matrix([[1,-s.Rational(1,2),-s.Rational(1,2)],[-s.Rational(1,2),1,-s.Rational(1,2)],[-s.Rational(1,2),-s.Rational(1,2),1]])
    C0=C-s.eye(3)/2
    require(set(C.eigenvals())=={s.Integer(0),s.Rational(3,2)}, 'physical_bridge_check: set(C.eigenvals())=={s.Integer(0),s.Rational(3,2)}')
    require(set(C0.eigenvals())=={-s.Rational(1,2),s.Integer(1)}, 'physical_bridge_check: set(C0.eigenvals())=={-s.Rational(1,2),s.Integer(1)}')
    checks=[]
    # Helstrom example c=3/5: optimal distributions (9/10,1/10) and reversed.
    p=[s.Rational(9,10),s.Rational(1,10)]
    q=p[::-1]
    c=s.Rational(3,5)
    B=sum(s.sqrt(x*y) for x,y in zip(p,q))
    require(B==c, 'physical_bridge_check: B==c')
    Cs=[s.Matrix([[x,c/B*s.sqrt(x*y)],[c/B*s.sqrt(x*y),y]]) for x,y in zip(p,q)]
    require(all(M.det()==0 and M.trace()>0 for M in Cs), 'physical_bridge_check: all(M.det()==0 and M.trace()>0 for M in Cs)')
    require(sum(Cs,s.zeros(2))==s.Matrix([[1,c],[c,1]]), 'physical_bridge_check: sum(Cs,s.zeros(2))==s.Matrix([[1,c],[c,1]])')
    err=(1-s.sqrt(1-c*c))/2
    require(err==s.Rational(1,10), 'physical_bridge_check: err==s.Rational(1,10)')
    return {"status":"PASS","qubit_c":"3/5","qubit_error":str(err),"qubit_B":str(B),"trine_channel_eigenvalues":[str(v) for v in C.eigenvals()],"impossible_common_outcome_eigenvalues":[str(v) for v in C0.eigenvals()],"scope":"exact finite algebraic controls only; general proofs in ZS-M76 v2.5 manuscript"}


# Source: adversarial_new_checks.py; arithmetic and finite sample scope retained.
def suite_adversarial_new_checks(profile="quick", mutation="none"):
    """Narrow exact checks; not a formal verification of the analytic theorems."""
    from fractions import Fraction as F

    rows = []
    def check(name, condition, cls, scope):
        rows.append({'id': name, 'class': cls, 'pass': bool(condition), 'scope': scope})

    # Rational arithmetic after the analytic dimension reductions d>=2, kappa_bar>=1.
    check('N_coefficient', F(1,4)+16+18 <= 35, 'C',
          'd delta + 32 d^2 kbar delta + 18 d^3 kbar delta <= 35 d^3 kbar delta')
    check('frame_factor', F(54,17) < F(16,5), 'C', 'C_alpha/g <= 54/17 < 16/5')
    check('frame_length', F(16,5)*(12+F(19,2)) == F(344,5), 'C', 'frame length coefficient')
    check('sqrt_term', F(24**2,2) < 17**2, 'C', '24/sqrt(2) < 17')
    check('N_term', 72 < F(17,2)**2, 'C', 'sqrt(72) < 17/2')
    check('tau', 17+F(17,2)+F(688,5)+1 <= 165, 'C', 'tau + delta coefficient')
    check('final', F(495**2,2) < 400**2, 'C', '495/sqrt(2) < 400')
    check('alpha_bound', F(1,32) < F(1,25), 'C', '1/(4 sqrt(2)) < 1/5')
    check('C_alpha', 4 <= 9*F(4,5)**3, 'C', '2/(1-alpha)^(3/2)<=3 when alpha<=1/5')
    check('two_E', F(64,72) <= 1, 'C', '8(d-1)sqrt(delta)<=8/sqrt(72)<1')
    check('near_identity', (2+F(1,4))*F(1,8) < F(1,2), 'C', 'r<=2p+p/(4d²)<1/2 for d>=1,p<=1/8')
    check('choi_margin', 1-2*F(1,4) == F(1,2), 'C', 'p/d-2d*[p/(4d²)]=p/(2d)')
    check('interior_radius', F(1,8)*F(1,4)*F(1,50) == F(1,1600), 'C', 'nu/(8*4*50*d³)')
    check('exterior_gap', 1-2*F(1,8) == F(3,4), 'C', 'nu-2*(nu/8)=3nu/4')

    # Live-fire: an invalid monotonicity shortcut is concretely false for amplitude damping.
    e=F(1,10)
    Fprime=-2*e*(1-2*e)
    V=F(0)
    check('nonunital_counterexample', Fprime == -F(4,25) and not (Fprime >= 2*V), 'W',
          'K=|0><1|, rho=diag(9/10,1/10): Fprime=-4/25, V=0')
    check('nonunital_correct_bound', abs(Fprime-2*V) <= 16*e, 'C',
          'the R1 remainder handles this exact counterexample to Fprime>=2V')
    return {'rows':rows, 'failures':sum(not r['pass'] for r in rows),
                      'limit':'Only encoded scalar comparisons and one exact state; no universal proof certification.'}


def expected_rows(name, profile):
    rows = copy.deepcopy(REGISTRY[name]['rows'])
    if name == 'v24_stability_paths' and profile == 'full':
        rows.insert(-1, copy.deepcopy(REGISTRY[name]['full_row']))
    return rows


def unavailable_rows(name, profile, reason):
    return [dict(row, status='UNKNOWN', reason=reason) for row in expected_rows(name, profile)]


def validate_error_packet(name, profile, packet):
    """Execution errors cannot erase rows or manufacture positive evidence."""
    require(packet.get('status') in ('FAIL','UNKNOWN'), 'Error packet cannot PASS')
    require(type(packet.get('error')) is str and bool(packet['error']), 'Missing execution-error diagnosis')
    rows=packet.get('rows');specs=expected_rows(name,profile)
    require(type(rows) is list and len(rows)==len(specs), 'Error packet row coverage mismatch')
    for row,spec in zip(rows,specs):
        require(type(row) is dict and all(row.get(k)==v for k,v in spec.items()), 'Error packet registry mismatch')
        require(row.get('status')=='UNKNOWN' and type(row.get('reason')) is str and bool(row['reason']),
                'Unexecuted row must remain UNKNOWN with a reason')


def validate_output_paths(paths, paper=None):
    protected={Path(__file__).resolve()}
    if paper is not None:
        protected.add(Path(paper).expanduser().resolve())
    targets=[Path(path).expanduser().resolve() for path in paths]
    require(len(targets)==len(set(targets)), 'Output paths alias each other')
    require(not (set(targets)&protected), 'Output must not overwrite the verifier or input manuscript')


def normalize_suite(name, data, profile):
    """Fail closed on empty, duplicate, malformed or nonfinite result payloads."""
    require(type(data) is dict, 'Suite result must be an object')
    finite_tree(data)
    specs = expected_rows(name, profile)
    if name == 'v25_interior_verify':
        require(data.get('result') == 'PASS_WITH_FINITE_SCOPE', 'Interior result marker missing')
        dims = data['exact_constant_dimensions']
        require(type(dims) is list and all(type(d) is int for d in dims), 'Invalid exact dimensions')
        exact_ok = dims == [2, 3, 4, 7, 100, 1000000]
        slack = data['exact_conditional_choi_slack']
        require(type(slack) is list and len(slack) == 3, 'Expected three exact Choi examples')
        choi_ok = [r['d'] for r in slack] == [2, 3, 4] and all(
            r['QJ_Omega_minus_id_Q'] == 'Q/d' and r['normalization_omission_detected'] is True for r in slack)
        positives = data['positive_controls']
        require(type(positives) is list and len(positives) == 45, 'Expected45 interior perturbations')
        require([(r['d'], r['sample']) for r in positives] == [(d,n) for d in (2,3,4) for n in range(15)],
                'Missing or duplicate interior sample')
        positive_ok = all(r['radius'] > 0 and r['proved_lower_bound'] == (1/16)/(2*r['d'])
                          and r['conditional_choi_min'] > r['proved_lower_bound']-1e-12
                          and r['channel_choi_min'] > 0 and 0 <= r['reconstruction_residual'] < 1e-10
                          for r in positives)
        negative = data['negative_control']
        negative_ok = negative['detected'] is True and negative['conditional_choi_min'] < 0
        values = [(exact_ok, dims), (choi_ok, slack), (positive_ok, positives), (negative_ok, negative)]
        return [dict(row, status='PASS' if ok else 'FAIL', data=value) for row,(ok,value) in zip(specs,values)]
    if name == 'physical_bridge_check':
        require(data.get('status') == 'PASS', 'Physical bridge status missing')
        require(all(key in data for key in ('qubit_c','qubit_error','qubit_B',
                'trine_channel_eigenvalues','impossible_common_outcome_eigenvalues')), 'Physical evidence missing')
        qubit_ok = data['qubit_c'] == '3/5' and data['qubit_error'] == '1/10' and data['qubit_B'] == '3/5'
        trine_ok = sorted(data['trine_channel_eigenvalues']) == ['0','3/2'] and sorted(
            data['impossible_common_outcome_eigenvalues']) == ['-1/2','1']
        return [dict(row, status='PASS' if ok else 'FAIL') for row,ok in zip(specs,(qubit_ok,trine_ok))]

    reg = REGISTRY[name]
    raw_rows = data.get(reg['container'])
    require(type(raw_rows) is list and len(raw_rows) == len(specs),
            f'{name}: expected {len(specs)} rows, not an empty/default result')
    require(all(type(row) is dict for row in raw_rows), 'Rows must be objects')
    require([r.get(reg['key']) for r in raw_rows] == [r['source_key'] for r in specs],
            f'{name}: missing, duplicate, reordered or unrecognized row ID')
    normalized = []
    for spec, raw in zip(specs, raw_rows):
        if name in ('bounded_degree', 'adversarial_new_checks'):
            require(type(raw.get('pass')) is bool, f'{spec["id"]}: pass must be an explicit boolean')
            status = 'PASS' if raw['pass'] else 'FAIL'
        else:
            status = raw.get('status')
            require(status in ('PASS','FAIL','UNKNOWN'), f'{spec["id"]}: missing/invalid status')
        cls = raw.get('class', raw.get('cls', raw.get('classification')))
        allowed = (None, spec['class']) if name in ('bounded_degree','derivations') else (spec['class'],)
        if spec['id'] == 'V22-01':
            allowed = ('V','X')  # Disclosed v2.5 correction, retained in v2.5.
        require(cls in allowed, f'{spec["id"]}: unexpected evidence classification {cls}')
        normalized.append(dict(spec, status=status))

    if name not in ('entropy_rounding_checks','adversarial_new_checks'):
        require(data.get('status') == combine_status(r['status'] for r in normalized),
                'Suite status contradicts its rows')
    if name == 'adversarial_new_checks':
        require(type(data.get('failures')) is int and data['failures'] == sum(r['status']=='FAIL' for r in normalized),
                'Failure count missing or inconsistent')
    if name == 'entropy_rounding_checks':
        paths = data['paths']
        require(type(paths) is list and [(r['d'],r['eps']) for r in paths] ==
                [(d,e) for d in range(2,6) for e in (1e-5,1e-4,1e-3)], 'Expected12 entropy paths')
        require(all(r['E'] < 1/3 and r['integral_V'] <= r['V_bound']+1e-12
                    and r['integral_N'] <= r['N_bound']+1e-12 for r in paths), 'Entropy path metric failed')
        require(data['census'] == {'P':0,'C':1,'V':3,'FAIL':0}, 'Entropy census mismatch')
    if name == 'v24_stability_paths':
        paths = data['paths']
        dims = (2,3,4,5,6) if profile == 'full' else (2,3,4)
        require(type(paths) is list and Counter(r['d'] for r in paths) == {d:14 for d in dims},
                'Path coverage does not match requested quick/full profile')
        if profile == 'full':
            adv = raw_rows[-2]['data']['runs']
            require([a['Omega'] for a in adv] == [1.2,0.95], 'Expected two full-profile optimization attempts')
        require(raw_rows[-1]['data']['trials'] == 3000, 'Expected3000 Lemma7.4 samples')
    if name == 'v24_localized_certificate':
        require([raw_rows[0]['data'][k]['branches'] for k in ('K4_w2','K4_mixed','prism_w2')] == [64,64,512],
                'Localized exact branch census mismatch')
    return normalized


def worker(name, profile, mutation):
    """Only stdout is machine JSON; captured source diagnostics remain in it."""
    diagnostics = io.StringIO()
    try:
        missing = []
        with contextlib.redirect_stdout(diagnostics), contextlib.redirect_stderr(diagnostics):
            for dependency in DEPENDENCIES[name]:
                try:
                    importlib.import_module(dependency)
                except Exception as exc:
                    missing.append({'dependency':dependency,'error':f'{type(exc).__name__}: {exc}'})
            if missing:
                packet = {'status':'UNKNOWN','dependency_errors':missing,'error':'Required dependency unavailable',
                          'rows':unavailable_rows(name,profile,'dependency unavailable')}
            else:
                raw = SUITES[name](profile, mutation)
                # JSON conversion exposes unsupported/nonfinite NumPy values now.
                raw = json.loads(canonical_json(raw))
                rows = normalize_suite(name, raw, profile)
                packet = {'status':combine_status(r['status'] for r in rows),'raw':raw,'rows':rows}
    except (CheckFailure, KeyError, TypeError, ValueError) as exc:
        packet = {'status':'FAIL','error':f'{type(exc).__name__}: {exc}',
                  'rows':unavailable_rows(name,profile,'suite aborted; no complete row verdict')}
    except Exception as exc:
        packet = {'status':'UNKNOWN','error':f'{type(exc).__name__}: {exc}',
                  'rows':unavailable_rows(name,profile,'unexpected execution error')}
    packet.update(name=name, profile=profile, mutation=mutation, log=diagnostics.getvalue())
    sys.stdout.write(canonical_json(packet))
    return exit_code(packet['status'])


def run_worker(name, profile, mutation, timeout, optimized=False):
    command = [sys.executable, '-I']
    if optimized or sys.flags.optimize:
        command += ['-O']
    # Preserve -S for a deliberate no-site-packages/dependency control.
    if sys.flags.no_site:
        command += ['-S']
    command += [str(Path(__file__).resolve()), '--_worker',name,'--_profile',profile,'--mutation',mutation]
    env = os.environ.copy()
    for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS',
                'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
        env[key] = '1'
    try:
        process = subprocess.run(command, capture_output=True, text=True, encoding='utf-8',
                                 env=env, timeout=timeout)
        packet = json.loads(process.stdout)
        require(type(packet) is dict and packet.get('name') == name and packet.get('profile') == profile
                and packet.get('mutation') == mutation, 'Worker identity mismatch')
        require(packet.get('status') in ('PASS','FAIL','UNKNOWN'), 'Worker status invalid')
        require(process.returncode == exit_code(packet['status']), 'Worker exit/status mismatch')
        if 'raw' in packet:
            rows = normalize_suite(name,packet['raw'],profile)
            require(rows == packet['rows'] and combine_status(r['status'] for r in rows) == packet['status'],
                    'Worker ledger/raw mismatch')
        else:
            validate_error_packet(name,profile,packet)
        finite_tree(packet)
        packet['exit_code'] = process.returncode
        if process.stderr:
            packet['stderr'] = process.stderr
        return packet
    except subprocess.TimeoutExpired:
        error = f'Per-suite timeout ({timeout:g} seconds)'
        status = 'UNKNOWN'
    except (OSError, json.JSONDecodeError) as exc:
        error = f'{type(exc).__name__}: {exc}'
        status = 'UNKNOWN'
    except (CheckFailure,KeyError,TypeError,ValueError) as exc:
        error = f'{type(exc).__name__}: {exc}'
        status = 'FAIL'
    return {'name':name,'profile':profile,'mutation':mutation,'status':status,
            'exit_code':exit_code(status),'error':error,'rows':unavailable_rows(name,profile,error)}


def self_test(timeout):
    """Live-fire observations, class G only. Does not run/certify all science."""
    rows, observed = [], []
    def guard(identifier, condition, details):
        rows.append({'id':identifier,'class':'G','status':'PASS' if condition else 'FAIL','details':details})
    baseline = run_worker('channel_controls','quick','none',timeout,optimized=True)
    observed.append(baseline)
    guard('G-optimized-baseline', baseline['status']=='PASS', {'observed_status':baseline['status']})
    for mutation,target in MUTATIONS.items():
        changed = run_worker('channel_controls','quick',mutation,timeout,optimized=True)
        observed.append(changed)
        failed = [r['id'] for r in changed['rows'] if r['status']=='FAIL']
        unchanged = False
        if 'raw' in changed and 'raw' in baseline:
            a = [r for r in baseline['raw']['rows'] if r['id']!=target]
            b = [r for r in changed['raw']['rows'] if r['id']!=target]
            unchanged = a == b
        guard('G-mutation-'+mutation, changed['exit_code']==1 and failed==[target] and unchanged,
              {'target':target,'failed_rows':failed,'non_target_evidence_unchanged':unchanged,
               'observed_exit_code':changed['exit_code']})
    # Real malformed-success examples accepted by the previous release runner.
    malformed = [
        ('bounded_degree',{'status':'PASS','cases':[]},'empty-cases'),
        ('physical_bridge_check',{'status':'PASS'},'missing-bridge-evidence'),
        ('v25_interior_verify',{'result':'PASS_WITH_FINITE_SCOPE'},'missing-interior-evidence'),
        ('entropy_rounding_checks',{'checks':[{}]},'missing-entropy-verdict'),
        ('adversarial_new_checks',{'failures':0,'rows':[{}]},'missing-adversarial-verdict'),
    ]
    adversarial = run_worker('adversarial_new_checks','quick','none',timeout,optimized=True)
    observed.append(adversarial)
    guard('G-exact-baseline',adversarial['status']=='PASS',{'observed_status':adversarial['status']})
    if 'raw' in adversarial:
        for label, value in [('string-false','false'),('missing-boolean',None)]:
            bad=copy.deepcopy(adversarial['raw']);bad['rows'][0]['pass']=value
            malformed.append(('adversarial_new_checks',bad,label))
        bad=copy.deepcopy(adversarial['raw']);bad['rows'][1]['id']=bad['rows'][0]['id']
        malformed.append(('adversarial_new_checks',bad,'duplicate-id'))
        bad=copy.deepcopy(adversarial['raw']);bad['metric']=float('inf')
        malformed.append(('adversarial_new_checks',bad,'nonfinite-metric'))
        bad=copy.deepcopy(adversarial['raw']);bad['rows'][0]['pass']=False;bad['failures']=1
        try:
            verdict=combine_status(r['status'] for r in normalize_suite('adversarial_new_checks',bad,'quick'))
        except Exception:
            verdict='ERROR'
        guard('G-exit-zero-failed-row',verdict=='FAIL',{'normalizer_status':verdict})
    for suite,bad,label in malformed:
        try:
            normalize_suite(suite,bad,'quick')
            caught=False; reason='incorrectly accepted'
        except (CheckFailure,KeyError,TypeError,ValueError) as exc:
            caught=True;reason=f'{type(exc).__name__}: {exc}'
        guard('G-schema-'+label,caught,{'suite':suite,'observed_rejection':reason})
    try:
        require(False,'intentional live-fire')
        active=False
    except CheckFailure:
        active=True
    guard('G-require-live',active,{'caught_in_optimized_parent':bool(sys.flags.optimize)})
    sample={'status':'UNKNOWN','error':'deliberate unavailable dependency',
            'rows':unavailable_rows('adversarial_new_checks','quick','dependency unavailable')}
    for label,kind in [('missing-rows',0),('empty-rows',1),('false-pass-rows',2)]:
        bad=copy.deepcopy(sample)
        if kind==0: del bad['rows']
        elif kind==1: bad['rows']=[]
        else:
            for row in bad['rows']: row['status']='PASS'
        try:
            validate_error_packet('adversarial_new_checks','quick',bad)
            rejected=False;reason='incorrectly accepted'
        except CheckFailure as exc:
            rejected=True;reason=str(exc)
        guard('G-error-packet-'+label,rejected,{'observed_rejection':reason})
    for label,paths,paper in [('self-overwrite',[Path(__file__)],None),
                              ('paper-overwrite',[Path('deliberate-manuscript.md')],Path('deliberate-manuscript.md'))]:
        try:
            validate_output_paths(paths,paper)
            rejected=False;reason='incorrectly accepted'
        except CheckFailure as exc:
            rejected=True;reason=str(exc)
        guard('G-output-'+label,rejected,{'observed_rejection':reason})
    return {'status':combine_status(r['status'] for r in rows),'rows':rows,'observed_workers':observed,
            'scope':'Functional mutation/schema controls only; not scientific evidence or a full run.'}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    mode=parser.add_mutually_exclusive_group()
    mode.add_argument('--quick',action='store_true',help='all ten suites, inherited d=2..4 (default)')
    mode.add_argument('--full',action='store_true',help='all ten suites, inherited d=2..6 plus optimizations')
    mode.add_argument('--new-only',action='store_true',help='only four v2.5 suites; explicitly partial coverage')
    mode.add_argument('--self-test',action='store_true',help='live-fire harness, not scientific verification')
    parser.add_argument('--suite',action='append',choices=tuple(DEPENDENCIES),help='select suite(s); partial profile')
    parser.add_argument('--list',action='store_true',help='list exact row registry without dependencies')
    output=parser.add_mutually_exclusive_group()
    output.add_argument('--out','--output',type=Path,help='one consolidated JSON report')
    output.add_argument('--out-dir',type=Path,help='directory for consolidated report and per-suite JSON')
    parser.add_argument('--paper',type=Path,help='optional v2.5 manuscript hash check')
    parser.add_argument('--timeout',type=float,default=1800,help='per-suite seconds; default1800')
    parser.add_argument('--mutation','--mutate',choices=('none',*MUTATIONS),default='none',
                        help='deliberate channel-control defect; must return FAIL')
    parser.add_argument('--_worker',choices=tuple(DEPENDENCIES),help=argparse.SUPPRESS)
    parser.add_argument('--_profile',choices=('quick','full','new-only'),default='quick',help=argparse.SUPPRESS)
    args=parser.parse_args(argv)
    if args._worker:
        return worker(args._worker,args._profile,args.mutation)
    if sys.version_info < (3,10):
        parser.error('Python3.10 or newer is required')
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        parser.error('--timeout must be positive and finite')
    profile='full' if args.full else ('new-only' if args.new_only else 'quick')
    if args.self_test and (args.suite or args.mutation!='none'):
        parser.error('--self-test cannot be combined with --suite/--mutation')
    selected=list(dict.fromkeys(args.suite)) if args.suite else list(NEW_SUITES if args.new_only else DEPENDENCIES)
    if args.new_only and any(n not in NEW_SUITES for n in selected):
        parser.error('--new-only cannot select an inherited suite')
    if args.mutation!='none' and 'channel_controls' not in selected:
        parser.error('--mutation requires channel_controls in the selected suites')
    if args.list:
        for name in selected:
            for row in expected_rows(name,profile):
                print(f'{name}\t{row["id"]}\t{row["class"]}\t{row["claim"]}')
        return 0
    label='self-test' if args.self_test else ('partial-'+profile if args.suite else profile)
    if args.mutation!='none':
        label+='-mutation-'+args.mutation
    destination=args.out or ((args.out_dir or Path.cwd())/f'zs_m76_verify_v2_5_{label}.json')
    planned_outputs=[destination]
    if args.out_dir and not args.self_test:
        planned_outputs += [args.out_dir/f'{name}_{label}.json' for name in selected]
    try:
        validate_output_paths(planned_outputs,args.paper)
    except CheckFailure as exc:
        parser.error(str(exc))
    report={'schema':'zs-m76-finite-verifier/2.5','paper_version':PAPER_VERSION,'code_version':CODE_VERSION,
            'profile':label,'requested_path_profile':profile,'environment':environment(),
            'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'paper_identity':{'expected_sha256':PAPER_SHA256,'status':'NOT_CHECKED'},
            'source_provenance':SOURCE_PROVENANCE,'repo2_references':REPO2_REFERENCES,
            'seeds':{n:SEEDS[n] for n in selected},'limitations':LIMITATIONS,
            'scientific_proof_status':'NOT_CERTIFIED','physical_realization':'OPEN',
            'grade_certification':'NOT_PERFORMED','formal_proof_objects':0}
    paper_status='PASS'
    if args.paper:
        try:
            actual=hashlib.sha256(args.paper.expanduser().read_bytes()).hexdigest()
            paper_status='PASS' if actual==PAPER_SHA256 else 'FAIL'
            report['paper_identity'].update(actual_sha256=actual,status=paper_status)
        except OSError as exc:
            paper_status='UNKNOWN';report['paper_identity'].update(status=paper_status,error=str(exc))
    if args.self_test:
        result=self_test(args.timeout);report['self_test']=result;rows=result['rows']
        report['complete_ten_suite_run']=False
        status=combine_status([result['status'],paper_status])
    else:
        runs=[]
        for name in selected:
            print(f'RUN {name} ({profile})',file=sys.stderr,flush=True)
            run=run_worker(name,profile,args.mutation if name=='channel_controls' else 'none',args.timeout)
            runs.append(run)
            print(f'{run["status"]} {name}',file=sys.stderr,flush=True)
        rows=[row for run in runs for row in run['rows']]
        report['runs']=runs
        report['suite_census']={r['name']:class_counts(r['rows']) for r in runs}
        report['suite_status_counts']=dict(Counter(r['status'] for r in runs))
        report['selected_suites']=selected
        report['omitted_suites']=[n for n in DEPENDENCIES if n not in selected]
        report['complete_ten_suite_run']=len(selected)==10 and all(r['status']=='PASS' for r in runs) and args.mutation=='none'
        report['full_profile_executed']=profile=='full' and report['complete_ten_suite_run']
        report['omitted_full_scope']=[] if profile=='full' and 'v24_stability_paths' in selected else [
            '28 inherited stability paths in d=5,6','two inherited six-segment local optimizations']
        status=combine_status([r['status'] for r in runs]+[paper_status])
    report['status']=status
    report['ledger_census']={'rows':len(rows),'by_class':class_counts(rows),'by_status':dict(Counter(r['status'] for r in rows)),
                              'meaning':'Operational row census; overlapping scopes are not independent proofs.'}
    try:
        serialized=canonical_json(report)
        if args.out_dir and not args.self_test:
            for run in report['runs']:
                atomic_write(args.out_dir/f'{run["name"]}_{label}.json',canonical_json(run))
        atomic_write(destination,serialized)
    except (OSError,TypeError,ValueError) as exc:
        print(f'UNKNOWN: cannot write complete report: {exc}',file=sys.stderr)
        return 2
    print(json.dumps({'status':status,'profile':label,'rows':len(rows),'census':report['ledger_census']['by_class'],
                      'complete_ten_suite_run':report['complete_ten_suite_run'],'output':str(destination)},ensure_ascii=False))
    return exit_code(status)


SUITES = {name: globals()['suite_'+name] for name in DEPENDENCIES}


if __name__ == '__main__':
    raise SystemExit(main())
