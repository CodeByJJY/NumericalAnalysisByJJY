import numpy as np
from numpy import linalg as LA
import warnings

# RuntimeWarning 무시 설정
warnings.filterwarnings("ignore", category=RuntimeWarning)

# 1. 벡터 a 생성
a = np.arange(9) - 4
print("Vector a:", a)

# 2. 행렬 b 생성 (3x3)
b = a.reshape((3, 3))
print("Matrix b:\n", b)

# 3. 벡터/행렬 norm 계산
print("\n--- Norms of vector a ---")
print("LA.norm(a):", LA.norm(a))
print("LA.norm(a, np.inf):", LA.norm(a, np.inf))
print("LA.norm(a, -np.inf):", LA.norm(a, -np.inf))
print("LA.norm(a, 1):", LA.norm(a, 1))
print("LA.norm(a, -1):", LA.norm(a, -1))
print("LA.norm(a, 2):", LA.norm(a, 2))
print("LA.norm(a, -2):", LA.norm(a, -2))
print("LA.norm(a, 3):", LA.norm(a, 3))
print("LA.norm(a, -3):", LA.norm(a, -3))

print("\n--- Norms of matrix b ---")
print("LA.norm(b):", LA.norm(b))
print("LA.norm(b, 'fro'):", LA.norm(b, 'fro'))
print("LA.norm(b, np.inf):", LA.norm(b, np.inf))
print("LA.norm(b, -np.inf):", LA.norm(b, -np.inf))
print("LA.norm(b, 1):", LA.norm(b, 1))
print("LA.norm(b, -1):", LA.norm(b, -1))
print("LA.norm(b, 2):", LA.norm(b, 2))
print("LA.norm(b, -2):", LA.norm(b, -2))

# 4. axis 기반 벡터 norm
c = np.array([[1, 2, 3], [-1, 1, 4]])
print("\n--- Norms with axis (matrix c) ---")
print("c:\n", c)
print("LA.norm(c, axis=0):", LA.norm(c, axis=0))
print("LA.norm(c, axis=1):", LA.norm(c, axis=1))
print("LA.norm(c, ord=1, axis=1):", LA.norm(c, ord=1, axis=1))

# 5. 다차원 행렬 norm
m = np.arange(8).reshape(2, 2, 2)
print("\n--- Norms of 3D matrix m ---")
print("m:\n", m)
print("LA.norm(m, axis=(1,2)):", LA.norm(m, axis=(1, 2)))
print("LA.norm(m[0, :, :]):", LA.norm(m[0, :, :]))
print("LA.norm(m[1, :, :]):", LA.norm(m[1, :, :]))
