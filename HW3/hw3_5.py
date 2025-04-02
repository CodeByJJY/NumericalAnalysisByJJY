import numpy as np
from fractions import Fraction

# ����
points = [(0, 10), (1, 35), (3, 31), (4, 2)]

# A ��İ� b ���� ���� (Fraction ���)
A = []
b = []

for x, y in points:
    A.append([Fraction(1), Fraction(x), Fraction(x**2), Fraction(x**3)])
    b.append(Fraction(y))

A = np.array(A)
b = np.array(b)

# ���������� Ax = b Ǯ��
coefficients = np.linalg.solve(A.astype(np.float64), b.astype(np.float64))

# ��� ��� (Fraction �ٻ� ���)
print("=== Coefficients of the polynomial ===")
for i, coef in enumerate(coefficients):
    print(f"a_{i} = {coef:.5f}")

# ���׽� ���� ���
print("\nPolynomial:")
poly = " + ".join([f"{coef:.3f}*x^{i}" if i > 0 else f"{coef:.3f}" for i, coef in enumerate(coefficients)])
print(f"y = {poly}")
