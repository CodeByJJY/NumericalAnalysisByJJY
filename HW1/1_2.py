def findmax(lst):
    max_val = lst[0]                # list�� ù��° ���� �ִ밪���� �ʱ�ȭ
    max_idx = 0                     # �ִ밪�� index�� 0���� �ʱ�ȭ
    for i in range(1, len(lst)):    
        if lst[i] > max_val:        # ���� ���� �ִ밪���� ũ��: �ִ밪 ���� & �ִ밪�� index ����
            max_val = lst[i]
            max_idx = i
    return max_idx, max_val         # �ִ밪�� index, �ִ밪 ��ȯ

print(findmax([3, 1, 7, 5, 9, 2]))  # (4, 9)



