from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.flow import cooling_trajectory
from zsim.lgt.loops import enumerate_bcc_rhombic_plaquettes
from zsim.lgt.mbp import extract_mbp_bilinear, mbp_prefactor
from zsim.lgt.su2_links import identity_links, random_su2_links
from zsim.lgt.valley import collective_valley_links


DEFAULT_AMPLITUDES = (-0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75)
DEFAULT_SHAPES = ((4, 4, 4), (6, 4, 4), (6, 6, 4), (8, 6, 4), (8, 8, 4), (8, 10, 4))
DEFAULT_ADAPTIVE_CHIRALITIES = ('left', 'right', 'vector')
DEFAULT_ADAPTIVE_R_GRID = (0.25, 0.5, 0.75, 1.0, 1.25)


@dataclass(frozen=True)
class Stage26ShapeRow:
    shape: tuple[int, int, int]
    grid_extent: int
    fixed_chirality_mode: str
    fixed_wilson_r: float
    fixed_best_amplitude: float
    fixed_gap: float
    fixed_sign_match: bool
    fixed_mu2_formula_proxy: float
    fixed_gamma_h2_trace: float
    fixed_gamma_h2_fd: float
    fixed_sigma_min: float
    fixed_sigma_next: float
    adaptive_chirality_mode: str
    adaptive_wilson_r: float
    adaptive_best_amplitude: float
    adaptive_gap: float
    adaptive_sign_match: bool
    adaptive_mu2_formula_proxy: float
    adaptive_gamma_h2_trace: float
    adaptive_gamma_h2_fd: float
    adaptive_sigma_min: float
    adaptive_sigma_next: float
    winner_mode: str
    winner_chirality_mode: str
    winner_wilson_r: float
    winner_best_amplitude: float
    winner_gap: float
    winner_sign_match: bool
    winner_mu2_formula_proxy: float
    winner_gamma_h2_trace: float
    winner_gamma_h2_fd: float
    winner_sigma_min: float
    winner_sigma_next: float
    stage25_scheme_match: bool
    stage25_shape_match: bool
    improvement_over_fixed: float
    winner_score: float

    def to_dict(self) -> dict[str, object]:
        return {
            'shape': 'x'.join(str(v) for v in self.shape),
            'grid_extent': self.grid_extent,
            'fixed_chirality_mode': self.fixed_chirality_mode,
            'fixed_wilson_r': self.fixed_wilson_r,
            'fixed_best_amplitude': self.fixed_best_amplitude,
            'fixed_gap': self.fixed_gap,
            'fixed_sign_match': self.fixed_sign_match,
            'fixed_mu2_formula_proxy': self.fixed_mu2_formula_proxy,
            'fixed_gamma_h2_trace': self.fixed_gamma_h2_trace,
            'fixed_gamma_h2_fd': self.fixed_gamma_h2_fd,
            'fixed_sigma_min': self.fixed_sigma_min,
            'fixed_sigma_next': self.fixed_sigma_next,
            'adaptive_chirality_mode': self.adaptive_chirality_mode,
            'adaptive_wilson_r': self.adaptive_wilson_r,
            'adaptive_best_amplitude': self.adaptive_best_amplitude,
            'adaptive_gap': self.adaptive_gap,
            'adaptive_sign_match': self.adaptive_sign_match,
            'adaptive_mu2_formula_proxy': self.adaptive_mu2_formula_proxy,
            'adaptive_gamma_h2_trace': self.adaptive_gamma_h2_trace,
            'adaptive_gamma_h2_fd': self.adaptive_gamma_h2_fd,
            'adaptive_sigma_min': self.adaptive_sigma_min,
            'adaptive_sigma_next': self.adaptive_sigma_next,
            'winner_mode': self.winner_mode,
            'winner_chirality_mode': self.winner_chirality_mode,
            'winner_wilson_r': self.winner_wilson_r,
            'winner_best_amplitude': self.winner_best_amplitude,
            'winner_gap': self.winner_gap,
            'winner_sign_match': self.winner_sign_match,
            'winner_mu2_formula_proxy': self.winner_mu2_formula_proxy,
            'winner_gamma_h2_trace': self.winner_gamma_h2_trace,
            'winner_gamma_h2_fd': self.winner_gamma_h2_fd,
            'winner_sigma_min': self.winner_sigma_min,
            'winner_sigma_next': self.winner_sigma_next,
            'stage25_scheme_match': self.stage25_scheme_match,
            'stage25_shape_match': self.stage25_shape_match,
            'improvement_over_fixed': self.improvement_over_fixed,
            'winner_score': self.winner_score,
        }


@dataclass(frozen=True)
class Stage26Summary:
    selected_shape: tuple[int, int, int]
    selected_source_label: str
    selected_scheme: str
    selected_chirality_mode: str
    selected_wilson_r: float
    selected_sign_match: bool
    shape_rows: list[Stage26ShapeRow]
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {
            'selected_shape': list(self.selected_shape),
            'selected_source_label': self.selected_source_label,
            'selected_scheme': self.selected_scheme,
            'selected_chirality_mode': self.selected_chirality_mode,
            'selected_wilson_r': self.selected_wilson_r,
            'selected_sign_match': self.selected_sign_match,
            'shape_rows': [row.to_dict() for row in self.shape_rows],
            'notes': dict(self.notes),
        }


def _load_payload(path: str | Path) -> Mapping[str, Any]:
    return json.loads(Path(path).read_text(encoding='utf-8'))


def _shape_size(shape: tuple[int, int, int]) -> int:
    nx, ny, nz = shape
    return int(nx * ny * nz)


def _sign_match(trace_value: float, fd_value: float) -> bool:
    if abs(trace_value) <= 1e-15 or abs(fd_value) <= 1e-15:
        return True
    return (trace_value > 0.0) == (fd_value > 0.0)


def _score(gap: float, sign_match: bool, mu2: float) -> float:
    penalty = 0.0 if sign_match else 0.25
    boost = 1.0 / (1.0 + abs(mu2))
    return float(gap + penalty + 0.01 * boost)


def _build_links(background: str, lattice, amplitude: float, *, seed: int, cooling_steps: int, alpha: float):
    if background == 'collective':
        return collective_valley_links(lattice.edges, lattice.positions, amplitude)
    if background == 'identity':
        return identity_links(lattice.edges)
    base = random_su2_links(lattice.edges, seed=seed + int(round(1000.0 * amplitude)))
    plaquettes = enumerate_bcc_rhombic_plaquettes(lattice)
    cooled = cooling_trajectory(base, cooling_steps, plaquettes, alpha=alpha)
    return cooled[-1]


def _run_single(*, lattice, background: str, amplitude: float, chirality_mode: str, fermion_scheme: str, wilson_r: float, yt: float, nc: float, mass: float, reg_epsilon: float, cutoff: float, fd_step: float, projector_mode: str, seed: int, cooling_steps: int, alpha: float) -> dict[str, object]:
    links = _build_links(background, lattice, float(amplitude), seed=seed, cooling_steps=cooling_steps, alpha=alpha)
    result = extract_mbp_bilinear(
        lattice,
        links,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
        fermion_scheme=fermion_scheme,
        yt=yt,
        nc=nc,
        mass=mass,
        reg_epsilon=reg_epsilon,
        cutoff=cutoff,
        fd_step=fd_step,
        wilson_r=wilson_r,
    )
    row = {'amplitude': float(amplitude), **result.to_dict()}
    row['wilson_r'] = float(wilson_r)
    row['prefactor_exp_minus_2S'] = mbp_prefactor()
    row['mu2_with_prefactor'] = float(row['mu2_formula_proxy']) * float(row['prefactor_exp_minus_2S'])
    row['gamma_sign_match'] = _sign_match(float(row['gamma_h2_trace']), float(row['gamma_h2_fd']))
    row['recommendation_score'] = _score(float(row['gamma_consistency_gap']), bool(row['gamma_sign_match']), float(row['mu2_formula_proxy']))
    return row


def _best_row(rows: Sequence[dict[str, object]]) -> dict[str, object]:
    return min(rows, key=lambda row: (not bool(row['gamma_sign_match']), float(row['recommendation_score']), float(row['gamma_consistency_gap']), -abs(float(row['mu2_formula_proxy']))))


def run_stage26_pipeline(
    *,
    reference_stage25_summary: str | Path = 'outputs/su2_mbp_stage25_heavier_live_hybrid_example/stage25_summary.json',
    shape_grid: Sequence[tuple[int, int, int]] = DEFAULT_SHAPES,
    background: str = 'cooled_random',
    amplitudes: Sequence[float] = DEFAULT_AMPLITUDES,
    projector_mode: str = 'center',
    fermion_scheme: str = 'wilson4',
    fixed_chirality_mode: str = 'left',
    fixed_wilson_r: float = 0.5,
    adaptive_chirality_modes: Sequence[str] = DEFAULT_ADAPTIVE_CHIRALITIES,
    adaptive_wilson_r_grid: Sequence[float] = DEFAULT_ADAPTIVE_R_GRID,
    yt: float = 1.0,
    nc: float = 3.0,
    mass: float = 0.0,
    reg_epsilon: float = 1e-6,
    cutoff: float = 1e-8,
    fd_step: float = 1e-3,
    seed: int = 350437,
    cooling_steps: int = 10,
    alpha: float = 0.15,
) -> tuple[Stage26Summary, dict[str, object]]:
    payload25 = _load_payload(reference_stage25_summary)
    summary25 = payload25['summary']
    stage25_scheme = str(summary25['selected_scheme'])
    stage25_shape = tuple(int(v) for v in summary25['selected_shape'])

    shape_rows: list[Stage26ShapeRow] = []
    for shape in shape_grid:
        lattice = build_bcc_supercell(*shape)
        fixed_rows = [
            _run_single(
                lattice=lattice,
                background=background,
                amplitude=float(amplitude),
                chirality_mode=fixed_chirality_mode,
                fermion_scheme=fermion_scheme,
                wilson_r=fixed_wilson_r,
                yt=yt,
                nc=nc,
                mass=mass,
                reg_epsilon=reg_epsilon,
                cutoff=cutoff,
                fd_step=fd_step,
                projector_mode=projector_mode,
                seed=seed,
                cooling_steps=cooling_steps,
                alpha=alpha,
            )
            for amplitude in amplitudes
        ]
        fixed_best = _best_row(fixed_rows)

        adaptive_candidates: list[dict[str, object]] = []
        for chirality_mode in adaptive_chirality_modes:
            for current_r in adaptive_wilson_r_grid:
                rows = [
                    _run_single(
                        lattice=lattice,
                        background=background,
                        amplitude=float(amplitude),
                        chirality_mode=chirality_mode,
                        fermion_scheme=fermion_scheme,
                        wilson_r=float(current_r),
                        yt=yt,
                        nc=nc,
                        mass=mass,
                        reg_epsilon=reg_epsilon,
                        cutoff=cutoff,
                        fd_step=fd_step,
                        projector_mode=projector_mode,
                        seed=seed,
                        cooling_steps=cooling_steps,
                        alpha=alpha,
                    )
                    for amplitude in amplitudes
                ]
                adaptive_candidates.append(_best_row(rows))
        adaptive_best = _best_row(adaptive_candidates)

        fixed_score = float(fixed_best['recommendation_score'])
        adaptive_score = float(adaptive_best['recommendation_score'])
        use_fixed = fixed_score <= adaptive_score and bool(fixed_best['gamma_sign_match'])
        winner = fixed_best if use_fixed else adaptive_best
        winner_mode = 'fixed_recommended' if use_fixed else 'shape_adaptive_winner'

        shape_rows.append(
            Stage26ShapeRow(
                shape=shape,
                grid_extent=_shape_size(shape),
                fixed_chirality_mode=fixed_chirality_mode,
                fixed_wilson_r=float(fixed_wilson_r),
                fixed_best_amplitude=float(fixed_best['amplitude']),
                fixed_gap=float(fixed_best['gamma_consistency_gap']),
                fixed_sign_match=bool(fixed_best['gamma_sign_match']),
                fixed_mu2_formula_proxy=float(fixed_best['mu2_formula_proxy']),
                fixed_gamma_h2_trace=float(fixed_best['gamma_h2_trace']),
                fixed_gamma_h2_fd=float(fixed_best['gamma_h2_fd']),
                fixed_sigma_min=float(fixed_best['sigma_min']),
                fixed_sigma_next=float(fixed_best['sigma_next']),
                adaptive_chirality_mode=str(adaptive_best['chirality_mode']),
                adaptive_wilson_r=float(adaptive_best['wilson_r']),
                adaptive_best_amplitude=float(adaptive_best['amplitude']),
                adaptive_gap=float(adaptive_best['gamma_consistency_gap']),
                adaptive_sign_match=bool(adaptive_best['gamma_sign_match']),
                adaptive_mu2_formula_proxy=float(adaptive_best['mu2_formula_proxy']),
                adaptive_gamma_h2_trace=float(adaptive_best['gamma_h2_trace']),
                adaptive_gamma_h2_fd=float(adaptive_best['gamma_h2_fd']),
                adaptive_sigma_min=float(adaptive_best['sigma_min']),
                adaptive_sigma_next=float(adaptive_best['sigma_next']),
                winner_mode=winner_mode,
                winner_chirality_mode=str(winner['chirality_mode']),
                winner_wilson_r=float(winner['wilson_r']),
                winner_best_amplitude=float(winner['amplitude']),
                winner_gap=float(winner['gamma_consistency_gap']),
                winner_sign_match=bool(winner['gamma_sign_match']),
                winner_mu2_formula_proxy=float(winner['mu2_formula_proxy']),
                winner_gamma_h2_trace=float(winner['gamma_h2_trace']),
                winner_gamma_h2_fd=float(winner['gamma_h2_fd']),
                winner_sigma_min=float(winner['sigma_min']),
                winner_sigma_next=float(winner['sigma_next']),
                stage25_scheme_match=fermion_scheme == stage25_scheme,
                stage25_shape_match=shape == stage25_shape,
                improvement_over_fixed=max(0.0, fixed_score - adaptive_score),
                winner_score=float(winner['recommendation_score']),
            )
        )

    ordered = sorted(shape_rows, key=lambda row: (not row.winner_sign_match, row.winner_score, -abs(row.winner_mu2_formula_proxy), row.grid_extent))
    selected = ordered[0]
    summary = Stage26Summary(
        selected_shape=selected.shape,
        selected_source_label='stage26_shape_adaptive:selected_background',
        selected_scheme=fermion_scheme,
        selected_chirality_mode=selected.winner_chirality_mode,
        selected_wilson_r=selected.winner_wilson_r,
        selected_sign_match=selected.winner_sign_match,
        shape_rows=ordered,
        notes={
            'status': 'surrogate',
            'non_claim': 'not a full caloron or production-lattice computation',
            'fixed_recommendation': 'left, wilson_r=0.5',
        },
    )

    payload = {
        'summary': summary.to_dict(),
        'gates': {
            'G-STAGE26-RUN': True,
            'G-STAGE25-AVAILABLE': bool(summary25),
            'G-FIXED-LEFT-R05-RUN': all(row.fixed_wilson_r == 0.5 and row.fixed_chirality_mode == 'left' for row in ordered),
            'G-ADAPTIVE-LEDGER': len(ordered) == len(tuple(shape_grid)),
            'G-FIXED-SURVIVES-LARGER-SHAPE': any(row.grid_extent > _shape_size((4, 4, 4)) and row.fixed_sign_match for row in ordered),
            'G-ADAPTIVE-WINNER-DEFINED': all(row.winner_mode in {'fixed_recommended', 'shape_adaptive_winner'} for row in ordered),
            'G-ADAPTIVE-IMPROVES-AT-LEAST-ONE-SHAPE': any(row.improvement_over_fixed > 0.0 for row in ordered),
            'G-WILSON4-PRESERVED': all(row.stage25_scheme_match for row in ordered),
            'G-SELECTED-SIGN-CONSISTENT': bool(selected.winner_sign_match),
        },
    }
    return summary, payload
