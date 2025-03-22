# ���ĵ� 2���� ��Ŀ��� target ���� ã�� �Լ�
def search_matrix(matrix, target):
    # �� ����� ��� : False ��ȯ
    if not matrix:
        return False
    
    # ���� ��ġ : �� �� ������
    row, col = 0, len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:      # ���� ã���� ��
            return True
        elif matrix[row][col] > target:     # ���� ���� target���� ũ�� : �������� �̵�
            col -= 1
        else:                               # ���� ���� target���� ������ : �Ʒ��� �̵�.
            row += 1
            
    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
print(search_matrix(matrix, 5))  # True : 4������ ���信 �����Ѵ�!


