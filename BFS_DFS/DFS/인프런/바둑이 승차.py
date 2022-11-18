c, n = map(int, input().split())

dogs = [0] + [int(input()) for _ in range(n)]

dp = [0]*(n+1)

weight = list()

def dfs(num):
    if num == n+1 :
        temp = 0
        # memoization의 flag 원소값이 1일 경우 해당 인덱스-1 에 해당하는 강아지의 무게를 더한다.
        for idx, flag in enumerate(dp) :
            if flag == 1 :
                temp += dogs[idx]


        # temp가 c를 넘지 않지 않을 경우
        if temp <= c :
            weight.append(temp)

    else :
        # 태운다
        dp[num] = 1
        dfs(num+1)

        # 안태운다
        dp[num] = 0
        dfs(num+1)


max_val = 0

dfs(1)
print(max(weight))

# dogs = [0] + [0 for _ in range(4)]
# print(dogs)
