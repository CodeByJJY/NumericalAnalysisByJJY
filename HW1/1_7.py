# 이진 탐색 함수 : 정렬된 리스트 lst에서 target의 인덱스를 찾는다.
def binary_search(lst, target):
    left, right = 0, len(lst) - 1   # 탐색 범위의 시작과 끝 설정.
    while left <= right:
        mid = (left + right) // 2   # 중간 인덱스 계산
        if lst[mid] == target:      # 중간 값이 목표값이면 : 인덱스 반환
            return mid
        elif lst[mid] < target:     # 중간 값보다 크면 : 오른쪽 반만 탐색
            left = mid + 1
        else:                       # 중간 값보다 작으면 : 왼쪽 반만 탐색
            right = mid - 1
    return -1                       # 찾지 못했을 경우 : -1 반환

sorted_list = [1, 3, 5, 7, 9]
print(binary_search(sorted_list, 5))  # 2


