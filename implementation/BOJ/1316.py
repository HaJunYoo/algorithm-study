n = int(input())
cnt = 0

for _ in range(n):
    string = input()
    before = {}
    prev = ''
    is_group_word = True

    for char in string:
        if char != prev:  # 연속되지 않는 새로운 문자 등장 시
            if char in before:
                # 이미 등장했던 문자가 다시 등장 → 그룹 단어 아님
                is_group_word = False
                break
            before[char] = 1
        prev = char

    if is_group_word:
        cnt += 1

print(cnt)