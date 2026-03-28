"""Z-Sim v3.1 — Canonical Field Inflation Module.

Full numerical slow-roll via canonical field phi transformation.
Uses ANALYTICAL derivatives (no finite differences) for stability.

The Z-Spin Einstein-frame action has non-canonical kinetic term K(eps):
  S_E = int d4x sqrt(-g_E) [R_E/2 - K(eps)(d_eps)^2/2 - V_E(eps)]

Canonical field phi defined by: dphi/deps = sqrt(K(eps))
  where K(eps) = 1/(1+A*eps^2) + 6A^2*eps^2/(1+A*eps^2)^2

Source: ZS-U1 S2, Paper 24 Appendix A, Paper 18 S2.1
Status: DERIVED
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import math

from zsim.core.constants import A_LOCKED, LAMBDA_POTENTIAL
from zsim.kernel.inflation import V_einstein, K_einstein


def canonical_field_integrand(eps: float, A: float = A_LOCKED) -> float:
    """dphi/deps = sqrt(K(eps))."""
    K = K_einstein(eps, A)
    return math.sqrt(max(K, 0.0))


def eps_to_phi(eps: float, A: float = A_LOCKED, eps_ref: float = 1.0) -> float:
    """Compute canonical field phi from eps via numerical integration."""
    if abs(eps - eps_ref) < 1e-12:
        return 0.0
    result, _ = quad(canonical_field_integrand, eps_ref, eps, args=(A,),
                     limit=200, epsabs=1e-14, epsrel=1e-12)
    return result


# ---- Analytical derivatives for numerical stability ----

def _dV_E_deps(eps: float, A: float, lam: float) -> float:
    """dV_E/deps = lam * eps * (eps^2-1) * (1+A) / (1+A*eps^2)^3.

    Derived analytically from V_E = (lam/4)(eps^2-1)^2/(1+A*eps^2)^2.
    """
    F = 1.0 + A * eps * eps
    u = eps * eps - 1.0
    return lam * eps * u * (1.0 + A) / (F * F * F)


def _d2V_E_deps2(eps: float, A: float, lam: float) -> float:
    """d^2 V_E / deps^2, fully analytical."""
    F = 1.0 + A * eps * eps
    u = eps * eps - 1.0
    e2 = eps * eps

    # Product rule: d/deps [lam * eps * u * (1+A) / F^3]
    # Let g = eps * u = eps^3 - eps, h = (1+A)/F^3
    # dg/deps = 3*eps^2 - 1
    # dh/deps = (1+A) * (-3) * F^(-4) * 2*A*eps = -6*A*eps*(1+A)/F^4
    dg = 3.0 * e2 - 1.0
    g = eps * u
    F3 = F * F * F
    F4 = F3 * F
    c = 1.0 + A

    return lam * c * (dg / F3 - 6.0 * A * eps * g / F4)


def _dK_deps(eps: float, A: float) -> float:
    """dK/deps, fully analytical.

    K = 1/F + 6A^2 eps^2 / F^2, F = 1+A*eps^2.
    """
    F = 1.0 + A * eps * eps
    F2 = F * F
    F3 = F2 * F
    A2 = A * A

    # d(1/F)/deps = -2*A*eps/F^2
    term1 = -2.0 * A * eps / F2

    # d(6*A^2*eps^2/F^2)/deps = 12*A^2*eps*(1 - A*eps^2)/F^3
    term2 = 12.0 * A2 * eps * (1.0 - A * eps * eps) / F3

    return term1 + term2


def slow_roll_canonical(eps: float, A: float = A_LOCKED,
                        lam: float = LAMBDA_POTENTIAL) -> dict:
    """Compute slow-roll parameters using ANALYTICAL derivatives.

    eps_V = (1/2)(V'/V)^2  where ' = d/dphi = (1/sqrt(K))(d/deps)
    eta_V = V''/V

    [STATUS: DERIVED]
    """
    K = K_einstein(eps, A)
    V = V_einstein(eps, A, lam)

    if V < 1e-50 or K < 1e-50:
        return {"eps_V": 0.0, "eta_V": 0.0, "n_s": 1.0, "r": 0.0}

    dV = _dV_E_deps(eps, A, lam)
    d2V = _d2V_E_deps2(eps, A, lam)
    dK = _dK_deps(eps, A)

    # V' = dV/dphi = (1/sqrt(K)) dV/deps
    V_prime = dV / math.sqrt(K)

    # V'' = (1/K)(d2V/deps2 - (dK/(2K)) * dV/deps)
    V_double_prime = (d2V - (dK / (2.0 * K)) * dV) / K

    eps_V = 0.5 * (V_prime / V) ** 2
    eta_V = V_double_prime / V

    n_s = 1.0 - 6.0 * eps_V + 2.0 * eta_V
    r = 16.0 * eps_V

    return {
        "eps_V": eps_V,
        "eta_V": eta_V,
        "n_s": n_s,
        "r": r,
        "V": V,
        "V_prime": V_prime,
        "K": K,
    }


def find_epsilon_at_Nstar(N_star: float, A: float = A_LOCKED,
                           lam: float = LAMBDA_POTENTIAL) -> float:
    """Find field value eps* where N* e-folds remain before inflation ends.

    Uses scipy.optimize.brentq for robust root-finding (replaces manual bisection).
    N* = integral_{eps_end}^{eps*} (V/V') K(eps) deps
    Inflation ends when eps_V = 1.
    [STATUS: DERIVED]
    """
    # Step 1: Find eps_end where eps_V = 1 using brentq
    def eps_V_minus_1(e):
        sr = slow_roll_canonical(e, A, lam)
        return sr["eps_V"] - 1.0

    # eps_V is small far from attractor, grows near it
    # Search for the crossing point
    eps_end = brentq(eps_V_minus_1, 1.001, 30.0, xtol=1e-12, rtol=1e-12)

    # Step 2: Integrate N(eps) and find eps* via brentq
    def N_integrand(eps):
        V = V_einstein(eps, A, lam)
        dV = _dV_E_deps(eps, A, lam)
        K = K_einstein(eps, A)
        if abs(dV) < 1e-50:
            return 0.0
        return V * K / dV

    def N_residual(eps_star):
        N_computed, _ = quad(N_integrand, eps_end, eps_star, limit=300,
                            epsabs=1e-12, epsrel=1e-10)
        return N_computed - N_star

    # eps* is far from attractor (large eps)
    eps_star = brentq(N_residual, eps_end + 0.01, 200.0, xtol=1e-10, rtol=1e-10)
    return eps_star


def compute_full_inflation(N_star_values=None, A: float = A_LOCKED,
                           lam: float = LAMBDA_POTENTIAL) -> list:
    """Compute full numerical inflation observables for multiple N*.

    Returns list of dicts with n_s, r, eps_V, eta_V, eps_field for each N*.
    [STATUS: DERIVED -- full canonical field treatment, analytical derivatives]
    """
    if N_star_values is None:
        N_star_values = [50, 55, 60, 65]

    results = []
    for N_star in N_star_values:
        eps_star = find_epsilon_at_Nstar(N_star, A, lam)
        sr = slow_roll_canonical(eps_star, A, lam)

        result = {
            "N_star": N_star,
            "epsilon_field": eps_star,
            "phi_canonical": eps_to_phi(eps_star, A),
            "n_s": sr["n_s"],
            "r": sr["r"],
            "eps_V": sr["eps_V"],
            "eta_V": sr["eta_V"],
            "method": "canonical_field_analytical_derivatives",
            "status": "DERIVED",
        }
        results.append(result)

    return results


def make_inflation_plots(results: list, output_dir: str):
    """Generate inflation diagnostic plots."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import os

    os.makedirs(output_dir, exist_ok=True)

    eps_arr = np.linspace(0.01, 15.0, 500)
    V_arr = [V_einstein(e) for e in eps_arr]
    K_arr = [K_einstein(e) for e in eps_arr]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    ax1.plot(eps_arr, V_arr, 'b-', linewidth=2)
    ax1.set_xlabel(r'$\varepsilon$', fontsize=12)
    ax1.set_ylabel(r'$V_E(\varepsilon)$', fontsize=12)
    ax1.set_title('Einstein-Frame Potential', fontsize=13)
    ax1.set_xlim(0, 15)
    ax1.grid(True, alpha=0.3)
    ax1.axvline(x=1.0, color='r', linestyle='--', alpha=0.5, label=r'$\varepsilon=1$')
    for r in results:
        ax1.axvline(x=r["epsilon_field"], color='g', linestyle=':', alpha=0.6)
        ax1.annotate(f'N*={r["N_star"]}', xy=(r["epsilon_field"], V_einstein(r["epsilon_field"])),
                     fontsize=8, color='green')
    ax1.legend()

    ax2.plot(eps_arr, K_arr, 'r-', linewidth=2)
    ax2.set_xlabel(r'$\varepsilon$', fontsize=12)
    ax2.set_ylabel(r'$K(\varepsilon)$', fontsize=12)
    ax2.set_title('Kinetic Metric', fontsize=13)
    ax2.set_xlim(0, 15)
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, 'inflation_potential.png'), dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 6))
    N_stars = [r["N_star"] for r in results]
    n_s_vals = [r["n_s"] for r in results]
    r_vals = [r["r"] for r in results]

    ax.plot(n_s_vals, r_vals, 'ro-', markersize=8, linewidth=2, label='Z-Spin (canonical)')
    for r in results:
        ax.annotate(f'N*={r["N_star"]}', xy=(r["n_s"], r["r"]),
                    xytext=(5, 5), textcoords='offset points', fontsize=9)

    ax.axvspan(0.9607, 0.9691, alpha=0.15, color='blue', label=r'Planck 1$\sigma$')
    ax.axhline(y=0.036, color='orange', linestyle='--', alpha=0.5, label='BK18 limit')
    ax.set_xlabel(r'$n_s$', fontsize=14)
    ax.set_ylabel(r'$r$', fontsize=14)
    ax.set_title('Z-Sim v3.1 Inflation: $n_s$-$r$ Plane', fontsize=14)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.94, 0.98)
    ax.set_ylim(0, 0.05)

    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, 'inflation_ns_r.png'), dpi=150)
    plt.close(fig)
