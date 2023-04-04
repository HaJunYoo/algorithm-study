# t = int(input())
# k = int(input())
# coins = [[0, 0]]
# for _ in range(k):
#     a, b = map(int, input().split())
#     coins.append([a, b])
#
# dp = [[0 for _ in range(t + 1)] for _ in range(k + 1)]
# for i in range(k + 1):
#     dp[i][0] = 1
#
# coins.sort(key=lambda x: x[0])
#
# for i in range(1, k + 1):
#     coin, numbers = coins[i]
#     for num in range(numbers + 1):
#         for j in range(t + 1):
#             temp = j + num * coin
#             if temp == 0:
#                 continue
#             if temp <= t:
#                 dp[i][temp] += dp[i - 1][j]
#             else:
#                 break
#
# print(dp[k][t])
T = int(input()) # 지폐의 금액
K = int(input()) # 동전의 가지 수
coins = [] # 동전 정보
dp = [0] * (T+1) # dp[n] : n 금액에 대한 동전 교환 방법의 가지 수
dp[0] = 1 # 0원은 아무 동전도 사용하지 않는 경우가 하나 있으므로 1로 초기화

for _ in range(K):
    p, n = map(int, input().split())
    coins.append((p, n))

coins.sort()

# 하나의 코인에 대해서 합을 만들 수 있는 경우의 수를 계산
for coin, cnt in coins:
    for summation in range(T, 0, -1): # T원부터 1원까지 내려가며 진행
        for i in range(1, cnt+1): # 현재 동전 coin의 개수만큼 for문 진행
            if summation - coin * i >= 0: # 0원 이상인 경우
                dp[summation] += dp[summation - coin * i]
                # print(f'{summation} : {coin} & {i} : {dp}')

print(dp[T])