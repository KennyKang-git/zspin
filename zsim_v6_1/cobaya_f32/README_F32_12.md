# Z-Spin Gate F32-12: Cobaya MCMC Run Guide

## Overview

Gate F32-12 is the **highest priority falsification gate** for Z-Spin Cosmology.
It tests the full CMB power spectrum against Planck 2018 data.

Z-Sim v3.1 Tier-0.7 already showed:
- CMB TT spectrum matches Planck LCDM within cosmic variance (76.3% of multipoles)
- H0_CMB = 69.15, H0_local = exp(A) × 69.15 = 74.92 km/s/Mpc
- No show-stopper visible

Gate F32-12 makes this rigorous with the full Planck likelihood.


## Prerequisites

### WSL Setup (Windows)
```bash
# Enter WSL
wsl

# Install Python (if needed)
sudo apt update
sudo apt install python3 python3-pip python3-venv -y

# Create virtual environment
python3 -m venv ~/cobaya_env
source ~/cobaya_env/bin/activate

# Install packages
pip install cobaya camb numpy scipy matplotlib

# Access ZSim from Windows
cd /mnt/c/Users/LG/zsim_v3.1
pip install -e .
```


## Three Test Levels

### Level 1: Local Test (5 minutes, no data download)

Uses only the Planck lite likelihood (bundled with cobaya).
Good for verifying the pipeline works.

```bash
source ~/cobaya_env/bin/activate
cd /mnt/c/Users/LG/zsim_v3.1

cobaya-run cobaya_f32/zspin_local_test.yaml
```

**Expected output:** MCMC chains in `zspin_local_test_output/`
**Check:** `cat zspin_local_test_output/*.1.txt | tail -5`


### Level 2: Grid Scan with Planck Lite (10 minutes)

2D grid over (A_s, tau) with plik lite likelihood.

```bash
cobaya-run cobaya_f32/zspin_grid_2d.yaml
```


### Level 3: Full Planck MCMC (1-4 hours)

The definitive test. Requires Planck likelihood data (~2GB).

```bash
# Step 1: Install Planck data (one-time, ~2GB download)
cobaya-install planck_2018_lowl.TT --packages-path ~/packages
cobaya-install planck_2018_lowl.EE --packages-path ~/packages  
cobaya-install planck_2018_highl_plik.TTTEEE --packages-path ~/packages
cobaya-install planck_2018_lensing.clik --packages-path ~/packages

# Step 2: Run MCMC
cobaya-run cobaya_f32/zspin_mcmc_planck.yaml \
    --packages-path ~/packages

# Step 3: Check convergence
# Look for Rminus1_last in the output log
# Rminus1 < 0.01 means converged
```


## Parameter Summary

| Parameter | Value | Status | Source |
|-----------|-------|--------|--------|
| A | 35/437 | LOCKED | ZS-F2 polyhedral geometry |
| H0_CMB | 69.15 km/s/Mpc | DERIVED | Tier-0.5 (chi2=1.33) |
| H0_local | 74.92 km/s/Mpc | DERIVED | exp(A) × H0_CMB |
| omega_b h^2 | 0.021953 | DERIVED | 6/(121(1+A)) × h^2 |
| omega_cdm h^2 | 0.120740 | DERIVED | 33/(121(1+A)) × h^2 |
| Omega_m^eff | 0.2984 | DERIVED | 39/(121(1+A)) |
| n_s | 0.9674 | DERIVED | Paper 18 canonical inflation |
| r | 0.0089 | DERIVED | Paper 18 |
| w0 | -1 (exact) | DERIVED | attractor |
| wa | 0 (exact) | DERIVED | attractor |
| **A_s** | ~2.1e-9 | **SAMPLED** | Cobaya explores |
| **tau** | ~0.054 | **SAMPLED** | Cobaya explores |


## PASS/FAIL Criterion (Paper 32)

```
If   Δχ² < 10    relative to Planck LCDM best-fit → PASS
If   Δχ² > 25    (5σ equivalent)                  → FAIL & framework revision needed
```

Planck LCDM best-fit χ² ≈ 2778 (for plik TTTEEE + lowl TT + lowl EE).
Z-Spin needs χ² < 2788 to PASS.


## After Running

### Quick Analysis
```python
import numpy as np

# Load chains
data = np.loadtxt('zspin_mcmc_planck_output/zspin_mcmc_planck_output.1.txt')
# Columns depend on parameter ordering - check .paramnames file

# Best-fit chi2
min_chi2 = -2 * np.max(data[:, 1])  # column 1 is log-likelihood
print(f"Best-fit chi2 = {min_chi2:.1f}")
print(f"Planck LCDM chi2 ~ 2778")
print(f"Delta chi2 = {min_chi2 - 2778:.1f}")
```

### GetDist Analysis (publication-quality plots)
```bash
pip install getdist
python -c "
from getdist import loadMCSamples
samples = loadMCSamples('zspin_mcmc_planck_output/zspin_mcmc_planck_output')
print(samples.getTable().tableTex())
"
```


## Troubleshooting

**"planck_2018_lowl not found"**
→ Run `cobaya-install planck_2018_lowl.TT --packages-path ~/packages`

**"CAMB error: H0 out of range"**
→ Check that H0=69.15 is within CAMB's allowed range (20-100)

**MCMC not converging**
→ Increase `max_tries`, or start with the grid scan (Level 2) first

**Windows path issues in WSL**
→ Use `/mnt/c/Users/LG/zsim_v3.1/` (forward slashes)
