from collections import deque


def is_valid(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


n = int(input())

dxs, dys = (-1, 1, 0, 0), (0, 0, -1, 1)

ans = 0

graph = [
    list(map(int, input())) for _ in range(n)
]

visited = [
    [False] * n for _ in range(n)
]


def bfs(x, y):
    queue = deque([])
    queue.append([x, y])
    visited[x][y] = True
    cnt = 1

    # print(queue)
    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, n):
                if not visited[new_x][new_y] and graph[new_x][new_y] == 1:
                    visited[new_x][new_y] = True
                    queue.append([new_x, new_y])
                    cnt += 1

    return cnt


house_counts = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            house_count = bfs(i, j)
            house_counts.append(house_count)

house_counts.sort()
print(len(house_counts))  # 총 단지 수
for count in house_counts:
    print(count)
