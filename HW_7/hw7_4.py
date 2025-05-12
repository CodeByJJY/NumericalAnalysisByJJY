import numpy as np
import matplotlib.pyplot as plt

# Constants for T(r)
q = 50
a = 0.005
k = 0.16
h = 20
T_inf = 280

# Objective function
def T(r):
    if r <= a:
        return 1e6  # invalid
    return (q / (2 * np.pi)) * (np.log(r / a) / k + 1 / (h * r)) + T_inf

# Brent's Method (simplified and pure)
def brent(f, a, b, tol=1e-5, max_iter=100):
    gr = (3 - np.sqrt(5)) / 2  # golden ratio factor

    x = w = v = a + gr * (b - a)
    fx = fw = fv = f(x)
    d = e = b - a

    for _ in range(max_iter):
        m = 0.5 * (a + b)
        tol1 = tol * abs(x) + 1e-10
        tol2 = 2 * tol1

        # Check convergence
        if abs(x - m) <= tol2 - 0.5 * (b - a):
            return x, f(x)

        # Parabolic fit condition
        r = q = p = 0
        if x != w and x != v and w != v:
            # Inverse quadratic interpolation
            r = (x - w) * (fx - fv)
            q = (x - v) * (fx - fw)
            p = (x - v) * q - (x - w) * r
            q = 2 * (q - r)
            if q != 0:
                p /= q
            u = x + p
        else:
            u = None  # fallback to golden

        # Accept interpolation step?
        accept_interp = (
            u is not None and
            a + tol1 <= u <= b - tol1 and
            abs(u - x) < e / 2
        )

        if accept_interp:
            d = abs(u - x)
        else:
            # Golden-section step
            if x < m:
                u = x + gr * (b - x)
                e = b - x
            else:
                u = x - gr * (x - a)
                e = x - a
            d = abs(u - x)

        fu = f(u)

        # Update a, b, x, w, v
        if fu <= fx:
            if u < x:
                b = x
            else:
                a = x
            v, fv = w, fw
            w, fw = x, fx
            x, fx = u, fu
        else:
            if u < x:
                a = u
            else:
                b = u
            if fu <= fw or w == x:
                v, fv = w, fw
                w, fw = u, fu
            elif fu <= fv or v == x or v == w:
                v, fv = u, fu

    raise RuntimeError("Brent's method did not converge.")

# Run Brent's method
r_min, T_min = brent(T, a + 1e-6, 0.05)
print(f"Brent's Method (manual):")
print(f"Optimal r = {r_min:.6f} m")
print(f"Minimum T = {T_min:.4f} K")

# Plot T(r)
r_vals = np.linspace(0.00501, 0.05, 300)
T_vals = [T(r) for r in r_vals]
plt.plot(r_vals, T_vals, label="T(r)")
plt.axvline(r_min, color='r', linestyle='--', label=f"Optimal r ? {r_min:.4f}")
plt.xlabel("r (m)")
plt.ylabel("T (K)")
plt.title("Brent's Method (manual) for Minimizing T(r)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
