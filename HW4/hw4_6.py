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
t = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5])
gamma = np.array([1.000, 0.994, 0.990, 0.985, 0.979, 0.977,
                  0.972, 0.969, 0.967, 0.960, 0.956, 0.952])

# ln(γ) = ln a - bt 형태로 변환
Y = np.log(gamma)
A = np.vstack((np.ones_like(t), -t)).T  # Y = c - bt

# 정규방정식
ATA = A.T @ A
ATY = A.T @ Y

# 계수 추정
params = gaussian_elimination(ATA.copy(), ATY.copy())
c, b = params
a = np.exp(c)
half_life = np.log(2) / b

# 출력
print(f"계수: a = {a:.6f}, b = {b:.6f}")
print(f"Radioactive Half-life ≈ {half_life:.4f} years")

# 예측값 및 시각화
t_plot = np.linspace(0, 6, 200)
gamma_fit = a * np.exp(-b * t_plot)

plt.figure(figsize=(8, 5))
plt.plot(t_plot, gamma_fit, label='Fitted Decay Curve', color='blue')
plt.scatter(t, gamma, color='red', label='Measured Data')
plt.title("Exponential Fit of Radioactive Decay")
plt.xlabel("Time t (years)")
plt.ylabel("Gamma(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
