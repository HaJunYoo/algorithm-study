arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))

dxs, dys = (-1, 1, 0, 0), (0, 0, -1, 1)

strings = []


def dfs(x, y, cnt, string):
    if cnt == 6:
        strings.append(string)
        return

    string += str(arr[x][y])

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, cnt + 1, string)


for i in range(5):
    for j in range(5):
        dfs(i, j, 0, '')

strings_s = set(strings)
# print(strings_s)
strings_s = list(strings_s)
print(len(strings_s))