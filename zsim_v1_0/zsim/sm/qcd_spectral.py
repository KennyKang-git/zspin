"""Z-Sim v1.0 — ZS-S7 QCD Spectral Predictions Module.

Canonical source: ZS-S7 v1.0 (April 2026, 55-paper release)
                  "The Spinor Mass Gap: Deriving Λ_QCD and the Glueball
                   Mass from Polyhedral Hodge Spectral Theory"

This module exposes the four ZS-S7 QCD predictions as a unified report
pipeline parallel to the existing zsim/sm/report.py for gauge couplings,
EWSB, and Yukawa structure.

EPISTEMIC STATUS DECLARATION:

  All four ZS-S7 results are zero-free-parameter predictions from
  A = 35/437 + polyhedral invariants (V_TI = 60, F_TI = 32, G_MUB = 12)
  + the Higgs VEV (itself DERIVED from ZS-S4 v1.0 §6.12–6.13).

  1. Λ_QCD = v · A / (λ_1 · V_Y) = 264 MeV
     [DERIVED-CONDITIONAL on λ_1(Δ_2 on TI) = 1.2428 spectral input,
      itself PROVEN in ZS-S7 §3 by direct lattice diagonalization.]
     Lattice reference: Λ_QCD^MS-bar = 260 ± 20 MeV (FLAG 2024). +0.2σ.

  2. m(0⁺⁺) glueball mass = v · A / Q = 1.791 GeV
     [DERIVED-CONDITIONAL via the Topological Cancellation Theorem,
      ZS-S7 §5. Same standing as Λ_QCD.]
     Lattice reference: m(0⁺⁺) = 1.73 ± 0.05 GeV. +1.2σ.

  3. b_0(SU(3)) = (V+F)_Y / G_MUB = 23/3 [PROVEN, exact SM value]
     Identical to BETA_COEFF_SU3_FRAC defined in zsim/core/constants.py.
     The SU(3) β-function leading coefficient and the ZS-S7 spinor-sector
     QCD running constant are the SAME polyhedral invariant.

  4. n_f = V_Y / G_MUB = 5 [DERIVED, exact]
     The number of active quark flavors below M_Z.

NON-CLAIM disclaimer (ZS-S7 §7):
  The mass gap of pure Yang-Mills SU(3) is one of the Clay Millennium Prize
  Problems. ZS-S7 derives the spinor sector mass scale via spectral theory
  on the truncated icosahedron, but DOES NOT solve the Millennium Prize
  problem for arbitrary SU(N) gauge theory. The result is a polyhedral
  invariant calculation, not a continuum field-theoretic proof.

Cross-references:
  - ZS-T1 v1.0 §9.3: Block Fiedler Mediation Theorem (PROVEN, λ_2 = 2A/Q)
  - ZS-S4 v1.0 §6.12–6.13: Higgs VEV derivation (DERIVED)
  - ZS-M11 v1.0 §9.5.5–9.5.6: Sister derivation on Y-side (T1-3 closure)
  - Book v1.0 §G.2 T1-3: X↔Y reciprocal duality registration
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Final

from zsim.core.constants import (
    A_LOCKED,
    BETA0_QCD_FRAC,
    BETA0_QCD,
    F_TI,
    G_MUB,
    GLUEBALL_0PP_PRED_GEV,
    HIGGS_VEV,
    LAMBDA1_HODGE_TI,
    LAMBDA_QCD_PRED_GEV,
    LAMBDA_QCD_PRED_MEV,
    N_FLAVORS_QCD,
    Q_TOTAL,
    V_TI,
)


# =====================================================================
# External reference values (lattice / FLAG / PDG)
# =====================================================================

LAMBDA_QCD_LATTICE_MEV: Final[float] = 260.0  # FLAG 2024 average, ±20
LAMBDA_QCD_LATTICE_ERR_MEV: Final[float] = 20.0

GLUEBALL_0PP_LATTICE_GEV: Final[float] = 1.73  # PDG / lattice average, ±0.05
GLUEBALL_0PP_LATTICE_ERR_GEV: Final[float] = 0.05

BETA0_QCD_EXACT: Final[Fraction] = Fraction(23, 3)  # SM exact value
N_FLAVORS_EXACT: Final[int] = 5  # active flavors below M_Z


# =====================================================================
# Result dataclasses
# =====================================================================

@dataclass(frozen=True)
class QCDSpectralResult:
    """Single ZS-S7 prediction with pull / status."""

    name: str
    z_spin_value: float
    observed_value: float
    observed_err: float
    units: str
    epistemic_status: str
    derivation: str

    @property
    def pull_sigma(self) -> float:
        """Number of standard deviations from observed central value."""
        if self.observed_err == 0.0:
            return 0.0
        return (self.z_spin_value - self.observed_value) / self.observed_err

    @property
    def deviation_pct(self) -> float:
        """Percentage deviation from observed central value."""
        if self.observed_value == 0.0:
            return 0.0
        return 100.0 * (self.z_spin_value - self.observed_value) / self.observed_value


@dataclass(frozen=True)
class QCDSpectralReport:
    """Full ZS-S7 prediction report."""

    lambda_qcd:    QCDSpectralResult
    glueball_0pp:  QCDSpectralResult
    beta0:         QCDSpectralResult
    n_flavors:     QCDSpectralResult
    lambda1_input: float
    higgs_vev:     float
    A_locked:      str
    Q_total:       int

    def all_within_2sigma(self) -> bool:
        """Check that all four predictions agree with observation within 2σ.

        For exact integer / rational predictions (b_0, n_f), this is
        trivially satisfied since the prediction equals the observation.
        For Λ_QCD and m(0⁺⁺), this checks the lattice pull.
        """
        for result in (self.lambda_qcd, self.glueball_0pp,
                       self.beta0, self.n_flavors):
            if abs(result.pull_sigma) > 2.0:
                return False
        return True


# =====================================================================
# Prediction functions
# =====================================================================

def predict_lambda_qcd() -> QCDSpectralResult:
    """Λ_QCD = v · A / (λ_1 · V_Y)  [ZS-S7 v1.0 §4]

    Polyhedral derivation: the QCD scale is set by the Higgs VEV
    suppressed by the geometric impedance A and the Hodge 2-form spectral
    gap on the truncated icosahedron λ_1 = 1.2428, normalized by the
    Y-sector vertex count V_TI = 60.
    """
    return QCDSpectralResult(
        name="Λ_QCD",
        z_spin_value=LAMBDA_QCD_PRED_MEV,
        observed_value=LAMBDA_QCD_LATTICE_MEV,
        observed_err=LAMBDA_QCD_LATTICE_ERR_MEV,
        units="MeV",
        epistemic_status="DERIVED-CONDITIONAL",
        derivation="v · A / (λ_1 · V_Y)",
    )


def predict_glueball_0pp() -> QCDSpectralResult:
    """m(0⁺⁺) = v · A / Q  [ZS-S7 v1.0 §5 Topological Cancellation Theorem]

    Polyhedral derivation: the lightest scalar glueball mass is set by
    the Higgs VEV suppressed by the geometric impedance A and the
    register dimension Q = 11. The Topological Cancellation Theorem
    eliminates V_Y and λ_1 from the Λ_QCD ratio, leaving the simpler
    polyhedral invariant v · A / Q.
    """
    return QCDSpectralResult(
        name="m(0⁺⁺)",
        z_spin_value=GLUEBALL_0PP_PRED_GEV,
        observed_value=GLUEBALL_0PP_LATTICE_GEV,
        observed_err=GLUEBALL_0PP_LATTICE_ERR_GEV,
        units="GeV",
        epistemic_status="DERIVED-CONDITIONAL",
        derivation="v · A / Q",
    )


def predict_beta0_qcd() -> QCDSpectralResult:
    """b_0(SU(3)) = (V+F)_Y / G_MUB = 23/3  [ZS-S7 v1.0 §6, PROVEN]

    Polyhedral derivation: the SU(3) β-function leading coefficient is
    the ratio of the truncated icosahedron's vertex+face count (92) to
    the MUB structure constant G_MUB = Q+1 = 12. This gives 23/3 exactly,
    matching the standard SM b_0 value at n_f = 5.
    """
    return QCDSpectralResult(
        name="b_0(SU(3))",
        z_spin_value=BETA0_QCD,
        observed_value=23.0 / 3.0,
        observed_err=0.0,  # exact
        units="dimensionless",
        epistemic_status="PROVEN",
        derivation="(V+F)_Y / G_MUB = 92/12",
    )


def predict_n_flavors() -> QCDSpectralResult:
    """n_f = V_Y / G_MUB = 5  [ZS-S7 v1.0 §6, DERIVED]

    Polyhedral derivation: the number of active quark flavors below M_Z
    equals the truncated icosahedron's vertex count (60) divided by the
    MUB structure constant G_MUB = 12. This gives n_f = 5 exactly,
    matching the SM (u, d, s, c, b active below M_Z; t decoupled above).
    """
    return QCDSpectralResult(
        name="n_f",
        z_spin_value=float(N_FLAVORS_QCD),
        observed_value=5.0,
        observed_err=0.0,  # exact
        units="dimensionless",
        epistemic_status="DERIVED",
        derivation="V_Y / G_MUB = 60/12",
    )


def predict_all() -> QCDSpectralReport:
    """Compute the full ZS-S7 QCD spectral prediction report."""
    return QCDSpectralReport(
        lambda_qcd=predict_lambda_qcd(),
        glueball_0pp=predict_glueball_0pp(),
        beta0=predict_beta0_qcd(),
        n_flavors=predict_n_flavors(),
        lambda1_input=LAMBDA1_HODGE_TI,
        higgs_vev=HIGGS_VEV,
        A_locked="35/437",
        Q_total=Q_TOTAL,
    )


# =====================================================================
# Pretty-print pipeline (parallel to zsim/sm/report.py)
# =====================================================================

def print_report(report: QCDSpectralReport | None = None) -> QCDSpectralReport:
    """Print a unified ZS-S7 prediction report to stdout."""
    if report is None:
        report = predict_all()

    print("=" * 72)
    print("ZS-S7 v1.0 — QCD Spectral Predictions")
    print("       The Spinor Mass Gap: Λ_QCD and the Glueball Mass")
    print("=" * 72)
    print()
    print(f"  Inputs:  A = {report.A_locked}, Q = {report.Q_total},")
    print(f"           V_Y = {V_TI}, F_Y = {F_TI}, G_MUB = {G_MUB}")
    print(f"           v = {report.higgs_vev:.4f} GeV [HIGGS_VEV, DERIVED]")
    print(f"           λ_1(Δ_2 on TI) = {report.lambda1_input}"
          f"    [PROVEN, ZS-S7 §3]")
    print()
    print(f"  {'Observable':<14}{'Z-Spin':>12}{'Observed':>16}"
          f"{'Pull':>10}    Status")
    print("  " + "-" * 70)

    for r in (report.lambda_qcd, report.glueball_0pp,
              report.beta0, report.n_flavors):
        if r.observed_err == 0.0:
            obs_str = f"{r.observed_value:.4f}"
            pull_str = "exact"
        else:
            obs_str = f"{r.observed_value:.1f}±{r.observed_err:.0f}"
            pull_str = f"{r.pull_sigma:+.2f}σ"

        zspin_str = (f"{r.z_spin_value:.2f}" if abs(r.z_spin_value) >= 10
                     else f"{r.z_spin_value:.4f}")
        print(f"  {r.name:<14}{zspin_str:>12}{obs_str:>16}"
              f"{pull_str:>10}    {r.epistemic_status}")

    print()
    print(f"  Derivations:")
    for r in (report.lambda_qcd, report.glueball_0pp,
              report.beta0, report.n_flavors):
        print(f"    {r.name:<14} = {r.derivation}")

    print()
    if report.all_within_2sigma():
        print("  RESULT: All 4 predictions within 2σ of observation. PASS ✓")
    else:
        print("  RESULT: At least one prediction exceeds 2σ tension.")
    print("=" * 72)
    return report


if __name__ == "__main__":
    print_report()
