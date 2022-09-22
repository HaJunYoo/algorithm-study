n, m, k = map(int, input().split())

numbers = list()

for _ in range(n):
    numbers.append(list(map(int, input().split())))

check = [[False]*m for _ in range(n)]

# print(numbers)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

ans = -2147483647

def in_range(x, y):
    if 0 <= x < n and 0 <= y < m :
        return True
    else :
        return False

def go(cnt, sum):
    # k개를 골랐다면 sum과 기존 최대값을 비교해보자
    if cnt == k :
        global ans
        if ans < sum :
            ans = sum
        return

    # nm을 탐색해보자
    for x in range(n):
        for y in range(m):
            if check[x][y] :
                continue
            # 인접한 칸을 방문했을 경우 False
            ok = True

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                # 만약 4방향 중에 방문한 곳이 있다면 인접한 칸이기 때문에 방문하면 안된다
                if in_range(nx, ny):
                    if check[nx][ny]:
                        ok = False

            if ok :
                check[x][y] = True
                go(cnt+1, sum + numbers[x][y])
                check[x][y] = False

go(0, 0)
print(ans)


