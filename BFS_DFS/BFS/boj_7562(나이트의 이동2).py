from collections import deque

# 나이트가 이동할 수 있는 방향 벡터
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def bfs():

    queue = deque()
    queue.append((a,b))

    # 큐 -> FIFO
    while queue :

        # 큐 가장 첫번째 인덱스 pop -> 기준점으로 함
        x, y = queue.popleft()

        # 목적지에 도착했다면
        if x == c and y == d:
            print(visited[x][y])
            return

        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            # 0 ~ n-1
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 방문 안했을 경우만 이동 횟수 증가시키고 큐에 추가 -> 이동횟수 최소화
            if not visited[nx][ny] :

                # 이동한 좌표에 이동횟수 1 증가해서 기록
                visited[nx][ny] = visited[x][y] + 1
                # 이동한 좌표 큐 끝에 추가
                queue.append((nx, ny))


test_num = int(input())

for _ in range(test_num):
    n = int(input())
    visited = [[0] * n for _ in range(n)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    bfs()

