def fact(n):
    if n == 0 or n == 1:        # n = 0 �Ǵ� 1 : ���丮���� 1 (���� ����)
        return 1
    return n * fact(n - 1)      # �׷��� ������ : ��������� n * (n - 1)! ���

print(fact(5))  # 120 = 5! = 5 * 4 * 3 * 2 * 1




