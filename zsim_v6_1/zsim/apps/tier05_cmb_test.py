"""Z-Sim v3.1 -- Tier-0.5 CMB Compressed Distance Prior Test.

Paper 21 v2.3.0 S4: "Tier-0.5 existence test: using compressed CMB
distance priors (R, l_A, omega_b) from Planck 2018."

Paper 21 result: minimum chi^2 = 0.285 at Omega_m^eff = 0.2977

Source: Planck 2018 compressed likelihood (Chen, Huang & Wang 2019)
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
import math

from zsim.core.constants import A_LOCKED, G_EFF_RATIO, OMEGA_M_EFF


# Planck 2018 compressed distance priors
R_OBS = 1.7502
LA_OBS = 301.471
OMEGAB_H2_OBS = 0.02236

# Inverse covariance matrix (Chen, Huang & Wang 2019)
COV_INV = np.array([
    [ 94395.2,  -1318.60,  -1.56e6],
    [ -1318.60,   21.4576,   23084.5],
    [ -1.56e6,    23084.5,   3.71e10],
])

Z_STAR = 1089.92
OMEGA_GAMMA_H2 = 2.469e-5  # photon physical density (T_CMB = 2.7255 K)
OMEGA_NU_H2 = 1.698e-5     # neutrino physical density (3 species)
OMEGA_R_H2 = OMEGA_GAMMA_H2 + OMEGA_NU_H2  # total radiation


def _E(z: float, omega_m: float, h: float = 0.6736) -> float:
    """Hubble parameter E(z) = H(z)/H0."""
    a = 1.0 / (1.0 + z)
    omega_r = OMEGA_R_H2 / (h * h)
    omega_lambda = 1.0 - omega_m - omega_r
    return math.sqrt(omega_m * (1+z)**3 + omega_r * (1+z)**4 + omega_lambda)


def _comoving_distance(z: float, omega_m: float, h: float = 0.6736) -> float:
    """D_C(z) / (c/H0) = integral_0^z dz'/E(z')."""
    result, _ = quad(lambda zp: 1.0 / _E(zp, omega_m, h), 0.0, z,
                     limit=300, epsrel=1e-12)
    return result


def _sound_horizon(omega_m: float, omega_b_h2: float, h: float = 0.6736) -> float:
    """Comoving sound horizon r_s(z*) / (c/H0).

    r_s = integral_{z*}^{inf} c_s/c dz / E(z)
    c_s/c = 1/sqrt(3(1 + R_b))
    R_b = 3 omega_b_h2 / (4 omega_gamma_h2) * a  [h^2 cancels between numerator and denominator]
    """
    R_b_coeff = 3.0 * omega_b_h2 / (4.0 * OMEGA_GAMMA_H2)

    def integrand(z):
        a = 1.0 / (1.0 + z)
        R_b = R_b_coeff * a
        cs_over_c = 1.0 / math.sqrt(3.0 * (1.0 + R_b))
        return cs_over_c / _E(z, omega_m, h)

    result, _ = quad(integrand, Z_STAR, 1e6, limit=500, epsrel=1e-12)
    return result


def compute_R(omega_m: float, h: float = 0.6736) -> float:
    """Shift parameter R = sqrt(Omega_m) * D_C(z*) / (c/H0)."""
    return math.sqrt(omega_m) * _comoving_distance(Z_STAR, omega_m, h)


def compute_lA(omega_m: float, omega_b_h2: float, h: float = 0.6736) -> float:
    """Acoustic scale l_A = pi * D_C(z*) / r_s(z*)."""
    DC = _comoving_distance(Z_STAR, omega_m, h)
    rs = _sound_horizon(omega_m, omega_b_h2, h)
    return math.pi * DC / rs if rs > 1e-30 else 0.0


def chi_squared(omega_m: float, omega_b_h2: float = OMEGAB_H2_OBS,
                h: float = 0.6736) -> float:
    """Chi-squared from compressed CMB distance priors."""
    delta = np.array([
        compute_R(omega_m, h) - R_OBS,
        compute_lA(omega_m, omega_b_h2, h) - LA_OBS,
        omega_b_h2 - OMEGAB_H2_OBS,
    ])
    return float(delta @ COV_INV @ delta)


def run_tier05_test(verbose: bool = True) -> dict:
    """Execute the Tier-0.5 compressed distance prior test."""
    if verbose:
        print("=" * 70)
        print("  Z-Sim v3.1 -- Tier-0.5 CMB Distance Prior Test")
        print("  Source: Paper 21 v2.3.0 S4, Planck 2018 compressed likelihood")
        print("=" * 70)

    h = 0.6736
    omega_b_zspin = 6.0 / (121.0 * (1.0 + A_LOCKED)) * h * h

    if verbose:
        # Sanity check: Planck LCDM should give chi2 ~ 0
        R_planck = compute_R(0.3153, h)
        lA_planck = compute_lA(0.3153, 0.02236, h)
        print(f"\n  Sanity check (Planck LCDM):")
        print(f"    R  = {R_planck:.4f} (expected: {R_OBS})")
        print(f"    l_A = {lA_planck:.2f} (expected: {LA_OBS})")
        chi2_planck = chi_squared(0.3153, 0.02236, h)
        print(f"    chi2 = {chi2_planck:.3f} (expected: ~ 0)")

    # Scan + optimize
    omega_m_range = np.linspace(0.20, 0.40, 500)
    chi2_values = np.array([chi_squared(om, omega_b_zspin, h) for om in omega_m_range])
    idx_min = np.argmin(chi2_values)

    result = minimize_scalar(lambda om: chi_squared(om, omega_b_zspin, h),
                            bounds=(max(0.15, omega_m_range[idx_min]-0.02),
                                    min(0.50, omega_m_range[idx_min]+0.02)),
                            method='bounded')
    omega_m_best = result.x
    chi2_min = result.fun

    chi2_zspin = chi_squared(OMEGA_M_EFF, omega_b_zspin, h)
    R_zspin = compute_R(OMEGA_M_EFF, h)
    lA_zspin = compute_lA(OMEGA_M_EFF, omega_b_zspin, h)

    if verbose:
        print(f"\n  Z-Spin locked parameters:")
        print(f"    A = 35/437 = {A_LOCKED:.10f}")
        print(f"    Omega_m^eff = {OMEGA_M_EFF:.6f}")
        print(f"    omega_b = {omega_b_zspin:.6f}")

        print(f"\n  Z-Spin observables:")
        print(f"    R    = {R_zspin:.4f}  (Planck: {R_OBS})")
        print(f"    l_A  = {lA_zspin:.2f}  (Planck: {LA_OBS})")

        print(f"\n  Optimization:")
        print(f"    Best-fit Omega_m = {omega_m_best:.6f}")
        print(f"    chi2_min         = {chi2_min:.3f}")
        print(f"    chi2(Z-Spin)     = {chi2_zspin:.3f}")
        print(f"    |Omega_m_best - Omega_m^ZS| = {abs(omega_m_best - OMEGA_M_EFF):.4f}")

        print(f"\n  Paper 21 comparison:")
        print(f"    Paper 21: chi2_min = 0.285, Omega_m = 0.2977")

        verdict = "PASS" if chi2_zspin < 10.0 else "FAIL"
        print(f"\n  {'='*54}")
        print(f"  TIER-0.5 VERDICT: {verdict}")
        print(f"  chi2(Z-Spin) = {chi2_zspin:.3f}")
        if verdict == "PASS":
            print(f"  Z-Spin is NOT trivially excluded by CMB priors.")
        print(f"  {'='*54}")

    return {
        "chi2_min": chi2_min, "omega_m_best": omega_m_best,
        "chi2_zspin": chi2_zspin, "omega_m_zspin": OMEGA_M_EFF,
        "R_zspin": R_zspin, "lA_zspin": lA_zspin,
        "pass": chi2_zspin < 10.0,
    }


if __name__ == "__main__":
    run_tier05_test()
