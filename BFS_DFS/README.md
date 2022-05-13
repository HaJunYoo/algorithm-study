## DFS

스택이나 재귀를 활용

재귀를 활용 자체가 스택을 활용하는 것

DFS 는 완전탐색이기 때문에 모든 노드를 깊이 우선적으로 살펴본다

0→ 1 → 2→ 3 → 4 → 5 → 6→ 7 →  8 → 9 → 10 → 11 → 12

최대한 계속 깊게 파고 내려간 후 올라온다 

해당 방법을 재귀적으로 반복한다

```python
### 인접 행렬로 구현

# 13 * 13 크기의 행렬 생성
adj = [[0] * 13 for _ in range(13)]

# 간선 별 1 연결 부여 
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1

for row in adj : 
	print(row)

# 현재 방문한 노드 now를 인자로 받음
def dfs(now):
	for nxt in range(13):
		# 다음으로 가는 노드가 있을 때
		if adj[now][nxt]: 
			# 다음 노드의 dfs 호출 
			dfs(nxt)

def(0)
```

## BFS


- 큐를 사용해서 구현
- 깊이를 한단계씩 내려가면서 좌 → 우 를 훑는 방식으로 진행
- pop을 한 노드에 연결되어 있는 노드들을 큐에 Enque 해준다

- 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12

큐 작동 방식

- 0 (0 pop)
- 1 2 (1 pop)
- 2 3 4 (2 pop)
- 34 56 ( 3 pop)
- 4 56 78 ( 4 pop)
- 56 78 9 (5 pop) → 5는 연결된 노드가 없음
- 6 78 9 ( 6 pop)
- 78 9 10 11 12
    
    

```python
from collections import deque

adj = [[0]*13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1

def bfs():
	dq = deque()
	dq.append(0)
	# 큐에 원소가 존재하는 동안 
	while dq :
		
		now = dq.popleft()
		# pop한 노드에 연결되어 있는 노드를 왼쪽부터 큐에 추가
		for nxt in range(13):
			if adj[now][nxt]:
				dq.append(nxt)

bfs()
```
