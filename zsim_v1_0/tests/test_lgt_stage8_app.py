from __future__ import annotations

from zsim.apps.su2_mbp_stage8_sign_ledger_validate import run_su2_mbp_stage8_sign_ledger_validate


def test_stage8_app_outputs(tmp_path) -> None:
    summary = run_su2_mbp_stage8_sign_ledger_validate(
        shape=(1, 1, 1),
        output_dir=tmp_path,
        scan_schemes=('staggered2', 'wilson4'),
        compare_schemes=('reduced2', 'staggered2', 'wilson4'),
        sign_methods=('smooth', 'tanh', 'rational'),
        amplitudes=(0.4, 0.7),
        separations=(0.55,),
        widths=(0.45,),
        seam_biases=(0.10, 0.20),
        mass=0.10,
        kappa=0.5,
        reg_epsilon=1e-4,
        cutoff=1e-6,
        fd_step=5e-4,
        sign_epsilon=1e-4,
    )
    assert summary['success'] is True
    assert (tmp_path / 'stage8_sign_rows.csv').exists()
    assert (tmp_path / 'stage8_ledger_rows.csv').exists()
    assert (tmp_path / 'stage8_summary.json').exists()
