n = int(input())

dp = [0]*(n+2)

dp[1] = 1
dp[2] = 2

for i in range(3, n+2):
    if dp[i] > 0:
        continue
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[-1])


# print(dp)
