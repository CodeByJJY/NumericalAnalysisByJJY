import numpy as np

# -----------------------------
# Step 1: 데이터 함수 정의
# -----------------------------
def advertising_budget_data():
    """
    Return R matrix (reach rate) and v_des vector (target views).
    R is shape (m, n), v_des is length m.
    """
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
# Step 2: 제약 최소제곱 해법
# -----------------------------
def solve_least_squares_with_constraint(R, v_des, b):
    """
    Solve min ||Rs - v_des||^2 subject to 1^T s = b
    using KKT system.
    """
    m, n = R.shape
    RtR = 2 * R.T @ R
    Rtv = 2 * R.T @ v_des
    ones = np.ones((n, 1))

    # KKT 시스템 구성
    KKT_matrix = np.block([
        [RtR,    ones],
        [ones.T, np.zeros((1, 1))]
    ])
    rhs = np.concatenate([Rtv, [b]])

    # 선형 시스템 풀기
    sol = np.linalg.solve(KKT_matrix, rhs)
    s_opt = sol[:n]
    return s_opt

# -----------------------------
# Step 3: 실행
# -----------------------------
R, v_des = advertising_budget_data()
b = 1300

s = solve_least_squares_with_constraint(R, v_des, b)

# 결과 출력
print("Optimal s:", s)
print("1^T s =", np.sum(s))

# RMS 오차 계산
m = R.shape[0]
rms = np.linalg.norm(R @ s - v_des) / np.sqrt(m)
print("RMS Error:", rms)
