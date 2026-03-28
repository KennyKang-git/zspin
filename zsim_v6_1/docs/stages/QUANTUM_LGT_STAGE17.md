
# QUANTUM_LGT_STAGE17

## Scope

Stage-17 adds a **snapshot-connected live stress ledger** on top of Stage-16.
Instead of rerunning the full heavy broad-grid pipeline again, this stage takes the recorded Stage-16 live bridge rows and applies a broader sign/shape stress comparison in one direct ledger.

## New modules

- `zsim.lgt.stage17`
- `zsim.apps.su2_mbp_stage17_live_stress_validate`

## Outputs

- `stage17_stress_rows.csv`
- `stage17_summary.json`

## Interpretation

This stage is still a **preproduction surrogate**.
It does **not** claim:
- exact continuum caloron,
- production overlap lattice,
- final Higgs bilinear closure.

What it does claim is narrower:
- the recorded Stage-16 live rows can be re-ranked in a broader stress ledger,
- a sign/shape stress-selected background can be compared directly against snapshot and control rows,
- the stress-selected background should still outrank the matched stress control and live control in this lightweight validation path.
