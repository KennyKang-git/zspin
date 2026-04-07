## v8.0 — April 2026 Update: §9.5 Lepton Channel + ZS-S7 + F-S2-IO3 Closure (2026-04-07)

**MAJOR FEATURE:** Three coordinated paper releases integrated into Z-Sim:
ZS-S7 (55-paper release), ZS-M11 §9.5 (Singlet ν_R Yukawa Vanishing,
Lepton-Channel Character Lift, ρ₂-Sector Golden-Ratio Spectral Quantization),
and ZS-S2 §8.1 F-S2-IO3 closure (OPEN → DERIVED at LO within the same
April 2026 release cycle in which it was posed).

### New: `zsim/sm/qcd_spectral.py` module (ZS-S7)

Unified pipeline parallel to `zsim/sm/report.py`. Four predictions:

1. **Λ_QCD = v · A / (λ_1 · V_Y) ≈ 264 MeV** [DERIVED-CONDITIONAL]
   - Conditional on λ_1(Δ_2 on TI) = 1.2428 (PROVEN in ZS-S7 §3).
   - Lattice reference: 260 ± 20 MeV (FLAG 2024). Pull: +0.21σ.
2. **m(0⁺⁺) = v · A / Q ≈ 1.791 GeV** [DERIVED-CONDITIONAL]
   - Topological Cancellation Theorem (ZS-S7 §5).
   - Lattice reference: 1.73 ± 0.05 GeV. Pull: +1.21σ.
3. **b_0(SU(3)) = (V+F)_Y / G_MUB = 23/3** [PROVEN, exact]
   - Structurally identical to existing `BETA_COEFF_SU3_FRAC`.
4. **n_f = V_Y / G_MUB = 5** [DERIVED, exact]

NON-CLAIM disclaimer (ZS-S7 §7): does not solve the Yang-Mills mass gap
Millennium Prize problem; result is a polyhedral-invariant calculation,
not a continuum field-theoretic proof for arbitrary SU(N).

### Extended: `zsim/sm/icosahedral.py` (§9.5 lepton-channel helpers)

Four new pure functions:

- **`singlet_yukawa_vanishing()`** — verifies dim Hom_I(1, 3⊗5⊗X) = (0,1,1,1,1)
  by character orthogonality on A₅. [PROVEN, ZS-M11 §9.5.4 paper-T25]
- **`lepton_character_lift()`** — verifies dim V₊ = 23, dim V₋ = 22 on
  V = 3⊗5⊗3' under any 2-fold σ ∈ I, with L: ρ₂⊗ρ₁⊗ρ₂ ⊂ V₊ by
  reflection parity (−1)·(+1)·(−1) = +1. [PROVEN, ZS-M11 §9.5.5 paper-T26]
- **`truncated_icosahedron_vertices()`** — 60-vertex TI from golden-ratio coords.
- **`truncated_icosahedron_laplacian()`** — graph Laplacian L_Y = D - A on TI
  (90 edges, 3-regular).
- **`tilattice_rho2_spectrum()`** — verifies ρ₂-sector spectrum contains
  {4-φ, 5-φ, 3+φ, 4+φ} with Fiedler eigenvalue matching ZS-M8 §4.2 reference
  0.243402 exactly. [COMPUTED, ZS-M11 §9.5.6 paper-T27]

### New constants in `zsim/core/constants.py`

- **`EPSILON_LEPTON_LO`** = `KAPPA_SQ` = 35/4807 ≈ 0.007281
  - Y-side reciprocal duality alias for the X-side `KAPPA_SQ` already in
    use for `ALPHA_EM_NLO`. The single Block Fiedler eigenvalue λ_2 = 2A/Q
    (PROVEN, ZS-T1 §9.3) manifests as both 1/α_EM ≈ Q/A (X-side, T1-2,
    propagator scale 1/κ²) and ε_solar ≈ A/Q (Y-side, T1-3, vertex
    coupling scale κ²). Compare to NuFIT 6.0 IO Δm²₂₁: residual +1.6%.
  - [STATUS: DERIVED at LO, conditional on ZS-M9 v1.0 Table 2 ν_R ↔ I-1]
- **`LAMBDA1_HODGE_TI`** = 1.2428 (ZS-S7 §3 PROVEN spectral input)
- **`LAMBDA_QCD_PRED_GEV`** / **`LAMBDA_QCD_PRED_MEV`** = 264.15 MeV
- **`GLUEBALL_0PP_PRED_GEV`** = 1.7906 GeV
- **`BETA0_QCD_FRAC`** = 23/3 (alias for `BETA_COEFF_SU3_FRAC`)
- **`N_FLAVORS_QCD`** = 5

Five new structural sanity assertions in constants.py (Λ_QCD ± 5 MeV,
m(0⁺⁺) ± 0.01 GeV, b_0 == 23/3, n_f == 5, EPSILON_LEPTON_LO == KAPPA_SQ).

### New: 9 tests in `tests/test_sm_predictions.py`

Two new test classes:

**`TestM11LeptonChannel`** (4 tests):
- `test_singlet_yukawa_vanishing` — ZS-M11 §9.5.4 paper-T25
- `test_lepton_character_lift` — ZS-M11 §9.5.5 paper-T26
- `test_TI_golden_ratio_quantization` — ZS-M11 §9.5.6 paper-T27
- `test_epsilon_lepton_LO` — F-S2-IO3 closure (paper-T33), with
  anti-numerology cross-check against A² alternative (~10× worse)

**`TestS7QCDSpectral`** (5 tests):
- `test_lambda_qcd_pred` — Λ_QCD ≈ 264 MeV, +0.21σ vs FLAG 2024
- `test_glueball_0pp_mass` — m(0⁺⁺) ≈ 1.791 GeV, +1.21σ vs lattice
- `test_qcd_b0` — b_0 = 23/3 [PROVEN]
- `test_qcd_n_flavors` — n_f = 5 [DERIVED]
- `test_zs_s7_full_pipeline` — INTEGRATION (all 4 within 2σ)

### Cross-link updates

- `zsim/sm/m0_lattice.py` docstring extended to cite ZS-T1 v1.0 §9.3
  Block Fiedler Mediation Theorem as upstream PROVEN structural input,
  and the Y-side T1-3 reciprocal-duality face (ZS-M11 §9.5.5–9.5.6,
  ZS-S2 §8.1 F-S2-IO3 closure).
- `zsim/sm/__init__.py` updated to list `qcd_spectral` and `m0_lattice`
  modules and the April 2026 update event log.

### Backward compatibility

- All existing tests pass with zero regressions: 64/64 in
  `test_sm_predictions.py` (was 55/55, +9 new tests).
- Total `tests/` collection: 412 collected, 386 pass, 26 expected
  stage-fixture failures (LGT stage14–stage26 pipelines requiring
  prior outputs — unchanged from baseline).
- All v1.0 cosmology, LGT, and quantum topology modules unchanged.
- CMB pipeline (Cobaya, face counting) unaffected.

### Physics summary (April 2026 additions)

| Observable                 | Z-Spin           | Observed         | Pull/Dev | Status              |
|----------------------------|------------------|------------------|----------|---------------------|
| Λ_QCD                      | 264.15 MeV       | 260 ± 20 MeV     | +0.21σ   | DERIVED-CONDITIONAL |
| m(0⁺⁺) glueball            | 1.7906 GeV       | 1.73 ± 0.05 GeV  | +1.21σ   | DERIVED-CONDITIONAL |
| b_0(SU(3))                 | 23/3             | 23/3             | exact    | PROVEN              |
| n_f                        | 5                | 5                | exact    | DERIVED             |
| ε_lepton(LO) (F-S2-IO3)    | 35/4807 ≈ 7.28e-3| 7.4e-3 (NuFIT 6) | +1.6%    | DERIVED at LO       |
| dim Hom_I(1, 3⊗5⊗1)        | 0                | (singlet vanish) | exact    | PROVEN              |
| (dim V₊, dim V₋) on 3⊗5⊗3' | (23, 22)         | sum = 45         | exact    | PROVEN              |
| TI Fiedler eigenvalue      | 0.243402         | (ZS-M8 §4.2)     | exact    | COMPUTED            |

### Cross-paper synchronization

This update is part of the April 2026 coordinated three-document batch
(ZS-M11, ZS-S2, Book) plus the ZS-S7 55-paper release. External label
remains v1.0 for all source papers (no version bump). Zero new free
parameters; A = 35/437 remains the sole geometric input.

---

## v7.0 — Standard Model Predictions from Polyhedral Geometry (2026-03-30)

**MAJOR FEATURE:** Complete Standard Model prediction module derived from A = 35/437.
Zero free parameters. All results from polyhedral geometry + i-tetration fixed point.

### New: `zsim/sm/` package (6 modules)

1. **`gauge_couplings.py`** — α_s = 11/93 (+0.31σ), sin²θ_W = (48/91)·x* (−1.26σ),
   α₂ = 3/95, β-function coefficients a₂ = 19/6, a₃ = 23/3, 1/α_EM = 137.036 (1.07 ppm).
   Adversarial Archimedean test: 0/6 alternative solids match. Derivation chain audit.

2. **`ewsb.py`** — Higgs VEV = 245.93 GeV (0.12% from 246.22, DERIVED via Factorized
   Determinant Theorem). Top quark mass m_t = 171.5 GeV (TESTABLE, FCC-ee ~2040).
   Spectral-Topological Duality documented.

3. **`icosahedral.py`** — Full A₅ ≅ I representation engine. 60 rotations generated,
   5 conjugacy classes [1,12,12,15,20], character table verified. Three irreps constructed:
   3 (natural), 5 (traceless Sym²(ℝ³), correct homomorphism convention per ZS-M11 §2.1),
   3' (vertex permutation, Frobenius reciprocity). Homomorphism error: 7.77×10⁻¹⁶.
   Yukawa tensor T ∈ 3⊗5⊗3' computed; dim Hom_I(1, 3⊗5⊗3') = 1 (PROVEN, unique).

4. **`yukawa.py`** — D₅ channel decomposition (Σfractions = 1.000, Schur conservation).
   S⁴ VEV optimization: σ₁/σ₂ = 17.00 (mτ/mμ, 1.1%), σ₁/σ₃ = 3477 (mτ/me, 0.0%).
   Schur sum Σσ² = 0.2000 = 1/5 for ALL VEV directions (PROVEN).
   CKM: Cabibbo = arctan(1/φ³) = 13.28° (observed 13.04°, 1.9%).
   V_ub = r_A4 × V_us × V_cb with r_A4 = 0.292.

5. **`report.py`** — Unified SM prediction pipeline. Pull table with PDG 2024 / CODATA.
   End-to-end in ~15s. 7/7 predictions within 3σ.

6. **`__init__.py`** — Package metadata, v7.0.0.

### Modified: `zsim/core/constants.py`

- **Tier 0 additions:** Archimedean solid invariants (V_TO, E_TO, F_TO, V_TI, E_TI, F_TI),
  symmetry group orders (|O_h|=48, |I|=60, |I_h|=120), β₀(Z) = 1.
- **Tier 1d (NEW):** SM gauge couplings — ALPHA_S = 11/93, SIN2_THETA_W, R_GEOM = 48/91,
  ALPHA_2 = 3/95, β-coefficients, KAPPA_SQ = A/Q, C4_NLO = 4/13, ALPHA_EM_INV_NLO.
- **Tier 1e (NEW):** EWSB — D_EFF = 9, GAMMA_CW = 38/9, C_M_SPECTRAL, HIGGS_VEV = 245.93 GeV,
  TOP_MASS_PRED = 171.5 GeV, HIGGS_MASS_HYPO.
- **Tier 1f (NEW):** Neutrino — M_D_NEUTRINO_KEV, M_R_HNL_GEV, THETA_SQ_SEESAW, ETA_B_EXACT.
- **Tier 2 additions:** PDG 2024 reference values for all SM parameters.

### New: `tests/test_sm_predictions.py`

42 automated tests across 7 categories: Polyhedral Invariants (10), Gauge Couplings (11),
EWSB (6), Icosahedral Group (7), Fermion Mass (3), CKM (1), Neutrino (3), Integration (1).

### Backward compatibility

- All existing cosmology, LGT, and quantum topology modules unchanged.
- 77 pre-existing tests pass with zero regressions.
- CMB pipeline (Cobaya, face counting) unaffected.

### Physics summary

| Observable          | Z-Spin          | Observed       | Pull/Dev | Status          |
|---------------------|-----------------|----------------|----------|-----------------|
| α_s(M_Z)           | 11/93 = 0.1183  | 0.1180 ± 0.0009| +0.31σ   | DERIVED         |
| sin²θ_W(M_Z)       | (48/91)·x*      | 0.23122±3e-5   | −1.26σ   | DERIVED         |
| 1/α_EM              | 137.036         | 137.036        | 1.07 ppm | HYPOTHESIS (s)  |
| v (Higgs VEV)       | 245.93 GeV      | 246.22 GeV     | 0.12%    | DERIVED         |
| m_t (top quark)     | 171.5 GeV       | 172.57±0.29    | −3.69σ   | TESTABLE        |
| σ₁/σ₂ (mτ/mμ)      | 17.00           | 16.82          | 1.1%     | DERIVED         |
| σ₁/σ₃ (mτ/me)      | 3477            | 3477           | 0.0%     | DERIVED         |
| Cabibbo angle       | 13.28°          | 13.04°         | 1.9%     | OBSERVATION     |

### Open items

- Cabibbo angle: 5-dim rep principal angle (63.43° = arccos(1/√5)) vs geometric
  arctan(1/φ³) = 13.28°. Full D₅×A₄ cross-structure derivation needed for ZS-M11's 13.96°.
- Quartic invariant P₄: proper I-invariant quartic (not Σvᵢ⁴) needed for Spearman ρ = −0.928.
- Gate F32-12 (Cobaya full Planck MCMC) remains highest priority.

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
