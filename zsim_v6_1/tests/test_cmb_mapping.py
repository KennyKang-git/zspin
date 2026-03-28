"""Tests for CMB parameter mapping and face counting.

Two counting systems coexist in Z-Spin:
  SLOT counting (DERIVED):  CDM = 33/121 = X*Q/Q^2
  FACE counting (OBSERVATION): CDM = 32/121 = F(truncated icosahedron)/Q^2

Cobaya validation (2026-03-18):
  Slot -> Dchi2 = 226  FAIL
  Face -> Dchi2 = 3.9  PASS
"""
import math
import pytest
from zsim.core.constants import (
    A_LOCKED, G_EFF_RATIO, H0_RATIO,
    OMEGA_M_BARE, OMEGA_CDM_SLOT,
    F_TETRAHEDRON, F_CUBE, F_OCTAHEDRON, F_DODECAHEDRON,
    F_ICOSAHEDRON, F_TRUNCATED_ICOSAHEDRON,
    OMEGA_B_FACE, OMEGA_CDM_FACE, OMEGA_M_FACE, OMEGA_LAMBDA_FACE,
    OMEGA_CDM_BARE, OMEGA_B_BARE,
    CMB_H0, CMB_H, CMB_OMBH2, CMB_OMCH2, CMB_NS, CMB_H0_LOCAL,
    TIER09_DCHI2_FACE, TIER09_DCHI2_SLOT, Q_TOTAL,
)


class TestPlatonicFaces:
    def test_tetrahedron(self):
        assert F_TETRAHEDRON == 4
    def test_cube(self):
        assert F_CUBE == 6
    def test_octahedron(self):
        assert F_OCTAHEDRON == 8
    def test_dodecahedron(self):
        assert F_DODECAHEDRON == 12
    def test_icosahedron(self):
        assert F_ICOSAHEDRON == 20
    def test_truncated_icosahedron(self):
        assert F_TRUNCATED_ICOSAHEDRON == 32
        assert F_TRUNCATED_ICOSAHEDRON == F_DODECAHEDRON + F_ICOSAHEDRON
    def test_sector_face_sums(self):
        assert F_TETRAHEDRON*2 == 8
        assert F_CUBE + F_OCTAHEDRON == 14
        assert F_DODECAHEDRON + F_ICOSAHEDRON == 32


class TestFaceCounting:
    def test_baryon_face_equals_slot(self):
        assert OMEGA_B_FACE == OMEGA_B_BARE
        assert abs(OMEGA_B_FACE - 6.0/121.0) < 1e-15
    def test_cdm_face(self):
        assert abs(OMEGA_CDM_FACE - 32.0/121.0) < 1e-15
    def test_cdm_slot_different(self):
        assert abs(OMEGA_CDM_SLOT - 33.0/121.0) < 1e-15
        assert OMEGA_CDM_FACE != OMEGA_CDM_SLOT
    def test_matter_face(self):
        assert abs(OMEGA_M_FACE - 38.0/121.0) < 1e-15
    def test_dark_energy_face(self):
        assert abs(OMEGA_LAMBDA_FACE - 83.0/121.0) < 1e-15
    def test_budget_sums_to_one(self):
        assert 6 + 32 + 83 == 121
        assert abs(OMEGA_B_FACE + OMEGA_CDM_FACE + OMEGA_LAMBDA_FACE - 1.0) < 1e-15
    def test_cdm_bare_uses_face(self):
        assert OMEGA_CDM_BARE == OMEGA_CDM_FACE


class TestCMBMapping:
    def test_cmb_ombh2(self):
        assert abs(CMB_OMBH2 - 6.0/121.0*(67.36/100)**2) < 1e-10
    def test_cmb_omch2(self):
        assert abs(CMB_OMCH2 - 32.0/121.0*(67.36/100)**2) < 1e-10
        assert abs(CMB_OMCH2 - 0.12000) < 0.0001
    def test_cmb_h0(self):
        assert CMB_H0 == 67.36
    def test_cmb_h0_local(self):
        assert abs(CMB_H0_LOCAL - 67.36*math.exp(A_LOCKED)) < 1e-10
        assert abs(CMB_H0_LOCAL - 73.04)/1.04 < 1.0
    def test_cmb_ns(self):
        assert CMB_NS == 0.9674


class TestCobayaValidation:
    def test_face_passes(self):
        assert TIER09_DCHI2_FACE < 10
    def test_slot_fails(self):
        assert TIER09_DCHI2_SLOT > 25
    def test_face_better(self):
        assert TIER09_DCHI2_FACE < TIER09_DCHI2_SLOT


class TestAntiNumerology:
    def test_32_is_geometric(self):
        assert F_TRUNCATED_ICOSAHEDRON == 32
    def test_uniqueness(self):
        h = 0.6736
        count = sum(1 for n in range(1,121)
                    if abs(n/121*h**2 - 0.1200) < 0.0012)
        assert count == 1
    def test_planck_precision(self):
        assert abs(32.0/121.0*0.6736**2 - 0.1200)/0.1200 < 0.001
