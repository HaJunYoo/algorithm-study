n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n)]
# dp[0] = 1

stuff = []
for _ in range(n):
    a, b = map(int, input().split())
    stuff.append((a, b))

stuff.sort(key=lambda x:(x[0], x[1]))

for idx, s in enumerate(stuff):
    w, v = s
    for j in range(1, k+1):
        # j - w > 0
        # dp[idx][j] = dp[idx][j-w] + v
        if j >= w:
            dp[idx][j] = max(dp[idx-1][j], dp[idx-1][j-w] + v)
        else:
            dp[idx][j] = dp[idx-1][j]

# print(dp)
print(dp[n-1][k])

