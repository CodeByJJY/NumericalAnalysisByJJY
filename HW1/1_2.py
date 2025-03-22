def findmax(lst):
    max_val = lst[0]                # list의 첫번째 값을 최대값으로 초기화
    max_idx = 0                     # 최대값의 index를 0으로 초기화
    for i in range(1, len(lst)):    
        if lst[i] > max_val:        # 현재 값이 최대값보다 크면: 최대값 갱신 & 최대값의 index 갱신
            max_val = lst[i]
            max_idx = i
    return max_idx, max_val         # 최대값의 index, 최대값 반환

print(findmax([3, 1, 7, 5, 9, 2]))  # (4, 9)



