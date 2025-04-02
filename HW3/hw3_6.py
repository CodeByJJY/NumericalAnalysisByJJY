import numpy as np

def gauss_elimination_complex(A, b):
    A = A.astype(complex)  # ensure complex type
    b = b.astype(complex)
    n = len(b)

    # Forward elimination
    for k in range(n):
        # Pivoting (partial, complex-compatible)
        max_row = np.argmax(np.abs(A[k:, k])) + k
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]

        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    # Back substitution
    x = np.zeros(n, dtype=complex)
    for i in reversed(range(n)):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    
    return x

# Define A and b
A = np.array([
    [5+1j, 5+2j, -5+3j, 6-3j],
    [5+2j, 7-2j, 8-1j, -1+3j],
    [-5+3j, 8-1j, -3-3j, 2+2j],
    [6-3j, -1+3j, 2+2j, 8+14j]
], dtype=complex)

b = np.array([15 - 35j, 2 + 10j, -2 - 34j, 8 + 14j], dtype=complex)

# Solve the system
x = gauss_elimination_complex(A, b)

# Ãâ·Â
for i, val in enumerate(x, 1):
    print(f"x{i} = {val:.6f}")
