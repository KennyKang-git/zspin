# QUANTUM_LGT_STAGE26

Stage-26 adds a shape-adaptive MBP ledger on top of the Stage-25 live-hybrid validation path.

## Purpose

The fixed recommendation identified in the Wilson-r / chirality sweep studies is:

- fermion scheme: `wilson4`
- chirality: `left`
- Wilson parameter: `r = 0.5`

Stage-26 uses that tuple as the default recommendation for larger-shape reruns, but it also constructs a shape-adaptive winner ledger to detect when the recommended tuple stops being the best consistency corner.

## New outputs

- `stage26_shape_rows.csv`
- `stage26_adaptive_rows.csv`
- `stage26_summary.json`

## Core gates

- `G-FIXED-LEFT-R05-RUN`
- `G-FIXED-SURVIVES-LARGER-SHAPE`
- `G-ADAPTIVE-WINNER-DEFINED`
- `G-ADAPTIVE-IMPROVES-AT-LEAST-ONE-SHAPE`
- `G-WILSON4-PRESERVED`
- `G-SELECTED-SIGN-CONSISTENT`

## Interpretation

Stage-26 is still a surrogate validation layer. It does not upgrade MBP to a production lattice proof. It narrows the consistency bottleneck by turning the question from

> “Does the left, r=0.5 corner exist?”

into

> “At each larger shape, does the fixed recommendation survive, or does the best `(chirality, r)` drift?”
