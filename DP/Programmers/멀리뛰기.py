def solution(n):
    memo = [0] * (n + 1)

    if n == 1:
        return 1
    elif n == 2:
        return 2

    memo[1] = 1
    memo[2] = 2

    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    answer = memo[-1] % 1234567
    return answer