# Z-Sim v1.0

**Z-Sim** is a theory-native simulator and validation harness for **Z-Spin Cosmology**.
It turns analytic claims into executable tests, structural kill-switches, and forward predictions that can be stress-tested before expensive external inference.

## Why a researcher would use this

- Test what Z-Spin predicts **before** full Bayesian fitting.
- Separate **structural claims** from **closure / implementation choices**.
- Fail early before expensive **Cobaya / CAMB / CLASS** runs.
- Run **Z-Spin-specific topology, Dirac, and lattice experiments** that standard cosmology pipelines do not target.
- Verify **Standard Model predictions** (gauge couplings, EWSB, fermion masses, CKM) derived from polyhedral geometry.

## What it is not

- **Not** a replacement for **Cobaya, CAMB, CLASS, MadGraph, PYTHIA, or Geant4**.
- It is an **executable bridge layer** between Z-Spin derivations and community-standard inference workflows.

## Quick facts

- **Version:** 1.0.0
- **Python:** ≥ 3.10 (3.11–3.12 recommended)
- **Tests:** 403 collected (377 pass on clean install; 26 stage-fixture tests require prior outputs)
- **Status:** Research / validation / preproduction

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/quickstart.py background
```

---

## 1. What Z-Sim is for

Z-Sim is built around five research tasks.

### A. Lock the theory into executable form
Z-Spin papers contain structural commitments that should not remain only prose-level claims.
Z-Sim encodes them as runnable kernels, observable compilers, and validation gates.

### B. Separate derivation from implementation choice
Many outcomes depend on closure choices, mediation modes, source terms, or lattice presets.
Z-Sim lets you scan those choices explicitly instead of hiding them in a single narrative result.

### C. Fail early before expensive external inference
Before running full Cobaya + CAMB + likelihood pipelines, Z-Sim can check whether a candidate model is even internally coherent.
This saves time and prevents over-claiming.

### D. Provide a Z-Spin-native numerical laboratory
The `lgt/`, `lgt2/`, and `quantum/` layers exist because some Z-Spin questions are not standard ΛCDM parameter-fitting questions.
They require custom topology, Dirac, chirality, instanton, and mediation experiments.

### E. Derive and verify Standard Model predictions from geometry
The `sm/` package computes gauge couplings, electroweak symmetry breaking parameters, fermion mass ratios, and CKM matrix elements — all from the geometric impedance constant `A = 35/437` and polyhedral geometry, with zero free parameters.

---

## 2. What you can test with Z-Sim

### 2.1 Core cosmology / forward prediction
Z-Sim can run background evolution and compile derived observables such as:

- `H₀`
- `Ω_m`
- `ω_cdm h²`
- `n_s`
- `r`
- selected closure-dependent proxy quantities

This is the right layer for asking:

- Does a zero-free-parameter closure produce a sensible cosmological trajectory?
- How sensitive are predictions to mediation or closure choices?
- Which outputs are robust enough to deserve external likelihood testing?

### 2.2 Standard Model predictions
The `sm/` package derives particle physics observables from polyhedral geometry:

- `α_s(M_Z)` — strong coupling constant from `A = 35/437` and `Q = 11`
- `sin²θ_W(M_Z)` — weak mixing angle via icosahedral geometry
- `1/α_EM` — fine structure constant with NLO correction (`c₄ = 4/13`)
- Higgs VEV `v = 245.93 GeV` — via Factorized Determinant Theorem
- Top quark mass `m_t = 171.5 GeV` — TESTABLE at FCC-ee (~2040)
- Fermion mass ratios via A₅ ≅ I representation theory and Yukawa tensor
- Cabibbo angle via `arctan(1/φ³)`

This is the right layer for asking:

- Which SM parameters are genuinely derived from geometry vs. numerological coincidence?
- Do the icosahedral group representations produce physically correct structures?
- Which predictions are falsifiable by current or near-future experiments?

### 2.3 Structural consistency and kill-switches
Z-Sim contains explicit validation layers for claims such as:

- `Q = 11` register slots
- `(X, Z, Y) = (3, 2, 6)` sector decomposition
- no direct `X ↔ Y` transfer
- Z-mediated transfer only
- effective transfer rank ≤ 2
- geometric constant `A = 35/437`

This is the right layer for asking:

- Is a proposed implementation still the same theory?
- Did a code change silently violate a structural invariant?
- Which claims survive automated regression tests?

### 2.4 Closure and implementation sensitivity
The closure matrix utilities let you vary items such as:

- phase-source mode
- mediation mode
- epsilon-source mode
- `H`-closure mode

This is the right layer for asking:

- Is a result genuinely derived, or only true for one fragile implementation choice?
- Which observables are stable across closures?
- Which branches should be labeled OBSERVATION, DERIVED, HYPOTHESIS, or FAIL?

### 2.5 Quantum / topology / lattice-side experiments
The `quantum/`, `lgt/`, and especially `lgt2/` stack provide a numerical testbed for Z-Spin-specific nonperturbative ideas, including:

- polyhedral / incidence / Hodge structures
- reduced SU(2) lattice experiments
- periodic BCC `T³` lattice construction
- Wilson gradient flow
- corrected Wilson-Dirac and overlap-Dirac operators
- I-Ī caloron backgrounds
- continuum extrapolation
- MBP v2 extraction / validation protocols

This is the right layer for asking:

- Does the sign structure survive a better fermion operator?
- Do chirality and topology behave correctly under overlap / GW checks?
- Does an MBP-style extraction improve or collapse when shape and β are scaled?

---

## 3. What Z-Sim does **not** replace

Z-Sim should be positioned honestly.

### It does **not** replace Cobaya
Cobaya is a sampling / inference framework.
Z-Sim is a theory-native simulator and validation harness.
Use Z-Sim to prepare and stress-test the theory side; use Cobaya to perform external statistical inference.

### It does **not** replace CAMB or CLASS
CAMB / CLASS are mature Boltzmann solvers used in community-standard cosmological inference.
Z-Sim is not yet a general-purpose perturbation solver at that level.

### It does **not** replace collider stacks
Z-Sim is not a substitute for MadGraph, PYTHIA, or Geant4.
It does not aim to be a full event generator, shower / hadronization chain, or detector simulator.

### It does **not** by itself prove observational viability
A good Z-Sim run can show internal consistency, forward predictions, and numerical robustness.
It cannot by itself replace official likelihood-based confrontation with data.

---

## 4. Why a researcher might use Z-Sim

A researcher who does **not** already believe Z-Spin may still find Z-Sim useful for four reasons.

### 4.1 It makes the claim inspectable
Instead of reading only equations in a paper, the researcher can see exactly what was implemented.

### 4.2 It makes failure reproducible
A negative result is valuable only if it can be reproduced. Z-Sim is organized around tests, gates, and explicit failure modes.

### 4.3 It prevents premature hand-waving
The closure scan and kill-switch philosophy force a distinction between:

- structural theorem-level content
- numerical observation
- implementation artifact
- unsupported overreach

### 4.4 It is a handoff layer to standard tools
The Cobaya scaffold is useful precisely because Z-Sim is **not** pretending to be the full external inference stack.
It helps package a Z-Spin hypothesis into a form that standard tools can challenge.

---

## 5. Core structural commitments

- `Q = 11` register slots
- `(X, Z, Y) = (3, 2, 6)` sector decomposition
- no direct `X ↔ Y` path; Z-mediated transfer only
- effective `X ↔ Y` transfer rank ≤ 2
- geometric constant `A = 35/437`

---

## 6. What's new in v1.0

v1.0 is the **Grand Setup** public release, consolidating all internal development (v3.1 through v7.0) into a single versioned package.

### Standard Model predictions from polyhedral geometry (v7.0 → v1.0)

The `zsim/sm/` package (7 modules) derives Standard Model observables from `A = 35/437`:

| Module | Description |
|---|---|
| `gauge_couplings.py` | α_s, sin²θ_W, α₂, 1/α_EM with NLO correction, β-function coefficients |
| `ewsb.py` | Higgs VEV = 245.93 GeV (DERIVED), top quark mass = 171.5 GeV (TESTABLE) |
| `icosahedral.py` | Full A₅ ≅ I representation engine: 60 rotations, 5 conjugacy classes, 3 irreps |
| `yukawa.py` | D₅ channel decomposition, S⁴ VEV optimization, fermion mass ratios, CKM |
| `m0_lattice.py` | McKay correspondence lattice construction |
| `mckay_bridge.py` | McKay bridge between polyhedral and gauge structures |
| `report.py` | Unified SM prediction pipeline with PDG 2024 / CODATA pull table |

42 new automated tests across 7 categories: Polyhedral Invariants, Gauge Couplings, EWSB, Icosahedral Group, Fermion Mass, CKM, and Neutrino.

### Face Counting `Ω_m` Synchronization (v6.1)
Resolved the internal inconsistency where CDM used face counting (`32/121`) but total matter density still used slot counting (`39/121`).

| Parameter | v6.0 (slot) | v6.1+ (face) |
|---|---|---|
| `Ω_m` bare | `39/121 = 0.3223` | `38/121 = 0.3140` |
| `Ω_m` eff | `0.2984` | `0.2908` |
| `S₈` prediction | `~0.794` | `~0.777` |
| `S₈` vs DES Y3 | `+1.06σ` | `+0.06σ` |
| `Ω_m` vs DESI | `0.11σ` | `0.78σ` |

Face-counting sector budget (all **OBSERVATION** status):

| Sector | Formula | Value |
|---|---|---|
| Baryon | `F(cube)/Q²` | `6/121` |
| CDM | `F(truncated icosahedron)/Q²` | `32/121` |
| Dark energy | `1 − 38/121` | `83/121` |
| Total matter | `(6+32)/121` | `38/121` |

### Production LGT rebuild (v6.0)

| # | v5.x (surrogate) | v6.0+ (production) | Module |
|---|---|---|---|
| 1 | Open boundary BCC | Periodic BCC `T³` (torus) | `zsim/lgt2/lattice.py` |
| 2 | Discrete cooling | Wilson gradient flow (Lüscher RK3) | `zsim/lgt2/gradient_flow.py` |
| 3 | Wilson fermion only | Overlap Dirac (exact GW) | `zsim/lgt2/dirac_overlap.py` |
| 4 | No lattice spacing | Explicit `a`, continuum extrapolation | `zsim/lgt2/continuum.py` |
| 5 | Cooled random | BPS monopole / I-Ī caloron | `zsim/lgt2/caloron.py` |

**Critical fix:** the v5.x Wilson hopping term `1j * gamma_dir` broke `γ₅`-Hermiticity.
v6.0 uses the correct `(r ∓ γ·n̂)` convention. GW residual now reaches `~10⁻¹⁴`.

---

## 7. Install

```bash
unzip zsim_v1_0.zip
cd zsim_v1_0
python -m pip install -r requirements.txt
```

For development and tests:

```bash
python -m pip install -r requirements-dev.txt
```

---

## 8. Validate the install

```bash
# Full test suite
python -m pytest -q
# Expected: 377+ passed on a clean install
# Note: stage-fixture tests need prior outputs

# Core cosmology tests
python -m pytest tests/test_friedmann.py tests/test_inflation.py tests/test_kernel.py -v

# Standard Model prediction tests
python -m pytest tests/test_sm_predictions.py -v

# Production LGT tests
python -m pytest tests/test_lgt2.py -v
```

---

## 9. Quick start — most useful entry points

### 9.1 Core cosmology

```bash
python scripts/quickstart.py background
python scripts/quickstart.py compare
python scripts/quickstart.py scan
python scripts/quickstart.py report
```

These use `configs/derived.yaml` and write outputs under `outputs/`.

### 9.2 Standard Model predictions

```python
from zsim.sm.report import run_sm_report

results = run_sm_report()
for r in results:
    print(f"{r.name}: Z-Spin={r.predicted}, Obs={r.observed}, Pull={r.pull}")
```

Or run the test suite directly:

```bash
python -m pytest tests/test_sm_predictions.py -v
```

### 9.3 Direct CLI

```bash
# Background evolution
python -m zsim.apps.run_background --config configs/derived.yaml \
  --output-dir outputs/smoke --no-plots

# Baseline comparison
python -m zsim.apps.compare_baselines --config configs/derived.yaml \
  --output-dir outputs/compare --no-plots

# Parameter scan
python -m zsim.apps.run_scan --config configs/derived.yaml \
  --output-dir outputs/scan --vary gamma_xz gamma_zy --factors 0.0,1.0,2.0

# Report generation
python -m zsim.apps.report_results --source-dir outputs/smoke \
  --output-dir outputs/smoke/report

# Index report over all outputs
python -m zsim.apps.report_results --source-dir outputs \
  --output-dir outputs/report_index --index

# Closure experiment matrix
python -m zsim.apps.run_closure_matrix --config configs/derived.yaml \
  --output-dir outputs/closure \
  --phase-source-modes full_state,currents_only \
  --mediation-modes raw_contrast,normalized_contrast \
  --epsilon-source-modes zero \
  --h-closure-modes sqrt_sum \
  --no-plots
```

### 9.4 Production LGT (`lgt2/`)

#### Build a periodic BCC lattice

```python
from zsim.lgt2.lattice import build_periodic_bcc
lattice = build_periodic_bcc(4, 4, 4, a=1.0)
print(f"Sites: {lattice.num_sites}")
print(f"Edges: {lattice.num_edges}")
print(f"Plaquettes: {lattice.num_plaquettes}")
```

#### Wilson gradient flow

```python
from zsim.lgt2.gauge_field import GaugeField
from zsim.lgt2.gradient_flow import WilsonGradientFlow

gf = GaugeField.random(lattice, beta=2.3, seed=42)
flow = WilsonGradientFlow(epsilon=0.01, max_steps=100)
trajectory = flow.flow(gf, n_steps=100, record_every=10)
for st in trajectory:
    print(f"t={st.flow_time:.3f}: <P>={st.avg_plaq:.6f}")
```

#### I-Ī caloron background

```python
from zsim.lgt2.caloron import CaloronBackground
cal = CaloronBackground.symmetric_pair(lattice, separation_fraction=0.4, rho_inst=0.5)
gf_caloron = cal.generate(beta=2.3)
```

#### Overlap Dirac spectrum

```python
from zsim.lgt2.dirac_overlap import OverlapDirac
ov = OverlapDirac(gf_caloron, rho=1.0, wilson_r=1.0)
gw_residual = ov.verify_ginsparg_wilson()
print(f"GW residual: {gw_residual:.2e}")
spec = ov.spectrum()
print(f"Q = {spec.topological_charge}, zero modes = {spec.zero_modes}")
```

#### Full MBP v2 pipeline

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
print(f"F-MBP-1 (exist):  {result.fmb1_bilinear_exists}")
print(f"F-MBP-2 (sign):   {result.fmb2_sign_correct}")
print(f"STATUS:           {result.status}")
```

#### Continuum extrapolation

```python
from zsim.lgt2.continuum import ContinuumExtrapolator, lattice_spacing_from_beta
from zsim.lgt2.mbp2 import run_mbp2_pipeline

ext = ContinuumExtrapolator()
for beta in [2.0, 2.3, 2.5, 2.7]:
    a = lattice_spacing_from_beta(beta)
    result = run_mbp2_pipeline(
        shape=(4, 4, 4),
        lattice_spacing=a,
        beta=beta,
        flow_steps=50,
        flow_epsilon=0.01,
    )
    ext.add_point(
        "gamma_h2_trace",
        beta,
        a,
        (4, 4, 4),
        result.gamma_h2_trace,
        abs(result.gamma_consistency_gap),
    )

continuum = ext.extrapolate("gamma_h2_trace")
print(f"Continuum limit: {continuum.continuum_value:.6e} ± {continuum.continuum_error:.2e}")
print(f"χ²/dof: {continuum.chi2_per_dof:.3f}")
```

---

## 10. Cobaya bridge / CMB validation

Z-Sim includes a **Cobaya bridge layer**, not a Cobaya replacement.

Requires separate installation of:

- Cobaya
- CAMB
- Planck likelihood packages

```bash
# Local smoke test
cobaya-run cobaya_f32/zspin_local_test.yaml

# Face-counting 38/121 test
cobaya-run cobaya_f32/zspin_38_121_test.yaml

# 2D grid scan
cobaya-run cobaya_f32/zspin_grid_2d.yaml

# Bare MCMC (no Planck)
cobaya-run cobaya_f32/zspin_bare_mcmc.yaml

# Full Planck MCMC (production; requires packages path)
cobaya-run cobaya_f32/zspin_mcmc_planck.yaml --packages-path ~/packages
```

Current best stored result: **Δχ² = 3.9** (`face counting`, `plik_lite`).

Use this layer when you want to ask:

- Is the theory packaged cleanly enough for external inference?
- Does a Z-Sim-generated closure survive a first likelihood confrontation?
- Which parameterizations are worth promoting to a full MCMC run?

---

## 11. Recommended research workflow

### Workflow A — Theory-side sanity check
1. Run `background`
2. Run `compare`
3. Run `scan`
4. Run `closure_matrix`
5. Keep only branches that survive kill-switches

### Workflow B — Lattice-side stress test
1. Start with a small periodic BCC lattice
2. Check flow stability
3. Verify overlap / GW residual
4. Run MBP v2 extraction
5. Increase shape and β
6. Attempt continuum extrapolation

### Workflow C — External confrontation
1. Select a robust closure branch from Workflow A
2. Package it through `cobaya_f32/`
3. Run local smoke test
4. Run bare MCMC / grid scan
5. Run full Planck-likelihood job only after prior gates pass

### Workflow D — Standard Model verification
1. Run `tests/test_sm_predictions.py` to verify all 42 SM tests
2. Inspect gauge coupling derivation chains via `sm/gauge_couplings.py`
3. Verify icosahedral group representations via `sm/icosahedral.py`
4. Check fermion mass ratios and CKM via `sm/yukawa.py`
5. Generate full pull table via `sm/report.py`

---

## 12. Package structure

```text
zsim_v1_0/
├── zsim/
│   ├── core/           Constants (A=35/437), config, state vector
│   ├── kernel/         Physics kernels (Friedmann, inflation, mediation)
│   ├── solver/         ODE integrator (segmented RK45)
│   ├── observables/    Observable compiler (n_s, r, H₀, Ω_m)
│   ├── validation/     Kill-switches and structural verification
│   ├── io/             Reports, plots, serialization, pipeline I/O
│   ├── apps/           CLI entry points
│   ├── quantum/        Polyhedral spectra, Hodge, Dirac, incidence
│   ├── lgt/            Reduced SU(2) lattice layer (Stage 4–26, surrogate)
│   ├── lgt2/           Production LGT layer (v6.0+)
│   └── sm/             Standard Model predictions from polyhedral geometry
├── configs/            YAML configurations
├── cobaya_f32/         Cobaya Gate F32-12 templates
├── cobaya_scaffold/    Cobaya scaffold configs
├── scripts/            Quickstart and scan scripts
├── tests/              Regression, stage, and SM prediction tests
├── docs/               Setup, run guides, stage notes
└── outputs/            Example outputs
```

### Key `sm/` modules

| Module | Description |
|---|---|
| `gauge_couplings.py` | α_s = 11/93, sin²θ_W, 1/α_EM = 137.036 (NLO) |
| `ewsb.py` | Higgs VEV = 245.93 GeV, m_t = 171.5 GeV |
| `icosahedral.py` | A₅ ≅ I engine: 60 rotations, character table, 3 irreps |
| `yukawa.py` | D₅ channels, S⁴ VEV, fermion mass ratios, CKM |
| `m0_lattice.py` | McKay correspondence lattice construction |
| `mckay_bridge.py` | McKay bridge between polyhedral and gauge structures |
| `report.py` | Unified prediction pipeline, pull table generation |

### Key `lgt2/` modules

| Module | Description |
|---|---|
| `lattice.py` | Periodic BCC `T³` lattice construction |
| `gauge_field.py` | Wilson plaquette action, staples, topological charge |
| `gradient_flow.py` | Wilson gradient flow (Lüscher RK3) |
| `dirac_wilson.py` | Corrected Wilson fermion (`γ₅`-Hermitian) |
| `dirac_overlap.py` | Neuberger overlap operator (exact GW relation) |
| `caloron.py` | I-Ī molecular instanton backgrounds |
| `continuum.py` | Multi-β continuum extrapolation (`O(a²)` fit) |
| `mbp2.py` | 5-phase MBP protocol |
| `su2.py` | SU(2) algebra utilities |

---

## 13. MBP v2 output reference

| Field | Meaning |
|---|---|
| `gamma_sign_match` | Trace method and FD method agree on sign |
| `gamma_consistency_gap` | `|trace − fd|`; should improve with scaling |
| `ginsparg_wilson_residual` | GW relation check (`~10⁻¹⁴` is correct) |
| `topological_charge` | `Q=0` for I-Ī, `Q=±1` for single instanton |
| `mu2_formula_proxy` | `N_c × MBP bracket` (positive → EWSB proxy) |
| `kappa2_extracted` | Compared to target `0.0906` |
| `fmb1_bilinear_exists` | F-MBP-1 gate |
| `fmb2_sign_correct` | F-MBP-2 gate |
| `status` | `OBSERVATION` / `HYPOTHESIS` / `FAIL:F-MBP-N` |

### Validated convergence snapshot (v6.0+)

| Observable | 2×2×2 | 3×3×3 | Trend |
|---|---|---|---|
| GW residual | `3.67×10⁻¹⁴` | `9.83×10⁻¹⁴` | Stable `~10⁻¹⁴` ✓ |
| Q (topological) | `0` | `0` | Correct for I-Ī ✓ |
| sign_match | `True` | `True` | Stable ✓ |
| consistency_gap | `4.690` | `0.044` | `×107` improvement ✓ |

---

## 14. Recommended experimental sequence for `lgt2/`

### Phase A — Shape scaling at fixed β

```python
for shape in [(2,2,2), (3,3,3), (4,4,4), (5,5,5), (6,6,6)]:
    result = run_mbp2_pipeline(shape=shape, flow_steps=100, flow_epsilon=0.01)
```

### Phase B — Multi-β continuum extrapolation

```python
for beta in [2.0, 2.3, 2.5, 2.7, 3.0]:
    for shape in [(4,4,4), (6,6,6)]:
        a = lattice_spacing_from_beta(beta)
        result = run_mbp2_pipeline(shape=shape, lattice_spacing=a, beta=beta, ...)
```

### Phase C — Caloron parameter scan

```python
for sep in [0.2, 0.3, 0.4, 0.5, 0.6]:
    for rho in [0.3, 0.5, 0.7, 1.0]:
        result = run_mbp2_pipeline(separation_fraction=sep, rho_inst=rho, ...)
```

---

## 15. Current status

### What v1.0 gives you

- **Standard Model predictions** from polyhedral geometry (gauge couplings, EWSB, fermion masses, CKM)
- Higgs VEV `v = 245.93 GeV` (**DERIVED** via Factorized Determinant Theorem)
- face-counting `Ω_m` synchronization (`38/121`)
- a production-grade `lgt2/` architecture
- periodic boundaries, overlap chirality, gradient flow, caloron backgrounds
- a bridge into Cobaya-based validation
- a test-oriented workflow for ruling out fragile claims early

### What v1.0 does **not** give you

- final full-Planck production validation by itself (Gate F32-12 pending)
- a community-standard replacement for CAMB / CLASS
- a collider / detector simulation stack
- a theoretical derivation of `32/121` CDM from truncated-icosahedron mediation (still **OBSERVATION**)
- full D₅×A₄ cross-structure derivation for the Cabibbo angle (still **OBSERVATION**)

### Selected zero-free-parameter headline outputs

#### Cosmology

| Observable | Z-Spin | Observation / reference |
|---|---|---|
| `H₀` (CMB) | `67.36 km/s/Mpc` | `67.36 ± 0.54` |
| `H₀` (local) | `72.98 km/s/Mpc` | `73.04 ± 1.04` |
| `n_s` (`N*=60`) | `0.9674` | `0.9649 ± 0.0042` |
| `r` | `0.0091` | `< 0.036` |
| `ω_cdm h²` | `0.12000` | `0.1200 ± 0.0012` |

#### Standard Model

| Observable | Z-Spin | Observed | Pull/Dev | Status |
|---|---|---|---|---|
| `α_s(M_Z)` | `11/93 = 0.1183` | `0.1180 ± 0.0009` | `+0.31σ` | DERIVED |
| `sin²θ_W(M_Z)` | `(48/91)·x*` | `0.23122 ± 3×10⁻⁵` | `−1.26σ` | DERIVED |
| `1/α_EM` | `137.036` | `137.036` | `1.07 ppm` | HYPOTHESIS (s) |
| `v` (Higgs VEV) | `245.93 GeV` | `246.22 GeV` | `0.12%` | DERIVED |
| `m_t` (top quark) | `171.5 GeV` | `172.57 ± 0.29` | `−3.69σ` | TESTABLE |
| `σ₁/σ₂` (mτ/mμ) | `17.00` | `16.82` | `1.1%` | DERIVED |
| `σ₁/σ₃` (mτ/me) | `3477` | `3477` | `0.0%` | DERIVED |
| Cabibbo angle | `13.28°` | `13.04°` | `1.9%` | OBSERVATION |

---

## 16. Version history

| Version | Key addition |
|---|---|
| `v3.1` | Z-Sim baseline: semantic closure, 227 tests, 7 modules |
| `v3.7–v5.7` | Quantum topology and reduced SU(2) LGT Stage 4–26 |
| `v6.0` | Production LGT: periodic `T³`, overlap Dirac, gradient flow, caloron, `γ₅` fix |
| `v6.1` | Face-counting `Ω_m` sync: `39/121 → 38/121`, improved `S₈` alignment |
| `v7.0` | Standard Model predictions: `sm/` package (gauge couplings, EWSB, Yukawa, CKM) |
| `v1.0` | **Grand Setup** public release — consolidated from internal v3.1–v7.0 |

See `CHANGELOG.md` for the full history.

---

## 17. Further documentation

| Document | Description |
|---|---|
| `docs/QUICKSTART.md` | Copy/paste quickstart guide |
| `docs/SETUP_AND_RUN_GUIDE.md` | Detailed Korean setup guide |
| `docs/STAGE_STATUS.md` | LGT stage implementation status |
| `docs/QUANTUM_LGT_STAGE*.md` | Per-stage notes |
| `docs/LGT2_PRODUCTION_GUIDE.md` | Production LGT guide |
| `cobaya_f32/README_F32_12.md` | Cobaya Gate F32-12 instructions |
| `CHANGELOG.md` | Complete version history |

---

## 18. Suggested one-line positioning

If you need to describe this repository to another researcher, use:

> **Z-Sim is an executable validation layer for Z-Spin Cosmology: a theory-native forward simulator, structural falsification harness, Standard Model prediction engine, and custom lattice / closure testbed designed to bridge analytic derivations and standard inference pipelines.**
