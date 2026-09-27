# ZS-M67 — Boundary symmetry obstructions and conditional selector bounds for a chiral-bag surface mode

### The `θ̄`-funnel, the chiral-bag surface mode, the action-derived operator-state lift, why a faithful biased boundary state must break the boundary's own boost symmetry, and what survives of the selector question under the stated spectral and diagonal-mean-field classes

> **Title changed in v3.3** (v3.2 audit, S2). The former title *"Classical selector exhaustion, a bare quantum no-go, and the boundary symmetry obstruction"* read as a total exhaustion; the paper's exclusions are exact only inside the spectral (A1–A5), free-bulk (A4), colour/charge-diagonal contact and linear-Goldstone classes, and K7, K8, K9b, the local-`α(x)` Jacobian, A5 and the environment construction remain open. History rows citing the former title refer to this paper.

**PAPER CODE / VERSION / DATE:** ZS-M67 / **v3.4.1** / 2026-09-04 KST (Ref_202609040800; correction-only; v3.4 was Ref_202609040640, v3.3 Ref_202609040058)
**OUTPUT ROLE:** SUPPORT (external mathematics) + RQ1/RQ3 selection-backbone **no-go map with a computed admission registry**: the chain is exhibited end to end, killed at its coefficient (Thm 36), the corpus Goldstone is classified by charge type (Thm 38: linear bulk couplings closed exactly; a flip-odd gradient class survives conditionally on `f = M_P`), and multi-band is repaired to a per-band bound (Thm 39). `F-M66.17` is **partially CLOSED-NEGATIVE** — exact on some routes, conditional on others, OPEN at the registered survivors. **The v2.9 "corpus-wide" closure and TERMINAL-IN-SCOPE are WITHDRAWN** after audit. Selector signature Definition 40 and an **RQ2→RQ3 handoff** ([가설]: a rest-frame datum as one input of the selector) are supplied; the RQ1 selection backbone is the frame in which the residual freedom is counted. v3.1 closed the constant-axial-rotation Jacobian inside A1–A4 (Thms 38.3–38.4), bounded the seam rest frame (Thm 41: `T/Δ ≤ 0.4147`) and counted the A5 residue (two reals). v3.2 integrated the v3.1 audit: Thm 39.4 re-quantified (K9a closed by gauge invariance; K9b, same-representation generation-flavour coherence, not), Cor. 41.2 as a necessary condition, Thm 38.3 narrowed. **v3.3 integrates the v3.2 audit in full:** the K9b *quantitative* conclusion of v3.2 — "unchanged bound", "`n_c/n_t ≈ 2×10⁷` needed", conditional rejection — is **withdrawn** (a single-band bound was transferred to a coherent two-band carrier without the theorem that would carry it; the audit's counterexample family reaches the target at `n_c/n_t ≈ 7×10⁵` with the charm diagonal kept, W16); **K9b is OPEN**, with the missing coherent-carrier theorem named (Proof obligation 39.8); Elitzur's scope, the sign of `κ`, A1–A6, the handoff label, the novelty class of Prop. 39.6 and the title are corrected; the package is self-contained (baseline embedded) and the guards are given sentence-level claim-state rules. **v3.4 integrates the v3.3 audit in full** (`AUDIT-MAJOR-REVISION`; central contribution SURVIVES; three S2, release-blocking): the §25 sentence that read the missing object as *constructed* is replaced by its **signature** statement (no CPTP map or state-selection mechanism is constructed here); the thermal ceiling is typed **target-independent** and the number `0.4147` **target-conditioned**, and Theorem 36's general functional form is separated from its `(T₂, θ̄_*)`-conditioned `×42` verdict; the release core is made to agree with the generated manifest (core = manuscript · verifier · ledger · release manifest; the session file is a provenance object; guard G25); Elitzur's theorem carries its citation and its boundary hypotheses; the empty-ledger exit is fail-closed. **Separately from the correction pass, §22.11 attacks Proof obligation 39.8 at linear order**: the record is a density-weighted mean of the diagonal blocks (Lemma 39.9), the coherent channel's normal overlap is the harmonic mean of the two localisation rates with ratio `ω = 2√(m₁m₂)/(m₁+m₂) ≤ 1` (Lemma 39.10), and about any flavour-diagonal reference the linearised coherent channel closes on itself by flavour number, so the flavour matrix `D` never enters its onset (Theorem 39.11) — C99d is CLOSED-NEGATIVE at linear order, C99e is reduced to one computation (Proof obligation 39.8′), **K9b stays OPEN**. **v3.4.1 (correction-only) integrates the v3.4 audit in full**: its one substantive finding — Proof obligation 39.8′ used `G₄` in two incompatible senses (Lemma 36.1's band-specific `G₄ = y²/4m_h²` and a flavour-blind strength multiplied by `y₁y₂`), so a successor computation would have started from a wrong normalisation — is repaired by naming the channel strengths `G₄^{(ij)} = y_iy_j/4m_h²`; no certificate changes
**RELEASE LABEL:** MANUSCRIPT DRAFT — **FREEZE-CANDIDATE PROPOSED** (the v3.4 audit, L3, re-examined the v3.4 repairs, §22.11 and G25 and recommends: after this minimal correction, freeze M67 and move to the positive-construction line; the freeze is a user decision, not granted here; K9b is accepted as an OPEN survivor of the no-go map, not discharged)
**Rules:** ZSPIN-RULES-2.1, kernel PACKAGE-MINOR 2.2 · dominant role MANUSCRIPT · auxiliary role VERIFY
**Mission:** LOADED (ZSPIN-MISSION v1.4) · **Kernel:** LOADED (v2.2)
**Verification artifacts:** `zs_m67_verify_v2_1.py` (82 rows, §4–12) **+** `zs_m67_verify_v2_4.py` (48 rows, §13–17) **+** `zs_m67_verify_v2_5.py` (22 rows, §18) **+** `zs_m67_verify_v2_6.py` (21 rows, §19) **+** `zs_m67_verify_v2_7.py` (18 rows, §20) **+** `zs_m67_verify_v2_8.py` (17 rows, §21) **+** artifact M = `zs_m67_verify_v3_4_1.py` (57 rows; §22 incl. §22.11; paper v3.4.1 ↔ script v3_4_1; **supersedes** `zs_m67_verify_v3_4.py` (56 rows), `v3_3`, `v3_2`, `v3_1`, `v3_0` and `v2_9`; the artifact-L baseline is **embedded** in the script, so the core files reproduce the ledger alone; `release_manifest_v3_4_1.json` is generated at run time and is the fourth core object)

> **One-line scope verdict.** No classical, spectral, free-bulk, contact-interaction, diagonal
> multi-band or linear-Goldstone structure available in the Z-Spin corpus selects the chiral-bag angle:
> the boundary polarisation of every mode is `m sin θ̄/E`, the derivative-free boundary-term class
> collapses on shell to `J_E` giving a gap equation `|cos θ̄| = g_c/|g|`, the upstream Yukawa sector
> supplies the coupling but misses the per-band admission bound `G₄m² ≥ πκ/(2c′ sin θ̄(1−κ))` by ×42 on
> every band, and the corpus Goldstone either drives the angle to the excluded minimum `π` (Horn A) or,
> on Horn B, couples linearly only through currents whose boundary effect is exactly zero or exactly a
> rotation that fixes the record. What survives, with signatures: a boundary-localised Goldstone
> gradient class (flip-odd on the carrier; dead only if `f = M_P`), a **same-gauge-representation
> generation-flavour-coherent** boundary condensate (K9b; gauge-invariant, so not excluded by Elitzur;
> **OPEN — no admission criterion exists for a coherent two-band carrier**, Proof obligation 39.8), and
> a corpus-external strongly coupled sector. `F-M66.17` is partially CLOSED-NEGATIVE; the v2.9
> corpus-wide closure is withdrawn. v3.1–v3.4: the Horn-B closure is exact at the level of the
> `H²`-regularised spectral supertrace and of constant axial co-rotation inside A1–A4 (local `α(x)`
> with fixed bag domain: open obligation); colour- and charge-changing off-diagonal condensates are
> gauge-variant (closed, K9a); the thermal ceiling `|κ| ≤ tanh(Δ/2T)` is target-independent and, conditioned
> on the target `|κ| = T₂`, gives the capacity bound `T/Δ ≤ 0.4147` — one necessary condition on
> `D-S14-EVENT-001`, not its discharge; the A5 residue is exactly two real numbers; at linear order the
> flavour-coherent channel of K9b closes on itself and its onset does not involve the flavour matrix `D`
> (Thm 39.11), so what remains of K9b is one response computation (Proof obligation 39.8′). Everything exact here is exact **inside the stated spectral,
> free-bulk, colour/charge-diagonal contact and linear-Goldstone classes**; nothing here is a selection.
---

## 0. 한국어 요약

> **구조 변경(v3.3; v3.4 유지).** 이전 판본들의 한국어 요약, v3.0 status map, 옛 non-claim·§26의 superseded
> 항목·§29의 v3.1 이전 정정 기록은 **provenance supplement**(`ZS-M67_v3_4_provenance_supplement.md`; v3.3 supplement에 v3.4 note를
> 덧붙인 것)로 이동했다. 본문에는 현재 유효한 과학 내용과 직전 판본들의 정정만 남긴다(논문작성 규칙 §7.1).

### 0.0 v3.4.1 (correction-only) — v3.4 감사의 통합: 증명 의무 39.8′의 `G₄` 정의 충돌 수리, 동결 제안

v3.4 감사(L3 다른 모델 계열)는 v3.4를 "양화사·물리 bridge·survivor typing·target conditioning·오류 계보 관리가 안정화된 논문"으로,
§22.11을 "실질적 진전(`order parameter ≠ response kernel`)"으로 판정하면서 **실질 결함 1건**을 찾았다: 증명 의무 39.8′가 `G₄`를 두 가지
의미로 썼다. Lemma 36.1의 `G₄ = m²/(2v²m_h²) = y²/(4m_h²)`는 해당 밴드의 Yukawa를 **이미 포함**하는데, v3.4의 정리 39.11 onset
`1 = G₄·y₁y₂·overlap·𝒦`는 Yukawa를 두 번 세었고, 의무 (c) "`1/(G₄y_ty_c…𝒦)`를 코퍼스 `G₄`와 비교"는 양변에 `G₄`가 있는 잘못된 식이었다.
다음 연구가 이 정규화로 시작하면 틀리므로 동결 전 수리가 필요하다는 판정. **전건 수용, 0건 기각.** 수리(표기 정정만; C101의 적분, C102의
kernel, V34의 비율은 불변): flavour-blind Higgs 접촉 세기 `Ĝ₄ := 1/(4m_h²)`, 채널 세기 `G₄^{(ij)} := y_iy_jĜ₄ = m_im_j/(2v²m_h²)`
(Lemma 36.1의 `G₄`는 `G₄^{(ii)}`; `G₄^{(12)} = √(G₄^{(11)}G₄^{(22)})`). 정리 39.11: `1 = G₄^{(12)}·[2κ₁κ₂/(κ₁+κ₂)]·𝒦₁₂`. 의무 (c):
무차원 admission 비 `A_tc := G₄^{(tc)}·[2κ_tκ_c/(κ_t+κ_c)]·𝒦_tc^max`를 코퍼스 값 `G₄^{(tc)} = m_tm_c/(2v²m_h²) = 1.150×10⁻⁷ GeV⁻²`
(`G₄^{(t)} = 1.557×10⁻⁵ GeV⁻²`, 비 `y_c/y_t`; V34)에서 평가, 코히어런트 onset은 `A_tc ≥ 1`을 요구. CLAIM-STATE `G4-channel=YUKAWA-INSIDE`.

**감사의 최종 권고를 제안으로 수용한다.** "v3.4 그대로 종결: NO / v3.4.1 최소 수정 → M67 동결 → positive construction 라인 진행: YES" —
M67이 실패해서가 아니라 자기 역할(**no-go map + missing-object extraction**)을 거의 완수했기 때문에 넘어간다는 감사의 framing을 기록한다.
따라서 **FREEZE-CANDIDATE = PROPOSED**(동결 자체는 사용자 승인 사항; 이 판본이 부여하지 않음). M67 안에서의 추가 깊은 연구(39.8′의
응답 계산, Cor. 38.7)는 **투입하지 않고** 후속 라인으로 이관한다(후속 식별자는 규칙에 따라 예약하지 않음). 아티팩트 M(57행) = L의 전 행 이월·재타이핑 + D42.

### 0.1 v3.4 신규분 — v3.3 감사의 전면 통합 (physical bridge · target-conditioning · release core) + §22.11 (증명 의무 39.8의 선형 차수 공략) — v3.4.1에서 (7)의 onset 정규화 정정됨

v3.4는 v3.3 감사(`AUDIT-MAJOR-REVISION`; 중심 기여 SURVIVES; 최고 심각도 S2 3건; release-blocking; 독립성 L3 다른 모델 계열 + L5
결정론적 재실행 48/48 byte-identical·고장 주입 4종 재현)를 **전건 수용, 0건 기각**했다. §4–21·§22.1–22.10의 수학은 불변이다.

**(1) §25 physical-bridge 과장문(S2).** v2.6 시기의 문장 "the remaining object is completely specified — an action-derived, non-unital,
flip/boost-symmetry-breaking CPTP map with a unique faithful stationary state … all now derived"는 누락 객체가 **구성되었다**고 읽힌다.
감사 대체문으로 교체했다: 특정된 것은 누락 객체의 **signature**이며, 그런 CPTP map이나 state-selection mechanism은 M67에서 **구성되지 않았다**
(유도된 것은 carrier·grading·boundary lift·허용 state/operation family뿐). `specification ≠ construction`. 가드 G20(iv)가 §25의
'completely specified' 문장에 부정/‘signature’ 표지를 요구하고 옛 문구의 재주입을 FAIL시킨다(CLAIM-STATE `MissingObject=SPECIFIED-NOT-CONSTRUCTED`).

**(2) target-independent와 target-conditioned의 혼동(S2).** 정리 41의 ceiling `|κ| ≤ tanh(Δ/2T)`는 target-independent이나, `|κ| = T₂`를
넣어 얻는 `T/Δ ≤ 0.4147`은 Z-Spin 표적에 **조건화된 필요 capacity bound**다. Cor. 41.3(ii)의 "first target-blind constraint" 문구는
**WITHDRAWN**. 정리 36도 같게 분리했다: 함수형 `G₄m² ≥ πκ/(2c′ sin θ̄(1−κ))`는 일반, `(T₂, θ̄_*)`를 대입한 ×42 판정은 target-conditioned.
이 정정은 부정 결과를 약화하지 않고 selection theorem으로의 오독만 차단한다(V32 재타이핑; CLAIM-STATE 토큰 2개).

**(3) release core와 manifest의 객체 그래프 불일치(S2).** 원고는 session을 포함한 4파일 core를 선언했으나 생성 manifest의 core는 3객체였다.
v3.4: **authoritative core = manuscript · verifier · ledger · release manifest**(VERIFY §9.1), session·감사 보고서·provenance supplement는
**provenance object**로 manifest에 측정 해시와 함께 등록. 신설 **G25**가 §27의 선언 core와 manifest core를 대조한다(live-fire: session을 core에
넣으면 FAIL).

**(4) Elitzur.** 원논문 인용(S. Elitzur, Phys. Rev. D **12**, 3978 (1975); DOI 확인)과 두 경계 가정 — (H1) 양의 게이지 불변 measure,
(H2) 경계조건과 measure가 국소 colour/electromagnetic 게이지 대칭을 보존하며 boundary gauge reduction·dressed 비국소 order parameter를
쓰지 않음 — 을 정리 39.4에 직접 넣었다(C96). **(5) G21.** `exit_code([]) = 0`은 fail-closed가 아니었다 → 빈 원장은 **exit 2**.

**(6) 감사 밖 자체 발견(S3).** W15의 claim 문자열에 실행 의존 잔차(`1.6e-16` vs 배송본 `1.7e-16`)가 박혀 있어 다른 기계에서 fingerprint가
바뀌고 G18의 carried 계수가 27→26으로 조용히 움직였다(VERIFY N4·§9.2). W15를 threshold 형식으로 재타이핑하고 측정값은 detail로 옮겼다.

**(7) §22.11 — 증명 의무 39.8의 선형 차수 공략(연구 추가분; 정정 pass와 분리; 논문작성 §16에 따라 major revision).** 감사는 correction-only
판본에 coherent many-body 정리를 억지로 넣지 말라고 권고했고, 그 권고를 지킨다: 새 many-body 정리를 주장하지 않으며 **K9b는 OPEN**이다.
확정된 것은 정확 대수 세 건이다. **Lemma 39.9(C100)** — 기록 연산자 `J_E⊗1`은 flavour-blind이므로 `κ = (n₁κ₁+n₂κ₂)/(n₁+n₂)`; `G₁₂`는 기록에
직접 기여하지 않는다(감사 반례족의 기록은 모든 `r`에서 정확히 `κ`). **Lemma 39.10(C101)** — coherent 채널의 법선 overlap은 두 localisation
rate의 **조화평균** `2κ₁κ₂/(κ₁+κ₂)`, 기하평균 대비 `ω = 2√(m₁m₂)/(m₁+m₂) ≤ 1`(`ω_tc = 0.1707`, `(y_c/y_t)ω_tc = 1.26×10⁻³`, V34).
**Theorem 39.11(C102)** — 임의의 flavour-대각 기준 상태에서 d-채널 Wick kernel은 `δ_jk δ_il`-support(16개 중 4개): coherent (tc) 채널은
선형 차수에서 **자기 자신에게 닫히고**, Prop. 39.6의 `D`(order parameter의 Fock 상)는 onset에 등장하지 않는다. ⇒ **C99d CLOSED-NEGATIVE
(선형 차수)**; **C99e는 OPEN**이되 단일 계산 **증명 의무 39.8′**(대각 상태의 interband 응답 `K_tc`, 고정 기록 `|κ| = T₂` 하 Pauli 극값, `G₄` 비교)로
축소. 선행연구 sweep(D41): Blasone–Jizba–Mavromatos–Smaldone(arXiv:1807.07616, 원문 PDF)은 flavour off-diagonal 응축을 mixing 생성의
signature로 확립 — K9b의 **객체는 IMPORTED**, Prop. 39.6 대수는 **SPECIALIZED**, 경계 carrier 판본은 NOT_FOUND → OPEN-NOVELTY(축소).

**Z-Spin에 대한 귀결.** `RQ3` bridge `OPEN → OPEN`. **SUPPORT 유지, CORE 승격 없음, SSOT 변경 없음. FREEZE-CANDIDATE 보류 유지**(targeted delta
재감사 전제). A4/A5의 v2.3 원문은 repo 1·2 검색에서 NOT_FOUND(검색족 기록; ABSENT 아님). 후속 식별자 미부여.

### 0.2 v3.3 신규분 — v3.2 감사의 전면 통합 (K9b 정량 결론 철회) — v3.4에서 (2)·(5)의 문구 일부 정정됨

v3.3은 v3.2 감사(`AUDIT-RESEARCH-REOPEN`; 표적 = v3.2의 핵심 신규분인 K9b 정량 결론 + 패키지·가드; 독립성 L3 다른
모델 계열 + L5 결정론적 재실행·반례)를 **전건 수용, 0건 기각**했다. §4–21·§22.1–22.7의 수학과 v3.2의 세 분리(K9a/K9b,
상수/국소 축회전, 필요조건/해소)는 보존한다.

**(1) K9b — S3, 정량 결론 철회.** Prop. 39.6에서 살아남는 것은 **대수**뿐이다: `(MGM)₁₂ = y₁y₂G₁₂`(C99a), `D_ij`의 trace
공식과 `D`의 Hermite성(C99b), 일반 2×2 Hermitian 행렬의 고윳값 bracket(C99c). 따라오지 **않는** 것: `λ_max(D)`가
coherent two-flavour carrier의 임계 결합이라는 것(C99d)과 정리 36의 단일 밴드 bound가 그 carrier에 그대로 유지된다는
것(C99e). 정리 36은 밴드 하나·질량 하나·gap 하나·밀도 하나·`⟨E⁻¹⟩` 하나·filled-disk 극값자로 유도되었고, 정리 39가 이를
여러 밴드로 옮길 수 있었던 이유는 대각 평균장이 gap 방정식을 분리했기 때문인데 K9b는 바로 그 대각성을 깬다. 따라서
"unchanged bound", "`n_c/n_t ≈ 2.16×10⁷` 필요", "`n_partner ≤ n_top`에서 조건부 기각"은 **모두 철회**하고 **K9b는 OPEN**으로
되돌린다. 감사의 반례족 `G = ww†, w = (u, √r·Nγ₅u)`(rank-one PSD)를 재현했다(W16): 감사가 지적한 대로 v3.2는 charm 대각항
`D_cc = q²r·D_tt`를 버렸고, 그것을 포함하면 `λ_max/D_tt = 42.07`은 `r ≈ 7.44×10⁵`에서 도달된다(`2.16×10⁷`이 아님). 어느
수도 admission 기준이 아니다 — 필요한 것은 **coherent two-band 정리**(joint dispersion, `κ`의 블록 합성, coherence 하의
Pauli 극값자, `λ_max(D)`가 임계 gap 방정식에 들어간다는 정리, 그 결과의 admission 기준)이며 이를 **증명 의무 39.8**로
등록한다. V33은 실제 내용(등밀도에서의 고윳값 보정 산술, C99d/e 조건부)으로 재타이핑했고, 레지스트리의 K9b 상태는
`OPEN`(정리 36 비적용)이다.

**(2) Elitzur 범위(S1/S2).** "게이지 이론의 모든 상태에서 0" → "게이지 불변 상태/게이지 불변 measure에서, **undressed** 국소
게이지 비불변 연산자의 기대값은 0"; 고정 게이지 기대값·경계 gauge reduction·dressed 비국소 연산자는 범위 밖(정리 39.4, C96).

**(3) `κ = T₂`의 부호(S1).** `z₀ = −tanh(Δ/2T)` 규약에서 정상 기록은 음수이므로 Cor. 41.1·W14는 **`|κ| = T₂`(`κ = −T₂`)**로
쓴다. 부등식은 불변.

**(4) 외부화(S2/S1).** A1–A6를 §2에 표로 다시 수록했다(A1–A3·A1′은 v1.1 원문, A4·A5는 본문 사용례에서 재구성했음을 표시).
front matter의 handoff를 **RQ2→RQ3**로 고쳤다. Prop. 39.6의 novelty는 선행연구 sweep 미수행이므로 **OPEN-NOVELTY**.
제목을 범위에 맞게 축소했다. 계보 자료는 supplement로 분리했다.

**(5) 패키지·가드(S2).** 감사자가 받은 4파일에는 baseline 원장이 없어 exit 2였다. v3.3은 artifact J의 42행 fingerprint를
**스크립트에 내장**하여 4 core 파일만으로 G18을 측정하고(JSON은 있으면 교차검증), release manifest를 실행 시 **생성**한다.
G20·G23은 감사의 두 의미적 주입("It is its discharge." / "The transverse Bloch relaxation time is denoted T₂.")을 통과시켰다.
v3.3: G20에 §22.9 문장 단위 claim-state 규칙('discharge'를 담은 문장은 부정·철회 표지를 가져야 함), G23에 symbol-table
문장 규칙('relaxation/dephasing time'을 말하는 문장은 `τ`를 말하고 `T₂`를 말하지 않아야 함), 신설 **G24**(원고의 기계 판독
CLAIM-STATE 블록 ↔ 원장이 계산한 상태), G21의 **기능화**(exit 정책 함수를 합성 행집합으로 실행). 두 주입은 이제 FAIL한다
(live-fire 기록). 한계는 숨기지 않는다: 이 가드들은 문장 단위 관계 규칙이지 산문의 의미 검사기가 아니다(§1).

**Z-Spin에 대한 귀결.** `RQ3` bridge `OPEN → OPEN`. **SUPPORT 유지, CORE 승격 없음, SSOT 변경 없음. FREEZE-CANDIDATE 보류
유지.** Mission 정렬은 높고(§6.2 4항목 충족), 달성은 아니다. 후속 식별자 미부여.

### 0.3 v3.2 신규분 — v3.1 감사의 전면 통합 — **v3.3에서 부분 철회됨** (K9b 정량 결론; §29 v3.3 참조. 아래 본문은 계보 보존을 위해 그대로 둔다)

v3.2는 v3.1 감사(`AUDIT-RESEARCH-REOPEN`; 재개방 범위 §22.8 정리 39.4, §22.9 handoff, release package)를
**전건 수용, 0건 기각**하고 다섯 수리를 수행했다. §4–21과 §22.1–22.7의 수학은 불변이다. 바뀐 것은 **정리 39.4의
양화사**, **Cor. 41.2의 강도**, **정리 38.3의 범위 문장**, **표기·front matter**, 그리고 **패키지**다. 감사가 요청한
계산 하나(K9b가 정리 39의 per-band bound를 바꾸는가)를 수행했다(Prop. 39.6, C99·V33).

**(1) 정리 39.4 — S3 결함 인정, K9를 둘로 분리.** C96이 실제로 증명하는 것은 (i) 색 비대각 bilinear가 `SU(3)`에
대해 게이지 비불변이고 (ii) `(t,b)` 비대각 bilinear가 전하 `1`을 띠어 `U(1)_em`에 대해 비불변이라는 것뿐이다.
v3.1은 여기서 "색/flavour-대각 평균장은 정리"로 확대하여 K9 전체를 닫았는데, **같은 게이지 표현·같은 전하를
갖는 세대 사이의 bilinear**(`ū Γ c`, `d̄ Γ s`, `ē Γ μ`; 색을 singlet으로 수축)는 게이지 **불변**이므로 Elitzur가
금지하지 않는다. ⇒ **K9a**(색·전하 변경 비대각) = CLOSED(정리 39.4, 재양화), **K9b**(동일 표현 세대-flavour
coherence) = **OPEN**. "대각 평균장은 정리"는 **철회**하고 "색·전하 대각성은 정리, 세대 대각성은 아님"으로 교체.

**(2) Prop. 39.6 — K9b를 한 번 계산했다(C99, 정확; V33, 수치).** Yukawa 꼭짓점 `diag(y₁,y₂)⊗1₄`와 flavour-coherent
2점함수(`G₁₂ ≠ 0`)에서 Fock 연산자는 **비대각 블록 `y₁y₂G₁₂`를 얻는다** — 정리 39의 블록대각성은 상호작용의
성질이 아니라 대각 평균장의 성질이었다. 대각 `d`-채널 계수 `D_ii = ¼y_i²Tr(Nγ₅G_ii)`는 `G₁₂`에 **불변**이고,
유효 결합은 2×2 Hermitian flavour 행렬 `D`이며 그 최대 고윳값은 **정확히** `max_i D_ii ≤ λ_max(D) ≤ max_i D_ii + |D₁₂|`.
즉 flavour coherence는 후보의 유효 계수를 (불변인) per-band bound에 대해 **올리기만** 할 수 있다(v2.9의 `1/N_b`
오류와 같은, 경로에 유리한 방향 — 그대로 보고한다). SM에서 top의 동일 표현 짝은 `u, c`뿐이고, 양의 2점함수의 Cauchy–Schwarz로
`|D₁₂|/D_tt ≤ (y_c/y_t)(n_c/n_t)^{1/2}/κ = 0.885%·(n_c/n_t)^{1/2}`: 밴드 밀도가 같으면 ×42.07 부족은 ×41.7이 되고, 부족을
메우려면 top 밴드보다 **~2×10⁷배 조밀한** coherent charm 밴드가 필요하다 — 코퍼스가 공급하지 않으나 이 논문이
배제하지도 못하는 객체. ⇒ K9b: `n_partner ≤ n_top` **조건부** REJECTED-BY-BOUND, 조건 밖에서는 **OPEN**. 생존자
집합은 {K7(조건), K8, **K9b(조건)**}이며, "코퍼스 안, 자체 정규화 아래서는 아무것도 살아남지 않는다"는 **철회**한다.

**(3) Cor. 41.2 — S2, 약화.** "기록 값의 선택 = `D-S14-EVENT-001`의 해소"는 과했다. Mission RQ3와 정의 40에 따르면
온도/rest frame은 누락 selector의 **한 성분**일 뿐이며, action-derived 환경·non-phase-covariant selector·faithful
biased 정상상태(S4)·instrument 선택·definite/Born 기록(S6)이 여전히 필요하다. 정확한 문장: **M67은
`D-S14-EVENT-001`의 필요조건 하나를 정량화했다 — 어떤 thermal rest-frame 경로도 `T/Δ ≤ 0.4147`을 만족해야
한다.** "RQ3 잔여와 RQ2 잔여가 일치한다"는 **[가설]**로 강등: RQ2의 clock/rest-frame 구성이 RQ3 환경 선택의 입력
하나를 공급할 **가능성**이 드러났을 뿐이며, 동일시는 공통 작용 또는 compatibility theorem을 요구한다(Mission §4.2).

**(4) 정리 38.3 — S2 범위 수정.** `H²`-정칙화 스펙트럼 supertrace 상쇄(C94의 대수: `𝒞`가 `E ↔ −E`를 짝짓고 밀도를
뒤집으며 `L_θ`를 보존)는 **유지**한다. "임의의 국소 축회전 `α(x)`에 대해 bag 정의역을 고정한 Fujikawa Jacobian이
1이고 `η`/inflow 항이 없다"는 **철회**: 국소 `α(x)`가 `dom H`를 보존한다는 증명이 없다. 상수 `α`는 정리 38.4의
co-rotation으로 닫혀 있고, 국소 `α(x)`의 domain-preservation은 **[열림] 증명 의무**로 등록한다(Cor. 38.7).

**(5) 표기·front matter·패키지.** 정리 41의 완화 시간은 **`τ₁, τ₂`** 로 쓰고 Z-Spin 표적 **`T₂ = 0.8354`** 는 기호를
유지한다(TYPE LOCK; 가드 G23이 §22.9를 검사). 생존자 목록·scope verdict·§23·§26·§27을 동기화하고, 아티팩트 I의
행수 오기(`37` → **38**)를 정정했다. 패키지: **v3.1 원장을 동봉**(G18 baseline), G22는 동봉되지 않은 계보
스크립트를 FAIL이 아니라 "NOT SHIPPED"로 보고, 원고 경로는 glob(`*M67_v3_2.md`)으로 해소, clean-room 재실행
**42행 · FAIL 0 · DEGRADED 0 · exit 0**. 감사 밖의 발견 하나: 전달된 v3.1 4-파일 패키지는 clean room에서 **exit 1**
(G18 DEGRADED **+ G22 FAIL**)이었다 — 감사의 exit 2보다 엄격한 실패이며 §26에 기록한다.

**Z-Spin에 대한 귀결.** `RQ3` bridge `OPEN → OPEN`. **OUTPUT ROLE `SUPPORT` 유지, `CORE` 승격 없음, SSOT 변경 없음.**
**FREEZE-CANDIDATE는 보류(WITHHELD)**: v3.2의 delta 재감사에서 새 S2+가 없을 때만 재제안한다. Mission §6.2의 no-go
4항목(EXCLUDED CLASS / EXACT ASSUMPTIONS / SURVIVING COMPLEMENT / NEXT MINIMAL CONSTRUCTION)은 §22.10에서 K9b를
포함하도록 갱신했다. 후속 식별자 미부여.

### 0.4 이전 판본 요약 (v3.1 → v2.4) — supplement로 이동

`ZS-M67_v3_3_provenance_supplement.md` §S0. 각 판본의 신규분 요약은 계보 보존을 위해 그대로 옮겼으며, 그중 v3.1의
"K9 폐쇄"·"남은 연산 없음"·"D-S14-EVENT-001 해소", v2.9의 전칭 폐쇄·TERMINAL-IN-SCOPE는 후속 판본에서 철회되었다(§29).

---

## 1. Verification banner

```text
artifact A: zs_m67_verify_v2_1.py    ledger zs_m67_verify_v2_1.json     (Sections 4-12)
            82 rows, FAIL 0.  RETYPED: C06, C07 (C -> W), V01 (quantifier).
            SUPERSEDED: G7 by G17, G8 by G18 of artifact B.
artifact B: zs_m67_verify_v2_4.py    ledger zs_m67_verify_v2_4.json     (Sections 13-16)
            sha256 = 5d4477d07fc373b4120f8aa475a001129a28902afabef61b028ff98efe85833d
            48 rows, FAIL 0, DEGRADED 0 (when run beside this manuscript).
            census C=25 V=6 W=4 / R=2 G=5 / D=6 X=0 T=0.  24 rows carry a UNIVERSAL flag.
            SUPERSEDES zs_m67_verify_v2_3.py (38 rows) in full.
artifact C: zs_m67_verify_v2_5.py    ledger zs_m67_verify_v2_5.json     (Section 18)
            sha256 = 7499b55cbfa2d68424bfe939f9be921532ca8a4aee44697d7d1f58d5626e22f7
            22 rows, FAIL 0, DEGRADED 0 (when run beside this manuscript and the v2.4 ledger).
            census C=7 V=2 W=2 / R=2 G=5 / D=4.  7 rows carry a UNIVERSAL flag.  Runtime ~11 s.
            Does NOT supersede artifact B; both are in force.
artifact D: zs_m67_verify_v2_6.py    ledger zs_m67_verify_v2_6.json     (Section 19)
            sha256 = 9bfe3cda2838931cf2187cbbdc65d077ea64eed8d9a658fd8cb42401447d0d16
            21 rows, FAIL 0, DEGRADED 0 (beside this manuscript and the v2.5 ledger).
            census C=6 V=2 W=1 / R=2 G=6 / D=4.  6 rows carry a UNIVERSAL flag.  Runtime ~13 s.
            NEW GUARD G20 fails the run if section 19 drops its mean-field / DERIVED-CONDITIONAL
            typing.  Does NOT supersede artifacts A-C; all four are in force.
artifact E: zs_m67_verify_v2_7.py    ledger zs_m67_verify_v2_7.json     (Section 20)
            sha256 = 6283b8c4c97f84062c7cee5ba9b7ef7a430d6525c77e8adc717b638362a45e8c
            18 rows, FAIL 0, DEGRADED 0 (beside this manuscript and the v2.6 ledger).
            census C=5 V=1 W=1 / R=1 G=6 / D=4.  5 rows carry a UNIVERSAL flag.  Runtime ~50 s
            (the exact Fierz completeness check dominates).  G20 widened to sections 19 AND 20.
            Does NOT supersede artifacts A-D; all five are in force.
artifact F: zs_m67_verify_v2_8.py    ledger zs_m67_verify_v2_8.json     (Section 21)
            sha256 = 13770a3ed5bbc3a551f3aa6c1ef119496982d9691d2f41f7490d935cedf8bf2e
            17 rows, FAIL 0, DEGRADED 0 (beside this manuscript and the v2.7 ledger).
            census C=4 V=2 W=0 / R=1 G=6 / D=4.  4 rows carry a UNIVERSAL flag.  Runtime ~10 s.
            G20 widened to sections 19-21 and requires CLOSED-NEGATIVE / KILLED in section 21.
artifact G: zs_m67_verify_v2_9.py    ledger zs_m67_verify_v2_9.json     (Section 22, v2.9)
            sha256 = 1d8d919a2e19b448d2668722650180d49349ec0eb71ef162cf848807d7e9a975
            16 rows.  SUPERSEDED IN FULL by artifact H after the v2.9 audit; its ledger is shipped
            with v3.0 as the provenance baseline measured by artifact H's G18.  Clean-room note:
            run from the delivered four-file v2.9 package (no v2.8 ledger) it reported G18 DEGRADED
            with exit 0 -- the audit finding is confirmed by re-execution this session.
artifact H: zs_m67_verify_v3_0.py    ledger zs_m67_verify_v3_0.json     (Section 22, v3.0)
            sha256 = ff4130076f4e3f69daa0081944a250572934cf201286ad96c3d387efb0f01c23
            27 rows, FAIL 0, DEGRADED 0.  SUPERSEDED IN FULL by artifact I; its ledger is shipped with
            v3.1 as the provenance baseline measured by artifact I's G18.
artifact I: zs_m67_verify_v3_1.py    ledger zs_m67_verify_v3_1.json     (Section 22, v3.1)
            sha256 = f9566700d023c9abdc0591277e7483510939db7ec7ef520b285fefd406525d70
            38 rows, FAIL 0, DEGRADED 0 (beside the v3.1 manuscript, the v3.0 ledger AND at least one
            lineage sibling script).  SUPERSEDED IN FULL by artifact J; its ledger is shipped with v3.2
            as the provenance baseline measured by artifact J's G18.  Clean-room note (v3.2): re-run
            from the delivered four-file v3.1 package (no v3.0 ledger, no sibling script) it gives
            36/38 rows identical, G18 DEGRADED and G22 FAIL, exit 1 -- the audit's package finding
            (exit 2) is confirmed and is stricter than reported.
artifact J: zs_m67_verify_v3_2.py    ledger zs_m67_verify_v3_2.json     (Section 22, v3.2)
            sha256 = 23ef0930278d36d83708cdbeb962476ed713180335799deec38ef701bf3969dd
            42 rows, FAIL 0, DEGRADED 0 (beside the v3.2 manuscript AND the v3.1 ledger).  SUPERSEDED
            IN FULL by artifact K; its 42 row fingerprints are EMBEDDED in artifact K as the G18
            baseline.  Clean-room note (v3.2 audit, confirmed): the four files the auditor received
            (manuscript, script, ledger, session) lacked the v3.1 ledger -> G18 DEGRADED, exit 2.
            Its C99 row is SPLIT in K (C99a-c algebra; C99d/e OPEN in D36); its V33 reading as a
            conditional rejection of K9b is WITHDRAWN.
artifact K: zs_m67_verify_v3_3.py    ledger zs_m67_verify_v3_3.json     (Section 22, v3.3)
            sha256 = 21b1c088d99560cba45bad58c76156996ddfd7e306b44d5285a9245d14dab266
            48 rows, FAIL 0, DEGRADED 0.  SUPERSEDED IN FULL by artifact L; its 48 row fingerprints
            (from the SHIPPED ledger, sha256 f5f577f0...) are EMBEDDED in L as the G18 baseline.  Cross-
            machine note (v3.4): re-run on python 3.12.3 / numpy 2.4.4 reproduces 48/48, exit 0, but the
            W15 claim text embedded a 1e-16 residual (1.6e-16 vs 1.7e-16 shipped), so the ledger was not
            byte-identical across machines and G18's carried count moved 27 -> 26; retyped in L.
            census C=16 V=6 W=3 / R=1 G=11 / D=11.  16 rows carry a UNIVERSAL flag.  Runtime ~15 s.
            ADDED: C99a, C99b, C99c (Prop. 39.6 algebra, split), W16 (the v3.2 audit's counterexample
            family, reproduced), D36 (C99d/C99e OPEN), D38 (v3.2 audit acceptance record), G24
            (CLAIM-STATE manifest guard).  REMOVED: C99 (split; the only removal G18 accepts).
            RETYPED (measured by G18): C96 (Elitzur scope), V32 and W14 (|kappa| = T_2), V33 (equal-density
            arithmetic only; conditional on D36), V30 (registry: K9b OPEN), G17/G18 (targets; embedded
            baseline), G20 (sentence rule), G21 (functional), G22, G23 (symbol-table rule), D27, D28, D34.
            Exit policy: 0 iff FAIL == 0 and DEGRADED == 0; 1 on FAIL; 2 on DEGRADED (fail-closed);
            the policy is ONE function, exercised by G21 on synthetic row sets.
            release_manifest_v3_3.json is GENERATED at run time from the measured hashes (VERIFY sect.10).
artifact L: zs_m67_verify_v3_4.py    ledger zs_m67_verify_v3_4.json     (Section 22 incl. 22.11, v3.4)
            SUPERSEDED IN FULL by artifact M; its 56 row fingerprints (from the SHIPPED v3.4 ledger, sha256
            f94024e5...) are EMBEDDED in M as the G18 baseline.  Its C102/D39 onset normalisation counted the
            Yukawas twice (v3.4 audit); corrected in M.  sha256 (historical, no longer measured) =
            c6a82d472699afd7731e0f0804bbe3a76c61acdc9e0ce889282fe735f3bab2be
            56 rows, FAIL 0, DEGRADED 0 (beside this manuscript ALONE; the v3.3 ledger is optional and
            is cross-checked against the embedded baseline when present).
            census C=19 V=7 W=3 / R=1 G=12 / D=14.  19 rows carry a UNIVERSAL flag.  Runtime ~15 s.
            ADDED: C100 (Lemma 39.9 record composition), C101 (Lemma 39.10 harmonic-mean overlap), C102
            (Thm 39.11 pair-channel decoupling), V34 (omega numbers), D39 (C99d/e after 22.11; obligation
            39.8'), D40 (v3.3 audit acceptance record), D41 (external baseline for K9b), G25 (package object
            graph).  REMOVED: none.  RETYPED (measured by G18): C96 (Elitzur citation + hypotheses H1/H2),
            V32 (target-independent ceiling / target-conditioned number), W15 (threshold form), G17/G18/G20
            (rule iv)/G21 (empty -> 2)/G22/G23/G24 (targets and tokens), D27, D28, D34, W16 (threshold form; a
            lineage rescan for the W15 defect type found its 1e-12 eigenvalue residual in the claim text).
            Exit policy: 0 iff FAIL == 0 and DEGRADED == 0; 1 on FAIL; 2 on DEGRADED or on an EMPTY ledger
            (fail-closed; the v3.3 audit noted exit_code([]) == 0); the policy is ONE function, exercised by
            G21 on synthetic row sets including {}.
            release_manifest_v3_4.json is GENERATED at run time and is the FOURTH CORE OBJECT (VERIFY sect.9.1);
            it registers session / audit report / provenance supplement as provenance objects with hashes.
artifact M: zs_m67_verify_v3_4_1.py    ledger zs_m67_verify_v3_4_1.json     (Section 22 incl. 22.11, v3.4.1)
            sha256 = ae76e712c4bc8999a9701fb337e46e4e145c1e90df3b2d4e50af353b7514a9dc
            57 rows, FAIL 0, DEGRADED 0 (beside this manuscript ALONE; the v3.4 ledger is optional and
            is cross-checked against the embedded baseline when present).
            census C=19 V=7 W=3 / R=1 G=12 / D=15.  19 rows carry a UNIVERSAL flag.  Runtime ~15 s.
            CORRECTION-ONLY (paper v3.4.1 <-> script v3_4_1; VERIFY sect.6.1).  ADDED: D42 (v3.4 audit record).
            REMOVED: none.  RETYPED (measured by G18): C101, C102, D39, V34 -- the G_4 channel-strength
            correction (G_4^(ij) = y_i y_j/(4 m_h^2); no certificate changed; V34 now prints G_4^(t), G_4^(tc),
            G_4^(tu)); D34, D40 (lifecycle: FREEZE-CANDIDATE PROPOSED); G17/G18/G20/G21/G22/G23/G24/G25
            (targets, tokens).  Exit policy unchanged (0 / 1 on FAIL / 2 on DEGRADED or empty ledger).
            release_manifest_v3_4_1.json is GENERATED at run time and is the FOURTH CORE OBJECT.
env:        python 3.12.3 (artifacts A-G, L) / 3.11 (artifacts H-K) · numpy 2.4.4 · sympy 1.14.0 ·
            mpmath 1.3.0 (dps=60) · scipy 1.17.1
            seed 20260902 · block C is exact (Q(i), exact radicals, Groebner reduction modulo
            the on-shell ideal), with NO tolerance anywhere
proof objects: 0 in ALL ledgers.  P-review-level: L2 (author lineage); the v3.2 and v3.3 audits were L3 + L5;
            the v3.4 audit was L3 (delta review of the repairs and sect.22.11).
guards:     G15 STRONG-PREDICATE BINDING · G19 UNIVERSAL-QUANTIFIER BINDING
            G17 MEASURES the artifact sha256 against the hash printed above
            G18 MEASURES ledger provenance over the FINAL row set against the EMBEDDED baseline
            G20 token guard + SENTENCE RULE: a sentence of sect.22.9 containing 'discharge' must carry
                a negation or retraction marker; sect.22.8 may not carry a live K9b REJECTED-BY-BOUND
            G23 glyph rule + SYMBOL-TABLE RULE: a sentence of sect.22.9 naming a relaxation/dephasing
                time must name tau_1/tau_2 and not T_2; every printed artifact-K row count; run lines
            G20(iv) v3.4: a sentence of sect.25 saying the missing object is 'completely specified' must also
                say it is not constructed (negation or 'signature'); the phrases 'all now derived' and
                'first target-blind' may not occur live anywhere (the v3.3 audit's S2-1 and S2-2 phrases);
                v3.4.1: the double-counted onset forms 'G_4 y_1 y_2' / 'G_4 y_t y_c' may not occur live either
                (the v3.4 audit's finding); live-fire: re-injecting v3.4's onset line -> G20 FAIL
            G24 CLAIM-STATE block (below) == ledger-computed registry statuses and lifecycle tokens; v3.4 adds
                C99d=CLOSED-NEGATIVE-LINEAR, MissingObject, ThermalCeiling, T-over-Delta; v3.4.1 adds
                FREEZE-CANDIDATE=PROPOSED (a proposal token, never a grant), G4-channel=YUKAWA-INSIDE and
                artifactM.rows
            G25 v3.4: the sect.27 package block's declared CORE must equal the manifest's core (manuscript,
                verifier, ledger, release manifest) and session / audit / supplement must be declared as
                provenance objects (v3.3 audit S2-3)
            G21 FUNCTIONAL: the exit-code function is run on synthetic row sets, including the empty set
            DEGRADED is a DISTINCT result state and is never reported as PASS.
            Live-fire (v3.3), outputs in the session file: the v3.2 audit's two injections --
            "It is its discharge." in sect.22.9 -> G20 FAIL, exit 1; "The transverse Bloch relaxation
            time is denoted T₂." in sect.22.9 -> G23 FAIL, exit 1; CLAIM-STATE K9b=REJECTED-BY-BOUND ->
            G24 FAIL, exit 1; "37 rows" injected -> G23 FAIL; banner hash altered -> G17 FAIL;
            manuscript removed -> G17/G20/G23/G24 DEGRADED, exit 2; WITHHELD removed from sect.23 ->
            G20 and G24 FAIL.
            Live-fire (v3.4), outputs in the session file: the v2.6 sentence 'completely specified ... all now
            derived' re-injected into sect.25 -> G20 FAIL; 'first target-blind constraint' re-injected -> G20
            FAIL; session file added to the core line of sect.27 -> G25 FAIL; CLAIM-STATE C99d=OPEN -> G24
            FAIL; manuscript removed -> G17/G20/G23/G24/G25 DEGRADED, exit 2.
WHAT THE GUARDS CANNOT DO (stated, not hidden): they are token-, sentence- and manifest-level
            consistency checks.  A paraphrase that restates a withdrawn claim without the guarded
            words ('discharge', 'relaxation time', 'REJECTED-BY-BOUND') is not caught.  Prose
            semantics are protected by audit, not by this script (VERIFY sect.7.2 S4: the guard reads
            declared tokens; the CLAIM-STATE block is where the relations are declared).
limitations: W-rows are witnesses; no interval arithmetic; no proof assistant; NO independent
            clean-room execution by a third party of artifact M (run from a fresh directory by the same
            model -- L2; the v3.3 audit's L3+L5 re-run covered artifact K); qualified-human anchor NONE.
```

<!-- CLAIM-STATE v3.4.1 (machine-readable; read by guard G24 and cross-checked against the ledger)
K1=REJECTED-BY-BOUND
K2=REJECTED-BY-BOUND
K3=REJECTED-BY-BOUND
K4=REJECTED-STRUCTURAL
K5=REJECTED-STRUCTURAL
K6=REJECTED-STRUCTURAL
K7=REJECTED-BY-BOUND
K8=EXTERNAL-UNEVALUABLE
K9a=REJECTED-STRUCTURAL
K9b=OPEN
K10=NOT-A-CANDIDATE
FREEZE-CANDIDATE=PROPOSED
D-S14-EVENT-001=NECESSARY-CONDITION-SUPPLIED
Cor38.7=OPEN
C99d=CLOSED-NEGATIVE-LINEAR
C99e=OPEN
RQ3=OPEN
T2=TARGET
tau1,tau2=RELAXATION
MissingObject=SPECIFIED-NOT-CONSTRUCTED
ThermalCeiling=TARGET-INDEPENDENT
T-over-Delta=TARGET-CONDITIONED
G4-channel=YUKAWA-INSIDE
artifactM.rows=57
-->

**A PASS row is not a theorem.** Only `P/C/V/W` rows carry scientific evidence, and `P = 0` in all thirteen ledgers; 57 PASS rows are not 57 theorems. K7's
registry status `REJECTED-BY-BOUND` is **conditional on `f = M_P`** (the registry vocabulary has no conditional token;
the condition is carried by the entry's `class = corpus-conditional` and by V30).

---

## 2. Paper contract

```text
QUESTION:
  Which self-adjoint boundary conditions survive target-blind covariance; does the action or
  the free quantum effective action narrow them; what exactly does the boundary datum supply
  towards F-M66.15; and what is the precise remaining obstruction?

ONE-SENTENCE CONTRIBUTION:
  Under a flat static planar boundary, minimal coupling and one 4-component Dirac spinor we
  prove (i)-(v) as in v2.3, and in addition (vi) that the carrier projector restricted to the
  boundary subspace is invertible, so the operator-state lift is action-derived rather than
  declared; (vii) that the residual rotation about the normal acts unitarily and commutes with
  the grading, so ZS-M66's one-parameter boundary state is derived; and (viii) that the
  tangential boost preserved by the boundary condition acts on the carrier as a NON-unitary
  SL(2,C) Bloch boost whose generator is a GRADING-ODD element of the flip family, whence
  every boost-invariant boundary state has kappa = 0 and the required faithful biased state
  exists only if the environment supplies a rest frame.  NEW in v2.5: (ix) every stationary
  mode of the wall has carrier polarisation kappa = m sin(thetabar)/E (bound or continuum, either
  energy sign), so kappa of any unpolarised stationary state is m sin(thetabar) <1/E>_boundary;
  (x) charge conjugation anticommutes with H for every mass phase and preserves every L_theta, so
  eta(H) == 0 and the edge-sector eta route is empty; with Thms 12-13 every spectral selector
  inside A1-A5 is exhausted; (xi) no autonomous map Phi_partial exists under A4 (witness), the
  carrier state is a pushforward, and the three necessary conditions of Cor. 21.1 collapse to
  "unique stationary state with kappa != 0"; (xii) the edge band is a qubit bundle over k_perp and
  its thermal states meet every state-side requirement of Cor. 14.2 without consulting lambda,
  while selecting nothing.  NEW in v2.6: (xiii) on the boundary subspace the entire
  derivative-free boundary-term class collapses to a multiple of the grading J_E, so a boundary
  interaction is on shell a self-coupling of the record observable; (xiv) its mean field gives a
  gap equation with critical coupling g_c = 1/(2 m <1/E>) and the exact selection identity
  |cos thetabar| = g_c/|g|, so the boundary angle is a function of a Lagrangian coupling rather
  than a free modulus; (xv) the edge band is a 2+1 Dirac fermion of mass m sin(thetabar), whose
  parity-odd level is piecewise constant on the arc; (xvi) ZS-M66 and ZS-M67 use opposite chiral
  sign conventions and the same invariant, discharging Cor. 8.2 and vacating Cor. 26.4.
MAIN CLAIMS:      Thm 1-5, Prop 6, Thm 9-15, Thm 19-21, Thm 23-39, Lemma 38.0, Lemma 39.0, Def 40,
                  Cor 7-8.2, 10.1, 13.1, 14.1-14.2, 15.1-15.3, 19.1, 21.1-21.3, 23.1-23.2,
                  24.1-24.3, 25.1-25.2, 26.1-26.4, 27.1-27.2, 28.1-28.3, 29.1-29.2, 30.1-30.2,
                  33.1-33.2, 34.1, 35.1-35.2, 36.1-36.2, 37.1-37.2, 38.1-38.5, 38.7, 39.1-39.5,
                  Prop 39.6 (algebra only), Proof obligation 39.8 (OPEN), 40.1-40.2, 41.1-41.4
                  (claim map, Section 24)
LOAD-BEARING ASSUMPTIONS (restated in full in v3.3; the v3.2 audit noted that "as in v2.3" left an
  independent reader without the exact class):
  A1  a flat, static, planar boundary (the plane x^3 = 0; relaxing A1 = curvature, Cor. 13.1 i)
  A2  minimal coupling; the boundary condition is a pointwise linear condition on psi|_bdy
      (higher-derivative and multi-fermion boundary terms are outside Thm 10, NC-M67.8)
  A3  one 4-component Dirac spinor in 3+1 (plus internal indices where Thm 2 / Thm 39 say so)
  A1' the boundary is a relativistic interface: tangential BOOSTS are imposed as a covariance
      requirement (dropping A1' enlarges the circle to a real 4-dimensional family, Remark 3.1)
  A4  FREE bulk: no gauge or axial background, no bulk interaction; the bulk is Gaussian
      (Thm 31).  Relaxed explicitly in Sections 19-22 where a boundary or Yukawa interaction is
      switched on, and every such result is typed mean field / DERIVED-CONDITIONAL
  A5  the boundary effective action is taken at its BARE value: the three boundary counterterms
      of Thm 13(c) (a cubic in A = m cos thetabar) are not fixed by any independent principle;
      Cor. 37.2 counts what fixing them would cost (two real parameters)
      [A4 and A5 are reconstructed from their use in this manuscript (Thms 13, 31, Cor. 13.1, 37.2);
       A1-A3 and A1' are v1.1's wording.  The v2.3 wording of A4/A5 was not re-read this session:
       [열림] (editorial) until reconciled.]
  A6  (NEW in v2.4)  a boundary REST FRAME is chosen.  The carrier E+ and the grading
      J_E = gamma5|E+ are defined through N = gamma0 gamma^n and therefore presuppose a
      boundary time direction; E+ is NOT invariant under the tangential boosts that the
      boundary CONDITION does preserve (C56).  Every statement about kappa is frame-relative.
      A6 is a physical assumption, not a theorem, and Theorem 21 shows it cannot be dropped.
EXTERNAL BASELINE (additions in v2.4):
  arXiv:2305.13606 = Phys. Lett. B 844 (2023) 138098, "Edge states and the eta invariant":
     for chiral bag boundary conditions the SMOOTH part of eta(0,H) does not depend on the
     chiral-bag parameter, and the theta-dependence sits in the edge states.
  A. Peres, P. F. Scudo, D. R. Terno, PRL 88, 230402 (2002), arXiv:quant-ph/0203033:
     the reduced spin density matrix of a free spin-1/2 particle is NOT Lorentz covariant and
     the spin entropy is not a relativistic scalar.
  arXiv:1308.5635 (JHEP 12 (2013) 073), "Edge States: Topological Insulators, Superconductors
     and QCD Chiral Bags": explicit chiral-bag edge spinor with e^{+-theta/2} components.
OPEN DEBTS:  F-M66.15 (OPEN; MECHANISM EXHIBITED -- spontaneous grading breaking above a boundary
             critical coupling -- but g, the sector, and the fluctuation treatment are open),
             F-M66.16 (OPEN; absorbed into "unique stationary state with kappa != 0"),
             F-M66.17 (CLOSED-NEGATIVE inside A1-A5; OPEN-BUT-TYPED outside: |cos thetabar| = g_c/g;
             after v3.0 PARTIALLY CLOSED-NEGATIVE: exact for spectral, free-bulk and the Goldstone's
             linear bulk couplings; conditional for Yukawa contact on diagonal bands and for the
             Goldstone residual class on f = M_P.  The v2.9 corpus-wide closure is WITHDRAWN.)
             STILL OPEN after v3.2: registry K7 (Goldstone normalisation other than M_P / external
             gradient) and K8 (corpus-external strongly coupled sector) -- both corpus-EXTERNAL;
             K9b (same-gauge-representation generation-flavour coherence; corpus object, gauge-
             invariant; OPEN -- Theorem 36's single-band bound has no proven extension to a coherent
             two-band carrier, Proof obligation 39.8; the v3.2 conditional rejection is WITHDRAWN);
             the local-alpha(x) domain-preservation obligation of Thm 38.3 (Cor. 38.7);
             upstream inputs A5 (exactly two real counterterm parameters, Cor. 37.2) and
             D-S14-EVENT-001 (OPEN; M67 supplies ONE NECESSARY CONDITION on it, T/Delta <= 0.4147,
             Cor. 41.1-41.2 -- not a discharge);
             prior art on the boundary Gross-Neveu mapping and on the bilinear atlas (OPEN-NOVELTY).
             CLOSED in v3.1-v3.2: the constant-axial-rotation Jacobian and the H^2-regularised
             spectral supertrace inside A1-A4 (Thms 38.3 as re-scoped, 38.4); K9a -- colour- and
             charge-changing off-diagonal condensates (Thm 39.4 re-quantified).
             WITHDRAWN in v3.2: "K9 closed", "the diagonal mean field is a theorem", "selecting the
             record value = discharging D-S14-EVENT-001", "no computation remains inside scope".
             WITHDRAWN in v3.3: "flavour coherence leaves Theorem 39's bound unchanged", "a coherent
             charm band ~2e7 times denser than the top band would be needed", "K9b REJECTED-BY-BOUND
             conditionally on n_partner <= n_top"; the title "Classical selector exhaustion".
             And, unchanged,
             faithfulness on the chosen sector, boundary counterterms (A5), the quantum axial
             invariant outside A4, boundary RP, Lorentzian<->Riemannian
             DISCHARGED in v2.6: the theta_m convention of Cor. 8.2 (Thm 30)
RELEASE TARGET:  independent review.  Not preprint-ready.
```

---
## 3. Setup and definitions

### 3.1 Conventions

Minkowski metric `η = diag(+,−,−,−)`, Dirac representation, `{γ^μ,γ^ν} = 2η^{μν}`, `γ₅ = iγ⁰γ¹γ²γ³`,
`(γ⁰)† = γ⁰`, `(γ^k)† = −γ^k`, `γ₅† = γ₅`, `γ₅² = 1`. Boundary: the static plane `x³ = 0`, unit
spacelike outward normal `n = e₃`, `γⁿ := γ³`. Tangential directions `{0,1,2}`.

**Definition 3.1 (boundary form).** `N := γ⁰γⁿ`; `N† = N`, `N² = 1`, `tr N = 0`, `[N,γ₅] = 0`.
`ψ†Nψ = ψ̄ n̸ ψ` is the normal Dirac current. *(exact: C03)*

**Definition 3.2 (admissible boundary condition).** A pointwise linear condition `ψ|_∂ ∈ L` is
**admissible** if `ψ†Nχ = 0` for all `ψ,χ ∈ L` and `L` is maximal with that property.

**Definition 3.3 (canonical involution).** For admissible `L`, `B_L := 2P_L − 1` with `P_L` the
**orthogonal** projector onto `L`. Then `B_L† = B_L`, `B_L² = 1`, `{B_L,N} = 0`, and `L ↦ B_L` is a
bijection (Theorem 1).

**Definition 3.4 (covariance).** Let `G` act on spinors by `ψ ↦ S(g)ψ`. An admissible `L` is
**`G`-covariant** if `S(g) L = L` for every `g ∈ G`.

**Definition 3.5 (boundary carrier and grading) — NEW in v2.2.** Let `ℂ⁴ = E₊ ⊕ E₋` be the spectral
split of `N`, `dim E_± = 2`. The **boundary carrier** is `E₊`, and the **boundary grading** is
`J_E := γ₅|_{E₊}`, which is well defined because `[N,γ₅] = 0`. In the basis fixed once and for all in
`zs_m67_verify_v2_2_newblock.py` (namely `e₋ = 2^{−1/2}(0,1,0,−1)`, `e₊ = 2^{−1/2}(1,0,1,0)`) one has

```
        N|_{E₊} = 1,        J_E = diag(−1, +1),        tr J_E = 0,      J_E² = 1,
```

which is exactly the carrier and grading declared by `ZS-M66` §5.1. *(exact: **C38**.)*

> **Basis-ordering caveat.** The ordering of `(e₋, e₊)` is a convention; the opposite ordering
> flips the sign of `J_E` and hence of `κ = Tr(ρJ_E)`, and simultaneously flips the sign of `θ`.
> The pair `(θ, κ)` is convention-independent; neither member is. All statements below use the
> `ZS-M66` §5.1 ordering. `[검증됨]` (C38, and the sign audit of Remark 3.0.)

> Covariance is defined at the level of **subspaces**. `[B,Σ] = 0` is a *sufficient* condition only
> (Lemma 6.2): the tangential boosts are not unitary, so conjugation of `B_L` is not equivalent to
> invariance of `L`. The verifier measures the non-unitarity directly: `‖S†S − 1‖ = 4.450` for
> `S = exp(0.7 γ⁰γ¹)` *(R02)*.

### 3.2 Dependency freeze

```text
corpus_as_of:        2026-09-04 KST (v3.0: plus the v2.9 audit text, accepted in full; v3.1: plus ZS-S14 v2.1
                     read from repo 1 and repo 2 searched for artifacts C-F: NOT_FOUND; v3.2: plus the v3.1
                     audit text, accepted in full, history approved through H-0281; v3.3: plus the v3.2
                     audit text (L3 + L5), accepted in full, history appended through H-0283)
active_upstream:     ZS-M66 v1.5.1 (FREEZE-PENDING-AUDIT), ZS-M61 v1.6, ZS-M60 v1.5,
                     ZS-S14 v2.1, PACKAGE_boundary_channel Ref_202609010052
locked_constants:    lambda = multiplier of T(z) = i^z at its fixed point z*, RECOMPUTED here
poison test:         the only M66 inputs used are the algebraic definition of N, the carrier
                     and grading of sect.5.1, the parameterisation a(theta), the existence of a
                     mass phase theta_m, and Thms 3.7/3.8 with ZS-D2/ZS-D3.  M66 Thm 3.9 - the
                     item subsumed by Szehr-Reeb-Wolf - is used ONLY with an IMPORTED tag. PASS
```

---

## 4. Theorem 1 — the moduli is `U(2)` (imported)

**Theorem 1.** `𝔅 := {B : B† = B, B² = 1, {B,N} = 0}` is diffeomorphic to `U(2)`;
`B ↦ L_B := ker(B−1)` is a bijection onto the admissible boundary conditions; every admissible `L`
has `dim L = 2`.

*Proof.* `N† = N`, `N² = 1`, `tr N = 0` give `ℂ⁴ = E₊ ⊕ E₋` with `dim E_± = 2` and
`ψ†Nψ = ‖ψ₊‖² − ‖ψ₋‖²`. Maximal isotropic subspaces of this split form are the graphs `{v ⊕ Wv}`
with `W : E₊ → E₋` unitary, hence `U(2)` and `dim L = 2`. For such `L`, `B_L = 2P_L − 1` is
Hermitian, involutive, and anticommutes with `N` because `N` exchanges `L` and `L^⊥`. Conversely
`B ∈ 𝔅` has `tr B = 0`, so `dim L_B = 2`, and `ψ†Nχ = (Bψ)†N(Bχ) = −ψ†Nχ` on `L_B`. ∎

*Certified: C03, C04, C05 (real dimension 8 of the linear part, exact over `ℚ(i)`).*
**Evidence retyping (audit A1).** Rows `C06`/`C07` of artifact A verify the `B ↔ W ∈ U(2)`
correspondence and the isotropy of the resulting subspace **on four Gaussian-rational unitaries**.
They are therefore **witnesses**, not universal certificates, and are retyped `C → W` in v2.2. The
analytic proof above is unaffected; the census of artifact A changes to `C=35, W=7`.
**Novelty: `IMPORTED-PROVEN`** — GUvdB Prop. 5.1; Al-Hashimi–Wiese.

---

## 5. Theorem 2 — colour and flavour insulation

**Theorem 2.** Let the spinor carry an internal index in a **finite-dimensional unitary irreducible**
representation `V` of a compact gauge group `K`, acting as `1₄ ⊗ ρ(k)`, with boundary form `N ⊗ 1_V`.
Then every gauge-covariant admissible boundary condition is `B = B_Dirac ⊗ 1_V` with `B_Dirac ∈ 𝔅`.

*Proof (repaired; audit A5).* Gauge covariance is the **group-level** statement
`[B, 1₄ ⊗ ρ(k)] = 0` for every `k ∈ K`. Since `ρ` is a finite-dimensional unitary **irreducible**
representation of the compact group `K`, Schur's lemma applies directly to the group action — no
passage to `Lie K` is needed, and none is legitimate, because for a **disconnected** compact `K`
the Lie-algebra commutant is strictly larger than the group commutant. Hence the commutant of
`1₄ ⊗ ρ(K)` is `M₄(ℂ) ⊗ 1_V`, and the remaining conditions read on `B_Dirac` alone. ∎

*Certified: C16 (real dimension `36 → 8` for `V = ℂ³` under `SU(3)`, exact), C17.*

**The irreducibility hypothesis is load-bearing, not decorative.** For the **reducible** `u(1)`
generator `diag(1,−1)` on `V = ℂ²` the covariant admissible real dimension is `4`, not `2`: two
independent chiral-bag circles survive *(counterexample W04, exact)*. Dropping unitarity or
compactness removes Schur's lemma and the theorem with it.

**Consequence.** This proves the Pre-Paper Dossier's colour-insulation lemma
(`[DERIVED-CANDIDATE]` → **PROVEN**) with an explicit dependency trace; no step uses the `D₃-2′`
assignment retracted by `ZS-S14 v2.1` Erratum E1/E2.

---

## 6. Theorem 3 — boundary covariance selects the chiral-bag circle

The boundary is invariant under the connected group generated by the two tangential boosts and the
rotation about the normal, `Spin(1,2)↑`, with spinor generators `Σ^{01} ∝ γ⁰γ¹`, `Σ^{02} ∝ γ⁰γ²`,
`Σ^{12} ∝ γ¹γ²`.

**Theorem 3 (selection).** The `Spin(1,2)↑`-covariant admissible boundary conditions are exactly

```
    L_{B_θ},      B_θ = cos θ · (i γⁿ)  +  sin θ · (γⁿ γ₅),      θ ∈ ℝ/2πℤ,
```

and this circle coincides with the chiral-bag family, `−i e^{iθγ₅}γⁿ = B_{θ+π}`. Boundary covariance
removes exactly three of the four real moduli parameters of Theorem 1, and the survivor is the
chiral angle.

### 6.1 Proof (subspace level)

*Proof.* **(i) Invariant planes.** As a `Spin(1,2)` representation `ℂ⁴ ≅ ℂ² ⊗ S` with `S` the
2-dimensional irreducible spinor representation. Every invariant 2-plane is `ℓ ⊗ S` with `ℓ` a line
in the multiplicity space, so the invariant 2-planes form `ℂP¹ ≅ S²` — a **two**-real-parameter
family, obtained before any admissibility requirement.

**(ii) Coordinates.** The multiplicity algebra is the commutant of the tangential generators,
`𝒜 = span_ℂ{1, γⁿ, γ₅, γⁿγ₅} ≅ M₂(ℂ)` (Lemma 6.1). A Pauli triple for `𝒜` is

```
        (σ_A^1, σ_A^2, σ_A^3) = (γ₅, iγⁿ, γⁿγ₅),
```

each Hermitian, involutive, mutually anticommuting; the invariant plane attached to `n ∈ S²` is
`L(n) := ran e(n)`, `e(n) = ½(1 + n·σ_A)`, with canonical involution `B(n) = n·σ_A`.

**(iii) Admissibility is one exact linear condition.**

```
        { B(n), N }  =  2 n₁ γ₅ N,        det(γ₅N) ≠ 0.
```

Hence `L(n)` is admissible iff `n₁ = 0`. Writing `n = (0, cos θ, sin θ)` gives `B(n) = B_θ`.

**(iv) Identification.** `−i e^{iθγ₅}γⁿ = −iγⁿ e^{−iθγ₅} = −cos θ (iγⁿ) − sin θ (γⁿγ₅) = B_{θ+π}`. ∎

*Certified (exact, over `ℚ(i)`): C08 (commutant), **C15 (the isotropy identity)**, C09 (real
dimension 2), C10–C12. Witnesses: W01 (400 lines), W02 (50,000-sample stress search).*
**Quantifier repair (audit A7).** Row `V01` of artifact A is retyped from "every off-circle `B`"
to "**every sampled** off-circle `B` (4,000 samples)".

The parameter accounting is `4 → 2 → 1`.

### 6.2 Two lemmas, and the price of A1′

**Lemma 6.1.** The commutant of the tangential generators in `M₄(ℂ)` is `span_ℂ{1, γⁿ, γ₅, γⁿγ₅}`.
*Proof.* `γⁿ` anticommutes with each tangential `γ^a`, hence commutes with every product of two of
them; `γ₅` commutes with all even elements; the four are independent; and by (i) the commutant is
`M₂(ℂ)`, of complex dimension 4. ∎ *(exact: C08)*

**Lemma 6.2 (sufficient, not necessary).** If `[B,Σ] = 0` for the three tangential generators and
`B ∈ 𝔅`, then `L_B` is covariant. The converse fails in general for non-unitary `S`; here the two
conditions happen to select the same set, but that is the content of §6.1, not an automatic
consequence.

**Remark 3.1 (A1′) — corrected (audit A6).** The two tangential boosts alone already give the circle,
because `[Σ^{01}, Σ^{02}] = −2 γ¹γ² ∝ Σ^{12}`. Imposing **only** the rotation about the normal leaves
a **real 4-dimensional** family of admissible boundary conditions *(exact: C13, C14)*. The v2.1 text
called this family "a 2-torus"; **the verifier certified only the real dimension, not the topology**,
so v2.2 states the dimension and drops the topological name. (It is in fact the centraliser of `γ⁵N`
inside the admissible set; identifying it with `U(1)×U(1)` is a one-line argument that has **not**
been carried out here and is left `[열림]`.) Whether tangential boosts must be imposed is A1′.
Section 10 shows that the same assumption at the level of the boundary **action** cuts a real
8-dimensional space of boundary bilinears to 4 *(C37)*.

**Remark 3.0 (convention dependence).** The literal basis `{iγⁿ, γⁿγ₅}` is written for
`η = diag(+,−,−,−)`. Flipping the sign of `γ₅` relabels `θ ↦ −θ`; flipping the orientation of `n`
shifts `θ ↦ θ + π`. The convention-free statement is: *the covariant admissible set is the circle
spanned by the Hermitian normalisations of `γⁿ` and `γⁿγ₅`.*

**Remark 3.2 (what Theorem 3 does not claim).** Covariance supplies the family; nothing here
supplies `θ`.

---

## 7. Theorem 4 — the Riemannian companion problem

Skew-Hermitian Clifford generators `{γ_i,γ_j} = −2δ_{ij}`, interior `x³ > 0`, normal `ν = e₃`,
chirality `γ̄`. Boundary form `N_E := −i ν̸`. Riemannian Pauli triple `(f₁,f₂,f₃) = (γ̄, ν̸γ̄, N_E)`
*(exact: C25)*.

**Theorem 4(a).** The tangential-`Spin(3)`-covariant admissible boundary conditions form the circle
`B_E(θ) = cos θ · f₁ + sin θ · f₂`, of real dimension 1. *(V03, V04.)*

**Theorem 4(b) — `IMPORTED-PROVEN`, not proved here.**
> **Grosse–Uribe–van den Bosch, arXiv:2412.17396, Corollary 5.8:** the generalized infinite-mass
> boundary conditions of their Example 5.3 are regular for `θ ∉ πℤ` and otherwise not regular.

**Mapping claim 4.1 (`DERIVED`).** Their Example 5.3 family `f̃ = e^{iθ}Id` is the circle of Theorem
4(a). The sampled Shapiro–Lopatinski gap is retained **only as a diagnostic** (`X01`, `X02`).

**Remark 4.1 (the two circles are different objects).** The Lorentzian circle contains **no**
chirality-preserving point (`[B_θ,γ₅] ≠ 0` for all `θ`); the Riemannian circle contains two *(V13)*.
`[열림]` — no Wick rotation identifying them is claimed. **This blocks any transport of the
Euclidean heat-kernel / `η`-invariant literature onto the results of Section 13, and Section 13 is
therefore proved directly in the Lorentzian problem, not imported.**

---

## 8. Theorem 5 — the exact chart, the atlas, and the fibration

Dürr–Wipf record, in footnote 3 of hep-th/9412018, a two-parameter general solution of the bag
boundary algebra, `B(t, ξ) = i γ̄ γ_n · exp(−t γ̄ e^{iξγ_n}) · exp(−iξγ_n)`, and then set `ξ = 0` with
no stated reason.

**Theorem 5.** For **every** `(t,ξ) ∈ ℝ²`: `B(t,ξ)² = 1`, `B†γ_n B = −γ_n`, the `+1` eigenspace is
admissible, and its canonical involution is `B_E(Θ)` with

```
        Θ(t, ξ)  =  2 arctan( e^{−t} )  −  ξ       (mod 2π)
```

*Proof.* With `G := iγ_n` and `R(ξ) := e^{−iξG/2}` unitary one has the exact identity
`B(t, ξ) = R(ξ)^{-1} B(t, 0) R(ξ)` *(C28)*; conjugation by `R^{-1}` is the rotation by `−ξ` in the
`(f₁,f₂)` plane and fixes `f₃` *(C29)*; and `B(t,0)` has the exact Bloch vector
`n(t) = (tanh t, sech t, 0)`, so `Θ(t,0) = arccot(sinh t) = 2 arctan(e^{−t})` *(C25)*. ∎

*Certified exactly and universally by C25, C28, C29, **C30**. V05 is a cross-engine corroboration in
floating point, kept because kernel §5.6-2 requires two engines to be compared.*

**(a) The atlas.** `Θ(·,0) : ℝ → (0,π)` is a strictly decreasing real-analytic bijection onto **one
open semicircle**. The second chart is a bijection onto `(π,2π)`; their union is
`S¹ ∖ {two chirality-projection points}` *(V06, V07; C31)*.

**(b) The fibration.** `p(t,ξ) = Θ(t,ξ)` is a surjective submersion `ℝ² → S¹` with `∂Θ/∂ξ = −1`
*(W03)*; the fibre is a countable disjoint union of graphs over `t` *(C31)*.

**(c) There is no global section.** `p ∘ s = id` would force `p_* ∘ s_* = id` on `π₁(S¹) = ℤ`,
impossible through `π₁(ℝ²) = 0`. *(R04.)*

**Corollary 5.1.** BGKS's *strong ellipticity for all real `t`* and GUvdB's *regularity iff
`θ ∉ πℤ`* are the same statement in two charts. No conflict exists.

---

## 9. Proposition 6 — the tangential reflection, and what may be said about `P` and `CP`

Let `S_R := γ₅γ¹`, `S_C = iγ²`, `S_T = iγ¹γ³`.

**Proposition 6 (`PROVEN`).** On the circle of Theorem 3, `R : θ ↦ −θ`, `T : θ ↦ −θ`, `C : θ ↦ θ`,
`C·R·T : θ ↦ θ`. Hence the `R`-invariant covariant admissible boundary conditions are exactly
`θ ∈ πℤ`, i.e. `B = ±iγⁿ`. ∎ *(exact: C18, C19, C20.)*

**Mapping claim 6.1 (`DERIVED-CONDITIONAL`).** Full spatial parity in 3+1 reverses the boundary
normal and the interior/exterior labelling; it is not the transformation computed above. Reading `θ`
as a `P`/`CP`-odd coupling is **imported** (Dürr–Wipf; Balog–Hraskó). Every physical `CP` sentence
here is conditional. *(D02.)*

---

## 10. Theorem 10/11 — the action derives the boundary condition, and derives no more than the circle

### 10.1 The boundary variation

```
    S  =  ∫_M [ (i/2)( ψ̄ γ^μ ∂_μ ψ − (∂_μψ̄) γ^μ ψ ) − m ψ̄ψ ]  +  ∫_{∂M} ψ̄ M ψ ,
    δS|_∂  =  ∮  [ − Im( ψ†N δψ )  +  2 Re( ψ†K δψ ) ],          K := γ⁰M .
```

Requiring this to vanish for **unconstrained** `δψ` gives the two mutually adjoint conditions
`ψ†(K + (i/2)N) = 0` and *(C33)*

```
        ( K − (i/2) N ) ψ |_∂  =  0 .                                             (†)
```

**Proposition 10.** The space of local, gauge-invariant, tangential-Lorentz-scalar, Hermitian,
derivative-free boundary bilinears `ψ̄Mψ` has **real dimension 4** and is carried by the commutant
of Lemma 6.1:

```
        K  =  a γ⁰  +  i b γ⁰γ₅  +  c N  +  d N γ₅ ,        (a,b,c,d) ∈ ℝ⁴ .
```

*(exact: C23, C24.)* Under the normal rotation alone the same space has real dimension **8** *(C37)*.

### 10.2 The well-posedness locus

**Theorem 10.** With `K` as above,

```
        det ( K − (i/2)N )  =  [ ( 4(a² + b² + c² − d²) − 1 − 4ic ) / 4 ]² ,
```

so `(†)` has a nonzero solution space iff

```
        c = 0        and        4( a² + b² − d² ) = 1 ,                            (H)
```

a one-sheeted hyperboloid `H ≅ S¹ × ℝ`. Off `H` the operator is invertible and the only solution is
`ψ|_∂ = 0` *(counterexample W05)*. Parameterising `H` by

```
        χ := arctan(2d) ∈ (−π/2, π/2),                                            [audit A8]
        (a, b) = (2 cos χ)^{-1}(cos Φ, sin Φ),        2d = tan χ,
        K̃ := 2 cos χ · K = cos Φ · γ⁰ + i sin Φ · γ⁰γ₅ + sin χ · Nγ₅ ,
```

— note that `χ` is defined on the **full** range `(−π/2,π/2)` at the point of definition, so the
factor `cos χ` never vanishes and the chart is global on `H` — one has the exact identity

```
        ( K̃ − i cos χ · N ) ( 1 + B_{−(Φ+χ)} )  =  0 .                            (‡)
```

**Theorem 11.** Consequently:

1. the solution space of `(†)` is 2-dimensional and, being `L_{B_θ}`, is automatically
   **`N`-isotropic**: admissibility is a *consequence* of well-posedness, not an extra axiom;
2. the induced boundary condition always lies on the **chiral-bag circle of Theorem 3**, with
   `θ = −(Φ + χ)`;
3. the map `H → S¹` is a surjective submersion with fibre `ℝ`; along every fibre the boundary
   Lagrangian **vanishes on the classical boundary condition it generates**,
   `(1+B_θ)† K (1+B_θ) = 0`.  **Scope correction (audit A9): this is a statement about the
   CLASSICAL boundary condition and the on-shell value of the boundary Lagrangian ONLY. No
   off-shell or quantum equivalence along the fibre is claimed — and Theorem 14.2 below shows the
   fibre is NOT inert for the induced boundary channel.** ∎

*Certified exactly: C33–C37, W05. V08 is the earlier chiral-phase special case, retained.*

**Corollary 10.1 (classical selector exhaustion, proved).** At the level of derivative-free,
Hermitian, gauge-invariant, tangential-Lorentz-scalar boundary terms, the bulk-plus-boundary action
**derives** an admissible boundary condition, and the set of boundary conditions so derived is the
whole chiral-bag circle. **The action does not narrow `θ`.**

**Sanity check against the literature.** At `χ = 0` the boundary Lagrangian is `½ ψ̄ e^{iΦγ₅} ψ` and
`(†)` becomes `iγⁿψ = e^{iΦγ₅}ψ` — the classical chiral-bag surface term, with the MIT bag at
`Φ = 0`. That subfamily is **not new**. What is stated as new is the *classification*.

**Scope (`NC-M67.8`).** Higher-derivative and multi-fermion boundary terms are outside Theorem 10.

---

## 11. Theorem 9 — the surviving parameter is a torsor coordinate

Let `U_A(α) := e^{iαγ₅}`.

**Theorem 9.** `U_A(α)` is unitary, preserves admissibility (`[U_A,N] = 0`) and covariance, and acts
by `U_A(α) B_θ U_A(α)^{-1} = B_{θ + 2α}`. The action is **transitive but not free**: the stabiliser
of every `B_θ` is `{0, π}` and `U_A(π) = −1` acts trivially. The induced action of the **effective
axial group** `Ū(1)_A := U(1)_A / {±1} ≅ ℝ/πℤ` is free and transitive. **The covariant admissible
circle is a torsor for `Ū(1)_A`.** *(exact: C21, C22, C26, C27; independently re-verified in v2.2 as
part of C50.)*

**Corollary 9.1.** If `Ū(1)_A` is a symmetry of the bulk theory then any two points of the circle
are related by a field redefinition: `θ` is unphysical, and acquires meaning only *relative to*
another axial-charged datum.

**Corollary 9.2 (the classical invariant, computed).** Under `ψ = U_A(−α)ψ′`, `θ ↦ θ + 2α` while a
bulk mass term `m ψ̄ e^{iθ_m γ₅} ψ` moves as `θ_m ↦ θ_m − 2α` *(exact: C32; independently
re-derived in v2.2)*. Hence

```
        θ̄  =  θ  +  θ_m .
```

`[열림]`: the quantum invariant requires the axial Jacobian, the bulk vacuum angle and, on a manifold
with boundary, the `η`-invariant / inflow contribution. **Section 13 shows that in the free flat
sector this question has a definite and negative answer; outside it, the item stays open.**

---

## 12. Corollaries 7, 8, 8.2 — what this costs the Z-Spin record channel

Recomputed from `z_* = i^{z_*}` at 60 digits *(V09, V12; independently re-run as V14)*:

| quantity | value | status |
|---|---|---|
| `z_*` | `0.438282936727032111626975163551 + 0.360592471871385485952940526906 i` | `CERTIFIED` |
| `λ = z_* · ln i` | `−0.566417330285464402675433374776 + 0.688453227107702130498767571177 i` | `CERTIFIED` |
| `θ_* = arccos(Re λ)` | `2.17294837955010601348309072071` | `CERTIFIED` |
| `κ_req = |Im λ|/√(1−(Re λ)²) = T₂` | `0.835381287313629904738451598261` | `CERTIFIED` |
| `sin θ_*` | `0.824118564256555945210913525978` | `CERTIFIED` (V15) |
| `M*` | `0.763362818245963536495696055558` | `CERTIFIED` |
| `2T₂` | `1.67076257462725980947690319652` | `CERTIFIED` (V17) |

**Corollary 7 (residual construction freedom) — SCOPE CORRECTED (audit A4).** In the Lorentzian
problem, after Theorems 2, 3 and 10 the admissible boundary condition is determined by exactly one
real **coordinate** `θ`. The M66 identification `a(θ_*) = λ` fixes that coordinate. **Once an axial
frame and a partner datum are fixed, this route has exactly one construction choice, and the
threshold match consumes it.** The v2.1 wording ("the physical freedom is consumed") is **withdrawn**:
by Theorem 9, `θ` is a torsor coordinate, not a physical invariant, so what is consumed is a
*coordinate representative*, not a physical degree of freedom. Epistemic status is lowered
`DERIVED → DERIVED-CONDITIONAL`. **Section 15 supersedes this corollary in the presence of a surface
mode**, where the count changes again.

**Corollary 8 (`DERIVED`; physical reading `DERIVED-CONDITIONAL`).** `Im λ ≠ 0`, so `sin θ_* ≠ 0`,
so `θ_* ∉ πℤ`; the carrying boundary condition is odd under the tangential reflection and under time
reversal. Conversely, at `θ ∈ πℤ` we have `a(θ) = ±1 ∈ ℝ`, so `a = λ` is **unsatisfiable** *(V10,
V11)*. **This corollary is what Theorem 13 collides with.**

**Corollary 8.1 (pre-registered kill test).** *Does reflection positivity for a free fermionic slab
with a chiral-bag boundary term require `θ ∈ πℤ`?* Prior-art sweep: `NOT FOUND IN QUERY SCOPE` in
both directions. Prerequisite: the Lorentzian/Riemannian reconstruction of Remark 4.1.

**Corollary 8.2 — DISCHARGED IN PART (see Theorem 12.3 and C50).** The M66 relation
`a(θ) = cos θ + iκ sin θ` and the target `a(θ_*) = λ` are written in `θ` alone and are therefore not
axially invariant. v2.2 discharges the structural half of the obligation: **`κ` is axially invariant
and `θ` is not**, so the invariant restatement is

```
        κ  =  T₂        (invariant content)      and        cos θ̄_*  =  Re λ        (chart content),
```

with `θ̄ = θ + θ_m`. What remains open is only whether `ZS-M66` §5.2 uses this sign convention for
`θ_m` (a mapping obligation) and whether the quantum invariant differs from `θ̄` outside the free
sector.

---

## 13. Theorems 12–13 — the `θ̄`-funnel and the bare quantum selection no-go

> **Round-4 repair notice.** In v2.2 this section reached its conclusion from the **continuum**
> scattering phase alone, while §15 of the same manuscript exhibited a **surface bound state**.
> That was a genuine gap: a discrete branch contributes to the spectral shift, and continuum
> monotonicity does not by itself fix the sign of the full spectral derivative. §13.2 below now
> constructs the object that contains **both** and shows the sign survives. The verdict of v2.2 is
> restored, but on a different and correct basis, and its scope is narrower (A5).

Everything here is proved **directly in the Lorentzian half-space problem**, because Remark 4.1
forbids importing Euclidean results. Assumptions **A1–A4** are in force.

### 13.1 The exact reflection determinant, derived universally

Fix an energy `E`, a transverse momentum `k_⊥` and `q := (E² − m² − k_⊥²)^{1/2} > 0`. Write the
positive-energy on-shell spinors in the Dirac representation as `u = (χ, (σ·k)/(E+m) χ)`, `k =
(k_⊥, ±q)`. Let `P_- = ½(1 − B_{θ̄})`; a basis of `ran P_-` is

```
        g₁ = ( iC, 0, −(1+S), 0 )ᵀ ,     g₂ = ( 0, iC, 0, (1−S) )ᵀ ,     C := cos θ̄, S := sin θ̄,
```

verified to satisfy `(B+1)g_i = 0` modulo `C²+S² = 1`. The reflection matrix `R` solves
`P_-(u_in c + u_out Rc) = 0`, so with `M_• := (g_i† u_{•,j})` one has `R = −M_out^{-1}M_in` and
`det R = det M_in / det M_out`, a quantity independent of the basis chosen for `ran P_-`.

**Theorem 12 (the `θ̄`-funnel; UNIVERSAL).** Over the free symbols `(m, E, q, k₁, C, S)`, modulo
only the on-shell relation `E² = m² + k₁² + q²` and `C² + S² = 1`,

```
        ┌──────────────────────────────────────────────────────────┐
        │   det R( θ̄ )  =  ( i m cos θ̄  −  q ) / ( i m cos θ̄  +  q ) │
        └──────────────────────────────────────────────────────────┘
```

and `|det R| = 1`. **There is no explicit dependence on the transverse momentum beyond the normal
momentum `q`.** *(This is the wording the round-4 audit correctly demanded: at fixed `E`, `q` itself
depends on `k_⊥`; the content of the theorem is that `k_⊥` enters only through `q`.)*

*Proof.* Direct computation of `det M_in` and `det M_out` from the explicit spinors. With
`a = (E+m)^{-1}`,

```
    det M_in  = C[ −C − 2iaq + a²C(q²+k₁²) ] ,     det M_out = C[ −C + 2iaq + a²C(q²+k₁²) ] ,
```

and `a²(q²+k₁²) = (E−m)/(E+m)`, so each bracket collapses to `∓(2mC ± 2iq)/(E+m)`, giving the boxed
form. ∎ *(**C52**, exact, universal; independently cross-checked by a different construction —
nullspaces rather than explicit spinors — at four exact rational on-shell points, **C44**; column
swap invariance, **R09**.)*

**Corollary 12.1 (the massless sector is exactly `θ̄`-blind).** At `m = 0`, `det R ≡ −1` and
`∂_C det R ≡ 0` *(**C45**)*.

**Corollary 12.2 (funnel).** The boundary enters every spectral quantity of the free half-space
problem only through `A := m cos θ̄`.

**Corollary 12.3 (`κ` is the axial-invariant half of the identification).** `e^{iαγ₅}` preserves
`E₊`, restricts to `e^{iαJ_E}` and **commutes with `J_E`**; hence `κ = Tr(ρJ_E)` is axially
invariant while `θ ↦ θ + 2α` *(**C50**)*. This discharges the structural half of Corollary 8.2.

### 13.2 The full spectral object: the Jost factor contains the bound state

**Lemma 13.1 (the boundary Jost factor).** Continue `q → iκ` (so that `e^{iqx³} = e^{−κx³}` decays).
The denominator of `det R` becomes `i(κ + A)`, whose zero is at

```
        κ  =  −A  =  −m cos θ̄ ,
```

which is **exactly** the surface-mode localisation rate of Theorem 15. Hence the boundary Jost
factor is `κ + A`, and the single function `log(κ + A)` carries the continuum phase shift (on the
cut) **and** the bound state (as its zero). *(**C53**.)*

**Definition 13.2.** Writing the Euclidean boundary momentum as `p` (one Euclidean time plus two
transverse directions) and `κ(p) = (p² + m²)^{1/2}`, the `θ̄`-dependent part of the one-loop boundary
effective action per unit area is

```
        Γ(A) / Area  =  ½ ∫ d³p/(2π)³  log[ ( κ(p) + A ) / κ(p) ] ,        A = m cos θ̄ ∈ [−m, m].
```

*Status `DERIVED`: this is the standard Jost/functional-determinant reduction, with the Jost factor
identified by Lemma 13.1. The identification of the prefactor and measure is not separately
certified here; nothing below depends on them, because every statement is about the **sign** of an
`A`-derivative of a positive-measure integral.*

**Theorem 13 (bare quantum selection fails in the free flat sector).**

*(a) Full-spectral positivity — the round-4 repair.* Pointwise,

```
        ∂_A log( κ(p) + A )  =  1 / ( κ(p) + A ) ,       κ(p) + A  ≥  m − |A|  ≥  0
```

for `|A| ≤ m`, with equality only at `p = 0, A = −m` (i.e. `θ̄ = π`, where the surface gap
`m|sin θ̄|` closes). The integrand is therefore **strictly positive**, so `∂_AΓ > 0` with a fixed
sign. **Including the surface bound state does not reverse the monotonicity obtained from the
continuum phase shift** *(**C54**; numerically corroborated at six values of `A`, including
`A = Re λ`, in **V18**)*.

*(b) Stationary points at the bare level.* By Corollary 12.2, `∂_{θ̄}Γ = −m sin θ̄ · Γ′(A)`. By (a),
`Γ′ ≠ 0`, so under **A5** the only stationary points are `θ̄ ∈ πℤ`.

*(c) The scheme ambiguity is exactly a cubic in `A`.* The `k`-th `A`-derivative of the integrand
falls off like `p^{-k}`, so with the measure `p²dp` the divergences terminate at `k = 3`
(quadratic, linear, logarithmic) and every derivative of order `≥ 4` is finite. Hence the
renormalisation freedom of `Γ(A)` is exactly a cubic polynomial in `A`, and

```
        ∂_A⁴ Γ  =  −3 ∫ d³p/(2π)³ ( κ(p) + A )^{-4}   <  0
```

is finite, scheme-independent and strictly negative *(**C55**, **V18**)*.

*(d) Collision with the target, and what is NOT claimed.* By Corollary 8, `a(θ) = ±1 ∈ ℝ` at
`θ ∈ πℤ` while `λ ∉ ℝ`. Hence under A5 the stationary points of the free-flat boundary effective
action and the `ZS-M66` identification are **mutually exclusive**. **Outside A5 no such claim is
made.** A counterterm linear in `A` already suffices to make `∂_AΓ` vanish at `A = Re λ` *(witness
**W08**)*. ∎

**Verdict (narrowed relative to v2.2).**

```
  [검증됨]  the BARE free-flat boundary effective action, bound state included, is strictly
            monotone in A and therefore selects no point of the circle other than θ̄ ∈ πℤ,
            which is incompatible with a(θ̄_*) = λ.
  [열림]    whether some independent principle fixes the three boundary counterterms so as to
            produce an off-πℤ stationary point.  v2.2 called this "parameter fitting"; that
            verdict is WITHDRAWN.  A counterterm can be fixed by symmetry, by a UV completion,
            by an independent observable or by an upstream action, all of which are target-blind.
```

**Corollary 13.1 (what survives as a target-blind selector).** Strictly: **(i)** curvature (relax
A1); **(ii)** a gauge or axial background, so that the Fujikawa Jacobian and the boundary
`η`/inflow terms are non-trivial (relax A4); **(iii)** an interacting sector (relax A4); **(iv)** an
external environment (§14); **(v)** an independent determination of the boundary counterterms
(relax A5). Item (v) is new in v2.3 and is a direct consequence of the round-4 audit.

**Consistency with the literature.** Esposito–Kirsten find `ζ(0)` `θ`-independent for **massless**
spinors on the Euclidean ball, consistent with Corollary 12.1. Ivanov–Vassilevich study the
`η`-invariant for local (including chiral-bag) boundary conditions. **No result is transported
across Remark 4.1.** `[검증됨]` for the Ivanov–Vassilevich bibliographic record (primary listing);
`[열림]` for the detailed content of the chiral-bag anomaly computations, not read from primary text.

---

## 14. Theorem 14 — what the boundary datum supplies, and the unitary-conjugation no-go

> **Round-4 scope repair.** v2.2 wrote that "three of the four declared construction choices move
> from declared to derived" and that "any boundary map induced by the M67 boundary datum alone is
> `Ad_R`". Both were too strong. `W : E₊ → E₋` and `Φ : ℬ(E₊) → ℬ(E₊)` are objects of **different
> type**, and integrating out bulk degrees of freedom need not produce a unitary conjugation. The
> statements below are re-typed accordingly, and the gap is registered as `NC-M67.12` — it is
> precisely the open construction that `F-M66.15` demands.

### 14.1 What is derived, and what is still declared

**Theorem 14.1 (derived: the Hilbert carrier, the grading, the static graph unitary).**

1. The spectral split of `N` supplies `E₊` (`dim = 2`), `N|_{E₊} = 1`, and `J_E = γ₅|_{E₊} =
   diag(−1,+1)` with `tr J_E = 0`, `J_E² = 1` *(**C38**, universal)*.
2. Of the four generators of `K`, `γ⁰` and `iγ⁰γ₅` have a **vanishing on-carrier block** and connect
   `E₊ ↔ E₋` only; `N|_{E₊} = 1`, `Nγ₅|_{E₊} = J_E` *(**C39**, universal)*.
3. The covariant admissible boundary condition is the **graph of the unitary**
   `W(θ) = i·e^{−iθ J_E} : E₊ → E₋`, exactly and symbolically in `θ` *(**C41**, universal)*. Hence
   `ZS-M66` §5.2's declared `U_θ = e^{iθJ_E}` is derived from the boundary form, up to the constant
   phase `i` and the orientation convention.

**What is NOT derived (`NC-M67.12`).** The passage from the Hilbert carrier `E₊` to an
**operator-state** description — adopting `ℬ(E₊)` as the physical state carrier, reading `ρ` as the
physical boundary state, and identifying `Tr(ρU_θ)` as the **record multiplier** — remains a
declared mapping. `F-M66.15` asks precisely for that layer to come from the action, together with a
positive/CPTP dynamics and a faithful mixing source. v2.2's phrasing is withdrawn; the accurate
statement is: *the two-dimensional Hilbert carrier, its grading and the static graph unitary are
boundary-form derived; the operator-state interpretation and the dynamics remain OPEN.*

### 14.2 The unitary-conjugation no-go

**Theorem 14.2 (no-go for the unitary-conjugation class).** Let `Φ` be a positive trace-preserving
map on the carrier of the form `Φ = Ad_R` with `R` unitary. Then

1. `Φ` is **unital** *(**C42**)*;
2. the fixed-point set of `Ad_R` on `2×2` matrices contains `span{1, n̂·σ}`, of real dimension `≥ 2`,
   so `Ad_R` **never** has a unique stationary state on `ℂ²` *(**C42**)*;
3. if a positive trace-preserving `Φ` on this carrier is unital **and** has a unique stationary
   state, then `ρ_* = ½` and `κ = tr(J_E)/2 = 0` *(**C43**; `ZS-D3` instantiated on the derived
   carrier)*.

Hence **no map in the unitary-conjugation class satisfies `F-M66.15`.** ∎

**Remark 14.1 (the type gap, stated as an open problem).** The boundary condition slaves `E₋` to
`E₊` by the unitary `W`, so the *static boundary datum* carries no independent second state. It does
**not** follow that a boundary map obtained by integrating out the bulk lies in the
unitary-conjugation class: eliminating bulk degrees of freedom from a globally unitary Dirac
dynamics can and generally does produce a non-unitary reduced map. **Constructing `Φ_∂` from the
bulk-plus-boundary action, and determining whether it escapes the class of Theorem 14.2, is the
central open problem of this route.** `[열림]`

**Theorem 14.3 (the unique X-odd on-carrier operator — algebraic).** On the carrier,
`K|_{E₊} = c·1 + d·J_E`. Under the flip family `𝔛(J_E) = {cos n·σ_x + sin n·σ_y}` — Hermitian,
involutive, and satisfying `X J_E X = −J_E` for symbolic `n` *(**C40**)* — the identity is X-even and
`J_E` is X-odd. Theorem 10 forces `c = 0`. Therefore the **unique** X-odd on-carrier operator the
derivative-free covariant class can supply is `d·J_E`, with `d = ½ tan χ` the Theorem-10 fibre
coordinate *(**C51**)*. ∎

**Scope note (round-4).** Theorem 14.3 is a statement about **operators**, not about any dynamical
map. Reading it as "the first-order flip defect is `𝔇^{(1)}(ρ) = −2i d⟨B⟩[J_E,ρ]`" requires a
collision/step model in which `d·J_E` appears as the system operator of a system–environment
coupling; that mapping is an **obligation**, not a result. `[열림]`

**Corollary 14.1 (the fibre is not inert).** Theorem 11(3) says the boundary Lagrangian vanishes on
the classical boundary condition along the fibre; Theorem 14.3 says the same fibre coordinate
carries the only X-odd on-carrier operator. "On-shell trivial" must therefore never be read as
"physically inert".

**Corollary 14.2 (the minimal missing object, named).** To close `F-M66.15` one must exhibit

```
        Φ_∂ : ℬ(E₊) → ℬ(E₊)      that is simultaneously
        action-derived · positive/CPTP · sufficiently non-unital (ZS-D3)
        · flip-ORBIT non-covariant, 𝔇_min = inf_{X∈𝔛(J_E)} ‖Φ − Ad_X Φ Ad_X‖_{1→1} > 0 (ZS-D2)
        · possessing a UNIQUE FAITHFUL stationary state with κ = Tr(ρ_*J_E) ≠ 0,
```

together with the **independent external environment state** that produces it, and satisfying the
floor `𝔇_min ≥ 2(1−η)T₂`, `2T₂ = 1.67076257462725980947690319652` *(V17)*.

---

## 15. Theorem 15 — the chiral-bag surface mode (universal), and the kinematic consequence

### 15.1 The mode

**Theorem 15 (UNIVERSAL).** For `cos θ̄ < 0` the chiral-bag wall carries a boundary-localised
solution `ψ = u·e^{−κ_loc x³}e^{−iEt + ik_⊥·x_⊥}` with

```
        κ_loc  =  − m cos θ̄  =  m|cos θ̄| ,        E(k_⊥) = ( k_⊥² + m² sin²θ̄ )^{1/2} ,
```

localisation length `1/κ_loc` and gap `m|sin θ̄|`. Modulo the ideal `⟨S²+C²−1, E²−k₁²−m²S²⟩` and over
the free symbols `(m, k₁, E, C, S)`, the boundary condition is satisfied and

```
        ⟨u|γ₅|u⟩ = 0 ,   ⟨u|N|u⟩ = 0 ,   |P₊u|² = ½|u|² ,
        ┌────────────────────────────────────────────────────────────────┐
        │   κ_bs := Tr( ρ₊ J_E )  =  m sin θ̄ / E(k_⊥)  =  ( 1 − v² )^{1/2}   │
        └────────────────────────────────────────────────────────────────┘
        κ_bs² + v² = 1 ,    v = dE/dk_⊥ ,      purity( ρ₊ ) = 1 .
```

*(**C48**, universal Groebner reduction — this replaces the three sampled rational angle families of
v2.2, per round-4 finding A15; **C49**.)* ∎

**Localisation test, fail-closed (round-4 finding A14).** v2.2 obtained the localisation rate by
eliminating variables and accepted the root list `{−m cos θ̄, k₁}` without resubstitution. `κ = k₁`
is **spurious**: resubstituted into the original rank condition it leaves the nonzero minor
`4Cm(Cm + k₁)`, so the rank does **not** drop and there is no nonzero common solution. `v2.3`
resubstitutes every candidate and rejects it; only `κ_loc = −m cos θ̄` survives *(**C47**)*. The
spurious root appeared because `4Cm(Cm+k₁)` vanishes on the coincidence locus `k₁ = κ_loc`, which
the elimination could not distinguish from a solution branch.

### 15.2 What this does to the Z-Spin identification

**Corollary 15.1 (target-blind existence check — passed).** The mode exists iff `cos θ̄ < 0`, and the
`ZS-M66` target forces `cos θ̄_* = Re λ = −0.566417330285464402675…< 0`. **The check could have
failed and did not** *(**V15**)*.

**Corollary 15.2 (kinematic consequence; `DERIVED-CONDITIONAL`).** `κ` is no longer a free
parameter of the boundary state: it is a computed function of the mode. Imposing `κ_bs = T₂` gives

```
        |v_*|          =  ( 1 − T₂² )^{1/2}          =  0.549670905912094390502195051221
        |k_⊥|_* / m    =  sin θ̄_* (1 − T₂²)^{1/2}/T₂ =  0.542260168707617546979016700257
        gap / m        =  |sin θ̄_*|                  =  0.824118564256555945210913525978
        κ_loc / m      =  |cos θ̄_*|                  =  0.566417330285464402675433374776
```

**Round-4 scope repair.** v2.2 called this a *prediction*. It is not one yet. Nothing in this paper
selects the surface branch as **the** carrier, selects a transverse momentum, shows the resulting
state is stationary under any dynamics, or names an environment. Until an action-level principle
does all four **before** `λ` is consulted, this is a `DERIVED-CONDITIONAL` **kinematic consequence**
of accepting the identification, not an independent prediction in the Mission's sense. What has
genuinely improved over v2.1 is structural: the identification now constrains a second, computable
quantity instead of being absorbed entirely into one coordinate.

**Corollary 15.3 (the residual obstruction).** The single-mode carrier state is **pure**, hence not
faithful, so `ZS-M66` Thm 3.7 / Q12 are unsatisfied *(**W06**)*. A `k_⊥`-ensemble makes it mixed but
its `κ` is cutoff-dependent, behaving like `2/Λ` *(**W07**)*. The mixing must come from the object
named in Corollary 14.2. ∎

**Non-claim `NC-M67.9`.** Theorem 15 supplies a *state*, not a *dynamics*.

---

## 16. Theorems 19–21 — the boundary symmetry group on the carrier **(new in v2.4)**

This section closes the *lift* half of `NC-M67.12` and identifies exactly why the *map* half
resists. Assumptions A1–A4 are in force; **A6** is introduced and shown to be unavoidable.

### 16.1 The operator-state lift is action-derived

**Theorem 19 (lift).** Every boundary value lies in `L_θ` (Theorem 1), and by Theorem 14.1 `L_θ` is
the graph of `W(θ) : E₊ → E₋`. Hence the restriction of the carrier projector to the boundary
subspace,

```
        P₊|_{L_θ} : L_θ ⟶ E₊ ,          det ( V₊† Ψ_θ ) = 1 ,
```

is a **linear isomorphism** *(**C61**, universal)*. Consequently, for any state of the field, the
boundary two-point function projected onto `E₊`,

```
        ρ₊  ∝  P₊ ⟨ψ|_∂ ψ|_∂† ⟩ P₊  =  Σ_modes n_mode · v_mode v_mode† ,     v_mode := P₊ψ_mode(0),
```

is a well-defined positive operator on the carrier. ∎

**Corollary 19.1.** `ZS-M66`'s **operator-state lift is not a construction choice.** It is the
projection of the boundary Wightman function through an isomorphism that the boundary condition
itself supplies. Of the four items `ZS-M66` Q11 recorded as declared, three — the Hilbert carrier
with its grading (Thm 14.1), the multiplier operator `U_θ` (Thm 14.1), and the operator-state lift
(here) — are now derived. **What remains declared is only the dynamics: a positive/CPTP map with a
unique faithful stationary state.**

*(This is the v2.4 replacement for the claim v2.2 made and v2.3 withdrew. The difference is that
the isomorphism `P₊|_{L_θ}` is now computed rather than assumed.)*

### 16.2 The residual rotation derives the one-parameter state family

**Theorem 20 (rotation).** The rotation about the normal, `R(φ) = exp(φ γ¹γ²/2)`, commutes with `N`
and with `γ₅`, is unitary, and induces on the carrier

```
        R(φ)|_{E₊}  =  diag( e^{iφ/2}, e^{−iφ/2} )  =  e^{−iφ J_E/2} ,        [ R|_{E₊}, J_E ] = 0 ,
```

whose invariant states are exactly `r_x = r_y = 0`, i.e. the one-parameter family
`ρ = ½(1 + r_z σ_z)` *(**C60**, universal)*. ∎

**Corollary 20.1.** Once a boundary rest frame is chosen (A6), `ZS-M66`'s **one-parameter boundary
state, coordinatised by `κ = Tr(ρJ_E)` alone, is derived from residual rotational symmetry**, not
declared. This also explains why `a(θ) = cos θ + iκ sin θ` has exactly the M66 form: it is
`Tr(ρ U_θ)` evaluated on the rotation-invariant family.

### 16.3 The boost obstruction — the central result of v2.4

**Theorem 21 (boost obstruction).**

*(a) The carrier is not boost-invariant.* `[γ⁰γ¹, N] ≠ 0`, so the tangential boost
`S(ζ) = exp(ζ γ⁰γ¹/2)` does **not** preserve `E₊`, even though it preserves the boundary subspace
`L_θ` (Theorem 3) and is not unitary *(**C56**, universal)*.

*(b) The induced carrier map is a Bloch boost generated by a flip element.*

```
        ┌─────────────────────────────────────────────────────────────────────────┐
        │  G(ζ) = cosh(ζ/2)·1 + sinh(ζ/2)·X_θ ,   X_θ = −sin θ·σ_x + cos θ·σ_y ,   │
        │  det G = 1 ,  G = G† ,  G not unitary ,  [G, J_E] ≠ 0 ,                  │
        │  X_θ ∈ 𝔛(J_E)  and  { X_θ , J_E } = 0 .                                  │
        └─────────────────────────────────────────────────────────────────────────┘
```

*(**C57**, **C58**, universal.)* `X_θ` is the flip element of index `n = θ + π/2`.

*(c) The transformation law and the obstruction.* With `ρ = ½(1 + r⃗·σ⃗)` and
`m̂_θ = (−sin θ, cos θ, 0)`,

```
        κ_out  =  κ_in / ( cosh ζ  +  sinh ζ · ( m̂_θ · r⃗ ) ) .
```

Invariance for all `ζ` forces `cosh ζ + c·sinh ζ ≡ 1`, impossible because the second derivative at
`ζ = 0` equals `1`. Therefore

```
        ┌───────────────────────────────────────────────────────────────┐
        │  every tangential-boost-invariant boundary state has κ = 0.   │
        └───────────────────────────────────────────────────────────────┘
```

*(**C59**, universal.)* ∎

**Corollary 21.1 (a third necessary condition, `(N-boost)`).** `F-M66.15` now requires **three**
independent structural conditions on the environment coupling, not two:

```
   (N-uni)    non-unitality               Tr(ρ_E [B_a,B_b]) ≠ 0            ZS-D3
   (N-cov)    flip-ORBIT non-covariance   𝔇_min = inf_{X∈𝔛(J_E)} ‖Φ−Ad_XΦAd_X‖ > 0   ZS-D2
   (N-boost)  breaking of the tangential boost symmetry preserved by the boundary condition
```

**and `(N-cov)` and `(N-boost)` are the same structure**, because the boost generator `X_θ` is an
element of the flip family. This is the first place in the M60–M67 sequence where assumption `A1′`
and debt `F-M66.16` are identified with one another.

**Corollary 21.2 (the vacuum cannot do it).** A Lorentz-invariant boundary state — in particular the
free vacuum — is boost-invariant, hence has `κ = 0`. The `2/Λ` falloff of the band-averaged `κ`
found in `W07` is therefore **not a cutoff artefact**: it is the boost orbit average converging to
an invariant state. The environment must supply a **rest frame**, not merely mixing *(witness
**W09**: the surface mode at `|k_⊥|_*` reaches `κ = T₂` exactly, while boost-invariant states give
`0`)*.

**Corollary 21.3 (A6 is mandatory).** Since `E₊` and `J_E` are defined through `N = γ⁰γⁿ`, every
statement about `κ` is relative to a boundary rest frame. **A6 cannot be dropped**, and Theorem 21
shows the cost of dropping it is `κ = 0`.

### 16.4 External corroboration

Two independent external results support this section, and one of them supports §13.

1. **Peres–Scudo–Terno**, *Quantum entropy and special relativity*, PRL **88**, 230402 (2002),
   arXiv:quant-ph/0203033. For a single free spin-½ particle, **the reduced spin density matrix is
   not covariant under Lorentz transformations and the spin entropy is not a relativistic scalar**.
   Theorem 21 is the boundary-carrier instance of exactly this phenomenon, sharpened to a definite
   consequence: the non-covariance is not merely a nuisance, it **annihilates `κ`** on the invariant
   states. The subsequent critical literature (Comments and Replies, and later work arguing that a
   frame-independent reduced spin state cannot be consistently defined at all) makes A6 an
   **obligation** rather than a convenience. `[검증됨]` for the PSTh statement (abstract read from
   primary listing); `[열림]` for the later reduced-spin-covariance debate, which was not read from
   primary text here and is not relied upon.
2. **Edge states and the `η` invariant**, arXiv:2305.13606 = Phys. Lett. B **844** (2023) 138098.
   For chiral-bag boundary conditions with a real chiral parameter, **the smooth part of `η(0,H)`
   does not depend on that parameter**, and the parameter dependence of the spectral asymmetry sits
   in the **edge states**; the paper also notes that the earlier `η`-inflow analyses covered only
   massless operators *admitting no boundary states*, which is precisely the case our Corollary 12.1
   shows to be `θ̄`-blind. This is an **independent external corroboration of Theorem 13's funnel**:
   the smooth/bulk quantum contribution does not select the angle. It also locates where a selector
   could still live — the edge sector, i.e. our Theorem 15. `[검증됨]` for the two quoted findings
   (read from the primary PDF text this session); `[열림]` for the mapping between that paper's
   hyperbolic parameter `τ` and our `θ̄` (its edge decay rate `|λ sinh τ + m cosh τ|` is
   energy-dependent while ours, `m|cos θ̄|`, is not — the two setups differ in dimension and in
   whether a Hamiltonian or a Euclidean operator is used, and no identification is claimed).
3. **Edge States: Topological Insulators, Superconductors and QCD Chiral Bags**, arXiv:1308.5635 =
   JHEP **12** (2013) 073, exhibits an explicit chiral-bag edge spinor with components
   `(e^{θ/2}, −i e^{−θ/2})` on the half-line. The *existence* and the *closed-form* character of
   chiral-bag edge spinors are therefore prior art and **not claimed**; what §15 retains as
   sweep-limited novelty is the 3+1 polarisation identity `κ_bs = m sin θ̄/E = √(1−v²)` with
   transverse momentum. `[열림]` for the chart mapping.

---

## 17. F-M66.17 — the target-blind arc reduction, and what is still missing

**Theorem 22 (arc reduction).** Two target-blind filters act on the circle:

```
   (i)  a boundary-LOCALISED carrier exists  ⟺  cos θ̄ < 0                       (Thm 15, C47)
   (ii) Shapiro-Lopatinski regularity fails exactly at θ̄ ∈ πℤ    (GUvdB Cor. 5.8, IMPORTED)
```

Neither filter mentions `λ`, `κ`, `T₂` or any Z-Spin datum. Together they cut

```
        S¹   ⟶   the open arc   ( π/2 , 3π/2 ) ∖ { π } .
```

*(**C62**.)* The `ZS-M66` target `θ̄_* = arccos(Re λ) = 2.17294837955010601348…` lies inside it
*(**V19**)* — a check that could have failed. ∎

**What this does and does not do.** `F-M66.17` asked for a selection principle taking `U(2)` to a
point. The record is now:

```
   U(2)  →(Thm 3, covariance)→  S¹  →(Thm 22, localisation + regularity)→  open arc  →  ?
   real dim 4                   real dim 1                                 real dim 1
```

The reduction from `S¹` to an arc is **topological, not dimensional**: it removes a closed half of
the circle and one further point but leaves a one-parameter family. `F-M66.17` therefore remains
**OPEN**. What has changed is that the surviving region is now characterised by two physical
conditions rather than by nothing, and that the target passes both.

**Why the remaining freedom cannot be removed by symmetry.** Theorems 20 and 21 close this off
sharply. The full symmetry available at the boundary is `Spin(1,2)↑` = (two boosts) ⋉ (one
rotation). The rotation acts unitarily and commutes with `J_E`, so it constrains the *state* (to the
`κ` family) but not `θ̄`. The boosts act non-unitarily with a grading-odd generator, so they do not
constrain `θ̄` either — they annihilate `κ`. **No further symmetry argument inside A1–A4 can select a
point.** By Corollary 13.1 the surviving routes are curvature, a gauge/axial background,
interactions, an environment, or an independent determination of the boundary counterterms — and by
the external result of §16.4(2), whichever route is taken, the smooth part of the quantum
contribution is angle-blind and the selector must come from the **edge sector**.

**Ranked next step for F-M66.17.** Compute the edge-sector contribution to the spectral asymmetry
`η` for the 3+1 chiral-bag wall at nonzero mass, following §16.4(2)'s decomposition, and ask whether
`∂_{θ̄} η_edge` is nonzero and whether the resulting boundary term is target-blind. Our Theorem 15
supplies exactly the input that computation needs — the edge dispersion `E = √(k_⊥²+m²sin²θ̄)` and
the polarisation `κ_bs = m sin θ̄/E`. `[열림]`

---

## 18. Theorems 23–26 — the boundary polarisation law, charge conjugation, and the type of the missing dynamics **(new in v2.5)**

This section attacks the two items v2.4 ranked first and second — the **map half of `NC-M67.12`**
(construct `Φ_∂`) and the **edge-sector `η`** — and closes both *as posed*: the first as a type
error under A4 (no autonomous map exists; the correct object is named and derived), the second as
a Lorentzian identity (`η ≡ 0` by charge conjugation). What survives is one universal law that
neither v2.3 nor v2.4 had: the carrier polarisation of **every** stationary mode of the half-space
problem is `κ = m sin θ̄ / E`. Assumptions A1–A4 and A6 are in force throughout.

### 18.0 Breakthrough record (route cards, frozen before external collision)

```text
FREEZE
  TARGET:        (a) NC-M67.12 map half; (b) F-M66.17 via edge-sector eta
  EXACT RESIDUE: (a) a CPTP Phi_partial on B(E+) with unique faithful kappa != 0 fixed point,
                     action-derived, non-unital, flip/boost-breaking
                 (b) d/dthetabar eta_edge for the 3+1 massive chiral-bag wall
  HARD:          Dirac algebra; N = gamma0 gamma^n; chiral-bag circle (Thm 3); carrier/grading
                 (Thm 14.1); lift isomorphism (Thm 19); det R (Thm 12); surface mode (Thm 15);
                 boost obstruction (Thm 21); Gamma(A) monotone (Thm 13)
  SOFT:          A4 (free bulk); A6 (rest frame); the notion of "the carrier state" of a
                 many-body state; Lorentzian-vs-Euclidean formulation of eta
  UNKNOWN:       whether the free bulk induces ANY autonomous map on the carrier
  FORBIDDEN:     fitted environments; reading lambda before fixing the construction;
                 transporting Euclidean eta results across Remark 4.1
  SUCCESS OBSERVABLE: (a) an explicit map or an explicit obstruction to its existence;
                      (b) an exact sign of d/dthetabar eta_edge

ROUTE-1 / B12 QUESTION REPAIR + B04 LAYER SPLIT  ("is Phi_partial even well-typed under A4?")
  MINIMAL CONSTRUCTION: two exact continuum modes at equal k_perp, polarisations chosen through
                        the invertible boundary map so that rho_+(0) coincide; compare rho_+(t)
  DECISIVE KILL TEST:   rho_+(t) equal for all such pairs (then a map may exist)  -> FAILED,
                        the pair differs (W10): NO autonomous map under A4
  MATURITY: constructed, collided, verified          STATUS: BT-REFORMULATED

ROUTE-2 / B13 UNIVERSALIZATION + B11 CANCELLATION  ("what is kappa of an arbitrary stationary mode?")
  MINIMAL CONSTRUCTION: polarisation-summed carrier operator T_E T_E^dag of a reflected mode
  DECISIVE KILL TEST:   kappa depends on q or k_perp  -> FAILED: kappa = m S/E exactly (C63)
  MATURITY: constructed, verified                    STATUS: BT-ROUTE (universal law)

ROUTE-3 / B10 INVARIANTIZATION  ("which symmetry controls eta_edge?")
  MINIMAL CONSTRUCTION: antiunitary C = i gamma2 K; test [C,H]_+ = 0 and C L_theta = L_theta
  DECISIVE KILL TEST:   C fails to preserve some L_theta or some mass phase -> PASSED both (C65)
  MATURITY: constructed, verified                    STATUS: BT-NO-GO-MAP (eta == 0)

ROUTE-4 / B15 QUOTIENT  ("are (N-uni),(N-cov),(N-boost) independent?")
  MINIMAL CONSTRUCTION: Tr(X rho X J_E) = -Tr(rho J_E) for symbolic flip X and state rho
  DECISIVE KILL TEST:   some flip-covariant map with unique kappa != 0 fixed point -> impossible (C67)
  MATURITY: constructed, verified                    STATUS: BT-REFORMULATED (three -> one)

NO-GO EMISSION GATE (kernel §5.5) for Theorems 24 and 25:
  SIGN        gate asked: "does the edge spectral asymmetry select a point?"  computed: eta(H)
              itself, which is the positive answer's carrier.  PASS
  QUANTIFIER  universal over thetabar, theta_m, k_perp, E (free symbols / ideal).  PASS
  SOURCE      external to the construction: a symmetry of the Dirac equation with the chiral-bag
              condition, not a failure of our ansatz.  PASS
  VALUE       erases the last spectral route inside A1–A5 -> publishable No-Go Map.
  For Theorem 25 (no autonomous map) SOURCE is internal (our framing), so per kernel §5.5 the
  output is a REFRAMING, and the object was actually built (the pushforward) before emission.
```

### 18.1 Theorem 23 — the boundary polarisation law (universal)

Let `E > 0`, `k_⊥`, `q = (E² − m² − k_⊥²)^{1/2} > 0`, and let `c ∈ ℂ²` label the two polarisations
of the incoming positive-energy spinor. The reflected stationary mode has boundary value
`ψ_c(0) = (U_in + U_out R) c` with `R` the reflection matrix of Theorem 12, and by Theorem 19 its
carrier vector is `v_c = P₊ψ_c(0) = T_E c`.

**Theorem 23 (boundary polarisation law).** Over the free symbols `(m, E, q, k₁, C, S)`, modulo
the on-shell relation and `C² + S² = 1`:

1. `ψ_c(0) ∈ L_θ` for every `c` *(C63)*;
2. the boundary map `T_E : ℂ² → E₊` is invertible *(R10, four exact points)*;
3. the **polarisation-summed** carrier operator `G_E = T_E T_E†` satisfies

```
        ┌──────────────────────────────────────────────────────────────┐
        │   κ(E)  :=  Tr( G_E J_E ) / Tr( G_E )  =  m sin θ̄ / E ,        │
        │   independent of q and of k_⊥ .                                │
        └──────────────────────────────────────────────────────────────┘
```

4. the same law holds for the surface mode at either sign of `E` *(C64, extending C48 to a real
   energy symbol)*.

Hence **every stationary mode of the half-space problem, bound or continuum, positive or negative
energy, has the same carrier polarisation `m sin θ̄ / E`.** ∎

**Corollary 23.1 (the state-side funnel).** For any stationary state whose occupation is
independent of the polarisation label — every thermal or Fermi-sea state, and every band state,
the band having no polarisation freedom (Thm 26) — the carrier polarisation is

```
        κ  =  m sin θ̄ · ⟨ E⁻¹ ⟩_∂ ,
```

the boundary-spectral mean of `1/E` (weights `n_mode |v_mode|²`, signed energies). The boundary
datum enters **only through the surface gap `m sin θ̄`**; the state enters only through **one
spectral moment**. This is the state-side companion of Theorem 12's funnel (`A = m cos θ̄` on the
spectral side, `m sin θ̄` on the polarisation side): the free flat wall's quantum sector sees `θ̄`
through `(cos θ̄, sin θ̄)` and nothing else.

**Corollary 23.2 (kinematic consequence; `DERIVED-CONDITIONAL`; a check that could have failed).**
For continuum modes `E ≥ m`, so `κ(E) ≤ sin θ̄`. The `ZS-M66` target requires `κ = T₂ =
0.83538…` while `sin θ̄_* = 0.82412…`. Since `T₂ > sin θ̄_*` *(V21)*, **no continuum-only stationary
unpolarised state can carry the record**: at least

```
        w_min  =  ( T₂ − sin θ̄_* ) / ( 1 − sin θ̄_* )  =  0.0640…
```

of the boundary spectral weight must sit in the surface band (`E < m`). Corollary 15.1 said the
band must *exist*; this says it must be *occupied*. The inequality `T₂ > sin θ̄_*` is equivalent
to `|Im λ| > 1 − (Re λ)²` and was not consulted before the law was derived.

**What Theorem 23 does not say (`NC-M67.19`).** An individual polarisation can deviate from the law
*(witness W11)*; spin-polarised occupations are a hidden freedom. The law is a statement about
unpolarised occupation and about the band.

### 18.2 Theorem 24 — charge conjugation, and why the edge-sector `η` route is empty

**Theorem 24 (spectral symmetry).** The antiunitary charge conjugation `𝒞ψ = iγ²ψ*` (position
preserving, `p ↦ −p`) anticommutes with the Dirac Hamiltonian `H = α·p + βm e^{iθ_m γ₅}` for
**every** mass phase `θ_m`, and preserves `B_θ` (hence `L_θ`) and `N` for **every** `θ` *(C65,
symbolic in `θ, θ_m, p`)*. Consequently the half-space chiral-bag Hamiltonian has a spectrum
symmetric under `E ↦ −E` at every `θ̄`, and

```
        η( H_θ̄ )  ≡  0 ,          ∂_θ̄ η_edge  ≡  0 ,          ρ_∂(−E) = ρ_∂(E) .
```
∎

**Corollary 24.1 (the edge route, closed as posed).** v2.4 §17 ranked "compute `∂_θ̄ η_edge`" as the
only remaining avenue for `F-M66.17` inside the free sector. In the Lorentzian Hamiltonian
formulation that quantity is identically zero — not small, not θ̄-independent by accident, but
zero by a symmetry that fixes `θ̄`. The edge band is a single 2-component 2+1 fermion with symmetric
spectrum `±(k_⊥² + m² sin² θ̄)^{1/2}` *(C66)*, so its spectral asymmetry vanishes mode by mode.

**Corollary 24.2 (the vacuum's `κ`, by a second route).** Since `ρ_∂` is even in `E`, the
𝒞-symmetric vacuum has `⟨E⁻¹⟩_∂ = 0` under any 𝒞-symmetric regularisation, hence `κ_vac = 0` by
Theorem 23. Corollary 21.2 obtained this from boosts; Theorem 24 obtains it from charge conjugation.
Two independent symmetries kill `κ` on the vacuum; an environment must break **both** (a rest
frame *and* a charge/energy asymmetry).

**Corollary 24.3 (complete spectral exhaustion inside A1–A5; `BT-NO-GO-MAP`).** With Theorem 12
(continuum phase depends on `θ̄` only through `m cos θ̄`), Theorem 13 (bare effective action, bound
state included, strictly monotone in `m cos θ̄`) and Theorem 24 (spectral asymmetry identically
zero), **no spectral quantity of the free flat wall selects a point of the arc.** The classes
exhausted are: continuum phase shift, full Jost determinant, edge free energy (contained in the
Jost factor), and Lorentzian spectral asymmetry. `F-M66.17` is therefore `CLOSED-NEGATIVE inside
A1–A5` while remaining `OPEN` outside.

**Scope (`NC-M67.20`).** Theorem 24 concerns the Lorentzian Hamiltonian. The Euclidean parity-odd
edge term — a 2+1 Chern–Simons level of order `½ sign(m sin θ̄)` if the edge band is coupled to a
background gauge field (relax A4) — is **not** computed here. If it exists it is piecewise
constant on the arc, distinguishing at most the half-arcs `(π/2, π)` and `(π, 3π/2)`, and cannot
select a point either. This is consistent with §16.4(2)'s external report that the θ-dependence of
`η` sits in the edge sector: in *their* dimension the edge band is chiral; in ours it is not.

### 18.3 Theorem 25 — there is no autonomous `Φ_∂` under A4, and what the dynamics condition really is

**Theorem 25 (no autonomous boundary map; witness-level under A4).** There exist two one-particle
states of the free bulk with identical projected boundary state `ρ₊(0)` and different `ρ₊(t)`
*(W10: two superpositions of exact continuum modes at `k_⊥ = 0`, energies 5 and 15, `m = 3`,
polarisations chosen through `T_E^{-1}` so that the projected vectors coincide; the beat phases are
opposite)*. Hence `ρ₊(t)` is not a function of `ρ₊(0)`: **no map `Φ_∂ : ℬ(E₊) → ℬ(E₊)` describes
the carrier dynamics in the free sector.** ∎

**What this closes, and how.** `NC-M67.12`'s map half asked for `Φ_∂` "obtained by integrating out
the bulk". Under A4 that request is **ill-typed**: the carrier is not a subsystem coupled to the
bulk; it is the projection of the boundary value through the isomorphism of Theorem 19, so its
state is the **pushforward** of the bulk state and its "dynamics" is the bulk's. The correct
object is therefore not a map but a **bulk stationary state**, and the three requirements of
Corollary 14.2 transform as follows.

**Theorem 25.1 (uniqueness-transfer lemma; universal).** For every flip `X ∈ 𝔛(J_E)` and every
state `ρ`, `Tr(XρX J_E) = −Tr(ρJ_E)` *(C67, symbolic in the flip index and the Bloch vector)*.
Hence, for any map `Φ` with a **unique** stationary state `ρ_*`:

```
   flip-covariance   ⇒  Ad_X ρ_* = ρ_*  ⇒  κ = −κ = 0        [(N-cov) is a corollary]
   unitality         ⇒  ρ_* = ½          ⇒  κ = 0             [(N-uni) is a corollary, C43]
   boost-covariance  ⇒  G ρ_* G†∝ ρ_*    ⇒  κ = 0             [(N-boost) is a corollary, C59]
```

**The three "necessary conditions" of Corollary 21.1 are consequences of one condition — a unique
stationary state with `κ ≠ 0` — not independent requirements.** ∎

**Corollary 25.2 (the residue of `F-M66.15`, re-typed).** After Theorems 19–25 the residue is:

```
   (i)   a UV-finite boundary sector on which "the carrier state" is defined          [sector choice]
   (ii)  a bulk stationary state, faithful on that sector, with ⟨E⁻¹⟩_∂ ≠ 0            [one spectral moment]
   (iii) whatever stabilises ⟨E⁻¹⟩_∂ at T₂/(m sin θ̄)                                 [the physics]
```

Item (ii) is automatically 𝒞-asymmetric and boost-asymmetric (Cors. 21.2, 24.2), so the
symmetry-breaking demands are absorbed into the single moment. Item (i) is a **hidden freedom**
named here for the first time (`D12`): the full one-body density matrix of any many-body state is
UV-dominated and has `κ = O(1/Λ)` (W07); a carrier state with `κ = O(1)` exists only on a UV-finite
sector — the gapped surface band being the canonical candidate. Item (iii) requires an interacting
or environmental sector (relax A4) and is where `F-M66.15` still lives.

### 18.4 Theorem 26 — the band is a qubit bundle, and temperature is a rest frame

**Theorem 26 (edge band structure; universal).** At fixed `(k_⊥, sign E)` the boundary-condition
system of the edge ansatz has rank exactly 1, so the band carries **exactly one** state per
`(k_⊥, sign E)`. The two states at the same `k_⊥` project to **antipodal** Bloch vectors,
`r(v₋) = −r(v₊)`, hence to orthogonal carrier vectors: **the band lift is onto `E₊` at every
`k_⊥`**, and the per-`k_⊥` band state is a genuine qubit state on the carrier *(C66)*. ∎

**Theorem 26.1 (per-`k_⊥` band thermal state; universal).** With occupation `n = n_F(E)`,
`ρ₊(k,T) = n v₊v₊† + (1−n) v₋v₋†` has

```
        κ(k, T)  =  −(1 − 2n) · m sin θ̄ / E  =  −tanh( E/2T ) · m sin θ̄ / E ,
```

is faithful iff `0 < n < 1` (`T > 0`), and is pure at `T = 0` with `κ = −m sin θ̄/E` — the
**Dirac-sea polarisation**, opposite in sign to the particle branch *(C69)*. ∎

**Theorem 26.2 (band-excitation ensemble; closed form).** For the thermal particle occupation of
the band, with `Δ = m|sin θ̄|` and `x = Δ/T`,

```
        κ_exc(x)  =  x ln(1+e^{−x}) / ( x ln(1+e^{−x}) − Li₂(−e^{−x}) ) ,
        κ_exc → 1 (T → 0),      κ_exc ≃ (12 ln 2/π²) x → 0 (T → ∞),
```

strictly increasing in `x` on a grid spanning four decades *(C68, V20)*. ∎

**Corollary 26.3 (temperature is a target-blind rest frame — but not a selector).** A KMS state of
the free bulk in the boundary rest frame is unique and faithful (imported: uniqueness of quasi-free
KMS states of the free Dirac field at fixed `(β, μ)`), rotation-invariant (so Theorem 20's
one-parameter family is automatic), boost-breaking and 𝒞-asymmetric (through `n_F`), and its band
pushforward has `κ ∈ (0,1)` with `sign κ = sign(sin θ̄)` on the excitation branch. **Every
requirement of Corollary 14.2 that concerns the state is met by a thermal band state, with no
parameter read from `λ`.** What is not met is selection: `κ_exc = T₂` has the unique solution
`x_* = 5.08249…` *(V20)*, i.e.

```
        T_* / ( m |sin θ̄| )  =  0.19675… ,        T_*/m  =  0.16215…  at  θ̄_* ,
```

a **kinematic consequence** of the identification (`DERIVED-CONDITIONAL`), exactly as Corollary
15.2's `|k_⊥|_*` was — now with a *physically named* rest-frame source instead of a hand-picked
momentum. Nothing here selects `T`. `[가설]` for the physical reading; `[검증됨]` for the algebra.

**Corollary 26.4 (a sign test, conditional on `θ_m = 0`).** The Dirac-sea branch has
`κ = −m sin θ̄/E`, the particle branch `+m sin θ̄/E`. If the mass phase is `θ_m = 0` (so `θ = θ̄`),
the target's requirement `κ sin θ_* = Im λ > 0` demands the **particle-branch sign**, i.e. a band
that is *not* in its ground state — population above the sea. If `θ_m ≠ 0` the sign is absorbed
into `θ_m` (C32) and no constraint follows. `[열림]` pending the `θ_m` convention of `ZS-M66` §5.2
(the mapping obligation of Corollary 8.2).

**Non-claims.** **`NC-M67.21`** Theorem 26 supplies states, not a dynamics; no thermalising
generator on the band is constructed (A4 forbids it). **`NC-M67.22`** The uniqueness of the KMS
state is IMPORTED and used only for the existence of *a* faithful stationary state; no theorem of
this paper depends on it.

### 18.5 Hidden-freedom audit (kernel / BREAKTHROUGH §12)

```text
candidate: "band thermal state as the carrier state"
  branch:         particle vs sea vs per-k qubit   (three readings; D12)     <- NOT derived
  dimension:      3+1 wall, 2+1 band                (fixed by A1)
  representation: Dirac rep, ZS-M66 §5.1 ordering  (sign of kappa convention-tied, Remark 3.0)
  normalisation:  Tr(rho)=1 on the chosen sector    (sector-dependent)
  window/grid:    none in C rows; 10-point grid in V20 (monotonicity witness only)
  truncation:     none (closed form)
  sign:           kappa sign tied to (theta, theta_m) convention; Cor. 26.4 is conditional
  subgroup/field: none
  boundary cond.: chiral bag, fixed by Thm 3
  discarded:      "continuum-only state" (V21 kills it conditionally); "full one-body density
                  matrix" (UV-dominated, W07); "autonomous Phi_partial" (W10 kills it)
formula fixed before target?  YES for Thms 23-26 (no Z-Spin datum enters);
                              V20/V21 consult T_2 AFTER the law is fixed.
free choices: 1 (sector).  search multiplicity: 0.  fitted parameters: 0.
```


---

## 19. Theorems 27–30 — the on-shell collapse, the boundary gap equation, the parity-odd level, and the `θ_m` convention **(new in v2.6)**

v2.5 ranked three next steps. This section takes all three and returns, in order: a **positive
construction** where v2.5 had only no-gos (W1′), a **confirmation with a sharp reason** (W2′), and
a **discharged obligation with a negative consequence for one conditional test** (W3′). The first
is the substantive result of this version and it is the first place in the `M60`–`M67` sequence
where the boundary angle stops being a free modulus.

### 19.0 Breakthrough record (route cards, frozen before external collision)

```text
FREEZE
  TARGET:        (a) can any boundary interaction of the Theorem-10 class change <1/E>_boundary?
                 (b) the Euclidean parity-odd edge term;  (c) the theta_m convention of ZS-M66
  EXACT RESIDUE: (a) whether the interacting sector (relax A4) can fix the one spectral moment
                     that Cor. 25.2 left as the whole of F-M66.15
  HARD:          Thms 1, 3, 10/11 (the locus H and the chart), 12, 13, 15, 19-26
  SOFT:          A4 (free bulk) -- deliberately relaxed here;  A5;  the choice of interaction channel
  UNKNOWN:       whether a boundary condensate is even well-typed on the well-posedness locus
  FORBIDDEN:     reading lambda before the gap equation is written down; tuning the channel to hit
                 the target; calling a mean-field result derived
  SUCCESS OBSERVABLE: an equation whose solution set for thetabar is discrete rather than a circle

ROUTE-5 / B16 BOUNDARY-CENTER + B03 TYPE REPAIR   ("what does a boundary term DO on shell?")
  MINIMAL CONSTRUCTION: restrict the whole 4-parameter bilinear class of Prop. 10 to L_theta
  DECISIVE KILL TEST:   the restriction depends on more than one operator -> FAILED:
                        it collapses to a multiple of J_E (C70).  The boundary term and the
                        record observable are conjugate variables.
  MATURITY: constructed, verified                    STATUS: BT-ROUTE

ROUTE-6 / B18 OBSTRUCTION->OBJECT + B11 CANCELLATION  ("make the condensate the angle")
  MINIMAL CONSTRUCTION: mean-field condensate on H;  chart theta = pi - 2 arctan(4J) (C72);
                        close with Thm 23's state equation
  DECISIVE KILL TEST:   the two equations are compatible for every thetabar (no selection)
                        -> FAILED: they force |cos thetabar| = g_c/g (C73).  Discrete solutions.
  MATURITY: constructed, verified                    STATUS: BT-ROUTE (first positive selection)

ROUTE-7 / B04 LAYER SPLIT  ("Lorentzian eta vs Euclidean level")
  MINIMAL CONSTRUCTION: Tr(H_edge J_E)/2 on the band projectors of C66
  DECISIVE KILL TEST:   the edge mass depends on k_perp or on the frame -> FAILED: it is
                        exactly m sin(thetabar) (C74).  Level = (1/2)sign(sin thetabar).
  MATURITY: constructed, verified                    STATUS: BT-NO-GO-MAP (completes v2.5's)

NO-GO EMISSION GATE (kernel sect.5.5) is NOT invoked in 19.1-19.2: the output there is a
CONSTRUCTION, not a no-go.  It is invoked for 19.3, where SIGN/QUANTIFIER/SOURCE/VALUE pass as
in 18.0 and the object (the level) is exhibited rather than merely excluded.
```

### 19.1 Theorem 27 — the on-shell collapse: boundary terms and the record are conjugate

**Theorem 27 (on-shell bilinear collapse; universal).** Let `Ψ_θ` be the basis of `L_θ` supplied by
Theorem 14.1. For every `(a,b,c,d) ∈ ℝ⁴` and every `θ`,

```
        ┌────────────────────────────────────────────────────────────────────┐
        │  Ψ_θ† K Ψ_θ  =  2( a sin θ + b cos θ + d ) · J_E ,                  │
        │  Ψ_θ† N Ψ_θ = 0 ,   Ψ_θ† γ₅ Ψ_θ = 0 ,   Ψ_θ† Ψ_θ = 2·1 .            │
        └────────────────────────────────────────────────────────────────────┘
```

*(C70, universal in `(a,b,c,d,θ)`.)* ∎

The four-parameter class of Proposition 10 — the whole derivative-free, gauge-invariant,
tangential-scalar, Hermitian boundary-term space — therefore acts **on shell through a single
operator**, and that operator is exactly `J_E`, whose expectation is `κ`. Off shell the four
generators are independent *(witness W12)*; the collapse is a property of the boundary subspace,
not an operator identity.

**Corollary 27.1 (the answer to v2.5's ranked-first question).** v2.5 asked whether any boundary
interaction of the Theorem-10 class can change `⟨E⁻¹⟩_∂`. Theorem 27 answers: **the only thing such
a term can couple to is `κ` itself.** A boundary interaction built from these bilinears is
therefore, on shell, a self-coupling of the record observable — which is precisely the structure
that can produce a self-consistent nonzero `κ`, and cannot produce anything else.

**Corollary 27.2 (why `N` decouples).** `Ψ_θ†NΨ_θ = 0` is the isotropy condition of Definition 3.2:
the normal vector current vanishes on any admissible boundary condition. This is why `c` was forced
to zero in Theorem 10 and why the `c`-direction is invisible here — the same fact seen twice.

### 19.2 Theorems 28 — the boundary gap equation

Theorem 27 makes a mean-field treatment well-typed. Let the boundary carry a four-fermion term
whose bilinears lie in the class of Proposition 10. **This is outside Theorem 10** (`NC-M67.8`) and
requires **relaxing A4**; it is the interacting-sector route of Corollary 13.1(iii), taken
explicitly rather than gestured at.

**Theorem 28(a) (the mean-field branch; universal).** A condensate `J` entering the well-posedness
locus `H` through the pair `(b,d) = (−4g₃J, +4g₃J)` — which lies on `H` for every `J`, since
`H` requires `b² = d²` once `a` is fixed by the kinetic normalisation — induces

```
        cos θ = (16J² − 1)/(16J² + 1) ,   sin θ = 8J/(16J² + 1) ,   i.e.   θ = π − 2 arctan(4J).
```

*(C72, universal in `J`; re-checked at four exact rational condensates, R12; the chart itself
independently re-derived from the nullspace of `(K − iN/2)`, C71.)* ∎

**At `J = 0` the boundary sits exactly at `θ = π`** — the point the Shapiro–Lopatinski filter of
Theorem 22 excludes, at which the surface gap `m|sin θ̄|` closes and `κ = 0` by Theorem 23. **Any
nonzero condensate moves the angle off `π` and into the arc.** The excluded point of Theorem 22 and
the symmetric point of the gap equation are the same point, which is not something either result
was built to produce.

**Theorem 28(b) (the gap equation and the selection identity; universal).** Write `s := m⟨E⁻¹⟩_∂`,
so that Theorem 23 reads `κ = s sin θ̄`, and let the condensate be proportional to the record,
`4J = 2gκ`, with `g` the boundary coupling in units fixed by the bilinear normalisation. Then

```
        κ = s sin θ̄ ,        θ̄ = π − arctan(2gκ)
   ⟹   κ = 0  always,  and a nonzero solution exists  ⟺  2s|g| > 1 ,
   ⟹   κ²  =  s² − 1/(4g²) ,
        ┌──────────────────────────────────────────────────────────┐
        │   | cos θ̄ |  =  1/(2s|g|)  =  g_c/|g| ,   g_c := 1/(2s).  │
        └──────────────────────────────────────────────────────────┘
```

*(C73, universal in `(s,g)`.)* ∎

**Corollary 28.1 (what this does to `F-M66.17`).** The boundary angle is no longer a free
coordinate on the circle: on the symmetry-broken branch it is **fixed by the ratio of the boundary
coupling to its critical value**. The freedom has not disappeared — it has moved from a
boundary-condition modulus, which has no home in any Lagrangian, to a **boundary coupling
constant**, which does and is subject to independent determination by matching or renormalisation.
That is exactly the type repair `RQ1`'s selection backbone asks for: *residual construction freedom
quantified and relocated to an action parameter.* `F-M66.17` moves from **OPEN** to
**OPEN-BUT-TYPED**: the missing arrow `S¹ → point` now exists as a map, and what is open is the
determination of its argument.

**Corollary 28.2 (spontaneous breaking supplies all three of v2.5's conditions at once).** Below
`g_c` the only solution is `κ = 0` — the flip-, boost- and 𝒞-symmetric state. Above `g_c` a
`κ ≠ 0` branch appears. By Theorem 25.1 the three "necessary conditions" of Corollary 21.1 are
consequences of a unique stationary state with `κ ≠ 0`; here that state is produced by
**spontaneous breaking of the grading symmetry at a boundary critical coupling**, and the
environment that Corollary 14.2 demanded is the boundary interaction itself. This is the first
positive mechanism in the `M60`–`M67` line rather than another exclusion.

**Corollary 28.3 (two conditional numbers, both of which could have failed).**
Since `κ = s sin θ̄` and `κ ≤ s`, and since `|cos θ̄| = g_c/g`:

```
   (i)  s_*  =  T₂ / sin θ̄_*  =  |Im λ| / (1 − (Re λ)²)  =  1.0136664…  >  1 .
        Every continuum mode has `E ≥ m`, so a continuum-only unpolarised state has `s ≤ 1`.
        BAND OCCUPATION IS FORCED — the sharp form of Cor. 23.2  (V22).
   (ii) g_* / g_c  =  1/|cos θ̄_*|  =  1/|Re λ|  =  1.7654827…
        The boundary coupling must sit at 1.77 times critical: ORDER ONE, neither near-critical
        nor fine-tuned  (V23).
```

Neither number is a prediction — both are read after the identification — but (ii) is a
**naturalness check the construction could have failed**: a required over-criticality of `10⁻⁶` or
`10⁶` would have killed the route on the spot. Status `DERIVED-CONDITIONAL`.

**What Theorem 28 is not (`NC-M67.24`).** It is a **mean field** result. No fluctuation is
computed, `g` is not renormalised, and the stability of the broken branch above `g_c` is not
proved. The channel ratio and the choice that places the free theory at `θ̄ = π` are **construction
choices** (`D16`). And `s` is itself `θ̄`-dependent through the band gap, so the closed solution
above is the constant-`s` illustration; the self-consistent problem is one equation in one unknown
with **discrete** solutions, and that — not the closed form — is the structural claim. The angle is
`DERIVED-CONDITIONAL`, never `DERIVED`.

### 19.3 Theorem 29 — the edge is a 2+1 Dirac fermion of mass `m sin θ̄`

**Theorem 29 (universal).** With the band projectors of Theorem 26, the edge Hamiltonian on the
carrier is `H_edge = E(P₊ − P₋)`, and

```
        Tr H_edge = 0 ,        ½ Tr( H_edge J_E )  =  m sin θ̄ ,
```

independent of `k_⊥` and — being a trace — independent of the carrier frame *(C74)*. The edge band
is therefore a **2+1 Dirac fermion of mass `m sin θ̄`**. ∎

**Corollary 29.1 (the Euclidean parity-odd level; `IMPORTED` step).** Coupled to a background gauge
field (relaxing A4), a 2+1 Dirac fermion of mass `M` induces a Chern–Simons level `½ sign(M)`.
Hence the boundary level is `½ sign(sin θ̄)`: **piecewise constant on the arc**, jumping only where
the gap closes at `θ̄ ∈ πℤ`. It separates the half-arcs `(π/2, π)` and `(π, 3π/2)` and **cannot
select a point.** This confirms `NC-M67.20`'s prediction with an exact reason rather than an
expectation, and completes the No-Go Map of Corollary 24.3 outside A4 for the parity-odd channel.
The level itself is not computed by a loop integral here (`D17`).

**Corollary 29.2 (consistency of the two spectral statements).** `η(H_θ̄) ≡ 0` in the Lorentzian
Hamiltonian (Theorem 24) and a half-integer Euclidean level are not in conflict: the first is a
statement about the symmetric spectrum of a 2+1 Dirac operator, the second about the regularised
parity-odd response of the same operator. Theorem 29 exhibits the single object both statements are
about, which is why the apparent tension of v2.5 §18.2 dissolves rather than being adjudicated.

### 19.4 Theorem 30 — the `θ_m` convention, discharged

**Theorem 30.** Under `exp(iαγ₅)` the boundary involution moves as `B_θ ↦ B_{θ+2α}`, and under the
inverse rotation as `B_θ ↦ B_{θ−2α}` *(C75, both certified on the same operator)*. `ZS-M67`
Cor. 9.2 uses the first sign and `ZS-M66` §6 the second; the two texts therefore use **opposite
signs for the rotation parameter and the same invariant**

```
        θ̄ = θ + θ_m .
```

**The mapping obligation of Corollary 8.2 is DISCHARGED**: there is no sign discrepancy, only two
conventions for `α`. ∎

**Corollary 30.1 (the sign test of Cor. 26.4 does not bite).** `ZS-M66` §6 records `θ_m` as the
chiral phase of the Yukawa mass, a function of the direction of `⟨H₅⟩`, and states explicitly that
the upstream action **leaves it unfixed** (eight unfixed real parameters, registered upstream as a
debt). The hypothesis `θ_m = 0` of Corollary 26.4 is therefore not available, and the
particle-branch sign requirement it derived is **absorbed into `θ_m`**. Corollary 26.4 is retyped
`[열림] → CLOSED-VACUOUS`: it is a true conditional whose antecedent the corpus does not supply.
*(Primary source: `ZS-M66 v1.5.1` §6 and §8, read this session from the repository.)*

**Corollary 30.2 (what remains of `θ_m`).** Since `θ̄` is what Theorem 28 determines and `θ` alone
is a torsor coordinate (Theorem 9), the gap equation fixes the **invariant**, and any split of it
between `θ` and `θ_m` is a chiral-frame choice. This is the second time this version finds that an
apparent freedom was a coordinate: the first was Theorem 27's collapse.

### 19.5 Hidden-freedom audit (kernel / BREAKTHROUGH §12)

```text
candidate: "the boundary gap equation selects thetabar"
  branch:         broken (kappa != 0) vs symmetric (kappa = 0)  -- selected by g vs g_c, not by hand
  channel:        the (b,d) pair and the ratio g3/g2               <- CONSTRUCTION CHOICE (D16)
  zero-coupling point: Phi = pi puts the free theory at thetabar = pi  <- CONSTRUCTION CHOICE
  normalisation:  4J = 2 g kappa defines g; no separate scale is introduced
  approximation:  mean field, no fluctuations, no RG               <- NOT a derivation
  s:              treated as constant in the closed solution; genuinely thetabar-dependent
  sign:           |cos thetabar| = g_c/g fixes the magnitude; the branch of the arc is fixed by
                  sign(sin thetabar), i.e. by the sign of the condensate -- one discrete choice
  discarded:      "no boundary interaction can move <1/E>" (refuted by C70/C73);
                  "theta_m = 0" (refuted by the M66 primary text, Cor. 30.1)
formula fixed before target?  YES.  C70, C71, C72, C73, C74, C75 contain no Z-Spin datum.
                              V22 and V23 consult lambda only AFTER the identity is fixed.
free choices: 2 (channel, zero-coupling point).  fitted parameters: 0.
NET: one continuous modulus (thetabar) traded for one coupling (g) plus two discrete choices.
     The dimension count is unchanged; the TYPE is not.  That is the whole claim.
```


---

## 20. Theorems 31–35 — the selection chain closed end to end, and what it costs **(new in v2.7)**

v2.6 left three items and a fair criticism: the line had been pruning around the core rather
than attacking it. The core is Mission §4.6's selection backbone — *does the action select the
record, target-blind?* This section answers it in the only form the evidence supports: **every
arrow of the chain now exists, the free theory is proved unable to supply the first one, the
upstream Yukawa sector supplies it, the broken branch is Goldstone-free and lands on an
established universality class, and the self-consistent equation has a unique solution.** What
it costs is stated at the end and enforced by a guard. The angle is still `DERIVED-CONDITIONAL`
and this remains a **mean field** result.

### 20.0 Breakthrough record

```text
FREEZE
  TARGET:   close the chain  action -> boundary coupling g -> gap equation -> thetabar -> kappa
  RESIDUE:  (X1) is g generated at all, and by what?  (X2) does the broken branch survive
            fluctuations in 2+1?  (X3) does the self-consistent equation with s(thetabar) select?
  HARD:     Thms 1-30; the corrected upstream action's Yukawa term (ZS-S14 v2.1, as recorded in
            ZS-M66 sect.6, read from primary this line)
  SOFT:     A4 (relaxed); tree-level scalar exchange; Hartree-Fock on the boundary; the sector
  FORBIDDEN: a new coupling not present upstream; reading lambda before the chain is written
  SUCCESS OBSERVABLE: (X1) an exact on-shell form of the induced interaction; (X2) an exact
            statement of which symmetry kappa breaks; (X3) a one-unknown equation with a
            discrete, ideally unique, solution

ROUTE-8 / B13 UNIVERSALIZATION  ("what does the free bulk generate?")   -> nothing (Thm 31)
ROUTE-9 / B07 RESPONSIBILITY FACTOR + B16  ("which upstream term reaches the boundary d-channel?")
   -> the Yukawa scalar, through Fierz (Thms 32-33).  KILL TEST: the induced bilinear depends on
      theta and theta_m separately -> FAILED: it depends on thetabar only (C76).
ROUTE-10 / B10 INVARIANTIZATION  ("what does kappa break?")
   -> a Z_2, nothing continuous (C79).  KILL TEST: some flip fixes kappa != 0 -> FAILED.
ROUTE-11 / B17 DISCRETE-CONTINUOUS  ("is the self-consistent set a point or a curve?")
   -> tan thetabar = -2g, unique on the half-arc (C80); 0 or 1 solutions on a (g,T) grid (W13).
NO-GO EMISSION GATE for Theorem 31: SIGN (gate asked "is g generated") PASS; QUANTIFIER
   (all of A4) PASS; SOURCE (Gaussian integration, external to our construction) PASS; VALUE
   (erases the free-bulk reading of Theorem 28) PASS.
```

### 20.1 Theorem 31 — the free bulk cannot select

**Theorem 31 (structural).** Under A4 the bulk is Gaussian; integrating it out generates no
quartic term anywhere, in particular no boundary four-fermion term. Hence `g ≡ 0`, the gap
equation of Theorem 28 has only the symmetric solution `κ = 0`, and **the free flat wall cannot
select** — not by spectral means (Cors. 13, 24.3) and not by the boundary interaction either.
*(D19; standard.)* ∎

This is the definitive form of the Corollary 13.1 dichotomy: **selection requires relaxing A4**,
and v2.6's ranked-first kill test — "is `g` generated at all?" — returns **NEGATIVE for the free
theory**. The next two theorems show it returns positive as soon as the sector that Z-Spin's own
action already contains is switched on.

### 20.2 Theorems 32–33 — the upstream Yukawa sector reaches the boundary through the invariant

`ZS-M66` §6, read from primary this line, records the corrected action's mass sector as a Yukawa
coupling `ψ̄ y e^{iθ_m γ₅}⟨H⟩ ψ` with the phase `θ_m` set by the direction of `⟨H₅⟩`. Exchange of
the massive scalar fluctuation `h` at tree level generates the bulk quartic term
`(y²/2M_h²)(ψ̄ e^{iθ_mγ₅} ψ)²`. No new coupling is introduced.

**Theorem 32 (the induced bilinear is invariant on shell; universal).**

```
        Ψ_θ† ( γ⁰ e^{iθ_mγ₅} ) Ψ_θ  =  2 sin(θ + θ_m) · J_E  =  2 sin θ̄ · J_E ,
```

for every `θ` and `θ_m` *(C76)*. The scalar that supplies `θ_m` couples on shell to the record
through the **axially invariant** angle alone: the coupling is torsor-covariant by construction,
not by fiat. ∎

**Theorem 33 (which channel does the work).**

*(a) The scalar (Hartree) channel is a reflection, not a selector.* A mean-field shift of the
boundary term confined to the `(a,b)` plane along `(cos θ_m, sin θ_m)`, forced onto the locus `H`,
requires the condensate `⟨O⟩ = −cos θ̄₀/λ` and acts on the invariant angle **exactly** as

```
        θ̄  ↦  −π − θ̄ ,
```

a two-cycle whose only fixed points are the arc endpoints `cos θ̄ = 0`, where the condensate
vanishes *(C77, universal)*. The scalar channel alone opens no symmetry-broken branch.

*(b) Fierz supplies the `d`-channel.* The completeness relation on the sixteen Dirac matrices
holds exactly, and `γ³γ₅` is self-inverse; hence the **exchange** (Fock) term of
`(ψ̄ e^{iθ_mγ₅}ψ)²` contains the boundary channel `(ψ†Nγ₅ψ)²` with coefficient `¼` (times the
Grassmann sign) *(C78, universal)*. This is exactly the `(b,d)`-channel that Theorem 28 needs and
Theorem 33(a) shows the Hartree term cannot provide. ∎

**Corollary 33.1 (the chain, written once).**

```
   Yukawa  ψ̄ y e^{iθ_mγ₅}⟨H⟩ψ       (upstream, ZS-S14 v2.1 / ZS-M66 §6)
     → scalar exchange, tree level:  (y²/2M_h²)(ψ̄ e^{iθ_mγ₅}ψ)²        [standard]
     → on shell:  bilinear = 2 sin θ̄ J_E                                 (Thm 32, C76)
     → Fock/Fierz:  (ψ†Nγ₅ψ)² channel with weight ¼                       (Thm 33b, C78)
     → boundary self-coupling of the record observable                   (Thm 27, C70)
     → gap equation, critical coupling g_c, |cos θ̄| = g_c/|g|             (Thm 28, C73)
     → κ = s sin θ̄ ;  a(θ) = cos θ + iκ sin θ                             (Thm 23; ZS-M66 §5.3)
```

**Every arrow exists.** The coupling `g` is not a new parameter: it is `c_F · (y²/M_h²) · ν_∂` with
`c_F` the Fierz weight and `ν_∂` the boundary spectral density of the chosen sector. What is not
computed here is `c_F ν_∂` in the units of Theorem 28 (`D21`); what is *not open* any more is
whether a term of the right type reaches the boundary from the action Z-Spin already has.

**Corollary 33.2 (what the target then demands of the upstream sector; `DERIVED-CONDITIONAL`).**
By Corollary 28.3 and Theorem 34 below, `g_*/g_c = 1/|Re λ| = 1.7655`. Read through Corollary
33.1 this is a single O(1) relation between upstream numbers — `y² ν_∂ /M_h²` must sit at `1.77`
times the boundary critical value — rather than a tuning of an angle. Whether the upstream action
delivers that ratio is the first question for the successor of this line, and it is a question
about `ZS-S14`, not about `ZS-M67`.

### 20.3 Theorem 34 — the broken branch is Goldstone-free, and it is Gross–Neveu

**Theorem 34(a) (what `κ` breaks; universal).** For **every** flip index `n`, `Ad_X` sends
`κ ↦ −κ`, so the orbit of the order parameter under the whole flip family `𝔛(J_E)` is the
two-point set `{κ, −κ}` — a `ℤ₂` — while the continuous rotation about the normal (Theorem 20)
leaves `κ` invariant for every `φ` *(C79)*. **The symmetry broken by `κ ≠ 0` is discrete. No
continuous symmetry is broken.** ∎

**Corollary 34.1 (X2, answered structurally).** The obstruction to ordering in 2+1 dimensions
(Mermin–Wagner / Coleman) concerns *continuous* symmetries. It does not apply to the broken branch
of Theorem 28. Fluctuations renormalise `g_c`; they do not remove the phase.

**Theorem 34(b) (the identification; `IMPORTED` physics, mapping ours).** By Theorem 29 the edge
band is a two-component 2+1 fermion whose mass matrix is `J_E`, and by Theorem 27 the boundary
interaction is a self-coupling of the `J_E` density. That is the field content and the interaction
of the **`N = 1` (two-component) 2+1 Gross–Neveu model** — the chiral-Ising class — whose `ℤ₂`
symmetry breaking above a finite critical coupling, with a dynamically generated mass, is
established beyond mean field by large-`N`, `ε`-expansion, lattice and bootstrap methods *(not
read from primary text this session; `D20`)*. Under the mapping, **the dynamically generated
Gross–Neveu mass is `m sin θ̄`**: at zero coupling the bare edge sits at `θ̄ = π` and is massless
(Theorem 28(a)); the interaction generates the mass, and the mass *is* the angle.

**What this does and does not do (`NC-M67.28`).** It places the boundary theory in a universality
class where the mean-field phase diagram is known to survive fluctuations *qualitatively*. It does
not compute the fluctuation-corrected `g_c`, and the mapping's novelty has had **no prior-art sweep
this session** (`OPEN-NOVELTY`).

### 20.4 Theorem 35 — the self-consistent equation has a unique solution

**Theorem 35 (T = 0 band sector; universal in `g`).** In the band-excitation reading at `T → 0`,
`κ_exc → 1` so the moment is `s = 1/sin θ̄` **exactly**, and the gap identity `|cos θ̄| = 1/(2sg)`
becomes

```
        ┌──────────────────────────────────────────────────┐
        │   tan θ̄  =  −2g ,       θ̄  =  π − arctan(2g) ,   │
        └──────────────────────────────────────────────────┘
```

with a **unique** solution on the half-arc `(π/2, π)`: the difference of the two sides is strictly
monotone there *(C80; derivative `sin θ̄ − cos θ̄/(2g) > 0`)*. The over-criticality
`g/g_c = 1/|cos θ̄|` is unchanged. ∎

**Corollary 35.1 (X3, answered).** v2.6's closed formula assumed constant `s`; the genuinely
self-consistent problem replaces it by one equation in one unknown, and at `T = 0` that equation is
`tan θ̄ = −2g`. At finite `T`, with `s = s(θ̄, T)` through the band gap, the closed equation has
**0 or 1** solutions on the half-arc at every point of a `5 × 4` `(g, T/m)` grid *(witness W13)*
— never a continuum. Discrete selection survives the `θ̄`-dependence of `s`.

**Corollary 35.2 (two sector readings agree on the invariant).** At the target,
`g_* = 0.72752`, `g_c = 0.41206`, `g_*/g_c = 1.76548 = 1/|Re λ|` *(V24)* — the same ratio v2.6
obtained with constant `s` (V23). The two readings differ in `g` and `g_c` separately and agree
on the invariant ratio, a consistency check that could have failed.

### 20.5 The honest ledger of what v2.7 changes

```text
CLOSED THIS VERSION
  X1  is g generated?      NO under A4 (Thm 31);  YES from the upstream Yukawa sector, through
                           an invariant on-shell bilinear and the Fierz d-channel (Thms 32-33)
  X2  fluctuations         the broken symmetry is Z_2; Goldstone-free (Thm 34a);  the boundary
                           theory is N=1 Gross-Neveu in 2+1, whose broken phase survives (34b)
  X3  self-consistency     unique solution tan thetabar = -2g at T = 0 (Thm 35);  0 or 1
                           solutions on a finite-T grid (W13)

STILL OPEN, NOW NAMED
  the number  c_F nu_partial  that turns y^2/M_h^2 into g          (D21; sector-dependent, D12)
  whether ZS-S14 v2.1's (y, M_h) put g at 1.77 g_c                 (Cor. 33.2 -> successor)
  the fluctuation-corrected g_c                                    (imported class, not computed)
  prior art on the chiral-bag / Gross-Neveu boundary mapping       (OPEN-NOVELTY)
  faithfulness on the sector; A5; RP; Lorentzian<->Riemannian      (unchanged)

WHAT DID NOT HAPPEN
  No CORE promotion.  Theorem 28 is mean field and Theorem 34b is imported.  The angle is
  DERIVED-CONDITIONAL.  RQ3 bridge OPEN -> OPEN.  The chain is exhibited; it is not yet computed
  to a number without a Z-Spin datum, and until it is, "the action selects" is a typed
  conjecture with every step written down -- which is the most this line has ever had.
```


---

## 21. Theorem 36 — the coefficient, and the kill **(new in v2.8)**

v2.7 wrote the selection chain arrow by arrow and left one number: does the upstream Yukawa sector
put the boundary coupling at `1.77 g_c`? This section computes it. **It does not.** For the top
quark it is short by a factor **42**; for every other Standard-Model fermion by seven to eight
orders of magnitude; and Theorem 36 shows the shortfall is not a matter of the sector cutoff — no
occupation of a single edge band can carry the record and be super-critical under contact exchange
of a perturbatively coupled scalar. The chain of Corollary 33.1 is **KILLED at the coefficient**,
and the route is **CLOSED-NEGATIVE** at the scope stated in §21.4. This is a mean field result, and
everything in it is `DERIVED-CONDITIONAL` on the identification; the algebra (C81–C84) is exact.

### 21.0 Breakthrough record

```text
FREEZE
  TARGET:   compute c_F nu_partial in Theorem-28 units; read (y, M_h) from ZS-S14 v2.1; decide g/g_c
  RESIDUE:  one number
  HARD:     Thms 23, 27, 28, 32, 33, 35; ZS-S14 v2.1 Def. 3.1', Prop. S14.K (<H> = v, y = sqrt2 m/v),
            sect.2.6 (v = 245.93 DERIVED, m_h = 125.25 HYPOTHESIS-strong, m_t = 171.872 DERIVED)
  SOFT:     the sector (D12) -- treated EXHAUSTIVELY here (Thm 36 ranges over all occupations);
            the O(1) factor c' (D25); mean field
  FORBIDDEN: rescuing with an unmotivated scale; reading lambda before the bound is written
  SUCCESS OBSERVABLE: an inequality on G_4 m^2 that the upstream numbers either satisfy or fail

ROUTE-12 / B13 + B08  ("separate existence from value")
   the bound of Theorem 36 is derived with no Z-Spin datum; the target enters only in V25.
   KILL TEST: the upstream numbers satisfy the bound -> FAILED by x42 (top), x1e7-1e8 (rest).
NO-GO EMISSION GATE (kernel sect.5.5):
   SIGN        gate asked "is g >= 1.77 g_c"; computed: g/g_c itself, with the sector maximised.  PASS
   QUANTIFIER  Theorem 36 is universal over Pauli-allowed occupations of the band; V25 enumerates the
               five SM fermion masses that matter.  PASS
   SOURCE      external: the Standard-Model Yukawa/Higgs numbers and the edge-band spectrum, not a
               choice of ours.  The object (the chain) was built first (v2.7).  PASS
   VALUE       closes the Yukawa-contact route to F-M66.17 and narrows the complement to
               non-contact boundary interactions.  PASS
```

### 21.1 The coefficient, assembled

**Lemma 36.1 (tree-level exchange; exact).** Eliminating the Higgs fluctuation `h` from
`−½m_h²h² − (y/√2)hψ̄ψ` at zero momentum gives the contact term `+(y²/4m_h²)(ψ̄ψ)²`; with the
Standard-Model relation `y = √2 m/v` in `ZS-S14`'s convention `⟨H⟩ = v` (Prop. S14.K),

```
        G₄  =  m² / ( 2 v² m_h² ) .                                                 (C81)
```

**Lemma 36.2 (edge overlap; exact).** With the normalised edge profile `ψ = √(2κ_loc) e^{−κ_loc x}χ`,
the bulk quartic integrates over the normal direction to `G₄ κ_loc (χ̄Γχ)²` — a 2+1 four-fermion
coupling of mass dimension −1; matching its mean field to the boundary bilinear `2κ_loc χ̄Kχ`, the
overlap cancels and the Theorem-28 coupling is

```
        g  =  c′ · G₄ · n_∂ ,        c′ = ½ at leading order (Fierz ¼ × collapse 2),      (C82)
```

with `n_∂` the 2+1 edge density. **Nothing else enters.** The coupling is a density times a
contact strength; the localisation length has dropped out.

### 21.2 Theorem 36 — the single-band contact bound

The two things the route needs are in tension: the record `κ = s sin θ̄` with `s = m⟨E⁻¹⟩_∂` wants
occupation **near the band bottom** (large `1/E`), while super-criticality `2gs ≥ 1` wants **large
density** `n_∂`. Theorem 36 makes the tension exact.

**Theorem 36 (universal over Pauli-allowed occupations of one edge band).** For the filled disk
`E ≤ E_max`, `N = (E_max² − Δ²)/4π` and `⟨E⁻¹⟩ = 2/(E_max + Δ)` exactly; the filled disk is the
maximal-density occupation at fixed `⟨E⁻¹⟩`. With `Δ = m sin θ̄` and `κ = s sin θ̄`,

```
        2gs  =  c′ G₄ m (E_max − Δ)/π ,          E_max = m sin θ̄ (2/κ − 1) ,
        ┌──────────────────────────────────────────────────────────────┐
        │   super-critical  ⟺   G₄ m²  ≥  π κ / ( 2 c′ sin θ̄ (1 − κ) ) . │
        └──────────────────────────────────────────────────────────────┘
```

*(C83, exact.)* ∎

> **Target-dependence typed (v3.4; v3.3 audit, S2).** The functional form `G₄m² ≥ πκ/(2c′ sin θ̄(1−κ))` is general —
> it holds for every record magnitude `κ` and angle `θ̄` of one Pauli-allowed band. The numbers that follow (`19.34`,
> the `×42` shortfall) insert `(κ, θ̄) = (T₂, θ̄_*)` and are therefore **target-conditioned**: they are a necessary
> admission bound evaluated on the Z-Spin identification, not a target-blind selection statement. The distinction
> weakens nothing below; it only blocks reading the kill as a selection theorem.

**Corollary 36.1 (in exchange variables).** With `G₄ = y²/4M²`,

```
        y m / M  ≥  √( 2π κ / ( c′ sin θ̄ (1 − κ) ) )  =  8.8   at (κ, θ̄) = (T₂, θ̄_*), c′ = ½ .
```

*(C84.)* The fermion must be heavier than the exchanged scalar by `≈ 9/y` — **outside the contact
regime `m ≪ M`** in which `G₄` was derived. Contact exchange of *any* perturbatively coupled heavy
scalar cannot make a single edge band super-critical while it carries the record.

### 21.3 The numbers

At `(κ, sin θ̄) = (T₂, sin θ̄_*)` and `c′ = ½`, Theorem 36 requires `G₄ m² ≥ 19.34`. The upstream
inputs (`v = 245.93` DERIVED, `m_h = 125.25` HYPOTHESIS-strong, `m_t = 171.872` DERIVED) give

```
   fermion              G₄ m² = m⁴/(2v²m_h²)      shortfall
   top  (ZS-S13)             0.460                 × 42.1
   top  (PDG 172.57)         0.467                 × 41.4
   bottom                    1.6 × 10⁻⁷            × 1.2 × 10⁸
   tau                       5.3 × 10⁻⁹            × 3.7 × 10⁹
   charm                     —                     × 10⁹ – 10¹⁰
```

*(V25.)* **The chain of Corollary 33.1 is KILLED at the coefficient for every Standard-Model
fermion.** For the record, the two sector cutoffs the corpus supplies do not help either: in the
filled-sea reading the critical edge cutoff is `Λ_c = 4πv²m_h²/m³ = 2.35 TeV` (top), against
`Λ = m_t` (sub-critical, `0.07 g_c`) and `Λ = m_ρ = 2A·M_P` (over-critical by `1.7×10¹⁴`, with
`κ ≈ 2m/Λ ≈ 10⁻¹⁵`) *(V26)* — and Theorem 36 says no `Λ` can land, because the sea sector's `κ`
collapses exactly when it becomes super-critical.

### 21.4 Verdict, scope, and the surviving complement

```text
CLOSED-NEGATIVE (this version)
  F-M66.17 via the Yukawa-contact / single-edge-band / mean-field chain of v2.6-v2.7:
     the boundary coupling supplied by the Standard-Model Yukawa sector is too small by x42
     (top) and by 1e7-1e8 (all other fermions) to reach the record value while super-critical.
     Robust to the O(1) factor c' (would need c' = 21), to fluctuations (expected to RAISE g_c,
     D23), to gluon exchange (a factor of a few at most, D25), and to the sector (Thm 36 ranges
     over all Pauli-allowed occupations).

WHAT SURVIVES (the complement, named)
  (i)   a NON-contact boundary interaction -- a light mediator living on the boundary, for which
        Lemma 36.1 does not apply.  The corpus has one candidate object of the right type: the
        Goldstone phase theta of the Z-bias field Phi (ZS-S14 sect.2.11, massless).  Whether it
        couples to the edge band is OPEN and is now the first question.
  (ii)  a fermion outside the Standard Model that is heavier than its own mediator (Cor. 36.1) --
        which is not a contact interaction and needs a different derivation.
  (iii) more than one edge band (a multi-band carrier), which changes the density count and is
        outside Theorem 36's hypothesis.  ZS-M66 Q11's carrier is one qubit; this would change it.
  (iv)  a record value below T_2 -- excluded by the identification, not by physics.

WHAT DID NOT HAPPEN
  No CORE promotion; no SSOT change.  RQ3 bridge OPEN -> OPEN.  The chain of v2.7 stands as
  written; what fell is the claim that the corpus's own Yukawa sector supplies its coefficient.
  The angle is not selected.  This is the first version of ZS-M67 whose headline is a kill, and
  the kill was reached by the deterministic route the Mission asks for: write every arrow, then
  compute the one number.
```

**Corollary 36.2 (what the Mission gains).** Under the Yukawa-contact chain the Z-Spin record
channel is not carried by any Standard-Model fermion. That closes a route the programme had held
open since `ZS-M66` — the reading in which the seam fermion is an ordinary quark or lepton whose
mass phase is set by `⟨H₅⟩` — and it does so with a bound (Theorem 36) that any future candidate
must pass before its angle is computed. The bound's **functional form** is target-independent; its `×42` **verdict** is
conditioned on the two numbers `(κ, sin θ̄) = (T₂, sin θ̄_*)` it is evaluated at (v3.4 typing); and it is reusable: **`G₄m² ≥ πκ/(2c′ sin θ̄(1−κ))` is the price of
admission for a boundary record on one edge band.**

### 21.5 Y2 and Y3, as found

- **Y2.** The fluctuation-corrected critical coupling of the 2+1 Gross–Neveu model is scheme- and
  cutoff-dependent — not a universal number. What is universal is the fixed point and its
  exponents. Anchors read at abstract level this session: one 2-component Dirac fermion is the
  `N = 2` Majorana chiral-Ising GNY theory with emergent `𝒩 = 2` supersymmetry
  (arXiv:1607.05316), and the GNY fixed points sit in bootstrap islands (arXiv:2210.02492).
  Fluctuations raise rather than lower the critical coupling; they cannot supply a factor 40
  *(D23)*.
- **Y3.** One query family on "chiral bag boundary + edge states + four-fermion / Gross–Neveu":
  `NOT_FOUND` in query scope. `NOT_FOUND` is not `ABSENT`; the mapping stays `OPEN-NOVELTY` *(D24)*.


---

## 22. Theorems 37–41 — the Goldstone route classified and closed at the spectral level, multi-band repaired and made unconditional on colour/charge, the candidate registry, the selector signature, and the thermal ceiling **(v2.9, REPAIRED in v3.0 after audit, extended in v3.1, RE-SCOPED in v3.2 after audit)**

> **Audit notice (v3.3).** The v3.2 audit (`AUDIT-RESEARCH-REOPEN`, targeted at the K9b quantitative
> conclusion; independence L3 other model family + L5 deterministic re-execution and counterexample) found:
> **S3** — Proposition 39.6's eigenvalue bracket was carried, without a theorem, from the flavour matrix `D` to
> Theorem 36's *physical* admission bound, which was derived for one band, one mass, one gap, one density, one
> `⟨E⁻¹⟩` and the filled-disk extremiser; Theorem 39 could transfer it to several bands only because a diagonal
> mean field decouples the gap equations, and K9b breaks exactly that. Corollary 39.7's "`n_c/n_t ≈ 2.16×10⁷`
> needed" further dropped the charm diagonal `D_cc`; a rank-one positive family with `D_cc` kept reaches
> `λ_max/D_tt = 42.07` at `r ≈ 7.4×10⁵`. **S2** — the four-file package the auditor received lacked the baseline
> ledger (G18 DEGRADED, exit 2); G20/G23 passed two semantic injections; G21 was a declaration. **S1/S2** —
> Elitzur's scope; the sign of `κ`; A1–A5 defined only by reference; "RQ1→RQ3" for an RQ2→RQ3 handoff;
> Prop. 39.6 marked NEW without a prior-art sweep; the title. **All findings are accepted; none is rejected.**
> §22.8 is rewritten: the algebra of Prop. 39.6 stays (C99a–c), its physical reading is typed OPEN (D36, Proof
> obligation 39.8), the audit's counterexample family is reproduced (W16), and **K9b returns to OPEN**.
> FREEZE-CANDIDATE stays **WITHHELD**.

> **Audit notice (v3.2).** The v3.1 audit (`AUDIT-RESEARCH-REOPEN`; reopened scope: Theorem 39.4 in §22.8,
> the handoff of §22.9, and the release package — not §22 as a whole) found: **S3** — Theorem 39.4's
> quantifier over-reaches: C96 proves gauge-variance for colour-off-diagonal and charge-changing bilinears
> only, while same-gauge-representation generation-flavour bilinears (`ū Γ c`, `d̄ Γ s`, `ē Γ μ`; colour
> contracted to a singlet) are gauge-invariant and are not excluded by Elitzur, so "K9 closed" and "the
> diagonal mean field is a theorem" are over-quantified and enter the FREEZE-CANDIDATE chain; **S2** —
> Corollary 41.2's "selecting the record value = discharging `D-S14-EVENT-001`" exceeds what Theorem 41
> supplies (a temperature is one component of the missing selector), and "the RQ3 and RQ2 residues coincide"
> exceeds what Mission v1.4 §4.2 allows without a common action or compatibility theorem; **S2 (scope)** —
> Theorem 38.3's "arbitrary local `α(x)` with fixed bag domain; no `η`/inflow term" needs a domain-preservation
> proof that is not given; **S1** — `T₂` used with two types (Bloch dephasing time vs. Z-Spin target); artifact I
> printed as 37 rows in §26–27 against 38 in the banner; the OPEN-DEBTS block still listed the off-diagonal
> condensate as a survivor after claiming it closed; **package** — the delivered v3.1 package does not reproduce
> a clean run (no v3.0 ledger; and, found here, no lineage sibling either). **All findings are accepted; none is
> rejected.** §22.8 is split (K9a closed / K9b open, computed once in Prop. 39.6), §22.9 is re-scoped, §22.7's
> Fujikawa sentence is narrowed (Cor. 38.7), the notation is type-locked (`τ₁, τ₂` for relaxation, `T₂` for the
> target), and §22.10 is rewritten. FREEZE-CANDIDATE is **WITHHELD**. Everything below that is unchanged from
> v3.1 is left as written.

> **Audit notice (v3.0).** The v2.9 audit (`AUDIT-RESEARCH-REOPEN`, scope §22) found an S3 defect in
> Theorem 38 (a type jump from the *scalar* on-shell space of Theorem 27 to *vector* currents; no
> current built, no divergence checked; no anomaly/inflow exclusion), an S2–S3 defect in Theorem 39
> (`dim E₊ = 2` is a fibre dimension, not a band count; the `1/N_b` scaling assumed identical bands
> sourcing one channel and **contradicted §25 item 19 of v2.8**), a mis-typed C88 (string count, not a
> certificate), a weak C85 wording, a stale docstring, and an exit-0-on-DEGRADED package. **All findings
> are accepted; none is rejected.** This section is rewritten. Theorem 37 survives strengthened; Theorem
> 38 becomes a classification with an exact part and a conditional part; Theorem 39 becomes a
> multiplicity lemma plus a channel-structure theorem whose conclusion is *stronger* than v2.9's in the
> no-go direction but *narrower* in scope; the "corpus-wide" closure and `TERMINAL-IN-SCOPE` are
> **WITHDRAWN**. Everything here is `DERIVED-CONDITIONAL` on the `ZS-M66` identification where numbers
> appear, exact where they do not, and Horn A inherits the **mean field** and A5 scope of Theorem 13.

### 22.0 Breakthrough record — repair pass, run before external collision

```text
FREEZE (v3.0)
  TARGET:   repair Thm 38 (Horn B) and Thm 39 (multi-band) so that every quantifier is owned by a
            certificate; replace C88 by a computed registry; extract the selector signature
  RESIDUE:  (i) which fermion CURRENT the corpus Goldstone can contract with, and whether it is
            conserved INCLUDING the boundary flux; (ii) whether one Dirac field can carry more than one
            edge band, and whether N fields share one record channel
  HARD:     Thms 9, 13, 15, 21, 23, 26, 27, 28, 33, 36; C38, C47, C50, C54, C66, C70, C78
  SOFT:     the U(1)_Phi charge assignment of the seam fermion (vector / axial / neutral) -- all three
            are computed; the colour/flavour-diagonality of the boundary mean field -- named, not assumed
  UNKNOWN:  the quantum axial Jacobian with boundary (eta/inflow) outside A4
  FORBIDDEN: re-closing Horn B by fiat; keeping a scaling that v2.8 sect.25 already contradicted
  SUCCESS OBSERVABLE: a bilinear atlas that says which currents exist on L_theta; a divergence
            identity on shell; an ideal computation for the band count; a Fock block computation

ROUTE-16 / B03 TYPE REPAIR + B18 OBSTRUCTION->OBJECT   (Horn B)
   "Which current?" is a type question: compute ALL sixteen bilinears on L_theta, derive the Noether
   current of each shift type, differentiate on shell.  KILL TEST: a nonzero, non-removable coupling
   of the Goldstone to the record -> FOUND for the tangential GRADIENT (boundary-localised, flip-odd);
   NOT found for linear bulk couplings.  Outcome: classification, not no-go.
ROUTE-17 / B05 AXIS SPLIT   (multi-band)
   Split "how many bands per field" (spectral) from "do bands share a channel" (interaction).
   KILL TEST 1: a second Jost zero -> NONE (C91).  KILL TEST 2: an off-diagonal Fock block in a
   diagonal mean field -> NONE (C92).  Outcome: the bound is per band; N_b is not a knob.
ROUTE-18 / B18 OBSTRUCTION->OBJECT   (selector signature)
   From Thms 20, 21, 25.1, 26.1, 27 and the atlas, write the signature of the missing object and run
   the three Mission kill tests on the corpus chain (W14).  Outcome: BT-REFORMULATED (sect.22.5).
NO-GO EMISSION GATE (kernel sect.5.5), applied to the REPAIRED verdict:
   SIGN        the gate asked "does the corpus select thetabar"; what is computed is the coupling
               of each corpus mediator to the record, and its size.                              PASS
   QUANTIFIER  C86/C89/C90 universal in (theta, alpha, m, theta_m); C91 universal in (m,k,E,theta);
               C92 universal in the two-point function; V30 quantifies over the REGISTRY only.  PASS
   SOURCE      external: Noether's theorem, the Dirac algebra, the Fock structure, the ZS-S14
               normalisation.  The v2.9 closure was partly our framing (the 1/N_b model) and is
               withdrawn on exactly that ground.                                                  PASS
   VALUE       erases the linear-Goldstone and multiplicity search spaces exactly; names two new
               survivors with signatures; leaves a conditional survivor with its condition.       PASS
```

### 22.1 Theorem 37 — Horn A: making the angle dynamical drives it to `π` (strengthened)

**Theorem 37 (Horn A, `Φ_Z = Φ`).** On this horn the Yukawa mass phase *is* the Goldstone, so
`θ̄ = θ_boundary + θ_m` is a **dynamical field**, and the potential it feels is the boundary effective
action `Γ(A)`, `A = m cos θ̄`, of Theorem 13. By the chain rule,

```
        ∂Γ/∂θ̄  =  − m sin θ̄ · Γ′(A) ,
        ∂²Γ/∂θ̄² =  − m cos θ̄ · Γ′(A)  +  m² sin²θ̄ · Γ″(A) ,
```

and `Γ′(A) > 0` on `[−m, m]` because, modulo `C² + S² = 1`, the Jost factor obeys the exact identity

```
        ( κ(p) + A )( κ(p) − A )  =  p²  +  m² sin²θ̄ ,          κ(p) − A ≥ κ(p) − m ≥ 0 ,       (C93)
```

so the integrand `(κ(p)+A)^{-1}` is strictly positive everywhere except the single point
`p = 0, θ̄ = π`. Hence the stationary set on `[0, 2π)` is **exactly `{0, π}`**, and

```
        ∂²Γ/∂θ̄² |_{θ̄=π} = + m Γ′ > 0   (minimum),        ∂²Γ/∂θ̄² |_{θ̄=0} = − m Γ′ < 0   (maximum).   (C85)
```

**`θ̄ = π` is the unique minimum**: the point that Shapiro–Lopatinski excludes (Theorem 22), at which
the surface gap `m|sin θ̄|` closes (Theorem 15) and `κ = 0` (Theorem 23). ∎

**Corollary 37.1.** Promoting the angle from parameter to field does not create a selector; it returns
the boundary to the excluded point and does so as a minimum, not merely a stationary point. Inside A5:
`CLOSED-NEGATIVE`. Outside A5: the v2.3 counterterm question, unchanged and not weakened *(D29)*.

**Remark.** Three independent structures — regularity (Thm 22), the gap (Thm 15/23), and the
effective potential (Thm 13 + 37) — single out `θ̄ = π`. **The record sits where the action does not
want it.** *(This remark survives the audit unchanged; what the audit asked for was the one sentence
about the extremum type, now supplied.)*

### 22.2 Lemma 38.0 and Theorem 38 — Horn B: the Goldstone current classification

The v2.9 argument contracted `∂_μθ` with an element of Theorem 27's *scalar* space. That space does
not contain a current. The correct object is the set of **tangential-vector and normal** bilinears on
the boundary subspace, which Theorem 27 never classified. Here it is.

**Lemma 38.0 (the boundary bilinear atlas; universal in `θ`).** Let `Ψ_θ` be the basis of `L_θ` of
Theorem 14.1, normalised as in Theorem 27 (`Ψ†Ψ = 2·1`), and let `X_θ = −sin θ σ_x + cos θ σ_y` be the
boost generator of Theorem 21 and `Y_θ = cos θ σ_x + sin θ σ_y` its rotation by `π/2`. For every one
of the sixteen Hermitian Dirac bilinears `ψ̄Γψ`:

```
   grading-EVEN, along J_E          ψ̄ψ = 2 sin θ J_E     ψ̄ iγ₅ ψ = 2 cos θ J_E     ψ̄γ³γ₅ψ = 2 J_E
   grading-EVEN, along 1            ψ̄γ⁰ψ = 2·1          ψ̄σ⁰³ψ = 2 cos θ ·1       ψ̄σ¹²ψ = 2 sin θ ·1
   grading-ODD (flip family)        ψ̄γ¹ψ = 2 X_θ        ψ̄γ²ψ = 2 Y_θ
                                    ψ̄σ⁰¹ψ, ψ̄σ⁰²ψ, ψ̄σ¹³ψ, ψ̄σ²³ψ  =  flip elements at angle 2θ
   ZERO                             ψ̄γ³ψ = 0            ψ̄γ⁰γ₅ψ = ψ̄γ¹γ₅ψ = ψ̄γ²γ₅ψ = 0
```

*(C90: 16/16 matched exactly; `{X_θ, J_E} = {Y_θ, J_E} = 0`.)* ∎

Three facts in this table carry the rest of the section. **(a)** The whole 16-dimensional bilinear
space collapses on `L_θ` onto `span{1, J_E, X_θ, Y_θ}`. **(b)** The **tangential axial current vanishes
identically** on the chiral-bag boundary, while the **normal axial flux is `2J_E`** — the record
observable itself: axial charge leaves the bag *through* the record. **(c)** The only bilinears that
reach the grading-odd flip family — the family whose breaking Theorem 25.1 makes necessary for a
biased unique stationary state — are the **tangential spatial vector currents** `ψ̄γ^{1,2}ψ` and four
tensors. Nothing in the scalar class of Theorem 27 does. *(This is the first universal statement of
this line about what a boundary coupling must contract with in order to be able to bias the record.)*

**Theorem 38 (Horn B, `Φ_Z ≠ Φ`; classification).** Let the seam fermion transform under the `U(1)_Φ`
whose Goldstone is `θ` as `ψ ↦ e^{iα(q_V + q_A γ₅)}ψ`, so that its Noether current is
`J^μ = q_V ψ̄γ^μψ + q_A ψ̄γ^μγ₅ψ`. On shell, for every `(m, θ_m)` *(C89)*:

```
        ∂_μ( ψ̄γ^μψ )    =  0 ,                      ∂_μ( ψ̄γ^μγ₅ψ )  =  2 i m ψ̄ γ₅ e^{iθ_mγ₅} ψ .
```

**(V) Vector charge, `q_A = 0` — EXACT decoupling of the linear coupling.** The bulk derivative
coupling `q_V ∂_μθ J_V^μ` is a total derivative, its boundary flux `ψ̄γ³ψ` vanishes on **every**
admissible `L` (isotropy; C70, C90), and the shift acts on the carrier as a scalar phase fixing `J_E`
and `X_θ`. The field redefinition `ψ ↦ e^{iq_Vθ}ψ` removes the coupling entirely. No coefficient
enters. There is no vector anomaly. *(C86, C89, C90.)*

**(A) Axial charge, `q_A ≠ 0` — record-blind at zeroth gradient order; not an exact Goldstone.** The
axial current is not conserved, and its normal flux on `L_θ` is `2J_E`: integrating by parts,

```
   ∫_M q_A ∂_μθ J_A^μ  =  2 q_A ∮_∂ θ · J_E   −   q_A ∫_M θ · 2im ψ̄γ₅e^{iθ_mγ₅}ψ ,
```

so the Goldstone reaches the record **directly through the axial boundary flux**. But the boundary
term and the bulk term are the two halves of one object: under `ψ = e^{iαγ₅}ψ′` the boundary angle of
`ψ′` is `θ − 2α` and its mass phase `θ_m + 2α` (Theorem 9, Corollary 9.2; re-certified in C86), so the
invariant `θ̄` is unchanged, and the shift acts on the carrier as `e^{iαJ_E}`, which fixes `J_E` (C50).
Hence for a Goldstone constant along the boundary (`∂_aθ = 0`, `a = 0,1,2`, any normal profile or
time dependence) **`κ` and `θ̄` are untouched**. What survives is order `∂_aθ`. Moreover the mass
term breaks the shift explicitly, so on this branch `θ` is a pseudo-Goldstone whose bulk potential is
`θ_b`-independent; the boundary potential is that of Theorem 37. *(C86, C89, C90; the quantum axial
Jacobian with boundary is **not** computed — see Cor. 9.2, [열림] outside A4.)*

**(N) Neutral, or the residual of (V)/(A) — the STRUCTURAL SURVIVOR.** Shift symmetry permits, for any
charge, (i) bulk operators of dimension `≥ 6` such as `(∂θ)²ψ̄ψ/f²`, and (ii) **boundary-localised
gradient terms** `∮ (c/f) ∂_aθ_can ψ̄γ^aXψ`. By Lemma 38.0 the tangential spatial part of (ii) acts on
the carrier as

```
        (c/f) ( ∂_1θ · X_θ  +  ∂_2θ · Y_θ )      —  a GRADING-ODD, flip-family element,
```

i.e. exactly the kind of term Theorem 25.1 requires and Theorem 27's class cannot supply. This class is
**not removable** and its coefficient `c` is not fixed by symmetry. It is the one place in the corpus
where the Goldstone can bias the record. ∎

**Corollary 38.1 (the conditional closure of the survivor).** `ZS-S14`'s normalisation
`½M_P²|D_μH₅|²` fixes `f = M_P`. Then (i) misses Theorem 36 by `(M_P/m_t)²/19.34 = 1.04 × 10³¹`
*(V28)*, and (ii) must compete with the edge gap `Δ = m_t sin θ̄_* = 141.6 GeV`, requiring a Goldstone
gradient `|∂θ_can| ≳ fΔ/c = 3.4 × 10²⁰ GeV²` whose energy density exceeds `m_t⁴` by `6.8 × 10³¹`
*(V31)*. No corpus background supplies this. **Horn B is therefore `CLOSED-NEGATIVE` for the linear
bulk couplings (exactly) and `CLOSED-NEGATIVE-CONDITIONAL`, on `f = M_P`, for the survivor.** The
survivor's condition is named: a Goldstone normalisation other than `M_P`, or a corpus-external
background gradient.

**Corollary 38.2 (what v2.9 got right and wrong).** Right: the on-shell scalar space is two-dimensional
and the shift preserves both of its elements. Wrong: that this closes the coupling — the derivative
coupling lives in the *vector* sector, which the scalar collapse does not see. The repaired statement
is stronger where it is exact (a Noether identity with the boundary flux computed) and honest where it
is not (a named, bounded, conditional survivor). *`NC-M67.35` is replaced by `NC-M67.38`.*

### 22.3 Lemma 39.0 and Theorem 39 — multi-band: one field, one band; one band, one channel

**Lemma 39.0 (edge-band multiplicity of one Dirac field; universal).** For the decaying ansatz
`ψ = u e^{−κx³} e^{−iEt + ik_⊥·x}` on the shell `κ² = k_⊥² + m² − E²`, the chiral-bag condition has a
nonzero solution iff the `2×2` minors of `P_−(θ̄)` restricted to `ker D` vanish. Their ideal, together
with the shell ideal, contains `(E + m)(κ + m cos θ̄)` in the chart valid for `E ≠ −m` and
`(E − m)(κ + m cos θ̄)` in the chart valid for `E ≠ m`. Hence the **only** localisation rate is
`κ = −m cos θ̄` (Theorem 15), and there the solution space has rank **exactly one**. One Dirac field
carries one edge state per `(k_⊥, sign E)` (Theorem 26) and **no second band**. *(C91, Groebner over
`ℚ(i)`, two charts.)* ∎

`dim E₊ = 2` (C38) is the dimension of the carrier *fibre*; it never was a band count. Extra bands can
come only from extra **fields** — colour, flavour, or a corpus-external sector.

**Theorem 39 (multi-band channel structure).** Let `N_b` Dirac fields share the boundary and couple
through the scalar contact term `(Σ_i ψ̄_iψ_i)²` of Lemma 36.1, and let the boundary mean field be
colour/flavour-**diagonal**, `G = diag(G_1, …, G_{N_b})`. Then the Fock operator `MGM` is
block-diagonal with vanishing off-diagonal blocks, and the `d`-channel coefficient
`¼ Tr(Nγ₅ F_ii)` of band `i` is a function of `G_i` **alone**; the Hartree term `Tr(MG) = Σ_i Tr G_i`
sums over bands but feeds the scalar `(a,b)`-plane, which is the reflection of Theorem 33(a), not the
record channel. Consequently the admission predicate is

```
        max_i  G₄,ᵢ m_ᵢ²   ≥   π κ / ( 2 c′ sin θ̄ (1 − κ) ) ,                      (C87, C92)
```

**independent of `N_b`.** ∎

**Corollary 39.1 (the numbers, retyped).** There is no "required `N_b`"; v2.9's `N_b ≥ 42.07` is
**withdrawn as moot**. The per-band shortfalls of §21.3 stand: top `42.1×`, bottom `1.2 × 10⁸×`, charm
`1.4 × 10¹⁰×`, tau `3.7 × 10⁹×` — unchanged by colour (3) or the weak doublet (6) *(V27)*.

**Corollary 39.2 (direction of the correction).** v2.9's `1/N_b` scaling was *favourable* to the
multi-band route and wrong; the repaired statement is *less* favourable. But its scope is narrower: it
assumes a diagonal mean field. **The named survivor is a colour/flavour-off-diagonal boundary
condensate `⟨ψ̄_iΓψ_j⟩ ≠ 0`, `i ≠ j`** — for colour, a boundary that breaks `SU(3)_c`. No such object
exists in `ZS-S14 v2.1`; it is registered as corpus-external (registry K9). *(v3.2: split into K9a — closed
by gauge invariance — and K9b, same-representation generation-flavour coherence, which is gauge-invariant,
IS a corpus object, and is open; see §22.8.)*

### 22.4 The candidate registry and the standing filter (Theorem 39.3, replacing 39.2/C88)

v2.9's C88 counted four hard-coded strings. v3.0 replaces it by a machine-readable registry in which
**every** entry carries `source / mediator / coupling class / band data / coefficient / status` and the
admission predicate of Theorem 39 is **computed** by the verifier for every entry that carries a corpus
number *(V30; integrity guard C88, retyped `C → G`)*.

| id | candidate (source) | mediator / coupling | `G₄m²` | status |
|---|---|---|---|---|
| K1 | top wall, `N_b = 3` (S14/M66 Yukawa) | Higgs contact, Fierz `d`-channel | 0.460 | REJECTED-BY-BOUND |
| K2 | weak doublet, `N_b = 6` | same, diagonal mean field | 0.460 | REJECTED-BY-BOUND |
| K3 | bottom / charm / tau | same | `1.6 × 10⁻⁷` | REJECTED-BY-BOUND |
| K4 | Goldstone `θ`, Horn A | non-derivative via mass phase | — | REJECTED-STRUCTURAL (C85) |
| K5 | Goldstone `θ`, Horn B, vector charge | linear bulk derivative | 0 | REJECTED-STRUCTURAL (C86 V) |
| K6 | Goldstone `θ`, Horn B, axial charge | linear bulk derivative + axial flux `2J_E` | 0 | REJECTED-STRUCTURAL (C86 A) |
| K7 | Goldstone `θ`, shift-symmetric residual | dim ≥ 6 / boundary gradient, flip-odd | `1.9 × 10⁻³⁰` | REJECTED-BY-BOUND, **conditional on `f = M_P`** |
| K8 | non-SM fermion heavier than its mediator (§21.4 ii) | non-contact | — | EXTERNAL-UNEVALUABLE |
| K9a | colour-off-diagonal or charge-changing boundary condensate (`t`–`b`) | contact, C92 hypothesis violated; gauge-**variant** | — | ~~EXTERNAL-UNEVALUABLE~~ **REJECTED-STRUCTURAL (Thm 39.4; quantifier corrected v3.2)** |
| K9b | same-representation generation-flavour coherence (`t`–`c`, `t`–`u`; colour singlet) **(split off in v3.2)** | contact, off-diagonal Fock block `y_t y_c G_tc` (C99a); gauge-**invariant** | — (Theorem 36 does not apply to a coherent carrier) | **OPEN** (v3.3; Proof obligation 39.8 — the v3.2 conditional rejection is withdrawn) |
| K10 | record value below `T₂` (§21.4 iv) | — | — | NOT-A-CANDIDATE (excluded by the identification) |

**Theorem 39.3 (the standing admission filter, as a computed predicate).** A future boundary-record
candidate is admitted only if it is registered with all six fields and, for each of its bands, satisfies
`G₄,ᵢ m_ᵢ² ≥ πκ/(2c′ sin θ̄(1−κ))` with a corpus-supplied coefficient; entries without a corpus number
are typed `EXTERNAL-UNEVALUABLE` and are **not** counted as closed; entries whose carrier is outside
Theorem 36's hypothesis are typed `OPEN`. Applied to the registry (v3.3, 11 entries): `0` admitted; `6`
entries carry a corpus number and all fail the bound (K5, K6 with coefficient `0`; K7 conditionally); `4`
are structurally rejected by a certified rule (K4–K6, K9a; overlapping K5, K6); `1` is external (K8); `1` is
a conditional rejection and is **not counted as closed** (K7); `1` is **OPEN** with no admission criterion
(K9b); `1` is not a candidate. **The quantifier the verifier owns is "every registered candidate", and it says
so** *(V30)*.

### 22.5 Definition 40 — the minimal selector signature, the kill tests, and the handoff

The audit asked for a "minimal selector signature" stronger than a `y m/M` window. Mission v1.4 RQ3
requires an *action-derived, non-phase-covariant, genuinely external* seam environment that selects
the instrument and a definite Born-weighted record. From Theorems 20, 21, 25.1, 26.1, 27 and Lemma
38.0, the signature is:

```text
DEFINITION 40  (admissible boundary-record sector)
  S1  ACTION-DERIVED   mediator and coupling appear in the Z-Spin action; no coefficient, state or
                       branch is read from lambda or T_2
  S2  EXTERNAL         a boundary rest frame (A6) AND a grading-ODD (flip-family) component --
                       Thm 21/25.1: a unique stationary state with kappa != 0 needs flip breaking;
                       Lemma 38.0: only tangential vector data supply it
  S3  ADMITTED         each band passes the per-band bound of Theorem 39 (C87)
  S4  FAITHFUL+BIASED  the record state is mixed with kappa != 0 (Cor. 14.2, 15.3)
  S5  POINTED          the record direction is derived: J_E, by the residual rotation (Thm 20)
  S6  DEFINITE         a definite record with Born weighting  [not addressed in this paper]
KILL TESTS  (Mission, applied on the carrier)
  K1  the action leaves several instrument directions          -> FAIL
  K2  the reduced dynamics is flip-covariant                    -> FAIL  (Thm 25.1: kappa = 0)
  K3  a coupling or state must be tuned to lambda or T_2         -> FAIL
```

**Witness W14 (the corpus chain against K1–K3, one qubit).** *(a)* The Theorem-27 channel alone — a
jump operator `∝ J_E` — is **QND dephasing**: its stationary manifold is the whole `J_E`-diagonal
family (dimension 2). The pointer is fixed (S5 holds, K1 passes) but **no record value is selected**.
*(b)* Rest-frame thermal damping in the `J_E` basis (the environment of Theorem 26.1) has a **unique
faithful** stationary state with `κ = −tanh(Δ/2T)` exactly (S2, S4 hold; K2 passes because the damping
is flip-odd). *(c)* A flip-odd Hamiltonian term `εX_θ` — the on-shell image of a tangential vector
datum — keeps uniqueness and moves `κ` continuously (`−0.905 → −0.770 → −0.307` at `ε/Δ = 0, 0.3, 1`).
*(d)* **K3 fails**: reaching `|κ| = T₂` in (b) (`κ = −T₂` in the `z₀` sign convention) needs `Δ/T = 2 artanh T₂ = 2.411`, a number read from `λ`
(the band-ensemble form of the same statement is Corollary 26.3's `x_* = 5.08`).

**Corollary 40.1 (the handoff; `BT-REFORMULATED`, [가설] for the physical reading).** On this route
the corpus chain supplies **S5** (pointing, derived), the necessary halves of **S2** and **S3** (as
theorems), and **S1** for the chain but not for its coefficient (which fails S3 inside the corpus). It
does not supply **S4** on a named sector or **S6**. What is left is precise: **the record *value* is set
by a rest-frame datum** — `Δ/T`, or a flip-odd tangential datum such as a Goldstone gradient — and
selecting it target-blind is the same problem as deriving the seam rest frame's clock/temperature from
the action. **At this point the RQ3 residue and an RQ2 residue coincide** — *(v3.2: read as [가설] per
Remark 41.4: the RQ2 clock/rest-frame construction may supply one input of the RQ3 selection; no
identification is asserted)*. Mission Architecture C (common-action co-emergence) is the reading in
which this is not a coincidence; it is not asserted here. The positive construction `S_Z → E_ext → 𝒥_phys → definite record` therefore starts from a
tangential-vector or thermal boundary datum derived from `S_Z`, and its cheapest kill tests are K1–K3
as run in W14. **No identifier is assigned or reserved for that work.**

### 22.6 Status map after the repair (v3.0) — moved to the supplement

Superseded by §22.10; kept verbatim as supplement §S22.6 together with Corollary 40.2 (v3.0).

### 22.7 Theorems 38.3–38.4 — the axial Jacobian with boundary, closed inside A1–A4 for constant rotations **(new in v3.1; scope narrowed in v3.2)**

v3.0 left one item of Theorem 38(A) open: whether a quantum Jacobian — an `η`-invariant or an inflow
term at the boundary — could distinguish two pairs `(θ_m, θ_b)` with the same invariant `θ̄`, and so
give the axial-charged Goldstone a record coupling that the classical rotation argument misses. Two
theorems address it, in the Lorentzian half-space problem where this paper lives (Remark 4.1): the first
is a spectral cancellation, the second a unitary equivalence for **constant** rotations. What they do
*not* cover — the Jacobian of a **local** rotation `α(x)` against a fixed bag domain — is stated in
Corollary 38.7 (v3.2 scope correction).

**Theorem 38.3 (the `H²`-regularised axial density vanishes pointwise; universal in `(θ, θ_m, m)`).**
Let `𝒞ψ = iγ²ψ*` be the charge conjugation of Theorem 24. Then *(C94)*:

```
   𝒞 γ₅ 𝒞⁻¹ = −γ₅ ,        (𝒞φ)†γ₅(𝒞φ) = −φ†γ₅φ   for every spinor φ ,
   𝒞 L_θ = L_θ  for every θ ,        𝒞 H 𝒞⁻¹ = −H   (kinetic and mass parts separately, every θ_m).
```

Hence `𝒞` maps the eigenspace of `H` at `E` onto the one at `−E`, and for every regulator `f(H²)` the
regularised axial density

```
   𝒜_f(x)  :=  Σ_n f(E_n²) φ_n(x)†γ₅φ_n(x)   =   Σ_{E_n>0} f(E_n²) [ φ_n(x)†γ₅φ_n(x) + (𝒞φ_n)(x)†γ₅(𝒞φ_n)(x) ]   =   0
```

**pointwise**, on the boundary as in the bulk (the continuum is handled identically through the local
spectral measure, which `𝒞` pairs). ∎

> **v3.2 scope correction (audit, S2).** v3.1 continued: *"The Fujikawa Jacobian of a local axial rotation
> `ψ ↦ e^{iα(x)γ₅}ψ` with the chiral-bag domain held fixed is therefore `exp(−2i∫α𝒜_f) = 1` for every `α(x)`,
> inside A1–A4. No `η` or inflow term survives."* That sentence is **withdrawn as stated**. Theorem 38.3 is a
> statement about the spectral supertrace of the self-adjoint operator `H` on its domain `dom H` (the
> chiral-bag condition). Reading it as the Jacobian of a *local* change of variables requires that
> `e^{iα(x)γ₅}` map `dom H` into itself — which it does not in general, since at the boundary
> `e^{iα(0)γ₅}` rotates `L_θ` to `L_{θ−2α(0)}` (C86) — or a separate treatment of the boundary Jacobian;
> neither is supplied here. See Corollary 38.7.

**Theorem 38.4 (spectral `θ̄`-invariance; universal).** `U = e^{iαγ₅}` is unitary on `L²(ℝ³₊, ℂ⁴)`,
fixes the kinetic matrices `γ⁰γ^k`, sends the mass matrix `γ⁰me^{iθ_mγ₅}` to that of `θ_m + 2α`, and
maps `L_θ` onto `L_{θ−2α}` *(C95; the last two are C86's identities, the first is new)*. Hence

```
   U† H(θ_m, θ_b) U  =  H(θ_m + 2α, θ_b − 2α) ,        U† dom H(θ_m, θ_b)  =  dom H(θ_m + 2α, θ_b − 2α) ,
```

a unitary equivalence of self-adjoint operators. Every spectral function — heat trace, `ζ`, `η`,
density of states, determinant, the pushforward of any spectrally defined state — coincides for the two
operators, so **any spectrally regularised effective action is a function of `θ̄` alone**, and the
co-rotating Jacobian of a constant axial rotation is exactly `1`. ∎

**Corollary 38.5 (Theorem 38(A), quantum half; re-scoped in v3.2).** Combining: the axial-charged
Goldstone's linear bulk coupling, for a Goldstone **constant along the boundary**, acts on the boundary data
as a rotation that (i) leaves the classical invariant `θ̄` fixed (Cor. 9.2), (ii) fixes the record `κ` on
the carrier (C50), (iii) has trivial co-rotating Jacobian (Thm 38.4), and (iv) produces no `H²`-regularised
axial density at the boundary (Thm 38.3). **Inside A1–A4 the statement "record-blind at zeroth gradient
order" is exact at the level of spectrally regularised effective actions.** For a Goldstone that varies
along the boundary the relevant transformation is local, and the quantum statement is not made (Cor. 38.7);
the classical order-`∂_aθ` survivor is K7 as before. Outside A4 (gauge fields), the bulk `F F̃` anomaly
returns and the statement is not made.

**Corollary 38.7 (what remains open at the quantum level; v3.2).** The Jacobian of a **local** axial
rotation `α(x)` against a fixed chiral-bag domain — the object a boundary `η`/inflow term would live in — is
**not computed here**. Theorem 38.3 shows that the `H²`-regularised density it would integrate vanishes;
it does not show that the transformation is a change of variables on `dom H`, nor that the boundary
Jacobian of the domain rotation `L_θ → L_{θ−2α(0)}` is trivial. This is recorded as an **[열림] proof
obligation** of Theorem 38(A) at order `∂_aθ`, alongside — and distinct from — the Euclidean boundary
anomaly of the Remark below, which is not transported.

**Remark (the Euclidean boundary anomaly is a different object).** The boundary contribution to the
chiral anomaly for bag boundary conditions is known in the Euclidean, `D̸²`-regulated setting
(Marachevsky–Vassilevich, arXiv:hep-th/0309019, read at abstract level this session, D32). That result
concerns a Euclidean operator whose boundary condition and regulator are not those of this paper
(Remark 4.1 forbids transport in either direction), and it is neither used nor contradicted here.
Theorem 38.3 says only that the Lorentzian `H²`-regulated density vanishes by `𝒞`; it does not claim
that every regularisation of the Euclidean problem does.

**Witness W15 and Observation 38.6 (a control that did not fire, reported as found).** A lattice
half-space model (40 sites, Wilson term, chiral-bag projection at site 0, `k_⊥ = (0.3, 0.4)`,
`θ_m = 0.4`) reproduces the conclusion of Theorem 38.3: symmetric spectrum, local supertrace
`≤ 2 × 10⁻¹⁶` at every site *(W15)*. The control designed to break the `𝒞`-pairing — a `𝒞`-even
potential `μ(x)`, which makes the spectrum asymmetric by `6.6 × 10⁻²` — **did not** raise the
supertrace, because on this lattice the axial density vanishes **level by level**:
`max_{n,x} |φ_n(x)†γ₅φ_n(x)| = 1.6 × 10⁻¹⁵`, robust under `x`-dependent mass, `x`-dependent `μ`, and
a second bag of different angle at the far end, and broken only by a generic polarisation-mixing
Hermitian perturbation (per-mode density `1.2 × 10⁻²`, supertrace `3.1 × 10⁻³`). We have **no proof**
of this level-wise vanishing: no pointwise unitary or antiunitary symmetry of the required type exists
(the commutant of `{α_k}` is `span{1, γ₅}`, and the antiunitary system is inconsistent), so it is
recorded as **Observation 38.6, [열림]**, a candidate lemma stronger than Theorem 38.3 (it would extend
the vanishing from `f(H²)` to every `f(H)`). Theorem 38.3 does not depend on it; its proof is C94's
algebra plus the spectral pairing.

### 22.8 Theorem 39.4 and Proposition 39.6 — K9 split: colour/charge-changing condensates are gauge-variant (K9a, closed); same-representation flavour coherence is not (K9b, OPEN) **(new in v3.1; re-quantified in v3.2; quantitative K9b conclusion withdrawn in v3.3)**

Theorem 39 assumed a colour/flavour-diagonal boundary mean field and registered the off-diagonal
condensate `⟨ψ̄_iΓψ_j⟩`, `i ≠ j`, as survivor K9. v3.1 wrote "the assumption is a theorem". The v3.1 audit
showed that this is true for exactly half of K9, and v3.2 splits it accordingly:

```
   K9a  gauge-CHANGING off-diagonal:   i, j in different colour states, or with different unbroken
                                       charges (t-b: Q_t - Q_b = 1)                     -> CLOSED (Thm 39.4)
   K9b  same-gauge-representation:     i, j in the same representation with the same unbroken charges
                                       (u-c, d-s, e-mu; colour contracted to a singlet)  -> OPEN (Prop. 39.6 is
                                       algebra only; no admission criterion, Proof obligation 39.8)
```

**Theorem 39.4 (K9a; exact + IMPORTED Elitzur; quantifier corrected in v3.2).** The commutant of
`su(3)` (all eight Gell-Mann generators) in `M₃(ℂ)` is `ℂ·1`, so the only gauge-invariant **colour**
bilinear `ψ̄_i M_{ij} ψ_j` has `M ∝ 1` (Schur, as in Theorem 2); every colour-off-diagonal elementary
bilinear `E_{ij}` transforms as `e^{i(φ_i−φ_j)}E_{ij}` under the Cartan torus and is gauge-variant *(C96)*.
By Elitzur's theorem (IMPORTED; scope stated precisely in v3.3) the expectation value of an **undressed
local** gauge-variant operator vanishes in every **gauge-invariant physical state** — equivalently under the
gauge-invariant measure — so a **colour-off-diagonal** boundary condensate of that type vanishes. Fixed-gauge
(unphysical) expectation values, gauge reductions induced by the boundary, and dressed non-local operators
are **outside** this statement and are not needed for K9a as registered (an undressed local bilinear at the
wall). For the weak doublet `(t, b)` the off-diagonal bilinear carries electric charge `Q_t − Q_b = 1 ≠ 0`
and vanishes by the same theorem for unbroken `U(1)_em`. **The theorem says nothing about a bilinear between
two fields of the same gauge representation and the same unbroken charges**: `ū Γ c` with colour contracted
to a singlet is gauge-invariant, and Elitzur does not apply. ∎

**Corollary 39.5 (re-scoped).** Colour-diagonality and charge-diagonality of the boundary mean field hold
in every gauge-invariant state. **Generation-flavour diagonality does not follow**, and Theorem 39's
per-band bound is therefore conditional on it. Registry entry K9 is split: K9a is
`REJECTED-STRUCTURAL` *(C96)*; K9b is registered as a corpus object (the Standard-Model generations exist
in `ZS-S14 v2.1`) and evaluated below *(V30)*. The v3.1 sentences "K9 is closed", "the diagonal mean field
is a theorem" and "the corpus-external survivor set shrinks to K8 alone" are **withdrawn**.

**Proposition 39.6 (the algebra of flavour coherence; exact — and only algebra).** Let two Dirac fields
`1, 2` with identical unbroken gauge charges couple through the Yukawa-induced contact term of Lemma 36.1,
whose flavour vertex is `M = diag(y₁, y₂) ⊗ 1₄` (the Yukawas differ, so the vertex is not flavour-blind), and
let the boundary two-point function be **flavour-coherent** and Hermitian, `G = [[G₁₁, G₁₂],[G₁₂†, G₂₂]]` with
`G₁₂ ≠ 0`. Then:

1. *(C99a)* the Fock operator `MGM` has the **nonzero** off-diagonal block `y₁y₂G₁₂` (and its adjoint) —
   Theorem 39's block-diagonality was a property of the diagonal mean field, not of the interaction;
2. *(C99b)* the matrix of `d`-channel coefficients `D_ij := ¼ Tr(Nγ₅ (MGM)_ij)` has diagonal entries
   `D_ii = ¼ y_i² Tr(Nγ₅G_ii)`, **unchanged** by `G₁₂`, off-diagonal entry `D₁₂ = ¼ y₁y₂ Tr(Nγ₅G₁₂)`, and
   `D₂₁ = D̄₁₂`: `D` is Hermitian;
3. *(C99c)* for any Hermitian `2×2` matrix `[[a, b],[b̄, c]]`, `max(a, c) ≤ λ_max ≤ max(a, c) + |b|`, with
   equality on the left iff `b = 0`. ∎

> **What Proposition 39.6 does not say (v3.2 audit, S3; accepted).** v3.2 continued: *"flavour coherence can
> therefore only raise a candidate's effective coefficient against Theorem 39's unchanged bound"*, and
> Corollary 39.7 then read `λ_max(D)` against `πκ/(2c′ sin θ̄(1−κ))`. That is a layer jump. Theorem 36 was
> derived for **one** edge band — one mass, one gap `Δ = m sin θ̄`, one density `n_∂`, one moment `⟨E⁻¹⟩`, and
> the filled-disk extremiser over Pauli-allowed occupations. Theorem 39 transferred it to several bands only
> because a **diagonal** mean field decouples the gap equations band by band. A flavour-coherent carrier breaks
> exactly that decoupling, and nothing in this paper supplies the objects that would carry the bound across:
>
> ```
>    coherent two-flavour carrier  →  matrix-valued gap equation  →  occupation constraint  →  admission criterion
> ```
>
> Missing: the joint dispersion of two bands with different masses `m_t, m_c` and different gaps; the composition
> of the record `κ` from the diagonal and off-diagonal density blocks; the Pauli occupation extremiser under
> coherence; a theorem placing `λ_max(D)` — or whatever functional replaces it — in the critical gap equation;
> and the admission criterion that results. These are recorded as **C99d** (`λ_max(D)` is the coherent carrier's
> critical coupling) and **C99e** (Theorem 36's bound is unchanged), both **OPEN** (D36), and as Proof obligation
> 39.8 below. The v3.2 sentences "unchanged bound", "a coherent charm band `~2 × 10⁷` times denser than the top
> band would be needed", and "K9b is REJECTED-BY-BOUND conditionally on `n_partner ≤ n_top`" are **withdrawn**.

**Witness W16 (the audit's counterexample family, reproduced; a witness, not a theorem).** Let `A = Nγ₅`
(a Hermitian involution), `u` a unit spinor with `u†Au = κ = T₂`, and `G = ww†` with `w = (u, √r·Au)` — a
rank-one **positive** block matrix, i.e. an object satisfying every hypothesis v3.2 declared. Then

```
        D / D_tt  =  [[ 1 ,  q√r/κ ],[ q√r/κ ,  q² r ]] ,        q = y_c/y_t ,        r = n_c/n_t ,
```

and solving `λ_max(D)/D_tt = 42.068` (the top shortfall of §21.3) gives **`r ≈ 7.44 × 10⁵`**, reproduced by
explicit construction (`λ_max = 42.06818`, `min eig G = −1×10⁻¹⁰`, positive to rounding). v3.2's
`r ≈ 2.16 × 10⁷` came from the off-diagonal entry alone: it **dropped the charm diagonal** `D_cc = q² r D_tt`,
which at `r ≈ 7.4 × 10⁵` is already `40.6 D_tt`. The family is not claimed to be a physical seam state; it shows
that positivity of `G` alone does not fix a required density ratio, and that neither number is an admission
criterion until Proof obligation 39.8 is discharged. *(W16.)*

**Corollary 39.7 (retyped; equal-density eigenvalue arithmetic, `DERIVED-CONDITIONAL` on C99d/e).** For the
charge-`⅔` partners of the top wall, *if* the flavour matrix `D` were the admission quantity, then at equal band
densities Cauchy–Schwarz on a positive `G` (`|Tr(Nγ₅G₁₂)| ≤ (Tr G_tt · Tr G_cc)^{1/2}`, `Tr(Nγ₅G_tt) = κ Tr G_tt`
on the record-carrying band) gives `|D₁₂|/D_tt ≤ (y_c/y_t)/κ = 0.885 %`, `D_cc/D_tt ≤ (y_c/y_t)²/κ = 6.5×10⁻⁵`,
hence `λ_max(D)/D_tt ≤ 1.0000782` (exact `2×2` eigenvalue of the two bounds; the crude bracket of C99c would give
`≤ 1.0089`) *(V33)*. This is arithmetic about a matrix whose physical role is OPEN; it is no
longer offered as a rejection of K9b, and it fixes no required density ratio (W16).

**Proof obligation 39.8 (K9b; the coherent two-band admission theorem — a research item, not a correction).**
To decide K9b one must prove, for two edge bands of masses `m₁ ≠ m₂` at a common boundary angle, coupled by the
Yukawa contact vertex `diag(y₁, y₂) ⊗ 1₄` in a flavour-coherent mean field: (i) the joint edge dispersion and the
carrier on which the record `κ` is defined; (ii) how `κ` is composed from the diagonal and off-diagonal blocks of
the boundary two-point function; (iii) the Pauli occupation extremiser at fixed `κ` under coherence (the
analogue of Theorem 36's filled disk); (iv) the critical gap equation and the functional of `D` (or of `G`) that
enters it; (v) the resulting admission criterion and its evaluation on the SM numbers. Until (i)–(v) exist,
**K9b is OPEN** and is registered as such (`OPEN`, class `corpus-open`; V30). No identifier is reserved for that
work. *(v3.4: §22.11 discharges (ii) and, at linear order about a flavour-diagonal reference, the need for (i); it closes
C99d negatively and reduces (iii)–(v) to the single computation of Proof obligation 39.8′. K9b remains OPEN.)*

**Remark (why this is still not a rescue).** Even open, what K9b offers is a flavour-mixed record carrier — a
coherent superposition of two edge bands — which changes `ZS-M66` Q11's one-qubit carrier and would have to
re-enter Definition 40 at S2–S5. It is a named survivor with a signature, not a candidate selection.

### 22.9 Theorem 41 — the thermal ceiling on the carrier record, and the A5 residue counted **(new in v3.1; notation type-locked and Cor. 41.2 re-scoped in v3.2)**

W14 showed, on one qubit, that the rest-frame thermal environment selects a unique record and that a
flip-odd tangential datum moves it. The closed form is exact and it bounds the record from above.

> **Type lock (v3.2; symbol table v3.3).** Throughout this paper `T₂ = |Im λ|/sin θ̄_* = 0.83538…` is the
> **Z-Spin target** record value (§12). The Bloch **relaxation times** of Theorem 41 are written `τ₁`
> (longitudinal) and `τ₂` (transverse). Earlier (v3.1) the target's glyph was used for both — a
> same-symbol/different-type error of the kind the project's TYPE LOCK rule forbids. Guard G23 now fails the
> run (a) if the target's glyph is used for a relaxation time anywhere in this subsection, and (b) if any
> sentence of this subsection that names a relaxation or dephasing time fails to name `τ₁`/`τ₂` or names the
> target's glyph (the v3.2 audit's injection); the guard reads the glyphs, not this paragraph's intent.

**Theorem 41 (thermal ceiling; exact in the Bloch variables; target-independent).** For the carrier class {`J_E`-thermal
damping with detailed balance (longitudinal time `τ₁`, equilibrium `z₀ = −tanh(Δ/2T)`), `J_E`-dephasing
(transverse time `τ₂ ≤ 2τ₁`), a static flip-odd Hamiltonian term `εX_θ` — the on-shell image of a
tangential vector datum, Lemma 38.0}, the Bloch equations

```
   ẋ = −Δy − x/τ₂ ,     ẏ = Δx − 2εz − y/τ₂ ,     ż = 2εy − (z − z₀)/τ₁
```

have the **unique** stationary record

```
   ┌──────────────────────────────────────────────────────────────────────┐
   │   κ  =  z₀ · (1 + Δ²τ₂²) / (1 + Δ²τ₂² + 4ε²τ₁τ₂) ,    |κ| ≤ tanh(Δ/2T) . │
   └──────────────────────────────────────────────────────────────────────┘
```

*(C97; reproduces W14's `−0.770215` at `ε/Δ = 0.3`.)* **A flip-odd tangential datum can only lower the
record below the rest-frame thermal value; it can never raise it.** ∎

**Corollary 41.1 (the rest-frame datum bounded; `DERIVED-CONDITIONAL`; sign fixed in v3.3).** Since
`z₀ = −tanh(Δ/2T)`, the stationary record of Theorem 41 is negative in this convention; the target condition
is on its magnitude, `|κ| = T₂` (i.e. `κ = −T₂`). *(Sign conventions across sections: §15 and §18 write `κ`
positive on the particle branch, `κ = +m sin θ̄/E`, and negative on the Dirac-sea branch (Thm 26.1); Theorem 41's
`z₀ = −tanh(Δ/2T)` is the thermal-ground sign. Which branch carries the target is a chiral-frame choice absorbed
into `θ_m` (Cor. 30.1), so every target condition in this paper is a condition on `|κ|`; earlier statements
written `κ = T₂` (§15, §16.4, §18, §23) are to be read that way.)* `|κ| = T₂` requires `tanh(Δ/2T) ≥ T₂`, i.e.

```
   T / Δ  ≤  1 / ( 2 artanh T₂ )  =  0.41470          (single-mode carrier; ε = 0 saturates it),
```

and the `k_⊥`-integrated band ensemble of Corollary 26.3 sharpens the equality case to `T/Δ = 0.19675`.
**Any seam rest frame warmer than `0.4147 Δ` cannot carry a record of magnitude `T₂` on this route, whatever tangential
datum it supplies** *(V32)*. **Typing (v3.4; v3.3 audit, S2).** The ceiling `|κ| ≤ tanh(Δ/2T)` of Theorem 41 is
**target-independent**; the number `0.4147` is **target-conditioned**, because it inserts `|κ| = T₂`. It is a necessary
*capacity* bound on the environment conditioned on the identification — an inequality on a temperature rather than on
a coupling — and that is what the handoff of Corollary 40.1 hands off. It is not a target-blind constraint.

**Corollary 41.2 (the handoff lands on a named upstream debt — as a necessary condition; re-scoped in
v3.2).** `ZS-S14 v2.1` was read in v3.1 (§2.11, §10.3.5, §14.1 item 4; D33): it supplies **no** rest-frame
temperature, clock or tangential vector, forbids tuning "a clock duration [or] a sector weight" to a
target, and registers the action-derived non-phase-covariant seam environment as debt
**`D-S14-EVENT-001`, OPEN**. What this paper supplies to that debt is **one necessary condition**:

```
   any thermal rest-frame route that discharges D-S14-EVENT-001 must satisfy  T/Δ ≤ 0.4147   (Cor. 41.1).
```

It is **not** its discharge. By Mission v1.4 RQ3 and Definition 40, a temperature/rest frame is one
component of the missing selector; what a discharge still requires is at least an action-derived
environment, a non-phase-covariant selector, a faithful biased stationary state on a named sector (S4),
the selection of the instrument, and a definite Born-weighted record (S6) — none of which Theorem 41
supplies (D30). The v3.1 wording *"selecting the record value on this route is exactly the discharge of
`D-S14-EVENT-001` by a rest-frame datum obeying Corollary 41.1"* is **withdrawn**.

**Remark 41.4 (RQ2 and RQ3; [가설]).** The datum Corollary 41.1 constrains is of clock/temperature type,
so the RQ2 clock/rest-frame construction *may* supply one input of the RQ3 environment selection. That is
the whole of what is asserted. Mission v1.4 §4.2 treats the commonality of the programme's selection
problems as a hypothesis and forbids identifying two selections without a common action or a
compatibility theorem; accordingly the v3.1 sentence "the RQ3 residue here coincides with an RQ2 residue"
is **downgraded to [가설]** and Corollary 40.1's "coincide" is to be read the same way. The inequality
itself is exact.

**Corollary 37.2 (the A5 residue, counted; universal).** The `A`-derivatives of the Jost integrand
alternate, `∂_A^k(κ(p)+A)^{-1} = (−1)^k k!(κ(p)+A)^{-k-1}` *(C98)*, so `Γ′ > 0, Γ″ < 0, Γ‴ > 0, Γ⁗ < 0`
on `(−m, m)`. With the counterterm freedom exactly a cubic in `A` (Theorem 13c), the renormalised
stationary equation `f(A) = Γ′(A) + c₁ + 2c₂A + 3c₃A² = 0` has `f‴ = Γ⁗ < 0`, hence at most one zero of
`f″`, two of `f′`, and **at most three roots** in `(−m, m)`: at most three off-`πℤ` stationary values of
`cos θ̄`. Landing on `A_* = m Re λ` and making it a minimum consumes one equation and one inequality,
leaving **exactly two real counterterm parameters** as the A5 residue. This is the complete statement
of what an upstream determination of the boundary counterterms must supply; nothing inside M67 supplies
it, and Theorem 37's `θ̄ = π` is the `c₁ = c₂ = c₃ = 0` member of that family.

### 22.10 Status map after v3.3

```text
F-M66.17 -- SELECTION OF THE CHIRAL-BAG ANGLE -- STATUS AFTER v3.4 (v3.3's map; K9b OPEN with its obligation narrowed)

  inside A1-A5, spectral routes                CLOSED-NEGATIVE, exact        (Thms 12, 13, 24)
  inside A4, boundary-interaction route        CLOSED-NEGATIVE, exact        (Thm 31)
  Yukawa contact, colour/charge-diagonal AND   CLOSED-NEGATIVE, conditional  (Thms 36, 39, 39.4; per band;
  generation-flavour-diagonal bands                                           colour/charge diagonality is a theorem,
                                                                              flavour diagonality is a HYPOTHESIS)
  Yukawa contact, generation-flavour-coherent  OPEN                          (Prop 39.6 algebra; C99d CLOSED-NEGATIVE at
  bands (same gauge representation)                                           linear order (Thm 39.11); C99e OPEN as Proof
                                                                              obligation 39.8' (one computation); W16) <- K9b
  corpus Goldstone, Horn A                     CLOSED-NEGATIVE inside A5     (Thm 37; A5 residue = 2 reals, Cor 37.2)
  corpus Goldstone, Horn B, linear bulk        CLOSED-NEGATIVE, exact        (Thm 38, classical; Thms 38.3, 38.4:
                                               (constant alpha, spectral)     H^2 supertrace + constant co-rotation
                                                                              inside A1-A4; local alpha(x): Cor 38.7 OPEN)
  corpus Goldstone, shift-symmetric residual   CLOSED-NEGATIVE-CONDITIONAL   (Cor 38.1; on f = M_P)  <- K7
  colour / charge-changing off-diag condensate CLOSED-NEGATIVE, exact        (Thm 39.4, Elitzur in gauge-invariant
                                                                              states, undressed operators)  <- K9a closed
  ---------------------------------------------------------------------------------------------
  SURVIVORS (registry), each with its condition or its locus:
     K7   a Goldstone normalisation other than M_P, or an external gradient background   (corpus-external; conditional)
     K8   a strongly coupled sector with a fermion heavier than its mediator (sect.21.4 ii) (corpus-external)
     K9b  a same-representation flavour-coherent boundary condensate                        (corpus object; OPEN --
          no admission criterion exists yet; at linear order its onset functional is
          G_4^(tc) x [2 k_t k_c/(k_t+k_c)] x K_tc with G_4^(tc) = m_t m_c/(2 v^2 m_h^2), Thms 39.9-39.11 (v3.4.1
          normalisation), and the response K_tc is not computed)
  UPSTREAM INPUTS this paper cannot supply:
     A5   two real counterterm parameters (Cor 37.2)
     D-S14-EVENT-001   OPEN; this paper supplies ONE NECESSARY CONDITION on any thermal route to it,
                       T/Delta <= 0.4147 for |kappa| = T_2 (Cor 41.1, 41.2) -- target-conditioned; not a discharge
  OPEN PROOF OBLIGATIONS inside the paper's own scope:
     the coherent-channel admission computation (Proof obligation 39.8', sect.22.11; research item)
     the local-alpha(x) Jacobian against a fixed bag domain (Cor 38.7)

  WHAT THIS IS:  a no-go map whose exact rows are exact inside the stated spectral, free-bulk,
                 colour/charge-diagonal-contact and linear-Goldstone classes, whose conditional rows carry
                 their conditions, and whose open rows are typed OPEN; a bilinear atlas; a Horn-B closure
                 exact classically and, for constant axial rotations, spectrally inside A1-A4; a per-band
                 admission bound unconditional on colour/charge and HYPOTHETICAL on flavour diagonality; a
                 thermal ceiling typed as a necessary, target-conditioned capacity condition; a two-parameter count
                 of the A5 residue; a selector signature with a carrier-level witness -- the missing object is
                 SPECIFIED by that signature and NOT CONSTRUCTED here; a linear-order decoupling theorem for K9b.
  WHAT THIS IS NOT:  "selector exhaustion"; "corpus-wide"; "nothing survives inside the corpus"; a bound on
                 K9b; a closure of RQ3; a selection; a discharge of D-S14-EVENT-001.  TERMINAL-IN-SCOPE
                 stays WITHDRAWN.
  LIFECYCLE:  FREEZE-CANDIDATE PROPOSED (v3.4 audit recommendation; user approval required).
  Output role SUPPORT; no CORE promotion; no SSOT change; RQ3 bridge OPEN -> OPEN.
```

**Corollary 41.3 (what the Mission gains from v3.1–v3.3, stated without inflation).** Three things, each
typed. *(i)* A no-go whose remaining hypotheses are named and typed — generation-flavour diagonality as a
hypothesis with its missing theorem written out (Proof obligation 39.8), constant vs. local axial rotation
(Cor. 38.7) — rather than bounded by an argument that did not carry.
*(ii)* An **inequality on the environment**: the seam rest frame must be colder than `0.4147 Δ` to carry a record of
magnitude `T₂` — a target-conditioned capacity bound on the object RQ3 asks for, obtained without choosing a sector
(the ceiling itself is target-independent; the v3.3 wording *"the first target-blind constraint"* is WITHDRAWN, v3.4). *(iii)* The handoff
names its recipient, `D-S14-EVENT-001`, and states precisely what it gives it: a necessary condition. Per
Mission §6.2 the four items a no-go owes — **excluded class**: the rows of §22.10; **exact assumptions**:
A1–A6 (§2), `f = M_P`, generation-flavour diagonality, the identification, mean field; **surviving complement**:
{K7, K8, K9b} with their conditions or, for K9b, its open obligation; **next minimal construction**: an action-derived seam environment of
`S_Z` whose rest-frame datum obeys Cor. 41.1 *and* that supplies S4 and S6 of Definition 40 — a construction
this paper does not attempt and for which no identifier is reserved.

### 22.11 Proof obligation 39.8 at linear order — record composition, the coherent channel's overlap, and pair-channel decoupling **(new in v3.4; a research addition kept separate from the correction pass)**

> **Why this section exists, and what it is not (MANUSCRIPT §16).** The v3.3 audit advised against forcing a coherent
> many-body theorem into a correction-only version. This section does not do that. It records three exact statements
> that were obtainable without solving the two-flavour spectral problem, states precisely which items of Proof
> obligation 39.8 they discharge, and leaves **K9b OPEN**. Its addition reclassifies v3.4 as a major revision. Route
> cards were frozen before the external sweep (D41); the breakthrough operators used were B04 LAYER SPLIT (order
> parameter / response kernel), B07 RESPONSIBILITY FACTOR (record / overlap / response) and B10 INVARIANTIZATION
> (flavour number). Outcome: `BT-REFORMULATED` for C99d/e; `BT-HOLD` for the response computation.

**Setting.** Two edge fields `1, 2` (top and its charge-`⅔` partner) with bulk masses `m₁ ≠ m₂` at the common wall,
edge localisation rates `κ_i = m_i|cos θ̄|` and gaps `Δ_i = m_i sin θ̄` (Theorem 15), coupled by the Yukawa contact vertex
`M = diag(y₁, y₂) ⊗ 1₄` of Lemma 36.1 in the `d`-channel `Γ := Nγ₅` (which restricts to `J_E` on the carrier, C39). The
boundary two-point function is `G = [[G₁₁, G₁₂],[G₁₂†, G₂₂]]` and the `d`-channel condensate matrix is `σ_ij := ⟨ψ̄_iΓψ_j⟩`.

**Lemma 39.9 (record composition; exact, universal in `G`).** The record operator of the carrier is flavour-blind,
`J_E ⊗ 1₂`. Hence for every Hermitian `G`,

```
   Tr((J_E ⊗ 1) G)  =  Tr(J_E G₁₁) + Tr(J_E G₂₂) ,        κ  =  ( n₁κ₁ + n₂κ₂ ) / ( n₁ + n₂ ) ,
```

independent of `G₁₂`: the record is the density-weighted mean of the diagonal-block records, and flavour coherence can
reach it only through the back-reaction of `G₁₂` on the diagonal blocks via the gap equation. On the v3.2 audit's family
`G = ww†, w = (u, √r·Γu)` the record is `u†Γu/|u|² = κ` for **every** `r` — the `r ≈ 7.4×10⁵` of W16 moves the partner
density, not the record. *(C100.)* ∎ This discharges item (ii) of Proof obligation 39.8 at the level of the carrier.

> **Channel strengths (v3.4.1; the v3.4 audit's finding).** Lemma 36.1's `G₄ = m²/(2v²m_h²) = y²/4m_h²` is *band-specific*:
> it already contains the Yukawa of the band it refers to. Write the flavour-blind Higgs-contact strength `Ĝ₄ := 1/4m_h²`
> and the channel strengths `G₄^{(ij)} := y_iy_j Ĝ₄ = m_im_j/(2v²m_h²)`, so that Lemma 36.1's `G₄` is `G₄^{(ii)}` and
> `G₄^{(12)} = √(G₄^{(11)}G₄^{(22)})`. v3.4 wrote a single `G₄` below and multiplied it by `y₁y₂` in Theorem 39.11 — the
> Yukawas were counted twice — and obligation (c) put `G₄` on both sides of a comparison. Both are corrected here; no
> certificate changes (C101's integral, C102's kernel and V34's ratios are unaffected).

**Lemma 39.10 (the coherent channel's normal overlap; exact).** With the normalised edge profiles
`φ_i = √(2κ_i) e^{−κ_i x}` of Lemma 36.2, the bulk quartic integrates over the normal direction to `G₄^{(ii)}κ_i` in the
diagonal channel `(ψ̄_iΓψ_i)²` and to

```
   G₄^{(12)} · 2κ₁κ₂/(κ₁ + κ₂)          (the HARMONIC mean of the two localisation rates)
```

in the coherent channel `(ψ̄₁Γψ₂)(ψ̄₂Γψ₁)`. Its ratio to the geometric mean `√(κ₁κ₂)` is

```
   ω  =  2√(m₁m₂)/(m₁ + m₂) ,          1 − ω²  =  ((m₁ − m₂)/(m₁ + m₂))²  ≥  0 ,
```

so `ω ≤ 1` with equality iff `m₁ = m₂`: the coherent channel's 2+1 contact strength is never larger than the geometric
mean of the two diagonal strengths. *(C101.)* ∎ For the top wall, `ω_tc = 0.1707`, `ω_tu = 0.00709`; the channel strengths
are `G₄^{(t)} = 1.557×10⁻⁵ GeV⁻²`, `G₄^{(tc)} = 1.150×10⁻⁷ GeV⁻²`, `G₄^{(tu)} = 1.96×10⁻¹⁰ GeV⁻²` (`G₄^{(tc)}/G₄^{(t)} = y_c/y_t =
m_c/m_t`), and the fixed weight of the coherent channel relative to the top diagonal channel is
`(G₄^{(tc)}/G₄^{(t)})ω_tc = 1.26×10⁻³` and `(G₄^{(tu)}/G₄^{(t)})ω_tu = 8.9×10⁻⁸` *(V34)*. These are factors of the onset
condition below, not a verdict.

**Theorem 39.11 (pair-channel decoupling of the linearised coherent gap equation; exact).** Let `G₀ = diag(G₁, G₂)` be any
flavour-diagonal reference two-point function — the flavour-symmetric point, or Theorem 39's diagonal broken state in
which the top band carries the record. Then the Wick kernel of the `d`-channel bilinears `B_ij = ψ̄_iΓψ_j`,

```
   K[(ij),(kl)]  :=  Tr( B_ij G₀ B_kl G₀ ) ,
```

is nonzero **only for `j = k` and `l = i`** — four of the sixteen entries survive — and the Hartree term `Tr(MG)·M` has no
off-diagonal block. Consequently the linearised equation for the coherent condensate `σ₁₂` **closes on itself**: `σ₁₂`
couples to `σ₂₁ = σ̄₁₂` alone, and its onset condition has the form

```
   1  =  G₄^{(12)} · [ 2κ₁κ₂/(κ₁+κ₂) ] · 𝒦₁₂ ,     G₄^{(12)} = y₁y₂/4m_h² ,   𝒦₁₂ := the interband d-channel response of G₀ ,
```

in which the flavour matrix `D` of Proposition 39.6 does not appear. *(C102, exact for symbolic diagonal blocks.)* ∎

*Proof.* Flavour number `U(1)₁ × U(1)₂` is conserved by the reference state (diagonal), by the bulk (diagonal masses),
by the boundary condition (flavour-blind) and by the interaction `(Σ_i y_iψ̄_iψ_i)²`; `B_ij` carries charge
`(+1)_i(−1)_j`, so a connected two-point function of `B_ij` with `B_kl` vanishes unless the charges cancel, i.e.
`j = k, l = i`. The certificate C102 evaluates all sixteen kernel entries on symbolic `4×4` blocks and finds exactly the
four allowed ones nonzero. The Hartree statement is the vanishing of the off-diagonal block of `Tr(MG)·M`. □

**Corollary 39.12 (what this does to C99d and C99e).** *(a)* C99d — *"`λ_max(D)` is the coherent carrier's critical
coupling"* — is **CLOSED-NEGATIVE at linear order**: `D_ij ∝ y_iy_jσ_ij` is the Fock image of the **order parameter**, and
the onset of the coherent channel is governed by the **response kernel** `𝒦₁₂` (Theorem 39.11); the two are different
objects (B04). In the deep coherent phase the larger eigenvalue of the condensate matrix sets the boundary angle of a
*rotated* flavour whose bulk mass matrix is not diagonal — not a band in the sense of Theorem 36 (one mass, one gap) — so
the v3.2 reading is ill-typed there as well. *(b)* C99e — *"Theorem 36's bound is unchanged"* — remains **OPEN** and is
**reformulated as one computation**:

```
   PROOF OBLIGATION 39.8'  (replaces (iii)-(v) of 39.8; (i) is not needed about a diagonal reference, (ii) is Lemma 39.9)
   (a) compute 𝒦_tc for Theorem 39's diagonal state from the edge dispersions E_i = (k² + Δ_i²)^{1/2}, the wall
       spinors of Theorem 15 and the overlap of Lemma 39.10;
   (b) maximise it over Pauli-allowed occupations of both bands at fixed total record |κ| = T₂ (Lemma 39.9);
   (c) evaluate the dimensionless admission ratio  A_tc := G₄^{(tc)} · [2κ_tκ_c/(κ_t+κ_c)] · 𝒦_tc^max  at the corpus
       value G₄^{(tc)} = m_t m_c/(2v²m_h²) = 1.150×10⁻⁷ GeV⁻² (V34); the coherent onset requires A_tc ≥ 1.
       (v3.4 wrote this line with G₄ on both sides and the Yukawas counted twice; corrected in v3.4.1.)
   Also owed: a first-order (discontinuous) appearance of the coherent phase is not excluded by a linear analysis.
```

*(D39.)* **K9b is OPEN.** A remark on sign, exact as arithmetic and [가설] as physics: in a Lindhard-type form of `𝒦_tc`,
a pair made of an occupied heavier-band state and an empty lighter-band state at the same `k` contributes with the sign of
`(f_t − f_c)/(E_c − E_t) < 0`, so a record-carrying top band facing an empty charm band lowers the coherent response;
whether this makes (b) small is exactly what (a)–(c) decide.

**External baseline (D41; sweep run after the route cards were frozen).** Blasone, Jizba, Mavromatos and Smaldone
(arXiv:1807.07616; primary PDF) establish that dynamically generated field mixing in a two-flavour chiral model
requires flavour-off-diagonal condensates, with residual symmetry the total flavour charge `U(1)_V` and a mean-field
vacuum containing inter-flavour pair condensates. The **object** of K9b is therefore IMPORTED and the algebra of
Proposition 39.6 is SPECIALIZED; the boundary-carrier form of the question and the onset functional of Theorem 39.11
were NOT_FOUND in the query family (OPEN-NOVELTY, narrowed; `NOT_FOUND ≠ ABSENT`).

**Hidden-freedom audit (BREAKTHROUGH §12).** No fitted parameter; the construction choices are the reference state
(flavour-diagonal — the only class in which the decoupling is a symmetry statement), the mean-field/Fock decoupling
inherited from §20, the profile normalisation of Lemma 36.2 and the linear order. Nothing here was chosen after seeing
a target number.

---

## 23. Effect on the corpus debts

**Audit disposition (v3.4.1): v3.4 audit (L3; delta review of the three S2 repairs, §22.11 and G25) — accepted in full,
0 findings rejected.** Verdict as received: the paper's quantifiers, physical bridge, survivor typing, target conditioning
and error lineage are stable and §22.11 is a substantive advance; **one substantive defect**: Proof obligation 39.8′ used `G₄`
in two incompatible senses. Repaired here, correction-only (channel strengths `G₄^{(ij)}`, §22.11; C101, C102, D39, V34
retyped; no certificate changed). Recommendation: *v3.4 as-is — not frozen; v3.4.1 minimal correction → freeze M67 → move to the
positive-construction line*, because M67's role (no-go map + missing-object extraction) is essentially complete, not because it
failed. **FREEZE-CANDIDATE: PROPOSED** — the freeze requires **user approval** and is not granted by this document; no further
deep research is invested inside M67 (obligation 39.8′'s response computation and Cor. 38.7 move to the successor line; no
identifier is reserved).

| Debt | v3.4 | **v3.4.1** | basis |
|---|---|---|---|
| `G₄` in Thm 39.11 / obligation 39.8′ | `1 = G₄·y₁y₂·overlap·𝒦` (Yukawas twice); (c) `1/(G₄y_ty_c…𝒦)` vs `G₄` (malformed) | `Ĝ₄ := 1/4m_h²`, `G₄^{(ij)} := y_iy_jĜ₄ = m_im_j/(2v²m_h²)`; `1 = G₄^{(12)}·[2κ₁κ₂/(κ₁+κ₂)]·𝒦₁₂`; (c) `A_tc = G₄^{(tc)}·overlap·𝒦_tc^max ≥ 1` at `G₄^{(tc)} = 1.150×10⁻⁷ GeV⁻²` | §22.11; C101, C102, D39, V34; D42 |
| paper lifecycle | FREEZE-CANDIDATE WITHHELD | **PROPOSED** (v3.4 audit recommendation; user decision) | D34, D42 |

**Audit disposition (v3.4): `AUDIT-MAJOR-REVISION` (v3.3 audit; central contribution SURVIVES; highest severity S2;
release-blocking YES; research reopen NO; L3 + L5: deterministic re-run 48/48 byte-identical in a clean directory and four
fault injections reproduced) — accepted in full, 0 findings rejected.** FREEZE-CANDIDATE stays **WITHHELD** until a targeted
delta re-audit of the three S2 repairs, §22.11 and G25.

**v3.4 movements (third audit-integration pass + §22.11).**

| Debt | v3.3 | **v3.4** | basis |
|---|---|---|---|
| §25 physical bridge | "the remaining object is completely specified — an action-derived … CPTP map … all now derived" (v2.6 sentence, live) | **REPLACED**: the *signature* of the missing object is completely specified; no such map or state-selection mechanism is constructed in M67; derived are the carrier, grading, boundary lift and admissible state/operation families. `specification ≠ construction` | §25; G20(iv); CLAIM-STATE `MissingObject` |
| Thm 41 / Cor. 41.1 / Cor. 41.3(ii) | "first target-blind constraint" | ceiling `\|κ\| ≤ tanh(Δ/2T)` **target-independent**; `T/Δ ≤ 0.4147` **target-conditioned** capacity bound; the phrase is **WITHDRAWN** | §22.9; V32; CLAIM-STATE tokens |
| Thm 36 / Cor. 36.2 | "target-blind except for the two numbers" | functional form general; the `×42` verdict **target-conditioned** on `(T₂, θ̄_*)` | §21.2, §21.4 |
| release core vs manifest | core declared as 4 files incl. session; manifest core = 3 objects, session unregistered | **core = manuscript · verifier · ledger · release manifest**; session, audit report, provenance supplement = provenance objects with measured hashes; **G25** compares the §27 declaration with the manifest | §27; G25; manifest |
| Elitzur (Thm 39.4) | scope narrowed, no citation, boundary assumption implicit | citation (Phys. Rev. D 12, 3978 (1975)); hypotheses **(H1)** positive gauge-invariant measure, **(H2)** boundary preserves the local gauge symmetry (no boundary gauge reduction, no dressed non-local order parameter) | §22.8; C96; ref. 22 |
| exit policy | `exit_code([]) = 0` | empty ledger → **exit 2** | G21 |
| W15, W16 (self-found, S3) | W15's claim text embeds a run-dependent `1e-16` residual (fingerprint not byte-stable across machines; "carried 27" environment-dependent); lineage rescan: W16 embeds a `1e-12` eigenvalue residual | **threshold form** for both; measured values in `detail` | §1; W15, W16; G18 |
| K9b — C99d | OPEN (D36) | **CLOSED-NEGATIVE at linear order** (Thm 39.11): the coherent channel closes on itself; `D` is the order parameter's Fock image, not the kernel | §22.11; C102; D39 |
| K9b — C99e / Proof obligation 39.8 | OPEN; five objects owed | **OPEN**; items (i) (about a diagonal reference) and (ii) (Lemma 39.9) discharged; (iii)–(v) reduced to **Proof obligation 39.8′** (one response computation with a Pauli extremiser at fixed record) | §22.11; C100, C101, D39 |
| K9b — novelty | OPEN-NOVELTY (no sweep) | object **IMPORTED** (Blasone et al. 2018), Prop. 39.6 algebra **SPECIALIZED**, boundary form **OPEN-NOVELTY (narrowed)** | D41; ref. 23 |
| A4/A5 wording | reconstructed from use | repo 1/2 title and full-text search: **NOT_FOUND** (not ABSENT); reconstruction stands, marked | §2 |
| paper lifecycle | FREEZE-CANDIDATE WITHHELD | **WITHHELD**; MANUSCRIPT DRAFT; SUPPORT; **major revision** (§22.11) | D34, D40 |

**Audit disposition (v3.3): `AUDIT-RESEARCH-REOPEN` (v3.2 audit; target: the K9b quantitative conclusion,
the package and the guards; L3 + L5) — accepted in full, 0 findings rejected.** The v3.2 rows below are corrected
where marked ⟂; FREEZE-CANDIDATE stays **WITHHELD**.

**v3.3 movements (second audit-integration pass).**

| Debt | v3.2 | **v3.3** | basis |
|---|---|---|---|
| K9b same-representation flavour coherence | REJECTED-BY-BOUND conditionally on `n_partner ≤ n_top`; "unchanged bound"; "`n_c/n_t ≈ 2×10⁷` needed" | **OPEN.** All three sentences **WITHDRAWN**: Theorem 36's single-band bound has no proven extension to a coherent two-band carrier (C99d/e OPEN, D36); the audit's rank-one positive family reaches the target at `r ≈ 7.4×10⁵` with `D_cc` kept (W16). Prop. 39.6 survives as algebra (C99a–c); the missing theorem is Proof obligation 39.8 | §22.8; C99a–c, D36, W16, V33 (retyped) |
| Elitzur (Thm 39.4) | "vanishing expectation in every state of the gauge theory" | **scope narrowed**: undressed local gauge-variant operators in gauge-invariant states / under the gauge-invariant measure; fixed-gauge expectations, boundary gauge reductions, dressed operators out of scope; K9a unchanged | C96 |
| `κ = T₂` (Cor. 41.1, W14) | signed value | **`\|κ\| = T₂`** (`κ = −T₂` in the `z₀` convention); inequality unchanged | V32, W14 |
| A1–A5 | "as in v2.3" | **restated in §2** (A1–A3, A1′ from v1.1; A4, A5 reconstructed from use, marked) | §2 |
| handoff label | RQ1→RQ3 | **RQ2→RQ3** ([가설]); RQ1 is the backbone frame | front matter, D28 |
| novelty of Prop. 39.6 | NEW (elementary) | **OPEN-NOVELTY** (no prior-art sweep on boundary flavour-coherent condensates) | §24, §27 |
| title | "Classical selector exhaustion, …" | **narrowed** to the stated classes | front matter |
| verifier package | 4 core + 5th baseline file; auditor's 4-file run: exit 2 | **artifact K** (48 rows); baseline **embedded**; 4 core files reproduce **0/0**; release manifest generated at run time | §27, G18 |
| guards | G20/G23 token-level; both passed semantic injections; G21 declarative | **sentence-level claim-state and symbol-table rules** (G20, G23), **CLAIM-STATE manifest** (G24), **functional** G21; both injections FAIL; limits stated in §1 | §1, G20–G24 |
| structure | lineage in the main text (~42k words) | **provenance supplement** split off | supplement |
| paper lifecycle | FREEZE-CANDIDATE WITHHELD | **WITHHELD** (unchanged); MANUSCRIPT DRAFT; SUPPORT | D34, D38 |

**Audit disposition (v3.2): `AUDIT-RESEARCH-REOPEN` (v3.1 audit; scope Thm 39.4, §22.9 handoff, release
package) — accepted in full, 0 findings rejected.** The v3.1 rows below are corrected where marked; the
FREEZE-CANDIDATE proposal is **WITHHELD**.

**v3.2 movements (audit-integration pass; rows marked ⟂ are corrected by the v3.3 table above).**

| Debt | v3.1 | **v3.2** | basis |
|---|---|---|---|
| ⟂ K9 off-diagonal boundary condensate | CLOSED-NEGATIVE (Elitzur) | **SPLIT.** K9a (colour-off-diagonal, charge-changing): CLOSED-NEGATIVE, exact. **K9b (same-representation generation-flavour coherence): OPEN**, gauge-invariant; computed once: coherence can only raise the effective coefficient against the unchanged bound, by `≤ 0.9 % (n_c/n_t)^{1/2}`; REJECTED-BY-BOUND only on `n_partner ≤ n_top`. "Diagonal mean field is a theorem" **WITHDRAWN** | Thm 39.4 (re-quantified), Prop. 39.6, Cor. 39.7; C96, C99, V33 |
| handoff recipient (Cor. 41.2) | "selecting the record value = discharging `D-S14-EVENT-001`" | **one NECESSARY CONDITION** on any thermal route to `D-S14-EVENT-001`: `T/Δ ≤ 0.4147`; S4, S6, the action-derived environment and the instrument selection are still owed; the discharge wording is **WITHDRAWN** | Cor. 41.2 (re-scoped), Def. 40, D28, D30 |
| RQ2 ↔ RQ3 residue | "coincide" | **[가설]**: RQ2's clock/rest-frame construction may supply one input of RQ3's selection; no identification without a common action or compatibility theorem (Mission §4.2) | Remark 41.4 |
| quantum axial Jacobian with boundary | CLOSED inside A1–A4 (any local `α(x)`) | **CLOSED for constant `α`** (co-rotation, Thm 38.4) and for the `H²`-regularised spectral density (Thm 38.3); **OPEN for local `α(x)`** against a fixed bag domain (domain preservation not proved) | Cor. 38.7; C94 (re-scoped), C95 |
| ⟂ survivors | K7 (cond.), K8 | **K7 (cond.), K8, K9b (cond.; corpus object)**; "inside the corpus nothing survives" **WITHDRAWN** — *v3.3: K9b OPEN, not conditional* | §22.10 |
| notation | `T₂` for both the target and the dephasing time | **`τ₁, τ₂`** relaxation times; **`T₂`** target only; guard G23 | §22.9 type lock |
| front matter / companion | artifact I printed as 37 rows in §26–27; OPEN-DEBTS listed the condensate as survivor and closed at once | **38** corrected; OPEN-DEBTS, scope verdict, §22.10, §24, §26, §27 re-synchronised (CPN11) | §1, §2, §27 |
| ⟂ verifier package | 4 files; v3.0 ledger not shipped; G22 needs a sibling script; clean room: exit 1 | **artifact J** (42 rows) + **v3.1 ledger shipped**; G22 reports NOT SHIPPED instead of failing; manuscript path by glob; **clean room: 42 rows, FAIL 0, DEGRADED 0, exit 0** — *v3.3: only with the 5th file; the 4-file package gave exit 2* | §27, G18, G22, G23 |
| "no computation remains inside scope" | claimed (D34) | **WITHDRAWN**: K9b was computed in v3.2 (Prop. 39.6); the local-`α(x)` obligation (Cor. 38.7) remains inside scope | D34 |
| paper lifecycle | FREEZE-CANDIDATE proposed | **WITHHELD** (audit); re-proposal only after a delta re-audit of v3.2 finds no new S2+ | D34, D35 |

**v3.1 movements (closure pass; rows marked ⟂ are corrected by the v3.2 table above).**

| Debt | v3.0 | **v3.1** | basis |
|---|---|---|---|
| ⟂ quantum axial Jacobian with boundary (Cor. 9.2 [열림], Thm 38(A) classical) | OPEN inside A1–A4 | **CLOSED inside A1–A4**: `𝒞` kills the `H²`-regularised density pointwise; `U` is a unitary equivalence, so spectral data depend on `θ̄` alone | Thms 38.3, 38.4; C94, C95 |
| ⟂ K9 off-diagonal boundary condensate | corpus-external survivor | **CLOSED-NEGATIVE** (gauge-variant; Elitzur IMPORTED + Schur) — *v3.2: K9a only* | Thm 39.4; C96 |
| ⟂ the record value on the carrier | rest-frame datum (unbounded) | **bounded**: `\|κ\| ≤ tanh(Δ/2T)`; `κ = T₂ ⇒ T/Δ ≤ 0.4147` — *v3.3: `\|κ\| = T₂`*; tangential datum can only lower it | Thm 41, Cor. 41.1; C97, V32 |
| ⟂ handoff recipient (Cor. 40.1) | "an RQ2 object" | **`D-S14-EVENT-001`** (ZS-S14 v2.1 read; no rest-frame datum in the corpus) — *v3.2: as a necessary condition* | Cor. 41.2; D33 |
| A5 counterterms | three coefficients, open | **residue counted: at most three off-`πℤ` stationary values; exactly two real parameters after landing** | Cor. 37.2; C98 |
| lineage rescan (VERIFY §7.3) | registered only | G (v2.9): 2/2 defects; H, I: clean; **C–F NOT_FOUND in repo 2 — unavailable, not clean** | G22 |
| ⟂ survivors | K7 (cond.), K8, K9 | **K7 (cond.), K8** — both corpus-external; inside the corpus with `f = M_P` nothing survives — *v3.2: plus K9b* | §22.10 |
| ⟂ paper lifecycle | MANUSCRIPT DRAFT, reopened | **FREEZE-CANDIDATE proposed** (selection question); not granted; TERMINAL-IN-SCOPE stays WITHDRAWN — *v3.2: WITHHELD* | D34 |

**Audit disposition: `AUDIT-RESEARCH-REOPEN` (v2.9, scope §22) — accepted in full. The v2.9 rows of this
table are WITHDRAWN where marked and replaced by the v3.0 column.**

| Debt | v2.9 (proposed) | **v3.0** | basis |
|---|---|---|---|
| `F-M66.17` | CLOSED-NEGATIVE corpus-wide | **WITHDRAWN → partial**: CLOSED-NEGATIVE *exactly* for spectral (A1–A5), free-bulk (A4), and the Goldstone's linear bulk couplings on Horn B; *conditionally* (identification, mean field, diagonal mean field, `f = M_P`) for Yukawa contact on any number of diagonal bands and for the Goldstone residual class; **OPEN** at K7 (condition), K8, K9 (corpus-external) | Thms 36–39, Cor. 38.1, registry V30 |
| the corpus Goldstone `θ` | CLOSED-NEGATIVE on both horns, exact, coefficient-free | Horn A: **CLOSED-NEGATIVE inside A5** (Thm 37, strengthened). Horn B: **linear bulk couplings CLOSED-NEGATIVE exactly** (V: removable; A: record-blind at zeroth gradient order); **shift-symmetric residual CLOSED-NEGATIVE-CONDITIONAL on `f = M_P`** and it is a **STRUCTURAL SURVIVOR** with a flip-odd carrier image | C85, C86, C89, C90, V28, V31 |
| multi-band carriers | CLOSED-NEGATIVE, bound `∝ 1/N_b`, `N_b ≥ 42` required | **`1/N_b` WITHDRAWN** (contradicted v2.8 §25.19). One field = one band (Lemma 39.0); bound **per band**, `N_b`-independent (Thm 39) in a diagonal mean field; **survivor: off-diagonal boundary condensate (K9)** *(v3.2: K9a closed, K9b open)* | C87, C91, C92, V27 |
| admission filter | four-item checklist, C88 | **computed registry predicate** (Thm 39.3, V30); C88 retyped `C → G` | §22.4 |
| `θ̄ = π` | stationary point of `Γ` | **unique minimum** of `Γ` when `θ̄` is dynamical | C85, C93 |
| boundary bilinear classification | Thm 27 (4 scalars) | **all 16 bilinears** (Lemma 38.0): `span{1, J_E, X_θ, Y_θ}`; tangential axial current `≡ 0`; only tangential vector currents reach the flip family | C90 |
| selector signature | `y m/M` window | **Definition 40** (S1–S6, K1–K3) + witness W14; handoff Cor. 40.1 | §22.5 |
| `ZS-S14` §10.3.5 dichotomy | irrelevant to `F-M66.17` | **relevant again**: the horns differ in *how* (A5 potential vs. gradient class), though both are closed or conditionally closed | Thms 37, 38 |
| paper lifecycle | TERMINAL-IN-SCOPE proposed | **WITHDRAWN.** MANUSCRIPT DRAFT; research reopened at K7/K9 and reformulated at Cor. 40.1 | §22.6 |
| verifier package | 16 rows, exit 0 with G18 DEGRADED | artifact H: 27 rows; exit 2 on DEGRADED; artifact-G ledger shipped | §27 |
| everything else | — | unchanged | — |

`RQ3` bridge state: **OPEN → OPEN.** Output role: **SUPPORT**, no `CORE` promotion. History: H-0277 is
not edited; a superseding correction row is proposed (session file).

---

## 24. Claim map (v2.4–v3.3 additions; §13–15 entries unchanged from v2.3)

| CLAIM-ID | statement | quantifier | assumptions | epistemic | gate | novelty | evidence | falsifier |
|---|---|---|---|---|---|---|---|---|
| **M67.19** | `P₊\|_{L_θ}` is an isomorphism (`det = 1`), so the operator-state lift is action-derived | ∀ `θ` | A1–A4, A6 | `PROVEN` | CLOSED-PASS | **NEW (sweep-limited)** | §16.1 + **C61** | a boundary value outside `L_θ`, or `det = 0` |
| **M67.20** | the normal rotation acts as `e^{−iφJ_E/2}`, commutes with `J_E`, and its invariant states are exactly the `κ`-family | ∀ `φ` | A1–A4, A6 | `PROVEN` | CLOSED-PASS | **NEW** | §16.2 + **C60** | a rotation-invariant state with `r_x ≠ 0` |
| **M67.21a** | `E₊` is not boost-invariant while `L_θ` is; the induced carrier map is `G(ζ) = cosh(ζ/2)+sinh(ζ/2)X_θ`, `det G = 1`, non-unitary | ∀ `ζ, θ` | A1–A4 | `PROVEN` | CLOSED-PASS | **NEW** | §16.3 + **C56, C57** | a unitary induced carrier map |
| **M67.21b** | `X_θ ∈ 𝔛(J_E)` and `{X_θ, J_E} = 0`: the boost generator is a grading-odd flip element | ∀ `θ` | A1–A4 | `PROVEN` | CLOSED-PASS | **NEW** | §16.3 + **C58** | `[X_θ, J_E] = 0` |
| **M67.21c** | `κ_out = κ_in/(cosh ζ + sinh ζ (m̂·r))`; every boost-invariant boundary state has `κ = 0` | ∀ `ζ`, ∀ states | A1–A4 | `PROVEN` | **CLOSED-NEGATIVE** for boost-invariant states | **NEW (sweep-limited)** | §16.3 + **C59**, W09 | a boost-invariant state with `κ ≠ 0` |
| **M67.22** | target-blind reduction `S¹ → (π/2,3π/2)∖{π}`, and `θ̄_*` lies inside | ∀ `θ̄` | A1–A4 + GUvdB (IMPORTED) | `PROVEN` + `IMPORTED` | CLOSED-PASS | NEW (combination) | §17 + **C62**, V19 | a localised carrier at `cos θ̄ ≥ 0` |
| **M67.23** | boundary polarisation law: every stationary mode has `κ = m sin θ̄/E` (polarisation-summed), independent of `q, k_⊥`, either energy sign | ∀ `(m,E,q,k_⊥,θ̄)` | A1–A4, A6 | `PROVEN` | CLOSED-PASS | **NEW (sweep-limited)** | §18.1 + **C63, C64**, R10 | a mode with `κ ≠ m sin θ̄/E` after polarisation sum |
| **M67.23.2** | continuum-only unpolarised states cannot reach `κ = T₂`; band weight `≥ 0.0640` | ∀ such states | + identification | `DERIVED-CONDITIONAL` | CLOSED-PASS (could have failed) | NEW | §18.1 + **V21** | `T₂ ≤ sin θ̄_*` |
| **M67.24** | `𝒞 = iγ²K` anticommutes with `H` for every `θ_m` and preserves every `L_θ`; `η(H_θ̄) ≡ 0`, `∂_θ̄ η_edge ≡ 0`; every spectral selector inside A1–A5 exhausted | ∀ `θ, θ_m, p` | A1–A4 | `PROVEN` | **CLOSED-NEGATIVE** (No-Go Map, gate §18.0) | NEW (combination; the 𝒞-symmetry itself is standard) | §18.2 + **C65, C66** | an `L_θ` not preserved by `𝒞`, or an asymmetric edge spectrum |
| **M67.25** | no autonomous `Φ_∂` under A4: identical `ρ₊(0)`, different `ρ₊(t)` | ∃ (witness) | A1–A4 | `PROVEN` (existence) | CLOSED-NEGATIVE for the map class | NEW | §18.3 + **W10** | a proof that `ρ₊(t)` is a function of `ρ₊(0)` |
| **M67.25.1** | uniqueness-transfer: `Tr(XρXJ_E) = −Tr(ρJ_E)`; (N-uni),(N-cov),(N-boost) are corollaries of "unique stationary state, `κ ≠ 0`" | ∀ `X, ρ` | none beyond the carrier | `PROVEN` | CLOSED-PASS | NEW (elementary) | §18.3 + **C67** | a flip-covariant map with unique `κ ≠ 0` fixed point |
| **M67.26** | edge band: one state per `(k_⊥, sign E)`, antipodal projections, band lift onto `E₊`; thermal band `κ = −tanh(E/2T) m sin θ̄/E`; `κ_exc(x)` closed form, 0→1 | ∀ `k_⊥, θ̄, T` | A1–A4, A6 | `PROVEN` (algebra) | CLOSED-PASS | NEW (sweep-limited) | §18.4 + **C66, C68, C69**, V20 | a second edge state at fixed `(k_⊥, sign E)`, or non-monotone `κ_exc` |
| **M67.26.3** | `κ_exc = T₂` ⇔ `T_*/(m|sin θ̄|) = 0.19675…` | one point | + identification | `DERIVED-CONDITIONAL` | — | NEW (kinematic) | §18.4 + **V20** | none (not a prediction) |
| **M67.27** | on-shell collapse: `Ψ†KΨ = 2(a sin θ + b cos θ + d)J_E`, `Ψ†NΨ = Ψ†γ₅Ψ = 0` | ∀ `(a,b,c,d,θ)` | A1–A4, A6 | `PROVEN` | CLOSED-PASS | **NEW (sweep-limited)** | §19.1 + **C70**, W12 | a boundary bilinear with an on-shell component off `J_E` |
| **M67.28a** | mean-field branch `θ = π − 2 arctan(4J)` on the locus `H`; `J = 0` sits at the excluded point `θ = π` | ∀ `J` | A1–A3, A6, mean field | `PROVEN` (algebra) | CLOSED-PASS | NEW | §19.2 + **C72**, C71, R12 | a condensate leaving `H`, or a different zero-coupling point |
| **M67.28b** | gap equation: `κ ≠ 0` iff `2s\|g\| > 1`; `κ² = s² − 1/(4g²)`; **`\|cos θ̄\| = g_c/\|g\|`** | ∀ `(s,g)` | + relax A4, mean field | `PROVEN` (algebra) / `DERIVED-CONDITIONAL` (physics) | **OPEN-BUT-TYPED** for F-M66.17 | **NEW** | §19.2 + **C73** | a second nonzero branch, or `\|cos θ̄\|` depending on anything but `g_c/g` |
| **M67.28.3** | `s_* > 1` forces band occupation; `g_*/g_c = 1/\|Re λ\| = 1.765`, order one | two points | + identification | `DERIVED-CONDITIONAL` | CLOSED-PASS (could have failed) | NEW | §19.2 + **V22, V23** | `s_* ≤ 1`, or an over-criticality far from unity |
| **M67.29** | `½Tr(H_edge J_E) = m sin θ̄`, `Tr H_edge = 0`: the edge is a 2+1 Dirac fermion; level `½ sign(sin θ̄)` | ∀ `k_⊥, θ̄` | A1–A4, A6; level step IMPORTED | `PROVEN` + `IMPORTED` | CLOSED-NEGATIVE for point selection | NEW (combination) | §19.3 + **C74** | a `k_⊥`-dependent edge mass |
| **M67.30** | M66 and M67 use opposite chiral sign conventions and the same invariant `θ̄ = θ + θ_m` | ∀ `α, θ` | none | `PROVEN` | **CLOSED-PASS**, discharges Cor. 8.2 | NEW (bookkeeping) | §19.4 + **C75**, M66 v1.5.1 §6 | a third convention in either text |
| **M67.31** | under A4 no boundary quartic is generated; `g ≡ 0`; the free bulk cannot select | ∀ of A4 | A4 | `PROVEN` (standard) | **CLOSED-NEGATIVE** (gate §20.0) | not new (structural) | §20.1, D19 | a quartic term from Gaussian integration |
| **M67.32** | `Ψ†γ⁰e^{iθ_mγ₅}Ψ = 2 sin θ̄ J_E` on `L_θ` | ∀ `θ, θ_m` | A1–A3, A6 | `PROVEN` | CLOSED-PASS | NEW (sweep-limited) | §20.2 + **C76** | dependence on `θ`, `θ_m` separately |
| **M67.33a** | `(a,b)`-plane Hartree on `H` is the reflection `θ̄ ↦ −π − θ̄` | ∀ `θ̄₀, θ_m` | mean field | `PROVEN` (algebra) | CLOSED-NEGATIVE as selector | NEW | §20.2 + **C77** | a fixed point off the arc endpoints |
| **M67.33b** | Fierz completeness exact; `γ³γ₅` self-inverse; the exchange term supplies `(ψ†Nγ₅ψ)²` with weight ¼ | ∀ indices | none | `PROVEN` | CLOSED-PASS | not new (Fierz); mapping new | §20.2 + **C78** | a failure of completeness |
| **M67.34a** | `κ` breaks a ℤ₂ and no continuous symmetry | ∀ flips, ∀ rotations | carrier only | `PROVEN` | CLOSED-PASS | NEW (elementary) | §20.3 + **C79** | a flip fixing `κ ≠ 0` |
| **M67.34b** | boundary theory = `N=1` 2+1 Gross–Neveu; dynamical mass = `m sin θ̄` | mapping | Thms 27, 29 | `IMPORTED` + mapping `DERIVED-CONDITIONAL` | OPEN-NOVELTY | mapping new; physics imported | §20.3, D20 | a GN feature absent on the boundary |
| **M67.35** | `T=0` band: `s = 1/sin θ̄`; `tan θ̄ = −2g`; unique on `(π/2,π)` | ∀ `g > 0` | mean field, band sector | `PROVEN` (algebra) / `DERIVED-CONDITIONAL` | CLOSED-PASS | NEW | §20.4 + **C80**, V24, W13 | a second solution on the half-arc |
| **M67.36.1** | contact exchange `G₄ = y²/4m_h² = m²/(2v²m_h²)`; edge overlap cancels, `g = c′G₄n_∂` | exact | tree level, contact | `PROVEN` (algebra) | CLOSED-PASS | not new | §21.1 + **C81, C82** | — |
| **M67.36** | single-band contact bound `G₄m² ≥ πκ/(2c′ sin θ̄(1−κ))`, universal over Pauli-allowed occupations | ∀ occupations | mean field, one band | `PROVEN` (algebra) | CLOSED-PASS | **NEW** | §21.2 + **C83, C84** | an occupation with larger density at fixed `⟨1/E⟩` |
| **M67.36.2** | upstream SM numbers miss the bound by ×42 (top), ×10⁷⁻⁸ (others) | five masses | + identification, `m_h` HYP-strong | `DERIVED-CONDITIONAL` | **CLOSED-NEGATIVE** (gate §21.0) | NEW | §21.3 + **V25, V26** | `c′ ≥ 21`, or a non-contact mediator |
| **M67.37** | Horn A: `θ̄` dynamical ⇒ potential `= Γ(A)`, stationary set exactly `{0, π}`, `π` the unique minimum | ∀ `θ̄` | A1–A5, mean field | `PROVEN` (given Thm 13) | **CLOSED-NEGATIVE** inside A5 | **NEW** | §22.1 + **C85, C93** | a stationary point off `πℤ`, or `Γ′ ≤ 0` somewhere |
| **M67.38.0** | bilinear atlas: all 16 bilinears on `L_θ` lie in `span{1, J_E, X_θ, Y_θ}`; tangential axial current `≡ 0`; `ψ̄γ^{1,2}ψ = 2X_θ, 2Y_θ` | ∀ `θ` | A1–A4, A6 | `PROVEN` | CLOSED-PASS | **NEW (sweep-limited)** | §22.2 + **C90** | a bilinear with an on-shell component outside the span |
| **M67.38** | Horn B classification: `∂J_V = 0`, `∂J_A = 2imψ̄γ₅e^{iθ_mγ₅}ψ` on shell; vector linear coupling exactly removable (flux 0); axial linear coupling is a rotation fixing `(θ̄, κ)`; a boundary-localised gradient class survives, flip-odd on the carrier | ∀ `(m, θ_m, θ, α)` | A1–A4; anomaly outside A4 not computed | `PROVEN` (V, A classical + C50) | **CLOSED-NEGATIVE** (linear bulk) / **CLOSED-NEGATIVE-CONDITIONAL** on `f = M_P` (residual) | **NEW** (repairs v2.9) | §22.2 + **C86, C89, C90**, V28, V31 | a non-removable linear bulk coupling to the record; or a corpus Goldstone with `f ≠ M_P` |
| **M67.39.0** | one Dirac field carries exactly one edge band: the minor ideal contains `(E ± m)(κ + m cos θ̄)`; rank 1 at the root | ∀ `(m, k_⊥, E, θ̄)` | A1–A4 | `PROVEN` | CLOSED-PASS | NEW (sharpening of Thm 15/26) | §22.3 + **C91** | a second Jost zero, or rank 2 at the root |
| **M67.39** | diagonal mean field: Fock operator block-diagonal, `d`-channel of band `i` depends on `G_i` alone; bound per band, `N_b`-independent | ∀ diagonal `G` | + scalar contact, mean field, **generation-flavour diagonality (a hypothesis; v3.3)** | `PROVEN` (algebra) / `DERIVED-CONDITIONAL` (numbers) | **CLOSED-NEGATIVE** (colour/charge diagonality a theorem, Thm 39.4) / **OPEN** off the diagonal (K9b, Proof obligation 39.8) | NEW (replaces v2.9's `1/N_b`) | §22.3 + **C87, C92**, V27 | an off-diagonal Fock block in a diagonal state |
| **M67.39.3** | computed admission registry: **11 entries** (v3.3), 0 admitted; 6 numeric entries all fail the bound (1 conditional: K7), 4 structural (2 overlapping), 1 external, **1 OPEN (K9b)**, 1 non-candidate | every **registered** candidate | — | `PROVEN` (computation) | CLOSED-PASS for the registry | NEW | §22.4 + **V30**, C88(G) | an admitted entry, or a corpus candidate absent from the registry |
| **M67.40** | selector signature S1–S6 with kill tests K1–K3; the corpus chain passes K1, K2 and fails K3; record value = rest-frame datum | signature | Thms 20, 21, 25.1, 26.1, 27 | `DERIVED-CONDITIONAL` / [가설] | BT-REFORMULATED | NEW | §22.5 + **W14** | a corpus-derived `Δ/T` or flip-odd datum landing on `T₂` without consulting `λ` |

| **M67.38.3** | the `H²`-regularised axial density `Σ f(E_n²)φ_n†γ₅φ_n` vanishes pointwise, boundary included, for every regulator `f(H²)`: `𝒞γ₅𝒞⁻¹ = −γ₅`, density flips, `L_θ` preserved, `{𝒞, H} = 0`. **Scope (v3.2): a spectral statement on `dom H`; the Jacobian of a local `α(x)` against a fixed bag domain is NOT claimed** | ∀ `(θ, θ_m, m)`, ∀ `f` | A1–A4 | `PROVEN` (spectral) | CLOSED-PASS (spectral) / **OPEN** (local-`α(x)` Jacobian, Cor. 38.7) | NEW (combination; `𝒞` itself standard) | §22.7 + **C94** | a spinor with `(𝒞φ)†γ₅𝒞φ ≠ −φ†γ₅φ`, or an `L_θ` not preserved |
| **M67.38.4** | `U†H(θ_m,θ_b)U = H(θ_m+2α, θ_b−2α)` with co-rotated domain: unitary equivalence ⇒ spectral data depend on `θ̄` only | ∀ `α` | A1–A4 | `PROVEN` | CLOSED-PASS | NEW (elementary) | §22.7 + **C95** | a kinetic matrix not fixed by `U` |
| **M67.39.4** | **colour-off-diagonal and charge-changing** bilinears are gauge-variant (commutant of `su(3)` = `ℂ·1`; Cartan phase; `Q_t − Q_b = 1`) ⇒ the K9a condensate vanishes (Elitzur: undressed local operators in gauge-invariant states; scope v3.3). **Quantifier corrected (v3.2): not for same-representation flavour bilinears** | ∀ colour-off-diagonal `(i,j)`; `(t,b)` | gauge invariance; Elitzur IMPORTED (gauge-invariant states) | `PROVEN` + `IMPORTED` | **CLOSED-NEGATIVE** (K9a only) | not new (Schur, Elitzur); mapping new | §22.8 + **C96** | a gauge-variant bilinear with nonzero expectation |
| **M67.39.6** | K9b algebra: with vertex `diag(y₁,y₂)⊗1` and flavour-coherent Hermitian `G`, the Fock block `y₁y₂G₁₂ ≠ 0`; `D_ii` unchanged, `D` Hermitian; for any Hermitian `2×2`, `max(a,c) ≤ λ_max ≤ max(a,c)+\|b\|`. **Not claimed (v3.3): that `λ_max(D)` is a critical coupling or that Theorem 36's bound is unchanged** | ∀ `G`, `y_i` | contact vertex | `PROVEN` (algebra) | **OPEN** for K9b (D36; Proof obligation 39.8) | **OPEN-NOVELTY** (no prior-art sweep on boundary flavour-coherent condensates) | §22.8 + **C99a, C99b, C99c** | an algebraic failure of any of the three identities |
| **M67.39.7** | equal-density arithmetic: if `D` were the admission quantity, `\|D₁₂\|/D_tt ≤ 0.885 %`, `D_cc/D_tt ≤ 6.5×10⁻⁵`, `λ_max/D_tt ≤ 1.0000782` at `n_c = n_t`; **no required density ratio follows** (W16: the audit's family reaches the target at `r ≈ 7.4×10⁵` with `D_cc` kept) | two partners `(u, c)`; one family | + identification, contact, positivity of `G`; **C99d/e OPEN** | `DERIVED-CONDITIONAL` (arithmetic) | **OPEN** (no admission criterion) | OPEN-NOVELTY | §22.8 + **V33, W16** | a coherent-carrier theorem (39.8) that fixes the admission quantity |
| **M67.39.8** | PROOF OBLIGATION (v3.3): joint two-band dispersion, record composition from density blocks, Pauli extremiser under coherence, the functional of `D`/`G` in the critical gap equation, the admission criterion. **v3.4: (i) not needed about a diagonal reference, (ii) = Lemma 39.9, (iii)–(v) → 39.8′** | — | — | **OPEN** (narrowed) | OPEN | — | §22.8, §22.11 | its discharge, in either direction |
| **M67.39.9** | record composition: `Tr((J_E⊗1)G) = Tr(J_E G₁₁) + Tr(J_E G₂₂)`, independent of `G₁₂`; the audit family's record is `κ` for every `r` | ∀ Hermitian `G` | flavour-blind `J_E` (C39) | `PROVEN` (algebra) | CLOSED-PASS | not new (algebra); mapping new | §22.11 + **C100** | a flavour-off-diagonal component of the record operator |
| **M67.39.10** | coherent-channel normal overlap `= 2κ₁κ₂/(κ₁+κ₂)`; `ω = 2√(m₁m₂)/(m₁+m₂) ≤ 1`, equality iff `m₁ = m₂`; `ω_tc = 0.1707` | ∀ `κ₁, κ₂ > 0` | Lemma 36.2 profiles; common angle | `PROVEN` (algebra) + `VERIFIED` (numbers) | CLOSED-PASS | not new (HM–GM); mapping new | §22.11 + **C101, V34** | an edge profile that is not the Theorem-15 exponential |
| **M67.39.11** | pair-channel decoupling: about any flavour-diagonal reference the d-channel Wick kernel is supported on `j = k, l = i`; the linearised coherent channel closes on itself, onset `1 = G₄^{(12)}·[2κ₁κ₂/(κ₁+κ₂)]·𝒦₁₂` (`G₄^{(12)} = y₁y₂/4m_h²`, v3.4.1); `D` does not enter | ∀ diagonal `G₀`; linear order | mean-field/Fock decoupling of §20; flavour number | `PROVEN` (algebra) | CLOSED-PASS (as a statement about the linearised equation) | **OPEN-NOVELTY** (narrowed; object IMPORTED, D41) | §22.11 + **C102** | a flavour-number-violating term in the reference state or interaction |
| **M67.39.12** | C99d CLOSED-NEGATIVE at linear order; C99e OPEN as Proof obligation 39.8′ (response `𝒦_tc`, Pauli extremiser at fixed record, admission ratio `A_tc = G₄^{(tc)}·overlap·𝒦_tc^max ≥ 1` at `G₄^{(tc)} = m_tm_c/(2v²m_h²)`; v3.4.1 normalisation) | linear order | Thm 39.11 | `DERIVED` (a) / **OPEN** (b) | CLOSED-NEGATIVE (a) / OPEN (b) | — | §22.11 + **D39** | (a) a linear-order onset that involves `D`; (b) the computation, in either direction |
| **M67.41** | thermal ceiling: unique stationary `κ = z₀(1+Δ²τ₂²)/(1+Δ²τ₂²+4ε²τ₁τ₂)`, `\|κ\| ≤ tanh(Δ/2T)` for the atlas-generated carrier class (`τ₁, τ₂` relaxation times; type-locked v3.2) | ∀ `ε, τ₁, τ₂ > 0` | Bloch/Lindblad on the carrier | `PROVEN` (algebra) | CLOSED-PASS | NEW (mapping; Bloch steady state standard) | §22.9 + **C97**, W14 | a stationary record above the thermal value |
| **M67.41.1** | `\|κ\| = T₂ ⇒ T/Δ ≤ 1/(2 artanh T₂) = 0.41470` (`κ = −T₂` in the `z₀` convention; sign fixed v3.3); ensemble equality case `0.19675` (`T₂` = the Z-Spin target) | one inequality | + identification | `DERIVED-CONDITIONAL` | CLOSED-PASS (a check that could have failed) | NEW | §22.9 + **V32** | a corpus rest-frame datum warmer than `0.4147 Δ` carrying the record |
| **M67.41.2** | the handoff (RQ2→RQ3) lands on `D-S14-EVENT-001` as **one necessary condition** (`T/Δ ≤ 0.4147` for any thermal route), not a discharge; RQ2↔RQ3 identity [가설] (Remark 41.4) | one condition | Def. 40; Mission RQ3 | `DERIVED-CONDITIONAL` / [가설] | BT-REFORMULATED (re-scoped v3.2) | not new (bookkeeping) | §22.9 + **D28, D30, D33** | a discharge of `D-S14-EVENT-001` violating Cor. 41.1 |
| **M67.38.6** | OBSERVATION: on the lattice half-space with chiral-bag projection the axial density vanishes level by level; robust to `m(x)`, `μ(x)`, a second bag; broken by polarisation-mixing noise | one lattice family | numerics | **[열림]** (no proof; no symmetry of the required type found) | — | OPEN-NOVELTY candidate | §22.7 + **W15** | a proof, or a counterexample in the continuum |
| **M67.37.2** | A5 residue: derivative signs alternate; renormalised stationary equation has ≤ 3 roots in `(−m, m)`; landing + stabilising leaves exactly two real parameters | ∀ cubic counterterm | A1–A4, mean field | `PROVEN` | CLOSED-PASS | NEW (counting) | §22.9 + **C98**, W08 | four off-`πℤ` stationary values |

**Non-claims (new in v3.3).**
**`NC-M67.50`** Proposition 39.6 is algebra about the Fock operator and a `2×2` Hermitian matrix. It does not
assert that `λ_max(D)` is the critical coupling of a coherent two-band carrier, nor that Theorem 36's admission
bound applies to such a carrier (C99d/e OPEN, D36); Corollary 39.7 is arithmetic conditional on those open
items and fixes no required density ratio (W16). K9b is OPEN. The v3.2 sentences "unchanged bound",
"`~2×10⁷` times denser" and "REJECTED-BY-BOUND conditionally on `n_partner ≤ n_top`" are withdrawn.
**`NC-M67.51`** Theorem 39.4 uses Elitzur's theorem for undressed local gauge-variant operators in
gauge-invariant states; it makes no statement about fixed-gauge expectation values, boundary-induced gauge
reductions, or dressed non-local operators.
**`NC-M67.52`** Guards G20, G23 and G24 check declared tokens, sentence-level co-occurrence relations and a
machine-readable claim-state block against the ledger. They do not check the semantics of prose; a
paraphrase of a withdrawn claim that avoids the guarded words is not caught (§1).
**`NC-M67.53`** The title names obstructions and conditional bounds; it does not claim exhaustion of selectors.

**Non-claims (new in v3.2).**
**`NC-M67.46`** Theorem 39.4 excludes colour-off-diagonal and charge-changing boundary condensates only
(K9a). It says nothing about same-gauge-representation generation-flavour coherence (K9b), which is
gauge-invariant; Proposition 39.6 bounds K9b's effect on Theorem 39's bound and Corollary 39.7 closes it
only conditionally on `n_partner ≤ n_top`. "The diagonal mean field is a theorem" (v3.1) is withdrawn.
*(v3.3: the bound and the conditional closure did not hold — Prop. 39.6 is algebra only, K9b is OPEN; NC-M67.50.)*
**`NC-M67.47`** Corollary 41.2 supplies `D-S14-EVENT-001` one necessary condition. It does not discharge
that debt, does not construct the seam environment, and does not identify the RQ2 and RQ3 residues; the
latter is [가설] (Remark 41.4). "Selecting the record value = discharging `D-S14-EVENT-001`" (v3.1) is
withdrawn.
**`NC-M67.48`** Theorem 38.3 does not compute the Fujikawa Jacobian of a local axial rotation `α(x)`
against a fixed bag domain, and does not assert the absence of a boundary `η`/inflow term for such
transformations (Cor. 38.7). "No `η` or inflow term survives" (v3.1) is withdrawn as a statement about
local transformations; for constant `α` the statement is Theorem 38.4.
**`NC-M67.49`** `τ₁, τ₂` (Theorem 41) and `T₂` (the target) are different types; no statement in this paper
relates them.

**Non-claims (new in v3.1; `NC-M67.42`–`NC-M67.44` re-scoped in v3.2 as marked).**
**`NC-M67.42`** Theorem 38.3 is a statement about the `H²`-regulated Lorentzian density inside A1–A4. It
does not compute, transport, or contradict the Euclidean `D̸²`-regulated boundary anomaly of the
bag-boundary literature (D32), and it says nothing outside A4. *(v3.2: and it says nothing about local
`α(x)` — NC-M67.48.)*
**`NC-M67.43`** Theorem 41 is exact for the Bloch class it names; it is not a derivation of the seam
environment. Corollary 41.1 bounds a datum that ZS-S14 does not supply (Cor. 41.2); nothing here
selects `T`. *(v3.2: and nothing here discharges `D-S14-EVENT-001` — NC-M67.47.)*
**`NC-M67.45`** Observation 38.6 is a numerical observation on one lattice family, not a theorem; Theorem
38.3 does not use it, and W15's control outcome is reported as a limitation of the witness, not as
evidence.
**`NC-M67.44`** ~~FREEZE-CANDIDATE is a proposal for the selection question only.~~ *(v3.2: FREEZE-CANDIDATE
is WITHHELD.)* §§4–21 are not terminal; K7's condition and K8 are corpus-external; K9b is a conditional
corpus survivor; A5 and `D-S14-EVENT-001` are upstream inputs.


**Non-claims of v2.4–v3.0** (`NC-M67.15`–`NC-M67.41`; `NC-M67.35`–`NC-M67.37` withdrawn in v3.0): carried unchanged in supplement §S24. `NC-M67.39` there is annotated: K9 = K9a (closed) + K9b (open).

---

## 25. Adversarial referee pass (author-side)

1. *Is Theorem 21 just Peres–Scudo–Terno restated?* No. PSTh show non-covariance; Theorem 21 shows
   the specific consequence that the **invariant** states have `κ = 0`, on a carrier that is not a
   momentum-traced spin state but the spectral subspace of the boundary form. PSTh is cited as
   corroboration of the premise, and §16.4(1) says so.
2. *Is the "A1′ = F-M66.16" identification real or verbal?* It is the exact statement `X_θ ∈ 𝔛(J_E)`
   with `{X_θ, J_E} = 0`, certified symbolically in `θ` (C58). The flip index is `n = θ + π/2`.
3. *Does Theorem 22 close F-M66.17?* No, and `NC-M67.15` says so. It is a topological reduction of
   the domain, not a selection.
4. *Is filter (i) of Theorem 22 target-blind?* Yes — `cos θ̄ < 0` comes from `C47`, which was derived
   before `Re λ` was consulted, and `V19` is the check.
5. *Is Corollary 19.1 the same overclaim v2.2 made and v2.3 withdrew?* No. v2.2 asserted the lift
   was derived without exhibiting the isomorphism; v2.4 computes `det(P₊|_{L_θ}) = 1`. The dynamics
   is still declared, and Corollary 19.1 says exactly that.
6. *Is the paper now three papers?* Very likely: §4–12 (classical), §13–15 (spectral), §16–17
   (symmetry and carrier). A split is the natural next editorial step.

7. *(v2.5)* *Is Theorem 23 just Theorem 15 restated?* No. Theorem 15 is the bound state; Theorem 23
   is every continuum mode at every `(q, k_⊥)`, and the surprise is that `q` drops out entirely.
8. *(v2.5)* *Is "`η ≡ 0`" in conflict with the external report that `η`'s θ-dependence sits in the
   edge states?* No; their edge band is chiral in their dimension, ours is a symmetric 2+1
   fermion. The Euclidean CS level is left open (NC-M67.20).
9. *(v2.5)* *Is Theorem 25 a no-go about our own framing?* Yes, and kernel §5.5 is applied: the
   object that does exist (the pushforward) was built first, and the output is a reframing, not a
   headline no-go.
10. *(v2.5)* *Does the thermal band state close F-M66.15?* No. It meets every **state-side**
    condition target-blind but selects nothing; the sector choice is a named hidden freedom.

11. *(v2.6)* *Is the gap equation just a reparametrisation — one free number for another?* The
    dimension count is unchanged and §19.5 states it. What changes is the **type**: `θ̄` was a
    modulus of a boundary condition with no Lagrangian home; `g` is a coupling with one. Mission
    §4.6 asks exactly for residual freedom to be quantified and relocated to an action parameter.
12. *(v2.6)* *Is `θ̄ = π` at zero coupling a coincidence engineered by the choice `Φ = π`?* `Φ` is a
    construction choice and `D16` says so. What is not a choice is that the point the gap equation
    makes symmetric is the same point Theorem 22 excludes on regularity grounds and Theorem 15
    identifies as the gap-closing point — three independent characterisations of one angle.
13. *(v2.6)* *Does Theorem 27 make the boundary interaction trivial?* The opposite: it makes it
    exactly a self-coupling of the record observable, which is the only kind of interaction that
    could produce a self-consistent `κ`.
14. *(v2.6)* *Is `g_*/g_c = 1.77` evidence?* No — it is read after the identification. It is a
    naturalness check that could have failed, and is typed `DERIVED-CONDITIONAL`.

15. *(v2.7)* *Is "every arrow exists" a selection claim?* No. It is the claim that the question
    "does the action select?" is now well-posed as a computation of one upstream number, with
    every intermediate object exhibited and certified. That is what Mission §4.6 calls closing
    the backbone up to "residual construction freedom computed".
16. *(v2.7)* *Is the Gross–Neveu identification decorative?* It is the only reason X2 has an
    answer: without it "fluctuations are strong in 2+1" would be an unanswerable worry; with it
    the broken phase is a known phase.
17. *(v2.7)* *Why is the residue's move to `ZS-S14` progress rather than deferral?* Because for
    seven versions the angle had no equation; it now has one whose only input is a coupling that
    already exists upstream. Deferral would be inventing a coupling. This is the opposite.

18. *(v2.8)* *Is a factor 42 a kill or a near miss?* A kill, because Theorem 36 already maximises
    the density over all occupations; the only knobs left are `c′` (needs 21) and the physics of
    the mediator (contact assumed). Near misses are factors of two.
19. *(v2.8)* *Could gluon exchange or colour multiplicity rescue the top?* Colour multiplicity
    enhances the Hartree channel, which is the reflection (Thm 33a), not the `d`-channel; gluon
    exchange at `q ~ m` is a factor of a few (D25). Neither reaches 42.
20. *(v2.8)* *Why is this the right kind of failure?* Because the route was written down completely
    before its number was computed, the number was computed with corpus inputs only, and the
    bound that killed it is reusable. That is what a selection backbone is supposed to produce
    when the answer is no.

21. *(v2.9)* *Is closing both horns of an OPEN dichotomy legitimate?* It is the strongest available
    move: the identification `Φ_Z = Φ` stays open, and the verdict no longer depends on it. An open
    question that no longer matters to the conclusion is better than a resolved one. *(v3.0 note: the
    move stands, but the two horns now close differently — A exactly inside A5, B exactly for linear
    bulk couplings and conditionally for the residual — so the dichotomy is relevant to *how*, §23.)*
22. *(v2.9)* *Is Theorem 38 too strong — surely something couples?* ~~The strength comes from Theorem
    27, which is exact: the on-shell bilinear space is two-dimensional.~~ **The audit was right and this
    answer was wrong**: Theorem 27's space is the scalar class; `∂_μθ` contracts a vector current, and
    Lemma 38.0 shows the tangential vector currents are flip elements, not scalars. See item 24.
23. *(v2.9)* *Does the paper end on a negative because the positive was not found?* The positive
    chain was built first (v2.6–v2.7) and is unchanged; what closed is its realisation. The output
    is a map with a reusable bound, which is what the No-Go Emission Gate asks a negative result to be.

24. *(v3.0)* *Does the repaired Theorem 38 still close Horn B?* For linear bulk couplings, yes and
    exactly (C86/C89/C90). For the shift-symmetric residual, only conditionally on `f = M_P`; the
    residual is a genuine flip-odd coupling to the record and is reported as a survivor, not hidden.
25. *(v3.0)* *Is the per-band Theorem 39 not just v2.8's item 19 restated?* It is item 19 promoted to a
    certificate (C92) and joined to the multiplicity lemma (C91). v2.9 contradicted item 19; v3.0
    proves it and names the case it excludes (K9). *(v3.2: K9 = K9a closed + K9b open.)*
26. *(v3.0)* *Is Corollary 40.1 a new theory smuggled in during a correction?* No theorem depends on
    it; it is typed [가설]/BT-REFORMULATED and lives in the handoff. What is certified is W14: on the
    corpus chain, the pointer is derived and the value is a rest-frame datum.
28. *(v3.1)* *Is Theorem 38.3 circular — `𝒞` was built to anticommute with `H`?* No: `𝒞` is the
    standard charge conjugation, fixed in v2.5 for a different purpose (Thm 24), and the new content is
    the pointwise density flip together with `𝒞L_θ = L_θ`, which is what makes the boundary cancel.
29. *(v3.1)* *Does Elitzur's theorem apply to a boundary condensate?* It applies to any **undressed** gauge-variant
    local operator in a gauge theory with the gauge symmetry unbroken as a local symmetry, **in gauge-invariant
    states** (scope narrowed in v3.3, Thm 39.4); a boundary does not change that for an undressed local bilinear
    at the wall. The mapping (the operator is gauge-variant) is what C96 certifies.
30. *(v3.1)* *Is the thermal ceiling a tautology of detailed balance?* For `ε = 0` it is; the content is
    that a static flip-odd term — the only carrier-level handle the atlas allows — cannot exceed it.
    That is what turns "rest-frame datum" into an inequality on `T`.
27. *(v3.0)* *Why not simply delete §22 and leave the kill at v2.8?* Because the repaired §22 contains
    results v2.8 did not have: the bilinear atlas, the current divergences with boundary flux, the
    multiplicity lemma, the Fock block theorem, and a registry that owns its quantifier.

31. *(v3.2)* *Item 29 said Elitzur applies to any gauge-variant local operator — so what went wrong in
    Theorem 39.4?* Nothing in item 29; the error was the quantifier in the next sentence. `ū Γ c` with colour
    contracted is not gauge-variant, so Elitzur has nothing to say about it. v3.1 wrote "colour/flavour" as
    one word where the certificate had only computed colour and charge. The audit was right.
32. *(v3.2)* *Is Proposition 39.6 a rescue of the multi-band route through the back door?* ~~No. It shows the
    coherent case can only loosen the bound, quantifies the loosening for the SM at `< 1 %` at equal
    density, and names the object that would be needed to close the gap (a `2 × 10⁷`-fold denser partner
    band).~~ **Withdrawn in v3.3 (S3): see item 36.** What survives: it is reported in the favourable direction
    precisely because v2.9's error was in that direction, and it is no rescue (Remark after Prop. 39.6).
33. *(v3.2)* *Does weakening Corollary 41.2 to a necessary condition cost the Mission anything?* It costs a
    sentence, not a result. The inequality is unchanged; what changed is that a temperature is no longer
    called a selector. Definition 40 already listed S4 and S6 as unsupplied; Cor. 41.2 had contradicted it.
34. *(v3.2)* *Is Theorem 38.3 weaker now?* Its certified content is identical (C94's algebra). What is
    withdrawn is a sentence that read a spectral cancellation on `dom H` as a change-of-variables Jacobian
    for transformations that leave `dom H`. The constant case was always Theorem 38.4.
35. *(v3.2)* *Why report the package's exit 1 when the audit found exit 2?* Because a clean room is defined
    by the files delivered, and the delivered four files failed two guards, not one. VERIFY §14: a package
    that does not reproduce its declared result on first run is a clean-room FAIL, whatever the exit code.

36. *(v3.3)* *Why did v3.2's K9b bound not survive?* Because a bound proved for one band was applied to a
    coherent carrier through a matrix inequality, without the theorem that says the matrix's eigenvalue is
    what the coherent gap equation sees. The inequality is true; the transfer was unproved; the audit's
    positive family shows the transferred number was not even the family's number (`7.4×10⁵` vs `2.16×10⁷`).
37. *(v3.3)* *Does restoring K9b to OPEN weaken the paper?* It removes a false precision. The map now says,
    for K9b, exactly what is proved (algebra), what is not (the admission criterion), and what would decide
    it (Proof obligation 39.8, five objects). That is what Mission §6.2's "surviving complement" asks for.
38. *(v3.3)* *Are the new guards semantic now?* No, and §1 says so. They protect declared tokens, sentence-level
    co-occurrence relations and a claim-state block. The audit's two injections now fail; a paraphrase would
    not. The honest claim is "the guards fail on the injections we have seen", not "the guards read prose".
39. *(v3.3)* *Why embed the baseline instead of shipping the file again?* Because a clean room is defined by
    the files received, and a five-file package delivered as four has failed twice. Fingerprints (id, class,
    hash of claim) are enough for G18 to measure carried/retyped/added/removed, and the JSON, when present, is
    checked against them.

40. *(v3.4)* *Does §22.11 do what the v3.3 audit told the paper not to do — add a coherent many-body theorem to a
    correction version?* No. It adds two algebraic lemmas and a symmetry statement about the *linearised* equation,
    each certified (C100–C102), and it leaves K9b OPEN; the version is reclassified as a major revision so that the
    addition is not silent (MANUSCRIPT §16). The many-body content — the response `𝒦_tc` and its extremiser — is
    written out as an obligation, not claimed.
41. *(v3.4)* *Is Theorem 39.11 a tautology?* As a symmetry statement it is elementary; its content is the layer split it
    forces: the object v3.2 compared with the bound (`λ_max(D)`) is the order parameter, and the object that decides the
    onset is a response kernel in which `D` cannot appear. That is what closes C99d at linear order.
42. *(v3.4)* *Does typing the ceiling as target-conditioned weaken Corollary 41.1?* No inequality changed. What changed is
    a word: a capacity bound conditioned on `|κ| = T₂` was called target-blind, which would have let it be read as a
    selection statement. The ceiling itself is target-independent and says so.
43. *(v3.4)* *Why make the manifest a core object when it is generated at run time?* Because VERIFY §9.1 names it as the
    fourth authoritative object and the audit found the declaration and the generated graph disagreeing; the manifest is
    now the single machine source for the object graph, the session file is what it is — a provenance record — and G25
    fails the run if the manuscript says otherwise.
44. *(v3.4)* *Why report the W15 residual at all?* Because "byte-identical re-runs" was true only on one machine. A claim
    string that embeds a `1e-16` number is not a claim; it is a measurement, and it belongs in the detail field.

45. *(v3.4.1)* *How could v3.4 count the Yukawas twice one section after certifying `G₄ = y²/4m_h²`?* Because §22.11 was
    written in the flavour-blind convention (`Ĝ₄ = 1/4m_h²`, Yukawas explicit) while every earlier section uses the
    band-specific one (`G₄ = y²/4m_h²`, Yukawas inside), and the symbol was not renamed at the seam. The certificates were
    never affected — C101 and C102 are statements about an integral and a kernel — but the *obligation* was, and an
    obligation is exactly what a successor computation reads first. The repair is a naming convention, `G₄^{(ij)}`, and a
    CLAIM-STATE token (`G4-channel=YUKAWA-INSIDE`) so that the seam is declared.

**Strongest single objection (v3.4).** *After three audits on the same section, the paper now adds new results to it;
why should a referee believe §22.11 is not the fourth over-reach?* Because each of its three statements is an exact
certificate about a finite algebraic object (a trace identity, an elementary integral, sixteen kernel entries), each
says in its own row what it does *not* establish, and the physical question they bear on (the coherent admission price)
is left OPEN with its computation written out. The delta re-audit decides whether the separation held.

**Strongest single objection (v3.3).** *The K9b episode shows the paper can certify algebra and still assert
physics it has not proved; why trust the other conditional rows?* Because the other conditional rows (K7, the
identification, `f = M_P`, mean field) name their conditions as hypotheses rather than as bounds, and the
exact rows are exact inside classes that are now written in the title, §2 and §22.10. The K9b failure was a
layer jump from a matrix to a gap equation; the v3.3 repair is to type the jump as an obligation, not to
re-derive around it. The delta re-audit decides whether that suffices; FREEZE-CANDIDATE is withheld until it.

**Strongest single objection (v3.2).** *The paper has now been re-scoped three times on the same section;
why believe the quantifiers are right this time?* Because each quantifier in §22.8–22.9 is now owned by a
certificate that says what it does **not** cover (C94, C96) or by a computation that bounds the excluded
case (C99, V33), and because the survivors are listed with their conditions rather than as absent. That is
a claim about the *form* of the statements, not their truth; the truth still waits on the delta re-audit,
and FREEZE-CANDIDATE is withheld until it.

**Strongest single objection.** *Three no-gos and a lift do not make a selection.* **Accepted for
v2.4–v2.5.** *(v2.6)* A mean-field gap equation is not a selection either, but it is a different
kind of object: for the first time the angle satisfies an equation instead of labelling a point.
Output role stays `SUPPORT`. ~~The value is that after v2.4 the remaining object is completely
specified — an action-derived, non-unital, flip/boost-symmetry-breaking CPTP map with a unique
faithful stationary state on a carrier whose lift, grading, unitary and state family are all now
derived — and the remaining angular freedom is confined to an explicitly characterised arc.~~
**Replaced in v3.4 (v3.3 audit, S2; the struck sentence read as a construction):** The **signature** of the missing
object is now completely specified: any successful completion must produce an action-derived, non-unital,
flip/boost-noncovariant CPTP map with a unique faithful biased stationary state. No such map or state-selection
mechanism is constructed in M67. What is derived is the carrier, the grading, the boundary lift and the admissible
state/operation families; the remaining angular freedom is confined to an explicitly characterised arc.

---

## 26. Limitations and open items

- **(v3.4.1) What remains, and where it goes.** The v3.4 audit found the `G₄` normalisation conflict of obligation 39.8′
  (repaired) and recommends freezing M67 after this correction. Accordingly nothing inside M67's scope is worked further
  in this line: Proof obligation 39.8′ (with the corrected admission ratio `A_tc`) and Cor. 38.7 are **handed to the
  successor positive-construction line** as typed inputs (no identifier reserved); K9b stays an OPEN survivor of the frozen
  map. FREEZE-CANDIDATE **PROPOSED**; user approval required.
- **(v3.4, superseded in its lifecycle sentence) What remains, after the third audit.** Inside the paper's scope: **Proof obligation 39.8′** (the interband
  response `𝒦_tc` of Theorem 39's diagonal state, its Pauli extremiser at fixed record `|κ| = T₂`, and the comparison with the
  corpus `G₄`; K9b is OPEN until it exists) and the local-`α(x)` domain-preservation obligation (Cor. 38.7, [열림], not
  attempted in v3.4). Conditional survivor: K7 (`f = M_P`). Corpus-external: K8. Upstream: A5 (two reals), `D-S14-EVENT-001`
  (OPEN; one target-conditioned necessary condition supplied). Standing: RP, Lorentzian↔Riemannian, OPEN-NOVELTY sweeps
  (bilinear atlas; boundary Gross–Neveu mapping; boundary flavour-coherent condensates — one family run, D41), Observation
  38.6, the v2.3 wording of A4/A5 (NOT_FOUND in repos 1/2), third-party clean-room / L6. **FREEZE-CANDIDATE WITHHELD**;
  re-proposal only after a targeted delta re-audit finds no new S2+. No identifier is assigned and none is reserved.
- **(v3.3, superseded in part) What remains, after the second audit.** Inside the paper's scope: **the coherent two-band admission
  theorem** for K9b (Proof obligation 39.8 — a research item; K9b is OPEN until it exists), and the
  local-`α(x)` domain-preservation obligation of Theorem 38.3 (Cor. 38.7, [열림]). Conditional survivor with a
  named condition: K7 (`f = M_P`). Corpus-external: K8. Upstream: A5 (two reals), `D-S14-EVENT-001` (OPEN;
  one necessary condition supplied). Standing: RP, Lorentzian↔Riemannian (Remark 4.1), OPEN-NOVELTY sweeps
  (bilinear atlas; boundary Gross–Neveu mapping; **boundary flavour-coherent condensates, none run**),
  Observation 38.6, the exact v2.3 wording of A4/A5 (editorial), third-party clean-room / L6.
  **FREEZE-CANDIDATE WITHHELD**; re-proposal only after a delta re-audit finds no new S2+. No identifier is
  assigned and none is reserved.
- **(v3.2, superseded) What remains, after the audit.** ~~Conditional survivors with named conditions: K7
  (`f = M_P`), K9b (`n_partner ≤ n_top`)~~ — *v3.3: K9b's condition was not a theorem; K9b is OPEN.*
- **Superseded open-item bullets (v2.5–v3.1)** are kept verbatim in supplement §S26; each carries its later disposition.
- **A6.** Mandatory and named. Any frame-independent reformulation must first solve the reduced-spin
  covariance problem, which the external literature reports as unsolved. `[열림]`
- **A5, A4, A1, A1′, faithfulness, Lorentzian↔Riemannian, Def. 13.2's prefactor**: unchanged from
  v2.3. `[열림]`
- **Independence (v3.3).** The v3.2 audit was **L3 (another model family) + L5 (deterministic re-execution and
  an explicit counterexample)**, and it is integrated in full. Artifact K: 48 rows, FAIL 0, DEGRADED 0, run
  from a fresh directory containing **only the four core files** (manuscript, script, ledger, session);
  live-fire outputs in the session file, including the audit's two semantic injections (both FAIL in v3.3);
  the audit's counterexample family re-derived by explicit `8×8` construction (W16: `λ_max = 42.068` at
  `r = 7.44×10⁵`, `min eig G = −1×10⁻¹⁰`); a blank-context subagent check of the five repair items (same
  model, L2). Third-party clean-room of artifact K and L6 anchor: NONE.
- **Independence (v3.2).** Artifact J: 42 rows, FAIL 0, DEGRADED 0, run from a fresh directory containing only
  the four v3.2 core files plus the v3.1 ledger; live-fire on G17/G18/G20/G23 with outputs recorded in the
  session file; sympy/numpy cross-check of C99 by an independent random-PSD route (2000 samples: the
  favourable direction `λ_max > max D_ii` occurs in every sample, the Cauchy–Schwarz bound is never
  violated; same model, L2). **Clean-room finding on the delivered v3.1 package (beyond the audit):** the
  four files as delivered (manuscript, script, ledger, session) give 38 rows, 36 identical to the delivered
  ledger, G18 DEGRADED (no v3.0 ledger) **and G22 FAIL** (no lineage sibling script beside it), exit 1 —
  a clean-room FAIL under VERIFY §14, stricter than the audit's exit 2. Third-party clean-room and L6
  anchor: NONE.
- **Independence (v3.1).** Artifact I: 38 rows *(v3.1 printed "37" here — corrected)*, FAIL 0, DEGRADED 0; live-fire on G17/G18/G20 repeated;
  numpy cross-check of C94–C97 by an independent route (same model, L2); the first lattice witness
  attempted a `μ`-control that could not fire (Observation 38.6) and is reported as such. Lineage rescan: G defective on
  both counts, H and I clean, C–F unavailable. ZS-S14 v2.1 read from repo 1. Third-party clean-room and
  L6 anchor: NONE.
- **Independence (v3.0).** The v2.9 audit was a cross-family round on §22 and is integrated in full.
  Artifact G was re-executed this session in a clean directory without the v2.8 ledger: 16 rows,
  FAIL 0, **G18 DEGRADED, exit 0** — reproducing the audit's package finding. Artifact H was run in the
  same environment: 27 rows, FAIL 0, DEGRADED 0. Same model; L2.
- **Independence.** Four cross-family adversarial audit rounds integrated (A1–A18). Artifact B
  re-executed in a fresh container this session (same model; L2): 48 rows, FAIL 0, 47/47
  non-provenance rows identical, sha identical. **No independent clean-room execution by a third
  party.** L6 anchor: NONE.

---

## 27. Availability

```text
artifact A:    zs_m67_verify_v2_1.py     ledger: zs_m67_verify_v2_1.json     (82 rows)
artifact B:    zs_m67_verify_v2_4.py     ledger: zs_m67_verify_v2_4.json     (48 rows)
artifact C:    zs_m67_verify_v2_5.py     ledger: zs_m67_verify_v2_5.json     (22 rows)
artifact D:    zs_m67_verify_v2_6.py     ledger: zs_m67_verify_v2_6.json     (21 rows)
artifact E:    zs_m67_verify_v2_7.py     ledger: zs_m67_verify_v2_7.json     (18 rows)
artifact F:    zs_m67_verify_v2_8.py     ledger: zs_m67_verify_v2_8.json     (17 rows)
artifact G:    zs_m67_verify_v2_9.py     ledger: zs_m67_verify_v2_9.json     (16 rows; SUPERSEDED
                                                                            by H; ledger shipped)
artifact H:    zs_m67_verify_v3_0.py     ledger: zs_m67_verify_v3_0.json     (27 rows; SUPERSEDED
                                                                            by I)
artifact I:    zs_m67_verify_v3_1.py     ledger: zs_m67_verify_v3_1.json     (38 rows; SUPERSEDED
                                                                            by J)
artifact J:    zs_m67_verify_v3_2.py     ledger: zs_m67_verify_v3_2.json     (42 rows; SUPERSEDED
                                                                            by K; its 42 row
                                                                            fingerprints are
                                                                            EMBEDDED in K)
artifact K:    zs_m67_verify_v3_3.py     ledger: zs_m67_verify_v3_3.json     (48 rows; SUPERSEDED
                                                                            by L; its 48 row
                                                                            fingerprints are
                                                                            EMBEDDED in L)
artifact L:    zs_m67_verify_v3_4.py     ledger: zs_m67_verify_v3_4.json     (56 rows; SUPERSEDED
                                                                            by M; its 56 row
                                                                            fingerprints are
                                                                            EMBEDDED in M)
artifact M:    zs_m67_verify_v3_4_1.py     ledger: zs_m67_verify_v3_4_1.json     (57 rows)
package (v3.4.1 core, AUTHORITATIVE, VERIFY sect.9.1; four objects):
               ZS-M67_v3_4_1.md · zs_m67_verify_v3_4_1.py · zs_m67_verify_v3_4_1.json ·
               release_manifest_v3_4_1.json (generated at run time from the measured hashes; the
               single machine source of the object graph; no self-hash fixed point)
provenance objects (registered in the manifest with measured hashes when present; NOT read by the
               verifier's evidence rows; not core):  session_M67_v3_4_1_Ref_202609040800.md ·
               the v3.3 and v3.4 audit reports as received (audit_M67_v3_3_as_received.md,
               audit_M67_v3_4_as_received.md) · ZS-M67_v3_4_1_provenance_supplement.md
optional:      zs_m67_verify_v3_4.json (cross-checked against the embedded baseline if present)
byte identity:  the shipped ledger is the core run (no optional v3.3 JSON).  Re-runs with the same
               file set on the same machine are byte-identical; adding the optional JSON changes the
               json_crosscheck field, hence the ledger's own sha256 and the manifest's baseline block
               -- and nothing in any row's result or in the census.  CROSS-MACHINE: v3.3's W15 embedded
               a 1e-16 residual in its claim text and was NOT byte-identical across machines (sect.1);
               v3.4 states residuals as thresholds so that claim fingerprints are machine-independent;
               detail fields may still differ at the last printed digit and are not fingerprinted.
               Declared here per VERIFY sect.9.2.
run:           python3 zs_m67_verify_v2_4.py            (exit 0 iff FAIL == 0)
               python3 zs_m67_verify_v2_5.py            (exit 0 iff FAIL == 0; ~11 s; expects the
                                                          v2.4 ledger beside it for G18)
               python3 zs_m67_verify_v2_6.py            (exit 0 iff FAIL == 0; ~13 s; expects the
                                                          v2.5 ledger and this manuscript)
               python3 zs_m67_verify_v2_7.py            (exit 0 iff FAIL == 0; ~50 s; expects the
                                                          v2.6 ledger and this manuscript)
               python3 zs_m67_verify_v2_8.py            (exit 0 iff FAIL == 0; ~10 s; expects the
                                                          v2.7 ledger and this manuscript)
               python3 zs_m67_verify_v3_4_1.py            (artifact M; exit 0 iff FAIL == 0 and
                                                          DEGRADED == 0; exit 1 on FAIL, 2 on
                                                          DEGRADED or on an empty ledger; ~15 s;
                                                          expects ONLY this manuscript beside it
                                                          (found as ZS-M67_v3_4_1.md or *M67_v3_4_1.md);
                                                          the v3.4 ledger is optional; paths
                                                          overridable by ZS_M67_PAPER,
                                                          ZS_M67_PREV_LEDGER; G22 rescans every
                                                          zs_m67_verify_v*.py beside it and reports
                                                          absent siblings as NOT SHIPPED; writes the
                                                          ledger and the manifest)
               python3 zs_m67_verify_v2_4.py --merge-notes
runtime note:  the Groebner reduction of C48 and the symbolic blocks of C52/C56-C60 dominate;
               allow several minutes.  An audit round previously timed out on the v2.3 block.
```

```text
AI_TOOL_RECORD
name/version:   Claude (claude-opus-5), 2026-09-02 KST  (v2.4);  Claude (Claude Fable 5.1),
                2026-09-02 KST  (v2.5: Section 18, artifact C, the fresh-container re-execution
                of artifact B, the corpus-index consultation);  Claude (Claude Fable 5.1),
                2026-09-02 KST  (v2.6: Section 19, artifact D, the ZS-M66 v1.5.1 primary read);
                Claude (Claude Fable 5.1), 2026-09-02 KST  (v2.7: Section 20, artifact E);
                Claude (Claude Fable 5.1), 2026-09-02 KST  (v2.8: Section 21, artifact F, the
                ZS-S14 v2.1 primary read, two web-search sweeps);
                Claude (Claude Fable 5.1), 2026-09-02 KST  (v2.9: Section 22, artifact G);
                Claude (Claude Fable 5.1), 2026-09-03 KST  (v3.0: audit integration, Section 22
                rewrite, artifact H, clean-room re-execution of artifact G);
                Claude (Claude Fable 5.1), 2026-09-03 KST  (v3.1: Thms 38.3-38.4, 39.4, 41, Cor 37.2,
                artifact I, the ZS-S14 v2.1 read, the repo-2 search, one web sweep);
                Claude (claude-fable-5-1, configured; serving model may differ), 2026-09-03 KST
                (v3.2: integration of the v3.1 audit, Thm 39.4 split, Prop 39.6 / Cor 39.7, Cor 38.7,
                Cor 41.2 re-scoping, type lock, artifact J, clean-room re-execution of artifact I);
                Claude (claude-fable-5-1, configured; serving model may differ), 2026-09-04 KST
                (v3.3: integration of the v3.2 audit (another model family, L3 + L5), withdrawal of
                the K9b quantitative conclusion, W16 reproduction of the audit's counterexample,
                Proof obligation 39.8, Elitzur scope, |kappa| sign, A1-A6 restatement, title,
                artifact K with embedded baseline and claim-state guards, provenance supplement);
                Claude (claude-fable-5-1, configured; serving model may differ), 2026-09-04 KST
                (v3.4: integration of the v3.3 audit (another model family; L3 + L5), the sect.25
                signature statement, target-independent/target-conditioned typing, the four-object
                core and G25, Elitzur citation and hypotheses, exit_code([]) -> 2, the W15 cross-
                machine finding, sect.22.11 (Lemmas 39.9-39.10, Thm 39.11, Cor. 39.12, obligation
                39.8'), the K9b prior-art sweep (Blasone et al. 2018, primary PDF), the repo-1/2
                search for the v2.3 wording, artifact L);
                Claude (claude-fable-5-1, configured; serving model may differ), 2026-09-04 KST
                (v3.4.1: integration of the v3.4 audit (another model family, L3): the G_4
                channel-strength correction of sect.22.11 / obligation 39.8', V34's channel
                strengths, the freeze proposal, artifact M)
tasks:          authoring; the boost/rotation carrier computation; the lift isomorphism; the
                literature search and interpretation of the three external anchors; artifact B;
                (v2.5) the polarisation law, charge-conjugation theorem, no-autonomous-map witness,
                uniqueness-transfer lemma, band thermal closed forms; artifact C;
                (v2.6) the on-shell collapse, the boundary gap equation and its selection identity,
                the edge 2+1 mass, the theta_m convention check; artifact D;
                (v2.7) the free-bulk no-go, the Yukawa on-shell bilinear, the Hartree reflection,
                the Fierz d-channel, the Z_2 orbit, the T=0 self-consistent solution; artifact E;
                (v2.8) the contact coefficient, the edge overlap, Theorem 36 and its evaluation;
                artifact F; (v2.9) both horns of the Goldstone route, the multi-band scaling, the
                standing filter; artifact G; (v3.0) the bilinear atlas, the on-shell current
                divergences, the multiplicity ideal computation, the Fock block theorem, the
                candidate registry, the selector signature and qubit witness; artifact H;
                (v3.1) the charge-conjugation Jacobian argument, the unitary-equivalence theorem, the
                su(3) commutant and Elitzur mapping, the Bloch steady state and ceiling, the
                derivative-sign count; artifact I; (v3.2) the flavour-coherent Fock block, the
                2x2 eigenvalue bracket, the Cauchy-Schwarz bound for K9b, guard G23; artifact J;
                (v3.3) the retraction analysis of Prop. 39.6's physical reading, the explicit 8x8
                reproduction of the audit's counterexample family, the embedded-baseline G18, the
                sentence-level guard rules, G24, the functional G21, the manifest writer; artifact K;
                (v3.4) the record-composition identity, the harmonic-mean overlap, the sixteen-entry
                kernel evaluation, the omega numbers, guard G25 and G20(iv), the four-object manifest,
                the W15 retyping; artifact L; (v3.4.1) the G_4^(ij) renaming, V34's channel-strength
                numbers and their consistency check, guard tokens; artifact M
independently checked: arXiv:2208.00476 authorship; arXiv:2305.13606 = PLB 844 (2023) 138098
                findings (smooth eta is chiral-bag-angle independent; theta dependence in edge
                states); PRL 88, 230402 (2002) statement.  All read from primary listings or
                primary PDF text this session.  (v3.1) arXiv:hep-th/0309019 existence and
                abstract-level entailment (boundary chiral anomaly for local bag conditions,
                Euclidean); ZS-S14 v2.1 sect.2.11 / 10.3.5 / 14.1 read in full from repo 1.
                (v3.4) Elitzur, Phys. Rev. D 12, 3978 (1975): existence and abstract-level entailment
                from the primary APS listing; Blasone-Jizba-Mavromatos-Smaldone, arXiv:1807.07616:
                primary PDF read in full (off-diagonal flavour condensates as the signature of mixing;
                residual U(1)_V; eq. 40).  Repo 1/2 searched for the ZS-M67 v2.3 manuscript by title
                and full text: NOT_FOUND.
not done:       independent human review; third-party clean-room reproduction; formal proof
                checking; full primary-text reading of the eta-invariant computations; (v3.2) a
                domain-preservation proof for local axial rotations (Cor. 38.7); a prior-art
                sweep on boundary flavour-coherent condensates (K9b) -- none run this session;
                (v3.3) the coherent two-band admission theorem (Proof obligation 39.8) -- NOT
                attempted in a correction version; the v2.3 wording of A4/A5 -- not re-read;
                (v3.4) the interband response computation of Proof obligation 39.8' -- not attempted;
                Cor. 38.7 -- not attempted; the v2.3 wording of A4/A5 -- NOT_FOUND in repos 1/2;
                third-party clean-room execution of artifact L; (v3.4.1) the response computation of
                obligation 39.8' and Cor. 38.7 -- handed to the successor line, NOT attempted;
                third-party clean-room execution of artifact M
```

---

## 28. References (v2.4 additions)

18. **A. Peres, P. F. Scudo, D. R. Terno**, *Quantum Entropy and Special Relativity*, Phys. Rev. Lett. **88**, 230402 (2002); arXiv:quant-ph/0203033. *(the reduced spin density matrix is not Lorentz covariant; the spin entropy is not a relativistic scalar)*
19. *Edge states and the `η` invariant*, arXiv:2305.13606; Phys. Lett. B **844** (2023) 138098. *(smooth part of `η(0,H)` is independent of the chiral-bag parameter; the parameter dependence resides in the edge states; earlier `η`-inflow analyses covered only massless operators without boundary states.* **Author list not verified from primary listing.** *This reference supersedes the "Phys. Lett. B 844 (2023) 138098" entry of v2.2/v2.3, which is the same paper.)*
20. *Edge States: Topological Insulators, Superconductors and QCD Chiral Bags*, arXiv:1308.5635; JHEP **12** (2013) 073. *(explicit chiral-bag edge spinor `(e^{θ/2}, −i e^{−θ/2})` on the half-line)*
21. L. F. Calderón, E. Marulanda, S. Morales, L. A. Pachón, *Galilean boost invariance does not survive the trace*, arXiv:2604.27459 (via `PACKAGE_boundary_channel` §3.2). *(precedent: an explicitly boost-invariant system–bath Lagrangian yields a reduced dynamics violating boost covariance)*

22. **S. Elitzur**, *Impossibility of spontaneously breaking local symmetries*, Phys. Rev. D **12**, 3978–3982 (1975). doi:10.1103/PhysRevD.12.3978. *(IMPORTED in Theorem 39.4; primary APS listing read in v3.4: "a spontaneous breaking of local symmetry for a symmetrical gauge theory without gauge fixing is impossible"; the proof uses gauge invariance and positivity of the measure, hence hypothesis H1.)*
23. **M. Blasone, P. Jizba, N. E. Mavromatos, L. Smaldone**, *Chiral symmetry-breaking schemes and dynamical generation of masses and field mixing*, arXiv:1807.07616. *(external baseline for K9b, §22.11 / D41; primary PDF read in v3.4: dynamically generated mixing requires flavour-off-diagonal condensates; residual `U(1)_V`; bulk, global symmetry, no boundary. Journal reference not verified this session.)*
24. **M. Blasone, P. Jizba, L. Smaldone**, *Effective action approach to dynamical generation of fermion mixing*, arXiv:1606.00320. *(secondary; abstract level only.)*

References 1–17 unchanged from v2.3.

---

## 29. Corrections of record (v2.4–v3.4.1)

**v3.4.1 (audit of v3.4 accepted in full, 0 findings rejected; correction-only; one notation/normalisation correction
inside §22.11; freeze proposed).**
- **`G₄` in Theorem 39.11 and Proof obligation 39.8′ CORRECTED** (scope/notation correction; the v3.4 audit's one substantive
  finding). Wrong statement: `1 = G₄·y₁y₂·[2κ₁κ₂/(κ₁+κ₂)]·𝒦₁₂` and "(c) compare `1/(G₄y_ty_cω_tc√(κ_tκ_c)𝒦_tc^max)` with the corpus
  `G₄ = m_t²/(2v²m_h²)`". Why wrong: Lemma 36.1's `G₄ = y²/4m_h²` already contains the band's Yukawa, so `G₄·y₁y₂` counts it
  twice, and (c) had `G₄` on both sides with a top-specific value on the right. Downstream: nothing certified changes (C101,
  C102 unchanged in content; V34's ratios unchanged); any successor computation that read (c) literally would have started
  from a wrong normalisation — that is why it is corrected before the freeze. Replacement: `G₄^{(ij)} := y_iy_j/4m_h²`,
  `1 = G₄^{(12)}·[2κ₁κ₂/(κ₁+κ₂)]·𝒦₁₂`, `A_tc := G₄^{(tc)}·[2κ_tκ_c/(κ_t+κ_c)]·𝒦_tc^max ≥ 1` at `G₄^{(tc)} = 1.150×10⁻⁷ GeV⁻²`.
  Guard: CLAIM-STATE `G4-channel=YUKAWA-INSIDE`. History: proposed row (session file); H-0288 is not edited.
- **Lifecycle:** FREEZE-CANDIDATE WITHHELD → **PROPOSED** on the v3.4 audit's recommendation; user approval required.
- **Package:** artifact M (57 rows) supersedes L; the artifact-L baseline is embedded; `release_manifest_v3_4_1.json`.

**v3.4 (audit of v3.3 accepted in full, 0 findings rejected; scope corrections, package repair, one self-found
artifact defect; a separated research addition).**
- **§25 physical-bridge sentence REPLACED** (S2): the v2.6 "Strongest single objection" reply asserted that the remaining
  object — an action-derived non-unital CPTP map with a unique faithful stationary state — was "completely specified …
  all now derived". Reason: the sentence read as a construction; the map, the environment, S4, the instrument and S6 are
  not constructed in M67. Replacement: the signature is specified, the object is not constructed. Guard G20(iv).
- **"first target-blind constraint" WITHDRAWN** (S2; Cor. 41.3(ii), and the "first inequality" sentence of Cor. 41.1).
  Reason: `T/Δ ≤ 0.4147` inserts `|κ| = T₂` and is target-conditioned; only the ceiling is target-independent. The same
  typing is written for Theorem 36's `×42` verdict. No inequality changed (V32 retyped).
- **Release core corrected** (S2): the §27 core now names manuscript, verifier, ledger and release manifest; the session
  file is a provenance object. Reason: the generated manifest and the declaration disagreed. Guard G25.
- **Elitzur**: citation and hypotheses H1/H2 added to Theorem 39.4 / C96 (editorial-scope).
- **`exit_code([]) → 2`** (G21). Reason: an empty ledger passed silently.
- **W15 and W16 retyped** (self-found, S3): W15's claim text embedded a machine-dependent `1e-16` residual; the v3.3 statement
  "re-runs are byte-identical" held on one machine only, and the provenance count "carried 27" moved to 26 on another. A
  lineage rescan (VERIFY §7.3) for the same defect type found one more instance, W16's `1e-12` eigenvalue residual.
  Replacement: threshold-form claims; measured values in `detail`.
- **§22.11 added** (research; major revision): Lemmas 39.9–39.10, Theorem 39.11, Corollary 39.12; **C99d CLOSED-NEGATIVE
  at linear order**; **C99e OPEN as Proof obligation 39.8′**; K9b OPEN. Nothing in §4–22.10 is changed by it.
- **Package**: artifact L (56 rows) supersedes K; the artifact-K baseline (48 fingerprints from the shipped ledger) is
  embedded; `release_manifest_v3_4.json` registers core and provenance objects. History rows H-0284/H-0285 are not edited;
  superseding rows are proposed (session file).

**v3.3 (audit of v3.2 accepted in full, 0 findings rejected; one retraction, scope corrections, package repair).**
- **The K9b quantitative conclusion of v3.2 is RETRACTED** (S3): "flavour coherence leaves Theorem 39's bound
  unchanged", "a coherent charm band `~2×10⁷` times denser than the top band would be needed", and "K9b is
  REJECTED-BY-BOUND conditionally on `n_partner ≤ n_top`". Reason: Theorem 36's bound is a single-band result
  whose transfer to a coherent two-band carrier requires a gap/occupation theorem that does not exist here;
  the `2×10⁷` figure also dropped the charm diagonal `D_cc` — the audit's positive rank-one family reaches the
  target at `r ≈ 7.4×10⁵` (W16). **Replacement**: Prop. 39.6 restricted to algebra (C99a–c); C99d/C99e typed
  OPEN (D36); Proof obligation 39.8; **K9b OPEN**; V33 retyped as equal-density arithmetic conditional on D36.
  Downstream: registry (V30), §22.10, §23, §24, the OPEN-DEBTS block, §26; history rows H-0282/H-0283 recorded
  the withdrawn statements and are superseded by proposed rows, not edited.
- **Elitzur's scope is NARROWED** in Theorem 39.4 / C96 (undressed local operators, gauge-invariant states);
  K9a's status is unchanged.
- **`κ = T₂` → `|κ| = T₂`** (`κ = −T₂` in the `z₀` convention) in Cor. 41.1 / V32 / W14; the inequality is unchanged.
- **A1–A6 restated** in §2 (A4/A5 reconstructed from use, marked). **"RQ1→RQ3" → "RQ2→RQ3"** in the front matter.
  **Prop. 39.6 novelty NEW → OPEN-NOVELTY.** **Title narrowed**; the former title is recorded under it.
- **Package**: artifact K (48 rows) supersedes J; the artifact-J baseline is **embedded** (the auditor's four-file
  run of v3.2 gave G18 DEGRADED, exit 2 — the fifth file was the baseline); `release_manifest_v3_3.json`
  generated at run time; four core files reproduce 42→48 rows, 0/0, exit 0.
- **Guards**: G20 and G23 passed the audit's semantic injections; v3.3 adds sentence-level claim-state and
  symbol-table rules, a CLAIM-STATE manifest guard (G24) and a functional G21; both injections now FAIL. The
  limits of these guards are stated in §1 (`NC-M67.52`).
- **Structure**: previous-version summaries, the v3.0 status map, old non-claims, superseded open items and
  pre-v3.2 corrections moved to `ZS-M67_v3_3_provenance_supplement.md`.
- **What v3.3 does not do**: it does not attempt Proof obligation 39.8 (a new theorem would end the
  correction-only status); does not close K7's condition, K8 or Cor. 38.7; does not run the K9b prior-art
  sweep; assigns no successor identifier.

**v3.2 (audit of v3.1 accepted in full, 0 findings rejected; scope corrections, one new computation; the K9b
quantitative conclusion retracted in v3.3 above).**
- **Theorem 39.4's quantifier is CORRECTED** (S3): the v3.1 statement "every colour/flavour off-diagonal
  condensate vanishes" and "the diagonal mean field is a theorem" are **withdrawn**. C96 establishes
  gauge-variance for colour-off-diagonal and charge-changing bilinears only (K9a, closed). Same-representation
  generation-flavour coherence (K9b) is gauge-invariant, is not excluded by Elitzur, and is **OPEN**; it was
  computed once (Prop. 39.6, C99; Cor. 39.7, V33): coherence can only raise the effective coefficient
  against the unchanged per-band bound, by `≤ 0.9 % (n_c/n_t)^{1/2}` for the SM, so K9b is rejected only conditionally on `n_partner ≤ n_top` — *v3.3: RETRACTED (S3): no coherent-carrier theorem carries Theorem 36's bound; K9b OPEN, see the v3.3 block above.* The
  survivor set {K7, K8} becomes {K7, K8, K9b}; "inside the corpus nothing survives" is withdrawn.
- **Corollary 41.2 is WEAKENED** (S2): "selecting the record value = discharging `D-S14-EVENT-001`" is
  withdrawn; this paper supplies that debt **one necessary condition** (`T/Δ ≤ 0.4147` for any thermal route).
  "The RQ3 residue coincides with an RQ2 residue" is downgraded to [가설] (Remark 41.4; Mission §4.2).
- **Theorem 38.3 is NARROWED** (S2, scope): its certified content is the `H²`-regularised spectral supertrace
  cancellation on `dom H`; the sentence asserting a trivial Fujikawa Jacobian for arbitrary local `α(x)` with
  fixed bag domain, and the absence of any `η`/inflow term, is withdrawn as stated. The constant case is
  Theorem 38.4; the local case is an [열림] proof obligation (Cor. 38.7). Cor. 38.5 is re-scoped accordingly.
- **Type lock**: the Bloch relaxation times of Theorem 41 are renamed `τ₁, τ₂`; `T₂` is the target only
  (guard G23). **Front matter re-synchronised**: OPEN-DEBTS, scope verdict, §22.10, §23, §24, §26, §27;
  artifact I's row count corrected from the erroneous "37" (§26–27 of v3.1) to 38.
- **Package**: artifact J (42 rows) supersedes I; the v3.1 ledger is shipped as the G18 baseline; G22 reports
  absent lineage siblings as NOT SHIPPED instead of failing; the manuscript path is resolved by glob;
  clean-room run 42/42, FAIL 0, DEGRADED 0, exit 0. **Finding beyond the audit**: the delivered v3.1 four-file
  package gives exit 1 (G18 DEGRADED + G22 FAIL), not the audit's exit 2; recorded in §26.
- **Lifecycle**: `FREEZE-CANDIDATE` is **WITHHELD** (a central closure at S3 blocks freeze); "no computation
  remains inside scope" (D34, v3.1) is withdrawn. Re-proposal only after a delta re-audit of v3.2.
- **History**: H-0280/H-0281 (approved) are not edited; superseding rows are proposed in the session file.
- **What v3.2 does not do**: it does not close K9b, K7's condition or K8; does not supply a rest-frame datum or
  the seam environment; does not prove domain preservation for local `α(x)`; does not run a prior-art sweep on
  K9b; assigns no successor identifier.

**v3.1 and earlier (v2.4–v3.1).** Kept verbatim in supplement §S29, with the v3.2/v3.3 annotations that mark which sentences were later withdrawn.

**Non-promotion contract (v3.3).** This manuscript changes no SSOT entry. The debt movements of §23 are
proposals pending user approval; the retractions of §29 are proposals for superseding history rows;
FREEZE-CANDIDATE is withheld, not proposed.
`RQ3` bridge state unchanged (`OPEN → OPEN`). Output role `SUPPORT`; not `CORE`. No numerical witness
is a theorem; no `NOT FOUND` is an absence theorem; no `PASS` count is a proof; all ledgers have
`P = 0`. The registry quantifies over its entries only. **Qualified-human anchor: NONE.**
