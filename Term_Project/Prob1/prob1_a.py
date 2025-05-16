import numpy as np
import matplotlib.pyplot as plt

# Common parameters
n = 30              # Total number of time steps
v0 = 0.5            # Initial velocity
vn = 2.3            # Target velocity

# ---------------------------------------------
# Case 1: Fastest Settling Time (Minimum Time)
# ---------------------------------------------
A1 = np.tril(np.ones((n, n)))                        # Lower triangular matrix of ones
b1 = np.full((n, 1), vn - v0)                         # Right-hand side vector: (vn - v0)
u1 = np.linalg.inv(A1.T @ A1) @ A1.T @ b1             # Least-squares solution for control input
v1 = [v0 + np.sum(u1[:i]) for i in range(n + 1)]      # Compute velocity at each step by integration

# -------------------------------------------------
# Case 2: Minimum Control Signal (Smooth Control)
# -------------------------------------------------
A2 = np.vstack((np.eye(n), np.ones((1, n))))          # Identity matrix + summation constraint
b2 = np.vstack((np.zeros((n, 1)), [[vn - v0]]))       # Zero vector + total velocity change constraint
u2 = np.linalg.inv(A2.T @ A2) @ A2.T @ b2
v2 = [v0 + np.sum(u2[:i]) for i in range(n + 1)]

# -----------------------------------------------------
# Case 3: Trade-off Between Speed and Control Effort
# -----------------------------------------------------
lambda_weight = 4                                     # Weight for control effort penalty
A3 = np.vstack((np.tril(np.ones((n, n))),             # Speed tracking part
                lambda_weight * np.eye(n)))           # Control effort penalty part
b3 = np.vstack((np.full((n, 1), vn - v0),              # Same as Case 1 for speed
                np.zeros((n, 1))))                     # Zero target for control input
u3 = np.linalg.inv(A3.T @ A3) @ A3.T @ b3
v3 = [v0 + np.sum(u3[:i]) for i in range(n + 1)]

# -------------------------
# Plotting results
# -------------------------
plt.figure(figsize=(12, 6))

# Velocity v(t)
plt.subplot(1, 2, 1)
plt.plot(v1, label="Case 1: Fastest")
plt.plot(v2, label="Case 2: Smoothest")
plt.plot(v3, label="Case 3: Trade-off")
plt.axhline(vn, color="gray", linestyle="--", label="Target Speed")
plt.title("Velocity v(t)")
plt.xlabel("Time Step")
plt.ylabel("Speed (m/s)")
plt.grid(True)
plt.legend()

# Control Input u(t)
plt.subplot(1, 2, 2)
plt.plot(u1, label="u(t) - Case 1")
plt.plot(u2, label="u(t) - Case 2")
plt.plot(u3, label="u(t) - Case 3")
plt.title("Control Input u(t)")
plt.xlabel("Time Step")
plt.ylabel("Acceleration")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
