n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

# 각 좌표까지의 최소 에너지
dp = [[0] * n for _ in range(n)]

def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]

    if x==0 and y==0:
        return a[0][0]

    else:
        if y==0:
            dp[x][y] = dfs(x - 1, y) + a[x][y]
        elif x==0:
            dp[x][y] = dfs(x, y-1) + a[x][y]
        else:
            dp[x][y] = min(dfs(x - 1, y), dfs(x, y - 1)) + a[x][y]
        return dp[x][y]


res = dfs(n-1,n-1)

print(res)