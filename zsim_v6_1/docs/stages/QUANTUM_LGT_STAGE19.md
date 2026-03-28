# Quantum/LGT Stage 19 - Recompute-Aware Control Sweep

Stage 19 turns the Stage-18 hybrid winner into a recompute-aware control-family sweep.

## What was added
- `zsim.lgt.stage19`
- `zsim.apps.su2_mbp_stage19_recompute_control_validate`
- `tests/test_lgt_stage19.py`
- `tests/test_lgt_stage19_app.py`

## Purpose
Provide a direct ledger that compares:
- the Stage-18 hybrid selected row
- the Stage-17 stress-selected row
- the Stage-16 live default/lightweight/snapshot references
- a synthetic recompute-aware selected row
- a sharpened control family bundle

This remains a **preproduction surrogate**.
