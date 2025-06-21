dxs, dys = (-1, 1, 0, 0), (0, 0, -1, 1)

ans = 0


def is_valid(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def dfs(x, y, n, graph, visited):
    visited[x][y] = True
    count = 1

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if is_valid(new_x, new_y, n) and graph[new_x][new_y] == 1 and not visited[new_x][new_y]:
            count += dfs(new_x, new_y, n, graph, visited)

    return count


n = int(input())

graph = [
    list(map(int, input())) for _ in range(n)
]

visited = [
    [False] * n for _ in range(n)
]

house_counts = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            house_count = dfs(i, j, n, graph, visited)
            house_counts.append(house_count)


house_counts.sort()
print(len(house_counts))  # 총 단지 수
for count in house_counts:
    print(count)
