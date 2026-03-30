# Z-Sim v1.0 — Stage Status

## Core Cosmology Pipeline (Stages 1–22)

All implemented and stable since v3.0.

| Stage | Module | Description |
|---|---|---|
| 1 | — | Repository scaffold |
| 2 | `core/config.py` | Typed base configuration |
| 3 | `core/constants.py` | Locked constants (A=35/437) and epistemic labels |
| 4 | `core/state.py` | Canonical state model |
| 5 | `core/config.py` | Config loading and validation |
| 6 | `kernel/phase.py` | Phase kernel |
| 7 | `kernel/mediation.py` | Mediation kernel |
| 8 | `kernel/background.py` | Background kernel |
| 9 | `kernel/epsilon.py` | Epsilon kernel |
| 10 | `solver/rhs.py` | RHS assembly |
| 11 | `solver/integrator.py` | Segmented integrator |
| 12 | `validation/kill_switches.py` | Validation and kill-switch layer |
| 13 | `observables/` | Observables compiler |
| 14 | `apps/run_background.py` | Background CLI |
| 15 | — | Smoke pipeline |
| 16 | `apps/compare_baselines.py` | Baseline comparison harness |
| 17 | `apps/run_scan.py` | Scan harness |
| 18 | — | Starter pack cleanup and quickstart assets |
| 19 | `apps/report_results.py` | Report generation CLI |
| 20 | `io/pipeline.py`, `apps/common.py` | Shared run-artifact pipeline |
| 21 | — | (reserved) |
| 22 | `apps/run_closure_matrix.py` | Closure experiment matrix |

Test count at Stage 22: 190 tests.

---

## Reduced SU(2) Lattice Experiments (Stages 4–26, `zsim/lgt/`)

Surrogate lattice experiments for MBP sign/bilinear verification.
**Status: preproduction surrogate** — superseded by `zsim/lgt2/` for physics conclusions.

| Stage | Module | Description |
|---|---|---|
| 4 | `lgt/chirality.py`, `lgt/backgrounds.py` | Chiral/caloron Stage-4 validation |
| 5 | `lgt/spinor.py` | Spinor validation |
| 6 | `lgt/pairing.py`, `lgt/stage6.py` | Pairing-aware valley ranking |
| 7 | `lgt/overlap.py`, `lgt/stage7.py` | Overlap-aware valley family scan |
| 8 | `lgt/stage8.py` | Sign-function comparison + MBP ledger bridge |
| 9 | `lgt/stage9.py` | Shape-aware multi-BCC harness |
| 10 | `lgt/stage10.py` | Direct comparison with larger shapes |
| 11 | `lgt/stage11.py` | Stress-ledger pipeline |
| 12 | `lgt/stage12.py` | Closure-calibration report |
| 13 | `lgt/stage13.py` | Broad-vs-lightweight preset comparison |
| 14 | `lgt/stage14.py` | Preset sweep |
| 15 | `lgt/stage15.py` | Recompute-aware orchestration |
| 16 | `lgt/stage16.py` | Live recompute path |
| 17 | `lgt/stage17.py` | Snapshot-connected live stress ledger |
| 18 | `lgt/stage18.py` | Hybrid live stress ledger |
| 19 | `lgt/stage19.py` | Recompute-aware control sweep |
| 20 | `lgt/stage20.py` | Live sweep expansion |
| 21 | `lgt/stage21.py` | Default-live bridge ledger |
| 22 | `lgt/stage22.py` | Recompute-enabled bridge |
| 23 | `lgt/stage23.py` | Hybrid recompute ledger |
| 24 | `lgt/stage24.py` | Live-hybrid sweep |
| 25 | `lgt/stage25.py` | Heavier live-hybrid sweep |
| 26 | `lgt/stage26.py` | Shape-adaptive MBP winner ledger |

Recommendation from Stage-26: `left` chirality, `wilson_r=0.5`, with adaptive fallback.

---

## Production LGT (`zsim/lgt2/`, v6.0+)

Production-quality lattice gauge theory package. 9 modules.

| Module | v5.x → v6.0+ improvement |
|---|---|
| `lattice.py` | Open boundary BCC → Periodic BCC T³ (torus) |
| `gradient_flow.py` | Discrete cooling → Wilson gradient flow (Lüscher RK3) |
| `dirac_overlap.py` | Wilson fermion → Overlap Dirac (exact GW relation) |
| `dirac_wilson.py` | Corrected γ₅-Hermiticity (`1j` bug fixed) |
| `continuum.py` | No lattice spacing → Explicit a, O(a²) extrapolation |
| `caloron.py` | Cooled random → BPS monopole / I-Ī caloron |
| `mbp2.py` | — → Full 5-phase MBP protocol (5 falsification gates) |
| `gauge_field.py` | — → Wilson plaquette, staples, topological charge |
| `su2.py` | — → SU(2) exp/log, projection, geodesic |

See `docs/LGT2_PRODUCTION_GUIDE.md` for detailed usage.

---

## v1.0 Changes

**Face Counting Ω_m Synchronization:**
- `constants.py`: OMEGA_M_BARE 39/121 → 38/121 (face counting)
- `constants.py`: OMEGA_M_EFF 0.2984 → 0.2908
- `cmb_evaluate.py`: S₈ display 0.794 → ~0.777
- `cobaya_scaffold.py`: All 39/121 → 38/121
- `camb_compare.py`: Hardcoded OMEGA_M_EFF corrected
- CMB pipeline (ombh2/omch2): No changes needed (already correct)
- LGT/MBP pipeline: No changes needed (no cosmological dependency)

Physics impact: S₈ vs DES Y3 improved from +1.06σ to +0.06σ.

---

## Test Suite Summary

| Category | Files | Tests | Status |
|---|---|---|---|
| Core cosmology | 18 | ~170 | ✓ All PASS |
| Quantum topology | 2 | ~10 | ✓ All PASS |
| LGT2 production | 1 | 42 | ✓ All PASS |
| LGT surrogate (standalone) | 28 | ~50 | ✓ All PASS |
| LGT surrogate (fixture-dependent) | 27 | 26 | ⚠ Require prior stage outputs |
| **Total** | **76** | **348** | **322 PASS on clean install** |

---

## Pending Gates

| Gate | Description | Status |
|---|---|---|
| **F32-12** | Full Planck MCMC (plik + lowl + lensing) | **PENDING** (highest priority) |
| MBP N≥8 | Production lattice → κ² → v = 246 GeV | PENDING |
| 32/121 derivation | Face counting CDM from ZS-F2 truncated icosahedron | PENDING |
| S₈ reassessment | New Ω_m=0.314 implications for framework scorecard | PENDING |
| A_s, τ derivation | From A=35/437 for true zero-free-parameter CMB | PENDING |
