import numpy as np

# 데이터 입력
M = np.array([1198, 1715, 2530, 2014, 2136, 1492, 1652, 1168, 1492, 1602, 1192, 2045], dtype=float)
phi = np.array([11.90, 6.80, 5.53, 6.38, 5.53, 8.50, 7.65, 13.60, 9.78, 8.93, 11.90, 6.38], dtype=float)

# A 행렬 구성: [1, M]
A = np.vstack((np.ones_like(M), M)).T

# A^T A, A^T b 계산
ATA = A.T @ A
ATb = A.T @ phi

# 가우스 소거법 + 역행렬로 해결 가능
def gaussian_elimination_solve(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)
    # Forward Elimination
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j,i] / A[i,i]
            A[j,i:] = A[j,i:] - factor * A[i,i:]
            b[j] = b[j] - factor * b[i]
    # Backward Substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]
    return x

# x = [a, b]
x = gaussian_elimination_solve(ATA.copy(), ATb.copy())
a, b = x

# 예측값 계산 및 표준 편차 계산
phi_pred = a + b * M
sigma = np.sqrt(np.mean((phi - phi_pred)**2))

print(f"회귀계수: a = {a:.4f}, b = {b:.6f}")
