# 병합 정렬
# - 리스트를 반으로 계속 나눠서 길이가 1인 리스트로 만든 다음,
# - 두 리스트를 정렬된 상태로 합쳐나가면서 전체 정렬을 완성하는 알고리즘.

# 알고리즘 흐름 요약
# 1. 분할(Divide) : 리스트를 반으로 계속 나눈다.
# 2. 정복(Conquer) : 각 부분을 재귀적으로 정렬한다.
# 3. 병합(Merge) : 정렬된 두 부분 리스트를 합쳐서 정렬된 하나의 리스트로 만든다.

def merge_sort(lst):
    # 리스트의 길이가 1 이하 : 이미 정렬된 상태 -> 그대로 반환 (재귀의 종료 조건)
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    result = []
    i = j = 0

    # 두 리스트를 병합하면서 정렬
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소들 추가
    result += left[i:]
    result += right[j:]

    return result

print(merge_sort([4, 2, 9, 7, 1]))  # [1, 2, 4, 7, 9]
