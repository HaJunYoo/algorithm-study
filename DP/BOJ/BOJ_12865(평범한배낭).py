n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n)]
# dp[0] = 1

stuff = []
for _ in range(n):
    # 물건의 무게, 가치
    a, b = map(int, input().split())
    stuff.append((a, b))

stuff.sort(key=lambda x: (x[0], x[1]))

# w, v = stuff[0]
# for j in range(1, k + 1):
#     if j >= w:
#         dp[0][j] = max(dp[0][j], dp[0][j - w] + v)
#     else:
#         continue

for idx in range(0, n):
    # print(idx)
    w = stuff[idx][0]
    v = stuff[idx][1]
    for j in range(1, k + 1):
        # dp[idx][j] = dp[idx][j-w] + v -> 이전 물건의 이번 무게 추가 전 최대 가치 + 이번 물건 추가 시
        if j >= w:
            dp[idx][j] = max(dp[idx - 1][j], dp[idx - 1][j - w] + v)
        else:
            dp[idx][j] = dp[idx - 1][j]

# print(dp)
print(dp[n - 1][k])
'''
4 11
5 12
3 8
6 14
4 8
'''