def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def check_palindrome_status(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # s_left = s[left]
            # s_right = s[right]
            # 한 글자 제거해서 회문이 될 수 있는가?
            if is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1):
                return 1  # 유사회문
            else:
                return 2  # 일반 문자열
        left += 1
        right -= 1

    return 0  # 회문

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(check_palindrome_status(input().strip().lower()))
