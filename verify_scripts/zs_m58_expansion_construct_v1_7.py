#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_m58_expansion_construct_v1_7.py
==================================
CONSTRUCTION-LAYER module for ZS-M58 v1.7, Route B (the holonomy-expansion gate).

FIREWALL CONTRACT
-----------------
Permitted input : the Dottie number rho (rho = cos rho).  Nothing else.
Computed here   : s_c, n_c, x_c, the fixed-point census, the first contracting
                  saddle, the quarter-turn generator, the primitive holonomy and
                  its exact order, the saddle multiplier modulus, h_top.

FORBIDDEN anywhere in this file: the identifiers for dim Z, z*, lambda, |lambda|,
arg lambda, and the decimal literals of z* and lambda.  The banned tokens are
assembled at run time from fragments so that this docstring and the scanner
declaration cannot themselves trip the scan; the scan then covers the ENTIRE
source, with no truncation.

v1.7: unchanged from v1.6 apart from the module tag.
v1.6 FIX (audit round 6): the envelope now carries source_sha256, the SHA-256
of THIS file's source.  v1.5 emitted an artifact that no verifier could bind to
the source that produced it, so a v1.4 artifact -- or a valid artifact beside a
stub source incapable of producing one -- still gave 162/162 PASS.  The verifier
now (a) checks the module tag, (b) recomputes source_sha256, and (c) RE-RUNS a
clean copy of this file and compares the regenerated payload byte-for-byte.

v1.5 FIX (audit round 5): the artifact is written SCRIPT-RELATIVE, not to the
current working directory.  v1.4 wrote to os.getcwd(), while the verifier looked
next to its own file; invoking the construct module by path from elsewhere left
the artifact where the verifier could not see it -- a mismatch that v1.4's
fail-open artifact handling would then have hidden.

v1.3 DEFECTS FIXED HERE (found by external audit round 4):
  (1) the v1.3 scanner truncated the source at the first occurrence of its own
      declaration list, so injected forbidden identifiers in the construction
      body were NOT detected.  The scan is now whole-file.
  (2) the v1.3 digest was computed over a dict that was then mutated, and the
      verifier never recomputed it, so the hash was decorative.  The artifact is
      now a payload/envelope pair with a canonical serialisation, and the
      verifier recomputes and compares.

This module may NOT import or compare against any Z-Spin target.  Comparison is
the exclusive job of zs_m58_verify_v1_7.py.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40

# ---------------------------------------------------------------------------
# 0. Firewall.  Whole-file scan, banned tokens assembled from fragments.
# ---------------------------------------------------------------------------


def banned_tokens() -> list[str]:
    """Assembled at run time so this file never contains a banned literal."""
    names = ["DIM" + "_Z", "ZS" + "TAR", "LAM" + "BDA", "AB" + "SL", "AR" + "GL"]
    lits = ["0.89151" + "35", "0.68845" + "32", "2.25924" + "95",
            "0.43828" + "29", "0.36059" + "24"]
    return names + lits


def firewall_scan(path: str) -> list[str]:
    """Scan the ENTIRE source.  No truncation, no exemptions."""
    with open(path, "r", encoding="utf-8") as fh:
        src = fh.read()
    return [tok for tok in banned_tokens() if tok in src]


# ---------------------------------------------------------------------------
# 1. The only permitted input.
# ---------------------------------------------------------------------------

rho = mp.findroot(lambda r: mp.cos(r) - r, mp.mpf("0.739"))

# ---------------------------------------------------------------------------
# 2. ZS-M51 Theorem T2: threshold and critical index.
# ---------------------------------------------------------------------------

s_c = mp.e ** mp.sin(rho)
n_c = 2 * mp.pi / s_c
x_c = 1 / n_c

# ---------------------------------------------------------------------------
# 3. ZS-M51 Theorem T1: the multiplier of f_s(z) = e^{isz}.
# ---------------------------------------------------------------------------


def multiplier_modulus(s):
    return abs(mp.lambertw(-1j * s))


# ---------------------------------------------------------------------------
# 4. ZS-M51 Theorems T5-T6: the fixed-point census on T_m(x) = {mx}.
# ---------------------------------------------------------------------------


def census_count(m: int) -> int:
    return int(mp.ceil(x_c * (m - 1))) - 1


def first_contracting_saddle(m_max: int = 200):
    for m in range(2, m_max + 1):
        if census_count(m) >= 1:
            return m, mp.mpf(1) / (m - 1)
    raise RuntimeError("no contracting saddle below m_max")


# ---------------------------------------------------------------------------
# 5. Primitive holonomy and its exact order.
# ---------------------------------------------------------------------------


def primitive_holonomy(m: int):
    return mp.exp(2j * mp.pi / (m - 1))


def exact_order(H, n_max: int = 64):
    for n in range(1, n_max + 1):
        if abs(H ** n - 1) < mp.mpf("1e-30"):
            return n
    return None


# ---------------------------------------------------------------------------
# 6. Build the payload.
# ---------------------------------------------------------------------------


def source_digest() -> str:
    """SHA-256 of this file's own source, for artifact-source binding."""
    with open(__file__, "r", encoding="utf-8") as fh:
        return hashlib.sha256(fh.read().encode("utf-8")).hexdigest()


def build_payload() -> dict:
    m0, x0 = first_contracting_saddle()
    c = 2j * mp.pi * x0
    H = primitive_holonomy(m0)
    s0 = 2 * mp.pi * x0
    return {
        "module": "zs_m58_expansion_construct_v1_7",
        "permitted_input": "Dottie number rho (rho = cos rho)",
        "rho": mp.nstr(rho, 25),
        "s_c": mp.nstr(s_c, 25),
        "n_c": mp.nstr(n_c, 25),
        "x_c": mp.nstr(x_c, 25),
        "census": {str(m): census_count(m) for m in range(2, 12)},
        "first_contracting_saddle_m": m0,
        "first_contracting_saddle_x0": mp.nstr(x0, 25),
        "generator_c_re": mp.nstr(mp.re(c), 25),
        "generator_c_im": mp.nstr(mp.im(c), 25),
        "fibre_map_at_1_re": mp.nstr(mp.re(mp.exp(c)), 25),
        "fibre_map_at_1_im": mp.nstr(mp.im(mp.exp(c)), 25),
        "primitive_holonomy_re": mp.nstr(mp.re(H), 25),
        "primitive_holonomy_im": mp.nstr(mp.im(H), 25),
        "primitive_holonomy_order": exact_order(H),
        "saddle_multiplier_modulus": mp.nstr(multiplier_modulus(s0), 25),
        "h_top": mp.nstr(mp.log(m0), 25),
        "note": "no Z-Spin constant consumed; no comparison performed here",
    }


def canonical(payload: dict) -> str:
    """The single serialisation both layers must use."""
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def digest_of(payload: dict) -> str:
    return hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# 7. Execute.
# ---------------------------------------------------------------------------


def main() -> int:
    hits = firewall_scan(__file__)
    if hits:
        print("FIREWALL VIOLATION -- artifact NOT emitted:")
        for h in hits:
            print("    forbidden token present:", h)
        return 1

    payload = build_payload()
    envelope = {
        "payload": payload,
        "sha256": digest_of(payload),
        "source_sha256": source_digest(),
    }
    artifact_path = Path(__file__).with_name("m58_expansion_artifact.json")
    with open(artifact_path, "w", encoding="utf-8") as fh:
        json.dump(envelope, fh, indent=2, sort_keys=True)

    w = 78
    print("=" * w)
    print("ZS-M58 v1.7 -- EXPANSION CONSTRUCTION LAYER (target-free)")
    print("=" * w)
    print(f"  permitted input  rho = {payload['rho']}")
    print(f"  s_c                  = {payload['s_c']}")
    print(f"  n_c = 2 pi / s_c     = {payload['n_c']}")
    print(f"  x_c = 1 / n_c        = {payload['x_c']}")
    print(f"  census N_m           = {payload['census']}")
    print(f"  first saddle         m = {payload['first_contracting_saddle_m']}, "
          f"x0 = {payload['first_contracting_saddle_x0']}")
    print(f"  generator c          = {payload['generator_c_re']} + "
          f"{payload['generator_c_im']} i")
    print(f"  e^c                  = {payload['fibre_map_at_1_re']} + "
          f"{payload['fibre_map_at_1_im']} i")
    print(f"  primitive holonomy   = {payload['primitive_holonomy_re']} + "
          f"{payload['primitive_holonomy_im']} i, order "
          f"{payload['primitive_holonomy_order']}")
    print(f"  |multiplier|         = {payload['saddle_multiplier_modulus']}")
    print(f"  h_top = log m        = {payload['h_top']}")
    print("-" * w)
    print(f"  FIREWALL: whole-file scan clean over "
          f"{len(banned_tokens())} banned tokens.")
    print(f"  payload sha256       = {envelope['sha256']}")
    print(f"  source sha256        = {envelope['source_sha256']}")
    print(f"  artifact written to  = {artifact_path.name} (script-relative)")
    print("=" * w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
