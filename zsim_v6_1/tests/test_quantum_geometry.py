import numpy as np

from zsim.quantum.geometry import build_truncated_icosahedron, build_truncated_octahedron
from zsim.quantum.incidence import assert_boundary_nilpotency, boundary_matrices


def test_truncated_icosahedron_counts():
    complex_ = build_truncated_icosahedron()
    assert (complex_.V, complex_.E, complex_.F) == (60, 90, 32)
    assert np.allclose(complex_.degree_sequence(), 3.0)


def test_truncated_octahedron_counts():
    complex_ = build_truncated_octahedron()
    assert (complex_.V, complex_.E, complex_.F) == (24, 36, 14)
    assert np.allclose(complex_.degree_sequence(), 3.0)


def test_boundary_nilpotency_for_ti():
    complex_ = build_truncated_icosahedron()
    B1, B2 = boundary_matrices(complex_)
    assert B1.shape == (60, 90)
    assert B2.shape == (90, 32)
    assert_boundary_nilpotency(B1, B2)
