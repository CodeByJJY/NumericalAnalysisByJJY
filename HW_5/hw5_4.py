import numpy as np

# gravity constant
g = 9.81

# f(x) [v, theta, t] -> R^3
def f(vec):
    v, theta, t = vec
    return np.array([
        v * np.cos(theta) * t - 300,
        v * np.sin(theta) * t - 0.5 * g * t**2 - 61,
        -g * t + v * np.sin(theta) + v * np.cos(theta)
    ])

# Jacobian
def J(vec):
    v, theta, t = vec
    return np.array([
        [np.cos(theta) * t, -v * np.sin(theta) * t, v * np.cos(theta)],
        [np.sin(theta) * t,  v * np.cos(theta) * t, v * np.sin(theta) - g * t],
        [np.sin(theta) + np.cos(theta), v * (np.cos(theta) - np.sin(theta)), -g]
    ])

# Newton-Raphson for nonlinear system
def newton_system(f, J, x0, tol=1e-10, max_iter=20):
    x = np.array(x0, dtype=float)
    for i in range(max_iter):
        fx = f(x)
        Jx = J(x)
        dx = np.linalg.solve(Jx, -fx)
        x += dx
        print(f"Iter {i+1}: x = {x}, |f| = {np.linalg.norm(fx):.3e}")
        if np.linalg.norm(fx) < tol:
            break
    return x

# initial guess[v, theta, t]
x0 = [100, np.radians(45), 3]  # v = 100 m/s, ceta = 45, t = 3(s)
sol = newton_system(f, J, x0)

v, theta_rad, t = sol
theta_deg = np.degrees(theta_rad)

print(f"\nFinal roots:")
print(f"v = {v:.4f} m/s")
print(f"ceta = {theta_deg:.4f} degrees")
print(f"t = {t:.4f} seconds")
