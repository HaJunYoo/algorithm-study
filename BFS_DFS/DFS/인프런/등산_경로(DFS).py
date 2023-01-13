n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]

dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)

cnt = 0


def valid_coord(x, y):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False
    else:
        return True


def dfs(x, y):
    global cnt

    if (x, y) == (n - 1, n - 1):
        cnt += 1
        return

    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy
        if valid_coord(new_x, new_y) and not visited[new_x][new_y]:
            if a[new_x][new_y] > a[x][y]:
                visited[new_x][new_y] = True
                dfs(new_x, new_y)
                visited[new_x][new_y] = False


visited[0][0] = True
dfs(0, 0)
print(cnt)