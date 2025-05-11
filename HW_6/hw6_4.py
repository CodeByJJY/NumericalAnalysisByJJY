import numpy as np
import matplotlib.pyplot as plt

def gaussian_elimination(A, b):
    A = A.copy().astype(float)
    b = b.copy().astype(float)
    n = len(b)

    # Forward elimination
    for i in range(n):
        # Pivoting
        max_row = np.argmax(np.abs(A[i:, i])) + i
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]

        # Eliminate below
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Back substitution
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x

# 행렬 A와 벡터 b 정의
A = np.array([
    [1, 1, 1],
    [4, 2, 1],
    [16, 4, 1]
], dtype=float)

b = np.array([2, 3, 1], dtype=float)

# 가우스 소거법으로 선형 시스템 Ax = b 풀기
x = gaussian_elimination(A, b)

a, b_, c = x
print(f"f(x) = {a:.3f}x^2 + {b_:.3f}x + {c:.3f}")

def f(x):
    return a * x**2 + b_ * x + c

x_vals = np.linspace(0, 5, 100)
y_vals = f(x_vals)

# 원래 주어진 점들
x_data = [1, 2, 4]
y_data = [2, 3, 1]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label='Interpolating Polynomial')
plt.plot(x_data, y_data, 'ro', label='Data Points')
plt.title('Quadratic Interpolation via Gaussian Elimination')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
