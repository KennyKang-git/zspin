# Z-Sim v1.0 — Production LGT2 Guide

This guide covers the `zsim/lgt2/` production lattice gauge theory package
in detail, including the full MBP v2 protocol, continuum extrapolation,
and recommended experimental sequences.

For quick-start examples, see `README.md` §4.

---

## 1. Architecture Overview

The `lgt2/` package implements the 5-phase MBP protocol (ZS-S4 §6.11.4)
with production-quality lattice infrastructure:

| Module | Description |
|---|---|
| `lattice.py` | Periodic BCC T³ lattice (torus topology, no boundary artifacts) |
| `gauge_field.py` | SU(2) Wilson plaquette action, staple sums, topological charge |
| `gradient_flow.py` | Wilson gradient flow via Lüscher 3rd-order Runge-Kutta ODE |
| `dirac_wilson.py` | Wilson fermion with correct γ₅-Hermiticity (`r ∓ γ·n̂`) |
| `dirac_overlap.py` | Neuberger overlap operator (exact Ginsparg-Wilson relation) |
| `caloron.py` | I-Ī molecular instanton / BPS monopole backgrounds |
| `continuum.py` | Multi-β O(a²) continuum extrapolation |
| `mbp2.py` | Full 5-phase MBP pipeline with 5 falsification gates |
| `su2.py` | SU(2) Lie algebra utilities (exp, log, projection, geodesic) |

### Critical fix from v5.x

The v5.x Wilson hopping term contained `1j * gamma_dir`, breaking γ₅-Hermiticity
of D_W. This was the root cause of shape-dependent consistency gap divergence
(4×4×4: 0.003 → 8×10×4: 0.181). v6.0+ uses `gamma_dir` directly. The
Ginsparg-Wilson residual is now verified at ~10⁻¹⁴.

---

## 2. The 5-Phase MBP Protocol

### Phase 1: Lattice Construction

Build a periodic BCC lattice on T³ (torus). Translation-invariant, no boundary
artifacts.

```python
from zsim.lgt2.lattice import build_periodic_bcc

lattice = build_periodic_bcc(Nx=4, Ny=4, Nz=4, a=1.0)
print(f"Sites: {lattice.num_sites}")          # 128
print(f"Edges: {lattice.num_edges}")           # 512
print(f"Plaquettes: {lattice.num_plaquettes}") # 768
```

### Phase 2: Gauge Smoothing (Wilson Gradient Flow)

Cool to the caloron constituent sector using continuous gradient flow.

```python
from zsim.lgt2.gauge_field import GaugeField, avg_plaquette
from zsim.lgt2.gradient_flow import WilsonGradientFlow

gf = GaugeField.random(lattice, beta=2.3, seed=42)
print(f"Initial <P>: {avg_plaquette(gf):.6f}")

flow = WilsonGradientFlow(epsilon=0.01, max_steps=200)
trajectory = flow.flow(gf, n_steps=100, record_every=10)

for step in trajectory:
    print(f"  t={step.flow_time:.3f}: <P>={step.avg_plaq:.6f}, "
          f"E={step.action_density:.6f}")
```

### Phase 3: Overlap Dirac Spectrum in I-Ī Background

Generate an I-Ī molecular instanton background and compute the overlap
Dirac spectrum.

```python
from zsim.lgt2.caloron import CaloronBackground
from zsim.lgt2.dirac_overlap import OverlapDirac

# I-Ī symmetric pair (net topological charge = 0)
cal = CaloronBackground.symmetric_pair(
    lattice,
    separation_fraction=0.4,  # instanton separation as fraction of box size
    rho_inst=0.5              # instanton size parameter
)
gf_cal = cal.generate(beta=2.3)

# Overlap Dirac operator (exact GW relation)
ov = OverlapDirac(gf_cal, rho=1.0, wilson_r=1.0)

# Verify Ginsparg-Wilson relation: {γ₅, D} = D γ₅ D
gw_res = ov.verify_ginsparg_wilson()
print(f"GW residual: {gw_res:.2e}")  # should be ~10⁻¹⁴

# Compute spectrum
spec = ov.spectrum()
print(f"Topological charge Q = {spec.topological_charge}")
print(f"Zero modes: {spec.zero_modes}")
print(f"Eigenvalues: {spec.eigenvalues[:6]}")
```

### Phase 4: h² Coefficient Extraction

Extract κ² from the fermion determinant ratio (handled internally by `mbp2.py`).

### Phase 5: MBP Formula Comparison

Compare extracted κ² with the Z-Spin target value 0.0906.

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

# Falsification gates
print(f"F-MBP-1 (bilinear exists):  {result.fmb1_bilinear_exists}")
print(f"F-MBP-2 (sign correct):     {result.fmb2_sign_correct}")
print(f"gamma_sign_match:            {result.gamma_sign_match}")
print(f"gamma_consistency_gap:       {result.gamma_consistency_gap:.6e}")
print(f"kappa2_extracted:            {result.kappa2_extracted:.6e}")
print(f"kappa2_target:               {result.kappa2_target}")
print(f"STATUS:                      {result.status}")
```

---

## 3. Output Field Reference

| Field | Meaning | Target |
|---|---|---|
| `gamma_sign_match` | Trace and FD methods agree on sign | True |
| `gamma_consistency_gap` | \|trace − fd\| | → 0 as L → ∞ |
| `ginsparg_wilson_residual` | GW relation violation | ~10⁻¹⁴ |
| `topological_charge` | Q = n₊ − n₋ (index theorem) | 0 for I-Ī |
| `mu2_formula_proxy` | N_c × MBP bracket | > 0 (EWSB) |
| `kappa2_extracted` | Extracted h² coefficient | 0.0906 |
| `gamma_h2_trace` | Raw Tr(γ₅ D) value | — |
| `fmb1_bilinear_exists` | F-MBP-1 gate | True |
| `fmb2_sign_correct` | F-MBP-2 gate (μ² > 0 → tachyonic) | True |
| `status` | Overall status | OBSERVATION |

---

## 4. Continuum Extrapolation

Physical results require extrapolation to a → 0.

```python
from zsim.lgt2.continuum import ContinuumExtrapolator, lattice_spacing_from_beta
from zsim.lgt2.mbp2 import run_mbp2_pipeline

ext = ContinuumExtrapolator()

for beta in [2.0, 2.3, 2.5, 2.7, 3.0]:
    a = lattice_spacing_from_beta(beta)
    for shape in [(4, 4, 4), (6, 6, 6)]:
        result = run_mbp2_pipeline(
            shape=shape, lattice_spacing=a, beta=beta,
            flow_steps=100, flow_epsilon=0.01,
            overlap_rho=1.0, wilson_r=1.0,
            chirality_mode="left",
        )
        ext.add_point(
            "gamma_h2_trace", beta, a, shape,
            result.gamma_h2_trace,
            abs(result.gamma_consistency_gap),
        )

# O(a²) weighted least-squares fit
continuum = ext.extrapolate("gamma_h2_trace")
print(f"Continuum limit: {continuum.continuum_value:.6e} ± {continuum.continuum_error:.2e}")
print(f"χ²/dof: {continuum.chi2_per_dof:.3f}")
print(f"Fit quality: {continuum.fit_quality}")
```

---

## 5. Recommended Experimental Sequence

### Phase A — Shape scaling (fixed β=2.3)

Goal: Confirm consistency gap converges to 0 as L → ∞.

```python
for shape in [(2,2,2), (3,3,3), (4,4,4), (5,5,5), (6,6,6), (8,8,8)]:
    result = run_mbp2_pipeline(shape=shape, flow_steps=100, flow_epsilon=0.01)
    print(f"{shape}: gap={result.gamma_consistency_gap:.4e}, "
          f"sign={result.gamma_sign_match}, κ²={result.kappa2_extracted:.4e}")
```

### Phase B — Multi-β continuum extrapolation

Goal: Remove lattice artifacts via a → 0 limit.

```python
for beta in [2.0, 2.3, 2.5, 2.7, 3.0]:
    for shape in [(4,4,4), (6,6,6)]:
        a = lattice_spacing_from_beta(beta)
        result = run_mbp2_pipeline(shape=shape, lattice_spacing=a, beta=beta,
                                    flow_steps=100, flow_epsilon=0.01)
```

### Phase C — Caloron parameter scan

Goal: Verify instanton-independence of the MBP result.

```python
for sep in [0.2, 0.3, 0.4, 0.5, 0.6]:
    for rho in [0.3, 0.5, 0.7, 1.0]:
        result = run_mbp2_pipeline(
            shape=(6,6,6), separation_fraction=sep, rho_inst=rho,
            flow_steps=100, flow_epsilon=0.01,
        )
```

### Phase D — Production campaign (target: closure or falsification)

Goal: N ≥ 8 lattices with multiple β values → continuum κ² → compare to 0.0906.

This is a computational campaign requiring significant CPU time. Use the HPC
scan script for parallelization:

```bash
python scripts/mbp2_hpc_scan.py --shapes 8,8,8 10,10,10 --betas 2.3 2.5 2.7 3.0 \
    --output-dir outputs/mbp2_production
```

---

## 6. Validated Physics Results (v6.0+)

### Small lattice convergence

| Observable | 2×2×2 | 3×3×3 | Trend |
|---|---|---|---|
| GW residual | 3.67×10⁻¹⁴ | 9.83×10⁻¹⁴ | Stable ~10⁻¹⁴ ✓ |
| Q (topological) | 0 | 0 | Correct for I-Ī ✓ |
| sign_match | True | True | Stable ✓ |
| consistency_gap | 4.690 | 0.044 | **×107 improvement** ✓ |
| F-MBP-1 | True | True | ✓ |
| F-MBP-2 | True | True | ✓ |

### Current status interpretation

- **v = 246 GeV remains NON-CLAIM** pending production lattice (N ≥ 8) computation.
- **κ² on research lattices** is far from target 0.0906 — this is expected; continuum
  extrapolation on larger lattices is needed.
- **The v5.x consistency gap divergence is resolved** — root cause (γ₅-Hermiticity
  breaking) is fixed, gap converges as expected.
- **Required molecular instanton action** S_mol ≈ 38.3 for v = 246 GeV given
  C_M = 92/(16π²).

---

## 7. Surrogate LGT (zsim/lgt/)

The `zsim/lgt/` package contains the Stage 4–26 surrogate lattice experiments
that preceded the production `lgt2/` architecture. These are preserved for
backward compatibility and development history but should NOT be used for
physics conclusions.

Key difference: `lgt/` uses open boundaries, discrete cooling, and Wilson
fermions (broken γ₅-Hermiticity in some stages). `lgt2/` uses periodic T³,
gradient flow, and overlap Dirac.

See `docs/stages/QUANTUM_LGT_STAGE*.md` for per-stage development notes.
