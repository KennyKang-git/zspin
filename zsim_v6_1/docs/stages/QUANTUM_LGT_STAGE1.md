# Z-Sim v3.4 Quantum/LGT Stage-1 Scaffold

This scaffold adds two new internal packages to the existing Z-Sim v3.1 layout.

- `zsim.quantum`: exact polyhedral geometry, incidence/Hodge operators, Hodge–Dirac spectra.
- `zsim.lgt`: reduced SU(2) BCC lattice scaffolding for link variables, cooling, and collective-coordinate valley probes.

## What is implemented now

- Exact truncated icosahedron generator with counts `(60, 90, 32)`.
- Exact truncated octahedron generator with counts `(24, 36, 14)`.
- Boundary matrices `B1`, `B2` with the nilpotency check `B1 @ B2 = 0`.
- Hodge Laplacians and Hodge–Dirac operator.
- CLI: `quantum_topology` for spectral summaries.
- CLI: `su2_bcc_scan` for reduced BCC link scans.
- CLI: `su2_valley_probe` for collective-coordinate singular-value scans.
- Basic tests for geometry, apps, and SU(2) link scaffolding.

## Honest limits

This is a stage-1 scaffold, not a full lattice-QCD replacement.

- The exact spectral engine is real and runnable.
- The SU(2) module is a reduced graph/LGT scaffold, not a full continuum-equivalent multi-cell BCC production engine.
- Plaquette enumeration, gradient-flow observables, and instanton diagnostics are not yet canonical in this scaffold.
