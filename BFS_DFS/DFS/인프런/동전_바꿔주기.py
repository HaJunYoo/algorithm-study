t = int(input())
n = int(input())
coins = []
for _ in range(n):
    a, b = map(int, input().split())
    coins.append([a, b])

dp = [0]*10001

coins.sort(key=lambda x: x[0], reverse=True)


def dfs(depth, sum, cnt):
    if sum > 0:
        dp[sum] += 1

    if sum == t:
        return
    if depth == n:
        return

    coin, num = coins[depth]
    for i in range(num + 1):
        if sum + (i * coin) > t:
            return
        else:
            dfs(depth + 1, sum + (i * coin), cnt+1)


dfs(0, 0, 0)
# print(dp)
print(dp[t])
# print(dp[15])
