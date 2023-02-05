n = int(input())
arr = list(map(int, input().split()))

dp = [0]*(n+1)
arr.insert(0, 0)
dp[1] = 1

res = 0

for i in range(2, n+1):
    max_num = 0
    for j in range(i-1, 0, -1):
        if arr[i] > arr[j] and dp[j] > max_num:
            max_num = dp[j]
    # print(max)
    dp[i] = max_num + 1

    # dp[2] 가 0
    if dp[i] > res:
        res = dp[i]

# print(max(dp))
print(res)
