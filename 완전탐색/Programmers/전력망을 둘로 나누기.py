from collections import deque

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

def bfs(node, arr):
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(node)
    visited[node] = True
    list = []

    while queue:
        curr = queue.popleft()
        # print(curr)
        list.append(curr)
        # 노드 기준 연결된 노드들
        for next in arr[curr]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

    return len(list)

def make_graph(temp, n):
    arr = [list() for _ in range(n+1)]
    for elem in temp:
        a = elem[0]
        b = elem[1]
        arr[a].append(b)
        arr[b].append(a)

    return arr


res = 100

arr = make_graph(wires, n)
print(arr)

for a, b in wires:
    # 간선 제거
    # 노드 인덱스 기준으로 remove
    arr[a].remove(b)
    arr[b].remove(a)
    # 간선 기준으로 왼쪽, 오른쪽
    val_a = bfs(a, arr)
    val_b = bfs(b, arr)

    res = min(abs(val_a-val_b), res)

    # 제거한 간선 다시 추가
    arr[a].append(b)
    arr[b].append(a)
    # print(v_list)


print(res)
