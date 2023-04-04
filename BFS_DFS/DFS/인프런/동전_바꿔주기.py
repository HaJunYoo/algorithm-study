t = int(input())
k = int(input())
coins = [[0, 0]]
for _ in range(k):
    a, b = map(int, input().split())
    coins.append([a, b])

dp = [[0 for _ in range(t + 1)] for _ in range(k + 1)]
for i in range(k+1):
    dp[i][0]=1

coins.sort(key=lambda x: x[0])

for i in range(1, k+1):
    coin, numbers = coins[i]
    for num in range(numbers + 1):
        for j in range(t + 1):
            temp = j + num * coin
            if temp == 0:
                continue
            if temp <= t:
                dp[i][temp] += dp[i - 1][j]
            else:
                break

# dfs(0, 0, 0)
# print(dp)
# print(dp[k][t])
# print(dp[15])
print(dp[k][t])
