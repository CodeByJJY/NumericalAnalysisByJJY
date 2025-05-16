import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: 데이터 함수 정의
# -----------------------------
def advertising_budget_data():
    R = np.array([
        [0.97, 1.86, 0.41],
        [1.23, 2.18, 0.53],
        [0.80, 1.24, 0.62],
        [1.29, 0.98, 0.51],
        [1.10, 1.23, 0.69],
        [0.67, 0.34, 0.54],
        [0.87, 0.26, 0.62],
        [1.10, 0.16, 0.48],
        [1.92, 0.22, 0.71],
        [1.29, 0.12, 0.62]
    ])
    m, n = R.shape
    v_des = 1e3 * np.ones(m)
    return R, v_des

# -----------------------------
# Step 2: 제약 최소제곱 함수
# -----------------------------
def solve_least_squares_with_constraint(R, v_des, b):
    m, n = R.shape
    RtR = 2 * R.T @ R
    Rtv = 2 * R.T @ v_des
    ones = np.ones((n, 1))

    KKT_matrix = np.block([
        [RtR,    ones],
        [ones.T, np.zeros((1, 1))]
    ])
    rhs = np.concatenate([Rtv, [b]])

    sol = np.linalg.solve(KKT_matrix, rhs)
    s_opt = sol[:n]
    return s_opt

# -----------------------------
# Step 3: 실험 - 다양한 b에 대해 RMS 계산
# -----------------------------
R, v_des = advertising_budget_data()
m = R.shape[0]
budgets = np.arange(1200, 1701, 100)
rms_list = []

for b in budgets:
    s = solve_least_squares_with_constraint(R, v_des, b)
    rms = np.linalg.norm(R @ s - v_des) / np.sqrt(m)
    rms_list.append(rms)
    print(f"b = {b}, RMS = {rms:.4f}")

# -----------------------------
# Step 4: 그래프 출력
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(budgets, rms_list, 'o-', linewidth=2)
plt.xlabel("Total Budget b")
plt.ylabel("RMS Error")
plt.title("RMS Error vs. Total Budget")
plt.grid(True)
plt.tight_layout()
plt.show()
