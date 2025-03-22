import numpy as np

A = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])

print("Rank of A:", np.linalg.matrix_rank(A))
print("Trace of A:", np.trace(A))
print("Determinant of A:", np.linalg.det(A))
print("Inverse of A:\n", np.linalg.inv(A))
print("Matrix A raised to power 3:\n", np.linalg.matrix_power(A, 3))
