# 정렬된 2차원 행렬에서 target 값을 찾는 함수
def search_matrix(matrix, target):
    # 빈 행렬일 경우 : False 반환
    if not matrix:
        return False
    
    # 시작 위치 : 맨 위 오른쪽
    row, col = 0, len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:      # 값을 찾았을 때
            return True
        elif matrix[row][col] > target:     # 현재 값이 target보다 크면 : 왼쪽으로 이동
            col -= 1
        else:                               # 현재 값이 target보다 작으면 : 아래로 이동.
            row += 1
            
    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
print(search_matrix(matrix, 5))  # True : 4번만에 정답에 도달한다!


