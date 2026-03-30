from __future__ import annotations

from zsim.apps.su2_mbp_stage6_pairing_validate import run_su2_mbp_stage6_pairing_validate


def test_stage6_app_outputs(tmp_path) -> None:
    summary = run_su2_mbp_stage6_pairing_validate(
        shape=(1, 1, 1),
        output_dir=tmp_path,
        scan_schemes=('reduced2',),
        compare_schemes=('reduced2', 'staggered2'),
        amplitudes=(0.4, 0.7),
        separations=(0.55,),
        widths=(0.45,),
        seam_biases=(0.10, 0.20),
        mass=0.10,
        kappa=0.5,
        reg_epsilon=1e-4,
        cutoff=1e-6,
        fd_step=5e-4,
        seed=17,
    )
    assert summary['success'] is True
    assert (tmp_path / 'stage6_scan_rows.csv').exists()
    assert (tmp_path / 'stage6_scheme_rows.csv').exists()
    assert (tmp_path / 'stage6_pairing_summary.json').exists()
