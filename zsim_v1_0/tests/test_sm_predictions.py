"""Z-Sim v1.0 — SM Prediction Test Suite (Grand Reset).

Honestly labels each test as PREDICT, FIT, PROVEN, or HARDCODED.
"""
import math, sys, os
import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fractions import Fraction
from zsim.core.constants import *


class TestPolyhedralInvariants:
    def test_TO_euler(self): assert V_TO - E_TO + F_TO == 2
    def test_TI_euler(self): assert V_TI - E_TI + F_TI == 2
    def test_TO_counts(self): assert (V_TO, E_TO, F_TO) == (24, 36, 14)
    def test_TI_counts(self): assert (V_TI, E_TI, F_TI) == (60, 90, 32)
    def test_mode_count_TO(self): assert VF_TO == 38
    def test_mode_count_TI(self): assert VF_TI == 92
    def test_symmetry_orders(self):
        assert ORDER_O_H == 48 and ORDER_I == 60 and ORDER_I_H == 120
    def test_2V_TO_equals_Oh(self): assert 2 * V_TO == ORDER_O_H
    def test_V_TI_equals_I(self): assert V_TI == ORDER_I
    def test_beta0_Z(self): assert BETA0_Z == 1


class TestGaugeCouplings:
    def test_alpha_s_exact(self): assert ALPHA_S_FRAC == Fraction(11, 93)
    def test_alpha_s_pull(self):
        assert abs((ALPHA_S - PDG_ALPHA_S) / PDG_ALPHA_S_ERR) < 1.0
    def test_sin2_theta_w_formula(self):
        assert abs(SIN2_THETA_W - (48.0/91.0)*X_STAR) < 1e-15
    def test_sin2_theta_w_pull(self):
        assert abs((SIN2_THETA_W - PDG_SIN2_THETA_W) / PDG_SIN2_THETA_W_ERR) < 2.0
    def test_alpha_2_exact(self): assert ALPHA_2_FRAC == Fraction(3, 95)
    def test_beta_su2(self): assert BETA_COEFF_SU2_FRAC == Fraction(19, 6)
    def test_beta_su3(self): assert BETA_COEFF_SU3_FRAC == Fraction(23, 3)
    def test_c4_nlo_exact(self): assert C4_NLO_FRAC == Fraction(4, 13)
    def test_alpha_em_ppm(self):
        ppm = abs(ALPHA_EM_INV_NLO - PDG_ALPHA_EM_INV) / PDG_ALPHA_EM_INV * 1e6
        assert ppm < 2.0


class TestEWSB:
    def test_d_eff(self): assert D_EFF == 9
    def test_gamma_cw(self): assert GAMMA_CW_FRAC == Fraction(38, 9)
    def test_higgs_vev_deviation(self):
        assert abs(HIGGS_VEV - PDG_HIGGS_VEV) / PDG_HIGGS_VEV * 100 < 0.5


class TestIcosahedralGroup:
    @pytest.fixture(scope="class")
    def ig(self):
        from zsim.sm.icosahedral import build_icosahedral_group
        return build_icosahedral_group()

    def test_group_order(self, ig): assert ig.order == 60
    def test_conjugacy_classes(self, ig):
        assert sorted([c.size for c in ig.classes]) == [1, 12, 12, 15, 20]
    def test_yukawa_unique(self, ig): assert ig.yukawa_unique is True
    def test_rep4_dim(self, ig):
        assert ig.rep4[0].shape == (4, 4)
        assert abs(np.trace(ig.rep4[0]) - 4.0) < 0.01
    def test_rep4_character(self, ig):
        phi = (1 + math.sqrt(5)) / 2
        for i, R3 in enumerate(ig.rep3):
            tr3, tr4 = np.trace(R3), np.trace(ig.rep4[i]).real
            if abs(tr3 - 3.0) < 0.01: assert abs(tr4 - 4) < 0.01
            elif abs(tr3 + 1.0) < 0.01: assert abs(tr4) < 0.01
            elif abs(tr3) < 0.1: assert abs(tr4 - 1) < 0.01
    def test_schur_conservation(self, ig):
        from zsim.sm.yukawa import mass_eigenvalues
        rng = np.random.RandomState(42)
        for _ in range(20):
            v = rng.randn(5); v /= np.linalg.norm(v)
            assert abs(mass_eigenvalues(ig.yukawa_tensor, v).schur_check - 0.2) < 0.001


class TestD5Channels:
    """[PROVEN] D5 Clebsch-Gordan decomposition."""
    @pytest.fixture(scope="class")
    def d5(self):
        from zsim.sm.icosahedral import build_icosahedral_group
        from zsim.sm.yukawa import d5_channel_decomposition
        ig = build_icosahedral_group()
        return d5_channel_decomposition(ig.yukawa_tensor, ig.rep3, ig.rep5,
                                         ig.rep3p, ig.rotations)

    def test_lepton_fraction(self, d5): assert abs(d5.fractions['lepton'] - 1/5) < 1e-6
    def test_small_channels(self, d5):
        assert abs(d5.fractions['quark-A'] - 2/15) < 1e-6
        assert abs(d5.fractions['quark-B'] - 2/15) < 1e-6
    def test_large_channels(self, d5):
        assert abs(d5.fractions['quark-C'] - 4/15) < 1e-6
        assert abs(d5.fractions['quark-D'] - 4/15) < 1e-6
    def test_schur_sum(self, d5): assert abs(d5.schur_sum - 1.0) < 1e-10
    def test_sqrt2(self, d5): assert abs(d5.quark_lepton_ratio - math.sqrt(2)) < 1e-10
    def test_silver_ratio(self, d5): assert abs(d5.silver_ratio - (1+math.sqrt(2))) < 1e-10


class TestRestrictedVEV:
    @pytest.fixture(scope="class")
    def ig(self):
        from zsim.sm.icosahedral import build_icosahedral_group
        return build_icosahedral_group()
    def test_hierarchy(self, ig):
        from zsim.sm.yukawa import restricted_vev_predict
        m10 = restricted_vev_predict(ig.yukawa_tensor, ig.rep5, ig.rotations)
        assert m10.ratio_12 > 10 and m10.ratio_13 > 1000
        assert abs(m10.schur_check - 0.2) < 0.001


class TestFitVEV:
    @pytest.fixture(scope="class")
    def ig(self):
        from zsim.sm.icosahedral import build_icosahedral_group
        return build_icosahedral_group()
    def test_fit_achievable(self, ig):
        from zsim.sm.yukawa import fit_vev_s4
        m11 = fit_vev_s4(ig.yukawa_tensor)
        assert abs(m11.ratio_12 - 17.0) < 1.0 and abs(m11.ratio_13 - 3477) < 100


class TestVEVForward:
    @pytest.fixture(scope="class")
    def pred(self):
        from zsim.sm.icosahedral import build_icosahedral_group
        from zsim.sm.yukawa import predict_vev_from_quartic
        ig = build_icosahedral_group()
        return predict_vev_from_quartic(ig.yukawa_tensor, ig.rep5)
    def test_hierarchy_at_cw_scale(self, pred): assert pred.spectrum.ratio_12 > 10
    def test_cw_scale(self, pred): assert abs(pred.cw_scale_pct - 0.63) < 0.15
    def test_schur_preserved(self, pred): assert abs(pred.spectrum.schur_check - 0.2) < 0.001


class TestCKM:
    def test_cabibbo(self):
        from zsim.sm.icosahedral import build_icosahedral_group
        from zsim.sm.yukawa import compute_ckm
        ig = build_icosahedral_group()
        ckm = compute_ckm(ig.rep3, ig.rep5, ig.rotations)
        assert abs(ckm.raw_principal_angle_deg - 18.61) < 1.0
        assert ckm.color_factor == 0.75
        assert abs(ckm.cabibbo_angle_deg - 13.96) < 0.5
    def test_cabibbo_geometric(self):
        phi = (1 + math.sqrt(5)) / 2
        assert abs(math.degrees(math.atan(1/phi**3)) - 13.04) / 13.04 < 0.03
    def test_a4_overlap_computed(self):
        """[COMPUTED] r_A4 from A₄ generation projector, not hardcoded."""
        from zsim.sm.icosahedral import build_icosahedral_group
        from zsim.sm.yukawa import compute_a4_overlap
        ig = build_icosahedral_group()
        a4 = compute_a4_overlap(ig.rep3, ig.rotations)
        assert abs(a4["dominant"] - 0.631) < 0.01
        assert abs(a4["subdominant"] - 0.184) < 0.01
        assert abs(a4["r_a4"] - 0.292) < 0.005
        assert abs(sum(a4["overlaps"]) - 1.0) < 1e-10


class TestQuartic:
    @pytest.fixture(scope="class")
    def ig(self):
        from zsim.sm.icosahedral import build_icosahedral_group
        return build_icosahedral_group()
    def test_reynolds_invariance(self, ig):
        from zsim.sm.yukawa import reynolds_quartic
        v = np.array([.3,.5,-.2,.7,-.1]); v /= np.linalg.norm(v)
        p4 = reynolds_quartic(v, ig.rep5)
        for M in ig.rep5[:20]:
            assert abs(reynolds_quartic(M@v, ig.rep5) - p4) < 1e-10
    def test_anticorrelation(self, ig):
        from zsim.sm.yukawa import reynolds_quartic, mass_eigenvalues
        rng = np.random.RandomState(42)
        p4s, s4s = [], []
        for _ in range(200):
            v = rng.randn(5); v /= np.linalg.norm(v)
            p4s.append(reynolds_quartic(v, ig.rep5))
            sp = mass_eigenvalues(ig.yukawa_tensor, v)
            s4s.append(sp.sigma_1**4 + sp.sigma_2**4 + sp.sigma_3**4)
        assert abs(np.corrcoef(p4s, s4s)[0, 1] + 1.0) < 0.001


class TestM0Lattice:
    def test_nlo_c4(self):
        from zsim.sm.m0_lattice import compute_nlo_coefficient
        r = compute_nlo_coefficient()
        assert abs(r['c4_corpus_4_13'] - 4/13) < 1e-15
        assert r['precision_4_13_ppm'] < 2.0
    def test_zeta5(self):
        from zsim.sm.m0_lattice import zeta5_bridge
        z = zeta5_bridge()
        assert z['c4_fraction'] == '4/13'
        assert z['precision_pct'] < 1.0


class TestHonestyDeclarations:
    def test_d5_proven(self):
        from zsim.sm.yukawa import d5_channel_status
        assert "PROVEN" in d5_channel_status()
    def test_fit_name(self):
        from zsim.sm import yukawa
        assert hasattr(yukawa, 'fit_vev_s4')
        assert not hasattr(yukawa, 'derive_vev_s4')
    def test_predict_exists(self):
        from zsim.sm import yukawa
        assert hasattr(yukawa, 'predict_vev_from_quartic')


class TestIntegration:
    def test_full_pipeline(self):
        from zsim.sm.report import run_full_pipeline
        r = run_full_pipeline(verbose=False)
        assert r["group_order"] == 60
        assert r["yukawa_unique"] is True
        assert abs(r["schur_sum"] - 0.2) < 0.001
        assert abs(r["d5_lepton"] - 0.2) < 0.001
        assert abs(r["d5_sqrt2"] - math.sqrt(2)) < 0.01


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])


class TestMcKayBridge:
    """[PROVEN] McKay correspondence Z₅→Â₄→SU(5)→SM."""
    @pytest.fixture(scope="class")
    def mckay(self):
        from zsim.sm.icosahedral import build_icosahedral_group
        from zsim.sm.mckay_bridge import compute_mckay_bridge
        ig = build_icosahedral_group()
        return compute_mckay_bridge(ig)

    def test_cross_verification_14_14(self, mckay):
        assert mckay.n_pass == 14, f"Cross-checks: {mckay.n_pass}/14"

    def test_z5_complementary(self, mckay):
        """3 and 3' carry complementary Z₅ charges (2:3 problem resolution)."""
        br3 = mckay.branching_rules[(3, "Z5")]
        br3p = mckay.branching_rules[("3p", "Z5")]
        assert br3.decomposition != br3p.decomposition

    def test_a4_irreducible(self, mckay):
        """3→3 under A₄ (generation structure)."""
        br = mckay.branching_rules[(3, "A4")]
        assert br.decomposition == {"3": 1}

    def test_d5_no_gauge_singlet(self, mckay):
        """Irrep 4 has no D₅-trivial component (gauge-color separation)."""
        br = mckay.branching_rules[(4, "D5")]
        assert "1" not in br.decomposition

    def test_chirality_sum(self, mckay):
        """Σ dᵢΔᵢ = 2 = dim(Z)."""
        s = sum(({1:1,3:3,"3p":3,4:4,5:5}[k]) * v
                for k, v in mckay.chirality.items())
        assert s == 2
