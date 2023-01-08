a = []
for _ in range(7):
    a.append(list(map(int, input().split())))

visited = [[False] * 7 for _ in range(7)]

dxs, dys = (1, -1, 0, 0), (0, 0, -1, 1)

res = 127000000
cnt = 0

def valid_ck(x, y):
    if 0 <= x < 7 and 0 <= y < 7:
        return True
    else:
        return False

def dfs(x, y, dis):
    global cnt, res

    if x == 6 and y == 6:
        if dis < res:
            res = dis
        cnt += 1
        return

    for dx, dy in zip(dxs, dys):
        n_x = x + dx
        n_y = y + dy
        if valid_ck(n_x, n_y) and a[n_x][n_y] == 0:
            if not visited[n_x][n_y]:
                visited[n_x][n_y] = True

                dfs(n_x, n_y, dis+1)

                visited[n_x][n_y] = False


visited[0][0] = True
dfs(0,0,0)
print(cnt) # 총 경우의 수
print(res) # 최단 거리