import numpy as np
from fractions import Fraction

# 점들
points = [(0, 10), (1, 35), (3, 31), (4, 2)]

# A 행렬과 b 벡터 구성 (Fraction 사용)
A = []
b = []

for x, y in points:
    A.append([Fraction(1), Fraction(x), Fraction(x**2), Fraction(x**3)])
    b.append(Fraction(y))

A = np.array(A)
b = np.array(b)

# 연립방정식 Ax = b 풀기
coefficients = np.linalg.solve(A.astype(np.float64), b.astype(np.float64))

# 결과 출력 (Fraction 근사 출력)
print("=== Coefficients of the polynomial ===")
for i, coef in enumerate(coefficients):
    print(f"a_{i} = {coef:.5f}")

# 다항식 형태 출력
print("\nPolynomial:")
poly = " + ".join([f"{coef:.3f}*x^{i}" if i > 0 else f"{coef:.3f}" for i, coef in enumerate(coefficients)])
print(f"y = {poly}")
