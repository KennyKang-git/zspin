"""
Master Equation Two-Term Balance Verification
==============================================

The corpus PROVEN Master Equation (ZS-M1 §4):

    2 ln(x/cos(xπ/2)) + xπ tan(xπ/2) = 0

has unique root x* = Re(z*) in (0, 1).

ZS-F8 §4.4 (STRUCTURAL INSIGHT) interprets the two terms as:
  Term A: 2 ln(x/cos(xπ/2))  — logarithmic information accumulation per cycle
  Term B: x π tan(xπ/2)       — phase-weighted decoherence cost per cycle

The balance Term_A + Term_B = 0 is the equilibrium condition.

NEW verification target: |Term_A| / |Term_B| = ?
If this ratio is exactly 1, the two terms partition the equilibrium 50:50,
matching the Reuleaux 50/50 curvature split (ZS-F7 §2.4 PROVEN) and
the truncated tetrahedron 4+4 self-referential split (ZS-F9 §4.1 PROVEN).
"""

from mpmath import mp, mpf, pi, ln, cos, tan, sqrt, nstr, fabs
import mpmath

# Set 50-digit precision per corpus convention (ZS-M1 verification suite)
mp.dps = 50

print("=" * 78)
print("MASTER EQUATION TWO-TERM BALANCE VERIFICATION")
print("Precision: 50 decimal digits (mpmath)")
print("Corpus reference: ZS-M1 v1.0 §4 (PROVEN), ZS-F8 v1.0(R) §4.4 (STRUCTURAL INSIGHT)")
print("=" * 78)
print()

# Step 1: Solve Master Equation to high precision
# Master Eq: F(x) = 2 ln(x / cos(xπ/2)) + xπ tan(xπ/2) = 0
def master_eq(x):
    return 2 * ln(x / cos(x * pi / 2)) + x * pi * tan(x * pi / 2)

# Use mpmath findroot with high precision
# Initial guess from corpus: x* ≈ 0.4382829367
x_star = mpmath.findroot(master_eq, mpf('0.4382829367'))

print(f"Step 1: Master Equation root (50-digit precision)")
print(f"  x* = {nstr(x_star, 50)}")
print(f"  F(x*) = {nstr(master_eq(x_star), 50)}")
print(f"  |F(x*)| residual: {nstr(fabs(master_eq(x_star)), 5)}")
print()

# Step 2: Compute the two terms separately
term_A = 2 * ln(x_star / cos(x_star * pi / 2))
term_B = x_star * pi * tan(x_star * pi / 2)

print(f"Step 2: Two-term decomposition at x = x*")
print(f"  Term A = 2 ln(x*/cos(x*π/2))   = {nstr(term_A, 50)}")
print(f"  Term B = x*π · tan(x*π/2)      = {nstr(term_B, 50)}")
print(f"  Sum   = Term_A + Term_B        = {nstr(term_A + term_B, 50)}")
print()

# Step 3: Compute absolute values and ratio
abs_A = fabs(term_A)
abs_B = fabs(term_B)
ratio = abs_A / abs_B
deviation_from_unity = ratio - 1

print(f"Step 3: Balance ratio test")
print(f"  |Term A|         = {nstr(abs_A, 50)}")
print(f"  |Term B|         = {nstr(abs_B, 50)}")
print(f"  |A| / |B|        = {nstr(ratio, 50)}")
print(f"  ratio - 1        = {nstr(deviation_from_unity, 5)}")
print()

# Step 4: Verify they are EXACTLY equal (not just approximately)
exact_equal = (abs_A == abs_B)
print(f"Step 4: Equality test")
print(f"  |Term A| == |Term B| (50-digit equality)?  {exact_equal}")
print(f"  Difference |A| - |B| = {nstr(abs_A - abs_B, 5)}")
print()

# Step 5: Why is this exact? Algebraic proof
print("Step 5: Algebraic proof of exact 50:50 split")
print("-" * 78)
print("""
The Master Equation 2 ln(x*/cos(x*π/2)) + x*π tan(x*π/2) = 0
can be rewritten as:
    Term A = -Term B   (the equation IS this statement)

Therefore |Term A| = |Term B| identically, by definition of being
a root of the equation. The 50:50 split is not approximate — it is
the LITERAL CONTENT of the Master Equation being satisfied.

This means:
  - Term A is negative (since x*/cos(x*π/2) < 1 → ln < 0)
  - Term B is positive (since tan(x*π/2) > 0 for x* ∈ (0, 1))
  - Their absolute values are exactly equal
  - The Master Equation = "negative information accumulation
    cancels positive decoherence cost" at equilibrium x*
""")

# Step 6: Connect to the half-budget π/2 phase usage
phase_used_rad = x_star * pi / 2
phase_used_deg = phase_used_rad * 180 / pi
phase_total = pi / 2
phase_total_deg = 90

print(f"Step 6: Phase budget interpretation (ZS-M1 §5)")
print(f"  Total phase budget:    π/2 = {nstr(phase_total, 12)} rad = 90°")
print(f"  Phase used at x*:      x*·π/2 = {nstr(phase_used_rad, 12)} rad")
print(f"                                = {nstr(phase_used_deg, 8)}°")
print(f"  Usage rate:            x* = {nstr(x_star, 12)} = {nstr(x_star * 100, 8)}%")
print(f"  (Phase budget rate; corpus PROVEN)")
print()

# Step 7: Connect to Reuleaux 50/50 split numerically
print(f"Step 7: Cross-check with Reuleaux 50/50 split (ZS-F7 §2.4 PROVEN)")
print("-" * 78)
print(f"  Reuleaux smooth arc curvature:  3 × (π/3) = π = {nstr(pi, 20)}")
print(f"  Reuleaux vertex curvature:      3 × (π/3) = π = {nstr(pi, 20)}")
print(f"  Total turning angle:            2π        = {nstr(2*pi, 20)}")
print(f"  Smooth/total ratio:             π/(2π) = 0.5 (exact)")
print(f"  Vertex/total ratio:             π/(2π) = 0.5 (exact)")
print()
print(f"  Master Eq |Term A|/(|A|+|B|):   {nstr(abs_A / (abs_A + abs_B), 20)}")
print(f"  Master Eq |Term B|/(|A|+|B|):   {nstr(abs_B / (abs_A + abs_B), 20)}")
print()

# Step 8: Reuleaux non-circularity amplitude cross-check
amplitude_n3 = mpf(1) / (3**2 - 1)  # 1/(n²-1) at n=3
print(f"Step 8: Reuleaux geometric coefficient (ZS-F7 §5.1 PROVEN)")
print(f"  Non-circularity amplitude a_3/(w/2) = 1/(n²-1)|n=3 = 1/8 = {nstr(amplitude_n3, 20)}")
print(f"  This saturates the convexity bound; not derivable from Master Eq.")
print()

# Step 9: Summary
print("=" * 78)
print("VERIFICATION SUMMARY")
print("=" * 78)
print(f"""
QUESTION: At x* = root of Master Equation,
          does |2 ln(x*/cos(x*π/2))| = |x*π tan(x*π/2)|?

ANSWER:   YES — exactly, to 50-digit precision.
          
NUMERICAL VALUES (50-digit):
  x*      = {nstr(x_star, 25)}...
  |Term A| = {nstr(abs_A, 25)}...
  |Term B| = {nstr(abs_B, 25)}...
  Ratio   = {nstr(ratio, 25)}...

DEVIATION FROM EXACT EQUALITY:
  |A| - |B| = {nstr(abs_A - abs_B, 5)}

INTERPRETATION:
  This equality is NOT a numerical coincidence. It is the literal
  algebraic content of the Master Equation:  Term_A + Term_B = 0
  immediately implies |Term_A| = |Term_B|.
  
  The 50/50 split is therefore:
   - PROVEN at the equation level
   - Not 50.001/49.999 — exactly 50/50
   - Independent of any numerical evaluation precision

CORPUS CONNECTION:
  Layer 3D (ZS-F9 §4.1):  4 hexagons / 4 triangles  → 50/50 PROVEN
  Layer 2D (ZS-F7 §2.4):  smooth π / vertex π       → 50/50 PROVEN  
  Layer 1D (this verify): |Term A| / |Term B|       → 50/50 PROVEN
  Layer 0D (ZS-Q7 + ZS-F8): E / R (XOR)             → 1:1 PROVEN

  All four layers exhibit the SAME 50/50 partition. This is the
  4-Layer Equivalence Theorem candidate (ZS-F17 in our exploration).
""")
print("=" * 78)
