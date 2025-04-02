from fractions import Fraction
import numpy as np

# LU 분해 for tridiagonal matrix (in-place + L/U 분리 출력)
def LUdecomp3_full(c_in, d_in, e_in):
    n = len(d_in)

    # 원본 보존을 위해 복사
    c = c_in.copy()
    d = d_in.copy()
    e = e_in.copy()

    # LU 병합 저장용
    L = np.eye(n, dtype=object)
    U = np.zeros((n, n), dtype=object)

    for k in range(n):
        if k == 0:
            U[k][k] = d[k]
            U[k][k+1] = e[k]
        else:
            L[k][k-1] = c[k-1] / d[k-1]
            d[k] = d[k] - L[k][k-1] * e[k-1]
            U[k-1][k] = e[k-1]
            U[k][k] = d[k]
    
    return L, U

# 간단한 버전 (값만 변경)
def LUdecomp3(c, d, e):
    n = len(d)
    for k in range(1, n):
        lam = c[k-1] / d[k-1]
        d[k] = d[k] - lam * e[k-1]
        c[k-1] = lam
    return c, d, e

# LU 해법
def LUsolve3(c, d, e, b):
    n = len(d)
    for k in range(1, n):
        b[k] -= c[k-1] * b[k-1]
    b[n-1] = b[n-1] / d[n-1]
    for k in range(n-2, -1, -1):
        b[k] = (b[k] - e[k] * b[k+1]) / d[k]
    return b

# 입력 (분수로 표현)
c = [Fraction(-1), Fraction(-2), Fraction(3), Fraction(3)]  # sub-diagonal
d = [Fraction(6), Fraction(7), Fraction(8), Fraction(7), Fraction(5)]  # main
e = [Fraction(2), Fraction(2), Fraction(2), Fraction(-2)]  # super
b = [Fraction(2), Fraction(-3), Fraction(4), Fraction(-3), Fraction(1)]  # RHS

# L, U 행렬 분해
L, U = LUdecomp3_full(c.copy(), d.copy(), e.copy())

# LU 분해 (값 반영)
c, d, e = LUdecomp3(c, d, e)
x = LUsolve3(c, d, e, b.copy())

# 출력
print("=== L 행렬 ===")
for row in L:
    print([str(val) for val in row])

print("\n=== U 행렬 ===")
for row in U:
    print([str(val) for val in row])

print("\n=== 해 x (분수 기반) ===")
for i, xi in enumerate(x):
    print(f"x[{i}] = {xi}  (approx. {float(xi):.4f})")
