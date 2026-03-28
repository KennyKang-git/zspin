from __future__ import annotations

import numpy as np

from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.mbp import build_yukawa_projector, extract_mbp_bilinear, k_matrices_from_links
from zsim.lgt.su2_links import identity_links, random_su2_links
from zsim.lgt.valley import collective_valley_links


def test_build_yukawa_projector_shape_and_rank() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    y = build_yukawa_projector(lattice, 'center', yt=1.0)
    assert y.shape == (2 * lattice.num_sites, 2 * lattice.num_sites)
    diag = np.diag(y)
    nonzero = np.count_nonzero(np.abs(diag) > 0)
    assert nonzero == 2 * lattice.site_types.count('center')


def test_k_matrices_are_hermitian_where_expected() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    links = identity_links(lattice.edges)
    _, _, k0, k1, k2 = k_matrices_from_links(lattice, links, projector_mode='center', yt=1.0)
    assert np.allclose(k0, k0.conj().T)
    assert np.allclose(k1, k1.conj().T)
    assert np.allclose(k2, k2.conj().T)


def test_mbp_trace_and_fd_consistency_on_identity_background() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    links = identity_links(lattice.edges)
    result = extract_mbp_bilinear(lattice, links, projector_mode='center', reg_epsilon=1e-3, cutoff=1e-6, fd_step=1e-3)
    assert result.masked_modes > 0
    assert result.gamma_consistency_gap < 5e-3


def test_random_background_changes_mu2_proxy() -> None:
    lattice = build_bcc_supercell(2, 2, 2)
    links0 = random_su2_links(lattice.edges, seed=1)
    links1 = random_su2_links(lattice.edges, seed=2)
    r0 = extract_mbp_bilinear(lattice, links0, projector_mode='positive_x', reg_epsilon=1e-3, cutoff=1e-6, fd_step=1e-3)
    r1 = extract_mbp_bilinear(lattice, links1, projector_mode='positive_x', reg_epsilon=1e-3, cutoff=1e-6, fd_step=1e-3)
    assert abs(r1.mu2_formula_proxy - r0.mu2_formula_proxy) > 1e-6
