## v6.1 — Face Counting Ω_m Synchronization (2026-03-21)

**CRITICAL FIX:** Resolved internal inconsistency where CDM used face counting
(32/121) but total matter density still used slot counting (39/121).

- `constants.py`: OMEGA_M_BARE switched from 39/121 (slot) to 38/121 (face counting).
  OMEGA_M_EFF: 0.2984 → 0.2908. OMEGA_M_BARE_SLOT retained for historical reference.
- `cmb_evaluate.py`: S₈ display string updated (0.794 → ~0.777).
- `cobaya_scaffold.py`: All 39/121 references → 38/121 in config generation.
- `camb_compare.py`: Hardcoded OMEGA_M_EFF corrected (39→38).
- `parameter_classification.json`, `zspin_planck2018.yaml`: Config values updated.
- `test_v3_derived.py`: 6 assertions updated for face counting values.
- **CMB pipeline (ombh2/omch2) was already correct** — no changes needed there.
- **LGT/MBP pipeline:** No changes needed (no cosmological parameter dependency).
- **348/348 tests PASS** (321 on clean install; 27 stage-fixture tests require prior outputs).

Physics impact:
  - S₈ vs DES Y3: +1.06σ → +0.06σ (near-perfect agreement)
  - Ω_m^eff vs DESI: 0.11σ → 0.78σ (still well within 3σ)
  - Ω_m discrepancy (geometry vs Planck MCMC): 0.96σ → 0.16σ

## v5.3 Stage-22 — Recompute-Enabled Bridge

- Added `zsim/lgt/stage22.py` and `zsim/apps/su2_mbp_stage22_recompute_bridge_validate.py`.
- Reconnected the Stage-21 default-live bridge ledger to the broadened Stage-13 rerun snapshot.
- Added Stage-22 tests, documentation, and bundled example outputs.

## v5.2 / Stage-21

- Added `zsim.lgt.stage21` broader default-live bridge ledger.
- Added `zsim.apps.su2_mbp_stage21_default_live_validate`.
- Added Stage-21 tests, docs, and bundled example outputs.

## v5.1 Stage-20
- Added Stage-20 live sweep expansion ledger (`zsim.lgt.stage20`) and validation CLI.
- Connected broadened live Stage-13 reruns to the Stage-19 recompute-aware ledger and Stage-18 hybrid reference.

# Changelog

## v5.0 / Stage-19
- Added recompute-aware control-family sweep ledger, CLI, tests, and example outputs.

v4.8 Stage-17
- Added snapshot-connected live stress ledger (`zsim.lgt.stage17`).
- Added Stage-17 validation CLI and tests.

## v4.7 — Stage-16 Live Recompute
- Added `zsim.lgt.stage16` for the first lightweight live broad-grid recompute path.
- Added `su2_mbp_stage16_live_recompute_validate` CLI and example outputs.
- Added Stage-16 notes/tests/addendum scaffolding.


## v4.2 Stage-11

- Added `zsim.lgt.stage11` stress-ledger pipeline.
- Added `su2_mbp_stage11_stress_validate` CLI and CSV/JSON outputs.
- Added broader larger-shape grid, sign-kernel stress diagnostics, and closure-ledger stress comparison against sharpened controls.

## v4.0 Stage-9
- Added shape-aware stage-9 harness over multiple BCC shapes.
- Added extended overlap sign family: arctan and pade11.
- Added sharpened negative controls: edge-permuted and conjugation-scrambled caloron surrogates.
- Added stage-9 CLI, docs, tests, and example outputs.

## v3.9 Stage-8
- Added sign-function comparison harness (smooth/tanh/rational).
- Added overlap-to-MBP ledger bridge and Stage-8 CLI.

# Z-Sim Changelog

## v6.0.0 — Production Lattice Gauge Theory Architecture

**Architecture rebuild of the LGT layer. 348/348 tests pass.**

### New: `zsim/lgt2/` package (9 modules)

1. **Periodic BCC T³** (`lattice.py`): Replaces open-boundary BCC with periodic
   boundary conditions on T³ torus. Translation-invariant, no boundary artifacts.

2. **Wilson gradient flow** (`gradient_flow.py`): Lüscher 3rd-order Runge-Kutta
   ODE integrator replacing discrete cooling. Continuous flow time t.

3. **Overlap Dirac operator** (`dirac_overlap.py`): Neuberger overlap operator
   satisfying exact Ginsparg-Wilson relation. GW residual ~10⁻¹⁴.
   Index theorem: n₊ − n₋ = Q_top (exact).

4. **Lattice spacing & continuum extrapolation** (`continuum.py`): Explicit
   lattice spacing a(β), multi-β weighted least-squares fit to O(a²) artifacts.

5. **Caloron/BPS backgrounds** (`caloron.py`): I-Ī molecular instanton
   backgrounds with BPS monopole profiles. Net ν=0 for MBP protocol.

6. **MBP v2 pipeline** (`mbp2.py`): Full 5-phase MBP protocol (ZS-S4 §6.11.4)
   with all 5 falsification gates (F-MBP-1 through F-MBP-5).

7. **SU(2) Lie algebra** (`su2.py`): exp/log maps, traceless anti-Hermitian
   projection, geodesic distance.

8. **Gauge field** (`gauge_field.py`): Wilson plaquette action, staple sums,
   topological charge estimator on periodic BCC.

9. **Wilson-Dirac** (`dirac_wilson.py`): Corrected Wilson fermion operator
   with proper γ₅-Hermiticity.

### Critical fix

The Wilson hopping term in v5.x contained `1j * gamma_dir` which broke
γ₅-Hermiticity of D_W. This caused the shape-dependent consistency gap
divergence (4×4×4: 0.003 → 8×10×4: 0.181). Fixed to `gamma_dir` (no `i`).

### Backward compatibility

All v5.7 modules (cosmology, quantum topology, reduced LGT, Stage 4-26)
preserved and passing (306/306 tests).

### Version metadata fix

- `pyproject.toml` version: 3.7.0 → 6.0.0
- `zsim/__init__.py` version: 4.0.0 → 6.0.0
- Authors field corrected

## v3.7.0 — Chiral / Caloron Stage-4 (2026-03-20)

### Added
- `zsim.lgt.chirality`: bipartite BCC chirality signs, reduced `gamma5`, left/right/vector projectors
- `zsim.lgt.backgrounds`: caloron-pair surrogate and scrambled-caloron negative control
- `zsim.lgt.controls`: standardized negative-control runner for stage-4 MBP checks
- `zsim.apps.su2_mbp_stage4_validate`: chiral/caloron validation CLI with gates + summary JSON/CSV
- `docs/QUANTUM_LGT_STAGE4.md`: stage-4 notes and scope boundary

### Changed
- `zsim.lgt.mbp` now accepts `chirality_mode` while preserving Stage-3 defaults
- Stage-4 bundled example output added under `outputs/su2_mbp_stage4_example`

### Validation
- Full regression: **249 / 249 tests PASS**
- Stage-4 gates on bundled example: `G-CONSISTENCY`, `G-CHIRAL-SPLIT`, `G-CONTROL-SEPARATION` all PASS
- Status remains **preproduction-surrogate** (not a continuum caloron / production lattice result)

## v3.1.0 — Semantic Closure (2026-03-18)

Addresses 7 specific feedback items to achieve "single source of truth" status.

### Fix #1: quickstart defaults to DERIVED closures
- `scripts/quickstart.py` now uses `configs/derived.yaml` (not `quickstart.yaml`)
- Paper 45 "zero-free-parameter" message and code UX are now aligned

### Fix #2: run_derived.py fully rewritten
- All 6 broken imports replaced with v3.1 API
- Removed `/home/claude` hardcoded path
- Removed frozen-dataclass mutation (uses `from_yaml` instead)
- Uses `zsim.io.persist_integrated_run` (proven pipeline)
- New integration test: `test_run_derived.py` (3 tests)

### Fix #3: version strings unified to v3.1
- README: `# Z-Sim v3.1`
- All 49 module docstrings: `v0.1`/`v2.x` → `v3.1`
- pyproject.toml: `version = "3.1.0"`

### Fix #4: constants.py 3-tier separation
- **Tier 0 (Locked Structural):** A, dims, delta_X, delta_Y, z*, lambda
- **Tier 1 (Exact Derived):** G_eff, H0_ratio, OMEGA_M_BARE, OMEGA_M_EFF
- **Tier 2 (Benchmark Predictions):** BENCH_NS_60, BENCH_R_TENSOR, PLANCK_*
- **OMEGA_M_EFF fixed:** was 39/121=0.3223 (bare), now 39/(121(1+A))=0.2984 (effective)
- Added OMEGA_M_BARE for the raw structural fraction
- Backward compatibility aliases preserved (N_S_60, R_TENSOR, OMEGA_B)

### Fix #5: inflation canonical runner stabilized
- Replaced finite-difference derivatives with **fully analytical** d/deps, d^2/deps^2, dK/deps
- Replaced manual bisection with `scipy.optimize.brentq` (guaranteed convergence)
- n_s monotonicity: **0 violations** across N*=45–74 (was 15 violations in v3.0)
- N*=60: n_s=0.9674, r=0.0089 — matches book Chapter 9 table exactly
- New regression tests: monotonicity, book-value match

### Fix #6: phase_gate_derivation.py SU(2) bug
- `sigma_z` → `sigma_y` in Wigner d-matrix verification
- σ_z rotation is diagonal → |U[1,0]|²=0 always (wrong)
- σ_y rotation gives correct |d^{1/2}_{-,+}(φ)|²=sin²(φ/2)
- All 13 verification checks now pass (was 3/13)

### Fix #7: HSI/i-tetration scope documented
- X_STAR, Z_STAR_MOD_SQ correctly scoped as Tier 0 constant supply
- Not yet integrated into runtime kernel dynamics (deferred to future version)
- Documented as intentional scope boundary, not missing feature

### Test Suite
- 202 tests total (was 190): 190 preserved + 12 new
- New: `test_run_derived.py` (3), monotonicity (2), book-match (2), tier system (5)

---

## v3.0.0 — Unified Release (2026-03-18)

[Previous changelog preserved below]
...

## v3.7.0
- Added near-zero pairing analysis and stage-6 valley ranking harness.
- Added multi-scheme reduced/staggered/Wilson comparison runner.
- Added stage-6 controls, docs, and tests.


## v3.8 Stage-7
- overlap-aware valley family scan
- Wilson-weighted comparison harness
- phase-scrambled negative control


## v4.1 Stage-10
- Added stage10 direct-comparison harness with larger-shape Wilson weighting and tighter sign calibration.

## v4.3 - Stage 12 closure-calibration report
- re-expanded larger-shape coverage with normalized support ranking
- added stage-12 calibration ledger and CLI
- added stage-12 tests and notes

## v4.4 Stage-13
- Added `zsim.lgt.stage13` broad-vs-lightweight preset comparison ledger.
- Added `zsim.apps.su2_mbp_stage13_broad_compare_validate`.
- Added Stage-13 tests, docs, and example output bundle.

## v4.6 - Stage 15 recompute-aware harness
- Added stage15 recompute-aware orchestration layer that reconnects the stage-14 preset sweep to the recorded stage-13 broad-grid execution snapshot.
- Added `su2_mbp_stage15_recompute_validate` CLI and stage15 CSV/JSON outputs.
- Added bridge-ledger diagnostics and tests for sign/scheme/shape stability versus the broad-grid reference.


## v5.4 Stage-23
- Added `zsim.lgt.stage23` hybrid recompute ledger.
- Added `su2_mbp_stage23_hybrid_recompute_validate` CLI.
- Added Stage-23 tests, docs, and example outputs.

## v5.5 — Stage 24 live-hybrid sweep
- Added `zsim.lgt.stage24` live-hybrid sweep ledger.
- Added `su2_mbp_stage24_live_hybrid_validate` CLI.
- Added Stage-24 tests, docs, and example outputs.
## v5.6 — Stage-25 heavier live-hybrid sweep
- Added stage25 heavier live-hybrid sweep ledger and validation CLI.


## v5.7

- Added Stage-26 shape-adaptive MBP winner ledger.
- Fixed recommendation path uses `wilson4`, `left`, `wilson_r=0.5` for larger-shape reruns.
- Added adaptive `(chirality, wilson_r)` fallback ledger and Stage-25 reference integration.
