from __future__ import annotations

from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.overlap import evaluate_overlap_background
from zsim.lgt.stage7 import evaluate_stage7_bundle, phase_scrambled_caloron_links, scan_stage7_valley_family, stage7_overlap_controls
from zsim.lgt.backgrounds import caloron_pair_links


def test_overlap_background_metrics_are_finite() -> None:
    lattice = build_bcc_supercell(1, 1, 1)
    links = caloron_pair_links(lattice.edges, lattice.positions, 0.6, separation=0.55, width=0.45, seam_bias=0.15)
    summary = evaluate_overlap_background(lattice, links, mass=0.10, kappa=0.5, sign_epsilon=1e-4)
    assert summary.score > 0.0
    assert summary.gw_residual >= 0.0
    assert summary.pairing.pair_count >= 1


def test_stage7_scan_and_controls() -> None:
    lattice = build_bcc_supercell(1, 1, 1)
    best, links, rows = scan_stage7_valley_family(
        lattice,
        amplitude_grid=(0.4, 0.7),
        separation_grid=(0.55,),
        width_grid=(0.45,),
        seam_bias_grid=(0.10, 0.20),
        scan_schemes=('staggered2', 'wilson4'),
        mass=0.10,
        kappa=0.5,
        reg_epsilon=1e-4,
        cutoff=1e-6,
        fd_step=5e-4,
        sign_epsilon=1e-4,
    )
    assert len(rows) == 4
    assert best.objective > 0.0
    scheme_rows, harness, overlap = evaluate_stage7_bundle(lattice, links, schemes=('reduced2', 'wilson4'), mass=0.10, kappa=0.5, reg_epsilon=1e-4, cutoff=1e-6, fd_step=5e-4, sign_epsilon=1e-4)
    assert len(scheme_rows) == 2
    assert harness['overlap_score'] == overlap.score
    assert overlap.chiral_abs_mean >= 0.0
    controls = stage7_overlap_controls(lattice, amplitude=0.5, schemes=('reduced2', 'wilson4'), mass=0.10, kappa=0.5, reg_epsilon=1e-4, cutoff=1e-6, fd_step=5e-4, sign_epsilon=1e-4, seed=7)
    assert {'identity', 'haar', 'scrambled_caloron', 'phase_scrambled_caloron'} <= set(controls)


def test_phase_scramble_changes_background() -> None:
    lattice = build_bcc_supercell(1, 1, 1)
    base = caloron_pair_links(lattice.edges, lattice.positions, 0.6)
    scrambled = phase_scrambled_caloron_links(lattice, 0.6, seed=11)
    deltas = [abs(base[e][0, 0] - scrambled[e][0, 0]) for e in lattice.edges]
    assert max(deltas) > 1e-8
