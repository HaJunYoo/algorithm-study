from typing import List
from collections import deque


def bfs(grid, i, j):
    len_x = len(grid)
    len_y = len(grid[0])

    dxs, dys = (0, 0, 1, -1), (1, -1, 0, 0)

    queue = deque([(i, j)])
    grid[i][j] = "0"

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            n_x, n_y = cur_x + dx, cur_y + dy
            if 0 <= n_x < len_x and 0 <= n_y < len_y:
                if grid[n_x][n_y] == "1":
                    queue.append((n_x, n_y))
                    grid[n_x][n_y] = "0"


# 1 <= m, n <= 300
# BFS로 접근 필요
def numIslands(grid: List[List[str]]) -> int:
    num = 0

    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                num += 1
                bfs(grid, i, j)

    return num


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print(numIslands(grid))
