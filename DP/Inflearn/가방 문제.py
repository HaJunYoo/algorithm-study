n, limit = map(int, input().split())

dp = [0]*(limit+1)

for _ in range(n):
    w, v = map(int, input().split())
    for j in range(limit+1):
        if j-w > 0:
            if dp[j] < dp[j-w] + v:
                dp[j] = dp[j-w] + v
        else:
            continue

print(dp[limit])
print(dp)

# dp[j] : 가방에 j 무게를 담을 수 있을 때, 담을 수 있는 보석들의 누적 최대 가치
# j의 길이를 가진 dp 리스트를 만들어야 한다.
# w, v -> 인풋(동전, 가치)
# 점화식 : d[j] = d[j-w] + v
# j-w > 0
# if d[j] < d[j-w] + v : d[j] = d[j-w] + v