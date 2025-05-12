import numpy as np
import matplotlib.pyplot as plt

# 목적 함수: f(R) = -P(R)
def f(R):
    if R <= 0:
        return 1e6  # 정의역 밖
    num = 120 * R
    denom = (3.5 + R) * (6.6 + R) - R**2
    i2 = num / denom
    return - (43.56 / R) * i2**2

# 수치 미분을 이용한 gradient 계산
def grad_f(R, h=1e-5):
    return (f(R + h) - f(R - h)) / (2 * h)

# Line search descent method
def gradient_descent(initial_R, alpha=0.01, tol=1e-6, max_iter=1000):
    R = initial_R
    history = [R]
    for i in range(max_iter):
        g = grad_f(R)
        if abs(g) < tol:
            break
        R = R - alpha * g
        history.append(R)
    return R, -f(R), history  # 최소화한 -f는 실제 최대값

# 실행
optimal_R, max_power, trajectory = gradient_descent(initial_R=1.0)
print(f"Best R: {optimal_R:.4f} (Ohm)")
print(f"Max Power: {max_power:.2f} W")

# 경로 시각화
R_vals = np.linspace(0.01, 10, 500)
P_vals = [-(f(R)) for R in R_vals]

plt.plot(R_vals, P_vals, label="Power dissipated")
plt.plot(trajectory, [-(f(R)) for R in trajectory], 'ro-', label="GD path")
plt.xlabel("R (Ohms)")
plt.ylabel("Power (W)")
plt.grid(True)
plt.title("Gradient Descent Optimization of R")
plt.legend()
plt.tight_layout()
plt.show()
