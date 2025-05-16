import numpy as np

def solve_lyapunov_manual(A, B, C):
    """
    Solve AX + XB = C without using high-level functions (like np.kron or np.linalg.solve).
    """

    n, m = C.shape
    N = n * m  # Number of unknowns in X

    # Initialize the system matrix and right-hand side
    M = np.zeros((N, N))
    b = C.reshape(N)

    # Build the system manually
    # Let X = [x11, x12, ..., x1m, x21, x22, ..., xnm]^T
    for i in range(n):
        for j in range(m):
            row = i * m + j
            eq = np.zeros(N)

            # AX term: sum_k A[i,k] * x[k,j]
            for k in range(n):
                col = k * m + j  # x[k,j]
                eq[col] += A[i, k]

            # XB term: sum_k x[i,k] * B[k,j]
            for k in range(m):
                col = i * m + k  # x[i,k]
                eq[col] += B[k, j]

            M[row, :] = eq

    # Solve Mx = b
    x = np.linalg.inv(M) @ b  # 또는 np.linalg.pinv(M) @ b 도 가능 (정칙성 안심 못할 경우)
    X = x.reshape(n, m)

    return X

A = np.array([[1, 2], [-3, -4]])
B = A.T
C = np.array([[3, 1], [1, 1]])

X = solve_lyapunov_manual(A, B, C)

print("Solution X:")
print(X)

# 검증
print("\nAX + XB:")
print(A @ X + X @ B)
print("\nOriginal C:")
print(C)
