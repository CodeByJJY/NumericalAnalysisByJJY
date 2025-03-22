def fact(n):
    if n == 0 or n == 1:        # n = 0 또는 1 : 팩토리얼은 1 (종료 조건)
        return 1
    return n * fact(n - 1)      # 그렇지 않으면 : 재귀적으로 n * (n - 1)! 계산

print(fact(5))  # 120 = 5! = 5 * 4 * 3 * 2 * 1




