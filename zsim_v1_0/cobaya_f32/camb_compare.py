#!/usr/bin/env python3
"""Z-Sim v1.0 — Tier-0.7 CAMB Comparison Script.

Computes CMB TT power spectra for Planck LCDM and Z-Spin,
then generates a comparison plot and statistics.

Requires only: pip install camb matplotlib numpy
No Planck data download needed.

Usage:
    python cobaya_f32/camb_compare.py
    python cobaya_f32/camb_compare.py --optimize   # optimize A_s and tau
"""
from __future__ import annotations

import argparse
import math
import sys

import numpy as np

try:
    import camb
except ImportError:
    print("CAMB not installed. Run: pip install camb")
    sys.exit(1)

# Z-Spin constants
A = 35 / 437
OMEGA_M_EFF = 38.0 / (121.0 * (1.0 + A))  # v1.0: face counting; was 39/121
H_ZSPIN = 67.36  # Tier-0.5 optimized
OMBH2_ZS = 6.0 / 121.0 * (H_ZSPIN / 100) ** 2  # bare, no G_eff
OMCH2_ZS = 32.0 / 121.0 * (H_ZSPIN / 100) ** 2  # face counting, truncated icosahedron
NS_ZS = 0.9674

# Planck LCDM baseline
H_PLANCK = 67.36
OMBH2_PL = 0.02237
OMCH2_PL = 0.12000
NS_PL = 0.9649

LMAX = 2500


def compute_cls(H0, ombh2, omch2, ns, As=2.1e-9, tau=0.054, label=""):
    """Compute CMB TT power spectrum with CAMB."""
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, tau=tau,
                       mnu=0.06, nnu=3.046)
    pars.InitPower.set_params(As=As, ns=ns)
    pars.set_for_lmax(LMAX, lens_potential_accuracy=1)
    pars.set_matter_power(redshifts=[0.0], kmax=2.0)
    results = camb.get_results(pars)
    cls = results.get_cmb_power_spectra(pars, CMB_unit='muK')
    tt = cls['total'][:LMAX + 1, 0]
    derived = {
        'sigma8': results.get_sigma8_0(),
        'age': results.get_derived_params()['age'] if 'age' in results.get_derived_params() else 0,
        'rdrag': results.get_derived_params()['rdrag'] if 'rdrag' in results.get_derived_params() else 0,
    }
    if label:
        print(f"  [{label}] sigma8={derived['sigma8']:.4f}, "
              f"age={derived['age']:.2f} Gyr, r_drag={derived['rdrag']:.2f} Mpc")
    return tt, derived


def optimize_As_tau(tt_ref):
    """Find best (A_s, tau) for Z-Spin to match reference spectrum."""
    from scipy.optimize import minimize

    ells = np.arange(LMAX + 1)
    mask = (ells >= 30) & (ells <= 2000) & (tt_ref > 1)
    cv = 2.0 * tt_ref[mask] ** 2 / (2.0 * ells[mask] + 1.0)

    def objective(params):
        logAs, tau = params
        if tau < 0.01 or tau > 0.12:
            return 1e10
        As = math.exp(logAs) * 1e-10
        try:
            tt, _ = compute_cls(H_ZSPIN, OMBH2_ZS, OMCH2_ZS, NS_ZS,
                                As=As, tau=tau)
            return float(np.sum((tt[mask] - tt_ref[mask]) ** 2 / cv))
        except Exception:
            return 1e10

    # Grid search
    best = (1e10, 3.044, 0.054)
    for logAs in np.linspace(2.9, 3.15, 15):
        for tau in np.linspace(0.035, 0.075, 15):
            c2 = objective([logAs, tau])
            if c2 < best[0]:
                best = (c2, logAs, tau)

    # Refine
    result = minimize(objective, [best[1], best[2]], method='Nelder-Mead',
                      options={'xatol': 1e-4, 'fatol': 0.1, 'maxiter': 200})
    return result.x[0], result.x[1], result.fun


def make_plot(ells, tt_planck, tt_zspin, output_path="zspin_cmb_comparison.png"):
    """Generate comparison plot."""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("  matplotlib not available — skipping plot")
        return

    dl_p = ells * (ells + 1) * tt_planck / (2 * np.pi)
    dl_z = ells * (ells + 1) * tt_zspin / (2 * np.pi)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8),
                                    gridspec_kw={'height_ratios': [3, 1]})

    ax1.plot(ells[2:2001], dl_p[2:2001], 'b-', lw=1.2,
             label=f'Planck LCDM (H0={H_PLANCK}, Om={0.315:.3f})')
    ax1.plot(ells[2:2001], dl_z[2:2001], 'r--', lw=1.2,
             label=f'Z-Spin (H0={H_ZSPIN}, Om={OMEGA_M_EFF:.4f})')
    ax1.set_ylabel(r'$\mathcal{D}_\ell^{TT}$ [$\mu$K$^2$]', fontsize=13)
    ax1.set_xlim(2, 2000)
    ax1.set_title('Z-Sim v1.0 — CMB TT Power Spectrum', fontsize=14)
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3)

    H0_local = H_ZSPIN * math.exp(A)
    ax1.text(0.02, 0.95,
             f'A = 35/437\nn$_s$ = {NS_ZS}\n'
             f'H$_0^{{local}}$ = {H0_local:.1f} km/s/Mpc',
             transform=ax1.transAxes, fontsize=10, va='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Residual
    mask = (ells >= 2) & (ells <= 2000) & (tt_planck > 0)
    frac = np.zeros_like(ells, dtype=float)
    frac[mask] = (tt_zspin[mask] - tt_planck[mask]) / tt_planck[mask] * 100
    cv = np.zeros_like(ells, dtype=float)
    cv[mask] = np.sqrt(2.0 / (2.0 * ells[mask] + 1.0)) * 100

    ax2.fill_between(ells[2:2001], -cv[2:2001], cv[2:2001],
                     alpha=0.2, color='gray', label=r'Cosmic variance 1$\sigma$')
    ax2.plot(ells[2:2001], frac[2:2001], 'r-', lw=0.8, alpha=0.8)
    ax2.axhline(0, color='k', lw=0.5)
    ax2.set_xlabel(r'Multipole $\ell$', fontsize=13)
    ax2.set_ylabel('Residual [%]', fontsize=11)
    ax2.set_xlim(2, 2000)
    ax2.set_ylim(-10, 10)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=10)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"  Plot saved: {output_path}")
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Z-Spin CMB comparison using CAMB")
    parser.add_argument("--optimize", action="store_true",
                        help="Optimize A_s and tau for Z-Spin")
    parser.add_argument("--output", default="zspin_cmb_comparison.png")
    args = parser.parse_args()

    print("=" * 70)
    print("  Z-Sim v1.0 — CAMB CMB Power Spectrum Comparison")
    print("=" * 70)

    print(f"\n  Planck LCDM: H0={H_PLANCK}, ombh2={OMBH2_PL}, omch2={OMCH2_PL}, ns={NS_PL}")
    print(f"  Z-Spin:      H0={H_ZSPIN}, ombh2={OMBH2_ZS:.6f}, omch2={OMCH2_ZS:.6f}, ns={NS_ZS}")
    print(f"  H0_local = exp(A) × {H_ZSPIN} = {H_ZSPIN * math.exp(A):.2f}")

    # Planck baseline
    print("\n  Computing Planck LCDM spectrum...")
    tt_planck, der_planck = compute_cls(H_PLANCK, OMBH2_PL, OMCH2_PL, NS_PL,
                                         label="Planck")

    if args.optimize:
        print("\n  Optimizing (A_s, tau) for Z-Spin...")
        logAs_opt, tau_opt, chi2_opt = optimize_As_tau(tt_planck)
        As_opt = math.exp(logAs_opt) * 1e-10
        print(f"  Best fit: ln(10^10 A_s) = {logAs_opt:.4f}, tau = {tau_opt:.5f}")
        print(f"  A_s = {As_opt:.4e}, chi2 = {chi2_opt:.1f}")
        tt_zspin, der_zspin = compute_cls(H_ZSPIN, OMBH2_ZS, OMCH2_ZS, NS_ZS,
                                           As=As_opt, tau=tau_opt, label="Z-Spin opt")
    else:
        print("\n  Computing Z-Spin spectrum (Planck A_s, tau defaults)...")
        tt_zspin, der_zspin = compute_cls(H_ZSPIN, OMBH2_ZS, OMCH2_ZS, NS_ZS,
                                           label="Z-Spin")

    # Statistics
    ells = np.arange(LMAX + 1)
    mask = (ells >= 30) & (ells <= 2000) & (tt_planck > 1)
    res_pct = (tt_zspin[mask] - tt_planck[mask]) / tt_planck[mask] * 100
    cv = np.sqrt(2.0 / (2.0 * ells[mask] + 1.0)) * 100
    within = np.sum(np.abs(res_pct) < cv) / len(res_pct) * 100

    print(f"\n  Residual statistics (l=30-2000):")
    print(f"    RMS:  {np.sqrt(np.mean(res_pct ** 2)):.2f}%")
    print(f"    Max:  {np.max(np.abs(res_pct)):.2f}%")
    print(f"    Within cosmic variance: {within:.1f}%")

    print(f"\n  Derived quantities:")
    print(f"    sigma8: Planck={der_planck['sigma8']:.4f}, Z-Spin={der_zspin['sigma8']:.4f}")
    S8_zs = der_zspin['sigma8'] * (OMEGA_M_EFF / 0.3) ** 0.5
    print(f"    S8(Z-Spin) = {S8_zs:.4f}  (face counting predicts: ~0.777)")

    # Plot
    make_plot(ells, tt_planck, tt_zspin, args.output)

    print(f"\n  {'=' * 54}")
    print(f"  TIER-0.7 COMPLETE")
    print(f"  Z-Spin CMB spectrum within cosmic variance: {within:.0f}%")
    print(f"  Next: Cobaya MCMC (cobaya_f32/zspin_mcmc_planck.yaml)")
    print(f"  {'=' * 54}")


if __name__ == "__main__":
    main()
