import numpy as np

def solve_using_numpy_cholesky(R):
    A = np.array([
        [50 + R, -R, -30],
        [-R, 65 + R, -15],
        [0, -45, 45]
    ], dtype=float)

    b = np.array([0, 0, 120], dtype=float)

    # Cholesky 분해
    L = np.linalg.cholesky(A)

    # Forward & Backward Substitution
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(L.T, y)

    return x

# 테스트
for R in [5, 10, 20]:
    x = solve_using_numpy_cholesky(R)
    print(f"R = {R} Ohm -> i1 = {x[0]:.4f} A, i2 = {x[1]:.4f} A, i3 = {x[2]:.4f} A")
