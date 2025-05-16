========================================
na2025_12191529_장준영
Student: 장준영
ID: 12191529
Date: 2025/05/16
File: readme.txt
========================================

■ Description
"na2025_12191529_장준영"에는 수치해석의 핵심 주제를 다루는 6가지 문제가 포함되어 있습니다.

- Problem 1: Optimal control with time discretization
- Problem 2: Linearized kinematic motion prediction
- Problem 3: Autoregressive (AR) time series modeling
- Problem 4: Electric motor and engine efficiency modeling
- Problem 5: Solving Lyapunov equations numerically
- Problem 6: Budget optimization with least squares under constraint

모든 문제는 Python(버전 ≥ 3.7)으로 구현되었으며, 일부 문제에는 matplotlib를 사용한 visualization 구현 코드가 포함되어 있습니다.



■ File List
1. Prob1
- prob1_a.py: 최소 시간 및 최소 제어 입력을 고려한 속도 제어 문제 구현 with Python.
- prob1_report.docx: 문제 1에 대한 해석 및 그래프 분석을 담은 word 문서 소스.
- prob1_report.pdf: 최종 제출용 문제 1 레포트 (PDF 변환본).

2. Prob2
- prob2_code_a.py: 선형화된 이동 모델 기반의 예측 시스템 구성 (Lyapunov 기반 시간 진화)
- prob2_code_c.py: 다양한 lambda 값에 따른 control trade-off 실험 및 시각화
- prob2_report.docx: 문제 2의 코드 설명 및 실험 결과 초안 문서
- prob2_report.pdf: 최종 제출용 문제 2 레포트

3. Prob3
- prob3_code_a.py: AR(8) 모델을 이용한 온도 예측 및 RMS 오차 계산
- prob3_code_c.py: AR 모델 차수(M=4,8,12,24)에 따른 성능 비교 및 시각화
- prob3_report.docx: 문제 3에 대한 모델 설명, 실험 방법 및 결과 분석 초안
- prob3_report.pdf: 최종 제출용 문제 3 레포트

4. Prob4
- prob4_code_a.py: 모터 및 회생제동 효율을 선형 회귀로 모델링 (기본 least squares)
- prob4_code_b.py: 정규화된 최소제곱 해법 적용 (ridge regression) 및 계수 norm 분석
- prob4_code_c.py: 커널 기반 회귀 (non-parametric regression) 적용 및 RMS 성능 비교
- motor_efficiency_data.mat: 모터 동작 효율 데이터 (MATLAB 형식)
- engine_efficiency_data.mat: 엔진 동작 효율 데이터 (MATLAB 형식)
- prob4_report.docx: 문제 4 전체 실험 내용 및 해석 초안
- prob4_report.pdf: 최종 제출용 문제 4 레포트

5. Prob5
- prob5_code_a.py: 고수준 함수 없이 Lyapunov 방정식을 직접 풀기 위한 수동 해법 구현
- prob5_code_b.py: 상태 피드백 제어기 설계 예제에 Lyapunov 해법을 적용하여 AT−TF=BK 형태 해석
- prob5_report.docx: 문제 5 전체 실습 내용, 코드 설명 및 수치 검증 초안
- prob5_report.pdf: 최종 제출용 문제 5 레포트

6. Prob6
- prob6_code_b.py: 총 광고 예산 제약 하에서 최소제곱 기반으로 최적 광고비 분배 계산 (KKT 해법)
- prob6_code_c.py: 예산 변화에 따른 RMS 오차 계산 및 성능 시각화 (budget sweep 실험)
- prob6_report.docx: 문제 6의 해석 및 실험 결과에 대한 초안 정리 문서
- prob6_report.pdf: 최종 제출용 문제 6 레포트

■ Execution Instructions
1. `numpy`와 `matplotlib`가 설치된 Python 환경에서 각 `.py` 파일을 실행해야 합니다.
2. 문제 4의 경우, 'prob4_code_a.py', 'prob4_code_b.py', 'prob4_code_c.py' 내부의 mat 경로에 '.mat' 파일(`motor_efficiency_data.mat`, `engine_efficiency_data.mat`)의 절대경로(mat = loadmat("절대경로 입력"))를 입력해야 합니다.
3. 문제 3, 6은 추가 데이터가 필요하지 않습니다. 모든 데이터는 코드에 이미 입력되어 있습니다.
4. 모든 플롯은 새 창에 표시됩니다. 필요한 경우 저장하세요.
5. 모든 코드 파일은 "utf-8" 환경에서 실행해야 합니다.


■ Notes
- 특별한 언급이 없는 한 모든 코드는 처음부터 작성되었습니다.
- 보고서 PDF에는 상징적 파생어(예: KKT, Lyapunov)가 포함되었습니다.
- 재현성을 위해 난수 시드는 사용되지 않았습니다(결정론적 문제에는 필요하지 않음).
- 이 코드는 high-level black-box solvers(ex. 고급 라이브러리 메서드)를 피하고 대신 수업에서 공부한 알고리즘 구현을 따릅니다.

Thank you!
