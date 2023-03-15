from collections import deque

n, m, v = map(int, input().split())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

for li in arr:
    li.sort()

# print(arr)


dfs_list = []
dfs_visited = [False]*(n+1)

### dfs
def dfs(vertex):
    dfs_visited[vertex] = True
    dfs_list.append(vertex)

    print(vertex, end=' ')

    for node in arr[vertex]:
        if not dfs_visited[node]:
            dfs(node)

dfs(v)
print()
### bfs

bfs_visited = [False]*(n+1)

def bfs(cur):
    queue = deque([cur])
    bfs_visited[cur] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for node in arr[vertex]:
            if not bfs_visited[node]:
                queue.append(node)
                bfs_visited[node] = True

bfs(v)

'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''