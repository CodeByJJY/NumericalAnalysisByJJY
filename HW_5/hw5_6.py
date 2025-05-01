import numpy as np

def my_newton(f, df, x0, tol):
    R = [x0]              # 추정값 저장 리스트
    E = [abs(f(x0))]      # 오차 저장 리스트

    while E[-1] > tol:
        x_new = R[-1] - f(R[-1]) / df(R[-1])  # Newton-Raphson 식
        R.append(x_new)
        E.append(abs(f(x_new)))

    return R, E

# Test 1
f = lambda x: x**2 - 2
df = lambda x: 2*x
R, E = my_newton(f, df, 1, 1e-5)
print("R =", R)
print("E =", E)

# Test 2
f = lambda x: np.sin(x) - np.cos(x)
df = lambda x: np.cos(x) + np.sin(x)
R, E = my_newton(f, df, 1, 1e-5)
print("R =", R)
print("E =", E)