n = int(input())
dp = [0] * (n + 1)

dp[1] = 1
dp[2] = 2


def dfs(k):
    if k == 1 or k == 2:
        return k

    if dp[k] > 0:
        return dp[k]

    else:
        dp[k] = dfs(k - 2) + dfs(k - 1)
        return dp[k]

print(dfs(n))