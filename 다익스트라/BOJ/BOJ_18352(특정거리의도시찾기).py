import heapq


INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist: continue
        
        # now에 연결된 노드들 = 노드, 노드 간 거리
        for node in graph[now]:
            # 연결 노드 방문 비용
            cost = dist + node[1]
            # 현재까지 연결 노드를 방문했던 거리보다 갱신(새로 방문)하는 것이 낮을 때
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

dijkstra(x)

answer = []
for i in range(1, n+1):
    if distance[i] == k: answer.append(i)

if len(answer) == 0: print(-1)
else:
  for i in answer: print(i, end='\n')