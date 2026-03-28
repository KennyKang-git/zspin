from __future__ import annotations

from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.pairing import analyze_near_zero_pairs_from_singular_values
from zsim.lgt.stage6 import evaluate_scheme_bundle, scan_stage6_valley_family, stage6_pairing_controls


def test_pairing_summary_basic_ordering() -> None:
    summary = analyze_near_zero_pairs_from_singular_values([0.01, 0.011, 0.015, 0.016, 0.20, 0.21, 0.30, 0.31], pair_count=2, sample_size=8)
    assert summary.pair_count == 2
    assert summary.bulk_gap > 0.0
    assert summary.score > 1.0


def test_stage6_scan_and_harness() -> None:
    lattice = build_bcc_supercell(1, 1, 1)
    best, links, rows = scan_stage6_valley_family(
        lattice,
        amplitude_grid=(0.4, 0.7),
        separation_grid=(0.55,),
        width_grid=(0.45,),
        seam_bias_grid=(0.10, 0.20),
        scan_schemes=('reduced2',),
        mass=0.10,
        kappa=0.5,
        reg_epsilon=1e-4,
        cutoff=1e-6,
        fd_step=5e-4,
    )
    assert len(rows) == 4
    assert best.objective > 0.0
    scheme_rows, harness = evaluate_scheme_bundle(lattice, links, schemes=('reduced2', 'staggered2'), mass=0.10, kappa=0.5, reg_epsilon=1e-4, cutoff=1e-6, fd_step=5e-4)
    assert len(scheme_rows) == 2
    assert harness['scheme_count'] == 2
    assert harness['pair_score_mean'] > 0.0


def test_stage6_controls_exist() -> None:
    lattice = build_bcc_supercell(1, 1, 1)
    controls = stage6_pairing_controls(lattice, amplitude=0.5, schemes=('reduced2',), mass=0.10, kappa=0.5, reg_epsilon=1e-4, cutoff=1e-6, fd_step=5e-4, seed=7)
    assert {'identity', 'haar', 'scrambled_caloron'} <= set(controls)
    assert controls['identity']['harness']['scheme_count'] == 1
