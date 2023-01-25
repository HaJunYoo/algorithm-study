n = int(input())
a = list(map(int, input().split()))
dp = [0]*(n+1)
a.insert(0, 0)

# 1개의 원소일때는 1개가 가장 길다
dp[1] = 1

for i in range(2, n+1):
    max_num = 0
    for j in range(i-1, 0, -1):
        if a[j] < a[i] and dp[j] > max_num:
            max_num = dp[j]
        dp[i] = max_num + 1

# print(dp)
print(max(dp))