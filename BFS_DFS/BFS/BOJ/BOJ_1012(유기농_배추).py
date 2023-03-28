from collections import deque

# y, x
def make_graph(n, m):
    graph = list()
    for _ in range(n):
        graph.append([0] * m)
    return graph


# 1인 부분을 탐색하고 0으로 바꾼 후 True를 반환, cnt를 증가
def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    graph[y][x] = 0

    while queue:
        temp = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx = temp[1] + dx
            ny = temp[0] + dy
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                queue.append((ny, nx))
                graph[ny][nx] = 0


t = int(input())
# graph = []
cnt_list = []
for _ in range(t):
    m, n, k = map(int, input().split())
    cnt = 0
    # y, x
    graph = make_graph(n, m)

    dxs, dys = (-1, 1, 0, 0), (0, 0, -1, 1)

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for y in range(n):  # y
        for x in range(m):  # x
            if graph[y][x] == 1:
                # print((y, x))
                bfs(y, x)
                cnt += 1

    cnt_list.append(cnt)

for c in cnt_list:
    print(c)

# for elem in graph:
#     print(elem)
# print(graph)
