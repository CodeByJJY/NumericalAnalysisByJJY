import numpy as np
import pandas as pd

# 구간 정의
segments = [
    (0.00, 0.25,  # Segment 0
     [8.0, 0.0, 3.5, 0.0],     # x(t) 계수 a,b,c,d
     [-64.0, 0.0, 12.0, 0.0]), # y(t) 계수 a,b,c,d

    (0.25, 0.50,  # Segment 1
     [-8.0, 6.0, 5.0, 1.0],
     [128.0, -48.0, 0.0, 2.0]),

    (0.50, 0.75,  # Segment 2
     [-8.0, 0.0, 6.5, 2.5],
     [-128.0, 48.0, 0.0, 1.0]),

    (0.75, 1.00,  # Segment 3
     [8.0, -6.0, 5.0, 4.0],
     [64.0, -48.0, 0.0, 2.0])
]

# 평가할 t 값
t_values = np.round(np.arange(0.0, 1.01, 0.1), 2)
x_results, y_results = [], []

# 각 t에 대해 해당 구간을 찾아 계산
for t in t_values:
    for (t_start, t_end, x_coeffs, y_coeffs) in segments:
        if t_start <= t <= t_end:
            tau = t - t_start
            a, b, c, d = x_coeffs
            e, f, g, h = y_coeffs
            x_t = a * tau**3 + b * tau**2 + c * tau + d
            y_t = e * tau**3 + f * tau**2 + g * tau + h
            x_results.append(round(x_t, 6))
            y_results.append(round(y_t, 6))
            break

# 결과 출력
df = pd.DataFrame({
    "t": t_values,
    "x(t)": x_results,
    "y(t)": y_results
})

print(df.to_string(index=False))
