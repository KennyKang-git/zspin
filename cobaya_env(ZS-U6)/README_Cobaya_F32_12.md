# Z-Spin Cosmology — Cobaya MCMC Configuration Bundle
# Gate F32-12: Full Planck 2018 Likelihood Validation
# ==============================================================================
# Author: Kenny Kang (Z-Spin Collaboration)
# Date:   March 2026
# Ref:    ZS-U6 v1.0 §10, The Book A-III.4
# ==============================================================================

## Files

| File | Purpose | Runtime |
|------|---------|---------|
| zspin_step0_evaluate.yaml | All 6 params FIXED. Single χ² evaluation. | ~30 sec |
| zspin_step1_base.yaml     | Base MCMC. N_ur=2.0328 (no Z-sector).     | 24-48 hrs |
| zspin_step2_full.yaml     | Full MCMC. N_ur=2.19298 (with Z-sector).  | 24-48 hrs |
| post_mcmc_judgment.py     | Automated Gate F32-12 judgment.            | ~1 min |

## Prerequisites

    # Ubuntu WSL environment (~/cobaya_env)
    conda activate cobaya_env
    
    # Required packages
    pip install cobaya getdist numpy scipy
    cobaya-install planck_2018_highl_plik.TTTEEE_lite
    cobaya-install planck_2018_lowl.TT
    cobaya-install planck_2018_lowl.EE
    cobaya-install planck_2018_lensing.clik

## Execution Order

    # Step 0: Evaluate (30 seconds)
    cobaya-run zspin_step0_evaluate.yaml
    
    # Step 1: Base MCMC (24-48 hours, use 4 chains)
    mpirun -n 4 cobaya-run zspin_step1_base.yaml
    
    # Step 2: Full MCMC (24-48 hours, use 4 chains)
    mpirun -n 4 cobaya-run zspin_step2_full.yaml
    
    # Post-MCMC Judgment
    python post_mcmc_judgment.py \
        --step0 chains/zspin_step0_evaluate \
        --step1 chains/zspin_step1_base \
        --step2 chains/zspin_step2_full

## Z-Spin Parameter Mapping

    A = 35/437 = 0.080091533181
    1+A = 472/437 = 1.080091533181
    
    T_cmb^eff   = 2.72548 × (1+A)^(-1/4) = 2.6735 K
    ω_b^eff     = 0.02237 / (1+A) = 0.020711
    ω_cdm^eff   = 0.12000 / (1+A) = 0.111102  [face counting: 32/121]
    H₀^ZS       = 67.36 / √(1+A) = 64.81 km/s/Mpc
    Ω_m^eff     = 38/(121×(1+A)) = 0.2908
    n_s         = 0.9674 (locked)
    
    N_ur (base) = 2.0328
    N_ur (full) = 2.0328 + 2A = 2.19298
    ΔN_eff      = 2A = 0.160183

## Gate F32-12 Sub-gates

| Sub-gate | Condition | Threshold |
|----------|-----------|-----------|
| F32-12a  | Ω_m^CLASS/(1+A) vs 0.2908 | 3σ |
| F32-12b  | H₀^CLASS/√(1+A) vs 64.81 | 3σ |
| F32-12c  | Gelman-Rubin R̂−1 < 0.01 | Convergence |
| F32-12d  | Best-fit χ²/N_dof < 1.1 | Goodness |
| F32-12e  | σ₈ posterior vs 0.777 | 3σ |

## Upgrade to Full Planck Likelihood

For the definitive Gate F32-12 test, replace plik_lite with full plik:

    # In all YAML files, change:
    planck_2018_highl_plik.TTTEEE_lite  →  planck_2018_highl_plik.TTTEEE
    
    # And install:
    cobaya-install planck_2018_highl_plik.TTTEEE

## Output

post_mcmc_judgment.py produces:
- Terminal report with all sub-gate evaluations
- gate_F32_12_judgment.json (machine-readable results)
- AIC/BIC model comparison (FU6-16)
- Savage-Dickey density ratio (FU6-17)
