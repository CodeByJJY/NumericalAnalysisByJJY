import numpy as np

# f(x) = x^4 + 2x^3 - 7x^2 + 3
def f(x):
    return x**4 + 2*x**3 - 7*x**2 + 3

# f'(x)
def df(x):
    return 4*x**3 + 6*x**2 - 14*x

# Newton-Raphson
def newton_raphson(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-12:
            print("Derivative is too small.")
            break
        dx = -fx / dfx
        x += dx
        print(f"Iter {i+1}: x = {x:.10f}, f(x) = {f(x):.3e}")
        if abs(fx) < tol:
            break
    return x

# initial guess
root = newton_raphson(f, df, x0=0.8)
print(f"\nfinal root: {root}")
