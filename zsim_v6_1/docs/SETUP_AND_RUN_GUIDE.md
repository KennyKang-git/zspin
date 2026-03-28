# Z-Sim v6.1 — Setup & Run Guide (한국어)

## 1. 설치 (Setup)

### 최소 요구사항
- **Python 3.10 이상** (3.11–3.12 권장)
- pip (Python 패키지 관리자)
- Git (선택 — GitHub 사용 시)

### Step 1: 압축 해제

```bash
unzip zsim_v6_1.zip
cd zsim_v6_1
```

폴더 구조:
```
zsim_v6_1/
├── configs/            ← 설정 파일 (YAML)
│   ├── base.yaml           기본 설정 (HYPOTHESIS 클로저)
│   ├── derived.yaml        이론 유도 설정 (DERIVED 클로저)
│   └── quickstart.yaml     빠른 테스트용 (짧은 구간)
├── zsim/               ← 핵심 소스 코드
│   ├── core/               상수 (A=35/437), 설정, 상태 벡터
│   ├── kernel/             물리 커널 (Friedmann, inflation, mediation)
│   ├── solver/             ODE 적분기 (segmented RK45)
│   ├── observables/        관측량 계산 (n_s, r, H₀, Ω_m)
│   ├── validation/         Kill-switches (구조 검증)
│   ├── io/                 입출력, 리포트, 플롯
│   ├── apps/               CLI 실행 앱들 (41개)
│   ├── quantum/            다면체 스펙트럼, Hodge, Dirac
│   ├── lgt/                축소 SU(2) 격자 (Stage 4–26, surrogate)
│   └── lgt2/               프로덕션 LGT (9개 모듈, v6.0+)
├── cobaya_f32/         ← Cobaya Gate F32-12 전용 (face counting)
├── cobaya_scaffold/    ← Cobaya 스캐폴드 템플릿
├── scripts/            ← 유틸리티 (quickstart, HPC scan, caloron scan)
├── tests/              ← 테스트 (76개 파일, 348개 테스트 항목)
├── docs/               ← 문서 (Stage 노트, 가이드, 매뉴얼)
├── outputs/            ← 시뮬레이션 결과 (자동 생성)
├── requirements.txt
├── requirements-dev.txt
└── pyproject.toml
```

### Step 2: 의존성 설치

```bash
# 기본 의존성 (4개)
pip install -r requirements.txt

# 개발용 (테스트 포함)
pip install -r requirements-dev.txt
```

설치되는 패키지:
| 패키지 | 용도 |
|--------|------|
| numpy ≥ 1.26 | 배열 연산, 선형대수 |
| scipy ≥ 1.12 | ODE 적분 (RK45), 최적화 |
| pyyaml ≥ 6.0 | 설정 파일 파싱 |
| matplotlib ≥ 3.8 | 플롯 생성 |
| pytest | 테스트 (개발용) |

### Step 3: 설치 검증

```bash
# 테스트 실행 — 322/348 PASS 확인 (26개 stage-fixture 테스트는 사전 출력 필요)
python -m pytest -q

# 빠른 동작 확인
python scripts/quickstart.py background
```

`322 passed` + `outputs/` 에 CSV 파일이 생성되면 설치 완료!

---

## 2. 실행 방법

Z-Sim v6.1에는 **9가지 실행 모드**가 있습니다.

### 모드 A: 배경 우주 진화 (Background Evolution)

**무엇을 하나?** X/Z/Y 3섹터 에너지 밀도의 시간 진화를 계산합니다.

```bash
# 빠른 테스트 (0.2 e-fold)
python -m zsim.apps.run_background \
    --config configs/quickstart.yaml \
    --output-dir outputs/quick_bg

# 이론 유도 클로저로 풀 진화 (38 e-folds)
python -m zsim.apps.run_background \
    --config configs/derived.yaml \
    --output-dir outputs/derived_bg

# 플롯 끄기 (서버/CI용)
python -m zsim.apps.run_background \
    --config configs/derived.yaml \
    --output-dir outputs/derived_bg --no-plots
```

**출력 파일:**
| 파일 | 내용 |
|------|------|
| `run_state.csv` | 매 스텝의 전체 상태 벡터 (N, a, h, ε, ρ_x, ρ_z, ρ_y, ...) |
| `run_observables.csv` | 관측량 (w_eff, H, 엔트로피, 매개효율, ...) |
| `run_diagnostics.json` | Kill-switch 결과, 이벤트 로그 |
| `run_metadata.json` | 설정, 버전, 타임스탬프 |

### 모드 B: 베이스라인 비교 (Baseline Comparison)

```bash
python -m zsim.apps.compare_baselines \
    --config configs/derived.yaml \
    --output-dir outputs/compare --N-end 5.0
```

### 모드 C: 파라미터 스캔 (Parameter Scan)

```bash
python -m zsim.apps.run_scan \
    --config configs/derived.yaml \
    --output-dir outputs/scan \
    --vary gamma_xz gamma_zy --factors "0.5,1.0,2.0"
```

### 모드 D: 클로저 매트릭스 (Closure Matrix)

```bash
python -m zsim.apps.run_closure_matrix \
    --config configs/derived.yaml \
    --output-dir outputs/closure \
    --phase-source-modes "full_state,currents_only" \
    --mediation-modes "raw_contrast" \
    --epsilon-source-modes "zero" \
    --h-closure-modes "sqrt_sum" --no-plots
```

### 모드 E: 인플레이션 관측량 (Inflation Observables)

```bash
python -m zsim.apps.run_inflation
```

**출력 (터미널):**
```
   N*        n_s            r
-----------------------------------------------------------------
   50   0.962757     0.012791
   55   0.967611     0.010679
   60   0.967400     0.008900     ← Z-Spin 예측
   65   0.964675     0.007771
```

### 모드 F: 리포트 생성 (Report)

```bash
python -m zsim.apps.report_results \
    --source-dir outputs/derived_bg \
    --output-dir outputs/derived_bg/report

# 전체 출력 인덱스 리포트
python -m zsim.apps.report_results \
    --source-dir outputs --output-dir outputs/report_index --index
```

### 모드 G: Cobaya CMB 검증 (Gate F32-12)

⚠️ Cobaya + CAMB + Planck likelihood 별도 설치 필요

```bash
# 로컬 스모크 테스트
cobaya-run cobaya_f32/zspin_local_test.yaml

# Face counting 38/121 테스트
cobaya-run cobaya_f32/zspin_38_121_test.yaml

# 풀 Planck MCMC (프로덕션)
cobaya-run cobaya_f32/zspin_mcmc_planck.yaml --packages-path ~/packages
```

현재 최고 결과: **Δχ² = 3.9** (face counting, plik_lite)

### 모드 H: 프로덕션 LGT MBP v2 파이프라인

```bash
# Python에서 직접 실행 (CLI 래퍼 없음)
python -c "
from zsim.lgt2.mbp2 import run_mbp2_pipeline
result = run_mbp2_pipeline(shape=(4,4,4), flow_steps=50, flow_epsilon=0.01)
print(f'sign_match: {result.gamma_sign_match}')
print(f'consistency_gap: {result.gamma_consistency_gap:.6e}')
print(f'STATUS: {result.status}')
"
```

상세 LGT2 사용법은 `docs/LGT2_PRODUCTION_GUIDE.md` 참조.

### 모드 I: Quickstart (원커맨드)

```bash
python scripts/quickstart.py background   # 배경 진화
python scripts/quickstart.py compare      # 베이스라인 비교
python scripts/quickstart.py scan         # 파라미터 스캔
python scripts/quickstart.py report       # 리포트 생성
```

모두 `configs/derived.yaml` (DERIVED 클로저) 사용.

---

## 3. Python API로 직접 사용하기

### 기본 시뮬레이션 실행

```python
from zsim.core.config import ZSimConfig
from zsim.solver.integrator import integrate

cfg = ZSimConfig.from_yaml("configs/derived.yaml")
result = integrate(cfg)

print(f"성공: {result.success}")
print(f"스텝 수: {result.step_count}")
print(f"최종 N: {result.states[-1].N}")
```

### 물리 상수 접근 (v6.1 face counting)

```python
from zsim.core.constants import (
    A_LOCKED,          # 35/437 = 0.08009153318...
    G_EFF_RATIO,       # 437/472 = 0.925847...
    H0_RATIO,          # exp(A) = 1.08339...
    OMEGA_M_BARE,      # 38/121 = 0.3140 [v6.1 face counting]
    OMEGA_M_EFF,       # 38/(121(1+A)) = 0.2908
    OMEGA_CDM_FACE,    # 32/121 = 0.2645 [OBSERVATION]
    OMEGA_B_FACE,      # 6/121  = 0.0496
    R_TENSOR,          # 0.0089
    LAMBDA_POTENTIAL,   # 1.79
    ETA_B,             # (6/11)^35
)

print(f"A = 35/437 = {A_LOCKED:.12f}")
print(f"H₀_local/H₀_CMB = {H0_RATIO:.6f}")
print(f"Ω_m (bare, face) = {OMEGA_M_BARE:.6f}")
print(f"Ω_m (eff) = {OMEGA_M_EFF:.6f}")
print(f"Ω_cdm (face) = {OMEGA_CDM_FACE:.6f}")
```

### Friedmann 방정식 직접 사용

```python
from zsim.kernel.friedmann import F_epsilon, G_eff_over_G, friedmann_h_squared
from zsim.core.config import ZSimConfig
from zsim.core.state import ZSimState

cfg = ZSimConfig.from_yaml("configs/derived.yaml")
state = ZSimState(
    N=0, a=1, h=1, epsilon=1.0, pi_epsilon=0,
    rho_x=0.3, rho_z=0.02, rho_y=0.68,
    J_xz=0, J_zy=0, phi_z=0, sigma_struct=0,
)

print(f"F(ε=1) = 1+A = {F_epsilon(1.0):.10f}")
print(f"G_eff/G = {G_eff_over_G(1.0):.10f}")
```

### 인플레이션 관측량 계산

```python
from zsim.kernel.inflation_canonical import compute_full_inflation

results = compute_full_inflation(N_star_values=[50, 55, 60, 65])
for r in results:
    print(f"N*={r['N_star']}: n_s={r['n_s']:.4f}, r={r['r']:.6f}")
```

---

## 4. 설정 파일 설명

| 설정 | 용도 | 클로저 상태 | 진화 구간 |
|------|------|------------|----------|
| `quickstart.yaml` | 빠른 테스트 | HYPOTHESIS | N: −18 → −17.8 (0.2) |
| `base.yaml` | 기본 탐색 | HYPOTHESIS | N: −18 → −17.8 (0.2) |
| `derived.yaml` | **이론 검증** | **DERIVED** (7/8 유도) | N: −18 → 20 (38) |

### derived.yaml 핵심 파라미터

| 파라미터 | 값 | 출처 |
|----------|-----|------|
| γ_xz | 2A/Q = 0.01456 | ZS-Q7 §5.1 Fermi 규칙 |
| γ_zy | 6A/Q = 0.04369 | ZS-Q7 §5.1 Fermi 규칙 |
| α_xz | X/Z = 3/2 | 상세 균형 정리 |
| α_zy | Z/Y = 1/3 | 상세 균형 정리 |
| ρ_x0, ρ_z0, ρ_y0 | 3/11, 2/11, 6/11 | 등분할 평형 |
| phase_mode | spinor_sin2 | SU(2) j=1/2 |

---

## 5. v6.1 핵심 변경사항 (v6.0 대비)

### Face Counting Ω_m 동기화

v6.0에서 CDM은 이미 face counting (32/121)을 사용했지만, 총 물질 밀도는 slot counting (39/121)을 사용하는 불일치가 있었습니다. v6.1에서 모든 물질 밀도를 face counting으로 통일했습니다.

| 파라미터 | v6.0 (slot) | v6.1 (face) |
|---|---|---|
| Ω_m bare | 39/121 = 0.3223 | 38/121 = 0.3140 |
| Ω_m eff | 0.2984 | 0.2908 |
| S₈ | ~0.794 | ~0.777 |
| S₈ vs DES Y3 | +1.06σ | **+0.06σ** |

### Face Counting 물질 예산

| 섹터 | 공식 | 값 |
|------|------|-----|
| 바리온 | F(정육면체)/Q² | 6/121 |
| 암흑물질 | F(깎인 정이십면체)/Q² | 32/121 |
| 암흑에너지 | 1 − 38/121 | 83/121 |
| 총 물질 | (6+32)/121 | 38/121 |

상태: CDM 32/121은 **OBSERVATION** (이론 유도 대기 중 — ZS-F2 깎인 정이십면체 매개 필요).

---

## 6. 자주 하는 질문

**Q: 실행이 안 돼요 / ModuleNotFoundError**
```bash
# zsim_v6_1 폴더 안에서 실행해야 합니다
cd zsim_v6_1
python -m zsim.apps.run_background --config configs/derived.yaml --output-dir outputs/test
```

**Q: 테스트가 26개 실패해요**
A: 정상입니다. Stage 14–26 테스트는 이전 stage 출력 파일에 의존합니다. 개발 환경에서 순차적으로 stage를 실행하면 모두 PASS합니다. 핵심 cosmology + LGT2 테스트(322개)는 clean install에서 바로 PASS합니다.

**Q: A = 35/437인데 맞나요?**
A: 정확합니다. `A = 35/437 = 0.08009153318...`의 IEEE 754 표현입니다. 이 값은 locked constant로 변경 불가합니다.

**Q: GPU가 필요한가요?**
A: 아닙니다. CPU만으로 충분합니다. 풀 진화가 ~10초, LGT2 MBP (4×4×4)가 ~30초 내 완료됩니다.

**Q: Cobaya 실행에 뭐가 더 필요한가요?**
A: Cobaya + CAMB + Planck likelihood 패키지가 별도 필요합니다. Ubuntu WSL 환경 권장. `cobaya_f32/README_F32_12.md` 참조.

**Q: v = 246 GeV가 유도되었나요?**
A: **아닙니다 (NON-CLAIM)**. MBP 프로덕션 격자 계산(N≥8, Wilson gradient flow)이 완료되어야 합니다. 현재 소규모 격자(2³–4³)에서 부호 일치 및 consistency gap 수렴은 확인되었습니다.
