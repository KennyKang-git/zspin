from __future__ import annotations

from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.backgrounds import caloron_pair_links
from zsim.lgt.overlap import evaluate_overlap_background_with_method
from zsim.lgt.stage8 import build_stage8_ledger, evaluate_sign_method_bundle, run_stage8_pipeline


def test_overlap_sign_methods_are_finite() -> None:
    lattice = build_bcc_supercell(1, 1, 1)
    links = caloron_pair_links(lattice.edges, lattice.positions, 0.6, separation=0.55, width=0.45, seam_bias=0.15)
    for method in ('smooth', 'tanh', 'rational'):
        summary = evaluate_overlap_background_with_method(lattice, links, mass=0.10, kappa=0.5, sign_epsilon=1e-4, sign_method=method)
        assert summary.score > 0.0
        assert summary.gw_residual >= 0.0


def test_stage8_sign_bundle_and_ledger() -> None:
    lattice = build_bcc_supercell(1, 1, 1)
    links = caloron_pair_links(lattice.edges, lattice.positions, 0.6, separation=0.55, width=0.45, seam_bias=0.15)
    sign_rows, selected = evaluate_sign_method_bundle(lattice, links, sign_methods=('smooth', 'tanh', 'rational'), mass=0.10, kappa=0.5, sign_epsilon=1e-4)
    assert len(sign_rows) == 3
    assert selected in {'smooth', 'tanh', 'rational'}
    ledger_rows, scheme = build_stage8_ledger(lattice, links, schemes=('reduced2', 'wilson4'), selected_sign_method=selected, mass=0.10, kappa=0.5, reg_epsilon=1e-4, cutoff=1e-6, fd_step=5e-4, sign_epsilon=1e-4)
    assert len(ledger_rows) == 2
    assert scheme in {'reduced2', 'wilson4'}


def test_stage8_pipeline_runs() -> None:
    lattice = build_bcc_supercell(1, 1, 1)
    summary, _links, payload = run_stage8_pipeline(
        lattice,
        amplitude_grid=(0.4, 0.7),
        separation_grid=(0.55,),
        width_grid=(0.45,),
        seam_bias_grid=(0.10, 0.20),
        scan_schemes=('staggered2', 'wilson4'),
        compare_schemes=('reduced2', 'staggered2', 'wilson4'),
        sign_methods=('smooth', 'tanh', 'rational'),
        mass=0.10,
        kappa=0.5,
        reg_epsilon=1e-4,
        cutoff=1e-6,
        fd_step=5e-4,
        sign_epsilon=1e-4,
    )
    assert len(summary.sign_rows) == 3
    assert len(summary.ledger_rows) == 3
    assert payload['gates']['G-WILSON-IN-LEDGER'] is True
