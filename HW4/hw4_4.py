import numpy as np
import matplotlib.pyplot as plt

# 가우스 소거 + 백워드 서브스티튜션
def gaussian_elimination(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)
    # Forward Elimination
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    # Backward Substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i, i]
    return x

# 데이터
x = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
y = np.array([6.008, 15.722, 27.130, 33.772, 5.257, 9.549, 11.098, 28.828])

# 1차 회귀: A = [1, x]
A1 = np.vstack((np.ones_like(x), x)).T
ATA1 = A1.T @ A1
ATy1 = A1.T @ y
x1 = gaussian_elimination(ATA1.copy(), ATy1.copy())
y_pred1 = A1 @ x1
rss1 = np.sum((y - y_pred1)**2)

# 2차 회귀: A = [1, x, x^2]
A2 = np.vstack((np.ones_like(x), x, x**2)).T
ATA2 = A2.T @ A2
ATy2 = A2.T @ y
x2 = gaussian_elimination(ATA2.copy(), ATy2.copy())
y_pred2 = A2 @ x2
rss2 = np.sum((y - y_pred2)**2)

# 결과 출력
print("1차 회귀식: y = {:.4f} + {:.4f}x".format(x1[0], x1[1]))
print("RSS = {:.4f}".format(rss1))

print("2차 회귀식: y = {:.4f} + {:.4f}x + {:.4f}x^2".format(x2[0], x2[1], x2[2]))
print("RSS = {:.4f}".format(rss2))

# 시각화
x_range = np.linspace(min(x), max(x), 200)
y_fit1 = x1[0] + x1[1] * x_range
y_fit2 = x2[0] + x2[1] * x_range + x2[2] * x_range**2

plt.scatter(x, y, label='Data Points', color='black')
plt.plot(x_range, y_fit1, label='Linear Fit', linestyle='--')
plt.plot(x_range, y_fit2, label='Quadratic Fit', linestyle='-')
plt.legend()
plt.title('Least Squares Fit via Gaussian Elimination')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
