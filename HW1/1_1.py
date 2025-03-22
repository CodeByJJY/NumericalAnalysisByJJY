# Python Code 1
def sum_n_1(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s

# Python Code 2
def sum_n_2(n):
    return n*(n + 1) // 2

print(sum_n_1(100))
print(sum_n_2(100))



