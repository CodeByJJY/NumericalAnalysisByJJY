# ȸ������ Ȯ���ϴ� �Լ� (��ҹ���, ����, Ư������ ����)
def is_palindrome(s):
    # filter(�Լ�, �ݺ������� ��ü) : ����Ʈ, ���ڿ� ��� "���ǿ� �´� ���� �ɷ�����" �Լ�
    # �Լ� : �� ��ҿ� ����� ���� �Լ�
    # �ݺ������� ��ü : ����Ʈ, Ʃ��, ���ڿ� ��
    s = ''.join(filter(str.isalnum, s)).lower() # str.isalnum : ���ڿ��� '������, ����'�θ� �̷���� �ִ��� Ȯ�����ִ� ���ڿ� �޼���.
       
    # ���ڿ��� ������ �Ͱ� ���� ���ڿ��� ������ ��
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False





