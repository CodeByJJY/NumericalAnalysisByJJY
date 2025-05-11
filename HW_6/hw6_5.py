import numpy as np
import matplotlib.pyplot as plt

# Points
x_vals = np.array([0.00, 0.25, 0.50, 0.75, 1.00])
y_vals = np.array([0.00, 0.03, 0.04, 0.03, 0.00])

# Vandermonde
A = np.vander(x_vals, 5)
b = y_vals.copy()

# Augmented matrix [A | b]
Ab = np.hstack((A, b.reshape(-1, 1)))
n = len(b)

# Gauss elimination
def gauss_elimination(Ab):
    # Forward Elimination
    for i in range(n):
        # Pivoting
        max_row = i + np.argmax(np.abs(Ab[i:, i]))
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        # Elimination Phase
        for j in range(i+1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    # Back Substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    return x

# Coefficients
coeffs = gauss_elimination(Ab)

# Result
print("Coefficients (a4 ~ a0):")
for i, a in enumerate(coeffs[::-1]):
    print(f"a{i} = {a:.6f}")


x_data = np.linspace(0, 1, 200)
y_data = np.polyval(coeffs, x_data)

plt.plot(x_data, y_data, label="Interpolated Curve")
plt.plot(x_vals, y_vals, 'ro', label="Data Points")
plt.axvline(0.6, linestyle='--', color='gray')
plt.title("Airfoil Surface Interpolation")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.grid(True)
plt.legend()
plt.show()
