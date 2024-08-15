def solution(keymap, targets):
    char_min = {}

    for key in keymap:
        for index, char in enumerate(key, 1):
            if char not in char_min or index < char_min[char]:
                char_min[char] = index

    result = []

    # print(char_min)
    for target in targets:
        total = 0
        flag = False
        for c in target:
            if c not in char_min:
                flag = True
                break
            total += char_min[c]

        if flag:
            result.append(-1)
        else:
            result.append(total)

    return result
