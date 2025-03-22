# ���� Ž�� �Լ� : ���ĵ� ����Ʈ lst���� target�� �ε����� ã�´�.
def binary_search(lst, target):
    left, right = 0, len(lst) - 1   # Ž�� ������ ���۰� �� ����.
    while left <= right:
        mid = (left + right) // 2   # �߰� �ε��� ���
        if lst[mid] == target:      # �߰� ���� ��ǥ���̸� : �ε��� ��ȯ
            return mid
        elif lst[mid] < target:     # �߰� ������ ũ�� : ������ �ݸ� Ž��
            left = mid + 1
        else:                       # �߰� ������ ������ : ���� �ݸ� Ž��
            right = mid - 1
    return -1                       # ã�� ������ ��� : -1 ��ȯ

sorted_list = [1, 3, 5, 7, 9]
print(binary_search(sorted_list, 5))  # 2


