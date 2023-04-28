"""
3
1 2 5
15
"""
if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [1000]*(m+1)
    dp[0] = 0

    for i in range(n):
        for j in range(coins[i], m+1):
            dp[j] = dp[j-coins[i]] + 1

    print(dp[m])