# Z-Spin Cosmology — Verification Scripts

Independent verification suites for all 46 papers in the Z-Spin Cosmology framework.  
Every physical prediction derives from a single geometric constant **A = 35/437** and the 11-dimensional register **Q = 11**, with **zero free parameters**.

📄 **Framework:** [Z-Spin Cosmology](https://github.com/KennyKang-git/zspin)  
📧 **Contact:** Kenny Kang (lead researcher)

---

## Quick Start

### 1. Prerequisites

- **Python 3.9+** (tested on 3.10, 3.11, 3.12)
- **pip** (Python package manager)

### 2. Clone & Setup

```bash
# Clone the repository
git clone https://github.com/KennyKang-git/zspin.git
cd zspin/verify_scripts

# Create a virtual environment (recommended)
python -m venv zspin_env

# Activate the virtual environment
# macOS / Linux:
source zspin_env/bin/activate
# Windows (Command Prompt):
zspin_env\Scripts\activate
# Windows (PowerShell):
zspin_env\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 3. Run

```bash
# Run ALL 46 verification suites
python run_all.py

# Run a single paper
python zs_f2_verify_v1_0.py

# Run by theme
python run_all.py --theme F    # Foundations (ZS-F0 ~ F5)
python run_all.py --theme M    # Mathematical Spine (ZS-M1 ~ M7)
python run_all.py --theme S    # Standard Model (ZS-S1 ~ S6)
python run_all.py --theme U    # Early Universe (ZS-U1 ~ U8)
python run_all.py --theme A    # Astrophysics (ZS-A1 ~ A6)
python run_all.py --theme Q    # Quantum Mechanics (ZS-Q1 ~ Q7)
python run_all.py --theme QX   # Quantum Computing (ZS-QC, QH, QS)
python run_all.py --theme T    # Translational (ZS-T1 ~ T3)

# Run a specific paper
python run_all.py --paper f2

# Verbose mode (show full output)
python run_all.py --verbose
```

---

## Paper Map

| Theme | Code | Papers | Tests |
|-------|------|--------|-------|
| **Foundations** | F | ZS-F0, F1, F2, F3, F4, F5 | Core axioms, A = 35/437 derivation, holonomy, Q = 11 |
| **Mathematical Spine** | M | ZS-M1 ~ M7 | i-tetration, sector independence, spectral theory |
| **Standard Model** | S | ZS-S1 ~ S6 | Gauge couplings, fermion masses, EWSB, CKM/PMNS |
| **Early Universe** | U | ZS-U1 ~ U8 | Inflation, baryogenesis, dark matter, CMB observables |
| **Astrophysics** | A | ZS-A1 ~ A6 | H₀ tension, S₈, neutron stars, gravitational waves |
| **Quantum Mechanics** | Q | ZS-Q1 ~ Q7 | Measurement, entanglement, decoherence |
| **Quantum Computing** | QX | ZS-QC, QH, QS | Quantum algorithms, hardware, simulation |
| **Translational** | T | ZS-T1 ~ T3 | Experimental proposals, observational tests |

---

## File Naming Convention

```
zs_{paper_id}_verify_v1_0.py
```

Examples: `zs_f2_verify_v1_0.py`, `zs_u3_verify_v1_0.py`, `zs_qc_verify_v1_0.py`

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `numpy` | ≥ 1.21 | Numerical arrays and linear algebra |
| `scipy` | ≥ 1.7 | Integration, optimization, special functions |
| `mpmath` | ≥ 1.3 | Arbitrary-precision arithmetic (50-digit precision) |
| `python-docx` | ≥ 0.8.11 | *(Optional)* Cross-reference checks for QC/QH/QS papers |

All scripts use only standard scientific Python packages — no custom frameworks required.

---

## What Each Script Verifies

Each verification suite independently checks:

1. **Zero Free Parameter audit** — every physical quantity traces back to A = 35/437 and Q = 11
2. **Algebraic correctness** — step-by-step re-derivation of all equations
3. **Cross-reference consistency** — results used by downstream papers remain valid
4. **Observational agreement** — comparison against Planck 2018, PDG, and other experimental data
5. **Anti-numerology tests** — Monte Carlo verification that numerical coincidences are statistically significant
6. **Falsification gate checks** — explicit pass/fail criteria for framework survival

---

## Expected Output

A successful run produces:

```
================================================================================
  Z-Spin Cosmology — Verification Suite Runner
  Papers: 46 | A = 35/437 | Q = 11
================================================================================

  [ 1/46] Running ZS-F0...  ✅ PASS  (34/34 tests, 2.1s)
  [ 2/46] Running ZS-F1...  ✅ PASS  (15/15 tests, 0.8s)
  ...
  [46/46] Running ZS-U8...  ✅ PASS  (18/18 tests, 1.2s)

================================================================================
  SUMMARY: 46/46 papers PASS
  Total individual tests: XXXX/XXXX
  Total time: XXs

  ★★★ ALL 46 PAPERS PASSED (XXXX individual tests) ★★★
================================================================================
```

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'numpy'`**  
→ Make sure the virtual environment is activated and dependencies are installed:
```bash
source zspin_env/bin/activate   # or zspin_env\Scripts\activate on Windows
pip install -r requirements.txt
```

**`python: command not found`**  
→ On some systems, use `python3` instead of `python`:
```bash
python3 -m venv zspin_env
python3 run_all.py
```

**Windows: `Activate.ps1 cannot be loaded because running scripts is disabled`**  
→ Run PowerShell as administrator and execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**`python-docx` import error on QC/QH/QS scripts**  
→ These scripts are optional. Install with: `pip install python-docx`

---

## License

This verification suite is publicly available for independent reproduction of Z-Spin Cosmology results.

## Citation

If you use these scripts in your research, please cite:

```
K. Kang, "Z-Spin Cosmology: A Zero-Free-Parameter Scalar-Tensor Framework,"
GitHub: https://github.com/KennyKang-git/zspin (2026).
```
