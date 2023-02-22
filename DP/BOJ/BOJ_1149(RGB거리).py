n = int(input())
arr = list()
arr.append([0, 0, 0])
for i in range(n):
    arr.append(list(map(int, input().split())))
# print(arr)
dp = [[0]*3 for _ in range(n+1)]
# dp[0] = (0, arr[0][0])
# for i in range(1, n):
#     temp = dp[i-1][1]
#     dp[i] = (i,  temp + arr[i][0])
# print(dp)

price = 0
for i in range(1, n+1):
    # print(arr[i])
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[n]))