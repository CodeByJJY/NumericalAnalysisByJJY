import numpy as np

# 보간점
x_vals = [1, 2, 3, 4, 5]
y_vals = [0, 1, 0, 1, 0]

# 방정식 개수 = 16 (4구간 x 4계수)
A = np.zeros((16, 16))
b = np.zeros(16)

# Eq 1~8: 각 구간의 양 끝점에서의 y값 (함수값 일치)
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

# Eq 9~11: C1 연속성 (도함수 연속)
for i in range(3):  # between S1-S2, S2-S3, S3-S4
    x = x_vals[i+1]
    A[row, i*4:i*4+4] = [3*x**2, 2*x, 1, 0]         # S_i'
    A[row, (i+1)*4:(i+1)*4+4] = [-3*x**2, -2*x, -1, 0]  # -S_{i+1}'
    b[row] = 0
    row += 1

# Eq 12~14: C2 연속성 (이차 도함수 연속)
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

# 가우스 소거법으로 해 풀기
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

# 결과 출력 (특히 a1~d1만 확인)
print("Coefficients a1~d1:")
print("a1 =", coeffs[0])
print("b1 =", coeffs[1])
print("c1 =", coeffs[2])
print("d1 =", coeffs[3])
