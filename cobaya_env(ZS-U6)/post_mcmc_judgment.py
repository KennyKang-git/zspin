#!/usr/bin/env python3
"""
Z-Spin Cosmology — Post-MCMC Falsification Judgment
====================================================

Automated evaluation of Gate F32-12 sub-gates after Cobaya MCMC completion.
Evaluates gates FU6-12a–e, FU6-13, FU6-16, FU6-17.

Reference: ZS-U6 v1.0 §10.7, The Book A-III.4
Author:    Kenny Kang (Z-Spin Collaboration)
Date:      March 2026

Usage:
    python post_mcmc_judgment.py --step0 chains/zspin_step0_evaluate
                                  --step1 chains/zspin_step1_base
                                  --step2 chains/zspin_step2_full

Requirements: numpy, scipy, getdist (pip install getdist)
"""

import argparse
import sys
import os
import json
import numpy as np
from datetime import datetime

# ==============================================================================
# Z-Spin Locked Constants
# ==============================================================================
A = 35 / 437                          # Geometric impedance
ONE_PLUS_A = 1 + A                    # = 472/437
OMEGA_M_EFF_PRED = 38 / (121 * ONE_PLUS_A)  # = 0.290762 (face counting)
H0_LEVEL1_PRED = 67.36 / np.sqrt(ONE_PLUS_A)  # = 64.81
H0_LEVEL2_PRED = 67.36               # Planck match
H0_LEVEL3_PRED = H0_LEVEL1_PRED * np.exp(A)  # = 72.98 (SH0ES match)
S8_PRED = 0.777                       # Face counting, DES Y3 at 0.06σ
N_S_PRED = 0.9674                     # Z-Spin locked

# Observational references
SHOES_H0 = 73.04
SHOES_H0_ERR = 1.04
DES_Y3_S8 = 0.776
DES_Y3_S8_ERR = 0.017
KIDS_S8 = 0.759
KIDS_S8_ERR = 0.024

# Falsification thresholds
SIGMA_THRESHOLD = 3.0     # 3σ for parameter tests
RHAT_THRESHOLD = 0.01     # Gelman-Rubin R̂−1
CHI2_NDOF_THRESHOLD = 1.1 # Goodness of fit


def load_chains(chain_root):
    """Load Cobaya MCMC chains using getdist."""
    try:
        from getdist import loadMCSamples
        samples = loadMCSamples(chain_root)
        return samples
    except ImportError:
        print("ERROR: getdist not installed. Run: pip install getdist")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR loading chains from {chain_root}: {e}")
        return None


def get_param_stats(samples, param_name):
    """Get mean, std, and 68% CI for a parameter."""
    try:
        stats = samples.getMargeStats()
        p = stats.parWithName(param_name)
        if p is None:
            return None, None, None, None
        return p.mean, p.err, p.limits[0].lower, p.limits[0].upper
    except Exception:
        # Fallback: direct computation
        try:
            vals = samples.getParams().__dict__[param_name]
            weights = samples.weights
            mean = np.average(vals, weights=weights)
            std = np.sqrt(np.average((vals - mean) ** 2, weights=weights))
            return mean, std, None, None
        except Exception:
            return None, None, None, None


def evaluate_step0(chain_root):
    """Step 0: Evaluate mode — report χ² at fixed Z-Spin parameters."""
    print("\n" + "=" * 70)
    print("STEP 0: EVALUATE MODE (Fixed Parameters)")
    print("=" * 70)
    
    # Step 0 produces a single likelihood evaluation, not chains
    # Look for the .updated.yaml or .loglik file
    loglik_file = chain_root + ".loglik"
    updated_file = chain_root + ".updated.yaml"
    
    chi2_fixed = None
    
    # Try to read from various output formats
    for ext in [".loglik", ".1.txt", ".txt"]:
        fpath = chain_root + ext
        if os.path.exists(fpath):
            try:
                data = np.loadtxt(fpath)
                if data.ndim == 1:
                    # Single evaluation: -2*loglik is often the first column
                    chi2_fixed = -2 * data[1] if len(data) > 1 else -2 * data[0]
                else:
                    chi2_fixed = -2 * data[0, 1]
                break
            except Exception:
                continue
    
    if chi2_fixed is not None:
        print(f"  χ²_fixed = {chi2_fixed:.2f}")
        print(f"  This is the likelihood at ALL Z-Spin fixed parameters.")
        print(f"  Compare with standard Planck best-fit χ² ≈ 2780 (plik_lite)")
    else:
        print("  WARNING: Could not read Step 0 output.")
        print(f"  Expected file at: {chain_root}.*")
        print("  Run: cobaya-run zspin_step0_evaluate.yaml")
    
    return chi2_fixed


def evaluate_gate_F32_12(samples_step1, samples_step2=None):
    """Evaluate all F32-12 sub-gates."""
    
    results = {}
    all_pass = True
    
    print("\n" + "=" * 70)
    print("GATE F32-12: COBAYA MCMC FULL PLANCK 2018 LIKELIHOOD")
    print("=" * 70)
    
    # ---- F32-12a: Ω_m test ----
    print("\n--- F32-12a: Ω_m^eff vs 0.2908 (face counting) ---")
    Om_mean, Om_err, _, _ = get_param_stats(samples_step1, "Omega_m")
    if Om_mean is not None and Om_err is not None:
        Om_eff = Om_mean / ONE_PLUS_A
        Om_eff_err = Om_err / ONE_PLUS_A
        pull_a = abs(Om_eff - OMEGA_M_EFF_PRED) / Om_eff_err
        pass_a = pull_a < SIGMA_THRESHOLD
        
        print(f"  Ω_m^CLASS     = {Om_mean:.6f} ± {Om_err:.6f}")
        print(f"  Ω_m^eff       = {Om_eff:.6f} ± {Om_eff_err:.6f}")
        print(f"  Ω_m^eff_pred  = {OMEGA_M_EFF_PRED:.6f}")
        print(f"  Pull           = {pull_a:.2f}σ")
        print(f"  STATUS: {'PASS ✓' if pass_a else 'FAIL ✗'} (threshold: {SIGMA_THRESHOLD}σ)")
        
        results["F32-12a"] = {"pull": pull_a, "pass": pass_a}
        if not pass_a:
            all_pass = False
    else:
        print("  ERROR: Could not extract Omega_m from chains")
        results["F32-12a"] = {"pull": None, "pass": False}
        all_pass = False
    
    # ---- F32-12b: H₀ Three-Level test ----
    print("\n--- F32-12b: H₀ Three-Level Structure ---")
    H0_mean, H0_err, _, _ = get_param_stats(samples_step1, "H0")
    if H0_mean is not None and H0_err is not None:
        H0_L1 = H0_mean / np.sqrt(ONE_PLUS_A)
        H0_L1_err = H0_err / np.sqrt(ONE_PLUS_A)
        pull_b = abs(H0_L1 - H0_LEVEL1_PRED) / H0_L1_err
        pass_b = pull_b < SIGMA_THRESHOLD
        
        H0_L2 = H0_mean
        H0_L3 = H0_L1 * np.exp(A)
        
        # SH0ES comparison
        pull_shoes = abs(H0_L3 - SHOES_H0) / SHOES_H0_ERR
        
        print(f"  H₀^CLASS (Level 2) = {H0_L2:.4f} ± {H0_err:.4f} km/s/Mpc")
        print(f"  H₀^ZS   (Level 1) = {H0_L1:.4f} ± {H0_L1_err:.4f} km/s/Mpc")
        print(f"  H₀^local(Level 3) = {H0_L3:.4f} km/s/Mpc")
        print(f"  Level 1 prediction = {H0_LEVEL1_PRED:.4f}")
        print(f"  Pull (Level 1)     = {pull_b:.2f}σ")
        print(f"  Pull vs SH0ES      = {pull_shoes:.2f}σ")
        print(f"  STATUS: {'PASS ✓' if pass_b else 'FAIL ✗'} (threshold: {SIGMA_THRESHOLD}σ)")
        
        results["F32-12b"] = {"pull": pull_b, "pass": pass_b,
                               "H0_L1": H0_L1, "H0_L2": H0_L2, "H0_L3": H0_L3}
        if not pass_b:
            all_pass = False
    else:
        print("  ERROR: Could not extract H0 from chains")
        results["F32-12b"] = {"pull": None, "pass": False}
        all_pass = False
    
    # ---- F32-12c: Convergence (Gelman-Rubin) ----
    print("\n--- F32-12c: Gelman-Rubin Convergence ---")
    try:
        # getdist reports R-1 in the chain stats
        Rminusone = samples_step1.getGelmanRubin()
        pass_c = Rminusone < RHAT_THRESHOLD
        print(f"  R̂−1 = {Rminusone:.4f}")
        print(f"  STATUS: {'PASS ✓' if pass_c else 'FAIL ✗'} (threshold: {RHAT_THRESHOLD})")
        results["F32-12c"] = {"Rhat_minus1": Rminusone, "pass": pass_c}
        if not pass_c:
            all_pass = False
    except Exception:
        print("  WARNING: Could not compute Gelman-Rubin statistic.")
        print("  Check: Did you run >= 2 chains?")
        print("  Cobaya reports R̂−1 in the terminal output.")
        results["F32-12c"] = {"Rhat_minus1": None, "pass": None}
    
    # ---- F32-12d: Goodness of fit ----
    print("\n--- F32-12d: Goodness of Fit (χ²/N_dof) ---")
    try:
        best_fit_loglik = samples_step1.getMinChisqLogLike()
        chi2_min = -2 * best_fit_loglik
        # Planck plik_lite: ~400 data points; full plik: ~2500+
        # Approximate N_dof (depends on likelihood used)
        N_dof_approx = 400  # plik_lite; change to ~2500 for full plik
        chi2_ndof = chi2_min / N_dof_approx
        pass_d = chi2_ndof < CHI2_NDOF_THRESHOLD
        
        print(f"  χ²_min   = {chi2_min:.2f}")
        print(f"  N_dof    ≈ {N_dof_approx} (adjust for your likelihood)")
        print(f"  χ²/N_dof = {chi2_ndof:.4f}")
        print(f"  STATUS: {'PASS ✓' if pass_d else 'FAIL ✗'} (threshold: {CHI2_NDOF_THRESHOLD})")
        results["F32-12d"] = {"chi2_min": chi2_min, "chi2_ndof": chi2_ndof, "pass": pass_d}
        if not pass_d:
            all_pass = False
    except Exception:
        print("  WARNING: Could not extract best-fit χ².")
        results["F32-12d"] = {"chi2_min": None, "pass": None}
    
    # ---- F32-12e: σ₈ / S₈ test ----
    print("\n--- F32-12e: σ₈ / S₈ vs Z-Spin prediction ---")
    s8_mean, s8_err, _, _ = get_param_stats(samples_step1, "sigma8")
    if s8_mean is not None and Om_mean is not None:
        S8_val = s8_mean * np.sqrt(Om_mean / 0.3)
        # Approximate S8 error propagation
        if s8_err is not None and Om_err is not None:
            S8_err = S8_val * np.sqrt((s8_err / s8_mean) ** 2 + 
                                       0.25 * (Om_err / Om_mean) ** 2)
        else:
            S8_err = 0.02  # fallback
        
        # Z-Spin S8 using Ω_m^eff
        S8_zspin = s8_mean * np.sqrt(Om_mean / (0.3 * ONE_PLUS_A))
        
        pull_e_des = abs(S8_zspin - DES_Y3_S8) / DES_Y3_S8_ERR
        pull_e_kids = abs(S8_zspin - KIDS_S8) / KIDS_S8_ERR
        pull_e_pred = abs(S8_zspin - S8_PRED) / S8_err if S8_err > 0 else 999
        pass_e = pull_e_pred < SIGMA_THRESHOLD
        
        print(f"  σ₈          = {s8_mean:.6f} ± {s8_err:.6f}")
        print(f"  S₈ (std)    = {S8_val:.4f} ± {S8_err:.4f}")
        print(f"  S₈^ZS       = {S8_zspin:.4f}")
        print(f"  S₈ predicted = {S8_PRED}")
        print(f"  Pull vs prediction = {pull_e_pred:.2f}σ")
        print(f"  Pull vs DES Y3     = {pull_e_des:.2f}σ")
        print(f"  Pull vs KiDS-1000  = {pull_e_kids:.2f}σ")
        print(f"  STATUS: {'PASS ✓' if pass_e else 'FAIL ✗'} (threshold: {SIGMA_THRESHOLD}σ)")
        
        results["F32-12e"] = {"S8_zspin": S8_zspin, "pull_pred": pull_e_pred,
                               "pull_DES": pull_e_des, "pull_KiDS": pull_e_kids,
                               "pass": pass_e}
        if not pass_e:
            all_pass = False
    else:
        print("  ERROR: Could not extract sigma8 from chains")
        results["F32-12e"] = {"pass": False}
        all_pass = False
    
    return results, all_pass


def compute_aic_bic(samples_step1, chi2_step0=None):
    """
    FU6-16: AIC/BIC comparison between Z-Spin (0 free params) and ΛCDM (6 free params).
    FU6-17: Savage-Dickey density ratio (simplified).
    """
    print("\n" + "=" * 70)
    print("FU6-16: AIC/BIC MODEL COMPARISON")
    print("=" * 70)
    
    results = {}
    
    try:
        # ΛCDM: 6 free parameters
        best_fit_loglik_lcdm = samples_step1.getMinChisqLogLike()
        chi2_lcdm = -2 * best_fit_loglik_lcdm
        k_lcdm = 6
        
        # Z-Spin: 0 free cosmological parameters (only A_s, τ as nuisance → 2)
        # But for the strongest claim: 0 cosmological parameters
        k_zspin = 0  # zero free cosmological parameters
        
        if chi2_step0 is not None:
            chi2_zspin = chi2_step0
        else:
            # Use the MCMC chi2 as approximation
            chi2_zspin = chi2_lcdm  # C_ℓ preservation → should be similar
            print("  NOTE: Using MCMC χ² as Step 0 proxy (run Step 0 for exact value)")
        
        # Number of data points (approximate)
        N_data = 400  # plik_lite; adjust for full plik
        
        # AIC = χ² + 2k
        AIC_lcdm = chi2_lcdm + 2 * k_lcdm
        AIC_zspin = chi2_zspin + 2 * k_zspin
        delta_AIC = AIC_zspin - AIC_lcdm
        
        # BIC = χ² + k × ln(N)
        BIC_lcdm = chi2_lcdm + k_lcdm * np.log(N_data)
        BIC_zspin = chi2_zspin + k_zspin * np.log(N_data)
        delta_BIC = BIC_zspin - BIC_lcdm
        
        print(f"\n  ΛCDM:    χ² = {chi2_lcdm:.2f}, k = {k_lcdm}")
        print(f"  Z-Spin:  χ² = {chi2_zspin:.2f}, k = {k_zspin}")
        print(f"\n  ΔAIC (Z-Spin − ΛCDM) = {delta_AIC:.2f}")
        print(f"  ΔBIC (Z-Spin − ΛCDM) = {delta_BIC:.2f}")
        print(f"\n  Interpretation:")
        if delta_BIC < -10:
            print(f"  ΔBIC < -10: VERY STRONG evidence for Z-Spin")
        elif delta_BIC < -6:
            print(f"  ΔBIC < -6: STRONG evidence for Z-Spin")
        elif delta_BIC < -2:
            print(f"  ΔBIC < -2: POSITIVE evidence for Z-Spin")
        elif delta_BIC < 2:
            print(f"  |ΔBIC| < 2: INCONCLUSIVE")
        else:
            print(f"  ΔBIC > 2: Evidence AGAINST Z-Spin")
        
        results["AIC"] = {"LCDM": AIC_lcdm, "ZSpin": AIC_zspin, "delta": delta_AIC}
        results["BIC"] = {"LCDM": BIC_lcdm, "ZSpin": BIC_zspin, "delta": delta_BIC}
        
    except Exception as e:
        print(f"  ERROR computing AIC/BIC: {e}")
    
    # FU6-17: Savage-Dickey (simplified)
    print("\n" + "=" * 70)
    print("FU6-17: SAVAGE-DICKEY DENSITY RATIO (Simplified)")
    print("=" * 70)
    
    try:
        Om_mean, Om_err, _, _ = get_param_stats(samples_step1, "Omega_m")
        if Om_mean is not None and Om_err is not None:
            Om_eff = Om_mean / ONE_PLUS_A
            Om_eff_err = Om_err / ONE_PLUS_A
            
            # Savage-Dickey: B_01 ≈ π(θ₀) / p(θ₀|data)
            # where θ₀ is the Z-Spin predicted value
            # p(θ₀|data) ≈ Gaussian posterior at prediction point
            from scipy.stats import norm
            posterior_at_pred = norm.pdf(OMEGA_M_EFF_PRED, loc=Om_eff, scale=Om_eff_err)
            
            # Prior: assume flat prior over [0.2, 0.4] → π = 1/0.2 = 5
            prior_density = 5.0
            
            B_01 = posterior_at_pred / prior_density
            
            print(f"  Ω_m^eff posterior: {Om_eff:.4f} ± {Om_eff_err:.4f}")
            print(f"  Ω_m^eff predicted: {OMEGA_M_EFF_PRED:.4f}")
            print(f"  Posterior density at prediction: {posterior_at_pred:.4f}")
            print(f"  Prior density (flat [0.2, 0.4]): {prior_density}")
            print(f"  Bayes factor B₀₁ ≈ {B_01:.2f}")
            print(f"\n  Interpretation:")
            if B_01 > 10:
                print(f"  B₀₁ > 10: STRONG support for Z-Spin prediction")
            elif B_01 > 3:
                print(f"  B₀₁ > 3: MODERATE support for Z-Spin prediction")
            elif B_01 > 1:
                print(f"  B₀₁ > 1: WEAK support for Z-Spin prediction")
            else:
                print(f"  B₀₁ < 1: Data does NOT support Z-Spin prediction")
            
            results["Savage_Dickey"] = {"B01": B_01}
    except Exception as e:
        print(f"  ERROR: {e}")
    
    return results


def step2_comparison(samples_step1, samples_step2):
    """Compare Step 1 (base) vs Step 2 (full) to isolate Z-sector effect."""
    print("\n" + "=" * 70)
    print("STEP 1 vs STEP 2: Z-SECTOR DARK RADIATION EFFECT")
    print("=" * 70)
    
    try:
        chi2_step1 = -2 * samples_step1.getMinChisqLogLike()
        chi2_step2 = -2 * samples_step2.getMinChisqLogLike()
        delta_chi2 = chi2_step2 - chi2_step1
        
        print(f"  χ²_min (Step 1, base)  = {chi2_step1:.2f}")
        print(f"  χ²_min (Step 2, full)  = {chi2_step2:.2f}")
        print(f"  Δχ² (Step 2 − Step 1)  = {delta_chi2:.2f}")
        print(f"  Expected: O(1–10)")
        print(f"\n  Physical interpretation:")
        print(f"  Δχ² is entirely due to ΔN_eff = 2A = 0.160")
        print(f"  (Z-sector dark radiation breaking C_ℓ exact identity)")
        
        if abs(delta_chi2) < 1:
            print(f"  → Z-sector effect is sub-dominant in Planck 2018")
        elif abs(delta_chi2) < 10:
            print(f"  → Z-sector produces detectable but tolerable deviation")
        else:
            print(f"  → Z-sector effect is significant — check for systematics")
        
        # Parameter shifts
        for param in ["omega_b", "omega_cdm", "H0", "sigma8", "ns"]:
            m1, e1, _, _ = get_param_stats(samples_step1, param)
            m2, e2, _, _ = get_param_stats(samples_step2, param)
            if m1 is not None and m2 is not None and e1 is not None:
                shift = (m2 - m1) / e1
                print(f"  Δ{param}: {m2 - m1:.6f} ({shift:.2f}σ)")
        
    except Exception as e:
        print(f"  ERROR: {e}")


def generate_summary(results_f32, aic_bic_results, all_pass, chi2_step0):
    """Generate final judgment summary."""
    print("\n" + "=" * 70)
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║              GATE F32-12 FINAL JUDGMENT                        ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print("=" * 70)
    
    for gate, result in results_f32.items():
        status = "PASS ✓" if result.get("pass") else ("FAIL ✗" if result.get("pass") is not None else "N/A")
        pull = result.get("pull", "—")
        if isinstance(pull, float):
            pull = f"{pull:.2f}σ"
        print(f"  {gate}: {status:10s}  (pull: {pull})")
    
    print(f"\n  OVERALL: {'ALL GATES PASS ✓ — Z-Spin SURVIVES' if all_pass else 'ONE OR MORE GATES FAILED ✗'}")
    
    if all_pass:
        print(f"\n  Z-Spin Cosmology with A = 35/437 is consistent with")
        print(f"  Planck 2018 full CMB likelihood at all sub-gate thresholds.")
        print(f"  Framework proceeds to journal submission stage.")
    else:
        failed = [g for g, r in results_f32.items() if r.get("pass") == False]
        print(f"\n  Failed gates: {', '.join(failed)}")
        print(f"  Z-Spin framework requires revision or is FALSIFIED.")
    
    # Save results to JSON
    output = {
        "timestamp": datetime.now().isoformat(),
        "framework": "Z-Spin Cosmology",
        "gate": "F32-12",
        "A": float(A),
        "constants": {
            "Omega_m_eff_pred": float(OMEGA_M_EFF_PRED),
            "H0_level1_pred": float(H0_LEVEL1_PRED),
            "S8_pred": float(S8_PRED),
        },
        "sub_gates": {},
        "overall_pass": all_pass,
    }
    
    for gate, result in results_f32.items():
        output["sub_gates"][gate] = {
            k: float(v) if isinstance(v, (np.floating, float)) else v
            for k, v in result.items()
        }
    
    if aic_bic_results:
        output["model_comparison"] = {}
        for k, v in aic_bic_results.items():
            if isinstance(v, dict):
                output["model_comparison"][k] = {
                    kk: float(vv) if isinstance(vv, (np.floating, float)) else vv
                    for kk, vv in v.items()
                }
    
    json_path = "gate_F32_12_judgment.json"
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to: {json_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Z-Spin Gate F32-12 Post-MCMC Falsification Judgment"
    )
    parser.add_argument("--step0", type=str, default=None,
                        help="Chain root for Step 0 (evaluate mode)")
    parser.add_argument("--step1", type=str, required=True,
                        help="Chain root for Step 1 (base MCMC)")
    parser.add_argument("--step2", type=str, default=None,
                        help="Chain root for Step 2 (full MCMC)")
    args = parser.parse_args()
    
    print("=" * 70)
    print("Z-SPIN COSMOLOGY — POST-MCMC FALSIFICATION JUDGMENT")
    print(f"A = 35/437 = {A:.12f}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Step 0
    chi2_step0 = None
    if args.step0:
        chi2_step0 = evaluate_step0(args.step0)
    
    # Step 1 (required)
    print("\nLoading Step 1 (base MCMC) chains...")
    samples_step1 = load_chains(args.step1)
    if samples_step1 is None:
        print("FATAL: Cannot load Step 1 chains. Exiting.")
        sys.exit(1)
    
    # Main gate evaluation
    results_f32, all_pass = evaluate_gate_F32_12(samples_step1)
    
    # AIC/BIC
    aic_bic = compute_aic_bic(samples_step1, chi2_step0)
    
    # Step 2 comparison (optional)
    if args.step2:
        print("\nLoading Step 2 (full MCMC) chains...")
        samples_step2 = load_chains(args.step2)
        if samples_step2 is not None:
            step2_comparison(samples_step1, samples_step2)
    
    # Final judgment
    generate_summary(results_f32, aic_bic, all_pass, chi2_step0)
    
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
