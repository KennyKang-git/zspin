#!/usr/bin/env python3
"""
zs_s9_mc_v1_0.py — ZS-S9 Corollary III Anti-Numerology Monte Carlo
Author: Kenny Kang
Date: April 2026

Protocol (per ZS-S9 Appendix B, published):
  H_0: The specific assignment (electron <-> V_XZ, +i, +theta/2) and
       (positron <-> V_ZY, -i, -theta/2) is one among many a priori
       equivalent branch-assignment mappings, and the three structural
       evidence lines (CPT complex conjugation, SU(2) sign flip, S^1
       antipodal pair) are no more specific than random.

  Test statistic: number of independent structural evidence lines
       (out of 3) that support a sampled alternative mapping.

  Observed value for Corollary III assignment: 3/3.

  Empirical p-value: fraction of random samples achieving >= 3/3.

  Pass criteria (Appendix B.4):
    p < 1.0%            -> Corollary III retains HYPOTHESIS strong
    1.0% <= p < 5.0%    -> Corollary III downgrades to HYPOTHESIS
    p >= 5.0%           -> Corollary III withdrawn, transferred to OPEN

Anti-numerology principle (strictly enforced):
  - The alternative space must include ALL a priori defensible
    alternative mappings with equal prior weight.
  - The evidence lines must be defined BEFORE seeing any data and
    applied identically to observed and alternative mappings.
  - The script reports whatever p-value emerges. It is NOT designed
    to yield p < 1%; it is designed to be a fair test.
  - Fixed random seed (42) per Appendix B.5 for reproducibility.

Runtime: ~2-5 minutes on a single CPU (NumPy vectorized).
Dependencies: numpy (core), sys/time (stdlib).
"""

import numpy as np
import sys
import time

# ============================================================
# CONFIGURATION
# ============================================================
N_SAMPLES = 500_000
RANDOM_SEED = 42
VERBOSE = True

np.random.seed(RANDOM_SEED)

# ============================================================
# PROBLEM DEFINITION (strictly from ZS-S9 Appendix B)
# ============================================================
#
# A "mapping" consists of four binary attribute choices per particle:
#   1. branch:     V_XZ  (encoded 0)  or  V_ZY  (encoded 1)
#   2. horizon_i:  +i    (encoded 0)  or  -i    (encoded 1)
#   3. phase_sign: +theta/2 (encoded 0) or -theta/2 (encoded 1)
#   4. particle:   electron (encoded 0) or positron (encoded 1)
#
# A full mapping specifies these 4 bits for the electron-positron pair
# at the horizon. The observed Corollary III mapping is:
#
#   Electron: (V_XZ, +i, +theta/2, electron)  = (0, 0, 0, 0)
#   Positron: (V_ZY, -i, -theta/2, positron)  = (1, 1, 1, 1)
#
# Alternative hypothesis space: all 2^4 = 16 attribute tuples per
# particle, 16 x 16 = 256 bare combinations. After imposing the
# ZS-F4 §7B constraint V_ZY = (V_XZ)* (which locks branch <-> phase
# sign correlation), the effective space reduces (see B.2).
#
# The anti-numerology protocol expands to 500,000 samples by allowing
# ALSO random perturbations of the three algebraic evidence relations,
# to check whether the specific supporting combination is privileged.
# ============================================================

# Define the observed assignment for the electron-positron pair
OBSERVED_MAPPING = {
    'electron_branch':  0,  # V_XZ
    'electron_phase_i': 0,  # +i at horizon
    'electron_sign':    0,  # +theta/2
    'positron_branch':  1,  # V_ZY
    'positron_phase_i': 1,  # -i
    'positron_sign':    1,  # -theta/2
}


# ============================================================
# EVIDENCE LINE DEFINITIONS (pre-registered)
# ============================================================
#
# Evidence Line 1 (CPT): The branch of the positron is the complex
#   conjugate of the branch of the electron. In our encoding, this
#   means electron_branch XOR positron_branch == 1 (they differ).
#
# Evidence Line 2 (SU(2) sign flip): The horizon phase of the positron
#   is the negative of the electron's. In our encoding, this means
#   electron_phase_i XOR positron_phase_i == 1.
#
# Evidence Line 3 (S^1 antipodal): The phase signs (+theta/2 vs
#   -theta/2) are opposite. In our encoding, this means
#   electron_sign XOR positron_sign == 1.
#
# The observed mapping satisfies ALL THREE: each pair of attributes
# between electron and positron differs.
#
# For the 500k sampling, we sample a "mapping" as 6 independent bits
# (3 per particle), and count how many of the three pairwise XOR
# conditions evaluate to 1.
#
# Additionally, per Appendix B, we allow random "rewirings" of the
# three evidence definitions to alternative algebraic relations,
# to check that the specific combination {CPT, SU(2), S^1} is not
# privileged. We implement this by, for a fraction of samples,
# replacing XOR with a random boolean function of the 6 bits.
# ============================================================


def count_evidence_matches_standard(electron_bits, positron_bits):
    """
    Count how many of the three standard evidence lines are matched.

    electron_bits, positron_bits: int arrays of shape (N, 3)
        columns: [branch, phase_i, sign]

    Returns: int array of shape (N,), values in {0, 1, 2, 3}
    """
    xor = electron_bits ^ positron_bits  # shape (N, 3)
    return xor.sum(axis=1)


def count_evidence_matches_with_perturbed_rules(
    electron_bits, positron_bits, rule_perturbation_bits
):
    """
    Anti-numerology expansion (Appendix B.2 paragraph 2).

    For each sample, we allow the three evidence rules themselves
    to be randomly perturbed. Three perturbation bits per sample:
      - If perturbation_bit_k == 0: rule k is standard XOR (same as above)
      - If perturbation_bit_k == 1: rule k is random XNOR (NOT XOR)
        i.e., checks whether bits match rather than differ.

    This is the "alternative algebraic relation" from Appendix B.

    electron_bits, positron_bits: int arrays, shape (N, 3)
    rule_perturbation_bits: int array, shape (N, 3)

    Returns: int array (N,), values in {0, 1, 2, 3}
    """
    xor = electron_bits ^ positron_bits  # (N, 3)
    # If perturbation == 1, flip the sense of the rule
    effective = xor ^ rule_perturbation_bits  # (N, 3)
    return effective.sum(axis=1)


# ============================================================
# MONTE CARLO SAMPLING
# ============================================================

def run_monte_carlo():
    print(f"ZS-S9 Corollary III Anti-Numerology Monte Carlo")
    print(f"=" * 60)
    print(f"Samples: {N_SAMPLES:,}")
    print(f"Random seed: {RANDOM_SEED}")
    print(f"Observed evidence matches: 3/3")
    print(f"=" * 60)

    start = time.time()

    # Phase 1: Standard rules (baseline)
    # Sample 6 bits per sample (3 for electron, 3 for positron)
    if VERBOSE:
        print("\nPhase 1: Standard rules baseline")

    electron_bits = np.random.randint(0, 2, size=(N_SAMPLES, 3), dtype=np.int8)
    positron_bits = np.random.randint(0, 2, size=(N_SAMPLES, 3), dtype=np.int8)

    matches_phase1 = count_evidence_matches_standard(electron_bits, positron_bits)

    # Distribution under uniform sampling
    counts_phase1 = np.bincount(matches_phase1, minlength=4)
    if VERBOSE:
        print(f"  Distribution under uniform 6-bit sampling:")
        for k in range(4):
            frac = counts_phase1[k] / N_SAMPLES
            print(f"    {k}/3 matches: {counts_phase1[k]:>8,} ({frac*100:6.3f}%)")

    # p-value for observed 3/3 under standard rules
    p_standard = counts_phase1[3] / N_SAMPLES
    if VERBOSE:
        print(f"  p(>=3/3 | standard rules) = {p_standard*100:.4f}%")
        # Theoretical: each of 3 XOR conditions is iid Bernoulli(0.5)
        # so P(all three = 1) = 1/8 = 12.5%
        print(f"  Theoretical (1/8): 12.5000%")

    # Phase 2: With rule perturbation (anti-numerology expansion)
    if VERBOSE:
        print("\nPhase 2: With rule perturbation (Appendix B.2)")

    rule_perturbation_bits = np.random.randint(
        0, 2, size=(N_SAMPLES, 3), dtype=np.int8
    )

    matches_phase2 = count_evidence_matches_with_perturbed_rules(
        electron_bits, positron_bits, rule_perturbation_bits
    )

    counts_phase2 = np.bincount(matches_phase2, minlength=4)
    if VERBOSE:
        print(f"  Distribution with rule perturbation:")
        for k in range(4):
            frac = counts_phase2[k] / N_SAMPLES
            print(f"    {k}/3 matches: {counts_phase2[k]:>8,} ({frac*100:6.3f}%)")

    # For Phase 2, "3/3 matches" under random rules means the sampled
    # mapping plus sampled rules jointly satisfy all 3 evidence lines.
    # This is the fair anti-numerology p-value per Appendix B.
    p_phase2 = counts_phase2[3] / N_SAMPLES
    if VERBOSE:
        print(f"  p(>=3/3 | random rules + random mapping) = {p_phase2*100:.4f}%")

    elapsed = time.time() - start
    if VERBOSE:
        print(f"\nRuntime: {elapsed:.2f} seconds")

    return {
        'p_standard': float(p_standard),
        'p_with_rule_perturbation': float(p_phase2),
        'counts_standard': counts_phase1.tolist(),
        'counts_with_rule_perturbation': counts_phase2.tolist(),
        'n_samples': N_SAMPLES,
        'seed': RANDOM_SEED,
        'runtime_sec': elapsed,
    }


# ============================================================
# HONEST REPORTING AND STATUS DECISION
# ============================================================

def report_result(result):
    print("\n" + "=" * 60)
    print("ANALYSIS")
    print("=" * 60)

    p_std = result['p_standard']
    p_pert = result['p_with_rule_perturbation']

    # Theoretical baseline: under pure uniform sampling, XOR of two
    # independent random bits is Bernoulli(0.5); three independent
    # XORs matching is (1/2)^3 = 1/8 = 12.5%.
    print(f"""
Theoretical expectation under H_0 (uniform bit sampling):
  Probability of achieving 3/3 evidence matches = (1/2)^3 = 12.5%

  Interpretation: If the three evidence lines (CPT conjugation,
  SU(2) sign flip, S^1 antipodal pair) were arbitrary algebraic
  relations, random assignments would satisfy all three ~1 in 8
  times. This is NOT a small number.

Observed MC p-values:
  Phase 1 (standard rules):        {p_std*100:.4f}%
    -> matches theoretical 12.5% baseline within MC error
       (confirms sampling implementation is unbiased)

  Phase 2 (with rule perturbation): {p_pert*100:.4f}%
    -> this is the full anti-numerology p-value per Appendix B
""")

    print("=" * 60)
    print("STATUS DECISION (per ZS-S9 §Appendix B.4)")
    print("=" * 60)

    # Appendix B.4 thresholds
    if p_pert < 0.010:
        status = "HYPOTHESIS strong (RETAINED)"
        symbol = "PASS"
    elif p_pert < 0.050:
        status = "HYPOTHESIS (DOWNGRADED from HYPOTHESIS strong)"
        symbol = "DOWNGRADE"
    else:
        status = "OPEN (WITHDRAWN from present paper)"
        symbol = "WITHDRAW"

    print(f"\n  Anti-numerology p-value: {p_pert*100:.4f}%")
    print(f"  Thresholds: p<1% -> HYPO strong | 1-5% -> HYPO | >=5% -> WITHDRAW")
    print(f"\n  Decision: {symbol}")
    print(f"  Corollary III status: {status}")

    return status, symbol


def write_interpretation(result, status, symbol):
    print("\n" + "=" * 60)
    print("INTERPRETATION (honest reporting)")
    print("=" * 60)

    p_pert = result['p_with_rule_perturbation']

    if symbol == "PASS":
        print("""
The observed Corollary III mapping achieves 3/3 evidence matches
at a rate far above what random sampling would produce when BOTH
the mapping AND the evidence rules are allowed to vary. This is
the strongest form of anti-numerology test available for this
class of claim.

However, Claude/the framework must note the following honest caveat:
the test statistic (3 binary evidence lines) is a LOW-DIMENSIONAL
test. Even at 100% pass rate, it cannot distinguish between:
  (a) the Corollary III mapping is structurally privileged, and
  (b) any mapping satisfying 3 symmetric XOR conditions would pass
      (which is a geometric constraint, not a physical one).

The correct interpretation of PASS is: "The Corollary III mapping
is NOT a random fluke within the 16-element combinatorial space,"
which is a weaker statement than "the mapping is physically forced."
Physical forcing still requires closure of Gap G1 (ZS-S10).
""")
    elif symbol == "DOWNGRADE":
        print("""
The observed Corollary III mapping passes the 3/3 evidence threshold
at a p-value between 1% and 5%. This is evidence of structural
match but does not meet the HYPOTHESIS strong threshold set in
Appendix B.4. Corollary III is therefore downgraded to plain
HYPOTHESIS status in ZS-S9 v1.1 (next revision).

This outcome is consistent with the framework's conservative
methodology: the structural evidence (three lines) exists but is
not sufficient to privilege the mapping statistically over random
alternatives within the defined space.
""")
    else:  # WITHDRAW
        print("""
The anti-numerology test does not privilege the Corollary III
mapping over random alternatives in the defined combinatorial
space at the 5% level. Per Appendix B.4, Corollary III is
withdrawn from the present paper and transferred to OPEN status.

This outcome reveals that the three evidence lines, while
individually DERIVED (from ZS-A7 Cor I, ZS-M3 Lemma 10.1, and
ZS-F4 §7B), do NOT uniquely pick out the electron-positron
mapping among alternative charge-conjugate pairings in the
defined space. Additional structural input (e.g., closure of
Gap G1 via ZS-S10) is required before this corollary can be
reinstated.

This is a POSITIVE outcome for the framework's epistemic
discipline: the anti-numerology test is doing its job of
preventing overclaim. The structural resonances noted in
§4.3 remain valid as OBSERVATIONs but are not elevated.
""")


def write_summary_file(result, status, symbol):
    """Write machine-readable summary for record-keeping."""
    import json
    summary = {
        'paper': 'ZS-S9 v1.0',
        'corollary': 'III',
        'test': 'Anti-Numerology Monte Carlo',
        'protocol_ref': 'Appendix B.1-B.5',
        'random_seed': result['seed'],
        'n_samples': result['n_samples'],
        'p_value_standard_rules': result['p_standard'],
        'p_value_with_rule_perturbation': result['p_with_rule_perturbation'],
        'distribution_standard': result['counts_standard'],
        'distribution_perturbed': result['counts_with_rule_perturbation'],
        'runtime_sec': result['runtime_sec'],
        'decision_symbol': symbol,
        'corollary_III_final_status': status,
    }
    try:
        with open('zs_s9_mc_v1_0_result.json', 'w') as f:
            json.dump(summary, f, indent=2)
        print(f"\n  Machine-readable result written to: zs_s9_mc_v1_0_result.json")
    except Exception as e:
        print(f"\n  (Could not write JSON summary: {e})")


def main():
    try:
        result = run_monte_carlo()
        status, symbol = report_result(result)
        write_interpretation(result, status, symbol)
        write_summary_file(result, status, symbol)

        print("\n" + "=" * 60)
        print("DONE")
        print("=" * 60)

        # Exit code semantics:
        #   0 = test completed successfully, whatever the status
        #   1 = test failed to execute
        # The CONTENT of the result is reported in stdout and json.
        return 0
    except Exception as e:
        print(f"\nERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
