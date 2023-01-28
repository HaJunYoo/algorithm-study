n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

# 오른쪽이나 아래쪽만 이동 가능
dxs, dys = (0, 1), (1, 0)

# 각 좌표까지의 최소 에너지
dp = [[0] * n for _ in range(n)]

dp[0][0] = a[0][0]
for i in range(n):
    dp[i][0] = dp[i-1][0] + a[i][0]
    dp[0][i] = dp[0][i-1] + a[0][i]

for j in range(1, n):
    for k in range(1, n):
        dp[j][k] = min(dp[j][k-1], dp[j-1][k]) + a[j][k]

print(dp[n-1][n-1])

