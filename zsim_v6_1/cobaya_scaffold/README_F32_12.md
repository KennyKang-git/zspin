# Z-Spin Cobaya Pipeline — Gate F32-12

## Overview
This is the scaffold for the HIGHEST PRIORITY pending falsification gate.
Until F32-12 is executed, no flagship journal submission is viable.

## What Z-Spin Predicts (NOT sampled by Cobaya)
- H₀_local/H₀_CMB = exp(A) = exp(35/437) = 1.08339
- Ω_m_eff = 39/121 = 0.29841
- w₀ = -1 (exactly at attractor), wₐ = 0
- G_eff = G/(1+A) = G × 437/472
- c_T = c (structural, G₅=0)
- n_s = 0.9667 (N*=60), r = 0.0089

## What Cobaya Samples (NOT predicted by Z-Spin)
- A_s (scalar amplitude): Planck prior ~2.1×10⁻⁹
- τ_reio (reionization optical depth): Planck prior ~0.054

## Execution Steps
1. Install Cobaya: `pip install cobaya`
2. Install CLASS: `cobaya-install cosmo -p /path/to/packages`
3. Install Planck likelihood: `cobaya-install planck_2018 -p /path/to/packages`
4. Run grid scan first: `cobaya-run zspin_grid_scan.yaml`
5. Run full MCMC: `cobaya-run zspin_planck2018.yaml`

## Critical Modification Required
Standard CLASS assumes G = G_Newton. Z-Spin requires G_eff = G/(1+A).
Two options:
  (a) Use hi_class (Horndeski CLASS) with α_M, α_T parameters
  (b) Modify CLASS source: replace G → G×437/472 in perturbation equations

## PASS/FAIL Criterion
If the best-fit χ² under Z-Spin parameters is within Δχ² < 10 of
standard LCDM best-fit, Gate F32-12 PASSES.
If Δχ² > 25 (5σ equivalent), Gate F32-12 FAILS and the framework
needs revision.

## Reference
ZS-U1 §4, Paper 32 specification
