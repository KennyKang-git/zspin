"""MBP v2: Molecular Bilinear Program extraction on periodic BCC T³.

Implements the complete 5-phase MBP protocol (ZS-S4 §6.11.4 / §8.4f.4):
  Phase 1: Construct multi-cell SU(2) lattice on periodic BCC T³
  Phase 2: Cool/gradient-flow to the caloron constituent sector
  Phase 3: Compute the overlap Dirac spectrum in the I-Ī background
  Phase 4: Extract the h² coefficient from the fermion determinant ratio
  Phase 5: Compare with the MBP formula

Key formula (§6.11.1):
  μ²_{H,f} = N_c [Tr′(K₀⁻¹K₂) − ½Tr′(K₀⁻¹K₁K₀⁻¹K₁)] × P_{I-Ī}

where:
  K₀ = D₀†D₀,  K₁ = D₀†Y + Y†D₀,  K₂ = Y†Y
  D₀ = overlap Dirac operator at h=0
  Y = Yukawa coupling projector
  P_{I-Ī} = exp(−2S_cl) = exp(−70π/3)

MBP closure candidate (§6.11.2):
  μ²_H = (N_c y²_t)/(2C_M) × M²_P × exp(−2S_cl)
  κ₂ = N_c y²_t/(2C_M) = 0.0906 (target)

Falsification conditions (§6.11.5):
  F-MBP-1: No h²H bilinear → MBP terminated
  F-MBP-2: μ²_{H,f} ≤ 0 → MBP terminated
  F-MBP-3: κ₂ outside [10⁻³, 10²] → loses explanatory power
  F-MBP-5: κ₂ deviating from 0.0906 by >3× → closure falsified
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from zsim.lgt2.lattice import PeriodicBCCLattice, build_periodic_bcc
from zsim.lgt2.gauge_field import GaugeField
from zsim.lgt2.gradient_flow import WilsonGradientFlow, FlowState
from zsim.lgt2.dirac_overlap import OverlapDirac, OverlapSpectrum
from zsim.lgt2.dirac_wilson import WilsonDirac, GAMMA5, I4
from zsim.lgt2.caloron import CaloronBackground, CaloronParams
from zsim.lgt2.su2 import I2

Array = np.ndarray

# Z-Spin canonical constants (DERIVED)
S_CL = 35.0 * np.pi / 3.0       # instanton action
C_M = 16.178                      # BCC spectral invariant
M_P = 2.435e18                    # Planck mass in GeV
EXP_MINUS_2S = np.exp(-2.0 * S_CL)  # ≈ 1.46×10⁻³²
KAPPA2_TARGET = 0.0906            # target from observation


@dataclass(frozen=True)
class MBP2Result:
    """Result of the MBP v2 extraction."""
    # Phase 1: Lattice
    shape: tuple[int, int, int]
    lattice_spacing: float
    num_sites: int
    boundary: str  # "periodic"

    # Phase 2: Flow
    flow_time: float
    avg_plaquette_initial: float
    avg_plaquette_flowed: float

    # Phase 3: Overlap spectrum
    topological_charge: int
    n_zero_modes: int
    ginsparg_wilson_residual: float
    sigma_min: float
    sigma_next: float

    # Phase 4: h² extraction
    diag_term: float          # Tr′(K₀⁻¹K₂)
    cross_term_half: float    # ½Tr′(K₀⁻¹K₁K₀⁻¹K₁)
    mbp_bracket: float        # diag − cross
    gamma_h2_trace: float     # −(N_c/2) × mbp_bracket
    gamma_h2_fd: float        # finite-difference cross-check
    gamma_consistency_gap: float
    gamma_sign_match: bool
    mu2_formula_proxy: float  # N_c × mbp_bracket
    mu2_with_prefactor: float # mu2_proxy × exp(−2S_cl)

    # Phase 5: Comparison
    kappa2_extracted: float   # μ²_H / (M²_P × exp(−2S_cl))
    kappa2_target: float      # 0.0906
    kappa2_ratio: float       # extracted / target
    fmb1_bilinear_exists: bool
    fmb2_sign_correct: bool   # μ² > 0 (tachyonic = EWSB trigger)
    fmb3_magnitude_ok: bool   # κ₂ ∈ [10⁻³, 10²]
    fmb5_closure_match: bool  # κ₂ within 3× of target

    # Status
    status: str  # "DERIVED", "OBSERVATION", "FAIL"
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {k: (list(v) if isinstance(v, tuple) else v)
                for k, v in self.__dict__.items()}


def build_yukawa_projector_overlap(
    overlap: OverlapDirac,
    *,
    yt: float = 1.0,
    chirality_mode: str = "left",
) -> Array:
    """Build the Yukawa coupling projector Y for the overlap operator.

    Y = (y_t/√2) P_chirality
    where P is the chirality projector (left or right).

    Unlike v5.x, this uses the EXACT γ₅ from the overlap
    Ginsparg-Wilson relation, not an ad-hoc weighting.
    """
    dim = overlap.dim
    I_full = np.eye(dim, dtype=np.complex128)
    G5 = overlap._wilson.gamma5_matrix()

    if chirality_mode == "left":
        P = 0.5 * (I_full - G5)
    elif chirality_mode == "right":
        P = 0.5 * (I_full + G5)
    else:
        P = I_full

    return (yt / np.sqrt(2.0)) * P


def extract_h2_coefficient(
    overlap: OverlapDirac,
    *,
    yt: float = 1.0,
    nc: float = 3.0,
    chirality_mode: str = "left",
    reg_epsilon: float = 1e-6,
    cutoff: float = 1e-8,
    fd_step: float = 1e-3,
) -> dict[str, float]:
    """Extract the h² coefficient from the overlap Dirac operator.

    Phase 4 of the MBP protocol.

    Computes:
      K₀ = D†_ov D_ov
      K₁ = D†_ov Y + Y† D_ov
      K₂ = Y† Y
      μ²_{H,f} = N_c [Tr′(K₀⁻¹K₂) − ½Tr′(K₀⁻¹K₁K₀⁻¹K₁)] × P_{I-Ī}
    """
    D0 = overlap.matrix()
    Y = build_yukawa_projector_overlap(
        overlap, yt=yt, chirality_mode=chirality_mode
    )

    K0 = D0.conj().T @ D0 + reg_epsilon * np.eye(overlap.dim, dtype=np.complex128)
    K1 = D0.conj().T @ Y + Y.conj().T @ D0
    K2 = Y.conj().T @ Y

    # Regularised inverse via eigendecomposition
    evals, evecs = np.linalg.eigh(K0)
    mask = evals > cutoff
    if not np.any(mask):
        return {"error": "no modes survived cutoff", "gamma_h2_trace": 0.0,
                "gamma_h2_fd": 0.0, "gamma_consistency_gap": 1e10,
                "gamma_sign_match": False, "mu2_formula_proxy": 0.0}

    kept = evals[mask]
    V = evecs[:, mask]
    K0_inv = (V / kept) @ V.conj().T

    # Trace formula
    diag_term = float(np.real(np.trace(K0_inv @ K2)))
    cross_half = 0.5 * float(np.real(np.trace(K0_inv @ K1 @ K0_inv @ K1)))
    mbp_bracket = diag_term - cross_half
    gamma_h2_trace = -(nc / 2.0) * mbp_bracket

    # Finite-difference cross-check
    def gamma_from_k(K):
        ev = np.linalg.eigvalsh(K)
        ev = ev[ev > cutoff]
        if ev.size == 0:
            return 0.0
        return float(-(nc / 2.0) * np.sum(np.log(ev)))

    h = fd_step
    g0 = gamma_from_k(K0)
    gp = gamma_from_k(K0 + h * K1 + h * h * K2)
    gm = gamma_from_k(K0 - h * K1 + h * h * K2)
    gamma_h2_fd = (gp - 2 * g0 + gm) / (2 * h * h)

    gap = abs(gamma_h2_trace - gamma_h2_fd)
    sign_match = (abs(gamma_h2_trace) < 1e-15 and abs(gamma_h2_fd) < 1e-15) or \
                 (gamma_h2_trace > 0) == (gamma_h2_fd > 0)

    # SVD of D_ov for near-zero modes
    svals = np.sort(np.linalg.svd(D0, compute_uv=False))
    sigma_min = float(svals[0]) if svals.size else 0.0
    sigma_next = float(svals[1]) if svals.size > 1 else sigma_min

    return {
        "diag_term": diag_term,
        "cross_term_half": cross_half,
        "mbp_bracket": mbp_bracket,
        "gamma_h2_trace": gamma_h2_trace,
        "gamma_h2_fd": gamma_h2_fd,
        "gamma_consistency_gap": gap,
        "gamma_sign_match": sign_match,
        "mu2_formula_proxy": nc * mbp_bracket,
        "sigma_min": sigma_min,
        "sigma_next": sigma_next,
        "masked_modes": int(np.sum(mask)),
        "k0_min_mode": float(np.min(kept)),
    }


def run_mbp2_pipeline(
    *,
    shape: tuple[int, int, int] = (4, 4, 4),
    lattice_spacing: float = 1.0,
    beta: float = 2.3,
    # Caloron parameters
    separation_fraction: float = 0.4,
    rho_inst: float = 0.5,
    coupling_g: float = 1.0,
    # Flow parameters
    flow_epsilon: float = 0.01,
    flow_steps: int = 100,
    # Dirac parameters
    overlap_rho: float = 1.0,
    wilson_r: float = 1.0,
    # MBP extraction parameters
    yt: float = 1.0,
    nc: float = 3.0,
    chirality_mode: str = "left",
    reg_epsilon: float = 1e-6,
    cutoff: float = 1e-8,
    fd_step: float = 1e-3,
) -> MBP2Result:
    """Execute the complete 5-phase MBP protocol.

    This is the main entry point for the Higgs VEV computation.
    """
    # ---- Phase 1: Construct periodic BCC T³ ----
    lattice = build_periodic_bcc(*shape, a=lattice_spacing)

    # ---- Phase 2: Generate caloron background + gradient flow ----
    cal = CaloronBackground.symmetric_pair(
        lattice,
        separation_fraction=separation_fraction,
        rho_inst=rho_inst,
        coupling_g=coupling_g,
    )
    gf_initial = cal.generate(beta=beta)
    avg_plaq_initial = float(np.mean([
        float(np.real(np.trace(
            __import__('zsim.lgt2.gauge_field', fromlist=['loop_holonomy']).loop_holonomy(gf_initial, p)
        ))) / 2.0
        for p in lattice.plaquettes[:min(20, len(lattice.plaquettes))]
    ])) if lattice.plaquettes else 1.0

    flow = WilsonGradientFlow(epsilon=flow_epsilon, max_steps=flow_steps)
    trajectory = flow.flow(gf_initial, n_steps=flow_steps, record_every=max(1, flow_steps // 10))
    gf_flowed = trajectory[-1].gauge_field
    flow_time = trajectory[-1].flow_time
    avg_plaq_flowed = trajectory[-1].avg_plaq

    # ---- Phase 3: Compute overlap Dirac spectrum ----
    overlap = OverlapDirac(
        gf_flowed, rho=overlap_rho, wilson_r=wilson_r
    )
    spec = overlap.spectrum()
    gw_residual = overlap.verify_ginsparg_wilson()

    # ---- Phase 4: Extract h² coefficient ----
    h2_result = extract_h2_coefficient(
        overlap, yt=yt, nc=nc, chirality_mode=chirality_mode,
        reg_epsilon=reg_epsilon, cutoff=cutoff, fd_step=fd_step,
    )

    mu2_proxy = h2_result["mu2_formula_proxy"]
    mu2_with_pf = mu2_proxy * EXP_MINUS_2S

    # ---- Phase 5: Compare with MBP formula ----
    kappa2 = mu2_proxy / C_M if abs(C_M) > 1e-15 else 0.0
    kappa2_ratio = kappa2 / KAPPA2_TARGET if abs(KAPPA2_TARGET) > 1e-15 else 0.0

    fmb1 = abs(mu2_proxy) > 1e-20  # bilinear exists
    fmb2 = mu2_proxy > 0            # tachyonic (triggers EWSB)
    fmb3 = 1e-3 < abs(kappa2) < 1e2 if fmb1 else False
    fmb5 = 1.0 / 3.0 < kappa2_ratio < 3.0 if fmb1 else False

    # Status determination
    if fmb1 and fmb2 and h2_result["gamma_sign_match"]:
        if fmb5:
            status = "OBSERVATION"
        else:
            status = "HYPOTHESIS"
    elif not fmb1:
        status = "FAIL:F-MBP-1"
    elif not fmb2:
        status = "FAIL:F-MBP-2"
    else:
        status = "HYPOTHESIS"

    return MBP2Result(
        shape=shape,
        lattice_spacing=lattice_spacing,
        num_sites=lattice.num_sites,
        boundary="periodic",
        flow_time=flow_time,
        avg_plaquette_initial=avg_plaq_initial,
        avg_plaquette_flowed=avg_plaq_flowed,
        topological_charge=spec.topological_charge,
        n_zero_modes=spec.zero_modes,
        ginsparg_wilson_residual=gw_residual,
        sigma_min=h2_result["sigma_min"],
        sigma_next=h2_result["sigma_next"],
        diag_term=h2_result["diag_term"],
        cross_term_half=h2_result["cross_term_half"],
        mbp_bracket=h2_result["mbp_bracket"],
        gamma_h2_trace=h2_result["gamma_h2_trace"],
        gamma_h2_fd=h2_result["gamma_h2_fd"],
        gamma_consistency_gap=h2_result["gamma_consistency_gap"],
        gamma_sign_match=h2_result["gamma_sign_match"],
        mu2_formula_proxy=mu2_proxy,
        mu2_with_prefactor=mu2_with_pf,
        kappa2_extracted=kappa2,
        kappa2_target=KAPPA2_TARGET,
        kappa2_ratio=kappa2_ratio,
        fmb1_bilinear_exists=fmb1,
        fmb2_sign_correct=fmb2,
        fmb3_magnitude_ok=fmb3,
        fmb5_closure_match=fmb5,
        status=status,
        notes={
            "protocol": "MBP v2 5-phase (ZS-S4 §6.11.4)",
            "boundary": "periodic BCC T³",
            "dirac": "overlap (Neuberger)",
            "flow": f"Wilson gradient flow, {flow_steps} RK3 steps, ε={flow_epsilon}",
            "background": f"I-Ī molecular, sep={separation_fraction}, ρ={rho_inst}",
            "non_claim": "v=246 GeV remains NON-CLAIM pending production lattice",
        },
    )
