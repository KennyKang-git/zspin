"""Quantum geometry and spectral tools for Z-Sim v1.0."""

from zsim.quantum.geometry import PolyhedralComplex, build_truncated_icosahedron, build_truncated_octahedron
from zsim.quantum.incidence import boundary_matrices
from zsim.quantum.hodge import hodge_laplacians
from zsim.quantum.dirac import hodge_dirac
from zsim.quantum.spectrum import eigensystem, spectral_summary

__all__ = [
    'PolyhedralComplex', 'build_truncated_icosahedron', 'build_truncated_octahedron',
    'boundary_matrices', 'hodge_laplacians', 'hodge_dirac', 'eigensystem', 'spectral_summary',
]
