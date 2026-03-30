# Z-Sim v1.0 — Quantum/LGT Stage 4

## What changed

Stage 4 upgrades the reduced MBP extractor into a **chiral/caloron preproduction surrogate**.

New pieces:

- `zsim.lgt.chirality`
  - bipartite chirality signs on the BCC scaffold
  - reduced `gamma5` surrogate
  - left/right/vector chiral projectors
- `zsim.lgt.backgrounds`
  - caloron-like instanton/anti-instanton pair background
  - scrambled-caloron negative control
- `zsim.lgt.controls`
  - standardized negative controls for identity / Haar / scrambled projector / scrambled caloron
- `zsim.apps.su2_mbp_stage4_validate`
  - stage-4 validation CLI with gates and summary JSON

## Honest scope

This is still **not** a continuum caloron solver and **not** a production-scale lattice result.
It is a structured reduced engine meant to test whether:

1. chiral projectors alter the bilinear in a controlled way,
2. a nontrivial valley background produces stronger response than identity,
3. negative controls separate from the structured background,
4. trace-formula and finite-difference remain mutually consistent.

## Recommended next step

The next physics step is to replace the reduced `gamma5` surrogate by a true Wilson/staggered spinor block and to move the caloron surrogate toward a constrained multi-cell valley fit.
