import numpy as np

# f(x)
def f(xy):
    x, y = xy
    return np.array([
        np.sin(x) + 3 * np.cos(x) - 2,
        np.cos(x) - np.sin(y) + 0.2
    ])

# Jacobian
def J(xy):
    x, y = xy
    return np.array([
        [np.cos(x) - 3 * np.sin(x), 0],
        [-np.sin(x), -np.cos(y)]
    ])

# Newton-Raphson for multivariable system
def newton_2d(f, J, x0, tol=1e-10, max_iter=10):
    x = np.array(x0, dtype=float)
    for i in range(max_iter):
        fx = f(x)
        Jx = J(x)
        delta = np.linalg.solve(Jx, -fx)
        x = x + delta
        print(f"Iter {i+1}: x = {x}, |f| = {np.linalg.norm(fx):.3e}")
        if np.linalg.norm(fx) < tol:
            break
    return x

# initial guess (1, 1)
x0 = [1, 1]
sol = newton_2d(f, J, x0)

print(f"\nroot: x = {sol[0]:.6f}, y = {sol[1]:.6f}")
