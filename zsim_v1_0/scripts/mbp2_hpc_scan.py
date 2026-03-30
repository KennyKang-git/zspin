"""Z-Sim v1.0 — SU(2) HPC Lattice Computation for Higgs VEV

Production scan script implementing the MBP v2 5-phase protocol
with near-zero mode projected extraction.

Physics: In the I-Ī background (Q=0), the overlap Dirac operator
has ~4 near-zero modes (2 from I × 2 from Ī color channels).
These modes are the PHYSICAL source of the h² bilinear.
The bulk modes contribute a volume-dependent background that
must be subtracted for a meaningful κ₂ extraction.

Method: Project K₀, K₁, K₂ onto the near-zero subspace (lowest
k eigenmodes of K₀ = D†D), then extract h² in this subspace.

Usage:
    python scripts/mbp2_hpc_scan.py
    python scripts/mbp2_hpc_scan.py --max-shape 5
    python scripts/mbp2_hpc_scan.py --caloron-scan
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np


def near_zero_projected_extraction(
    D_ov: np.ndarray,
    Y: np.ndarray,
    *,
    n_modes: int = 4,
    nc: float = 3.0,
    reg_epsilon: float = 1e-10,
    fd_step: float = 1e-3,
) -> dict:
    """Extract h² coefficient from near-zero mode subspace.

    Projects K₀, K₁, K₂ onto the k lowest eigenmodes of K₀ = D†D,
    then computes the MBP bilinear in this projected space.

    This removes the volume-dependent bulk contribution, isolating
    the physical I-Ī molecular signal.

    Parameters
    ----------
    D_ov : array (N×N)
        Overlap Dirac matrix at h=0.
    Y : array (N×N)
        Yukawa projector.
    n_modes : int
        Number of near-zero modes to keep (4 for Q=0 I-Ī in SU(2)).
    """
    K0 = D_ov.conj().T @ D_ov + reg_epsilon * np.eye(D_ov.shape[0], dtype=np.complex128)
    K1 = D_ov.conj().T @ Y + Y.conj().T @ D_ov
    K2 = Y.conj().T @ Y

    # Eigendecomposition of K₀ (Hermitian, so eigenvalues real)
    evals, evecs = np.linalg.eigh(K0)

    # Project onto the k lowest eigenmodes
    k = min(n_modes, len(evals))
    V_nz = evecs[:, :k]  # Near-zero eigenvectors
    lam_nz = evals[:k]   # Near-zero eigenvalues

    # Projected matrices: k×k
    K0_proj = np.diag(lam_nz)  # Diagonal in this basis
    K1_proj = V_nz.conj().T @ K1 @ V_nz
    K2_proj = V_nz.conj().T @ K2 @ V_nz

    K0_inv_proj = np.diag(1.0 / lam_nz)

    # Trace formula in projected space
    diag_term = float(np.real(np.trace(K0_inv_proj @ K2_proj)))
    cross_half = 0.5 * float(np.real(np.trace(K0_inv_proj @ K1_proj @ K0_inv_proj @ K1_proj)))
    mbp_bracket = diag_term - cross_half
    gamma_h2_trace = -(nc / 2.0) * mbp_bracket

    # Finite-difference cross-check in projected space
    def gamma_nz(K):
        ev = np.linalg.eigvalsh(K)
        ev = ev[ev > 1e-15]
        return float(-(nc / 2.0) * np.sum(np.log(ev))) if ev.size else 0.0

    h = fd_step
    g0 = gamma_nz(K0_proj)
    gp = gamma_nz(K0_proj + h * K1_proj + h**2 * K2_proj)
    gm = gamma_nz(K0_proj - h * K1_proj + h**2 * K2_proj)
    gamma_h2_fd = (gp - 2 * g0 + gm) / (2 * h**2)

    gap = abs(gamma_h2_trace - gamma_h2_fd)
    sign_match = (abs(gamma_h2_trace) < 1e-15 and abs(gamma_h2_fd) < 1e-15) or \
                 ((gamma_h2_trace > 0) == (gamma_h2_fd > 0))

    # Also compute the FULL trace (all modes) for comparison
    cutoff = 1e-8
    mask_full = evals > cutoff
    V_full = evecs[:, mask_full]
    lam_full = evals[mask_full]
    K0_inv_full = (V_full / lam_full) @ V_full.conj().T
    diag_full = float(np.real(np.trace(K0_inv_full @ K2)))
    cross_full = 0.5 * float(np.real(np.trace(K0_inv_full @ K1 @ K0_inv_full @ K1)))
    mu2_full = nc * (diag_full - cross_full)

    # SVD of D_ov
    svals = np.sort(np.linalg.svd(D_ov, compute_uv=False))

    return {
        "n_projected_modes": k,
        "projected_eigenvalues": [float(l) for l in lam_nz],
        "diag_term_proj": diag_term,
        "cross_term_half_proj": cross_half,
        "mbp_bracket_proj": mbp_bracket,
        "gamma_h2_trace_proj": gamma_h2_trace,
        "gamma_h2_fd_proj": gamma_h2_fd,
        "consistency_gap_proj": gap,
        "sign_match_proj": sign_match,
        "mu2_proxy_proj": nc * mbp_bracket,
        "mu2_full_all_modes": mu2_full,
        "sigma_min": float(svals[0]) if svals.size else 0.0,
        "sigma_1": float(svals[1]) if svals.size > 1 else 0.0,
        "sigma_2": float(svals[2]) if svals.size > 2 else 0.0,
        "sigma_3": float(svals[3]) if svals.size > 3 else 0.0,
        "sigma_4": float(svals[4]) if svals.size > 4 else 0.0,
        "spectral_gap_4_5": float(svals[4] / max(svals[0], 1e-30)) if svals.size > 4 else 0.0,
        "total_modes_above_cutoff": int(np.sum(mask_full)),
    }


def run_single(
    shape, *, sep_frac=0.4, rho_inst=0.5, coupling_g=1.0,
    flow_steps=30, flow_eps=0.01, overlap_rho=1.0, wilson_r=1.0,
    chirality="left", yt=1.0, n_nz_modes=4, beta=2.3, a=1.0,
):
    """Run a single MBP v2 computation with projected extraction."""
    from zsim.lgt2.lattice import build_periodic_bcc
    from zsim.lgt2.gauge_field import GaugeField, avg_plaquette
    from zsim.lgt2.gradient_flow import WilsonGradientFlow
    from zsim.lgt2.caloron import CaloronBackground
    from zsim.lgt2.dirac_overlap import OverlapDirac
    from zsim.lgt2.mbp2 import build_yukawa_projector_overlap, S_CL, C_M, KAPPA2_TARGET

    EXP_M2S = float(np.exp(-2.0 * S_CL))

    # Phase 1: Lattice
    lat = build_periodic_bcc(*shape, a=a)

    # Phase 2: Caloron + Flow
    cal = CaloronBackground.symmetric_pair(
        lat, separation_fraction=sep_frac, rho_inst=rho_inst, coupling_g=coupling_g
    )
    gf = cal.generate(beta=beta)
    p0 = avg_plaquette(gf)

    flow = WilsonGradientFlow(epsilon=flow_eps, max_steps=flow_steps)
    traj = flow.flow(gf, n_steps=flow_steps, record_every=max(1, flow_steps))
    gf_fl = traj[-1].gauge_field
    pf = avg_plaquette(gf_fl)

    # Phase 3: Overlap Dirac
    ov = OverlapDirac(gf_fl, rho=overlap_rho, wilson_r=wilson_r)
    gw = ov.verify_ginsparg_wilson()
    spec = ov.spectrum()

    # Phase 4: Near-zero mode projected extraction
    D = ov.matrix()
    Y = build_yukawa_projector_overlap(ov, yt=yt, chirality_mode=chirality)
    h2 = near_zero_projected_extraction(D, Y, n_modes=n_nz_modes, nc=3.0)

    # Phase 5: Compare
    mu2_proj = h2["mu2_proxy_proj"]
    kappa2_proj = mu2_proj / C_M if abs(C_M) > 1e-15 else 0.0
    kappa2_ratio = kappa2_proj / KAPPA2_TARGET if abs(KAPPA2_TARGET) > 1e-15 else 0.0

    fmb1 = abs(mu2_proj) > 1e-20
    fmb2 = mu2_proj > 0

    return {
        "shape": list(shape),
        "a": a,
        "beta": beta,
        "V": lat.volume_cells,
        "dim": 8 * lat.num_sites,
        "sep_frac": sep_frac,
        "rho_inst": rho_inst,
        "coupling_g": coupling_g,
        "flow_steps": flow_steps,
        "chirality": chirality,
        "n_nz_modes": n_nz_modes,
        "plaq_initial": p0,
        "plaq_flowed": pf,
        "Q": spec.topological_charge,
        "GW_residual": gw,
        **h2,
        "kappa2_proj": kappa2_proj,
        "kappa2_target": KAPPA2_TARGET,
        "kappa2_ratio": kappa2_ratio,
        "F_MBP_1": fmb1,
        "F_MBP_2": fmb2,
    }


def print_row(r, label=""):
    """Print a single result row compactly."""
    shape_str = f"{r['shape'][0]}x{r['shape'][1]}x{r['shape'][2]}"
    print(f"  {label:12s} {shape_str:8s}  gap_proj={r['consistency_gap_proj']:.4e}  "
          f"sign={r['sign_match_proj']}  k2_proj={r['kappa2_proj']:.6e}  "
          f"mu2_proj={r['mu2_proxy_proj']:.4e}  mu2_full={r['mu2_full_all_modes']:.4e}  "
          f"σ₀={r['sigma_min']:.4e}  σ₄/σ₀={r['spectral_gap_4_5']:.2f}  "
          f"GW={r['GW_residual']:.1e}  Q={r['Q']}")


def main():
    parser = argparse.ArgumentParser(description="Z-Sim v1.0 MBP v2 HPC Scan")
    parser.add_argument("--max-shape", type=int, default=5, help="Maximum N for N³ lattice")
    parser.add_argument("--caloron-scan", action="store_true", help="Run caloron parameter scan")
    parser.add_argument("--flow-scan", action="store_true", help="Run flow-step scan")
    parser.add_argument("--mode-scan", action="store_true", help="Scan number of projected modes")
    parser.add_argument("--output-dir", type=str, default="outputs/mbp2_hpc", help="Output directory")
    args = parser.parse_args()

    outdir = Path(args.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    all_results = []

    # ================================================================
    # SCAN 1: Shape scaling with projected extraction
    # ================================================================
    print("=" * 80)
    print("SCAN 1: Shape Scaling (near-zero mode projected extraction)")
    print("=" * 80)
    print(f"  n_modes=4, sep=0.4, rho=0.5, flow=30, chirality=left")
    print()

    for N in range(2, args.max_shape + 1):
        shape = (N, N, N)
        t0 = time.time()
        print(f"  Running {shape}...", end="", flush=True)
        r = run_single(shape, n_nz_modes=4, flow_steps=30)
        dt = time.time() - t0
        r["scan"] = "shape_scaling"
        r["time_s"] = dt
        all_results.append(r)
        print(f" done ({dt:.1f}s)")
        print_row(r, f"N={N}")

    print()

    # ================================================================
    # SCAN 2: Number of projected modes
    # ================================================================
    print("=" * 80)
    print("SCAN 2: Mode Projection Sensitivity (4³, varying n_modes)")
    print("=" * 80)

    for n_modes in [2, 4, 6, 8, 12, 16]:
        t0 = time.time()
        r = run_single((4, 4, 4), n_nz_modes=n_modes, flow_steps=30)
        dt = time.time() - t0
        r["scan"] = "mode_projection"
        r["time_s"] = dt
        all_results.append(r)
        print_row(r, f"k={n_modes}")

    print()

    # ================================================================
    # SCAN 3: Caloron parameter scan
    # ================================================================
    if args.caloron_scan:
        print("=" * 80)
        print("SCAN 3: Caloron Parameters (4³)")
        print("=" * 80)

        for sep in [0.2, 0.3, 0.4, 0.5]:
            for rho in [0.3, 0.5, 0.8, 1.0]:
                t0 = time.time()
                r = run_single((4, 4, 4), sep_frac=sep, rho_inst=rho, n_nz_modes=4, flow_steps=30)
                dt = time.time() - t0
                r["scan"] = "caloron_params"
                r["time_s"] = dt
                all_results.append(r)
                print_row(r, f"s={sep},r={rho}")
        print()

    # ================================================================
    # SCAN 4: Flow steps
    # ================================================================
    if args.flow_scan:
        print("=" * 80)
        print("SCAN 4: Flow Steps (4³)")
        print("=" * 80)

        for fs in [10, 20, 30, 50, 80, 100]:
            t0 = time.time()
            r = run_single((4, 4, 4), flow_steps=fs, n_nz_modes=4)
            dt = time.time() - t0
            r["scan"] = "flow_steps"
            r["time_s"] = dt
            all_results.append(r)
            print_row(r, f"flow={fs}")
        print()

    # ================================================================
    # Summary & Falsification Analysis
    # ================================================================
    print("=" * 80)
    print("FALSIFICATION GATE ANALYSIS")
    print("=" * 80)

    shape_results = [r for r in all_results if r["scan"] == "shape_scaling"]
    if len(shape_results) >= 2:
        gaps = [(r["shape"], r["consistency_gap_proj"]) for r in shape_results]
        k2s = [(r["shape"], r["kappa2_proj"]) for r in shape_results]
        signs = [(r["shape"], r["sign_match_proj"]) for r in shape_results]

        print()
        print("  Shape Scaling Convergence:")
        for s, g in gaps:
            print(f"    {s}: gap = {g:.6e}")

        if len(gaps) >= 2:
            gap_trend = gaps[-1][1] / max(gaps[-2][1], 1e-30)
            print(f"  Gap ratio (last/prev): {gap_trend:.4f}")
            if gap_trend < 1.0:
                print("  → CONVERGING ✓")
            else:
                print("  → NOT YET CONVERGING ✗")

        print()
        print("  κ₂ Scaling:")
        for s, k in k2s:
            print(f"    {s}: κ₂_proj = {k:.6e}")

        print()
        print("  F-MBP-1 (bilinear exists):", all(r["F_MBP_1"] for r in shape_results))
        print("  F-MBP-2 (tachyonic sign): ", all(r["F_MBP_2"] for r in shape_results))
        print("  Sign match (all shapes):  ", all(r["sign_match_proj"] for r in shape_results))
        print("  GW residual < 10⁻¹⁰:     ", all(r["GW_residual"] < 1e-10 for r in shape_results))
        print("  Q = 0 (all shapes):       ", all(r["Q"] == 0 for r in shape_results))

    # Save results
    outfile = outdir / "mbp2_hpc_scan_results.json"
    with open(outfile, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\n  Results saved to: {outfile}")
    print("=" * 80)


if __name__ == "__main__":
    main()
