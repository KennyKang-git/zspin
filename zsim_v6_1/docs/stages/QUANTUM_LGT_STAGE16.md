# QUANTUM_LGT_STAGE16

## Scope

Stage-16 adds the first **live recompute path** on top of the recorded Stage-15 bridge.
Instead of only reconnecting saved broad-grid snapshots, this stage runs a fresh Stage-13 broad-vs-lightweight comparison and places the live result in one ledger with the recorded Stage-15 winner.

## New modules

- `zsim.lgt.stage16`
- `zsim.apps.su2_mbp_stage16_live_recompute_validate`

## Outputs

- `stage16_live_rows.csv`
- `stage16_summary.json`

## Interpretation

This stage is still a **preproduction surrogate**.
It does **not** claim:
- exact continuum caloron,
- production overlap lattice,
- final Higgs bilinear closure.

What it does claim is narrower:
- a fresh live broad-grid recompute can be run,
- the live default-broad winner and the recorded Stage-15 winner can be compared in one bridge ledger,
- the selected live background should still outrank the matching live control in the lightweight validation path.
