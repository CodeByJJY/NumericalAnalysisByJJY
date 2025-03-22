# 회문인지 확인하는 함수 (대소문자, 공백, 특수문자 무시)
def is_palindrome(s):
    # filter(함수, 반복가능한 객체) : 리스트, 문자열 등에서 "조건에 맞는 값만 걸러내는" 함수
    # 함수 : 각 요소에 적용될 조건 함수
    # 반복가능한 객체 : 리스트, 튜플, 문자열 등
    s = ''.join(filter(str.isalnum, s)).lower() # str.isalnum : 문자열이 '영문자, 숫자'로만 이루어져 있는지 확인해주는 문자열 메서드.
       
    # 문자열을 뒤집은 것과 원래 문자열이 같은지 비교
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False





