import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import pandas as pd

# 1. Waypoints 정의
x = np.array([0.0, 1.0, 2.5, 4.0, 5.0])
y = np.array([0.0, 2.0, 1.0, 2.0, 0.0])
t = np.linspace(0, 1, len(x))  # [0.00, 0.25, 0.50, 0.75, 1.00]

# 2. CubicSpline 생성 (natural boundary 조건)
spline_x = CubicSpline(t, x, bc_type='natural')
spline_y = CubicSpline(t, y, bc_type='natural')

# 3. 각 구간에 대해 계수 추출 및 방정식 구성
coeffs_x = spline_x.c.T  # (4, 4): a, b, c, d for each segment
coeffs_y = spline_y.c.T
t_segments = list(zip(t[:-1], t[1:]))

equations = []
for i, (t0, t1) in enumerate(t_segments):
    a_x, b_x, c_x, d_x = coeffs_x[i]
    a_y, b_y, c_y, d_y = coeffs_y[i]

    x_expr = f"{a_x:.6f}*(t - {t0:.2f})**3 + {b_x:.6f}*(t - {t0:.2f})**2 + {c_x:.6f}*(t - {t0:.2f}) + {d_x:.6f}"
    y_expr = f"{a_y:.6f}*(t - {t0:.2f})**3 + {b_y:.6f}*(t - {t0:.2f})**2 + {c_y:.6f}*(t - {t0:.2f}) + {d_y:.6f}"

    equations.append({
        "segment": f"[{t0:.2f}, {t1:.2f})",
        "x_expr": x_expr,
        "y_expr": y_expr
    })

# 4. 한 줄씩 출력 (방법 2)
for eq in equations:
    print(f"Segment {eq['segment']}")
    print(f"x_i(t) = {eq['x_expr']}")
    print(f"y_i(t) = {eq['y_expr']}")
    print("-" * 70)

# 5. 시각화
t_dense = np.linspace(0, 1, 300)
x_vals = spline_x(t_dense)
y_vals = spline_y(t_dense)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label="Spline path (x(t), y(t))")
plt.plot(x, y, 'ro', label="Waypoints")
plt.title("Cubic Spline Trajectory via x(t), y(t)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.tight_layout()
plt.show()
