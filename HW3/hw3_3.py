from fractions import Fraction

def gauss_elimination_fraction(A, B):
    n = len(A)
    # Deep copy to avoid modifying input
    A = [[Fraction(A[i][j]) for j in range(n)] for i in range(n)]
    B = [[Fraction(B[i][j]) for j in range(len(B[0]))] for i in range(n)]

    # Forward elimination
    for i in range(n):
        # Pivoting if needed (simple row swap)
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    B[i], B[k] = B[k], B[i]
                    break
        
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            for k in range(len(B[0])):
                B[j][k] -= factor * B[i][k]

    # Back substitution
    X = [[Fraction(0) for _ in range(len(B[0]))] for _ in range(n)]
    for i in reversed(range(n)):
        for j in range(len(B[0])):
            total = sum(A[i][k] * X[k][j] for k in range(i + 1, n))
            X[i][j] = (B[i][j] - total) / A[i][i]
    
    return X

# A, B 정의 (리스트로)
A = [
    [2, 0, -1, 0],
    [0, 1, 2, 0],
    [-1, 2, 0, 1],
    [0, 0, 1, -2]
]

B = [
    [1, 0],
    [0, 0],
    [0, 1],
    [0, 0]
]

# 계산
X = gauss_elimination_fraction(A, B)

# 결과 출력
print("Solution X (as fractions):")
for row in X:
    print([str(val) for val in row])
