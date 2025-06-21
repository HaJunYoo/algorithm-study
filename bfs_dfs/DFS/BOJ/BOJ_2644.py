n = int(input())

x, y = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 촌은 양방향 연결이기 때문에 각각 노드에 할당
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

    # 그래프에 연결된 노드 탐색
    for i in graph[x]:
        # 연결된 노드 중 방문하지 않는 노드가 있다면
        if not visited[i]:
            # path.append(i)
            # 방문
            dfs(i, cnt + 1)
            # path.pop()


dfs(x, 0)

if ans == 0:
    print(-1)
else:
    print(ans)
