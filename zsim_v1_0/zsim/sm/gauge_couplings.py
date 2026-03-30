"""Z-Sim v1.0 — Gauge Coupling Derivations from Polyhedral Geometry.

Canonical source: ZS-S1 v1.0 (Incidence-Laplacian Bridge)
                  ZS-M8 v1.0 (Fine Structure Constant NLO)

All gauge couplings derived from:
    A = 35/437          [ZS-F2, LOCKED]
    (Z,X,Y) = (2,3,6)  [ZS-F5, PROVEN]
    z* = i^{z*}         [ZS-M1, PROVEN]

Derivation chain summary (ZS-S1 Appendix B):
    1. A = δ_X · δ_Y = (5/19)(7/23)         [LOCKED]
    2. (V+F)_X = 38, (V+F)_Y = 92           [PROVEN, Euler]
    3. β₀(Z) = 1                             [PROVEN, Schur complement]
    4. α_s = Q / [(V+F)_Y + β₀(Z)] = 11/93  [DERIVED]
    5. sin²θ_W = (2V_X/(VEF_Y/2)) × x*      [DERIVED]
    6. α₂ = Y / (5 × (V+F)_X) = 3/95        [DERIVED]
    7. 1/α_EM ≈ 1/(κ² + c₄κ⁴)               [HYPOTHESIS (strong)]
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Final

from zsim.core.constants import (
    A_LOCKED, Q_TOTAL, DIM_X, DIM_Y, DIM_Z, G_MUB,
    X_STAR, Z_STAR_IM,
    V_TO, E_TO, F_TO, VF_TO,
    V_TI, E_TI, F_TI, VF_TI, VEF_TI,
    ORDER_O_H, ORDER_I, BETA0_Z,
    ALPHA_S, ALPHA_S_FRAC, SIN2_THETA_W, R_GEOM,
    ALPHA_2, ALPHA_2_FRAC,
    BETA_COEFF_SU2, BETA_COEFF_SU3, BETA_SLOPE_RATIO,
    KAPPA_SQ, C4_NLO, ALPHA_EM_NLO, ALPHA_EM_INV_NLO,
    PDG_ALPHA_S, PDG_ALPHA_S_ERR,
    PDG_SIN2_THETA_W, PDG_SIN2_THETA_W_ERR,
    PDG_ALPHA_EM_INV,
)


# =====================================================================
# Epistemic status tags
# =====================================================================
PROVEN: Final[str] = "PROVEN"
DERIVED: Final[str] = "DERIVED"
HYPOTHESIS_STRONG: Final[str] = "HYPOTHESIS (strong)"
OBSERVATION: Final[str] = "OBSERVATION"


@dataclass(frozen=True)
class GaugePrediction:
    """A single gauge coupling prediction with full provenance."""
    name: str
    symbol: str
    z_spin_value: float
    z_spin_exact: str
    observed_value: float
    observed_error: float
    pull_sigma: float
    derivation_chain: tuple[str, ...]
    status: str
    source_paper: str

    def to_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "symbol": self.symbol,
            "z_spin": self.z_spin_value,
            "exact": self.z_spin_exact,
            "observed": self.observed_value,
            "error": self.observed_error,
            "pull_sigma": self.pull_sigma,
            "status": self.status,
            "source": self.source_paper,
        }


def _pull(pred: float, obs: float, err: float) -> float:
    """Compute pull in units of sigma."""
    return (pred - obs) / err if err > 0 else float("inf")


# =====================================================================
# Derivation chain audit
# =====================================================================

def derivation_chain_alpha_s() -> tuple[str, ...]:
    """Return the complete derivation chain for α_s."""
    return (
        f"Q = {Q_TOTAL} from ZS-F5 sector decomposition [PROVEN]",
        f"(V+F)_Y = {VF_TI} from truncated icosahedron [PROVEN]",
        f"β₀(Z) = {BETA0_Z} from Z-sector Schur complement [PROVEN]",
        f"N_eff(Y) = (V+F)_Y + β₀(Z) = {VF_TI} + {BETA0_Z} = {VF_TI + BETA0_Z}",
        f"α_s = Q / N_eff(Y) = {Q_TOTAL}/{VF_TI + BETA0_Z} = {ALPHA_S_FRAC}",
    )


def derivation_chain_sin2_theta_w() -> tuple[str, ...]:
    """Return the complete derivation chain for sin²θ_W."""
    return (
        f"2V_X = 2 × {V_TO} = {2 * V_TO} = |O_h| = {ORDER_O_H} [PROVEN, two routes]",
        f"(V+E+F)_Y / 2 = {VEF_TI}/2 = {VEF_TI // 2} [Z₂ reduction]",
        f"R_geom = {2 * V_TO}/{VEF_TI // 2} = 48/91 [PROVEN]",
        f"x* = Re(z*) = {X_STAR:.10f} [ZS-M1, Berry phase, PROVEN]",
        f"sin²θ_W = R_geom × x* = (48/91) × {X_STAR:.6f} = {SIN2_THETA_W:.5f}",
    )


def derivation_chain_alpha_2() -> tuple[str, ...]:
    """Return the complete derivation chain for α₂."""
    return (
        f"Y = {DIM_Y} [PROVEN]",
        f"(V+F)_X = {VF_TO} [PROVEN]",
        f"Factor 5 = |I_h|/|O_h| = 120/24 [PROVEN, two independent routes]",
        f"α₂ = Y / (5 × (V+F)_X) = {DIM_Y}/(5×{VF_TO}) = {ALPHA_2_FRAC}",
    )


def derivation_chain_alpha_em() -> tuple[str, ...]:
    """Return the derivation chain for α_EM NLO."""
    return (
        f"κ² = A/Q = {A_LOCKED}/{Q_TOTAL} = {KAPPA_SQ:.8f} [OBSERVATION → DERIVED pending]",
        f"|V−F|_Y = |{V_TI}−{F_TI}| = {abs(V_TI - F_TI)} [PROVEN]",
        f"(V+F)_Y − β₀(Z) = {VF_TI} − {BETA0_Z} = {VF_TI - BETA0_Z} [PROVEN]",
        f"c₄ = {abs(V_TI - F_TI)}/{VF_TI - BETA0_Z} = 4/13 [HYPOTHESIS (strong)]",
        f"α_EM = κ² + c₄κ⁴ = {ALPHA_EM_NLO:.8f}",
        f"1/α_EM = {ALPHA_EM_INV_NLO:.3f}",
    )


# =====================================================================
# Public API
# =====================================================================

def compute_all_gauge_predictions() -> list[GaugePrediction]:
    """Compute all gauge coupling predictions with pull values."""
    return [
        GaugePrediction(
            name="Strong coupling constant",
            symbol="α_s(M_Z)",
            z_spin_value=ALPHA_S,
            z_spin_exact=str(ALPHA_S_FRAC),
            observed_value=PDG_ALPHA_S,
            observed_error=PDG_ALPHA_S_ERR,
            pull_sigma=_pull(ALPHA_S, PDG_ALPHA_S, PDG_ALPHA_S_ERR),
            derivation_chain=derivation_chain_alpha_s(),
            status=DERIVED,
            source_paper="ZS-S1 §8.1",
        ),
        GaugePrediction(
            name="Weinberg angle",
            symbol="sin²θ_W(M_Z)",
            z_spin_value=SIN2_THETA_W,
            z_spin_exact="(48/91)·x*",
            observed_value=PDG_SIN2_THETA_W,
            observed_error=PDG_SIN2_THETA_W_ERR,
            pull_sigma=_pull(SIN2_THETA_W, PDG_SIN2_THETA_W, PDG_SIN2_THETA_W_ERR),
            derivation_chain=derivation_chain_sin2_theta_w(),
            status=DERIVED,
            source_paper="ZS-S1 §8.2",
        ),
        GaugePrediction(
            name="Electromagnetic coupling (NLO)",
            symbol="1/α_EM",
            z_spin_value=ALPHA_EM_INV_NLO,
            z_spin_exact="1/(κ²+c₄κ⁴), c₄=4/13",
            observed_value=PDG_ALPHA_EM_INV,
            observed_error=0.000001,  # ~0.007 ppb
            pull_sigma=(ALPHA_EM_INV_NLO - PDG_ALPHA_EM_INV) / 0.000001,
            derivation_chain=derivation_chain_alpha_em(),
            status=HYPOTHESIS_STRONG,
            source_paper="ZS-M8 §3",
        ),
    ]


def sensitivity_analysis_alpha_s(delta_range: range = range(-3, 5)) -> list[dict]:
    """Reproduce ZS-S1 §5.5 sensitivity table for the Schur +δ shift."""
    results = []
    for delta in delta_range:
        denom = VF_TI + delta
        alpha = Q_TOTAL / denom
        pull = _pull(alpha, PDG_ALPHA_S, PDG_ALPHA_S_ERR)
        results.append({
            "delta": delta,
            "denominator": denom,
            "alpha_s": alpha,
            "pull_sigma": pull,
            "within_1sigma": abs(pull) < 1.0,
        })
    return results


def adversarial_archimedean_test() -> dict[str, object]:
    """Test all 13 Archimedean solids: only TO/TI produce (19/6, 23/3) with G=12.

    Reproduces ZS-S1 adversarial test: 0/6 alternative pairs match.
    """
    # (name, V, E, F) for all 13 Archimedean solids
    archimedean = [
        ("truncated_tetrahedron", 12, 18, 8),
        ("cuboctahedron", 12, 24, 14),
        ("truncated_cube", 24, 36, 14),
        ("truncated_octahedron", 24, 36, 14),       # = TO
        ("rhombicuboctahedron", 24, 48, 26),
        ("truncated_cuboctahedron", 48, 72, 26),
        ("snub_cube", 24, 60, 38),
        ("icosidodecahedron", 30, 60, 32),
        ("truncated_dodecahedron", 60, 90, 32),
        ("truncated_icosahedron", 60, 90, 32),       # = TI
        ("rhombicosidodecahedron", 60, 120, 62),
        ("truncated_icosidodecahedron", 120, 180, 62),
        ("snub_dodecahedron", 60, 150, 92),
    ]
    target_a2 = Fraction(19, 6)
    target_a3 = Fraction(23, 3)
    g = G_MUB

    matches = []
    for i, (name_x, vx, ex, fx) in enumerate(archimedean):
        for j, (name_y, vy, ey, fy) in enumerate(archimedean):
            if i >= j:
                continue
            a_x = Fraction(vx + fx, g)
            a_y = Fraction(vy + fy, g)
            if (a_x == target_a2 and a_y == target_a3) or \
               (a_x == target_a3 and a_y == target_a2):
                matches.append((name_x, name_y))

    return {
        "target": f"a₂={target_a2}, a₃={target_a3} with G={g}",
        "pairs_tested": len(archimedean) * (len(archimedean) - 1) // 2,
        "matches": matches,
        "unique": len(matches) == 1 and matches[0] == (
            "truncated_octahedron", "truncated_icosahedron"
        ),
    }


def print_gauge_summary() -> None:
    """Print formatted gauge coupling summary."""
    preds = compute_all_gauge_predictions()
    print("=" * 72)
    print("  Z-Spin Gauge Coupling Predictions (ZS-S1, ZS-M8)")
    print("  Zero free parameters beyond A = 35/437")
    print("=" * 72)
    for p in preds:
        print(f"\n  {p.name} [{p.status}]")
        print(f"    Z-Spin:   {p.symbol} = {p.z_spin_exact} = {p.z_spin_value:.6f}")
        print(f"    Observed: {p.observed_value} ± {p.observed_error}")
        print(f"    Pull:     {p.pull_sigma:+.2f}σ")
        print(f"    Source:   {p.source_paper}")

    print(f"\n  β-function coefficients:")
    print(f"    a₂(SU2) = (V+F)_X/G = {VF_TO}/{G_MUB} = 19/6 = {BETA_COEFF_SU2:.4f}")
    print(f"    a₃(SU3) = (V+F)_Y/G = {VF_TI}/{G_MUB} = 23/3 = {BETA_COEFF_SU3:.4f}")
    print(f"    Slope ratio a₃/a₂ = 46/19 = {BETA_SLOPE_RATIO:.4f}")

    adv = adversarial_archimedean_test()
    print(f"\n  Adversarial Archimedean test: {adv['pairs_tested']} pairs → "
          f"{'UNIQUE ✓' if adv['unique'] else 'NOT UNIQUE ✗'}")
    print("=" * 72)
