import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
visited = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)  # 양방향

# dfs로 탐색 -> bfs로도 풀어보기
def dfs(node):
    visited[node] = True
    for neighbor in tree[node]:
        if not visited[neighbor]:
            parent[neighbor] = node
            dfs(neighbor)

dfs(1)


def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)

bfs(1)


for i in range(2, n + 1):
    print(parent[i])
