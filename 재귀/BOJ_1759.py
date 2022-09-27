l, c = map(int, input().split())

words = list(map(str, input().split()))
# ord(str) => number
# chr(int) => char
words_ord = [ord(elem) for elem in words]
words_ord.sort()

# print(words_ord)
visited = [False] * c
numbers = list()

condition = ['a', 'e', 'i', 'o', 'u']


def decode():

    cnt1, cnt2 = 0, 0
    # 자음 모음 개수를 체크함
    for num in numbers:
        temp = chr(num)
        if temp in condition:
            cnt1 += 1
        else :
            cnt2 += 1
    # 자음 모음 개수를 충족할 경우에만 출력
    if (cnt1 >= 1) and (cnt2 >= 2) :
        for elem in numbers:
            print(chr(elem), end="")
        print()

# temp = [99, 105, 116, 119]
# print(any([(chr(num) in condition) for num in temp]))

def code(cnt, index):
    if cnt == l:
        decode()
        # print(numbers)
        return

    for i in range(index, c):

        if not visited[i]:
            numbers.append(words_ord[i])
            code(cnt + 1, i + 1)
            numbers.pop()

        else:
            continue


code(0, 0)
