import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1. Given data points (x_i, y_i)
x_data = np.array([0.15, 2.30, 3.15, 4.85, 6.25, 7.95])
y_data = np.array([4.79867, 4.49013, 4.22430, 3.47313, 2.66674, 1.51909])

# 2. Compute divided difference coefficients for Newton interpolation
def divided_differences(x, y):
    n = len(x)
    coef = y.copy().astype(float)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j - 1]) / (x[j:n] - x[j - 1])
    return coef

a = divided_differences(x_data, y_data)

# 3. Generate human-readable Newton interpolation polynomial expression
def interpolation_formula(a, x_data):
    terms = [f"{a[0]:.6f}"]
    for i in range(1, len(a)):
        factors = '*'.join([f"(x - {x_data[j]:.2f})" for j in range(i)])
        terms.append(f"{a[i]:+f}*{factors}")
    return "P(x) = " + ' '.join(terms)

interp_eq = interpolation_formula(a, x_data)
print("Newton Interpolation Formula:")
print(interp_eq)

# 4. Evaluate Newton polynomial at a given x using Horner's method
def newton_eval(a, x_data, x):
    n = len(a)
    result = a[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x - x_data[i]) + a[i]
    return result

# 5. Evaluate at x = 0, 0.5, ..., 8.0 and compare with actual function
x_eval = np.arange(0.0, 8.01, 0.5)
y_eval = [newton_eval(a, x_data, x) for x in x_eval]
real_eval = [4.8 * np.cos(np.pi * x / 20) for x in x_eval]
error_eval = np.array(real_eval) - np.array(y_eval)

# 6. Create table comparing interpolated and actual values
result_df = pd.DataFrame({
    "x": x_eval,
    "P(x)": np.round(y_eval, 6),
    "f(x)": np.round(real_eval, 6),
    "Err": np.round(error_eval, 6)
})
print("\nInterpolated Values at x = 0, 0.5, ..., 8.0:")
print(result_df.to_string(index=False))

# 7. Plot interpolated curve, original data points, and evaluated points
x_dense = np.linspace(0, 8.0, 400)
y_dense = [newton_eval(a, x_data, x) for x in x_dense]

plt.figure(figsize=(10, 6))
plt.plot(x_dense, y_dense, label="Interpolated Curve (P(x))", color='orange')
plt.plot(x_data, y_data, 'ro', label="Original Data Points")
plt.scatter(x_eval, y_eval, color='blue', label="Evaluated Points (step size=0.5)")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("5th-order Newton Polynomial Interpolation Graph")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
