import sys
sys.setrecursionlimit(10**6)

from collections import deque

n = int(input())
arr = []
for _ in range(n):
    temp = input()
    arr.append([int(num) for num in temp])

dxs, dys = (-1, 1, 0, 0), (0, 0, -1, 1)

def valid_coord(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

queue = deque()

def BFS(x, y):
    global cnt
    if arr[x][y] == 1:
        cnt = 1
        arr[x][y] = 0
        queue.append((x, y))

        while queue:
            nx, ny = queue.popleft()
            for dx, dy in zip(dxs, dys):
                new_x = nx + dx
                new_y = ny + dy
                if valid_coord(new_x, new_y) and arr[new_x][new_y] == 1:
                    cnt += 1
                    arr[new_x][new_y] = 0
                    queue.append((new_x, new_y))

cnt_arr = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 0
            BFS(i, j)
            cnt_arr.append(cnt)

print(len(cnt_arr))
cnt_arr.sort()
for elem in cnt_arr:
    print(elem)

