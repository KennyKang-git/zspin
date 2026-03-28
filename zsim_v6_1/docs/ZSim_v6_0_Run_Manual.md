# Z-Sim v6.0 Run Manual

| Field | Value |
|---|---|
| **Primary package** | `zsim_v6_0.zip` |
| **Current scope** | Integrated cosmology + production LGT architecture |
| **Status** | Research / validation / preproduction |
| **Tests** | 348/348 PASS (306 v5.7 backward + 42 v6.0 new) |

> **What v6.0 is:** A complete architectural rebuild of the lattice gauge theory (LGT) layer,
> implementing the 5-phase MBP protocol (ZS-S4 §6.11.4) with periodic boundaries, overlap
> Dirac operator, Wilson gradient flow, caloron backgrounds, and continuum extrapolation.
> All v5.7 cosmology and reduced-LGT modules are preserved and backward-compatible.

> **What v6.0 is NOT:** A final Higgs VEV closure artifact. v = 246 GeV remains **NON-CLAIM**
> pending production-scale lattice computation on larger lattices with proper continuum extrapolation.

---

## 1. Architecture Improvements over v5.x

| # | v5.x (surrogate) | v6.0 (production architecture) | Module |
|---|---|---|---|
| 1 | Open boundary BCC | **Periodic BCC T³** (torus) | `zsim/lgt2/lattice.py` |
| 2 | Discrete cooling (10 steps) | **Wilson gradient flow** (Lüscher RK3 ODE) | `zsim/lgt2/gradient_flow.py` |
| 3 | Wilson fermion only | **Overlap Dirac** (Neuberger, exact GW) | `zsim/lgt2/dirac_overlap.py` |
| 4 | No lattice spacing concept | **Explicit a, continuum extrapolation** | `zsim/lgt2/continuum.py` |
| 5 | `cooled_random` background | **BPS monopole / I-Ī caloron** | `zsim/lgt2/caloron.py` |

### Critical Bug Fix

v5.x contained `1j * gamma_dir` in the Wilson hopping term, which **broke γ₅-Hermiticity** of the
Dirac operator. This was the root cause of the shape-dependent consistency gap divergence observed
in v5.6.4 experiments. v6.0 uses the correct `(r ∓ γ·n̂)` convention, and the Ginsparg-Wilson
residual is now verified at ∼10⁻¹⁴.

---

## 2. Setup

```bash
unzip zsim_v6_0.zip
cd zsim_v6_0
python -m venv .venv
source .venv/bin/activate   # Linux/WSL
# .venv\Scripts\Activate.ps1   # Windows PowerShell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Recommended Python: **3.11 or 3.12**. Minimum: 3.10.

---

## 3. Validation

Run the full test suite first:

```bash
python -m pytest -q
# Expected: 348 passed
```

Run only the new v6.0 LGT2 tests:

```bash
python -m pytest tests/test_lgt2.py -v
# Expected: 42 passed
```

---

## 4. Quick Start: Core Cosmology (unchanged from v5.7)

```bash
python scripts/quickstart.py background
python scripts/quickstart.py compare
python scripts/quickstart.py scan
python scripts/quickstart.py report
```

---

## 5. Quick Start: v6.0 Production LGT

### 5.1 Build a Periodic BCC Lattice

```python
from zsim.lgt2.lattice import build_periodic_bcc
lattice = build_periodic_bcc(4, 4, 4, a=1.0)
print(f"Sites: {lattice.num_sites}")        # 128
print(f"Edges: {lattice.num_edges}")         # 512
print(f"Plaquettes: {lattice.num_plaquettes}") # 768
print(f"Boundary: periodic T³")
```

### 5.2 Create a Gauge Field + Wilson Gradient Flow

```python
from zsim.lgt2.gauge_field import GaugeField, avg_plaquette
from zsim.lgt2.gradient_flow import WilsonGradientFlow

gf = GaugeField.random(lattice, beta=2.3, seed=42)
print(f"Initial <P>: {avg_plaquette(gf):.6f}")

flow = WilsonGradientFlow(epsilon=0.01, max_steps=100)
trajectory = flow.flow(gf, n_steps=100, record_every=10)
for st in trajectory:
    print(f"  t={st.flow_time:.3f}: <P>={st.avg_plaq:.6f}")
```

### 5.3 Generate I-Ī Caloron Background

```python
from zsim.lgt2.caloron import CaloronBackground

cal = CaloronBackground.symmetric_pair(
    lattice, separation_fraction=0.4, rho_inst=0.5
)
gf_caloron = cal.generate(beta=2.3)
```

### 5.4 Compute Overlap Dirac Spectrum

```python
from zsim.lgt2.dirac_overlap import OverlapDirac

ov = OverlapDirac(gf_caloron, rho=1.0, wilson_r=1.0)
gw_residual = ov.verify_ginsparg_wilson()
print(f"GW residual: {gw_residual:.2e}")  # should be ~10⁻¹⁴

spec = ov.spectrum()
print(f"Q = {spec.topological_charge}, zero modes = {spec.zero_modes}")
```

### 5.5 Full MBP v2 Pipeline (5-Phase Protocol)

```python
from zsim.lgt2.mbp2 import run_mbp2_pipeline

result = run_mbp2_pipeline(
    shape=(4, 4, 4),
    flow_steps=50,
    flow_epsilon=0.01,
    overlap_rho=1.0,
    wilson_r=1.0,
    chirality_mode="left",
)
print(f"sign_match:       {result.gamma_sign_match}")
print(f"consistency_gap:  {result.gamma_consistency_gap:.6e}")
print(f"kappa2_extracted: {result.kappa2_extracted:.6e}")
print(f"kappa2_target:    {result.kappa2_target}")
print(f"F-MBP-1 (exist):  {result.fmb1_bilinear_exists}")
print(f"F-MBP-2 (sign):   {result.fmb2_sign_correct}")
print(f"STATUS:           {result.status}")
```

---

## 6. Continuum Extrapolation

```python
from zsim.lgt2.continuum import ContinuumExtrapolator, lattice_spacing_from_beta
from zsim.lgt2.mbp2 import run_mbp2_pipeline

ext = ContinuumExtrapolator()
for beta in [2.0, 2.3, 2.5, 2.7]:
    a = lattice_spacing_from_beta(beta)
    result = run_mbp2_pipeline(shape=(4,4,4), lattice_spacing=a, beta=beta,
                                flow_steps=50, flow_epsilon=0.01)
    ext.add_point("gamma_h2_trace", beta, a, (4,4,4),
                  result.gamma_h2_trace, abs(result.gamma_consistency_gap))

continuum = ext.extrapolate("gamma_h2_trace")
print(f"Continuum limit: {continuum.continuum_value:.6e} ± {continuum.continuum_error:.2e}")
print(f"χ²/dof: {continuum.chi2_per_dof:.3f}")
```

---

## 7. Cobaya CMB Runs (unchanged from v5.7)

```bash
cobaya-run cobaya_f32/zspin_local_test.yaml
cobaya-run cobaya_f32/zspin_grid_2d.yaml
cobaya-run cobaya_f32/zspin_bare_mcmc.yaml
cobaya-run cobaya_f32/zspin_mcmc_planck.yaml --packages-path ~/packages
```

---

## 8. What to Inspect in Outputs

### MBP v2 results

| Field | Meaning |
|---|---|
| `gamma_sign_match` | Trace method and FD method agree on sign |
| `gamma_consistency_gap` | |trace − fd| (should decrease with shape) |
| `ginsparg_wilson_residual` | GW relation check (~10⁻¹⁴ is correct) |
| `topological_charge` | Q=0 for I-Ī, Q=±1 for single instanton |
| `mu2_formula_proxy` | N_c × MBP bracket (should be positive for EWSB) |
| `kappa2_extracted` | Compared to target 0.0906 |
| `fmb1_bilinear_exists` | F-MBP-1 gate |
| `fmb2_sign_correct` | F-MBP-2 gate (μ² > 0 → tachyonic → EWSB) |
| `status` | OBSERVATION / HYPOTHESIS / FAIL:F-MBP-N |

---

## 9. v6.0 Validated Physics Results (2×2×2 → 3×3×3)

| Observable | 2×2×2 | 3×3×3 | Trend |
|---|---|---|---|
| GW residual | 3.67×10⁻¹⁴ | 9.83×10⁻¹⁴ | Stable ∼10⁻¹⁴ ✅ |
| Q (topological charge) | 0 | 0 | Correct for I-Ī ✅ |
| sign_match | True | True | Stable ✅ |
| consistency_gap | 4.690 | 0.044 | **Converging** ✅ |
| F-MBP-1 (exist) | True | True | ✅ |
| F-MBP-2 (sign) | True | True | ✅ |

The consistency gap dropping from 4.69 → 0.044 (×107 improvement) as lattice size increases
is the critical convergence signature that v5.x never achieved.

---

## 10. Recommended Experimental Sequence

### Phase A: Shape Scaling (fixed β)

```python
for shape in [(2,2,2), (3,3,3), (4,4,4), (5,5,5), (6,6,6)]:
    result = run_mbp2_pipeline(shape=shape, flow_steps=100, flow_epsilon=0.01)
    # Track: consistency_gap, sign_match, kappa2_extracted
```

### Phase B: Multi-β Continuum Extrapolation

```python
for beta in [2.0, 2.3, 2.5, 2.7, 3.0]:
    for shape in [(4,4,4), (6,6,6)]:
        a = lattice_spacing_from_beta(beta)
        result = run_mbp2_pipeline(shape=shape, lattice_spacing=a, beta=beta, ...)
```

### Phase C: Caloron Parameter Scan

```python
for sep in [0.2, 0.3, 0.4, 0.5, 0.6]:
    for rho in [0.3, 0.5, 0.7, 1.0]:
        result = run_mbp2_pipeline(separation_fraction=sep, rho_inst=rho, ...)
```

---

## 11. Version History

| Version | Key Addition |
|---|---|
| v3.1 | ZSim baseline: 227 tests, 7 modules |
| v5.6.4 | Wilson-r / chirality sweep, reduced SU(2) lattice |
| v5.7 | Stage-26 shape-adaptive ledger, integrated package |
| **v6.0** | **Periodic BCC T³, overlap Dirac, Wilson gradient flow, caloron backgrounds, continuum extrapolation, γ₅-Hermiticity fix** |

---

## 12. Current Status Interpretation

- **What v6.0 gives you:** The correct mathematical and physical architecture for MBP verification — periodic boundaries, exact chiral symmetry (GW relation), proper gauge smoothing, and instanton-based backgrounds.

- **What v6.0 does NOT yet give you:** Final Higgs VEV closure. The `kappa2_extracted` values on small research lattices are still far from the target 0.0906. This requires larger lattices (8³+), multiple β values, and proper continuum extrapolation — a computational campaign, not a code fix.

- **The v5.x consistency gap divergence is resolved.** The root cause (broken γ₅-Hermiticity from the `1j` factor in the Wilson hopping term) is fixed, and the gap now converges as expected with increasing lattice size.
