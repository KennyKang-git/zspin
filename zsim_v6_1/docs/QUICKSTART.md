# Z-Sim Quickstart

## 1. Install

From the repository root:

```bash
python -m pip install -r requirements.txt
```

## 2. Fast background run

```bash
python scripts/quickstart.py background
```

Outputs are written to `outputs/quickstart_background/`.

## 3. Baseline comparison

```bash
python scripts/quickstart.py compare
```

Outputs are written to `outputs/quickstart_compare/`.

## 4. Small scan

```bash
python scripts/quickstart.py scan
```

Outputs are written to `outputs/quickstart_scan/`.

## 5. Direct CLI equivalents

```bash
python -m zsim.apps.run_background --config configs/quickstart.yaml --output-dir outputs/quickstart_background --no-plots
python -m zsim.apps.compare_baselines --config configs/quickstart.yaml --output-dir outputs/quickstart_compare --no-plots
python -m zsim.apps.run_scan --config configs/quickstart.yaml --output-dir outputs/quickstart_scan --vary gamma_xz gamma_zy --factors 0.0,1.0 --no-plots
```

## 6. Test suite

```bash
pytest -q
```


## Generate a report

```bash
python scripts/quickstart.py report
```


Stage 20 note: result-writing and CLI formatting were refactored into shared helpers, so the output layout is now more consistent across `background`, `compare`, `scan`, and `report`.


Index report example:
```bash
python -m zsim.apps.report_results --source-dir outputs --output-dir outputs/report_index --index
```


## Closure matrix

```bash
python scripts/quickstart.py closure-matrix
```
