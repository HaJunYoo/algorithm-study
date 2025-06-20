def fibonacci_mod(n):
    MOD = 1000000
    PISANO = 1500000

    n %= PISANO  # 피사노 주기로 인덱스 축소

    dp = [0] * (n + 2)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    return dp[n]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_mod(n))
