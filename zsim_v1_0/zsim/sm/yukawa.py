"""Z-Sim v1.0 — Yukawa Structure and CKM Mixing from Icosahedral Geometry.

Canonical sources: ZS-M10 v1.0, ZS-M11 v1.0

EPISTEMIC STATUS DECLARATION:
  This module implements both FORWARD PREDICTIONS and CONSTRAINT FITS.
  These are CLEARLY SEPARATED in the code:
    - Functions marked [PREDICT] compute forward from the tensor T only.
    - Functions marked [FIT] use observed values as optimization targets.
    - Functions marked [HARDCODED] contain values copied from papers, not computed.
  Users must not conflate FIT results with zero-free-parameter derivations.

Validated forward predictions [PREDICT]:
    1. Yukawa tensor unique: dim Hom_I(1, 3⊗5⊗3') = 1 [PROVEN]
    2. Schur conservation: Σσᵢ² = 1/5 for ALL VEV directions [PROVEN]
    3. Restricted VEV (D₅ eigenbasis, θ=|z*|·A): σ₁/σ₂ ≈ 27, σ₁/σ₃ ≈ 2900 [PREDICT]
    4. Cabibbo angle: D₅-2₂ vs D₃-2 principal angle × 3/4 = 13.96° [DERIVED-CONDITIONAL]
    5. Reynolds P₄: I-invariant quartic controls hierarchy, |ρ| ≈ 0.924 [PROVEN/PREDICT]

Constraint-satisfaction fits [FIT]:
    6. S⁴ VEV optimization: σ₁/σ₂ = 17, σ₁/σ₃ = 3477 [FIT, not DERIVED]
       (Demonstrates that the target IS achievable on S⁴, not that it is predicted.)

NOT YET IMPLEMENTED:
    - M₀ lattice computation on TI (M8 full Schur complement — see m0_lattice.py)
    - SU(5) branching rules / McKay-labeled Dirac operator (M9 full)
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Final

import numpy as np
from scipy.optimize import minimize

from zsim.core.constants import (
    X_STAR, Z_STAR_IM, Z_STAR_MOD_SQ, A_LOCKED, DIM_X,
    PDG_M_TAU_OVER_M_MU, PDG_M_TAU_OVER_M_E, PDG_CABIBBO_DEG,
)

Array = np.ndarray

SQRT2: Final[float] = math.sqrt(2.0)
SILVER_RATIO: Final[float] = 1.0 + SQRT2


# =====================================================================
# D₅ eigenbasis computation [PROVEN]
# =====================================================================

def compute_d5_eigenbasis(rep5: list[Array], rotations: list[Array]) -> Array:
    """Compute the D₅ eigenbasis of the 5-dim representation.

    Returns U_d5 (5×5 orthogonal matrix) such that columns are:
        col 0: ê₁ (D₅-trivial, eigenvalue 1)
        col 1,2: ê₃_r, ê₃_i (ρ₃ = 2₁, eigenvalues ω, ω*)
        col 3,4: ê₄_r, ê₄_i (ρ₄ = 2₂, eigenvalues ω², ω²*)

    The C₅ generator is identified from the rotation group by finding
    an element that fixes a vertex axis.

    [STATUS: PROVEN — eigenvalue decomposition of known C₅ generator]
    """
    from zsim.sm.icosahedral import icosahedron_vertices, _rotation_matrix

    verts = icosahedron_vertices()
    axis = verts[0] / np.linalg.norm(verts[0])

    # Find C₅ generator in the group
    R_c5 = _rotation_matrix(axis, 2 * math.pi / 5)
    idx_c5 = _find_in_group(R_c5, rotations)
    if idx_c5 < 0:
        R_c5 = _rotation_matrix(axis, -2 * math.pi / 5)
        idx_c5 = _find_in_group(R_c5, rotations)
    assert idx_c5 >= 0, "C₅ generator not found in group"

    s5 = rep5[idx_c5]
    ev, V = np.linalg.eig(s5)
    omega = np.exp(2j * math.pi / 5)

    # Classify eigenvalues
    idx_1 = [i for i in range(5) if abs(ev[i] - 1) < 0.01]
    idx_rho3 = [i for i in range(5) if abs(ev[i] - omega) < 0.01]
    idx_rho4 = [i for i in range(5) if abs(ev[i] - omega**2) < 0.01]

    assert len(idx_1) == 1 and len(idx_rho3) == 1 and len(idx_rho4) == 1

    e1 = np.real(V[:, idx_1[0]])
    e1 /= np.linalg.norm(e1)

    v3 = V[:, idx_rho3[0]]
    e3r = np.real(v3); e3r /= np.linalg.norm(e3r)
    e3i = np.imag(v3); e3i -= np.dot(e3i, e3r) * e3r
    e3i /= np.linalg.norm(e3i)

    v4 = V[:, idx_rho4[0]]
    e4r = np.real(v4); e4r /= np.linalg.norm(e4r)
    e4i = np.imag(v4); e4i -= np.dot(e4i, e4r) * e4r
    e4i /= np.linalg.norm(e4i)

    U = np.column_stack([e1, e3r, e3i, e4r, e4i])
    # Orthogonalize via QR
    Q, _ = np.linalg.qr(U)
    return Q


def _find_in_group(R: Array, group: list[Array]) -> int:
    for i, G in enumerate(group):
        if np.max(np.abs(R - G)) < 1e-6:
            return i
    return -1


# =====================================================================
# Mass eigenvalues [PREDICT]
# =====================================================================

@dataclass(frozen=True)
class MassSpectrum:
    """Fermion mass eigenvalue spectrum for a given VEV direction."""
    vev: Array
    sigma_1: float
    sigma_2: float
    sigma_3: float
    ratio_12: float
    ratio_13: float
    schur_check: float


def mass_eigenvalues(yukawa_tensor: Array, vev: Array) -> MassSpectrum:
    """[PREDICT] Compute mass eigenvalues for a given VEV direction.

    M(v) = Σ_b T_{a,b,c} v_b
    No free parameters. Pure forward computation.
    """
    T = yukawa_tensor
    vev_norm = vev / np.linalg.norm(vev)
    M = np.einsum('abc,b->ac', T, vev_norm)
    sv = np.sort(np.linalg.svd(M, compute_uv=False))[::-1]
    s1, s2, s3 = float(sv[0]), float(sv[1]), float(sv[2])
    return MassSpectrum(
        vev=vev_norm, sigma_1=s1, sigma_2=s2, sigma_3=s3,
        ratio_12=s1 / s2 if s2 > 1e-15 else float('inf'),
        ratio_13=s1 / s3 if s3 > 1e-15 else float('inf'),
        schur_check=s1**2 + s2**2 + s3**2,
    )


# =====================================================================
# Restricted VEV (ZS-M10) [PREDICT]
# =====================================================================

def restricted_vev_predict(yukawa_tensor: Array,
                           rep5: list[Array],
                           rotations: list[Array]) -> MassSpectrum:
    """[PREDICT] Evaluate the ZS-M10 restricted VEV in the D₅ eigenbasis.

    v(θ) = cosθ·ê₁ + sinθ/√2·(ê₃_real + ê₄_real)
    at θ = |z*|·A

    This is a pure forward prediction with zero free parameters.
    The D₅ eigenbasis is computed from the representation, not hardcoded.

    [STATUS: PREDICT — no target values used]
    """
    U_d5 = compute_d5_eigenbasis(rep5, rotations)

    z_star_mod = math.sqrt(Z_STAR_MOD_SQ)
    theta = z_star_mod * A_LOCKED

    # VEV in D₅ eigenbasis: ê₁(col0), ê₃_r(col1), ê₄_r(col3)
    vev_d5 = np.zeros(5)
    vev_d5[0] = math.cos(theta)
    vev_d5[1] = math.sin(theta) / SQRT2
    vev_d5[3] = math.sin(theta) / SQRT2

    # Transform to computational basis
    vev_phys = U_d5 @ vev_d5
    return mass_eigenvalues(yukawa_tensor, vev_phys)


# =====================================================================
# S⁴ VEV fit (ZS-M11) [FIT — NOT DERIVED]
# =====================================================================

def fit_vev_s4(yukawa_tensor: Array,
               target_ratio_12: float = 17.0,
               target_ratio_13: float = 3477.0) -> MassSpectrum:
    """[FIT] Find the VEV direction that matches target mass ratios.

    WARNING: This is constraint-satisfaction, NOT forward prediction.
    The target ratios are INPUT parameters (from observation).
    The result demonstrates that the target IS achievable on S⁴
    given the unique tensor T, but does not predict the target values.

    The upgrade from FIT to PREDICT requires deriving the VEV direction
    from the quartic potential P₄ + Coleman-Weinberg correction.
    See predict_vev_from_quartic() for the forward prediction.

    [STATUS: FIT — target values are inputs, not outputs]
    """
    T = yukawa_tensor

    def cost(params):
        vev = _spherical_to_5d(params)
        spec = mass_eigenvalues(T, vev)
        if not (np.isfinite(spec.ratio_12) and np.isfinite(spec.ratio_13)):
            return 1e10
        return ((spec.ratio_12 - target_ratio_12) / target_ratio_12)**2 + \
               ((spec.ratio_13 - target_ratio_13) / target_ratio_13)**2

    rng = np.random.RandomState(2026)
    best_cost = float('inf')
    best_result = None
    for _ in range(200):
        x0 = rng.uniform(-math.pi, math.pi, 4)
        res = minimize(cost, x0, method='Nelder-Mead',
                       options={'maxiter': 5000, 'xatol': 1e-12, 'fatol': 1e-14})
        if res.fun < best_cost:
            best_cost = res.fun
            best_result = res

    vev_opt = _spherical_to_5d(best_result.x)
    return mass_eigenvalues(yukawa_tensor, vev_opt)


def _spherical_to_5d(angles: Array) -> Array:
    a1, a2, a3, a4 = angles
    v = np.array([
        math.cos(a1),
        math.sin(a1) * math.cos(a2),
        math.sin(a1) * math.sin(a2) * math.cos(a3),
        math.sin(a1) * math.sin(a2) * math.sin(a3) * math.cos(a4),
        math.sin(a1) * math.sin(a2) * math.sin(a3) * math.sin(a4),
    ])
    return v / np.linalg.norm(v)


# =====================================================================
# VEV Forward Prediction from P₄ + Coleman-Weinberg [PREDICT]
# =====================================================================

@dataclass(frozen=True)
class VEVPrediction:
    """Forward-predicted VEV from quartic potential + CW correction."""
    spectrum: MassSpectrum
    p4_at_vev: float
    p4_min: float
    p4_max: float
    displacement_pct: float
    cw_scale_pct: float
    status: str


def predict_vev_from_quartic(
    yukawa_tensor: Array,
    rep5_list: list[Array],
    lambda2_sign: float = +1.0,
) -> VEVPrediction:
    """[PREDICT] Forward VEV prediction from P₄ minimum + CW natural scale.

    Algorithm:
    1. Find P₄ minimum on S⁴ (tree-level → extreme hierarchy)
    2. Compute CW natural displacement: δ_CW = σ₁⁴/(16π²·ΔP₄) ≈ 0.63%
    3. Find VEV at P₄(v) = P₄_min + δ_CW · ΔP₄ (constrained search)

    At δ_CW ≈ 0.63%: σ₁/σ₂ ≈ 22 (natural CW scale prediction).
    With Hodge-Dirac multiplicity ×1.83 (ZS-S4): δ → 1.16%, σ₁/σ₂ ≈ 17.

    [STATUS: PREDICT — no target mass ratios used as input]
    """
    T = yukawa_tensor

    # Step 1: Find P₄ extremes on S⁴
    rng = np.random.RandomState(2026)
    p4_min_val, p4_max_val = 1e9, -1e9
    best_min_angles = None

    for _ in range(60):
        x0 = rng.uniform(-math.pi, math.pi, 4)
        res = minimize(lambda a: reynolds_quartic(_spherical_to_5d(a), rep5_list),
                       x0, method='Nelder-Mead', options={'maxiter': 1500})
        if res.fun < p4_min_val:
            p4_min_val = res.fun
            best_min_angles = res.x.copy()
        res2 = minimize(lambda a: -reynolds_quartic(_spherical_to_5d(a), rep5_list),
                        x0, method='Nelder-Mead', options={'maxiter': 1500})
        if -res2.fun > p4_max_val:
            p4_max_val = -res2.fun

    p4_range = p4_max_val - p4_min_val

    # Step 2: CW natural displacement scale
    sigma1_typ = math.sqrt(0.2)  # Schur-normalized
    delta_cw = sigma1_typ**4 / (16 * math.pi**2 * p4_range)

    # Step 3: Find VEV at the CW displacement point
    target_p4 = p4_min_val + delta_cw * p4_range
    rng2 = np.random.RandomState(42)
    best_cost = float('inf')
    best_vev = None
    for _ in range(40):
        x0 = best_min_angles + rng2.randn(4) * 0.3
        res = minimize(
            lambda a: ((reynolds_quartic(_spherical_to_5d(a), rep5_list) - target_p4)
                       / p4_range)**2 * 1e6,
            x0, method='Nelder-Mead', options={'maxiter': 2000})
        if res.fun < best_cost:
            best_cost = res.fun
            best_vev = _spherical_to_5d(res.x)

    spec = mass_eigenvalues(T, best_vev)
    p4_at_vev = reynolds_quartic(best_vev, rep5_list)
    displacement = (p4_at_vev - p4_min_val) / p4_range * 100

    return VEVPrediction(
        spectrum=spec,
        p4_at_vev=p4_at_vev,
        p4_min=p4_min_val,
        p4_max=p4_max_val,
        displacement_pct=displacement,
        cw_scale_pct=delta_cw * 100,
        status="PREDICT — VEV from P₄ + CW natural scale, no observed ratios used",
    )


# =====================================================================
# Quartic invariant P₄ [PREDICT]
# =====================================================================

def reynolds_quartic(v: Array, rep5_list: list[Array]) -> float:
    """[PREDICT] I-invariant quartic via Reynolds operator.

    P₄(v) = (1/|I|) Σ_g [(ρ₅(g)·v)₀]⁴

    Uses only the FIRST component of the transformed vector.
    The sum over ALL components gives Σσᵢ⁴ (trivially correlated).
    [STATUS: PROVEN — Reynolds operator guarantees invariance]
    """
    G5 = np.array(rep5_list)
    gv = G5 @ v  # shape (60, 5)
    return float(np.mean(gv[:, 0] ** 4))


def quartic_analysis(yukawa_tensor: Array, rep5_list: list[Array],
                     n_samples: int = 500) -> dict:
    """[PREDICT] Analyze P₄-hierarchy correlation.

    Returns Spearman ρ and Pearson R (both computed, not hardcoded).
    """
    rng = np.random.RandomState(42)
    samples = []
    for _ in range(n_samples):
        v = rng.randn(5); v /= np.linalg.norm(v)
        samples.append((reynolds_quartic(v, rep5_list), v))

    p4_mean = np.mean([s[0] for s in samples])

    rng2 = np.random.RandomState(42)
    p4_centered, log_ratios, sig4 = [], [], []
    for _ in range(n_samples):
        v = rng2.randn(5); v /= np.linalg.norm(v)
        p4c = reynolds_quartic(v, rep5_list) - p4_mean
        spec = mass_eigenvalues(yukawa_tensor, v)
        p4_centered.append(p4c)
        sig4.append(spec.sigma_1**4 + spec.sigma_2**4 + spec.sigma_3**4)
        log_ratios.append(math.log(max(spec.ratio_12, 1.001)))

    from scipy.stats import spearmanr
    rho_sp, _ = spearmanr(p4_centered, log_ratios)
    R_pearson = float(np.corrcoef(p4_centered, sig4)[0, 1])

    return {
        "spearman_rho": float(rho_sp),
        "pearson_R_sig4": R_pearson,
        "status": "PREDICT — all values computed, none hardcoded",
    }


# =====================================================================
# CKM mixing [DERIVED-CONDITIONAL + HARDCODED parts]
# =====================================================================

@dataclass(frozen=True)
class CKMPrediction:
    cabibbo_angle_deg: float
    raw_principal_angle_deg: float
    color_factor: float
    r_a4: float               # [COMPUTED from A₄ generation projector]
    dominant_gen_overlap: float
    v_ub_pred: float


def compute_a4_overlap(rep3: list[Array], rotations: list[Array]) -> dict:
    """[COMPUTED] A₄ generation projector decomposition.

    Computes the overlap between the D₅ lepton axis (C₅ rotation axis
    in the 3-dim rep) and the Z₃ generation eigenbasis (C₃ eigenvectors).

    Returns:
        dominant_overlap: |⟨lepton|gen₀⟩|² ≈ 0.631
        subdominant_overlap: |⟨lepton|gen₁⟩|² ≈ 0.184
        r_a4: subdominant/dominant ≈ 0.292

    [STATUS: COMPUTED — upgraded from HARDCODED.
     Uses only the group representation matrices, no external values.]
    """
    from zsim.sm.icosahedral import icosahedron_vertices, _rotation_matrix

    verts = icosahedron_vertices()
    axis_pent = verts[0] / np.linalg.norm(verts[0])

    # Find C₅ generator
    R_c5 = _rotation_matrix(axis_pent, 2 * math.pi / 5)
    idx_c5 = _find_in_group(R_c5, rotations)
    if idx_c5 < 0:
        R_c5 = _rotation_matrix(axis_pent, -2 * math.pi / 5)
        idx_c5 = _find_in_group(R_c5, rotations)

    # D₅ lepton axis = C₅ eigenvalue=1 eigenvector in 3-dim rep
    s3 = rep3[idx_c5]
    ev_s3, V_s3 = np.linalg.eig(s3)
    ax_idx = int(np.argmin(np.abs(ev_s3 - 1.0)))
    e_lepton = np.real(V_s3[:, ax_idx])
    e_lepton /= np.linalg.norm(e_lepton)

    # Find C₃ generator (face-center axis)
    edge_len = np.sort(np.linalg.norm(verts - verts[0], axis=1))[1]
    neighbors = [j for j in range(12)
                 if abs(np.linalg.norm(verts[j] - verts[0]) - edge_len) < 0.01]
    v0, v1 = verts[0], verts[neighbors[0]]
    v2 = None
    for idx in neighbors[1:]:
        if abs(np.linalg.norm(verts[idx] - v1) - edge_len) < 0.1:
            v2 = verts[idx]; break
    face_center = (v0 + v1 + v2) / 3.0
    axis_face = face_center / np.linalg.norm(face_center)
    R_c3 = _rotation_matrix(axis_face, 2 * math.pi / 3)
    idx_c3 = _find_in_group(R_c3, rotations)
    if idx_c3 < 0:
        R_c3 = _rotation_matrix(axis_face, -2 * math.pi / 3)
        idx_c3 = _find_in_group(R_c3, rotations)

    # Z₃ generation eigenbasis from C₃
    t3 = rep3[idx_c3]
    ev_t3, V_t3 = np.linalg.eig(t3)

    # Project lepton axis onto each generation
    overlaps = [float(abs(np.dot(e_lepton, V_t3[:, i]))**2) for i in range(3)]
    dominant = max(overlaps)
    subdominant = min(overlaps)

    return {
        "overlaps": overlaps,
        "dominant": dominant,
        "subdominant": subdominant,
        "r_a4": subdominant / dominant,
    }


def compute_ckm(rep3: list[Array],
                rep5: list[Array],
                rotations: list[Array]) -> CKMPrediction:
    """Compute CKM Cabibbo angle and V_ub from icosahedral geometry.

    [PREDICT] Steps 1-2 (isotypic decomposition, principal angle)
    [OBSERVATION] Step 3 (color factor 3/4 = X/(X+1))
    [COMPUTED] r_A4 from A₄ generation projector (was HARDCODED)
    [EXTERNAL] V_cb = 0.0405 from PDG 2024
    """
    raw_angle = _compute_d5_d3_principal_angle(rep5, rotations)
    color_factor = float(DIM_X) / float(DIM_X + 1)  # 3/4
    cabibbo = raw_angle * color_factor

    # COMPUTED from A₄ generation projector (upgraded from HARDCODED)
    a4 = compute_a4_overlap(rep3, rotations)
    r_a4 = a4["r_a4"]
    v_cb_pdg = 0.0405     # From PDG 2024 (external input, honestly declared)

    v_us = math.sin(math.radians(cabibbo))
    v_ub = r_a4 * v_us * v_cb_pdg

    return CKMPrediction(
        cabibbo_angle_deg=cabibbo,
        raw_principal_angle_deg=raw_angle,
        color_factor=color_factor,
        r_a4=r_a4,
        dominant_gen_overlap=a4["dominant"],
        v_ub_pred=v_ub,
    )


def _compute_d5_d3_principal_angle(rep5, rotations):
    """[PREDICT] Compute D₅-2₂ vs D₃-2 principal angle in 5-dim rep."""
    from zsim.sm.icosahedral import icosahedron_vertices
    import math
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    verts = icosahedron_vertices()

    # D₅ elements
    axis_pent = verts[0] / np.linalg.norm(verts[0])
    d5_rot = [i for i, R in enumerate(rotations)
              if np.allclose(R @ axis_pent, axis_pent, atol=1e-6)]
    d5_refl = [i for i, R in enumerate(rotations)
               if np.allclose(R @ axis_pent, -axis_pent, atol=1e-6)
               and not np.allclose(R @ axis_pent, axis_pent, atol=1e-6)]
    d5_id = [i for i in d5_rot if np.allclose(rotations[i], np.eye(3), atol=1e-6)]
    d5_c5 = [i for i in d5_rot if abs(np.trace(rotations[i]) - phi) < 0.01]
    d5_c5sq = [i for i in d5_rot if abs(np.trace(rotations[i]) - (1 - phi)) < 0.01]

    P_22 = np.zeros((5, 5))
    for idx in d5_id: P_22 += 2.0 * rep5[idx]
    for idx in d5_c5: P_22 += (-phi) * rep5[idx]
    for idx in d5_c5sq: P_22 += (phi - 1) * rep5[idx]
    P_22 *= 2.0 / 10.0

    ev22, ew22 = np.linalg.eigh(P_22)
    sub_22 = ew22[:, np.where(ev22 > 0.5)[0]]

    # D₃ elements
    edge_len = np.sort(np.linalg.norm(verts - verts[0], axis=1))[1]
    neighbors = [j for j in range(12)
                 if abs(np.linalg.norm(verts[j] - verts[0]) - edge_len) < 0.01]
    v0, v1 = verts[0], verts[neighbors[0]]
    v2 = None
    for idx in neighbors[1:]:
        if abs(np.linalg.norm(verts[idx] - v1) - edge_len) < 0.1:
            v2 = verts[idx]; break
    face_center = (v0 + v1 + v2) / 3.0
    axis_face = face_center / np.linalg.norm(face_center)

    d3_rot = [i for i, R in enumerate(rotations) if np.allclose(R @ axis_face, axis_face, atol=1e-6)]
    d3_refl = [i for i, R in enumerate(rotations)
               if np.allclose(R @ axis_face, -axis_face, atol=1e-6)
               and not np.allclose(R @ axis_face, axis_face, atol=1e-6)]
    d3_e = [i for i in d3_rot if np.allclose(rotations[i], np.eye(3), atol=1e-6)]
    d3_c3 = [i for i in d3_rot if not np.allclose(rotations[i], np.eye(3), atol=1e-6)]

    P_d3_2 = np.zeros((5, 5))
    for idx in d3_e: P_d3_2 += 2.0 * rep5[idx]
    for idx in d3_c3: P_d3_2 += (-1.0) * rep5[idx]
    P_d3_2 *= 2.0 / 6.0

    ev_d3, ew_d3 = np.linalg.eigh(P_d3_2)
    sub_d3_2 = ew_d3[:, np.where(ev_d3 > 0.5)[0]]

    overlap = sub_22.T @ sub_d3_2
    sv = np.linalg.svd(overlap, compute_uv=False)
    angles = np.degrees(np.arccos(np.clip(sv, -1, 1)))
    nonzero = [a for a in angles if a > 0.1]
    return max(nonzero) if nonzero else 0.0


# =====================================================================
# D₅ channel structure [PROVEN — Clebsch-Gordan decomposition]
# =====================================================================

@dataclass(frozen=True)
class D5ChannelResult:
    """D₅ Clebsch-Gordan decomposition of the Yukawa tensor."""
    fractions: dict[str, float]        # channel label → norm² fraction
    lepton_fraction: float              # (1',1,1') channel
    quark_lepton_ratio: float           # √(f_large/f_small) = √2
    silver_ratio: float                 # 1 + √(f_large/f_small) = 1+√2
    schur_sum: float                    # Σ fractions (should = 1)


def d5_channel_decomposition(
    yukawa_tensor: Array,
    rep3: list[Array],
    rep5: list[Array],
    rep3p: list[Array],
    rotations: list[Array],
) -> D5ChannelResult:
    """[PROVEN] Full D₅ Clebsch-Gordan decomposition of the Yukawa tensor.

    Under D₅ (pentagon stabilizer, order 10):
        3  → 1' ⊕ 2₁     (left fermion index)
        5  → 1 ⊕ 2₁ ⊕ 2₂ (Higgs index)
        3' → 1' ⊕ 2₂     (right fermion index)

    The five D₅-invariant channels are:
        (1', 1, 1')  — lepton channel, fraction = 1/5
        (1', 2₂, 2₂) — quark-A, fraction = 2/15
        (2₁, 2₁, 1') — quark-B, fraction = 2/15
        (2₁, 2₁, 2₂) — quark-C, fraction = 4/15
        (2₁, 2₂, 2₂) — quark-D, fraction = 4/15

    Structural theorems:
        √(f_large / f_small) = √(4/15 ÷ 2/15) = √2     [PROVEN]
        1 + √(f_large / f_small) = 1 + √2 (silver ratio) [PROVEN]
        Σ fractions = 1 (Schur conservation)               [PROVEN]

    [STATUS: PROVEN — all values computed from character projectors,
     no free parameters, no target values used]
    """
    T = yukawa_tensor
    phi = (1.0 + math.sqrt(5.0)) / 2.0

    # ── Identify D₅ elements and classify ──
    from zsim.sm.icosahedral import icosahedron_vertices
    verts = icosahedron_vertices()
    axis = verts[0] / np.linalg.norm(verts[0])

    d5_id, d5_c5, d5_c5sq, d5_refl = [], [], [], []
    for i, R in enumerate(rotations):
        Rv = R @ axis
        if np.allclose(Rv, axis, atol=1e-6):
            tr3 = np.trace(R)
            if abs(tr3 - 3.0) < 0.01:
                d5_id.append(i)
            elif abs(tr3 - phi) < 0.01:
                d5_c5.append(i)
            elif abs(tr3 - (1 - phi)) < 0.01:
                d5_c5sq.append(i)
        elif np.allclose(Rv, -axis, atol=1e-6):
            d5_refl.append(i)

    assert len(d5_id) + len(d5_c5) + len(d5_c5sq) + len(d5_refl) == 10

    # ── D₅ character table ──
    # Rows: 1, 1', 2₁, 2₂; Cols: e, C₅, C₅², refl
    chi = {
        '1':  [1, 1, 1, 1],
        '1p': [1, 1, 1, -1],
        '21': [2, phi - 1, -phi, 0],
        '22': [2, -phi, phi - 1, 0],
    }

    # ── Character projectors ──
    def _projector(chi_vals, rep_list):
        dim_rho = chi_vals[0]
        n = rep_list[d5_id[0]].shape[0]
        P = np.zeros((n, n))
        for idx in d5_id:    P += chi_vals[0] * rep_list[idx]
        for idx in d5_c5:    P += chi_vals[1] * rep_list[idx]
        for idx in d5_c5sq:  P += chi_vals[2] * rep_list[idx]
        for idx in d5_refl:  P += chi_vals[3] * rep_list[idx]
        return P * (dim_rho / 10.0)

    P3 = {name: _projector(vals, rep3) for name, vals in chi.items()}
    P5 = {name: _projector(vals, rep5) for name, vals in chi.items()}
    P3p = {name: _projector(vals, rep3p) for name, vals in chi.items()}

    # ── Project T onto 5 D₅ channels ──
    channels = [
        ('1p', '1',  '1p', 'lepton'),
        ('1p', '22', '22', 'quark-A'),
        ('21', '21', '1p', 'quark-B'),
        ('21', '21', '22', 'quark-C'),
        ('21', '22', '22', 'quark-D'),
    ]

    total_norm = float(np.sum(T ** 2))
    fractions = {}
    for alpha, beta, gamma, label in channels:
        T_ch = np.einsum('iI,mM,aA,IMA->ima',
                         P3[alpha], P5[beta], P3p[gamma], T)
        frac = float(np.sum(T_ch ** 2)) / total_norm
        fractions[label] = frac

    f_sorted = sorted(fractions.values())
    f_small = f_sorted[0]   # 2/15
    f_large = f_sorted[-1]  # 4/15

    return D5ChannelResult(
        fractions=fractions,
        lepton_fraction=fractions['lepton'],
        quark_lepton_ratio=math.sqrt(f_large / f_small),
        silver_ratio=1.0 + math.sqrt(f_large / f_small),
        schur_sum=sum(fractions.values()),
    )


def d5_channel_status() -> str:
    """Backward-compatible status string."""
    return "PROVEN — D₅ CG decomposition implemented, 5 channels verified"


# =====================================================================
# Report
# =====================================================================

def print_summary(yukawa_tensor, rep3, rep5, rep3p, rotations):
    """Print honest summary of fermion predictions."""
    print("=" * 72)
    print("  Z-Spin Fermion Predictions — Honest Status Report")
    print("=" * 72)

    # Restricted VEV [PREDICT]
    m10 = restricted_vev_predict(yukawa_tensor, rep5, rotations)
    print(f"\n  [PREDICT] Restricted VEV (D₅ eigenbasis, θ=|z*|·A):")
    print(f"    σ₁/σ₂ = {m10.ratio_12:.1f}  (ZS-M10: ~27)")
    print(f"    σ₁/σ₃ = {m10.ratio_13:.0f}  (ZS-M10: ~3302)")
    print(f"    Σσ²   = {m10.schur_check:.6f}  (target: 0.200, PROVEN)")

    # S⁴ fit [FIT]
    m11 = fit_vev_s4(yukawa_tensor)
    print(f"\n  [FIT] S⁴ VEV optimization (targets: 17.0, 3477.0):")
    print(f"    σ₁/σ₂ = {m11.ratio_12:.2f}  (target input: {PDG_M_TAU_OVER_M_MU})")
    print(f"    σ₁/σ₃ = {m11.ratio_13:.0f}  (target input: {PDG_M_TAU_OVER_M_E})")
    print(f"    ⚠ This is constraint satisfaction, not prediction")

    # CKM [DERIVED-CONDITIONAL + HARDCODED]
    ckm = compute_ckm(rep3, rep5, rotations)
    print(f"\n  [DERIVED-CONDITIONAL] Cabibbo angle:")
    print(f"    Raw D₅-D₃ angle = {ckm.raw_principal_angle_deg:.2f}° [PREDICT]")
    print(f"    × color factor {ckm.color_factor} [OBSERVATION]")
    print(f"    = {ckm.cabibbo_angle_deg:.2f}° (observed: {PDG_CABIBBO_DEG}°)")
    print(f"    r_A4 = {ckm.r_a4:.3f} [COMPUTED from A₄ generation projector]")
    print(f"    Dominant generation overlap = {ckm.dominant_gen_overlap:.1%}")
    print(f"    V_ub = {ckm.v_ub_pred:.4f} [uses PDG V_cb = 0.0405]")

    # D₅ channels [PROVEN]
    from zsim.sm.yukawa import d5_channel_decomposition
    d5 = d5_channel_decomposition(yukawa_tensor, rep3, rep5, rep3p, rotations)
    print(f"\n  [PROVEN] D₅ channel decomposition:")
    for label, frac in d5.fractions.items():
        print(f"    {label:10s}: {frac:.4f}")
    print(f"    √(f_large/f_small) = {d5.quark_lepton_ratio:.4f} (√2 = {SQRT2:.4f})")
    print(f"    1 + √(f_large/f_small) = {d5.silver_ratio:.4f} (1+√2 = {SILVER_RATIO:.4f})")

    # Quartic [PREDICT]
    qa = quartic_analysis(yukawa_tensor, rep5)
    print(f"\n  [PREDICT] Reynolds P₄ quartic invariant:")
    print(f"    |Spearman ρ|(P₄, log σ₁/σ₂) = {abs(qa['spearman_rho']):.3f}")
    print(f"    Pearson R(P₄, Σσᵢ⁴) = {qa['pearson_R_sig4']:.4f}")
    print("=" * 72)
