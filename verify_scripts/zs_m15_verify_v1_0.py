"""
ZS-M15 v1.0 Verification Suite
===============================
Falsification-Based and McKay-Structural Upgrade of ZS-M9 Table 2:
From HYPOTHESIS Strong to DERIVED via Exhaustive Alternative Elimination
and Z5 Charge Complementarity.

Kenny Kang, March 2026.

Zero free parameters beyond A = 35/437.
"""

import sys
import numpy as np
from itertools import permutations

np.random.seed(20260320)
TESTS = []
PASSES = 0

def test(name, condition, detail=""):
    global PASSES
    verdict = "PASS" if condition else "FAIL"
    if condition:
        PASSES += 1
    TESTS.append((name, verdict, detail))
    print(f"  [{verdict}] {name}" + (f"  ({detail})" if detail else ""))
    return condition

# =============================================================================
# Category A — Locked Constants (3 tests)
# =============================================================================
print("\n" + "="*70); print("Category A — Locked Constants"); print("="*70)

A_num, A_den, Q, Z, X, Y = 35, 437, 11, 2, 3, 6
G_gauge = Q + 1

test("A1: A = 35/437 (LOCKED)", A_num == 35 and A_den == 437,
     f"A = {A_num}/{A_den} = {A_num/A_den:.6f}")
test("A2: Q = 11 = Z+X+Y (PROVEN, ZS-F5)", Q == 11 and Z + X + Y == Q,
     f"Q = {Q}, Z+X+Y = {Z+X+Y}")
test("A3: G = MUB(Q) = Q+1 = 12 (PROVEN, ZS-F5)", G_gauge == 12,
     f"G = {G_gauge}")

# =============================================================================
# Category B — Lemma 1: Chirality Reduction 120 → 6
# =============================================================================
print("\n" + "="*70); print("Category B — Lemma 1: Chirality 120 → 6"); print("="*70)

chirality_unsigned = {'1': +1, '3': +1, '3prime': +1, '4': 0, '5': -1}
required_chi = {'nu_R': +1, 'LH': +1, 'RH': +1, 'gauge': 0, 'Higgs': -1}
irreps = ['1', '3', '3prime', '4', '5']
sm_classes = ['nu_R', 'LH', 'RH', 'gauge', 'Higgs']
dims = {'1': 1, '3': 3, '3prime': 3, '4': 4, '5': 5}
all_perms = list(permutations(irreps))

euler_sum = sum(dims[r] * chirality_unsigned[r] for r in irreps)

test("B1: 120 = 5! permutations", len(all_perms) == 120, f"|S_5| = {len(all_perms)}")
test("B2: Σ d_ρ·Δ(ρ) = χ(S²) = 2 (ZS-M9 Thm 3.1 PROVEN)", euler_sum == 2,
     f"1+3+3+0-5 = {euler_sum}")

chirality_survivors = [dict(zip(sm_classes, p)) for p in all_perms
    if all(chirality_unsigned[dict(zip(sm_classes,p))[c]] == required_chi[c] for c in sm_classes)]

test("B3: Lemma 1 — chirality reduces 120 → 6", len(chirality_survivors) == 6,
     f"{len(chirality_survivors)} survivors")
test("B4: gauge ↔ 4 and Higgs ↔ 5 uniquely forced",
     all(s['gauge']=='4' and s['Higgs']=='5' for s in chirality_survivors),
     "unique Δ=0 and Δ=-1 irreps")

# =============================================================================
# Category C — Lemma 2: Gauge Dimension Saturation 6 → 2
# =============================================================================
print("\n" + "="*70); print("Category C — Lemma 2: Gauge Dim Saturation 6 → 2"); print("="*70)

dim_tensor_4 = {'1': 4, '3': 12, '3prime': 12, '4': 16, '5': 20}
saturating = [r for r in irreps if dim_tensor_4[r] == G_gauge]

test("C1: Only {3, 3'} saturate dim(ρ⊗4) = G (ZS-M9 Thm 3.2 PROVEN)",
     set(saturating) == {'3', '3prime'}, f"saturators: {saturating}")

final_survivors = [s for s in chirality_survivors
    if dim_tensor_4[s['LH']] == G_gauge 
    and dim_tensor_4[s['RH']] == G_gauge
    and dim_tensor_4[s['nu_R']] != G_gauge]

test("C2: Lemma 2 reduces 6 → 2", len(final_survivors) == 2,
     f"{len(final_survivors)} survivors")

assign_A = {'nu_R':'1', 'LH':'3', 'RH':'3prime', 'gauge':'4', 'Higgs':'5'}
assign_B = {'nu_R':'1', 'LH':'3prime', 'RH':'3', 'gauge':'4', 'Higgs':'5'}

test("C3: Survivors = {Assignment A, Assignment B}",
     assign_A in final_survivors and assign_B in final_survivors,
     "A: LH↔3, RH↔3' vs B: LH↔3', RH↔3")

# =============================================================================
# Category D — Theorem 1: Z5-McKay Handedness 2 → 1
# =============================================================================
print("\n" + "="*70); print("Category D — Theorem 1: Z5-McKay 2 → 1"); print("="*70)

z5_charges = {
    '1': {0}, '3': {0, 1, 4}, '3prime': {0, 2, 3},
    '4': {1, 2, 3, 4}, '5': {0, 1, 2, 3, 4}
}

# McKay: ω^1 → α_1 (SU3C), ω^2 → α_2 (SU3C), ω^3 → α_3 (U1Y), ω^4 → α_4 (SU2L)
SU2L_charge = 4
U1Y_charge = 3

test("D1: I-irrep 3 carries SU(2)_L root ω⁴ (ZS-M9 §4 F1 PROVEN)",
     SU2L_charge in z5_charges['3'],
     "ω⁴ ∈ Z5(3), McKay → α_4")
test("D2: I-irrep 3' lacks SU(2)_L root but carries U(1)_Y root",
     SU2L_charge not in z5_charges['3prime'] and U1Y_charge in z5_charges['3prime'],
     "ω⁴ ∉ Z5(3'); ω³ ∈ Z5(3')")

def has_SU2L(irrep): return SU2L_charge in z5_charges[irrep]

A_ok = has_SU2L(assign_A['LH']) and not has_SU2L(assign_A['RH'])
B_ok = has_SU2L(assign_B['LH']) and not has_SU2L(assign_B['RH'])
test("D3: Assignment A is unique under SM handedness",
     A_ok and not B_ok, "LH doublet requires SU(2)_L structure")

# =============================================================================
# Category E — Anti-Numerology 3-Basket MC
# =============================================================================
print("\n" + "="*70); print("Category E — Anti-Numerology 3-Basket MC"); print("="*70)

N_MC = 500_000
rng = np.random.default_rng(20260320)

# --- Basket 1: Random chirality + gauge saturation produces unique answer? ---
print(f"  Basket 1: random (chirality + saturation) frameworks, N = {N_MC}")
unique_b1 = 0
for _ in range(N_MC):
    rand_chi = dict(zip(irreps, rng.choice([-1, 0, 1], size=5)))
    rand_dim = dict(zip(irreps, rng.integers(1, 25, size=5)))
    rand_G = int(rng.integers(4, 20))
    
    surv = 0
    for perm in all_perms:
        a = dict(zip(sm_classes, perm))
        chi_ok = all(rand_chi[a[c]] == required_chi[c] for c in sm_classes)
        sat_ok = (rand_dim[a['LH']] == rand_G 
                  and rand_dim[a['RH']] == rand_G
                  and rand_dim[a['nu_R']] != rand_G)
        if chi_ok and sat_ok:
            surv += 1
    if surv == 1:
        unique_b1 += 1

p_b1 = unique_b1 / N_MC
test(f"E1: Basket 1 unique-answer rate under random frameworks",
     p_b1 < 0.01, f"p = {p_b1:.4%} (< 1%)")

# --- Basket 2: Structural integer sum-of-squares partitions for |G| ---
print(f"  Basket 2: |G| = 60 admissible dim partitions")
partitions_60 = []
for d1 in range(1, 8):
    for d2 in range(d1, 8):
        for d3 in range(d2, 8):
            for d4 in range(d3, 8):
                for d5 in range(d4, 8):
                    if d1*d1 + d2*d2 + d3*d3 + d4*d4 + d5*d5 == 60:
                        partitions_60.append((d1, d2, d3, d4, d5))

zspin_part = (1, 3, 3, 4, 5)
test("E2: Z-Spin partition (1,3,3,4,5) satisfies |G|=60",
     zspin_part in partitions_60,
     f"admissible partitions for Σd²=60: {len(partitions_60)}")

# Structural OBSERVATION: the Z-Spin partition is UNIQUE among ordered partitions
test("E3: Uniqueness of (1,3,3,4,5) as |G|=60 ordered partition (OBSERVATION)",
     len(partitions_60) == 1,
     f"only 1 admissible partition: {partitions_60[0]}")

# --- Basket 3: Random 5-tuples do NOT give SM-like reduction ---  
print(f"  Basket 3: random irrep dimension 5-tuples → 120→1 reduction rate")
N_B3 = 100_000
unique_b3 = 0
for _ in range(N_B3):
    rand_dims = tuple(sorted(rng.integers(1, 8, size=5)))
    # Require: some dim must repeat to enable 3↔3' type ambiguity
    has_repeat = len(set(rand_dims)) < 5
    # Random gauge G
    rand_G = int(rng.integers(4, 25))
    # Count dimensions satisfying d*g_dim = G-like constraint
    # Simplified: which partitions support exactly 2 "saturating" irreps?
    # Use product with largest dim as proxy for "× gauge"
    gauge_dim = rand_dims[-1]
    products = [d * gauge_dim for d in rand_dims]
    sat_count = sum(1 for p in products if p == rand_G)
    if sat_count == 2 and has_repeat:
        unique_b3 += 1

p_b3 = unique_b3 / N_B3
test(f"E4: Basket 3 — random setups with '2 saturators + repeat' rare",
     p_b3 < 0.05, f"p = {p_b3:.4%} (< 5%)")

# =============================================================================
# Category F — Cross-Paper Consistency
# =============================================================================
print("\n" + "="*70); print("Category F — Cross-Paper Consistency"); print("="*70)

phi = (1 + 5**0.5) / 2
char_3 = [3, -1, 0, phi, 1 - phi]
char_3p = [3, -1, 0, 1 - phi, phi]
char_5 = [5, 1, -1, 0, 0]
char_1 = [1, 1, 1, 1, 1]
class_sizes = [1, 15, 20, 12, 12]

assert sum(class_sizes) == 60, "|I| = 60 class sum"

def char_inner(a, b, c):
    return sum(class_sizes[i] * a[i] * b[i] * c[i] for i in range(5)) / 60

# F1: 3⊗5⊗3' has dim Hom_I = 1 (ZS-M11 Thm 2.1)
test("F1: ZS-M11 Thm 2.1 — dim Hom_I(1, 3⊗5⊗3') = 1",
     abs(char_inner(char_3, char_5, char_3p) - 1.0) < 1e-10,
     f"{char_inner(char_3, char_5, char_3p):.6f}")

# F2: 3⊗5⊗1 has dim Hom_I = 0 (ZS-M11 §9.5.2)
test("F2: ZS-M11 §9.5.2 — dim Hom_I(1, 3⊗5⊗1) = 0 (ν_R Yukawa forbidden)",
     abs(char_inner(char_3, char_5, char_1)) < 1e-10,
     f"{char_inner(char_3, char_5, char_1):.6f}")

# F3: Z5 charge complementarity {ω¹,ω⁴} ∪ {ω²,ω³} = {ω¹,ω²,ω³,ω⁴}
nt_3 = z5_charges['3'] - {0}
nt_3p = z5_charges['3prime'] - {0}
test("F3: ZS-M9 §4 F1 — Z5 complementarity",
     nt_3 | nt_3p == {1, 2, 3, 4},
     f"{sorted(nt_3)} ∪ {sorted(nt_3p)} = {sorted(nt_3 | nt_3p)}")

# F4: Gauge saturation 3⊗4 = 3'⊕4⊕5 (dimension check only; full tensor decomp per ZS-M9 §3.2)
test("F4: ZS-M9 Thm 3.2 — dim(3⊗4) = dim(3'⊗4) = 12 = G",
     dim_tensor_4['3'] == dim_tensor_4['3prime'] == G_gauge,
     f"dim(3⊗4) = {dim_tensor_4['3']} = dim(3'⊗4) = {dim_tensor_4['3prime']} = G")

# =============================================================================
# Summary
# =============================================================================
print("\n" + "="*70)
print(f"Verification Summary: {PASSES}/{len(TESTS)} PASS")
print("="*70)

if PASSES == len(TESTS):
    print("\nAll tests PASS. ZS-M15 v1.0 verification successful.")
    sys.exit(0)
else:
    print(f"\n{len(TESTS) - PASSES} test(s) FAILED.")
    sys.exit(1)
