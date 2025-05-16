import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 10
dt = 1.0
l = 2.0

# Nominal state and input
x_bar = np.array([[0], [-2], [0]])      # Initial state
u_bar = np.array([[10], [0]])           # Nominal input
x_goal = np.array([[100], [2], [0]])    # Target state
x_goal_stack = np.tile(x_goal, (T, 1))  # Stack target state T times

# Linearization
theta = x_bar[2, 0]
v = u_bar[0, 0]
delta = u_bar[1, 0]

# Jacobians
A = np.array([
    [0, 0, -v * np.sin(theta)],
    [0, 0,  v * np.cos(theta)],
    [0, 0,  0]
])

B = np.array([
    [np.cos(theta), 0],
    [np.sin(theta), 0],
    [0, v / l]
])

c = np.array([
    [v * np.cos(theta)],
    [v * np.sin(theta)],
    [v / l * np.tan(delta)]
])

# Discretize
Ad = np.eye(3) + dt * A
Bd = dt * B
cd = dt * c

# Construct F, G, H
F = np.zeros((3 * T, 2 * T))
G = np.zeros((3 * T, 3))
H = np.zeros((3 * T, 1))

for t in range(T):
    row = slice(3*t, 3*(t+1))
    for j in range(t+1):
        col = slice(2*j, 2*(j+1))
        Ad_k = np.linalg.matrix_power(Ad, t - j)
        F[row, col] += Ad_k @ Bd
    G[row, :] = np.linalg.matrix_power(Ad, t)
    H[row, :] = sum(np.linalg.matrix_power(Ad, k) @ cd for k in range(t + 1))

# Run least squares for multiple lambda values
lambdas = [0.01, 0.1, 1, 10, 100]
trajectories = []

for lam in lambdas:
    A_ls = np.vstack([F, np.sqrt(lam) * np.eye(2 * T)])  # augmented matrix
    b_ls = np.vstack([x_goal_stack - G @ x_bar - H, np.zeros((2 * T, 1))])  # augmented target
    u_star = np.linalg.lstsq(A_ls, b_ls, rcond=None)[0]
    x_stack = F @ u_star + G @ x_bar + H
    trajectories.append((lam, x_stack, u_star))

# Plot results
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Position trajectory plot
for lam, x_stack, _ in trajectories:
    x = x_stack[0::3].flatten()
    y = x_stack[1::3].flatten()
    axes[0].plot(x, y, label=f"lambda = {lam}")
axes[0].plot(x_goal[0], x_goal[1], 'ro', label='Goal')
axes[0].set_title("Position Trajectory")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].legend()
axes[0].grid(True)

# Control magnitude plot
for lam, _, u_star in trajectories:
    u_reshaped = u_star.reshape(T, 2)
    u_norm = np.linalg.norm(u_reshaped, axis=1)
    axes[1].plot(range(T), u_norm, label=f"lambda = {lam}")
axes[1].set_title("Control Magnitude per Step")
axes[1].set_xlabel("Time step")
axes[1].set_ylabel("||u_t||")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()