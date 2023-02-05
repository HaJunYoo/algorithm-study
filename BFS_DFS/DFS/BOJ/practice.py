def coord_valid(x, y):
    if x < 0 or x > h - 1 or y < 0 or y > w - 1:
        return False
    else:
        return True

# 상하좌우
dxs1, dys1 = (-1, 1, 0, 0), (0, 0, -1, 1)
# 대각선
dxs2, dys2 = (1, -1, 1, -1), (1, -1, -1, 1)


def dfs(x, y):
    if not coord_valid(x, y):
        return False

    if arr[x][y] == 0:
        return False

    if not visited[x][y] and arr[x][y] == 1:
        visited[x][y] = True

        for dx, dy in zip(dxs1, dys1):
            nx = x + dx
            ny = y + dy
            dfs(nx, ny)
        for dx, dy in zip(dxs2, dys2):
            nx = x + dx
            ny = y + dy
            dfs(nx, ny)
        return True

    return False


w, h = map(int, input().split())

print(w, h)
arr = []
for _ in range(h):
    temp = list(map(int, input().split()))
    arr.append(temp)
print(arr)

visited = [[False] * w for _ in range(h)]
print(visited)

result = 0
for i in range(h):
    for j in range(w):

        if dfs(i, j):
            result += 1

print(result)

# #
# print(visited[0][4])
'''
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
'''