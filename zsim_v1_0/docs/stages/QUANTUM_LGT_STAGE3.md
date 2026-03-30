# QUANTUM / LGT Stage 3 — Reduced MBP Extractor

This stage adds a reduced operator-level MBP extractor on top of the Stage 2 SU(2) engine.

## What is now implemented

- Construction of `K0`, `K1`, `K2` from a gauge-covariant hopping operator `D0` and a Yukawa projector `Y`.
- Prime-masked inverse `K0^{-1}` with spectral cutoff.
- Direct evaluation of the two MBP pieces
  - `Tr'(K0^{-1} K2)`
  - `1/2 Tr'(K0^{-1} K1 K0^{-1} K1)`
- Reduced proxy outputs
  - `mbp_bracket = diag - cross`
  - `mu2_formula_proxy = N_c * mbp_bracket`
  - `gamma_h2_trace = -(N_c/2) * mbp_bracket`
- Centered finite-difference cross-check of the `h^2` coefficient of `Gamma_f(h)`

## What this is not

- Not a production-scale caloron computation.
- Not a full continuum-equivalent SU(2) lattice extraction.
- Not yet a physics claim for the sign/magnitude of the full MBP.

## New app

```bash
python -m zsim.apps.su2_mbp_extract --background collective --projector-mode center
```

Outputs:

- `mbp_extract_scan.csv`
- `mbp_extract_summary.json`

## Intended use

This stage is a bridge between the reduced SU(2) engine and the future multi-cell MBP verification code.
The main engineering goal is consistency: the trace formula and finite-difference estimate of the `h^2` coefficient should agree on the same reduced background.
