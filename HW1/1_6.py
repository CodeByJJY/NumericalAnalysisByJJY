# ���� ����
# - ����Ʈ�� ������ ��� ������ ���̰� 1�� ����Ʈ�� ���� ����,
# - �� ����Ʈ�� ���ĵ� ���·� ���ĳ����鼭 ��ü ������ �ϼ��ϴ� �˰���.

# �˰��� �帧 ���
# 1. ����(Divide) : ����Ʈ�� ������ ��� ������.
# 2. ����(Conquer) : �� �κ��� ��������� �����Ѵ�.
# 3. ����(Merge) : ���ĵ� �� �κ� ����Ʈ�� ���ļ� ���ĵ� �ϳ��� ����Ʈ�� �����.

def merge_sort(lst):
    # ����Ʈ�� ���̰� 1 ���� : �̹� ���ĵ� ���� -> �״�� ��ȯ (����� ���� ����)
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    result = []
    i = j = 0

    # �� ����Ʈ�� �����ϸ鼭 ����
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # ���� ���ҵ� �߰�
    result += left[i:]
    result += right[j:]

    return result

print(merge_sort([4, 2, 9, 7, 1]))  # [1, 2, 4, 7, 9]
