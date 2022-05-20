### 길찾기 문제

보통 🔼🔽◀️▶️ 4개의 방향이 많다

방향값을 미리 코드에 짜두고 for 문으로 순회하는 기법을 꼭 익혀두자

### DFS

![스크린샷 2022-05-19 오후 9.38.10.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/95d3d245-989e-4df9-9596-d3c6876e211b/스크린샷_2022-05-19_오후_9.38.10.png)

```python
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

chk = [[False]*100 for _ in range(100)]
# False로 채워진 100*100 -> 아직은 모두 미방문
N = int(input())

def is_valid_coord(y,x):
	return 0 <= y < N and 0 <= x < N

def dfs(start_y, start_x):
    	# start_y, start_x 에서 ny, nx로 변경이 되서 dfs 재귀 형식으로 호출되어 진행

	chk[y][x] = True
	for k in range(4):
		ny = y + dy[k]
		nx = x + dx[k]
		if is_valid_coord(y,x) and not chk[ny][nx]:
			dfs(ny, nx)

```

### BFS

```python
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

chk = [[False]*100 for _ in range(100)]
# False로 채워진 100*100 -> 아직은 모두 미방문
N = int(input())

def is_valid_coord(y,x):
	return 0 <= y < N and 0 <= x < N

def bfs(start_y, start_x):
# bfs는 큐를 사용하여 구현한다
# 큐는 FirstinFirstout, 반면 스택은 LIFO 이다 
	q = deque() # deque 선언 
	q.append((start_y, start_x)) # queue에 start y, start x
	while len(q) > 0 : # 큐가 존재할 때 
		y, x = q.popleft() # 큐의 왼쪽을 pop한다 -> 남아 있는 것들 중 제일 번호가 작은 것
		chk[y][x] = True # 뽑아낸 번호를 방문을 하였다 로 변경 -> True 
	
		for k in range(4): # 다음 방문의 후보(총 4군데, 상하좌우)
			ny = y + dy[k]
			nx = x + dx[k]
			if is_valid_coord(ny, nx) and not chk[ny][nx]: 
													# 방향 별 유효성 검증 및 방문여부 확인
				q.append((ny, nx)) 
```

- 방문 체크 필요
- 각 칸이 노드
- 상하 좌우 4방향의 간선

먼저 dx, dy를 통해 방향을 4개로 잡는다 

범위 이동을 할 때 범위 유효 체크(isValidCoord), 방문 여부 체크( not chk[nx][ny])를 병행해야 한다

→ 두 개의 체크가 통과하였을 때 재귀 형식으로 dfs 혹은 bfs를 불러온다

dy, dx 배열을 사용 안하고도 구현은 가능하지만

- 코드가 길어지고
- 코딩 실수가 날 가능성이 농후하다

⇒ dx dy를 먼저 정의해주고 공통된 부분은 묶어서 구현을 해주는 쪽이 좋다

![스크린샷 2022-05-19 오후 10.30.46.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9ce0a81b-791e-4bca-92ea-7bf75732082e/스크린샷_2022-05-19_오후_10.30.46.png)