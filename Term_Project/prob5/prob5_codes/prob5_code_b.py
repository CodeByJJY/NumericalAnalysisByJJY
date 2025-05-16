import numpy as np

# Lyapunov solver (manual)
def solve_lyapunov_manual(A, B, C):
    n, m = C.shape
    N = n * m
    M = np.zeros((N, N))
    b = C.reshape(N)

    for i in range(n):
        for j in range(m):
            row = i * m + j
            eq = np.zeros(N)

            for k in range(n):
                col = k * m + j
                eq[col] += A[i, k]

            for k in range(m):
                col = i * m + k
                eq[col] += B[k, j]

            M[row, :] = eq

    x = np.linalg.inv(M) @ b
    X = x.reshape(n, m)
    return X

# --------------------------------
# Step 1: Define system matrices
# --------------------------------
A = np.array([[0, 1],
              [-2, -3]])
B = np.array([[0],
              [1]])

# --------------------------------
# Step 2: Define desired closed-loop poles
# --------------------------------
# Desired poles: -2 and -5
# Characteristic equation: s^2 + 7s + 10
# Corresponding F matrix with desired poles
F = np.array([[0, 1],
              [-10, -7]])

# --------------------------------
# Step 3: Manually choose state feedback gain K
# --------------------------------
# A - B*K should match F
K = np.array([[12, 8]])

# --------------------------------
# Step 4: Build Lyapunov equation: A*T - T*F = B*K
# --------------------------------
C = B @ K
T = solve_lyapunov_manual(A, -F, C)

# --------------------------------
# Step 5: Print results
# --------------------------------
print("T matrix (solution of A*T - T*F = B*K):")
print(T)

print("\nA*T - T*F:")
print(A @ T - T @ F)

print("\nB*K:")
print(C)
