# Quantum LGT Stage-22 — Recompute-Enabled Bridge

## Goal
Stage-22 reconnects the Stage-21 default-live bridge ledger to a broadened Stage-13
rerun snapshot. The intent is to compare the stable Stage-21 bridge winner against a
broader recompute candidate without pretending that the package is already a full
production lattice execution.

## Added files
- `zsim/lgt/stage22.py`
- `zsim/apps/su2_mbp_stage22_recompute_bridge_validate.py`
- `tests/test_lgt_stage22.py`
- `tests/test_lgt_stage22_app.py`

## Outputs
- `stage22_recompute_rows.csv`
- `stage22_control_rows.csv`
- `stage22_summary.json`

## Honest scope
Stage-22 is still a **preproduction surrogate**. It is a bridge/orchestration layer on
top of the existing reduced SU(2) lattice machinery. It does **not** claim exact
continuum calorons, a production overlap lattice run, or final Higgs bilinear closure.
