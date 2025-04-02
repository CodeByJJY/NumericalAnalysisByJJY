def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)
    return det

# 행렬 정의 (리스트로 직접 입력)
A_list = {
    'a': [[1, 2, 3], [2, 3, 4], [3, 4, 5]],
    'b': [[2.11, -0.80, 1.72], [-1.84, 3.03, 1.29], [-1.57, 5.25, 4.30]],
    'c': [[2, -1, 0], [-1, 2, -1], [0, -1, 2]],
    'd': [[4, 3, -1], [7, -2, 3], [5, -18, 13]]
}

threshold = 1e-1

# 계산 및 분류
for key, mat in A_list.items():
    det = determinant(mat)
    print(f"Matrix {key}: Determinant = {det:.6f}", end=' -> ')
    if abs(det) < 1e-10:
        print("Singular")
    elif abs(det) < threshold:
        print("Ill-conditioned")
    else:
        print("Well-conditioned")
