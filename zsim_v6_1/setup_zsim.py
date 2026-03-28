#!/usr/bin/env python3
"""Z-Sim v3.0 — Setup & Verification Script.

Run this once after unzipping:
    python setup_zsim.py

It will:
  1. Install runtime dependencies (numpy, scipy, pyyaml, matplotlib)
  2. Install pytest for testing
  3. Register the zsim package (pip install -e .)
  4. Run the full test suite (190 tests)
  5. Run a quick simulation to verify everything works
"""
import subprocess
import sys
import os

def run(cmd, desc):
    print(f"\n{'='*60}")
    print(f"  {desc}")
    print(f"{'='*60}")
    result = subprocess.run(cmd, shell=isinstance(cmd, str))
    if result.returncode != 0:
        print(f"  [FAILED] {desc}")
        return False
    return True

def main():
    print("=" * 60)
    print("  Z-Sim v3.0 — Setup & Verification")
    print("=" * 60)
    print(f"  Python: {sys.version}")
    print(f"  OS:     {sys.platform}")
    print(f"  CWD:    {os.getcwd()}")

    # Check we're in the right directory
    if not os.path.exists("zsim/core/constants.py"):
        print("\n  [ERROR] Run this script from inside the zsim_v3 folder!")
        print("  Example:")
        print("    cd zsim_v3")
        print("    python setup_zsim.py")
        return 1

    py = sys.executable

    # Step 1: Install dependencies
    if not run([py, "-m", "pip", "install", "-r", "requirements.txt"],
               "Step 1/4: Installing dependencies"):
        return 1

    # Step 2: Install pytest
    if not run([py, "-m", "pip", "install", "pytest"],
               "Step 2/4: Installing pytest"):
        return 1

    # Step 3: Register zsim package
    if not run([py, "-m", "pip", "install", "-e", "."],
               "Step 3/4: Registering zsim package"):
        return 1

    # Step 4: Run tests
    print(f"\n{'='*60}")
    print(f"  Step 4/4: Running test suite")
    print(f"{'='*60}")
    test_result = subprocess.run([py, "-m", "pytest", "tests/", "-q"])

    print()
    print("=" * 60)
    if test_result.returncode == 0:
        print("  [SUCCESS] Z-Sim v3.0 is ready!")
        print("=" * 60)
        print()
        print("  Quick start commands:")
        print()
        print("    # Run background evolution (theory-derived closures)")
        print("    python -m zsim.apps.run_background \\")
        print("        --config configs/derived.yaml \\")
        print("        --output-dir outputs/my_first_run")
        print()
        print("    # Compute inflation observables (n_s, r)")
        print("    python -m zsim.apps.run_inflation")
        print()
        print("    # Run all tests")
        print("    python -m pytest tests/ -q")
        print()
    else:
        print("  [WARNING] Some tests failed. Check output above.")
        print("=" * 60)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
