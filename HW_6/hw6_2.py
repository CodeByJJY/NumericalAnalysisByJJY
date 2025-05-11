import numpy as np

# ������
x_vals = [1, 2, 3, 4, 5]
y_vals = [0, 1, 0, 1, 0]

# ������ ���� = 16 (4���� x 4���)
A = np.zeros((16, 16))
b = np.zeros(16)

# Eq 1~8: �� ������ �� ���������� y�� (�Լ��� ��ġ)
row = 0
for i in range(4):
    x0 = x_vals[i]
    x1 = x_vals[i+1]

    # Si(xi) = yi
    A[row, i*4:i*4+4] = [x0**3, x0**2, x0, 1]
    b[row] = y_vals[i]
    row += 1

    # Si(xi+1) = yi+1
    A[row, i*4:i*4+4] = [x1**3, x1**2, x1, 1]
    b[row] = y_vals[i+1]
    row += 1

# Eq 9~11: C1 ���Ӽ� (���Լ� ����)
for i in range(3):  # between S1-S2, S2-S3, S3-S4
    x = x_vals[i+1]
    A[row, i*4:i*4+4] = [3*x**2, 2*x, 1, 0]         # S_i'
    A[row, (i+1)*4:(i+1)*4+4] = [-3*x**2, -2*x, -1, 0]  # -S_{i+1}'
    b[row] = 0
    row += 1

# Eq 12~14: C2 ���Ӽ� (���� ���Լ� ����)
for i in range(3):
    x = x_vals[i+1]
    A[row, i*4:i*4+4] = [6*x, 2, 0, 0]              # S_i''
    A[row, (i+1)*4:(i+1)*4+4] = [-6*x, -2, 0, 0]     # -S_{i+1}''
    b[row] = 0
    row += 1

# Eq 15~16: Natural boundary condition
# S1''(x1) = 0
A[row, 0:4] = [6*x_vals[0], 2, 0, 0]
b[row] = 0
row += 1

# S4''(x5) = 0
A[row, 12:16] = [6*x_vals[-1], 2, 0, 0]
b[row] = 0

# ���콺 �ҰŹ����� �� Ǯ��
def gauss_elimination(A, b):
    n = len(b)
    M = np.hstack([A.astype(float), b.reshape(-1,1)])

    for k in range(n):
        # Pivoting
        max_row = np.argmax(abs(M[k:, k])) + k
        M[[k, max_row]] = M[[max_row, k]]

        # Elimination
        for i in range(k+1, n):
            factor = M[i, k] / M[k, k]
            M[i, k:] = M[i, k:] - factor * M[k, k:]

    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]

    return x

coeffs = gauss_elimination(A, b)

# ��� ��� (Ư�� a1~d1�� Ȯ��)
print("Coefficients a1~d1:")
print("a1 =", coeffs[0])
print("b1 =", coeffs[1])
print("c1 =", coeffs[2])
print("d1 =", coeffs[3])
