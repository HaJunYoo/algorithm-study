n = int(input())
b = [tuple(map(int, input().split())) for i in range(n)]

dp = [0] * (n + 1)
b.insert(0, (0, 0, 0))
# print(b)
dp[1] = b[1][1]

b_num = [1] * n
b_num.insert(0, 0)

b_dict = {}

for i in range(2, n + 1):
    # 최대 높이
    max_height = 0
    # 개수
    temp = 0
    # 가장 긴 인덱스
    res = 0
    for j in range(i - 1, 0, -1):
        # 넓이, 높이, 무게
        if b[i][0] < b[j][0] and b[i][2] < b[j][2] and dp[j] > max_height:
            max_height = dp[j]
            temp += 1
            res = j

    dp[i] = max_height + b[i][1]
    b_num[i] += temp
    # 쌓은 벽돌
    b_dict[i] = res

print(max(b_num))
# print(b_dict)
idx = b_num.index(max(b_num))

flag = True
print(idx)
while flag:
    idx = b_dict.get(idx)
    print(idx)
    if b_dict.get(idx) is None:
        break

