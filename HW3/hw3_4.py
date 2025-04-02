import numpy as np
from fractions import Fraction
import math

##############################
# Fraction 기반 행렬 정의
##############################
A = np.array([
    [Fraction(4), Fraction(-1), Fraction(0)],
    [Fraction(-1), Fraction(4), Fraction(-1)],
    [Fraction(0), Fraction(-1), Fraction(4)]
])

##############################
# (a) Doolittle’s LU decomposition (Fraction)
##############################
def doolittle_fraction(A):
    n = A.shape[0]
    L = np.array([[Fraction(0) for _ in range(n)] for _ in range(n)])
    U = np.array([[Fraction(0) for _ in range(n)] for _ in range(n)])

    for i in range(n):
        L[i][i] = Fraction(1)
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(i))
        for j in range(i+1, n):
            L[j][i] = (A[j][i] - sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]

    return L, U

L_d, U_d = doolittle_fraction(A)
print("=== Doolittle LU Decomposition (Fraction) ===")
print("L =")
print(L_d)
print("U =")
print(U_d)
print("LU =")
print(np.dot(L_d, U_d))


##############################
# (b) Choleski decomposition (float version)
##############################
def choleski(A_float):
    A = A_float.copy()
    n = len(A)
    for k in range(n):
        try:
            A[k, k] = math.sqrt(A[k, k] - np.dot(A[k, :k], A[k, :k]))
        except ValueError:
            raise ValueError("Matrix is not positive definite")

        for i in range(k+1, n):
            A[i, k] = (A[i, k] - np.dot(A[i, :k], A[k, :k])) / A[k, k]

    for k in range(1, n):
        A[:k, k] = 0.0

    return A

def choleskiSol(L, b):
    n = len(b)
    # [L]{y} = {b}
    for k in range(n):
        b[k] = (b[k] - np.dot(L[k, :k], b[:k])) / L[k, k]
    # [L.T]{x} = {y}
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(L[k+1:n, k], b[k+1:n])) / L[k, k]
    return b

# A를 float로 변환 후 Cholesky 수행
A_float = np.array([[4.0, -1.0, 0.0],
                    [-1.0, 4.0, -1.0],
                    [0.0, -1.0, 4.0]])
L_c = choleski(A_float)
print("\n=== Choleski Decomposition (Float) ===")
print("L =")
print(L_c)
print("L @ L.T =")
print(np.dot(L_c, L_c.T))
