from itertools import combinations
from collections import deque

n, m = map(int, input().split())

graph = list(list(map(int, input().split())) for _ in range(n))

# print(graph)


def distance_calculate(r1, c1, r2, c2):
    distance = abs(r1 - r2) + abs(c1 - c2)
    return distance


def distance_initialize():
    dis = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if graph[x][y] == 1:
                dis[x][y] = 127000000
    return dis

def distance_summation(array):

    temp = 0
    for x in range(n):
        for y in range(n):
            if array[x][y] > 0:
                temp += array[x][y]

    return temp


chickens = list()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickens.append((i, j))

# print(chickens)

res = 127000000
for comb in combinations(chickens, m):
    ck_queue = deque(comb)
    # print(ck_queue)
    dis = distance_initialize()
    while ck_queue:
        r2, c2 = ck_queue.popleft()
        for r1 in range(n):
            for c1 in range(n):
                if graph[r1][c1] == 1:
                    temp_dis = distance_calculate(r1, c1, r2, c2)
                    dis[r1][c1] = min(dis[r1][c1], temp_dis)

    cnt = distance_summation(dis)
    res = min(res, cnt)

print(res)
