import numpy as np
import matplotlib.pyplot as plt

# 가우스 소거법 함수
def gaussian_elimination(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j,i] / A[i,i]
            A[j,i:] -= factor * A[i,i:]
            b[j] -= factor * b[i]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - A[i,i+1:] @ x[i+1:]) / A[i,i]
    return x

# 데이터
x_vals = np.array([-0.5, -0.19, 0.02, 0.20, 0.35, 0.50])
y_vals = np.array([-3.558, -2.874, -1.995, -1.040, -0.068, 0.677])

# 디자인 행렬 A = [sin(πx/2), cos(πx/2)]
A = np.column_stack((
    np.sin(np.pi * x_vals / 2),
    np.cos(np.pi * x_vals / 2)
))

# 정규 방정식
ATA = A.T @ A
ATy = A.T @ y_vals

# 계수 추정
params = gaussian_elimination(ATA.copy(), ATy.copy())
a, b = params

# 예측값
y_pred = A @ params
rss = np.sum((y_vals - y_pred)**2)

print(f"회귀식: f(x) = {a:.4f} * sin(πx/2) + {b:.4f} * cos(πx/2)")
print(f"RSS = {rss:.6f}")

# 시각화용 x축 범위 및 예측 함수 정의
x_plot = np.linspace(-0.6, 0.6, 300)
y_plot = a * np.sin(np.pi * x_plot / 2) + b * np.cos(np.pi * x_plot / 2)

# 플로팅
plt.figure(figsize=(8, 5))
plt.scatter(x_vals, y_vals, color='red', label='Data points')
plt.plot(x_plot, y_plot, label=r'$f(x) = a \sin(\frac{\pi x}{2}) + b \cos(\frac{\pi x}{2})$', color='blue')
plt.title("Least Squares Fit of f(x) = a*sin(pi*x/2) + b*cos(pi*x/2)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
