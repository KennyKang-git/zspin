# QUANTUM LGT STAGE 13 - Broad preset vs lightweight direct comparison

## Goal
Stage-13 runs the Stage-12 closure-calibration pipeline twice:
- `default_broad` preset with the broader shape grid
- `lightweight` preset with the smaller fast grid

The result is a direct comparison ledger that keeps the selected background and the top control from each preset in one place.

## New outputs
- `stage13_preset_rows.csv`
- `stage13_comparison_rows.csv`
- `stage13_summary.json`

## Interpretation
This is still a preproduction surrogate. The purpose is not final Higgs closure. The purpose is to check whether the broader preset keeps the same sign/scheme choice and whether its selected background stays above its own sharpened controls while being compared directly to the lightweight-selected run.
