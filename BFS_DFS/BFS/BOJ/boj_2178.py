from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

board = [input() for _ in range(N)]


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x <= M


def bfs():
    # check 배열은 격자판과 똑같이 만들어준다
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    dq = deque()
    # 현재 좌표 y, x 와 간 거리 d
    dq.append((0, 0, 1))
    while dq:  # dq 내 원소가 있을 때
        y, x, d = dq.popleft()

        if y == N - 1 and x == M - 1:
            return d

        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nd))


# 만약 목적지에 도착할 수 없는 경우라면 -1을 리턴해라
# return -1

print(bfs())