import numpy as np
from scipy import io
import os

# -------------------------------------------------------
# Step 1: Load data from .mat file
# -------------------------------------------------------
mat = io.loadmat("C:/Users/SAMSUNG/OneDrive/Desktop/대학/Solution 모음/25-1/수치해석/Project/prob4/prob4_codes/motor_efficiency_data.mat")
data_traction = mat['Data_traction']             # shape: (180, 3)
data_braking = mat['Data_regen_braking']         # shape: (170, 3)

# -------------------------------------------------------
# Step 2: Define basis function builder
# -------------------------------------------------------
def basis_functions(omega, torque):
    """
    Construct design matrix B using 7 basis functions:
    b1 = 1, b2 = w_m, b3 = w_m^2, b4 = w_m*T_m, b5 = T_m^2, b6 = w_m*T_m^2, b7 = w_m^2*T_m^2
    """
    return np.vstack([
        np.ones_like(omega),                  # b1
        omega,                                # b2
        omega**2,                             # b3
        omega * torque,                       # b4
        torque**2,                            # b5
        omega * torque**2,                    # b6
        omega**2 * torque**2                  # b7
    ]).T  # Shape: (N, 7)

# -------------------------------------------------------
# Step 3: Build regression matrices
# -------------------------------------------------------
def build_regression_matrix(data, mode='traction'):
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

# -------------------------------------------------------
# Step 4: Solve least-squares for both modes
# -------------------------------------------------------
B_plus, y_plus = build_regression_matrix(data_traction, mode='traction')
c_plus = np.linalg.lstsq(B_plus, y_plus, rcond=None)[0]

B_minus, y_minus = build_regression_matrix(data_braking, mode='braking')
c_minus = np.linalg.lstsq(B_minus, y_minus, rcond=None)[0]

# -------------------------------------------------------
# Step 5: Output the coefficients
# -------------------------------------------------------
print("Estimated coefficients for traction mode (c+):")
for i, val in enumerate(c_plus, start=1):
    print(f"c+_{i} = {val:.6f}")

print("\nEstimated coefficients for braking mode (c-):")
for i, val in enumerate(c_minus, start=1):
    print(f"c-_{i} = {val:.6f}")
