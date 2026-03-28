from __future__ import annotations

import numpy as np

from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.mbp import extract_mbp_bilinear
from zsim.lgt.spinor import euclidean_gamma_set, wilson_chirality_projector, wilson_gamma5_matrix
from zsim.lgt.valley_fit import fit_caloron_valley_family


def test_euclidean_gamma5_is_involutive() -> None:
    gs = euclidean_gamma_set()
    assert np.allclose(gs.gamma5 @ gs.gamma5, np.eye(4, dtype=np.complex128))


def test_wilson_chirality_projectors_complete() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    left = wilson_chirality_projector(lattice, 'left')
    right = wilson_chirality_projector(lattice, 'right')
    ident = np.eye(left.shape[0], dtype=np.complex128)
    assert np.allclose(left + right, ident)
    assert np.allclose(left @ right, 0.0)
    assert wilson_gamma5_matrix(lattice).shape[0] == 8 * lattice.num_sites


def test_valley_fit_returns_nontrivial_best_point() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    best, links, rows = fit_caloron_valley_family(lattice, amplitude_grid=(0.25, 0.5), separation_grid=(0.55, 0.75), width_grid=(0.45, 0.75), seam_bias_grid=(0.1, 0.2), mass=0.15)
    assert rows
    assert best.score >= max(row.score for row in rows) - 1e-12
    assert len(links) == lattice.num_edges


def test_wilson4_scheme_differs_from_staggered2() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    _, links, _ = fit_caloron_valley_family(lattice, amplitude_grid=(0.5,), separation_grid=(0.75,), width_grid=(0.6,), seam_bias_grid=(0.15,), mass=0.15)
    wilson = extract_mbp_bilinear(lattice, links, fermion_scheme='wilson4', chirality_mode='left', mass=0.15, kappa=0.6, reg_epsilon=1e-4, cutoff=1e-6, fd_step=5e-4)
    staggered = extract_mbp_bilinear(lattice, links, fermion_scheme='staggered2', chirality_mode='left', mass=0.15, kappa=0.6, reg_epsilon=1e-4, cutoff=1e-6, fd_step=5e-4)
    assert abs(wilson.mu2_formula_proxy - staggered.mu2_formula_proxy) > 1e-8
