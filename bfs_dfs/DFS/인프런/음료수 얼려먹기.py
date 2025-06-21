n, m = map(int,input().split())

graph = [list(map(int, input())) for _ in range(n)]

# print(graph)

# 방향 벡터
dx = (1, -1, 0, 0)
dy = (0, 0 , 1, -1)

def dfs(x, y):

    # 0 ~ n-1, m-1
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if graph[x][y] == 0:

        graph[x][y] = 1

        for k in range(4):
            nx = x+ dx[k]
            ny = y+ dy[k]
            dfs(nx, ny)

        return True

    return False

cnt = 0
# 행
for i in range(n) :
    # 열
    for j in range(m) :
        if dfs(i, j) == True :
            cnt +=1

print(cnt)


