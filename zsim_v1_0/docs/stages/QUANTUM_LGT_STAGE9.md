# Z-Sim Quantum/LGT Stage-9

Stage-9 extends Stage-8 in two directions.

1. Sign-family refinement
- Add `arctan` and `pade11` overlap sign surrogates on top of `smooth`, `tanh`, and `rational`.
- Keep the overlap-selected background connected to the MBP bilinear ledger.

2. Shape-aware robustness
- Compare a baseline BCC shape and a larger BCC shape in a single harness.
- Score the selected ledger row with a mild size-gain factor to avoid over-rewarding tiny lattices.

3. Sharpened negative controls
- Keep Stage-7/8 controls.
- Add `edge_permuted_caloron` and `conjugation_scrambled_caloron` to break geometric coherence in harder ways.

Outputs
- `stage9_shape_rows.csv`
- `stage9_control_rows.csv`
- `stage9_summary.json`

Status
- preproduction surrogate
- not exact continuum caloron
- not production overlap lattice
- not final Higgs bilinear closure
