@echo off
echo ============================================
echo  Z-Sim v3.0 Windows Setup
echo ============================================
echo.

REM Step 1: Install dependencies
echo [1/3] Installing dependencies...
pip install -r requirements.txt
pip install pytest
echo.

REM Step 2: Install zsim as editable package
echo [2/3] Installing zsim package...
pip install -e .
echo.

REM Step 3: Verify
echo [3/3] Verifying installation...
python -m pytest tests/ -q
echo.

echo ============================================
echo  Setup complete!
echo ============================================
echo.
echo  Try these commands:
echo.
echo    python -m zsim.apps.run_background --config configs/quickstart.yaml --output-dir outputs/test --no-plots
echo    python -m zsim.apps.run_inflation
echo    python -m pytest tests/ -q
echo.
pause
