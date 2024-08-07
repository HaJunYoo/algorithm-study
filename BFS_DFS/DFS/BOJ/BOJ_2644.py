n = int(input())

x, y = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

# print(graph)

ans = 0

path = []


def dfs(x, cnt):
    global ans

    visited[x] = True
    # print(path)
    if x == y:
        ans = cnt
        # print('sss', path)
        return

    if cnt == n + 1:
        # print(path)
        return

    for i in graph[x]:
        if not visited[i]:
            # path.append(i)
            dfs(i, cnt + 1)
            # path.pop()


dfs(x, 0)

if ans == 0:
    print(-1)
else:
    print(ans)
