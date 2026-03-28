# Z-Sim v3.4 Quantum/LGT Stage 2

This stage upgrades the SU(2) tooling from a bare scaffold to a reduced multi-cell engine.

Implemented components:
- multi-cell BCC rhombic plaquette enumeration
- Wilson/plaquette observables on reduced SU(2) links
- plaquette-informed cooling / gradient-flow surrogate
- valley scan with even-quartic bilinear proxy fit
- reduced collective-coordinate HMC chain

What is still intentionally outside scope:
- full caloron/instanton localization on a continuum-equivalent lattice
- exact Dirac operator with chirality/projector structure
- explicit h^2 coefficient extraction from K0^{-1}K2 and K0^{-1}K1K0^{-1}K1 on a production lattice
