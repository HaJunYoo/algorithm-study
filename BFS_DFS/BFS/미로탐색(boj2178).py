from collections import deque

n, m = map(int, input().split())
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

board = []
for _ in range(n):
    board.append(list(map(int, input())))

def bfs(x, y):
    # 덱을 생성
    queue = deque()
    # 덱에 현재 좌표을 대입
    queue.append((x,y))
    # 큐에 원소가 있을 경우
    while queue :
        # pop left
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue

            if board[nx][ny] == 0 :
                continue

            if  board[nx][ny] == 1 :
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))


bfs(0, 0)

# 0, 0 부터 n-1, m-1 의 위치로 가야함
print(board[n-1][m-1])