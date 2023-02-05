import sys
from collections import deque
sys.setrecursionlimit(2500)

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# print(arr)

max_h = max(max(arr))
min_h = min(min(arr))
# print(f'{max_h}-{min_h}')

dxs = (-1, 1, 0, 0)
dys = (0, 0, -1, 1)

def bfs(x, y, height):
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        temp = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx = temp[0] + dx
            ny = temp[1] + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > height and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


result = 0
# min_h = max(min_h, 0)
for h in range(0, max_h+1):
    res = 0
    visited = [[False] * n for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and not visited[i][j]:
                bfs(i, j, h)
                res += 1
    result = max(result, res)

print(result)

