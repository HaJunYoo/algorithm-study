from typing import List


def attach(x, y, M, key, board):
    # 현재 보드판 위치 기준으로 키를 위치시킨다
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]


def detach(x, y, M, key, board):
    # 위치 시킨 키를 다시 제거한다
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] -= key[i][j]


def rotate_keys(key: List, M):
    ret = [[0] * M for _ in range(M)]
    # 4번
    for r in range(M):
        for c in range(M):
            ret[c][M - 1 - r] = key[r][c]
    # ret = key[:]
    # ret = list(zip(*ret[::-1]))
    return ret


def check_fit(board, M, N):
    # lock 위치에 하나라도 비어 있다면 그것은 안 맞는 것
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1:
                return False
    return True


def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]

    # print(board)
    for i in range(N):
        for j in range(N):
            # key 기준으로 i, j을 배치 (가운데 배치)
            board[M + i][M + j] = lock[i][j]

    # print(board)
    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate_keys(rotated_key, M)
        # 겹치기 위해서는 1부터 시작해야한다
        for x in range(1, M + N):
            for y in range(1, M + N):
                attach(x, y, M, rotated_key, board)
                if (check_fit(board, M, N)):
                    return True
                detach(x, y, M, rotated_key, board)

    return False


if __name__ == '__main__':
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]  # len = m
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]  # len = n

    boolean = solution(key, lock)
    print(boolean)
