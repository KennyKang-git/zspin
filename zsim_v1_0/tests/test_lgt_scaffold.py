import numpy as np

from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.fermion import gauge_covariant_hopping_matrix
from zsim.lgt.loops import enumerate_bcc_rhombic_plaquettes
from zsim.lgt.su2_links import identity_links, random_su2
from zsim.lgt.wilson import plaquette_observables


def test_random_su2_is_unitary():
    U = random_su2(rng=np.random.default_rng(123))
    assert np.allclose(U.conj().T @ U, np.eye(2), atol=1e-12)
    assert np.allclose(np.linalg.det(U), 1.0 + 0.0j, atol=1e-12)


def test_bcc_supercell_counts():
    lattice = build_bcc_supercell(1, 1, 1)
    assert lattice.num_sites == 9
    assert lattice.num_edges == 8


def test_bcc_multicell_has_plaquettes():
    lattice = build_bcc_supercell(2, 2, 2)
    plaquettes = enumerate_bcc_rhombic_plaquettes(lattice)
    assert len(plaquettes) == 48
    obs = plaquette_observables(identity_links(lattice.edges), plaquettes)
    assert obs['avg_plaquette'] == 1.0


def test_gauge_covariant_hopping_is_hermitian():
    lattice = build_bcc_supercell(1, 1, 1)
    H = gauge_covariant_hopping_matrix(lattice.num_sites, lattice.edges, identity_links(lattice.edges), mass=0.25)
    assert H.shape == (18, 18)
    assert np.allclose(H, H.conj().T)
