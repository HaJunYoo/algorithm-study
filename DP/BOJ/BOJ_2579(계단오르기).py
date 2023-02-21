n = int(input())

arr = [int(input()) for _ in range(n)]
arr.insert(0, 0)

dp = [0] * (n+1)

if n < 3:
    print(sum(arr))
else:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    for i in range(3, n+1): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
    print(dp[-1])