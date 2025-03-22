# 빗물이 고일 수 있는 총량을 계산하는 함수
def trap(height):
    left, right = 0, len(height) - 1    # 양쪽 포인터 설정
    left_max = right_max = water = 0    # 왼/오 최대 높이와 물 저장량 초기화
    
    while left < right:
        # 더 낮은 쪽을 기준으로 물의 높이를 계산.
        if height[left] < height[right]:
            left_max = max(left_max, height[left])  # 왼쪽에서 가장 높은 벽 갱신
            water += left_max - height[left]        # 현재 위치에서 고일 수 있는 물 계산
            left += 1                               # 왼쪽 포인터 오른쪽으로 1칸 이동.
        else:
            right_max = max(right_max, height[right])   # 오른쪽에서 가장 높은 벽 갱신
            water += right_max - height[right]          # 현재 위치에서 고일 수 있는 물 계산
            right -= 1                                  # 오른쪽 포인터 왼쪽으로 1칸 이동.
            
    return water    # 총 고인 물의 양 반환

print(trap([0,1,0,2,1,0,3,2,1,2,1]))  # 5



