from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# print(graph)
dxs, dys = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(x, y):
    size = 0
    graph[x][y] = 0
    queue = deque([(x, y)])
    size += 1

    while queue:
        temp_x, temp_y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx = temp_x + dx
            ny = temp_y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                size += 1

    return size


cnt = 0
res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tmp = bfs(i, j)
            res = max(tmp, res)
            cnt += 1

if cnt == 0:
    res = 0

print(cnt)
print(res)
