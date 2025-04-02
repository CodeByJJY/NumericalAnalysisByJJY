from fractions import Fraction

# L과 U 행렬 (Fraction 사용)
L = [
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(3, 2), Fraction(1), Fraction(0)],
    [Fraction(1, 2), Fraction(11, 13), Fraction(1)]
]

U = [
    [Fraction(2), Fraction(-3), Fraction(-1)],
    [Fraction(0), Fraction(13, 2), Fraction(-7, 2)],
    [Fraction(0), Fraction(0), Fraction(32, 13)]
]

# b 벡터
b = [Fraction(1), Fraction(-1), Fraction(2)]

# Step 1: Ly = b => forward substitution
y = [Fraction(0) for _ in range(3)]
y[0] = b[0]
y[1] = b[1] - L[1][0] * y[0]
y[2] = b[2] - L[2][0] * y[0] - L[2][1] * y[1]
print("Solution y =", y)

# Step 2: Ux = y => back substitution
x = [Fraction(0) for _ in range(3)]
x[2] = y[2] / U[2][2]
x[1] = (y[1] - U[1][2] * x[2]) / U[1][1]
x[0] = (y[0] - U[0][1] * x[1] - U[0][2] * x[2]) / U[0][0]

print("Solution x =", x)
