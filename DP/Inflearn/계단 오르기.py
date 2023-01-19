n = int(input())

dp = [0]*(n+1)
dp[1] = 1
dp[2] = 2

def dfs(len):
    if len in (1, 2):
        return len

    if dp[len] > 0:
        return dp[len]

    else:
        dp[len] = dfs(len-1) + dfs(len-2)
        return dp[len]


print(dfs(n))
