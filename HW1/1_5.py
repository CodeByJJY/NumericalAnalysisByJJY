# ����Ʈ lst���� target ���� ã�� ���� Ž�� �Լ�
def sequential_search(lst, target):
    for i, val in enumerate(lst):       # enumerate�� ����Ͽ� �ε���(i), ��(val)�� ���ÿ� �ݺ�
        if val == target:               # ���� target�� ������ �ε��� ��ȯ
            return i
    return -1                           # ������ �� ã���� -1 ��ȯ

# ��� �ؼ�
# ����Ʈ [4, 2, 9, 7]���� 9(target)�� �ε����� 2
print(sequential_search([4, 2, 9, 7], 9))  # 2

