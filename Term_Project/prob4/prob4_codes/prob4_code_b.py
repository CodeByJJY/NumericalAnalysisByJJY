import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

# Step 1: Load data
mat = loadmat("C:/Users/SAMSUNG/OneDrive/Desktop/대학/Solution 모음/25-1/수치해석/Project/prob4/prob4_codes/motor_efficiency_data.mat")
data_traction = mat["Data_traction"]
data_braking = mat["Data_regen_braking"]

# Step 2: Define basis functions
def basis_functions(omega, torque):
    return np.vstack([
        np.ones_like(omega),
        omega,
        omega**2,
        omega * torque,
        torque**2,
        omega * torque**2,
        omega**2 * torque**2
    ]).T

# Step 3: Construct design matrix and target vector
def build_matrix(data, mode):
    eta = data[:, 0]
    omega = data[:, 1]
    torque = data[:, 2]
    B = basis_functions(omega, torque)

    if mode == 'traction':
        y = (torque * omega) / eta
    elif mode == 'braking':
        y = torque * omega * eta
    else:
        raise ValueError("mode must be 'traction' or 'braking'")

    return B, y

# Step 4: Ridge regression solver
def ridge_regression(B, y, lam):
    n = B.shape[1]
    A = B.T @ B + lam * np.eye(n)
    return np.linalg.solve(A, B.T @ y)

# Step 5: Run for multiple lambda values
lambdas = [0, 0.01, 0.1, 1, 10, 100, 1000]
norms_traction, norms_braking = [], []

B_traction, y_traction = build_matrix(data_traction, "traction")
B_braking, y_braking = build_matrix(data_braking, "braking")

print("Lambda     ||c||^2 (Traction)     ||c||^2 (Braking)")
print("----------------------------------------------------")
for lam in lambdas:
    c_trac = ridge_regression(B_traction, y_traction, lam)
    c_brake = ridge_regression(B_braking, y_braking, lam)
    norm_trac = np.linalg.norm(c_trac)**2
    norm_brake = np.linalg.norm(c_brake)**2
    norms_traction.append(norm_trac)
    norms_braking.append(norm_brake)
    print(f"{lam:<10} {norm_trac:<24.6f} {norm_brake:<.6f}")

# Step 6: Plot results
plt.figure(figsize=(10, 5))
plt.semilogx(lambdas, norms_traction, 'o-', label="||c||^2 (Traction)")
plt.semilogx(lambdas, norms_braking, 's-', label="||c||^2 (Braking)")
plt.xlabel("Lambda (Regularization Strength, log scale)")
plt.ylabel("Squared norm of coefficients ||c||^2")
plt.title("Ridge Regression: Coefficient Norm vs Lambda")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
