"""Caloron parameter scan for MBP v2."""
import sys, time
sys.path.insert(0, ".")
from scripts.mbp2_hpc_scan import run_single

print("=" * 85)
print("CALORON PARAMETER SCAN (4x4x4, k=4 projected modes)")
print("=" * 85)
print(f"{'sep':>5} {'rho':>5} | {'k2_proj':>14} {'mu2_proj':>12} {'gap_proj':>12} {'sign':>5} {'sg4/0':>6} {'t(s)':>5}")
print("-" * 85)

best_k2 = None
best_params = None
results = []

for sep in [0.2, 0.3, 0.4, 0.5, 0.6]:
    for rho in [0.3, 0.5, 0.8, 1.2]:
        t0 = time.time()
        r = run_single((4,4,4), sep_frac=sep, rho_inst=rho, n_nz_modes=4, flow_steps=30)
        dt = time.time() - t0
        k2 = r["kappa2_proj"]
        mu2 = r["mu2_proxy_proj"]
        gap = r["consistency_gap_proj"]
        sm = r["sign_match_proj"]
        sg = r["spectral_gap_4_5"]
        print(f"  {sep:4.1f} {rho:5.1f} | {k2:+14.6e} {mu2:12.4e} {gap:12.4e} {sm!s:>5} {sg:6.2f} {dt:5.0f}")
        results.append((sep, rho, k2, mu2, gap, sm, sg))
        if sm and mu2 > 0:
            if best_k2 is None or abs(k2 - 0.0906) < abs(best_k2 - 0.0906):
                best_k2 = k2
                best_params = (sep, rho)

print()
print("=" * 85)
if best_params:
    print(f"BEST positive-sign kappa2: {best_k2:.6e} at sep={best_params[0]}, rho={best_params[1]}")
    print(f"Target: 0.0906, ratio: {best_k2/0.0906:.4f}")
else:
    print("No positive-sign result found.")

# Also run flow scan at best caloron params
if best_params:
    print()
    print("=" * 85)
    print(f"FLOW SCAN at best caloron params (sep={best_params[0]}, rho={best_params[1]})")
    print("=" * 85)
    for fs in [10, 20, 30, 50, 80]:
        t0 = time.time()
        r = run_single((4,4,4), sep_frac=best_params[0], rho_inst=best_params[1],
                       n_nz_modes=4, flow_steps=fs)
        dt = time.time() - t0
        k2 = r["kappa2_proj"]
        mu2 = r["mu2_proxy_proj"]
        gap = r["consistency_gap_proj"]
        sm = r["sign_match_proj"]
        print(f"  flow={fs:3d}: k2={k2:+14.6e}, mu2={mu2:12.4e}, gap={gap:12.4e}, sign={sm}, ({dt:.0f}s)")
