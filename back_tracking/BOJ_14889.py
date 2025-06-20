from itertools import combinations


def calculate():
    s1 = 0
    s2 = 0
    team_2 = list(num_list - set(team_1))

    for a in range(n // 2):
        for b in range(n // 2):
            if a == b:
                continue
            s1 += numbers[team_1[a]][team_1[b]]
            s2 += numbers[team_2[a]][team_2[b]]

    res = abs(s1 - s2)

    return res

# def calculate():
#     s1 = 0
#     s2 = 0
#     team_2 = list(num_list - set(team_1))
#
#     for elem in combinations(team_1, 2):
#         i = elem[0]
#         j = elem[1]
#         temp = numbers[i][j] + numbers[j][i]
#         s1 += temp
#
#     for elem in combinations(team_2, 2):
#         i = elem[0]
#         j = elem[1]
#         temp = numbers[i][j] + numbers[j][i]
#         s2 += temp
#
#     res = abs(s1 - s2)
#
#     return res


def choice(cnt, index):
    global ans

    if index == n:
        return

    if cnt == n // 2:
        temp = calculate()
        ans = min(temp, ans)
        return

    team_1.append(index)
    choice(cnt + 1, index + 1)
    team_1.pop()

    choice(cnt, index + 1)


n = int(input())

numbers = []
for _ in range(n):
    numbers.append(list(map(int, input().split())))

team_1 = []
visited = [False] * n

num_list = set([i for i in range(n)])

ans = 10000000000

choice(0, 0)

print(ans)
