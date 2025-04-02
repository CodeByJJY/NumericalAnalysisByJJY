import numpy as np

# 주어진 행렬 A
A = np.array([
    [80, -50, -30,   0],
    [-50, 100, -10, -25],
    [-30, -10, 65, -20],
    [0, -25, -20, 100]
], dtype=float)

# 우변 벡터 b
b = np.array([120, 0, 0, 0], dtype=float)

def is_positive_definite(A):
    # Leading principal minors 양수인지 확인
    for k in range(1, A.shape[0] + 1):
        if np.linalg.det(A[:k, :k]) <= 0:
            return False
    return True

def cholesky_decomposition(A):
    n = A.shape[0]
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i+1):
            sum_val = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = (A[i][i] - sum_val) ** 0.5
            else:
                L[i][j] = (A[i][j] - sum_val) / L[j][j]
    return L

def doolittle_decomposition(A):
    n = A.shape[0]
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    for i in range(n):
        L[i][i] = 1
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(i))
        for j in range(i+1, n):
            L[j][i] = (A[j][i] - sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]
    return L, U

def forward_substitution(L, b):
    n = L.shape[0]
    y = np.zeros_like(b)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]
    return y

def backward_substitution(U, y):
    n = U.shape[0]
    x = np.zeros_like(y)
    for i in reversed(range(n)):
        x[i] = (y[i] - np.dot(U[i,i+1:], x[i+1:])) / U[i,i]
    return x

# 1. Positive definite 확인
if is_positive_definite(A):
    print("Positive definite -> Cholesky decomposition 사용")
    L = cholesky_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(L.T, y)
else:
    print("Not positive definite -> Doolittle decomposition 사용")
    L, U = doolittle_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)

# 결과 출력
for i, val in enumerate(x, 1):
    print(f"i{i} = {val:.6f}")
