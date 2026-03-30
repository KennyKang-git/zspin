from __future__ import annotations

import numpy as np

from zsim.lgt.backgrounds import caloron_pair_links
from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.chirality import bipartite_chirality_signs, chirality_projector, gamma5_matrix
from zsim.lgt.controls import run_negative_controls
from zsim.lgt.mbp import extract_mbp_bilinear


def test_bipartite_chirality_signs_balance() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    signs = bipartite_chirality_signs(lattice)
    assert set(np.unique(signs)) == {-1.0, 1.0}
    assert np.count_nonzero(signs > 0) > 0
    assert np.count_nonzero(signs < 0) > 0


def test_gamma5_is_involutive() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    g5 = gamma5_matrix(lattice)
    ident = np.eye(g5.shape[0], dtype=np.complex128)
    assert np.allclose(g5 @ g5, ident)


def test_left_right_projectors_complete() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    left = chirality_projector(lattice, 'left')
    right = chirality_projector(lattice, 'right')
    ident = np.eye(left.shape[0], dtype=np.complex128)
    assert np.allclose(left + right, ident)
    assert np.allclose(left @ right, 0.0)


def test_caloron_background_changes_chiral_mbp_proxy() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    links = caloron_pair_links(lattice.edges, lattice.positions, amplitude=0.6)
    left = extract_mbp_bilinear(lattice, links, projector_mode='center', chirality_mode='left', reg_epsilon=1e-3, cutoff=1e-6, fd_step=1e-3)
    right = extract_mbp_bilinear(lattice, links, projector_mode='center', chirality_mode='right', reg_epsilon=1e-3, cutoff=1e-6, fd_step=1e-3)
    assert abs(left.mu2_formula_proxy - right.mu2_formula_proxy) > 1e-8


def test_negative_controls_payload() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    links = caloron_pair_links(lattice.edges, lattice.positions, amplitude=0.6)
    payload = run_negative_controls(lattice, links, amplitude=0.6, yt=1.0, nc=3.0, mass=0.0, reg_epsilon=1e-3, cutoff=1e-6, fd_step=1e-3, seed=123)
    assert 'identity_vector' in payload
    assert 'scrambled_caloron' in payload
