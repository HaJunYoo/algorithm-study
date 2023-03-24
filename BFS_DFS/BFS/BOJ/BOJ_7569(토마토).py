'''
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
'''
from collections import deque
import sys
input = sys.stdin.readline


m, n, h = map(int, input().split())

graph = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, input().split())))
    graph.append(tmp)
# print(graph)
queue = deque()
# print(queue)

dxs = (-1, 1, 0, 0, 0, 0)
dys = (0, 0, -1, 1, 0, 0)
dzs = (0, 0, 0, 0, -1, 1)

# print(graph[0][2][4])
def valid_coord(z, x, y):
    if 0 <= z < h and 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


# 여긴 틀린 것 없음
def bfs():
    while queue:
        z, x, y = queue.popleft()
        for dx, dy, dz in zip(dxs, dys, dzs):
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if valid_coord(nz, nx, ny) and graph[nz][nx][ny] == 0:
                queue.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1


for z in range(h):
    for x in range(n):
        for y in range(m):
            e = graph[z][x][y]
            if e == 1:
                queue.append((z, x, y))

bfs()
# print(visit)

flag = 0
res = -1
for z in range(h):
    for x in range(n):
        for y in range(m):
            t = graph[z][x][y]
            if t == 0:
                flag = 1
                break
            res = max(t, res)
        if flag == 1:
            break
    if flag == 1:
        break


if flag == 1:
    print(-1)
elif res == -1:
    print(0)
else:
    print(res-1)



