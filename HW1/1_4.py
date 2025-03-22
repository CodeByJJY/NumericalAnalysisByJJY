# Euclid Algorithm
# (a, b 의 최대공약수) = (b, a%b 의 최대공약수)

def gcd(a, b):
    # b가 0이 될 때까지 반복
    while b != 0:
        a, b = b, a % b  # a를 b로, b를 a를 b로 나눈 나머지로 갱신
    return a  # b가 0이 되면 a가 최대공약수

# 출력 해설
# gcd(48, 16) -> gcd(18, 48 % 18) -> gcd(18, 12)
# gcd(18, 12) -> gcd(12, 6)
# gcd(12, 6) -> gcd(6, 0)

print(gcd(48, 18))  # 6
