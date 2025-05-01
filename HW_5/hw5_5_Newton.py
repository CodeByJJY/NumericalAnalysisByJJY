# f(w)
def f(w):
    return w**4 + 24*w**3 + 4500*w**2 + 18000*w + 2.25e6

def df(w):
    return 4*w**3 + 72*w**2 + 9000*w + 18000

# Newton-Raphson iteration
def newton_raphson(f, df, w0, tol=1e-10, max_iter=100):
    w = w0
    for i in range(max_iter):
        fw = f(w)
        dfw = df(w)
        if abs(dfw) < 1e-12:
            print(f"Derivative near to zero , Iter {i}")
            break
        w_next = w - fw / dfw
        print(f"Iter {i+1}: w = {w_next:.10f}, f(w) = {f(w_next):.3e}")
        if abs(f(w_next)) < tol:
            return w_next
        w = w_next
    return w

# initial guess
w0 = -10 + 60j
root = newton_raphson(f, df, w0)

print(f"\nroot: w = {root:.6f}")
