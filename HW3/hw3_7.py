import numpy as np

def gaussElimin(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # Forward elimination
    for k in range(n):
        # Pivoting
        max_row = np.argmax(np.abs(A[k:, k])) + k
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]
        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    # Back substitution
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x

# 테스트용 코드
def test_gaussElimin(n=200, seed=42):
    np.random.seed(seed)  # 재현성을 위해 시드 고정
    A = np.random.rand(n, n)
    b = np.sum(A, axis=1)  # 각 행의 합 -> x = [1, 1, ..., 1]이 해가 되게 함
    x = gaussElimin(A.copy(), b.copy())
    
    # 결과 비교
    expected = np.ones(n)
    error = np.linalg.norm(x - expected)
    print(f"오차 = {error:.6e}")
    if error < 1e-6:
        print("정답과 거의 일치합니다.")
    else:
        print("오차가 큽니다. 수치 안정성 확인 필요.")

# 실행
test_gaussElimin(n=200)
