from collections import deque

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def valid_coord(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

# 상하좌우
dxs1 = (-1, 1, 0, 0)
dys1 = (0, 0, -1, 1)

# 대각선
dxs2 = (-1, 1, -1, 1)
dys2 = (-1, 1, 1, -1)

queue = deque()

def bfs(x, y):
    queue.append((x, y))
    arr[x][y] = 0

    while queue:
        temp = queue.popleft()
        for dx, dy in zip(dxs1, dys1):
            nx = temp[0] + dx
            ny = temp[1] + dy
            if valid_coord(nx, ny) and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))

        for dx, dy in zip(dxs2, dys2):
            nx = temp[0] + dx
            ny = temp[1] + dy
            if valid_coord(nx, ny) and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))

res = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bfs(i, j)
            res += 1

print(res)