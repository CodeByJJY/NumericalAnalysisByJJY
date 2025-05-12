import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# --- Constants ---
L1, L2, L3 = 1.2, 1.5, 1.0
W1, W2 = 20000, 30000
B = 3.5
L3_sq = L3**2

# --- θ₁ search range ---
theta1_range_deg = np.linspace(1, 89, 500)
theta1_range_rad = np.radians(theta1_range_deg)

# --- Store θ₂ and V ---
theta2_results = []
V_results = []

# --- Main loop over θ₁ ---
for theta1 in theta1_range_rad:
    def constraint(theta2):
        term1 = B**2 - 2*B*(L1*np.cos(theta1) + L2*np.cos(theta2))
        term2 = L1**2 + L2**2 + 2*L1*L2*np.cos(theta1 - theta2)
        return term1 + term2 - L3_sq

    try:
        sol = root_scalar(constraint, bracket=[np.radians(1), np.radians(89)], method='brentq')
        if sol.converged:
            theta2 = sol.root
            V = -(W1 + W2) * L1 * np.sin(theta1) - W2 * L2 * np.sin(theta2)
            theta2_results.append(np.degrees(theta2))
            V_results.append(V)
        else:
            theta2_results.append(None)
            V_results.append(None)
    except:
        theta2_results.append(None)
        V_results.append(None)

# --- Find optimal index ---
valid_indices = [i for i, v in enumerate(V_results) if v is not None]
min_index = min(valid_indices, key=lambda i: V_results[i])
theta1_opt = theta1_range_rad[min_index]
theta2_opt = np.radians(theta2_results[min_index])
V_min = V_results[min_index]

# --- Compute theta3 ---
cos_theta3 = (B - L1 * np.cos(theta1_opt) - L2 * np.cos(theta2_opt)) / L3
sin_theta3 = (-L1 * np.sin(theta1_opt) - L2 * np.sin(theta2_opt)) / L3
theta3_rad = np.arctan2(sin_theta3, cos_theta3)
theta3_deg = np.degrees(theta3_rad)

# --- Print result ---
print(f"Optimal θ₁: {np.degrees(theta1_opt):.4f}°")
print(f"Optimal θ₂: {np.degrees(theta2_opt):.4f}°")
print(f"Optimal θ₃: {theta3_deg:.4f}°")
print(f"Minimum potential energy: {V_min:.2f} J")

# --- Plot V vs θ₁ ---
plt.figure(figsize=(10, 5))
plt.plot(theta1_range_deg, [v if v is not None else np.nan for v in V_results], label='Potential Energy V(θ₁)')
plt.scatter(np.degrees(theta1_opt), V_min, color='red', label='Minimum')
plt.xlabel("θ₁ (degrees)")
plt.ylabel("Potential Energy (J)")
plt.title("Potential Energy vs θ₁ (θ₂ from constraint)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
