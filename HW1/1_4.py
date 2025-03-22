# Euclid Algorithm
# (a, b �� �ִ�����) = (b, a%b �� �ִ�����)

def gcd(a, b):
    # b�� 0�� �� ������ �ݺ�
    while b != 0:
        a, b = b, a % b  # a�� b��, b�� a�� b�� ���� �������� ����
    return a  # b�� 0�� �Ǹ� a�� �ִ�����

# ��� �ؼ�
# gcd(48, 16) -> gcd(18, 48 % 18) -> gcd(18, 12)
# gcd(18, 12) -> gcd(12, 6)
# gcd(12, 6) -> gcd(6, 0)

print(gcd(48, 18))  # 6
