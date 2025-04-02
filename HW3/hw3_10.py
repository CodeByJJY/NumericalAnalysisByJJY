from fractions import Fraction

# 삼대각 LU 분해 함수 (Doolittle 방식)
def LUdecomp3(c, d, e):
    n = len(d)
    for k in range(1, n):
        lam = c[k-1] / d[k-1]
        d[k] = d[k] - lam * e[k-1]
        c[k-1] = lam
    return c, d, e

# 전방 및 후방 대입 함수
def LUsolve3(c, d, e, b):
    n = len(d)

    # Forward substitution: Ly = b
    for k in range(1, n):
        b[k] -= c[k-1] * b[k-1]

    # Backward substitution: Ux = y
    b[n-1] = b[n-1] / d[n-1]
    for k in range(n-2, -1, -1):
        b[k] = (b[k] - e[k] * b[k+1]) / d[k]

    return b

# 문제 3.10 설정 (n = 10)
n = 10
c = [Fraction(-1)] * (n - 1)  # 하삼각 부분
d = [Fraction(4)] * n         # 주대각
e = [Fraction(-1)] * (n - 1)  # 상삼각 부분
b = [Fraction(9)] + [Fraction(5)] * (n - 1)  # 우변 벡터

# LU 분해 및 풀이
c, d, e = LUdecomp3(c, d, e)
x = LUsolve3(c, d, e, b)

# 결과 출력
print("=== 문제 3.10 해 (분수 기반) ===")
for i, xi in enumerate(x):
    print(f"x[{i+1}] = {xi}  (approx. {float(xi):.6f})")
