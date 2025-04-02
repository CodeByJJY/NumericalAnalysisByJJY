import numpy as np

# 주어진 ill-conditioned matrix
A = np.array([
    [1, 4, 9, 16],
    [4, 9, 16, 25],
    [9, 16, 25, 36],
    [16, 25, 36, 49]
], dtype=float)

# (1) Condition number 함수 직접 구현
def condition_number(A):
    A_norm = np.linalg.norm(A, 2)
    A_inv = np.linalg.inv(A)
    A_inv_norm = np.linalg.norm(A_inv, 2)
    cond = A_norm * A_inv_norm
    return A_norm, A_inv, A_inv_norm, cond

# (2) 함수 호출
A_norm, A_inv, A_inv_norm, cond_custom = condition_number(A)
cond_numpy = np.linalg.cond(A, 2)

# (3) 출력
print("=== Condition Number Analysis ===")
print("Matrix A:")
print(A)

print("\n2-Norm of A:")
print(f"{A_norm:.5e}")

print("\nInverse of A:")
print(A_inv)

print("\n2-Norm of A-inverse:")
print(f"{A_inv_norm:.5e}")

print("\nCondition Number (Custom):")
print(f"{cond_custom:.5e}")

print("\nCondition Number (NumPy built-in):")
print(f"cond(A) = {cond_numpy:.5e}")
