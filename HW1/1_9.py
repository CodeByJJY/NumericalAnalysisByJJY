# ������ ���� �� �ִ� �ѷ��� ����ϴ� �Լ�
def trap(height):
    left, right = 0, len(height) - 1    # ���� ������ ����
    left_max = right_max = water = 0    # ��/�� �ִ� ���̿� �� ���差 �ʱ�ȭ
    
    while left < right:
        # �� ���� ���� �������� ���� ���̸� ���.
        if height[left] < height[right]:
            left_max = max(left_max, height[left])  # ���ʿ��� ���� ���� �� ����
            water += left_max - height[left]        # ���� ��ġ���� ���� �� �ִ� �� ���
            left += 1                               # ���� ������ ���������� 1ĭ �̵�.
        else:
            right_max = max(right_max, height[right])   # �����ʿ��� ���� ���� �� ����
            water += right_max - height[right]          # ���� ��ġ���� ���� �� �ִ� �� ���
            right -= 1                                  # ������ ������ �������� 1ĭ �̵�.
            
    return water    # �� ���� ���� �� ��ȯ

print(trap([0,1,0,2,1,0,3,2,1,2,1]))  # 5



