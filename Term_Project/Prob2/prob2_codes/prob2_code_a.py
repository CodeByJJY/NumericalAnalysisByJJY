import numpy as np

# Parameters
T = 10           # Time horizon
dt = 1.0         # Discrete time step
l = 2.0          # Wheel base (vehicle constant)

# Nominal state and input
x_bar = np.array([[0], [-2], [0]])     # Initial state: [x, y, theta]
u_bar = np.array([[10], [0]])          # Nominal input: [v, delta]

# Goal state
x_goal = np.array([[100], [2], [0]])

# Linearization around (x?, u?)
theta = x_bar[2, 0]
v = u_bar[0, 0]
delta = u_bar[1, 0]

# Jacobians A, B and constant term c
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

# Euler-forward time discretization
Ad = np.eye(3) + dt * A    # Discrete A matrix
Bd = dt * B                # Discrete B matrix
cd = dt * c                # Discrete constant term

# Construct F, G, H matrices
F = np.zeros((3 * T, 2 * T))    # For stacking all u_0 to u_{T-1}
G = np.zeros((3 * T, 3))        # For initial state influence
H = np.zeros((3 * T, 1))        # For offset cd influence

Ad_power = np.eye(3)
for t in range(T):
    row = slice(3*t, 3*(t+1))
    
    # Fill F: sum of Ad^k * Bd * u_{t-k}
    for j in range(t+1):
        col = slice(2*j, 2*(j+1))
        Ad_k = np.linalg.matrix_power(Ad, t - j)
        F[row, col] += Ad_k @ Bd

    # Fill G: Ad^t * x0
    G[row, :] = np.linalg.matrix_power(Ad, t)

    # Fill H: sum of Ad^k * cd
    H[row, :] = sum(np.linalg.matrix_power(Ad, k) @ cd for k in range(t + 1))

# Example usage: compute x_T from u and x0
x0 = x_bar
u_seq = np.zeros((2 * T, 1))  # zero input as placeholder
xT = F @ u_seq + G @ x0 + H   # full stacked trajectory

# Print shapes to verify
print("F:", F.shape)
print("G:", G.shape)
print("H:", H.shape)
print("xT:", xT.shape)
