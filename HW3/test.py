import numpy as np

n = 10

# 계수 행렬 A 생성
A = np.zeros((n, n))

# 대각선
np.fill_diagonal(A, 4)

# 아래/위 대각선 -1
for i in range(n - 1):
    A[i + 1, i] = -1
    A[i, i + 1] = -1

# 우변 벡터 b 생성
b = np.full(n, 5)
b[0] = 9  # 첫 번째 식의 우변
b[-1] = 5  # 마지막 식의 우변

# 선형 시스템 Ax = b 풀기
x = np.linalg.solve(A, b)

# 결과 출력
for i, val in enumerate(x, 1):
    print(f"x{i} = {val:.6f}")
