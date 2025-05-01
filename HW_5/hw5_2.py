import numpy as np

# constants
u = 2510         # m/s
M0 = 2.8e6       # kg
mdot = 13.3e3    # kg/s
g = 9.81         # m/s^2
v_target = 335   # m/s

# f(t)
def f(t):
    return u * np.log(M0 / (M0 - mdot * t)) - g * t - v_target

# f'(t)
def df(t):
    return (u * mdot) / (M0 - mdot * t) - g

# Newton-Raphson method
def newton(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        dx = -fx / dfx
        x += dx
        print(f"Iter {i+1}: t = {x:.10f}, f(t) = {fx:.3e}")
        if abs(fx) < tol:
            break
    return x

# initial guess
t0 = 5
t_solution = newton(f, df, t0)

print(f"\nroot: {t_solution:.6f}(s)")
