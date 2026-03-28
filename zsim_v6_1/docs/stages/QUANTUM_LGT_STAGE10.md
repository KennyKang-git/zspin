# QUANTUM_LGT_STAGE10

Stage-10 extends the Stage-9 shape-aware harness with three tighter checks:

1. larger-shape Wilson weighting,
2. explicit sign-family calibration,
3. direct comparison between the overlap-selected background and the sharpened control family.

## What is new

- A calibrated shape score is used when selecting the current best background.
- The sign family is still scanned over `smooth`, `tanh`, `rational`, `arctan`, and `pade11`, but the chosen method now receives an explicit calibration factor based on relative stability.
- A direct comparison ledger is written for the selected background and all sharpened controls on the selected shape.

## Main files

- `zsim/lgt/stage10.py`
- `zsim/apps/su2_mbp_stage10_compare_validate.py`
- `tests/test_lgt_stage10.py`
- `tests/test_lgt_stage10_app.py`

## Outputs

- `stage10_shape_rows.csv`
- `stage10_comparison_rows.csv`
- `stage10_summary.json`

## Non-claim boundary

Stage-10 remains a preproduction surrogate layer. It does not claim:

- an exact continuum caloron,
- a production overlap implementation on a large BCC lattice,
- final Higgs bilinear closure.
