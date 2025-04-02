import numpy as np
import math

# 각도 설정
theta_deg = 53
theta_rad = math.radians(theta_deg)

s = math.sin(theta_rad)
c = math.cos(theta_rad)

# 계수 행렬 A (5x5)
A = np.array([
    [ c,  1,   0,  0,  0],
    [ 0,  s,   0,  0,  1],
    [ 0,  0, 2*s,  0,  0],
    [ 0, -c,   c, 1,  0],
    [ 0,  s,   s, 0,  0]
], dtype=float)

# 우변 벡터 b
b = np.array([0, 0, 1, 0, 0], dtype=float)

# 선형 시스템 Ax = b 풀기
P = np.linalg.solve(A, b)

# 결과 출력
print("=== 문제 3.11: Truss 구조 해석 결과 ===")
for i, p in enumerate(P, start=1):
    print(f"P{i} = {p:.6f}")
