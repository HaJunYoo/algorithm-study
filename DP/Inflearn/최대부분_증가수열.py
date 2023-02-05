n = int(input())
arr = list(map(int, input().split()))
# top-down 방식으로
# dp 리스트는 n번째 인덱스가 마지막항일 때의 최대 길이
dp = [0]*(n+1)
arr.insert(0, 0)
dp[1] = 1
res = 0

# 2번째부터 탐색
for i in range(2, n+1):
    max=0
    # i-1부터 0까지 -1만큼씩 이동
    for j in range(i-1, 0, -1):
        # j번째 인덱스가 마지막 수보다 작거나 해당 인덱스 dp가 기존최대값보다 크다면 갱신
        # 아래 코드가 점화식 규칙
        if arr[j] < arr[i] and dp[j] > max:
            max = dp[j]
    # i번째 최장 길이는 갱신된 max보다 1만큼 긴 길이
    dp[i] = max+1
    # 갱신된 dp 값이 기존 최대값보다 크다면 갱신
    if dp[i] > res:
        res=dp[i]

print(res)

'''
▣ 입력예제 1
8
5 3 7 8 6 2 9 4
▣ 출력예제 1
4
'''
