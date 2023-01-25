n = int(input())
b = [tuple(map(int, input().split())) for i in range(n)]
dp = [0] * (n + 1)
b.insert(0, (0, 0, 0))
# print(b)
dp[1] = b[1][1]

b_num = [1] * n
b_num.insert(0, 0)

b_list = {}

for i in range(2, n + 1):

    max_height = 0
    # 개수
    temp = 0

    res = 0
    for j in range(i - 1, 0, -1):
        # print(f'{j}번째')
        # 넓이, 높이, 무게
        if b[i][0] < b[j][0] and b[i][2] < b[j][2] and dp[j] > max_height:
            max_height = dp[j]
            temp += 1
            res = j

    # print(max_height)
    dp[i] = max_height + b[i][1]
    b_num[i] += temp
    # 쌓은 벽돌
    b_list[i] = res

# print(dp)

# print(max(dp))
print(max(b_num))
# print(b_num.index(max(b_num)))
# print(b_list)

idx = b_num.index(max(b_num))
flag = True
print(idx)
while flag:
    idx = b_list.get(idx)
    print(idx)
    if b_list.get(idx) is None:
        break


# for
