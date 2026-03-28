# Quantum/LGT Stage 18 — Hybrid Live–Stress Bridge

Stage 18 reconnects the Stage-17 stress winner to the Stage-16 live recompute rows in one direct hybrid ledger.

## What was added
- `zsim.lgt.stage18`
- `zsim.apps.su2_mbp_stage18_hybrid_live_stress_validate`
- `tests/test_lgt_stage18.py`
- `tests/test_lgt_stage18_app.py`

## Purpose
Provide a hybrid ledger that compares:
- Stage-17 stress-selected background
- Stage-16 live default selected/control
- Stage-16 lightweight selected
- Stage-16 snapshot reference
- a synthetic hybrid-selected and hybrid-control row

This remains a **preproduction surrogate**.
