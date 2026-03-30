from __future__ import annotations

from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.stage9 import edge_permuted_caloron_links, conjugation_scrambled_caloron_links, run_stage9_pipeline, stage9_sharpened_controls


def test_stage9_controls_cover_sharpened_family() -> None:
    lattice = build_bcc_supercell(1, 1, 1)
    controls = stage9_sharpened_controls(lattice, amplitude=0.6, separation=0.55, width=0.45, seam_bias=0.15)
    assert {'identity', 'haar', 'scrambled_caloron', 'phase_scrambled_caloron', 'edge_permuted_caloron', 'conjugation_scrambled_caloron'} <= set(controls)


def test_stage9_scrambled_controls_match_edge_set() -> None:
    lattice = build_bcc_supercell(1, 1, 1)
    permuted = edge_permuted_caloron_links(lattice, 0.6, separation=0.55, width=0.45, seam_bias=0.15)
    conj = conjugation_scrambled_caloron_links(lattice, 0.6, separation=0.55, width=0.45, seam_bias=0.15)
    assert set(permuted) == set(lattice.edges)
    assert set(conj) == set(lattice.edges)


def test_stage9_pipeline_runs() -> None:
    summary, payload = run_stage9_pipeline(
        shape_grid=((1, 1, 1), (2, 1, 1)),
        scan_schemes=('staggered2', 'wilson4'),
        compare_schemes=('reduced2', 'wilson4'),
        sign_methods=('smooth', 'tanh', 'rational', 'arctan', 'pade11'),
        amplitudes=(0.4, 0.7),
        separations=(0.55,),
        widths=(0.45,),
        seam_biases=(0.10, 0.20),
        mass=0.10,
        kappa=0.5,
        reg_epsilon=1e-4,
        cutoff=1e-6,
        fd_step=5e-4,
        sign_epsilon=1e-4,
    )
    assert len(summary.shape_rows) == 2
    assert len(summary.control_rows) >= 6
    assert payload['gates']['G-HARD-CONTROLS-PRESENT'] is True
