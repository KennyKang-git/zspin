"""Z-Sim v1.0 — Production Lattice Gauge Theory package.

Architecture improvements over lgt/ (v5.x surrogate):
  1. Periodic boundary conditions on BCC T³
  2. Wilson gradient flow (Lüscher RK3 ODE integrator)
  3. Overlap Dirac operator (exact sign function)
  4. Lattice spacing a and continuum extrapolation
  5. Caloron constituent / BPS monopole backgrounds

This package implements the 5-phase MBP protocol (ZS-S4 §6.11.4):
  Phase 1: Construct multi-cell SU(2) lattice on periodic BCC T³
  Phase 2: Cool/gradient-flow to caloron constituent sector
  Phase 3: Compute overlap Dirac spectrum in I-Ī background
  Phase 4: Extract h² coefficient from fermion determinant ratio
  Phase 5: Compare with MBP formula
"""

__all__ = [
    "PeriodicBCCLattice",
    "GaugeField",
    "WilsonGradientFlow",
    "WilsonDirac",
    "OverlapDirac",
    "CaloronBackground",
    "MBP2Result",
    "ContinuumExtrapolator",
]
