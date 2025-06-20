def fibonacci(n):

    if n == 1 or n == 2:
        return 1

    dp = [0] * n

    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        if dp[i] != 0:
            continue

        dp[i] = dp[i - 1] + dp[i - 2]

    ans = dp[-1]
    # print(dp)
    return ans

if __name__ == '__main__':

    n = int(input())
    print(fibonacci(n))