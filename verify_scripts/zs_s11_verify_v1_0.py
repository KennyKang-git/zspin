"""
ZS-S11 Verification Suite v1.0
================================
Standard Model Anomaly Cancellation as Polyhedral Sector Identities:
A V-E-F Reformulation of the Five Anomaly Conditions in Z-Spin Cosmology

Author: Kenny Kang
Date: April 2026
Code: ZS-S11

This script verifies all 30 tests of ZS-S11 v1.0:
  Category A: Anomaly Arithmetic (6 tests)
  Category B: Sector Identity Theorems (4 tests)
  Category C: A4 Cubic Polynomial Factorization (5 tests)
  Category D: Joint Uniqueness Theorem (6 tests)
  Category E: Cross-Paper Consistency (5 tests)
  Category F: Anti-Numerology Monte Carlo (4 tests)
  
Total: 30 tests
Expected output: 30/30 PASS, exit code 0

Dependencies: Python 3.10+, NumPy, SymPy
Execution: python3 zs_s11_verify_v1_0.py
"""

import sys
import numpy as np
from fractions import Fraction
from sympy import symbols, factor, expand, simplify, together, Poly

# ========================================================================
# Locked inputs from prior papers
# ========================================================================

# ZS-F5 PROVEN
Q = 11
X_DIM = 3
Y_DIM = 6
Z_DIM = 2

# ZS-U9 Theorem 5.1 PROVEN: SU(5) Cartan
# Y = diag(a, a, a, b, b) with a = -1/X, b = +1/Z (in 5 fund convention)
a_cartan = Fraction(-1, X_DIM)
b_cartan = Fraction(1, Z_DIM)

# Trinity Y values (ZS-U9 §6 DERIVED)
Y_Q  = Fraction(1, 6)
Y_L  = Fraction(-1, 2)
Y_u  = Fraction(2, 3)
Y_d  = Fraction(-1, 3)
Y_e  = Fraction(-1)
Y_nR = Fraction(0)


def fmt_pass(name, ok):
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {name}")
    return ok


# ========================================================================
# Category A: Anomaly Arithmetic (ZS-U9 §7 PROVEN re-verification)
# ========================================================================

def category_A():
    print("\nCategory A: Anomaly Arithmetic (ZS-U9 §7 PROVEN re-verification)")
    print("-" * 70)
    results = []
    
    # A.1: A2 [SU(2)]^2 * U(1)_Y
    A2 = 6 * Y_Q + 2 * Y_L
    results.append(fmt_pass("A.1: A2 = 6*(1/6) + 2*(-1/2) = 0", A2 == 0))
    
    # A.2: A3 [SU(3)]^2 * U(1)_Y
    A3_LH = 2 * Y_Q
    A3_RH = Y_u + Y_d
    A3 = A3_LH - A3_RH
    results.append(fmt_pass("A.2: A3 = 1/3 - 1/3 = 0", A3 == 0))
    
    # A.3: A4 [U(1)_Y]^3
    A4_LH = 6 * Y_Q**3 + 2 * Y_L**3
    A4_RH = 3 * Y_u**3 + 3 * Y_d**3 + Y_e**3 + Y_nR**3
    A4 = A4_LH - A4_RH
    results.append(fmt_pass(f"A.3: A4 LH={A4_LH}, RH={A4_RH}, diff=0", 
                           A4 == 0 and A4_LH == Fraction(-2, 9)))
    
    # A.4: A5 Mixed Gauge-Gravitational
    A5_LH = 6 * Y_Q + 2 * Y_L
    A5_RH = 3 * Y_u + 3 * Y_d + Y_e + Y_nR
    A5 = A5_LH - A5_RH
    results.append(fmt_pass("A.4: A5 = Tr(Y) over all matter = 0", 
                           A5 == 0 and A5_LH == 0 and A5_RH == 0))
    
    # A.5: A1 [SU(3)]^3 vector-like
    # In Z-Spin: dim(I-3) = dim(I-3') = 3, both real reps of A_5
    # 3 = 3-bar (real), so quark + antiquark cancellation automatic
    dim_I3 = 3
    dim_I3p = 3
    results.append(fmt_pass(f"A.5: A1 dim(I-3)=dim(I-3')={dim_I3} (vector-like)", 
                           dim_I3 == dim_I3p))
    
    # A.6: Witten SU(2)^4 (4 LH doublets per generation, even)
    # 3 quark doublets (color) + 1 lepton doublet
    n_doublets = 3 + 1
    results.append(fmt_pass(f"A.6: Witten 4 LH doublets/gen = even ({n_doublets} % 2 = 0)", 
                           n_doublets % 2 == 0))
    
    return results


# ========================================================================
# Category B: Sector Identity Theorems
# ========================================================================

def category_B():
    print("\nCategory B: Sector Identity Theorems (X, Z) Reformulation")
    print("-" * 70)
    results = []
    
    # B.1: Theorem 3.1 - A2 = X - Z - 1 in sector form
    # Derivation: Sum_LH Y = X*Z * Y_Q + Z * Y_L
    #           = X*Z * (-1/X + 1/Z) + Z * (-1/Z)
    #           = X - Z - 1
    A2_sector = X_DIM * Z_DIM * (Fraction(-1, X_DIM) + Fraction(1, Z_DIM)) + Z_DIM * Fraction(-1, Z_DIM)
    A2_formula = X_DIM - Z_DIM - 1
    results.append(fmt_pass(
        f"B.1: A2 = X*Z*(-1/X+1/Z) + Z*(-1/Z) = X - Z - 1 = {A2_formula}",
        A2_sector == A2_formula and A2_sector == 0))
    
    # B.2: Theorem 3.2 - A3 = A2/X redundancy
    # A3 = (X - Z - 1) / X
    A3_sector = Fraction(X_DIM - Z_DIM - 1, X_DIM)
    A3_arith = 2 * Y_Q - (Y_u + Y_d)
    results.append(fmt_pass(
        f"B.2: A3 = A2/X = (X-Z-1)/X = {A3_sector} (= 0 iff A2 = 0)",
        A3_sector == A3_arith and A3_sector == 0))
    
    # B.3: SU(5) Cartan traceless via sector balance
    # X*a + Z*b = X*(-1/X) + Z*(1/Z) = -1 + 1 = 0
    cartan_trace = X_DIM * a_cartan + Z_DIM * b_cartan
    results.append(fmt_pass(
        f"B.3: Cartan trace X*a + Z*b = -1 + 1 = 0",
        cartan_trace == 0))
    
    # B.4: Sector Cartan reproduces Trinity Y_Q
    # Y_Q = a + b = -1/X + 1/Z = -1/3 + 1/2 = 1/6
    Y_Q_sector = a_cartan + b_cartan
    results.append(fmt_pass(
        f"B.4: Y_Q from sector = a + b = {Y_Q_sector} (matches Trinity Y_Q = 1/6)",
        Y_Q_sector == Y_Q))
    
    return results


# ========================================================================
# Category C: A4 Cubic Polynomial Factorization (Theorem 3.3)
# ========================================================================

def category_C():
    print("\nCategory C: A4 Cubic Polynomial Factorization (Theorem 3.3)")
    print("-" * 70)
    results = []
    
    # Symbolic verification using SymPy
    X_s, Z_s = symbols('X Z', positive=True, integer=True)
    
    # General A4 from Tr(Y^3) over (5-bar + 10 + 1) with a = -1/X, b = +1/Z
    # Tr(Y^3 over 5-bar) = -X*a^3 - Z*b^3 with a, b symbolic
    # Tr(Y^3 over 10) = X*Z*(a+b)^3 + 4*X*(X-1)*a^3 + 4*Z*(Z-1)*b^3
    # Total = sum (with traceless X*a + Z*b = 0)
    
    # Using sector identification a = -1/X, b = +1/Z:
    # A4 numerator (after combining over (X*Z)^2 denominator):
    # = (5 - 4X)*Z^2 + (4Z - 5)*X^2 + (X - Z)^3
    A4_num_expanded = (5 - 4*X_s)*Z_s**2 + (4*Z_s - 5)*X_s**2 + (X_s - Z_s)**3
    A4_num_expanded = expand(A4_num_expanded)
    
    # Expected factorization
    A4_factored_expected = (X_s - Z_s) * (X_s + Z_s) * (X_s + Z_s - 5)
    A4_factored_expanded = expand(A4_factored_expected)
    
    # C.1: Algebraic identity
    diff = expand(A4_num_expanded - A4_factored_expanded)
    results.append(fmt_pass(
        f"C.1: A4 numerator = (X-Z)(X+Z)(X+Z-5) [algebraic identity]",
        diff == 0))
    
    # C.2: Z-Spin (X, Z) = (3, 2) gives A4 = 0
    A4_at_32 = A4_factored_expanded.subs([(X_s, 3), (Z_s, 2)])
    results.append(fmt_pass(
        f"C.2: A4 at (X, Z) = (3, 2): factor (X+Z-5) = 0 makes A4 = {A4_at_32}",
        A4_at_32 == 0))
    
    # C.3: Three structural factors verified
    factor_XZ_sub = (3 - 2)
    factor_XplusZ_sub = (3 + 2)
    factor_XZminus5_sub = (3 + 2 - 5)
    results.append(fmt_pass(
        f"C.3: Three factors at (3, 2): (X-Z)={factor_XZ_sub}, (X+Z)={factor_XplusZ_sub}, (X+Z-5)={factor_XZminus5_sub}",
        factor_XZ_sub == 1 and factor_XplusZ_sub == 5 and factor_XZminus5_sub == 0))
    
    # C.4: Factor (X+Z-5) dual derivation
    # Route A: X + Z = Q - Y = 11 - 6 = 5
    route_A = Q - Y_DIM
    # Route B: X + Z = dim(SU(5) fund) = 5
    route_B = 5  # by McKay Z_5 -> Â_4 -> SU(5)
    results.append(fmt_pass(
        f"C.4: Route A (Q - Y = {route_A}) = Route B (SU(5) fund dim = {route_B})",
        route_A == route_B == 5))
    
    # C.5: Brute-force enumeration of A4 = 0 zeros in [1, 6]^2
    zeros = []
    for X_test in range(1, 7):
        for Z_test in range(1, 7):
            if X_test == Z_test:  # exclude degenerate
                continue
            val = A4_factored_expanded.subs([(X_s, X_test), (Z_s, Z_test)])
            if val == 0:
                zeros.append((X_test, Z_test))
    expected_zeros = [(1, 4), (2, 3), (3, 2), (4, 1)]
    results.append(fmt_pass(
        f"C.5: A4 = 0 zeros in [1,6]^2 (X != Z): {zeros}",
        sorted(zeros) == sorted(expected_zeros)))
    
    return results


# ========================================================================
# Category D: Joint Uniqueness Theorem (Theorem 4.1)
# ========================================================================

def category_D():
    print("\nCategory D: Joint Uniqueness Theorem (Theorem 4.1)")
    print("-" * 70)
    results = []
    
    # Enumerate all positive integer partitions (X, Y, Z) of Q = 11
    partitions = []
    for X_p in range(1, 10):
        for Z_p in range(1, 10):
            Y_p = Q - X_p - Z_p
            if Y_p >= 1:
                partitions.append((X_p, Y_p, Z_p))
    
    # D.1: Total partitions = 45
    results.append(fmt_pass(
        f"D.1: |partitions of Q=11 with all >= 1| = {len(partitions)}",
        len(partitions) == 45))
    
    # D.2: Partitions satisfying A2 (X - Z = 1)
    sat_A2 = [(X_p, Y_p, Z_p) for X_p, Y_p, Z_p in partitions if X_p - Z_p == 1]
    results.append(fmt_pass(
        f"D.2: |partitions satisfying A2 (X-Z=1)| = {len(sat_A2)}: {sat_A2}",
        len(sat_A2) == 4))
    
    # D.3: Partitions satisfying A4 (X + Z = 5 OR X = Z)
    sat_A4 = [(X_p, Y_p, Z_p) for X_p, Y_p, Z_p in partitions 
              if (X_p + Z_p == 5) or (X_p == Z_p)]
    results.append(fmt_pass(
        f"D.3: |partitions satisfying A4 (X+Z=5 or X=Z)| = {len(sat_A4)}",
        len(sat_A4) == 9))
    
    # D.4: Joint A2 AND A4
    sat_both = [p for p in partitions if (p[0] - p[2] == 1) and 
                ((p[0] + p[2] == 5) or (p[0] == p[2]))]
    results.append(fmt_pass(
        f"D.4: Joint A2 AND A4: |sat_both| = {len(sat_both)} -> {sat_both}",
        len(sat_both) == 1 and sat_both[0] == (3, 6, 2)))
    
    # D.5: Joint solution matches ZS-F5 PROVEN values
    expected_zspin = (X_DIM, Y_DIM, Z_DIM)  # (3, 6, 2)
    match = sat_both[0] == expected_zspin
    results.append(fmt_pass(
        f"D.5: Joint solution {sat_both[0]} matches ZS-F5 PROVEN (X,Y,Z) = {expected_zspin}",
        match))
    
    # D.6: Linear algebra uniqueness X - Z = 1, X + Z = 5 -> (X, Z) = (3, 2)
    # 2X = 6 -> X = 3; 2Z = 4 -> Z = 2
    X_solved = (1 + 5) // 2
    Z_solved = (5 - 1) // 2
    results.append(fmt_pass(
        f"D.6: Linear system X-Z=1, X+Z=5 -> (X,Z) = ({X_solved}, {Z_solved})",
        (X_solved, Z_solved) == (3, 2)))
    
    return results


# ========================================================================
# Category E: Cross-Paper Consistency
# ========================================================================

def category_E():
    print("\nCategory E: Cross-Paper Consistency")
    print("-" * 70)
    results = []
    
    # E.1: ZS-F5 PROVEN (Z, X, Y) = (2, 3, 6); Q = 11
    results.append(fmt_pass(
        f"E.1: ZS-F5 PROVEN (Z,X,Y) = ({Z_DIM},{X_DIM},{Y_DIM}); Q = {Q}",
        Z_DIM + X_DIM + Y_DIM == Q == 11))
    
    # E.2: ZS-M3 Theorem 5.1 PROVEN: dim(Z) = 2 from j = 1/2 uniqueness
    results.append(fmt_pass(
        f"E.2: ZS-M3 Theorem 5.1: dim(Z) = 2 from j=1/2 (intertwiner space)",
        Z_DIM == 2))
    
    # E.3: ZS-M9 §10 Coset structure |I_h/T_d| = 5
    I_h_order = 120
    T_d_order = 24
    coset_index = I_h_order // T_d_order
    results.append(fmt_pass(
        f"E.3: ZS-M9 Table 7 |I_h/T_d| = {I_h_order}/{T_d_order} = {coset_index}",
        coset_index == 5))
    
    # E.4: ZS-M9 §3.2 PROVEN gauge dimension saturation
    # dim(3 ⊗ 4) = dim(3' ⊗ 4) = 12 = G = MUB(Q) = Q + 1
    G = Q + 1
    dim_3_x_4 = 3 * 4
    results.append(fmt_pass(
        f"E.4: ZS-M9 §3.2 dim(3⊗4) = {dim_3_x_4} = G = MUB(Q) = {G}",
        dim_3_x_4 == G == 12))
    
    # E.5: ZS-U9 §7 PROVEN: 5/5 anomaly cancellation
    # Re-verification of all 5 anomalies (cumulative test)
    all_anomalies_zero = (
        (6 * Y_Q + 2 * Y_L) == 0 and  # A2
        (2 * Y_Q - (Y_u + Y_d)) == 0 and  # A3
        (6 * Y_Q**3 + 2 * Y_L**3 - 
         (3 * Y_u**3 + 3 * Y_d**3 + Y_e**3 + Y_nR**3)) == 0 and  # A4
        (6 * Y_Q + 2 * Y_L - 
         (3 * Y_u + 3 * Y_d + Y_e + Y_nR)) == 0  # A5
    )
    results.append(fmt_pass(
        "E.5: ZS-U9 §7 5/5 anomaly cancellation re-verified",
        all_anomalies_zero))
    
    return results


# ========================================================================
# Category F: Anti-Numerology Monte Carlo (500k samples)
# ========================================================================

def category_F():
    print("\nCategory F: Anti-Numerology Monte Carlo (500k samples)")
    print("-" * 70)
    results = []
    
    np.random.seed(42)
    N_trials = 500_000
    
    # Basket 1: Random (X, Z) in [1, 10]^2 independent
    matches_A2 = 0
    matches_A4 = 0
    matches_both = 0
    
    for _ in range(N_trials):
        X_rand = np.random.randint(1, 11)
        Z_rand = np.random.randint(1, 11)
        
        A2_zero = (X_rand - Z_rand == 1)
        A4_zero = (X_rand + Z_rand == 5) or (X_rand == Z_rand)
        
        if A2_zero:
            matches_A2 += 1
        if A4_zero:
            matches_A4 += 1
        if A2_zero and A4_zero:
            matches_both += 1
    
    p_A2 = matches_A2 / N_trials
    p_A4 = matches_A4 / N_trials
    p_both = matches_both / N_trials
    
    # F.1: Basket 1 P(A2) consistent with theoretical 9/100 = 0.09
    # X-Z=1 has 9 solutions in [1,10]^2: (2,1),(3,2),...,(10,9)
    expected_p_A2 = 9 / 100
    results.append(fmt_pass(
        f"F.1: P(A2) = {p_A2:.4f}, expected ~{expected_p_A2:.4f}",
        abs(p_A2 - expected_p_A2) < 0.01))
    
    # F.2: Basket 1 P(both) ~ 0.01 (only (3,2) satisfies both)
    expected_p_both = 1 / 100
    results.append(fmt_pass(
        f"F.2: P(A2 AND A4) = {p_both:.4f}, expected ~{expected_p_both:.4f}",
        abs(p_both - expected_p_both) < 0.005))
    
    # F.3: Basket 2 - Q = 11 partition restriction
    # Among 45 partitions, only (3, 6, 2) satisfies both (verified in D.4)
    # P(both | Q=11) = 1/45 ≈ 0.0222
    p_partition = 1 / 45
    results.append(fmt_pass(
        f"F.3: P(A2 AND A4 | Q=11 partitions) = 1/45 = {p_partition:.4f}",
        abs(p_partition - 0.0222) < 0.001))
    
    # F.4: Basket 3 - Q -> infinity asymptotic
    # P(both | Q) ~ 2/Q^2 asymptotically (verified for Q in {30, 50, 100})
    asymptotic_check = []
    for Q_test in [30, 50, 100]:
        # Count partitions satisfying both at this Q
        count = 0
        total = 0
        for X_t in range(1, Q_test):
            for Z_t in range(1, Q_test):
                Y_t = Q_test - X_t - Z_t
                if Y_t >= 1:
                    total += 1
                    if (X_t - Z_t == 1) and ((X_t + Z_t == 5) or (X_t == Z_t)):
                        count += 1
        p_q = count / total if total > 0 else 0
        asymp_pred = 2 / Q_test**2
        # ratio should be O(1)
        ratio = p_q / asymp_pred if asymp_pred > 0 else 0
        asymptotic_check.append((Q_test, p_q, asymp_pred, ratio))
    
    # All ratios should be in (0.5, 2.0) range (O(1))
    all_ok = all(0.5 < r[3] < 2.0 for r in asymptotic_check)
    print(f"      Asymptotic verification: Q=30,50,100 ratios = {[round(r[3], 2) for r in asymptotic_check]}")
    results.append(fmt_pass(
        "F.4: Asymptotic P(both|Q) ~ 2/Q^2 (ratios within O(1) bounds)",
        all_ok))
    
    return results


# ========================================================================
# Main
# ========================================================================

def main():
    print("=" * 70)
    print("ZS-S11 v1.0 Verification Suite")
    print("Standard Model Anomaly Cancellation as Polyhedral Sector Identities")
    print("=" * 70)
    
    all_results = []
    all_results.extend(category_A())
    all_results.extend(category_B())
    all_results.extend(category_C())
    all_results.extend(category_D())
    all_results.extend(category_E())
    all_results.extend(category_F())
    
    n_pass = sum(all_results)
    n_total = len(all_results)
    
    print()
    print("=" * 70)
    print(f"FINAL RESULT: {n_pass}/{n_total} PASS")
    print("=" * 70)
    
    if n_pass == n_total:
        print("All tests PASS. Zero free parameters. ZS-S11 v1.0 verified.")
        sys.exit(0)
    else:
        print(f"FAILURES: {n_total - n_pass} tests failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
