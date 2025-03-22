# 리스트 lst에서 target 값을 찾는 순차 탐색 함수
def sequential_search(lst, target):
    for i, val in enumerate(lst):       # enumerate을 사용하여 인덱스(i), 값(val)을 동시에 반복
        if val == target:               # 값이 target과 같으면 인덱스 반환
            return i
    return -1                           # 끝까지 못 찾으면 -1 반환

# 출력 해설
# 리스트 [4, 2, 9, 7]에서 9(target)의 인덱스는 2
print(sequential_search([4, 2, 9, 7], 9))  # 2

