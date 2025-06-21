from collections import deque

n, m = map(int, input().split())

mat = [[0] * n for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    mat[a - 1][b - 1] = 1


def dfs(cur):
    global res
    array = deque() # 각 분기마다 deque 초기화

    if cur == n-1:
        res += 1
        for idx, num in enumerate(visited):
            if num:
                print(idx+1, end=' ')
        print()
        return

    for i in range(n):
        if not visited[i] and mat[cur][i] == 1:
            array.append(i)

    while len(array) != 0:
        node = array.popleft()
        visited[node] = True
        dfs(node)
        visited[node] = False


visited[0] = True
res = 0

dfs(0)
print(res)

