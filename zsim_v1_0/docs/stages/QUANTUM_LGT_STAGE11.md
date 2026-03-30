# Quantum LGT Stage-11

Stage-11 adds a stress-ledger layer on top of Stage-10.

## What changed

- Broader larger-shape scan: `(1,1,1)`, `(2,1,1)`, `(2,2,1)`, `(2,2,2)`, `(3,2,1)` by default.
- Stricter sign-kernel diagnostics: scan over `sign_epsilon_grid` and `fd_scale_grid` instead of using a single sign/FD point.
- Closure-ledger stress test: compare the overlap-selected background against sharpened controls using a robust score `mean(score) - std(score)`.

## Outputs

- `stage11_shape_rows.csv`
- `stage11_stress_rows.csv`
- `stage11_summary.json`

## Interpretation

This is still a preproduction surrogate. It does **not** claim:

- an exact continuum caloron,
- a production overlap lattice,
- or final Higgs bilinear closure.

What it does provide is a stricter ledger for checking whether the selected overlap-aware background remains ahead of sharpened controls when the sign-kernel and closure settings are stressed.
