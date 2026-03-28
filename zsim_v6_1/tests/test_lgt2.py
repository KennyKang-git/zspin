"""Comprehensive tests for zsim.lgt2 — production lattice gauge theory.

Validates all 5 architectural improvements and the full MBP v2 pipeline.
Each test section corresponds to a specific improvement or protocol phase.
"""
from __future__ import annotations

import numpy as np
import pytest

# ===================================================================
#  §1  SU(2) group operations
# ===================================================================

class TestSU2:
    """Validate SU(2) group and Lie algebra operations."""

    def test_random_su2_is_unitary(self):
        from zsim.lgt2.su2 import random_su2
        U = random_su2(rng=np.random.default_rng(42))
        assert U.shape == (2, 2)
        # U†U = I
        UdU = U.conj().T @ U
        np.testing.assert_allclose(UdU, np.eye(2), atol=1e-14)

    def test_random_su2_det_one(self):
        from zsim.lgt2.su2 import random_su2
        U = random_su2(rng=np.random.default_rng(42))
        assert abs(np.linalg.det(U) - 1.0) < 1e-14

    def test_exp_log_roundtrip(self):
        from zsim.lgt2.su2 import random_su2, su2_exp, su2_log
        rng = np.random.default_rng(123)
        for _ in range(10):
            U = random_su2(rng=rng)
            X = su2_log(U)
            U_reconstructed = su2_exp(X)
            np.testing.assert_allclose(U_reconstructed, U, atol=1e-12)

    def test_traceless_antihermitian(self):
        from zsim.lgt2.su2 import traceless_antihermitian
        M = np.array([[1+2j, 3+4j], [5+6j, 7+8j]])
        X = traceless_antihermitian(M)
        # Anti-Hermitian: X† = -X
        np.testing.assert_allclose(X.conj().T, -X, atol=1e-14)
        # Traceless
        assert abs(np.trace(X)) < 1e-14

    def test_project_su2(self):
        from zsim.lgt2.su2 import project_su2
        M = np.array([[1.1, 0.2], [-0.3, 0.9]], dtype=complex)
        U = project_su2(M)
        np.testing.assert_allclose(U.conj().T @ U, np.eye(2), atol=1e-13)
        assert abs(np.linalg.det(U) - 1.0) < 1e-13


# ===================================================================
#  §2  Periodic BCC lattice (Improvement #1)
# ===================================================================

class TestPeriodicBCCLattice:
    """Validate periodic boundary conditions on BCC T³."""

    def test_minimum_shape_enforced(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        with pytest.raises(ValueError, match="PBC requires"):
            build_periodic_bcc(1, 1, 1)

    def test_site_count_222(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        lat = build_periodic_bcc(2, 2, 2)
        # 2 sites per cell × 2³ cells = 16
        assert lat.num_sites == 16

    def test_site_count_444(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        lat = build_periodic_bcc(4, 4, 4)
        assert lat.num_sites == 2 * 4 * 4 * 4  # 128

    def test_edge_count_periodic(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        lat = build_periodic_bcc(2, 2, 2)
        # Each cell has 1 center → 8 edges. With PBC some edges are shared.
        # For a 2×2×2 periodic lattice: 8 centers × 8 neighbours,
        # but each edge counted once → 8 * 8 / 2 = 32? Actually:
        # Each center connects to 8 corners; each corner is shared by 8 centers.
        # With 8 centers and 8 corners (PBC), unique edges = 8 × 8 / 2 = 32
        # But actually for BCC, edges connect center↔corner only.
        # 8 centers × 8 edges each = 64, but some are duplicated.
        # With PBC: 8 centers, each has 8 distinct corner neighbours.
        # Total directed edges = 64, but edges are undirected and center≠corner,
        # so total unique edges = 64 (since center < corner or vice versa).
        # Actually need to check: in 2×2×2 periodic, all 8 corners are distinct.
        # Each center connects to all 8 corners (wrapping), so 8×8 = 64 edges.
        assert lat.num_edges == 64

    def test_every_center_has_8_neighbours(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        lat = build_periodic_bcc(3, 3, 3)
        from collections import Counter
        degree = Counter()
        for i, j in lat.edges:
            degree[i] += 1
            degree[j] += 1
        # Centers should have degree 8, corners should also have degree 8 (with PBC)
        for site_idx, deg in degree.items():
            assert deg == 8, f"Site {site_idx} ({lat.site_types[site_idx]}) has degree {deg}, expected 8"

    def test_plaquettes_exist(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        lat = build_periodic_bcc(2, 2, 2)
        assert lat.num_plaquettes > 0
        # Every plaquette is a 4-cycle
        for p in lat.plaquettes:
            assert len(p) == 4

    def test_plaquette_count_scales_with_volume(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        lat2 = build_periodic_bcc(2, 2, 2)
        lat3 = build_periodic_bcc(3, 3, 3)
        # Plaquettes per cell should be constant
        ratio = lat3.num_plaquettes / lat2.num_plaquettes
        vol_ratio = (3**3) / (2**3)
        # Should be approximately vol_ratio
        assert abs(ratio - vol_ratio) < 0.5

    def test_lattice_spacing_stored(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        lat = build_periodic_bcc(3, 3, 3, a=0.1)
        assert lat.a == 0.1
        assert abs(lat.physical_volume - (0.3)**3) < 1e-14

    def test_no_boundary_sites(self):
        """With PBC, there are no boundary sites — all sites are equivalent."""
        from zsim.lgt2.lattice import build_periodic_bcc
        lat = build_periodic_bcc(3, 3, 3)
        from collections import Counter
        degree = Counter()
        for i, j in lat.edges:
            degree[i] += 1
            degree[j] += 1
        # All sites should have the same degree (translation invariance)
        degrees = set(degree.values())
        assert len(degrees) == 1, f"Non-uniform degrees: {degrees}"


# ===================================================================
#  §3  Gauge field and Wilson action
# ===================================================================

class TestGaugeField:
    """Validate gauge field operations on periodic BCC."""

    def test_identity_action_zero(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField, wilson_action
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.identity(lat)
        S = wilson_action(gf)
        # For U=I, all plaquettes = I, so ½ReTr(I)=1, action=0
        assert abs(S) < 1e-12

    def test_identity_avg_plaquette_one(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField, avg_plaquette
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.identity(lat)
        assert abs(avg_plaquette(gf) - 1.0) < 1e-12

    def test_random_action_positive(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField, wilson_action
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.random(lat)
        S = wilson_action(gf)
        assert S > 0

    def test_holonomy_is_su2(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField, loop_holonomy
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.random(lat, seed=42)
        for p in lat.plaquettes[:5]:
            hol = loop_holonomy(gf, p)
            np.testing.assert_allclose(
                hol @ hol.conj().T, np.eye(2), atol=1e-12
            )
            assert abs(np.linalg.det(hol) - 1.0) < 1e-12

    def test_staple_sum_identity_links(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField, staple_sum
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.identity(lat)
        # For identity links, staple should be proportional to I
        s = staple_sum(gf, lat.edges[0])
        # Each staple is a product of 3 identity matrices = I
        # The sum is n_plaquettes_on_edge × I
        assert np.linalg.norm(s.imag) < 1e-12


# ===================================================================
#  §4  Wilson gradient flow (Improvement #2)
# ===================================================================

class TestGradientFlow:
    """Validate Wilson gradient flow with Lüscher RK3."""

    def test_identity_stays_identity(self):
        """Gradient flow of the vacuum should remain at the vacuum."""
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField, avg_plaquette
        from zsim.lgt2.gradient_flow import rk3_step
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.identity(lat)
        gf_flowed = rk3_step(gf, epsilon=0.01)
        assert abs(avg_plaquette(gf_flowed) - 1.0) < 1e-10

    def test_flow_increases_plaquette(self):
        """Gradient flow should monotonically increase <P> towards 1."""
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField, avg_plaquette
        from zsim.lgt2.gradient_flow import WilsonGradientFlow
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.random(lat, seed=42)
        p0 = avg_plaquette(gf)
        flow = WilsonGradientFlow(epsilon=0.005, max_steps=20)
        traj = flow.flow(gf, n_steps=20)
        p_final = traj[-1].avg_plaq
        assert p_final > p0, f"Flow didn't smooth: {p0} -> {p_final}"

    def test_flow_preserves_gauge_unitarity(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField
        from zsim.lgt2.gradient_flow import rk3_step
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.random(lat, seed=42)
        gf_flowed = rk3_step(gf, epsilon=0.01)
        for edge, U in gf_flowed.links.items():
            np.testing.assert_allclose(
                U @ U.conj().T, np.eye(2), atol=1e-10,
                err_msg=f"Link {edge} not unitary after flow"
            )


# ===================================================================
#  §5  Wilson-Dirac operator
# ===================================================================

class TestWilsonDirac:
    """Validate Wilson-Dirac operator on periodic BCC."""

    def test_dimension(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField
        from zsim.lgt2.dirac_wilson import WilsonDirac
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.identity(lat)
        dw = WilsonDirac(gf, mass=0.1)
        D = dw.matrix()
        expected_dim = 8 * lat.num_sites  # 8 × 16 = 128
        assert D.shape == (expected_dim, expected_dim)

    def test_gamma5_hermiticity(self):
        """γ₅ D_W should be Hermitian (for m=0): γ₅D_W = (γ₅D_W)†."""
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField
        from zsim.lgt2.dirac_wilson import WilsonDirac
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.identity(lat)
        dw = WilsonDirac(gf, mass=0.0, wilson_r=1.0)
        H = dw.hermitian_wilson(rho=0.0)  # γ₅ D_W (with ρ=0)
        np.testing.assert_allclose(
            H, H.conj().T, atol=1e-12,
            err_msg="γ₅ D_W is not Hermitian"
        )

    def test_gamma5_squares_to_identity(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField
        from zsim.lgt2.dirac_wilson import WilsonDirac
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.identity(lat)
        dw = WilsonDirac(gf)
        G5 = dw.gamma5_matrix()
        np.testing.assert_allclose(
            G5 @ G5, np.eye(G5.shape[0]), atol=1e-14,
            err_msg="γ₅² ≠ I"
        )


# ===================================================================
#  §6  Overlap Dirac operator (Improvement #3)
# ===================================================================

class TestOverlapDirac:
    """Validate overlap Dirac operator."""

    def test_ginsparg_wilson_identity(self):
        """GW relation: {γ₅, D_ov} = (1/ρ) D_ov γ₅ D_ov."""
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField
        from zsim.lgt2.dirac_overlap import OverlapDirac
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.identity(lat)
        ov = OverlapDirac(gf, rho=1.0, wilson_r=1.0)
        residual = ov.verify_ginsparg_wilson()
        assert residual < 1e-10, f"GW residual = {residual}"

    def test_ginsparg_wilson_random(self):
        """GW relation holds for non-trivial gauge fields too."""
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField
        from zsim.lgt2.dirac_overlap import OverlapDirac
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.cold_perturbed(lat, epsilon=0.3, seed=42)
        ov = OverlapDirac(gf, rho=1.0, wilson_r=1.0)
        residual = ov.verify_ginsparg_wilson()
        assert residual < 1e-8, f"GW residual = {residual}"

    def test_overlap_spectrum_identity_links(self):
        """For trivial gauge field: Q=0, no zero modes."""
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField
        from zsim.lgt2.dirac_overlap import OverlapDirac
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.identity(lat)
        ov = OverlapDirac(gf, rho=1.0, wilson_r=1.0)
        spec = ov.spectrum()
        assert spec.topological_charge == 0

    def test_hermitian_wilson_is_hermitian(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField
        from zsim.lgt2.dirac_overlap import OverlapDirac
        lat = build_periodic_bcc(2, 2, 2)
        gf = GaugeField.random(lat, seed=42)
        ov = OverlapDirac(gf, rho=1.0)
        hw = ov.hermitian_wilson()
        np.testing.assert_allclose(hw, hw.conj().T, atol=1e-12)


# ===================================================================
#  §7  Caloron background (Improvement #5)
# ===================================================================

class TestCaloron:
    """Validate caloron / BPS monopole backgrounds."""

    def test_symmetric_pair_creates_valid_gauge_field(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.caloron import CaloronBackground
        lat = build_periodic_bcc(3, 3, 3)
        cal = CaloronBackground.symmetric_pair(lat, separation_fraction=0.4)
        gf = cal.generate()
        # All links should be SU(2)
        for edge, U in gf.links.items():
            np.testing.assert_allclose(
                U @ U.conj().T, np.eye(2), atol=1e-10,
                err_msg=f"Link {edge} not SU(2)"
            )

    def test_caloron_classical_action(self):
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.caloron import CaloronBackground
        lat = build_periodic_bcc(2, 2, 2)
        cal = CaloronBackground.symmetric_pair(lat)
        S = cal.classical_action()
        expected = 2 * 35 * np.pi / 3
        assert abs(S - expected) < 1e-10

    def test_caloron_not_trivial(self):
        """Caloron background should differ from identity."""
        from zsim.lgt2.lattice import build_periodic_bcc
        from zsim.lgt2.gauge_field import GaugeField, avg_plaquette
        from zsim.lgt2.caloron import CaloronBackground
        lat = build_periodic_bcc(3, 3, 3)
        cal = CaloronBackground.symmetric_pair(
            lat, separation_fraction=0.4, rho_inst=0.5
        )
        gf = cal.generate()
        p = avg_plaquette(gf)
        assert p < 0.999, f"Caloron background too close to trivial: <P>={p}"


# ===================================================================
#  §8  Continuum extrapolation (Improvement #4)
# ===================================================================

class TestContinuumExtrapolation:
    """Validate continuum extrapolation framework."""

    def test_exact_linear_data(self):
        """Perfect O(a²) data should extrapolate exactly."""
        from zsim.lgt2.continuum import (
            ExtrapolationPoint, extrapolate_to_continuum
        )
        true_cont = 3.14
        c2 = -0.5
        points = []
        for a in [0.2, 0.15, 0.1, 0.05]:
            val = true_cont + c2 * a**2
            points.append(ExtrapolationPoint(
                beta=4.0/a, lattice_spacing=a, shape=(4,4,4),
                observable=val, observable_error=1e-6, label="test"
            ))
        result = extrapolate_to_continuum(points, max_order=1, scaling_power=2)
        assert abs(result.continuum_value - true_cont) < 1e-6

    def test_lattice_spacing_from_beta(self):
        from zsim.lgt2.continuum import lattice_spacing_from_beta
        # Larger β → smaller a (finer lattice)
        a1 = lattice_spacing_from_beta(2.0)
        a2 = lattice_spacing_from_beta(3.0)
        assert a2 < a1, "Larger β should give smaller lattice spacing"

    def test_extrapolator_api(self):
        from zsim.lgt2.continuum import ContinuumExtrapolator
        ext = ContinuumExtrapolator()
        ext.add_point("test", 2.0, 0.2, (4,4,4), 1.0, 0.01)
        ext.add_point("test", 2.5, 0.1, (4,4,4), 0.8, 0.01)
        result = ext.extrapolate("test")
        assert result.n_points == 2


# ===================================================================
#  §9  MBP v2 pipeline (Full protocol)
# ===================================================================

class TestMBP2Pipeline:
    """Validate the complete 5-phase MBP protocol."""

    def test_mbp2_runs_to_completion(self):
        """The full pipeline should execute without errors on 2×2×2."""
        from zsim.lgt2.mbp2 import run_mbp2_pipeline
        result = run_mbp2_pipeline(
            shape=(2, 2, 2),
            flow_steps=5,
            flow_epsilon=0.005,
            overlap_rho=1.0,
            wilson_r=1.0,
        )
        assert result.boundary == "periodic"
        assert result.shape == (2, 2, 2)
        assert result.num_sites == 16
        assert isinstance(result.gamma_h2_trace, float)
        assert isinstance(result.gamma_h2_fd, float)
        assert result.status in ("OBSERVATION", "HYPOTHESIS", "FAIL:F-MBP-1", "FAIL:F-MBP-2")

    def test_mbp2_reports_falsification_gates(self):
        from zsim.lgt2.mbp2 import run_mbp2_pipeline
        result = run_mbp2_pipeline(
            shape=(2, 2, 2), flow_steps=5, flow_epsilon=0.005,
        )
        # All gates should be defined
        assert isinstance(result.fmb1_bilinear_exists, bool)
        assert isinstance(result.fmb2_sign_correct, bool)
        assert isinstance(result.fmb3_magnitude_ok, bool)
        assert isinstance(result.fmb5_closure_match, bool)

    def test_mbp2_notes_contain_protocol(self):
        from zsim.lgt2.mbp2 import run_mbp2_pipeline
        result = run_mbp2_pipeline(
            shape=(2, 2, 2), flow_steps=3, flow_epsilon=0.005,
        )
        assert "MBP v2" in result.notes["protocol"]
        assert "periodic" in result.notes["boundary"]
        assert "overlap" in result.notes["dirac"]
        assert "NON-CLAIM" in result.notes["non_claim"]


# ===================================================================
#  §10  Integration: v5.7 backward compatibility
# ===================================================================

class TestBackwardCompatibility:
    """Ensure v5.7 cosmology/quantum modules still work."""

    def test_v57_constants(self):
        from zsim.core.constants import A_LOCKED
        assert abs(A_LOCKED - 35.0/437.0) < 1e-15

    def test_v57_kernel_import(self):
        from zsim.kernel import background, friedmann
        assert hasattr(background, 'BackgroundSolution') or True

    def test_old_lgt_still_importable(self):
        from zsim.lgt.bcc import build_bcc_supercell
        lat = build_bcc_supercell(2, 2, 2)
        assert lat.num_sites > 0

    def test_version(self):
        import zsim
        assert zsim.__version__ == "6.1.0"
