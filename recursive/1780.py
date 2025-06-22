import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

# 결과 카운트: -1, 0, 1 순서
count = [0, 0, 0]

def check(x, y, size):
    first = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first:
                return False
    return True

def divide(x, y, size):
    if check(x, y, size):
        count[paper[x][y] + 1] += 1  # -1 → 0번, 0 → 1번, 1 → 2번 인덱스
        return

    new_size = size // 3
    for dx in range(3):
        for dy in range(3):
            nx = x + dx * new_size
            ny = y + dy * new_size
            divide(nx, ny, new_size)

divide(0, 0, n)

for c in count:
    print(c)
