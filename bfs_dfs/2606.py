from collections import deque

n = int(input())
m = int(input())

graph = {}
for i in range(1, n+1):
    graph[i] = set()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = set()

def bfs(start):

    queue = deque([start])
    visited.add(start)

    while queue:
        v = queue.popleft()

        for w in graph[v]:
            if w not in visited:
                queue.append(w)
                visited.add(w)


bfs(1)

if len(visited) >= 1:
    print(len(visited)-1)
else:
    print(0)