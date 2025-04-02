import numpy as np

n = 10

# ��� ��� A ����
A = np.zeros((n, n))

# �밢��
np.fill_diagonal(A, 4)

# �Ʒ�/�� �밢�� -1
for i in range(n - 1):
    A[i + 1, i] = -1
    A[i, i + 1] = -1

# �캯 ���� b ����
b = np.full(n, 5)
b[0] = 9  # ù ��° ���� �캯
b[-1] = 5  # ������ ���� �캯

# ���� �ý��� Ax = b Ǯ��
x = np.linalg.solve(A, b)

# ��� ���
for i, val in enumerate(x, 1):
    print(f"x{i} = {val:.6f}")
