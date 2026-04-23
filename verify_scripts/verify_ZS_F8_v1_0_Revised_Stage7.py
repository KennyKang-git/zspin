#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_ZS_F8_v1_0_Revised_Stage7.py
===================================

ZS-F8 v1.0(Revised) — Stage 7 Parallel-Handshake Commutativity Closure
Cross-Reference Verification Suite (V28–V31)

Scope:
    V28 : Curry-form Boolean construction triviality (Appendix D.1).
          F := R_{q'->p} ∘ AND_{q,q'} ∘ E_{p->q} has p-component identically
          zero over all 8 initial states.
    V29 : Two-handshake commutativity at n = 2 (Appendix D.2).
          Case A (no coupling, L_{q1 q2} = 0)  : 8/8 commute.
          Case B (XOR-propagation coupling)    : 4/8 commute, 4/8 non-commute
                                                  with XOR(s_q1, s_q2) = 1 pattern.
    V30 : Pairwise-sync hypothesis across graph topologies (Appendix D.3).
          Hypothesis holds for 9 of 10 enumerated configurations across
          n ∈ {2, 3, 4, 5}; 1 configuration (n = 3 chain, shared middle node)
          fails and is registered as NON-CLAIM (explicitly non-claimed,
          outside Z-Spin's actual mediation structure).
    V31 : Z-mediator commutativity across three 2-bit Z models (Appendix D.4).
          Exhaustive enumeration over Models A, B, C × n ∈ {2, 3, 4} × all
          Boolean initial states = 3 * (32 + 64 + 128) = 672 configurations.
          All 672 commute.

Source: ZS-F8 v1.0(Revised) Stage 7, April 16, 2026, Appendix C (V28–V31),
Appendix D (D.0–D.5).
Reference: Book Z-Spin Cosmology v1.0, Appendix D.1 Stage 7 addendum.

This script is independent of and does not import verify_ZS_F8_v1_0_Revised.py.
It is the Stage 7 addendum per the no-deletion rule and v1.0 freeze
convention: Stage 6 (V1–V27) remains in its own script.

Falsification gates exercised here:
    F-F8.9  : Commutativity at n = 2 under L_{q1 q2} = 0.     [V29 Case A]
    F-F8.10 : Cross-sector coupling detection (L ≠ 0).        [V29 Case B]
    F-F8.11 : Z-mediator robustness across three 2-bit Z models.  [V31]

Dependencies:
    Python >= 3.10
    (Standard library only — itertools, functools, sys.)

Usage:
    python3 verify_ZS_F8_v1_0_Revised_Stage7.py
    # Exit code 0  = 4/4 PASS (= 31/31 total when combined with Stage 6)
    # Exit code 1  = any failure

Author: Kenny Kang
License: same as Z-Spin corpus (see repository root)
"""

from __future__ import annotations

import itertools
import sys
from functools import reduce
from typing import Callable, Dict, List, Tuple

# =============================================================================
# Reporting utilities
# =============================================================================

_results: List[Tuple[str, str, bool, str]] = []


def _record(tag: str, title: str, ok: bool, detail: str = "") -> None:
    _results.append((tag, title, ok, detail))
    mark = "PASS" if ok else "FAIL"
    line = f"[{mark}] {tag:<4} {title}"
    if detail:
        line += f"  | {detail}"
    print(line)


def _check(tag: str, title: str, condition: bool, detail: str = "") -> None:
    _record(tag, title, bool(condition), detail)


# =============================================================================
# Boolean handshake operators and state-update rule (ZS-F8 §4.1, App. D.0)
# =============================================================================

def E_update(s_p: int, s_q: int) -> Tuple[int, int]:
    """
    E_{p->q} state update (ZS-F8 App. D.0):
        e := (1 - s_p) * s_q
        s_p_new := 0,  s_q_new := s_q XOR e
    """
    e = (1 - s_p) * s_q
    return 0, s_q ^ e


def R_update(s_p: int, s_q: int) -> Tuple[int, int]:
    """
    R_{q->p} state update (ZS-F8 App. D.0):
        r := s_p * (1 - s_q)
        s_p_new := s_p XOR r,  s_q_new := 0
    """
    r = s_p * (1 - s_q)
    return s_p ^ r, 0


def H_pair(s_p: int, s_q: int) -> Tuple[int, int]:
    """Direct (non-Z-mediated) handshake H = R ∘ E on a (p, q) pair."""
    sp1, sq1 = E_update(s_p, s_q)
    return R_update(sp1, sq1)


# =============================================================================
# V28 : Curry-form Boolean construction triviality (App. D.1)
#
# F := R_{q'->p} ∘ AND_{q,q'} ∘ E_{p->q}
# where AND_{q,q'} : (s_q, s_q') -> (s_q AND s_q', s_q AND s_q').
# Enumerate over all 8 initial states (s_p, s_q, s_q'); verify p-component
# of F is identically zero.
# =============================================================================

def v28_curry_form_triviality() -> None:
    """V28: F ≡ 0 on s_p over all 8 initial states (ZS-F8 App. D.1)."""
    details = []
    all_zero = True
    for s_p, s_q, s_qp in itertools.product([0, 1], repeat=3):
        # Step 1: E_{p->q} updates (s_p, s_q); s_qp is untouched.
        sp1, sq1 = E_update(s_p, s_q)
        # Step 2: AND_{q,q'} replaces (s_q, s_q') with (s_q AND s_q', s_q AND s_q').
        conj = sq1 & s_qp
        sq2, sqp2 = conj, conj
        # Step 3: R_{q'->p} on (sp1 = 0, sqp2).  (R only sees (s_p, s_qp) pair.)
        sp3, _ = R_update(sp1, sqp2)
        if sp3 != 0:
            all_zero = False
            details.append(f"(s_p,s_q,s_q')=({s_p},{s_q},{s_qp}) -> F_p={sp3}")
    detail = "F_p ≡ 0 on all 8 inputs" if all_zero else "; ".join(details)
    _check("V28", "Curry-form Boolean F ≡ 0 on s_p (App. D.1)", all_zero, detail)


# =============================================================================
# V29 : Two-handshake commutativity at n = 2 (App. D.2)
#
# Joint state (s_p, s_{q_1}, s_{q_2}) ∈ {0, 1}^3.
# H_i := R_{q_i->p} ∘ E_{p->q_i} acting on (s_p, s_{q_i}).
#
# Case A (no coupling):
#   H_1 acts only on (s_p, s_{q_1}), leaves s_{q_2} fixed; vice versa.
#   Expected: 8/8 commute.
#
# Case B (XOR-propagation coupling):
#   When H_i changes s_{q_i} by Δ, propagate s_{q_{3-i}} := s_{q_{3-i}} XOR Δ.
#   Expected: 4/8 commute, with non-commuting states satisfying
#   s_{q_1} XOR s_{q_2} = 1 (the "distinguishable-difference" XOR pattern).
# =============================================================================

def _H_i_no_coupling(
    state: Tuple[int, int, int], i: int
) -> Tuple[int, int, int]:
    """H_i applied to (s_p, s_q1, s_q2) with no cross-partner coupling."""
    s_p, s_q1, s_q2 = state
    if i == 1:
        sp_new, sq1_new = H_pair(s_p, s_q1)
        return sp_new, sq1_new, s_q2
    elif i == 2:
        sp_new, sq2_new = H_pair(s_p, s_q2)
        return sp_new, s_q1, sq2_new
    else:
        raise ValueError(i)


def _H_i_with_coupling(
    state: Tuple[int, int, int], i: int
) -> Tuple[int, int, int]:
    """
    H_i applied with XOR-propagation coupling.
    When H_i changes s_{q_i} by Δ := s_{q_i}_new XOR s_{q_i}_old, the
    partner s_{q_{3-i}} is toggled by Δ.
    """
    s_p, s_q1, s_q2 = state
    if i == 1:
        sp_new, sq1_new = H_pair(s_p, s_q1)
        delta = sq1_new ^ s_q1
        sq2_new = s_q2 ^ delta
        return sp_new, sq1_new, sq2_new
    elif i == 2:
        sp_new, sq2_new = H_pair(s_p, s_q2)
        delta = sq2_new ^ s_q2
        sq1_new = s_q1 ^ delta
        return sp_new, sq1_new, sq2_new
    else:
        raise ValueError(i)


def v29_two_handshake_commutativity() -> None:
    """V29: Two-handshake commutativity (F-F8.9 + F-F8.10)."""
    # Case A: no coupling
    caseA_commute = 0
    caseA_total = 0
    for s_p, s_q1, s_q2 in itertools.product([0, 1], repeat=3):
        st = (s_p, s_q1, s_q2)
        a = _H_i_no_coupling(_H_i_no_coupling(st, 2), 1)  # H_1 ∘ H_2
        b = _H_i_no_coupling(_H_i_no_coupling(st, 1), 2)  # H_2 ∘ H_1
        caseA_total += 1
        if a == b:
            caseA_commute += 1

    # Case B: with XOR-propagation coupling
    caseB_commute = 0
    caseB_total = 0
    xor_pattern_ok = True
    xor_pattern_detail = ""
    for s_p, s_q1, s_q2 in itertools.product([0, 1], repeat=3):
        st = (s_p, s_q1, s_q2)
        a = _H_i_with_coupling(_H_i_with_coupling(st, 2), 1)
        b = _H_i_with_coupling(_H_i_with_coupling(st, 1), 2)
        caseB_total += 1
        commutes = a == b
        if commutes:
            caseB_commute += 1
        # Pattern check: non-commuting states must have s_q1 XOR s_q2 = 1.
        xor_val = s_q1 ^ s_q2
        if (not commutes) and xor_val != 1:
            xor_pattern_ok = False
            xor_pattern_detail = (
                f"non-commuting state (s_p,s_q1,s_q2)=({s_p},{s_q1},{s_q2}) "
                f"has XOR=0 (expected XOR=1)"
            )
        if commutes and xor_val == 1:
            # Some XOR=1 states may still commute by accident; that's fine.
            # The asserted pattern is: non-commuting -> XOR=1 (necessary).
            pass

    ok = (
        caseA_commute == 8
        and caseA_total == 8
        and caseB_commute == 4
        and caseB_total == 8
        and xor_pattern_ok
    )
    detail = (
        f"Case A: {caseA_commute}/{caseA_total} commute; "
        f"Case B: {caseB_commute}/{caseB_total} commute; "
        f"XOR=1 pattern on non-commuters: {'OK' if xor_pattern_ok else xor_pattern_detail}"
    )
    _check("V29", "Two-handshake commutativity (App. D.2)", ok, detail)


# =============================================================================
# V30 : Pairwise-sync hypothesis across graph topologies (App. D.3)
#
# Generic coupled-partner handshakes H_i act on (s_p, s_{q_1}, ..., s_{q_n}).
# A "coupling graph" G is an undirected graph on vertices {q_1, ..., q_n}.
# When H_i changes s_{q_i} by Δ, each neighbour of q_i in G has its bit
# toggled by Δ (XOR-propagation along edges).
#
# Pairwise-sync hypothesis: parallel handshakes commute (all orderings agree)
# iff every directly coupled pair (q_i, q_j) ∈ E(G) already has s_{q_i} = s_{q_j}.
#
# Test across 10 configurations as listed in ZS-F8 App. D.3:
#   (a) n = 2 coupled
#   (b) n = 2 uncoupled (control)
#   (c) n = 3 triangle (all three pairs coupled)
#   (d) n = 3 single coupled pair, third uncoupled
#   (e) n = 3 uncoupled (control)
#   (f) n = 4 complete graph
#   (g) n = 4 two disjoint coupled pairs
#   (h) n = 4 uncoupled (control)
#   (i) n = 5 complete graph
#   (j) n = 3 chain (q1-q2, q2-q3): the documented NON-CLAIM counterexample.
#
# Expected: 9/10 match hypothesis; configuration (j) has at least one
# initial state that satisfies pairwise-sync yet produces order-dependent
# outcomes (counterexample).
# =============================================================================

def _apply_Hi_graph(
    state: Tuple[int, ...], i: int, n: int, edges: List[Tuple[int, int]]
) -> Tuple[int, ...]:
    """
    Apply H_i to state = (s_p, s_q_1, ..., s_q_n) on a coupling graph
    with edges (undirected, 1-indexed partner indices).
    When s_{q_i} changes by Δ, each neighbour q_j toggles by Δ.
    """
    s_p = state[0]
    partners = list(state[1:])  # partners[i-1] = s_{q_i}
    sp_new, sqi_new = H_pair(s_p, partners[i - 1])
    delta = sqi_new ^ partners[i - 1]
    new_partners = list(partners)
    new_partners[i - 1] = sqi_new
    # Toggle neighbours
    for (a, b) in edges:
        if a == i:
            new_partners[b - 1] ^= delta
        elif b == i:
            new_partners[a - 1] ^= delta
    return (sp_new, *new_partners)


def _all_orderings_agree(
    n: int, edges: List[Tuple[int, int]], state: Tuple[int, ...]
) -> bool:
    """Check whether all n! orderings of H_1,...,H_n applied to `state` agree."""
    reference = None
    for perm in itertools.permutations(range(1, n + 1)):
        st = state
        for idx in perm:
            st = _apply_Hi_graph(st, idx, n, edges)
        if reference is None:
            reference = st
        elif st != reference:
            return False
    return True


def _pairwise_sync_holds(
    edges: List[Tuple[int, int]], state: Tuple[int, ...]
) -> bool:
    """True if for every (i, j) ∈ edges: s_{q_i} = s_{q_j}."""
    partners = state[1:]
    for (a, b) in edges:
        if partners[a - 1] != partners[b - 1]:
            return False
    return True


def _config_matches_hypothesis(
    n: int, edges: List[Tuple[int, int]]
) -> Tuple[bool, str]:
    """
    For a given (n, edges), enumerate all 2^(n+1) joint states (s_p, s_q1..s_qn).
    Check the biconditional: all-orderings-agree  <==>  pairwise-sync-holds.
    Returns (matches, detail).
    """
    violations = []
    for bits in itertools.product([0, 1], repeat=n + 1):
        state = bits
        agree = _all_orderings_agree(n, edges, state)
        sync = _pairwise_sync_holds(edges, state)
        if agree != sync:
            violations.append((state, agree, sync))
    if not violations:
        return True, ""
    # Report first few violations
    v0 = violations[0]
    return False, (
        f"{len(violations)} violation(s); first: state={v0[0]}, "
        f"agree={v0[1]}, sync={v0[2]}"
    )


def v30_pairwise_sync_graph_topologies() -> None:
    """V30: 9/10 graph configurations match pairwise-sync hypothesis."""
    configs: List[Tuple[str, int, List[Tuple[int, int]]]] = [
        ("n=2 coupled",                 2, [(1, 2)]),
        ("n=2 uncoupled",               2, []),
        ("n=3 triangle",                3, [(1, 2), (2, 3), (1, 3)]),
        ("n=3 single-pair",             3, [(1, 2)]),
        ("n=3 uncoupled",               3, []),
        ("n=4 complete",                4, [(1, 2), (1, 3), (1, 4),
                                             (2, 3), (2, 4), (3, 4)]),
        ("n=4 two-disjoint-pairs",      4, [(1, 2), (3, 4)]),
        ("n=4 uncoupled",               4, []),
        ("n=5 complete",                5, [(1, 2), (1, 3), (1, 4), (1, 5),
                                             (2, 3), (2, 4), (2, 5),
                                             (3, 4), (3, 5), (4, 5)]),
        ("n=3 chain (NON-CLAIM)",       3, [(1, 2), (2, 3)]),
    ]

    match_count = 0
    breakdown: List[str] = []
    chain_fails = False
    for name, n, edges in configs:
        matches, _ = _config_matches_hypothesis(n, edges)
        if matches:
            match_count += 1
            breakdown.append(f"{name}: MATCH")
        else:
            breakdown.append(f"{name}: MISMATCH")
            if "chain" in name:
                chain_fails = True

    # Expected: 9 configurations match, chain fails.
    ok = (match_count == 9) and chain_fails
    detail = f"{match_count}/10 match; chain n=3 fails as expected: {chain_fails}"
    _check("V30", "Pairwise-sync hypothesis across topologies (App. D.3)",
           ok, detail)


# =============================================================================
# V31 : Z-mediator commutativity across three 2-bit Z models (App. D.4)
#
# Joint state (s_p, s_{Z_0}, s_{Z_1}, s_{q_1}, ..., s_{q_n}).
# A Z-mediated handshake H_i^Z takes the form (per the paper):
#    H_i^Z = R_{q_i->Z} ∘ E_{Z->q_i} ∘ R_{Z->p} ∘ E_{p->Z}
# with the interpretation of "Z" differing across three models:
#
#   Model A (parallel address with σ_x closure):
#     p handshakes with Z[0]; q handshakes with Z[1]; final σ_x swaps Z[0]↔Z[1].
#
#   Model B (sequential through Z[0] with Z[1] as transient memory):
#     both p and q handshake with Z[0]; Z[1] records the intermediate
#     p-Z[0] result as a memory register.
#
#   Model C (J|_Z = σ_x sandwich):
#     p handshakes with Z[0]; σ_x swap; q handshakes with the now-active Z[0]
#     (originally Z[1]); second σ_x restores orientation.
#
# Exhaustive enumeration: 3 models × n ∈ {2, 3, 4} × all 2^(n+3) states = 672.
# The paper states "3 × (32 + 64 + 128) = 672". At n=2 there are 2^(2+3) = 32
# initial states; n=3 gives 64; n=4 gives 128.
#
# All 672 configurations must yield H_1 ∘ H_2 ∘ ... ∘ H_n equal across all
# n! orderings. (The paper's result: "All 672 pass.")
# =============================================================================

def _model_A(state: Tuple[int, ...], i: int, n: int) -> Tuple[int, ...]:
    """
    Model A: p handshakes with Z[0]; q_i handshakes with Z[1];
    final σ_x swaps Z[0] <-> Z[1].

    state = (s_p, s_Z0, s_Z1, s_q1, ..., s_qn)
    """
    s_p = state[0]
    s_Z0 = state[1]
    s_Z1 = state[2]
    partners = list(state[3:])
    s_qi = partners[i - 1]

    # (1) E_{p -> Z[0]}: acts on (s_p, s_Z0); updates both.
    sp1, sZ0_1 = E_update(s_p, s_Z0)
    # (2) R_{Z[0] -> p}: acts on (s_p, s_Z0).
    sp2, sZ0_2 = R_update(sp1, sZ0_1)
    # (3) E_{Z[1] -> q_i}: acts on (s_Z1, s_qi).  Interpret "Z->q" with Z as
    #     'self' role, q as 'other': use E with (s_Z1, s_qi).
    sZ1_1, sqi_1 = E_update(s_Z1, s_qi)
    # (4) R_{q_i -> Z[1]}: acts on (s_qi, s_Z1) with q as self, Z as other.
    sqi_2, sZ1_2 = R_update(sqi_1, sZ1_1)
    # (5) σ_x closure: swap Z[0] <-> Z[1].
    sZ0_new, sZ1_new = sZ1_2, sZ0_2

    new_partners = list(partners)
    new_partners[i - 1] = sqi_2
    return (sp2, sZ0_new, sZ1_new, *new_partners)


def _model_B(state: Tuple[int, ...], i: int, n: int) -> Tuple[int, ...]:
    """
    Model B: both p and q_i handshake with Z[0]; Z[1] records the
    intermediate p-Z[0] result as memory.

    state = (s_p, s_Z0, s_Z1, s_q1, ..., s_qn)
    """
    s_p = state[0]
    s_Z0 = state[1]
    s_Z1 = state[2]
    partners = list(state[3:])
    s_qi = partners[i - 1]

    # (1) E_{p -> Z[0]}.
    sp1, sZ0_1 = E_update(s_p, s_Z0)
    # (2) R_{Z[0] -> p}.
    sp2, sZ0_2 = R_update(sp1, sZ0_1)
    # Record intermediate into Z[1] (memory register write): XOR update so
    # the memory reflects the p-Z[0] transition; this is the "transient"
    # coupling of Model B.
    sZ1_mem = s_Z1 ^ sZ0_2
    # (3) E_{Z[0] -> q_i}: acts on (s_Z0, s_qi) (same Z channel).
    sZ0_3, sqi_1 = E_update(sZ0_2, s_qi)
    # (4) R_{q_i -> Z[0]}.
    sqi_2, sZ0_4 = R_update(sqi_1, sZ0_3)

    new_partners = list(partners)
    new_partners[i - 1] = sqi_2
    return (sp2, sZ0_4, sZ1_mem, *new_partners)


def _model_C(state: Tuple[int, ...], i: int, n: int) -> Tuple[int, ...]:
    """
    Model C: p handshakes with Z[0]; σ_x swap; q_i handshakes with the
    now-active Z[0] (originally Z[1]); second σ_x restores orientation.

    state = (s_p, s_Z0, s_Z1, s_q1, ..., s_qn)
    """
    s_p = state[0]
    s_Z0 = state[1]
    s_Z1 = state[2]
    partners = list(state[3:])
    s_qi = partners[i - 1]

    # (1) E_{p -> Z[0]}.
    sp1, sZ0_1 = E_update(s_p, s_Z0)
    # (2) R_{Z[0] -> p}.
    sp2, sZ0_2 = R_update(sp1, sZ0_1)
    # (3) σ_x swap: Z[0] <-> Z[1].
    sZ0_s1, sZ1_s1 = s_Z1, sZ0_2
    # (4) E_{Z[0] -> q_i} on the now-active Z[0] (which was Z[1]).
    sZ0_3, sqi_1 = E_update(sZ0_s1, s_qi)
    # (5) R_{q_i -> Z[0]}.
    sqi_2, sZ0_4 = R_update(sqi_1, sZ0_3)
    # (6) Second σ_x swap to restore orientation.
    sZ0_final, sZ1_final = sZ1_s1, sZ0_4

    new_partners = list(partners)
    new_partners[i - 1] = sqi_2
    return (sp2, sZ0_final, sZ1_final, *new_partners)


MODELS: Dict[str, Callable[[Tuple[int, ...], int, int], Tuple[int, ...]]] = {
    "A": _model_A,
    "B": _model_B,
    "C": _model_C,
}


def _all_z_orderings_agree(
    model: Callable[[Tuple[int, ...], int, int], Tuple[int, ...]],
    n: int,
    state: Tuple[int, ...],
) -> bool:
    """Check that all n! orderings of Z-mediated handshakes produce the same
    final state."""
    reference = None
    for perm in itertools.permutations(range(1, n + 1)):
        st = state
        for idx in perm:
            st = model(st, idx, n)
        if reference is None:
            reference = st
        elif st != reference:
            return False
    return True


def v31_z_mediator_commutativity() -> None:
    """V31: Z-mediator commutativity across Models A/B/C × n ∈ {2,3,4}."""
    expected_counts_per_model = {2: 32, 3: 64, 4: 128}
    total_per_model = sum(expected_counts_per_model.values())   # 224
    grand_total = 3 * total_per_model                           # 672

    breakdown: List[str] = []
    all_pass = True
    total_checked = 0
    total_commuting = 0

    for model_name, model_fn in MODELS.items():
        for n in (2, 3, 4):
            commute = 0
            checked = 0
            # state = (s_p, s_Z0, s_Z1, s_q1, ..., s_qn), total 2^(n+3)
            for bits in itertools.product([0, 1], repeat=n + 3):
                checked += 1
                if _all_z_orderings_agree(model_fn, n, bits):
                    commute += 1
            total_checked += checked
            total_commuting += commute
            if commute != expected_counts_per_model[n]:
                all_pass = False
            breakdown.append(
                f"Model {model_name} n={n}: {commute}/{checked} commute"
            )

    ok = all_pass and total_checked == grand_total and total_commuting == grand_total
    detail = (
        f"Total {total_commuting}/{total_checked} commute (expected 672/672); "
        + "; ".join(breakdown)
    )
    _check("V31", "Z-mediator commutativity across Models A/B/C (App. D.4)",
           ok, detail)


# =============================================================================
# Driver
# =============================================================================

TESTS: List[Callable[[], None]] = [
    v28_curry_form_triviality,
    v29_two_handshake_commutativity,
    v30_pairwise_sync_graph_topologies,
    v31_z_mediator_commutativity,
]


def main() -> int:
    print("=" * 72)
    print("ZS-F8 v1.0(Revised) Stage 7 — Parallel-Handshake Commutativity")
    print("Cross-Reference Verification Suite V28–V31")
    print("=" * 72)

    for test in TESTS:
        try:
            test()
        except Exception as e:  # pragma: no cover
            _record(test.__name__, "EXCEPTION", False, f"{type(e).__name__}: {e}")

    n_pass = sum(1 for _, _, ok, _ in _results if ok)
    n_total = len(_results)
    print("=" * 72)
    print(f"ZS-F8 v1.0(Revised) Stage 7: {n_pass}/{n_total} PASS")
    print("(Combined with Stage 6 V1–V27 this contributes to 31/31 total.)")
    print("=" * 72)
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    sys.exit(main())
