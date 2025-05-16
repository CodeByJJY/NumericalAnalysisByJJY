import numpy as np
from scipy.io import loadmat
from tqdm import tqdm  # optional: for progress bar
import matplotlib.pyplot as plt

# Step 1: Load data
mat = loadmat("C:/Users/SAMSUNG/OneDrive/Desktop/대학/Solution 모음/25-1/수치해석/Project/prob4/prob4_codes/motor_efficiency_data.mat")
data_traction = mat["Data_traction"]
data_braking = mat["Data_regen_braking"]

# Step 2: Extract (x, y) pairs
def extract_xy(data, mode):
    eta = data[:, 0]
    omega = data[:, 1]
    torque = data[:, 2]
    X = np.stack((omega, torque), axis=1)

    if mode == 'traction':
        y = (torque * omega) / eta
    elif mode == 'braking':
        y = torque * omega * eta
    else:
        raise ValueError("Mode must be 'traction' or 'braking'")
    return X, y

# Step 3: Gaussian Kernel
def gaussian_kernel(x, x_i, h):
    diff = x - x_i
    return np.exp(-np.dot(diff, diff) / (2 * h**2))

# Step 4: Kernel regression prediction with leave-one-out
def kernel_regression_LOO(X, y, h):
    N = len(y)
    y_pred = np.zeros(N)

    for i in range(N):
        x_i = X[i]
        numer = 0.0
        denom = 0.0
        for j in range(N):
            if i == j:
                continue  # leave-one-out
            w = gaussian_kernel(x_i, X[j], h)
            numer += w * y[j]
            denom += w
        y_pred[i] = numer / denom if denom > 0 else 0.0
    return y_pred

# Step 5: Test over multiple bandwidths
bandwidths = [0.1, 0.5, 1, 2, 5]
rms_traction = []
rms_braking = []

X_trac, y_trac = extract_xy(data_traction, 'traction')
X_brake, y_brake = extract_xy(data_braking, 'braking')

print("Bandwidth   RMS Error (Traction)   RMS Error (Braking)")
print("-------------------------------------------------------")

for h in bandwidths:
    y_trac_pred = kernel_regression_LOO(X_trac, y_trac, h)
    y_brake_pred = kernel_regression_LOO(X_brake, y_brake, h)

    rms_t = np.sqrt(np.mean((y_trac_pred - y_trac) ** 2))
    rms_b = np.sqrt(np.mean((y_brake_pred - y_brake) ** 2))

    rms_traction.append(rms_t)
    rms_braking.append(rms_b)

    print(f"{h:<11} {rms_t:<22.4f} {rms_b:<.4f}")

# Step 6: Plot RMS error vs bandwidth
plt.figure(figsize=(10, 5))
plt.plot(bandwidths, rms_traction, 'o-', label="Traction")
plt.plot(bandwidths, rms_braking, 's-', label="Braking")
plt.xlabel("Bandwidth h")
plt.ylabel("RMS Error")
plt.title("Kernel Regression: RMS Error vs Bandwidth")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
